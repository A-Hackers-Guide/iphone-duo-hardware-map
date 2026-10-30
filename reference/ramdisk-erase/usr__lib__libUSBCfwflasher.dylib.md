# `/usr/lib/libUSBCfwflasher.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 463,728 bytes.

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
no error
    aceTotalBinaryCRC:  %08x
    signatureLength: 0x%08lx
E
ASTRIS_ERR_IFSTATE
ASTRIS_ERR_RESETTING
Invalid Ace Image ((ace_length 0x%X + ace_offset 0x%X) <= image_size 0x%zX) && (TotalFlashImageSize 0x%X <= kAceAppSize 0x%X)
incr_drain_packets
Values Not The Type We Expected. Expected: Number and String\n
ViewSWD
    swapOutROMBase:     %08x
Firmware is not within range required for useBorkedSFWWorkarounds
Either firmware didn't update or we haven't switched active partitions.
booster
KanziSWD
MODE
Silence backflashing failures
aceOffset: 0x%x
Failed to write \"MAGIC\" data or send memory modify command. status=0x%02x
customer version read was short (less than 2 bytes).  Is this the correct HW?
[%s] Booster System Is Not Initialized\n
=== Detailed %s Boosters ===\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
explore
INVALID KIS VERSION
OS build version: %s
ASTRIS_ERR_NOTSUPPORTED
ASTRIS_ERR_PROBEINUSE
FlamingoSWD
TGTSTAT
Ace not scheduled to boot from newly flashed region for some reason... NEEDS DEBUG
recheckFirmwareVersion marker: %u
USB-C_%s
Failed to hold sleep assertion
/usr/local/share/astris/boosterpack
JTAG chain not yet explored
{%s@%d} neither socket nor kext connection available
Aborting silently as this would re-install the same firmware as is already running
***** before it's able to accept a firmware update.  It *should* work when if you
Block Count at Failure
Note:  System may require a full A/C power cycle to update to the new FW.
RegionStart
Toto
useBorkedSFWWorkarounds: %s
execCmd - flashed.  result = %s
%s.%s.%s
NOTICE: Failure to backflash will be allowed to fail silently
***** The USB-C controller chip is in a bad state and needs to be reset/power cycled
newBoot_flags[0]:               0x%02X %u %u
Did Not Find Any Boosters For: %s \n
BoosterManager.CPU
not connected
Imago
Supplied Image missing signatures.
N/A
createClientList
Gathered:\n
!!!! Critical Error: batch attitude thread trying to lock - CAN'T LOCK !!!!\n
defaults.create.key.no_probe
Transaction
%s:%s
Skipped due to error in Async batch
Current firmware looks old enough to require I2C stability work-arounds (0x%08X)
Flash write returned 0x%02x
!! Unknown Error !!
...Firmware didn't update to expected version.  This was likely an attempt to backflash secured firmware.  Succeeding anyway
IODeviceTree:/options
Failed to write
socnames
Exception %d Stack Trace
NOTICE: Port micro reset disabled.  Must reset port micro manually after flash attempt'
Note:  Backflashing disabled via input parameters.  FW v%.8x <= FW v%.8x
execCmd - queried.  error = %s
socs_supported
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
Error closing %s [%d]
Firmware does not appear to match hardware.  Aborting (0x%X vs. 0x%X)
\n
Standard level
HTTP transaction failed
(%s) %s
invalid parameter
HTTP transaction running in background
ASTRIS_ERR_ASYNC_BARRIER
probe on host %s
INIT
We Are Matching Development Booster\n
Could Not Get BoosterManager\n
KongSWD
SPIXACT
version string INVALID
Backflashing allowed
PlayerSWD
TCP recv
probe matching %s on localhost
SETTHREAD
** Firmware is not newer, but CustomerVersion is - 0x%08X.%d vs. 0x%08X.%d
FAILURE
Held sleep assertion
SWDFlasher
BoosterManager.SOC
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
This error may be recoverable.  Allowing retries
SOC
m_core_api_serial_queue
Failed to read boot flags. status=0x%02X
missing property aod-type
Creating Nordic Flasher\n
[CLEANUP]\n
UNKNOWN_DAPSTAT
PersiesSWD
SFWi response: 0x%02x %02x %02x
Previous Error
app1Version
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
%s %s
ParrotSWD
{%s@%d} Drain empty on decr [%s].
    swapInROMLength:    %08x
Error data: %@
AppleHIDTransportInterface
Firmware Path
Failed To Init Booster's Astris API In: %s with %s (%d)\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
FAULT
normal
Error executing xfer / SFWd command @ offset 0x%x
Did NOT find service(s) matching AppleHPMDevice(index:%d)
Creating Cypress Flasher\n
ERROR
%s_probe
XPROG
BLK
 
FW
Attempting to un-bork firmware... status = 0x%X
Verify found mismatched data
Hardware model: %s
unable to create connection
BoosterManager
probed
ASTRIS_ERR_PROBED
PROBED_USB_RSP_ERROR
JTAGAP
This is an Ace firmware image
Could Not Find Booster Entry Function: %s\n
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Aborting the flash attempt.  Please follow care & feeding instructions
Ace NOT expecting more data even though we have data left to send.  ABORTING
!! Hash write error !!
SoC
ret.storePairForPref
Using 10pin connector skipping orientation check
currentFirmwareVersion: 0x%08X
required
astris_ba_free_attitude
Warning: Default logging location requested when running as root (using [%s])\n
signature %@ (Ace2)
Using useBorkedSFWWorkarounds.  Claiming keys not present
Beginning of set
ASTRIS_ERR_EMPTY
target is probably resetting
SWDFlashErase
Status/State
{%s@%d} Received %d bytes when requested %d bytes [%s].
{%s@%d} Failed to send probe command (error %d).
AXbooster_interface_cleanup_astris_api
EXPLORE
%s.%s
%02d:%02d:%02d:%06ld|%s <%s> %s
ASTRIS_ERR_TIMEOUT
Response at Failure
AXbooster_interface_create_cpu
target not in appropriate state for action
AstrisSWD
{%s@%d} Found cached response
    ... Updater not Valid!
execCmd - flashing...
Matched via Bundle ID\n
AXbooster_interface_create_swdflasher
Bug
high level connection to probe [connect state/status]
probe %s [port %u] on host %s
CPU
astris_cs_code_name
useResetZWorkarounds: %s
hid-fw-personality
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
Custom-Feature
/var/log/astrisclient
specified CPU is not available
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s} Thread %#llx clearing key %lu
probe refused to process the command
PROBED_USB_RSP_TIMEOUT
Could Not Allocate Memory
XSTAT
newFirmwareVersion: 0x%08X
%02X %02X %02X %02X
Failed to convert CFString to C String.
MISMATCH
Failed to read firmware version. status=0x%02x
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
%s: chip was NULL when attempting to release soc
This firmware image appears to be for a different ROM image variant of Ace (%X vs. %X), but additional header(s) found.  Trying next header.
AppleHPMDevice
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
AXbooster_interface_init_astris_api
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
AXconn_showname
{%s} error %d(%s) reading data from the connection (at recv)
EPIWRITE
Existing firmware version: %X%02X.%02X.%02X.%u
Ace expecting more data even though all data has been written.  ABORTING
no MEMAP access
ASTRIS_ERR_PENDING
DIAGS
Port micro not able to idle.
new offset: 0x%02X, firmware_bytes_remaining: 0x%02X
DEBUG_AUTH_REGS
Component is not present
PAYLOAD_OVERFLOW
Creating ADI Flasher\n
DEBUG
INVPARM
probe %s on host %s
HIDBridgeSWD
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
Failed to write \"RESETZ\" data. status=0x%02x
execCmd - prepping for flash
Crash level
UNKNOWN_CS_CODE
probe %s on localhost
Boot flags (before mask)=0x%04X, (after mask)=0x%04X
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp
  Error path [%s]\n
RESPONSE_PAYLOAD_DONE
TARGETSEL
RID
Error: Failed to connect (0x%08x)
Kick has been requested by probe server
    appConfigOffset:    %08x
Not a secure update.  No need for useBorkedSFWWorkarounds
New region booted: %s
probe %s [port %u] on localhost
reset_connect_state
{%s@%d} Received %d bytes when requested %d bytes.
Efficient-Core
defaults.board.not_connected
ASTRIS_ERR_MASKERR
deviceType=0x%04X
Bad Sequence Number %u (0x%X), expected %u (0x%X)
JTAG
ASTRIS_ERR_USB_EXPIRED
alt signatureLength: 0x%08lx
*** NOTICE: Power cycle unit immediately to prevent risk of unexpected behavior ***
probe on localhost
Total bytes to flash %08x
This firmware image appears to be for a different ROM image variant of Ace2.  This will probably fail. (%X vs. %X)
data_buffer[] = %02X %02X %02X
Could Not Allocate Mutable Dictionary For BoosterMangers
Error while %s:\n  %s %s
{%s} drain_packets=%d [%s]
Sending data...
Hash matches production key
STM
stdout
{%s:%s@%d} Critical error encountered:
ACQ_SAMPLE_I2C
*****
Signature write returned 0x%02x
Execution Error
Connection is NULL, might not have found something to connect to.\n
kext connect name %s\n
Invalid hostname or port specified as
Connect
probeBoardNames
%04X:
Begin
isAce1 = YES
end marker
No more devices
generic error injected by probed
%s_%s
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
read_via_sock
activeRegion
ProductBuildVersion
command timed out
ASTRIS_ERR_NOBOARDINFO
no DP (Debug Port)
invalid command
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
Failed to read customer version. status=0x%02x
IECSInterface::createUserClient...
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
BYPASSCH
appConfigVersion:               0x%04X
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
Can't get hardware model - failed to allocate data buffer
!*!*!* Lightning header facing up.                                                    !*!*!*
Firmware header:
ace_length %08x, aceTotal %08x, TotalFlashImageSize %08x, nextImageOffset %08x  (Ace2)
Failed to send warm-reset command. status=0x%02x
Expected firmware version: %02X%01X.%01X%02X.%02X.%u
ASTRIS_ERR_OK
Created Connection - : %s
Firmware appears to be within the range known to have a broken update path.  Attempting to fix
BoosterManager.Utility
NOP
Bad app image size %x
!! Overlay was present !!
User
ASTRIS_ERR_USB_NOTOPEN
PROBED_USB_REQ_TIMEOUT
AXconn_create
param.booster_handle==NULL
Can't get OS build version - failed to create ReadStream
user
ASTRIS_ERR_STOPCLOCK
%s_%d
ONEWIRE
...Retrying...
Could Not Create Dictionary From Booster: %s
protocol version is too old
SLEEPCTL
=== Loaded %s Boosters ===\n
UNKNOWN_CODE
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
Error transferring the payload, bytes remaining: %d
class_var.m_interface_name==NULL
general-purpose failure
!! ENGR over PROD !!
/swdflashers
PMGR_CTI_MUX_REGS
{%s} couldn't set thread specific - %s\n
Timeout occurred while connecting to
Memory modify failed and out of retries.  Aborting as retries were exhausted
UUID
performFlash
Could Not Get Bundle Out Array of Found Boosters\n
Can't get OS build version - failed to create plist
lldb
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
Memory Access Port
%s
astris_explore_enabler_init
[AstrisAsync] Failed to restart Async batch\n
\n!!!!!!!!!! Error: %d (%s) opening log file %s !!!!!!!!!!\n
ASTRIS_ERR_PROBEERROR
USB connection not currently open
Koko
{%s} %s: |%s|-|%s|
Successfully updated to %s%x.%x.%x
We are done with clean up\n
_log_setup_thread_specific
RESPONSE_CMD
OPEN
Port micro not in correct mode.
This can be a valid condition, and should be cleared by the SMC.
SFWi parameters: 0x%02x %02x %02x %02x
...    ridge offset: 0x%08x
***************
partnum
ASTRIS_ERR_BADPARAM
CSPDATA
Could Not Allocate All Boosters Array
Invalid SoC Booster. SoC Booster Requires PID\n
ASTRIS_ERR_NOTEXPLORED
{%s:%s@%d} [%s] unable to transfer command\n
read_resp_cmd_via_sock
New boot flags (before mask)=0x%04X, (after mask)=0x%04X
True
IOPropertyMatch
 %02X
astris
Unable to connect to
    aceBinarySize:      %08x
This is a firmware image for an unknown Ace variant
appConfig Version: 0x%X
Error: Zero payload length sent
!! CRC busy !!
AppleAstrisGpioProbe
ASTRIS_ERR_NOMEM
remote probe closed connection
Can't find header in firmware file
xfer_acmd_via_sock
GEN
GETSETTCK
status = 0x%X
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
Firmware does not appear to match hardware (0x%X vs. 0x%X).  Continuing anyway... likely to fail because of this
storeBoardName
ASTRIS_ERR_JTAGERROR
PROBED
ACQ_STARTSTOP
Tiny-Core
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
ASTRIS_ERR_NOAP
no USB device
PROBED_USB_REQ_ERROR
MiniSWD (USB Comm)
MEMm response: %02X %02X %02X %02X
ASTRIS_ERR_INVALCOMMAND
ASTRIS_ERR_NOPORTAL
Async barrier encountered
astris_command
Region 1
load_booster
Can't get OS build version - failed to get build version
port_%d
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
ASC_TCORE_ROM
astris_command_lock
ASTRIS_ERR_WAIT
firmware version is too old DEPRECATED
Already connected to
Error Message
activeFWVersion
Client already present in dictionary %x
init_astris_api
Raw level
ASTRIS_ERR_NODP
no SOC object available
%02X 
Writing version %@ to disk at %@ (2)
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
more than one when unique required
LOSTCONN
Connected to Probe Device Server [Default Log]
FACTSERNO
Unknown Port micro variant?
Existing firmware version: %02X%01X.%01X%02X.%02X.%u
Signature index %04u / %04u
Released sleep assertion
Both debug and xbs versions are set, maybe a bug: %s
APCIE_ANS1
astris_command_base
Required Key-Value is a string, and not an array. Old booster found\n
Standard
ASTRIS_ERR_DISASM
Did NOT build matching dict(index:%d)
/socs
DOCK-CH-DATA
Warn
PROBED_ERROR
firmwareVersionBuffer[3] = %02X
False
Probe
dbgarch
OCLA_IP_REGS
environment variable not found
ASTRIS_ERR_TOOMANY
ASTRIS_ERR_NOTOPEN
connection created
KIS translator version : %d\n
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s}#%02X cmd: %s, resp: %s
Modifying memory...
%s.console.%s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
ACQ_SETUP
Port micro in mode '%c%c%c%c'
IOClass
%s/%s
CPU is not halted
TLR
newCustomerVersion:             0x%04X
With Preflash Type %d\n
Warning
ASTRIS_ERR_USB_EMPTY
{%s}#%02X %s [%s]
DPAP
Attempting to force RESETZ...
Failed to initialize Astris
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
ASTRIS_ERR_CPUHALTED
ASTRIS_ERR_IGNORED
relay_get: %s = CMD_ERR (%s)
{%s@%d} Timeout while sending probe command.
PERSEIS
Likely it means you will need to either manually cold boot
%s: failed to create dictionary
defaults.create.key.outofmem
generic probed USB error
Ace got a signature verify request when no keys were programmed?
Note:  Skipping flash
%02X%01X.%01X%02X.%02X.%u
connect
2.34.0
Offset: %08x
 next Header Offset: 0x%08x
Failed to erase
Can't get OS build version - failed to open ReadStream
!*!*!* ****************************************************************************** !*!*!*
Pause to allow any existing connection to stabilize
Could Not Allocate Info Keys Array
Gathered Value is Not Number\n
Debug-Components
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
Target was lost while connecting to
New firmware version: %02X%01X.%01X%02X.%02X.%u (0x%08X)
AppleHCPM
...Unable to create Device Interface. err = 0x%X
IECS command '%c%c%c%c' still outstanding
Failed to read
UserCreated
interface not in appropriate state for action
**!** DeviceID for USB-C port controller not recognized: 0x%02X
target power is OFF
Error with SFWv command
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (after to IOCreatePlugInInterfaceForService or at exit)
abort
ASTRIS_ERR_NOTCONN
probe matching %s on host %s
Firmware Data
** Firmware is newer (yay!)
SFWd response: 0x%02x %02x %02x
SFWs response: %02X %02X %02X
None
/System/Library/CoreServices/SystemVersion.plist
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c
Note:  Running FW version 0x%.8x format in region %d ok.
3679.40.30b172
AXbooster_interface_create_soc
Exception
!!!!!!!!!! Please enter the following commands to set proper permissions:\n
vvvvvvvvvvvvvvvvvvvv DUMP OF HISTORY LOG vvvvvvvvvvvvvvvvvvvv
operation still in progress
astris_soc_release
FARB header not at front of file %08x %08x
isAce1 = %s
Main
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s@%d} Failed to find cached response
!! Wrong Device ID !!
execCmd - ...and done
deleteClientFromList
=== Found %s Boosters ===\n
One time initialization of oslog API failed!\n
BitboxSWD
length = %u bytes
Booster Value is Not String\n
ASTRIS_ERR_PROBEEOF
JTAG level control
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
End
SoC clocks are stopped. No MEMAPs allowed 
Did NOT build matching dict
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
!!!! FILE RADAR: Don't know how to compare two values\n
Attitude
{%s[select]} timeout while waiting for data from the connection
CoreSight
Can't get hardware model - failed to create string
Previously dumped the process tree, skipping
Unable to get version info from %s [error %s]
allow_swd_updates=1
failed super::init()
Didnt match any service/parent for AppleAstrisGpioProbe
Status
Error:  Verification failed.
Initializing Booster Layer\n
DOCK-CH-AGENT0-STATUS
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Someone is calling iescUpdater::init directly - should always use custom initializer
This is an Ace2 firmware image
Signature missing and hardware requires signing.  Aborting
AUSB_REGS
Astris
{%s[recv]} %d(%s) [RETRYING]
FPI2C
GETRELAY
Failed to send signature write command. status=0x%02x
Invalid Ace Image (ace_offset 0x%X >= image_size 0x%zX)
    firmwareVersion: 0x%08x
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
ERR
ASTRIS_ERR_INVAL
astris_command_complete_cache
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
!! Production key was present !!
Failed to send cold-reset command. status=0x%02x
status: %u
Error
remote EEPROM not found
general error reported by probe
PROBED_ASYNCSKIP
CHIPCNT
!!!!!!!!!!   $ sudo chmod 0775 %s\n
{%s@%d} Probe response payload read when no payload indicated.
SRSTM
MAP_CMD
cleanup
/usr/standalone/firmware
development
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
astris_dpwrite
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
invalid host name or port
ASTRIS_ERR_HTTP_FAILURE
ASTRIS_ERR_NOTPRESENT
Region booted: %s
preflash routine returned error
probe [port %u] on localhost
probe [port %u] on host %s
LCDCTL
JTAGPORT
PORTAL ERR PENDING
probed USB transaction timer expired
Wait indication while connecting to
{%s@%d} socket connection is not available
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
ret._release_gateway_control
Payload description INVALID
   appConfigVersion: 0x%04x
Error occurred: 0x%X
fn.missing_booster_init_api
Could Not Match A Booster for %s\n
VERSION
Warning:  Error setting Grst.
APCIE_ANS0
target no longer responding
ASTRIS_ERR_NOTFOUND
NO
KIS
Region 0
Could Not Find Any Boosters\n
ASTRIS_ERR_TGTOFF
{%s} already connected
gaidEnabled = %s
getDeviceInfoNameWithConfigOnly returned: %s
Flash start returned 0x%02x
Expected firmware version: %X%02X.%02X.%02X.%u
PMGR_OCLA_REGS
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
ASTRIS_ERR_MISSINGPARAM
TCP send
***** NOTE: PurpleRestore will fail now, as this is going to drop the USB link.
Using older sigatures.  Flashing only Ace component (%u bytes from 0x%X)
\t%s (%s)\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
hostid
astris_command_async
.
IDLE
FPGAINIT
ace_length %08x, aceTotal %08x, TotalFlashImageSize %08x (Ace1)
Block Count at Failure: %u
app2Version
usbc-flash-update
%s failure - %s
Gathered Info:\n%s
axlog_assert_upcall
%s (%d)
MAIN_DEBUG_ROM
ASTRIS_ERR_BADFIRMWARE
Too many open files
RTI
KIS_DOCK
typehint
Can't get hardware model - failed to find matching IOService
xfer_acmd_via_kext
Initialization Error
Could Not Find Plugin For Chip Information Provided\n
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
result.booster_api_vers==NULL
stderr
!!!!!!!!!!   $ sudo chown $USER %s\n
MINISWD
Version
Aborting as this would result in a backflash
Retrying memory modify command as it looks like it didn't execute...
Prompt
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp
cleanup_astris_api
OK
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
Error detected
{%s@%d} Unknown CS command error [%d]
APEXPLORE
IECS interface not found or you are running as a non-root user.
Path to Firmware Version
Failed to read write expected firmware version to file: %s
SFWu response: 0x%02x %02x %02x
preflash_type
GorillaSWD
{%s} %s: |%s|
Note:  Running FW is not upgradeable by this utility.  0x%.8x < 0x%.8x.
XINIT
Initializing (%s) Booster's Astris API\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp
param.conn == NULL
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
%s v%s%s [%s]
some generic JTAG hardware fault
ASTRIS_ERR_NODEVICE
ASTRIS_ERR_USB_PROBED
force
    aceDeviceID:        %08x
Hash matches engineering key
ASC_ECORE_ROM
Error %d (%s) while expanding ~ for Astris log file base\n
ASTRIS_ERR_BADPROTOCOL
Access Port
MAX_KISSWD
unable to transfer command to/from remote probe
    aceBinaryCRC:       %08x
ASTRIS v%s%s [%s]
Unique required when more than one probe identified by
REG
!
Creating STM Flasher\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
access to target is blocked
INVMODE
%s-%06X
Failed to send flash verify command. status=0x%02x
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Can't get OS build version - failed to create URL
ASTRIS_ERR_BADENV
ASTRIS_ERR_PROBECOMMAND
mismatch detected
checking if relay \"%s\" is valid
ACQ_SAMPLE_SPI
Hash matches UID key
Ignoring bad result code from SFWs.
Invalid Bundle: %s
Could not find bundle () in given array: %s\n
ASTRIS_ERR_VARNOTFOUND
Invalid condition while connecting to
Unable to process command while connecting to
    nextImageOffset:    %08x
This firmware image appears to be for a different ROM image variant of Ace2.  Aborting. (%X vs. %X)
execCmd - failed to release power assertion: 0x%X
Value Types Are Not Strings\n
ASTRIS_ERR_OUTOFMEMORY
ASTRIS_ERR_ASYNCSKIP
%s-%06d
Firmware appears to be below minimum requirement to flash J327.  Attempting to fix
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
execCmd - hcpmInfo dict: %@
ASYNC
MEMAP
NOTICE: Retries disabled as per request
getAceHeaderOffset failed
%X%02X.%02X.%02X.%u
Error initializing flash mode
soc-pid
firmwareVersionBuffer[2] = %02X
Failed to sync prefs at beginning
Bug detected
/
empty USB packet encountered
firmwareVersionBuffer[1] = %02X
Flash verify returned %02x
astris_remove_loaded_cpu_boosters
process (%s) (%d) path: %s
Mask condition met in conditional operation
    aceFWVersion:       %08x
Available signature is too short for RSA-2048 flashing.  Aborting
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
INFO
PoodleSWD
Invalid Ace Image (currHeaderOffset 0x%X >= image_size 0x%zX)
    DeviceConfigPtr:    %08x
Failed to start flash. status=0x%02x
%s: Didn't find client in dictionary
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
DEBUG CLOCK OFF
TRST
isFactory
Note:  FW version is not same or newer (running v%.8x, thisVersion v%.8x
JTAG IN CONTROL
%s.console
SETCLR
HCPM detected, deviceType=0x%04X
Attempting to reset port micro to load new firmware
IDE ACCESS OUT OF BOUNDS
a
ARM7
Failed to send command. status=0x%02x
This appears to be running on unrecognized port micro hardware.  This will probably fail
CPU is halted
anomaly detected
CPU disabled by SW, not accessable
firmwareVersionBuffer:          0x%02X %02X %02X %02X
aagp-name
Should be run as root (uid = %d)
No version information found in booster: %s
{%s:%s@%d} [%s] unable to drain response\n
*deviceID: 0x08%X
***** restart or begin another restore attempt
fn.missing_entry_function
assert
Dumping Process Tree
bad parameter(s) specified
ASTRIS_ERR_NODATA
LMFLASH
[CMD] %02u:%02u:%02u:%06u|%s <%s> %s\n
required parameter is missing
No MEMAP access while connecting to
KICKINFO
execCmd - setting firmware location: %s
Booster:\n
TIMEOUT
MASK ERROR
ASTRIS_ERR_FDSETOVERFLOW
New region booted unable to be reported: Unrecognized silicon!
A
framework
   {%s} (DP): status=0x%X(%s) - %s\n
model
PROBED_USB_RSP_NODEVICE
AXconn_connect_kext
HOSTID=0x%x which is invalid, skipping orientation check
the new firmware image running
Should be ready to proceed with SFWi
  TotalFlashImageSize: 0x%08X
ASTRIS_ERR_ISCONN
Communication error occurred while connecting to
SCAN
header_ace->aceID = 0x%X, bootConfigSize = 0x%X
Firmware Offset
i
!! Engineering key was present !!
Port micro not in correct mode (yet).
IOService
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
%s/Library/Logs/Astris
Should think SFWu now usable
basic_string
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
ASTRIS_ERR_FAILURE
Portal Status has an error
Sprocket
{%s[select]} %d(%s) [RETRYING]
Error data:
SETRELAY
User created bundle found, ignoring version checking via plist
(0x%08llX) %s
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Note:  Flashing v%.8x over v%.8x in target region %d
...Unable to find parent for IECS service.  err = 0x%X
Could Not Get BoosterManagerUtility\n
PROBED_SLEEPING
...      ace offset: 0x%08x
Writing version %@ to disk at %@ (1)
AXconn_create failed
Apple
connection to probe is lost
WARNING
ASTRIS_ERR_ANOMALY
INVCHIP
Successfully connected to
ace_firmware_length: 0x%08x
!! Hash doesn't match any key !!
...Either firmware didn't update or we haven't switched active partitions. Retrying...
Error: Failed to erase (0x%08x)
PROBED_LOSTCONN
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
status
End of set
alloc_drain_payload
Name
Region 0x%02x%02x
execCmd - flashed.  error = %s
In Eraseflash\n
exit
no data when data expected
CPU-level (general and architecture-specific)
Failed to stat file (1): %s %s
execCmd - failed to hold power assertion: 0x%X
In Readflash\n
IOPlatformExpertDevice
connection not currently open
AstrisArmProbeServer-3679.40.30~172 (RavePopB tools)
Tarsier
MEMAP_APB
Using modern sigatures.  Flashing combined components (%u bytes from 0x%X)
toggle-reset-enabled
Required Key-Value is a string, and not an array. Old booster found: %s\n
Can't get hardware model - failed to convert to C string
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
SCANDEBUG
Index: %u
usbc-fw-personality
%s%s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
-Lite
ASTRIS_ERR_NOCPU
SWDONLY
PROBED_USB_INUSE
{%s} flags:0x%08x
Zero payload length sent
This error is not recoverable.  Exiting
Error: Failed to write (0x%08x)
ASTRIS_ERR_SLEEPING
    swapInROMBase:      %08x
NOTICE: Forcing install regardless of chipID (likely enforced by hardware anyway)
You appear to be running a firmware version that cannot be updated from DFU mode.
Flash verify success.
soc-name
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
no device when sending request
Booster Info:\n%s
Can't get hardware model - failed to allocate data string
SPI
ace_firmware_offset: 0x%08x
NOTE: The dead battery flag appears to be set
Region booted: Unrecognized silicon!
Flashing error encountered
customer version read was short (less than 2 bytes).  Is this possibly Ace1?
SLEEPING
RELAY
sendGAID marker
Warning level
Low level
queryInfo
b
probe
isAce2 = YES
  Decoding error responses...
DP
%02u:%02u:%02u:%06u|%s <%s> %s\n
host is going to sleep
relay_get: %s = %d
{%s} probe device server closed the connection while trying to read data (at recv)
!! CRC Failure !!
boot_flags.rawBytes[0]:         0x%02X %u %u
Error: Failed to connect (0x%08x). Please confirm boot-arg \"allow_swd_updates=1\" is set.
%d
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
We are in clean up\n
Matched Booster: %s\n
BoosterManager.SWDFlash
Can't get hardware model - failed to get property
Error while trying to disassemble memory
EmulatorSWD
ENUM
No probes were found matching
SUCCESS
Note:  Setting Grst for reset on SSPS(6).
DAP
ASTRIS_ERR_LOSTCONN
Error while %s:\n  Unable to connect to %s - %s
.bin
execCmd - input dict: %@
param.booster_bundle==NULL
timeout or watchdog expired
ASTRIS_ERR_PORTAL_STATUS
{%s} Batch attitude key created for %p thread %#llx key %lu
failed init() with device detection failure: %@
invalid aod-type
Temporary level
too many of something
DISCONNECT
    bootConfigSize:     %08x
expectedFirmwareVersionBuffer:  0x%02X %02X %02X %02X
Error sending signature
Connected to Probe Device Server [Log File %s]
ret._cleanup_hw
SWDFlashWrite
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
Current firmware version: 0x%08X
teardown marker
                Status: %u
Error: Failed to read (0x%08x)
Failed to release sleep assertion
UNKNOWN
cpus
PORTAL UNAVAILABLE
Flash start failed as region is invalid
Bad Sequence Number %u (0x%X), expected %x (0x%X)
Ace believes it got all required data
XBSRelease
remote probe is currently in use
invalid environment variable
Creating NXP Flasher\n
    aceID:              %08x
vector
Could Not Allocate Loaded Booster Array
AXLOG
ASTRIS_ERR_NOSOC
connected
RESPONSE_PAYLOAD
Retries Enabled: %s
%s\n
User interaction
decr_drain_packets
Firmware appears to correctly match the target hardware. (0x%X)
PROBED_USB_NOTOPEN
{%s@%d} Unknown CS code [%u]
implementer
default
Astris default logging context
UNKNOWN CODE
%s given a NULL conn object
...checking firmware update ability.  (See <rdar://problem/42441690>)
YES
J327
Adding new booster path: %s\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
[AstrisAsync] Got ASYNC_RESTART response!
ASTRIS_ERR_USB_NODEVICE
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
Missing property aagp-name
Could Not Find Any Loaded Boosters of Type: %s\n
com.apple.astris
RESPONSE_NO_PAYLOAD
CLOSE
PongoSWD
New firmware version: %X%02X.%02X.%02X.%u (0x%08X)
boot-args
no board info file loaded
IRSCAN
Flashing index %04u / %04u
SWDFlashRead
Std
Debug Port
Another application is connected to
TPS65983
Ace/Ace2 found.
Port micro successfully restarted after flash
batch_cmd_count: %d
NRF
{%s@%d} IOServiceOpen failed, err = 0x%08x
KobaSWD
preflash-type
astris_remove_loaded_soc_boosters
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ASTRIS_ERR_EXPIRED
ASTRIS_ERR_PROBETIMEOUT
{%s:%s@%d} [%s] unable to read command response\n
newFWVersionBuffer:             0x%02X %02X %02X %02X
SWDFlash
Could Not Find The Entry Function: %s
AP
already connected
No portal under found for that type
You appear to be running a no longer supported version of Ace1 hardware.  Aborting. (%X)
  ...moreDataExpected: %s
%02u:%02u:%02u.%06u|%s <%s> %s
ASTRIS_ERR_BADHOST
ASTRIS_ERR_TGTLOST
hardware error reported by probe
You appear to be running a no longer supported version of Ace1 hardware.  This is almost certainly going to fail. (%X)
!! Needs SFWd !!
USB-C_FW
Astris Source Version: %s\n
NOTEXPLORED
  ...responseCode: %u - %s
Arm
Unable to connect to %s - %s
{%s:%s@%d} [%s] failed preconnect\n
           deviceID: 0x%08x
EICE
BananaSplit
Flashing failure detected...
Unable to check freshly installed firmware version as port micro has not been reset
Error Code
GitHashDebug
\t\t%s\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
empty request encountered
astris_server_read
** Current firmware is an engineering build. Ignoring firmware version check - 0x%08X.%d vs. 0x%08X.%d
HostInfo
ASTRIS_ERR_NOTUNIQUE
ChimpSWD
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
Note:  Running FW version in region %d is not formatted correctly (0x%.8x), indicating very old FW that cannot be updated.
ret.createKey
Ace believes it got all required signature data
AXconn_connect_kext failure - %s
ASTRIS_ERR_CPUNOTHALTED
operation not supported
read_resp_payload_via_sock
Could Not Find Any Boosters of Type: %s\n
Could Not Find The Astris Init Function (%s) in %s
rpc
SimulatorSWD
...checking firmware update ability...
Error: [0x%08X] Mismatch expected: 0x%02x received: 0x%02x
Failed to connect to AppleAstrisGpioProbe kext %x
AMCNP_GFX
%s %s:l=%u,c=0x%X,i=0x%X,f=0x%X
/cpus
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
time out reported by probe
{%s} select success without file descriptor set
ARMDAP
Failed to write \"RESETZ\" data or send memory modify command. status=0x%02x
Warning:  Error resetting PRGN after flashing.
%s%x.%x.%x
WRBUF
Output
{%s} %s
postconnect
Available signature is too short for RSA-3072 flashing.  Aborting
AppleSPUControl
PreventUserIdleSystemSleep
com.apple.usbcfwflasher.SleepAssertionID
In Postflash\n
   Response at Failure: 0x%02X
In Writeflash\n
unknown
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
Master BoosterManager
HWERR
Unable to create pthread key for conenction. errno=%d %s.
SWDRESET
Command set required to update this HW is not available.  Update process is forced to abort.
     New firmware version: %02X%01X.%01X%02X.%02X.%u
Error level
TOOMANY
...Unable to create CFPlugInInterface. err = 0x%X
Did not create enumerator
complexes
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s} DAP command nwords=%d trimmed to %lu\n
preconnect
Attempting update to RID %@...
SWDFlasher.API
RegionEnd
JTAGONLY
    swapOutROMLength:   %08x
SWD_BYPASS_REGS
Replacing key with value
PROBED_USB_REQ_EMPTY
{%s:%s@%d} [%s] unable to read response payload\n
options
firmwareVersionBuffer[0] = %02X
{%s:%s@%d} Critical error [radar already requested]
file/object not found
read_resp_via_sock
NOTICE: Backflashing attempts are allowed
failed init() for flashUpdater instance
aod-type
Failed to sync prefs at end
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
ace_offset: 0x%X, header_ace->appConfigOffset: 0x%X
Error:  Flashed Version is unexpected version
EPIREAD
device
Flashing signature 0x%x bytes (%u blocks)
BoosterPublicAPI
param.conn.user_defaults == NULL
Can't get OS build version - failed to allocate buffer
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
** Firmware is NOT newer - 0x%08X.%d vs. 0x%08X.%d
Hash match value unknown: 0x%02X
HCPM flash status: %d
aod_type
DOCK-CH-CONFIG
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
no AP (Access Port)
ASTRIS_ERR_TGTSTATE
InterfaceLocked
getAceHeaderOffset reporting status = 0x%X
isAce2 = %s
Not Applicable
Did NOT find service matching AppleHPMDevice
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
APCIE_REGS
XACT
!! Hash failed !!
bundle_id
ASTRIS_ERR_MISMATCH
%s/%@%s
!! Version check failed !!
IECS createUserClient - status = 0x%X, self.service = %u, _deviceInterface = %p (prior to IOCreatePlugInInterfaceForService)
JTAG error while communicating with
?
astris_err_from_cs_type
BADCODE
This appears to be running on unrecognized port micro hardware.  Aborting
DBG_WRAP_REGS
Key initialization for oslog API failed! %s\n
PROBED_USB_REQ_NODEVICE
    Status: %u
Ace response code: 0x%02X
localhost
astris_user_default_set_boardname
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
     New firmware version: %X%02X.%02X.%02X.%u
Flashing 0x%x bytes (%u blocks) from 0x%08x
!! Too much data !!
~
Dock-Channels
createKey
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Exo
    aceTotalBinarySize: %08x
this unit or manually reset the port micro before you will see
## dpw 0x%02X 0x%08X\n
Input
ASTRIS_ERR_EENOTFOUND
CHAINERR
SRST
Note:  Resetting PRGN.
darts
## dpw 0x%02X failed (%s)\n
out of memory
TGTOFF
relay_get: %s = ERR
astris_command_complete
Creating Flasher For An Unknown AOD Type: %d\n
XBS Version Modified: %s -> %s\n
ADI
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
ASTRIS_ERR_DISABLED
PortBridgeSWD
  ...SFWi_status: %u - %s
Available alternate signature is too short for RSA-3072 flashing.  Aborting
Failure code: 0x%08X
In Preflash\n
ASTRIS_ERR_PROBEHWERR
ASTRIS_ERR_BLOCKED
{%s@%d} IOServiceClose failed, err = 0x%08x
New region selected for next boot of port micro.
Note:  Running FW v%.8x >= min FW v%.8x -- Can update: %s
Could Not Allocate Booster Location Array
META
For production parts make sure you have allow_swd_updates=1 set in your boot-args
NXP
Unable to register assert upcall %s (Insufficient memory)
STATUS
FWUPDATE
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
HOSTID=0x%x which is invalid, skipping orientation check
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s@%d} neither socket nor kext connection available
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
=== Loaded %s Boosters ===\n
Adding new booster path: %s\n
Could Not Match A Booster for %s\n
{%s} Thread %#llx clearing key %lu
Can't get hardware model - failed to allocate data string
Can't get OS build version - failed to create plist
Connected to Probe Device Server [Log File %s]
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
%s\n
Can't get hardware model - failed to get property
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s} drain_packets=%d [%s]
{%s@%d} Failed to send probe command (error %d).
{%s@%d} Timeout while sending probe command.
{%s@%d} Unknown CS command error [%d]
XBS Version Modified: %s -> %s\n
\n
Exception %d Stack Trace
Can't get OS build version - failed to allocate buffer
Previously dumped the process tree, skipping
{%s} select success without file descriptor set
{%s} probe device server closed the connection while trying to read data (at recv)
{%s} %s: |%s|
For production parts make sure you have allow_swd_updates=1 set in your boot-args
preflash routine returned error
Both debug and xbs versions are set, maybe a bug: %s
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
{%s@%d} Failed to find cached response
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
Didnt match any service/parent for AppleAstrisGpioProbe
Could Not Allocate All Boosters Array
Could Not Find Any Boosters of Type: %s\n
%s
Could Not Create Dictionary From Booster: %s
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
   {%s} (DP): status=0x%X(%s) - %s\n
Can't get OS build version - failed to create ReadStream
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
%s: Didn't find client in dictionary
Creating Nordic Flasher\n
missing property aod-type
Could Not Allocate Booster Location Array
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Could Not Get Bundle Out Array of Found Boosters\n
Failed to connect to AppleAstrisGpioProbe kext %x
Matched Booster: %s\n
Could Not Allocate Info Keys Array
[AstrisAsync] Discarding response due to ASYNCSKIP state!
{%s} already connected
Using 10pin connector skipping orientation check
Connected to Probe Device Server [Default Log]
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
In Readflash\n
No version information found in booster: %s
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
relay_get: %s = %d
{%s@%d} Drain empty on decr [%s].
{%s@%d} Unknown CS code [%u]
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Client already present in dictionary %x
Failed to convert CFString to C String.
Did Not Find Any Boosters For: %s \n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
Creating ADI Flasher\n
Could not find bundle () in given array: %s\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
{%s@%d} socket connection is not available
%s: chip was NULL when attempting to release soc
Required Key-Value is a string, and not an array. Old booster found: %s\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s[select]} %d(%s) [RETRYING]
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s@%d} Received %d bytes when requested %d bytes.
{%s} %s: |%s|-|%s|
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
In Postflash\n
Failed to sync prefs at end
collect_responses
{%s:%s@%d} Critical error [radar already requested]
unable to create connection
Error closing %s [%d]
relay_get: %s = CMD_ERR (%s)
{%s@%d} Found cached response
Creating STM Flasher\n
!!!! FILE RADAR: Don't know how to compare two values\n
Replacing key with value
{%s} DAP command nwords=%d trimmed to %lu\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s}#%02X %s [%s]
{%s}#%02X cmd: %s, resp: %s
Booster:\n
[AstrisAsync] Got ASYNC_RESTART response!
Can't get OS build version - failed to create URL
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
{%s[recv]} %d(%s) [RETRYING]
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
\t%s (%s)\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
Should be run as root (uid = %d)
=== Found %s Boosters ===\n
[AstrisAsync] Failed to restart Async batch\n
{%s[select]} timeout while waiting for data from the connection
In Preflash\n
%s given a NULL conn object
{%s} %s
{%s@%d} Probe response payload read when no payload indicated.
In Eraseflash\n
Could Not Allocate Loaded Booster Array
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
## dpw 0x%02X 0x%08X\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
kext connect name %s\n
relay_get: %s = ERR
Missing property aagp-name
Gathered Value is Not Number\n
OS build version: %s
checking if relay \"%s\" is valid
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
Creating Flasher For An Unknown AOD Type: %d\n
Value Types Are Not Strings\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
Can't get OS build version - failed to get build version
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Could Not Find Any Boosters\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
Unable to register assert upcall %s (Insufficient memory)
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
Could Not Find Plugin For Chip Information Provided\n
%s failure - %s
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Gathered Info:\n%s
Initializing (%s) Booster's Astris API\n
Could Not Find Booster Entry Function: %s\n
Can't get hardware model - failed to allocate data buffer
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
Could Not Get BoosterManager\n
Initializing Booster Layer\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
Can't get hardware model - failed to convert to C string
Initialized Logging - %s
{%s:%s@%d} Critical error encountered:
process (%s) (%d) path: %s
KIS translator version : %d\n
Could Not Find Any Loaded Boosters of Type: %s\n
\t\t%s\n
Required Key-Value is a string, and not an array. Old booster found\n
## dpw 0x%02X failed (%s)\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Unable to create pthread key for conenction. errno=%d %s.
{%s} Batch attitude key created for %p thread %#llx key %lu
Creating Cypress Flasher\n
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
User created bundle found, ignoring version checking via plist
Invalid Bundle: %s
Could Not Allocate Mutable Dictionary For BoosterMangers
outstanding=%zu
Can't get hardware model - failed to create string
Hardware model: %s
Invalid SoC Booster. SoC Booster Requires PID\n
Booster Value is Not String\n
batch_cmd_count: %d
Creating NXP Flasher\n
We are in clean up\n
[%s] Booster System Is Not Initialized\n
Booster Info:\n%s
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
AXconn_connect_kext failure - %s
Could Not Get BoosterManagerUtility\n
We Are Matching Development Booster\n
Matched via Bundle ID\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
Values Not The Type We Expected. Expected: Number and String\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Failed to sync prefs at beginning
Astris Source Version: %s\n
In Writeflash\n
We are done with clean up\n
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
[CLEANUP]\n
%s: failed to create dictionary
=== Detailed %s Boosters ===\n
Gathered:\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Astris Version Set: %s
Dumping Process Tree
Created Connection - : %s
{%s} flags:0x%08x
With Preflash Type %d\n
Connection is NULL, might not have found something to connect to.\n
Can't get hardware model - failed to find matching IOService
Can't get OS build version - failed to open ReadStream
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s} error %d(%s) reading data from the connection (at recv)
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s@%d} Received %d bytes when requested %d bytes [%s].
connection created
!*!*!* ****************************************************************************** !*!*!*
Kick has been requested by probe server
AXconn_create failed
invalid aod-type
flasher
IECSInterface
swdUpdater
IOKitUtilities
flashUpdater
iecsUpdater
defaultManager
length
setDeviceService:
initWithDevice:
dictionaryWithCapacity:
findSWDMatchingDeviceNode:withError:
initWithDomain:code:userInfo:
_cfPlugInInterface
flash:andErrorResponse:
retriesEnabled
whitespaceAndNewlineCharacterSet
isDone:
service
copy
objectForKey:
initWithService:
initWithFormat:
data
errorWithDomain:code:userInfo:
initWithOptions:andErrorResponse:
query:andErrorResponse:
selectUpdaterWithRID:
setData:
bytes
checkForBootArgs:
iecsAtomicCommand:data:dataLength:retData:retDataLength:flags:timeout:
addObject:
device
getHCPMinfo:
initWithInterface:
setLength:
setObject:forKeyedSubscript:
attributesOfItemAtPath:error:
currentDevice
getBytes:length:
isEqualToString:
setObject:forKey:
updaterSupported:
_deviceService
updated
verbose
description
getHCPMinfoImpl:
next:
rid
catalogSWDDevices:
fConnection
initForSimulation
objectEnumerator
createFileNameForFirmware:
enableDisableGAID:
enableDisableRetries:
rangeOfData:options:range:
unsignedLongValue
entryID
compare:
flashHCPM:andErrorResponse:
initWithService:isHCPM:
isEqualToDictionary:
numberWithUnsignedInt:
numberWithUnsignedLong:
objectAtIndexedSubscript:
countByEnumeratingWithState:objects:count:
enableDisableFirmwareUpdateMode:
name
unsignedIntValue
getDeviceInfoNameWithConfigOnly:
isHCPMversionFormat:
releasePowerAssertion:
uint64ForRegistryEntry:andKey:outValue:
_userClientActive
UTF8String
getAceHeaderOffset:ofSize:intoRidgeOffset:intoAceOffset:andLength:signature:alternateSignature:andDeviceType:andVersion:andAppConfigVersion:andNextHeaderOffset:
nextObject
stringByTrimmingCharactersInSet:
takePowerAssertion:
appendBytes:length:
fGAIDEnabled
iecsWaitForIdle:pollInterval:timeout:
attemptIECSCommand:flags:withData:dataLength:retData:retDataLength:timeout:andErrorResponse:
createUserClient
dataWithBytes:length:
fInterface
isAllowableBCDByte:
version
dealloc
destroyUserClient
dictionaryWithObject:forKey:
sharedInstance
stashFirmwareVersionInFile:
.cxx_destruct
_deviceInterface
sharedInstance:
catalogIECSDevices:
count
fUpcomingFirmwareVersionStash
iecsReadForAddress:buffer:length:flags:andOutReadLength:
initWithConnection:
locatedDevices
locatedObjects
stringWithFormat:
unsignedLongLongValue
dictionary
isRegistryEntry:descendentOfRegistryEntry:outValue:
locatedDeviceEnumerator
setLocatedObjects:
_locatedObjects
T@\"NSArray\",&,N,V_locatedObjects
TI,N,V_service
arrayForRegistryEntry:andKey:outValue:
dictionaryWithDictionary:
setService:
upcomingFirmwareVersionStash
writeToFile:atomically:encoding:error:
TI,N,V_deviceService
setValue:forKey:
uint32ForRegistryEntry:andKey:outValue:
uuid
device_id
init
gaidEnabled
reset:
stringWithUTF8String:
arrayWithCapacity:
boolValue
deviceService
setVerbose:
optkeyshash
fRetriesEnabled
_service
execCmd:withInput:andOutput:andErrorResponse:
iecsWriteForAddress:buffer:length:flags:
objectForKeyedSubscript:
B24@0:8^@16
@24@0:8^@16
@\"IECSInterface\"
@24@0:8I16B20
i16@0:8
i36@0:8I16@20^Q28
i36@0:8I16@20^@28
i32@0:8I16I20^B24
B24@0:8@\"NSString\"16
B32@0:8@\"NSMutableDictionary\"16^@24
^^{AppleHPMLibInterfaceStructV3}
i24@0:8^I16
v24@0:8^@16
@\"NSMutableDictionary\"
B20@0:8B16
B32@0:8@\"NSDictionary\"16^@24
B104@0:8r*16Q24^I32^I40^I48@56@64^I72^I80^S88^I96
B20@0:8I16
@\"NSArray\"
Q
i20@0:8I16
@\"NSEnumerator\"
@20@0:8I16
i60@0:8I16I20*24S32*36S44I48^@52
@\"NSNumber\"
i48@0:8C16^v20Q28I36^Q40
i28@0:8I16I20I24
I
@\"NSNumber\"16@0:8
B
i64@0:8I16^v20Q28^v36Q44I52Q56
v24@0:8@16
B32@0:8@16^@24
@\"NSString\"16@0:8
@20@0:8B16
B20@0:8C16
i40@0:8C16^v20Q28I36
I32@0:8[128c]16^@24
@32@0:8@16^@24
B48@0:8@16@24@32^@40
@16@0:8
@24@0:8@16
v16@0:8
@\"NSString\"
^^{IOCFPlugInInterfaceStruct}
i36@0:8I16@20^I28
@\"<flasher>\"
B24@0:8@16
I16@0:8
v20@0:8I16
B24@0:8*16
```
