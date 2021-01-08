#!/usr/bin/env python3
#
# Connects anytone programming software to anytone radio via network.
# The data stream is sent via network to a script (at_intercept_radio.py) where
# the radio is connected via USB. On the radio side the datastream can be exported
# for further investigation.
#
# This script connects to a virtual com port COM26 which is connected via a virtual
# null modem cable to the virtual com port COM18 which is used by the programming software.
# This virtual ports and cable can be provided by the COM0COM tool.
#
# Linux users can use
# socat -d -d pty,raw,echo=0,b4000000 pty,raw,echo=0,b4000000
# for emulating a virtual null modem cable.

import serial
import time
import socket
import sys
import select

# config
servername = '192.168.1.2' # ip or hostname of server
serverport = 4242
comport = 'COM26' # connected to COM18 with com0com. use COM18 in CPS



# parameters?
if len(sys.argv) == 3:
   servername = sys.argv[1]
   comport = sys.argv[2]
elif len(sys.argv) == 2:
   servername = sys.argv[1]
elif len(sys.argv) >3:
   print("Usage: " + sys.argv[0] + ' servername [comport]')
   exit()



# open serial port
serialPort = None

try:
   print("Opening comport " + comport)
   serialPort = serial.Serial(port = comport, baudrate=4000000, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000
   #serialPort.setblocking(False)
except:
   print('ERR: Could not open port ' + comport)
   print("Usage: " + sys.argv[0] + ' servername [comport]')
   exit()



# make tcp connection
print("Connecting to " + servername + ":" + str(serverport) )
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((servername, serverport))
sock.setblocking(False)


# wait for data

try:

   while 1:

      readers, _, _ = select.select([sock], [], [], 0.1) # timeout 0.1s / serialPort is not supported on windows :-(

      for reader in readers:

         if reader is sock:

            ## copy data from remote radio to serial port
            data_from_network = sock.recv(1024)

            for line in data_from_network.split(b'\n'):
               if len(line) > 0:
                  print("< " + line.decode() )
                  try:
                     serialPort.write(bytes.fromhex(line.decode()))
                  except:
                     e = sys.exc_info()[0]
                     print(e)
                  
         
         #elif reader is serialPort:
      

      ## copy data from serial port to remote radio
      command_from_programmer = b''

      command_from_programmer += serialPort.read()
      while serialPort.in_waiting > 0:
         command_from_programmer += serialPort.read()

      if ( len (command_from_programmer) > 0 ):
         # send data from programming software on serial port to server with connected radio as hex encoded line
         to_network = (command_from_programmer.hex() + '\n').encode()
         print("> " + to_network[:-1].decoder() )
         try:
            sock.sendall(to_network)
         except:
            e = sys.exc_info()[0]
            print(e)


finally:
   print('QRT')
   serialPort.close()
   sock.close()
