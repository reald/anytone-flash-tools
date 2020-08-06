# AT878UV memory layout

* Observations done with firmware version 1.19. 

* **Observations and interpretations of memory dumps might be wrong. Use at your own risk!**

* Single memory sections cannot be written alone!

## ARPS

### General APRS Settings 0x02501000
```
57 | 02501000 | 10 | 00144800 001e0000 13003c00 00001700 | 52 06 || ..H. .... ..<. .... || ..H.......<..... ||
                       TFTFTF TFTDSTCT DC  MIAI TTFBLALA
57 | 02501010 | 10 | 00007100 00004150 41543831 00444c39 | 4b 06 || ..q. ..AP AT81 .DL9 || ..q...APAT81.DL9 ||
                     LALALOLO LOLODCDC DCDCDCDC DICSCSCS 
57 | 02501020 | 10 | 43415409 57494445 312d3157 49444532 | 86 06 || CAT. WIDE 1-1W IDE2 || CAT.WIDE1-1WIDE2 ||
                     CSCSCSID SPSPSPSP SPSPSPSP SPSPSPSP
57 | 02501030 | 10 | 2d310000 00000000 002f3e03 00000000 | 70 06 || -1.. .... ./>. .... || -1......./>..... ||
                     SPSP                STMIPW PT    ??
57 | 02501040 | 10 | a20fa20f a20fa20f a20fa20f a20fa20f | 3a 06 || ¢.¢. ¢.¢. ¢.¢. ¢.¢. || ¢.¢.¢.¢.¢.¢.¢.¢. ||
                     RCRCRCRC RCRCRCRC RCRCRCRC RCRCRCRC
57 | 02501050 | 10 | 00262999 00000000 00000000 00000000 | aa 06 || .&). .... .... .... || .&)............. ||
                     TGTGTGTG TGTGTGTG TGTGTGTG TGTGTGTG
57 | 02501060 | 10 | 00000000 00000000 00000000 00000000 | d2 06 || .... .... .... .... || ................ ||
                     TGTGTGTG TGTGTGTG TGTGTGTG TGTGTGTG
57 | 02501070 | 10 | 00000000 00000000 00000000 00000000 | e2 06 || .... .... .... .... || ................ ||
                     CTCTCTCT CTCTCTCT ROSLSLSL SLSLSLSL
57 | 02501080 | 10 | 00010000 00000000 00000000 00000000 | f3 06 || .... .... .... .... || ................ ||
                     SLRD
57 | 02501090 | 10 | 00000000 00000000 00000000 00000000 | 02 06 || .... .... .... .... || ................ ||
=> Size: 0x2501000 .. 0x250109f: 160 bytes

- TF - Tx Frequency: BCD (4 bytes)
- TD - Transmit Delay: 1 byte, 0x00 -> off, 0x03 -> 60ms, 0xff 5100ms. Transmit Delay = value * 20ms 
- ST - Send Sub Tone: 1 byte 0x00 -> off, 0x01 -> CTCSS, 0x02 -> DCS
- CT - CTCSS: 1 byte 0x00-> 62.5, 0x03 -> 71.9 Hz. Todo: complete list
- DC - DCS: 1 byte: 0x13 -> D023. Todo: complete list
- AI - Manual TX Interval: 0x00 -> 0; 0xff -> 255s
- AI - APRS Auto TX Interval: 0 -> Off; 2 -> 60s; 255 -> 7650s
- FB - Fixed location beacon: 0x00 -> Off (GPS), 0x01 -> On (send fix position) ?
- LA - latitude: 1 byte degree, 1 byte minute, 1 byte minute fraction, 1 byte sign (0 -> N, 1 -> S)
- TT - ARPS Tx Tone: 0x00 -> off, 0x01 -> on
- LO - longitude: 1 byte degree, 1 byte minute, 1 byte minute fraction, 1 byte sign (0 -> E, 1 -> W)
- DC - Destination Call Sign: ASCII
- DI - Destination SSID, 1 byte
- CS - Your Callsign, ASCII, max. 6 bytes
- ID - SSID: 1 byte
- SP - ARPS Signal Path: ASCII, max. 20 bytes in CPS
- ST - Symbol Table: 1 byte
- MI - Map Icon: 1 byte
- PW - TX Power: 00 -> Low: 01 -> Mid; 02 -> High; 03 -> Turbo
- PT - Prewave Time: 1 byte, Prewave Time = value * 10ms
- ?? - WHAT IS THIS BYTE USED FOR? 0x00 and 0xff seen!
- RC - Report Channel 1-8: 2 bytes per channel, 0xfa2 = 4002 -> Current Channel, other values point to channel list (use digital channels only)
- TG - APRS TG 1-8: BCD coded, 4 bytes each, one after another
- CT - Call Type 1-8: 0x00 -> Private Call, 0x01 -> Group Call, 0x?? -> All Call; 1 byte each, one after another
- RO - Support for Roaming: 0x00 -> off, 0x01 -> on
- SL - Slot 1-8: 0x00 -> Channel Slot, 0x01 -> Slot 1, 0x02 -> Slot 2, 1 byte, one after another
- RD - Repeater Activation Delay: 0x00 -> off, 0x01 -> 100ms, 0x03 -> 300ms, 0x10 -> 1000ms
```

Other expected values: "APRS TG","Call Type"



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

### 4000 Channels + 2 VFO
```
57 | 00800000 | 10 | 14550000 00000000 04000000 11001100 | 1f 06 || .U.. .... .... .... || .U.............. ||
                     RFRFRFRF TOTOTOTO MMCTCECD DEDEDDDD
57 | 00800010 | 10 | cf090000 07000000 00000005 ff000000 | 83 06 || Ï... .... .... ÿ... || Ï...........ÿ... ||
                     CCCC     CI       RISQBLSL RG2T5TDT
57 | 00800020 | 10 | 01000041 6e727566 20326d00 00000000 | 6c 06 || ...A nruf  2m. .... || ...Anruf 2m..... ||
                     CLWWAKCN CNCNCNCN CNCNCNCN CNCNCNCN
57 | 00800030 | 10 | 00000000 00000000 0000ff00 00000000 | bf 06 || .... .... ..ÿ. .... || ..........ÿ..... ||
                     CNCNCN   EXARAPDP DRCOENKK
                     
57 | 00800040 | 10 | 14547500 00000000 08000000 11001100 | d7 06 || .Tu. .... .... .... || .Tu............. ||
57 | 00800050 | 10 | cf090000 00000000 000000ff ff000000 | b6 06 || Ï... .... ...ÿ ÿ... || Ï..........ÿÿ... ||
57 | 00800060 | 10 | 0100004f 56204efc 726e6265 72672053 | f3 06 || ...O V Nü rnbe rg S || ...OV Nürnberg S ||
57 | 00800070 | 10 | fc640000 00000000 00000000 00000000 | 60 06 || üd.. .... .... .... || üd.............. ||

[...]

57 | 00fc0800 | 10 | 43350000 00000000 08000909 00000000 | a6 06 || C5.. .... .... .... || C5.............. ||
57 | 00fc0810 | 10 | 26050000 07000000 000000ff 00000000 | 55 06 || &... .... ...ÿ .... || &..........ÿ.... ||
57 | 00fc0820 | 10 | 01030043 68616e6e 656c2056 464f2041 | 5d 06 || ...C hann el V FO A || ...Channel VFO A ||
57 | 00fc0830 | 10 | 00000000 00000000 0000ff00 00000000 | 43 06 || .... .... ..ÿ. .... || ..........ÿ..... ||

57 | 00fc0840 | 10 | 14550000 00000000 08000606 00000000 | d1 06 || .U.. .... .... .... || .U.............. ||
57 | 00fc0850 | 10 | 26050000 07000000 000000ff 00000000 | 95 06 || &... .... ...ÿ .... || &..........ÿ.... ||
57 | 00fc0860 | 10 | 01020043 68616e6e 656c2056 464f2042 | 9d 06 || ...C hann el V FO B || ...Channel VFO B ||
57 | 00fc0870 | 10 | 00000000 00000000 0000ff00 00000000 | 83 06 || .... .... ..ÿ. .... || ..........ÿ..... ||

- RF - RX Frequency, BCD, 4 bytes
- TO - TX Offset absolute, BCD 4 bytes
- MM - Bandwith, Power, A/D mode: SS?BPPTT
        S Sign: 01 -> TX offset to receive freq is positive; 10 -> TX offset to receive freq is negative
        B Bandwith: 1 for 25khz, 0 otherwise
        PP TX Power: 00 -> Low; 01 -> Mid; 10 -> High; 11 Turbo
        RR Channel Type: 00 -> A-Analog; 01 -> D-Digital; 10 -> A+D TX A; 11 -> D+A TX D
- CT - TCPREEDD
       T Talk Around: 0 -> unset; 1 -> set
       C Call Confirmation: 0 -> unset; 1 -> set
       P PTT Prohibit: 0 -> unset; 1 -> set
       R Reverse (Swap TX/RX Freq)
       EE CTCSS/DCS Encode: 00 -> off; 01 -> CTCSS; 10 -> DCS
       DD CTCSS/DCS Decode: 00 -> off; 01 -> CTCSS; 10 -> DCS
- CE - CTCSS Encode Tone: 0x01 -> 67.0; 0x0f -> 107.2; 0x32 -> 254.1; 0x33 -> Custom
- CD - CTCSS Decode Tone: 0x01 -> 67.0; 0x32 -> 254.1; 0x33 -> Custom
- DE - DCS Encode Tone: 0x0016 -> D026N; 0x0018 -> D030N; 0x03fe -> D776i
- DD - DCS Decode Tone: 0x03ff -> D777i
- CC - Custom CTCSS: 2 byte, low byte first, resolution 1/10 Hz, 0x9cf = 2511 -> 255.1 Hz
- CI - Contact Identifier
- RI - Radio ID
- SQ - Bits ???S??PI
       S Squelch Mode: 0 -> Carrier; 1 -> CTCSS/DCS
       PI PTT ID: 00 -> off; 01 -> Start; 10 -> End; 11 -> Start+End
- BL - ??OO??BB
       OO Optional Signal: 00 -> off; 01 -> DTMF; 10 -> 2Tone; 11 -> 5Tone
       BB Busy Lock/TX Permit: 00 -> off: 01 -> Repeater; 10 -> Busy
- SL - Scanlist: 0 -> Scanlist 1; 1 -> Scanlist 1; 0xff -> No Scanlist
- RG - Receive Group List: 0 -> Group 1; ... 249 -> Group 250; 0xff -> None
- 2T - 2Tone ID: 0 -> 1; 1 -> 2, ...
- 5T - 5Tone ID: 0 -> 1; 1 -> 2, ...
- DT - DTMF ID: 0 -> 1; 1 -> 2, ...
- CL - Color Code: 0x01 -> 1; 0x0f -> 15
- WW - W??A?DCS
       W Work Alone: 0 -> unset; 1 -> set
       A TDMA Adaption: 0 -> unset; 1 -> set
       D DMR Mode Double Slot: 0 -> unset; 1 -> set
       C SMS Confirmation: 0 -> unset; 1 -> set
       S Slot: 0 -> Slot 1; 1 -> Slot 2
- AK   AES Digital Encryption: 0x00 -> off
- CN - Channel Name, ASCII, 16 bytes
- EX - ?????ESR
       E Exclude channel from roaming: 0 -> off; 1 -> on
       S DMR Mode: Simplex or double slot???
       R Ranging: 0 -> unset; 1 -> set
- AR - ??????AA
       AA: APRS report type: 00 -> off; 01 -> analog; 10 -> digital
- AP:  Analog APRS PTT Mode: 0x00 -> off; 0x01 -> Start of Transmission; 0x02 -> End of Transmission
- DP:  Digital APRS PTT Mode: 00 -> off; 01 -> on ??
- DR - Digital APRS Report Channel: 0x00 -> off; 0x01 -> 1
- CO - Freq Correction. 1 byte signed char; 10 Hz steps. 0x84 -> -1240 Hz; 0x7d -> 1250 Hz; -1250..1250 Hz range
- EN - Digital Encryption: 0xff -> None; 0x20 -> 32
- KK - ?????SRM
       S SMS Forbid: 0 -> off; 1 -> on
       R Random key: 0 -> off; 1 -> on
       M Multiple Key: 0 -> off; 1 -> on

Other Expected Values: "Contact Call Type","Through Mode","Digi APRS RX"

Some IDs/values refer to other lists!

```

Start at 0x00800000, 64 byte per Channel, one channel after each other. As seen on other data the memory is partitioned in multiple sections and has gaps in between.

```
memSectChannels = [
   { 'address' : 0x800000, 'size' : 8192 },
   { 'address' : 0x840000, 'size' : 8192 },
   { 'address' : 0x880000, 'size' : 8192 },
   { 'address' : 0x8c0000, 'size' : 8192 },
   { 'address' : 0x900000, 'size' : 8192 },
   { 'address' : 0x940000, 'size' : 8192 },
   { 'address' : 0x980000, 'size' : 8192 },
   { 'address' : 0x9c0000, 'size' : 8192 },
   { 'address' : 0xa00000, 'size' : 8192 },
   { 'address' : 0xa40000, 'size' : 8192 },
   { 'address' : 0xa80000, 'size' : 8192 },
   { 'address' : 0xac0000, 'size' : 8192 },
   { 'address' : 0xb00000, 'size' : 8192 },
   { 'address' : 0xb40000, 'size' : 8192 },
   { 'address' : 0xb80000, 'size' : 8192 },
   { 'address' : 0xbc0000, 'size' : 8192 },
   { 'address' : 0xc00000, 'size' : 8192 },
   { 'address' : 0xc40000, 'size' : 8192 },
   { 'address' : 0xc80000, 'size' : 8192 },
   { 'address' : 0xcc0000, 'size' : 8192 },
   { 'address' : 0xd00000, 'size' : 8192 },
   { 'address' : 0xd40000, 'size' : 8192 },
   { 'address' : 0xd80000, 'size' : 8192 },
   { 'address' : 0xdc0000, 'size' : 8192 },
   { 'address' : 0xe00000, 'size' : 8192 },
   { 'address' : 0xe40000, 'size' : 8192 },
   { 'address' : 0xe80000, 'size' : 8192 },
   { 'address' : 0xec0000, 'size' : 8192 },
   { 'address' : 0xf00000, 'size' : 8192 },
   { 'address' : 0xf40000, 'size' : 8192 },
   { 'address' : 0xf80000, 'size' : 8192 },
   { 'address' : 0xfc0000, 'size' : 2176 }
]
```

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

### Part 2: Index at 0x044c0000
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
