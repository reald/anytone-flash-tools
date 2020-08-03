# AT878UV memory layout

* Observations done with firmware version 1.19. 

* **Observations and interpretations of memory dumps might be wrong. Use at your own risk!**

## ARPS

### General APRS Settings 0x02501000
```
57 | 02501000 | 10 | 00144800 001e0000 13003c00 00001700 | 52 06 || ..H. .... ..<. .... || ..H.......<..... ||
                       TFTFTF                AI     LA
57 | 02501010 | 10 | 00007100 00004150 41543831 00444c39 | 4b 06 || ..q. ..AP AT81 .DL9 || ..q...APAT81.DL9 ||
                         LO       DCDC DCDCDCDC DICSCSCS 
57 | 02501020 | 10 | 43415409 57494445 312d3157 49444532 | 86 06 || CAT. WIDE 1-1W IDE2 || CAT.WIDE1-1WIDE2 ||
                     CSCSCSID SPSPSPSP SPSPSPSP SPSPSPSP
57 | 02501030 | 10 | 2d310000 00000000 002f3e03 00000000 | 70 06 || -1.. .... ./>. .... || -1......./>..... ||
                     SPSP                STMIPW
57 | 02501040 | 10 | a20fa20f a20fa20f a20fa20f a20fa20f | 3a 06 || ¢.¢. ¢.¢. ¢.¢. ¢.¢. || ¢.¢.¢.¢.¢.¢.¢.¢. ||
57 | 02501050 | 10 | 00262999 00000000 00000000 00000000 | aa 06 || .&). .... .... .... || .&)............. ||
                       TGTGTG
57 | 02501060 | 10 | 00000000 00000000 00000000 00000000 | d2 06 || .... .... .... .... || ................ ||
57 | 02501070 | 10 | 00000000 00000000 00000000 00000000 | e2 06 || .... .... .... .... || ................ ||
57 | 02501080 | 10 | 00010000 00000000 00000000 00000000 | f3 06 || .... .... .... .... || ................ ||
57 | 02501090 | 10 | 00000000 00000000 00000000 00000000 | 02 06 || .... .... .... .... || ................ ||
=> Size: 0x2501000 .. 0x250109f: 160 bytes

- TF - Tx Frequency: BCD
- AI - APRS Auto TX Interval: 0 -> Off; 2 -> 60s; 255 -> 7650s
- LA - part of latitude
- LO - part of longitude
- DC - Destination Call Sign: ASCII
- DI - Destination SSID ??, 1 byte
- CS - Callsign, ASCII, max. 6 bytes ?
- ID - SSID: 1 byte ?
- SP - Signal Path: ASCII, max. 20 bytes in CPS
- ST - Symbol Table: 1 byte
- MI - Map Icon: 1 byte
- PW - TX Power: 00 -> Low: 01 -> Mid; 02 -> High; 03 -> Turbo ?
- TG - APRS TG

```

### APRS Sending Text 0x02501200
```
57 | 02501200 | 10 | 37332044 4520444c 39434154 00000000 | 48 06 || 73 D E DL 9CAT .... || 73 DE DL9CAT.... ||
57 | 02501210 | 10 | 00000000 00000000 00000000 00000000 | 84 06 || .... .... .... .... || ................ ||
57 | 02501220 | 10 | 00000000 00000000 00000000 00000000 | 94 06 || .... .... .... .... || ................ ||
57 | 02501230 | 10 | 00000000 00000000 00000000 00000000 | a4 06 || .... .... .... .... || ................ ||
=> Size: 0x2501200 .. 0x250123f: 64 bytes
```

CPS supports up to 60 Bytes sending text.

## Channel List

### 4000 Channels
```
57 | 00800000 | 10 | 14550000 00000000 04000000 11001100 | 1f 06 || .U.. .... .... .... || .U.............. ||
                     RFRFRFRF TOTOTOTO MMCTCECD DE  DDDD
57 | 00800010 | 10 | cf090000 07000000 00000005 ff000000 | 83 06 || Ï... .... .... ÿ... || Ï...........ÿ... ||
                     CCCC                SQBLSL
57 | 00800020 | 10 | 01000041 6e727566 20326d00 00000000 | 6c 06 || ...A nruf  2m. .... || ...Anruf 2m..... ||
                       WW  CN CNCNCNCN CNCNCNCN CNCNCNCN
57 | 00800030 | 10 | 00000000 00000000 0000ff00 00000000 | bf 06 || .... .... ..ÿ. .... || ..........ÿ..... ||
                     CNCN       AR       CO
                     
57 | 00800040 | 10 | 14547500 00000000 08000000 11001100 | d7 06 || .Tu. .... .... .... || .Tu............. ||
57 | 00800050 | 10 | cf090000 00000000 000000ff ff000000 | b6 06 || Ï... .... ...ÿ ÿ... || Ï..........ÿÿ... ||
57 | 00800060 | 10 | 0100004f 56204efc 726e6265 72672053 | f3 06 || ...O V Nü rnbe rg S || ...OV Nürnberg S ||
57 | 00800070 | 10 | fc640000 00000000 00000000 00000000 | 60 06 || üd.. .... .... .... || üd.............. ||

57 | 00800080 | 10 | 14565000 00060000 8400000d 11001100 | 83 06 || .VP. .... .... .... || .VP............. ||
57 | 00800090 | 10 | cf090000 07000000 000000ff ff000000 | fd 06 || Ï... .... ...ÿ ÿ... || Ï..........ÿÿ... ||
57 | 008000a0 | 10 | 01000044 4230554e 00000000 00000000 | 8a 06 || ...D B0UN .... .... || ...DB0UN........ ||
57 | 008000b0 | 10 | 00000000 00000000 00c4ff00 00000000 | 03 06 || .... .... .Äÿ. .... || .........Äÿ..... ||

- RF - RX Frequency, BCD, 4 bytes
- TO - TX Offset absolute, BCD 4 bytes
- MM - Bandwith, Power, A/D mode: SS?BPPTT
        S Sign: 01 -> TX offset to receive freq is positive; 10 -> TX offset to receive freq is negative
        B Bandwith: 1 for 25khz, 0 otherwise
        PP TX Power: 00 -> Low; 01 -> Mid; 10 -> High; 11 Turbo
        RR Channel Type: 00 -> A-Analog; 01 -> D-Digital; 10 -> A+D TX A; 11 -> D+A TX D
- CT - T?PREEDD
       T Talk Around: 0 -> unset; 1 -> set
       P PTT Prohibit: 0 -> unset; 1 -> set
       R Reverse (Swap TX/RX Freq)
       EE CTCSS/DCS Encode: 00 -> off; 01 -> CTCSS; 10 -> DCS
       DD CTCSS/DCS Decode: 00 -> off; 01 -> CTCSS; 10 -> DCS
- CE - CTCSS Encode Tone: 0x01 -> 67.0; 0x0f -> 107.2; 0x32 -> 254.1; 0x33 -> Custom
- CD - CTCSS Decode Tone: 0x01 -> 67.0; 0x32 -> 254.1; 0x33 -> Custom
- DE - DCS Encode Tone: 0x16 -> D026N; 0x18 -> D030N
- DD - DCS Decode Tone: 0x3ff -> D777i
- CC - Custom CTCSS: 2 byte, low byte first, resolution 1/10 Hz, 0x9cf = 2511 -> 255.1 Hz
- SQ - Bits ???S????
       S Squelch Mode: 0 -> Carrier; 1 -> CTCSS/DCS
- BL - ??????BB
       B Busy Lock: 00 -> off: 01 -> Repeater; 10 -> Busy
- SL - Scanlist: 0 -> Scanlist 1; 1 -> Scanlist 1; 0xff -> No Scanlist
- CD - CTCSS/DCS Decode as BCD ??
- WW - W???????
       W Work Alone: 0 -> unset; 1 -> set
- CN - Channel Name, ASCII, 15 bytes
- AR - ??????AA
       AA: APRS report type: 00 -> off; 01 -> analog; 10 -> digital
- CO - Freq Correction. 1 byte signed char; 10 Hz steps. 0x84 -> -1240 Hz; 0x7d -> 1250 Hz; -1250..1250 Hz range 
```

Start at 0x00800000, 64 byte per Channel.

Other Expected Values: "Contact","Contact Call Type","Contact TG/DMR ID","Radio ID","Busy Lock/TX Permit","Optional Signal","DTMF ID","2Tone ID","5Tone ID","PTT ID","Color Code","Slot","Receive Group List","Simplex TDMA","TDMA Adaptive","AES Digital Encryption","Digital Encryption","Call Confirmation","2TONE Decode","Ranging","Through Mode","Digi APRS RX","Analog APRS PTT Mode","Digital APRS PTT Mode","Digital APRS Report Channel","SMS Confirmation","Exclude channel from roaming","DMR MODE"



### VFO Frequencies 0x00fc0800
```
57 | 00fc0800 | 10 | 43350000 00000000 08000909 00000000 | a6 06 || C5.. .... .... .... || C5.............. ||
57 | 00fc0810 | 10 | 26050000 07000000 000000ff 00000000 | 55 06 || &... .... ...ÿ .... || &..........ÿ.... ||
57 | 00fc0820 | 10 | 01030043 68616e6e 656c2056 464f2041 | 5d 06 || ...C hann el V FO A || ...Channel VFO A ||
57 | 00fc0830 | 10 | 00000000 00000000 0000ff00 00000000 | 43 06 || .... .... ..ÿ. .... || ..........ÿ..... ||

57 | 00fc0840 | 10 | 14550000 00000000 08000606 00000000 | d1 06 || .U.. .... .... .... || .U.............. ||
57 | 00fc0850 | 10 | 26050000 07000000 000000ff 00000000 | 95 06 || &... .... ...ÿ .... || &..........ÿ.... ||
57 | 00fc0860 | 10 | 01020043 68616e6e 656c2056 464f2042 | 9d 06 || ...C hann el V FO B || ...Channel VFO B ||
57 | 00fc0870 | 10 | 00000000 00000000 0000ff00 00000000 | 83 06 || .... .... ..ÿ. .... || ..........ÿ..... ||
=> Size: 0xfc0800 .. 0xfc087f: 128 bytes
```
Layout same as 4000 channels. (?)

## Digital contact list

For managing the digital contact list 3 memory parts are used. The first part starting at 0x04000000 contains information about the digital radio ID (and the call type) and an memory offset to the contact list. Part 2 only hosts the number of contact list entries and a pointer to the next free contact list memory address.
Part 3 contains the contact list with all information (ID, Callsign, Name, City, ...).

### Part 1: Contact offsets (used for writing contacts)

One entry contains the BCD coded radio ID shifted left by 1 bit in the first 4 bytes (low byte first). The free lowest bit will be 1 for group calls and 0 for private calls. The next four bytes are the memory offset to the contact list (low byte first) stored in Part 3. 

Example:
```
0x04000000: 22010000 00000000 24010000 63000000 
0x04000010: 26010000 c6000000 28010000 29010000

22010000 => 0x122. Lowest bit is 0 so we have a private call type. Shift 0x122 1 bit down => 0x91 This is the radio ID as BCD.
The next four bytes are 0 the contact list memory offset for this entry is 0.

24010000 => 0x124. Lowest bit is 0 so we have a private call type. Shift 0x124 1 bit down => 0x92 This is the radio ID as BCD.
The next four bytes are 0x00000063 so the contact list entry for the first entry was 99 bytes long.

```

So for every entry in the contact list 8 bytes are stored in this memory part. One after each other. But the memory is partitioned in multiple sections with gaps in between:

~~~
memSectContactsOffsetWrite = [
   { 'address' : 0x4000000, 'size' : 128000},
   { 'address' : 0x4040000, 'size' : 128000},
   { 'address' : 0x4080000, 'size' : 128000},
   { 'address' : 0x40C0000, 'size' : 128000},
   { 'address' : 0x4100000, 'size' : 128000},
   { 'address' : 0x4140000, 'size' : 128000},
   { 'address' : 0x4180000, 'size' : 128000},
   { 'address' : 0x41C0000, 'size' : 128000},
   { 'address' : 0x4200000, 'size' : 128000},
   { 'address' : 0x4240000, 'size' : 128000},
   { 'address' : 0x4280000, 'size' : 128000},
   { 'address' : 0x42c0000, 'size' : 128000},
   { 'address' : 0x4300000, 'size' : 64000} # maybe more. at least 64000 bytes seen
]
~~~
So when reaching address 0x401F3FF (0x4000000 + 128000 dec) storing these data will be continued in the next section beginning at 0x4040000.

### Part 2: Index 044c0000
This section only contains 4 bytes with the total number of stored contacts (low byte first) and the relative memory address to the next free contact list entry.

```
0x044c0000: 400d0300 00006807 00000000 00000000

0x00030d40 => 200000 entries
Next free entry at memory address 0x07680000
```

### Part 3: Contact list

In this block beginning at address 0x04500000 the contact information for every contact is stored:

```
         00167764 15023939 39393939 39393939 || ..wd ..99 9999 9999 || ..wd..9999999999 ||
         CTIDIDID IDCANANA NANANANA NANANANA

         39393939 39390063 69747900 63616c6c || 9999 99.c ity. call || 999999.city.call ||
         NANANANA NANA00CI CICICI00 CSCSCSCS

         7369676e 00737461 74657072 6f760063 || sign .sta tepr ov.c || sign.stateprov.c ||
         CSCSCSCS 00SPSPSP SPSPSPSP SPSP00CO

         6f756e74 72790072 656d6172 6b7300 || ount ry.r emar ks.. || ountry.remarks. ||
         COCOCOCO COCO00RE RERERERE RERE00
         
         - CT: Call Type: 00 -> Private Call, 01 -> Group Call, 02 -> "All" (only once possible), 1 byte
         - ID: TG/DMRID as BCD, 4 bytes
         - CA: Call Alert. 00 -> none, 01 -> Ring, 02 -> Online Alert
         - NA: Name. ASCII, 0 terminated, max 16 bytes
         - CI: City. ASCII, 0 terminated, max 15 bytes
         - CS: Callsign, ASCII, 0 terminated, max. 8 bytes
         - SP: State/Prov, ASCII, 0 terminated, max. 16 bytes
         - CO: Country, ASCII, 0 terminated, max. 16 bytes
         - RE: Remarks, 0 terminated, max. 16 bytes

```
After one data set the next follows immediately. As in block 1 the memory is partitioned in multiple sections with gaps in between. The memory offset described in part 1 does not care about the gaps it only belongs to the relative offset in the valid memory sections.
```
memSectContacts = [
   { 'address' : 0x4500000, 'size' : 100000},
   { 'address' : 0x4540000, 'size' : 100000},
   { 'address' : 0x4580000, 'size' : 100000},
   { 'address' : 0x45c0000, 'size' : 100000},
   { 'address' : 0x4600000, 'size' : 100000},
   { 'address' : 0x4640000, 'size' : 100000},
   { 'address' : 0x4680000, 'size' : 100000},
   { 'address' : 0x46c0000, 'size' : 100000},
   { 'address' : 0x4700000, 'size' : 100000},
   { 'address' : 0x4740000, 'size' : 100000},
   { 'address' : 0x4780000, 'size' : 100000},
   { 'address' : 0x47c0000, 'size' : 100000},
   { 'address' : 0x4800000, 'size' : 100000},
   { 'address' : 0x4840000, 'size' : 100000},
   { 'address' : 0x4880000, 'size' : 100000},
   { 'address' : 0x48c0000, 'size' : 100000},
   { 'address' : 0x4900000, 'size' : 100000},
   { 'address' : 0x4940000, 'size' : 100000},
   { 'address' : 0x4980000, 'size' : 100000},
   { 'address' : 0x49c0000, 'size' : 100000},
   { 'address' : 0x4a00000, 'size' : 100000},
   { 'address' : 0x4a40000, 'size' : 100000},
   { 'address' : 0x4a80000, 'size' : 100000},
   { 'address' : 0x4ac0000, 'size' : 100000},
   { 'address' : 0x4b00000, 'size' : 100000},
   { 'address' : 0x4b40000, 'size' : 100000},
   { 'address' : 0x4b80000, 'size' : 100000},
   { 'address' : 0x4bc0000, 'size' : 100000},
   { 'address' : 0x4c00000, 'size' : 100000},
   { 'address' : 0x4c40000, 'size' : 100000},
   { 'address' : 0x4c80000, 'size' : 100000},
   { 'address' : 0x4cc0000, 'size' : 100000},
   { 'address' : 0x4d00000, 'size' : 100000},
   { 'address' : 0x4d40000, 'size' : 100000},
   { 'address' : 0x4d80000, 'size' : 100000},
   { 'address' : 0x4dc0000, 'size' : 100000},
   { 'address' : 0x4e00000, 'size' : 100000},
   { 'address' : 0x4e40000, 'size' : 100000},
   { 'address' : 0x4e80000, 'size' : 100000},
   { 'address' : 0x4ec0000, 'size' : 100000},
   { 'address' : 0x4f00000, 'size' : 100000},
   { 'address' : 0x4f40000, 'size' : 100000},
   { 'address' : 0x4f80000, 'size' : 100000},
   { 'address' : 0x4fc0000, 'size' : 100000},
   { 'address' : 0x5000000, 'size' : 100000},
   { 'address' : 0x5040000, 'size' : 100000},
   { 'address' : 0x5080000, 'size' : 100000},
   { 'address' : 0x50c0000, 'size' : 100000},
   { 'address' : 0x5100000, 'size' : 100000},
   { 'address' : 0x5140000, 'size' : 100000},
   { 'address' : 0x5180000, 'size' : 100000},
   { 'address' : 0x51c0000, 'size' : 100000},
   { 'address' : 0x5200000, 'size' : 100000},
   { 'address' : 0x5240000, 'size' : 100000},
   { 'address' : 0x5280000, 'size' : 100000},
   { 'address' : 0x52c0000, 'size' : 100000},
   { 'address' : 0x5300000, 'size' : 100000},
   { 'address' : 0x5340000, 'size' : 100000},
   { 'address' : 0x5380000, 'size' : 100000},
   { 'address' : 0x53c0000, 'size' : 100000},
   { 'address' : 0x5400000, 'size' : 100000},
   { 'address' : 0x5440000, 'size' : 100000},
   { 'address' : 0x5480000, 'size' : 100000},
   { 'address' : 0x54c0000, 'size' : 100000},
   { 'address' : 0x5500000, 'size' : 100000},
   { 'address' : 0x5540000, 'size' : 100000},
   { 'address' : 0x5580000, 'size' : 100000},
   { 'address' : 0x55c0000, 'size' : 100000},
   { 'address' : 0x5600000, 'size' : 100000},
   { 'address' : 0x5640000, 'size' : 100000},
   { 'address' : 0x5680000, 'size' : 100000},
   { 'address' : 0x56c0000, 'size' : 100000},
   { 'address' : 0x5700000, 'size' : 100000},
   { 'address' : 0x5740000, 'size' : 100000},
   { 'address' : 0x5780000, 'size' : 100000},
   { 'address' : 0x57c0000, 'size' : 100000},
   { 'address' : 0x5800000, 'size' : 100000},
   { 'address' : 0x5840000, 'size' : 100000},
   { 'address' : 0x5880000, 'size' : 100000},
   { 'address' : 0x58c0000, 'size' : 100000},
   { 'address' : 0x5900000, 'size' : 100000},
   { 'address' : 0x5940000, 'size' : 100000},
   { 'address' : 0x5980000, 'size' : 100000},
   { 'address' : 0x59c0000, 'size' : 100000},
   { 'address' : 0x5a00000, 'size' : 100000},
   { 'address' : 0x5a40000, 'size' : 100000},
   { 'address' : 0x5a80000, 'size' : 100000},
   { 'address' : 0x5ac0000, 'size' : 100000},
   { 'address' : 0x5b00000, 'size' : 100000},
   { 'address' : 0x5b40000, 'size' : 100000},
   { 'address' : 0x5b80000, 'size' : 100000},
   { 'address' : 0x5bc0000, 'size' : 100000},
   { 'address' : 0x5c00000, 'size' : 100000},
   { 'address' : 0x5c40000, 'size' : 100000},
   { 'address' : 0x5c80000, 'size' : 100000},
   { 'address' : 0x5cc0000, 'size' : 100000},
   { 'address' : 0x5d00000, 'size' : 100000},
   { 'address' : 0x5d40000, 'size' : 100000},
   { 'address' : 0x5d80000, 'size' : 100000},
   { 'address' : 0x5dc0000, 'size' : 100000},
   { 'address' : 0x5e00000, 'size' : 100000},
   { 'address' : 0x5e40000, 'size' : 100000},
   { 'address' : 0x5e80000, 'size' : 100000},
   { 'address' : 0x5ec0000, 'size' : 100000},
   { 'address' : 0x5f00000, 'size' : 100000},
   { 'address' : 0x5f40000, 'size' : 100000},
   { 'address' : 0x5f80000, 'size' : 100000},
   { 'address' : 0x5fc0000, 'size' : 100000},
   { 'address' : 0x6000000, 'size' : 100000},
   { 'address' : 0x6040000, 'size' : 100000},
   { 'address' : 0x6080000, 'size' : 100000},
   { 'address' : 0x60c0000, 'size' : 100000},
   { 'address' : 0x6100000, 'size' : 100000},
   { 'address' : 0x6140000, 'size' : 100000},
   { 'address' : 0x6180000, 'size' : 100000},
   { 'address' : 0x61c0000, 'size' : 100000},
   { 'address' : 0x6200000, 'size' : 100000},
   { 'address' : 0x6240000, 'size' : 100000},
   { 'address' : 0x6280000, 'size' : 100000},
   { 'address' : 0x62c0000, 'size' : 100000},
   { 'address' : 0x6300000, 'size' : 100000},
   { 'address' : 0x6340000, 'size' : 100000},
   { 'address' : 0x6380000, 'size' : 100000},
   { 'address' : 0x63c0000, 'size' : 100000},
   { 'address' : 0x6400000, 'size' : 100000},
   { 'address' : 0x6440000, 'size' : 100000},
   { 'address' : 0x6480000, 'size' : 100000},
   { 'address' : 0x64c0000, 'size' : 100000},
   { 'address' : 0x6500000, 'size' : 100000},
   { 'address' : 0x6540000, 'size' : 100000},
   { 'address' : 0x6580000, 'size' : 100000},
   { 'address' : 0x65c0000, 'size' : 100000},
   { 'address' : 0x6600000, 'size' : 100000},
   { 'address' : 0x6640000, 'size' : 100000},
   { 'address' : 0x6680000, 'size' : 100000},
   { 'address' : 0x66c0000, 'size' : 100000},
   { 'address' : 0x6700000, 'size' : 100000},
   { 'address' : 0x6740000, 'size' : 100000},
   { 'address' : 0x6780000, 'size' : 100000},
   { 'address' : 0x67c0000, 'size' : 100000},
   { 'address' : 0x6800000, 'size' : 100000},
   { 'address' : 0x6840000, 'size' : 100000},
   { 'address' : 0x6880000, 'size' : 100000},
   { 'address' : 0x68c0000, 'size' : 100000},
   { 'address' : 0x6900000, 'size' : 100000},
   { 'address' : 0x6940000, 'size' : 100000},
   { 'address' : 0x6980000, 'size' : 100000},
   { 'address' : 0x69c0000, 'size' : 100000},
   { 'address' : 0x6a00000, 'size' : 100000},
   { 'address' : 0x6a40000, 'size' : 100000},
   { 'address' : 0x6a80000, 'size' : 100000},
   { 'address' : 0x6ac0000, 'size' : 100000},
   { 'address' : 0x6b00000, 'size' : 100000},
   { 'address' : 0x6b40000, 'size' : 100000},
   { 'address' : 0x6b80000, 'size' : 100000},
   { 'address' : 0x6bc0000, 'size' : 100000},
   { 'address' : 0x6c00000, 'size' : 100000},
   { 'address' : 0x6c40000, 'size' : 100000},
   { 'address' : 0x6c80000, 'size' : 100000},
   { 'address' : 0x6cc0000, 'size' : 100000},
   { 'address' : 0x6d00000, 'size' : 100000},
   { 'address' : 0x6d40000, 'size' : 100000},
   { 'address' : 0x6d80000, 'size' : 100000},
   { 'address' : 0x6dc0000, 'size' : 100000},
   { 'address' : 0x6e00000, 'size' : 100000},
   { 'address' : 0x6e40000, 'size' : 100000},
   { 'address' : 0x6e80000, 'size' : 100000},
   { 'address' : 0x6ec0000, 'size' : 100000},
   { 'address' : 0x6f00000, 'size' : 100000},
   { 'address' : 0x6f40000, 'size' : 100000},
   { 'address' : 0x6f80000, 'size' : 100000},
   { 'address' : 0x6fc0000, 'size' : 100000},
   { 'address' : 0x7000000, 'size' : 100000},
   { 'address' : 0x7040000, 'size' : 100000},
   { 'address' : 0x7080000, 'size' : 100000},
   { 'address' : 0x70c0000, 'size' : 100000},
   { 'address' : 0x7100000, 'size' : 100000},
   { 'address' : 0x7140000, 'size' : 100000},
   { 'address' : 0x7180000, 'size' : 100000},
   { 'address' : 0x71c0000, 'size' : 100000},
   { 'address' : 0x7200000, 'size' : 100000},
   { 'address' : 0x7240000, 'size' : 100000},
   { 'address' : 0x7280000, 'size' : 100000},
   { 'address' : 0x72c0000, 'size' : 100000},
   { 'address' : 0x7300000, 'size' : 100000},
   { 'address' : 0x7340000, 'size' : 100000},
   { 'address' : 0x7380000, 'size' : 100000},
   { 'address' : 0x73c0000, 'size' : 100000},
   { 'address' : 0x7400000, 'size' : 100000},
   { 'address' : 0x7440000, 'size' : 100000},
   { 'address' : 0x7480000, 'size' : 100000},
   { 'address' : 0x74c0000, 'size' : 100000},
   { 'address' : 0x7500000, 'size' : 100000},
   { 'address' : 0x7540000, 'size' : 100000},
   { 'address' : 0x7580000, 'size' : 100000},
   { 'address' : 0x75c0000, 'size' : 100000},
   { 'address' : 0x7600000, 'size' : 100000},
   { 'address' : 0x7640000, 'size' : 100000},
   { 'address' : 0x7680000, 'size' : 16}, # maybe more. at least 16 bytes seen
]
```
