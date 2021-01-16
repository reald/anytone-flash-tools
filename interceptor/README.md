# Traffic interceptor

For analyzing unknown protocols between programming software and a serial device like a radio this interceptor scripts can be used. On the programming software side a virtual null modem cable is used to connect the programming software
and the interceptor script. All communication will be forwarded via network to another interceptor script. The radio is connected to an USB port here. 
It is not mandatory to use two different machines and a LAN here, you can run both interceptor scripts on the same machine. Just use "localhost" as server name.

So instead of

```
Programming software <-> Anytone D878UV
                   COM10 via USB
```

you will have this scenario:

```
Programming software <-> virtual null modem cable <-> at_intercept_programmer.py <-> LAN <-> at_intercept_radio.py <-> Radio
                    COM18                        COM26                                                         /dev/ttyACM0
```

The script on radio side will intercept all data between the programming software and the radio and saves everything in a hex dump file. If the serial port is disconnected it will automatically open
a diff tool (meld by default) and compare the stored files of the latest communication flow and the one before. This lets you very efficiently analyse each byte of the 
the communication protocol. Wireshark to intercept the USB connection is not needed any longer.


## Start interceptor on radio side

```
python3 ./at_d878uv_server.py
or
python3 ./at_d878uv_server.py /dev/ttyACM1
```
By default /dev/ttyACM0 as used as serial port. You can add other port names as first parameter. As storage directory /tmp and as diff tool "meld" is used. You can change this in the config section in the server script. 
The radio side must be started first. Make sure you have write permissions in the storage directory. This script has not been tested on windows!


## Start interceptor on programming software side

```
python3 ./at_d878uv_emulator.py ServernameWithRadio COM26`
``` 

The server name can be "localhost" if its on the same machine. If you are using a different port in your virtual null modem cable than COM26 
make sure to adapt the port name to your settings.


## Virtual null modem cables

### Linux

```
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

For Linux you can use a shorter intercepting script without network support, too.

```
Programming software <-> virtual null modem cable <-> at_intercept_nonet.py <-> Radio
                    /dev/pts/2                 /dev/pts/1                /dev/ttyACM0
```


### Windows

- e.g. com0com - http://com0com.sourceforge.net
- Remove default cable pair with CNCx1 port (Anytone CPS has problems with alphanumeric port ids)
- Add pair e.g. COM18 - COM26
- Activate "use Ports class [x]" at least for port COM18 (otherwise CPS will not find it)

![com0com settings](../emulator/com0com_settings.png)

- Use COM18 in programming software
- Use COM26 on emulator side
