# `/usr/local/bin/tconctl`

From the upgrade restore ramdisk (141-29011-104.dmg). 243,088 bytes.

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
prc0
Error: can't switch to WP
viucnrwe:pPRKWCZDl:o:t:zg:d:AOXhm:M:LVNIJEF:fT:Yya:
r
failed erase %x (ret = %x)\n
[_tcon configure]
IODeviceTree:/arm-io
Error: A file must be specified for writes > %lu\n
TCON:      %s (%s)\n
DCPMCU.m
iPad8,6
Error: Number of values must be <= 256
    tconctl -m file                                  - Program MCU
prc2
Error: Page must be in range [0,%d]\n
Done
reading %d byte%s from EEPROM @ %x\n
TCONCTL: Error: NVM file corrupted - read %x bytes from %s (expected %x)\n
Updating Dither
Loaded %u bytes from %s\n
iPad8,8
Display.m
ret == 0 
TCONCTL: Erasing 0x%x...
bootloader dtcm length: %x\n
TCONCTL: got major version 0x%x\n
TCONCTL: TCONCTL: Failed to validate read-only NVM -- likely a coding bug
Error: Eeprom file not found
Loading bootblock
DP815.m
iPad8,12
Config differs
%c
Bridge SPI/SPMI\n
DP855
failed read %x (ret = %x)\n
LIVE RptPol Bins(%d): 
Application Mode
lcd-
Error: after programming MCU not running correct Bootloader
Vinca
PROD:      %d\n
Replacing FW Image Section (Address): 0x%08X with ROM Section (Address): 0x%08X, Length: 0x%08X \n
Unknown
   
w
IOService:/
error: could not find mogul service (%s) in registry\n
BOE
 Programming mcuBlocks[i].base = %06X mcuBlocks[i].size = %06X imagePtr = %06X\n
sstLoc
Error: retrying to write EEPROM
buffer
    tconctl -r [-n] [page] offset [count]            - Read count internal registers, -n for offset only format, otherwise legacy format with page
    tconctl -C addr offset [count]                   - Combined I2C transaction to set current offset and read count bytes, this is deprecated and should not be used\n
TCONCTL: Verifying section contents...
TCONCTL: Erasing Block:  Address=0x%08X, Length=0x%08X\n
%@/%s/%s
%08x: 
Error: File %s could not be created\n
Frame Tolerance %d\n
IODeviceTree:/arm-io/smc/iop-smc-nub/smc-mogul
    tconctl -P dpcd data [data..]                    - Write consecutive DPCD registers\n
TCONCTL: Skipping protected region starting at 0x%08X (length 0x%lX)\n
PRC0Ver:   %02X.%02X\n
NVM Entry %d:\n
Error: Count must be <= 256
    tconctl [-f] -e file                             - Program NVM, skipping critical sections. -f to force program
Page 0x2D offset 0xC2 ,Bit 0 not set 
NVM InvFrm Bins(%d): 
Failed to read boot arom status register
Failed reading EDID CRC
TCONCTL: Failed to read shadow section 0x%x from EEPRM. Will not update section 0x%x
Updating Config
NVMEM write size must be greater than 256.
Updating Agile
Sending 0x%04X bytes\n
Updating PRC table %d\n
displayRef is nil
Comparing Config
_%s_
tempData
DP875.m
EDID version differs
Comparing Config version
can't enable FW Access
/usr/local/standalone/firmware/DP825/%s_MCU_%s.bin
Error: Write exceeds register space
Error: Extra param
Commands\n
TCONCTL: ERROR: Failed to prepare FW image (0x%x)\n
NVM does not need update
FRCVer:    %02X.%02X\n
    tconctl -R device offset [count]                 - Read count bytes from device at offset. device:eeprom, pmic, cpld, pgamma, pls
Updating build
SDC
TCONCTL: error: getConfigMajorVersion:0x%x\n
NESOS
MCU Error: BL versions mismatch
    tconctl -T TCON                                  - Force use of specific TCON (DP655 DP815 DP825 DP835 DP855 DP875 S6TUUP1)
cpld_config
    tconctl -K eeprom offset [count]                 - Read count bytes from eeprom device at offset.
HWCID:     %x\n
fcbist
TCONCTL: Updating Section (Address) 0x%08X Length: 0x%08X
TCON.m
Initializing DP835
LGD
%@/%s/%s_%s_%c%c.bin
q24@?0@\"NSNumber\"8@\"NSNumber\"16
size && *size >= 70
wpc
start restore f/w authentication
Read done with status: 0x%02X\n
Error: Count must be <= %lu\n
status == 0 
TCONCTL: Aborting update after erasing 0%x!
Failed to write tconcfg
error: auth-passed property not found
    tconctl -w [-n] [page] offset [data...]          - Write consecutive internal registers, -n for offset only format, otherwise legacy format with page\n
DP875
Skipping update for boardId %d hwcid %d\n
TCONCTL: Updating Block: Address=0x%08X, Length=0x%08X\n
appleTcon != ((io_object_t) 0)
Error: Offset must be in range [0,FF]
i
tcon
iPad8,11
----  --- --------
S6TUUP1
cpld
eeprom
NVM Read Address: 0x%08lx\n
    tconctl -i -R [-n] addr [offset] [count]         - Read count bytes from I2C device, -n to specify an offset, otherwise legacy format where offset is pre-set using -C
Loaded %d bytes from %s\n
Error: failed programming EEPROM (0x%x)\n
Verify build version
WPCVer:    %02X.%02X\n
iPad16,5
MCU
 |%s|\n
MCU Error: after programming not running correct Application
auth-error
Error: Missing filename param 
    tconctl -p dpcd [count]                          - Read count DPCD registers
    tconctl -W device offset data [data..]           - Write data bytes to device at offset. device:eeprom, pmic, cpld, pgamma, pls
lcd-pls
TCONCTL: Verifying block contents...
iPad7,3
Failed to start f/w authentication
Initializing S6TUUP1
Read of EEPROM offset: 0x%x size: 0x%x\n
TCONCTL: error: unsupported vendor (%d)\n
TCONCTL: setRegisterBits:0x%x mask:0x%x ret:0x%x
product
Error: %x\n
.bin
DP815
LIVE InvFrm Bins(%d): 
    tconctl -Y                                       - Put TCON into FW_NO_LOAD mode\n
TCONCTL: Added Section (Address): 0x%08X to update list 
writeRegister:0x%x ret:0x%x
SDOM fused
 Failed to enable the SPI access
MCU.m
Failed handshake with MCU. Aborting
super.display.dmTcon && IOAVDisplayMemoryRead(super.display.dmTcon, 0x10a4, &reg, 1) == 0
 FAILED
Current EEPROM Ver: %02X.%02X\n
self.display.dmMcu
MCU Error: failed programming
Nesos.m
_dpDevice
%-12s 0x%X\n
    tconctl -y                                       - Put TCON into FW_LOAD mode
TCON BootRom in restore mode
LIVE CurrCaVal %d\nLIVE MaxCaVal %d\nLIVE Log %d\n
Failed to get boardId
AppleTCON
pathBase != ((void *)0)
DitherVer: %02X.%02X\n
default
TCONCTL: BRDID:     %x\n
Failed reading Config
 Programming base = %06X size = %06X \n
NVM TotalFrmCt %u\nNVM IdxLastBad %u\nNVM PwrOnCnt %u\nNVM InvPwrOffs %u\nNVM PolPwrOffs %u\nNVM MaxCaVal %d\nNVM Log %d\nNVM Last %d\nNVM ConsPolPwrOffs %u\n
self.display.dmEeprom
IODeviceTree:/arm-io/dcp-tcon
 SIPI
MCU Unknown Device ID: %02X.%02X\n
Unsuported
Failed reading from EEPROM
TCONCTL: Skipping address 0x%x (NVM content matches that of update)\n
Error: Eeprom file corrupted
Erase done with status: 0x%02X\n
error: auth-error property not found
fw
TCONCTL: SDOM:      %d\n
1k
SHA
Platform Type 0x%08X\n
chip-revision
Error: Size must be <= %lu\n
Error: Display off
Invalid image size: %lu\n
ibc
Auto Shutdown 0x%08X\n
iPad17,3
Checking display authenticity...
Page 0x2D offset 0xC2 ,Bit 0 not clear 
\ntconctl for Baobab (DP835) Hibiscus (DP825) TulipW (DP815) Magnolia2 (DP655) Larkspur (DP855) Banyan (DP865) Vinca (DP875) Gaenari (S6TUUP1) Nesos v%s\n\n
Program components\n
TCONCTL: WARNING: Forcing update of protected block at 0x%08X\n
AP Rev:    %c%u\n
Adjusting length to: 0x%04X\n
iPad7,1
Not initialized
File MCU BL Ver:    %d.%d\n
Error: Can't set offset pointer to %04X (addr = %02X ret = %x)\n
number of bins exceeds preset %d\n
Error: Read exceeds 16 bit addressing
TCONCTL: Searching for %s\n
bootloader itcm length: %x\n
vcomCfg
Error: failed programming MCU
PRC
Failed reading EDID version
TCONCTL: PROD:      %d\n
Loading itcm 
iPad16,6
retVal == 0 
Error: A file must be specified for reads > %lu\n
    tconctl [-f] -u                                  - Auto-update NVM, skipping critical sections. -f to force update
Failed to read SDOM (ret = %x)\n
I2C interface not supported for Goldfinch, use the MCU interface
 Done
 Apple
gain2DU
setI2CAddr: can't enable FW Access
iPad7,7
model
Read ROM Section (Address): 0x%08X, Length: 0x%08X \n
readRegister:0x%x ret:0x%x
Dumping NVM
Erasing and programming all NVM sections, this may take a minute...
Program external display\n
MCU Error: after programming running in Bootloader mode
MCU Error: BL version expected %d.%d\n
Initializing Display
Error: Read exceeds register space
DPCD registers\n
Config version differs
Current MCU FW Ver: %d.%d\n
Added FW Update Section (Address): 0x%08X, Length: 0x%08X \n
dither
File MCU FW Ver:    %d.%d\n
Error: Crossing page boundary
Error: NVM file corrupted
kern.bootargs
Buffer is empty or null.
Checking @ %x for %d bytes\n
Failed to write IMG4Data
prc1
%s
Initializing NESOS
Usage:\n
pls
Skipping update since it requires personalized FW FuseCFG: 0x%02x\n
lcd-%s
iPad17,1
NVM not accessible %x %lx\n
TCONCTL: Skipping block at 0x%08X (NVM content matches)\n
Unknown (%02X)
_%c%u.bin
Error: Timeout retrying to write EEPROM
Error: after programming MCU not running Application
eeprom       SPI
Error: Data must be in range [0,FF]
s
lcd-cpld1
S6E8GS0
Build version differs
NVM Erase Address: 0x%08lx\n
    tconctl -A page offset mask                      - Bitwise and the value in an internal register with mask
boot_rom status = 0x%X\n
Error: Memory alloc
Polarity Stuck MS %d\n
TCONCTL: note: locked NVM does not contain the major version, falling back to register value
AUO
Error setting offset: %x\n
%08lx: 
_display
Error: Illegal option
Error: Missing required param
TCONCTL: failed to read EEPROM at offset 0x%x (0x%x)\n
Current EEPROM Ver: XX.XX
TulipW
Error: %s file %s not found\n
    tconctl -Z device offset length                  - Erase sector(s) containing offset + length (not all devices support erasing)\n
Larkspur
super.display.dmTcon
readRegisters: Failed to enable access to the internal registers
vcomData
Initializing DP655
Internal registers\n
TCONCTL: Actual contents:
Failed reading build version
agile
Updating Agile Tables
MCU Error: FW versions mismatch
Initializing DP855
(unsigned long)CFDataGetLength(tconModelObj) >= sizeof(uint32_t)
Gaenari
TCONCTL: ERROR: Image too small (0x%lx bytes, expected at least 0x%x)\n
Serial:    %s\n
setI2CAddr: can't write to %04X\n
%4d %4d %8u\n
iPad8,4
iPad8,7
Loading bootloader size
Loading dtcm 
MCU does not need update
*** FAIL ***
    tconctl -o file -t [0|1]                         - Dump PRC in table 0|1 (0|1|2|3 for DP825) into a file in txt format\n
loader
TCONCTL: Verifying erase succeeded...
MCU Error: FW version expected %d.%d\n
_mcu
    tconctl -F file                                  - Force program all NVM, without skipping sections
EepromCfg: %02X %02X %02X\n
AgileVer:  %02X.%02X\n
Error: Failed updating PRC table %d\n
MCU Error: 
EDID CRC differs
prop
Vendor:    
APP
Initializing DP875
lcd-cpld2
failed program %x (ret = %x)\n
gain
EEPROM
NVM Erase Journal: 0x%08lx\n
NVMEM size must be a multiple of four.
degamma
IOAVDisplayMemory
Error: Can't switch WP to Frame_Pol
    tconctl -X page offset mask                      - Bitwise xor the value in an internal register with mask
DP655
sstTemp
Display component (%s) not found in registry\n
    tconctl -I cmd sub opt1 opt2 count [file]        - Send a read command to the firmware command interface
displayRef
use-default-major
%02x 
X2232_LGD_BUNDLE_LC8
clearI2CAddress: can't write to %04X\n
Error: -t allowed only with -o or -l
Verify EDID CRC
TCONCTL: failed to write EEPROM at offset 0x%x (0x%x)\n
Write done with status: 0x%02X\n
iPad8,1
Error: Can't switch to WP
sstdda
tconctl-dcptcon=
 eRVDS
offset: %08X payload: %016llX, sizeInWords: %08X\n
DP825
iPad7,9
Initializing Display with DP835
v8@?0
File EEPROM Ver:    %02X.%02X\n
Error: Can't set offset pointer to %04X (ret = %x)\n
Failed to write itcm
reg
Initializing DP815
Error: Can't switch to FRM_POL
    tconctl -o file                                  - Dump whole NVM in bin format
pmic
TCONCTL: Invalid update range: %lu\n
TCONCTL: failed to erase EEPROM at offset 0x%x (0x%x)\n
Error: reading %s\n
Error: NVM file corrupted - read %x bytes from %s (expected %x)\n
whole
TCONCTL: readRegister:0x%x ret:0x%x
TCONCTL: Aborting update before writing block at 0x%X for corruption test!\n
Current MCU BL Ver: %d.%d\n
Error: Only one action allowed
TCONCTL: Done
Failed to write bootloader size
    tconctl -l file [-t [0|1|2|3]]                   - Update PRC in table 0|1|2|3 from a file in txt format
NVM not accessible %x size %lx\n
Error: failed reading EEPROM
iPad7,2
Failed reading Config version
 bootloader size =%X\n
Loading IMG4Data
vcom
vendor
 Programming base = %06X size = %06X\n
Initializing DP865
 | 
DP865
iPad17,4
TCONCTL: This TCON does not support legacy I2C format
%@/%s/%s.bin
iPad8,9
    tconctl -v                                       - Verbose
DCPTCON.m
Error: PRC index out of range [0, 3]
MCU required but not initiallized
tconModelObj
lcd-eeprom
Error: Incorrect params. Usage: -R eeprom <offset> <size>
Data length must equal count
    tconctl -d 0|1                                   - Dithering enable(1) or disable(0)
max-request-size
DP865.m
Error: Error parsing file
NVM TotalFrmCt %u\nNVM IdxLastBad %u\nNVM PwrOnCnt %u\nNVM PPOrSDPwrOffs %u\nNVM PolPwrOffs %u\nNVM MaxCaVal %d\nNVM Log %d\nNVM Last %d\nNVM ConsPolPwrOffs %u\nNVM GoodPwrOffs %u\n
iPad8,5
TCON unsupported
lcd-pmic
Error: Write exceeds 16 bit addressing
Non-authentic display detected, skipping update.
    tconctl -a device file                           - Program display device: eg: cpld\n
DP855.m
Failed to put TCON into DFU mode. Quiting Updating the firmware
AppleCfg:  %02X %02X %02X %02X %02X %02X %02X %02X\n
frc
TCONCTL: error: failed to read major version from NVM (0x%x)\n
vendorString
Found MCU: NXP KL02
lcd-pgamma
NVM RptPol Bins(%d): 
Error: Count must be <= %u\n
Error: NVM file not found
Searching for %s\n
Error: Can't read from offset %04X (addr = %02X ret = %x)\n
    tconctl -J cmd sub opt1 opt2 count [file|data..] - Send a write command to the firmware command interface\n
Live Histogram\nIndx Rate FrameCnt
iPad17,2
Failed to get HWCID
TCONCTL: writeRegister:0x%x ret:0x%x
Error: Can't protect EEPROM
Updating EDID
%d:\t%d\t%d\t%d\n
dataImage length is %d \n
TCONCTL: Successfully prepared FW Image
TCONCTL: Error: EEPROM contents did not match expected
File not available
Error: Can't read from offset %04X\n
NVMEM offset must be multiple of 256.
tconctl.m
    tconctl -i -W [-n] addr [offset] data [data..]   - Write data bytes to I2C device, -n to specify an offset, otherwise legacy format where offset is pre-set using -C
    tconctl -g 0|1                                   - Gamma Correction enable(1) or disable(0)
S6TUUP1.m
Error: Failed programming NVM (0x%x)\n
Error: Missing %s filename param\n
Error: Unsupported TCON
Error: Offset must be in range [0,FFFFFF]
 failed to enabled TCON I2C bridge
Error: failed programming EEPROM
Saving PRC table %d\n
%u 
lcd-mcu
TCONCTL: error: could not find dcp-tcon service in registry
 Failed to read after Reset TCON
DP835
TCONCTL: readGPIOIn:%d
TCONCTL: Failed to sort FW Sections
Error: Mismatch
    tconctl -O page offset mask                      - Bitwise or the value in an internal register with mask
Comparing EDID version
TCONCTL: Expected contents:
self.dmApi
MCU\n
ConfigVer: %02X.%02X\n
cdic
boot status = 0x%X\n
appleCfg
Updating Config0
iPad8,2
iPad8,3
iPad8,10
TCONCTL: note: using default major version
gamma
Loading tconcfg 
Live Buffer\nIndx Rate FrameCnt
/usr/local/standalone/firmware
Failed to read boot status
_display.dmMcu
%02X%c
tconctl v12.1
lut
sstTempDda
Bootloader Mode
    tconctl -D                                       - List devices\n
fw_b
 
NVM Write Address: 0x%08lx\n
iPad7,10
App Invalidate failed. Aborting
*** PASS ***
iPad7,4
Error: Command data file not found
eq
/usr/standalone/firmware
Can't update device - not present or already updating
Failed sending image size to MCU. Aborting
auth-passed
    tconctl -V                                       - Verify MCU version
pgamma
fw_a
EDID:      %d / %d\n
tcon-api
    tconctl -z                                       - Reload PRC from NVM
MCU is not running application
ret
Initializing DP825
    tconctl -L                                       - Get all MCU logs
BL
iPad16,4
self.display.dmI2c
Hibiscus
iPad7,8
tcon-registers
lcd-i2c-generic
Fail - passed:%d error:%d\n
12.1
    tconctl -N                                       - Get MCU NVM entries
TCONCTL: File not found in %s\n
TCONCTL: Successfully copied ROM 0x%08X, into firmware image 0x%08X,
TCONCTL: FAILED to write EEPROM at offset 0x%x (0x%x)\n
devices
Reading bootloader size
Failed to write dtcm
engamma
sstloc
SDOM:      %d\n
Magnolia2
Error: Error reading file %s\n
\nFailed to read NVM at offset %x\n
Fail %x\n
    tconctl -c                                       - Print display configuration
edid
cfg
Bridge I2C\n
backlight
TCONCTL: FAILED to erase EEPROM at offset 0x%x (0x%x)\n
Failed to write boot blk offset
prc3
Error: Command data file corrupted
com.apple.tcon
 EPI
tcon-
iPad16,3
[%s:%d] Error:(%s) ret:0x%lx\n
DisplayJ327
DP655
DP835
DP815
DP855
TCON
DP865
DCPMCU
MCU
DP875
DCPTCON
Nesos
DP825
S6TUUP1
Display
i32@0:8^@16@24
v20@0:8B16
@\"TCON\"
i32@0:8I16*20I28
i36@0:8@16*24S32
i28@0:8@16i24
[32c]
i32@0:8@16@24
{_NSRange=QQ}20@0:8I16
i24@0:8^I16
^{__IODPDevice=}16@0:8
@24@0:8i16B20
i16@0:8
i28@0:8I16*20
i28@0:8@16I24
B
i28@0:8r*16B24
[16C]
i36@0:8{_TCONMCUCommand=CCCCI}16*24B32
i20@0:8i16
@24@0:8r*16
^{__IODPDevice=}
I28@0:8@16B24
i32@0:8*16^I24
v20@0:8C16
I
@\"NSDictionary\"
B32@0:8@16^@24
i32@0:8@16I24I28
C24@0:8r*16
^{__IOAVDisplayMemory=}
C16@0:8
v20@0:8I16
@\"NSMutableDictionary\"
@\"NSSet\"
i32@0:8C16C20*24
i24@0:8*16
v24@0:8@16
i24@0:8I16C20
[11C]
i20@0:8C16
i24@0:8^B16
i32@0:8*16*24
I24@0:8r*16
i40@0:8r*16I24*28I36
^{__IOAVDisplayMemory=}16@0:8
@\"NSMutableArray\"
i24@0:8I16I20
i20@0:8I16
i32@0:8i16i20*24
i40@0:8^@16*24*32
i32@0:8r*16r*24
i28@0:8C16^B20
i24@0:8^@16
i32@0:8C16*20I28
^{__IOAVDevice=}16@0:8
^{__IOAVDevice=}
@16@0:8
i36@0:8C16I20*24I32
C
@\"NSArray\"
@36@0:8@16@24B32
i24@0:8C16C20
i28@0:8*16I24
@28@0:8@16B24
B16@0:8
I16@0:8
i24@0:8@16
v16@0:8
i28@0:8i16*20
*16@0:8
B36@0:8I16*20*28
i24@0:8^S16
i36@0:8C16C20*24I32
@\"Display\"
@\"MCU\"
i24@0:8r*16
^{__IOAVDisplayMemory=}24@0:8r*16
i20@0:8B16
i28@0:8C16r*20
getAppVersion:
getPolarityStuckMS:
stringWithContentsOfFile:encoding:error:
getIORegistryEntryForComponentByName:
initWithDisplay:eeMemMap:verbose:
verify
T@\"NSMutableArray\",&,V_nvmUpdateSectionsKeysSorted
_mcuRequired
getProdStatus:
tconPageCount
getConfigMajorVersion:
hasPrefix:
maxRequestSize
setRegisterBits:mask:
display
spiAccessEnable
ditherControl:
nvmForceUpdateSections
objectForKey:
TI,R,D,N
_nvmSkipSectionsKeysSorted
array
isEqualToData:
setWithArray:
stringWithFormat:
T^{__IOAVDisplayMemory=},R,N,V_dmCPLDUsr
T@\"NSMutableDictionary\",&,V_nvmUpdateSections
T^{__IOAVDisplayMemory=},R,N,V_dmPgamma
_bootArgs
_dmPLS
copy
dmPLS
setNvmSkipSectionsKeysSorted:
_nvmForceUpdateSections
bytes
prcReload
printNVMSummary:
setObject:forKeyedSubscript:
T@\"NSSet\",&,V_protectedSections
useDefaultMajor
_dmCPLDConfig
_eeMemMap
getConfigVersion:
getParameter:param:
setFrameTolerance:
defaultMajorVersion
getSDOM:
setParameter:param:
_modelStr
appendData:
protectedSections
readBridgeI2C:offset:buffer:size:
printLiveBuffer
dmPmic1
readDPCD:buffer:size:
update:mask:
writeRegister:buffer:
_dmApi
T@\"NSArray\",&,N,V_protectedRanges
T^{__IOAVDisplayMemory=},R,N,V_dmEeprom
_display
dmCPLDConfig
objectForKeyedSubscript:
readRegister:offset:buffer:
getDmFromString:
dictionaryWithObjects:forKeys:count:
dumpLogs:
dumpPrc:filename:
i2cAddressOfBridgeDevice:
initWithDisplay:verbose:
setPlatformType:
write:size:
programEeprom:force:
setProtectedSections:
eepromSize
printNVMEntries:
replaceBytesInRange:withBytes:
write:data:size:
T@\"Display\",&,N,V_display
_majorVersionAddr
displayConfig
dmCPLDUsr
length
writeToFile:atomically:
tconFWDoNotLoad
clearRegisterBits:mask:
loadImage:withPathBase:
readRegisters:buffer:size:
.cxx_destruct
_nvmUpdateSections
configure
dataWithBytesNoCopy:length:
dictionaryWithDictionary:
getHwCID:
read:size:
setProtectedRanges:
_nvmUpdateSectionsKeysSorted
command:data:read:
programMCU:reset:
sendCommand:sub:reply:
writeI2C:buffer:size:
writeSPI:offset:buffer:size:
configEEPROMWP:
_nvmSkipSections
eraseEeprom:size:
getDisplayComponentHandleByName:
printHistogram
setPolarityStuckMS:
writeEepromAt:buffer:size:
_verbose
bootArgs
initWithTcon:verbose:
T@\"NSArray\",&,V_nvmForceUpdateSections
dmTcon
insertObject:atIndex:
read:buffer:size:
valueWithRange:
deviceSpecificHelp
setDisplay:
stringWithCString:encoding:
writeDPCD:buffer:size:
_tcon
dpDevice
getAPChipRev:
loadImage:
printLiveSummary
_defaultMajorVersion
_dmPmic1
isEqualToString:
newlineCharacterSet
_fwAccessSecret
T^{__IOAVDisplayMemory=},R,N,V_dmI2c
_avDevice
_dmCPLDUsr
writeRegister:offset:buffer:
TB,N,V_verbose
stringWithUTF8String:
unsignedIntValue
writeRegisters:buffer:size:
dataWithBytes:length:
disableRegAccess
getStateBL:FW:
getWeekAndYear:
T@\"NSMutableArray\",&,V_nvmSkipSectionsKeysSorted
characterAtIndex:
fwRunning
init
mcuCommand:data:read:
setAutoShutdown:
T^{__IOAVDisplayMemory=},R,N,V_dmApi
_findIntersectingProtectedRangeForAddress:
_mcu
gammaControl:
mutableCopy
skipLines:line:
dataWithContentsOfFile:
displayKnownDevices
getInterfaceType:
setNvmForceUpdateSections:
TB,V_fwRunning
T^{__IOAVDisplayMemory=},R,N,V_dmTcon
_dmEeprom
getModelStringDPCD:
parseTable:output:version:
TC,R,N,V_fwRunning
componentsSeparatedByCharactersInSet:
setEepromShadowSections:
enableRegAccess
T^{__IOAVDevice=},R,N,V_avDevice
enableFwAccess
numberWithUnsignedInt:
setVerbose:
substringFromIndex:
dmPgamma
getAppleVersions:
resetNVMLogs
_protectedRanges
avDevice
getEepromAddress
getFrameTolerance:
intValue
integerValue
containsObject:
verbose
TC,V_defaultMajorVersion
protectedRanges
addSection:intoSection:
getDisplayComponentAddressByName:
setMajorVersionAddr:
_dmI2c
_dmPgamma
majorVersionAddr
tconI2CBridgeEnable:
verifyEEPROMMatches:offset:length:
_protectedSections
programPrc:filename:
unlock
dfuModeAndResetTCON:
T@\"NSMutableDictionary\",&,V_eepromShadowSections
countByEnumeratingWithState:objects:count:
getAutoShutdown:
indexOfObject:inSortedRange:options:usingComparator:
loadImage:model:type:
_regAccessSecret
disableMCU:
getDPCDMappingForOffset:page:offset:
getVendorId:
readBridge:offset:buffer:size:
whitespaceCharacterSet
T^{__IOAVDisplayMemory=},R,N,V_dmMcu
getBLVersion:
raise:format:
readRegister:buffer:
update:state:
nvmSkipSections
UTF8String
_dmMcu
count
isAuthentic
T@\"NSMutableDictionary\",&,V_nvmSkipSections
TI
prepareFWImage:
getCodeNameString
removeObjectForKey:
dataWithLength:
nvmSkipSectionsKeysSorted
resetLiveLogs
wpControl:state:
TI,V_majorVersionAddr
eepromShadowSections
getConfigSize:
nvmUpdateSections
arrayWithObjects:count:
enableNVMLogs:
getBoardId:
getEepromSNOffset
getPageCount
rangeValue
readRegisters:offset:buffer:size:
resetBanyan
setBootArgs:
setDefaultMajorVersion:
writeEeprom:buffer:size:
enableMCU
nextObject
objectEnumerator
setNvmUpdateSections:
T@\"Display\",&,N,Vdisplay
clearI2CAddress
getSdom:
objectAtIndexedSubscript:
readI2C:buffer:size:
writeRegisters:offset:buffer:size:
addObject:
storeNVM
subdataWithRange:
tconFWLoad
programDisplayDevice:filename:
readSPI:offset:buffer:size:
supportsShadowSectionsROMCopy
readGPIOIn:val:
T^{__IODPDevice=},R,N,V_dpDevice
dmMcu
needEepromUpdate:force:
verifyPlatformType:
T^{__IOAVDisplayMemory=},R,N,V_dmPLS
getDisplayComponentPropertiesByName:
setNvmSkipSections:
enableLiveLogs:
_dpDevice
dmI2c
nvmUpdateSectionsKeysSorted
readEeprom:buffer:size:
readEepromAt:buffer:size:
writeBridgeI2C:offset:buffer:size:
combinedI2C:offset:buffer:size:
T^{__IOAVDisplayMemory=},R,N,V_dmPmic1
verify:
_bootArgsValid
dmApi
getModelStr
getPlatformType:
lock
T@\"NSArray\",&,V_nvmUpdateSections
initWithLength:
setNvmUpdateSectionsKeysSorted:
appendString:
getBytes:length:
setI2CAddr:
writeBridge:offset:buffer:size:
_dmTcon
_eepromI2CAddr
setFwRunning:
T^{__IOAVDisplayMemory=},R,N,V_dmCPLDConfig
update:
_eepromShadowSections
_fwRunning
dmEeprom
getProductString
getSerialNumber:size:
```
