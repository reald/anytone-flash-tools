#!/usr/bin/python3 
#
# Reformat data of usb pcap

import sys
import re
import fileinput


    
    
expnextaddr = 0
blockstartaddr = 0
nummemoryblocks = 0

if len(sys.argv) > 1 :
   if sys.argv[1] != '-':
      # open file
      f = open(sys.argv[1], "r")
   else:
      # open stdin
      f = sys.stdin

else:
   # open stdin
   f = sys.stdin



# read input file or stdin   

for line in f.readlines():

   line = line.rstrip()

   #print (line)

   # parse line

   m = re.search('^(57)(........)(..)(.*)(..)(06)$', line)
   m_firmwarewrite = re.search('^(01)(........)(.*)(....)(06)$', line)

   if m is not None:

      # line with data (type W - 0x57)

      datalen = len(m.group(4))

      memoryaddr = m.group(2)
      memorylen = m.group(3)

      if int(memoryaddr, 16) != expnextaddr : #and memoryaddr != '02fa0020':
         # new memory section started
         if expnextaddr != 0:
            print( '=> Block ' + str(nummemoryblocks) + ': ' )
            print( '=> Size: ' + str(hex(blockstartaddr)) + ' .. ' + str(hex(expnextaddr-1)) + ': ' + str( expnextaddr - blockstartaddr ) + ' bytes' )
         blockstartaddr = int(memoryaddr, 16)
         nummemoryblocks += 1
         print("")

      expnextaddr = int(memoryaddr, 16) + int(memorylen, 16)

      print( m.group(1) + ' | ' + memoryaddr + ' | ' + memorylen + ' | ', end = '' )
      print( m.group(4)[0:int(datalen/4)] + ' ' + m.group(4)[int(datalen/4):int(datalen/2)] + ' ' + m.group(4)[int(datalen/2):int(3*datalen/4)] + ' ' + m.group(4)[int(3*datalen/4):] , end = '' )
      print( ' | ' + m.group(5) + ' ' + m.group(6) + ' ||', end = '' )

      # print printable chars
      for i in range(0, len(m.group(4)), 2):

         if i % 8 == 0:
            print(' ', end = '')

         idec = int(m.group(4)[i:i+2], 16)
         if (32 <= idec and idec < 127) or (160 <= idec):
            print( chr(idec), end = '')
         else:
            print('.', end = '')


      print(' || ', end='')

      # print everything again without spaces (better for searching)      
      for i in range(0, len(m.group(4)), 2):

         idec = int(m.group(4)[i:i+2], 16)
         if (32 <= idec and idec < 127) or (160 <= idec):
            print( chr(idec), end = '')
         else:
            print('.', end = '')


      print(" ||")

   elif m_firmwarewrite is not None:

      # line with firmware write data (type 0x01)

      datalen = len(m_firmwarewrite.group(3))

      memoryaddr = m_firmwarewrite.group(2)
      data = m_firmwarewrite.group(3)

      print( m_firmwarewrite.group(1) + ' | ' + memoryaddr + ' | ', end = '' )
      print( m_firmwarewrite.group(3)[0:int(datalen/4)] + ' ' + m_firmwarewrite.group(3)[int(datalen/4):int(datalen/2)] + ' ' + m_firmwarewrite.group(3)[int(datalen/2):int(3*datalen/4)] + ' ' + m_firmwarewrite.group(3)[int(3*datalen/4):] , end = '' )
      print( ' | ' + m_firmwarewrite.group(4) + ' ' + m_firmwarewrite.group(5) + ' ||', end = '' )

      # print printable chars
      for i in range(0, len(m_firmwarewrite.group(3)), 2):

         if i % 8 == 0:
            print(' ', end = '')

         idec = int(m_firmwarewrite.group(3)[i:i+2], 16)
         if (32 <= idec and idec < 127) or (160 <= idec):
            print( chr(idec), end = '')
         else:
            print('.', end = '')


      print(' || ', end='')

      # print everything again without spaces (better for searching)      
      for i in range(0, len(m_firmwarewrite.group(3)), 2):

         idec = int(m_firmwarewrite.group(3)[i:i+2], 16)
         if (32 <= idec and idec < 127) or (160 <= idec):
            print( chr(idec), end = '')
         else:
            print('.', end = '')


      print(" ||")


   elif line == '':
      # throw away empty line
      pass

   elif line == '454e44':
      # end of transmission. print size of last block

      if expnextaddr != 0:
         print( '=> Block ' + str(nummemoryblocks) + ': ' )
         print( '=> Size: ' + str(hex(blockstartaddr)) + ' .. ' + str(hex(expnextaddr-1)) + ': ' + str( expnextaddr - blockstartaddr ) + ' bytes' )
         print("")
         print(line)

   elif line == '5202fa002010':
      # special address read by cps before writing to device
      print("")
      print(line)
      
   elif line[0:2] == '52' and line != '5202fa002010':
      # throw away read request
      pass

   elif len(line) > 2:
   
      # other data. do some hex decode
   
      print( line + ' || ', end = '')

      # print printable chars
      for i in range(0, len(line), 2):
         idec = int(line[i:i+2], 16)
         if (32 <= idec and idec < 127) or (160 <= idec):
            print(chr(idec), end = '')
         else:
            print('.', end = '')
      
      print("")


   elif line == '06':
      # throw away acknowledge message
      pass

   else:
      # just print everything else
      print( line )
   
      
f.close()
