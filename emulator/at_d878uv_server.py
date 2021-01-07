#!/usr/bin/env python3
#
# receive intercepted programming data from at-d878uv emulator via network
# and diff hexdumps


import socket
import sys
from datetime import datetime
import pipes
import os


# config
myservername = '0.0.0.0' # 0.0.0.0 means listen on all interfaces
mylistenport = 2342 # port name to listen on
pathcreatehexdump = '../createhexdump.py'
datadir = '/tmp'
comparetool = 'meld'


# vars
numconnects = 0
datasetname = ''
lastfilename = ''



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (myservername, mylistenport)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


while True:
   # Wait for a connection
   print('Waiting for a connection...', file=sys.stderr)
   connection, client_address = sock.accept()

    
   try:
       print ('Connection from', client_address, file=sys.stderr)

       line = ''
       alldata = ''

       # Receive data
       while True:

          data = connection.recv(1)

          #print ('received "%s"' % data, file=sys.stderr)

          if data:
             
             if data != b'\n':
                line += data.decode('latin1')
                # print(line)
                
             else:
                # EOL received

                alldata += line + '\n'

                
                if ( line == '50524f4752414d' ): # "PROGRAM"
                   print("Programming session started!", file=sys.stderr)
                   numconnects += 1
                   datasetname = datetime.now().strftime("%y%m%d-%H%M%S-") + str(numconnects)

                elif ( line == '454e44' ): # "END"
                   print("Programming session ended!", file=sys.stderr)
                   #print(datasetname)
                   
                   p = pipes.Template()
                   p.append(pathcreatehexdump + ' - > $OUT', '-f')
                   # p.debug(True)
                   
                   outfilename = datadir + '/' + datasetname + '.data'
                   f = p.open(outfilename, 'w')
                   try:
                      f.write(alldata)
                   finally:
                      f.close()

                   #print(alldata)
                   
                   if ( len(lastfilename) > 0 ):
                      # compare last 2 dumps
                      print('Starting compare ' + lastfilename + ' ' + outfilename)
                      os.spawnlp(os.P_NOWAIT, comparetool, comparetool, lastfilename , outfilename)
                   
                   alldata = ''
                   lastfilename = outfilename
                   datasetname = ''

                elif ( line == '555044415445' ): # 'UPDATE'
                   print("Firmware update session started!", file=sys.stderr)
                   numconnects += 1
                   datasetname = datetime.now().strftime("%y%m%d-%H%M%S-firmware-") + str(numconnects)

                elif ( line == '18' ): # firmware update end
                   p = pipes.Template()
                   p.append(pathcreatehexdump + ' - > $OUT', '-f')
                   # p.debug(True)

                   outfilename = datadir + '/' + datasetname + '.data'
                   f = p.open(outfilename, 'w')
                   try:
                      f.write(alldata)
                   finally:
                      f.close()

                   #print(alldata)

                   if ( len(lastfilename) > 0 ):
                      # compare last 2 dumps
                      print('Starting compare ' + lastfilename + ' ' + outfilename)
                      os.spawnlp(os.P_NOWAIT, comparetool, comparetool, lastfilename , outfilename)
                   
                   alldata = ''
                   lastfilename = outfilename
                   datasetname = ''


                else:
                   pass

                   
                line = ''
             
          else:
             print ('No more data from', client_address, file=sys.stderr)
             break
            
   finally:
      # Clean up the connection
      connection.close()

