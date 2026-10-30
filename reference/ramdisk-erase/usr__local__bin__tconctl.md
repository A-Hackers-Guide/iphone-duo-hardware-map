# `/usr/local/bin/tconctl`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 243,088 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 3216)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.ioavfamily.user-access-displaymemory</key>
	<true/>
</dict>
</plist>
```

## Objective-C (15 classes, 0 protocols)

Classes: `DCPMCU`, `DCPTCON`, `DP655`, `DP815`, `DP825`, `DP835`, `DP855`, `DP865`, `DP875`, `Display`, `DisplayJ327`, `MCU`, `Nesos`, `S6TUUP1`, `TCON`

## Strings (953)

```
Config version differs
Failed to put TCON into DFU mode. Quiting Updating the firmware
*** FAIL ***
self.display.dmEeprom
TCONCTL: note: using default major version
 FAILED
Current MCU BL Ver: %d.%d\n
writeRegister:0x%x ret:0x%x
AP Rev:    %c%u\n
Error: Can't read from offset %04X\n
iPad7,2
    tconctl -A page offset mask                      - Bitwise and the value in an internal register with mask
TCONCTL: Erasing Block:  Address=0x%08X, Length=0x%08X\n
File EEPROM Ver:    %02X.%02X\n
%08lx: 
    tconctl -I cmd sub opt1 opt2 count [file]        - Send a read command to the firmware command interface
TCONCTL: Searching for %s\n
TCONCTL: Error: EEPROM contents did not match expected
Loading IMG4Data
Platform Type 0x%08X\n
Initializing DP865
MCU\n
NVM RptPol Bins(%d): 
tconModelObj
.bin
NVM Erase Address: 0x%08lx\n
MCU Unknown Device ID: %02X.%02X\n
iPad8,11
Bootloader Mode
Error: Missing required param
Error: Timeout retrying to write EEPROM
Failed to write tconcfg
Error: A file must be specified for writes > %lu\n
Added FW Update Section (Address): 0x%08X, Length: 0x%08X \n
Loading itcm 
MCU Error: BL versions mismatch
TCONCTL: error: could not find dcp-tcon service in registry
TCONCTL: Updating Block: Address=0x%08X, Length=0x%08X\n
lcd-eeprom
Unknown (%02X)
self.dmApi
Unsuported
lcd-pmic
displayRef
Updating Config0
MCU Error: failed programming
Program external display\n
TCONCTL: Skipping address 0x%x (NVM content matches that of update)\n
TCONCTL: Failed to read shadow section 0x%x from EEPRM. Will not update section 0x%x
pls
self.display.dmI2c
devices
Failed to write bootloader size
reg
Erasing and programming all NVM sections, this may take a minute...
Skipping update for boardId %d hwcid %d\n
vcom
q24@?0@\"NSNumber\"8@\"NSNumber\"16
iPad8,9
Non-authentic display detected, skipping update.
Vendor:    
iPad17,1
Program components\n
boot_rom status = 0x%X\n
%s
FRCVer:    %02X.%02X\n
iPad8,4
Error: Command data file corrupted
TCONCTL: error: getConfigMajorVersion:0x%x\n
backlight
lcd-%s
gain
IODeviceTree:/arm-io
Error: Missing %s filename param\n
auth-passed
Not initialized
tconctl-dcptcon=
Error: Eeprom file corrupted
offset: %08X payload: %016llX, sizeInWords: %08X\n
EDID version differs
BOE
iPad7,10
Gaenari
Loaded %d bytes from %s\n
NVM Erase Journal: 0x%08lx\n
    tconctl -o file                                  - Dump whole NVM in bin format
TCONCTL: failed to read EEPROM at offset 0x%x (0x%x)\n
max-request-size
Current EEPROM Ver: XX.XX
Error: Mismatch
Buffer is empty or null.
TCONCTL: Invalid update range: %lu\n
NESOS
Initializing DP835
Error: Only one action allowed
    tconctl -V                                       - Verify MCU version
[_tcon configure]
cdic
tconctl.m
Read ROM Section (Address): 0x%08X, Length: 0x%08X \n
 EPI
clearI2CAddress: can't write to %04X\n
%-12s 0x%X\n
Error: Count must be <= 256
    tconctl -d 0|1                                   - Dithering enable(1) or disable(0)
DCPTCON.m
TCONCTL: File not found in %s\n
TCONCTL: setRegisterBits:0x%x mask:0x%x ret:0x%x
TCONCTL: Successfully copied ROM 0x%08X, into firmware image 0x%08X,
 | 
DP875.m
fw
iPad8,7
Error: Can't switch WP to Frame_Pol
TCONCTL: Verifying erase succeeded...
Checking @ %x for %d bytes\n
Can't update device - not present or already updating
iPad16,5
eeprom       SPI
buffer
Done
S6E8GS0
Failed reading build version
tcon
TCONCTL: got major version 0x%x\n
SDOM fused
NVMEM write size must be greater than 256.
w
TCONCTL: PROD:      %d\n
 Done
Failed to read boot status
_display.dmMcu
NVM InvFrm Bins(%d): 
error: could not find mogul service (%s) in registry\n
    tconctl -r [-n] [page] offset [count]            - Read count internal registers, -n for offset only format, otherwise legacy format with page
    tconctl -i -R [-n] addr [offset] [count]         - Read count bytes from I2C device, -n to specify an offset, otherwise legacy format where offset is pre-set using -C
S6TUUP1
Skipping update since it requires personalized FW FuseCFG: 0x%02x\n
TCONCTL: Updating Section (Address) 0x%08X Length: 0x%08X
Initializing DP825
EEPROM
Error: Illegal option
    tconctl -J cmd sub opt1 opt2 count [file|data..] - Send a write command to the firmware command interface\n
prop
X2232_LGD_BUNDLE_LC8
PRC0Ver:   %02X.%02X\n
status == 0 
TCONCTL: Expected contents:
appleCfg
 bootloader size =%X\n
Error: Number of values must be <= 256
    tconctl -c                                       - Print display configuration
com.apple.tcon
Unknown
TCON:      %s (%s)\n
 Apple
sstLoc
_mcu
EDID CRC differs
bootloader itcm length: %x\n
Updating Agile Tables
tconctl v12.1
DP655
kern.bootargs
Error: Command data file not found
pgamma
super.display.dmTcon && IOAVDisplayMemoryRead(super.display.dmTcon, 0x10a4, &reg, 1) == 0
TCONCTL: BRDID:     %x\n
Loading bootloader size
prc2
APP
Polarity Stuck MS %d\n
Found MCU: NXP KL02
MCU Error: FW versions mismatch
----  --- --------
Error: Size must be <= %lu\n
    tconctl -i -W [-n] addr [offset] data [data..]   - Write data bytes to I2C device, -n to specify an offset, otherwise legacy format where offset is pre-set using -C
    tconctl -O page offset mask                      - Bitwise or the value in an internal register with mask
TCONCTL: FAILED to write EEPROM at offset 0x%x (0x%x)\n
Error: Read exceeds register space
TCONCTL: Failed to sort FW Sections
whole
loader
TCONCTL: FAILED to erase EEPROM at offset 0x%x (0x%x)\n
Erase done with status: 0x%02X\n
Error: %s file %s not found\n
eeprom
Error: Error reading file %s\n
Auto Shutdown 0x%08X\n
Failed sending image size to MCU. Aborting
Error setting offset: %x\n
failed program %x (ret = %x)\n
_%s_
 Failed to read after Reset TCON
Error: Missing filename param 
model
iPad16,6
Initializing DP815
Failed reading EDID CRC
%@/%s/%s_%s_%c%c.bin
Error: NVM file corrupted - read %x bytes from %s (expected %x)\n
Failed reading Config
%02X%c
eq
Sending 0x%04X bytes\n
viucnrwe:pPRKWCZDl:o:t:zg:d:AOXhm:M:LVNIJEF:fT:Yya:
    tconctl -m file                                  - Program MCU
dither
DP825
MCU Error: after programming running in Bootloader mode
prc0
DP815
chip-revision
PRC
Dumping NVM
default
fw_b
TCONCTL: Verifying block contents...
Error: retrying to write EEPROM
Bridge I2C\n
Config differs
TCONCTL: Erasing 0x%x...
Error: failed programming EEPROM (0x%x)\n
engamma
iPad8,6
\nFailed to read NVM at offset %x\n
Error: Crossing page boundary
DP875
Replacing FW Image Section (Address): 0x%08X with ROM Section (Address): 0x%08X, Length: 0x%08X \n
Reading bootloader size
readRegisters: Failed to enable access to the internal registers
lcd-
    tconctl -X page offset mask                      - Bitwise xor the value in an internal register with mask
Comparing Config
Updating PRC table %d\n
Error: after programming MCU not running correct Bootloader
AUO
/usr/local/standalone/firmware
TCON BootRom in restore mode
File MCU FW Ver:    %d.%d\n
MCU Error: FW version expected %d.%d\n
Error: failed programming MCU
error: auth-error property not found
Error: Extra param
TCONCTL: Error: NVM file corrupted - read %x bytes from %s (expected %x)\n
tempData
    tconctl -R device offset [count]                 - Read count bytes from device at offset. device:eeprom, pmic, cpld, pgamma, pls
    tconctl -a device file                           - Program display device: eg: cpld\n
lcd-pgamma
_display
iPad7,8
Magnolia2
 Programming base = %06X size = %06X\n
Error: PRC index out of range [0, 3]
Live Buffer\nIndx Rate FrameCnt
lcd-i2c-generic
Initializing DP875
Error: Read exceeds 16 bit addressing
    tconctl [-f] -e file                             - Program NVM, skipping critical sections. -f to force program
Searching for %s\n
cfg
Error: Can't set offset pointer to %04X (ret = %x)\n
gain2DU
Error: Error parsing file
iPad17,4
 |%s|\n
Verify build version
AppleTCON
Current MCU FW Ver: %d.%d\n
Display.m
Error: Offset must be in range [0,FFFFFF]
readRegister:0x%x ret:0x%x
iPad7,3
Error: A file must be specified for reads > %lu\n
TCONCTL: readRegister:0x%x ret:0x%x
NVM TotalFrmCt %u\nNVM IdxLastBad %u\nNVM PwrOnCnt %u\nNVM InvPwrOffs %u\nNVM PolPwrOffs %u\nNVM MaxCaVal %d\nNVM Log %d\nNVM Last %d\nNVM ConsPolPwrOffs %u\n
    tconctl -Y                                       - Put TCON into FW_NO_LOAD mode\n
Vinca
S6TUUP1.m
TCONCTL: ERROR: Failed to prepare FW image (0x%x)\n
DP865
Error: reading %s\n
DCPMCU.m
Frame Tolerance %d\n
IODeviceTree:/arm-io/smc/iop-smc-nub/smc-mogul
Fail - passed:%d error:%d\n
TCONCTL: WARNING: Forcing update of protected block at 0x%08X\n
pathBase != ((void *)0)
tcon-
NVM does not need update
Commands\n
DP855
1k
Adjusting length to: 0x%04X\n
Error: Count must be <= %u\n
Error: Eeprom file not found
retVal == 0 
I2C interface not supported for Goldfinch, use the MCU interface
NVM not accessible %x size %lx\n
failed erase %x (ret = %x)\n
LGD
ibc
setI2CAddr: can't write to %04X\n
MCU.m
MCU Error: 
Nesos.m
%@/%s/%s
Live Histogram\nIndx Rate FrameCnt
/usr/local/standalone/firmware/DP825/%s_MCU_%s.bin
Error: after programming MCU not running Application
12.1
    tconctl -N                                       - Get MCU NVM entries
Error: failed programming EEPROM
Saving PRC table %d\n
IOAVDisplayMemory
Error: Write exceeds register space
    tconctl -z                                       - Reload PRC from NVM
TCONCTL: error: unsupported vendor (%d)\n
TCONCTL: failed to erase EEPROM at offset 0x%x (0x%x)\n
   
Display component (%s) not found in registry\n
Error: Can't switch to FRM_POL
\ntconctl for Baobab (DP835) Hibiscus (DP825) TulipW (DP815) Magnolia2 (DP655) Larkspur (DP855) Banyan (DP865) Vinca (DP875) Gaenari (S6TUUP1) Nesos v%s\n\n
size && *size >= 70
%c
frc
Error: %x\n
degamma
Initializing NESOS
Error: NVM file not found
TCONCTL: failed to write EEPROM at offset 0x%x (0x%x)\n
cpld
Comparing Config version
Read done with status: 0x%02X\n
SDOM:      %d\n
reading %d byte%s from EEPROM @ %x\n
Failed to get boardId
TCONCTL: ERROR: Image too small (0x%lx bytes, expected at least 0x%x)\n
super.display.dmTcon
TulipW
fw_a
TCONCTL: writeRegister:0x%x ret:0x%x
product
NVMEM size must be a multiple of four.
Failed to read boot arom status register
iPad7,1
App Invalidate failed. Aborting
s
TCONCTL: note: locked NVM does not contain the major version, falling back to register value
ConfigVer: %02X.%02X\n
wpc
Updating EDID
failed read %x (ret = %x)\n
self.display.dmMcu
dataImage length is %d \n
ret
_%c%u.bin
Current EEPROM Ver: %02X.%02X\n
NVM TotalFrmCt %u\nNVM IdxLastBad %u\nNVM PwrOnCnt %u\nNVM PPOrSDPwrOffs %u\nNVM PolPwrOffs %u\nNVM MaxCaVal %d\nNVM Log %d\nNVM Last %d\nNVM ConsPolPwrOffs %u\nNVM GoodPwrOffs %u\n
iPad8,5
iPad8,12
tcon-registers
Read of EEPROM offset: 0x%x size: 0x%x\n
v8@?0
TCONCTL: Skipping protected region starting at 0x%08X (length 0x%lX)\n
vendorString
NVM Write Address: 0x%08lx\n
start restore f/w authentication
DPCD registers\n
DP865.m
sstTempDda
prc3
Error: Failed programming NVM (0x%x)\n
vendor
TCONCTL: Verifying section contents...
Build version differs
NVMEM offset must be multiple of 256.
Hibiscus
iPad7,9
iPad16,4
auth-error
lcd-pls
TCONCTL: TCONCTL: Failed to validate read-only NVM -- likely a coding bug
Serial:    %s\n
File not available
%08x: 
boot status = 0x%X\n
iPad8,10
MCU required but not initiallized
Failed reading from EEPROM
tcon-api
    tconctl -D                                       - List devices\n
    tconctl -y                                       - Put TCON into FW_LOAD mode
Page 0x2D offset 0xC2 ,Bit 0 not clear 
Failed to write IMG4Data
DitherVer: %02X.%02X\n
Application Mode
Error: -t allowed only with -o or -l
lcd-cpld2
Error: Failed updating PRC table %d\n
iPad8,1
/usr/standalone/firmware
Failed to start f/w authentication
vcomCfg
LIVE CurrCaVal %d\nLIVE MaxCaVal %d\nLIVE Log %d\n
iPad16,3
 SIPI
Error: Can't switch to WP
MCU
    tconctl -W device offset data [data..]           - Write data bytes to device at offset. device:eeprom, pmic, cpld, pgamma, pls
HWCID:     %x\n
TCONCTL: Aborting update after erasing 0%x!
LIVE RptPol Bins(%d): 
    tconctl [-f] -u                                  - Auto-update NVM, skipping critical sections. -f to force update
PROD:      %d\n
i
TCONCTL: Aborting update before writing block at 0x%X for corruption test!\n
AppleCfg:  %02X %02X %02X %02X %02X %02X %02X %02X\n
%4d %4d %8u\n
    tconctl -g 0|1                                   - Gamma Correction enable(1) or disable(0)
TCONCTL: SDOM:      %d\n
Failed to read SDOM (ret = %x)\n
%d:\t%d\t%d\t%d\n
Checking display authenticity...
Error: Write exceeds 16 bit addressing
    tconctl -C addr offset [count]                   - Combined I2C transaction to set current offset and read count bytes, this is deprecated and should not be used\n
edid
 Programming mcuBlocks[i].base = %06X mcuBlocks[i].size = %06X imagePtr = %06X\n
Loading tconcfg 
    tconctl -v                                       - Verbose
cpld_config
EepromCfg: %02X %02X %02X\n
bootloader dtcm length: %x\n
TCONCTL: Added Section (Address): 0x%08X to update list 
TCON.m
 Failed to enable the SPI access
iPad8,2
ret == 0 
TCONCTL: error: failed to read major version from NVM (0x%x)\n
Failed to write itcm
Updating Dither
sstloc
fcbist
TCONCTL: Done
Updating Agile
Initializing DP855
 failed to enabled TCON I2C bridge
Error: Can't protect EEPROM
Updating build
NVM Read Address: 0x%08lx\n
Loading dtcm 
*** PASS ***
sstTemp
prc1
Initializing Display with DP835
    tconctl -L                                       - Get all MCU logs
r
Initializing Display
    tconctl -w [-n] [page] offset [data...]          - Write consecutive internal registers, -n for offset only format, otherwise legacy format with page\n
use-default-major
AgileVer:  %02X.%02X\n
%u 
Bridge SPI/SPMI\n
lut
%02x 
agile
Error: File %s could not be created\n
iPad8,3
    tconctl -K eeprom offset [count]                 - Read count bytes from eeprom device at offset.
pmic
Failed reading EDID version
TCONCTL: Successfully prepared FW Image
TCONCTL: Actual contents:
sstdda
iPad17,2
iPad17,3
Data length must equal count
iPad8,8
Error: can't switch to WP
Error: Display off
Internal registers\n
    tconctl -Z device offset length                  - Erase sector(s) containing offset + length (not all devices support erasing)\n
Error: Memory alloc
Loaded %u bytes from %s\n
Failed handshake with MCU. Aborting
Error: Incorrect params. Usage: -R eeprom <offset> <size>
Error: NVM file corrupted
WPCVer:    %02X.%02X\n
_dpDevice
Error: Page must be in range [0,%d]\n
EDID:      %d / %d\n
(unsigned long)CFDataGetLength(tconModelObj) >= sizeof(uint32_t)
Verify EDID CRC
Error: failed reading EEPROM
Error: Offset must be in range [0,FF]
lcd-cpld1
gamma
Page 0x2D offset 0xC2 ,Bit 0 not set 
Loading bootblock
MCU is not running application
NVM not accessible %x %lx\n
SDC
 eRVDS
TCON unsupported
    tconctl -l file [-t [0|1|2|3]]                   - Update PRC in table 0|1|2|3 from a file in txt format
Error: Can't set offset pointer to %04X (addr = %02X ret = %x)\n
DP835
    tconctl -T TCON                                  - Force use of specific TCON (DP655 DP815 DP825 DP835 DP855 DP875 S6TUUP1)
Failed reading Config version
Write done with status: 0x%02X\n
File MCU BL Ver:    %d.%d\n
IODeviceTree:/arm-io/dcp-tcon
Updating Config
MCU Error: after programming not running correct Application
IOService:/
MCU Error: BL version expected %d.%d\n
error: auth-passed property not found
    tconctl -o file -t [0|1]                         - Dump PRC in table 0|1 (0|1|2|3 for DP825) into a file in txt format\n
%@/%s/%s.bin
Error: Can't read from offset %04X (addr = %02X ret = %x)\n
Failed to get HWCID
Failed to write dtcm
Failed to write boot blk offset
Initializing S6TUUP1
    tconctl -P dpcd data [data..]                    - Write consecutive DPCD registers\n
TCONCTL: readGPIOIn:%d
appleTcon != ((io_object_t) 0)
 Programming base = %06X size = %06X \n
iPad7,4
iPad7,7
    tconctl -F file                                  - Force program all NVM, without skipping sections
can't enable FW Access
Invalid image size: %lu\n
DP855.m
TCONCTL: This TCON does not support legacy I2C format
 
    tconctl -p dpcd [count]                          - Read count DPCD registers
setI2CAddr: can't enable FW Access
number of bins exceeds preset %d\n
Comparing EDID version
vcomData
Error: Unsupported TCON
Usage:\n
BL
LIVE InvFrm Bins(%d): 
NVM Entry %d:\n
lcd-mcu
MCU does not need update
Fail %x\n
SHA
DP815.m
Error: Data must be in range [0,FF]
TCONCTL: Skipping block at 0x%08X (NVM content matches)\n
Initializing DP655
Error: Count must be <= %lu\n
displayRef is nil
Larkspur
[%s:%d] Error:(%s) ret:0x%lx\n
DP875
DCPTCON
Nesos
TCON
DP865
DCPMCU
MCU
DP655
DP835
DP825
DisplayJ327
Display
S6TUUP1
DP855
DP815
i40@0:8^@16*24*32
I
@\"NSArray\"
[11C]
B32@0:8@16^@24
^{__IOAVDevice=}16@0:8
i36@0:8C16I20*24I32
i32@0:8r*16r*24
@24@0:8r*16
[32c]
@16@0:8
i32@0:8I16*20I28
i20@0:8B16
i32@0:8^@16@24
v24@0:8@16
@\"NSDictionary\"
i24@0:8I16I20
C
@\"NSSet\"
i32@0:8C16C20*24
i24@0:8I16C20
i36@0:8{_TCONMCUCommand=CCCCI}16*24B32
@24@0:8i16B20
I28@0:8@16B24
i16@0:8
i36@0:8@16*24S32
i32@0:8i16i20*24
^{__IOAVDisplayMemory=}24@0:8r*16
i28@0:8@16I24
@\"NSMutableArray\"
B36@0:8I16*20*28
[16C]
i28@0:8*16I24
i28@0:8r*16B24
^{__IODPDevice=}
i32@0:8*16^I24
C16@0:8
i28@0:8C16^B20
v16@0:8
{_NSRange=QQ}20@0:8I16
i28@0:8I16*20
i24@0:8^S16
i24@0:8^I16
I16@0:8
*16@0:8
@\"NSMutableDictionary\"
i24@0:8C16C20
i32@0:8*16*24
@\"MCU\"
^{__IOAVDevice=}
@28@0:8@16B24
^{__IOAVDisplayMemory=}16@0:8
v20@0:8B16
B
i20@0:8I16
i24@0:8*16
I24@0:8r*16
B16@0:8
i40@0:8r*16I24*28I36
i28@0:8C16r*20
i24@0:8^@16
i24@0:8^B16
i20@0:8i16
i36@0:8C16C20*24I32
v20@0:8I16
i28@0:8i16*20
^{__IODPDevice=}16@0:8
@\"TCON\"
i20@0:8C16
i32@0:8C16*20I28
C24@0:8r*16
i32@0:8@16I24I28
v20@0:8C16
@36@0:8@16@24B32
i28@0:8@16i24
i24@0:8r*16
^{__IOAVDisplayMemory=}
i32@0:8@16@24
i24@0:8@16
@\"Display\"
dmPLS
T^{__IOAVDisplayMemory=},R,N,V_dmPgamma
getInterfaceType:
getProductString
loadImage:model:type:
_dmTcon
valueWithRange:
T^{__IOAVDisplayMemory=},R,N,V_dmTcon
getBoardId:
T^{__IOAVDisplayMemory=},R,N,V_dmCPLDConfig
_eepromShadowSections
dpDevice
spiAccessEnable
dmMcu
eepromSize
init
tconI2CBridgeEnable:
writeRegister:buffer:
dmCPLDUsr
getDmFromString:
programDisplayDevice:filename:
readI2C:buffer:size:
write:size:
enableLiveLogs:
configEEPROMWP:
setNvmUpdateSectionsKeysSorted:
_verbose
enableRegAccess
intValue
printLiveBuffer
_eepromI2CAddr
defaultMajorVersion
read:buffer:size:
sendCommand:sub:reply:
setNvmUpdateSections:
clearI2CAddress
_dmI2c
ditherControl:
dmPgamma
readRegisters:buffer:size:
setFrameTolerance:
command:data:read:
getBytes:length:
getCodeNameString
getSerialNumber:size:
writeBridgeI2C:offset:buffer:size:
writeBridge:offset:buffer:size:
getModelStr
readSPI:offset:buffer:size:
removeObjectForKey:
newlineCharacterSet
setAutoShutdown:
stringWithFormat:
tconPageCount
writeEeprom:buffer:size:
nvmSkipSections
T^{__IOAVDisplayMemory=},R,N,V_dmI2c
T^{__IOAVDisplayMemory=},R,N,V_dmEeprom
clearRegisterBits:mask:
configure
_fwRunning
update:
verbose
T^{__IOAVDisplayMemory=},R,N,V_dmPmic1
_dmPLS
readEepromAt:buffer:size:
setI2CAddr:
TB,V_fwRunning
T^{__IOAVDevice=},R,N,V_avDevice
arrayWithObjects:count:
copy
nvmUpdateSectionsKeysSorted
objectForKeyedSubscript:
protectedSections
T^{__IODPDevice=},R,N,V_dpDevice
bytes
getDisplayComponentPropertiesByName:
setRegisterBits:mask:
T@\"NSArray\",&,V_nvmUpdateSections
_defaultMajorVersion
lock
read:size:
readBridgeI2C:offset:buffer:size:
setEepromShadowSections:
subdataWithRange:
T^{__IOAVDisplayMemory=},R,N,V_dmMcu
_dmCPLDConfig
nvmSkipSectionsKeysSorted
unlock
verify
TI,V_majorVersionAddr
addObject:
appendData:
getAPChipRev:
resetLiveLogs
T@\"NSMutableArray\",&,V_nvmUpdateSectionsKeysSorted
TI,R,D,N
appendString:
getEepromAddress
getParameter:param:
isEqualToData:
isEqualToString:
majorVersionAddr
avDevice
bootArgs
count
tconFWLoad
unsignedIntValue
writeDPCD:buffer:size:
_avDevice
replaceBytesInRange:withBytes:
T@\"NSMutableDictionary\",&,V_nvmSkipSections
readRegisters:offset:buffer:size:
setBootArgs:
setNvmSkipSectionsKeysSorted:
verifyPlatformType:
T^{__IOAVDisplayMemory=},R,N,V_dmPLS
_mcu
_modelStr
_nvmSkipSections
dmCPLDConfig
isAuthentic
setVerbose:
T@\"Display\",&,N,Vdisplay
_bootArgsValid
printNVMEntries:
readRegister:buffer:
setWithArray:
stringWithUTF8String:
T^{__IOAVDisplayMemory=},R,N,V_dmCPLDUsr
maxRequestSize
readBridge:offset:buffer:size:
protectedRanges
_dpDevice
getEepromSNOffset
mcuCommand:data:read:
setPolarityStuckMS:
length
update:state:
dataWithLength:
_majorVersionAddr
_protectedRanges
dataWithBytesNoCopy:length:
getConfigSize:
getHwCID:
numberWithUnsignedInt:
raise:format:
_tcon
initWithLength:
displayConfig
setDefaultMajorVersion:
setObject:forKeyedSubscript:
setProtectedRanges:
update:mask:
addSection:intoSection:
dfuModeAndResetTCON:
getAppleVersions:
getDisplayComponentHandleByName:
combinedI2C:offset:buffer:size:
printLiveSummary
readDPCD:buffer:size:
TB,N,V_verbose
getWeekAndYear:
_protectedSections
objectEnumerator
initWithTcon:verbose:
objectAtIndexedSubscript:
rangeValue
whitespaceCharacterSet
_dmEeprom
_findIntersectingProtectedRangeForAddress:
_nvmForceUpdateSections
getPolarityStuckMS:
getSdom:
writeRegisters:offset:buffer:size:
getPageCount
parseTable:output:version:
setNvmSkipSections:
tconFWDoNotLoad
enableFwAccess
getAutoShutdown:
getVendorId:
useDefaultMajor
T@\"NSArray\",&,V_nvmForceUpdateSections
getAppVersion:
getDisplayComponentAddressByName:
setProtectedSections:
writeRegister:offset:buffer:
writeToFile:atomically:
.cxx_destruct
prcReload
_dmMcu
dumpLogs:
getSDOM:
writeI2C:buffer:size:
T^{__IOAVDisplayMemory=},R,N,V_dmApi
TC,V_defaultMajorVersion
readEeprom:buffer:size:
resetNVMLogs
setPlatformType:
supportsShadowSectionsROMCopy
_nvmUpdateSections
dmI2c
dmTcon
setMajorVersionAddr:
T@\"NSSet\",&,V_protectedSections
dataWithBytes:length:
dumpPrc:filename:
objectForKey:
programEeprom:force:
programMCU:reset:
programPrc:filename:
dmEeprom
getIORegistryEntryForComponentByName:
setNvmForceUpdateSections:
writeRegisters:buffer:size:
display
_display
getFrameTolerance:
printNVMSummary:
getDPCDMappingForOffset:page:offset:
loadImage:
needEepromUpdate:force:
printHistogram
_dmCPLDUsr
disableRegAccess
getConfigVersion:
readRegister:offset:buffer:
_bootArgs
_dmPmic1
TC,R,N,V_fwRunning
_eeMemMap
array
dictionaryWithDictionary:
integerValue
componentsSeparatedByCharactersInSet:
i2cAddressOfBridgeDevice:
initWithDisplay:eeMemMap:verbose:
insertObject:atIndex:
T@\"NSMutableArray\",&,V_nvmSkipSectionsKeysSorted
characterAtIndex:
dataWithContentsOfFile:
dictionaryWithObjects:forKeys:count:
hasPrefix:
resetBanyan
setFwRunning:
writeSPI:offset:buffer:size:
skipLines:line:
_nvmUpdateSectionsKeysSorted
getModelStringDPCD:
getStateBL:FW:
nextObject
stringWithCString:encoding:
stringWithContentsOfFile:encoding:error:
wpControl:state:
prepareFWImage:
eraseEeprom:size:
setParameter:param:
getConfigMajorVersion:
containsObject:
eepromShadowSections
fwRunning
getProdStatus:
writeEepromAt:buffer:size:
countByEnumeratingWithState:objects:count:
gammaControl:
getBLVersion:
indexOfObject:inSortedRange:options:usingComparator:
_nvmSkipSectionsKeysSorted
_fwAccessSecret
TI
dmPmic1
_dmApi
_mcuRequired
disableMCU:
enableMCU
T@\"NSMutableDictionary\",&,V_eepromShadowSections
verify:
initWithDisplay:verbose:
setDisplay:
enableNVMLogs:
nvmForceUpdateSections
storeNVM
T@\"NSArray\",&,N,V_protectedRanges
T@\"NSMutableDictionary\",&,V_nvmUpdateSections
_dmPgamma
_regAccessSecret
dmApi
verifyEEPROMMatches:offset:length:
write:data:size:
T@\"Display\",&,N,V_display
loadImage:withPathBase:
nvmUpdateSections
substringFromIndex:
displayKnownDevices
getPlatformType:
mutableCopy
readGPIOIn:val:
UTF8String
deviceSpecificHelp
```
