#!/usr/bin/env python3

import sys
import re
import at_serial
import at_devices

comport = '/dev/ttyACM0'   


if len(sys.argv) == 3:
   importfilename = sys.argv[1]
   comport = sys.argv[2]
elif len(sys.argv) == 2:
   importfilename = sys.argv[1]
else:
   print("Usage: " + sys.argv[0] + ' inputfilename.hex [comport]')
   exit()



# open hex file
print("Reading hexdump...")
file = open(sys.argv[1], 'r') 
lines = file.readlines() 
file.close()



# connect to device
at_serial.open_device(comport)


# is this file data or firmware write?
logtype = 0
for line in lines:

   if re.search('^50524f4752414d.*', line, re.IGNORECASE):
       # PROGRAM
       logtype = logtype | 1
   elif re.search('^555044415445.*', line):
       # UPDATE
       logtype = logtype | 2

if logtype == 3:
   sys.exit("Unclear log file. PROGRAM or UPDATE?")
elif logtype == 0:
   sys.exit("No PROGRAM or UPDATE marker found.")
elif logtype == 1:
   print("PROGRAM MODE")
   at_serial.start_pcmode()
elif logtype == 2:
   print("UPDATE MODE")
   at_serial.start_updatemode()


# is this device supported?
[devicename, version] = at_serial.get_device_info()

if at_devices.is_device_supported(devicename, version):
   # known device found
   print('OK: Radio ' + str(devicename[:-1], "utf-8") + ' / ' + str(version[:-1], "utf-8") + ' connected.')
else:
   print('ERR: Device not supported (' + str(devicename) + ' ' + str(version) + ')' )
   exit()



# do something. what is this read command for?
[resp, resplen] = at_serial.read_memory(0x02fa0020, 16)


# retransfer hexdump
print("Retransfer write hexdump...")
for line in lines:
   
   line = line.rstrip()
   
   # remove formatting if already formatted
   m = re.search('^(57|01)(.*)(06 \|\|).*$', line)
   
   if m is not None:
      line = m.group(1) + m.group(2) + m.group(3)
      line = line.replace (' ', '')
      line = line.replace ('|', '')

   
   if line[0:2] == '57' or line[0:2] == '01':
      print(line)
      at_serial.write_raw_hex(line)
   

# end pc or update  mode
if logtype == 1:
   at_serial.end_pcmode()
elif logtype == 2:
   at_serial.end_updatemode()


# close device
at_serial.close_device()
