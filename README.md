# anytone-flash-tools
Independend flash tools for Anytone D878UV radios and maybe other anytone models

## Goal
Understand the communication protocol between customer programming software (CPS) and radio. Provide open source platform independent reprogramming tools.

## Why?
Because it has to be done. CPS is only available on windows. Device and CPS will be discontinued and stop working some time. Most of the features are only programmable via software and not on the device itself. So there must be a free alternative.

## How?
Install Wireshark with USBPcap Option and Capture the USB traffic when using the CPS. Save the capture file and filter out the "Leftover Capture Data". This is the data between the CPS and the radio. Tshark helps exporting the traffic:

```
tshark -T fields -e usb.capdata -r file.pcapng
```
The script createhexdump.py formats the hex output to a more readable form. Then make transfers with small configuration changes and watch the difference in the hex dumps.

Instead of using wireshark and a real radio you can try the [AT-D878UV emulator](emulator/README.md) for programming protocol analysis. This script emulates the radio behaviour to the programming software and sends all of the programming data to a server script for deeper analysis. 

## AT-D878UV Serial protocol
https://github.com/reald/anytone-flash-tools/blob/master/at-d878uv_protocol.md

## AT-D878UV memory layout
https://github.com/reald/anytone-flash-tools/blob/master/at-d878uv_memory.md

## Available tools so far...
This is highly experimental code. Use it at your own risk!

* Digital contact list

  * Write digital contact list from .csv file to radio ([writecontacts.py](writecontacts.py))
  * Read digital contact list from radio to .csv file ([readcontacts.py](readcontacts.py))
  * Hint: You can download digital contact lists for Anytone devices e.g. here: 
       * https://github.com/ContactLists/ContactLists/tree/master/Anytone  

* Emulator for flash protocol analysis
  * Emulate Anytone D878UV radio to customer programming software via virtual null modem cables ([Emulator](emulator/at_d878uv_emulator.py))
  * Receive intercepted programming data from AT-D878UV emulator via network and diff hexdumps ([Server](emulator/at_d878uv_server.py))

* Flash Firmware
  * [Transfer firmware update](firmware/README.md) to radio. Attention: Updating firmware will delete codeplug. Backup with CPS first! 
  
* Rewrite Hex Dump
  * Retransfer hex dump (saved by emulator) to a serial port (rewrite_hexdump.py)

## Done - understand memory layout
* Channel
* 2 Tone Encode
* APRS
* Analog Address Book
* 5 Tone Encode
* FM
* DTMF Encode
* Radio ID List
* Prefabricated SMS
* Talk Groups
* Auto Repeater Offset Frequencies
* Roaming Channel
* Roaming Zone
* Receive Group Call List
* Zone
* Scan List
* Optional Settings
* Alarm Settings
* Encryption Code
* Talk Alias
* AES Encryption Code
* Hotkey_QuickCall
* Hotkey_State
* Hotkey_Hotkey
* Firmware Update

## Todo - understand memory layout

* Local information
* Written memory areas which not part of this list

## Todo - other things

* Icon Update
* Boot Image
* ...
