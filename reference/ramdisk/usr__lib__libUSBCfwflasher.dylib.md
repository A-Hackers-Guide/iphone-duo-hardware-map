# `/usr/lib/libUSBCfwflasher.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 463,728 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 3832)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libUSBCfwflasher.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (5 classes, 1 protocols)

Classes: `IECSInterface`, `IOKitUtilities`, `flashUpdater`, `iecsUpdater`, `swdUpdater`

Protocols: `flasher`

## Strings (1,648)

```
iecsUpdater
flasher
IECSInterface
swdUpdater
IOKitUtilities
flashUpdater
isEqualToDictionary:
setService:
takePowerAssertion:
whitespaceAndNewlineCharacterSet
isDone:
isRegistryEntry:descendentOfRegistryEntry:outValue:
unsignedLongValue
releasePowerAssertion:
updaterSupported:
init
locatedObjects
name
numberWithUnsignedInt:
_cfPlugInInterface
attemptIECSCommand:flags:withData:dataLength:retData:retDataLength:timeout:andErrorResponse:
enableDisableRetries:
iecsReadForAddress:buffer:length:flags:andOutReadLength:
setData:
setVerbose:
_deviceInterface
addObject:
bytes
query:andErrorResponse:
writeToFile:atomically:encoding:error:
appendBytes:length:
fUpcomingFirmwareVersionStash
gaidEnabled
dealloc
arrayWithCapacity:
copy
deviceService
flashHCPM:andErrorResponse:
initWithInterface:
optkeyshash
.cxx_destruct
initWithService:isHCPM:
_locatedObjects
_userClientActive
boolValue
objectEnumerator
uint32ForRegistryEntry:andKey:outValue:
verbose
getBytes:length:
setDeviceService:
setLength:
enableDisableGAID:
initForSimulation
createUserClient
dataWithBytes:length:
defaultManager
fInterface
rangeOfData:options:range:
initWithDevice:
createFileNameForFirmware:
device
data
dictionary
initWithService:
objectAtIndexedSubscript:
stringByTrimmingCharactersInSet:
uint64ForRegistryEntry:andKey:outValue:
updated
checkForBootArgs:
countByEnumeratingWithState:objects:count:
dictionaryWithDictionary:
getHCPMinfoImpl:
isEqualToString:
arrayForRegistryEntry:andKey:outValue:
isHCPMversionFormat:
next:
nextObject
T@\"NSArray\",&,N,V_locatedObjects
getAceHeaderOffset:ofSize:intoRidgeOffset:intoAceOffset:andLength:signature:alternateSignature:andDeviceType:andVersion:andAppConfigVersion:andNextHeaderOffset:
objectForKey:
setLocatedObjects:
sharedInstance
stringWithUTF8String:
UTF8String
compare:
dictionaryWithCapacity:
isAllowableBCDByte:
stashFirmwareVersionInFile:
initWithFormat:
catalogIECSDevices:
enableDisableFirmwareUpdateMode:
fConnection
stringWithFormat:
_service
catalogSWDDevices:
description
findSWDMatchingDeviceNode:withError:
locatedDevices
device_id
retriesEnabled
fRetriesEnabled
rid
errorWithDomain:code:userInfo:
selectUpdaterWithRID:
service
length
setObject:forKey:
_deviceService
version
attributesOfItemAtPath:error:
getDeviceInfoNameWithConfigOnly:
objectForKeyedSubscript:
reset:
unsignedIntValue
count
dictionaryWithObject:forKey:
execCmd:withInput:andOutput:andErrorResponse:
flash:andErrorResponse:
getHCPMinfo:
iecsAtomicCommand:data:dataLength:retData:retDataLength:flags:timeout:
initWithConnection:
initWithOptions:andErrorResponse:
numberWithUnsignedLong:
entryID
TI,N,V_service
TI,N,V_deviceService
destroyUserClient
fGAIDEnabled
iecsWriteForAddress:buffer:length:flags:
initWithDomain:code:userInfo:
upcomingFirmwareVersionStash
iecsWaitForIdle:pollInterval:timeout:
locatedDeviceEnumerator
setValue:forKey:
unsignedLongLongValue
sharedInstance:
currentDevice
setObject:forKeyedSubscript:
uuid
i20@0:8I16
v24@0:8^@16
B32@0:8@16^@24
B20@0:8C16
i28@0:8I16I20I24
I16@0:8
v24@0:8@16
I32@0:8[128c]16^@24
i36@0:8I16@20^I28
i36@0:8I16@20^@28
B32@0:8@\"NSMutableDictionary\"16^@24
i60@0:8I16I20*24S32*36S44I48^@52
@\"IECSInterface\"
B24@0:8*16
Q
i32@0:8I16I20^B24
@\"NSMutableDictionary\"
@20@0:8I16
B104@0:8r*16Q24^I32^I40^I48@56@64^I72^I80^S88^I96
@24@0:8I16B20
i48@0:8C16^v20Q28I36^Q40
v20@0:8I16
@\"NSEnumerator\"
@\"<flasher>\"
B
B20@0:8B16
B24@0:8@16
B32@0:8@\"NSDictionary\"16^@24
v16@0:8
i64@0:8I16^v20Q28^v36Q44I52Q56
i36@0:8I16@20^Q28
B48@0:8@16@24@32^@40
@\"NSNumber\"16@0:8
@\"NSString\"16@0:8
@24@0:8@16
@24@0:8^@16
@\"NSNumber\"
^^{AppleHPMLibInterfaceStructV3}
@\"NSArray\"
@32@0:8@16^@24
B24@0:8^@16
@20@0:8B16
B20@0:8I16
i16@0:8
^^{IOCFPlugInInterfaceStruct}
@16@0:8
B24@0:8@\"NSString\"16
@\"NSString\"
i40@0:8C16^v20Q28I36
I
i24@0:8^I16
length = %u bytes
end marker
Raw level
ASTRIS_ERR_NOTSUPPORTED
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
Error initializing flash mode
Crash level
relay_get: %s = CMD_ERR (%s)
{%s} select success without file descriptor set
ace_firmware_offset: 0x%08x
Flash start failed as region is invalid
Expected firmware version: %X%02X.%02X.%02X.%u
ASTRIS_ERR_TGTOFF
Toto
Ace got a signature verify request when no keys were programmed?
Warning:  Error resetting PRGN after flashing.
[AstrisAsync] Got ASYNC_RESTART response!
ASTRIS_ERR_EENOTFOUND
XINIT
DIAGS
Failed to stat file (1): %s %s
!! Production key was present !!
execCmd - prepping for flash
AppleAstrisGpioProbe
unable to create connection
Unique required when more than one probe identified by
the new firmware image running
Did NOT build matching dict
Failed to read
/swdflashers
Debug Port
ACQ_STARTSTOP
USB-C_FW
Failure code: 0x%08X
SUCCESS
Failed to send flash verify command. status=0x%02x
Error transferring the payload, bytes remaining: %d
=== Found %s Boosters ===\n
EICE
## dpw 0x%02X failed (%s)\n
!! CRC Failure !!
activeFWVersion
explore
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
Writing version %@ to disk at %@ (2)
***** The USB-C controller chip is in a bad state and needs to be reset/power cycled
Initialization Error
Attempting to un-bork firmware... status = 0x%X
...Unable to create Device Interface. err = 0x%X
Std
invalid host name or port
Unable to create pthread key for conenction. errno=%d %s.
darts
ret.storePairForPref
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
ace_length %08x, aceTotal %08x, TotalFlashImageSize %08x, nextImageOffset %08x  (Ace2)
...Unable to find parent for IECS service.  err = 0x%X
!! Engineering key was present !!
Did NOT find service(s) matching AppleHPMDevice(index:%d)
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
Can't get OS build version - failed to allocate buffer
ASTRIS_ERR_FDSETOVERFLOW
IOPropertyMatch
not connected
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
With Preflash Type %d\n
ViewSWD
%s_probe
INIT
complexes
cleanup_astris_api
ASTRIS_ERR_TOOMANY
!! Version check failed !!
a
ASTRIS_ERR_ASYNC_BARRIER
NOP
Firmware Path
Creating NXP Flasher\n
Could Not Match A Booster for %s\n
bad parameter(s) specified
PROBED_ASYNCSKIP
ace_length %08x, aceTotal %08x, TotalFlashImageSize %08x (Ace1)
signature %@ (Ace2)
Ace believes it got all required data
Execution Error
command timed out
{%s} Batch attitude key created for %p thread %#llx key %lu
MODE
!! Unknown Error !!
    aceTotalBinaryCRC:  %08x
FAILURE
exit
relay_get: %s = %d
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
LMFLASH
YES
Current firmware looks old enough to require I2C stability work-arounds (0x%08X)
EXPLORE
Low level
BoosterManager.Utility
ASTRIS_ERR_BADENV
ASTRIS_ERR_NOSOC
probe on localhost
KongSWD
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
Error: Zero payload length sent
Ace expecting more data even though all data has been written.  ABORTING
PORTAL ERR PENDING
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
Values Not The Type We Expected. Expected: Number and String\n
probeBoardNames
default
status
*deviceID: 0x08%X
stdout
You appear to be running a no longer supported version of Ace1 hardware.  Aborting. (%X)
Firmware appears to be below minimum requirement to flash J327.  Attempting to fix
Hash matches engineering key
MiniSWD (USB Comm)
useBorkedSFWWorkarounds: %s
Could Not Create Dictionary From Booster: %s
preflash_type
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
defaults.create.key.outofmem
OK
environment variable not found
Sprocket
JTAGPORT
ace_offset: 0x%X, header_ace->appConfigOffset: 0x%X
performFlash
~
Initializing (%s) Booster's Astris API\n
Could Not Allocate Mutable Dictionary For BoosterMangers
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
ASTRIS_ERR_USB_EMPTY
implementer
PORTAL UNAVAILABLE
invalid environment variable
probed USB transaction timer expired
CPU disabled by SW, not accessable
RESPONSE_NO_PAYLOAD
{%s:%s@%d} Critical error encountered:
Failed to read boot flags. status=0x%02X
Could Not Find Plugin For Chip Information Provided\n
stderr
JTAGAP
** Firmware is NOT newer - 0x%08X.%d vs. 0x%08X.%d
Signature index %04u / %04u
%s%x.%x.%x
deleteClientFromList
UNKNOWN
operation not supported
Failed to send cold-reset command. status=0x%02x
Matched Booster: %s\n
FPGAINIT
...Either firmware didn't update or we haven't switched active partitions. Retrying...
You appear to be running a no longer supported version of Ace1 hardware.  This is almost certainly going to fail. (%X)
Region 0
=== Loaded %s Boosters ===\n
Temporary level
PROBED_ERROR
Signature write returned 0x%02x
IDE ACCESS OUT OF BOUNDS
isAce1 = YES
This firmware image appears to be for a different ROM image variant of Ace2.  This will probably fail. (%X vs. %X)
DOCK-CH-DATA
{%s} DAP command nwords=%d trimmed to %lu\n
Prompt
%s v%s%s [%s]
empty request encountered
  Error path [%s]\n
User
{%s} %s
alt signatureLength: 0x%08lx
init_astris_api
Custom-Feature
param.conn == NULL
ASTRIS_ERR_OUTOFMEMORY
PAYLOAD_OVERFLOW
Firmware appears to be within the range known to have a broken update path.  Attempting to fix
Signature missing and hardware requires signing.  Aborting
soc-pid
{%s} Thread %#llx clearing key %lu
failed init() with device detection failure: %@
In Eraseflash\n
UserCreated
XACT
In Writeflash\n
TIMEOUT
No portal under found for that type
{%s[select]} %d(%s) [RETRYING]
.
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp
Astris
{%s@%d} neither socket nor kext connection available
{%s@%d} Found cached response
SPI
Expected firmware version: %02X%01X.%01X%02X.%02X.%u
Error detected
[AstrisAsync] Discarding response due to ASYNCSKIP state!
HostInfo
KanziSWD
    swapInROMLength:    %08x
Port micro not able to idle.
This error is not recoverable.  Exiting
PMGR_OCLA_REGS
ASTRIS v%s%s [%s]
ASTRIS_ERR_NOAP
probe %s [port %u] on localhost
{%s@%d} Unknown CS code [%u]
Failed to read customer version. status=0x%02x
Region booted: %s
Available signature is too short for RSA-2048 flashing.  Aborting
Error:  Verification failed.
XBS Version Modified: %s -> %s\n
ARM7
XBSRelease
Could Not Allocate Loaded Booster Array
DEBUG_AUTH_REGS
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
{%s:%s@%d} [%s] unable to read response payload\n
!! Wrong Device ID !!
/usr/local/share/astris/boosterpack
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
Firmware Data
Available signature is too short for RSA-3072 flashing.  Aborting
Not a secure update.  No need for useBorkedSFWWorkarounds
ASTRIS_ERR_USB_NOTOPEN
ASTRIS_ERR_DISASM
Error while %s:\n  %s %s
RESPONSE_CMD
Flashing 0x%x bytes (%u blocks) from 0x%08x
localhost
Hash match value unknown: 0x%02X
ASTRIS_ERR_BADPARAM
ParrotSWD
read_resp_payload_via_sock
A
Warning: Default logging location requested when running as root (using [%s])\n
general error reported by probe
NOTICE: Backflashing attempts are allowed
Firmware Offset
Bad Sequence Number %u (0x%X), expected %x (0x%X)
firmware version is too old DEPRECATED
invalid command
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c
port_%d
SPIXACT
Memory modify failed and out of retries.  Aborting as retries were exhausted
usbc-flash-update
com.apple.usbcfwflasher.SleepAssertionID
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
   {%s} (DP): status=0x%X(%s) - %s\n
Failed to hold sleep assertion
In Postflash\n
Firmware does not appear to match hardware (0x%X vs. 0x%X).  Continuing anyway... likely to fail because of this
Can't get OS build version - failed to create plist
high level connection to probe [connect state/status]
probe %s [port %u] on host %s
NOTICE: Retries disabled as per request
currentFirmwareVersion: 0x%08X
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
ret.createKey
astris_dpwrite
Can't get hardware model - failed to find matching IOService
           deviceID: 0x%08x
app2Version
%s: failed to create dictionary
Did Not Find Any Boosters For: %s \n
Value Types Are Not Strings\n
ASTRIS_ERR_PENDING
SWDONLY
    appConfigOffset:    %08x
Offset: %08x
Note:  Running FW version 0x%.8x format in region %d ok.
RID
missing property aod-type
We are in clean up\n
no device when sending request
Error while %s:\n  Unable to connect to %s - %s
Failed to write \"RESETZ\" data. status=0x%02x
\t%s (%s)\n
development
DOCK-CH-CONFIG
Memory Access Port
Invalid Ace Image (ace_offset 0x%X >= image_size 0x%zX)
...checking firmware update ability.  (See <rdar://problem/42441690>)
** Firmware is not newer, but CustomerVersion is - 0x%08X.%d vs. 0x%08X.%d
boot_flags.rawBytes[0]:         0x%02X %u %u
%02X%01X.%01X%02X.%02X.%u
GitHashDebug
     New firmware version: %02X%01X.%01X%02X.%02X.%u
Failed to send warm-reset command. status=0x%02x
New region booted: %s
Error
ASTRIS_ERR_PROBETIMEOUT
time out reported by probe
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
{%s} error %d(%s) reading data from the connection (at recv)
Attempting to force RESETZ...
***** before it's able to accept a firmware update.  It *should* work when if you
Response at Failure
Could Not Find The Entry Function: %s
Can't get OS build version - failed to create URL
ASTRIS_ERR_BLOCKED
%s-%06X
GETSETTCK
Error Message
E
RegionStart
Unable to process command while connecting to
probe [port %u] on host %s
DISCONNECT
OPEN
Could Not Allocate Booster Location Array
no data when data expected
PROBED_USB_REQ_TIMEOUT
JTAG IN CONTROL
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
CSPDATA
ACQ_SAMPLE_SPI
Note:  Flashing v%.8x over v%.8x in target region %d
...Unable to create CFPlugInInterface. err = 0x%X
Connection is NULL, might not have found something to connect to.\n
SimulatorSWD
{%s@%d} socket connection is not available
read_via_sock
%s %s:l=%u,c=0x%X,i=0x%X,f=0x%X
Failed To Init Booster's Astris API In: %s with %s (%d)\n
APCIE_ANS1
Async barrier encountered
Someone is calling iescUpdater::init directly - should always use custom initializer
    firmwareVersion: 0x%08x
ASC_ECORE_ROM
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
ASTRIS_ERR_BADPROTOCOL
BitboxSWD
MAIN_DEBUG_ROM
{%s} %s: |%s|-|%s|
SRST
rpc
ONEWIRE
Booster:\n
MINISWD
Another application is connected to
    aceDeviceID:        %08x
IOPlatformExpertDevice
SLEEPING
Flashing failure detected...
failed init() for flashUpdater instance
Could Not Get BoosterManager\n
Exception
[AstrisAsync] Failed to restart Async batch\n
/var/log/astrisclient
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
?
J327
Astris Source Version: %s\n
partnum
probe
SWDRESET
BLK
Boot flags (before mask)=0x%04X, (after mask)=0x%04X
i
AXbooster_interface_init_astris_api
socnames
Already connected to
STATUS
Creating Nordic Flasher\n
HOSTID=0x%x which is invalid, skipping orientation check
!*!*!* ****************************************************************************** !*!*!*
This is an Ace2 firmware image
status: %u
execCmd - flashing...
ProductBuildVersion
INVMODE
IDLE
GETRELAY
Bad app image size %x
Failed to read firmware version. status=0x%02x
!! Overlay was present !!
basic_string
ASTRIS_ERR_CPUHALTED
XSTAT
ret._cleanup_hw
...Firmware didn't update to expected version.  This was likely an attempt to backflash secured firmware.  Succeeding anyway
Invalid SoC Booster. SoC Booster Requires PID\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
defaults.create.key.no_probe
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
FlamingoSWD
FARB header not at front of file %08x %08x
Connected to Probe Device Server [Log File %s]
{%s@%d} Failed to send probe command (error %d).
APEXPLORE
Ace/Ace2 found.
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
End
   Response at Failure: 0x%02X
ASTRIS_ERR_LOSTCONN
firmwareVersionBuffer[0] = %02X
False
Error:  Flashed Version is unexpected version
IECS command '%c%c%c%c' still outstanding
SFWu response: 0x%02x %02x %02x
%s:%s
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
ASTRIS_ERR_DISABLED
Invalid hostname or port specified as
    aceFWVersion:       %08x
SFWi parameters: 0x%02x %02x %02x %02x
/usr/standalone/firmware
Dock-Channels
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
normal
{%s:%s@%d} [%s] unable to read command response\n
    nextImageOffset:    %08x
Current firmware version: 0x%08X
%s
b
Required Key-Value is a string, and not an array. Old booster found\n
class_var.m_interface_name==NULL
PROBED_USB_INUSE
Exo
Failed to read write expected firmware version to file: %s
Error: Failed to write (0x%08x)
queryInfo
preflash routine returned error
createClientList
Adding new booster path: %s\n
Replacing key with value
ASTRIS_ERR_NOTFOUND
Using useBorkedSFWWorkarounds.  Claiming keys not present
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
host is going to sleep
ASTRIS_ERR_IFSTATE
SETTHREAD
Payload description INVALID
This is a firmware image for an unknown Ace variant
Sending data...
customer version read was short (less than 2 bytes).  Is this possibly Ace1?
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
TGTOFF
astris_command_complete_cache
SFWs response: %02X %02X %02X
New region selected for next boot of port micro.
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
appConfig Version: 0x%X
Ace NOT expecting more data even though we have data left to send.  ABORTING
Failed to write \"MAGIC\" data or send memory modify command. status=0x%02x
param.booster_handle==NULL
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
empty USB packet encountered
Too many open files
SETCLR
aod_type
out of memory
Connected to Probe Device Server [Default Log]
Failed to start flash. status=0x%02x
!
result.booster_api_vers==NULL
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
Warning
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
RTI
%s failure - %s
version string INVALID
Note:  Running FW is not upgradeable by this utility.  0x%.8x < 0x%.8x.
AstrisSWD
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp
Flash write returned 0x%02x
Pause to allow any existing connection to stabilize
IECSInterface::createUserClient...
For production parts make sure you have allow_swd_updates=1 set in your boot-args
Could Not Find Booster Entry Function: %s\n
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Exception %d Stack Trace
createKey
new offset: 0x%02X, firmware_bytes_remaining: 0x%02X
Error Code
execCmd - failed to release power assertion: 0x%X
AP
process (%s) (%d) path: %s
AXconn_create
This firmware image appears to be for a different ROM image variant of Ace2.  Aborting. (%X vs. %X)
ret._release_gateway_control
status = 0x%X
dbgarch
socs_supported
connection not currently open
no SOC object available
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
hid-fw-personality
\t\t%s\n
Booster Value is Not String\n
ASTRIS_ERR_OK
ASTRIS_ERR_PROBEEOF
ASTRIS_ERR_NOBOARDINFO
required parameter is missing
general-purpose failure
toggle-reset-enabled
ASTRIS_ERR_NOTEXPLORED
Communication error occurred while connecting to
{%s[recv]} %d(%s) [RETRYING]
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (prior to IOCreatePlugInInterfaceForService)
InterfaceLocked
STM
Could Not Get Bundle Out Array of Found Boosters\n
/socs
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
this unit or manually reset the port micro before you will see
Attempting to reset port micro to load new firmware
soc-name
BoosterManager.SOC
CoreSight
In Preflash\n
2.34.0
connection to probe is lost
{%s@%d} IOServiceClose failed, err = 0x%08x
Block Count at Failure
aagp-name
Astris default logging context
    aceID:              %08x
specified CPU is not available
{%s} flags:0x%08x
Failed to write
execCmd - ...and done
No more devices
Debug-Components
 %02X
DAP
Previously dumped the process tree, skipping
ASTRIS_ERR_MISSINGPARAM
Can't find header in firmware file
Either firmware didn't update or we haven't switched active partitions.
Error executing xfer / SFWd command @ offset 0x%x
KIS
bundle_id
WRBUF
Can't get OS build version - failed to create ReadStream
Target was lost while connecting to
SOC
APCIE_ANS0
WARNING
ASTRIS_ERR_NODEVICE
ASTRIS_ERR_INVALCOMMAND
probe %s on host %s
{%s@%d} Drain empty on decr [%s].
SRSTM
Apple
Bug
ASTRIS_ERR_USB_EXPIRED
{%s@%d} Timeout while sending probe command.
MAX_KISSWD
You appear to be running a firmware version that cannot be updated from DFU mode.
IODeviceTree:/options
allow_swd_updates=1
(%s) %s
JTAGONLY
PROBED
KIS_DOCK
probed
Begin
ASTRIS_ERR_VARNOTFOUND
ASTRIS_ERR_NOCPU
{%s} probe device server closed the connection while trying to read data (at recv)
Invalid Ace Image (currHeaderOffset 0x%X >= image_size 0x%zX)
force
*****
!! Hash write error !!
Initializing Booster Layer\n
framework
SETRELAY
New firmware version: %02X%01X.%01X%02X.%02X.%u (0x%08X)
Status
Attempting update to RID %@...
booster
IRSCAN
    Status: %u
NOTICE: Failure to backflash will be allowed to fail silently
Failed to send signature write command. status=0x%02x
AppleHIDTransportInterface
We are done with clean up\n
%02d:%02d:%02d:%06ld|%s <%s> %s
PlayerSWD
ACQ_SAMPLE_I2C
Path to Firmware Version
newBoot_flags[0]:               0x%02X %u %u
!!!!!!!!!! Please enter the following commands to set proper permissions:\n
ASTRIS_ERR_BADFIRMWARE
getAceHeaderOffset failed
SFWd response: 0x%02x %02x %02x
IOService
Failed to convert CFString to C String.
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
Region 0x%02x%02x
***************
!! ENGR over PROD !!
Did not create enumerator
One time initialization of oslog API failed!\n
ASTRIS_ERR_STOPCLOCK
CPU-level (general and architecture-specific)
probe %s on localhost
alloc_drain_payload
Warning:  Error setting Grst.
Failed to initialize Astris
SWDFlasher
Bug detected
ARMDAP
Hash matches UID key
RegionEnd
## dpw 0x%02X 0x%08X\n
relay_get: %s = ERR
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (after to IOCreatePlugInInterfaceForService or at exit)
execCmd - setting firmware location: %s
param.conn.user_defaults == NULL
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
XPROG
 
Master BoosterManager
unknown
Aborting the flash attempt.  Please follow care & feeding instructions
!! Hash failed !!
%s%s
\n
ASTRIS_ERR_IGNORED
ASTRIS_ERR_ANOMALY
{%s@%d} IOServiceOpen failed, err = 0x%08x
Error closing %s [%d]
Region 1
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Can't get OS build version - failed to get build version
postconnect
Note:  FW version is not same or newer (running v%.8x, thisVersion v%.8x
AXLOG
ASTRIS_ERR_NOTCONN
ASTRIS_ERR_NOTPRESENT
Successfully connected to
FACTSERNO
NOTICE: Forcing install regardless of chipID (likely enforced by hardware anyway)
ASTRIS_ERR_EXPIRED
Note:  System may require a full A/C power cycle to update to the new FW.
_log_setup_thread_specific
checking if relay \"%s\" is valid
xfer_acmd_via_sock
ace_firmware_length: 0x%08x
Supplied Image missing signatures.
True
Creating ADI Flasher\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
Kick has been requested by probe server
TCP recv
Firmware does not appear to match hardware.  Aborting (0x%X vs. 0x%X)
*** NOTICE: Power cycle unit immediately to prevent risk of unexpected behavior ***
None
%s.%s
remote probe is currently in use
PROBED_USB_REQ_ERROR
EmulatorSWD
%s-%06d
Port micro not in correct mode.
Retrying memory modify command as it looks like it didn't execute...
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s@%d} Failed to find cached response
RELAY
isAce2 = YES
firmwareVersionBuffer[3] = %02X
Both debug and xbs versions are set, maybe a bug: %s
ERR
\n!!!!!!!!!! Error: %d (%s) opening log file %s !!!!!!!!!!\n
PortBridgeSWD
NOTICE: Port micro reset disabled.  Must reset port micro manually after flash attempt'
Can't get hardware model - failed to convert to C string
HTTP transaction failed
PROBED_LOSTCONN
**!** DeviceID for USB-C port controller not recognized: 0x%02X
Released sleep assertion
PROBED_USB_REQ_EMPTY
connection created
SCANDEBUG
AXconn_create failed
SWDFlash
No version information found in booster: %s
LOSTCONN
Using 10pin connector skipping orientation check
    aceBinaryCRC:       %08x
Flash verify success.
Didnt match any service/parent for AppleAstrisGpioProbe
ASC_TCORE_ROM
PROBED_USB_RSP_TIMEOUT
Port micro not in correct mode (yet).
Error: Failed to erase (0x%08x)
Command set required to update this HW is not available.  Update process is forced to abort.
failed super::init()
execCmd - flashed.  error = %s
ASTRIS_ERR_MASKERR
  ...responseCode: %u - %s
Failed to connect to AppleAstrisGpioProbe kext %x
%s/%s
{%s}#%02X cmd: %s, resp: %s
  ...moreDataExpected: %s
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
Main
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
FPI2C
Ace believes it got all required signature data
PMGR_CTI_MUX_REGS
connect
ASTRIS_ERR_ISCONN
already connected
target no longer responding
Bad Sequence Number %u (0x%X), expected %u (0x%X)
Error: Failed to connect (0x%08x). Please confirm boot-arg \"allow_swd_updates=1\" is set.
BoosterPublicAPI
[%s] Booster System Is Not Initialized\n
We Are Matching Development Booster\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Key initialization for oslog API failed! %s\n
unable to transfer command to/from remote probe
BoosterManager.CPU
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
{%s:%s@%d} [%s] failed preconnect\n
{%s@%d} Probe reported connection lost [PROBEEOF].
EPIWRITE
NOTE: The dead battery flag appears to be set
BoosterManager.SWDFlash
[CMD] %02u:%02u:%02u:%06u|%s <%s> %s\n
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
ASTRIS_ERR_EMPTY
AXconn_connect_kext
probe on host %s
 next Header Offset: 0x%08x
   appConfigVersion: 0x%04x
ERROR
target is probably resetting
PROBED_USB_RSP_ERROR
Wait indication while connecting to
Probe
Efficient-Core
some generic JTAG hardware fault
JTAG chain not yet explored
ASTRIS_ERR_FAILURE
Failed to send command. status=0x%02x
Writing version %@ to disk at %@ (1)
Failed to erase
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
PROBED_SLEEPING
{%s@%d} Received %d bytes when requested %d bytes [%s].
This appears to be running on unrecognized port micro hardware.  Aborting
Invalid condition while connecting to
recheckFirmwareVersion marker: %u
Could not find bundle () in given array: %s\n
SWD_BYPASS_REGS
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
UNKNOWN_CODE
Error while trying to disassemble memory
preconnect
{%s[select]} timeout while waiting for data from the connection
Backflashing allowed
Error sending signature
Warn
no USB device
This appears to be running on unrecognized port micro hardware.  This will probably fail
Flashing index %04u / %04u
!!!! FILE RADAR: Don't know how to compare two values\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
ASTRIS_ERR_NODP
astris_err_from_cs_type
Zero payload length sent
Unable to check freshly installed firmware version as port micro has not been reset
N/A
astris
Beginning of set
End of set
target power is OFF
PROBED_USB_REQ_NODEVICE
IECS interface not found or you are running as a non-root user.
firmwareVersionBuffer[2] = %02X
HWERR
{%s:%s@%d} [%s] unable to transfer command\n
Invalid Bundle: %s
cpus
no AP (Access Port)
HTTP transaction running in background
...    ridge offset: 0x%08x
Total bytes to flash %08x
hardware error reported by probe
Region booted: Unrecognized silicon!
Should be ready to proceed with SFWi
aceOffset: 0x%x
Note:  Skipping flash
Should be run as root (uid = %d)
no MEMAP access
incr_drain_packets
firmwareVersionBuffer[1] = %02X
fn.missing_booster_init_api
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
interface not in appropriate state for action
hostid
%s.%s.%s
FAULT
probe [port %u] on localhost
Tarsier
ASTRIS_ERR_NOTUNIQUE
** Firmware is newer (yay!)
This can be a valid condition, and should be cleared by the SMC.
!! Needs SFWd !!
Note:  Backflashing disabled via input parameters.  FW v%.8x <= FW v%.8x
astris_remove_loaded_soc_boosters
AXbooster_interface_create_swdflasher
MEMAP
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
UNKNOWN_CS_CODE
file/object not found
ASTRIS_ERR_MISMATCH
%s given a NULL conn object
%s_%d
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
META
Error data:
assert
KICKINFO
AppleHPMDevice
MASK ERROR
%s.console.%s
{%s:%s@%d} [%s] unable to drain response\n
%02X 
PERSEIS
Could Not Get BoosterManagerUtility\n
target not in appropriate state for action
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
RESPONSE_PAYLOAD_DONE
usbc-fw-personality
batch_cmd_count: %d
INVALID KIS VERSION
Error with SFWv command
ASTRIS_ERR_NOPORTAL
!! CRC busy !!
Gathered Info:\n%s
ADI
User interaction
Created Connection - : %s
** Current firmware is an engineering build. Ignoring firmware version check - 0x%08X.%d vs. 0x%08X.%d
Note:  Running FW v%.8x >= min FW v%.8x -- Can update: %s
Dumping Process Tree
Version
HCPM detected, deviceType=0x%04X
Existing firmware version: %02X%01X.%01X%02X.%02X.%u
probe matching %s on localhost
NO
Firmware appears to correctly match the target hardware. (0x%X)
This error may be recoverable.  Allowing retries
Flashing signature 0x%x bytes (%u blocks)
newCustomerVersion:             0x%04X
Flashing error encountered
ASTRIS_ERR_SLEEPING
ASTRIS_ERR_USB_PROBED
expectedFirmwareVersionBuffer:  0x%02X %02X %02X %02X
AXbooster_interface_cleanup_astris_api
Required Key-Value is a string, and not an array. Old booster found: %s\n
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
%s %s
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
Creating Cypress Flasher\n
DP
Hardware model: %s
Error level
ASTRIS_ERR_TGTLOST
astris_command_async
MAP_CMD
Invalid Ace Image ((ace_length 0x%X + ace_offset 0x%X) <= image_size 0x%zX) && (TotalFlashImageSize 0x%X <= kAceAppSize 0x%X)
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
UNKNOWN CODE
ASTRIS_ERR_BADHOST
GorillaSWD
CLOSE
    signatureLength: 0x%08lx
Standard
Unable to connect to
{%s} drain_packets=%d [%s]
deviceType=0x%04X
useResetZWorkarounds: %s
Timeout occurred while connecting to
probe matching %s on host %s
Koko
ASYNC
abort
isAce2 = %s
activeRegion
astris_explore_enabler_init
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
This firmware image appears to be for a different ROM image variant of Ace (%X vs. %X), but additional header(s) found.  Trying next header.
execCmd - failed to hold power assertion: 0x%X
TARGETSEL
  Decoding error responses...
User created bundle found, ignoring version checking via plist
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Standard level
Name
MEMm response: %02X %02X %02X %02X
Previous Error
com.apple.astris
%02u:%02u:%02u:%06u|%s <%s> %s\n
Access Port
No MEMAP access while connecting to
read_resp_cmd_via_sock
Note:  Running FW version in region %d is not formatted correctly (0x%.8x), indicating very old FW that cannot be updated.
AppleSPUControl
Could Not Allocate All Boosters Array
Output
generic error injected by probed
Note:  Setting Grst for reset on SSPS(6).
execCmd - flashed.  result = %s
%s: Didn't find client in dictionary
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
TLR
    ... Updater not Valid!
Connect
SWDFlashErase
BYPASSCH
execCmd - input dict: %@
load_booster
astris_command_lock
ASTRIS_ERR_INVAL
ASTRIS_ERR_CPUNOTHALTED
    aceBinarySize:      %08x
In Readflash\n
NRF
%s_%s
%s/%@%s
Warning level
ASTRIS_ERR_WAIT
    swapInROMBase:      %08x
appConfigVersion:               0x%04X
!!!! Critical Error: batch attitude thread trying to lock - CAN'T LOCK !!!!\n
!!!!!!!!!!   $ sudo chmod 0775 %s\n
EPIREAD
New boot flags (before mask)=0x%04X, (after mask)=0x%04X
Unable to register assert upcall %s (Insufficient memory)
CPU is not halted
ASTRIS_ERR_PROBED
DPAP
teardown marker
Missing property aagp-name
[CLEANUP]\n
Error %d (%s) while expanding ~ for Astris log file base\n
kext connect name %s\n
JTAG error while communicating with
astris_command_base
astris_soc_release
%d
Skipped due to error in Async batch
Did NOT build matching dict(index:%d)
Error: [0x%08X] Mismatch expected: 0x%02x received: 0x%02x
AXconn_showname
KobaSWD
Can't get hardware model - failed to allocate data buffer
no DP (Debug Port)
SoC clocks are stopped. No MEMAPs allowed 
    swapOutROMBase:     %08x
Flash verify returned %02x
Index: %u
required
INFO
ASTRIS_ERR_HTTP_FAILURE
ENUM
    bootConfigSize:     %08x
Using older sigatures.  Flashing only Ace component (%u bytes from 0x%X)
Port micro successfully restarted after flash
execCmd - queried.  error = %s
%04X:
ASTRIS_ERR_ASYNCSKIP
TGTSTAT
.bin
ASTRIS_ERR_NODATA
getAceHeaderOffset reporting status = 0x%X
Likely it means you will need to either manually cold boot
app1Version
Successfully updated to %s%x.%x.%x
m_core_api_serial_queue
axlog_assert_upcall
NOTEXPLORED
INVPARM
boot-args
SWDFlasher.API
fn.missing_entry_function
/cpus
Failed to sync prefs at beginning
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
AstrisArmProbeServer-3679.40.30~172 (RavePopB tools)
Could Not Allocate Memory
Ace not scheduled to boot from newly flashed region for some reason... NEEDS DEBUG
USB-C_%s
-Lite
{%s} %s: |%s|
GEN
Could Not Find The Astris Init Function (%s) in %s
Can't get OS build version - failed to open ReadStream
Error data: %@
Creating Flasher For An Unknown AOD Type: %d\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
Can't get hardware model - failed to allocate data string
Status/State
{%s} couldn't set thread specific - %s\n
sendGAID marker
SWDFlashWrite
Tiny-Core
Can't get hardware model - failed to create string
ASTRIS_ERR_NOMEM
CHAINERR
REG
newFirmwareVersion: 0x%08X
Firmware is not within range required for useBorkedSFWWorkarounds
Could Not Find Any Boosters of Type: %s\n
typehint
Could Not Allocate Info Keys Array
Arm
Unable to get version info from %s [error %s]
ChimpSWD
Did NOT find service matching AppleHPMDevice
invalid aod-type
astris_remove_loaded_cpu_boosters
Gathered Value is Not Number\n
user
{%s@%d} Unknown CS command error [%d]
***** restart or begin another restore attempt
lldb
no board info file loaded
timeout or watchdog expired
TOOMANY
newFWVersionBuffer:             0x%02X %02X %02X %02X
AXconn_connect_kext failure - %s
CPU
ASTRIS_ERR_PROBECOMMAND
Transaction
KIS translator version : %d\n
SLEEPCTL
DBG_WRAP_REGS
LCDCTL
Port micro in mode '%c%c%c%c'
SFWi response: 0x%02x %02x %02x
AMCNP_GFX
Flash start returned 0x%02x
NXP
read_resp_via_sock
This is an Ace firmware image
options
remote EEPROM not found
astris_command_complete
VERSION
     New firmware version: %X%02X.%02X.%02X.%u
New region booted unable to be reported: Unrecognized silicon!
Block Count at Failure: %u
isFactory
BoosterManager
DOCK-CH-AGENT0-STATUS
!!!!!!!!!!   $ sudo chown $USER %s\n
ASTRIS_ERR_TIMEOUT
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp
ASTRIS_ERR_NOTOPEN
OS build version: %s
{%s} already connected
CHIPCNT
ASTRIS_ERR_USB_NODEVICE
astris_cs_code_name
  TotalFlashImageSize: 0x%08X
customer version read was short (less than 2 bytes).  Is this the correct HW?
IOClass
Error: Failed to connect (0x%08x)
ASTRIS_ERR_JTAGERROR
Imago
decr_drain_packets
Firmware header:
...checking firmware update ability...
Error occurred: 0x%X
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
AXbooster_interface_create_soc
storeBoardName
%s/Library/Logs/Astris
Portal Status has an error
{%s@%d} Probe response payload read when no payload indicated.
                Status: %u
UNKNOWN_DAPSTAT
BADCODE
    DeviceConfigPtr:    %08x
***** NOTE: PurpleRestore will fail now, as this is going to drop the USB link.
ASTRIS_ERR_PROBEERROR
ASTRIS_ERR_RESETTING
Mask condition met in conditional operation
No probes were found matching
    swapOutROMLength:   %08x
gaidEnabled = %s
UUID
Gathered:\n
Can't get hardware model - failed to get property
%s.console
no error
ASTRIS_ERR_PROBEINUSE
Silence backflashing failures
preflash-type
Booster Info:\n%s
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
probe refused to process the command
ASTRIS_ERR_PORTAL_STATUS
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
    aceTotalBinarySize: %08x
Existing firmware version: %X%02X.%02X.%02X.%u
Held sleep assertion
Could Not Find Any Loaded Boosters of Type: %s\n
/System/Library/CoreServices/SystemVersion.plist
MEMAP_APB
!! Too much data !!
=== Detailed %s Boosters ===\n
Input
xfer_acmd_via_kext
isAce1 = %s
AXbooster_interface_create_cpu
astris_user_default_set_boardname
USB connection not currently open
reset_connect_state
PersiesSWD
%s: chip was NULL when attempting to release soc
remote probe closed connection
PROBED_USB_NOTOPEN
/
Could Not Find Any Boosters\n
%s\n
Failed to sync prefs at end
too many of something
{%s}#%02X %s [%s]
Aborting as this would result in a backflash
Using modern sigatures.  Flashing combined components (%u bytes from 0x%X)
...Retrying...
HCPM flash status: %d
model
Ace response code: 0x%02X
Failed to release sleep assertion
DEBUG CLOCK OFF
Error: Failed to read (0x%08x)
aod-type
OCLA_IP_REGS
astris_ba_free_attitude
vvvvvvvvvvvvvvvvvvvv DUMP OF HISTORY LOG vvvvvvvvvvvvvvvvvvvv
Component is not present
%s (%d)
ASTRIS_ERR_PROBEHWERR
Modifying memory...
!! Hash doesn't match any key !!
Note:  Resetting PRGN.
invalid parameter
FWUPDATE
Failed to write \"RESETZ\" data or send memory modify command. status=0x%02x
  ...SFWi_status: %u - %s
Should think SFWu now usable
(0x%08llX) %s
anomaly detected
astris_server_read
data_buffer[] = %02X %02X %02X
DEBUG
mismatch detected
INVCHIP
connected
astris_command
...      ace offset: 0x%08x
New firmware version: %X%02X.%02X.%02X.%u (0x%08X)
Ignoring bad result code from SFWs.
Creating STM Flasher\n
JTAG
Unable to connect to %s - %s
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
%02X %02X %02X %02X
param.booster_bundle==NULL
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
SCAN
Unknown Port micro variant?
Available alternate signature is too short for RSA-3072 flashing.  Aborting
Retries Enabled: %s
vector
CPU is halted
ASTRIS_ERR_TGTSTATE
JTAG level control
cleanup
%X%02X.%02X.%02X.%u
AppleHCPM
Not Applicable
Verify found mismatched data
SoC
PROBED_USB_RSP_NODEVICE
MISMATCH
execCmd - hcpmInfo dict: %@
PreventUserIdleSystemSleep
SWDFlashRead
ACQ_SETUP
RESPONSE_PAYLOAD
Hash matches production key
%02u:%02u:%02u.%06u|%s <%s> %s
{%s:%s@%d} Critical error [radar already requested]
PoodleSWD
header_ace->aceID = 0x%X, bootConfigSize = 0x%X
3679.40.30b172
APCIE_REGS
AUSB_REGS
Attitude
defaults.board.not_connected
operation still in progress
more than one when unique required
TPS65983
Aborting silently as this would re-install the same firmware as is already running
firmwareVersionBuffer:          0x%02X %02X %02X %02X
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
protocol version is too old
PongoSWD
{%s@%d} Received %d bytes when requested %d bytes.
TCP send
generic probed USB error
access to target is blocked
device
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
TRST
FW
getDeviceInfoNameWithConfigOnly returned: %s
Client already present in dictionary %x
Matched via Bundle ID\n
BananaSplit
HIDBridgeSWD
{%s@%d} Probe response payload read when no payload indicated.
Failed to connect to AppleAstrisGpioProbe kext %x
%s failure - %s
We are in clean up\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Failed to sync prefs at end
Can't get hardware model - failed to allocate data buffer
OS build version: %s
{%s@%d} Received %d bytes when requested %d bytes.
Initializing Booster Layer\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
{%s@%d} socket connection is not available
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
We Are Matching Development Booster\n
Could not find bundle () in given array: %s\n
Exception %d Stack Trace
{%s} Thread %#llx clearing key %lu
Can't get OS build version - failed to create URL
Could Not Find Plugin For Chip Information Provided\n
Could Not Allocate Booster Location Array
=== Loaded %s Boosters ===\n
\t\t%s\n
Booster Info:\n%s
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s:%s@%d} Critical error encountered:
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
In Readflash\n
Could Not Get Bundle Out Array of Found Boosters\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
[AstrisAsync] Failed to restart Async batch\n
[CLEANUP]\n
Initialized Logging - %s
Error closing %s [%d]
{%s@%d} Probe reported connection lost [PROBEEOF].
AXconn_create failed
Creating NXP Flasher\n
With Preflash Type %d\n
Gathered Info:\n%s
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
Hardware model: %s
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
{%s:%s@%d} Critical error [radar already requested]
invalid aod-type
AXconn_connect_kext failure - %s
Required Key-Value is a string, and not an array. Old booster found: %s\n
Initializing (%s) Booster's Astris API\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
In Writeflash\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
HOSTID=0x%x which is invalid, skipping orientation check
!*!*!* Lightning header facing up.                                                    !*!*!*
KIS translator version : %d\n
{%s[select]} %d(%s) [RETRYING]
{%s} drain_packets=%d [%s]
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
missing property aod-type
Could Not Allocate Loaded Booster Array
Invalid Bundle: %s
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s} DAP command nwords=%d trimmed to %lu\n
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
relay_get: %s = ERR
Both debug and xbs versions are set, maybe a bug: %s
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
outstanding=%zu
Can't get hardware model - failed to allocate data string
checking if relay \"%s\" is valid
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s@%d} Unknown CS code [%u]
Missing property aagp-name
Invalid SoC Booster. SoC Booster Requires PID\n
{%s}#%02X %s [%s]
{%s@%d} Found cached response
We are done with clean up\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
   {%s} (DP): status=0x%X(%s) - %s\n
Can't get OS build version - failed to open ReadStream
unable to create connection
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
{%s@%d} Drain empty on decr [%s].
{%s} %s: |%s|
In Eraseflash\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
process (%s) (%d) path: %s
Using 10pin connector skipping orientation check
{%s@%d} Received %d bytes when requested %d bytes [%s].
{%s@%d} Failed to send probe command (error %d).
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Could Not Get BoosterManager\n
Could Not Find Any Boosters\n
Failed to sync prefs at beginning
connection created
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
User created bundle found, ignoring version checking via plist
No version information found in booster: %s
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[AstrisAsync] Discarding response due to ASYNCSKIP state!
## dpw 0x%02X failed (%s)\n
Can't get hardware model - failed to create string
Can't get OS build version - failed to create plist
Can't get OS build version - failed to allocate buffer
Client already present in dictionary %x
%s: failed to create dictionary
In Postflash\n
Gathered:\n
## dpw 0x%02X 0x%08X\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
Previously dumped the process tree, skipping
{%s@%d} IOServiceClose failed, err = 0x%08x
preflash routine returned error
Could Not Allocate All Boosters Array
!!!! FILE RADAR: Don't know how to compare two values\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
kext connect name %s\n
!*!*!* ****************************************************************************** !*!*!*
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
%s: Didn't find client in dictionary
Booster Value is Not String\n
[AstrisAsync] Got ASYNC_RESTART response!
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
Could Not Find Any Loaded Boosters of Type: %s\n
Could Not Create Dictionary From Booster: %s
Failed to convert CFString to C String.
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Can't get hardware model - failed to convert to C string
relay_get: %s = %d
{%s} %s: |%s|-|%s|
Didnt match any service/parent for AppleAstrisGpioProbe
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
Dumping Process Tree
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s} select success without file descriptor set
%s\n
XBS Version Modified: %s -> %s\n
Booster:\n
Could Not Allocate Info Keys Array
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Can't get hardware model - failed to find matching IOService
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
Creating Cypress Flasher\n
\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Can't get OS build version - failed to create ReadStream
relay_get: %s = CMD_ERR (%s)
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
In Preflash\n
Did Not Find Any Boosters For: %s \n
Matched via Bundle ID\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
{%s@%d} Timeout while sending probe command.
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
%s: chip was NULL when attempting to release soc
Could Not Match A Booster for %s\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Astris Version Set: %s
Connected to Probe Device Server [Default Log]
Connected to Probe Device Server [Log File %s]
{%s} probe device server closed the connection while trying to read data (at recv)
{%s@%d} neither socket nor kext connection available
{%s}#%02X cmd: %s, resp: %s
Should be run as root (uid = %d)
Could Not Get BoosterManagerUtility\n
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
[%s] Booster System Is Not Initialized\n
Matched Booster: %s\n
Could Not Find Booster Entry Function: %s\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Required Key-Value is a string, and not an array. Old booster found\n
Can't get hardware model - failed to get property
{%s} flags:0x%08x
%s given a NULL conn object
{%s@%d} Failed to find cached response
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s@%d} Unknown CS command error [%d]
\t%s (%s)\n
%s
Value Types Are Not Strings\n
collect_responses
Unable to register assert upcall %s (Insufficient memory)
Created Connection - : %s
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s[select]} timeout while waiting for data from the connection
Astris Source Version: %s\n
Creating ADI Flasher\n
=== Found %s Boosters ===\n
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s[recv]} %d(%s) [RETRYING]
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
=== Detailed %s Boosters ===\n
Adding new booster path: %s\n
Could Not Allocate Mutable Dictionary For BoosterMangers
Gathered Value is Not Number\n
Replacing key with value
Can't get OS build version - failed to get build version
{%s} already connected
Creating STM Flasher\n
Creating Nordic Flasher\n
For production parts make sure you have allow_swd_updates=1 set in your boot-args
Could Not Find Any Boosters of Type: %s\n
Values Not The Type We Expected. Expected: Number and String\n
batch_cmd_count: %d
Unable to create pthread key for conenction. errno=%d %s.
Kick has been requested by probe server
Creating Flasher For An Unknown AOD Type: %d\n
Connection is NULL, might not have found something to connect to.\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
{%s} %s
{%s} error %d(%s) reading data from the connection (at recv)
```
