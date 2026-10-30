# `/usr/local/share/astris/boosterpack/swdflashers/arm_stm32_swdflasher.booster/arm_stm32_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,843,744 bytes.

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

## Strings (7,126)

First 2,500 of 7,126.
```
Both debug and xbs versions are set, maybe a bug: %s
[%s] E2H is set, virtualization is supported\n
Trying to use size of 8 on not AXI bus
Programming STM32Hxxx...\n
HOSTID=0x%x which is invalid, skipping orientation check
%s probe[*] from Probe Map Server [local host]
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
KIS Readvals putting back the value
Probe %s selected
Creating CPU With Name: %s\n
Early dbgwrap base extracted: 0x%llx\n
[%s] %d -> %08x\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
{%s=>%s} no soc reference; falling back to direct cpu method
Preferences does not exists: %s, creating one.\n
{%s} %s: |%s|-|%s|
Failed to init from cpu desc armv7m cpu: %s \n
using multi-target booster products_%s.plist
{%s} collect result = %s
{%s} handle ROM entry
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
[PREFS] Key: %s - Val: NULL
{%s} set=%u (sh=%u), way=%u (sh=%u)
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Can't get hardware model - failed to create string
Extract Offset: 0x%X for %d\n
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
Breakpoint Index: %d
Proceeding with full explore instead of instantiation
Warning: chip exploration did not complete successfully (%s)\n
{%s} bridge returned an error
\tErasing the entire chip and then programming a larger image may work,\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
could not perform cpu_preflight
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
      Explore of JTAG-AP port %u failed with %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
Verification Mismatch starting at offset %d\n
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
[AstrisAsync] Discarding %zu completed command(s)\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
probetimeout retrying access...\n
%s probe[*] from Probe Map Server [%s]
Failed to convert primateLoc %s to unsigned long long
Probe %s status: Idle
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
couldn't find CPU1. this is expected sometimes.
TargetSel Before Disable: 0x%x
Failed to read ide_table from KIS explore
1: ARM64_SYSOP_ATS12E1W\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
[PREFS] Key: %s - Val: ??
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
Invalid current AP (%d), adopting latest (%d)
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Xtensa Option ocd_address: 0x%llx
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
DHCSR write failure - %s (%d)
Had an error during transfer: %s
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
response == NONE; failed to get kis target info\n
{%s} %d(%s) [RETRYING]
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
getOrCreateValue: addMember failed, returning doc root
[PAR] Failed KIS Portal Access Preflight =%s (%d)
Probe Type (%d) FW Version: %s does not support KIS.
Could Not Allocate Booster Location Array
Portal Group Offset: 0x%X Entries: %d\n
{%s} Failed to extract portal info from table (%d); continuing anyway
Can't find descriptor for group - can't index\n
[WRITE] %d -> %08X\n
[%s] AP, DP, or chip given is NULL
Could Not Get BoosterManager. Need To Call AXbooster_init\n
=== Found %s Boosters ===\n
[CACHEOP] %d, 0x%016llx, %d\n
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Hardware model: %s
Can't get OS build version - failed to allocate buffer
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
[1500] Detected plist version %d
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
batch_cmd_count: %d
{%s::%s} error %s writing EDSCR %s
Switch back to primate KIS: %s\n
UPDATE cop64 %d -> 0x%016llx\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
Setting bypass channel to: %d\n
Multi target booster, checking for %s.plist\n
Complex Name: %s\n
[1500] Using %s.plist
Probe (port=%d) with unknown status %s dropped from available list
Kick off the current process using probe %s? (y|n)\n
setCategoryValue: path='%.*s'
CPU Subsystem: %s\n
Unable to disassemble_at_addr 0x%016llx
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
   ROM entry %d (level %u): AVOIDED\n
Done.\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
[AstrisAsync] Deactivate while async is not active!\n
[AstrisAsync] Resume when not paused!\n
type_hint not NULL, but creating a placeholder, this is off
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
\t0x%08llX...\n
Initial DSPSR_EL0: 0x%llx
[COLLECT] Chip %x\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
Failed AP write of R_MEMAP_CSW res: %i newval %i
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s} host:%s, flags:0x%08x
Probe %s with unknown status %s dropped from available list
component group %d\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
DCCCTRL = %08X   res=%d\n
Original Content: 0x%08x
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
{%s} Unrecognized Component: %08X (class %u)
{%s} match any probe [localhost]
[1500] run_steps: unknown instruction '%s'
{%s} no response from bridge
Write Protection Error is Set\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
{%s} %s resumed\n
{%s=>%s} AXconn_t has no SoC object
Programming STM32Fxxx...\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
[1500] Error parsing v2 bridges
Die Config Disabled
Exception %d Stack Trace
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
{%s::%s} failed: %s
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
{%s} probe_host = %s
{%s} %s
Setting CPU %s is_boot_core to %d\n
--> cmd        addrsize=%d datasize=%d
%s constructed
{%s::%s} %s resumed\n
{%s} Component ID read fail on romtable (%s)
%s: chip was NULL when attempting to release soc
Gathered Info:\n%s
Chip %x Status = %d\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
OK: address translation resumed for %s successfully
\tWriting 0x%X bytes @ 0x%08llX...\n
After powerup CMDSTAT=%08X\n
{%s} Failed to extract CID from table (%d); continuing anyway
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
Breakpoint Size: %d
      Select port %u: already explored..re-exploring\n
{%s} Exploring with option: %s\n
dfu-Type: %s\n
[%s] {%s->%s} END handling exception
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
[REMBP] bp%d\n
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
KIS Chip Found, Doing KIS Explore Setup
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
read_dbg failed to access R_v7M_CLIDR
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
{%s::%s} [%s] error (%s) getting number of HW BPs
SoC has been setup using standard instantiation (setup result=%d)
   Debug Base: %08X\n
%s [RETRYING]
gmtime() returned NULL, using epoch time
DEMCR write failure - %s (%d)
Cannot create DART descriptions from NULL info\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
Successfully Authenticated Probe\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
CPU with %s Not Created via Name
Required key: %s @ index %d is NULL\n
[SSTEP] using BP %d\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
{%s=>%s} AXconn_t has no chips
Flash Reg Adress 0x%llX\n
[%s] Booster System Is Not Initialized Bailing\n
Cannot create SoC [unknown chip identity (%d)]
Did Not Find Any Boosters For: %s \n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
CPU Monitor key does not exists for: %s\n
\tCould not get sector size for address: 0x%llX\n
{%s} already connected
%s: []\n
{%s} found single_port probedaemon on port %d
%2d) %s %s%s\n
!!!! DART Key %s is INVALID !!!!\n
[1500] v2 plist missing required field 'bridges'
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s::%s} [%s] length=%u when width=%d
Gateway is KIS, seeing what probe this is\n
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Programming Error is Set\n
[1500] No %s.plist resource found
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
AXmemap_stmflash calling STM32F4xx::eraseflash\n
SoC does NOT support IDE Explore\n
Flash unlocked...(before erase)\n
[CLEANUP]\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
{%s} Failed to get watchpoint count for %s: %s
Xtensa Core %s NOT configured\n
Skipping CPU %s at 0x%llx: not present in IDE\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
probetimeout retry failed logging as hang\n
## ARM32cpu_t::read_register %u\n
[INS_WP] 0x%016llx x %d\n
[AstrisAsync] Barrier before pause\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
Result while reading third entry: %s , entry val 2: 0x%X\n
Probe Map Server Information: %s
start rev and/or end rev is NULL; skipping cpu_desc override\n
    %s(): %s
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
Can't get OS build version - failed to create ReadStream
{%s} probe device server closed the connection while trying to read data (at recv)
Generated JSON (first 500 chars):\n%.500s%s
Dart Dart Type: %s\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
[1500] TAP %d missing required field 'ir-cmds'
{%s} Extracted CIP Gen Number from table  (%d)
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
SoC not identified by IDCODE - enumerating instead of instantiating
invalid IR command '%s'
We Are Matching Development Booster\n
failed read from DEMCR - %s
[AstrisAsync] Resuming Async Mode\n
{%s} Class 9 ROMTABLE (nest=%d)\n
In %s, DEVICE ID: 0x%X\n
Xtensa Option num_bp: %d
Connection to server accepted
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Unknown number of groups in the explore table; can't parse group attributes
{%s} category=%d
successfully updated DEMCR
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
[AstrisAsync] Completing all async commands. Initial err = %d\n
first read of CMDSTAT may fail if external reset occurred
\t%s (%s)\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
     ARM %s debug CPU rev %d\n
Increasing length by: %d\n
{%s} select success without file descriptor set
unknown match criteria type: %d
{%s::%s} creating AP slave: name=%s
Portal Group Base: 0x%llX \n
## armcpu: bad status even though all bytes read (%d)\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
[INIT]\n
Type 'jebdump' to do scan/mem dump\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
{%s[select]} timeout while waiting for data from the connection
1500 IR Commands:
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
      AXap_write of R_JTAGAP_PSTA failed with error %s
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
Hang Radar Info:\n%s\n
{%s} unable to allocate probe name
Could Not Allocate Loaded Booster Array
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[HALT] Chip %x\n
[RESUME] Chip %x\n
caller=%s, async=%d, iterations=%lu
AXconn or json_out are NULL
Could not find TAP at index %d to attach 1500 bridge to\n
HOSTID bit not set\n
Matched via Bundle ID\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
{%s@%d} Unable to create socket
There is no system bus access port on the debug port
CPU Core Number: %i\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
      Read of JTAG-AP port %u PSTA failed with %s\n
AuthDebugWithTimer_t destructor \n
[KIS] CMD: %s \n
[READ] cop %d -> 0x%08x\n
{%s} %s DC cache clean complete, marking as clean
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Async is disabled for localhost connection
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
comparing against match entry [pid] %d: %s\n
Error happened when reading edscr. Retry #%i\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
AXmemap_stmflash calling STM32F7xx::eraseflash\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
Error returned from explore_pid
Error %d(%s) executing instruction 0x%08X
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
   MEM-AP not enabled\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
DBGSTATUS = %08X   res=%d\n
dbgwrap halt failed, falling back to classic method
{%s} PRIMECELL [DONE]
{%s} Error %d(%s) sending message
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
--> debug      size=%3d acsr=%d
{%s} calling _collect_hw on %s
==== Exception Trace ====\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
AXmemap_stmflash calling STM32Lxxx::reflash(0x40023C00)\n
Can't get hardware model - failed to get property
%s given a NULL conn object
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Sprocket probe, for now I guess we will just say yes...\n
Could Not Find Booster Entry Function: %s\n
Complex Type: %s\n
     0x%016llx: 0x%08x    %s\n
\t\t%s\n
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
{%s} Component ID read fail for 0x%llx (%s)
received %zd bytes from Probe Map Server when have %zu
Mass Erase...\n
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
[1500] %s step %d missing required field 'instr'
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s} skipping dcache flush, cache already clean
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
En masse...\n
Probe Map name of probe %d is: %s
{astris_probed_print_events} not supported in this build configuration
[ARM32cpu_t::_update_register64] 0x%08x\n
Failed to explore chip: %d
{%s} probe_match = %s
** Add the --with-force option or use the explore_override console command **\n\n
VBAR: %#llx\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
{%s} _halt_hw result = %s
{%s} Error reading CPUID (%s)
## memapr %u 0x%016llX %d -> 0x%08X ...\n
register    %-15s %3u     \"%-s\"\n
Connected to Probe Device Server [Default Log]
%#09llx-%#09llx: %s\n
XBS Version Modified: %s -> %s\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s::%s} [%s] error %s from _synchronize_context.
replayPreflight
{%s[recv]} %d(%s) [RETRYING]
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Found match - bypass_device: %s; channel: %d\n
{%s} halting %s\n
Stepping Stone Final =  %#x\n
\tAligned Read Failed
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
SSO with no prompt being used
Portal Status, Changing STATUS and CMD/STAT to reflect
User created bundle found, ignoring version checking via plist
Error %d(%s) executing instruction 0x%08X FAST
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
Failed to create optional file. Not fatal, moving on
Previous attempt to connect to probe failed: %d (%s). Retrying...
{%s} %s did not match any valid host
Connected toProbe Map Server (single_port) 
no system bus AP present when expected
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
unable to identify chip
Valid Portal
Initializing (%s) Booster's Astris API\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
[AstrisAsync] Failed to restart Async batch\n
{%s} explore with exploreflags 0x%X complete [%d chip%s]
connection created
Could Not Get Bundle Out Array of Found Boosters\n
[1500] %s step %d: unknown instruction '%s'
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
SoC has been setup using standard instantiation (setup result=%s)
{%s} handle ROM entry %d (level %u): %08x
--> extrawrstn %d
Found form-factor specific channel %u for device '%s'
{%s::%s} halting %s\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s} Failed to get breakpoint count for %s: %s
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
\tCould not read the flash size. Using default 2MB size.\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Using 10pin connector skipping orientation check
Unable to allocate memory for big response
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
Section 1 Offset: 0x%llX\n
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s::%s} timeout while waiting for EDSCR ITE
[%s] CPU BM Not Found, Bailing\n
{%s} _pre_resume_hw result = %s
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
Failed to read flash size at 0x%08llX : read failed\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
{%s} Failed to single-step %s: %s
Error %d (%s) while expanding ~ for Astris history save\n
STM32Hxxx flash programming status fault: 0x%08X\n
Could Not Get BoosterManagerUtility\n
Failed to convert %s key @ index %d
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s::%s} write OK but took %d tries
[READ] %d -> %08x\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
Request Dict:\n%s
Astris Source Version: %s\n
[1500] Error parsing IR command: %s
   Debug Port not responding (%s)\n
Could not find portal by select %d, while interpreting result\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
\t Erasing Page %d...\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
     ARM %s breakpoints: %u\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s} _resume_hw result = %s
{%s} unable to find single_port probedaemon on port %d
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} no matching 1500-to-* bridge
Target ID: 0x%X\n
## memapr %u 0x%016llX -> 0x%08X\n
Pages %d\n
Die Config Disabled\n
error %s checking for data abort(uint32_t)
     0x%016llx: ERROR\n
Found %d APs
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Passed NULL booster without custom plist\n
Component Group Offset: 0x%X\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
[AstrisAsync] Activating async...\n
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
Breakpoint Enabled: %s
{%s} FAILURE - max length exceeded
X12 Part
Error %s connecting to server %s:%s [RETRYING]
relay_set: %s -> %d
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
tckrate_check returned error %s
Optional Key: SubsystemMonitor not in preferences
AXjtag_explore failure - %s (%d)
Complex CPU ID: %d\n
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
{%s::%s} [%s] error (%s) getting number of HW WPs
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
read failed, using old cached as base: 0x%x
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Xtensa Option num_wp: %d
process (%s) (%d) path: %s
[1500] TAP %d: irlen must be > 0 (got %d)
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
{%s} Unable to read SP_EL0
failed write of 0x%08X to DEMCR - %s
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
{%s} Failed to extract die infofrom table (%d); continuing anyway
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
JsonLogger: Creating new category '%.*s'
CPU PS-Register: 0x%llX\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
Cached async_replay capability version: %u
{%s} asc status=%d being reported as Unknown
\tReading left over chunk 0x%x @ 0x%llx\n
Error - STM32Hxxx reflash failed (%s).\n
KIS translator version : %d\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
2: ARM64_SYSOP_ATS12E1R\n
Caught a portal that we dont have a status map for: %d
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s}ERR: bypass_device_name is NULL\n
\t%s\n
bypass-config-name: %s\n
We are at max iterations, still didnt get full JSON
Board ID: 0x%X\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
   Debug Port: SELECT %X: DISABLED\n
[%s]\n
max_scan_bits is low: %d
Invalid value for 'entry' tuple element - can't index
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
[AstrisAsync] Activate while async is already active!\n
\tPrologue Aligned Read Failed
   {%s} Read AP's R_MEMAP_CSW\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
choice: %d\n
Please answer y=yes or n=no.\n
CPU %s already in the map with status: %d
{%s} already collected %s, skipping
AP[%d]: MEM_AP_APB\n
CPU Monitor[%i]: %s\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
Probe %s Device Does Not Have LocationID
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
{%s::%s} ERROR %d(%s) pre_resuming %s\n
   --> IDR: %08X\n
Can't get OS build version - failed to get build version
Probe Map comm error %d(%s) %s [%s]
Die-Count: %d Current-Die: %d Die-Type: %d
%s NOT configured\n
{%s} status=%d being reported as Unknown
      Select port %u: AVOIDED\n
X09 Part
[1500] Error parsing bridge '%s': missing required field 'tap'
==== User Error Messages ====\n
Magic does not match: %#x vs %#x\n
   Created Fake Debug Port Debug Port
Xtensa Option reg_file_size: %d
Failed to get PMU Name
{%s} Failed to resume %s: %s
{%s::%s} [%s] MMU not active - returning %s
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
\t Sector %u...\n
Read error (%s) @ 0x%08llX - retrying.\n
Xtensa Option non_tie_ranges: %zu range(s)
Created Connection - : %s
JsonLogger: Wrote %zu bytes to '%s'
\t Erasing 0x%08llX...\n
probe event: %s
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s} m_exception_level(%d) != current_el(%d)
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
[AsyncSnapshot] No snapshots collected\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
{%s} %sing word #%d at address 0x%09llx: %s
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
[AstrisAsync] Deactivating async...\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
register lookup by name not supported when Astris is statically linked
%s status is '%s'\n
{%s} setting up nameless target (address=0x%llx)
AXmemap_stmflash calling STM32L4xx::reflash()\n
Matched Booster: %s\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s:%s}: cpu powered off: unable to access a register for this CPU
Invalid Size Given for AP AP=%d Size=%d
Disconnected from Probe Map Server
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
\n
[AstrisAsync] Pausing Async Mode\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
STM_FLASH_KEYR: 0x%x\n
{%s} probeList has probeCount of zero
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
CPU (%s) has explore flag of: 0x%llx which is not set\n
Dart Base Address: 0x%llX\n
Replacing key with value
{%s=>%s} null reference to AXconn_t record, `conn`
AP[%d]: MEM_AP_AXI\n
{%s} explore with exploreflags 0x%X completed with error [%s]
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
  Error path [%s]\n
Erasing...\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
Booster Bundle: %s\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s->%s} m_exception_level=%u
EICE chip %x initialized\n
{%s::%s} cpu powered off: failed init() %s
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s} Error setting up memap target (%s)
   Debug base is in legacy format\n
Couldnt figure out the size of flash, defaulting to 2MB\n
{%s::%s} [%s] unsupported width %d
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
Can't get OS build version - failed to create plist
{%s} hostname:%s, flags:0x%08x
Probe %s Device Not Connected on USB-C Port
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Failed to read IDE through DAP\n
relay_get: %s = %d
AXmemap_read failure - %s
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
Error - STM32Lxxx reflash failed (%s).\n
{%s} unsupported bridge type for %s
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
Failed to unlock flash\n
Taking gateway control failed
{%s} 0 words from probe when %d words left to read for reg %d
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
[KIS] Portal Status: 0x%X\n
Found another target for the plist\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
AXmemap_stmflash calling STM32Lxxx::reflash(0x40022000)\n
%s %3d'b%s\n
{astris_probed_print_events_from_json} not supported in this build configuration
[REM_WP] wp%d\n
{%s} Error reading PID (%s)
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
Error - STM32Fxxx reflash failed (%s).\n
STM_FLASH_WRPR: 0x%x\n
{%s} error %d(%s) reading data from the connection (at recv)
Could Not Create Dictionary From Booster: %s
Failed to get Bypass Config
{%s::%s} [%s] error %s reading SCTLR_ELx
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Selecting polling method %s
{%s@%d} Connection to server failed, error=%d (%s)
Map is empty, not removing CPU %s
ERROR: unable to resume translation for %s
   {%s} Probe requires overrun detect mode.\n
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
{%s}#%02X %s [%s]
{%s->%s}
can't find pid in response\n
{%s@%d} Found cached response
AXjtag_srst deassert failure - %s (%d)
Invalid SoC Booster. SoC Booster Requires PID\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
can't find bid in response\n
Probe %s removed before port determined\n
comparing against match entry %d: %s
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
\t[MATCH_SKIP] skipping entry
CPU Die: %d\n
{%s} Failed to extract ECID from table (%d); continuing anyway
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
   Debug Port: SELECT %X: AVOIDED\n
--> wrstn_wir2 size=%3d dpcsoc=%d
Cannot create complex descriptions from NULL info\n
Variables not setup
Can't get OS build version - failed to open ReadStream
AP given is not a MEMAP
{%s} FAILURE - malloc error
[KIS] Words (Read/Write/Wrote): %d\n
Cannot create CPU descriptions from NULL info\n
     ARM %s watchpoints: %u\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
{%s} FAILURE - NULL parameter
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
AXmemap_stmflash calling STM32F2xx::eraseflash\n
Spew change. old=0x%016llX, new=0x%016X
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} Unrecognized component: %08X, class %02X\n
%2d) %s %s [Busy]%s\n
Init objects failed
--> master     size=%3d localwrstn=%d debug=%d
Unable to read SP
Invalid file name: \"%s\". File names must not start with '.'
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
STM_FLASH_ACR: 0x%x\n
Can't get hardware model - failed to find matching IOService
[KIS] Portal ID: %d\n
--> localwrstn size=%3d debug=%d
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Warning: spun for a long time (> %ld seconds)\n
ERROR!! Wrote %zd bytes, expected %zd\n
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
Failed to convert CFArray to C Array\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
Unable to read GPR 28
## armcpu: success status even though not all bytes read\n
## apw %u 0x%08X 0x%08X\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
Programming STM32%s...\n
Fast Programming Error is Set\n
Logging Context Is NULL\n
BoosterManager Types:\n
[MEM] Aborted; DSCR = %08x\n
About to call fault reg latch, min_operating_el: %d\n
Awaiting response from Probe Map Server
{%s} valid response from bridge
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
AP[%d]: JTAG_AP (Exploring Later) \n
   {%s} Clearing HNONSEC on AP \n
Error Reading Device Production-Fusing\n
The log file has been updated with all available diagnostics.\n
Failed to convert kisHubLoc %s to unsigned long long
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s} bridge returned DECERR
[%s] Booster System Is Not Initialized\n
CPU %s not found or already removed from the map
{%s} restored el is now %d
dropping empty probeInfo (port=%u)
Probe %s Device Server listening on port %d
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
Unable to read CPSR
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
Error status from AMAuthInstallSsoInitializePtr = %i
Xtensa Option num_high_pri_intr: %d
{%s@%d} neither socket nor kext connection available
Kick has been requested by probe server
=== Detailed %s Boosters ===\n
CPU Explore: 0x%llX\n
CPU Supported in Integration: %s\n
Flash Size 0x%X KB\n
Hang Address: 0x%016llx\n
Unable to create pthread key for conenction. errno=%d %s.
{%s} checking for single_port probe daemon on port %d
end rev is not of expected format; skipping cpu_desc override\n
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
{%s} NOMEM
Could Not Find a DCM Portal
Could Not Find Any Loaded Boosters of Type: %s\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
[MEM] Uncompleted; DSCR = %08x\n
{%s::%s} %s pre_resumed\n
Going To Create Generic ARMV8\n
Turning Debug Clock On
In Writeflash\n
Could Not Allocate All Boosters Array
Protocol Version: 0x%X\n
 MEM-AP %X is hung\n
{%s} Error setting up jtag-ap target (%s)
{%s::%s@%d [%s]} Error %s: initializing cache parameters
   DPv3 bus is %u bits wide\n
Flash Address Max 0x%llX\n
{%s} drain_packets=%d [%s]
Init dbgwrap obj failed
product-name: %s\n
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
[AstrisAsync] Async mode %s
{%s} 0 words from probe when %d words left to read for address 0x%016llX
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
Can't get OS build version - failed to create URL
Connected to Probe Map Server
JsonLogger: Writing category '%.*s' to '%s'
Match Count is Zero. This is invalid.
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
CPU ASC Offset: %d\n
[SSTEP] bvr=%08x bcr=%08x\n
We are Deallocating\n
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
In Postflash\n
[1500] Error parsing TAP description
{%s} wrote %d words to probe when %d words provided in request
{%s@%d} Failed to send probe command (error %d).
Programming (addr: 0x%08llX) Failed!!!
There is no debug port associated with this chip.
DEMCR: 0x%08X -> 0x%08X
Booster System Is Not Initialized Bailing\n
{%s} _pre_halt_hw result = %s
{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s} Debug Base: %08X
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
Unable to allocate memory for next part of big response
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
{%s} timed out waiting for cpu to halt during collect
{%s} empty response string provided
\tAstris does not support page-erase beyond first %d KB of flash.\n
[KIS] Register Read/Write/Wrote: %d\n
[1500] TAP key is not a valid integer
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
Hang Description:\n%s\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
no debug bus AP present when expected
Gateway Version: 0x%X\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
[Auth Debug] Disabled\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Required Key-Value is a string, and not an array. Old booster found\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
Min Component - %s\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
[%s] cop %d -> 0x%08x\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
Koko probe, for now I guess we will just say yes...\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
DBGCTRL = %08X   res=%d\n
CPU has no regions, maybe powered off?\n
{%s} 0 words requested for read at address 0x%016llX
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
We are done with clean up\n
Passed NULL plist file\n
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
{%s} flags:0x%08x
{%s} unmodified-probe_match = %s
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Got an error reading the DCM Control Register: %s
%s
DBG_CPU: %s\n
{%s::%s} read OK but took %d tries
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Connected to Probe Device Server [Log File %s]
{%s} %s: |%s|
\t[MATCH_FOUND] identified chip: %s
Bundle: %s NOT FOUND\n
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Could Not Allocate Mutable Dictionary For BoosterMangers
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
{%s} Failed to get watchpoint mask for %s: %s
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
{%s@%d} Probe response payload read when no payload indicated.
CPU state %d
Failed to allocate space for table!
Found an async abort pending; clearing it\n
Error status from AMAuthInstallSsoEnablePtr = %i
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
%-16s @ 0x%08llX : 0x%08X\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
Unable to read FP
[REM_HWBP] bp%d\n
Flash Reg Adress is not set, using what is there\n
kext connect name %s\n
CPU DBG Ack: 0x%llx\n
Stop Clock: %s\n
VBAR: %#x\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
Failed to access new_cpu status
   JEDEC ID: 0x%08X\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
In Preflash\n
{%s::%s} NULL parameter
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
Unable to read GPR %d
Failed to read register to figure out flash address %s\n
Can't get hardware model - failed to allocate data string
sent %zd bytes to Probe Map Server when sending %zu
Modified Word To Write: 0x%08x
[AstrisAsync] astris_async_override_disable_async: conn is NULL
Failed explore before forced KIS reset: %s\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
chip is 0??\n
ERROR!! Couldn't save %s binary data\n
{%s:%s@%d} Critical error encountered:
Full JSON that failed validation:\n%s
[1500] IR command '%s' missing required field 'opcode'
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
[HALTED] dfsr = 0x%08x\n
Previous authentication in-flight, wait for it to finish\n
Couldnt figure out the size of flash, defaulting to 1MB\n
Probe %s with unknown kick response %s
%d KB flash size detected.\n
AXconn_t Struct Is NULL
Gathered Value is Not Number\n
replay_counter=%lu
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
## dpw 0x%02X failed (%s)\n
Invalid character [0x%02X] received from Probe Map Server
CPU AP-Select: %d\n
Found the RTXCID Structure!\n
[%s] {%s->%s} Transitioning to exception level %u.\n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
Creating CPU Returned: %s\n
Asked To Write To A Negative Register Index
{%s} Failed to extract IDCODE from table (%d); continuing anyway
{%s::%s} ITE is not set: 0x%X\n
[AstrisAsync] Got ASYNC_RESTART response!
[AstrisAsync] replay preflight: Async not active!\n
   JTAG-AP: Identification = %08X\n
{%s} bridge timed out
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
using standard products.plist for %s
{%s} [%s] m_exception_level=%u\n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
[ARM64 INS_WP] 0x%016llx x %d\n
Unable to read PC
Start Address=0x%08llX....End Address=0x%08llX
Failed to find a plist for this soc %s
Table Size: %d\n
astris_get_async_ver failed with error: %s
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
SOC AP[%d]: JTAG_AP\n
SWDACKDELAY relay write failed\n
{%s} connectName[%s]
Dart Coastguarded CPU: %s\n
!!!! CPU Key %s is INVALID !!!!\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
AP[%d]: MEM_AP_AHB\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
{%s=>%s} AXconn_t has more than one chip
Error %d (%s) opening history save file
Initialized Logging - %s
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
Invalid file name: \"%s\". File names must be at least %d characters long.
ERROR!! write binary data parameters invalid\n
Probe Map comm error %d(%s) %s
{%s}#%02X cmd: %s, resp: %s
KIS Writevals putting back the value
!!!! FILE RADAR: Don't know how to compare two values\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
[PREFS] Key: %s - Val: %s
\tCould not read the flash size. Using default 1MB size.\n
Xtensa Option dbg_intr_level: %d
{%s:%s@%d} Critical error [radar already requested]
Switch to primate res: %s\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Old ProbeDaemon does not support this command
Complex ID: %d\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
   {%s} (DP): status=0x%X(%s) - %s\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s} probe_port = %d
Connect using RSD not supported\n
{%s@%d} Timeout while attempting connect to server
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
[1500] TAP %d missing required field 'chip-index' or 'irlen'
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} (end) current_el is now %d
   Debug Port has unknown type\n
Error - STM32%s reflash failed (%s).\n
JsonLogger: Schema loaded successfully for category '%.*s'
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s::%s} HDE not set on %s. Will re-enable.
## apw %u 0x%08X 0x%08X ...(%d)\n
Original Length: %d\n
OS build version: %s
Unable to register assert upcall %s (Insufficient memory)
Probe %s removed during selection process
{%s@%d} socket connection is not available
\tWhole chip...\n
STM_FLASH_OBR: 0x%x\n
relay_set: %s = CMD_ERR (%s)
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
Error while trying to authorize: %d - %s\n
Flash Size %d KB\n
Can't get hardware model - failed to allocate data buffer
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
Failed to create Xtensa CPU %s \n
coalesced-target: %s\n
Start Page: %d\n
[%s] {%s->%s} clear async abort
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
=== Loaded %s Boosters ===\n
Complex CPM Offset: 0x%llX\n
SoC must have a DAP
SoC BM Not Found, Bailing\n
Initialized %d 1500 bridges\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
error %s reading DAP MMFR0
{%s} read ESR EL1|EL2|EL3 (%d)
   {%s} Before powerup CMDSTAT=%08X\n
\t%4X: %8X %8X\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
Banana split probe, for now I guess we will just say yes...\n
{%s} invalid data width %d bytes
collect_responses
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
replay_counter=%lu, last_replay=%d
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Complex Address: 0x%llX\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
     0x%016llx: 0x%04x      %s\n
Failed to sync prefs at beginning
probing %s status\n
Dumping Process Tree
Probe %s status: Busy
AXjtag_srst assert failure - %s (%d)
Dart Name: %s\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
{%s} ROMTABLE (dbgbase=0x%llx)
Failed to convert kisLoc %s to unsigned long long
no system bus AP present with AHB, trying AHB5
[%s] EL @ end of Collect: %d\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
AXmemap_readvals failure - %s
Could not find bundle () in given array: %s\n
CPU AP-Type: %d\n
{%s} Failed to extract PID from table (%d); continuing anyway
Debug Base: 0x%llX\n
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
Unable to read LR
[INSWP] 0x%08llx wp%d rdwr=%X\n
Debug Clock Already Enabled
Cleaning up Main Booster Object\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
Raising to EL2 cause in Guest\n
runBlock
## apr %u 0x%08X %d -> 0x%08X ...\n
New Length: %d\n
=== Starting Gather and Clear ===
Adding new booster path: %s\n
CPU Supported in Runtime: %s\n
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s} Thread %#llx clearing key %lu
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
STM_FLASH_SR: 0x%x\n
relay_get: %s = CMD_ERR (%s)
No 1500 bridges specified\n
haskis bit not set\n
[1500] Error parsing bridge '%s': missing required field 'select'
New format for cip gen register, unsupported: %d\n
{%s::%s@%d [%s]} Error %s: resuming HW
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
Result while reading first entry: %s , entry val 0: 0x%X\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
No 1500 bridges or TAPs specified (v2 plist)\n
Could Not Find Any Boosters\n
STM_FLASH_CR: 0x%x\n
[ANAMOLY] Could not find AXcpu_t object for CPU\n
KIS Preflight No Need To Write to AP CSW
Failed to find a product plist for this soc %s
After Programming (addr: 0x%08llX) Programming Error is Set: 0x%08X
Failed to convert primateHubLoc %s to unsigned long long
start rev is not of expected format; skipping cpu_desc override\n
{%s::%s} creating CPU
{%s} bridge returned SLVERR
%-16s @ 0x%08llX : read failed\n
[DCC] Grabbing DTR failed: %s\n\n
Successfully Authenticated\n
Unsupported device identification 0x%03X\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Astris Version Set: %s
Awaiting next chunk of big response
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
Translate Stage Chosen: %d\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Probe %s USB-C location is %s
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
{%s} FIFO full, try again
Cleaning up Each Booster Manager\n
Values Not The Type We Expected. Expected: Number and String\n
Value Types Are Not Strings\n
{%s::%s} ERROR %d(%s) resuming %s\n
{%s->%s} ERROR=%d(%s)
{%s::%s} [%s] error %s writing SCTLR_ELx
## armcpu: success status even though not all bytes written\n
unable to obtain sysap
Got an error writing 0x%X the DCM Control Register: %s
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
Failed to Identify & Explore Chip via KIS: %d (%s)\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
=== Ending Gather and Clear ===
write to CMD/STAT failed - %s
In Readflash\n
[%s] TGE is set so we traping to EL2\n
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
Result while reading second entry: %s , entry val 1: 0x%X\n
{%s} DEVARCH read fail in CoreSight component (%s)
Subsystem Monitor[%i]: %s\n
\tWriting @ 0x%08llX...\n
Initializing Booster Layer\n
[AstrisAsync] Barrier hit!\n
{%s} read %d words from probe when %d words requested
## memapw %u 0x%016llX 0x%08X\n
X00 Part
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
AXmemap_stmflash calling STM32F4xx::reflash(0x40023C00)\n
Set custom PSD json file: %s
--> misc_wdr   size=%3d wirtestporten=%d
CPU at Index: %d has to specify only one AP Type or AP Select\n
[1500] v2 plist missing required field 'taps'
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
CPU: %s halting debug is now %s\n
Going to do imago workaround\n
Production Fused Device\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00,single)\n
CPU Address: 0x%llX\n
Failed to get DFU Type
   Debug Port: SELECT %X: SKIPPING (%s)\n
** Unauthorized User/Network or ECID **\n
Issuing request to Probe Map Server: %s
Form-factor specific channel not found, falling back to generic channel for device '%s'
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s@%d [%s]} Error %s: checking exception
pc:  0x%16s cpsr: 0x%16s %s\n
{%s} %s status is '%s' [Status Read %d times]\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
{%s@%d} Received %d bytes when requested %d bytes [%s].
End of Operation Bit Is Set - %s
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
\tbut is not guaranteed on this device.\n
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s::%s@%d [%s]} Error %s: flushing HW state
Invalid current AP (%d), adopting APTABLE (%d)
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
Couldnt figure out the size of flash (we read: %d), using default\n
{%s[select]} %d(%s) [RETRYING]
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Failed to sync prefs at end
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
{%s} DAP command nwords=%d trimmed to %lu\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
[Auth Debug] External Debug Interfaces Open\n
Flash Sector Max %d\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
{%s} host = %s
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
SOC_t::{%s} CPU_t group=%d when group 0 expected
Too many portals, we are at portal: %d while max is %d\n
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s@%d} Unknown CS code [%u]
No version information found in booster: %s
Could Not Allocate Info Keys Array
!!!! Complex Key %s is INVALID !!!!\n
Breakpoint Address: 0x%llx
Wrong width, should be either 4 or 8\n
Fabric access is blocked. Expected if production unit, won't explore further.
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Can't get hardware model - failed to convert to C string
Die Addr Info LSB: %d Mask: 0x%016llX\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
\tCould not get sector number for address: 0x%llX\n
{%s@%d} Drain empty on decr [%s].
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
Invalid Bundle: %s
AP[%d]: unknown type\n
connection about to be destroyed
JsonLogger: Loading schema for category '%.*s' from '%s'
Dart CPU SID(s): %s\n
Failed to convert %s key @ index %d to a number with base of %d\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s::%s} [%s] MMU is already active - returning %s
## armcpu: bad status even though all bytes written (%d)\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
Booster Info:\n%s
Complex CPU Name: %s\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
\t\tARMv6 debug CPU xxx ID\n
Exploring IDE in JTAG\n
{%s@%d} IOServiceClose failed, err = 0x%08x
Booster:\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
[AstrisAsync] Discarding response due to ASYNCSKIP state!
[AstrisAsync] Pause when already paused!\n
%s probe[%s] from Probe Map Server [%s]
Probe Map comm: request[%s], response[%s]
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
[ARM32cpu_t::_read_register64] 0x%08x\n
error trying to unlock MSR %s
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
Optional Key: CPUMonitor not in preferences
Programming STM32Lxxx...\n
Using Built In SoCs\n
!!!! Complex CPU Key %s is INVALID !!!!\n
   Debug Port: Trying SELECT %X\n
Error %d (%s) opening cmd snapshost save file
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Successfully connected to server, %s:%d
We are in clean up\n
Could Not Get BoosterManager\n
%s Bridge @ 0x%09llx-0x%09llx: %s
USER %s(%04u): %s(): %s
   {%s} Enabling debug unit\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
{%s} host name(RSD): %s\n
%s SoC created
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
Failed AP read of R_MEMAP_CSW res: %i
{%s} no chip found
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
Failed To Instantiate SOC From Booster\n
sending abort to clear a timeout\n
Gathered:\n
[1500] Error parsing bridge: %s
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
codeblock
Length is 0
PKA Base: 0x%llX\n
Asked To Read A Negative Register Index
TAP IDCODE: 0x%X\n
{%s} pmgr status=%d being reported as Unknown
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
Successfully Authenticated DFT\n
STM32Fxxx flash programming status fault: 0x%08X\n
%s construction failed
Xtensa Option options: 0x%x
--> 0x%02x = %s
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
ERROR: unable to suspend translation for %s
Failed to instantiate %s\n
Chip Revision: 0x%X\n
error %s checking for data abort
{%s::%s@%d [%s]} Error %s: collecting HW
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
\tFailure: status errors: 0x%08X\n
Error closing %s [%d]
{%s} probe [%s] added to list
{%s@%d} Received %d bytes when requested %d bytes.
{%s} no TAP detected that supports 1500
\tLeft To Read (%d) < width (%d).\n
   DPv3 baseptr is not valid (%X)\n
{%s@%d} Failed to find cached response
Failed to create CPU %s - %s\n
DEMCR read failure - %s (%d)
Write Failed: address=0x%08llX, length(in)=%lu, width=%d, length(out)=%d, result=%s\n
We are Allocating\n
AXmemap_stmflash calling STM32H7xx::eraseflash\n
{%s::%s} creating placeholder for CPU: name=%s
AXportal_t Struct Is NULL
Failed to convert CFString to C String.
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
Async is disabled for current seesion
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
Using KIS-STM to flash, on some parts we might be too fast for this using KIS-STM
\t Bank %u Sector %u...\n
Error - eraseflash failed.\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Width: %d not supported
!*!*!* ****************************************************************************** !*!*!*
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
{%s} error %s at line %d
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s@%d [%s]} Error %s: synchronizing context
Buffer is NULL
## apr %u 0x%08X -> 0x%08X\n
      Select of JTAG-AP port %u failed with %s\n
\tReading left over chunk expected 0x%x got 0x%x\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
{%s@%d} Timeout while sending probe command.
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
** CPU %s requires forced explore override flag on this SoC **\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
Sending DYN Bypas Channel Set: %d
   Debug Port: SELECT %X; error: %s, retrying..\n
{%s} ROMTABLE (nest=%d)\n
TatsuServer Found: %s\n
SSO info present but SSO disabled.
JsonLogger: Created with default schema version '%s'
WARNING: %d KB flash size detected.\n
ERR: conn->nchips != 0; looks like chip is explored\n
In Eraseflash\n
%s probe[%s] from Probe Map Server [local host]
Enabling USB Gateway
Failed To Initialize Logging\n
--> psr        size=%3d bit=%d
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s::%s} [%s] !bpwp_initted, retrying init
\t Sector %u failed: %s\n
\t Writing 0x%08llX failed: %s
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
\t Writing 0x%08llX...\n
%s\n
    INFO(%u,%d): %s(%04u): %s(): %s
{%s} L2 cache operation completed [%s]
outstanding=%zu
{%s} Failed to get breakpoint mask for %s: %s
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
## dpr 0x%02X failed (%s)\n
{%s} Failed to extract component info from table (%d); continuing anyway
error %s reading DAP PFR1
{%s} %s DC cache already clean since last halt, skipping flush
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
in stmflash api\n
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
Before astris_kis_init_dp, CMDSTAT=%08X\n
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
%s: not supported.\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
Invalid APTABLE (%d), so using most restrictive
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Unable to convert plist file name to CFString: %s\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
## dpw 0x%02X 0x%08X\n
   DPv3 BASEPTR0 is 0x%08X\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
[%s] chipinfo is NULL
{%s} Found extra info in = %s, chopping string
{%s} connectName[local host]
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s} %s status failed. error: %d (%s)
AP is NULL
{%s@%d} Unknown CS command error [%d]
Problematic JSON value:\n%s
[READ] %d -> 0x%08x\n
error %s reading DAP MPIDR
Flash unlocked...\n
unable to create connection
{%s} unaligned %d-byte access at address 0x%09llx
AXportal_t Is Not Valid Type - %d
[PAW] Failed KIS Portal Access Preflight =%s (%d)
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
{%s->%s} current EL (%d) already == target EL.\n
Using Built In CPUs\n
AP Only Explore was asked for, stopping here
{%s} Error looking up architecture (%s)
2: ARM64_SYSOP_ATS12E1W\n
Could not enable KIS SoC Access\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Probe %s LocationID Info is %s
{%s@%d} Unable to connect to server, %s:%d
Size or Count provided are 0.
CPU Name: %s\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
SSO is DISABLED\n
STM_FLASH_AR: 0x%x\n
Groups %d\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
OK: address translation suspended for %s successfully
   CPUID: 0x%08X\n
[FLUSH]\n
{%s=>%s} null reference to AXchip_t[0]
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
[KIS] Register Index: %llu\n
CPU Typehint: %s\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
{%s::%s} EDSCR with TXU set - unable to recover.\n
\tLeft Over Chunk Read Failed\n
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
AuthDebug::authenticate_probe - no need to authenticate\n
[Auth Debug] Ticket Active, Debug Interface Locked\n
{%s} Unable to read CPSR
caller=%s, async=%d
## dpr 0x%02X -> 0x%08X\n
   Setting up AP IDR %08X\n
      Read of JTAG-AP port %u CSW failed with %s\n
** \tTatsu AuthDebug Triage | All     **\n
{%s} strsep empty so match any probe [localhost]
Probe %s with unknown port response %s
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Could Not Match A Booster for %s\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
{%s::%s} waiting for EDSCR ITE
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
Choose a device: 
relay_get: %s = ERR
Could not find TAP at chip-index %d for v2 1500 config\n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
[AsyncSnapshot] #%zu: %s\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
{%s@%d} Probe reported connection lost [PROBEEOF].
Not Creating CPU: %s\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
Explore: %u chip%s\n
{%s->%s} START handling exception
{%s->%s} (top) current_el=%d
1: ARM64_SYSOP_ATS12E1R\n
   Debug Port: SELECT %X: SKIPPING\n
Subsystem Monitor Key does not exists: %s\n
Connecting to server, %s:%d
{%s@%d} gethostbyname failed, error=%d (%s)
\t[MATCH_TARGETID] FAIL <= unable to find DP
error %s checking for data abort(first)
[%s] %d -> 0x%08x\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
iter=%lu
{%s} failed (%s)
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
checking if relay \"%s\" is valid
The debug port associated with this chip has not been explored.
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[REMWP] wp%d\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40022000)\n
Could Not Find Any Boosters of Type: %s\n
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} Reading base 0x%llx entry's component ID
\tTatsu AuthDebug Triage | All\n
no debug bus AP present when expected; after sysap is NULL
Setting STOP CLOCK to TRUE
  Nested path: parent='%s', child='%s'
Failed to get KIS translator version\n
[READ] cop64 %d -> 0x%016llx\n
Aligned Address: %llx
{%s} error: %s
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
STM_FLASH_OPTKEYR: 0x%x\n
{%s} unable to allocate probeInfo
{%s} drop ProbeName %s
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Probe %s removed prior to kick\n
[KIS] Address: 0x%llX\n
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Unaligned Read @ 0x%llx Width: %d Bytes: %d
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Previously dumped the process tree, skipping
{%s@%d} Connection to server rejected, error=%d (%s)
Booster Value is Not String\n
Highest EL: %d, -- Min Op EL: %d
   {%s} select %u port %u: %u chip%s\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
CPU state %d (stm_preflash)
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
pmu-name: %s\n
X06 Part
operandStack.GetSize() >= sizeof(Frag)
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
function
jtag_get_soc
ret.reg.write.K_DA_REG_NAME_AUTH_KEEP_DECISION
META
!!!! DART Key %s is INVALID !!!!\n
ret._a64cpu_raise_el_hw.el=2.to_read_hcr
{%s} handle ROM entry %d (level %u): %08x
RF18
Register file 18
fn._ocd_exec_instr.wsr.ddr.t1.1
No portal under found for that type
astris_kis_cfg_readvals_swd
Adding new booster path: %s\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
_memory_set_base
enable_timer_ovr
Apple Fabric Timeout
{%s} host:%s, flags:0x%08x
Error closing %s [%d]
[%s] %s
\t[MATCH_TARGETID] FAIL <= unable to find DP
cpu_lacc_count_insert
!!!! Critical Error: Thread %#llx key %lu relaxing attitude for %p when not attached - NOT ALLOWED !!!!\n
[%s] chipinfo is NULL
{%s:%s@%d} [%s] PECR write (erase) failed: %s\n
Probe %s removed before port determined\n
cpu_read_dcc
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
{%s->%s} [aarch64] exec: encode_mrs(%s=%d[%s], MDDTR_EL0, %d)\n
op_TIEInitiateReadProtectedI_encode
%s/Library/Logs/Astris
M
transact
irlen
{%s:%s@%d} [%s] executing MRC\n
setway_reg
\tFailure: region @ 0x%08llX failed to verify\n
CPU-level (general and architecture-specific)
TRST
      Select port %u: AVOIDED\n
Programming STM32%s...\n
LCOUNT
RF21
description
{%s:%s@%d} [%s] Writing FLASH_CR failed during lock sequence: %s\n\n
{%s:%s@%d} [%s] DEMCR read failed: %s\n
{%s:%s@%d} [%s] doing IR scan (DTRRX EXTEST)\n
cpu-xtensa-num-intr
address-size
ret._a64cpu_read_gpr_cached
Register file 45
SWDONLY
CLIDR
probe [port %u] on host %s
Invalid port[%s] for probe %s provided by probe server
{%s} empty response string provided
PushBack
complex-base-address
{%s:%s@%d} [%s] reading BCR %d\n
Table 5–152
MMID
Warn
file/object not found
{%s:%s@%d} [%s] updating CPSR\n
{%s:%s@%d} [%s] doing IR scan (DIDR INTEST)\n
astris_cpu_get_cl4_debug_signpost
cpu_clean_l2cache
GetStringLength
ret._a64cpu_write_sysreg_hw
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
VectorCatch
PROBETIMEOUT WHILE WRITTING\n
ret.clear_authentication
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
Kick off the current process using probe %s? (y|n)\n
ARMV4
Protocol Version: 0x%X\n
_read_special_reg
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
virtual_memory_bytes
vers_gateway < 2
{%s} (end) current_el is now %d
{%s} Failed to get breakpoint count for %s: %s
HTTP transaction running in background
Skipped due to error in Async batch
code
Complex CPU ID: %d\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
uri.h
failed write of 0x%08X to DEMCR - %s
Ticket Data is NULL\n
{%s:%s@%d} [%s] Cannot initialize flash for erasure: %s\n
Failed to get KIS translator version\n
Invalid Bundle: %s
param.cpu==NULL
param.reg_name.invalid.null
{%s:%s@%d} [%s] executing MOV (diff mode)\n
_tie_read_word32
IsArray()
Terminate parsing due to Handler error.
ParseArray
cpu-apselect
astris_ide_get_bootid
Update
ret.generate_nonce_and_send_request
AXbreadcrumbs_clear
ParseStringToStream
AXexplore_set_explicit_mode
CortexM33
JsonLogger: Loading schema for category '%.*s' from '%s'
Waiting for flash to idle before page erase, failed\n
ret.memap.write
CPU[%s] Read Reg: %d
MESAVE
Unable to connect to %s - %s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
check_for_flash_error
{%s:%s@%d} [%s] \tCould not unlock flash\n\n
Enabling USB Gateway
_update_register64
DebugAuth
failed to create log dump file
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
data_.o.size > 0
_D
Initial DSPSR_EL0: 0x%llx
Reading FLASH_CR1 failed during unlock sequence\n
TARGETSEL
Sending DYN Bypas Channel Set: %d
{%s:%s@%d} Nested exceptions... get someone to debug this.\n
MESR
!!!! Critical Error: Error %d(%s) deleting info %p batch_attitude_key !!!!\n
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
ESR_EL1
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
%02u:%02u:%02u:%06u|%s <%s> %s
astris_json_logger_delete_all
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
Interrupt enable bits
Creating CPU With Name: %s\n
DISPSEC
Section 1 Offset: 0x%llX\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
AXdp_write_with_recovery
Register file 36
{%s} already connected
Connect using RSD not supported\n
{%s:%s@%d} [%s] \t Erasing Page %d failed: %s\n\n
Logging Context Is NULL\n
astris_command_lock
[SSTEP] using BP %d\n
ELR_EL2
{%s::%s} EDSCR with RXO set - unable to recover.\n
_a64cpu_el_fault_reg_latch
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
CPU
Complex Type: %s\n
M4F
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
      AXap_write of R_JTAGAP_PSTA failed with error %s
Vector Base
Register file 41
bp_index=%d
ret.restoring_el_after_raising_to_read_hcr
SSO with no prompt being used
EPC2
fn._read_special_reg.icountlevel
#ch-
Failed to init from cpu desc armv7m cpu: %s \n
logger already initialized
RdProt
BoosterManager.SOC
CPS
unswitch_regset
{%s} Unable to read SP_EL0
ASTRIS_ERR_NOTSUPPORTED
KIS-SIM
MODE
DBGWRAP_PAUTH
_a64cpu_write_aarch64_sp_hw
ret.exec.drps
ARMV7M
writeToFile
%s at offset %zu
fn.missing_booster_init_api
instruction=0x%llx
{%s=>%s} AXconn_t has no SoC object
{%s:%s@%d} [%s] End of Operation Check Failed, After Mass Erase\n\n
%s: chip was NULL when attempting to release soc
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
--> 0x%02x = %s
Tiny-Core
astris_ide_get_from_chip
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
astris_dpread
{%s:%s@%d} [%s] FLASH_CR PG write failed: %s\n
Table 5–161
AXconn_t Struct Is NULL
%s constructed
{%s::%s} cpu powered off: failed init() %s
AXcpu_nmi
Trying to use size of 8 on not AXI bus
var.reg_srn.invalid.>=256
op_XSR_encode
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - ADDRESS=0x%llX
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/logging/astris_except_classes.cpp
param.info.invalid.null
TRANSLATION_ERR_L1
ARMV7EM
Dart Base Address: 0x%llX\n
GPR_1
dest_gpr <= 15
Error - STM32%s reflash failed (%s).\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40023C00)\n
fn._ocd_reg_r.dsr.2
Hang Description:\n%s\n
Get
haskis bit not set\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
ret.init_params.raise_to_min
ASYNC
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
MAX_KISSWD
{%s->%s} [!aarch64] exec: encode_mrs(%s=%d[%s], MDDTRRX_EL0, %d)\n
AXdebug_auth_get_timer_count
ASTRIS_ERR_EMPTY
ASTRIS_ERR_PROBETIMEOUT
astris_soc_release
required
reset-network
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
{%s:%s@%d} [%s] Writing START in FLASH_CR failed during page erase: %s\n\n
RF62
init_astris_api
!!!! CPU Key %s is INVALID !!!!\n
{%s:%s@%d} [%s] reading GPR 0\n
{%s::%s@%d} [FALSE] postinc[%d] < MAX_IMM\n
{%s} Component ID read fail on romtable (%s)
FLASH_OBR
Error - STM32Fxxx reflash failed (%s).\n
Table 5–170
tc1500
error %s reading DAP MMFR0
EXPLORE_DAPONLY
get_ecid
DEBUGCAUSE
Register file 47
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
%s %s
Sprocket probe, for now I guess we will just say yes...\n
Master BoosterManager
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
Error status from AMAuthInstallSsoEnablePtr = %i
\tWriting @ 0x%08llX...\n
special reg. number %u not present
cleanup
ret.get_hang_crumb
_resume_hw
fn._return_from_debug_interrupt
fn._ocd_reg_r.ddr
document.h
/usr/local/share/astris/schemas
AXbooster_refresh
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s:%s@%d} [%s] setting GPR\n
EDBVR0+index
symbol.check.loaded.AMAuthInstallSsoSetAppleConnectInfoPtr == NULL
{%s:%s@%d} [%s] FLASH_CR sz write failed: %s\n
General register 4
addMember
AXbooster_print_all_booster_managers
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
{%s:%s@%d} [%s] Writing MER in FLASH_CR failed during mass erase: %s\n\n
PROBED_ERROR
exploreCPU
Failed to allocate JSON string
Call-window start bits
Can't get OS build version - failed to get build version
Low level
encodings.h
Device name is required
{%s::%s} [%s] error %s reading SCTLR_ELx
defaults.create.key.outofmem
DEDICATED
Parent key is not an object
chip->ide_table == NULL
ret.ite.read.edscr
(instr & ARM64_MSR_MRS_BASE_MASK) == 0
W
[CLEANUP]\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
Single_port connection to probe server unavailable
SPI
 
Got an error reading the DCM Control Register: %s
RegionEnd
AXdebug_auth_enable_test
astris_command
debug-size
arch_hw=%d
{%s:%s@%d} Critical error [radar already requested]
internal.is_dft_authenticated.chip->soc == NULL
xtensa-non-tie-range-size
ret.getSubsystemEnableStatus
AMAuthInstallSsoSetAppleConnectInfo
\t Sector %u...\n
Xtensa Option reg_file_size: %d
Probe %s removed prior to kick\n
prettywriter.h
kis_stm_name %s %d
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
framework_url == NULL
fn.__ocd_reg_w.ddr
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
{%s} m_exception_level(%d) != current_el(%d)
HardwareBreak
INFO
Setting CPU %s is_boot_core to %d\n
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
using multi-target booster products_%s.plist
couldn't read TTBR1
## memapr %u 0x%016llX -> 0x%08X\n
Unknown Subcommand
{%s@%d} Connection to server failed, error=%d (%s)
Append
ret.cfg_write(R_DCM_GPIO)
development
## apw %u 0x%08X 0x%08X ...(%d)\n
*
KIS translator version : %d\n
VERSION
{%s::%s@%d} [FALSE] base_reg[%d] < 15\n
M23
astris_setup_placeholder
{%s} DEVARCH read fail in CoreSight component (%s)
s
swdackdelay
AstrisSWD
cpu_writemem
Gathered Value is Not Number\n
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
fn._read_general_reg
Connected to Probe Device Server [Log File %s]
environment variable not found
Idle
AXconn_conndesc
cpu_collect
coredump_diagnostic
STM32G0B1xx
Erasing...\n
astris_addr_which_die
Error occured during nonce command
options=0x%8.8X, #addr_bp=%u, #data_bp=%u,deb_int_lvl=%u
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
ret.cfg_write(R_DCM_GPIO).deassert
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
Failed to sync prefs at beginning
astris_command_base
\n
astris_write_hang_crumb
ret.test1
{%s:%s@%d} [%s] writing CSSELR\n
ret.storePairForPref
   ROM entry %d (level %u): AVOIDED\n
Register file 22
fn._resume
sr=%u,ar=%u,opcode=0x%6.6X
is.Peek() == 't'
{%s:%s@%d} [%s] flushing state\n
SPSR_EL3
internal.authenticate_probe.debug_auth == NULL
ASTRIS_ERR_CPUHALTED
XACT
probe matching %s on host %s
{%s} connectName[%s]
pc:  0x%16s cpsr: 0x%16s %s\n
connection not currently open
psr-size
%d > %d
_log_setup_thread_specific
CPU is not halted
backtrace
booster
APCIE
fn._ocd_reg_r.DCR
AXI-ERROR=0x%X - AXI-XACTION-FLAG=0x%X - ADDRESS=0x%llX
passed
path
ASC_TCORE_ROM
full word
{%s:%s@%d} [%s] busy timeout on open: %s\n
COMPARE2
Table 5–153
_read_general_reg_by_name
_ocd_reg_dsr_r
{%s:%s@%d} [%s] reading DFAR\n
RXO
n't
param.reg_name.invalid.<0
PROBED_USB_REQ_ERROR
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
fn._ocd_reg_dcr_clr.dcr_enable_ocd
{%s:%s@%d} [%s] doing JTAG scan (DSCR)\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
New Length: %d\n
internal.get-timer-count.debut_auth == NULL
{%s@%d} Connection to server rejected, error=%d (%s)
BADCODE
pointer.IsValid()
boot-core
Die Config Disabled
{%s:%s@%d} !(prsr[0x%08X] & DLK)\n
Failed to exec DCPS in order to move EL up to %d
Reset
INVALID KIS VERSION
Table 5–167
fn._ocd_exec_instr.rsr.ddr.r0_r12
span
Wake
{%s:%s@%d} [%s] Cannot obtain the (alternate) device identification\n
fn._ocd_reg_r.ddr.value
fn.stmflash.h7.eraseflash.sector_erase
Unknown kick response[%s] (for probe %s) from probe server
{%s::%s} creating CPU
line
ret.rx-full.mddtr
INTENABLE
Setting bypass channel to: %d\n
coalesced-target
{%s::%s} halting %s\n
CTI_CH_PULSE
{%s::%s} read OK but took %d tries
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
fn.stmflash.h7.program.writevals
1970-01-01T00:00:00Z
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
_resume_translation_hw
AuthDbg,Nonce
Table 5–184
cpu_halt
\tAstris does not support page-erase beyond first %d KB of flash.\n
KIS Writevals putting back the value
wir-dpcsoc
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
AXconn_destroy
Logger is null
AXcpu_status_asc
{%s:%s@%d} [%s] PECR read (prog) failed: %s\n
\tFailure: status errors: 0x%08X\n
fn._write_special_reg.dbreaka0.address
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
u64toa
Could Not Get BoosterManager. Need To Call AXbooster_init\n
EDDTRRX
defaults.board.not_connected
AXjtag_settck
Table 5–160
var.devid.INVALID
RESPONSE_NO_PAYLOAD
ESR_EL2
{%s} skipping dcache flush, cache already clean
   JEDEC ID: 0x%08X\n
reg.ocd.dsr.stopped.invalid.cpu_running
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s:%s@%d} [%s] failed to read cfg reg: %d\n
xres = %p, table = %p, key = %d
## memapr %u 0x%016llX %d -> 0x%08X ...\n
AXdebug_auth_clear_dft_auth
op_WSR_encode
ASTRIS_ERR_STOPCLOCK
Portal Access Write
[1500] Error parsing bridge: %s
!!!! Critical Error: Error %d(%s) destroying info %p cmdmutex !!!!\n
Need to be connected to set nickname
AXcpu_writereg_vals
SOC AP[%d]: JTAG_AP\n
EXPLORE_JTAGONLY
_gen_debug_interrupt
AuthDbg,BoardID
Please run one of the following commands to collect a jebdump:\nFrom Astris Console: jebdump\nOR\nNew Astris Session: astris %s  --xpl aponly --script /dev/stdin {} <<< \"::astris::jebscantools::jebdump\"\nCreate a radar with the jebdump zi
SLEEPING
cpm-offset
DCS_BC6
Unknown number of groups in the explore table; can't parse group attributes
ASTRIS_ERR_USB_EXPIRED
postconnect
SETRELAY
SLEEPCTL
panic
{%s} [%s] EDSCR with ITO set - unable to recover.\n
ret.reg.read.K_PKA_REG_NAME_DBG_VERSION
Register file 25
timeout or watchdog expired
out of memory
%s on %s
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
(data_.f.flags & kUint64Flag) != 0
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
EXPLORE
Error %d(%s) executing instruction 0x%08X
AXcpu_hwwp_disable
{%s} Error reading PID (%s)
XSTAT
setTargetOS
0123456789abcdef
astris_kis_poll_cfg_reg
Memory error PC register
Register file 40
_set_single_step
preconnect
probe
get_soc_resource_filepath
_write_gpr
UNKNOWN_CS_CODE
kext connect name %s\n
{%s:%s@%d} [%s] reading GPR 1\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s:%s@%d} [%s] \tCould not erase flash\n\n
{%s::%s} ERROR %d(%s) resuming %s\n
DEMCR: 0x%08X -> 0x%08X
PARTNO_KIS
op_L8UI_encode
HOSTID=0x%x which is invalid, skipping orientation check
default_schema_version is NULL
mempool-size
DEBUG
AXcpu_getmode
Error %d (%s) opening history save file
Caught a portal that we dont have a status map for: %d
ASTRIS_ERR_INVALCOMMAND
{%s@%d} Timeout while sending probe command.
cpu-xtensa-dbg-intr
AXconn_get_pid_bid
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
Cause of last debug exception
val =0x%X is too large for 32 bit unsigned.
CPU state %d
DCS11
SUCCESS
AXcpu_halt
{%s} host = %s
(Last: %s) (%s)
xtensa-non-tie-range-name
astris_ide_get_soc_stop_clock
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
lower_el.el2.noimplemented
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
Problematic JSON value:\n%s
Writing PER and PNB in FLASH_CR failed during page erase\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
astris_setup_ap_mem
{%s} Debug Base: %08X
Successfully Authenticated DFT\n
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
AXcpu_mmu_walk
AP given is not a MEMAP
JTAG chain not yet explored
Data break 0 address
Required Key-Value is a string, and not an array. Old booster found: %s\n
Couldnt figure out the size of flash, defaulting to 1MB\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
(src_gpr & (0x40000000 | 0x80000000)) == 0
ret._mmu_init
OK: address translation suspended for %s successfully
symbol.check.loaded.AMAuthInstallSsoEnablePtr == NULL
FLASH_PDKEYR
LBEG
Beginning of set
DEMCR read failure - %s (%d)
{%s} exec: DC_CIVAC_X1_ENC\n
ban
Selecting
cpu_swbp_insert
stack.h
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
INTERRUPT
result.read_vals(portal_group)==
virtual int ARMv7cpu_t::_halt_hw()
_check_exception
_a64cpu_get_current_el_hw
No windowed register option.
Hang Address: 0x%016llx\n
{%s:%s@%d} [%s] getting GPR 1\n
UPDATE
GPR
fn._init_configuration.w2.audio.HIFI3_1
pnav_create_probelist
Could not find TAP at chip-index %d for v2 1500 config\n
expFrac <= 0
MemberCount
get
get_gpr
read memory
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
{%s:%s@%d} [%s] FLASH_WRPR3 write failed: %s (continuing)\n
fn.stmflash.h7.unlock_flash.write.cr1.key1
%02X 
cpu_cache_cleaninv
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
bool
%s-%06X
no debug bus AP present when expected; after sysap is NULL
## armcpu: bad status even though all bytes read (%d)\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Register file 35
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
component group %d\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
AP Only Explore was asked for, stopping here
{%s:%s@%d} [%s] timeout waiting for R1RDY\n
{%s:%s@%d} [%s] busy timeout after open: %s\n
Register file 62
complex-type
chip == NULL
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
Table 5–156
AXI Error
{%s@%d} Failed to send probe command (error %d).
Could Not Find Any Boosters\n
[ARM32cpu_t::_read_register64] 0x%08x\n
AXarm7_dbgscan
{%s} Unrecognized Component: %08X (class %u)
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
ASTRIS_ERR_MASKERR
In Preflash\n
ERROR
[1500] TAP %d: irlen must be > 0 (got %d)
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
copyBoardNameForPrimate
astris_setup_jtagap_target
{%s:%s@%d} [%s] busy timeout on unlock (out): %s\n
Hang Radar Info:\n%s\n
DBGSTATUS = %08X   res=%d\n
Preferences does not exists: %s, creating one.\n
{%s:%s@%d} [%s] Waiting for flash to idle before page erase, failed\n\n
connected-listing
Toto
Not Creating CPU: %s\n
allocator_
Failed to read transfer register (EDDTRTX)
NONE
## dpr 0x%02X failed (%s)\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
{%s:%s@%d} [%s] FLASH_PRGKEYR write (second) failed: %s\n
{%s:%s@%d} [%s] \tFailure: only %u of %u write transfers were done\n\n
_write_mem
fn._clear_portal_status
Turning Debug Clock On
param.dbgap  == NULL
Found form-factor specific channel %u for device '%s'
astris_ide_get_revision
FLASH_WRPR1AR
RF17
ASTRIS_ERR_NOTFOUND
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_components.cpp
[KIS] CMD: %s \n
AXconn_copy_nickname
time out reported by probe
CPU AP-Type: %d\n
RMX
result.init==
write.sysreg.el_check
AMAuthInstallGetLocalizedStatusString
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
STM32G0A1xxx
Failed To Init Booster's Astris API In: %s with %s (%d)\n
result.dbgap==NULL
ret.modify.edscr.~ma
enabled
   Setting up AP IDR %08X\n
Wat!: 0x%llx
ret.raise_el.read
operator()
Async is disabled for current seesion
probe %s on host %s
Awaiting response from Probe Map Server
CPU3
GetCachedPowerByIndex
tdi-wsi
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
EXCSAVE2
M2
v%s.%s
{%s:%s@%d} [%s] unable to drain response\n
virtual int ARMv6cpu_t::_resume_hw(bool)
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
ApSecurityMode
Connection aborted: kick required for probe %s.  Received eof in stdin
quiesce
cpu-explore-flag
{%s::%s} failed: %s
HardwareWatch
{%s} probe_match = %s
KobaSWD
End of Operation Bit Is Set - %s
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_REGID_MASK < NUM_ENCODINGS\n
EXPLORE_WITH_DISPLAY
par
{%s::%s} creating AP slave: name=%s
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
_get_bpcr_hw
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
param.invalid.reg_file_index.outofrange
Write Data Length Mismatch
ASTRIS_ERR_USB_EMPTY
\t Bank %u Sector %u...\n
Unknown error.
sso_user.sso_data == NULL
User
No probes were found matching
Cannot create CPU descriptions from NULL info\n
astris_arm64cpu.cpp
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
Failed to instantiate %s\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
ret.reg.write.K_DA_REG_NAME_ENABLE_PKA_VALID
_ocd_reg_dcr_set
** CPU %s requires forced explore override flag on this SoC **\n
{%s::%s} write OK but took %d tries
{%s} L2 cache operation completed [%s]
Original Length: %d\n
Successfully Authenticated\n
Register file 32
param.num_data_bp_regs.invalid.1
\n!!!!!!!!!! Error: %d (%s) opening log file %s !!!!!!!!!!\n
AuthDebugUseSSO
specified CPU is not available
parse_soc_info_from_booster
.success
%s status transitioned: %d ('%s') -> %d ('%s')\n
RF9
fn.stmflash.h7.wait_bank_flash_idle.read.sr_reg
connecting to selected probe
AXcpu_mmu_get_page_shift
RF0
.chip_id
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
{%s} Extracted CIP Gen Number from table  (%d)
ret.test.2.0
instruction size too large
load_framework
R15
_ocd_reg_dsr_clear_and_validate
End of set
DCM
param.portal_base == 0
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
Kick required to connect: Busy probe
%s:
cpu_hwbp_info
COMMIT
ASTRIS_ERR_ISCONN
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
PAM
astris_remove_loaded_cpu_boosters
dspsr_el0
RF13
invalid host name or port
TCP send
rhs.IsString()
{%s:%s@%d} [%s] Programming failed: %s\n
{%s:%s@%d} [%s] wait_for_flash_idle (write-verify) failed: %s\n\n
fn._write_window_base.wb.wb_save
AXcpu_resume_translation
AMAuthInstallSetSigningServerURL
address=0x%8.8X, len=%u, rdwr=%d
read_resp_via_sock
Die-Count: %d Current-Die: %d Die-Type: %d
AuthDbg,ChipID
R0
memory_read
!!!! Complex CPU Key %s is INVALID !!!!\n
SCS
AXcpu_lacc_status_remove
[PREFS] Key: %s - Val: ??
_return_from_debug_interrupt
no DP (Debug Port)
Portal Group Offset: 0x%X Entries: %d\n
Aligned Address: %llx
astris_cpu_mmu_configure
Can't get hardware model - failed to create string
ASTRIS_ERR_OK
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
setTargetIdentifiers
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
KIS Timeout
{%s} checking for single_port probe daemon on port %d
kon
Already connected to
ret.clear.async
[HALT] Chip %x\n
Created Connection - : %s
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
Accept
far_el2
EXPLORE_GENTLY
Register file 38
fastsimSWD
nameBuffer_ == 0
Size
AXbooster_interface_init_astris_api
BoosterManager Types:\n
astris_ba_uses_attitude
{%s:%s@%d} [%s] executing MSR (switched)\n
_sw_breakpoint_remove
Corruption detected selecting probe from probe server
quit
cpu_lacc_pipe
Cannot create DART descriptions from NULL info\n
ret.ito.clear_edscr_err
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
_read_general_reg
Invalid object or key for engineer array
PushUnsafe
AXdisassemble_at_addr
CPU AP-Select: %d\n
astris_dump_exploreflags
fn._ocd_enable.true
_%04d-%02d-%02d_%02d.%02d.%02d
relay_get: %s = CMD_ERR (%s)
Incorrect hex digit after \\u escape in string.
[%s] error  reading EDSCR
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
ocd_base_address = 0x%8.8X is not 4 KByte aligned
config.invalid.no_window_reg_option
Temporary level
dtoa
/socs
EL1t
M7
CPU[%s] Write Reg: %d Val: 0x%llx
PowerOff
{%s} Reading base 0x%llx entry's component ID
sso_user.sso_user == NULL
fn._ocd_reg_dcr_set.debug_interrupt_msk
We Are Matching Development Booster\n
cpu is NULL
probe %s on localhost
cpu_hwwp_info
read-back (sys AP) did not contain SW BP instruction
SCAN
[%s] EL @ end of Collect: %d\n
SSO info present but SSO disabled.
RF36
RF45
_read_gpr
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
/System/Library/CoreServices/SystemVersion.plist
read
localwrstn-size
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
fn._read_pc
fn._ocd_reg_w.dcrclr.regval
Probe
{%s::%s} creating placeholder for CPU: name=%s
Going To Create Generic ARMV8\n
ret.auth.data == NULL
SETTHREAD
soc or sysap not available
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
EDPRSR_AON
got a translation error translating VA to PA
Failed AP write of R_MEMAP_CSW res: %i newval %i
too many of something
PAYLOAD_OVERFLOW
nullptr == file_path_cfstr
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
AXexplore_enable_cpu_pattern
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
SOC
Could Not Allocate Loaded Booster Array
ESR_EL3
Enabled
{%s} handle ROM entry
fn._ocd_reg_w.dcrset.regval
Long Packet
ASTRIS_ERR_OUTOFMEMORY
ret.state_valid_entry_exit
!!! Critical Error msr_cache[%d] IS NOT cached !!!
_a64cpu_read_aarch64_sp_hw
Register file 27
ASTRIS_ERR_BADPARAM
Probe Map Server Information: %s
NXP_RT117x
engineer
_write_internal
op_S8I_encode
Failed calling AppleSOC_t::switch_taps\n
_a64cpu_msr_mrs_encoding_for_sysreg_id
i8@?0
fn._write_window_base
fn._ocd_reg_r.dsr.regval_raw
REG
set.user
cpu-xtensa-non-tie-ranges
Literal base
ASTRIS_ERR_NOPORTAL
JTAG level control
ret.astris_soc_get_applesoc
KIS
targetid/instance must both be set or both be unset
{%s:%s@%d} [%s] executing MRS\n
astris_memap_bus_write
AuthDbg,SecurityMode
{%s:%s@%d} [%s] Writing page address to FLASH_AR failed during page erase: %s\n\n
fn._ocd_exec_instr.rsr.ddr.t1.1
hostid
AXbooster_print_loaded_boosters
far_el3
_a64cpu_lower_el_hw
failed to read memory; can't confirm breakpoint set
AXcpu_readmem
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
ASTRIS_ERR_ASYNC_BARRIER
Could Not Allocate Info Keys Array
dfu-type
{%s:%s@%d} [%s] writing GPR\n
!!!! Critical Error: el[%d] == m_exception_level[%d] !!!!\n
copyNicknameForPrimate
astris_preferences_cpu_monitor_list
DCCCTRL = %08X   res=%d\n
Type 'jebdump' to do scan/mem dump\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
DEPC
Too many address breakpoint regs (%u). Maximum is 2.
param.bp_index.invalid.outofrange
We are Deallocating\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
_a64cpu_read_edscr
EXPLORE_SET_MODE
{%s=>%s} AXconn_t has more than one chip
AXconn_port
reflash
Both debug and xbs versions are set, maybe a bug: %s
astris_ide_refresh_boardid
astris_get_die_count
_update_register32
FAR_EL1
   JTAG-AP: Identification = %08X\n
General register 13
SP
PARTNO_DAPLITE
Writing FLASH_CR1 failed during lock sequence\n
MEMAP_APB
[KIS] Register Read/Write/Wrote: %d\n
~HDE
{%s::%s} [%s] length=%u when width=%d
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
ret.spmi_read
symbol.check.loaded.AMAuthInstallApSetParametersPtr == NULL
Register file 5
IsObject()
dest_reg < 32 || dest_reg == 31
_a64cpu_assert_state_valid_entry_exit
select
_clean_invalidate_dcache_setway
read_page_descriptor
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
Flash Reg Adress is not set, using what is there\n
DIAGS
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
RF40
%s construction failed
fn._ocd_reg_w.ddr.wb_next_u32
{%s@%d} Timeout while attempting connect to server
NOP
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
internal.clear-auth.chip->soc == NULL
[%s] Booster System Is Not Initialized Bailing\n
{%s:%s@%d} [%s] writing DRCR\n
[ARM64 INS_WP] 0x%016llx x %d\n
EXPLORE_WITH_SEP_DEBUG
Data break 1 control
Table 5–150
astris_cpu_raise_el
AXcpu_collect
   Debug Port: Trying SELECT %X\n
AMAuthInstallSsoSetStealthMode
RF14
ASTRIS_ERR_WAIT
createSOC
[1500] run_steps: unknown instruction '%s'
param.booster_bundle==NULL
src_reg < 32 || src_reg == 31
EL3h
{%s:%s@%d} [%s] Waiting for flash to idle after starting mass erase, failed\n\n
at=%u,as=%u,offset=%u,opcode=0x%6.6X
createKey
[AstrisAsync] Discarding response due to ASYNCSKIP state!
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Register file 21
Probe %s Device Does Not Have LocationID
cpu_translate_with_dart
ret.cfg_read(R_DCM_GPIO)
AXdisassemble_at_phys_addr
CPU Supported in Integration: %s\n
[ARM64] exec(DCPSX_BASE_ENC)
Setting WP length not currently supported: %u
ret.write_reponse_and_check_authentication
Could not find portal by select %d, while interpreting result\n
general error reported by probe
Flash unlocked...(before erase)\n
CPU.ARM32
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
High level 4 exception PS
info
Min Component - %s\n
{%s} PRIMECELL [DONE]
_remove_watchpoint
required parameter is missing
Error %s opening single_port connection to probe server
check_dcc
_exec_recover
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
Register file 7
param.wb.invalid.>wb_max
!!!!!!!!!!   $ sudo chmod 0775 %s\n
Extract Offset: 0x%X for %d\n
```
