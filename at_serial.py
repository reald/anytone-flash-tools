# serial port communication

import serial
import time


serialPort = None
maxBytesPerReadMessage = 255 # Anytone CPS uses 16, up to 255 possible
maxBytesPerWriteMessage = 16 # Anytone CPS uses 16, more possible?
printDebug = 0

def open_device(portname):
   global serialPort 

   # open serial port
   try:
      serialPort = serial.Serial(port = portname, baudrate=921600, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000
   except:
      print('ERR: Could not open port ' + portname)
      exit()



def start_pcmode():
   global serialPort

   # change to pc mode
   serialPort.write(b'PROGRAM')

   resp = serialPort.read()
   while serialPort.in_waiting > 0:
      resp += serialPort.read()

   if resp != b'QX\x06':
      print ('ERR: Unexpected response from device (' + str(resp) + ')' )
      exit()
   else:
      print('PC Mode ok.')



def end_pcmode():
   global serialPort

   # leave pc mode
   serialPort.write(b'END')

   resp = serialPort.read()
   while serialPort.in_waiting > 0:
      resp += serialPort.read()

   if resp != b'\x06':
      print ('ERR: Unexpected response from device (' + str(resp) + ')' )
      exit()



def start_updatemode():
   global serialPort

   # change to update mode
   serialPort.write(b'UPDATE')

   resp = serialPort.read()
   while serialPort.in_waiting > 0:
      resp += serialPort.read()

   if resp != b'\x06':
      print ('ERR: Unexpected response from device (' + str(resp) + ')' )
      exit()



def end_updatemode():
   global serialPort

   # leave pc mode
   serialPort.write(b'\x18')

   resp = serialPort.read()
   while serialPort.in_waiting > 0:
      resp += serialPort.read()

   if resp != b'\x06':
      print ('ERR: Unexpected response from device (' + str(resp) + ')' )
      exit()



def close_device():
   global serialPort

   # close serial port   
   serialPort.close()



def get_device_info():
   global serialPort

   serialPort.write(b'\x02')

   resp = serialPort.read()

   while serialPort.in_waiting > 0:
      resp += serialPort.read()

   # return devicename and version
   return ( resp[0:8], resp[9:14] )



def print_debug_message(message):

      if len(message) > 8: # 1 byte command + 4 byte address + 1 byte length + 1 byte checksum + 1 byte ACK
         # at least 1 byte data present

         print( message[0:1].hex() + ' | ' + message[1:5].hex() + ' | ' + message[5:6].hex() + ' || ', end = '' )


         # print data as hex
         startdata = 6
         enddata = len(message) - 3
         
         i = startdata
         j = 0
         while i <= enddata:
         
            print('{0:0{1}x}'.format(message[i],2), end = '')
            
            if j == 3:
               print(' ' , end = '')
               j = 0
            else:
               j += 1
               
            i += 1


         # print checksum and ack
         print ( '| ' + message[enddata+1:enddata+2].hex() + ' ' + message[enddata+2:enddata+3].hex() + ' || ', end = '' )
 
         # print data as ascii with spaces

         i = startdata
         j = 0
         while i <= enddata:

            idec = message[i]
            
            if (32 <= idec and idec < 127) or (160 <= idec):
               print( chr(idec), end = '')

            else:
               print('.', end = '')
            
            if j == 3:
               print(' ' , end = '')
               j = 0
            else:
               j += 1
               
            i += 1

         print('|| ', end = '')

         # print data as ascii without spaces
         i = startdata
         while i <= enddata:

            idec = message[i]
            
            if (32 <= idec and idec < 127) or (160 <= idec):
               print( chr(idec), end = '')

            else:
               print('.', end = '')
            
            i += 1

         print(' || ', end = '')


      print()


   
def read_memory(address, num_bytes_left):
   global serialPort

   resp = bytearray()
    
   while num_bytes_left > 0:
   
      #print(num_bytes_left) # debug
   
      num_bytes = min(num_bytes_left, maxBytesPerReadMessage)
   
      #5202fa002010
      readcmd = bytearray()
      readcmd.append( ord('R') )
      readcmd.append( (address & 0xff000000) >> 24 )
      readcmd.append( (address & 0x00ff0000) >> 16 )
      readcmd.append( (address & 0x0000ff00) >> 8 )
      readcmd.append( (address & 0x000000ff) )
      readcmd.append( num_bytes )
   
      serialPort.write(readcmd)
   
      message = bytearray()
      message.append( ord(serialPort.read()) )
      while serialPort.in_waiting > 0:
         message.append( ord(serialPort.read()) )
      
      checksum = sum(message[1:-2]) & 0xff

      if ( printDebug != 0):
         print_debug_message(message)
      
      # check response      
      if message[-2] != checksum:
         print('WARN: Checksum failed. Retransmitting at ' + str(address) )
         continue
      elif message[0] != ord('W'):
         print('WARN: First byte of response not "W": ' + hex(message[0]) + ' Retransmitting at ' + str(address) )
         continue
      elif message[-1] != 0x06:
         print('WARN: Last byte of response not 0x06. Retransmitting at ' + str(address) )
         continue
         
      # message ok.   
      num_bytes_left -= num_bytes
      address += num_bytes

      # save payload only (skip 'W' + 4 bytes address + 1 byte length, cut checksum and ack)
      resp = resp + message[6:-2]
   
   return [resp, len(resp)]



def write_memory(address, data):
   global serialPort
   
   num_bytes_left = len(data)
   dataptr = 0
    
   while num_bytes_left > 0:
   
      #print(num_bytes_left) # debug
   
      num_bytes = min(num_bytes_left, maxBytesPerWriteMessage)
      
      while num_bytes_left < maxBytesPerWriteMessage:
         # pad with zeros to reach at least 16 bytes per message
         data.append(0)
         num_bytes_left += 1
         num_bytes += 1
         
   
      # 57 | 05ccab80 | 10 || ffffffff ffffffff ffffffff ffffffff | fc 06 
      writecmd = bytearray()
      writecmd.append( ord('W') )
      writecmd.append( (address & 0xff000000) >> 24 )
      writecmd.append( (address & 0x00ff0000) >> 16 )
      writecmd.append( (address & 0x0000ff00) >> 8 )
      writecmd.append( (address & 0x000000ff) )
      writecmd.append( num_bytes )
      
      i = 0
      while i < num_bytes:
         writecmd.append( data[dataptr+i] )
         i += 1

      checksum = sum(writecmd[1:]) & 0xff
      writecmd.append( checksum )
      writecmd.append( 0x06 )
      
      
      print_debug_message(writecmd)

      serialPort.write(writecmd)
  
      # read answer
      answ = bytearray()
      answ.append( ord(serialPort.read()) )
      while serialPort.in_waiting > 0:
         answ.append( ord(serialPort.read()) )
      
      if answ[0] == 0x06:
         # ack received, ok
         num_bytes_left -= num_bytes
         dataptr += num_bytes
         address += num_bytes
      else:
         # no response. write again
         print('WARN: No response on write request. Retransmitting at ' + str(address) )
         


def write_memory_hex(address, hexdata):
   global serialPort
   
   data = bytes.fromhex(hexdata)
   
   num_bytes_left = len(data)
   dataptr = 0
    
   while num_bytes_left > 0:
   
      #print(num_bytes_left) # debug
   
      num_bytes = min(num_bytes_left, maxBytesPerWriteMessage)
   
      # 57 | 05ccab80 | 10 || ffffffff ffffffff ffffffff ffffffff | fc 06 
      writecmd = bytearray()
      writecmd.append( ord('W') )
      writecmd.append( (address & 0xff000000) >> 24 )
      writecmd.append( (address & 0x00ff0000) >> 16 )
      writecmd.append( (address & 0x0000ff00) >> 8 )
      writecmd.append( (address & 0x000000ff) )
      writecmd.append( num_bytes )

      i = 0
      while i < num_bytes:
         writecmd.append( data[dataptr+i] )
         i += 1

      checksum = sum(writecmd[1:]) & 0xff
      writecmd.append( checksum )
      writecmd.append( 0x06 )
      
      
      print_debug_message(writecmd)

      serialPort.write(writecmd)
  
      # read answer
      answ = bytearray()
      answ.append( ord(serialPort.read()) )
      while serialPort.in_waiting > 0:
         answ.append( ord(serialPort.read()) )
      
      if answ[0] == 0x06:
         # ack received, ok
         num_bytes_left -= num_bytes
         dataptr += num_bytes
         address += num_bytes
      else:
         # no response. write again
         print('WARN: No response on write request. Retransmitting at ' + str(address) )
         


def write_raw_hex(hexline):
   # write raw and already complete hex string to radio
   # warning: no checks!

   global serialPort

   data = bytes.fromhex(hexline)

   serialPort.write(data)

   # read answer
   answ = bytearray()
   answ.append( ord(serialPort.read()) )
   while serialPort.in_waiting > 0:
      answ.append( ord(serialPort.read()) )

   if answ[0] == 0x06:
      # ack received, ok
      pass
   else:
      # no response. write again
      print('WARN: No response on write request. Retransmitting not implemented. FIXME' )

