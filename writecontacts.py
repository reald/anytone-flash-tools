#!/usr/bin/env python3

import sys
import at_serial
import at_devices

comport = '/dev/ttyACM0'   


if len(sys.argv) == 3:
   importfilename = sys.argv[1]
   comport = sys.argv[2]
elif len(sys.argv) == 2:
   importfilename = sys.argv[1]
else:
   print("Usage: " + sys.argv[0] + ' inputfilename.csv [comport]')
   exit()


# connect to device
at_serial.open_device(comport)



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


# read contact list from file
[offsetData, contactListData, numContacts] = at_devices.csv2contactlist(importfilename)

contactlistdatalen = len(contactListData)

# calculate next free memory address
for contactsection in at_devices.memSectContacts:

   #print('address:' + hex(contactsection['address']) )
   #print('rest ' + str(contactlistdatalen) )

   if ( contactlistdatalen >= contactsection['size'] ):
      # this not the section with free memory
      contactlistdatalen -= contactsection['size']
   else:
      nextfreememoryaddr = contactsection['address'] + contactlistdatalen
      break
      


# write contact offsets (cannot be read back)

print("Writing contact offsets...")

i = 0

while ( len(offsetData) > 0 \
        and i < len(at_devices.memSectContactsOffsetWrite) ):
   
   # write block
   numbytestowrite = min( at_devices.memSectContactsOffsetWrite[i]['size'], len(offsetData) )

   print("i " + str(i) + " numbytestofwrite " + str(numbytestowrite) + " len offsetData " + str(len(offsetData)) + ' ' + hex(at_devices.memSectContactsOffsetWrite[i]['address']) )

   at_serial.write_memory( at_devices.memSectContactsOffsetWrite[i]['address'], offsetData[:numbytestowrite] )
   offsetData = offsetData[numbytestowrite:]
   i += 1



# write index

print("Writing index...")

numandindex = bytearray()

numandindex.append( numContacts & 0xff )
numandindex.append( (numContacts >> 8) & 0xff )
numandindex.append( (numContacts >> 16) & 0xff )
numandindex.append( (numContacts >> 24) & 0xff )
numandindex.append( nextfreememoryaddr & 0xff )
numandindex.append( (nextfreememoryaddr >> 8) & 0xff )
numandindex.append( (nextfreememoryaddr >> 16) & 0xff )
numandindex.append( (nextfreememoryaddr >> 24) & 0xff )

at_serial.write_memory( at_devices.memSectContactsIndexAddr, numandindex)



# write contact data

print("Writing contact data...")

i = 0

while ( len(contactListData) > 0 \
        and i < len(at_devices.memSectContacts) ):
   
   # write block
   numbytestowrite = min( at_devices.memSectContacts[i]['size'], len(contactListData) )

   print("i " + str(i) + " numbytestofwrite " + str(numbytestowrite) + " len offsetData " + str(len(contactListData)) + ' ' + hex(at_devices.memSectContacts[i]['address']) )

   at_serial.write_memory( at_devices.memSectContacts[i]['address'], contactListData[:numbytestowrite] )
   contactListData = contactListData[numbytestowrite:]
   i += 1

   
# fixme: write padding

# close device
at_serial.close_device()
