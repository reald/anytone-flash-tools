#!python3
#
# Emulate anytone 878uv radio to customer programming software. 
# Send intercepted data stream over network to server script for further investigation.
#
# This script connects to a virtual com port COM26 which is connected via a virtual
# null modem cable to the virtual com port COM18 which is used by the programming software.
# This virtual ports and cable can be provided by the COM0COM tool.


import serial
import time
import socket
import sys

# config
servername = '192.168.1.2' # ip or hostname of server
serverport = 2342
portname = 'COM26' # connected to COM18 with com0com. use COM18 in CPS





# open serial port
serialPort = None

try:
   serialPort = serial.Serial(port = portname, baudrate=4000000, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000
except:
   print('ERR: Could not open port ' + portname)
   exit()


# make tcp connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (servername, serverport)
sock.connect(server_address)



# wait for data

try:
   
   while 1:

      command = ''

      command = serialPort.read()
      while serialPort.in_waiting > 0:
         command += serialPort.read()

      # print("Command " + str(command) )
   
      # mirror command to server as hex string
      if ( len(command) > 0 ):
         sock.sendall( (command.hex() + '\n').encode() )

      # respond to command on com port
      if ( len(command) == 0 ):
         pass

      elif ( command == b'PROGRAM'):
         print("Program session requested.")
         resp = b'QX\x06'
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command == b'\x02' ):
         print("Device info requested.")
         resp = b'ID878UV\x00\x00V100\x00\x00\x06'
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command == b'R\x02\xfa\x00\x20\x10' ):
         print("Read special memory request.")
         resp = b'W\x02\xfa\x00\x20\x10\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x24\x06'
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )
         
      elif ( command[0:4] == b'R\x02\xfa\x00' and command[5] == 16 ):
         # 0x02fa00..
         print("Read local information.")
         
         resp = b'W\x02\xfa\x00' + bytes([command[4]]) + b'\x10'
         
         if ( command[4] == 0x00 ):
            resp += b'\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x01\x20\x20\x20\x20\xff'
                                           
         elif ( command[4] == 0x10 ): # Radio Type
            resp += b'\x44\x38\x37\x38\x55\x56\x00\x01\x00\xff\xff\xff\xff\xff\xff\xff'

         elif ( command[4] == 0x30 ): # Serial Number
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0x40 ): # Production Date
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0x50 ): # Manucfacture Code
            resp += b'\x31\x32\x33\x34\x35\x36\x37\x38\xff\xff\xff\xff\xff\xff\xff\xff'
         elif ( command[4] == 0x60 ): # Maintained Date
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0x70 ): # Dealer Code
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0x80 ): # Stock Date
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0x90 ): # Sell Date
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0xa0 ): # Seller
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

         elif ( command[4] == 0xb0 ): # Maintained Description
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0xc0 ): 
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0xd0 ): 
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0xe0 ): 
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
         elif ( command[4] == 0xf0 ): 
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

         else:
            resp += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

         resp = resp + bytes( [sum(resp[1:]) & 0xff] ) + b'\x06'
         #print(resp.hex())
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command[0] == ord('W') ) :
         print("write request.")
         resp = b'\x06' # just ack
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command == b'END' ):
         print("End session.")
         resp = b'\x06' # just ack
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command == b'UPDATE' ):
         # for firmware update the device has to be switched on while pressing PF3 (blue button on top) and PTT keys
         print("Start Firmware Update. Only useful if device is in update receiving mode. (Switch on while pressing PF3 (blue button on top) and PTT keys)")
         resp = b'\x06' # just ack
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command == b'\x18' ):
         print("Firmware Update Send Complete. Switch device on while pressing PF2 (top left side) and PTT keys to start installer.")
         resp = b'\x06' # just ack
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )

      elif ( command[0] == 0x01 ):
         print("Firmware data.")
         resp = b'\x06' # just ack
         serialPort.write(resp)
         sock.sendall( (resp.hex() + '\n').encode() )
      else:
         #print("> " + str(command))
         pass



finally:
   print('QRT')
   serialPort.close()
   sock.close()

