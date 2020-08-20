# AT878UV memory layout

* Observations done with firmware version 1.19. 

* **Observations and interpretations of memory dumps might be wrong. Use at your own risk!**

* Single memory sections cannot be written alone!

# "Other info"

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
- SL - Scanlist: 0 -> Scanlist 1; 1 -> Scanlist 2; 0xff -> No Scanlist
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
- DP:  Digital APRS PTT Mode: 00 -> off; 01 -> on
- DR - Digital APRS Report Channel: 0x00 -> off; 0x01 -> 1
- CO - Freq Correction. 1 byte signed char; 10 Hz steps. 0x84 -> -1240 Hz; 0x7d -> 1250 Hz; -1250..1250 Hz range
- EN - Digital Encryption: 0xff -> None; 0x20 -> 32
- KK - ?????SRM
       S SMS Forbid: 0 -> off; 1 -> on
       R Random key: 0 -> off; 1 -> on
       M Multiple Key: 0 -> off; 1 -> on


Some IDs/values refer to other lists!

```

Start at 0x00800000, 64 bytes per Channel, one channel after each other. 
As seen on other data the memory is partitioned in multiple sections and has gaps in between.

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

## Zone (0x01000000) 

Here are the list of a zone stored. For every of the 250 zones are 512 byte memory reserved which contains up to 250 2-byte channel identifiers.
The start adresse if a zone is calculated 0x0100000 + 512 * [zonenumber].

```
57 | 01002800 | 10 | 00000300 22002300 24002500 26002700 | 17 06 || .... ".#. $.%. &.'. || ....".#.$.%.&.'. ||
                     I001I002 ID03...

[...]

57 | 010029f0 | 10 | 2c012d01 ffffffff ffffffff ffffffff | 79 06 || ,.-. ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ,.-.ÿÿÿÿÿÿÿÿÿÿÿÿ ||
                     I249I250

  - Ixxx - ID: 2 bytes, low byte first, channel id. 0xffffffff for unused space.
```
Empty zones will not be written.


## Roaming Channels (0x01040000)

Each entry has 32 bytes and start at 0x01040000 + 32 * [id number]. 

```
57 | 01040000 | 10 | 44000000 43990000 0201526f 616d2043 | 2a 06 || D... C... ..Ro am C || D...C.....Roam C ||
                     RXRXRXRX TXTXTXTX CCSLNANA NANANANA
57 | 01040010 | 10 | 68616e6e 656c2031 00000000 00000000 | ec 06 || hann el 1 .... .... || hannel 1........ ||
                     NANANANA NANANANA NANA

   - RX - RX Frequency: 4 bytes, BCD Coded, resolution 10 Hz.
   - TX - TX Frequency: 4 bytes, BCD Coded, resolution 10 Hz.
   - CC - Color Code: 1 byte, range 0 (0x00).. 15 (0x0f), 16 (0x10) -> No Use
   - SL - Slot: 0x00 -> Slot 1, 0x01 -> Slot 2, 0x02 -> No Use
   - NA - Name: ASCII, max 16 byte, unused characters are 0x00.
```

Empty entries will not be written.

## Roaming Channels used (0x01042000)

1 bit for every used channel. 0 -> channel is free, 1 -> channel in use. Max. 250 channels.

```
57 | 01042000 | 10 | 01000000 00000000 00000000 00000000 | 36 06 || .... .... .... .... || ................ ||
57 | 01042010 | 10 | 00000000 00000000 00000000 00000002 | 47 06 || .... .... .... .... || ................ ||

In this example the first channel is used (first bit in first byte is 1) and the last one (250) is used (8bit/byte*4byte)*7 + (3byte*8bit/byte) + 2.

```

## Roaming Zones used (0x01042080)

1 bit for every used zone. 0 -> zone is free, 1 -> zone in use. Max. 64 zones.
```
57 | 01042080 | 10 | 09000000 00000080 00000000 00000000 | 3e 06 || .... .... .... .... || ................ ||

Byte 1: 0x09 = b1001 -> zone 1 and 4 used
Byte 8: 0x80 = b10000000 -> zone 64 used. (8 bit/byte * 7 bytes before + eighths bit in byte 8 = 64)
                     
```

## Roaming Zones (0x01043000)

Each entry has 128 bytes and start at 0x01043000 + 128 * [id number]. Range of [id number] = 0 .. 63.

```
57 | 01043000 | 10 | 00ffffff ffffffff ffffffff ffffffff | 36 06 || .ÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || .ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
                     RNRN
57 | 01043010 | 10 | ffffffff ffffffff ffffffff ffffffff | 45 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01043020 | 10 | ffffffff ffffffff ffffffff ffffffff | 55 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01043030 | 10 | ffffffff ffffffff ffffffff ffffffff | 65 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01043040 | 10 | 526f616d 205a6f6e 65204848 00000000 | 80 06 || Roam  Zon e HH .... || Roam Zone HH.... ||
                     NANANANA NANANANA NANANANA NANANANA
57 | 01043050 | 10 | 00000000 00000000 00000000 00000000 | 95 06 || .... .... .... .... || ................ ||
57 | 01043060 | 10 | 00000000 00000000 00000000 00000000 | a5 06 || .... .... .... .... || ................ ||
57 | 01043070 | 10 | 00000000 00000000 00000000 00000000 | b5 06 || .... .... .... .... || ................ ||

   - RN - Roaming channel member: 1 byte each, id of included roaming channel in this zone. (0x00 -> 1 ... 0xf9 -> 250)
          TBD: How many channels can be inserted in a roaming zone? 64?
   - NA - Name: ASCII, max 16 byte, unused characters are 0x00.
```

Empty entries will not be written.

## Scanlists (0x001080000)

There are up to 250 scanlists programmable which each can contain up to 50 channels.

```
57 | 01080000 | 10 | 0000ffff ffff1400 1e001f00 1f000048 | cd 06 || ..ÿÿ ÿÿ.. .... ...H || ..ÿÿÿÿ.........H ||
                       PRPCH1 PCH2LA   LB  DR   DW  RVNA
57 | 01080010 | 10 | 482d4d65 74726f70 6f6c2d54 47380000 | f0 06 || H-Me trop ol-T G8.. || H-Metropol-TG8.. ||
                     NANANANA NANANANA NANANANA NANANA
57 | 01080020 | 10 | 9500a900 1e01ffff ffffffff ffffffff | 8c 06 || ..©. ..ÿÿ ÿÿÿÿ ÿÿÿÿ || ..©...ÿÿÿÿÿÿÿÿÿÿ ||
                     I001I002 I003I004 I005I006 I007I008

[...]

57 | 01080080 | 10 | ffffffff 00000000 00000000 00000000 | 95 06 || ÿÿÿÿ .... .... .... || ÿÿÿÿ............ ||
                     I050

   - PR - Priority Channel Select: 0x00 -> Off, 0x03-> Priority Channel Select1 + Priority Channel Select2
   - PHCx - Priority Channel x: 2 bytes, low byte first, channel id. 0xffff -> Off
   - LA - Look Back Time A: 1 byte, time = rawvalue / 10 s, valid range 0.5 .. 5.0s.
   - LB - Look Back Time B: 1 byte, time = rawvalue / 10 s, valid range 0.5 .. 5.0s.   
   - DR - Dropout Delay Time: 1 byte, time = rawvalue / 10 s, valid range 0.1 .. 5.0s.   
   - DW - Dwell Time: 1 byte, time = rawvalue / 10 s, valid range 0.1 .. 5.0s.   
   - RV - Revert Channel: 1 byte, 0x00 -> Selected, 0x01 -> Selected + TalkBack, 0x02 -> Priority Channel Select1, 
                                  0x03 -> Priority Channel Select2, 0x04 -> Last Called, 0x05 -> Last Used, 
                                  0x06 -> Priority Channel Select1 + TalkBack, 0x07 -> Priority Channel Select2 + TalkBack
   - NA - Name: ASCII, max 16 bytes, unused characters are 0x00.                     
   - Ix - ID: 2 bytes, low byte first. Channel ID, 0xffff if free.

```
Empty scanlist entries will not be written.

One Scanlist contains 144 bytes. The memory is partitioned in multiple sections sometimes with bigger gaps in between. 

The memory addresses for each scanlist are:

```
memSectScanlist = [
   { 'address' : 0x01080000, 'size' : 144 }, # Scanlist 1
   { 'address' : 0x01080200, 'size' : 144 }, # Scanlist 2
   { 'address' : 0x01080400, 'size' : 144 }, # Scanlist 3
   { 'address' : 0x01080600, 'size' : 144 }, # Scanlist 4
   { 'address' : 0x01080800, 'size' : 144 }, # Scanlist 5
   { 'address' : 0x01080a00, 'size' : 144 }, # Scanlist 6
   { 'address' : 0x01080c00, 'size' : 144 }, # Scanlist 7
   { 'address' : 0x01080e00, 'size' : 144 }, # Scanlist 8
   { 'address' : 0x01081000, 'size' : 144 }, # Scanlist 9
   { 'address' : 0x01081200, 'size' : 144 }, # Scanlist 10
   { 'address' : 0x01081400, 'size' : 144 }, # Scanlist 11
   { 'address' : 0x01081600, 'size' : 144 }, # Scanlist 12
   { 'address' : 0x01081800, 'size' : 144 }, # Scanlist 13
   { 'address' : 0x01081a00, 'size' : 144 }, # Scanlist 14
   { 'address' : 0x01081c00, 'size' : 144 }, # Scanlist 15
   { 'address' : 0x01081e00, 'size' : 144 }, # Scanlist 16
   { 'address' : 0x010c0000, 'size' : 144 }, # Scanlist 17
   { 'address' : 0x010c0200, 'size' : 144 }, # Scanlist 18
   { 'address' : 0x010c0400, 'size' : 144 }, # Scanlist 19
   { 'address' : 0x010c0600, 'size' : 144 }, # Scanlist 20
   { 'address' : 0x010c0800, 'size' : 144 }, # Scanlist 21
   { 'address' : 0x010c0a00, 'size' : 144 }, # Scanlist 22
   { 'address' : 0x010c0c00, 'size' : 144 }, # Scanlist 23
   { 'address' : 0x010c0e00, 'size' : 144 }, # Scanlist 24
   { 'address' : 0x010c1000, 'size' : 144 }, # Scanlist 25
   { 'address' : 0x010c1200, 'size' : 144 }, # Scanlist 26
   { 'address' : 0x010c1400, 'size' : 144 }, # Scanlist 27
   { 'address' : 0x010c1600, 'size' : 144 }, # Scanlist 28
   { 'address' : 0x010c1800, 'size' : 144 }, # Scanlist 29
   { 'address' : 0x010c1a00, 'size' : 144 }, # Scanlist 30
   { 'address' : 0x010c1c00, 'size' : 144 }, # Scanlist 31
   { 'address' : 0x010c1e00, 'size' : 144 }, # Scanlist 32
   { 'address' : 0x01100000, 'size' : 144 }, # Scanlist 33
   { 'address' : 0x01100200, 'size' : 144 }, # Scanlist 34
   { 'address' : 0x01100400, 'size' : 144 }, # Scanlist 35
   { 'address' : 0x01100600, 'size' : 144 }, # Scanlist 36
   { 'address' : 0x01100800, 'size' : 144 }, # Scanlist 37
   { 'address' : 0x01100a00, 'size' : 144 }, # Scanlist 38
   { 'address' : 0x01100c00, 'size' : 144 }, # Scanlist 39
   { 'address' : 0x01100e00, 'size' : 144 }, # Scanlist 40
   { 'address' : 0x01101000, 'size' : 144 }, # Scanlist 41
   { 'address' : 0x01101200, 'size' : 144 }, # Scanlist 42
   { 'address' : 0x01101400, 'size' : 144 }, # Scanlist 43
   { 'address' : 0x01101600, 'size' : 144 }, # Scanlist 44
   { 'address' : 0x01101800, 'size' : 144 }, # Scanlist 45
   { 'address' : 0x01101a00, 'size' : 144 }, # Scanlist 46
   { 'address' : 0x01101c00, 'size' : 144 }, # Scanlist 47
   { 'address' : 0x01101e00, 'size' : 144 }, # Scanlist 48
   { 'address' : 0x01140000, 'size' : 144 }, # Scanlist 49
   { 'address' : 0x01140200, 'size' : 144 }, # Scanlist 50
   { 'address' : 0x01140400, 'size' : 144 }, # Scanlist 51
   { 'address' : 0x01140600, 'size' : 144 }, # Scanlist 52
   { 'address' : 0x01140800, 'size' : 144 }, # Scanlist 53
   { 'address' : 0x01140a00, 'size' : 144 }, # Scanlist 54
   { 'address' : 0x01140c00, 'size' : 144 }, # Scanlist 55
   { 'address' : 0x01140e00, 'size' : 144 }, # Scanlist 56
   { 'address' : 0x01141000, 'size' : 144 }, # Scanlist 57
   { 'address' : 0x01141200, 'size' : 144 }, # Scanlist 58
   { 'address' : 0x01141400, 'size' : 144 }, # Scanlist 59
   { 'address' : 0x01141600, 'size' : 144 }, # Scanlist 60
   { 'address' : 0x01141800, 'size' : 144 }, # Scanlist 61
   { 'address' : 0x01141a00, 'size' : 144 }, # Scanlist 62
   { 'address' : 0x01141c00, 'size' : 144 }, # Scanlist 63
   { 'address' : 0x01141e00, 'size' : 144 }, # Scanlist 64
   { 'address' : 0x01180000, 'size' : 144 }, # Scanlist 65
   { 'address' : 0x01180200, 'size' : 144 }, # Scanlist 66
   { 'address' : 0x01180400, 'size' : 144 }, # Scanlist 67
   { 'address' : 0x01180600, 'size' : 144 }, # Scanlist 68
   { 'address' : 0x01180800, 'size' : 144 }, # Scanlist 69
   { 'address' : 0x01180a00, 'size' : 144 }, # Scanlist 70
   { 'address' : 0x01180c00, 'size' : 144 }, # Scanlist 71
   { 'address' : 0x01180e00, 'size' : 144 }, # Scanlist 72
   { 'address' : 0x01181000, 'size' : 144 }, # Scanlist 73
   { 'address' : 0x01181200, 'size' : 144 }, # Scanlist 74
   { 'address' : 0x01181400, 'size' : 144 }, # Scanlist 75
   { 'address' : 0x01181600, 'size' : 144 }, # Scanlist 76
   { 'address' : 0x01181800, 'size' : 144 }, # Scanlist 77
   { 'address' : 0x01181a00, 'size' : 144 }, # Scanlist 78
   { 'address' : 0x01181c00, 'size' : 144 }, # Scanlist 79
   { 'address' : 0x01181e00, 'size' : 144 }, # Scanlist 80
   { 'address' : 0x011c0000, 'size' : 144 }, # Scanlist 81
   { 'address' : 0x011c0200, 'size' : 144 }, # Scanlist 82
   { 'address' : 0x011c0400, 'size' : 144 }, # Scanlist 83
   { 'address' : 0x011c0600, 'size' : 144 }, # Scanlist 84
   { 'address' : 0x011c0800, 'size' : 144 }, # Scanlist 85
   { 'address' : 0x011c0a00, 'size' : 144 }, # Scanlist 86
   { 'address' : 0x011c0c00, 'size' : 144 }, # Scanlist 87
   { 'address' : 0x011c0e00, 'size' : 144 }, # Scanlist 88
   { 'address' : 0x011c1000, 'size' : 144 }, # Scanlist 89
   { 'address' : 0x011c1200, 'size' : 144 }, # Scanlist 90
   { 'address' : 0x011c1400, 'size' : 144 }, # Scanlist 91
   { 'address' : 0x011c1600, 'size' : 144 }, # Scanlist 92
   { 'address' : 0x011c1800, 'size' : 144 }, # Scanlist 93
   { 'address' : 0x011c1a00, 'size' : 144 }, # Scanlist 94
   { 'address' : 0x011c1c00, 'size' : 144 }, # Scanlist 95
   { 'address' : 0x011c1e00, 'size' : 144 }, # Scanlist 96
   { 'address' : 0x01200000, 'size' : 144 }, # Scanlist 97
   { 'address' : 0x01200200, 'size' : 144 }, # Scanlist 98
   { 'address' : 0x01200400, 'size' : 144 }, # Scanlist 99
   { 'address' : 0x01200600, 'size' : 144 }, # Scanlist 100
   { 'address' : 0x01200800, 'size' : 144 }, # Scanlist 101
   { 'address' : 0x01200a00, 'size' : 144 }, # Scanlist 102
   { 'address' : 0x01200c00, 'size' : 144 }, # Scanlist 103
   { 'address' : 0x01200e00, 'size' : 144 }, # Scanlist 104
   { 'address' : 0x01201000, 'size' : 144 }, # Scanlist 105
   { 'address' : 0x01201200, 'size' : 144 }, # Scanlist 106
   { 'address' : 0x01201400, 'size' : 144 }, # Scanlist 107
   { 'address' : 0x01201600, 'size' : 144 }, # Scanlist 108
   { 'address' : 0x01201800, 'size' : 144 }, # Scanlist 109
   { 'address' : 0x01201a00, 'size' : 144 }, # Scanlist 110
   { 'address' : 0x01201c00, 'size' : 144 }, # Scanlist 111
   { 'address' : 0x01201e00, 'size' : 144 }, # Scanlist 112
   { 'address' : 0x01240000, 'size' : 144 }, # Scanlist 113
   { 'address' : 0x01240200, 'size' : 144 }, # Scanlist 114
   { 'address' : 0x01240400, 'size' : 144 }, # Scanlist 115
   { 'address' : 0x01240600, 'size' : 144 }, # Scanlist 116
   { 'address' : 0x01240800, 'size' : 144 }, # Scanlist 117
   { 'address' : 0x01240a00, 'size' : 144 }, # Scanlist 118
   { 'address' : 0x01240c00, 'size' : 144 }, # Scanlist 119
   { 'address' : 0x01240e00, 'size' : 144 }, # Scanlist 120
   { 'address' : 0x01241000, 'size' : 144 }, # Scanlist 121
   { 'address' : 0x01241200, 'size' : 144 }, # Scanlist 122
   { 'address' : 0x01241400, 'size' : 144 }, # Scanlist 123
   { 'address' : 0x01241600, 'size' : 144 }, # Scanlist 124
   { 'address' : 0x01241800, 'size' : 144 }, # Scanlist 125
   { 'address' : 0x01241a00, 'size' : 144 }, # Scanlist 126
   { 'address' : 0x01241c00, 'size' : 144 }, # Scanlist 127
   { 'address' : 0x01241e00, 'size' : 144 }, # Scanlist 128
   { 'address' : 0x01280000, 'size' : 144 }, # Scanlist 129
   { 'address' : 0x01280200, 'size' : 144 }, # Scanlist 130
   { 'address' : 0x01280400, 'size' : 144 }, # Scanlist 131
   { 'address' : 0x01280600, 'size' : 144 }, # Scanlist 132
   { 'address' : 0x01280800, 'size' : 144 }, # Scanlist 133
   { 'address' : 0x01280a00, 'size' : 144 }, # Scanlist 134
   { 'address' : 0x01280c00, 'size' : 144 }, # Scanlist 135
   { 'address' : 0x01280e00, 'size' : 144 }, # Scanlist 136
   { 'address' : 0x01281000, 'size' : 144 }, # Scanlist 137
   { 'address' : 0x01281200, 'size' : 144 }, # Scanlist 138
   { 'address' : 0x01281400, 'size' : 144 }, # Scanlist 139
   { 'address' : 0x01281600, 'size' : 144 }, # Scanlist 140
   { 'address' : 0x01281800, 'size' : 144 }, # Scanlist 141
   { 'address' : 0x01281a00, 'size' : 144 }, # Scanlist 142
   { 'address' : 0x01281c00, 'size' : 144 }, # Scanlist 143
   { 'address' : 0x01281e00, 'size' : 144 }, # Scanlist 144
   { 'address' : 0x012c0000, 'size' : 144 }, # Scanlist 145
   { 'address' : 0x012c0200, 'size' : 144 }, # Scanlist 146
   { 'address' : 0x012c0400, 'size' : 144 }, # Scanlist 147
   { 'address' : 0x012c0600, 'size' : 144 }, # Scanlist 148
   { 'address' : 0x012c0800, 'size' : 144 }, # Scanlist 149
   { 'address' : 0x012c0a00, 'size' : 144 }, # Scanlist 150
   { 'address' : 0x012c0c00, 'size' : 144 }, # Scanlist 151
   { 'address' : 0x012c0e00, 'size' : 144 }, # Scanlist 152
   { 'address' : 0x012c1000, 'size' : 144 }, # Scanlist 153
   { 'address' : 0x012c1200, 'size' : 144 }, # Scanlist 154
   { 'address' : 0x012c1400, 'size' : 144 }, # Scanlist 155
   { 'address' : 0x012c1600, 'size' : 144 }, # Scanlist 156
   { 'address' : 0x012c1800, 'size' : 144 }, # Scanlist 157
   { 'address' : 0x012c1a00, 'size' : 144 }, # Scanlist 158
   { 'address' : 0x012c1c00, 'size' : 144 }, # Scanlist 159
   { 'address' : 0x012c1e00, 'size' : 144 }, # Scanlist 160
   { 'address' : 0x01300000, 'size' : 144 }, # Scanlist 161
   { 'address' : 0x01300200, 'size' : 144 }, # Scanlist 162
   { 'address' : 0x01300400, 'size' : 144 }, # Scanlist 163
   { 'address' : 0x01300600, 'size' : 144 }, # Scanlist 164
   { 'address' : 0x01300800, 'size' : 144 }, # Scanlist 165
   { 'address' : 0x01300a00, 'size' : 144 }, # Scanlist 166
   { 'address' : 0x01300c00, 'size' : 144 }, # Scanlist 167
   { 'address' : 0x01300e00, 'size' : 144 }, # Scanlist 168
   { 'address' : 0x01301000, 'size' : 144 }, # Scanlist 169
   { 'address' : 0x01301200, 'size' : 144 }, # Scanlist 170
   { 'address' : 0x01301400, 'size' : 144 }, # Scanlist 171
   { 'address' : 0x01301600, 'size' : 144 }, # Scanlist 172
   { 'address' : 0x01301800, 'size' : 144 }, # Scanlist 173
   { 'address' : 0x01301a00, 'size' : 144 }, # Scanlist 174
   { 'address' : 0x01301c00, 'size' : 144 }, # Scanlist 175
   { 'address' : 0x01301e00, 'size' : 144 }, # Scanlist 176
   { 'address' : 0x01340000, 'size' : 144 }, # Scanlist 177
   { 'address' : 0x01340200, 'size' : 144 }, # Scanlist 178
   { 'address' : 0x01340400, 'size' : 144 }, # Scanlist 179
   { 'address' : 0x01340600, 'size' : 144 }, # Scanlist 180
   { 'address' : 0x01340800, 'size' : 144 }, # Scanlist 181
   { 'address' : 0x01340a00, 'size' : 144 }, # Scanlist 182
   { 'address' : 0x01340c00, 'size' : 144 }, # Scanlist 183
   { 'address' : 0x01340e00, 'size' : 144 }, # Scanlist 184
   { 'address' : 0x01341000, 'size' : 144 }, # Scanlist 185
   { 'address' : 0x01341200, 'size' : 144 }, # Scanlist 186
   { 'address' : 0x01341400, 'size' : 144 }, # Scanlist 187
   { 'address' : 0x01341600, 'size' : 144 }, # Scanlist 188
   { 'address' : 0x01341800, 'size' : 144 }, # Scanlist 189
   { 'address' : 0x01341a00, 'size' : 144 }, # Scanlist 190
   { 'address' : 0x01341c00, 'size' : 144 }, # Scanlist 191
   { 'address' : 0x01341e00, 'size' : 144 }, # Scanlist 192
   { 'address' : 0x01380000, 'size' : 144 }, # Scanlist 193
   { 'address' : 0x01380200, 'size' : 144 }, # Scanlist 194
   { 'address' : 0x01380400, 'size' : 144 }, # Scanlist 195
   { 'address' : 0x01380600, 'size' : 144 }, # Scanlist 196
   { 'address' : 0x01380800, 'size' : 144 }, # Scanlist 197
   { 'address' : 0x01380a00, 'size' : 144 }, # Scanlist 198
   { 'address' : 0x01380c00, 'size' : 144 }, # Scanlist 199
   { 'address' : 0x01380e00, 'size' : 144 }, # Scanlist 200
   { 'address' : 0x01381000, 'size' : 144 }, # Scanlist 201
   { 'address' : 0x01381200, 'size' : 144 }, # Scanlist 202
   { 'address' : 0x01381400, 'size' : 144 }, # Scanlist 203
   { 'address' : 0x01381600, 'size' : 144 }, # Scanlist 204
   { 'address' : 0x01381800, 'size' : 144 }, # Scanlist 205
   { 'address' : 0x01381a00, 'size' : 144 }, # Scanlist 206
   { 'address' : 0x01381c00, 'size' : 144 }, # Scanlist 207
   { 'address' : 0x01381e00, 'size' : 144 }, # Scanlist 208
   { 'address' : 0x013c0000, 'size' : 144 }, # Scanlist 209
   { 'address' : 0x013c0200, 'size' : 144 }, # Scanlist 210
   { 'address' : 0x013c0400, 'size' : 144 }, # Scanlist 211
   { 'address' : 0x013c0600, 'size' : 144 }, # Scanlist 212
   { 'address' : 0x013c0800, 'size' : 144 }, # Scanlist 213
   { 'address' : 0x013c0a00, 'size' : 144 }, # Scanlist 214
   { 'address' : 0x013c0c00, 'size' : 144 }, # Scanlist 215
   { 'address' : 0x013c0e00, 'size' : 144 }, # Scanlist 216
   { 'address' : 0x013c1000, 'size' : 144 }, # Scanlist 217
   { 'address' : 0x013c1200, 'size' : 144 }, # Scanlist 218
   { 'address' : 0x013c1400, 'size' : 144 }, # Scanlist 219
   { 'address' : 0x013c1600, 'size' : 144 }, # Scanlist 220
   { 'address' : 0x013c1800, 'size' : 144 }, # Scanlist 221
   { 'address' : 0x013c1a00, 'size' : 144 }, # Scanlist 222
   { 'address' : 0x013c1c00, 'size' : 144 }, # Scanlist 223
   { 'address' : 0x013c1e00, 'size' : 144 }, # Scanlist 224
   { 'address' : 0x01400000, 'size' : 144 }, # Scanlist 225
   { 'address' : 0x01400200, 'size' : 144 }, # Scanlist 226
   { 'address' : 0x01400400, 'size' : 144 }, # Scanlist 227
   { 'address' : 0x01400600, 'size' : 144 }, # Scanlist 228
   { 'address' : 0x01400800, 'size' : 144 }, # Scanlist 229
   { 'address' : 0x01400a00, 'size' : 144 }, # Scanlist 230
   { 'address' : 0x01400c00, 'size' : 144 }, # Scanlist 231
   { 'address' : 0x01400e00, 'size' : 144 }, # Scanlist 232
   { 'address' : 0x01401000, 'size' : 144 }, # Scanlist 233
   { 'address' : 0x01401200, 'size' : 144 }, # Scanlist 234
   { 'address' : 0x01401400, 'size' : 144 }, # Scanlist 235
   { 'address' : 0x01401600, 'size' : 144 }, # Scanlist 236
   { 'address' : 0x01401800, 'size' : 144 }, # Scanlist 237
   { 'address' : 0x01401a00, 'size' : 144 }, # Scanlist 238
   { 'address' : 0x01401c00, 'size' : 144 }, # Scanlist 239
   { 'address' : 0x01401e00, 'size' : 144 }, # Scanlist 240
   { 'address' : 0x01440000, 'size' : 144 }, # Scanlist 241
   { 'address' : 0x01440200, 'size' : 144 }, # Scanlist 242
   { 'address' : 0x01440400, 'size' : 144 }, # Scanlist 243
   { 'address' : 0x01440600, 'size' : 144 }, # Scanlist 244
   { 'address' : 0x01440800, 'size' : 144 }, # Scanlist 245
   { 'address' : 0x01440a00, 'size' : 144 }, # Scanlist 246
   { 'address' : 0x01440c00, 'size' : 144 }, # Scanlist 247
   { 'address' : 0x01440e00, 'size' : 144 }, # Scanlist 248
   { 'address' : 0x01441000, 'size' : 144 }, # Scanlist 249
   { 'address' : 0x01441200, 'size' : 144 }  # Scanlist 250
]
```


## Prefabricated SMS

Up to 100 prefabricated SMS can be stored. Besides the SMS texts two management memory sections must be written.

### List of used SMS storage 1 (0x01640000)

```
57 | 01640000 | 10 | 00000100 00000000 00000000 00000000 | 76 06 || .... .... .... .... || ................ ||
                         NEAC
   
   - NE - Next used SMS number (0xff if no further SMS to be stored)
   - AC - Actual SMS number
                         
57 | 01640010 | 10 | 00000201 00000000 00000000 00000000 | 88 06 || .... .... .... .... || ................ ||
57 | 01640020 | 10 | 00000302 00000000 00000000 00000000 | 9a 06 || .... .... .... .... || ................ ||

[...]

57 | 01640100 | 10 | 00001110 00000000 00000000 00000000 | 97 06 || .... .... .... .... || ................ ||
57 | 01640110 | 10 | 00006311 00000000 00000000 00000000 | fa 06 || ..c. .... .... .... || ..c............. ||

[...]

57 | 01640630 | 10 | 0000ff63 00000000 00000000 00000000 | 0d 06 || ..ÿc .... .... .... || ..ÿc............ ||

memSectSMSUse1 = [
   { 'address' : 0x01640000, 'size' = 16 }, # SMS 1 (ID: 0)
   { 'address' : 0x01640010, 'size' = 16 }, # SMS 2 (ID: 1)
   { 'address' : 0x01640020, 'size' = 16 }, # SMS 3 (ID: 2)
   { 'address' : 0x01640030, 'size' = 16 }, # SMS 4 (ID: 3)
   { 'address' : 0x01640040, 'size' = 16 }, # SMS 5 (ID: 4)
   { 'address' : 0x01640050, 'size' = 16 }, # SMS 6 (ID: 5)
   { 'address' : 0x01640060, 'size' = 16 }, # SMS 7 (ID: 6)
   { 'address' : 0x01640070, 'size' = 16 }, # SMS 8 (ID: 7)
   { 'address' : 0x01640080, 'size' = 16 }, # SMS 9 (ID: 8)
   { 'address' : 0x01640090, 'size' = 16 }, # SMS 10 (ID: 9)
   { 'address' : 0x016400a0, 'size' = 16 }, # SMS 11 (ID: 10)
   { 'address' : 0x016400b0, 'size' = 16 }, # SMS 12 (ID: 11)
   { 'address' : 0x016400c0, 'size' = 16 }, # SMS 13 (ID: 12)
   { 'address' : 0x016400d0, 'size' = 16 }, # SMS 14 (ID: 13)
   { 'address' : 0x016400e0, 'size' = 16 }, # SMS 15 (ID: 14)
   { 'address' : 0x016400f0, 'size' = 16 }, # SMS 16 (ID: 15)
   { 'address' : 0x01640100, 'size' = 16 }, # SMS 17 (ID: 16)
   { 'address' : 0x01640110, 'size' = 16 }, # SMS 18 (ID: 17)
   { 'address' : 0x01640120, 'size' = 16 }, # SMS 19 (ID: 18)
   { 'address' : 0x01640130, 'size' = 16 }, # SMS 20 (ID: 19)
   { 'address' : 0x01640140, 'size' = 16 }, # SMS 21 (ID: 20)
   { 'address' : 0x01640150, 'size' = 16 }, # SMS 22 (ID: 21)
   { 'address' : 0x01640160, 'size' = 16 }, # SMS 23 (ID: 22)
   { 'address' : 0x01640170, 'size' = 16 }, # SMS 24 (ID: 23)
   { 'address' : 0x01640180, 'size' = 16 }, # SMS 25 (ID: 24)
   { 'address' : 0x01640190, 'size' = 16 }, # SMS 26 (ID: 25)
   { 'address' : 0x016401a0, 'size' = 16 }, # SMS 27 (ID: 26)
   { 'address' : 0x016401b0, 'size' = 16 }, # SMS 28 (ID: 27)
   { 'address' : 0x016401c0, 'size' = 16 }, # SMS 29 (ID: 28)
   { 'address' : 0x016401d0, 'size' = 16 }, # SMS 30 (ID: 29)
   { 'address' : 0x016401e0, 'size' = 16 }, # SMS 31 (ID: 30)
   { 'address' : 0x016401f0, 'size' = 16 }, # SMS 32 (ID: 31)
   { 'address' : 0x01640200, 'size' = 16 }, # SMS 33 (ID: 32)
   { 'address' : 0x01640210, 'size' = 16 }, # SMS 34 (ID: 33)
   { 'address' : 0x01640220, 'size' = 16 }, # SMS 35 (ID: 34)
   { 'address' : 0x01640230, 'size' = 16 }, # SMS 36 (ID: 35)
   { 'address' : 0x01640240, 'size' = 16 }, # SMS 37 (ID: 36)
   { 'address' : 0x01640250, 'size' = 16 }, # SMS 38 (ID: 37)
   { 'address' : 0x01640260, 'size' = 16 }, # SMS 39 (ID: 38)
   { 'address' : 0x01640270, 'size' = 16 }, # SMS 40 (ID: 39)
   { 'address' : 0x01640280, 'size' = 16 }, # SMS 41 (ID: 40)
   { 'address' : 0x01640290, 'size' = 16 }, # SMS 42 (ID: 41)
   { 'address' : 0x016402a0, 'size' = 16 }, # SMS 43 (ID: 42)
   { 'address' : 0x016402b0, 'size' = 16 }, # SMS 44 (ID: 43)
   { 'address' : 0x016402c0, 'size' = 16 }, # SMS 45 (ID: 44)
   { 'address' : 0x016402d0, 'size' = 16 }, # SMS 46 (ID: 45)
   { 'address' : 0x016402e0, 'size' = 16 }, # SMS 47 (ID: 46)
   { 'address' : 0x016402f0, 'size' = 16 }, # SMS 48 (ID: 47)
   { 'address' : 0x01640300, 'size' = 16 }, # SMS 49 (ID: 48)
   { 'address' : 0x01640310, 'size' = 16 }, # SMS 50 (ID: 49)
   { 'address' : 0x01640320, 'size' = 16 }, # SMS 51 (ID: 50)
   { 'address' : 0x01640330, 'size' = 16 }, # SMS 52 (ID: 51)
   { 'address' : 0x01640340, 'size' = 16 }, # SMS 53 (ID: 52)
   { 'address' : 0x01640350, 'size' = 16 }, # SMS 54 (ID: 53)
   { 'address' : 0x01640360, 'size' = 16 }, # SMS 55 (ID: 54)
   { 'address' : 0x01640370, 'size' = 16 }, # SMS 56 (ID: 55)
   { 'address' : 0x01640380, 'size' = 16 }, # SMS 57 (ID: 56)
   { 'address' : 0x01640390, 'size' = 16 }, # SMS 58 (ID: 57)
   { 'address' : 0x016403a0, 'size' = 16 }, # SMS 59 (ID: 58)
   { 'address' : 0x016403b0, 'size' = 16 }, # SMS 60 (ID: 59)
   { 'address' : 0x016403c0, 'size' = 16 }, # SMS 61 (ID: 60)
   { 'address' : 0x016403d0, 'size' = 16 }, # SMS 62 (ID: 61)
   { 'address' : 0x016403e0, 'size' = 16 }, # SMS 63 (ID: 62)
   { 'address' : 0x016403f0, 'size' = 16 }, # SMS 64 (ID: 63)
   { 'address' : 0x01640400, 'size' = 16 }, # SMS 65 (ID: 64)
   { 'address' : 0x01640410, 'size' = 16 }, # SMS 66 (ID: 65)
   { 'address' : 0x01640420, 'size' = 16 }, # SMS 67 (ID: 66)
   { 'address' : 0x01640430, 'size' = 16 }, # SMS 68 (ID: 67)
   { 'address' : 0x01640440, 'size' = 16 }, # SMS 69 (ID: 68)
   { 'address' : 0x01640450, 'size' = 16 }, # SMS 70 (ID: 69)
   { 'address' : 0x01640460, 'size' = 16 }, # SMS 71 (ID: 70)
   { 'address' : 0x01640470, 'size' = 16 }, # SMS 72 (ID: 71)
   { 'address' : 0x01640480, 'size' = 16 }, # SMS 73 (ID: 72)
   { 'address' : 0x01640490, 'size' = 16 }, # SMS 74 (ID: 73)
   { 'address' : 0x016404a0, 'size' = 16 }, # SMS 75 (ID: 74)
   { 'address' : 0x016404b0, 'size' = 16 }, # SMS 76 (ID: 75)
   { 'address' : 0x016404c0, 'size' = 16 }, # SMS 77 (ID: 76)
   { 'address' : 0x016404d0, 'size' = 16 }, # SMS 78 (ID: 77)
   { 'address' : 0x016404e0, 'size' = 16 }, # SMS 79 (ID: 78)
   { 'address' : 0x016404f0, 'size' = 16 }, # SMS 80 (ID: 79)
   { 'address' : 0x01640500, 'size' = 16 }, # SMS 81 (ID: 80)
   { 'address' : 0x01640510, 'size' = 16 }, # SMS 82 (ID: 81)
   { 'address' : 0x01640520, 'size' = 16 }, # SMS 83 (ID: 82)
   { 'address' : 0x01640530, 'size' = 16 }, # SMS 84 (ID: 83)
   { 'address' : 0x01640540, 'size' = 16 }, # SMS 85 (ID: 84)
   { 'address' : 0x01640550, 'size' = 16 }, # SMS 86 (ID: 85)
   { 'address' : 0x01640560, 'size' = 16 }, # SMS 87 (ID: 86)
   { 'address' : 0x01640570, 'size' = 16 }, # SMS 88 (ID: 87)
   { 'address' : 0x01640580, 'size' = 16 }, # SMS 89 (ID: 88)
   { 'address' : 0x01640590, 'size' = 16 }, # SMS 90 (ID: 89)
   { 'address' : 0x016405a0, 'size' = 16 }, # SMS 91 (ID: 90)
   { 'address' : 0x016405b0, 'size' = 16 }, # SMS 92 (ID: 91)
   { 'address' : 0x016405c0, 'size' = 16 }, # SMS 93 (ID: 92)
   { 'address' : 0x016405d0, 'size' = 16 }, # SMS 94 (ID: 93)
   { 'address' : 0x016405e0, 'size' = 16 }, # SMS 95 (ID: 94)
   { 'address' : 0x016405f0, 'size' = 16 }, # SMS 96 (ID: 95)
   { 'address' : 0x01640600, 'size' = 16 }, # SMS 97 (ID: 96)
   { 'address' : 0x01640610, 'size' = 16 }, # SMS 98 (ID: 97)
   { 'address' : 0x01640620, 'size' = 16 }, # SMS 99 (ID: 98)
   { 'address' : 0x01640630, 'size' = 16 }  # SMS 100 (ID: 99)
]
```

Empty fields will not be written.


### List of used SMS storage 2 (0x01640800)

100 bytes starting at address 0x01640800 are used to mark if a predefined SMS is available or not.

```
57 | 01640800 | 10 | 00000000 00000000 00000000 00000000 | 7d 06 || .... .... .... .... || ................ ||
57 | 01640810 | 10 | 0000ffff ffffffff ffffffff ffffffff | 7f 06 || ..ÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ..ÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01640820 | 10 | ffffffff ffffffff ffffffff ffffffff | 8d 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01640830 | 10 | ffffffff ffffffff ffffffff ffffffff | 9d 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01640840 | 10 | ffffffff ffffffff ffffffff ffffffff | ad 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01640850 | 10 | ffffffff ffffffff ffffffff ffffffff | bd 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 01640860 | 10 | ffffff00 00000000 00000000 00000000 | da 06 || ÿÿÿ. .... .... .... || ÿÿÿ............. ||
57 | 01640870 | 10 | 00000000 00000000 00000000 00000000 | ed 06 || .... .... .... .... || ................ ||
57 | 01640880 | 10 | 00000000 00000000 00000000 00000000 | fd 06 || .... .... .... .... || ................ ||

1 byte per SMS entry, 0x00 -> SMS stored, 0xff -> no SMS stored.

In this example SMS 1..18 and 100 are stored. All other memories are free.
```

### SMS Text (0x02140000)

Example of one SMS (SMS No. 100):

```
57 | 02440300 | 10 | 65696e74 72616731 30302d46 46464646 | 5f 06 || eint rag1 00-F FFFF || eintrag100-FFFFF ||
57 | 02440310 | 10 | 46464646 46464646 46464646 46464646 | c9 06 || FFFF FFFF FFFF FFFF || FFFFFFFFFFFFFFFF ||
57 | 02440320 | 10 | 46464646 46464646 46464646 46464646 | d9 06 || FFFF FFFF FFFF FFFF || FFFFFFFFFFFFFFFF ||
57 | 02440330 | 10 | 46464646 46464646 46464646 46464646 | e9 06 || FFFF FFFF FFFF FFFF || FFFFFFFFFFFFFFFF ||
57 | 02440340 | 10 | 46464646 46464646 46464646 46464646 | f9 06 || FFFF FFFF FFFF FFFF || FFFFFFFFFFFFFFFF ||
57 | 02440350 | 10 | 46464646 46464646 46464646 46464646 | 09 06 || FFFF FFFF FFFF FFFF || FFFFFFFFFFFFFFFF ||
57 | 02440360 | 10 | 46464646 00000000 00000000 00000000 | d1 06 || FFFF .... .... .... || FFFF............ ||
57 | 02440370 | 10 | 00000000 00000000 00000000 00000000 | c9 06 || .... .... .... .... || ................ ||
57 | 02440380 | 10 | 00000000 00000000 00000000 00000000 | d9 06 || .... .... .... .... || ................ ||
57 | 02440390 | 10 | 00000000 00000000 00000000 00000000 | e9 06 || .... .... .... .... || ................ ||
57 | 024403a0 | 10 | 00000000 00000000 00000000 00000000 | f9 06 || .... .... .... .... || ................ ||
57 | 024403b0 | 10 | 00000000 00000000 00000000 00000000 | 09 06 || .... .... .... .... || ................ ||
57 | 024403c0 | 10 | 00000000 00000000 00000000 00000000 | 19 06 || .... .... .... .... || ................ ||
```
Every entry has its own 208 byte memory section. The first 100 bytes can be used as text (ASCII), all others are 0x00.

The reserved memory sections are:
```
memSectPrefSMS = [
   { 'address' : 0x02140000, 'size' : 208 }, # SMS 1
   { 'address' : 0x02140100, 'size' : 208 }, # SMS 2
   { 'address' : 0x02140200, 'size' : 208 }, # SMS 3
   { 'address' : 0x02140300, 'size' : 208 }, # SMS 4
   { 'address' : 0x02140400, 'size' : 208 }, # SMS 5
   { 'address' : 0x02140500, 'size' : 208 }, # SMS 6
   { 'address' : 0x02140600, 'size' : 208 }, # SMS 7
   { 'address' : 0x02140700, 'size' : 208 }, # SMS 8
   { 'address' : 0x02180000, 'size' : 208 }, # SMS 9
   { 'address' : 0x02180100, 'size' : 208 }, # SMS 10
   { 'address' : 0x02180200, 'size' : 208 }, # SMS 11
   { 'address' : 0x02180300, 'size' : 208 }, # SMS 12
   { 'address' : 0x02180400, 'size' : 208 }, # SMS 13
   { 'address' : 0x02180500, 'size' : 208 }, # SMS 14
   { 'address' : 0x02180600, 'size' : 208 }, # SMS 15
   { 'address' : 0x02180700, 'size' : 208 }, # SMS 16
   { 'address' : 0x021c0000, 'size' : 208 }, # SMS 17
   { 'address' : 0x021c0100, 'size' : 208 }, # SMS 18
   { 'address' : 0x021c0200, 'size' : 208 }, # SMS 19
   { 'address' : 0x021c0300, 'size' : 208 }, # SMS 20
   { 'address' : 0x021c0400, 'size' : 208 }, # SMS 21
   { 'address' : 0x021c0500, 'size' : 208 }, # SMS 22
   { 'address' : 0x021c0600, 'size' : 208 }, # SMS 23
   { 'address' : 0x021c0700, 'size' : 208 }, # SMS 24
   { 'address' : 0x02200000, 'size' : 208 }, # SMS 25
   { 'address' : 0x02200100, 'size' : 208 }, # SMS 26
   { 'address' : 0x02200200, 'size' : 208 }, # SMS 27
   { 'address' : 0x02200300, 'size' : 208 }, # SMS 28
   { 'address' : 0x02200400, 'size' : 208 }, # SMS 29
   { 'address' : 0x02200500, 'size' : 208 }, # SMS 30
   { 'address' : 0x02200600, 'size' : 208 }, # SMS 31
   { 'address' : 0x02200700, 'size' : 208 }, # SMS 32
   { 'address' : 0x02240000, 'size' : 208 }, # SMS 33
   { 'address' : 0x02240100, 'size' : 208 }, # SMS 34
   { 'address' : 0x02240200, 'size' : 208 }, # SMS 35
   { 'address' : 0x02240300, 'size' : 208 }, # SMS 36
   { 'address' : 0x02240400, 'size' : 208 }, # SMS 37
   { 'address' : 0x02240500, 'size' : 208 }, # SMS 38
   { 'address' : 0x02240600, 'size' : 208 }, # SMS 39
   { 'address' : 0x02240700, 'size' : 208 }, # SMS 40
   { 'address' : 0x02280000, 'size' : 208 }, # SMS 41
   { 'address' : 0x02280100, 'size' : 208 }, # SMS 42
   { 'address' : 0x02280200, 'size' : 208 }, # SMS 43
   { 'address' : 0x02280300, 'size' : 208 }, # SMS 44
   { 'address' : 0x02280400, 'size' : 208 }, # SMS 45
   { 'address' : 0x02280500, 'size' : 208 }, # SMS 46
   { 'address' : 0x02280600, 'size' : 208 }, # SMS 47
   { 'address' : 0x02280700, 'size' : 208 }, # SMS 48
   { 'address' : 0x022c0000, 'size' : 208 }, # SMS 49
   { 'address' : 0x022c0100, 'size' : 208 }, # SMS 50
   { 'address' : 0x022c0200, 'size' : 208 }, # SMS 51
   { 'address' : 0x022c0300, 'size' : 208 }, # SMS 52
   { 'address' : 0x022c0400, 'size' : 208 }, # SMS 53
   { 'address' : 0x022c0500, 'size' : 208 }, # SMS 54
   { 'address' : 0x022c0600, 'size' : 208 }, # SMS 55
   { 'address' : 0x022c0700, 'size' : 208 }, # SMS 56
   { 'address' : 0x02300000, 'size' : 208 }, # SMS 57
   { 'address' : 0x02300100, 'size' : 208 }, # SMS 58
   { 'address' : 0x02300200, 'size' : 208 }, # SMS 59
   { 'address' : 0x02300300, 'size' : 208 }, # SMS 60
   { 'address' : 0x02300400, 'size' : 208 }, # SMS 61
   { 'address' : 0x02300500, 'size' : 208 }, # SMS 62
   { 'address' : 0x02300600, 'size' : 208 }, # SMS 63
   { 'address' : 0x02300700, 'size' : 208 }, # SMS 64
   { 'address' : 0x02340000, 'size' : 208 }, # SMS 65
   { 'address' : 0x02340100, 'size' : 208 }, # SMS 66
   { 'address' : 0x02340200, 'size' : 208 }, # SMS 67
   { 'address' : 0x02340300, 'size' : 208 }, # SMS 68
   { 'address' : 0x02340400, 'size' : 208 }, # SMS 69
   { 'address' : 0x02340500, 'size' : 208 }, # SMS 70
   { 'address' : 0x02340600, 'size' : 208 }, # SMS 71
   { 'address' : 0x02340700, 'size' : 208 }, # SMS 72
   { 'address' : 0x02380000, 'size' : 208 }, # SMS 73
   { 'address' : 0x02380100, 'size' : 208 }, # SMS 74
   { 'address' : 0x02380200, 'size' : 208 }, # SMS 75
   { 'address' : 0x02380300, 'size' : 208 }, # SMS 76
   { 'address' : 0x02380400, 'size' : 208 }, # SMS 77
   { 'address' : 0x02380500, 'size' : 208 }, # SMS 78
   { 'address' : 0x02380600, 'size' : 208 }, # SMS 79
   { 'address' : 0x02380700, 'size' : 208 }, # SMS 80
   { 'address' : 0x023c0000, 'size' : 208 }, # SMS 81
   { 'address' : 0x023c0100, 'size' : 208 }, # SMS 82
   { 'address' : 0x023c0200, 'size' : 208 }, # SMS 83
   { 'address' : 0x023c0300, 'size' : 208 }, # SMS 84
   { 'address' : 0x023c0400, 'size' : 208 }, # SMS 85
   { 'address' : 0x023c0500, 'size' : 208 }, # SMS 86
   { 'address' : 0x023c0600, 'size' : 208 }, # SMS 87
   { 'address' : 0x023c0700, 'size' : 208 }, # SMS 88
   { 'address' : 0x02400000, 'size' : 208 }, # SMS 89
   { 'address' : 0x02400100, 'size' : 208 }, # SMS 90
   { 'address' : 0x02400200, 'size' : 208 }, # SMS 91
   { 'address' : 0x02400300, 'size' : 208 }, # SMS 92
   { 'address' : 0x02400400, 'size' : 208 }, # SMS 93
   { 'address' : 0x02400500, 'size' : 208 }, # SMS 94
   { 'address' : 0x02400600, 'size' : 208 }, # SMS 95
   { 'address' : 0x02400700, 'size' : 208 }, # SMS 96
   { 'address' : 0x02440000, 'size' : 208 }, # SMS 97
   { 'address' : 0x02440100, 'size' : 208 }, # SMS 98
   { 'address' : 0x02440200, 'size' : 208 }, # SMS 99
   { 'address' : 0x02440300, 'size' : 208 } # SMS 100
]
```

Unused memory sections will not be written.



## FM (0x02480000)

```
57 | 02480000 | 10 | 00876000 00942000 00923000 01036000 | 1b 06 || ..`. .. . ..0. ..`. || ..`... ...0...`. ||
                     FFFFFF
57 | 02480010 | 10 | 01000000 01068000 00971000 01080000 | a2 06 || .... .... .... .... || ................ ||
57 | 02480020 | 10 | 00903000 00000000 00000000 00000000 | 3a 06 || ..0. .... .... .... || ..0............. ||

57 | 02480180 | 10 | 00000000 00000000 01000000 01000000 | dd 06 || .... .... .... .... || ................ ||

   - FF - FM Frequency: 3 bytes BCD coded

4 bytes per record, 100 records in total. Last record ends at 0x0248018f.

57 | 02480200 | 10 | 00903000 00000000 00000000 00000000 | 1c 06 || ..0. .... .... .... || ..0............. ||
                     VVVVVV

   - VV - VFO FM Frequency: 3 bytes BCD coded
```

## FM channels used (0x02480010)
```
57 | 02480210 | 10 | ff010000 00000000 00000000 0c000000 | 78 06 || ÿ... .... .... .... || ÿ............... ||
                     UUUU..                     UU
   - UU - Channel Used: Bit fields, byte 1 contains channel 1 (LSB) .. 8 (MSB), byte 2 9-16, ...
          0 channel not used, 1 channel used.
```
13 bytes for 100 channels.


## FM channels scan (0x02480010)
```
57 | 02480220 | 10 | 00000000 00000000 00000000 08000000 | 84 06 || .... .... .... .... || ................ ||
                     S1S2S3...
   - Sx - FM Scan: Bit field S1 contains channel 1 (LSB) .. 8 (MSB), S2 9-16, ...
     Del -> 0  Add -> 1
```
13 bytes for 100 channels. VFO has no scan type.

## 5 Tone (0x024c0000)

```
57 | 024c0000 | 10 | 00000646 38501e00 00000000 00000000 | 50 06 || ...F 8P.. .... .... || ...F8P.......... ||
                       ESLITI EIEIEIEI EIEIEIEI EIEIEIEI
57 | 024c0010 | 10 | 00000000 00000000 444c3149 4e5f3100 | 56 06 || .... .... DL1I N_1. || ........DL1IN_1. ||
                     EIEIEIEI EIEIEIEI NANANANA NANANA
57 | 024c0020 | 10 | 0000061e 38502e00 00000000 00000000 | 58 06 || .... 8P.. .... .... || ....8P.......... ||
57 | 024c0030 | 10 | 00000000 00000000 444c3149 4e5f3200 | 77 06 || .... .... DL1I N_2. || ........DL1IN_2. ||
57 | 024c0040 | 10 | 00010146 1e000000 00000000 00000000 | 04 06 || ...F .... .... .... || ...F............ ||
57 | 024c0050 | 10 | 00000000 00000000 31202020 20202000 | 9f 06 || .... .... 1       . || ........1      . ||
57 | 024c0060 | 10 | 00020146 2e000000 00000000 00000000 | 35 06 || ...F .... .... .... || ...F............ ||
57 | 024c0070 | 10 | 00000000 00000000 32202020 20202000 | c0 06 || .... .... 2       . || ........2      . ||

[...]

57 | 024c0c60 | 10 | 000e0a21 12345679 80000000 00000000 | 98 06 || ...! .4Vy .... .... || ...!.4Vy........ ||
57 | 024c0c70 | 10 | 00000000 00000000 656e6465 20202000 | d6 06 || .... .... ende    . || ........ende   . ||

   - ES - Encoding standard. 0x00 -> ZWEI1, 0x01 -> ZVEI2, 0x01 -> ZVEI2, ... TBD: make list
   - LI - Length of ID
   - TI - Time of encode tone: 1 byte, resolution 1ms, valid range 30..100 ms. (0x46 = 70ms)
   - EI - Encode id: BCD coded. Max 40 characters.
   - NA - Name: ASCII, max. 7 byte, 0 padded.

Start at 0x024c0000. 1 record is 32 bytes. 100 records possible. End of records therefore at 0x024c0c7f. Empty records will not be written.
```

## 5 tone encodings used (0x024c0c80)

1 bit for every used encoding. 0 -> encoding is free, 1 -> encoding in use. Max. 100 encodings.
```
57 | 024c0c80 | 10 | 0f000000 00000000 00000000 0c000000 | 05 06 || .... .... .... .... || ................ ||

Byte 1: 0x0f = b1111 -> encoding 1-4 used
Byte 13: 0x0c = b1100 -> zone 99 and 100 used. (8 bit/byte * 12 bytes before + 3rd/4ths bit in byte 13 = 99/100)
```

### 5 Tone list of information IDs (0x024c0d00)

```
57 | 024c0d00 | 10 | 06000c01 02030405 06070809 00010200 | ad 06 || .... .... .... .... || ................ ||
                     FODRLIII IIIIIIII IIIIIIII IIIIII
57 | 024c0d10 | 10 | 00000000 00000000 00000000 00000000 | 7b 06 || .... .... .... .... || ................ ||
                     FNFNFNFN FNFNFN
57 | 024c0d20 | 10 | 00000000 00000000 00000000 00000000 | 8b 06 || .... .... .... .... || ................ ||
57 | 024c0d30 | 10 | 00000000 00000000 00000000 00000000 | 9b 06 || .... .... .... .... || ................ ||
57 | 024c0d40 | 10 | 00000000 00000000 00000000 00000000 | ab 06 || .... .... .... .... || ................ ||
57 | 024c0d50 | 10 | 00000000 00000000 00000000 00000000 | bb 06 || .... .... .... .... || ................ ||
57 | 024c0d60 | 10 | 00000000 00000000 00000000 00000000 | cb 06 || .... .... .... .... || ................ ||
57 | 024c0d70 | 10 | 00000000 00000000 00000000 00000000 | db 06 || .... .... .... .... || ................ ||
57 | 024c0d80 | 10 | 00000000 00000000 00000000 00000000 | eb 06 || .... .... .... .... || ................ ||
57 | 024c0d90 | 10 | 00000000 00000000 00000000 00000000 | fb 06 || .... .... .... .... || ................ ||
57 | 024c0da0 | 10 | 00000000 00000000 00000000 00000000 | 0b 06 || .... .... .... .... || ................ ||
57 | 024c0db0 | 10 | 00000000 00000000 00000000 00000000 | 1b 06 || .... .... .... .... || ................ ||
57 | 024c0dc0 | 10 | 00000000 00000000 00000000 00000000 | 2b 06 || .... .... .... .... || ................ ||
57 | 024c0dd0 | 10 | 00000000 00000000 00000000 00000000 | 3b 06 || .... .... .... .... || ................ ||
57 | 024c0de0 | 10 | 00000000 00000000 00000000 00000000 | 4b 06 || .... .... .... .... || ................ ||
57 | 024c0df0 | 10 | 00000000 00000000 00000000 00000000 | 5b 06 || .... .... .... .... || ................ ||
57 | 024c0e00 | 10 | 00000000 00000000 00000000 00000000 | 6c 06 || .... .... .... .... || ................ ||
57 | 024c0e10 | 10 | 00000000 00000000 00000000 00000000 | 7c 06 || .... .... .... .... || ................ ||
57 | 024c0e20 | 10 | 00000000 00000000 00000000 00000000 | 8c 06 || .... .... .... .... || ................ ||
57 | 024c0e30 | 10 | 00000000 00000000 00000000 00000000 | 9c 06 || .... .... .... .... || ................ ||
57 | 024c0e40 | 10 | 00000000 00000000 00000000 00000000 | ac 06 || .... .... .... .... || ................ ||
57 | 024c0e50 | 10 | 00000000 00000000 00000000 00000000 | bc 06 || .... .... .... .... || ................ ||
57 | 024c0e60 | 10 | 00000000 00000000 00000000 00000000 | cc 06 || .... .... .... .... || ................ ||
57 | 024c0e70 | 10 | 00000000 00000000 00000000 00000000 | dc 06 || .... .... .... .... || ................ ||
57 | 024c0e80 | 10 | 00000000 00000000 00000000 00000000 | ec 06 || .... .... .... .... || ................ ||
57 | 024c0e90 | 10 | 00000000 00000000 00000000 00000000 | fc 06 || .... .... .... .... || ................ ||
57 | 024c0ea0 | 10 | 00000000 00000000 00000000 00000000 | 0c 06 || .... .... .... .... || ................ ||
57 | 024c0eb0 | 10 | 00000000 00000000 00000000 00000000 | 1c 06 || .... .... .... .... || ................ ||
57 | 024c0ec0 | 10 | 00000000 00000000 00000000 00000000 | 2c 06 || .... .... .... .... || ................ ||
57 | 024c0ed0 | 10 | 00000000 00000000 00000000 00000000 | 3c 06 || .... .... .... .... || ................ ||
57 | 024c0ee0 | 10 | 00000000 00000000 00000000 00000000 | 4c 06 || .... .... .... .... || ................ ||
57 | 024c0ef0 | 10 | 00000000 00000000 00000000 00000000 | 5c 06 || .... .... .... .... || ................ ||

   - FO - Function option: 0x00 squelch off, 0x01 Call all, 0x02 Emergency Alarm, 0x03 Remotely Kill, 
                           0x04 Remotely Stun, 0x05 Remoteley Wake Up, 0x06 Group Call
   - DR - Decoding Response: 1 byte 0x00 -> None, 0x01 -> Beep Tone, 0x02 -> Beep Tone & Respond
   - LI - Length of ID: 1 byte
   - II - Information ID: 1 byte per character, max 12 characters.
   - FN - Function name: ASCII, max 7 bytes, 0 terminated.

Start at 0x024c0d00. 32 bytes per record, 16 records total. So end of last record at 0x0024c0eff. Empty records will be 0 everywhere.
```


### 5 tone and DTMF general settings (0x024c1000)
```
5 Tone:

57 | 024c1000 | 10 | c05d6829 502d9c31 b036c43b 3c417c47 | 8b 06 || À]h) P-.1 °6Ä; <A|G || À]h)P-.1°6Ä;<A|G ||
                     ???????? ???????? ???????? ????????
57 | 024c1010 | 10 | 204ef055 606da41f e4259222 90655424 | eb 06 ||  NðU `m¤. ä%." .eT$ ||  NðU`m¤.ä%.".eT$ ||
                     ???????? ???????? ???????? ????????

57 | 024c1020 | 10 | 00020005 46030805 00010000 14006401 | 65 06 || .... F... .... ..d. || ....F.........d. ||
                       DRDSLI DTSISISI SISISISI TLPIARDF
57 | 024c1030 | 10 | 010d0f00 14320100 00000000 00000000 | 02 06 || .... .2.. .... .... || .....2.......... ||
                     CS??SCST DTFDPT
57 | 024c1040 | 10 | 00000746 1234567e 00000000 00000000 | 15 06 || ...F .4V~ .... .... || ...F.4V~........ ||
                       ESLITI ISISISIS ISISISIS ISISISIS
57 | 024c1050 | 10 | 00000000 00000000 00000000 00000000 | be 06 || .... .... .... .... || ................ ||
57 | 024c1060 | 10 | 00000646 75321000 00000000 00000000 | d1 06 || ...F u2.. .... .... || ...Fu2.......... ||
                       ESLITI IEIEIEIE IEIEIEIE IEIEIEIE
57 | 024c1070 | 10 | 00000000 00000000 00000000 00000000 | de 06 || .... .... .... .... || ................ ||
   
   - DR - Decoding Response: 1 byte 0x00 -> None, 0x01 -> Beep Tone, 0x02 -> Beep Tone & Respond
   - DS . Decode Standard: 1 byte 0x00 -> ZVEI1. 0x01 -> ZWEI2, ... todo: make list
   - LI - Length of ID, 1 byte
   - DT - Decode Time: 1 byte, resolution 1ms, valid range 30..100 ms. (0x46 = 70ms)   
   - SI - Self Id: max 7 byte

   - TL - Time-Lapse After Encode: 1 byte, time = rawvalue * 10 ms (valid range 10 .. 2550 ms)
   - PI - PTT ID: 1 byte, 0x00 -> off, 0x09 -> 9 (valid range 5 (0x5) .. 75 (0x4B))
   - AR - Auto Reset Time: 1 byte, time = rawvalue / 10 s (valid range 0 .. 25 s, resolution 1/10s)
   - DF - First Delay: 1 byte, time = rawvalue * 10 ms (valid range 10 .. 2550 ms)

   - SS - Side Tone: 1 byte, 0x00 -> disable, 0x01 -> enable
   - ?? - 1 byte UNCLEAR!
   - SC - Stop Code: 1 byte, off -> 0x00,  0x0b -> 'B', 0x0c -> 'C', 0x0d -> 'D', 0x0e -> 'E', 0x0f -> 'F'
   - ST - Stop Time: 1 byte. time = rawvalue * 10ms
   - DT - Decode Time: 1 byte, time = rawvalue * 10 ms (valid range 0 .. 2000 ms)
   - FD - First Delay Time After Stop: 1 byte, time = rawvalue * 10 ms
   - PT - Pretime: 1 byte, time = rawvalue * 10 ms (valid range 10 .. 2550 ms)

   - ES - Encoding standard. 0x00 -> ZWEI1, 0x01 -> ZVEI2, 0x01 -> ZVEI2, ... TBD: make list
   - LI - Length of ID, 1 byte
   - TI - Time of encode tone: 1 byte, resolution 1ms, valid range 30..100 ms. (0x46 = 70ms)
   - IS - PTT ID Starting (BOT) Encode ID: BCD coded, max. 12 bytes/24 chars, uneven ID padded with one 'e' than 0?
   
   - ES - Encoding standard. 0x00 -> ZWEI1, 0x01 -> ZVEI2, 0x01 -> ZVEI2, ... TBD: make list
   - LI - Length of ID?
   - TI - Time of encode tone: 1 byte, resolution 1ms, valid range 30..100 ms. (0x46 = 70ms).
   - IE - PTT ID Ending (EOT) Encode ID: BCD coded, max. 12 bytes/24 chars, uneven ID padded with one 'e' than 0?

   
DTMF:

57 | 024c1080 | 10 | 0e0a0032 14640100 00001400 00000000 | c5 06 || ...2 .d.. .... .... || ...2.d.......... ||
57 | 024c1080 | 10 | 0f0d0238 19800102 0300f90c 010d0000 | f6 06 || ...8 .... ..ù. .... || ...8......ù..... ||
                     INGCDRPT FDARSISI SISTTLPI PPDC

   - IN - DTMF Interval Character: 0x0a -> A, 0x0b -> B, 0x0c -> C, 0x0d -> D, 0x0e -> *, 0x0f -> #
   - GC - Group Code: 1 byte, 0x00 -> off, 0x0a -> A, 0x0b -> B, 0x0c -> C, 0x0d -> D, 0x0e -> *, 0x0f -> #
   - DR - Decoding Response: 1 byte, 0x00 -> off, 0x01 -> Beep Tone, 0x02 -> Beep Tone & Respond
   - PT - Pretime: 1 byte, time = rawvalue * 10 ms (valid range 10 .. 2500 ms)
   - FD - First Digit Time: 1 byte, time = rawvalue * 10 ms (valid range 0 .. 2500 ms)
   - AR - Auto Reset Time: 1 byte, time = rawvalue / 10 s (valid range 0 .. 25 s, resolution 1/10s)
   - SI - Self ID: max 3 bytes, unused character paddding by 0x00
   - TL - Time laps after encode: 1 byte, time = rawvalue * 10 ms (valid range 10 .. 2500 ms)
   - PI - PTT ID Pause Time: 1 byte, time = rawvalue * 1 s (valid range 0 (off) .. 12 s)
   - PP - PTT ID: 0x00 -> off, 0x01 -> on
   - DC - D Code Pause: 1 byte, time = rawvalue * 1 s (valid range 0 (off) .. 16 s)
   - ST - Side Tone: 0x00 -> off, 0x01 -> on
                                         
57 | 024c1090 | 10 | 01020304 05060708 09000102 03040506 | 40 06 || .... .... .... .... || ................ ||

   - PTT ID Starting (BOT): max. 16 characters, 0x00 .. 0x09, 0xff padded at the end

57 | 024c10a0 | 10 | 06050403 02010009 08070605 04030201 | 50 06 || .... .... .... .... || ................ ||
   
   - PTT ID Ending (EOT): max. 16 characters, 0x00 .. 0x09, 0xff padded at the end

57 | 024c10b0 | 10 | 06060606 06060606 06060606 0606ffff | 70 06 || .... .... .... ..ÿÿ || ..............ÿÿ ||

   - Remotely Kill: max. 14 characters, 0x00 .. 0x09, 0xff padded at the end

57 | 024c10c0 | 10 | 09080706 05040302 01000102 0304ffff | 63 06 || .... .... .... ..ÿÿ || ..............ÿÿ ||

   - Remotely Stun: max. 14 characters, 0x00 .. 0x09, 0xff padded at the end

```


## 2 Tone Encode (0x024c1100)

**2 Encode general settings are NOT exported to .cvx files by CPS!!**

```
57 | 024c1100 | 10 | 910c4124 00000000 686f7273 74000000 | a1 06 || ..A$ .... hors t... || ..A$....horst... ||
                     11112222          NANANANA NANANA
                     
  - 11 - 1st Tone Frequency: 2bytes, low byte first, freq = rawvalue / 10 Hz
  - 22 - 2nd Tone Frequency: 2bytes, low byte first, freq = rawvalue / 10 Hz
  - NA - Name: ASCII, up to 7 bytes, pad with 0x00 if shorter

[...] 
```
Start at 0x024c1100, 24 entries max, 16 bytes per entry, one after another. Last entry therefore ends at 0x024c127f.
Empty entries will not be written.


## 2 Tone encodings used

1 bit for every used 2 tone decoding. 0 -> memory is free, 1 -> memory in use. Bit field for each entry. Max. 24 entries.
```
57 | 024c1280 | 10 | 03008000 00000000 00000000 00000000 | 73 06 || .... .... .... .... || ................ ||
                     ^^^^^^
```

## General 2 Tone Encoding settings (0x024c1290)
```
57 | 024c1290 | 10 | 00000000 00000000 0005050a 0a640100 | 83 06 || .... .... .... .d.. || .............d.. ||
                                         1D2DLD GAARST
                                         
   - 1D - 1st Tone Duration: 1 byte, duration = rawvalue / 10 s. Valid from 0.5 s .. 10 s.
   - 2D - 1st Tone Duration: 1 byte, duration = rawvalue / 10 s. Valid from 0.5 s .. 10 s. 
   - LD - Long Tone Duration: 1 byte, duration = rawvalue / 10 s. Valid from 0.5 s .. 10 s.
   - GA - Gap Time: 1 byte, duration = rawvalue * 10 ms. Valid from 0 ... 2000 ms, resolution 100 ms.
   - AR - Auto Reset Time: 1 byte, time = rawvalue/10 s. Valid from 0.0 .. 25.0s, resolution 0.1s.
   - ST - Side Tone: 1 byte, 0x00 -> disabled, 0x01 -> enabled

```



## Zones used (0x024c1300)

1 bit for every used zone. 0 -> zone is free, 1 -> zone in use. Max. 250 zones.

```
57 | 024c1300 | 10 | 6fff1700 e0bfffbf 01000000 00000000 | 54 06 || oÿ.. à¿ÿ¿ .... .... || oÿ..à¿ÿ¿........ ||
57 | 024c1310 | 10 | 00000000 00000000 00000000 00000002 | 83 06 || .... .... .... .... || ................ ||
```


## Radio id list entries used (024c1320)

1 bit for every used radio id. 0 -> memory is free, 1 -> memory in use. Max. 250 entries.
```
57 | 024c1320 | 10 | 01000000 00000000 00000000 00000000 | 92 06 || .... .... .... .... || ................ ||
57 | 024c1330 | 10 | 00000000 00000000 00000000 00000002 | a3 06 || .... .... .... .... || ................ ||
```

## Scanlists used (0x024c1340)

1 bit for every used scanlist. 0 -> scanlist is free, 1 -> scanlist in use. Max. 250 scanlists.

```
57 | 024c1340 | 10 | bfffff0b 00000000 00000000 00000000 | 79 06 || ¿ÿÿ. .... .... .... || ¿ÿÿ............. ||
57 | 024c1350 | 10 | 00000000 00000000 00000000 00000002 | c3 06 || .... .... .... .... || ................ ||

Byte 1: 0xbf = b10111111 -> scanlist 7 not used
Byte 4; 0x0b = b00001011 -> scanlist 25, 26, 28 used, 27 not used
Byte 8: 0x02 = b10000010 -> scanlist 250 used. (8 bit/byte * 31 bytes before + 2nd bit in byte 32 = 250)
```

## Alarm Settings (0x024c1400)

```
57 | 024c1400 | 10 | 03010f0a ff013909 00fe0005 0a0a400c | 34 06 || .... ÿ.9. .þ.. ..@. || ....ÿ.9..þ....@. ||
                     EAETEIAT DTDRCICI ESECDADT TXRXDCDC
                     
   - EA - Emergency Alarm (Analog Alarm): 0x00 -> Alarm, 0x01 -> Transpond+Background, 0x02 -> Transpond+Alarm, 0x03 -> Both
   - ENI Type Select (Analog Alarm): 0x00 -> None, 0x01 -> DTMF, 0x02 -> 5Tone
   - EI - Emergency ID (Analog Alarm):
       For ENI Type Select DTMF: ID in DTMF Encode List: 0x00 -> 1 .. 0x0f -> 16
       For ENI Type Select 5 Tone: ID in 5-Tone Encode List: 0x00 -> 1 .. 0x63 -> 100
   - AT: Alarm Time Analog Alarm): valid range 0x01 (1s) .. 0xff (255s), available only for "Alarm"
   
   - DT - Duration of TX (Analog Alarm): range 0x01 (1s) .. 0xff (255s)
   - DR - Duration of RX (Analog Alarm): range 0x01 (1s) .. 0xff (255s)
   - CI - Emergency Channel (Analog Alarm): 2 bytes, low byte first, channel id, analog channels only
   
   - ES - Emergency ENI Send Select (Analog Alarm): 0x00 -> Assigned Channel, 0x01 -> Selected Channel
   - EC - Emergency Cycle (Analog Alarm): 0x00 -> Continuous, range 0x01 -> 1 .. 0xff -> 255
   - DA - Emergency Alarm (Digital Alarm): 0x00 -> Alarm, 0x01 -> Transpond+Background, 0x02 -> Transpond+NoLocalAlarm, 0x03 -> Transpond+LocalAlarm
   - DT - Alarm Time (Digital Alarm): range 0x01 (1s) .. 0xff (255s)
   
   - TX - Duration of TX (Digital Alarm): range 0x01 (1s) .. 0xff (255s)
   - RX - Duration of RX (Digital Alarm): range 0x01 (1s) .. 0xff (255s)
   - DC - Emergency Channel (Digital Alarm): 2 bytes, low byte first, channel id, digital channels only
   
57 | 024c1410 | 10 | 01010909 00000000 00000000 00000000 | 96 06 || .... .... .... .... || ................ ||
                     ESECVSAS MSRA
                     
   - ES - Emergency ENI Send Select (Digital Alarm): 0x00 -> Assigned Channel, 0x01 -> Selected Channel                     
   - EC - Emergency Cycle (Digital Alarm): 0x00 -> Continuous, range 0x01 -> 1 .. 0xff -> 255
   - VS - Voice switch broadcast (Work Alone): valid range 0x00 (1m) .. 0xff (256m)
   - AS - Area switch broadcast (Work Alone): valid range 0x00 (1m) .. 0xff (256m)
   
   - MS - Mic broadcast (Work Alone): 0x00 -> Key, 0x01 -> Voice Transmit
   - RA - Receive Alarm (Digital Alarm): 0x00 -> off, 0x00 -> on

57 | 024c1440 | 10 | 02000000 00000000 00000000 00000000 | b4 06 || .... .... .... .... || ................ ||
                     CT

   - CT - Call Type (Digital Alarm): 0x00 -> Pricate Call,  0x01 -> Group Call, 0x02 -> All Call
                     
57 | 024c1450 | 10 | 00000000 00000000 00000000 00000000 | c2 06 || .... .... .... .... || ................ ||
57 | 024c1460 | 10 | 00000012 34561900 00000000 00000000 | 87 06 || .... 4V.. .... .... || ....4V.......... ||
                           DI DIDIDI

   - DI . TG/DMR ID (Digital Alarm): BCD coded, max 8 characters
```

## Auto Repeater Offset Frequencies (0x024c2000)

4 bytes per offset, low byte first, 250 entries. Resolution 10 Hz.

```
57 | 024c2000 | 10 | 60ea0000 c0980b00 e0570e00 00000000 | 70 06 || `ê.. À... àW.. .... || `ê..À...àW...... ||
                     Offset 1 Offset 2 Offset 3 Offset 4

[...]

57 | 024c23e0 | 10 | 00000000 30251a00 00000000 00000000 | d0 06 || .... 0%.. .... .... || ....0%.......... ||
                     Offs.249 Offs.250

0xea60 = 60000 => 600000 Hz => 600 Khz
0x000b98c0 = 760000 => 7.6 Mhz
0xe57e0 = 940000 => 9.4 Mhz
(0x1a2530 = 17.13456 Mhz)
```


## 2 Tone Decode (0x024c2400)
**2 Tone Decode data are NOT exported to .cvx files by CPS!!**

```
57 | 024c2400 | 10 | 910c4124 00000000 00000000 00000000 | 84 06 || ..A$ .... .... .... || ..A$............ ||
                     11112222 DRNANANA NANANANA
57 | 024c2410 | 10 | 00000000 00000000 00000000 00000000 | 92 06 || .... .... .... .... || ................ ||

  - 11 - 1st Tone Frequency: 2bytes, low byte first, freq = rawvalue / 10 Hz
  - 22 - 2nd Tone Frequency: 2bytes, low byte first, freq = rawvalue / 10 Hz
  - DR - Decoding Resonse: 1 byte, 0x00 -> none, 0x01 -> Beep Tone, 0x02 Beep Tone and Respond
  - NA - Name: ASCII, up to 7 bytes, pad with 0x00 if shorter

57 | 024c2420 | 10 | 00000000 00000000 00000000 00000000 | a2 06 || .... .... .... .... || ................ ||
=> Block 127: 
=> Size: 0x24c2400 .. 0x24c242f: 48 bytes

[...]

57 | 024c25e0 | 10 | 400bb80b 01626565 70000000 00000000 | 0e 06 || @.¸. .bee p... .... || @.¸..beep....... ||
57 | 024c25f0 | 10 | 00000000 00000000 00000000 00000000 | 73 06 || .... .... .... .... || ................ ||
```
Start at 0x024c2400. 32 bytes per entry, 24 entries max, one after another. Last entry therefore ends at 0x024c25ff. 

Empty entries will not be written. 

## 2 Tone decodings used (024c2600)
1 bit for every used 2 tone decoding. 0 -> memory is free, 1 -> memory in use. Max. 16 entries.
```
57 | 024c2600 | 10 | 01e00000 00000000 00000000 00000000 | 65 06 || .à.. .... .... .... || .à.............. ||
                     ^^^^
```

## Power on and other optional settings (0x02500000)
```
57 | 02500000 | 10 | 00000000 00000101 04020200 000f0104 | 80 06 || .... .... .... .... || ................ ||
                     KTDMKLAS TOLAPIPA FSSASBPS VLVDVSMG
   - KT - Key Tone (Alert Tone): 0x00 -> off, 0x01 -> Ring
   - DM - Display Mode (Work Mode): 0x00 -> Channel, 0x01 -> Frequency
   - KL - Key Lock (Key Function): 0x00 -> Man, 0x01 -> Auto
   - AS - Auto Shutdown: 0x00 -> Off, 0x01 -> 10 min, 0x02 -> 30 min, 0x03 -> 60 min, 0x04 -> 120 min
   
   - TO - TOT (Other): 0x00 -> Off, value = rawvalue * 30s, valid range 0x01 (30s) .. 0x08 (240s)
   - LA - Language (Other): 0x00 -> English, 0x01 -> German
   - PI - Power on interface: 0x00 -> Default interface, 0x01 -> Custom Char, 0x02 -> Custom Picture
   - PA - Power on password set: 0x00 -> no password, 0x01 password active. 
          If password is set the radio cannot communicate to CPS if _unlocked_!! If device is still locked, CPS communicates!
          
   - FS - Frequency Step (Other): 0x00 -> 2.5 Khz, 0x01 -> 5Khz, 0x02 -> 6.25 Khz, 0x03 -> 10 Khz, 
                                  0x04 -> 12.5 Khz, 0x05 -> 20 Khz, 0x06 -> 25 Khz, 0x07 -> 30 Khz, 0x08 ->  50 Khz
   - SA - SQL Level(A) (Other): 0x00 -> off, range 0x01 (1) .. 0x05 (5)
   - SB - SQL Level(B) (Other): 0x00 -> off, range 0x01 (1) .. 0x05 (5)   
   - PS - Power save: 0x00 -> Off, 0x01 -> 1:1, 0x02 -> 2:1
   
   - VL - VOS Level (VOX/BT): 0x00 -> off, 0x01 -> 1, 0x02 -> 2, 0x03 -> 3
   - VD - VOX Delay (VOX/BT): 1 byte, value = rawvalue * 0.1s + 0.5s, valid range: 0x00 (0.5s) .. 0x19 (3.0s)
   - VS - VFO Scan Type: 0x00 -> TO, 0x01 -> CO, 0x02 -> SE
   - MG - Mic gain: 1 byte, valid range 0x00 -> 1 .. 0x04 -> 5
   
57 | 02500010 | 10 | 1c210213 08000000 0003030a 0a000001 | e7 06 || .!.. .... .... .... || .!.............. ||
                     S1S2S3S4 S5VAVBST SNGHPHPT WHFWFVMA

   - S1 - PF1 Short Key (Key Function): 1 byte, key list see below
   - S2 - PF2 Short Key (Key Function): 1 byte, key list see below
   - S3 - PF3 Short Key (Key Function): 1 byte, key list see below
   - S4 - P1 Short Key (Key Function): 1 byte, key list see below
   
   - S5 - P2 Short Key (Key Function): 1 byte, key list see below
   - VA - VF/MR(A) (Work Mode): 0x00 -> MEM, 0x01 -> VFO
   - VB - VF/MR(B) (Work Mode): 0x00 -> MEM, 0x01 -> VFO   
   - ST - STE Type Of CTCSS (STE): 0x00 -> Off, 0x01 -> Silent, 0x02 -> 120 Degree, 0x03 -> 180 Degree, 0x04 -> 240 Degree
   
   - SN - STE When No Signal: 0x00 -> Off, 0x01 55.2 Hz, 0x02 -> 259.2 Hz
   - GH - Group Call Hold Time (Digital Func): valid range: 0x01 (1s) .. 0x1e (30s), 0x1f (30 min), 0x20 (infinite)
   - PH - Person Call Hold Time (Digital Func): valid range: 0x01 (1s) .. 0x1e (30s), 0x1f (30 min), 0x20 (infinite)
   - PT - Prewave Time (Digital Func): value = rawvalue * 20ms, valid range 0x00 (0ms) .. 0x32 (5000ms)
   
   - WH - Wake Head Period (Digital Func): value = rawvalue * 20ms, valid range 0x00 (0ms) .. 0x32 (5000ms)
   - FW - FM Work Channel: 1 byte, id out fm channel list, valid range: 0x00 (1) .. 0x63 (100). Channel must be used.
   - FV - FM VFO/MEM: 1 byte: 0x00 -> MEM, 0x01 -> VFO
   - MA - MEM Zone(A) (Work Mode): 1 byte, zone id


57 | 02500020 | 10 | 06000002 00000400 00010100 01000201 | 94 06 || .... .... .... .... || ................ ||
                     MB  RFDT MD  DBBD GPSA??FM MCSMTBCA

   - MB - MEM Zone(B) (Work Mode): 1 byte, zone id   
   - RF - Record Function: 0x00 -> off, 0x01 -> on
   - DT - DTMF Transmitting Time: 1 bybte, 0x00 -> 50 ms, 0x01 -> 100 ms, 0x02 -> 200 ms, 0x03 -> 300ms, 0x04 -> 500 ms
   
   - MD . Man Down (Alarm Settings): 0x00 -> Off, 0x01 -> On
   - DB - Display Brightness: 1 byte, 0x00 -> 1 .. 0x04 -> 5
   - BD - Auto Backlight Duration: 1 byte: 0x00 -> Always, 0x01 -> 5s, 0x02 -> 10s, 0x03 -> 15s, 0x04 -> 20s, 0x05 -> 25s, 0x06 -> 30s, 0x07 -> 1m
                                           0x08 -> 2m, 0x09 -> 3m, 0x0a -> 4m, 0x0b -> 5m, 0x0c -> 15m, 0x0d -> 30m, 0x0e -> 45m, 0x0f -> 60m
   - GP - GPS: 0x00 -> off, 0x01 -> on
   - SA - SMS Alert (Alert Tone): 0x00 -> off, 0x01 -> Ring
   - FM - FM Monitor: 0x00 -> off, 0x01 -> on
   - MC - Main Channel Set (Work Mode): 0x00 -> A, 0x01 -> B
   - SM - Sub-Channel Mode: 0x00 -> off, 0x01 -> on
   - TB - TBST: 0x00 -> 1000 Hz, 0x01 -> 1450 Hz, 0x02 -> 1750 Hz, 0x03 -> 2100 Hz
   - CA - Call Alert (Alert Tone): 0x00 -> None, 0x01 -> Ring
   
57 | 02500030 | 10 | 0e010002 0000010b 00000005 00000101 | b6 06 || .... .... .... .... || ................ ||
                     TZCTDRVD WM  ITME FOSSEPMV SK  RMGG
                                             
   - TZ: Time Zone: 0x00 -> GMT-12 ... 0x0c -> GMT0 ...  0x0e -> GMT2 ... 0x19 -> GMT13
   - CT: Call Tone (Call Alert): 0x00 -> Off, 0x01 -> Digital, 0x02 -> Analog, 0x03 -> Digital&Analog
   - DR: Digi Call ResetTone: 0x00 -> off, 0x01 -> on
   - VD: VOX Detection (VOX/BT): 0x00 -> Built-in Microphone, 0x01 -> External Microphone, 0x02 -> Both

   - WM: choose working mode (Other): 0x00 -> amateur mode, 0x01 -> professional mode
   - IT: Idle Channel Tone (Alert Tone): 0x00 -> off, 0x01 -> on
   - ME: Menu Exit Time: 1 byte, value = rawvalue * 5s + 5s, valid range: 0x00 (5s) .. 0x0b (60s)

   - FO; Filter Own ID in MissCall (Digital Func): 0x00 -> off, 0x01 -> on
   - SS: Startup Sound (Alert Tone): 0x00 -> off, 0x01 -> on
   - EP: Call End Prompt Box: 0x00 -> off, 0x01 -> on
   - MV: Max volume: 0x00 -> "Indoors", 0x01 .. 0x08 possible.

   - SK: Digital Remote Stun&&Kill (Digital Func): 0x00 -> off, 0x01 -> on
   - RM: Remote Monitor (Digital Func): 0x00 -> off, 0x01 -> on
   - GG: Get GPS Positioning: 0x00 -> off, 0x01 -> on


57 | 02500040 | 10 | 0127300a 1d220101 02000000 00030000 | 4a 06 || .'0. .".. .... .... || .'0..".......... ||
                       L1L2L3 L4L5LTVC RADMCCID MSLC  MD

   - L1 - PF1 Long Key (Key Function): 1 byte, key list see below
   - L2 - PF2 Long Key (Key Function): 1 byte, key list see below
   - L3 - PF3 Long Key (Key Function): 1 byte, key list see below
   
   - L4 - P1 Long Key (Key Function): 1 byte, key list see below
   - L5 - P2 Long Key (Key Function): 1 byte, key list see below
   - LT - Long Key Time (Key Function): 1 byte, range 0x00 (1s) .. 0x04 (5s)
   - VC: Volume Change Prompt (Alert Tone): 0x00 -> off, 0x01 -> on
   
   - RA: Auto Repeater A (Auto repeater): 0x00 -> off, 0x01 -> Positive, 0x02 -> Negative
   - DM: Digital Monitor (Digital Func): 0x00 -> Off, 0x01 -> Single Slot, 0x02 -> Double Slot
   - CC: Digital Monitor CC (Digital Func): 0x00 -> Any, 0x01 -> Same
   - ID: Digital Monitor ID (Digital Func): 0x00 -> Any, 0x01 -> Same
   
   - MS: Monitor Slot Hold (Digital Func): 0x00 -> off, 0x01 -> on
   - LC: Last Caller: 1 byte, 0x00 -> off, 0x01 -> Display ID, 0x02 -> Display Callsign, 0x03 -> Show Both
   
   - MD: Man Down Delay (Alarm Settings): 0x00 (0s) .. 0xff (255s)


57 | 02500050 | 10 | 01010001 00000001 005a6202 006cdc02 | be 06 || .... .... .Zb. .lÜ. || .........Zb..lÜ. ||
                     CHTDMH         ES VFOSSUHF VFOESUHF          

   - CH: Analog Call Hold Time (Other): 1 byte, valid range 0x00 (0s) .. 0x1e (30s), step 1s
   - TD: Time Display: 0x00 -> off, 0x01 -> on
   - MH: Max headphone volume: 0x00 -> "Indoors", 0x01 .. 0x08 possible.
   
   - ES: Enhance Sound quality: 0x00 -> off, 0x01 -> on
   
   - VFOSSUHF: VFO Scan Start Freq (UHF): 4 bytes, low byte first, resolution 10 Hz
   
   - VFOESUHF: VFO Scan End Freq (UHF): 4 bytes, low byte first, resolution 10 Hz
```
### Key list 

CPS does not allow each value for each key!!!

Off - 0x00,
Voltage - 0x01,
Power - 0x02,
Repeater - 0x03,
Reverse - 0x04,
Digital Encryption - 0x05,
Call - 0x06,
Vox - 0x07,
V/M - 0x08,
Sub PTT - 0x09,
Scan - 0x0a,
FM - 0x0b,
Alarm - 0x0c,
Record Switch - 0x0d,
Record - 0x0e,
SMS - 0x0f,
Dial - 0x10,
GPS Information - 0x11 ?? Not selectable in CPS!,
Monitor - 0x12,
Main Channel Switch - 0x13,
Hot Key 1 - 0x14,
Hot Key 2 - 0x15,
Hot Key 3 - 0x16,
Hot Key 4 - 0x17,
Hot Key 5 - 0x18,
Hot Key 6 - 0x19,
Work Alone - 0x1a,
Nuisance Delete 0x1b,
Digital Monitor - 0x1c,
Sub CH Switch - 0x1d,
Priority Zone - 0x1e,
VFO Scan - 0x1f,
MIC Sound Quality - 0x20,
LastCall Reply - 0x21,
Channel Type Switch - 0x22,
Ranging - 0x23 ?? Not selectable in CPS!,
Roaming - 0x24,
Channel Ranging - 0x25 ?? Not selectable in CPS!,
Max Volume - 0x26,
Slot Switch - 0x27,
APRS Type Switch - 0x28 ?? Not selectable in CPS!,
Zone Select - 0x29,
Timed Roaming Set - 0x2a,
APRS Set - 0x2b ?? Not selectable in CPS!,
Mute timing - 0x2c,
CTC/DCS Set - 0x2d,
TBST Send - 0x2e,
Bluetooth - 0x2f,
Gps - 0x30,
Ch.Name - 0x31,
CDT Scan - 0x32

```
57 | 02500060 | 10 | 0085cf00 c0800901 01000000 00000100 | 62 06 || ..Ï. À... .... .... || ..Ï.À........... ||
                     VFOSSVHF VFOESVHF 1U1V         MAPA
                     
   - VFOSSVHF - VFO Scan Start Freq (VHF): 4 bytes, low byte first, resolution 10 Hz
   - VFOESVHF - VFO Scan End Freq (VHF): 4 bytes, low byte first, resolution 10 Hz
   - 1U - Auto Repeater1 (UHF): 1 byte, auto repeater offset id, 0xff for Off
   - 1V - Auto Repeater1 (VHF): 1 byte, auto repeater offset id, 0xff for Off
   - MA - call channel is maintained (Other): 0x00 -> Off, 0x01 -> On
   - PA - Priority Zone A (Other): 0x00 -> Off, range 0x01 (1) .. 0xf9 (250) with gaps in CPS!
                     
57 | 02500070 | 10 | 00012206 10042206 28050000 04000400 | 6c 06 || ..". ..". (... .... || .."...".(....... ||
                     PB  CT#1 CT#2CT#3 CT#4CT#5 PE#1PE#2

57 | 02500080 | 10 | 04000400 0a008e03 00000000 00000000 | 85 06 || .... .... .... .... || ................ ||
                     PE#3PE#4 PE#5IT#1 IT#2IT#3 IT#4IT#5

   - PB - Priority Zone B (Other): 0x00 -> Off, range 0x01 (1) .. 0xf9 (250) with gaps in CPS!
   - CT#1 - Call Tone, First Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - CT#2 - Call Tone, Second Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.   
   - CT#3 - Call Tone, Third Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.      
   - CT#4 - Call Tone, Fourth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.         
   - CT#5 - Call Tone, Fifth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.         
   - PE#1 - Call Tone, First Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - PE#2 - Call Tone, Second Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - PE#3 - Call Tone, Third Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - PE#4 - Call Tone, Fourth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - PE#5 - Call Tone, Fifth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - IT#1 - Idle Channel Tone, First Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - IT#2 - Idle Channel Tone, Second Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - IT#3 - Idle Channel Tone, Third Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - IT#4 - Idle Channel Tone, Fourth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - IT#5 - Idle Channel Tone, Fifth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   
57 | 02500090 | 10 | 05000a00 05000a00 0a007503 75032206 | 32 06 || .... .... ..u. u.". || ..........u.u.". ||
                     IP#1IP#2 IP#3IP#4 IP#5CR#1 CR#2CR#3

   - IP#1 - Idle Channel Tone, First Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - IP#2 - Idle Channel Tone, Second Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - IP#3 - Idle Channel Tone, Third Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - IP#4 - Idle Channel Tone, Fourth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - IP#5 - Idle Channel Tone, Fifth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - CR#1 - Call Reset Tone, First Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.
   - CR#2 - Call Reset Tone, Second Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.   
     CR#3 - Call Reset Tone, Third Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.         

57 | 025000a0 | 10 | 28050000 14001400 00000000 00000000 | 57 06 || (... .... .... .... || (............... ||
                     CR#4CR#5 RP#1RP#2 RP#3RP#4 RP#5RDCD

   - CR#4 - Call Reset Tone, Fourth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.         
   - CR#5 - Call Reset Tone, Fifth Tone Frequency (Alert Tone): 2 bytes, low byte first, resolution 1 Hz, valid range 300 ... 3000 Hz.         
   - RP#1 - Call Reset Tone, First Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - RP#2 - Call Reset Tone, Second Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - RP#3 - Call Reset Tone, Third Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - RP#4 - Call Reset Tone, Fourth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - RP#5 - Call Reset Tone, Fifth Tone Period (Alert Tone): 2 bytes, low byte first, value = rawvalue * 10ms, valid range 0 .. 200ms
   - RD - Record Delay (Record): 1 byte, value = rawvalue * 0.2s, valid range 0x00 (0.0s) .. 0x19 (5.0s)
   - CD - Call Display Mode: 1 byte, 0x00 -> Turn off Talker Alias, 0x01 -> Call Sign Based, 0x02 -> Name Based


57 | 025000b0 | 10 | 00010000 00fe0000 00000001 00000b00 | 1d 06 || .... .þ.. .... .... || .....þ.......... ||
                                RI     CNDCAIKS CC  LKWT

   - RI - Ranging intervals: 1 byte, valid range 0x05 (5s) .. 0xfe (254 s)

   - CN - Display Channel Number: 0x00 -> Actual Channel Number, 0x01 -> Sequence Number In Zone
   - DC - Display Current Contact: 0x00 -> Off, 0x01 -> On
   - AI - Auto Roaming interval (Auto repeater): 1 byte, 0x00 -> 1, 0xff -> 256m
   - KS - Key Sound Adjustable (Alert Tone): 0x00 -> Adjustable, 0x01 -> 1 .. 0x0f -> 15
   
   - CC - Call Sign Display Color: 1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White
   - LK - Bits ???FS?KN (Key Function):
      - F - Forced Lock Key: 0x00 -> Off, 0x01 -> On
      - S - Side Key Lock: 0x00 -> Off, 0x01 -> On
      - K - Keyboard Lock: 0x00 -> Off, 0x01 -> On
      - N - Knob Lock: 0x00 -> Off, 0x01 -> On
   - WT - Roaming Effect Wait Time (Auto repeater): 1 byte, 0x00 -> None, range 0x01 (1 s) .. 0xff (256 s)


57 | 025000c0 | 10 | 00000000 002bde00 2079de00 c0559c02 | 55 06 || .... .+Þ.  yÞ. ÀU.. || .....+Þ. yÞ.ÀU.. ||
                     SCBPSLSM MINFAR1V MAXFAR1V MINFAR1U

   - SC - Standby Char Color: 1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White
   - BP - Standby BK Picture: 1 byte, 0x00 -> Default, 0x01 -> Custom 1, 0x02 -> Custom 2
   - SL - Show Last Call On Launch: 1 byte: 0x00 -> off, 0x01 -> on
   - SM - SMS Format (Digital Func): 0x00 -> M-SMS, 0x01 -> H-SMS, (0x02 -> DMR Standard not selectable in CPS)
   - MINFAR1V - Min Freq Of Auuto Repeater 1 (VHF) (Auto Repeater): 4 bytes, low byte first, resolution 10 Hz
   - MAXFAR1V - Max Freq Of Auuto Repeater 1 (VHF) (Auto Repeater): 4 bytes, low byte first, resolution 10 Hz
   - MINFAR1U - Min Freq Of Auuto Repeater 1 (UHF) (Auto Repeater): 4 bytes, low byte first, resolution 10 Hz


57 | 025000d0 | 10 | 00639f02 02000001 f900ff0b 00000000 | 3c 06 || .c.. .... ù.ÿ. .... || .c......ù.ÿ..... ||
                     MAXFAR1U RBAB  DC ZAZBCACB RZRCRICR

   - MAXFAR1U - Max Freq Of Auuto Repeater 1 (UHF) (Auto Repeater): 4 bytes, low byte first, resolution 10 Hz
   - RB: Auto Repeater B (Auto repeater): 0x00 -> off, 0x01 -> Positive, 0x02 -> Negative
   - AB: Address Book Is Sent With Its Own Code (Other): 0x00 -> off, 0x01 -> on
   - DC - Default startup channel: 0x00 -> off, 0x01 -> on
   - ZA - Zone A: 1 byte Zone ID
   - ZB - Zone B: 1 byte Zone ID
   - CA - Channel A: number of channel in selected zone. 0xff for VFO.
   - CB - Channel B: number of channel in selected zone. 0xff for VFO.   
   - RZ - Roaming Zone (Auto repeater): 1 byte, roaming zone id
   - RC - Repeater Check (Auto Repeater): 0x00 -> off, 0x01 -> on
   - RI - Repeater Check Interval (Auto Repeater): value = rawvalue * 5s + 5s, valid range 0x00 (5s) .. 0x09 (50s)
   - CR - Repeater Check Reconnections (Auto Repeater): 0x00 -> 3, 0x01 -> 4, 0x02 -> 5
                                    
57 | 025000e0 | 10 | 00000000 01000000 00000001 00000000 | 44 06 || .... .... .... .... || ................ ||
                     TCBTSDKL ACOORDAR   MTRRSG SR
                     
   - TC - Timed Roaming Start Condition (Auto repeater): 0x00 -> Fixed time, 0x01 -> Out Of Range
   - BT - Backlight Delay auf TX (Display): 1 byte, valid range: 0x00 (0s) .. 0x1e (30s)
   - SD - Separate Display (Display): 0x00 -> off; 0x01 -> on
   - KL - CH Switching Keeps Last Caller:  0x00 -> off, 0x01 -> on   
   
   - AC - A Channel Name Color (Display): 1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White
   - OO - Alert Out Of Repeat Range (Auto Repeater): 0x00 -> Off, 0x01 -> Bell, 0x02 -> Voice
   - RD - Receive  Backlight Delay (Display): 0x00 -> Always, 0x01 (1s) .. 0x1e (30s)
   - AR - Auto Roaming (Auto repeater): 0x00 -> off, 0x01 -> on
   
   - MT - Mute Timing (Other): 1 byte, valid range: 0x00 (1min) .. 0xff (256 min)
   - RR - Repeater out of range reminder (time (Auto Repeater): 0x00 -> 1 .. 0x09 -> 10) unit?
   - SG - Startup GPS Test (GPS): 0x00 -> off; 0x01 -> on
   - SR - Startup Reset (Power-On): 0x00 -> off, 0x01 -> on ("Set ON to allow MCU reboot")
                                             
```



## Zone A Channel (0x02500100)

In this memory block the channel A for each zone is stored. The position is calculated by position = 0x0250100 + 2 * [zonenumber]

```
57 | 02500100 | 10 | 00000100 00000500 05000000 08000800 | 7e 06 || .... .... .... .... || ................ ||
                     I000I001 I002I003 I004I005 I006I007

   - Ix: Index of channel in zone, 2 bytes, low byte first. The index refers to the position of a channel in the zone
         this is NOT the index of a channel in the channel list! Default/unused value is 0x02.
```

## Zone B Channel (0x02500300)

In this memory block the channel B for each zone is stored. The position is calculated by position = 0x0250300 + 2 * [zonenumber]

```
57 | 02500300 | 10 | 01000100 09000000 00000b00 0a000a00 | 8f 06 || .... .... .... .... || ................ ||
                     I000I001 I002I003 I004I005 I006I007

   - Ix: Index of channel in zone, 2 bytes, low byte first. The index refers to the position of a channel in the zone
         this is NOT the index of a channel in the channel list! Default/unused value is 0x02.
```


## DTMF Encode List (M1..M16) (0x02500500)

```
57 | 02500500 | 10 | 0d09ffff ffffffff ffffffff ffffffff | 6f 06 || ..ÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ..ÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
                     M1M1M1M1 M1M1M1M1 M1M1M1M1 M1M1M1M1
57 | 02500510 | 10 | 01020304 05060708 09000102 03040506 | b9 06 || .... .... .... .... || ................ ||
                     M2M2M2M2 M2M2M2M2 M2M2M2M2 M2M2M2M2
57 | 02500520 | 10 | ffffffff ffffffff ffffffff ffffffff | 77 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500530 | 10 | ffffffff ffffffff ffffffff ffffffff | 87 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500540 | 10 | ffffffff ffffffff ffffffff ffffffff | 97 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500550 | 10 | ffffffff ffffffff ffffffff ffffffff | a7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500560 | 10 | ffffffff ffffffff ffffffff ffffffff | b7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500570 | 10 | ffffffff ffffffff ffffffff ffffffff | c7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500580 | 10 | ffffffff ffffffff ffffffff ffffffff | d7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 02500590 | 10 | ffffffff ffffffff ffffffff ffffffff | e7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005a0 | 10 | ffffffff ffffffff ffffffff ffffffff | f7 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005b0 | 10 | ffffffff ffffffff ffffffff ffffffff | 07 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005c0 | 10 | ffffffff ffffffff ffffffff ffffffff | 17 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005d0 | 10 | 0dffffff ffffffff ffffffff ffffffff | 35 06 || .ÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || .ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005e0 | 10 | 0effffff ffffffff ffffffff ffffffff | 46 06 || .ÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || .ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
57 | 025005f0 | 10 | 0fffffff ffffffff ffffffff ffffffff | 57 06 || .ÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || .ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||

   - Mx: 0x00 -> 0 ... 0x09 -> 9, 0x0a -> A, 0x0b -> B, 0x0c -> C, 0x0d -> D, 0x0e -> *, 0x0f, -> #

16 bytes per entry, 16 entries (M1...M16). Empty characters are 0xff.
```

## Power On Settings (0x02500600)
```
57 | 02500600 | 10 | 00000000 00000000 00000000 00000000 | 09 06 || .... .... .... .... || ................ ||
                     L1L1L1L1 L1L1L1L1 L1L1L1L1 L1L1
57 | 02500610 | 10 | 00000000 00000000 00000000 00000000 | 39 06 || .... .... .... .... || ................ ||
                     L2L2L2L2 L2L2L2L2 L2L2L2L2 L2L2
57 | 02500620 | 10 | 00000000 00000000 00000000 00000000 | 88 06 || .... .... .... .... || ................ ||
                     PAPAPAPA PAPAPAPA

   - L1 - Power on message line 1: ASCII, max 14 byte, 0x00 for unused characters
   - L2 - Power on message line 1: ASCII, max 14 byte, 0x00 for unused characters
   - PA - Power on Password: ASCII, max. 8 byte, 0x00 for unused characters
```

## ARPS

### General APRS Settings (0x02501000)
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
- FB - Fixed location beacon: 0x00 -> Off (GPS), 0x01 -> On (send fix position)
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
- CT - Call Type 1-8: 0x00 -> Private Call, 0x01 -> Group Call, 0x02 -> All Call; 1 byte each, one after another
- RO - Support for Roaming: 0x00 -> off, 0x01 -> on
- SL - Slot 1-8: 0x00 -> Channel Slot, 0x01 -> Slot 1, 0x02 -> Slot 2, 1 byte, one after another
- RD - Repeater Activation Delay: 0x00 -> off, 0x01 -> 100ms, 0x03 -> 300ms, 0x10 -> 1000ms
```

Other expected values: "APRS TG","Call Type"


### APRS Sending Text (0x02501200)

```
57 | 02501200 | 10 | 37332044 4520444c 39434154 00000000 | 48 06 || 73 D E DL 9CAT .... || 73 DE DL9CAT.... ||
57 | 02501210 | 10 | 00000000 00000000 00000000 00000000 | 84 06 || .... .... .... .... || ................ ||
57 | 02501220 | 10 | 00000000 00000000 00000000 00000000 | 94 06 || .... .... .... .... || ................ ||
57 | 02501230 | 10 | 00000000 00000000 00000000 00000000 | a4 06 || .... .... .... .... || ................ ||
```

CPS supports up to 60 Bytes sending text.

## GPS Template Information text (0x02501280)

```
57 | 02501280 | 10 | 54656d70 6c617465 3a000000 00000000 | 6a 06 || Temp late :... .... || Template:....... ||
                     TETETETE TETETETE TETETETE TETETETE
57 | 02501290 | 10 | 00000000 00000000 00000000 00000000 | 04 06 || .... .... .... .... || ................ ||
                     TETETETE TETETETE TETETETE TETETETE

   - TE - Text: ASCII, max 32 characters, unused = 0x00
                     
```

## more optional settings  (0x02501400)
```
57 | 02501400 | 10 | 00000000 00000000 00000000 00000000 | 76 06 || .... .... .... .... || ................ ||
                     TA

   - TA - Send Talker Alias (Talk Alias): 0x00 -> off, 0x01 -> on


57 | 02501410 | 10 | 00000000 00000000 00000000 00000000 | 86 06 || .... .... .... .... || ................ ||
                                                    APAD

   - AP - Alias Display Priority (Talk Alias): 0x00 -> off, 0x01 -> Contact Alias, 0x02 -> Air Alias
   - AD - Alias Data Format (Talk Alias): 0x00 -> ISO 8, 0x01 -> ISO 7, 0x02 -> Unicode

57 | 02501420 | 10 | 000002ff 0085cf00 c0800901 c2199f02 | b1 06 || ...ÿ ..Ï. À... Â... || ...ÿ..Ï.À...Â... ||
                         2U2V MINFAR2V MAXFAR2V MINFAR2U
                         
   - 2U - Auto Repeater2 (UHF): 1 byte, auto repeater offset id, 0xff for Off
   - 2V - Auto Repeater2 (VHF): 1 byte, auto repeater offset id, 0xff for Off
   - MINFAR2V - Min Freq Of Auuto Repeater 2 (VHF): 4 bytes, low byte first, resolution 10 Hz
   - MAXFAR2V - Max Freq Of Auuto Repeater 2 (VHF): 4 bytes, low byte first, resolution 10 Hz
   - MINFAR2U - Min Freq Of Auuto Repeater 2 (UHF): 4 bytes, low byte first, resolution 10 Hz

57 | 02501430 | 10 | 3c599f02 00026401 01000000 00000000 | 44 06 || <Y.. ..d. .... .... || <Y....d......... ||
                     MAXFAR2U   GMSTMG MPBCETTP TGCACBAK

   - MAXFAR2U - Max Freq Of Auuto Repeater 2 (UHF): 4 bytes, low byte first, resolution 10 Hz
   - GM - GPS Mode: 0x00 -> GPS, 0x01 -> BDS, 0x02 -> GPS + BDS
   - ST - Ste Time (STE): 1 byte, value = rawvalue * 10ms, valid range 0x00 (0ms) .. 0x64 (1000ms)
   - MG - Manual Dial - Group TG Hold Time (Digital Func): valid range: 0x01 (1s) .. 0x1e (30s), 0x1f (30 min), 0x20 (infinite)
   
   - MP - Manual Dial - Private TG Hold Time (Digital Func): valid range: 0x01 (1s) .. 0x1e (30s), 0x1f (30 min), 0x20 (infinite)
   - BC - B Channel Name Color:  1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White
   - ET - Encryption Type (Other): 0x00 ->  Common, 0x01 -> AES
   - TP - TOT Predict (Other): 0x00 -> off, 0x01 -> on
   - TG - TxPow Agc (Other):  0x00 -> off, 0x01 -> on
   - CA - Zone Name Colour A: 1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White
   - Cb - Zone Name Colour B: 1 byte, 0x00 -> orange, 0x01 -> Red, 0x02 -> Yellow, 0x03 -> Green, 0x04 -> Turquoise, 0x05 -> Blue, 0x06 -> White                          - ApoKind (Power Save): 1 byte, 0x00 -> is affected by call, 0x01 -> is not affected by call


```

## Encryption (0x024c1800)

0x24c1800 .. 0x24c1cff


## Zone names (0x02540000)

Each entry has 32 bytes and starts at 0x02540000 + 32 * [id number]. Up to 250 Zones possible.

```
57 | 02540000 | 10 | 44423047 46000000 00000000 00000000 | a9 06 || DB0G F... .... .... || DB0GF........... ||
                     NANANANA NANANANA NANANANA NANANANA
57 | 02540010 | 10 | 00000000 00000000 00000000 00000000 | 76 06 || .... .... .... .... || ................ ||

   - NA - Name: ASCII, max 16 chars. 0x00 for unused characters.
```
Empty entries will not be written.


## Radio ID List (0x02580000)

```
57 | 02580000 | 10 | 02620848 00444c39 43415400 00000000 | bf 06 || .b.H .DL9 CAT. .... || .b.H.DL9CAT..... ||
                     RIRIRIRI   NANANA NANANANA NANANANA
57 | 02580010 | 10 | 00000000 00000000 00000000 00000000 | 7a 06 || .... .... .... .... || ................ ||
                     NANANANA NANANANA NANANANA NANANA
                     
  - RI - Radio ID: 4 bytes, BCD coded.
  - NA - Name: ASCII, max. 26 bytes, 0 terminated

```
250 entries can be made. Every entry has 32 bytes. One follows after another so the last entry will end at address 0x02580000 + 32*250 - 1 = 0x02581f3f

Empty entries will not be written.

## ??

```
57 | 025c0b00 | 10 | 01000000 00000000 00000000 00000000 | 7a 06 || .... .... .... .... || ................ ||
```

## Receive group call list entry used (0x025c0b10)

1 bit for every used receive group call list entry. 0 -> place is free, 1 -> place in use. Max. 250 places.
```
57 | 025c0b10 | 10 | ff030000 00000000 00000000 00000000 | 8b 06 || ÿ... .... .... .... || ÿ............... ||
57 | 025c0b20 | 10 | 00000000 00000000 00000000 00000002 | 9b 06 || .... .... .... .... || ................ ||
```

## Talk groups control data (0x02600000)

The talk group list can contain up to 10000 entries. In this memory section the used entries are numbered.

```
57 | 02600000 | 10 | 00000000 01000000 02000000 03000000 | 78 06 || .... .... .... .... || ................ ||
                     IDID     IDID     IDID     IDID
57 | 02600010 | 10 | 04000000 05000000 06000000 07000000 | 98 06 || .... .... .... .... || ................ ||
                     IDID     IDID     IDID     IDID

   - ID - Number of Talk group entry.
                     
[...]

57 | 02600340 | 10 | d0000000 d1000000 d2000000 ffffffff | 24 06 || Ð... Ñ... Ò... ÿÿÿÿ || Ð...Ñ...Ò...ÿÿÿÿ ||
57 | 02600350 | 10 | ffffffff ffffffff ffffffff ffffffff | b5 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||

[...]

57 | 02609c30 | 10 | ffffffff ffffffff ffffffff ffffffff | 2e 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||
```
4 bytes per entry, 10000 entries in total so memory section ends at 0x02609C3F. One big memory section, no gaps. 
Empty fields are 0xFFFFFFFF. 
The software does not support gaps or empty entries. Talk groups after empty fields will be moved forward to the first empty field.


## ?? Unknown Talk group info (0x02640000)

```
57 | 02640000 | 10 | 00000000 00000000 00000000 00000000 | 76 06 || .... .... .... .... || ................ ||
57 | 02640010 | 10 | 00000000 00000000 0000f8ff ffffffff | 79 06 || .... .... ..øÿ ÿÿÿÿ || ..........øÿÿÿÿÿ ||
                                           ??
57 | 02640020 | 10 | ffffffff ffffffff ffffffff ffffffff | 86 06 || ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ ÿÿÿÿ || ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ||

?? What is this byte for?
[...]
```

## Talk group list

Max 10000 entries.

```
57 | 02680000 | 10 | 00424d20 4563686f 20323632 39393700 | 0b 06 || .BM  Echo  262 997. || .BM Echo 262997. ||
                     CTNANANA NANANANA NANANANA NANANANA
57 | 02680010 | 10 | 00000000 00000000 00000000 00000000 | 8a 06 || .... .... .... .... || ................ ||
                     NA
57 | 02680020 | 10 | 00000000 26299701 00000000 00000000 | 81 06 || .... &).. .... .... || ....&).......... ||
                           ID IDIDIDCA
57 | 02680030 | 10 | 00000000 00000000 00000000 00000000 | aa 06 || .... .... .... .... || ................ ||
57 | 02680040 | 10 | 00000000 00000000 00000000 00000000 | ba 06 || .... .... .... .... || ................ ||
57 | 02680050 | 10 | 00000000 00000000 00000000 00000000 | ca 06 || .... .... .... .... || ................ ||
57 | 02680060 | 10 | 00000000 01323633 33382061 66753338 | a8 06 || .... .263 38 a fu38 || .....26338 afu38 ||
                              CT
57 | 02680070 | 10 | 00000000 00000000 00000000 00000000 | ea 06 || .... .... .... .... || ................ ||
57 | 02680080 | 10 | 00000000 00000000 02633800 00000000 | 97 06 || .... .... .c8. .... || .........c8..... ||
57 | 02680090 | 10 | 00000000 00000000 00000000 00000000 | 0a 06 || .... .... .... .... || ................ ||
57 | 026800a0 | 10 | 00000000 00000000 00000000 00000000 | 1a 06 || .... .... .... .... || ................ ||
57 | 026800b0 | 10 | 00000000 00000000 00000000 00000000 | 2a 06 || .... .... .... .... || ................ ||
57 | 026800c0 | 10 | 00000000 00000000 014e692d 4f737400 | 55 06 || .... .... .Ni- Ost. || .........Ni-Ost. ||
57 | 026800d0 | 10 | 00000000 00000000 00000000 00000000 | 4a 06 || .... .... .... .... || ................ ||
57 | 026800e0 | 10 | 00000000 00000000 00000000 02623900 | f7 06 || .... .... .... .b9. || .............b9. ||
57 | 026800f0 | 10 | 00000000 00000000 00000000 00000000 | 6a 06 || .... .... .... .... || ................ ||
57 | 02680100 | 10 | 00000000 00000000 00000000 00000000 | 7b 06 || .... .... .... .... || ................ ||
57 | 02680110 | 10 | 00000000 00000000 00000000 00000000 | 8b 06 || .... .... .... .... || ................ ||
57 | 02680120 | 10 | 00000000 00000000 00000000 014e532f | 6c 06 || .... .... .... .NS/ || .............NS/ ||
57 | 02680130 | 10 | 42726520 32363233 00000000 00000000 | b1 06 || Bre  2623 .... .... || Bre 2623........ ||
57 | 02680140 | 10 | 00000000 00000000 00000000 00000000 | bb 06 || .... .... .... .... || ................ ||
57 | 02680150 | 10 | 00262300 00000000 00000000 00000000 | 14 06 || .&#. .... .... .... || .&#............. ||
57 | 02680160 | 10 | 00000000 00000000 00000000 00000000 | db 06 || .... .... .... .... || ................ ||
57 | 02680170 | 10 | 00000000 00000000 00000000 00000000 | eb 06 || .... .... .... .... || ................ ||

   - CT - Call Type: 00 -> Private Call, 01 -> Group Call, 02 -> "All" (only once possible), 1 byte
   - NA - Name: ASCII, max. 16 bytes, end and unused bytes are 0x00
   - ID - TG/DMR ID, 4 bytes, BCD coded
   - CA - Call Alert. 00 -> none, 01 -> Ring, 02 -> Online Alert

[...]
```
On entry after another. 100 bytes per dataset? TBC. More management information at 0x04340000 when writing.


## Analog Address Book (0x02940000)

```
57 | 02940000 | 10 | 38501000 00000005 444c3149 4e5f3100 | 2b 06 || 8P.. .... DL1I N_1. || 8P......DL1IN_1. ||
                     NRNRNRNR       LN NANANANA NANANANA
57 | 02940010 | 10 | 00000000 00000000 38502000 00000005 | 63 06 || .... .... 8P . .... || ........8P ..... ||
                     NANANANA NANANA   NRNRNRNR       LN
57 | 02940020 | 10 | 444c3149 4e5f3200 00000000 00000000 | af 06 || DL1I N_2. .... .... || DL1IN_2......... ||
57 | 02940030 | 10 | 45764000 00000006 234f4537 4d46492d | ce 06 || Ev@. .... #OE7 MFI- || Ev@.....#OE7MFI- ||
57 | 02940040 | 10 | 4c000000 00000000 71128000 00000006 | 3b 06 || L... .... q... .... || L.......q....... ||
57 | 02940050 | 10 | 50656761 73757320 50726f6a 656b7400 | cd 06 || Pega sus  Proj ekt. || Pegasus Projekt. ||

   - NR - Number, 4 bytes BCD coded. Highest nibble at lowest address. 0 Padded at the end. Max 8 digits, more will crash CPS.
   - LN - 1 byte, length of number/digits. Necessary to compare end from 0 at the last digits.
   - NA - NAME, 15 byte, ASCII. Zero padded.
   
Start at 0x02940000, 1 record is 24 bytes, up to 128 records can be stored. There are no empty records, CPS moves other records to empty places. End of last record is approx. at 0x02940bff. TBC.

```

## Receive Group Call List (0x02980000)

Up to 250 receive group calls possible. Start address for each group 0x02980000 + 512 * [groupid] (groupid valid range 0...249).

```
57 | 02980000 | 10 | b7000000 01000000 b9000000 ba000000 | d5 06 || ·... .... ¹... º... || ·.......¹...º... ||
                     I1I1I1I1 I2I2I2I2 I3I3I3I3 I4I4I4I4
[...]

57 | 02980100 | 10 | 57572061 6c6c6573 00000000 00000000 | 8a 06 || WW a lles .... .... || WW alles........ ||
                     NANANANA NANANANA NANANANA NANANANA
57 | 02980110 | 10 | 00000000 00000000 00000000 00000000 | bb 06 || .... .... .... .... || ................ ||

   - Ix - ID of group in Talk group list, 4 bytes, low byte first. 64 entries possible, unused will be 0xffffffff
   - NA - Name of Group: max 16 characters, ASCII, unused chars are 0x00.
```

Empty groups will not be written.

## Talk group offsets (used for writing talk groups) - (0x04340000) 

Similar to contact list for talk group writing some offsets are calculated, too. These offsets are use for writing only and will not read back.

One entry contains the BCD coded radio ID shifted left by 1 bit in the first 4 bytes (low byte first). The free lowest bit will be 1 for group calls and 0 for private calls or all call. The list is sorted ascending by this calculated value. The next four bytes are the position of the talk group list (low byte first,  0 (0x0000) - 9999 (0x0f27)) for the 10000 entries). 


```
57 | 04340000 | 10 | 03000000 39000000 05000000 3a000000 | c3 06 || .... 9... .... :... || ....9.......:... ||
                     IDIDIDID POPOPOPO IDIDIDID POPOPOPO

[...]

57 | 04340690 | 10 | 2ae4ee2c c5000000 ffffffff ffffffff | c3 06 || *äî, Å... ÿÿÿÿ ÿÿÿÿ || *äî,Å...ÿÿÿÿÿÿÿÿ ||
                     IDIDIDID POPOPOPO

  Example:
  2ae4ee2c -> 0x2ceee42a. Lowest bit is 0 so we have no group call type. Shift 0x2ceee42a 1 bit down => 0x16777215 This is the talk group ID as BCD.
  cf000000 -> 0x000000c5 = 197 dec => This talk group has position 198 (id 197 counting from 0) in the talk group list.
```
TBC: There might be more memory sections involved if the list gets bigger.

If there is an unused place at the end (uneven number of talk groups), the 8 bytes are filled with 0xff.


# Digital contact list

For managing the digital contact list 3 memory parts are used. The first part starting at 0x04000000 contains information about the digital radio ID (and the call type) and an memory offset to the contact list. Part 2 only hosts the number of contact list entries and a pointer to the next free contact list memory address.
Part 3 contains the contact list with all information (ID, Callsign, Name, City, ...).

## Part 1: Contact offsets (used for writing contacts)

One entry contains the BCD coded radio ID shifted left by 1 bit in the first 4 bytes (low byte first). The free lowest bit will be 1 for group calls and 0 for private calls. The next four bytes are the memory offset to the contact list (low byte first) stored in Part 3. 

Example:
```
0x04000000: 22010000 00000000 24010000 63000000 
0x04000010: 26010000 c6000000 28010000 29010000

22010000 => 0x122. Lowest bit is 0 so we have a private call type. Shift 0x122 1 bit down => 0x91 This is the radio ID as BCD.
The next four bytes are 0 so the contact list memory offset for this entry is 0.

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

## Part 2: Index at 0x044c0000
This section only contains 4 bytes with the total number of stored contacts (low byte first) and the relative memory address to the next free contact list entry.

```
0x044c0000: 400d0300 00006807 00000000 00000000

0x00030d40 => 200000 entries
Next free entry at memory address 0x07680000
```

## Part 3: Contact list

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
