import csv

# devices supported by this software
list_known_devices = []
list_known_devices.append({'devicename': b'ID878UV\x00', 'version': b'V100\x00'}) # Anytone 878UV



memSectContactsOffsetWrite = []
memSectContactsIndexAddr = 0
memSectContactsIndexSize = 0
memSectContacts = []



def is_device_supported(devicename, version):
   # is this device supported?

   for device in list_known_devices:

      if devicename == device['devicename'] and version == device['version']:

         # known device found
         if devicename == b'ID878UV\x00':
            import at_878uv as atm
         else:
            print('ERR: Device found but no data file defined.')
            exit()

         global memSectContactsOffsetWrite
         global memSectContactsIndexAddr
         global memSectContactsIndexSize
         global memSectContacts
         
         memSectContactsOffsetWrite = atm.memSectContactsOffsetWrite
         memSectContactsIndexAddr = atm.memSectContactsIndexAddr
         memSectContactsIndexSize = atm.memSectContactsIndexSize
         memSectContacts = atm.memSectContacts
         
         return True

   return False
   


# read contact list from device and save to csv file
def contactlist2csv(rawdata, numallcontacts, filename):

   f = open(filename, "w")
   
   f.write ('"No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"' + "\r\n")

   i = 0
   numdatasets = 0
   
   while ( numdatasets < numallcontacts ): # fixme. add checks and avoid out of bound access

      numdatasets += 1
   
      # CT: Call Type: 00 -> Private Call, 01 -> Group Call, 02 -> "All" (only 1x allowed), 1 byte
      if rawdata[i] == 0:
         calltype = 'Private Call'
      elif rawdata[i] == 1:
         calltype = 'Group Call'
      elif rawdata[i] == 2:
         calltype = 'All'
      else:
         print("ERR: Unknown call type " + hex(rawdata[i]) + ' at offset ' + str(i) )
         exit()
         
      i += 1

      # ID: TG/DMRID als BCD, 4 bytes
      radioid = ''
      radioid += str( (rawdata[i] & 0xf0) >> 4 )
      radioid += str( (rawdata[i] & 0x0f) )
      radioid += str( (rawdata[i+1] & 0xf0) >> 4 )
      radioid += str( (rawdata[i+1] & 0x0f) )
      radioid += str( (rawdata[i+2] & 0xf0) >> 4 )
      radioid += str( (rawdata[i+2] & 0x0f) )
      radioid += str( (rawdata[i+3] & 0xf0) >> 4 )
      radioid += str( (rawdata[i+3] & 0x0f) )
      radioid = radioid.lstrip('0')
      
      i += 4

      # CA: Call Alert. 00 -> none, 01 -> Ring, 02 -> Online Alert
      if rawdata[i] == 0:
         callalert = 'None'
      elif rawdata[i] == 1:
         callalert = 'Ring'
      elif rawdata[i] == 2:
         callalert = 'Online Alert'
      else:
         print("ERR: Unknown call alert " + hex(rawdata[i]) + ' at offset ' + str(i) )
         exit()
      
      i += 1
      
      # NA: Name. Ascii, 0 terminated, max 16 bytes
      name = ''
      while ( rawdata[i] != 0x00 ):
         name += chr(rawdata[i])
         i += 1
         
      i += 1
   
      # CI: City. Ascii, 0 terminated, max 15 bytes
      city = ''
      while ( rawdata[i] != 0x00 ):
         city += chr(rawdata[i])
         i += 1

      i += 1

      # CS: Callsign, Ascii, 0 terminated , max 8 bytes
      callsign = ''
      while ( rawdata[i] != 0x00 ):
         callsign += chr(rawdata[i])
         i += 1

      i += 1

      # SP: State/Prov, Ascii, 0 terminated, max. 16 bytes
      state = ''
      while ( rawdata[i] != 0x00 ):
         state += chr(rawdata[i])
         i += 1
      
      i += 1

      # CO: Country, Ascii, 0 terminated, max. 16 bytes
      country = ''
      while ( rawdata[i] != 0x00 ):
         country += chr(rawdata[i])
         i += 1

      i += 1

      # RE: Remarks, Ascii, 0 terminated, max. 16 bytes
      remarks = ''
      while ( rawdata[i] != 0x00 ):
         remarks += chr(rawdata[i])
         i += 1

      i += 1

      #1,1023001,VE3THW,Wayne,Toronto,Ontario,Canada,,Private Call,None
      f.write( '"' + str(numdatasets) + '","' + radioid + '","' + callsign + '","' + name + '","' + city + '","' + state + '","' + country + '","' + remarks + '","' + calltype + '","' + callalert + '"' + "\r\n" )

   # all done. close file
   f.close()


# read csv and write contact list to device
def csv2contactlist(importfilename):
   offsetData = bytearray()
   contactListData = bytearray()
   numContacts = 0

   # read contact list file
   with open(importfilename, newline = '', encoding='latin1') as csvfile:
   
      csvreader = csv.reader(csvfile, delimiter=',')  #, quotechar='"') # fixme: CPS uses quotechar, https://github.com/ContactLists/ContactLists doesn´t

      # read header
      headers = next(csvreader, None)
      
      # 'No.', 'Radio ID', 'Callsign', 'Name', 'City', 'State', 'Country', 'Remarks', 'Call Type', 'Call Alert'
      numcols = 0
      
      # mandatory columns
      columnidx = {
         'radioid' : -1,
         'callsign' : -1,
         'name' : -1,
         'city' : -1,
         'state' : -1,
         'country' : -1,
         'remarks' : -1,
         'calltype' : -1,
         'callalert' : -1
      }

      for h in headers:
         if h == 'No.':
            pass # number is not needed
         
         elif h == 'Radio ID':
            columnidx['radioid'] = numcols
         elif h == 'Callsign':
            columnidx['callsign'] = numcols
         elif h == 'Name':
            columnidx['name'] = numcols
         elif h == 'City':
            columnidx['city'] = numcols
         elif h == 'State':
            columnidx['state'] = numcols
         elif h == 'Country':
            columnidx['country'] = numcols
         elif h == 'Remarks':
            columnidx['remarks'] = numcols
         elif h == 'Call Type':
            columnidx['calltype'] = numcols
         elif h == 'Call Alert':
            columnidx['callalert'] = numcols
         else:
            print('WAR: Unknown column: ' + h)
            
         numcols += 1
      
      for x in columnidx:
         if columnidx[x] == -1:
            print('ERR: Mandatory column for ' + x + ' not present in .csv file!')
            exit()



      ### read all datasets
      
      numcalltypeall = 0
      actualcontactofs = 0
      numContacts = 0

      for line in csvreader:
         
         ## build contact list data

         # byte 0: Call Type
         contactentry = bytearray()

         if line[columnidx['calltype']] == 'All':
            contactentry.append(2)
            numcalltypeall += 1
            
            if numcalltypeall > 1:
               print('ERR: Only one entry with call type "All" allowed')
               exit()

         elif line[columnidx['calltype']] == 'Group Call':
            contactentry.append(1)
         else:
            contactentry.append(0)


         # byte 1..4: radio id
         radioidstr = line[columnidx['radioid']]

         if radioidstr != '':

            radioid = 0
          
            for i in range(len(radioidstr)):
               radioid <<= 4
               radioid |= ord(radioidstr[i]) - ord('0')

            contactentry.append( (radioid >> 24) & 0xff )
            contactentry.append( (radioid >> 16) & 0xff )
            contactentry.append( (radioid >> 8) & 0xff )
            contactentry.append( radioid & 0xff )
            
         else:
            print('ERR: Radio ID does not be empty!')
            exit()


         # byte 5: call alert
         if line[columnidx['callalert']] == 'Online Alert':
            contactentry.append(2)
         elif line[columnidx['callalert']] == 'Ring':
            contactentry.append(1)
         else:
            contactentry.append(0)
         
         # byte 6+ ... name
         for i in range( min(16, len(line[ columnidx['name'] ])) ):
            contactentry.append( ord(line[ columnidx['name'] ][i]) )
         contactentry.append(0)
         
         # ... city ...
         for i in range( min(15, len(line[ columnidx['city'] ])) ):
            contactentry.append( ord(line[ columnidx['city'] ][i]) )
         contactentry.append(0)

         # ... callsign ...
         for i in range( min(8, len(line[ columnidx['callsign'] ])) ):
            contactentry.append( ord(line[ columnidx['callsign'] ][i]) )
         contactentry.append(0)

          # ... state ...
         for i in range( min(16, len(line[ columnidx['state'] ])) ):
            contactentry.append( ord(line[ columnidx['state'] ][i]) )
         contactentry.append(0)

          # ... country ...
         for i in range( min(16, len(line[ columnidx['country'] ])) ):
            contactentry.append( ord(line[ columnidx['country'] ][i]) )
         contactentry.append(0)

          # ... remarks ...
         for i in range( min(16, len(line[ columnidx['remarks'] ])) ):
            contactentry.append( ord(line[ columnidx['remarks'] ][i]) )
         contactentry.append(0)


         ## build offset table
         offsetentry = bytearray()

         calltype = line[columnidx['calltype']]
         
         idandtype = radioid << 1
         idandtype |= (calltype == 'Group Call') # fixme: what about "all"?
               
         offsetentry.append( idandtype & 0xff )
         offsetentry.append( (idandtype >> 8) & 0xff )
         offsetentry.append( (idandtype >> 16) & 0xff )
         offsetentry.append( (idandtype >> 24) & 0xff )
            
         offsetentry.append( actualcontactofs & 0xff )
         offsetentry.append( (actualcontactofs >> 8) & 0xff )
         offsetentry.append( (actualcontactofs >> 16) & 0xff )
         offsetentry.append( (actualcontactofs >> 24) & 0xff )

         # everything collected for this dataset
         contactListData += contactentry
         offsetData += offsetentry
         actualcontactofs += len(contactentry)
         numContacts += 1
         

   return [offsetData, contactListData, numContacts]
   