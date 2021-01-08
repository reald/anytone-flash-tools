# Flash Firmware Update to Anytone D878 (and maybe others)

## Attention: 

* Updating firmware will delete codeplug. Backup with CPS first!
* Code is highly experiemental, you might destroy your device! USE AT YOUR OWN RISK!

## Flash Firmware

Transfer Anytone firmware update file to radio. 

  1. The firmware consists of 3 files (*.spi, *.CDI, *.CDD) with the same base name. Copy all of them into the same folder.
  1. Backup your code plug!
  1. Boot radio in firmware update mode:  Switch device on holding PF3 (blue button on top) and PTT.
  1. Run the flash tool with the .spi file as first and the serial port as second parameter:
    ```./flash_firmware.py firmware_image.spi /dev/ttyACM0```
  1. Watch for error messages. Stop process if something fails.
  1. Switch device off and hold PF2 (top left side) and PTT keys while switching radio on again to start installer.
  1. Rewrite code plug
