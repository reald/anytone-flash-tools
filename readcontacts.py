#!/usr/bin/env python3

import sys
import at_serial
import at_devices

comport = '/dev/ttyACM0'   


if len(sys.argv) == 3:
   exportfilename = sys.argv[1]
   comport = sys.argv[2]
elif len(sys.argv) == 2:
   exportfilename = sys.argv[1]
else:
   print("Usage: " + sys.argv[0] + ' outputfilename.csv [comport]')
   exit()


# connect to device
at_serial.open_device(comport)


# set pc mode
at_serial.start_pcmode()


# is this device supported?
[devicename, version] = at_serial.get_device_info()

if at_devices.is_device_supported(devicename, version):
   # known device found
   print('OK: Radio ' + str(devicename[:-1], "utf-8") + ' / ' + str(version[:-1], "utf-8") + ' connected.')
else:
   print('ERR: Device not supported (' + str(devicename) + ' ' + str(version) + ')' )
   exit()



# do something
#[resp, resplen] = at_serial.read_memory(0x02fa0020, 32)

# read contact list index
[resp, resplen] = at_serial.read_memory(at_devices.memSectContactsIndexAddr, at_devices.memSectContactsIndexSize)
numContacts = (resp[3] << 24) + (resp[2] << 16) + (resp[1] << 8) + resp[0]
memAddrEndContacts = (resp[7] << 24) + (resp[6] << 16) + (resp[5] << 8) + resp[4]


if numContacts > 0:
   print( "Reading " + str(numContacts) + ' contacts from radio...' )

   # read contact list data
   contactListData = bytearray()

   #memAddrEndContacts = 0x45c0000 # debug

   i = 0

   while ( i < len(at_devices.memSectContacts) \
           and at_devices.memSectContacts[i]['address'] <= memAddrEndContacts \
         ):
   
      # read block
      numbytestoread = min ( at_devices.memSectContacts[i]['size'], (memAddrEndContacts - at_devices.memSectContacts[i]['address'] + 1) )

      [resp, resplen] = at_serial.read_memory(at_devices.memSectContacts[i]['address'], numbytestoread)
      contactListData = contactListData + resp
   
      i += 1

   # parse data and create contact list .csv
   at_devices.contactlist2csv(contactListData, numContacts, exportfilename)

else:
   print("No contacts stored.")



# end pc mode
at_serial.end_pcmode()


# close device
at_serial.close_device()
