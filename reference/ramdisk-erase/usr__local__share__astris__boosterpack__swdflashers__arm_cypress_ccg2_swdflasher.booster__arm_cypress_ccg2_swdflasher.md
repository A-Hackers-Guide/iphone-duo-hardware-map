# `/usr/local/share/astris/boosterpack/swdflashers/arm_cypress_ccg2_swdflasher.booster/arm_cypress_ccg2_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,806,432 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = BUNDLE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 2952)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, HasTLVDescriptors
```

## Linked libraries (5)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (6,986)

First 2,500 of 6,986.
```
Failed to read IDE through DAP\n
probetimeout retrying access...\n
astris_romtable_pid Error: %s
no debug bus AP present when expected; after sysap is NULL
write to CMD/STAT failed - %s
!!!! Complex CPU Key %s is INVALID !!!!\n
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Can't find descriptor for group - can't index\n
Failed to access new_cpu status
[1500] Using %s.plist
[1500] v2 plist missing required field 'bridges'
Creating a 4200L Flasher to Acquire\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
{%s} probe [%s] added to list
\t%s\n
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
Failed to allocate space for table!
Failed AP read of R_MEMAP_CSW res: %i
[1500] Error parsing IR command: %s
{%s::%s} [%s] MMU is already active - returning %s
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
Invalid current AP (%d), adopting latest (%d)
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
[REM_WP] wp%d\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
\t\t%s\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
## armcpu: success status even though not all bytes written\n
sent %zd bytes to Probe Map Server when sending %zu
{%s::%s} creating AP slave: name=%s
CPU AP-Select: %d\n
      Select of JTAG-AP port %u failed with %s\n
{%s::%s} EDSCR with TXU set - unable to recover.\n
replay_counter=%lu
Creating CPU With Name: %s\n
DHCSR write failure - %s (%d)
astris_get_async_ver failed with error: %s
Got an error writing 0x%X the DCM Control Register: %s
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
error %s checking for data abort(first)
   {%s} Before powerup CMDSTAT=%08X\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
Creating a PSOC6 Flasher to Erase\n
Can't get hardware model - failed to create string
Setting bypass channel to: %d\n
Failed to convert primateLoc %s to unsigned long long
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
comparing against match entry [pid] %d: %s\n
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
{%s} skipping dcache flush, cache already clean
{%s} _pre_resume_hw result = %s
   ROM entry %d (level %u): AVOIDED\n
Error %d (%s) while expanding ~ for Astris history save\n
Failed to convert kisHubLoc %s to unsigned long long
Probe Map comm error %d(%s) %s [%s]
Skipping CPU %s at 0x%llx: not present in IDE\n
{%s} (end) current_el is now %d
EICE chip %x initialized\n
[AstrisAsync] Barrier hit!\n
   {%s} Read AP's R_MEMAP_CSW\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
Probe (port=%d) with unknown status %s dropped from available list
{%s@%d} neither socket nor kext connection available
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
Buffer is NULL
max_scan_bits is low: %d
[PREFS] Key: %s - Val: NULL
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
## ARM32cpu_t::read_register %u\n
{%s::%s@%d [%s]} Error %s: checking exception
{%s} explore with exploreflags 0x%X completed with error [%s]
Successfully Authenticated DFT\n
Can't get OS build version - failed to allocate buffer
\t[MATCH_TARGETID] FAIL <= unable to find DP
=== Detailed %s Boosters ===\n
{%s::%s} [%s] error %s writing SCTLR_ELx
{%s::%s} cpu powered off: failed init() %s
Error %d (%s) opening history save file
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Failed to instantiate %s\n
Could Not Get BoosterManagerUtility\n
Could Not Allocate All Boosters Array
Error happened when reading edscr. Retry #%i\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Could not find TAP at chip-index %d for v2 1500 config\n
{%s} invalid data width %d bytes
{%s} read ESR EL1|EL2|EL3 (%d)
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
type_hint not NULL, but creating a placeholder, this is off
Proceeding with full explore instead of instantiation
Warning: chip exploration did not complete successfully (%s)\n
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
%s
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
[AstrisAsync] Async mode %s
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
Awaiting response from Probe Map Server
[ANAMOLY] Could not find AXcpu_t object for CPU\n
--> 0x%02x = %s
[HALT] Chip %x\n
Failed to convert kisLoc %s to unsigned long long
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Invalid file name: \"%s\". File names must not start with '.'
{%s} Failed to get watchpoint count for %s: %s
   Debug Port: SELECT %X: DISABLED\n
Can't get OS build version - failed to create URL
Taking gateway control failed
Booster:\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
%s %d\n
Booster System Is Not Initialized Bailing\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s} unable to allocate probe name
{%s} no response from bridge
## ARM32cpu_t::read_register 64 bit 0x%x\n
{%s->%s} m_exception_level=%u
Unable to read LR
replayPreflight
Variables not setup
Error status from AMAuthInstallSetSigningServerURLPtr = %i
\nSaved %s binary data to %s\nWrote %lu bytes\n
!!!! FILE RADAR: Don't know how to compare two values\n
CPU Supported in Runtime: %s\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
\tPrologue Aligned Read Failed
   DPv3 baseptr is not valid (%X)\n
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s} [%s] error %s from _synchronize_context.
[%s]\n
AP[%d]: MEM_AP_AXI\n
{%s@%d} Unable to connect to server, %s:%d
{%s} %s: |%s|-|%s|
[ARM32cpu_t::_update_register64] 0x%08x\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
{%s} handle ROM entry %d (level %u): %08x
!*!*!* Lightning header facing up.                                                    !*!*!*
Disconnected from Probe Map Server
[KIS] Register Read/Write/Wrote: %d\n
BoosterManager Types:\n
{%s} already collected %s, skipping
{%s@%d} Probe response payload read when no payload indicated.
[PAR] Failed KIS Portal Access Preflight =%s (%d)
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
Using Built In CPUs\n
{%s} pmgr status=%d being reported as Unknown
{%s}#%02X cmd: %s, resp: %s
[KIS] CMD: %s \n
--> misc_wdr   size=%3d wirtestporten=%d
Cannot create complex descriptions from NULL info\n
Error returned from explore_pid
{%s->%s} ERROR=%d(%s)
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
Failed to explore chip: %d
  Error path [%s]\n
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
replay_counter=%lu, last_replay=%d
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Complex Type: %s\n
{%s::%s} error %s writing EDSCR %s
JsonLogger: Writing category '%.*s' to '%s'
using standard products.plist for %s
[1500] Error parsing bridge '%s': missing required field 'tap'
We Are Padding\n
CPU %s not found or already removed from the map
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
First Erase Failed, Lets Reset and Try Again\n
Probe Map Server Information: %s
{%s@%d} Failed to send probe command (error %d).
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Dart Base Address: 0x%llX\n
Hang Radar Info:\n%s\n
DBG_CPU: %s\n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
{%s} %s DC cache clean complete, marking as clean
   --> IDR: %08X\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
Values Not The Type We Expected. Expected: Number and String\n
Chip Revision: 0x%X\n
Switch back to primate KIS: %s\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Dumping Process Tree
{%s} found single_port probedaemon on port %d
{%s} drain_packets=%d [%s]
About to call fault reg latch, min_operating_el: %d\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
Erasing All Flash\n
Caught a portal that we dont have a status map for: %d
{%s} FIFO full, try again
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
Trying to use size of 8 on not AXI bus
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Creating a PSOC6 Flasher to Flash\n
Could Not Allocate Booster Location Array
read failed, using old cached as base: 0x%x
[PREFS] Key: %s - Val: ??
Unable to allocate memory for next part of big response
  Nested path: parent='%s', child='%s'
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} Error reading CPUID (%s)
{%s} Component ID read fail for 0x%llx (%s)
AP[%d]: unknown type\n
SSO is DISABLED\n
Re-Exploring...\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Probe Type (%d) FW Version: %s does not support KIS.
{%s} %s resumed\n
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
ERROR!! write binary data parameters invalid\n
%s given a NULL conn object
{%s} empty response string provided
Successfully connected to server, %s:%d
{%s::%s} creating placeholder for CPU: name=%s
{%s} bridge timed out
%s [RETRYING]
Asked To Write To A Negative Register Index
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
SoC not identified by IDCODE - enumerating instead of instantiating
{%s} Error looking up architecture (%s)
CPU: %s halting debug is now %s\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
{%s} ROMTABLE (dbgbase=0x%llx)
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
{%s} bridge returned an error
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Enabling USB Gateway
caller=%s, async=%d, iterations=%lu
dbgwrap halt failed, falling back to classic method
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
CPU Name: %s\n
!!!! DART Key %s is INVALID !!!!\n
{%s} Failed to resume %s: %s
## apw %u 0x%08X 0x%08X ...(%d)\n
Failed to create CPU %s - %s\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
{%s} handle ROM entry
Xtensa Option ocd_address: 0x%llx
{%s@%d} IOServiceClose failed, err = 0x%08x
%s status transitioned: %d ('%s') -> %d ('%s')\n
ERROR!! Couldn't save %s binary data\n
Could not find portal by select %d, while interpreting result\n
{%s} flags:0x%08x
XBS Version Modified: %s -> %s\n
[INS_WP] 0x%016llx x %d\n
Preferences does not exists: %s, creating one.\n
Setting STOP CLOCK to TRUE
{%s:%s}: cpu powered off: unable to access a register for this CPU
Unable to read PC
JsonLogger: Wrote %zu bytes to '%s'
JsonLogger: Loading schema for category '%.*s' from '%s'
Booster Bundle: %s\n
Failed to get DFU Type
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
Error %d (%s) opening cmd snapshost save file
{%s} select success without file descriptor set
{%s@%d} Drain empty on decr [%s].
using multi-target booster products_%s.plist
Reflashing\n
{%s} Error setting up memap target (%s)
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
Pages %d\n
{%s::%s} ERROR %d(%s) resuming %s\n
runBlock
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Setting CPU %s is_boot_core to %d\n
[1500] run_steps: unknown instruction '%s'
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
Failed to get PMU Name
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
   {%s} (DP): status=0x%X(%s) - %s\n
[%s] chipinfo is NULL
{%s::%s} [%s] unsupported width %d
collect_responses
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Chip Is In Open Mode\n
can't find pid in response\n
Old ProbeDaemon does not support this command
Probe %s removed prior to kick\n
Generated JSON (first 500 chars):\n%.500s%s
Logging Context Is NULL\n
Cannot create CPU descriptions from NULL info\n
{%s} L2 cache operation completed [%s]
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
Increasing length by: %d\n
response == NONE; failed to get kis target info\n
Cleaning up Each Booster Manager\n
## dpw 0x%02X failed (%s)\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
There is no system bus access port on the debug port
{%s} asc status=%d being reported as Unknown
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
{%s@%d} Failed to find cached response
Dart Dart Type: %s\n
Failed to convert %s key @ index %d
INFO: %s(%04u): %s(): err=%s(%d): %s\n
error %s reading DAP MMFR0
     ARM %s debug CPU rev %d\n
Going To Create Generic ARMV8\n
Error %s connecting to server %s:%s [RETRYING]
Probe Map comm: request[%s], response[%s]
{%s} %sing word #%d at address 0x%09llx: %s
[1500] IR command '%s' missing required field 'opcode'
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} restored el is now %d
Unable to disassemble_at_addr 0x%016llx
     0x%016llx: ERROR\n
Found match - bypass_device: %s; channel: %d\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
Found the RTXCID Structure!\n
[RESUME] Chip %x\n
[INIT]\n
probing %s status\n
      Read of JTAG-AP port %u CSW failed with %s\n
{%s} strsep empty so match any probe [localhost]
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
Failed To Erase All Flash
{%s} already connected
Failed To Instantiate SOC From Booster\n
{%s::%s} creating CPU
In Postflash\n
Size or Count provided are 0.
!!!! Complex Key %s is INVALID !!!!\n
pmu-name: %s\n
Magic does not match: %#x vs %#x\n
Async is disabled for localhost connection
Error status from AMAuthInstallSsoInitializePtr = %i
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
ERROR: unable to suspend translation for %s
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s} m_exception_level(%d) != current_el(%d)
{%s->%s}
   CPUID: 0x%08X\n
Switch to primate res: %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
checking if relay \"%s\" is valid
{%s} probe device server closed the connection while trying to read data (at recv)
{%s@%d} socket connection is not available
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
[ARM64 INS_WP] 0x%016llx x %d\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
## apw %u 0x%08X 0x%08X\n
CPU Already Halted\n
{%s} drop ProbeName %s
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
Failed to find a plist for this soc %s
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
   {%s} Enabling debug unit\n
%2d) %s %s [Busy]%s\n
SoC BM Not Found, Bailing\n
Initial DSPSR_EL0: 0x%llx
## armcpu: bad status even though all bytes written (%d)\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
[KIS] Words (Read/Write/Wrote): %d\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[1500] Detected plist version %d
[AstrisAsync] Failed to restart Async batch\n
\tTatsu AuthDebug Triage | All\n
{%s:%s@%d} Critical error encountered:
{%s} %s did not match any valid host
We are in clean up\n
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
Kick off the current process using probe %s? (y|n)\n
Init dbgwrap obj failed
JsonLogger: Created with default schema version '%s'
%s\n
Could Not Find Booster Entry Function: %s\n
## armcpu: bad status even though all bytes read (%d)\n
read_dbg failed to access R_v7M_CLIDR
[AstrisAsync] Resume when not paused!\n
{%s} FAILURE - NULL parameter
Could Not Allocate Loaded Booster Array
--> extrawrstn %d
%s constructed
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
{%s::%s} [%s] error (%s) getting number of HW BPs
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
{%s} %s status is '%s' [Status Read %d times]\n
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
{%s} no matching 1500-to-* bridge
Failed to convert %s key @ index %d to a number with base of %d\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
[COLLECT] Chip %x\n
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
     ARM %s watchpoints: %u\n
CCG Acquire Sequence Failed - %s (%d)
[1500] %s step %d missing required field 'instr'
{%s@%d} Received %d bytes when requested %d bytes [%s].
The debug port associated with this chip has not been explored.
Cannot create DART descriptions from NULL info\n
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
SoC has been setup using standard instantiation (setup result=%d)
{%s} FAILURE - max length exceeded
Astris Version Set: %s
--> psr        size=%3d bit=%d
product-name: %s\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
error %s reading DAP MPIDR
{%s::%s} %s pre_resumed\n
Can't get hardware model - failed to allocate data string
SoC must have a DAP
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
[READ] %d -> %08x\n
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
register lookup by name not supported when Astris is statically linked
   Debug Base: %08X\n
Problematic JSON value:\n%s
Complex Address: 0x%llX\n
Could Not Get Bundle Out Array of Found Boosters\n
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
{%s} Failed to get breakpoint count for %s: %s
Explore: %u chip%s\n
{%s} poll_srom_status is %s
Connected to Probe Device Server [Default Log]
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
OK: address translation resumed for %s successfully
Created Connection - : %s
Awaiting next chunk of big response
      AXap_write of R_JTAGAP_PSTA failed with error %s
CPU with %s Not Created via Name
=== Starting Gather and Clear ===
[%s] Booster System Is Not Initialized Bailing\n
CPU1 Status: %s\n
USER %s(%04u): %s(): %s
VBAR: %#x\n
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
Map is empty, not removing CPU %s
Invalid file name: \"%s\". File names must be at least %d characters long.
\tReading left over chunk expected 0x%x got 0x%x\n
SSO with no prompt being used
[Auth Debug] Disabled\n
Clocking To 48Mhz\n
{%s} host name(RSD): %s\n
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
[FLUSH]\n
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
setCategoryValue: path='%.*s'
--> debug      size=%3d acsr=%d
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
==== User Error Messages ====\n
{%s} connectName[%s]
{%s@%d} Received %d bytes when requested %d bytes.
[1500] TAP %d missing required field 'ir-cmds'
error trying to unlock MSR %s
Checking Write Protection\n
Creating a PSOC6 2M Flasher to Flash\n
{%s:%s@%d} Critical error [radar already requested]
relay_set: %s = CMD_ERR (%s)
{%s} Error %d(%s) sending message
Gathered Value is Not Number\n
Protocol Version: 0x%X\n
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
pc:  0x%16s cpsr: 0x%16s %s\n
{%s} failed (%s)
   JEDEC ID: 0x%08X\n
Failed to init from cpu desc armv7m cpu: %s \n
No version information found in booster: %s
[1500] TAP %d missing required field 'chip-index' or 'irlen'
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
Unable to read GPR %d
relay_set: %s -> %d
Invalid value for 'entry' tuple element - can't index
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
CPU DBG Ack: 0x%llx\n
batch_cmd_count: %d
{%s} PRIMECELL [DONE]
{%s} Component ID read fail on romtable (%s)
Connect using RSD not supported\n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
CPU Explore: 0x%llX\n
[1500] Error parsing bridge '%s': missing required field 'select'
error %s checking for data abort(uint32_t)
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
{%s} collect result = %s
AXportal_t Struct Is NULL
[1500] No %s.plist resource found
[INSWP] 0x%08llx wp%d rdwr=%X\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
X06 Part
Creating a PSOC6 Flasher to Acquire\n
Probe %s Device Not Connected on USB-C Port
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
bypass-config-name: %s\n
   {%s} Probe requires overrun detect mode.\n
=== Ending Gather and Clear ===
JsonLogger: Schema loaded successfully for category '%.*s'
Booster Info:\n%s
\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
KIS translator version : %d\n
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
Cannot create SoC [unknown chip identity (%d)]
{%s} bridge returned SLVERR
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
{%s->%s} START handling exception
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
OK: address translation suspended for %s successfully
      Select port %u: already explored..re-exploring\n
CPU Monitor[%i]: %s\n
[SSTEP] using BP %d\n
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
choice: %d\n
{%s@%d} Connection to server failed, error=%d (%s)
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Spew change. old=0x%016llX, new=0x%016X
{%s@%d} gethostbyname failed, error=%d (%s)
{%s} Failed to extract portal info from table (%d); continuing anyway
[REM_HWBP] bp%d\n
Failed To Acquire Chip\n
Hardware model: %s
Probe %s status: Idle
Failed To Init Booster's Astris API In: %s with %s (%d)\n
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
Could not write system request (SROM_SYSREQ_BIT | SROM_CMD_SET_IMO_48_MHz) error %s
{%s} unable to allocate probeInfo
start rev and/or end rev is NULL; skipping cpu_desc override\n
Got an error reading the DCM Control Register: %s
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
Erasing all flash at once\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
   Debug Port: SELECT %X: SKIPPING\n
Can't get OS build version - failed to create ReadStream
\tWriting 0x%08llX - 0x%08llX -> Row %u\n
UPDATE cop64 %d -> 0x%016llx\n
{%s=>%s} AXconn_t has more than one chip
Previous authentication in-flight, wait for it to finish\n
Astris Source Version: %s\n
Complex ID: %d\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
Result while reading third entry: %s , entry val 2: 0x%X\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Using 10pin connector skipping orientation check
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
Asked To Read A Negative Register Index
probe event: %s
{%s} Failed to extract ECID from table (%d); continuing anyway
Xtensa Option non_tie_ranges: %zu range(s)
{%s} Found extra info in = %s, chopping string
{%s} Extracted CIP Gen Number from table  (%d)
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
KIS Chip Found, Doing KIS Explore Setup
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
{%s[select]} %d(%s) [RETRYING]
Invalid SoC Booster. SoC Booster Requires PID\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
{%s} wrote %d words to probe when %d words provided in request
Hang Description:\n%s\n
SoC does NOT support IDE Explore\n
error %s reading DAP PFR1
Stepping Stone Final =  %#x\n
CPU Typehint: %s\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
{%s::%s} %s resumed\n
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
We are done with clean up\n
Could Not Match A Booster for %s\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
[%s] {%s->%s} clear async abort
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Complex CPU Name: %s\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
received %zd bytes from Probe Map Server when have %zu
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Type 'jebdump' to do scan/mem dump\n
Changed Write Protection To Open, Resetting and Reacquiring Chip...\n
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
Could not find bundle () in given array: %s\n
{%s} unable to find single_port probedaemon on port %d
unknown match criteria type: %d
Initializing (%s) Booster's Astris API\n
{%s::%s@%d [%s]} Error %s: flushing HW state
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
Multi target booster, checking for %s.plist\n
codeblock
   Debug Port: Trying SELECT %X\n
Connected to Probe Map Server
{astris_probed_print_events_from_json} not supported in this build configuration
{%s::%s} ITE is not set: 0x%X\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
failed read from DEMCR - %s
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
CPU has no regions, maybe powered off?\n
{%s} ROMTABLE (nest=%d)\n
tckrate_check returned error %s
coalesced-target: %s\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
DCCCTRL = %08X   res=%d\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
{%s} FAILURE - malloc error
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
Koko probe, for now I guess we will just say yes...\n
Sprocket probe, for now I guess we will just say yes...\n
Invalid Bundle: %s
[%s] E2H is set, virtualization is supported\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
   {%s} Clearing HNONSEC on AP \n
No 1500 bridges specified\n
Sending DYN Bypas Channel Set: %d
Dart Coastguarded CPU: %s\n
Commit Code: 0x%X\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
Unable to register assert upcall %s (Insufficient memory)
Adding new booster path: %s\n
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
first read of CMDSTAT may fail if external reset occurred
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
Creating a S1 Flasher to Acquire\n
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
1500 IR Commands:
Die Config Disabled\n
{%s} error: %s
{%s@%d} Timeout while sending probe command.
Did Not Find Any Boosters For: %s \n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
Error status from AMAuthInstallSsoEnablePtr = %i
no system bus AP present when expected
%s Bridge @ 0x%09llx-0x%09llx: %s
[ARM32cpu_t::_read_register64] 0x%08x\n
{%s} Error setting up jtag-ap target (%s)
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
DEMCR read failure - %s (%d)
Could Not Get BoosterManager. Need To Call AXbooster_init\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
Passed NULL booster without custom plist\n
--> localwrstn size=%3d debug=%d
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
{%s} 0 words from probe when %d words left to read for reg %d
VBAR: %#llx\n
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
Production Fused Device\n
{%s} connectName[local host]
{%s} %s: |%s|
AXconn_t Struct Is NULL
Valid Portal
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
   Debug Port not responding (%s)\n
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
X12 Part
We Are Matching Development Booster\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
## armcpu: success status even though not all bytes read\n
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
[KIS] Register Index: %llu\n
Failed to find a product plist for this soc %s
[%s] %d -> 0x%08x\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s::%s} [%s] error %s reading SCTLR_ELx
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
[AstrisAsync] Pause when already paused!\n
## memapw %u 0x%016llX 0x%08X\n
CPU Monitor key does not exists for: %s\n
The log file has been updated with all available diagnostics.\n
%s probe[*] from Probe Map Server [local host]
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Debug Clock Already Enabled
Die Addr Info LSB: %d Mask: 0x%016llX\n
Chip %x Status = %d\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Groups %d\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
Connected to Probe Device Server [Log File %s]
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
AXportal_t Is Not Valid Type - %d
Turning Debug Clock On
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
Could not write system argument param: %u error %s
[%s] {%s->%s} END handling exception
     0x%016llx: 0x%08x    %s\n
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
Chip Is Write Protected. Trying To Move Chip To Open Mode\n
relay_get: %s = %d
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
We are Allocating\n
CPU Subsystem: %s\n
** \tTatsu AuthDebug Triage | All     **\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
[READ] cop %d -> 0x%08x\n
Error Reading Device Production-Fusing\n
%s probe[%s] from Probe Map Server [local host]
Probe %s removed during selection process
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
error %s checking for data abort
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
AuthDebug::authenticate_probe - no need to authenticate\n
relay_get: %s = CMD_ERR (%s)
[1500] Error parsing bridge: %s
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s} Unable to read CPSR
Async is disabled for current seesion
Going To Create Generic Xtensa Core, name=\"%s\".\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{%s[recv]} %d(%s) [RETRYING]
iter=%lu
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
Xtensa Core %s NOT configured\n
Can't get hardware model - failed to allocate data buffer
process (%s) (%d) path: %s
Probe %s with unknown kick response %s
{%s@%d} Probe reported connection lost [PROBEEOF].
%s: chip was NULL when attempting to release soc
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
--> master     size=%3d localwrstn=%d debug=%d
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
Timed Out While Polling For Status\n
unable to create connection
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
Probe %s status: Busy
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
Found an async abort pending; clearing it\n
{%s::%s} failed: %s
[%s] CPU BM Not Found, Bailing\n
{%s}#%02X %s [%s]
unable to obtain sysap
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
## dpw 0x%02X 0x%08X\n
Creating a CCG3 Flasher to Erase\n
relay_get: %s = ERR
Complex CPM Offset: 0x%llX\n
Portal Group Base: 0x%llX \n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
[%s] TGE is set so we traping to EL2\n
[CACHEOP] %d, 0x%016llx, %d\n
Error closing %s [%d]
Matched via Bundle ID\n
{%s} timed out waiting for cpu to halt during collect
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
\tReading left over chunk 0x%x @ 0x%llx\n
## apr %u 0x%08X -> 0x%08X\n
      Read of JTAG-AP port %u PSTA failed with %s\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
Error %d(%s) executing instruction 0x%08X FAST
%s status is '%s'\n
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
{%s@%d} Found cached response
SoC has been setup using standard instantiation (setup result=%s)
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Successfully Authenticated\n
AuthDebugWithTimer_t destructor \n
Can't get OS build version - failed to open ReadStream
Issuing request to Probe Map Server: %s
--> cmd        addrsize=%d datasize=%d
Required key: %s @ index %d is NULL\n
Value Types Are Not Strings\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s} Failed to get breakpoint mask for %s: %s
Creating a S1 Flasher to Flash\n
Unable to allocate memory for big response
ERR: conn->nchips != 0; looks like chip is explored\n
--> wrstn_wir2 size=%3d dpcsoc=%d
%s NOT configured\n
{%s} calling _collect_hw on %s
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Probe %s selected
Could not find TAP at index %d to attach 1500 bridge to\n
Can't get hardware model - failed to get property
{%s::%s} write OK but took %d tries
%s: []\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
Creating a S1 Flasher to Erase\n
!*!*!* ****************************************************************************** !*!*!*
[AstrisAsync] Deactivate while async is not active!\n
Wrong width, should be either 4 or 8\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Matched Booster: %s\n
Failed to sync prefs at end
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
## memapr %u 0x%016llX %d -> 0x%08X ...\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
Section 1 Offset: 0x%llX\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Breakpoint Size: %d
SOC_t::{%s} CPU_t group=%d when group 0 expected
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
[KIS] Portal Status: 0x%X\n
Too many portals, we are at portal: %d while max is %d\n
{%s::%s} [%s] error (%s) getting number of HW WPs
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
    %s(): %s
caller=%s, async=%d
Previous attempt to connect to probe failed: %d (%s). Retrying...
AP[%d]: JTAG_AP (Exploring Later) \n
Could Not Get BoosterManager\n
Board ID: 0x%X\n
[AsyncSnapshot] #%zu: %s\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
Creating a CCG3 Flasher to Flash\n
ERROR!! Wrote %zd bytes, expected %zd\n
connection about to be destroyed
CPU0 Status Not Valid\n
Error %d(%s) executing instruction 0x%08X
{%s} Unable to read SP_EL0
   Created Fake Debug Port Debug Port
Failed to convert CFArray to C Array\n
Re-Acquiring...\n
%2d) %s %s%s\n
Failed to get KIS translator version\n
[1500] TAP key is not a valid integer
=== Loaded %s Boosters ===\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} [%s] MMU not active - returning %s
Failed to sync prefs at beginning
   Debug Port: SELECT %X; error: %s, retrying..\n
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
{%s} bridge returned DECERR
In Preflash\n
TAP IDCODE: 0x%X\n
** CPU %s requires forced explore override flag on this SoC **\n
[MEM] Uncompleted; DSCR = %08x\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
Error status from AMAuthInstallSsoSetStealthModePtr = %i
unable to identify chip
Initializing Booster Layer\n
{%s} Failed to extract PID from table (%d); continuing anyway
{%s} halting %s\n
Fabric access is blocked. Expected if production unit, won't explore further.
no system bus AP present with AHB, trying AHB5
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
[READ] %d -> 0x%08x\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
Found %d APs
[Auth Debug] Ticket Active, Debug Interface Locked\n
%s SoC created
{%s} error %s at line %d
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
couldn't find CPU1. this is expected sometimes.
Early dbgwrap base extracted: 0x%llx\n
[AstrisAsync] Discarding response due to ASYNCSKIP state!
haskis bit not set\n
Could Not Allocate Info Keys Array
Subsystem Monitor[%i]: %s\n
HOSTID=0x%x which is invalid, skipping orientation check
Connected toProbe Map Server (single_port) 
We are at max iterations, still didnt get full JSON
[AsyncSnapshot] No snapshots collected\n
[Auth Debug] External Debug Interfaces Open\n
%s probe[*] from Probe Map Server [%s]
{%s} unsupported bridge type for %s
CPU PS-Register: 0x%llX\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
Found form-factor specific channel %u for device '%s'
CPU0 Status: %s\n
{%s::%s@%d [%s]} Error %s: collecting HW
Original Content: 0x%08x
{%s} setting up nameless target (address=0x%llx)
AXjtag_srst assert failure - %s (%d)
{%s::%s} ERROR %d(%s) pre_resuming %s\n
[%s] %d -> %08x\n
Result while reading second entry: %s , entry val 1: 0x%X\n
After powerup CMDSTAT=%08X\n
[1500] Error parsing TAP description
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
{%s} NOMEM
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
** Add the --with-force option or use the explore_override console command **\n\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
{%s} probe_host = %s
{%s@%d} Unknown CS command error [%d]
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
Required Key-Value is a string, and not an array. Old booster found\n
Dart Name: %s\n
Debug Base: 0x%llX\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
[DCC] Grabbing DTR failed: %s\n\n
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
Had an error during transfer: %s
Stop Clock: %s\n
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
Replacing key with value
[AstrisAsync] Got ASYNC_RESTART response!
ERROR: unable to resume translation for %s
   Debug base is in legacy format\n
!!!! CPU Key %s is INVALID !!!!\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
{%s@%d} Connection to server rejected, error=%d (%s)
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
[1500] Error parsing v2 bridges
Target ID: 0x%X\n
[AstrisAsync] Pausing Async Mode\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
{%s} _halt_hw result = %s
Breakpoint Index: %d
{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s} Unrecognized component: %08X, class %02X\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
Reflashing Advanced\n
New format for cip gen register, unsupported: %d\n
[CLEANUP]\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
PKA Base: 0x%llX\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
{%s::%s} [%s] length=%u when width=%d
Probe %s with unknown status %s dropped from available list
Please answer y=yes or n=no.\n
gmtime() returned NULL, using epoch time
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
%s: not supported.\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
\tLeft To Read (%d) < width (%d).\n
{%s@%d} Timeout while attempting connect to server
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Modified Word To Write: 0x%08x
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
   {%s} APB/AXI address for target setup = 0x%llx\n
Could Not Create Dictionary From Booster: %s
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
Erase All Flash\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Cypress PID: 0x%llX\n
%s construction failed
Found another target for the plist\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
   Debug Port: SELECT %X: AVOIDED\n
Both debug and xbs versions are set, maybe a bug: %s
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s::%s} HDE not set on %s. Will re-enable.
[%s] {%s->%s} Transitioning to exception level %u.\n
Successfully Authenticated Probe\n
Xtensa Option num_wp: %d
Failed to create Xtensa CPU %s \n
{%s} _resume_hw result = %s
Error while trying to authorize: %d - %s\n
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
2: ARM64_SYSOP_ATS12E1W\n
Cached async_replay capability version: %u
Breakpoint Address: 0x%llx
connection created
{%s@%d} IOServiceOpen failed, err = 0x%08x
Probe %s Device Does Not Have LocationID
CPU ASC Offset: %d\n
Die-Count: %d Current-Die: %d Die-Type: %d
Failed to read ide_table from KIS explore
[AstrisAsync] Resuming Async Mode\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
SSO info present but SSO disabled.
New Length: %d\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
   Setting up AP IDR %08X\n
Xtensa Option num_bp: %d
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
{%s=>%s} null reference to AXconn_t record, `conn`
Buffer Size Is Larger Than Flash Size: %d
Selecting polling method %s
Failed To Initialize Logging\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
{%s} Reading base 0x%llx entry's component ID
Xtensa Option reg_file_size: %d
%s %3d'b%s\n
[SSTEP] bvr=%08x bcr=%08x\n
{%s::%s} read OK but took %d tries
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
1: ARM64_SYSOP_ATS12E1R\n
outstanding=%zu
{%s} Unrecognized Component: %08X (class %u)
Probe %s LocationID Info is %s
[KIS] Address: 0x%llX\n
Gathered Info:\n%s
Table Size: %d\n
DEMCR: 0x%08X -> 0x%08X
Creating a CCG3 Flasher to Acquire\n
{%s[select]} timeout while waiting for data from the connection
Going To Create Generic ARMV7m, but typehint is present (%s)\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
AXconn or json_out are NULL
Connecting to server, %s:%d
no debug bus AP present when expected
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
KIS Preflight No Need To Write to AP CSW
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
   {%s} select %u port %u: %u chip%s\n
TatsuServer Found: %s\n
CPU (%s) has explore flag of: 0x%llx which is not set\n
Match Count is Zero. This is invalid.
[AstrisAsync] Barrier before pause\n
{%s} Failed to single-step %s: %s
Breakpoint Enabled: %s
In Eraseflash\n
Unable to read FP
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
Exploring IDE in JTAG\n
Failed To Request Chip ID\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
CPU Core Number: %i\n
CPU Die: %d\n
{%s} Failed to extract CID from table (%d); continuing anyway
[AstrisAsync] Activate while async is already active!\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Subsystem Monitor Key does not exists: %s\n
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
Could Not Allocate Mutable Dictionary For BoosterMangers
ERROR - Cypress Flash Failed (%s)
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
Polling Rom Status\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
Gateway is KIS, seeing what probe this is\n
{%s} probe_port = %d
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} Debug Base: %08X
Acquiring Chip\n
kext connect name %s\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
Passed NULL plist file\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
Creating a 4200L Flasher to Flash\n
Portal Status, Changing STATUS and CMD/STAT to reflect
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
Complex CPU ID: %d\n
[1500] %s step %d: unknown instruction '%s'
[READ] cop64 %d -> 0x%016llx\n
{%s::%s@%d [%s]} Error %s: synchronizing context
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
Creating a PSOC6 2M Flasher to Erase\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s} read %d words from probe when %d words requested
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Not Creating CPU: %s\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s} 0 words requested for read at address 0x%016llX
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
      Explore of JTAG-AP port %u failed with %s\n
No 1500 bridges or TAPs specified (v2 plist)\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
{%s=>%s} AXconn_t has no chips
X09 Part
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
{%s} Failed to extract component info from table (%d); continuing anyway
Translate Stage Chosen: %d\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
\tAligned Read Failed
{%s} no TAP detected that supports 1500
{%s}ERR: bypass_device_name is NULL\n
Banana split probe, for now I guess we will just say yes...\n
{%s} checking for single_port probe daemon on port %d
Failed to convert primateHubLoc %s to unsigned long long
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
[1500] TAP %d: irlen must be > 0 (got %d)
    INFO(%u,%d): %s(%04u): %s(): %s
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
\tLeft Over Chunk Read Failed\n
{%s} %s
Complex Name: %s\n
Portal Group Offset: 0x%X Entries: %d\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
[%s] cop %d -> 0x%08x\n
failed write of 0x%08X to DEMCR - %s
   DPv3 bus is %u bits wide\n
Optional Key: SubsystemMonitor not in preferences
{%s} [%s] m_exception_level=%u\n
## dpr 0x%02X failed (%s)\n
 MEM-AP %X is hung\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s} valid response from bridge
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Gateway Version: 0x%X\n
{%s->%s} (top) current_el=%d
Highest EL: %d, -- Min Op EL: %d
Unable to read SP
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
   DPv3 BASEPTR0 is 0x%08X\n
{%s} explore with exploreflags 0x%X complete [%d chip%s]
Failed explore before forced KIS reset: %s\n
{%s=>%s} AXconn_t has no SoC object
** Unauthorized User/Network or ECID **\n
X00 Part
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
Probe %s Device Server listening on port %d
\t[MATCH_SKIP] skipping entry
Using Built In SoCs\n
invalid IR command '%s'
DEMCR write failure - %s (%d)
In Writeflash\n
{%s} Thread %#llx clearing key %lu
   MEM-AP not enabled\n
Could not enable KIS SoC Access\n
Reading Chip ID\n
{%s} error %d(%s) reading data from the connection (at recv)
{%s} DEVARCH read fail in CoreSight component (%s)
Creating a PSOC6 2M Flasher to Acquire\n
{%s} probeList has probeCount of zero
comparing against match entry %d: %s
Unknown number of groups in the explore table; can't parse group attributes
component group %d\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
[INSBP] bp%d addr=%08llx fpr=%08X\n
{%s} _pre_halt_hw result = %s
AP Only Explore was asked for, stopping here
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Dart CPU SID(s): %s\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[HALTED] dfsr = 0x%08x\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
Unable to create pthread key for conenction. errno=%d %s.
{%s} hostname:%s, flags:0x%08x
Erasing all flash a sector at a time\n
{%s} Error reading PID (%s)
Initialized %d 1500 bridges\n
CPU Supported in Integration: %s\n
{astris_probed_print_events} not supported in this build configuration
\nERROR - Cypress Flash Failed (%s)
Exception %d Stack Trace
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
Hang Address: 0x%016llx\n
Creating CPU Returned: %s\n
Failed to convert CFString to C String.
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
Kick has been requested by probe server
In Readflash\n
Failed to get Bypass Config
Booster Value is Not String\n
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
{%s} no chip found
Probe Map name of probe %d is: %s
Choose a device: 
HOSTID bit not set\n
Could Not Find Any Boosters\n
[MEM] Aborted; DSCR = %08x\n
{%s::%s@%d [%s]} Error %s: resuming HW
[AstrisAsync] Discarding %zu completed command(s)\n
can't find bid in response\n
{%s} host:%s, flags:0x%08x
end rev is not of expected format; skipping cpu_desc override\n
Min Component - %s\n
Die Config Disabled
{%s::%s} timeout while waiting for EDSCR ITE
Can't get OS build version - failed to create plist
Initialized Logging - %s
Could Not Find Any Loaded Boosters of Type: %s\n
dfu-Type: %s\n
Start Page: %d\n
Aligned Address: %llx
[PREFS] Key: %s - Val: %s
JsonLogger: Creating new category '%.*s'
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
Invalid Size Given for AP AP=%d Size=%d
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
start rev is not of expected format; skipping cpu_desc override\n
SOC AP[%d]: JTAG_AP\n
SWDACKDELAY relay write failed\n
Original Length: %d\n
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
TargetSel Before Disable: 0x%x
Gathered:\n
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
[%s] EL @ end of Collect: %d\n
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
AP[%d]: MEM_AP_AHB\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
AXmemap_readvals failure - %s
[1500] v2 plist missing required field 'taps'
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
==== Exception Trace ====\n
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
[%s] AP, DP, or chip given is NULL
{%s->%s} current EL (%d) already == target EL.\n
Invalid APTABLE (%d), so using most restrictive
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s} Exploring with option: %s\n
getOrCreateValue: addMember failed, returning doc root
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
AP[%d]: MEM_AP_APB\n
Can't get hardware model - failed to find matching IOService
{%s} %d(%s) [RETRYING]
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
{%s} category=%d
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
Width: %d not supported
{%s} unmodified-probe_match = %s
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
=== Found %s Boosters ===\n
Unable to read CPSR
Invalid current AP (%d), adopting APTABLE (%d)
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
OS build version: %s
Probe %s with unknown port response %s
sending abort to clear a timeout\n
AXjtag_explore failure - %s (%d)
CPU Address: 0x%llX\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
AP is NULL
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
## memapr %u 0x%016llX -> 0x%08X\n
{%s} host = %s
{%s@%d} Unknown CS code [%u]
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
Could Not Erase
Creating a 4200L Flasher to Erase\n
Xtensa Option options: 0x%x
We are Deallocating\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
{%s::%s} NULL parameter
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
successfully updated DEMCR
{%s} Failed to get watchpoint mask for %s: %s
   JTAG-AP: Identification = %08X\n
Failed to create optional file. Not fatal, moving on
[PAW] Failed KIS Portal Access Preflight =%s (%d)
Cleaning up Main Booster Object\n
CPU1 Status Not Valid\n
\tWriting 0x%08llX - 0x%08llX\n
{%s} %s DC cache already clean since last halt, skipping flush
{%s} status=%d being reported as Unknown
Cypress PID: 0x%llX Not Supported For Advance Flash\n
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
      Select port %u: AVOIDED\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
Optional Key: CPUMonitor not in preferences
\t[MATCH_FOUND] identified chip: %s
Full JSON that failed validation:\n%s
CPU state %d
{%s} %s status failed. error: %d (%s)
Unaligned Read @ 0x%llx Width: %d Bytes: %d
%#09llx-%#09llx: %s\n
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
DBGCTRL = %08X   res=%d\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
Request Dict:\n%s
register    %-15s %3u     \"%-s\"\n
dropping empty probeInfo (port=%u)
{%s} unaligned %d-byte access at address 0x%09llx
Before astris_kis_init_dp, CMDSTAT=%08X\n
User created bundle found, ignoring version checking via plist
   Debug Port has unknown type\n
{%s=>%s} null reference to AXchip_t[0]
Exc Cause: 0x%x - Exc Vaddr: 0x%x
%s probe[%s] from Probe Map Server [%s]
Could Not Find a DCM Portal
Could Not Find Any Boosters of Type: %s\n
Unable to convert plist file name to CFString: %s\n
\t\tARMv6 debug CPU xxx ID\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[AstrisAsync] Deactivating async...\n
{%s} DAP command nwords=%d trimmed to %lu\n
Xtensa Option dbg_intr_level: %d
Explored\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
Going to do imago workaround\n
Probe %s removed before port determined\n
CPU %s already in the map with status: %d
Unable to read GPR 28
[AstrisAsync] Activating async...\n
## dpr 0x%02X -> 0x%08X\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} set=%u (sh=%u), way=%u (sh=%u)
{%s::%s} halting %s\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
[KIS] Portal ID: %d\n
\t%s (%s)\n
1: ARM64_SYSOP_ATS12E1W\n
     0x%016llx: 0x%04x      %s\n
{%s=>%s} no soc reference; falling back to direct cpu method
probetimeout retry failed logging as hang\n
CPU AP-Type: %d\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
There is no debug port associated with this chip.
Raising to EL2 cause in Guest\n
[REMWP] wp%d\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
Can't get OS build version - failed to get build version
{%s} probe_match = %s
Probe %s USB-C location is %s
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
{%s@%d} Unable to create socket
Init objects failed
Extract Offset: 0x%X for %d\n
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
[WRITE] %d -> %08X\n
[AstrisAsync] replay preflight: Async not active!\n
{%s::%s} [%s] !bpwp_initted, retrying init
could not perform cpu_preflight
{%s} Class 9 ROMTABLE (nest=%d)\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
Bundle: %s NOT FOUND\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
2: ARM64_SYSOP_ATS12E1R\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
Creating a CCG2 Flasher to Flash\n
Invalid character [0x%02X] received from Probe Map Server
Probe Map comm error %d(%s) %s
[%s] Booster System Is Not Initialized\n
AP given is not a MEMAP
Connection to server accepted
{%s::%s} waiting for EDSCR ITE
Xtensa Option num_high_pri_intr: %d
Set custom PSD json file: %s
AXjtag_srst deassert failure - %s (%d)
{%s} Failed to extract die infofrom table (%d); continuing anyway
[REMBP] bp%d\n
Length is 0
Can't get hardware model - failed to convert to C string
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
{%s} match any probe [localhost]
DBGSTATUS = %08X   res=%d\n
     ARM %s breakpoints: %u\n
Result while reading first entry: %s , entry val 0: 0x%X\n
Previously dumped the process tree, skipping
Could Not Get SYS AP
KIS Writevals putting back the value
KIS Readvals putting back the value
Component Group Offset: 0x%X\n
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
astris_json_logger_delete
ret.test.2.1
spsr_select
AXjtag_transmitraw
OCD control register, set
Register file 50
AXI Error
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
DISASM
--> wrstn_wir2 size=%3d dpcsoc=%d
ipc_acquire
_get_num_hwwp_hw
cpu_resume_translation
coredump_diagnostic
invalid environment variable
%s%d
dcm
A64
enable
OK: address translation resumed for %s successfully
DESIGNER_APPL
PID
fn._ocd_exec_instr.l16ui.r1.r0
OS build version: %s
set
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s} Error reading CPUID (%s)
astris_apread
AXdebug_auth_is_dft_authenticated
Section 5.2
Unknown Subcommand
allocator_
armv7m-region-offset
targetid
SBR
MISC2
fn._ocd_enable.true
astris_ide_get_cpu_halt_group
Failed to sync prefs at beginning
AXcpu_hwwp_remove
!!!! Complex CPU Key %s is INVALID !!!!\n
result.read_vals(table)==
Not supported portal of type: 0x%X
Too many portals, we are at portal: %d while max is %d\n
Error %d(%s) executing instruction 0x%08X
.astris_version
type >= kNullType && type <= kNumberType
_init_params
\nERROR - Cypress Flash Failed (%s)
ret.generate_nonce_and_send_request
RF38
name.IsString()
AXdisassemble_at_addr
Unable to disassemble_at_addr 0x%016llx
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
SLEEPCTL
AddMember
Could Not Allocate Info Keys Array
_pre_resume_hw
PAR_EL1
Table 5–161
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
   Debug Port: SELECT %X; error: %s, retrying..\n
ret.CFReadStreamOpen
cpu-xtensa-reg-size
[1500] %s step %d missing required field 'instr'
astris_explore_enabler_get_subsystem_status
Wat!: 0x%llx
ret.ito.clear_edscr_err
[AstrisAsync] astris_async_override_disable_async: conn is NULL
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
{%s:%s@%d} [%s] Failed To Program Row %u\n\n
apb-regs
[SSTEP] using BP %d\n
[1500] %s step %d: unknown instruction '%s'
Booster Value is Not String\n
AXexplore_enable_cpu_pattern
!!!! Critical Error: m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15 !!!!\n
Table 5–168
%02u:%02u:%02u:%06u|%s <%s> %s\n
virtual int ARMv6cpu_t::_resume_hw(bool)
ret.dlr_el0
## apr %u 0x%08X -> 0x%08X\n
{%s:%s@%d} [%s] Could Not Get AP After Reacquire: %s\n
Xtensa Option non_tie_ranges: %zu range(s)
no MEMAP access
ASTRIS_ERR_PROBEINUSE
GetState
dr ->
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
PS
RF24
fn._ocd_exec_instr.wsr
fn.AXmemap_write.address.regval.
_
ret.memap.write
AXjtag_scanout
var.bp.invalid
TAP-Only
n >= 0 && n <= 308
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
virtual int ARMv7cpu_t::_halt_hw()
ret._a64cpu_el_fault_reg_latch
dest_reg < 32 || dest_reg == 31
s
Prompt
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/disassembly/astris_disassemble.cpp
virtual int ARMv7cpu_t::_resume_hw(bool)
Unable to read FP
AXcpu_lacc_status_remove
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
ret.CFURLCreateCopyAppendingPathComponent
param._tgt.invalid.null
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
resolve_platform_details
Going To Create Generic ARMV8\n
{%s:%s@%d} [%s] Failed Unhalt During Acquire Sequence: %s\n
DCRSET
SimulatorSWD
GetDouble
operandStack.GetSize() >= sizeof(Frag) * 2
AXbooster_get_loaded_boosters
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
sector: %d
astris_explore_enabler_init
sso_user.sso_data_length == 0
Probe %s Device Not Connected on USB-C Port
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Asked To Write To A Negative Register Index
soc-name
using multi-target booster products_%s.plist
AVD
DCS15
i8@?0
Status/State
IDLE
{%s->%s} exec: aarch64_add_imm(REG_SP, scratch=%d)\n
{%s::%s@%d} [FALSE] aarch64\n
Enabled
Creating a S1 Flasher to Flash\n
i32toa
Required key: %s @ index %d is NULL\n
value
param.m_ap == NULL && param.m_lam == NULL
%s/%s
DISCONNECT
complex-cpus
reset-network
## armcpu: bad status even though all bytes written (%d)\n
{%s} Error looking up architecture (%s)
astris_init_ap_mem
Got an error writing 0x%X the DCM Control Register: %s
   Debug Port has unknown type\n
relay_set: %s = CMD_ERR (%s)
Skipping CPU %s at 0x%llx: not present in IDE\n
setCategoryValue: path='%.*s'
index != kRegexInvalidState
[%s] Executing instruction=%llx
{%s->%s} [!aarch64] exec: encode_mrs(scratch=%d, MDDTRRX_EL0, %d)\n
[PREFS] Key: %s - Val: %s
haskis
param.chip->conn == NULL
param.cpu_name == NULL
lower_el.check.el = target_el
64 
hwbp_remove
\tReading left over chunk 0x%x @ 0x%llx\n
EPC2
Misc register 0
ASTRIS_ERR_EENOTFOUND
cpu
Connection aborted: kick required by probe server
host
Topology
Variables not setup
probetimeout retrying access...\n
cpu_hwwp_enable
AXbooster_interface_init_astris_api
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
Failed to get PMU Name
Die Config Disabled
!!!! Critical Error: Thread %#llx key %lu losing when suspended for info %p - NOT ALLOWED !!!!\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
PrettyPrefix
j1500i2
Invalid value for 'entry' tuple element - can't index
{%s} Failed to get breakpoint count for %s: %s
AXcpu_status_pmgr
{%s}ERR: bypass_device_name is NULL\n
revive
ARMv8-R CPU
internal.enable-test.chip == NULL
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
pnav_drop_probe
BADCODE
cpu_translate_with_dart
_collect_hw
[DCC] Grabbing DTR failed: %s\n\n
{%s} Unable to read SP_EL0
fn._ocd_exec_instr.rsr.ddr.t1.2
PROBED_ERROR
connecting to selected probe (single_port)
Old ProbeDaemon does not support this command
AXcpu_readreg
L1_INSTRUCTION
probe matching %s on localhost
We are in clean up\n
CPU Supported in Runtime: %s\n
{%s:%s@%d} [%s] reading PRSR (!oslk)\n
AXarm7_dbgread
rpc
M4F
!!!! Critical Error: batch attitude thread trying to lock - CAN'T LOCK !!!!\n
AXarm7_dbgscan
EXCSAVE3
Xtensa Option options: 0x%x
CHIPCNT
TargetSel Before Disable: 0x%x
Magic does not match: %#x vs %#x\n
!!! Critical Error msr_cache[%d] IS NOT cached !!!
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
Discon
param.at.invalid.>15
cpu_go
Base::level_stack_.template Top<typename Base::Level>()->inArray
GetUri
ret.rx-full.mddtrrx
print_debug_regs
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
RF25
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp
GenericStringRef
target_el <= 3 && target_el >= 0
defaults.create.key.no_probe
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_cpu.cpp
Can't get OS build version - failed to create URL
JsonLogger: Created with default schema version '%s'
Could Not Allocate All Boosters Array
socnames
astris_ide_explore_release
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s:%s@%d} [%s] updating ADFSR\n
NONE
ETM/PTM
Table 5–159
LITBASE
TRANSLATION_ERR_L1
cpu_swbp_remove
UNKNOWN 
DCS14
{%s:%s@%d} [%s] moving DBGDTRTX to GPR 0\n
_a64cpu_encode_hint
AXjtag_setclr
 JTAG Access Port.
APF
--> extrawrstn %d
Wake
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
astris_memap_masked_read
ARMv8 CPU
CypressFlasher_4100S
EPS7
ASTRIS_ERR_PROBED
sib-network-psr-reset
_clean_l2cache_setway
[%s] {%s->%s} clear async abort
{%s} Failed to get breakpoint mask for %s: %s
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
cpu_mmu_walk
EvalQuantifier
dbgarch
{%s} [is_64] exec: encode_msr(MDDTR_EL0, 0, %d)\n
High level exception save location
pnav_create_probelist
{%s::%s} NULL parameter
CPU.ARM
internal.authenticate_dft.debug_auth == NULL
AddState
XBS Version Modified: %s -> %s\n
dest_reg < 32 && dest_reg != 31
astris_memap_bus_read
Chip Is Write Protected. Trying To Move Chip To Open Mode\n
_write_mem
%s\n%s [%s]
EPIWRITE
ret.cfg_read(R_DCM_GPIO)
Failed to program row: 0x%08llX - 0x%08llX -> Row %u\n
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
RF4
fn._ocd_reg_r.ddr.regval
UNKNOWN CODE
ide_checker
error %s reading DAP PFR1
0
, and bits [15:4] are 0xC20 indicating Cortex-M0 core
Low level
{%s} 0 words from probe when %d words left to read for reg %d
chip->ide_table == NULL
{%s:%s@%d} [%s] reading CPSR(1)\n
_get_bpaddr_hw
New
n APB Access Port.
Can't get hardware model - failed to find matching IOService
Can't get hardware model - failed to allocate data string
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_swdflash.cpp
(system_reg & (0x40000000 | 0x80000000)) != 0
Table 5–185
!!!!!!!!!!   $ sudo chown $USER %s\n
no AP (Access Port)
cpu_cleaninv_dcache
dbgfifo
Schema parse error
EL0t
ret._mmu_init
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
%s:?? (%s)
High level 6 exception PS
param.cpu_reg_file_size.invalid.1
Apple Fabric Timeout
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
[READ] %d -> %08x\n
   Debug base is in legacy format\n
options=0x%8.8X, #addr_bp=%u, #data_bp=%u,deb_int_lvl=%u
A32
swdackdelay
ConsistDbg
ASTRIS_ERR_NODATA
INVCHIP
addMember.user
{%s:%s@%d} [%s] reading GPR 0\n
{%s} pmgr status=%d being reported as Unknown
Values Not The Type We Expected. Expected: Number and String\n
astris_ide_refresh_boardid
tckrate_check returned error %s
indicating a %s, and 
var.m_debug_interrupt_level.invalid.outofrange
var.num_loops.invalid>3.curr_instr
%u
%s_%s
ret.restoring_el_after_raising_to_read_hcr
FAR_EL1
internal_dft.is_authenticated.debug_auth == NULL
Probe %s removed before port determined\n
cpu_hwbp_info
ret.read.rtxcid
MR2
R10
_get_type_hw
:usb
{%s} %s did not match any valid host
!Base::level_stack_.template Top<typename Base::Level>()->inArray
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
version
AXconn_copy_nickname
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
CPU ASC Offset: %d\n
M3
SoC has been setup using standard instantiation (setup result=%s)
{%s} explore with exploreflags 0x%X completed with error [%s]
, indicating an unrecognized ARM Cortex-M core
DBREAKA1
MAC16 data register 0
Parameter length = %u > 4.
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
Caught a portal that we dont have a status map for: %d
DISPEXT
DBGWRAP_FULL
PFR0_LO
{%s} Failed to single-step %s: %s
AXmemap_read_modify_write
Data TLB configuration
_remove_instr_breakpoint
=== Starting Gather and Clear ===
complex-type
%d > %d
AXcpu_lacc_bp_status
fn._ocd_exec_instr.wsr.ddr.t1.2
xfer=%u, xfer_length=%u, address=0x%8.8X
astris_clear_user_die_select
{%s:%s@%d} [%s] setting GPR 1 (todo 1)\n
elr_el1
Vector Base
dtoa.h
ret.write.infinite_loop
CPU[%s] Read Reg: %d
AXcpu_mmu_get_page_shift
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
connect
ASTRIS_ERR_NOTPRESENT
[1500] Error parsing IR command: %s
ret._a64cpu_read_vfpreg_hw
EDDTRRX
generic error injected by probed
write to CMD/STAT failed - %s
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
WindowBase
cpu_lacc_pc_status
Logger is null
setToolInfo
{%s} invalid data width %d bytes
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
fn._ocd_exec_instr.wsr.ddr.t2
HIDBridgeSWD
AXchip_get_chip_variant
LAM
Invalid GPR Given: %d > %D
Exception occured after executing MSR to write into sysreg
{%s:%s@%d} current_el[%d] == 1|2|3\n
EXPLORE_IN_PROG
    IDR[31:28] is 0x%02X (revision).\n
{%s:%s@%d} [%s] Failed To Write Infinite Loop To SRAM: %s\n
Register file 37
CDPUL
ASC_TCORE_ROM
[%s] error reading EDSCR with mask
Result while reading third entry: %s , entry val 2: 0x%X\n
CTM
One time initialization of oslog API failed!\n
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
PERSEIS
psr-bit
L1CRT
{%s} halting %s\n
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
ret.write.spsr_elx
VectorCatch
Xtensa Core %s NOT configured\n
fn._ocd_reg_r.dsr.regval_raw
dbgwrap halt failed, falling back to classic method
astris_findidcode
, indicating Component Class == <unknown>
write_memory_dbgwrap
operation still in progress
USB connection not currently open
{%s} already connected
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
DOCK-CH-DATA
{%s:%s@%d} [%s] reading DFAR\n
{%s:%s@%d} [%s] writing DTRRX(first)\n
dlr_el0
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
      Select port %u: AVOIDED\n
AuthDbg,EnSecureTestExternal
ret.m_lam.paccess_write
{%s:%s@%d} [%s] executing STCpi(uint32_t)\n
error %s reading DAP MPIDR
{%s} ROMTABLE (nest=%d)\n
ret.reg.write.K_DA_REG_NAME_ECID1
Only Auth-Debug, DFT-Auth and Probe-Auth are currently supported.\n
General register 8
fn._ocd_exec_instr.rsr.ddr.t1
ret._release_gateway_control
CTI_GATE
[AstrisAsync] Deactivating async...\n
fn._ocd_exec_instr.TIEWriteProtectedI
rhs.GetType() == kObjectType
wrstn-reg
!!!! Critical Error:  dspsr_el0 NOT CACHED !!!!\n
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
init_hw.pid0
n AXI Access Port.
Table 5–135
ret.astris_clear_user_die_select.astris_soc_get_applesoc
Size
ParseNumber
{%s} status=%d being reported as Unknown
fn._ocd_exec_instr.s32i.r1.r0
!*!*!* Lightning header facing up.                                                    !*!*!*
AXbooster_print_boosters_detailed
ret.reflash.read.verify
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s:%s@%d} [%s] reading OSLSR\n
error %s checking for data abort(uint32_t)
UPDATE cop64 %d -> 0x%016llx\n
AMAuthInstallSupportDictionarySetInteger32
MESR
Failed to read DCM GPIO (0x%x)
hostid
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
internal.is_authenticated.chip->soc == NULL
op_DSYNC_encode
fn._ocd_exec_instr.rsr.ddr.addr_reg
target not in appropriate state for action
 (eng)
opcode
_a64cpu_assert_rw_matches_hw
TatsuServer Found: %s\n
RF9
connecting to Ethernet probe
cpu-typehint
L1C
{%s} error: %s
a
!*!*!* ****************************************************************************** !*!*!*
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
%s probe[%s] from Probe Map Server [local host]
debug-acsr
ret.nop
!!!! Critical Error: Nested exceptions... get someone to debug this. !!!!\n
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
        CID[15:12] is 0x%X
Error while trying to authorize: %d - %s\n
???
Register file 2
lower_el.el2.noimplemented
AXcpu_flush_icache
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
{%s:%s@%d} [%s] \tCould Not Read System Argument Register (0x%08llX): %s\n\n
Table 5–180
op_ESYNC_encode
Error while %s:\n  %s %s
read_resp_via_sock
psr-partition-number
DCS_BC0
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
## memapr %u 0x%016llX %d -> 0x%08X ...\n
MISC3
RF45
PROBED_USB_REQ_NODEVICE
astris_json_logger_get
BCR0_EL1+index
PARTNO_SWDP_M0P2
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
param.num_data_bp_regs.invalid.1
SAM
Fabric access is blocked. Expected if production unit, won't explore further.
KIS-SIM
{%s} drain_packets=%d [%s]
str != 0
CPU Name: %s\n
PMGR_OCLA_REGS
operator()
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
comparing against match entry [pid] %d: %s\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
timestamp
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
[AstrisAsync] Activating async...\n
param.tgt.null
n AHB Access Port.
ApProductionMode
PC
R13
haskis bit not set\n
ir-cmds
bypass-configs
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
astris_ide_get_pid
[ARM32cpu_t::_read_register64] 0x%08x\n
ret.write.msr_lock_reg
R0
Target ID: 0x%X\n
Subsystem Monitor Key does not exists: %s\n
param.wb.invalid.>wb_max
fn._write_special_reg.dbreakc1
CPU is halted
EPIREAD
codepoint <= 0x10FFFF
set.os
IBREAKA1
fn._init_configuration_by_name.failed
fn._read_pc
axlog_assert_upcall
v%s.%s
Stringify
setTargetOS
init_astris_api
ret.astris_disassemble_at_addr
astris_addr_which_die
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
Xtensa Option dbg_intr_level: %d
instr
fn._ocd_reg_r.ddr.t1_save
kisHubLoc
DISPSEC
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
get_tsz
Hang Radar Info:\n%s\n
pmu-name
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, scratch=%d, %d)\n
Unable to read LR
virtual int CPU_t::halt()
## memapw %u 0x%016llX 0x%08X\n
Invalid Size Given for AP AP=%d Size=%d
SAM2
Result while reading second entry: %s , entry val 1: 0x%X\n
symbol.check.loaded.AMAuthInstallSsoInitializePtr == NULL
Missing a comma or ']' after an array element.
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
astris_jtag_irscan_idle_impl
Register file 39
_ocd_reg_dcr_set
virtual_memory_bytes
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
KIS Writevals putting back the value
!!!! FILE RADAR: Don't know how to compare two values\n
_update_register32
{%s:%s@%d} [%s] reading CCSIDR\n
RF33
Shift-amount register
Xtensa Option ocd_address: 0x%llx
fn._read_general_reg
unable to write memory (using system ap)
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
INVPARM
Invalid object or key for engineer array
{%s:%s@%d} [%s] executing MRC\n
{%s::%s} %s pre_resumed\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
ret.CFReadStreamCreateWithFile
Re-Exploring...\n
Error %d (%s) while expanding ~ for Astris history save\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
Failed To Instantiate SOC From Booster\n
Dart Dart Type: %s\n
nullptr == soc_bm
    %s(): %s
{%s:%s@%d} GRPS[0] cached\n
unable to read memory (using system ap)
{%s=>%s} null reference to AXchip_t[0]
%s:%02X 
MAC16 Data register 3
astris_setup_ap_mem
R6
Can't get hardware model - failed to get property
Failed to write the write params @ 0x%08llX val: 0x%08X
Exception %d Stack Trace
invalid command
mismatch detected
probe %s on localhost
RTI
Both debug and xbs versions are set, maybe a bug: %s
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
astris_explore_ap_mem
\t%s\n
   Debug Port: SELECT %X: AVOIDED\n
Register file 20
fn._ocd_exec_instr.WSR.DDR.R1
fn._ocd_reg_w.ddr.value
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
AXchip_find_dap
Get
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
: [
AXcpu_lacc_count_clear
X12 Part
Re-Acquiring...\n
{%s:%s@%d} [%s] executing MRS (switched)\n
M4
astris_init_dp
n ARM SWDP Debug Port.
fn._ocd_reg_r.dsr.2
fn._ocd_exec_instr.TIECompleteRead
GetUint64
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
{%s} calling _collect_hw on %s
m_loaded_framework == NULL
Register file 38
unable to identify chip
!!!! Complex Key %s is INVALID !!!!\n
_a64cpu_raise_el_hw_safe
[INS_WP] 0x%016llx x %d\n
read memory (permission checks suspended)
AXcpu_clean_dcache
from
probe %s [port %u] on host %s
Logger internal is null
[PAW] Failed KIS Portal Access Preflight =%s (%d)
_write_internal
go
internal.enable-test.debut_auth == NULL
defaults.board.not_connected
, indicating this is a Cortex-M33 core
ret.write_reponse_and_check_authentication
fn._ocd_exec_instr.rfdo
UNKNOWN CMD
preflash_type
{%s:%s@%d} [%s] Failed To Enable BP Unit: %s\n
Std
Spew change. old=0x%016llX, new=0x%016X
\t[MATCH_FOUND] identified chip: %s
memap_bus_write
s != 0
CPU1 Status: %s\n
Unable to read GPR 28
{%s:%s@%d} [%s] \tCould Not Write System Argument, To Program Row Into Flash\n\n
Register file 60
UNKNOWN_PORTAL_ERROR
GetSize() >= count * sizeof(T)
astris_ide_get_soc_stop_clock
{%s:%s@%d} [%s] writing DRCR\n
ret.current_state_aarch64
fn._read_cpu_reg_file.regval
fn._write_special_reg.dbreakc0
port
CFG
astris_cpu.cpp
Failed to access new_cpu status
Polling Rom Status\n
Another application is connected to
Invalid port[%s] for probe %s provided by probe server
{%s:%s@%d} [%s] failed to read cfg reg: %d\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
Probe %s selected
CPU1
astris_batch_attitude_suspend
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
set_gpr
EPS3
cpu-ascdebug-offset
astris_cpu_mmu_configure
%s (%d)
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
connected
Failed to convert CFString to C String.
cpu-armv7m-regions
{%s:%s@%d} [%s] scanning out\n
Width: %d not supported
ret.get_hang_crumb
wrstn-pipes
{%s:%s@%d} [%s] writing ITR\n
{%s:%s@%d} [%s] \tCould Not Write Parameter 2 Into SRAM Base: %s\n\n
DCRCLR
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
astris_soc_release
_status_hw
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
ret.clear.async
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
_a64cpu_reset_catch
     0x%016llx: 0x%08x    %s\n
(addr=0x%llx)
authenticate_probe
ret.clearing-async
{%s::%s@%d [%s]} Error %s: resuming HW
DEMCR: 0x%08X -> 0x%08X
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_STATUS
IBREAKA0
setup_wp.not_halted
ASTRIS_ERR_NOTCONN
PROBED_USB_REQ_EMPTY
astris_ide_get_dbgwrap_aperature
ret.memap.read
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Error while %s:\n  Unable to connect to %s - %s
is.Peek() == 't'
AXjtag_explore failure - %s (%d)
astris_kis_poll_cfg_reg
SCODEC
_get_bpcr_hw
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
CTI_INT_ACK
AXcpu_cache_info
var.reg_srn.invalid.>=256
m_regstate.a64r_dspsr_el0
{%s::%s} waiting for EDSCR ITE
%02X 
ASTRIS_ERR_NOCPU
{%s} hostname:%s, flags:0x%08x
astris_select_probe
no debug bus AP present when expected
Invalid category name
cpu-armv7m-dmem-size
{%s:%s@%d} [%s] reading DFSR\n
[READ] cop %d -> 0x%08x\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
Failed to raise EL to %d to write register: 0x%llx
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Could Not Get SYS AP
Probe Type (%d) FW Version: %s does not support KIS.
copyBoardNameForPrimate
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
AXmemap_read_get_field
MAC16 data register 1
Register file 19
Register file 22
SoC
ACC-CTI
CPU.ARM7
ret.previous_authenticate.timedout
reg.ocd.dsr.invalid.not_cleared
Warn
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
No version information found in booster: %s
dfu-Type: %s\n
, indicating this is a Cortex-M0 core
internal.get-timer-count.debut_auth == NULL
fn._resume
==== Exception Trace ====\n
ret.reg.write.K_DA_REG_NAME_AUTH_KEEP_DECISION
ACCLO
Warning level
Probe %s status: Idle
cpu_readreg_vals
set.target_os
AXcpu_mmu_get_tsz
CPU has no regions, maybe powered off?\n
ProbeNav
Probe %s with unknown status %s dropped from available list
Schema validation failed at: %s (keyword: %s)
Parse
ret.read.spsr_elx
{%s::%s@%d [%s]} Error %s: initializing cache parameters
{%s:%s@%d} [%s] reading CCSIDR[L1-I]\n
AXcpu_translate_with_stage
PARTNO_1176JZFS
default
   Debug Port not responding (%s)\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
AuthBase_t::init failed (AuthDebug_t)
COMPARE2
fn._read_special_reg.debugcause
PROBED_USB_RSP_NODEVICE
DefaultConnectAddress
select_v2
%s%s
indicating a %s\n
_tie_write_word32
ASTRIS_ERR_USB_EMPTY
Key is null
result.read_vals(portal_group)==
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
{%s:%s@%d} [%s] \tFailed To Poll For SROM Status After Trying To Load Latch\n
arch_hw=%d
param.cpu_name.invalid.NULL
process (%s) (%d) path: %s
Encode
In Readflash\n
ApSecurityDomain
AuthDebugWithTimer_t destructor \n
ASTRIS_ERR_BLOCKED
{%s@%d} Connection to server failed, error=%d (%s)
cpu_lacc_status_remove
result.astris_identify_load_booster
Passed NULL plist file\n
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
EXPLORE_WITH_AVE
{%s} connectName[%s]
{%s:%s@%d} [%s] moving DSB to GPR 0\n
_a64cpu_is_current_state_aarch64_hw
X00 Part
Invalid data breakpoint index %d
Failed to open file for writing
KIS Readvals putting back the value
[1500] TAP %d missing required field 'chip-index' or 'irlen'
result.read_vals(group0)==
_write_memory_fast_try
DFR0_LO
Invalid reg_index %u
op_SDDR32_encode
ASTRIS_ERR_BADENV
{%s:%s@%d} [%s] setting GPR 1\n
n unknown type of Access Port.
read_settings
RF5
abort
Could Not Find Booster Entry Function: %s\n
General register 3
There is no debug port associated with this chip.
astris_user_default_remove_all_boardnames
RF6
fn._ocd_reg_r.DSR
operator[]
Failed to execute DRPS, in order to restore PSTATE after exception
Entry L%d %2u: [0x%08X] => AVOIDED\n
cpu_clean_l2cache
0 == Base::level_stack_.template Top<typename Base::Level>()->valueCount % 2
newpos == 0 || path_[newpos - 1] == '/'
Form-factor specific channel not found, falling back to generic channel for device '%s'
ret.enableAll
_read_memory_slow
{%s:%s@%d} [%s] performing single step\n
ret.raise_el.read
MemoryBlock_t
Disabled
AXcpu_translate_with_dart
_write_pc
empty USB packet encountered
CortexA5
ret.production_emulation
GRP_0
Breakpoint Index: %d
i16@?0^v8
Can't get hardware model - failed to allocate data buffer
NRF
Section 1 Offset: 0x%llX\n
[Timeout running ARM7 scan list]
ETB
ret.reg.write.K_DA_REG_NAME_ENABLE_PKA_VALID
shift=%d,opcode=0x%6.6X
Imago
wir-size
[SSTEP] bvr=%08x bcr=%08x\n
ret._handle_exception_for_el
     0x%016llx: ERROR\n
{%s} flags:0x%08x
{%s@%d} Timeout while attempting connect to server
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
chip-index
AXcpu_nmi
ret.reg.write.K_PKA_REG_NAME_DBG_CMD
addError
result.AXproduct_copy_bypass_info_for_bid
result.read.memap.s2r_fsm
_write_memory_slow
{%s::%s@%d} [FALSE] gpr[%d] != SP\n
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
WrProt
ret.erase_all_flash.srom_api.erase_all
exit.exception_test_1
[%s] TGE is NOT set. Traping to EL1 allowed.\n
%s (addr=0x%llx)
R14
_tie_read_word32
{%s} unable to allocate probe name
reflash_advanced
{%s->%s} exec: encode_msr(%s=0x%X, scracth=%d, %d)\n
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT || == SP\n
ban
Successfully connected to
dtoa
astris_conn_has_kis
ret.test.2.0
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
MESAVE
handle_pending_async_aborts
error trying to unlock MSR %s
{%s->%s} [is_64] exec: DRPS current_el(%d) -> target_el=%d \n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
HardwareWatch
JTAG
fn.AXmemap_read.address.regval
preconnect
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
MR1
_read_gpr
param.conn.user_defaults == NULL
ret.reg.read.K_DA_REG_NAME_SECURE_DOMAIN
RF54
ret.write_hang_breadcrumb
explore_pid_swd
extract
Clear (1<<1)
CPU DBG Ack: 0x%llx\n
Failed to find a plist for this soc %s
{%s::%s@%d} [FALSE] OP2 out of range [0x%08x]\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
{%s::%s} [%s] MMU not active - returning %s
Type:GenericVerif
cpu_writereg_vals
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
{%s:%s@%d} [%s] scanning out (DIDR)\n
vaddr
runBlock
fn._read_special_reg.dbreakc1
AP[%d]: JTAG_AP (Exploring Later) \n
## memapr %u 0x%016llX -> 0x%08X\n
param.no_dp
fn._ocd_reg_w.ddr.reg_val
probe %s on host %s
relay_get: %s = ERR
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s:%s@%d} [%s] updating DFSR\n
PortBridgeSWD
Before astris_kis_init_dp, CMDSTAT=%08X\n
Astris Source Version: %s\n
ret.rx-full.mddtr
EDSCR
ENABLED
internal.enable-timer-ovr.chip == NULL
AXchip_is_prod_fused
param.bp_info.invalid.null
[%s] Booster System Is Not Initialized\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp
{%s:%s@%d} [%s] setting GPR 0\n
createKey
AXcpu_lacc_count_remove
RF48
Can't get OS build version - failed to create plist
Bug
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
ret.read.edscr.masked
AMAuthInstallCreate
param.cpu_reg_file_size.invalid.2
_remove_data_breakpoint
ASTRIS_ERR_IGNORED
ret.ipc_poll_lock_status.read.ipc_lock
VBAR: %#llx\n
Switch back to primate KIS: %s\n
DESIGNER_ARM
PARTNO_SWDP_M23
, and bits [15:4] are 0xC60 indicating Cortex-M0+ core
internal.authenticate_probe.chip == NULL
JTAG chain not yet explored
param.descr==NULL
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
ECID is 0\n
Increasing length by: %d\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
SCANDEBUG
CortexM4
cpu-armv7m-imem-size
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
, but this manufacturer ID (bits [31:24] are 0x%02X) is unrecognized (MEM-AP read result: %s)\n
performing direct connect by port number
PoodleSWD
{%s:%s@%d} [%s] writing GPR\n
hwbp_disable
CPU-level (general and architecture-specific)
incr_drain_packets
ACQ_SAMPLE_SPI
buffer != 0
ParseFalse
Sprocket probe, for now I guess we will just say yes...\n
nothing written
Unable to connect after multiple attempts:\n%s,\n%s
SETCLR
GPR
ERROR: nothing to do; resuming address translation for %s without previously suspending it
LEND
ASTRIS_ERR_DISASM
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
GenericRegexSearch
RF40
.json
framework
write_register
val < 4294967295U
{%s} exec: DRPS_ENC\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
astris_setup_placeholder
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
Ticket Data is NULL\n
Reflashing Advanced\n
Creating a CCG3 Flasher to Acquire\n
XTENSAcpu_t
Xtensa Option num_high_pri_intr: %d
fn._ocd_exec_instr.rsr.reg_srn.t1
Probe Map comm error %d(%s) %s [%s]
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Incorrect hex digit after \\u escape in string.
{%s} FAILURE - NULL parameter
Register file 58
Table 5–148
```
