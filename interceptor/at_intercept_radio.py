#!/usr/bin/env python3
#
# receive intercepted programming data from at-d878uv emulator via network
# and diff hexdumps


import socket
import select
import sys
from datetime import datetime
import pipes
import os
import serial
import time

# config
myservername = '0.0.0.0' # 0.0.0.0 means listen on all interfaces
mylistenport = 4242 # port name to listen on
pathcreatehexdump = '../createhexdump.py'
datadir = '/tmp'
comparetool = 'meld'
comport = '/dev/ttyACM0'

# vars
numconnects = 0
datasetname = ''
lastfilename = ''
datadump = ''
serialPort = None


# parameters?
if len(sys.argv) == 2:
   comport = sys.argv[1]
elif len(sys.argv) >2:
   print("Usage: " + sys.argv[0] + ' [comport]')
   exit()



def openSerialPort(comport):

   global numconnects
   global datasetname

   try:
      print("Opening comport " + comport)
      serialPort = serial.Serial(port = comport, baudrate=4000000, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000
      numconnects += 1
      datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)

      return serialPort
   except:
      print('ERROR: Could not open port ' + comport)
      print("Usage: " + sys.argv[0] + ' [comport]')
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

# open serial port

serialPort = openSerialPort(comport)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
sock.bind((myservername, mylistenport))

# Listen for incoming connections
sock.listen(1)
#sock.setblocking(False)



inputs = [sock, serialPort]
connection = None

try:

   print('Waiting for a connection on ' + str(mylistenport) + '...', file=sys.stderr)

   while True:


      # receive data
      readers, _, _ = select.select(inputs, [], [])
      
      for reader in readers:

         if reader is sock:

            ## incoming connection

            connection, client_address = sock.accept()
            print ('Connection from', client_address, file=sys.stderr)
            inputs.append(connection)

         
         elif reader is connection:

            ## copy data from network/programming software to serial port

            data_from_network = connection.recv(1024)
            
            if len(data_from_network) > 0:

               for line in data_from_network.split(b'\n'):

                  if len(line) > 0:
                     print( "> " + line.decode() )
                     datadump += "> " + line.decode() + '\n'

                     try:
                        serialPort.write(bytes.fromhex(line.decode()))
                     except:
                        e = sys.exc_info()[0]
                        print( "ERROR: " + str(e) )
            
            
            else:
               print("Connection closed.")
               inputs.remove(connection)
                  
         
         elif reader is serialPort:
            
            ## copy data from serial port with radio to network
            try:
               data_from_radio = serialPort.read()

               while serialPort.in_waiting > 0:
                  data_from_radio += serialPort.read()
               
               if ( len (data_from_radio) > 0 ):
                  print( "< " + data_from_radio.hex() )
                  datadump += "< " + data_from_radio.hex() + '\n'
                  
                  connection.sendall( (data_from_radio.hex() + '\n').encode() )
              
               else:
                  print("No data on serial port.")


            except:
               # serial port gone
               print("Serial port gone.")
               inputs.remove(serialPort)
               serialPort.close()
               
               # save dump file
               writeHexdump()
               
               # reconnect serial port
               print("Reconnecting serial port in 20s...")
               time.sleep(20)
               serialPort = openSerialPort(comport)
               inputs.append(serialPort)


finally:
   print("QRT")
   serialPort.close()
   sock.close()

   # save dump file
   writeHexdump()
