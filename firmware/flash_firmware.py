#!/usr/bin/env python3
#
# Flash firmware to Anytone D878UV (and maybe others)
#
# Tested with firmware version 1.20p and 1.21.
#
# ./flashfirmware firmware.spi [comport]
#

import sys
import serial

# config
comport = '/dev/ttyACM0'


# parameters

if len(sys.argv) == 3:
   firmwarefilename = sys.argv[1]
   comport = sys.argv[2]
elif len(sys.argv) == 2:
   firmwarefilename = sys.argv[1]
else:
   print("Usage: " + sys.argv[0] + ' firmware_file.spi [comport]')
   exit()


print("Anytone 8x8 firmware flash tool")
print("===============================")

print("WARNING! THIS SOFTWARE IS HIGHLY EXPERIMENTAL!")
print("YOU CAN DAMAGE YOUR DEVICE! USE AT YOUR OWN RISK!")
print("")
print("FLASHING FIRMWARE WILL DELETE CODEPLUG! BACKUP CODEPLUG FIRST!")
print("")


# .spi file
print("Investigating .spi file...")

file = open(firmwarefilename, "rb")
with file:
   spifile = file.read()
file.close

if len(spifile) != 51:
   sys.exit("ERROR: " + firmwarefilename + " size is expected to be 51 bytes and not " + len(spifile) + " bytes!")

if spifile[0:6] != b' \x00\x00\x00\x01\x00' \
   or spifile[10:14] != b'\x00\x00\x00\x00' \
   or spifile[20:22] != b'  ' \
   or spifile[32:42] != b'          ' \
   or spifile[46:51] != b'    \x00' :
      sys.exit("ERROR: Unexpected .spi file format!")
   
model1 = spifile[14:20]
hwvers1 = spifile[22:26]
model2 = spifile[26:32]
hwvers2 = spifile[42:46]

if model1 != model2 :
   sys.exit("ERROR: Model name different!")
   
if hwvers1 != hwvers2 :
   sys.exit("ERROR: HW version name different!")
  
   
filesize = spifile[6] + (spifile[7]<<8) + (spifile[8]<<16) + (spifile[9]<<24)

print("Detected firmware for " + str(model1) + " hardware version " + str(hwvers1) + "; firmware should be " + str(filesize) + " bytes.\n")



# .CDI
print("Investigating .CDI file...")

file = open(firmwarefilename[0:-3] + "CDI", "rb")
with file:
   cdifile = file.read()
file.close

if len(cdifile) != 278:
   sys.exit("ERROR: " + firmwarefilename[0:-3] + "CDI" + " size is expected to be 278 bytes and not " + str(len(cdifile)) + " bytes!")

if cdifile[0:6] != model1 \
   or cdifile[6:14] != b'_1G.bin\x00' \
   or cdifile[14:256] != b'                                                                                                                                                                                                                                                  ' \
   or cdifile[264:278] != b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00' :
      sys.exit("ERROR: Unexpected .CDI file format!")

filesize2 = cdifile[260] + (cdifile[261]<<8) + (cdifile[262]<<16) + (cdifile[263]<<24)

if filesize != filesize2:
   sys.exit("ERROR: filesize mismatch (" + str(filesize) + "/" + str(filesize2) + ")!")

startaddress = cdifile[256] + (cdifile[257]<<8) + (cdifile[258]<<16) + (cdifile[259]<<24)

if cdifile[259] != 0x08:
   sys.exit("ERROR: Expecting start address starting with 0x8 and not " + str(hex(cdifile[259])) )

print("Found start address: " + hex(startaddress) + "\n")



# .CDD
print("Investigating .CDD file...")

file = open(firmwarefilename[0:-3] + "CDD", "rb")
with file:
   cddfile = file.read()
file.close

if len(cddfile) != filesize:
   sys.exit("ERROR: " + firmwarefilename[0:-3] + "CDD" + " size is expected to be " + str(filesize) + " bytes and not " + str(len(cddfile)) + " bytes!")
else:
   print("File size OK.\n")


# open serial port
serialPort = None

try:
   print("Trying comport " + comport)
   serialPort = serial.Serial(port = comport, baudrate=4000000, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE) # 115200 921600 4000000
except Exception as e:
   sys.exit('ERR: Could not open port ' + comport + ". " + str(e))




# activate "UPDATE" mode.
print("\nPlease start device holding PF3 (blue button on top) and PTT. Press key when ready.")
print("Do you have a backup of your codeplug?")

input("Ready to update?")

serialPort.write(b'UPDATE')

resp = serialPort.read()
while serialPort.in_waiting > 0:
   resp += serialPort.read()

if resp != b'\x06':
   print ('ERR: Unexpected response from device (' + str(resp) + ')' )
   exit()



# read device string
serialPort.write(b'\x02')

resp = serialPort.read()
while serialPort.in_waiting > 0:
   resp += serialPort.read()

if resp[1:7] != model1:
   print ("ERROR: Device identifier " + str(resp[1:7]) + " does not fit to firmware identifier (" + str(model1)  + ")" )
   exit()

if resp[9:13] != hwvers1:
   print ("ERROR: Hardware version " + str(resp[9:13]) + " does not fit to firmware version (" + str(hwvers1)  + ")" )
   exit()

print("Device " + str(model1) + " version " + str(hwvers1) + " detected. Start transmitting firmware...")

# CDD in 32 byte blöcke verpacken und an das gerät senden. wenn kein ACK, dann paket widerholen. letztes paket mit 0 padden. 2 byte checksum

writecmd = bytearray()
writecmd.append ( 0x01 )
writecmd.append( (startaddress & 0x000000ff) )
writecmd.append( (startaddress & 0x0000ff00) >> 8 )
writecmd.append( (startaddress & 0x00ff0000) >> 16 )
writecmd.append( (startaddress & 0xff000000) >> 24 )


for i in range(filesize):
   
   writecmd.append( cddfile[i] )
   
   if (i == filesize-1) and (((i+1) % 32) != 0) :

      # end. append 0
      while ( ((i+1)% 32) != 0 ):
         writecmd.append( 0x00 )
         i += 1
      
   
   if ((i+1) % 32) == 0:

      # add checksum
      checksum = sum(writecmd[1:])
      writecmd.append(checksum & 0xff)
      writecmd.append((checksum>>8) & 0xff)

      # add ack
      writecmd.append(0x06)

      print(str(i), hex(startaddress), writecmd.hex())
      
      # write to serial port
      numtries = 0
      while ( numtries < 3 ):
      
         serialPort.write(writecmd)

         resp = serialPort.read()
         while serialPort.in_waiting > 0:
            resp += serialPort.read()

         if ( resp != b'\x06' ):
            print("Command not received (" + str(resp) + "). Retransfer command")
            numtries += 1
         else:
            numtries = 4

      if numtries == 3:
         sys.exit("Transfer finally failed")
      
      # new command string
      startaddress += 32
      
      writecmd = bytearray()
      writecmd.append ( 0x01 )
      writecmd.append( (startaddress & 0x000000ff) )
      writecmd.append( (startaddress & 0x0000ff00) >> 8 )
      writecmd.append( (startaddress & 0x00ff0000) >> 16 )
      writecmd.append( (startaddress & 0xff000000) >> 24 )





# finish transfer
try:
   
   print("Finishing transfer")

   serialPort.write(b'\x18')

   resp = serialPort.read()
   while serialPort.in_waiting > 0:
     resp += serialPort.read()

   if resp == b'\x06':
      print("Firmware successfully transferred. Switch device off and hold PF1 (top function key on the left side next to PTT) and PTT keys together while switching on to start installer.")
   else:
      print("ERROR: Closing transfer failed (" + str(resp) + ")" )

except Exception as e:
   print(e)

serialPort.close()
