#!/usr/bin/env python3
#
# intercept serial data and diff hexdumps
#
# seems not to work on windows

import sys
from datetime import datetime
import pipes
import os
import serial
import time
import select

# config
pathcreatehexdump = '../createhexdump.py'
datadir = '/tmp'
comparetool = 'meld'
comporthw = '/dev/ttyUSB0'
comportprog = '/dev/pts/1'
secscomfinished = 10 # idle time in seconds after one
hwbaudrate = 9600

# vars
numconnects = 0
datasetname = ''
lastfilename = ''
datadump = ''
serialPortHw = None
serialPortProg = None
dataparts = ''
datadirection = 0
timelastaction = 0

# parameters?
if len(sys.argv) == 2:
   comportprog = sys.argv[1]
if len(sys.argv) == 3:
   comportprog = sys.argv[1]
   comporthw = sys.argv[2]
if len(sys.argv) == 4:
   comportprog = sys.argv[1]
   comporthw = sys.argv[2]
   hwbaudrate = sys.argv[3]
elif len(sys.argv) >4:
   print("Usage: " + sys.argv[0] + ' [comportprogrammer] [comporthw] [baudrate]')
   exit()



def openSerialPort(comport):

   try:
      print("Opening comport " + comport)
      # serialPort = serial.Serial(port = comport, baudrate=9600, bytesize=8, timeout=0.05, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000 / timeout 0.05 and 0.1 ok
      serialPort = serial.Serial(port = comport, baudrate=hwbaudrate, bytesize=8, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000

      return serialPort
   except:
      print('ERROR: Could not open port ' + comport)
      print("Usage: " + sys.argv[0] + ' [comportprogrammer] [comporthw] [baudrate]')
      exit()



def dehexify(hexstr):

   retstr = ''

   if len(hexstr) > 2:

      ascstr = bytes.fromhex(str(hexstr[2:]))

      for i in range(len(ascstr)):
   
         idec = int(ascstr[i])

         if (32 <= idec and idec < 127) or (160 <= idec):
            retstr += chr(idec)
         else:
            retstr += '.'

   return retstr



def writeHexdump():

   global datadump
   global lastfilename
   global datasetname
   global datadir


   if len(datadump) > 0:
      outfilename = datadir + '/' + datasetname + '.hexdump'
      print("Saving " + outfilename + " ...")

      f = open(outfilename, 'w')

      for line in datadump.splitlines():
         f.write(line + ' || ' + dehexify(line) + '\n')

      f.close()

      if ( len(lastfilename) > 0 ):
         # compare last 2 dumps
         print('Starting compare ' + lastfilename + ' ' + outfilename)
         os.spawnlp(os.P_NOWAIT, comparetool, comparetool, lastfilename , outfilename)
                    
      datadump = ''
      lastfilename = outfilename
      datasetname = ''



## main

# open serial ports

serialPortHw = openSerialPort(comporthw)
serialPortProg = openSerialPort(comportprog)

numconnects += 1
datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)

inputs = [serialPortHw, serialPortProg]

try:

   while True:

      # receive data
      readers, _, _ = select.select(inputs, [], [], 5)

      if ( len(datadump) > 0 and (datetime.now()-timelastaction).seconds >= secscomfinished ):
         # no more communication. save last session
         # save dump file
         writeHexdump()
         # open new session
         numconnects += 1
         datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)
         datadirection = 0

      # some data received      
      for reader in readers:
         
         timelastaction = datetime.now()

         if reader is serialPortHw:
            
            ## copy data from serial port with radio to serial port with programmer
            try:
               data_from_radio = serialPortHw.read()

               while serialPortHw.in_waiting > 0:
                  data_from_radio += serialPortHw.read()
               
               if ( len (data_from_radio) > 0 ):
                 
                  if datadirection == 1:
                     # append received data
                     dataparts = dataparts + data_from_radio.hex()
                  else:
                     # direction changed
                     datadirection = 1

                     print(dataparts)
                     dataparts = "< " + data_from_radio.hex()
                     if len(datadump) != 0:
                        datadump += '\n'
                     datadump += "< "   

                  datadump += data_from_radio.hex()
                  
                  serialPortProg.write(data_from_radio)
                  serialPortProg.flush()
               else:
                  print("No data on hw serial port.")


            except:
               # serial port gone
               e = sys.exc_info()[0]
               print( "ERROR: " + str(e) )

               print("Serial port hw gone.")
               inputs.remove(serialPortHw)
               serialPortHw.close()
               
               # save dump file
               writeHexdump()
               
               # reconnect serial port
               print("Reconnecting serial port with hw in 15s...")
               time.sleep(15)
               serialPortHw = openSerialPort(comporthw)
               inputs.append(serialPortHw)
               numconnects += 1
               datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)

         elif reader is serialPortProg:
            
            ## copy data from serial port with programming software to serial port with radio
            try:
               data_from_prog = serialPortProg.read()

               while serialPortProg.in_waiting > 0:
                  data_from_prog += serialPortProg.read()
               
               if ( len (data_from_prog) > 0 ):

                  if datadirection == 2:
                     # append received data
                     dataparts += data_from_prog.hex()
                  else:
                     # direction changed
                     datadirection = 2

                     print(dataparts)
                     dataparts = "> " + data_from_prog.hex()
                     if len(datadump) != 0:
                        datadump += '\n'
                     datadump += "> "   

                  datadump += data_from_prog.hex()
                  
                  serialPortHw.write(data_from_prog)
                  serialPortHw.flush()
              
               else:
                  print("No data on programmer serial port.")


            except:
               # serial port gone
 
               e = sys.exc_info()[0]
               print( "ERROR: " + str(e) )

               print("Serial port with programmer gone.")
               inputs.remove(serialPortProg)
               serialPortProg.close()
               
               # save dump file
               writeHexdump()
               
               # reconnect serial port
               print("Reconnecting serial port with programmer in 15s...")
               time.sleep(15)
               serialPortProg = openSerialPort(comportprog)
               inputs.append(serialPortProg)
               numconnects += 1
               datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)



finally:
   print("QRT")
   serialPortHw.close()
   serialPortProg.close()


   # save dump file
   writeHexdump()
