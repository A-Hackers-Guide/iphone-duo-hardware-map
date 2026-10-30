# `/usr/local/share/astris/boosterpack/swdflashers/arm_stm32l15xc_swdflasher.booster/arm_stm32l15xc_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,843,728 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = BUNDLE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 2952)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, HasTLVDescriptors
```

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (7,124)

First 2,500 of 7,124.
```
Section 1 Offset: 0x%llX\n
Result while reading third entry: %s , entry val 2: 0x%X\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
KIS Chip Found, Doing KIS Explore Setup
choice: %d\n
Portal Group Offset: 0x%X Entries: %d\n
error %s checking for data abort
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
{%s} FAILURE - max length exceeded
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
!!!! Complex CPU Key %s is INVALID !!!!\n
[1500] Error parsing bridge '%s': missing required field 'tap'
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
{%s} drop ProbeName %s
\n
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
{%s->%s} (top) current_el=%d
   DPv3 baseptr is not valid (%X)\n
Failed to convert kisLoc %s to unsigned long long
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Die-Count: %d Current-Die: %d Die-Type: %d
{%s::%s} timeout while waiting for EDSCR ITE
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
Error status from AMAuthInstallSsoInitializePtr = %i
{%s} no TAP detected that supports 1500
Banana split probe, for now I guess we will just say yes...\n
{%s=>%s} null reference to AXconn_t record, `conn`
[Auth Debug] Ticket Active, Debug Interface Locked\n
Error - STM32Fxxx reflash failed (%s).\n
OS build version: %s
setCategoryValue: path='%.*s'
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Variables not setup
Invalid Bundle: %s
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
Probe %s removed before port determined\n
SoC BM Not Found, Bailing\n
Turning Debug Clock On
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
[1500] TAP key is not a valid integer
[INSBP] bp%d addr=%08llx fpr=%08X\n
Error status from AMAuthInstallSsoEnablePtr = %i
Production Fused Device\n
STM32Hxxx flash programming status fault: 0x%08X\n
{%s} match any probe [localhost]
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Probe %s removed during selection process
relay_set: %s -> %d
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Flash Size 0x%X KB\n
Couldnt figure out the size of flash, defaulting to 1MB\n
Hang Description:\n%s\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
Could Not Find a DCM Portal
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s} Debug Base: %08X
Gateway is KIS, seeing what probe this is\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
Probe %s Device Server listening on port %d
CPU (%s) has explore flag of: 0x%llx which is not set\n
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
Stepping Stone Final =  %#x\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
[AstrisAsync] replay preflight: Async not active!\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
   {%s} Probe requires overrun detect mode.\n
   {%s} (DP): status=0x%X(%s) - %s\n
[1500] Detected plist version %d
Early dbgwrap base extracted: 0x%llx\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
{%s=>%s} no soc reference; falling back to direct cpu method
   Debug base is in legacy format\n
\tWriting 0x%X bytes @ 0x%08llX...\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
[REMWP] wp%d\n
ERROR!! Wrote %zd bytes, expected %zd\n
%s given a NULL conn object
{%s@%d} Connection to server rejected, error=%d (%s)
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
{%s@%d} Failed to send probe command (error %d).
TargetSel Before Disable: 0x%x
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
     0x%016llx: 0x%04x      %s\n
Disconnected from Probe Map Server
Not Creating CPU: %s\n
[1500] run_steps: unknown instruction '%s'
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
Chip %x Status = %d\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
Xtensa Option reg_file_size: %d
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
Probe Map name of probe %d is: %s
{%s@%d} Probe response payload read when no payload indicated.
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Error %d(%s) executing instruction 0x%08X FAST
[AstrisAsync] Async mode %s
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
\t[MATCH_TARGETID] FAIL <= unable to find DP
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} Error reading PID (%s)
We are Deallocating\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
Invalid APTABLE (%d), so using most restrictive
[AsyncSnapshot] No snapshots collected\n
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Failed AP read of R_MEMAP_CSW res: %i
Probe Map comm error %d(%s) %s
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
coalesced-target: %s\n
     0x%016llx: 0x%08x    %s\n
[AstrisAsync] Got ASYNC_RESTART response!
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s} empty response string provided
End of Operation Bit Is Set - %s
CPU DBG Ack: 0x%llx\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
   {%s} Before powerup CMDSTAT=%08X\n
start rev and/or end rev is NULL; skipping cpu_desc override\n
error %s reading DAP MPIDR
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
Unable to read LR
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
Proceeding with full explore instead of instantiation
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} Unrecognized component: %08X, class %02X\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
JsonLogger: Loading schema for category '%.*s' from '%s'
X00 Part
\tWriting @ 0x%08llX...\n
=== Ending Gather and Clear ===
AXconn_t Struct Is NULL
Booster:\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
{%s} Failed to extract component info from table (%d); continuing anyway
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
HOSTID=0x%x which is invalid, skipping orientation check
error trying to unlock MSR %s
outstanding=%zu
{%s} Unrecognized Component: %08X (class %u)
Error - STM32%s reflash failed (%s).\n
Connected toProbe Map Server (single_port) 
{%s@%d} Timeout while sending probe command.
JsonLogger: Wrote %zu bytes to '%s'
{%s} Error %d(%s) sending message
Using Built In SoCs\n
Sending DYN Bypas Channel Set: %d
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
[1500] Error parsing v2 bridges
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
{%s@%d} Drain empty on decr [%s].
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Failed to get PMU Name
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
Optional Key: SubsystemMonitor not in preferences
Write Protection Error is Set\n
error %s checking for data abort(first)
Can't get OS build version - failed to allocate buffer
CPU ASC Offset: %d\n
Failed to get KIS translator version\n
There is no system bus access port on the debug port
%s\n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Board ID: 0x%X\n
   DPv3 bus is %u bits wide\n
{%s} DAP command nwords=%d trimmed to %lu\n
Complex Address: 0x%llX\n
[%s] %d -> 0x%08x\n
iter=%lu
Failed to Identify & Explore Chip via KIS: %d (%s)\n
SSO info present but SSO disabled.
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Programming STM32%s...\n
Xtensa Option num_high_pri_intr: %d
[%s] cop %d -> 0x%08x\n
[CACHEOP] %d, 0x%016llx, %d\n
Error %d (%s) opening cmd snapshost save file
Unable to register assert upcall %s (Insufficient memory)
Failed to unlock flash\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} error %s at line %d
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
AP given is not a MEMAP
SOC AP[%d]: JTAG_AP\n
{%s} unmodified-probe_match = %s
{%s@%d} Probe reported connection lost [PROBEEOF].
CPU: %s halting debug is now %s\n
%s NOT configured\n
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
STM_FLASH_SR: 0x%x\n
{%s:%s@%d} Critical error [radar already requested]
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
Match Count is Zero. This is invalid.
product-name: %s\n
Couldnt figure out the size of flash, defaulting to 2MB\n
Cleaning up Each Booster Manager\n
Booster Bundle: %s\n
probe event: %s
Error returned from explore_pid
{%s::%s} failed: %s
Invalid current AP (%d), adopting APTABLE (%d)
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
In Writeflash\n
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
Optional Key: CPUMonitor not in preferences
{%s} probe_match = %s
%2d) %s %s [Busy]%s\n
{%s}ERR: bypass_device_name is NULL\n
CPU Monitor key does not exists for: %s\n
Xtensa Option num_wp: %d
ERR: conn->nchips != 0; looks like chip is explored\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
[1500] IR command '%s' missing required field 'opcode'
Trying to use size of 8 on not AXI bus
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
{%s:%s}: cpu powered off: unable to access a register for this CPU
{%s} skipping dcache flush, cache already clean
   JTAG-AP: Identification = %08X\n
CPU with %s Not Created via Name
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
in stmflash api\n
Valid Portal
[%s] E2H is set, virtualization is supported\n
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
Aligned Address: %llx
PKA Base: 0x%llX\n
[KIS] Words (Read/Write/Wrote): %d\n
The debug port associated with this chip has not been explored.
Found form-factor specific channel %u for device '%s'
[AstrisAsync] Completing all async commands. Initial err = %d\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
%s %3d'b%s\n
--> psr        size=%3d bit=%d
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
Awaiting response from Probe Map Server
unable to identify chip
AXportal_t Struct Is NULL
=== Found %s Boosters ===\n
replayPreflight
{%s} 0 words requested for read at address 0x%016llX
Failed To Instantiate SOC From Booster\n
CPU Supported in Runtime: %s\n
Die Config Disabled
DCCCTRL = %08X   res=%d\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
{%s} already connected
{%s@%d} Unable to create socket
{%s@%d} Found cached response
==== Exception Trace ====\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
{%s} FAILURE - NULL parameter
Flash Reg Adress is not set, using what is there\n
Flash Reg Adress 0x%llX\n
%d KB flash size detected.\n
{%s} Failed to extract ECID from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: synchronizing context
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
[AstrisAsync] Deactivating async...\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
In %s, DEVICE ID: 0x%X\n
SoC must have a DAP
{%s} no response from bridge
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s} Failed to extract CID from table (%d); continuing anyway
{%s} timed out waiting for cpu to halt during collect
Breakpoint Index: %d
Failed to access new_cpu status
{%s} handle ROM entry %d (level %u): %08x
%2d) %s %s%s\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
[%s] CPU BM Not Found, Bailing\n
{%s} status=%d being reported as Unknown
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
AXconn or json_out are NULL
Asked To Write To A Negative Register Index
--> extrawrstn %d
!!!! CPU Key %s is INVALID !!!!\n
[1500] TAP %d missing required field 'ir-cmds'
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
Magic does not match: %#x vs %#x\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
{%s} checking for single_port probe daemon on port %d
Could Not Allocate Loaded Booster Array
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Setting STOP CLOCK to TRUE
Could Not Find Booster Entry Function: %s\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
%s: []\n
 MEM-AP %X is hung\n
{%s} unable to find single_port probedaemon on port %d
SOC_t::{%s} CPU_t group=%d when group 0 expected
WARNING: %d KB flash size detected.\n
Bundle: %s NOT FOUND\n
[WRITE] %d -> %08X\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
JsonLogger: Schema loaded successfully for category '%.*s'
!!!! Complex Key %s is INVALID !!!!\n
%s constructed
pc:  0x%16s cpsr: 0x%16s %s\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
sent %zd bytes to Probe Map Server when sending %zu
Cannot create SoC [unknown chip identity (%d)]
Enabling USB Gateway
DEMCR write failure - %s (%d)
Complex CPU Name: %s\n
New format for cip gen register, unsupported: %d\n
AP[%d]: unknown type\n
{%s} invalid data width %d bytes
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
{%s::%s} [%s] unsupported width %d
## dpr 0x%02X -> 0x%08X\n
Error - STM32Hxxx reflash failed (%s).\n
pmu-name: %s\n
[SSTEP] bvr=%08x bcr=%08x\n
[READ] %d -> 0x%08x\n
{%s::%s} [%s] length=%u when width=%d
astris_get_async_ver failed with error: %s
{%s} failed (%s)
chip is 0??\n
{%s} bridge returned an error
Erasing...\n
{%s} bridge returned DECERR
No version information found in booster: %s
probetimeout retry failed logging as hang\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
\t0x%08llX...\n
{%s@%d} Unknown CS code [%u]
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
X12 Part
{%s@%d} IOServiceClose failed, err = 0x%08x
Connection to server accepted
AXportal_t Is Not Valid Type - %d
Got an error reading the DCM Control Register: %s
Logging Context Is NULL\n
Unknown number of groups in the explore table; can't parse group attributes
    INFO(%u,%d): %s(%04u): %s(): %s
Using 10pin connector skipping orientation check
{%s::%s} creating placeholder for CPU: name=%s
[1500] v2 plist missing required field 'taps'
{%s} Failed to extract PID from table (%d); continuing anyway
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Multi target booster, checking for %s.plist\n
dbgwrap halt failed, falling back to classic method
{%s} no chip found
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
Debug Clock Already Enabled
HOSTID bit not set\n
Booster Value is Not String\n
CPU %s already in the map with status: %d
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
[HALT] Chip %x\n
CPU %s not found or already removed from the map
Invalid file name: \"%s\". File names must not start with '.'
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
{%s} read ESR EL1|EL2|EL3 (%d)
probing %s status\n
{%s} Failed to get watchpoint count for %s: %s
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
{%s} connectName[local host]
dfu-Type: %s\n
Invalid SoC Booster. SoC Booster Requires PID\n
caller=%s, async=%d
{%s@%d} Failed to find cached response
CPU Die: %d\n
{%s::%s} NULL parameter
UPDATE cop64 %d -> 0x%016llx\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
## armcpu: success status even though not all bytes written\n
Original Content: 0x%08x
Can't get hardware model - failed to create string
Choose a device: 
Cleaning up Main Booster Object\n
--> master     size=%3d localwrstn=%d debug=%d
{%s} Thread %#llx clearing key %lu
[INS_WP] 0x%016llx x %d\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
\t%4X: %8X %8X\n
Please answer y=yes or n=no.\n
Could Not Match A Booster for %s\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
\t Writing 0x%08llX failed: %s
Can't get hardware model - failed to allocate data buffer
{%s} error %d(%s) reading data from the connection (at recv)
{%s@%d} socket connection is not available
Unable to read GPR 28
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
Unable to allocate memory for next part of big response
sending abort to clear a timeout\n
getOrCreateValue: addMember failed, returning doc root
=== Loaded %s Boosters ===\n
Could Not Find Any Boosters\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
{%s@%d} Connection to server failed, error=%d (%s)
XBS Version Modified: %s -> %s\n
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
replay_counter=%lu
AP[%d]: MEM_AP_APB\n
      Read of JTAG-AP port %u CSW failed with %s\n
\tCould not read the flash size. Using default 2MB size.\n
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Probe Type (%d) FW Version: %s does not support KIS.
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
## memapw %u 0x%016llX 0x%08X\n
[%s] chipinfo is NULL
Failed to create CPU %s - %s\n
[ARM32cpu_t::_read_register64] 0x%08x\n
{%s} asc status=%d being reported as Unknown
Error %d (%s) opening history save file
  Error path [%s]\n
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
invalid IR command '%s'
Initializing Booster Layer\n
TAP IDCODE: 0x%X\n
{%s::%s} halting %s\n
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
replay_counter=%lu, last_replay=%d
{%s} already collected %s, skipping
STM_FLASH_AR: 0x%x\n
{%s::%s} write OK but took %d tries
EICE chip %x initialized\n
Going To Create Generic ARMV8\n
{%s@%d} Unknown CS command error [%d]
[%s] Booster System Is Not Initialized Bailing\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
\tPrologue Aligned Read Failed
Programming STM32Lxxx...\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
Map is empty, not removing CPU %s
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
[AstrisAsync] Resuming Async Mode\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
{%s@%d} Unable to connect to server, %s:%d
{%s} FIFO full, try again
{%s} 0 words from probe when %d words left to read for reg %d
error %s reading DAP PFR1
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
Subsystem Monitor[%i]: %s\n
Error - STM32Lxxx reflash failed (%s).\n
{%s[select]} timeout while waiting for data from the connection
Could Not Get BoosterManager\n
Failed to read ide_table from KIS explore
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Can't find descriptor for group - can't index\n
{%s} Error looking up architecture (%s)
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
{%s=>%s} null reference to AXchip_t[0]
{%s} drain_packets=%d [%s]
Failed to convert CFArray to C Array\n
received %zd bytes from Probe Map Server when have %zu
unable to obtain sysap
Could Not Find Any Loaded Boosters of Type: %s\n
=== Detailed %s Boosters ===\n
!!!! DART Key %s is INVALID !!!!\n
   Debug Port: Trying SELECT %X\n
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
{%s=>%s} AXconn_t has no chips
AXmemap_stmflash calling STM32F4xx::reflash(0x40023C00)\n
Could Not Get Bundle Out Array of Found Boosters\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
{%s} ROMTABLE (nest=%d)\n
first read of CMDSTAT may fail if external reset occurred
Gathered Info:\n%s
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Warning: spun for a long time (> %ld seconds)\n
  Nested path: parent='%s', child='%s'
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
{%s} Error reading CPUID (%s)
checking if relay \"%s\" is valid
!!!! FILE RADAR: Don't know how to compare two values\n
Required key: %s @ index %d is NULL\n
Found the RTXCID Structure!\n
The log file has been updated with all available diagnostics.\n
[1500] TAP %d: irlen must be > 0 (got %d)
component group %d\n
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
OK: address translation resumed for %s successfully
Failed explore before forced KIS reset: %s\n
Preferences does not exists: %s, creating one.\n
Can't get OS build version - failed to get build version
%s probe[%s] from Probe Map Server [local host]
[AstrisAsync] Activate while async is already active!\n
AP[%d]: MEM_AP_AXI\n
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
In Readflash\n
Cannot create CPU descriptions from NULL info\n
{%s} probe [%s] added to list
Failed to convert CFString to C String.
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
Found %d APs
## apw %u 0x%08X 0x%08X ...(%d)\n
%-16s @ 0x%08llX : 0x%08X\n
CPU AP-Type: %d\n
     ARM %s breakpoints: %u\n
Failed to sync prefs at beginning
{%s} Failed to get breakpoint count for %s: %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
[AstrisAsync] replayConditionalCheck: condition hit!\n
[AsyncSnapshot] #%zu: %s\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
Successfully Authenticated DFT\n
%s construction failed
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Mass Erase...\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
%s: not supported.\n
[REM_WP] wp%d\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
{%s} Failed to resume %s: %s
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Result while reading first entry: %s , entry val 0: 0x%X\n
Error Reading Device Production-Fusing\n
\tbut is not guaranteed on this device.\n
\t Erasing Page %d...\n
ERROR: unable to resume translation for %s
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
{%s} probe_port = %d
Probe %s USB-C location is %s
Failed To Init Booster's Astris API In: %s with %s (%d)\n
\t%s\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
Generated JSON (first 500 chars):\n%.500s%s
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
## armcpu: success status even though not all bytes read\n
[AstrisAsync] Pause when already paused!\n
{%s} PRIMECELL [DONE]
{%s} Component ID read fail on romtable (%s)
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
dropping empty probeInfo (port=%u)
Programming Error is Set\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
{%s} Unable to read CPSR
[ARM64 INS_WP] 0x%016llx x %d\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
Error while trying to authorize: %d - %s\n
Astris Version Set: %s
[KIS] Address: 0x%llX\n
KIS Writevals putting back the value
using standard products.plist for %s
Chip Revision: 0x%X\n
Extract Offset: 0x%X for %d\n
     ARM %s debug CPU rev %d\n
collect_responses
{%s} unable to allocate probeInfo
Sprocket probe, for now I guess we will just say yes...\n
[1500] v2 plist missing required field 'bridges'
Protocol Version: 0x%X\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
** Unauthorized User/Network or ECID **\n
Connected to Probe Device Server [Log File %s]
Probe %s with unknown kick response %s
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} error %s writing EDSCR %s
SoC not identified by IDCODE - enumerating instead of instantiating
Caught a portal that we dont have a status map for: %d
{%s@%d} Received %d bytes when requested %d bytes.
Failed to find a plist for this soc %s
{%s::%s} EDSCR with TXU set - unable to recover.\n
{%s} m_exception_level(%d) != current_el(%d)
Request Dict:\n%s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
{%s} set=%u (sh=%u), way=%u (sh=%u)
%s probe[*] from Probe Map Server [%s]
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
After powerup CMDSTAT=%08X\n
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
## dpr 0x%02X failed (%s)\n
## apr %u 0x%08X %d -> 0x%08X ...\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
We are done with clean up\n
Pages %d\n
codeblock
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
No 1500 bridges or TAPs specified (v2 plist)\n
[DCC] Grabbing DTR failed: %s\n\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
{%s} Error setting up jtag-ap target (%s)
STM_FLASH_CR: 0x%x\n
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
Failed to init from cpu desc armv7m cpu: %s \n
CPU Supported in Integration: %s\n
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} [%s] m_exception_level=%u\n
[RESUME] Chip %x\n
[AstrisAsync] Pausing Async Mode\n
[AstrisAsync] Barrier hit!\n
STM32Fxxx flash programming status fault: 0x%08X\n
Probe (port=%d) with unknown status %s dropped from available list
Min Component - %s\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[AstrisAsync] Activating async...\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
relay_get: %s = ERR
Successfully connected to server, %s:%d
{%s} select success without file descriptor set
JsonLogger: Created with default schema version '%s'
{%s} read %d words from probe when %d words requested
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
{%s@%d} gethostbyname failed, error=%d (%s)
JsonLogger: Writing category '%.*s' to '%s'
Could Not Create Dictionary From Booster: %s
{%s} handle ROM entry
Can't get hardware model - failed to find matching IOService
Taking gateway control failed
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Unable to read FP
response == NONE; failed to get kis target info\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
Kick has been requested by probe server
comparing against match entry %d: %s
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Flash Size %d KB\n
Skipping CPU %s at 0x%llx: not present in IDE\n
Could Not Allocate Booster Location Array
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
CPU Address: 0x%llX\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
Error closing %s [%d]
{%s} %s: |%s|
{%s} %sing word #%d at address 0x%09llx: %s
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[%s] %d -> %08x\n
      Read of JTAG-AP port %u PSTA failed with %s\n
Hang Address: 0x%016llx\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
%#09llx-%#09llx: %s\n
[REMBP] bp%d\n
   Debug Port: SELECT %X: DISABLED\n
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
\tAligned Read Failed
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
\tCould not get sector number for address: 0x%llX\n
no system bus AP present when expected
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[PAR] Failed KIS Portal Access Preflight =%s (%d)
CPU PS-Register: 0x%llX\n
{%s::%s} ITE is not set: 0x%X\n
{%s::%s} [%s] error %s writing SCTLR_ELx
Hardware model: %s
{%s[recv]} %d(%s) [RETRYING]
{%s}#%02X %s [%s]
Complex Type: %s\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
\t[MATCH_SKIP] skipping entry
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
{%s::%s} [%s] error (%s) getting number of HW BPs
Wrong width, should be either 4 or 8\n
TatsuServer Found: %s\n
Can't get OS build version - failed to create plist
{%s} probeList has probeCount of zero
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s} probe device server closed the connection while trying to read data (at recv)
couldn't find CPU1. this is expected sometimes.
[1500] Error parsing IR command: %s
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Buffer is NULL
** \tTatsu AuthDebug Triage | All     **\n
Awaiting next chunk of big response
\tAstris does not support page-erase beyond first %d KB of flash.\n
--> debug      size=%3d acsr=%d
Breakpoint Address: 0x%llx
Type 'jebdump' to do scan/mem dump\n
En masse...\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
{%s::%s} %s resumed\n
{%s->%s} m_exception_level=%u
   {%s} Enabling debug unit\n
Setting CPU %s is_boot_core to %d\n
\t Writing 0x%08llX...\n
Groups %d\n
[%s] {%s->%s} END handling exception
## armcpu: bad status even though all bytes written (%d)\n
{%s::%s} [%s] !bpwp_initted, retrying init
could not perform cpu_preflight
## dpw 0x%02X 0x%08X\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
Got an error writing 0x%X the DCM Control Register: %s
read_dbg failed to access R_v7M_CLIDR
{%s} explore with exploreflags 0x%X complete [%d chip%s]
[PREFS] Key: %s - Val: %s
Xtensa Core %s NOT configured\n
[KIS] Portal Status: 0x%X\n
Found an async abort pending; clearing it\n
Probe Map comm error %d(%s) %s [%s]
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
[HALTED] dfsr = 0x%08x\n
{%s} %s status is '%s' [Status Read %d times]\n
%s SoC created
{%s} valid response from bridge
In Postflash\n
Raising to EL2 cause in Guest\n
{%s} FAILURE - malloc error
Subsystem Monitor Key does not exists: %s\n
!*!*!* Lightning header facing up.                                                    !*!*!*
Full JSON that failed validation:\n%s
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
Required Key-Value is a string, and not an array. Old booster found\n
VBAR: %#llx\n
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
In Eraseflash\n
1500 IR Commands:
[AstrisAsync] Resume when not paused!\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
Invalid current AP (%d), adopting latest (%d)
Successfully Authenticated\n
{%s:%s@%d} Critical error encountered:
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
Start Address=0x%08llX....End Address=0x%08llX
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s} Unable to read SP_EL0
   CPUID: 0x%08X\n
      Explore of JTAG-AP port %u failed with %s\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40022000)\n
AXmemap_stmflash calling STM32F7xx::eraseflash\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
[%s] TGE is NOT set. Traping to EL1 allowed.\n
[COLLECT] Chip %x\n
Cached async_replay capability version: %u
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
[PREFS] Key: %s - Val: NULL
     ARM %s watchpoints: %u\n
Failed to convert kisHubLoc %s to unsigned long long
%s: chip was NULL when attempting to release soc
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
relay_set: %s = CMD_ERR (%s)
Init objects failed
DEMCR read failure - %s (%d)
CPU Subsystem: %s\n
{%s::%s} HDE not set on %s. Will re-enable.
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
2: ARM64_SYSOP_ATS12E1R\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
\tCould not get sector size for address: 0x%llX\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
[1500] %s step %d: unknown instruction '%s'
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s} ROMTABLE (dbgbase=0x%llx)
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
connection about to be destroyed
can't find bid in response\n
Connected to Probe Device Server [Default Log]
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
[%s] EL @ end of Collect: %d\n
1: ARM64_SYSOP_ATS12E1R\n
{%s->%s}
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
Portal Status, Changing STATUS and CMD/STAT to reflect
Programming STM32Hxxx...\n
{%s[select]} %d(%s) [RETRYING]
\tErasing the entire chip and then programming a larger image may work,\n
[FLUSH]\n
{%s::%s} ERROR %d(%s) resuming %s\n
[%s] {%s->%s} Transitioning to exception level %u.\n
Width: %d not supported
{%s} DEVARCH read fail in CoreSight component (%s)
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
Probe %s LocationID Info is %s
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
## ARM32cpu_t::read_register 64 bit 0x%x\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
max_scan_bits is low: %d
[Auth Debug] Disabled\n
There is no debug port associated with this chip.
{%s} unaligned %d-byte access at address 0x%09llx
Could Not Get BoosterManager. Need To Call AXbooster_init\n
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
{%s} %s resumed\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
Before astris_kis_init_dp, CMDSTAT=%08X\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
USER %s(%04u): %s(): %s
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
Dumping Process Tree
Probe %s status: Busy
Could not find TAP at chip-index %d for v2 1500 config\n
Initializing (%s) Booster's Astris API\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
Stop Clock: %s\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
{%s} Failed to single-step %s: %s
{%s} Class 9 ROMTABLE (nest=%d)\n
unable to create connection
[1500] Error parsing bridge '%s': missing required field 'select'
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
   Debug Port: SELECT %X: SKIPPING\n
   Debug Port has unknown type\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Could not find portal by select %d, while interpreting result\n
Probe %s status: Idle
{%s} Reading base 0x%llx entry's component ID
Old ProbeDaemon does not support this command
Connect using RSD not supported\n
{%s} Failed to extract portal info from table (%d); continuing anyway
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
AP[%d]: MEM_AP_AHB\n
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
\tFailure: status errors: 0x%08X\n
KIS translator version : %d\n
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
DHCSR write failure - %s (%d)
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
Error %d(%s) executing instruction 0x%08X
Unable to read CPSR
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
   Debug Port not responding (%s)\n
[ANAMOLY] Could not find AXcpu_t object for CPU\n
{%s} no matching 1500-to-* bridge
In Preflash\n
We Are Matching Development Booster\n
{astris_probed_print_events} not supported in this build configuration
failed read from DEMCR - %s
[AstrisAsync] Failed to restart Async batch\n
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
!*!*!* ****************************************************************************** !*!*!*
Dart Base Address: 0x%llX\n
no debug bus AP present when expected; after sysap is NULL
end rev is not of expected format; skipping cpu_desc override\n
Problematic JSON value:\n%s
%s status transitioned: %d ('%s') -> %d ('%s')\n
process (%s) (%d) path: %s
{%s} %s
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
[%s] TGE is set so we traping to EL2\n
{%s} Found extra info in = %s, chopping string
{%s} %d(%s) [RETRYING]
{%s}#%02X cmd: %s, resp: %s
{%s} unsupported bridge type for %s
Could Not Allocate Mutable Dictionary For BoosterMangers
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
Unaligned Read @ 0x%llx Width: %d Bytes: %d
[PREFS] Key: %s - Val: ??
Programming (addr: 0x%08llX) Failed!!!
KIS Preflight No Need To Write to AP CSW
haskis bit not set\n
CPU Core Number: %i\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
\tTatsu AuthDebug Triage | All\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Failed to instantiate %s\n
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
CPU state %d
{%s->%s} ERROR=%d(%s)
DBGCTRL = %08X   res=%d\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
relay_get: %s = %d
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
AP is NULL
Hang Radar Info:\n%s\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
Warning: chip exploration did not complete successfully (%s)\n
AXmemap_stmflash calling STM32F2xx::eraseflash\n
Complex CPM Offset: 0x%llX\n
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
Write Failed: address=0x%08llX, length(in)=%lu, width=%d, length(out)=%d, result=%s\n
read failed, using old cached as base: 0x%x
Set custom PSD json file: %s
Gathered:\n
Complex ID: %d\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s} category=%d
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
Previous authentication in-flight, wait for it to finish\n
connection created
Probe %s Device Does Not Have LocationID
Failed to convert %s key @ index %d
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
{%s} Failed to get watchpoint mask for %s: %s
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
Flash Address Max 0x%llX\n
Xtensa Option num_bp: %d
no debug bus AP present when expected
[KIS] Portal ID: %d\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
{%s} collect result = %s
   Created Fake Debug Port Debug Port
Spew change. old=0x%016llX, new=0x%016X
Probe Map comm: request[%s], response[%s]
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
%-16s @ 0x%08llX : read failed\n
Koko probe, for now I guess we will just say yes...\n
Booster Info:\n%s
Gathered Value is Not Number\n
probetimeout retrying access...\n
After Programming (addr: 0x%08llX) Programming Error is Set: 0x%08X
Did Not Find Any Boosters For: %s \n
Both debug and xbs versions are set, maybe a bug: %s
[1500] Error parsing TAP description
   {%s} Clearing HNONSEC on AP \n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Creating CPU Returned: %s\n
Failed to allocate space for table!
Translate Stage Chosen: %d\n
[AstrisAsync] Barrier before pause\n
   JEDEC ID: 0x%08X\n
Increasing length by: %d\n
KIS Readvals putting back the value
Values Not The Type We Expected. Expected: Number and String\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
[CLEANUP]\n
AP Only Explore was asked for, stopping here
Xtensa Option dbg_intr_level: %d
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Init dbgwrap obj failed
Setting bypass channel to: %d\n
runBlock
Failed to read IDE through DAP\n
{%s} wrote %d words to probe when %d words provided in request
      AXap_read of R_JTAGAP_PSTA failed with error %s
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
New Length: %d\n
Creating CPU With Name: %s\n
Failed To Initialize Logging\n
--> cmd        addrsize=%d datasize=%d
using multi-target booster products_%s.plist
{%s::%s} [%s] error %s from _synchronize_context.
{%s} L2 cache operation completed [%s]
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
Could Not Allocate All Boosters Array
Matched via Bundle ID\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s} explore with exploreflags 0x%X completed with error [%s]
Going to do imago workaround\n
X06 Part
{%s} flags:0x%08x
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
register    %-15s %3u     \"%-s\"\n
\t%s (%s)\n
Failed to find a product plist for this soc %s
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s->%s} current EL (%d) already == target EL.\n
{%s} Component ID read fail for 0x%llx (%s)
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
AXmemap_read failure - %s
Found another target for the plist\n
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
Replacing key with value
[AstrisAsync] Deactivate while async is not active!\n
CPU has no regions, maybe powered off?\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
{%s} strsep empty so match any probe [localhost]
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s::%s} [%s] error %s reading SCTLR_ELx
Probe %s with unknown status %s dropped from available list
{%s@%d} Timeout while attempting connect to server
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
Matched Booster: %s\n
--> 0x%02x = %s
Invalid value for 'entry' tuple element - can't index
{%s} halting %s\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
successfully updated DEMCR
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Using KIS-STM to flash, on some parts we might be too fast for this using KIS-STM
{%s} bridge timed out
User created bundle found, ignoring version checking via plist
Complex CPU ID: %d\n
%s Bridge @ 0x%09llx-0x%09llx: %s
Component Group Offset: 0x%X\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
AXmemap_stmflash calling STM32Fxxx::reflash(0x40022000)\n
Using Built In CPUs\n
Original Length: %d\n
Can't get hardware model - failed to allocate data string
[READ] cop %d -> 0x%08x\n
{%s::%s} read OK but took %d tries
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
{%s} _pre_halt_hw result = %s
%s status is '%s'\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Selecting polling method %s
Passed NULL plist file\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
{%s} pmgr status=%d being reported as Unknown
Can't get OS build version - failed to create URL
Initialized Logging - %s
Could Not Allocate Info Keys Array
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
\t Sector %u...\n
Too many portals, we are at portal: %d while max is %d\n
[MEM] Uncompleted; DSCR = %08x\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Unable to disassemble_at_addr 0x%016llx
      Select port %u: AVOIDED\n
Target ID: 0x%X\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
{%s} connectName[%s]
Could Not Find Any Boosters of Type: %s\n
Explore: %u chip%s\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Read error (%s) @ 0x%08llX - retrying.\n
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
Unsupported device identification 0x%03X\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
ERROR!! Couldn't save %s binary data\n
{%s@%d} Received %d bytes when requested %d bytes [%s].
Debug Base: 0x%llX\n
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
{%s::%s} waiting for EDSCR ITE
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
Failed to read register to figure out flash address %s\n
kext connect name %s\n
Done.\n
    %s(): %s
{%s::%s@%d [%s]} Error %s: checking exception
{%s::%s} EDSCR in unexpected state. Returning %s.\n
OK: address translation suspended for %s successfully
   MEM-AP not enabled\n
Failed to convert %s key @ index %d to a number with base of %d\n
Booster System Is Not Initialized Bailing\n
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
batch_cmd_count: %d
Dart Name: %s\n
Cannot create complex descriptions from NULL info\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
[AstrisAsync] Discarding %zu completed command(s)\n
   Setting up AP IDR %08X\n
\tCould not read the flash size. Using default 1MB size.\n
Value Types Are Not Strings\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
Failed to sync prefs at end
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Fast Programming Error is Set\n
==== User Error Messages ====\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
About to call fault reg latch, min_operating_el: %d\n
[%s] {%s->%s} clear async abort
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
{%s} _pre_resume_hw result = %s
   ROM entry %d (level %u): AVOIDED\n
Initial DSPSR_EL0: 0x%llx
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
{%s} hostname:%s, flags:0x%08x
Initialized %d 1500 bridges\n
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
caller=%s, async=%d, iterations=%lu
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Verification Mismatch starting at offset %d\n
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
DBGSTATUS = %08X   res=%d\n
failed write of 0x%08X to DEMCR - %s
      Select port %u: already explored..re-exploring\n
%s
Adding new booster path: %s\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
register lookup by name not supported when Astris is statically linked
Breakpoint Enabled: %s
Failed to create optional file. Not fatal, moving on
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
[KIS] Register Read/Write/Wrote: %d\n
bypass-config-name: %s\n
** CPU %s requires forced explore override flag on this SoC **\n
[INIT]\n
{%s} %s status failed. error: %d (%s)
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
Can't get hardware model - failed to get property
Failed to create Xtensa CPU %s \n
{%s} _halt_hw result = %s
   {%s} Read AP's R_MEMAP_CSW\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
{%s} NOMEM
Dart CPU SID(s): %s\n
1: ARM64_SYSOP_ATS12E1W\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[MEM] Aborted; DSCR = %08x\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
   Debug Port: SELECT %X; error: %s, retrying..\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
ERROR!! write binary data parameters invalid\n
Error %d (%s) while expanding ~ for Astris history save\n
{%s} bridge returned SLVERR
[1500] Using %s.plist
Failed to get DFU Type
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
2: ARM64_SYSOP_ATS12E1W\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
{%s} %s did not match any valid host
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
--> wrstn_wir2 size=%3d dpcsoc=%d
{%s} Failed to extract chip debug base from table (%d); continuing anyway
[READ] cop64 %d -> 0x%016llx\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
CPU Monitor[%i]: %s\n
unknown match criteria type: %d
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
Breakpoint Size: %d
   DPv3 BASEPTR0 is 0x%08X\n
{%s@%d} neither socket nor kext connection available
\t Erasing 0x%08llX...\n
Unable to read PC
   Debug Port: SELECT %X: AVOIDED\n
{%s} Error setting up memap target (%s)
      AXap_write of R_JTAGAP_PSTA failed with error %s
{%s=>%s} AXconn_t has no SoC object
Successfully Authenticated Probe\n
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
{%s} (end) current_el is now %d
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
{%s} Exploring with option: %s\n
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
start rev is not of expected format; skipping cpu_desc override\n
[1500] No %s.plist resource found
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
## armcpu: bad status even though all bytes read (%d)\n
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
AXmemap_stmflash calling STM32L4xx::reflash()\n
Portal Group Base: 0x%llX \n
\tReading left over chunk 0x%x @ 0x%llx\n
Invalid Size Given for AP AP=%d Size=%d
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
{%s} found single_port probedaemon on port %d
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
{%s} Extracted CIP Gen Number from table  (%d)
{%s} %s DC cache clean complete, marking as clean
comparing against match entry [pid] %d: %s\n
[%s] Booster System Is Not Initialized\n
Could not find bundle () in given array: %s\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
Async is disabled for localhost connection
{%s} calling _collect_hw on %s
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
Complex Name: %s\n
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
## dpw 0x%02X failed (%s)\n
--> localwrstn size=%3d debug=%d
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
error %s reading DAP MMFR0
{%s::%s@%d [%s]} Error %s: collecting HW
Length is 0
type_hint not NULL, but creating a placeholder, this is off
=== Starting Gather and Clear ===
Async is disabled for current seesion
SSO is DISABLED\n
Programming STM32Fxxx...\n
AXmemap_stmflash calling STM32H7xx::eraseflash\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
%s probe[%s] from Probe Map Server [%s]
Issuing request to Probe Map Server: %s
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
DEMCR: 0x%08X -> 0x%08X
{%s::%s} cpu powered off: failed init() %s
SWDACKDELAY relay write failed\n
Xtensa Option non_tie_ranges: %zu range(s)
{%s} probe_host = %s
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s} [%s] MMU not active - returning %s
AXjtag_srst assert failure - %s (%d)
Unable to read SP
Modified Word To Write: 0x%08x
## apr %u 0x%08X -> 0x%08X\n
Switch to primate res: %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
{%s::%s} creating AP slave: name=%s
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Highest EL: %d, -- Min Op EL: %d
Previous attempt to connect to probe failed: %d (%s). Retrying...
Probe %s with unknown port response %s
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
[REM_HWBP] bp%d\n
Exploring IDE in JTAG\n
Can't get OS build version - failed to open ReadStream
CPU Explore: 0x%llX\n
{%s->%s} START handling exception
\tLeft Over Chunk Read Failed\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
Start Page: %d\n
## memapr %u 0x%016llX -> 0x%08X\n
Error - eraseflash failed.\n
   {%s} select %u port %u: %u chip%s\n
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
Can't get OS build version - failed to create ReadStream
Could Not Get BoosterManagerUtility\n
BoosterManager Types:\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40023C00)\n
{%s} host:%s, flags:0x%08x
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
CPU Name: %s\n
[1500] Error parsing bridge: %s
{%s::%s} %s pre_resumed\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
tckrate_check returned error %s
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Error happened when reading edscr. Retry #%i\n
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Couldnt figure out the size of flash (we read: %d), using default\n
STM_FLASH_OPTKEYR: 0x%x\n
%s [RETRYING]
JsonLogger: Creating new category '%.*s'
[SSTEP] using BP %d\n
   --> IDR: %08X\n
Failed to explore chip: %d
Switch back to primate KIS: %s\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
\tWhole chip...\n
Can't get hardware model - failed to convert to C string
Invalid character [0x%02X] received from Probe Map Server
Cannot create DART descriptions from NULL info\n
Failed to get Bypass Config
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
   Debug Base: %08X\n
AuthDebug::authenticate_probe - no need to authenticate\n
STM_FLASH_ACR: 0x%x\n
STM_FLASH_KEYR: 0x%x\n
AXmemap_stmflash calling STM32F4xx::eraseflash\n
We are in clean up\n
Created Connection - : %s
can't find pid in response\n
Error %s connecting to server %s:%s [RETRYING]
Probe Map Server Information: %s
Failed to convert primateLoc %s to unsigned long long
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
Could not find TAP at index %d to attach 1500 bridge to\n
CPU AP-Select: %d\n
## apw %u 0x%08X 0x%08X\n
relay_get: %s = CMD_ERR (%s)
SoC does NOT support IDE Explore\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
CPU Typehint: %s\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
Die Config Disabled\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
     0x%016llx: ERROR\n
Result while reading second entry: %s , entry val 1: 0x%X\n
[1500] %s step %d missing required field 'instr'
{%s::%s@%d [%s]} Error %s: resuming HW
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s} _resume_hw result = %s
## memapr %u 0x%016llX %d -> 0x%08X ...\n
Could not enable KIS SoC Access\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Flash unlocked...\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
X09 Part
{%s} host name(RSD): %s\n
Flash unlocked...(before erase)\n
[KIS] CMD: %s \n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
[READ] %d -> %08x\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Xtensa Option options: 0x%x
%s probe[*] from Probe Map Server [local host]
Astris Source Version: %s\n
## ARM32cpu_t::read_register %u\n
Unable to read GPR %d
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s=>%s} AXconn_t has more than one chip
\t[MATCH_FOUND] identified chip: %s
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
no system bus AP present with AHB, trying AHB5
Xtensa Option ocd_address: 0x%llx
Unable to create pthread key for conenction. errno=%d %s.
{%s::%s} creating CPU
[KIS] Register Index: %llu\n
AXjtag_explore failure - %s (%d)
AXjtag_srst deassert failure - %s (%d)
\tLeft To Read (%d) < width (%d).\n
\t Sector %u failed: %s\n
STM_FLASH_WRPR: 0x%x\n
Dart Coastguarded CPU: %s\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
      Select of JTAG-AP port %u failed with %s\n
SSO with no prompt being used
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
STM_FLASH_OBR: 0x%x\n
Probe %s selected
Failed to convert primateHubLoc %s to unsigned long long
Connected to Probe Map Server
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
error %s checking for data abort(uint32_t)
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
ERROR: unable to suspend translation for %s
Failed to read flash size at 0x%08llX : read failed\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
Table Size: %d\n
VBAR: %#x\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
{%s} Failed to get breakpoint mask for %s: %s
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
Size or Count provided are 0.
--> misc_wdr   size=%3d wirtestporten=%d
Fabric access is blocked. Expected if production unit, won't explore further.
AuthDebugWithTimer_t destructor \n
Probe %s removed prior to kick\n
Unable to allocate memory for big response
Dart Dart Type: %s\n
[%s] AP, DP, or chip given is NULL
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00,single)\n
Connecting to server, %s:%d
Passed NULL booster without custom plist\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s} Failed to extract die infofrom table (%d); continuing anyway
DBG_CPU: %s\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s} %s DC cache already clean since last halt, skipping flush
We are Allocating\n
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
{%s::%s} [%s] MMU is already active - returning %s
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
{%s} error: %s
AXmemap_readvals failure - %s
{%s::%s} EDSCR with RXO set - unable to recover.\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
\tReading left over chunk expected 0x%x got 0x%x\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
SoC has been setup using standard instantiation (setup result=%s)
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
Probe %s Device Not Connected on USB-C Port
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
Had an error during transfer: %s
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
{%s} restored el is now %d
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
[%s]\n
\t Bank %u Sector %u...\n
\t\t%s\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s} setting up nameless target (address=0x%llx)
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
Previously dumped the process tree, skipping
{%s} unable to allocate probe name
Asked To Read A Negative Register Index
Gateway Version: 0x%X\n
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
SoC has been setup using standard instantiation (setup result=%d)
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Flash Sector Max %d\n
write to CMD/STAT failed - %s
Found match - bypass_device: %s; channel: %d\n
AP[%d]: JTAG_AP (Exploring Later) \n
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Kick off the current process using probe %s? (y|n)\n
gmtime() returned NULL, using epoch time
We are at max iterations, still didnt get full JSON
** Add the --with-force option or use the explore_override console command **\n\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
Unable to convert plist file name to CFString: %s\n
Exception %d Stack Trace
[Auth Debug] External Debug Interfaces Open\n
{%s} %s: |%s|-|%s|
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s} host = %s
No 1500 bridges specified\n
\t\tARMv6 debug CPU xxx ID\n
OCD ID register
Could Not Get Bundle Out Array of Found Boosters\n
{astris_probed_print_events} not supported in this build configuration
[%s] TGE is set so we traping to EL2\n
{%s::%s} ERROR %d(%s) resuming %s\n
read_dbg failed to access R_v7M_CLIDR
internal.is_probe_authenticated.debug_auth == NULL
Expected data value for S32C1I
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
lock_flash
CPU Explore: 0x%llX\n
AXjtag_settck
LMFLASH
AXbooster_interface_cleanup_astris_api
{%s:%s@%d} [%s] setting GPR\n
ret.restoring_el_after_raising_to_read_hcr
localhost
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
{%s} Unrecognized component: %08X, class %02X\n
_remove_data_breakpoint
[COLLECT] Chip %x\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
process_status_transition
AXcpu_suspend_translation
invalid command
Banana split probe, for now I guess we will just say yes...\n
bundle_id
!!!! Critical Error:  dspsr_el0 NOT DIRTY !!!!\n
{%s::%s@%d} [FALSE] src_gpr[0x%08X] < GPR_COUNT\n
Failed to write CR reg @ 0x%llX\n
Connected to Probe Map Server
Pop
JsonLogger: Loading schema for category '%.*s' from '%s'
astris_ide_print_platform_info
astris_addr_which_die
unable to read memory (permission checks suspended)
   DPv3 BASEPTR0 is 0x%08X\n
EPS7
MAC16 data register 0
param.reg_name.!match
RdProt
PARTNO_SWDP_M7
at=%u,as=%u,offset=%u,opcode=0x%6.6X
TGTOFF
FLASH_WRPR1
no DP (Debug Port)
Unable to read SP
EL2h
Going To Create Generic Xtensa Core, name=\"%s\".\n
ret.reg.write.K_DA_REG_NAME_ECID1
AXdebug_auth_is_authenticated
astris_ide_get_boardid
{%s} set=%u (sh=%u), way=%u (sh=%u)
far_el1
far_el3
Failed to exec DCPS in order to move EL up to %d
Invalid current AP (%d), adopting APTABLE (%d)
Data break 0 control
M1
[1500] TAP key is not a valid integer
_ocd_reg_dcr_set
Low level
Failed to create Xtensa CPU %s \n
cpu_cleaninv_l2cache
ObjectEmpty
AXdisassemble_at_phys_addr
Error occured during nonce command (v.5)
ERROR!! write binary data parameters invalid\n
AXconn_hostname
Connected to Probe Device Server [Log File %s]
{%s} empty response string provided
soc or sysap not available
chip->ide_table == NULL
!!!! Critical Error: batch attitude thread must be active when checking usage !!!!\n
DLR_EL0
EPC4
fn._ocd_reg_w.ddr.t2_save
fn._ocd_exec_instr.TIECompleteRead
PAYLOAD_OVERFLOW
AXchip_get_chip_variant
go
Could not enable KIS SoC Access\n
op_RSR_encode
fn._read_cfg_reg_0
Error - STM32Hxxx reflash failed (%s).\n
data-size
Type 'jebdump' to do scan/mem dump\n
PRID
fn._read_special_reg.ibreakenable
high
{%s:%s@%d} [%s] timeout waiting for flash idle: SR = 0x%08X\n
Register file 11
param.op.invalid.outofrange
Failed to read ide_table from KIS explore
0x2
https://gs.apple.com:443
JTAG level control
phase
Probe Type (%d) FW Version: %s does not support KIS.
!!!! Critical Error: {%s->%s} EL3 not implemented !!!!\n
WRBUF
{%s:%s@%d} [%s] FLASH_CR START read failed: %s\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
[HALT] Chip %x\n
{%s=>%s} no soc reference; falling back to direct cpu method
General register 6
fn.stmflash.h7.sector_erase.param_check
cpu_hwbp_disable
Invalid object or key for engineer array
Standard
Tarsier
astris_batch_attitude_cop
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
OCD debug status register
ret.get_hang_crumb
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
ret.ito.clear_edscr_err
RF44
src_gpr <= 15
more than one when unique required
META
ParseNull
STM
Failed to sync prefs at end
_sw_breakpoint_remove
astris_setup_memap_target
SWDACKDELAY relay write failed\n
Table 5–134
Section 5.3.6
WindowStart
{%s} exec: DRPS_ENC\n
OUTEN_RESTART
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
AXcpu_read_dcc
{%s} wrote %d words to probe when %d words provided in request
RF27
JTAGONLY
fn.stmflash.h7.reflash.flash_size
Dart Dart Type: %s\n
AuthDbg,ECID
/AppleInternal/Applications/PurpleRestore 3.app/Contents/Frameworks/MobileDevice.framework
ASTRIS_ERR_RESETTING
{%s:%s@%d} [%s] failed to select probe\n
param.chip->conn == NULL
ret.spmi_write
{%s:%s@%d} [%s] FLASH_CR MER write failed: %s\n
General register 9
Probe %s with unknown port response %s
There is no system bus access port on the debug port
{astris_probed_print_events_from_json} not supported in this build configuration
{%s::%s@%d [%s]} Error %s: pre_resuming HW
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
FLASH_PEKEYR
AXlog_init_with_ctx: lock could not be obtained
[1500] v2 plist missing required field 'taps'
spsr_el2
Error happened when reading edscr. Retry #%i\n
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
!!!! Critical Error: current_el[%d] <  %d !!!!\n
AXdebug_auth_is_dft_authenticated
Register file 32
access to target is blocked
Info_
Going to do imago workaround\n
clear_probe_authentication
Memory error PC register
j1500i2
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
AXcpu_lacc_count_read
Port
MISC
.start_time
CS-ETB
astris_explore_enabler_del_cpu
_set_bpaddr_hw
{%s:%s@%d} [%s] config_write_protection failed: %s\n
Table 5–179
fn.local
fn._ocd_reg_r.dsr.1
{%s} Found extra info in = %s, chopping string
reset_dcm: %s
vaddr
]
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
!!!! FILE RADAR: Don't know how to compare two values\n
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
[%s] AP, DP, or chip given is NULL
OCD control register, set
setup_bp.not_halted
cpu not halted
Failed to get Bypass Config
Going To Create Generic ARMV8\n
RF49
setup_transaction_objects
{%s:%s@%d} [%s] writing DRCR\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
*
fn.stmflash.h7.sector_erase.flash_idle
astris_soc_release
panic_diagnostic
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
ret.pka.verify.valid
OCDID
fn.remove_epcn_epsn
\tWriting 0x%08llX failed: %s
Waiting for flash to idle before mass erase, failed\n
_a64cpu_encode_aarch64_add_imm
Breakpoint Enabled: %s
{%s=>%s} null reference to CPU_t object, `cpu->state`
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_preferences.cpp
var._tgt.invalid.null
fn.stmflash.h7.sector_erase.read.cr_reg
Register file 48
FindMember
{%s:%s@%d} [%s] PECR read (prog) failed: %s\n
{%s} %d(%s) [RETRYING]
product-name: %s\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
hardware error reported by probe
internal.is_dft_authenticated.chip == NULL
fn._ocd_reg_r.regval
data_reg=%u,opcode=0x%6.6X
Unknown Subcommand
ASTRIS_ERR_TIMEOUT
_synchronize_context
fn._ocd_exec_instr.rsr.2
CSSELR
internal.enable-test.debut_auth == NULL
set_voltage_scaling1
Can't get OS build version - failed to create URL
generic probed USB error
setCategoryValue
WCR0_EL1+index
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
ret.reg.write.K_DA_REG_NAME_NONCE_1
Memory error PS register
path
Terminate parsing due to Handler error.
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
wpcr
R8
Invalid reg_index %u
{%s@%d} Timeout while sending probe command.
framework
Could Not Create Dictionary From Booster: %s
AOP
read back of modified data did not match
@AuthDbg,Ticket
New Length: %d\n
%02u:%02u:%02u:%06u|%s <%s> %s
ASTRIS_ERR_ASYNC_BARRIER
fn.stmflash.g071.mass_erase.write.cr_reg
ERR
fn._ocd_exec_instr.wsr
fn._write_pc
%d.%dbeta%d
host
NXP
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
PARTNO_ARM7TDMI2
Unknown kick response[%s] (for probe %s) from probe server
Kick has been requested by probe server
Schema parse error
Invalid Bundle: %s
DCS_BC2
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
{%s::%s@%d} [FALSE] CRm out of range [0x%08x]\n
High level exception save location
LOSTCONN
Writing for flash to idle berore unlock, failed\n
Failed to convert %s key @ index %d to a number with base of %d\n
m_bp_details
!*!*!* ****************************************************************************** !*!*!*
[Auth Debug] External Debug Interfaces Open\n
{%s:%s@%d} [%s] unable to read command response\n
cpu_mmu_configure
astris_update_ap_slave
Register file 17
RF3
Xtensa Option dbg_intr_level: %d
AXLOG
localhost with name matching %s
memap_bus_read
_a64cpu_write_gpr_cached
High level 3 exception PS
THREADPTR
description
set.success
result.booster_api_vers==NULL
[REMWP] wp%d\n
op_L32I_encode
host_get_probehost
Die Config Disabled
_read_register32
AMAuthInstallSsoSetAppleConnectInfo
ret.astris_set_user_die_select.astris_soc_get_applesoc
{%s} ROMTABLE (dbgbase=0x%llx)
param.sr.invalid.>255
ASTRIS_ERR_USB_NODEVICE
pid
expFrac <= 0
Impeded
astris_init_dp
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
STM32F10x_XLDensity_FLASH
{%s} %s did not match any valid host
runBlock
[AsyncSnapshot] No snapshots collected\n
ExcCatch
## memapw %u 0x%016llX 0x%08X\n
EPIREAD
wrstn-reg
Exception occured after executing MSR to write into sysreg
Failed AP read of R_MEMAP_CSW res: %i
Table 5–175
astris_stmflash_h7xxx.cpp
start rev is not of expected format; skipping cpu_desc override\n
write.dspsr_el0 NOT CACHED
AuthDebugUseSSO
ret.CFURLCreateCopyAppendingPathComponent
(system_reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) != 0
%04X:
op_S32I_encode
!!!! Critical Error: m_exception_level[%d] == 0|1|2|3 !!!!\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
RF51
stack.h
elapsed_seconds
True
{%s} Unrecognized Component: %08X (class %u)
ret.pka.nonce.status.err
General register 13
fn._write_mem
Could Not Get BoosterManager. Need To Call AXbooster_init\n
RF30
Can't get OS build version - failed to create plist
{%s} unable to find single_port probedaemon on port %d
NotNullStrLen
!Base::level_stack_.template Top<typename Base::Level>()->inArray
Eval
{%s} 0 words from probe when %d words left to read for reg %d
{%s} _resume_hw result = %s
param.bp_state.invalid.null
CortexM4
Dart Name: %s\n
Portal Group Offset: 0x%X Entries: %d\n
exit.exception_test_2
{%s::%s@%d} [FALSE] src_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
string_view::substr
are_any_bp_wp_set
   --> IDR: %08X\n
Register file 41
Register file 52
RF7
astris_probeV2_list
ret.test.2.0
{%s:%s@%d} [%s] executing MRRC\n
FLASH_PECR
FAR_EL3
!!!! Critical Error: m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15 !!!!\n
AXdebug_auth_authenticate
[PREFS] Key: %s - Val: NULL
Failed to read register to figure out flash address %s\n
RF29
Kick error while communicating with probe server
Could Not Get BoosterManager\n
3679.40.30b172
Unable to convert plist file name to CFString: %s\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s} Component ID read fail on romtable (%s)
## memapr %u 0x%016llX -> 0x%08X\n
symbol.check.loaded.AMAuthInstallSupportDictionarySetBooleanPtr == NULL
AMAuthInstallLogSetHandler
wrstn-dpcsoc
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
CPU Monitor[%i]: %s\n
Memory error status register
fn._read_special_reg.reg_srn
v%s.%s
mach_absolute_time
error %s checking for data abort(first)
(crm & ~ARM64_HINT_CRM_MAX) == 0
cs_type:0x%x
_sw_breakpoint_insert
\tReading left over chunk expected 0x%x got 0x%x\n
write_reponse_and_check_authentication
Register file 5
%s/%s
Warning: spun for a long time (> %ld seconds)\n
Register file 22
FLASH_CR1
Connection to server accepted
{%s:%s@%d} [%s] writing WVR %d\n
lower.safe.aarch32=notsupported
HOSTID bit not set\n
param.conn == NULL
{%s} Thread %#llx clearing key %lu
dest_reg < 15
CTI_OUT_EN1
{%s::%s} [%s] error %s reading SCTLR_ELx
astris_user_default_set_nickname_for_key
PARTNO_DAPLITE
FAR_EL1
src_gpr < 32
{%s} Error reading PID (%s)
Table 5–177
RF32
HIFI3_1
%s: %s\n
{%s} unmodified-probe_match = %s
_status_hw
!!!! Critical Error:  dlr_el0 NOT DIRTY !!!!\n
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, &d, %d, false, %d)\n
!!!! Critical Error: (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0 !!!!\n
DP
AXjtagap_explore
sso_user.sso_data == NULL
SubsystemMonitor
fn._ocd_reg_dcr_clr.dcr_enable_ocd
kisHubLoc
%2d) %s %s [Busy]%s\n
%s
_clean_l2cache_setway
{%s:%s@%d} [%s] doing JTAG scan (DTRTX)\n
COMPARE0
High level 4 exception PC
Could not find portal by select %d, while interpreting result\n
target not in appropriate state for action
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
AXchip_fromreset
stack_.GetSize() == sizeof(ValueType)
STM32G0A1xxx
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
Invalid condition while connecting to
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
EXPLORE_WITH_DISPLAY
{%s:%s@%d} [%s] FLASH_CR SER read failed: %s\n
{%s:%s@%d} [%s] FLASH_CR sz write failed: %s\n
var.num_loops.invalid>3.curr_instr
CHAINERR
read_resp_payload_via_sock
_read_memory_slow
GPR
ret.transfer.half_duplex
1: ARM64_SYSOP_ATS12E1W\n
MAC16 data register 2
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
JSON string output is null
n <= m
[%s] m_dc_max_level %d, m_ic_max_level %d\n
{%s} probeList has probeCount of zero
PERSEIS
astris_exc_bread_test_1
{%s:%s@%d} m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15\n
[WRITE] %d -> %08X\n
X06 Part
{%s:%s@%d} [%s] Couldn't get CPU from AP\n
R0
HF3
_write_window_base
ret.read.edscr.masked.beginning
[%s] {%s->%s} clear async abort
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_dapcmds.cpp
{%s} no chip found
PARTNO_SWDP_SOC600
sso_user.sso_data_length == 0
Register file 43
regidx_save=%u
_get_wpcr_hw
{%s} [is_64] exec: ISB_SY_ENCODING\n
copyNickname
Xtensa Option ocd_address: 0x%llx
%s.console
KongSWD
query_events
timestamp
15002AXI
xtensa-non-tie-range-base
protocol version is too old
Specified host %s did not resolve to valid host
GetCachedPowerByIndex
{%s}ERR: bypass_device_name is NULL\n
Complex CPU Name: %s\n
astris_ide_get_dbgwrap_base
ret.read.gpr_0
clear_authentication
Single_port connection to probe server unavailable
u64toa
TAP IDCODE: 0x%X\n
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
SUCCESS
init_hw.pid0
virtual int CPU_t::halt()
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
Register file 16
Ring ASID values
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
AXconn_copy_nickname
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
AXcpu_hwbp_remove
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
## memapr %u 0x%016llX %d -> 0x%08X ...\n
Flash unlocked...\n
High level 4 exception PS
{%s:%s@%d} [%s] executing STCpi(uint32_t)\n
ret._set_wpcr_hw
Found %d APs
RF14
fn.__ocd_reg_w.ddr
Reading FLASH_CR1 failed during lock sequence\n
fn.stmflash.h7.mass_erase.read_optcr
classic
(dest_gpr & (0x40000000 | 0x80000000)) == 0
FLASH_SR2
KIS-HUB-NULL
MAX_KISSWD
storeNickname
{%s:%s@%d} [%s] PECR write (clean) failed: %s\n
High level 6 exception PC
fn._ocd_exec_instr.xsr.ddr.t1
Multi target booster, checking for %s.plist\n
PCORE
Failed to fetch if we are in ARM64 or AARCH32
ret.reg.write.K_PKA_REG_NAME_DBG_STATUS
SAR
Async barrier encountered
Probe %s removed prior to kick\n
.rsd
astris_kis_cfg_writevals_swd
astris_ide_get_soc_stop_clock
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
HostInfo
SWDRESET
IsString()
index < 87
Could Not Find Booster Entry Function: %s\n
ACC
%s: []\n
astris_cpu_status
astris_preferences_cpu_monitor_list
complexes
We are Allocating\n
ERROR: unable to suspend translation for %s
HWERR
fn._ocd_reg_r.ddr.memval_tgt_32
_ocd_reg_dsr_clear_and_validate
ASTRIS_ERR_NOCPU
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
dbgwrap halt failed, falling back to classic method
UNKNOWN_DAPSTAT
ASTRIS_ERR_USB_EMPTY
ARMV8
Category name is null
operator[]
{%s} read ESR EL1|EL2|EL3 (%d)
astris_user_default_remove_all_boardnames
Failed to read IDE through DAP\n
read_memory_dbgwrap
Exc Cause: 0x%x - Exc Vaddr: 0x%x
INFO
.json
dfu-Type: %s\n
Table 5–164
Could not find TAP at chip-index %d for v2 1500 config\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
PROBED_SLEEPING
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
ret.production_emulation
STM32G0B1xx
CPU DBG Ack: 0x%llx\n
gpr < 32
## dpw 0x%02X failed (%s)\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40022000)\n
op_ESYNC_encode
ASTRIS_ERR_FDSETOVERFLOW
read_resp_via_sock
Data TLB configuration
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
soc-name
DSPSR_EL0
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
plist
json
[KIS] Portal ID: %d\n
AXbooster_get_all_boosters
[AstrisAsync] Completing all async commands. Initial err = %d\n
OCD control register, clear
Register file 8
status
:
cpu_lacc_pipe
_init_bpwp
** \tTatsu AuthDebug Triage | All     **\n
AXdebug_auth_get_timer_count
{%s:%s@%d} [%s] CR write (prog) failed: %s\n
STM_FLASH_AR: 0x%x\n
Connection aborted: kick required to probe server
Connection is null
[iter %lu] after_codeblock_execution
Unaligned Read @ 0x%llx Width: %d Bytes: %d
ret.memap.read
{%s:%s@%d} [%s] busy timeout on open: %s\n
M4
Sleep
   {%s} Clearing HNONSEC on AP \n
connecting to selected probe (user-specified single_port)
AXexplore_enable_cpu_pattern
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
{%s:%s@%d} [%s] reading DSCR\n
{%s} (end) current_el is now %d
DBGCTRL = %08X   res=%d\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s::%s} cpu powered off: failed init() %s
Variables not setup
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
environment variable not found
poo
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
ACQ_SAMPLE_I2C
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
Put
development
!!!! DART Key %s is INVALID !!!!\n
{%s->%s} exec: encode_mov_vfp_to_gpr(scratch=%d, sysreg=0x%X, %d)\n
AuthDbg,EnSecureTestExternal
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
SoftwareBreak
Timeout waiting for flash idle: SR = 0x%08X\n
Astris-%d.%d~%d
clear_flash_errors
ret.createKey
tckrate_check returned error %s
read_resp_cmd_via_sock
R7
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
astris_batch_attitude_suspend
{%s:%s@%d} [%s] executing STRpi\n
unlock
RF26
fn._ocd_exec_instr.wsr.ddr.r0_r12
interface not in appropriate state for action
{%s:%s@%d} [%s] moving DSB to GPR 0\n
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
: [
PARTNO_SWDP_M0P1
fn._read_special_reg.dbreakc0
op_RFDD_encode
Warning: Default logging location requested when running as root (using [%s])\n
str != 0
EPC2
Lowering exception in AARCH32 Mode NOT SUPPORTED
(reg & (0x40000000 | 0x80000000)) != 0
Writing START in FLASH_CR failed during mass erase\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
write.dlr_el0 NOT CACHED
read_page_descriptor
AXcpu_hwwp_remove
False
internal.authenticate_probe.chip->soc == NULL
{%s:%s@%d} [%s] FLASH_WRPR2 write failed: %s (continuing)\n
{%s:%s@%d} [%s] Could not read MCU_IDCODE\n\n
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
Dumping Process Tree
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
astris_batch_attitude_attach
ret.read.edscr.after-drain
AuthDebug_t::init failed (AuthDebugWithTimer_t)
Xtensa Option reg_file_size: %d
{%s@%d} neither socket nor kext connection available
Failed to convert %s key @ index %d
_a64cpu_assert_state_valid_entry_exit
param.ar.invalid.>15
Set custom PSD json file: %s
ARMV7M
Missing a comma or ']' after an array element.
AXbooster_refresh
[%s] cop %d -> 0x%08x\n
Highest EL: %d, -- Min Op EL: %d
{%s:%s@%d} [%s] Programming failed: %s\n
High level 2 exception PC
ASTRIS_ERR_PROBECOMMAND
regex_.IsValid()
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
probing %s status\n
RF25
Register file 42
Table 5–138
Access Port
{%s:%s@%d} [%s] unable to drain response\n
revive
Failed to exec MSR to move contents of scratch (containing val to write) into sysregscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT || == SP\n
storeNicknameForKey
MEVADDR
=== Ending Gather and Clear ===
cpu_translate_with_dart
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
copyNicknameForKey
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
Enabled
EPS6
fn._collect_snr.excvaddr
remote probe is currently in use
explore_min
_read_gpr
_set_wpaddr_hw
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
ret.board.copyPairForPref
AXcpu_cache_info
wb=%u
{%s::%s} failed: %s
symbol.check.loaded.AMAuthInstallCreatePtr == NULL
authenticate_dft
{%s:%s@%d} [%s] wait_for_flash_idle failed (zero): %s\n
BADCODE
cpu_mmu_walk
[KIS] Portal Status: 0x%X\n
result.ide==NULL
spsr_el1
Trying to use size of 8 on not AXI bus
{%s:%s@%d} [%s] \tFailure: half-page @ 0x%08llX failed to verify\n\n
Register file 57
XTENSA
CDPUL
read-back (sys AP) did not contain SW BP instruction
internal.is_probe_authenticated.chip == NULL
ARM7
ARC
Invalid value for 'entry' tuple element - can't index
hwwp_insert
EXCSAVE1
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Chip identification failed
[1500] Error parsing bridge '%s': missing required field 'tap'
DCS_BC3
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
EXPLORE_WITH_AVE
OCD Debug data register
fn._clear_portal_status
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Error while %s:\n  %s %s
cpu-ascdebug-dbgack
Dock-Channels
astris_explore_enabler_destroy
_resume_translation_hw
Increasing length by: %d\n
{%s:%s@%d} [%s] SR write failed: %s\n
{%s:%s@%d} [%s] FLASH_WRPR2BR write failed: %s (continuing)\n
Error - STM32Fxxx reflash failed (%s).\n
ret.enableCpu
[AstrisAsync] Pause when already paused!\n
Table 5–153
Accumulator high bits
IBREAKENABLE
R2
opcode=0x%6.6X
.apple.com
astris_remove_loaded_soc_boosters
NRF
ret.reg.write.K_DA_REG_NAME_NONCE_0
too many of something
no device when sending request
ASTRIS_ERR_EXPIRED
CortexM0
Misc_NoSoC
{%s:%s@%d} [%s] getting GPR (diff mode)\n
Chip %x Status = %d\n
General register 15
ret.astris_soc_get_applesoc
Missing a closing quotation mark in string.
astris_ide_get_from_chip
_a64cpu_write_sysreg_hw
_log_setup_thread_specific
UNKNOWN_CODE
get_chipid
bool
probed USB transaction timer expired
str != 0 || len == 0u
USER %s(%04u): %s(): %s
ret.write_sysreg_hw.spsr_el
TatsuServer Found: %s\n
\t0x%08llX...\n
DBREAKA0
{%s:%s@%d} [%s] doing IR scan\n
OK: address translation resumed for %s successfully
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
{%s:%s@%d} [%s] Waiting for flash to idle before mass erase, failed\n\n
fn._write_mem.bp_info
Connecting to server, %s:%d
PROBETIMEOUT WHILE READING\n
Table 5–159
_set_single_step
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
comparing against match entry %d: %s
CPU2
ret.reg.write.K_DA_REG_NAME_ECID0
probe [port %u] on localhost
_
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
base_reg < 32
{%s::%s@%d [%s]} Error %s: initializing cache parameters
{%s:%s@%d} [%s] \tCould not read the flash size\n\n
createSOC
gpr != 31
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Table 5–181
/var/log/astrisclient
connecting to selected probe (single_port)
setup_booster_soc
diagnostic_checks
{%s:%s@%d} [%s] writing OSLAR (oslk)\n
fn._write_window_base
Breakpoint Index: %d
fn.stmflash.h7.unlock_flash.write.cr2.key2
cpu_translate_with_stage
pointer.h
ECID is 0\n
da_base == 0
lock
addMember.description
ret.find_dap
fn._ocd_enable.true
register    %-15s %3u     \"%-s\"\n
no system bus AP present with AHB, trying AHB5
')
Exception %d Stack Trace
EDSCR
load_framework_at_path
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
{%s:%s@%d} [%s] \tCould not unlock flash before erase\n\n
Could Not Find The Entry Function: %s
using standard products.plist for %s
Not supported portal of type: 0x%X
EL2t
     ARM %s breakpoints: %u\n
astris_user_default_copy_boardname_for_primate
Failed to setup bp=%d
cpu-xtensa-non-tie-ranges
EXPLORE_WITH_SEP_DEBUG
PARTNO_SWDP_M0P2
PROBED_USB_INUSE
Value is null
{%s:%s@%d} [%s] AIRCR write failed: %s\n
cpu-xtensa-ocd-base
_a64cpu_encode_mrs
DebugAuth
EXCSAVE4
Register file 58
fn._ocd_exec_instr.wsr.ddr.t1.2
!!!! Complex CPU Key %s is INVALID !!!!\n
~A
ret.modify.edscr.~a
_setup_wp
TatsuServer
fn.stmflash.h7.lock_flash.write.cr1
astris_write_hang_crumb
name.IsString()
cpu-xtensa-num-intr
result.read.portal.s2r_fsm
-
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
outstandingAcmds
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
AXdebug_auth_clear_dft_auth
Writing FLASH_CR1 failed during lock sequence\n
KIS Readvals putting back the value
{%s:%s@%d} exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this...\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
L5x2
Register file 29
ERROR!! Couldn't save %s binary data\n
astris_identify_load_booster
Full JSON that failed validation:\n%s
{%s::%s} [%s] MMU not active - returning %s
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
ret.authdebug.is_prod
Can't get hardware model - failed to get property
RaspberryPi3_BCM2837
start_time
ret.exec.drps
{%s=>%s} AXconn_t has no chips
RF31
Register file 55
RF6
fn._ocd_reg_r.dsr.2
JTAG Slave Unavailable
{%s:%s@%d} m_exception_level[%d] == 0|1|2|3\n
L1_INSTRUCTION
Waiting for flash to idle before sector erase\n
Probe %s status: Idle
RESPONSE_PAYLOAD_DONE
hwbp_enable
fn.stmflash.h7.reflash.read.verfied!=actual
PROBED
cpu_lacc_pc_status
init_hw.read.dhcr
Table 5–150
\"%s\" not a regular register
Key is null
relay
astris_explore_enabler_get_cpu_status
ret.dock_disconnect_mode
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
Kick required to connect: Busy probe
KIS-STM
end rev is not of expected format; skipping cpu_desc override\n
Size or Count provided are 0.
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
!!!! Critical Error: aarch64[%d] == believed_64bit[%d] !!!!\n
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
configure_mmu failed
ret.reg.write.K_DA_REG_NAME_NONCE_3
EXCSAVE3
OCD.DSR=0x%8.8X
Booster Value is Not String\n
PROBED_USB_REQ_EMPTY
CPU state %d
{%s:%s@%d} [%s] moving DTRTX to GPR\n
[READ] %d -> 0x%08x\n
EXPLORE_ONE_DIE
SSO with no prompt being used
Unable to register assert upcall %s (Insufficient memory)
XACT
.user
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
chip-index
src_reg < 32 || src_reg == 31
EXCSAVE6
{%s} pmgr status=%d being reported as Unknown
Register file 34
ASTRIS_ERR_TOOMANY
soc-revisions
mempool-base
result.read.dbgwrap_base==
offset = %d
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
DCCCTRL = %08X   res=%d\n
astris_dpread
ret.home_url == NULL
APCIE_ANS0
Table 5–136
ICOUNT
dtoa.h
cpu-xtensa-options
bridges
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Register file 59
fn._read_special_reg.SRN_WindowBase
mismatch detected
fn.stmflash.h7.wait_bank_flash_idle.read.sr_reg
probe %s [port %u] on localhost
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
ret.cfg.read.swd
DFR0_LO
hwbp_disable
{%s:%s@%d} [%s] Not idle after mass erase: %s\n
CPU with %s Not Created via Name
n >= 0 && n <= 308
/usr/local/share/astris/boosterpack
Table 5–169
Unable to allocate memory for next part of big response
{%s:%s@%d} [%s] unable to transfer command\n
JAM
s
{%s:%s@%d} [%s] PECR write (prog) failed: %s\n
ARMDAP
Schema validation failed at: %s (keyword: %s)
AXchip_is_prod_fused
ret.test1
{%s:%s@%d} [%s] reading OSLSR\n
M23
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
0123456789abcdef
STM32G051xx
EDDTRRX
intack
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp
Bug
TRST
Failed to populate component info
fn._ocd_reg_w.dcrclr.regval
Error %d (%s) while expanding ~ for Astris history save\n
JsonLogger: Schema loaded successfully for category '%.*s'
Write Failed: address=0x%08llX, length(in)=%lu, width=%d, length(out)=%d, result=%s\n
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
CTI_CTL
ret.dspsr_el0
## dpr 0x%02X failed (%s)\n
ret.reg.write.K_PKA_REG_NAME_DBG_CMD
Table 5–152
{%s:%s@%d} [%s] Writing PG to FLASH_CR during programming failed: %s\n\n
{%s} Failed to extract component info from table (%d); continuing anyway
deinit
M3_ROM
{%s} [!is_64] exec: encode_msr(MDDTRTX_EL0, 0, %d\n
Setting WP length not currently supported: %u
lldb
ret._a64cpu_write_sysreg_hw
AXcpu_sstep
CPU at Index: %d has to specify only one AP Type or AP Select\n
ESR_EL1
load_framework
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
General register 4
param.invalid.reg_file_index.outofrange
CortexM7
GetType() == kNumberType
class_var.m_interface_name==NULL
/cpus
!!!! Critical Error: Thread %#llx key %lu suspending when already suspended for info %p - IGNORED !!!!\n
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
[CACHEOP] %d, 0x%016llx, %d\n
Error status from AMAuthInstallSsoEnablePtr = %i
Probe Map name of probe %d is: %s
relay_get: %s = %d
AMCP0
[%s] Executing instruction=%llx
```
