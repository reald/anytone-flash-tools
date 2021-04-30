# AT-D878UV Protocol

Notes: 
- Most investigations have been done with firmware version 1.19.
- Firmware version 1.21 seems to still be compatible.

## Connection
The cable has no logic inside and just connects 3 USB wires (not the 5V pin). After plugging in and switching on the a serial port appears (/dev/ttyACM0 under linux).
Set terminal or connection mode to 8-N-1, baudrate seems to be set by the driver. Selecting 9600, 115200, 921600 or 4000000 baud made no difference in transfer speed.

## Commands

### Start programming session

To start a programming session send the hex string "50524f4752414d" ("PROGRAM") to the device. The radio will answer with "515806" ("QX[ACK]") and shows "PC Mode" on the display.

```
> 50524f4752414d (PROGRAM)
< 515806 (QX[ACK])
```

### Read device identifier

Send hex "02" to the radio. The answer will be something like ASCII "ID878UV..V100..[ACK]".
```
> 02
< 49443837385556000056313030000006 (ID878UV..V100..[ACK])
  IDIDIDIDIDIDID??BFVVVVVVVV???? 
   - ID - Device ID
   - BF - Band Frequency: 0x00 Rx: 400-480 136-174 Tx:400-480 136-174
                          0x01 Rx: 400-480 136-174 Tx:400-480 136-174 (12,5KHz Only)
                          0x02 Rx: 430-440 136-174 Tx:430-440 136-174
                          0x03 Rx: 400-480 136-174 Tx:430-440 144-146
                          0x04 Rx: 440-480 136-174 Tx:440-480 136-174
                          0x05 Rx: 440-480 144-146 Tx:440-480 144-146
                          0x06 Rx: 446-447 136-174 Tx:446-447 136-174
                          0x07 Rx: 400-480 136-174 Tx:420-450 144-148
                          0x08 Rx: 400-470 136-174 Tx:400-470 136-174
                          0x09 Rx: 430-432 144-146 Tx:430-432 144-146
                          0x0a Rx: 400-480 136-174 Tx:430-450 144-148
                          0x0b Rx: 400-520 136-174 Tx:400-520 136-174
                          0x0c Rx: 400-490 136-174 Tx:400-490 136-174
                          0x0d Rx: 400-480 136-174 Tx:403-470 136-174
                          0x0e Rx: 400-520 220-225 136-174 Tx:400-520 220-225 136-174
                          0x0f Rx: 420-520 144-148 Tx:420-520 144-148
                          0x10 Rx: 430-440 144-147 Tx:430-440 144-147
                          0x11 Rx: 430-440 136-174 Tx:136-174
   
   - VV - Version?
```

### Read memory

Reading memory is done with the "R" command (0x52) followed by a 4 byte memory address (0x02fa0020 in this case, high byte first) and the number of requested bytes. Usually 16 Bytes (0x10) are read at once but it is possible to enlarge the answer to 255 Bytes (0xff). This rapidly increases reading speed. The radio will answer with a "W" command (0x57), the requested 4 byte memory address, the length, the data itself, a 1 byte checksum (0x24 in this case) and 1 byte ACK (0x06):

```
> 5202fa002010
< 5702fa002010ffffffffffffffff00000000000000002406
```
The checksum is just a 1 byte sum over the 4 byte address and all data. The first byte "W" is NOT included here.

### Writing memory

Writing memory is done the same way as the radio response to a read request: 1 byte "W" as write command, a 4 byte address (0x02fa0020 in this case, high byte first), 1 byte length (0x10), the data to write to this memory address, 1 byte checksum (0x24 here) and 1 byte ACK (0x06). The radio will just answer with an ACK byte (0x06).
```
> 5702fa002010ffffffffffffffff00000000000000002406
< 06
```
The checksum is calculated the same way as in the read response. 1 byte sum over address, length and payload, but not over the "W" byte. Contrary to the read memory command it seems not to be possible to set other data length values than 16 (0x10). :angry:

### Leave programing session

Just send Ascii "END". The radio will respond with an ACK byte (0x06) and return to normal operation. If write commands have been sent to the radio, writing seems to start now.

```
> 454e44 (END)
< 06 ([ACK])
```
### Start Firmware Update

Boot radio in firmware receive mode (AT-D878UV: Hold PF3 (blue button on top) and PTT while switching on). Send Ascii "UPDATE". The radio will respond with an ACK byte (0x06).

```
> 555044415445 (UPDATE)
< 06
```
A "Read device identifier" query (see above) will follow.

### Send Firmware Update data

After 1 command byte = 0x01 ("FW" below), 4 bytes of memory address follow ("MAMAMAMA" below). The lowest byte is transmitted first! Then the complete .CDD file file will be transmitted in packets of 32 bytes ("." below). At the end of the file unused bytes will be padded by 0x00 to get 32 bytes of data. Then 2 bytes checksum follow ("CS" below). This is just a 2 byte sum of all bytes in memory address and data. The lowest byte is transmitted first! At the end of the packet an ACK byte (0x06) is send.

```
> 0100400008b83d0120e14b00082148000823480008274800082b4800082f48000800000000e70406
  FWMAMAMAMA................................................................CSCS06

MAMAMAMA = 00400008 => Memory adress is 0x08004000
CSCS = e704 => Checksum is 0x04e7
```

The radio will respond with a single ACK byte (0x06).

### End of Firmware Update

To finish the firmware transfer process 1 byte 0x18 is send to the radio. The radio will respond with a single ACK byte (0x06). To finally flash this image the radio has been switched on while pressing PF1 (AT-D878UV: top function key on the left side next to PTT) and PTT while switching on. In the following menu you can confirm flashing the device. Important: **All settings will be overwritten!** So **backup your code plug BEFORE updating the firmware"**

```
> 18
< 06
```
