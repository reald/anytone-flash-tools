# AT878UV Protocol

Note: All investigations have been done with firmware version 1.19.

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
The checksum is calculated the same way as in the read response. 1 byte sum over address, length and payload, but not over the "W" byte. Contrary the the read memory command it seems not to be possible to set other data length values than 16 (0x10). :angry:

### Leave programing session

Just send Ascii "END". The radio will respond with an ACK byte (0x06) and return to normal operation. If write commands have been sent to the radio, writing seems to start now.

```
> 454e44 (END)
< 06 ([ACK])
```


