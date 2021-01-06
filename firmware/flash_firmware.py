#!/usr/bin/python3

# D878UV_V1.19_20200616.CDD  
# D878UV_V1.19_20200616.CDI  
# D878UV_V1.19_20200616.spi

# usage $0 firmware.spi comport

# warung highly experimental

# spi file lesen: 51 bytes, fw size, gerät, hw version
# CDI file lesen: 278 bytes, gerät und hw version 2x, fw size, startadresse
# CDD lesen. dateigröße muss stimmen

# serial port öffnen und zum gerät verbinden

# in update mode gehen "UPDATE"

# device string lesen 0x02, gerät und hw version prüfen

# CDD in 32 byte blöcke verpacken und an das gerät senden. wenn kein ACK, dann paket widerholen. letztes paket mit 0 padden. 2 byte checksum

# 18 senden, 06 kommt zurück