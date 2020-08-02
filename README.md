# anytone-flash-tools
Independend flash tools for Anytone 878UV radios and maybe other anytone models

## Goal
Understand the communication protocol between customer programming software (CPS) and radio. Provide open source platform independent reprogramming tools.

## Why?
Because it has to be done. CPS is only available on windows. Device and CPS will be discontinued and stop working some time. Most of the features are only programmable via software and not on the device itself. So there must be a free alternative.

## How?
Install Wireshark with USBPcap Option and Capture the USB traffic when using the CPS. Save the capture file and filter out the "Leftover Capture Data". This is the data between the CPS and the radio. Tshark helps exporting the traffic:

```
tshark -T fields -e usb.capdata -r file.pcapng
```

## AT878UV Protocol
https://github.com/reald/anytone-flash-tools/blob/master/at878uv_protocol.md

## AT878UV memory layout

## Available tools so far...
This his highly experimental code. Use it at your own risk!

* Read digital contact list from radio to .csv file (readcontacts.py)
* Write digital contact list from .csv file to radio (writecontacts.py)
