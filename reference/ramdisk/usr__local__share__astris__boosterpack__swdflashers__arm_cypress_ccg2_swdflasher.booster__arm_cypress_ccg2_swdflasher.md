# `/usr/local/share/astris/boosterpack/swdflashers/arm_cypress_ccg2_swdflasher.booster/arm_cypress_ccg2_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,806,432 bytes.

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
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
Unable to disassemble_at_addr 0x%016llx
%s status transitioned: %d ('%s') -> %d ('%s')\n
can't find bid in response\n
Setting bypass channel to: %d\n
[ARM64 INS_WP] 0x%016llx x %d\n
[REM_WP] wp%d\n
Async is disabled for current seesion
   Debug Port: SELECT %X; error: %s, retrying..\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
Optional Key: CPUMonitor not in preferences
{%s} valid response from bridge
Matched Booster: %s\n
{%s} m_exception_level(%d) != current_el(%d)
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
Error %d (%s) opening history save file
Init dbgwrap obj failed
The debug port associated with this chip has not been explored.
TAP IDCODE: 0x%X\n
{%s->%s} ERROR=%d(%s)
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
SoC must have a DAP
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[AstrisAsync] Failed to restart Async batch\n
{%s=>%s} null reference to AXconn_t record, `conn`
Can't get hardware model - failed to find matching IOService
Connected to Probe Device Server [Default Log]
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
Cannot create SoC [unknown chip identity (%d)]
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Sending DYN Bypas Channel Set: %d
[1500] Error parsing bridge: %s
{%s} Failed to extract PID from table (%d); continuing anyway
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
\tAligned Read Failed
In Writeflash\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Error %d(%s) executing instruction 0x%08X
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Invalid APTABLE (%d), so using most restrictive
{%s} status=%d being reported as Unknown
{%s} FAILURE - NULL parameter
Did Not Find Any Boosters For: %s \n
Found form-factor specific channel %u for device '%s'
Die Config Disabled\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
{%s} explore with exploreflags 0x%X complete [%d chip%s]
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Xtensa Core %s NOT configured\n
HOSTID=0x%x which is invalid, skipping orientation check
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
Could Not Allocate Info Keys Array
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
Complex Type: %s\n
[SSTEP] using BP %d\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
Failed to convert kisHubLoc %s to unsigned long long
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
{%s->%s} m_exception_level=%u
## armcpu: success status even though not all bytes read\n
Creating a PSOC6 2M Flasher to Erase\n
Failed to convert primateHubLoc %s to unsigned long long
Connection to server accepted
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Failed to get Bypass Config
Found the RTXCID Structure!\n
Unable to read CPSR
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
probetimeout retry failed logging as hang\n
Caught a portal that we dont have a status map for: %d
Stepping Stone Final =  %#x\n
Issuing request to Probe Map Server: %s
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
Probe %s status: Busy
%s SoC created
AXportal_t Is Not Valid Type - %d
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
[Auth Debug] Ticket Active, Debug Interface Locked\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
{%s@%d} Unknown CS command error [%d]
Failed To Instantiate SOC From Booster\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
[1500] TAP %d: irlen must be > 0 (got %d)
CPU0 Status: %s\n
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
Required Key-Value is a string, and not an array. Old booster found: %s\n
%s: not supported.\n
{%s::%s@%d [%s]} Error %s: synchronizing context
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
## dpw 0x%02X 0x%08X\n
Successfully Authenticated Probe\n
{%s[select]} timeout while waiting for data from the connection
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
{%s::%s} creating AP slave: name=%s
Invalid SoC Booster. SoC Booster Requires PID\n
[1500] Error parsing IR command: %s
Booster Value is Not String\n
Min Component - %s\n
{%s::%s} halting %s\n
[%s] {%s->%s} clear async abort
{%s} Failed to get watchpoint count for %s: %s
Kick off the current process using probe %s? (y|n)\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: collecting HW
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
CPU Monitor key does not exists for: %s\n
ERROR!! Couldn't save %s binary data\n
Probe %s with unknown kick response %s
DEMCR write failure - %s (%d)
CPU state %d
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s::%s} failed: %s
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s} 0 words requested for read at address 0x%016llX
Timed Out While Polling For Status\n
Initializing (%s) Booster's Astris API\n
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
replayPreflight
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
Probe %s with unknown port response %s
{%s} empty response string provided
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
{%s:%s}: cpu powered off: unable to access a register for this CPU
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
CPU Monitor[%i]: %s\n
Xtensa Option dbg_intr_level: %d
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
Dart Dart Type: %s\n
We Are Padding\n
1: ARM64_SYSOP_ATS12E1W\n
[REM_HWBP] bp%d\n
iter=%lu
      Read of JTAG-AP port %u PSTA failed with %s\n
[%s] %d -> 0x%08x\n
Invalid current AP (%d), adopting latest (%d)
Probe %s removed during selection process
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
Gathered:\n
CPU Supported in Runtime: %s\n
error %s reading DAP MPIDR
{%s::%s} ITE is not set: 0x%X\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
Proceeding with full explore instead of instantiation
Cypress PID: 0x%llX Not Supported For Advance Flash\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
using multi-target booster products_%s.plist
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
About to call fault reg latch, min_operating_el: %d\n
{%s::%s} write OK but took %d tries
{%s::%s} waiting for EDSCR ITE
   Debug Port has unknown type\n
Old ProbeDaemon does not support this command
--> psr        size=%3d bit=%d
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
AP Only Explore was asked for, stopping here
astris_romtable_pid Error: %s
[KIS] Register Index: %llu\n
Failed to get DFU Type
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
Can't get hardware model - failed to allocate data string
Probe %s Device Not Connected on USB-C Port
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Unable to read GPR %d
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Erasing All Flash\n
{%s} connectName[%s]
Could Not Match A Booster for %s\n
{%s} Failed to extract die infofrom table (%d); continuing anyway
{%s} Unable to read SP_EL0
collect_responses
{%s} Component ID read fail on romtable (%s)
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
** Unauthorized User/Network or ECID **\n
Failed to create CPU %s - %s\n
Size or Count provided are 0.
Reflashing\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
{%s::%s} EDSCR with RXO set - unable to recover.\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s} [%s] error %s from _synchronize_context.
{%s} pmgr status=%d being reported as Unknown
{%s=>%s} null reference to AXchip_t[0]
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
Complex CPU Name: %s\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
[INSWP] 0x%08llx wp%d rdwr=%X\n
{%s} _pre_resume_hw result = %s
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
Debug Clock Already Enabled
There is no debug port associated with this chip.
=== Found %s Boosters ===\n
Booster Bundle: %s\n
## dpr 0x%02X -> 0x%08X\n
{%s=>%s} AXconn_t has more than one chip
Error status from AMAuthInstallSsoEnablePtr = %i
Target ID: 0x%X\n
{%s} Unable to read CPSR
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s} Failed to single-step %s: %s
start rev is not of expected format; skipping cpu_desc override\n
\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
register lookup by name not supported when Astris is statically linked
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
User created bundle found, ignoring version checking via plist
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
[AstrisAsync] Activating async...\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
\tPrologue Aligned Read Failed
connection about to be destroyed
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
[KIS] Register Read/Write/Wrote: %d\n
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
%s given a NULL conn object
Awaiting response from Probe Map Server
\t[MATCH_TARGETID] FAIL <= unable to find DP
[1500] Error parsing bridge '%s': missing required field 'select'
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
{%s} asc status=%d being reported as Unknown
Probe Map Server Information: %s
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
{%s} Unrecognized component: %08X, class %02X\n
%s [RETRYING]
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s::%s} [%s] length=%u when width=%d
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Error Reading Device Production-Fusing\n
Creating a S1 Flasher to Flash\n
Hang Radar Info:\n%s\n
We are Allocating\n
product-name: %s\n
\tWriting 0x%08llX - 0x%08llX\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
DBGSTATUS = %08X   res=%d\n
Re-Exploring...\n
No version information found in booster: %s
pmu-name: %s\n
Invalid file name: \"%s\". File names must not start with '.'
{%s} no chip found
Chip Is Write Protected. Trying To Move Chip To Open Mode\n
Banana split probe, for now I guess we will just say yes...\n
Cleaning up Each Booster Manager\n
[1500] %s step %d: unknown instruction '%s'
   MEM-AP not enabled\n
{%s} read %d words from probe when %d words requested
{%s} Failed to extract ECID from table (%d); continuing anyway
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s} HDE not set on %s. Will re-enable.
[AstrisAsync] Barrier hit!\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
Error returned from explore_pid
JsonLogger: Loading schema for category '%.*s' from '%s'
error trying to unlock MSR %s
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s} Failed to get watchpoint mask for %s: %s
   Debug Port: SELECT %X: SKIPPING\n
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
Buffer is NULL
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
{%s=>%s} AXconn_t has no SoC object
Optional Key: SubsystemMonitor not in preferences
{%s} select success without file descriptor set
dfu-Type: %s\n
UPDATE cop64 %d -> 0x%016llx\n
{%s} FAILURE - malloc error
Probe %s removed prior to kick\n
invalid IR command '%s'
Cannot create complex descriptions from NULL info\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
Taking gateway control failed
JsonLogger: Created with default schema version '%s'
Chip Revision: 0x%X\n
## memapr %u 0x%016llX -> 0x%08X\n
=== Ending Gather and Clear ===
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s::%s} ERROR %d(%s) resuming %s\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s=>%s} no soc reference; falling back to direct cpu method
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
Failed to create Xtensa CPU %s \n
\t%s\n
Cannot create CPU descriptions from NULL info\n
probe event: %s
[FLUSH]\n
{%s} _halt_hw result = %s
Could Not Allocate Loaded Booster Array
bypass-config-name: %s\n
error %s reading DAP MMFR0
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
New Length: %d\n
Buffer Size Is Larger Than Flash Size: %d
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
[AstrisAsync] Got ASYNC_RESTART response!
AP given is not a MEMAP
AP[%d]: MEM_AP_AHB\n
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
CPU AP-Select: %d\n
{%s} setting up nameless target (address=0x%llx)
Found %d APs
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
\tTatsu AuthDebug Triage | All\n
{%s@%d} Unable to connect to server, %s:%d
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
[AstrisAsync] Pausing Async Mode\n
{%s} poll_srom_status is %s
{%s@%d} Received %d bytes when requested %d bytes [%s].
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
[HALT] Chip %x\n
CPU Address: 0x%llX\n
{%s->%s} current EL (%d) already == target EL.\n
{%s::%s} error %s writing EDSCR %s
In Preflash\n
Too many portals, we are at portal: %d while max is %d\n
Chip %x Status = %d\n
max_scan_bits is low: %d
%s probe[%s] from Probe Map Server [local host]
{%s@%d} Probe response payload read when no payload indicated.
[1500] run_steps: unknown instruction '%s'
Magic does not match: %#x vs %#x\n
Result while reading second entry: %s , entry val 1: 0x%X\n
Failed explore before forced KIS reset: %s\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Failed to convert CFArray to C Array\n
Could not write system argument param: %u error %s
Error closing %s [%d]
Had an error during transfer: %s
{%s} 0 words from probe when %d words left to read for reg %d
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
{%s} unmodified-probe_match = %s
no debug bus AP present when expected
--> extrawrstn %d
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s} error: %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
[AsyncSnapshot] #%zu: %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
Unable to register assert upcall %s (Insufficient memory)
\t\t%s\n
Invalid current AP (%d), adopting APTABLE (%d)
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
unable to create connection
Passed NULL plist file\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
{%s@%d} Failed to send probe command (error %d).
{%s} error %s at line %d
Erase All Flash\n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
2: ARM64_SYSOP_ATS12E1R\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
   Debug Port not responding (%s)\n
AP[%d]: JTAG_AP (Exploring Later) \n
      Select port %u: already explored..re-exploring\n
CPU %s already in the map with status: %d
DBGCTRL = %08X   res=%d\n
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
[PREFS] Key: %s - Val: %s
Could not write system request (SROM_SYSREQ_BIT | SROM_CMD_SET_IMO_48_MHz) error %s
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
{%s} connectName[local host]
Unable to allocate memory for big response
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
SoC has been setup using standard instantiation (setup result=%s)
{%s} Exploring with option: %s\n
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} [%s] MMU is already active - returning %s
## armcpu: bad status even though all bytes read (%d)\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Created Connection - : %s
Not Creating CPU: %s\n
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
Dart CPU SID(s): %s\n
{%s} category=%d
Going To Create Generic ARMV7m, but typehint is present (%s)\n
Breakpoint Address: 0x%llx
Failed to access new_cpu status
{%s} checking for single_port probe daemon on port %d
Probe (port=%d) with unknown status %s dropped from available list
replay_counter=%lu
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
{%s@%d} Timeout while attempting connect to server
We Are Matching Development Booster\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
CPU with %s Not Created via Name
Early dbgwrap base extracted: 0x%llx\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
## armcpu: success status even though not all bytes written\n
[CACHEOP] %d, 0x%016llx, %d\n
{%s::%s} [%s] error (%s) getting number of HW BPs
{%s} drain_packets=%d [%s]
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[PAR] Failed KIS Portal Access Preflight =%s (%d)
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
   {%s} (DP): status=0x%X(%s) - %s\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Connecting to server, %s:%d
Failed to convert CFString to C String.
CPU1 Status Not Valid\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
response == NONE; failed to get kis target info\n
{%s} probe_port = %d
{%s} probe device server closed the connection while trying to read data (at recv)
{%s::%s} %s pre_resumed\n
{%s} %s status is '%s' [Status Read %d times]\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
write to CMD/STAT failed - %s
Turning Debug Clock On
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Production Fused Device\n
  Error path [%s]\n
no system bus AP present when expected
Required Key-Value is a string, and not an array. Old booster found\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
Failed to allocate space for table!
{%s->%s} (top) current_el=%d
Booster System Is Not Initialized Bailing\n
{%s=>%s} null reference to CPU_t object, `cpu->state`
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
[1500] v2 plist missing required field 'taps'
Erasing all flash at once\n
Error happened when reading edscr. Retry #%i\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
Invalid Size Given for AP AP=%d Size=%d
Failed to explore chip: %d
SSO with no prompt being used
Error %d (%s) while expanding ~ for Astris history save\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s} set=%u (sh=%u), way=%u (sh=%u)
[READ] %d -> %08x\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
## dpw 0x%02X failed (%s)\n
Creating a 4200L Flasher to Erase\n
Unable to create pthread key for conenction. errno=%d %s.
Invalid character [0x%02X] received from Probe Map Server
Sprocket probe, for now I guess we will just say yes...\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
--> master     size=%3d localwrstn=%d debug=%d
!!!! CPU Key %s is INVALID !!!!\n
Unknown number of groups in the explore table; can't parse group attributes
{%s->%s} START handling exception
{%s} Found extra info in = %s, chopping string
relay_get: %s = CMD_ERR (%s)
[COLLECT] Chip %x\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
CPU Already Halted\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
choice: %d\n
comparing against match entry [pid] %d: %s\n
couldn't find CPU1. this is expected sometimes.
Could Not Get BoosterManager\n
%s\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
Breakpoint Index: %d
Xtensa Option options: 0x%x
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
{%s} Extracted CIP Gen Number from table  (%d)
Board ID: 0x%X\n
{%s::%s} timeout while waiting for EDSCR ITE
failed write of 0x%08X to DEMCR - %s
Could not enable KIS SoC Access\n
Re-Acquiring...\n
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
    %s(): %s
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
     0x%016llx: ERROR\n
Trying to use size of 8 on not AXI bus
   --> IDR: %08X\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
Failed To Init Booster's Astris API In: %s with %s (%d)\n
CPU Explore: 0x%llX\n
Required key: %s @ index %d is NULL\n
Stop Clock: %s\n
Map is empty, not removing CPU %s
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
\tReading left over chunk 0x%x @ 0x%llx\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
{%s@%d} Drain empty on decr [%s].
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
unknown match criteria type: %d
DEMCR read failure - %s (%d)
[1500] v2 plist missing required field 'bridges'
{%s} halting %s\n
{%s::%s@%d [%s]} Error %s: resuming HW
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Can't get hardware model - failed to allocate data buffer
connection created
CPU AP-Type: %d\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
SoC has been setup using standard instantiation (setup result=%d)
Booster:\n
Failed to find a product plist for this soc %s
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
{%s} NOMEM
AXjtag_srst deassert failure - %s (%d)
Could Not Find Any Loaded Boosters of Type: %s\n
Pages %d\n
Async is disabled for localhost connection
HOSTID bit not set\n
Protocol Version: 0x%X\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
tckrate_check returned error %s
{%s} host:%s, flags:0x%08x
{%s::%s} read OK but took %d tries
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
runBlock
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
   {%s} Enabling debug unit\n
AuthDebug::authenticate_probe - no need to authenticate\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
AXjtag_explore failure - %s (%d)
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
## armcpu: bad status even though all bytes written (%d)\n
   DPv3 baseptr is not valid (%X)\n
Chip Is In Open Mode\n
Can't get OS build version - failed to open ReadStream
Astris Version Set: %s
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
[KIS] CMD: %s \n
Asked To Write To A Negative Register Index
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
[WRITE] %d -> %08X\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
{%s@%d} Unknown CS code [%u]
Match Count is Zero. This is invalid.
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
[CLEANUP]\n
Xtensa Option num_wp: %d
Can't get OS build version - failed to create URL
{%s} %s: |%s|
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
Debug Base: 0x%llX\n
[READ] cop %d -> 0x%08x\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
Could Not Create Dictionary From Booster: %s
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Could not find portal by select %d, while interpreting result\n
    INFO(%u,%d): %s(%04u): %s(): %s
{%s} restored el is now %d
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Can't get OS build version - failed to allocate buffer
{%s}#%02X cmd: %s, resp: %s
getOrCreateValue: addMember failed, returning doc root
Exception %d Stack Trace
[REMWP] wp%d\n
{%s} Error setting up jtag-ap target (%s)
X06 Part
INFO: %s(%04u): %s(): err=%s(%d): %s\n
[REMBP] bp%d\n
 MEM-AP %X is hung\n
Probe %s USB-C location is %s
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
Got an error reading the DCM Control Register: %s
[%s] Booster System Is Not Initialized\n
Failed to convert %s key @ index %d to a number with base of %d\n
[1500] No %s.plist resource found
CPU0 Status Not Valid\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
Could Not Erase
Disconnected from Probe Map Server
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
[AstrisAsync] Deactivate while async is not active!\n
%s status is '%s'\n
Previous authentication in-flight, wait for it to finish\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
Set custom PSD json file: %s
Kick has been requested by probe server
Initializing Booster Layer\n
Complex CPU ID: %d\n
{%s} %s DC cache clean complete, marking as clean
AP[%d]: MEM_AP_APB\n
[Auth Debug] External Debug Interfaces Open\n
Failed to convert primateLoc %s to unsigned long long
relay_get: %s = %d
Could not find TAP at chip-index %d for v2 1500 config\n
AXjtag_srst assert failure - %s (%d)
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
{%s} handle ROM entry
{%s} Unrecognized Component: %08X (class %u)
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Polling Rom Status\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
!!!! Complex CPU Key %s is INVALID !!!!\n
Breakpoint Enabled: %s
{%s} Reading base 0x%llx entry's component ID
Probe Map comm: request[%s], response[%s]
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
\tLeft Over Chunk Read Failed\n
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Subsystem Monitor Key does not exists: %s\n
Creating a PSOC6 Flasher to Flash\n
Can't get hardware model - failed to create string
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Groups %d\n
{%s::%s} %s resumed\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
## apr %u 0x%08X -> 0x%08X\n
Could not find TAP at index %d to attach 1500 bridge to\n
gmtime() returned NULL, using epoch time
Could Not Find Booster Entry Function: %s\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
component group %d\n
[RESUME] Chip %x\n
SoC not identified by IDCODE - enumerating instead of instantiating
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Original Length: %d\n
Creating a S1 Flasher to Acquire\n
[DCC] Grabbing DTR failed: %s\n\n
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
[AstrisAsync] Discarding %zu completed command(s)\n
   Debug Port: SELECT %X: DISABLED\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Creating CPU With Name: %s\n
Table Size: %d\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
==== Exception Trace ====\n
%s constructed
{%s::%s} EDSCR with TXU set - unable to recover.\n
EICE chip %x initialized\n
[%s] %d -> %08x\n
VBAR: %#x\n
KIS Preflight No Need To Write to AP CSW
haskis bit not set\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
[%s] {%s->%s} Transitioning to exception level %u.\n
Unable to read GPR 28
Breakpoint Size: %d
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Failed to get KIS translator version\n
AXconn_t Struct Is NULL
Error status from AMAuthInstallSsoInitializePtr = %i
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
{%s@%d} neither socket nor kext connection available
no system bus AP present with AHB, trying AHB5
[KIS] Words (Read/Write/Wrote): %d\n
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
CPU PS-Register: 0x%llX\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
[AsyncSnapshot] No snapshots collected\n
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
Xtensa Option num_bp: %d
Can't get OS build version - failed to create ReadStream
Both debug and xbs versions are set, maybe a bug: %s
==== User Error Messages ====\n
Can't get OS build version - failed to get build version
{%s} strsep empty so match any probe [localhost]
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
Found another target for the plist\n
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
Aligned Address: %llx
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
OK: address translation suspended for %s successfully
OK: address translation resumed for %s successfully
type_hint not NULL, but creating a placeholder, this is off
\t[MATCH_FOUND] identified chip: %s
We are Deallocating\n
{%s} read ESR EL1|EL2|EL3 (%d)
## apw %u 0x%08X 0x%08X ...(%d)\n
      Explore of JTAG-AP port %u failed with %s\n
{%s@%d} Connection to server failed, error=%d (%s)
Could Not Find Any Boosters of Type: %s\n
Unable to read LR
[PREFS] Key: %s - Val: NULL
Xtensa Option non_tie_ranges: %zu range(s)
%2d) %s %s [Busy]%s\n
JsonLogger: Creating new category '%.*s'
Logging Context Is NULL\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s::%s} [%s] error %s writing SCTLR_ELx
{%s} host name(RSD): %s\n
setCategoryValue: path='%.*s'
Could Not Find a DCM Portal
using standard products.plist for %s
[1500] %s step %d missing required field 'instr'
{%s} Error reading PID (%s)
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
Creating a CCG3 Flasher to Acquire\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
%s probe[%s] from Probe Map Server [%s]
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
caller=%s, async=%d
Creating a PSOC6 Flasher to Erase\n
{%s} probe [%s] added to list
Connect using RSD not supported\n
{%s::%s} creating CPU
ERR: conn->nchips != 0; looks like chip is explored\n
Cleaning up Main Booster Object\n
Dart Name: %s\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
   Debug Port: Trying SELECT %X\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
--> localwrstn size=%3d debug=%d
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
   DPv3 bus is %u bits wide\n
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
{%s} invalid data width %d bytes
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
     ARM %s breakpoints: %u\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
Switch to primate res: %s\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Acquiring Chip\n
Failed To Request Chip ID\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
replay_counter=%lu, last_replay=%d
{%s} _pre_halt_hw result = %s
Creating a S1 Flasher to Erase\n
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Using 10pin connector skipping orientation check
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
[1500] Error parsing v2 bridges
X12 Part
Clocking To 48Mhz\n
register    %-15s %3u     \"%-s\"\n
sent %zd bytes to Probe Map Server when sending %zu
{%s} no matching 1500-to-* bridge
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
!!!! DART Key %s is INVALID !!!!\n
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
In Eraseflash\n
Dart Base Address: 0x%llX\n
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
Gathered Value is Not Number\n
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s} L2 cache operation completed [%s]
%s Bridge @ 0x%09llx-0x%09llx: %s
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
CPU: %s halting debug is now %s\n
[INS_WP] 0x%016llx x %d\n
Failed to sync prefs at beginning
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
outstanding=%zu
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
Die Config Disabled
   Debug Port: SELECT %X: AVOIDED\n
Gateway is KIS, seeing what probe this is\n
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Checking Write Protection\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
can't find pid in response\n
{%s} %s did not match any valid host
We are in clean up\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
AP is NULL
   DPv3 BASEPTR0 is 0x%08X\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
Connected to Probe Map Server
relay_set: %s -> %d
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
Using Built In CPUs\n
{%s} %s status failed. error: %d (%s)
[PREFS] Key: %s - Val: ??
Creating a CCG3 Flasher to Flash\n
{%s@%d} IOServiceClose failed, err = 0x%08x
TargetSel Before Disable: 0x%x
Multi target booster, checking for %s.plist\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[%s] {%s->%s} END handling exception
read_dbg failed to access R_v7M_CLIDR
   JTAG-AP: Identification = %08X\n
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} Class 9 ROMTABLE (nest=%d)\n
Complex Name: %s\n
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
Invalid file name: \"%s\". File names must be at least %d characters long.
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s} PRIMECELL [DONE]
   {%s} Read AP's R_MEMAP_CSW\n
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
[1500] TAP %d missing required field 'ir-cmds'
X00 Part
Creating a PSOC6 2M Flasher to Flash\n
Hardware model: %s
{%s} probe_match = %s
Skipping CPU %s at 0x%llx: not present in IDE\n
[%s] cop %d -> 0x%08x\n
Probe %s status: Idle
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
{%s} %s DC cache already clean since last halt, skipping flush
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
[AstrisAsync] Pause when already paused!\n
{%s} already collected %s, skipping
Hang Description:\n%s\n
Full JSON that failed validation:\n%s
CPU Typehint: %s\n
{astris_probed_print_events} not supported in this build configuration
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s} [%s] error (%s) getting number of HW WPs
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
AXconn or json_out are NULL
[%s] EL @ end of Collect: %d\n
Complex Address: 0x%llX\n
CPU %s not found or already removed from the map
[MEM] Uncompleted; DSCR = %08x\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
Failed to read IDE through DAP\n
{%s} Batch attitude key created for %p thread %#llx key %lu
Values Not The Type We Expected. Expected: Number and String\n
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
{%s} probe_host = %s
Awaiting next chunk of big response
Probe Map comm error %d(%s) %s
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
Can't find descriptor for group - can't index\n
TatsuServer Found: %s\n
{%s} unable to allocate probeInfo
Setting STOP CLOCK to TRUE
Original Content: 0x%08x
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
{%s} error %d(%s) reading data from the connection (at recv)
In Readflash\n
!!!! FILE RADAR: Don't know how to compare two values\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Going To Create Generic ARMV8\n
process (%s) (%d) path: %s
{%s}ERR: bypass_device_name is NULL\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
--> wrstn_wir2 size=%3d dpcsoc=%d
DBG_CPU: %s\n
Cached async_replay capability version: %u
{%s} DEVARCH read fail in CoreSight component (%s)
## memapr %u 0x%016llX %d -> 0x%08X ...\n
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
{%s} wrote %d words to probe when %d words provided in request
{%s} failed (%s)
Creating CPU Returned: %s\n
Failed to instantiate %s\n
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
Error %d(%s) executing instruction 0x%08X FAST
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
Failed AP read of R_MEMAP_CSW res: %i
   Created Fake Debug Port Debug Port
{%s} Failed to get breakpoint count for %s: %s
Generated JSON (first 500 chars):\n%.500s%s
Adding new booster path: %s\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
Connected to Probe Device Server [Log File %s]
Passed NULL booster without custom plist\n
%s %d\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
** \tTatsu AuthDebug Triage | All     **\n
{%s} hostname:%s, flags:0x%08x
{%s} unable to allocate probe name
{%s} unaligned %d-byte access at address 0x%09llx
Could Not Allocate Mutable Dictionary For BoosterMangers
{%s->%s}
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
Result while reading third entry: %s , entry val 2: 0x%X\n
{%s} Thread %#llx clearing key %lu
[ARM32cpu_t::_read_register64] 0x%08x\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
[AstrisAsync] Deactivating async...\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
{%s} Error reading CPUID (%s)
Error %d (%s) opening cmd snapshost save file
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
DEMCR: 0x%08X -> 0x%08X
[AstrisAsync] Activate while async is already active!\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
[INIT]\n
{%s::%s} cpu powered off: failed init() %s
--> misc_wdr   size=%3d wirtestporten=%d
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
%s: []\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
ERROR!! write binary data parameters invalid\n
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
Setting CPU %s is_boot_core to %d\n
Before astris_kis_init_dp, CMDSTAT=%08X\n
KIS Writevals putting back the value
Invalid Bundle: %s
Section 1 Offset: 0x%llX\n
Fabric access is blocked. Expected if production unit, won't explore further.
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
kext connect name %s\n
Error %s connecting to server %s:%s [RETRYING]
{%s} bridge returned DECERR
[KIS] Portal ID: %d\n
Extract Offset: 0x%X for %d\n
[%s] TGE is set so we traping to EL2\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[AstrisAsync] Async mode %s
Request Dict:\n%s
Found match - bypass_device: %s; channel: %d\n
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
Subsystem Monitor[%i]: %s\n
Creating a 4200L Flasher to Flash\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
{%s} %s: |%s|-|%s|
no debug bus AP present when expected; after sysap is NULL
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Found an async abort pending; clearing it\n
{%s} Error looking up architecture (%s)
{%s} Component ID read fail for 0x%llx (%s)
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
      AXap_write of R_JTAGAP_PSTA failed with error %s
{%s} found single_port probedaemon on port %d
Failed to convert kisLoc %s to unsigned long long
{%s} drop ProbeName %s
[KIS] Address: 0x%llX\n
Complex CPM Offset: 0x%llX\n
[MEM] Aborted; DSCR = %08x\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
Modified Word To Write: 0x%08x
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
--> debug      size=%3d acsr=%d
error %s checking for data abort(first)
Raising to EL2 cause in Guest\n
[AstrisAsync] Resume when not paused!\n
PKA Base: 0x%llX\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s} probeList has probeCount of zero
After powerup CMDSTAT=%08X\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
{%s} (end) current_el is now %d
[AstrisAsync] Barrier before pause\n
{%s} ROMTABLE (nest=%d)\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
JsonLogger: Writing category '%.*s' to '%s'
%s
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s} collect result = %s
Failed to find a plist for this soc %s
Erasing all flash a sector at a time\n
{%s::%s} [%s] unsupported width %d
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Koko probe, for now I guess we will just say yes...\n
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
Probe %s Device Does Not Have LocationID
relay_get: %s = ERR
Unable to convert plist file name to CFString: %s\n
     0x%016llx: 0x%04x      %s\n
[%s] CPU BM Not Found, Bailing\n
Increasing length by: %d\n
AXmemap_readvals failure - %s
\t%s (%s)\n
## ARM32cpu_t::read_register %u\n
[%s]\n
Failed To Erase All Flash
KIS translator version : %d\n
SOC AP[%d]: JTAG_AP\n
Unable to allocate memory for next part of big response
CPU (%s) has explore flag of: 0x%llx which is not set\n
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
Probe Type (%d) FW Version: %s does not support KIS.
{%s} _resume_hw result = %s
   Debug Port: SELECT %X: SKIPPING (%s)\n
Failed To Initialize Logging\n
=== Detailed %s Boosters ===\n
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
{%s} already connected
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
CPU1 Status: %s\n
Die Addr Info LSB: %d Mask: 0x%016llX\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
Result while reading first entry: %s , entry val 0: 0x%X\n
Failed to create optional file. Not fatal, moving on
Xtensa Option ocd_address: 0x%llx
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
Cannot create DART descriptions from NULL info\n
Failed to get PMU Name
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
probing %s status\n
KIS Readvals putting back the value
Dart Coastguarded CPU: %s\n
Component Group Offset: 0x%X\n
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
1: ARM64_SYSOP_ATS12E1R\n
failed read from DEMCR - %s
could not perform cpu_preflight
   JEDEC ID: 0x%08X\n
Could Not Get BoosterManagerUtility\n
Unable to read FP
     ARM %s watchpoints: %u\n
   Debug Base: %08X\n
   {%s} Clearing HNONSEC on AP \n
%s probe[*] from Probe Map Server [%s]
Probe Map comm error %d(%s) %s [%s]
relay_set: %s = CMD_ERR (%s)
--> cmd        addrsize=%d datasize=%d
Initial DSPSR_EL0: 0x%llx
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
WARNING, reserved / slide bits not zero! Zeroing out!\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
{%s[recv]} %d(%s) [RETRYING]
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
end rev is not of expected format; skipping cpu_desc override\n
CPU ASC Offset: %d\n
[%s] E2H is set, virtualization is supported\n
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
[AstrisAsync] Completing all async commands. Initial err = %d\n
Matched via Bundle ID\n
Value Types Are Not Strings\n
We are at max iterations, still didnt get full JSON
Gateway Version: 0x%X\n
[SSTEP] bvr=%08x bcr=%08x\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
Highest EL: %d, -- Min Op EL: %d
{%s::%s} creating placeholder for CPU: name=%s
Could Not Allocate All Boosters Array
\tLeft To Read (%d) < width (%d).\n
=== Starting Gather and Clear ===
{%s} FIFO full, try again
{%s} Failed to extract portal info from table (%d); continuing anyway
codeblock
X09 Part
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
{%s::%s@%d [%s]} Error %s: initializing cache parameters
Switch back to primate KIS: %s\n
Could Not Allocate Booster Location Array
Unable to read SP
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
Dumping Process Tree
Previous attempt to connect to probe failed: %d (%s). Retrying...
Selecting polling method %s
{%s} match any probe [localhost]
## apr %u 0x%08X %d -> 0x%08X ...\n
[%s] chipinfo is NULL
Previously dumped the process tree, skipping
error %s reading DAP PFR1
ERROR: unable to resume translation for %s
## dpr 0x%02X failed (%s)\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
{%s} %s
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
Enabling USB Gateway
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} flags:0x%08x
[KIS] Portal Status: 0x%X\n
ERROR - Cypress Flash Failed (%s)
{%s::%s} NULL parameter
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
Failed To Acquire Chip\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s::%s} [%s] !bpwp_initted, retrying init
probetimeout retrying access...\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
The log file has been updated with all available diagnostics.\n
CPU DBG Ack: 0x%llx\n
\nERROR - Cypress Flash Failed (%s)
VBAR: %#llx\n
Variables not setup
      Select of JTAG-AP port %u failed with %s\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
--> 0x%02x = %s
\t\tARMv6 debug CPU xxx ID\n
Translate Stage Chosen: %d\n
{%s} Error setting up memap target (%s)
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Changed Write Protection To Open, Resetting and Reacquiring Chip...\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
CPU Subsystem: %s\n
batch_cmd_count: %d
Failed to sync prefs at end
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
Xtensa Option reg_file_size: %d
Can't get hardware model - failed to get property
!*!*!* ****************************************************************************** !*!*!*
DHCSR write failure - %s (%d)
## memapw %u 0x%016llX 0x%08X\n
%s construction failed
SOC_t::{%s} CPU_t group=%d when group 0 expected
Failed to convert %s key @ index %d
{%s} Failed to extract CID from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Replacing key with value
   CPUID: 0x%08X\n
[%s] AP, DP, or chip given is NULL
   {%s} Probe requires overrun detect mode.\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
   {%s} Before powerup CMDSTAT=%08X\n
First Erase Failed, Lets Reset and Try Again\n
Init objects failed
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
!!!! Complex Key %s is INVALID !!!!\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
Creating a PSOC6 Flasher to Acquire\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
\tWriting 0x%08llX - 0x%08llX -> Row %u\n
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
%s NOT configured\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
SoC does NOT support IDE Explore\n
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
ERROR: nothing to do; resuming address translation for %s without previously suspending it
{%s} Debug Base: %08X
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Hang Address: 0x%016llx\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
      Read of JTAG-AP port %u CSW failed with %s\n
Probe Map name of probe %d is: %s
{%s@%d} gethostbyname failed, error=%d (%s)
sending abort to clear a timeout\n
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
{%s} timed out waiting for cpu to halt during collect
Width: %d not supported
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
%s probe[*] from Probe Map Server [local host]
dbgwrap halt failed, falling back to classic method
Spew change. old=0x%016llX, new=0x%016X
start rev and/or end rev is NULL; skipping cpu_desc override\n
AP[%d]: MEM_AP_AXI\n
Problematic JSON value:\n%s
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
{%s} bridge returned SLVERR
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
SSO info present but SSO disabled.
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
received %zd bytes from Probe Map Server when have %zu
comparing against match entry %d: %s
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
Start Page: %d\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
Can't get OS build version - failed to create plist
OS build version: %s
Abnormal %s termination: Assert Area Mask = 0x%016llX
Please answer y=yes or n=no.\n
{%s} bridge returned an error
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
{%s} Failed to resume %s: %s
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
Type 'jebdump' to do scan/mem dump\n
%s: chip was NULL when attempting to release soc
Could Not Get Bundle Out Array of Found Boosters\n
Complex ID: %d\n
{%s::%s@%d [%s]} Error %s: checking exception
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Reading Chip ID\n
Can't get hardware model - failed to convert to C string
Explored\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
pc:  0x%16s cpsr: 0x%16s %s\n
\tReading left over chunk expected 0x%x got 0x%x\n
Cypress PID: 0x%llX\n
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s@%d} Received %d bytes when requested %d bytes.
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
Die-Count: %d Current-Die: %d Die-Type: %d
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
successfully updated DEMCR
      Select port %u: AVOIDED\n
Warning: chip exploration did not complete successfully (%s)\n
Successfully Authenticated DFT\n
{%s} skipping dcache flush, cache already clean
SWDACKDELAY relay write failed\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
{%s[select]} %d(%s) [RETRYING]
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
coalesced-target: %s\n
Unable to read PC
dropping empty probeInfo (port=%u)
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Failed to init from cpu desc armv7m cpu: %s \n
Could Not Get SYS AP
Failed to read ide_table from KIS explore
[HALTED] dfsr = 0x%08x\n
Asked To Read A Negative Register Index
CPU Supported in Integration: %s\n
CPU Core Number: %i\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
[AstrisAsync] Resuming Async Mode\n
AXportal_t Struct Is NULL
=== Loaded %s Boosters ===\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
Initialized Logging - %s
{%s} no response from bridge
AuthDebugWithTimer_t destructor \n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
{%s} no TAP detected that supports 1500
BoosterManager Types:\n
[AstrisAsync] replay preflight: Async not active!\n
first read of CMDSTAT may fail if external reset occurred
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
{%s} unable to find single_port probedaemon on port %d
Commit Code: 0x%X\n
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Length is 0
Probe %s with unknown status %s dropped from available list
%2d) %s %s%s\n
Choose a device: 
[1500] Using %s.plist
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
{%s} FAILURE - max length exceeded
Connected toProbe Map Server (single_port) 
{%s} %d(%s) [RETRYING]
Reflashing Advanced\n
Portal Group Offset: 0x%X Entries: %d\n
Exploring IDE in JTAG\n
   Setting up AP IDR %08X\n
SSO is DISABLED\n
Probe %s Device Server listening on port %d
{%s} Error %d(%s) sending message
{%s@%d} Found cached response
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
{%s} host = %s
{%s@%d} socket connection is not available
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
1500 IR Commands:
## apw %u 0x%08X 0x%08X\n
We are done with clean up\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
2: ARM64_SYSOP_ATS12E1W\n
astris_get_async_ver failed with error: %s
CPU has no regions, maybe powered off?\n
[Auth Debug] Disabled\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
{%s@%d} Failed to find cached response
Could Not Find Any Boosters\n
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
Initialized %d 1500 bridges\n
{%s} unsupported bridge type for %s
[READ] cop64 %d -> 0x%016llx\n
     0x%016llx: 0x%08x    %s\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
Error while trying to authorize: %d - %s\n
%s %3d'b%s\n
AP[%d]: unknown type\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
No 1500 bridges specified\n
** Add the --with-force option or use the explore_override console command **\n\n
USER %s(%04u): %s(): %s
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
read failed, using old cached as base: 0x%x
Explore: %u chip%s\n
error %s checking for data abort
DCCCTRL = %08X   res=%d\n
ERROR!! Wrote %zd bytes, expected %zd\n
  Nested path: parent='%s', child='%s'
Invalid value for 'entry' tuple element - can't index
[READ] %d -> 0x%08x\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
{%s} ROMTABLE (dbgbase=0x%llx)
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
Using Built In SoCs\n
CPU Die: %d\n
caller=%s, async=%d, iterations=%lu
There is no system bus access port on the debug port
Valid Portal
Gathered Info:\n%s
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
%#09llx-%#09llx: %s\n
Booster Info:\n%s
{%s} Failed to get breakpoint mask for %s: %s
Creating a 4200L Flasher to Acquire\n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Got an error writing 0x%X the DCM Control Register: %s
[1500] Detected plist version %d
error %s checking for data abort(uint32_t)
{%s} calling _collect_hw on %s
   ROM entry %d (level %u): AVOIDED\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
Failed to Identify & Explore Chip via KIS: %d (%s)\n
Preferences does not exists: %s, creating one.\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
Xtensa Option num_high_pri_intr: %d
{%s:%s@%d} Critical error encountered:
Portal Status, Changing STATUS and CMD/STAT to reflect
Probe %s selected
\t[MATCH_SKIP] skipping entry
{%s} bridge timed out
Astris Source Version: %s\n
XBS Version Modified: %s -> %s\n
{%s} %s resumed\n
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
KIS Chip Found, Doing KIS Explore Setup
JsonLogger: Wrote %zu bytes to '%s'
[1500] Error parsing TAP description
{%s} DAP command nwords=%d trimmed to %lu\n
Creating a CCG3 Flasher to Erase\n
Probe %s LocationID Info is %s
{%s} %sing word #%d at address 0x%09llx: %s
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s::%s} [%s] MMU not active - returning %s
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
ERROR: unable to suspend translation for %s
   Debug base is in legacy format\n
{%s:%s@%d} Critical error [radar already requested]
In Postflash\n
** CPU %s requires forced explore override flag on this SoC **\n
{%s}#%02X %s [%s]
[%s] Booster System Is Not Initialized Bailing\n
CCG Acquire Sequence Failed - %s (%d)
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
New format for cip gen register, unsupported: %d\n
{%s} [%s] m_exception_level=%u\n
{%s::%s} [%s] error %s reading SCTLR_ELx
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
{%s@%d} Connection to server rejected, error=%d (%s)
CPU Name: %s\n
Portal Group Base: 0x%llX \n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
checking if relay \"%s\" is valid
JsonLogger: Schema loaded successfully for category '%.*s'
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
{%s} explore with exploreflags 0x%X completed with error [%s]
Successfully Authenticated\n
{%s} handle ROM entry %d (level %u): %08x
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
[1500] IR command '%s' missing required field 'opcode'
   {%s} select %u port %u: %u chip%s\n
Probe %s removed before port determined\n
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
Successfully connected to server, %s:%d
{%s@%d} Timeout while sending probe command.
SoC BM Not Found, Bailing\n
Could not find bundle () in given array: %s\n
unable to identify chip
No 1500 bridges or TAPs specified (v2 plist)\n
Bundle: %s NOT FOUND\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
unable to obtain sysap
[1500] TAP key is not a valid integer
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
     ARM %s debug CPU rev %d\n
{%s=>%s} AXconn_t has no chips
Creating a CCG2 Flasher to Flash\n
{%s@%d} Unable to create socket
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
Going to do imago workaround\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
[ANAMOLY] Could not find AXcpu_t object for CPU\n
[1500] Error parsing bridge '%s': missing required field 'tap'
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
Wrong width, should be either 4 or 8\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
Creating a PSOC6 2M Flasher to Acquire\n
Category is null
mempool-dmem-offset-reg
{%s::%s@%d [%s]} Error %s: resuming HW
Failed to write register: 0x%llx val: 0x%llx
fn._return_from_debug_interrupt
op_RSR_encode
No probes were found matching
postconnect
{%s} Failed to get watchpoint count for %s: %s
AXdebug_auth_is_dft_authenticated
fn.local
ret.modify.edscr.~a
storeNickname
   DPv3 bus is %u bits wide\n
program_row
Memory error status register
RF41
operation not supported
Connection aborted: kick required for probe %s.  Received eof in stdin
{%s:%s@%d} [%s] writing GPR\n
!!!! Critical Error: m_exception_level[%d] == 0|1|2|3 !!!!\n
Error while trying to authorize: %d - %s\n
OCD Debug data register
s0=%d,ar=%d
DBGWRAP_PAUTH
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
SSO is DISABLED\n
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
file_type
Invalid Bundle: %s
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
can't find bid in response\n
wrstn-reg
fn.entry
kon
ret.call_srom_api.poll_srom_status.scratch_addr
_invalidate_icache_all
hwbp_enable
OK: address translation suspended for %s successfully
PKA Command Verify Completed, No Errors, but Enable Valid Not Set
file
Encode
no enable slot available
Parameter len = %d > 64.
firmware version is too old DEPRECATED
Unable to allocate memory for big response
CPU.ARM7
n AHB Access Port.
AuthDbg,SecurityDomain
Long Packet
ERR: conn->nchips != 0; looks like chip is explored\n
~
localwrstn-debug
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
resident_memory_bytes
buffer != 0
param.halt_group == NULL
DHCSR write failure - %s (%d)
product-name: %s\n
_set_bpcr_hw
AuthDbg,EnSecureTestExternal
EPC6
data_reg=%u,opcode=0x%6.6X
got a translation error translating VA to PA
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
ret.m_lam.paccess_read
PC
param.invalid.reg_file_index.outofrange
Commit Code: 0x%X\n
resolve_debug_components
entry.exception_test_1
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
RF4
{%s} couldn't set thread specific - %s\n
{%s@%d} Failed to send probe command (error %d).
result.read_vals==
astris_cpu_mmu_get_config
General register 3
param.address.invalid.>max
New
Timed Out While Polling For Status\n
param.bp_index.invalid.outofrange
ASTRIS_ERR_TOOMANY
general error reported by probe
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
defaults.nickname.too_long
ret.reg.read.K_DA_REG_NAME_PKA_BASE_HI
interface not in appropriate state for action
%d
cpu-xtensa-dbg-intr
dfu-type
{%s:%s@%d} [%s] reading DSCR\n
PowerOff
PRID
astris_kis_clear_status_registers
CPU1 Status Not Valid\n
src_gpr <= 15
{%s::%s@%d [%s]} Error %s: initializing cache parameters
OPEN
PARTNO_SWDP_M0P2
start rev and/or end rev is NULL; skipping cpu_desc override\n
astris_kis_cfg_readvals
!!!! Critical Error: current_el[%d] == 1|2|3 !!!!\n
AddMember
data-size
{%s:%s@%d} [%s] executing STRBpi\n
EL0t
DoCopyMembers
ret.acquire_chip.get_cpu
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_armdap.cpp
_log_setup_thread_specific
ide_checker
CurrentContext().valueSchema
[%s] cop %d -> 0x%08x\n
SP_EL0
%016llx
fn._write_mem.length.incorrect
base
CACHE
AuthDbg,ECID
Invalid hostname or port specified as
No loggers container
getOrCreateObject.messages
timestamp
{%s} FIFO full, try again
[KIS] CMD: %s \n
ret.call_srom_api.poll_srom_status.ipc_struct
{%s->%s} exec: encode_mrs(scratch=%d, MDDTR_EL0, true)\n
init_hw.read.dhcr
unable to read memory (permission checks suspended)
internal.is_dft_authenticated.chip == NULL
INVMODE
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s->%s} START handling exception
astris_jtag_get_pipe_cycles
var.num_loops.invalid>3.curr_instr
probe %s on host %s
ret.ipc_poll_lock_status.read.ipc_lock
ret.read.edscr.masked.beginning
astris_findidcode
%s%d
Unspecific syntax error.
{%s:%s@%d} [%s] doing IR scan (DIDR INTEST)\n
ExampleValue
RF2
RF23
Koko
{%s}#%02X %s [%s]
nameBuffer_ == 0
MA
buf != 0
ret.getSubsystemEnableStatus
Creating a 4200L Flasher to Flash\n
Table 5–172
ITLBCFG
fn._write_window_base
NoSOC
Generated JSON (first 500 chars):\n%.500s%s
Got an error writing 0x%X the DCM Control Register: %s
ret.reg.read.K_DA_REG_NAME_PRODUCTION_MODE
VECBASE
ret.dspsr_el0
ESR_EL3
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
instance
{%s:%s@%d} [%s] executing STRpi\n
{%s::%s} [%s] error %s writing SCTLR_ELx
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
Didnt read back the expected amount (actual: %d != expected: %d) on row between: 0x%08llX - 0x%08llX\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
cpu did not stop. OCD.DSR=0x%8.8X
Can't get OS build version - failed to create ReadStream
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s} category=%d
Length is 0
, and bits [15:4] are 0xC23 indicating Cortex-M3 core
_write_pc
soc or sysap not available
elapsed_seconds
AXcpu_lacc_pipe_set
Warning: chip exploration did not complete successfully (%s)\n
Type:OptimoDE
Table 5–186
setTargetInfo
ret.reg.read.K_PKA_REG_NAME_DBG_STATUS
{%s:%s@%d} [%s] reading PRSR\n
Breakpoint Index: %d
wb_u32=%u
not connected
deinit
, indicating this is a Cortex-A8 core
param.ticket_data == NULL
{%s} asc status=%d being reported as Unknown
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
_remove_data_breakpoint
_ocd_reg_dcr_clr
Probe %s Device Does Not Have LocationID
AXbooster_interface_init_astris_api
ret.call_srom_api.write.callid_params
op_LDDR32_encode
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
param.sys_addr == nullptr
AXmemap_readvals failure - %s
Could Not Get Bundle Out Array of Found Boosters\n
storeBoardName
General register 5
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
Error %s opening single_port connection to probe server
LMFLASH
IsArray()
CPU Name: %s\n
ARM32cpu_t
{%s} pmgr status=%d being reported as Unknown
RF35
Register file 54
fn._read_snr.exccause
AXchip_production_emulation_enable
ret.alloc.soc_key == NULL
fn._ocd_reg_w.ddr.value
Raw level
Unaligned Access
ASTRIS_ERR_PROBEERROR
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
[%s] E2H is set, virtualization is supported\n
Invalid current AP (%d), adopting APTABLE (%d)
Type:DbgComponent 
_remove_watchpoint
{%s:%s@%d} [%s] unable to drain response\n
CopyFrom
Found an async abort pending; clearing it\n
{%s} Unable to read CPSR
fn._ocd_exec_instr.xsr.ddr.t1.2
plist
collect-probemap
DCS_BC6
all
astris_batch_attitude_resume
far_el3
hwbp_remove
read memory (permission checks suspended)
top-level ROM Table
param.reg_name.invalid
astris_remove_loaded_cpu_boosters
ir-cmds
ret.exec.msr.scratch->mddtr
{%s} restored el is now %d
RF47
Abnormal %s termination: Assert Area Mask = 0x%016llX
unable to read memory (using system ap)
ret.read.ecid
Creating a PSOC6 Flasher to Acquire\n
RF20
fn._setup_data_bp.wp_state
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
AXcpu_hwbp_insert
OS build version: %s
ASTRIS_ERR_NOTCONN
ApProductionMode
_ocd_enable
Can't get hardware model - failed to find matching IOService
STATUS
!!!! Critical Error:  dlr_el0 NOT CACHED !!!!\n
_clean_dcache_setway
[%s] m_dc_max_level %d, m_ic_max_level %d\n
ret._mmu_init
astris_memap_debug_readbuf
TIMEOUT
{%s:%s@%d} [%s] \tCould Not Read System Request Register While SROM Status Polling\n\n
HCR_EL2
EDWVR0+index
%s probe[*] from Probe Map Server [%s]
JSON structure error: key '
ipc_poll_lock_status
astris_ide_is_component_present_at_addr
ret.modify.edscr.~ma
ret.read.edscr.after-drain
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, %s=%d, %d)\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armv7mcpu.cpp
read memory
/System/Library/CoreServices/SystemVersion.plist
select
!!!! Critical ERROR: current_el[%d] != m_exception_level[%d] after exeption handling
CTI_INT_ACK
{%s:%s@%d} [%s] reading CCSIDR[L1-D]\n
HardwareStep
Erasing All Flash\n
Misc register 3
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
astris_kis_cfg_readvals_swd
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
ret.clear_edscr_err
copyNickname
\tLeft To Read (%d) < width (%d).\n
_read_general_reg
fn._write_special_reg.srn.regval
fn._ocd_reg_w.dcrclr.regval
{%s:%s@%d} [%s] reading PAR[64]\n
Enabled
Cause of last debug exception
High level 6 exception PC
Table 5–173
Misc register 1
astris_probeV2_list
v8@?0
UNKNOWN
DCS13
virtual int ARMv6cpu_t::read_dcc(int *, uint32_t *)
fn._read_cfg_reg_0
_create_cpus
SoC
explore-level
{%s} Failed to extract component info from table (%d); continuing anyway
Cached async_replay capability version: %u
ret.set_spmi_interface
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
maxDecimalPlaces >= 1
Reserve
{%s:%s@%d} el[%d] == m_exception_level[%d]\n
Exception occured after executing MRS to bounce through scratch register
defaults.get.nickname.not_connected
EXPLORE_WITH_SEP_DEBUG
, indicating Component Class == ROM Table
AMAuthInstallGetLocalizedStatusString
ret.CFPropertyListCreateWithStream
connecting to Ethernet probe
FPB
read_register
DEDICATED
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
astris_soc_check_debug_root
reader.h
PMS
OFFLINE
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
set.os
complex-id
tap
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
ret.storeNicknameForKey
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
cpu_swbp_info
AXbreadcrumbs_clear
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
resolve_portals
AXchip_is_prod_fused
Failed to create optional file. Not fatal, moving on
astris_json_logger_init
hwwp_remove
astris_setup_jtagap_target
AXjtag_scanout
, and bits [15:4] are 0xC20 indicating Cortex-M0 core
AXdebug_auth_authenticate_dft
%s/%s-%s%s%s.bin
chimp
0123456789abcdef
result.dbgap==NULL
MISC3
Table 5–149
Table 5–138
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
address=0x%8.8X, len=%u, rdwr=%d
ASTRIS_ERR_USB_PROBED
RF29
allocator_
version
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
AXcpu_hwwp_remove
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
R8
Hang Description:\n%s\n
ARMV8
json
ret.reflash.erase_all_flash
1
{%s=>%s} null reference to AXchip_t[0]
data_.o.size > 0
(system_reg & (0x40000000 | 0x80000000)) != 0
AuthDbg,TicketIdentifier
RaspberryPi3_t
Address formatting failed
setTargetOS
Passed NULL booster without custom plist\n
D0-PKA
{%s:%s@%d} ARM64-specific _sstep method not currently supported\n
init_hw.pid0
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
vvvvvvvvvvvvvvvvvvvv DUMP OF HISTORY LOG vvvvvvvvvvvvvvvvvvvv
AXconn_hostname
Failed to convert kisLoc %s to unsigned long long
esr_el2
instr != 0
EL3h
PARTNO_SWDP_M33
cpu_mode
_read_pc
name <= nameBuffer_ + length
output_type
Failed to execute DRPS, in order to restore PSTATE after exception
Table 5–171
PROBED_USB_INUSE
MCORE
[AstrisAsync] Deactivating async...\n
indicating a %s\n
Register file 50
fn._ocd_exec_instr.TIEInitiateReadProtectedI
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Invalid object or key for engineer array
Complex CPM Offset: 0x%llX\n
GROUP
Processor status
xtensa-non-tie-range-name
astris_preferences_subsystem_monitor_list
Table 5–132
DEBUGCAUSE
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
document.h
ret.cpu_status.check_vect_catch
astris_apread
Connection aborted: kick required for probe %s
setEnvironmentInfo
relay
CPU PS-Register: 0x%llX\n
extract
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
{%s} Unrecognized component: %08X, class %02X\n
#ch-
Choose a device: 
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
        PID[23:20]       is 0x%01X (revision)\n
PublicCypressFlashAPI
fn._tie_read_word32.last
getOrCreateArray.generated_files
Match Count is Zero. This is invalid.
ret.read.edscr.ma-mode
{%s=>%s} AXconn_t has no chips
Type:GenericIP
[Auth Debug] Disabled\n
reg_addr_offset=0x%4.4X, m_ocd_base_address=0x%8.8X
astris_gather_poral_error_info
Setting STOP CLOCK to TRUE
transact
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
1: ARM64_SYSOP_ATS12E1R\n
Gone
RF1
virtual int ARM7cpu_t::_resume_hw(bool)
%s: []\n
read failed, using old cached as base: 0x%x
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
{%s:%s@%d} [%s] \tCould Not Write Request To Register To Erase Flash\n\n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llX) - reg_count=%d - val=0x%X
cpus
cpu-xtensa-ocd-base
HENRY
m_regstate.a64r_dspsr_el0
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
group=%d
    %s(): %s
{%s:%s@%d} [%s] Address must be aligned to length\n
_write_window_base
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
cpu_cache_info_group0
shared_->refcount > 0
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
AXcpu_status
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
end rev is not of expected format; skipping cpu_desc override\n
Clear
set.hostname
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
RF45
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/xtensa_cpu/xtensa_cpu.cpp
var.reg_srn.invalid.not_present
Failed to open file for writing
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
baseReg
SoC not identified by IDCODE - enumerating instead of instantiating
General register 13
ASTRIS_ERR_BADPROTOCOL
Misc_CortexM_AHB5
ret.dfu.dcm.reset
KIS Readvals putting back the value
unswitch_regset
Failed to write SPS_EL%d
ret._set_wpcr_hw
{%s::%s} [%s] error (%s) getting number of HW BPs
AXchip_getinfo
fn._write_mem.bp_info
localwrstn-size
{%s:%s@%d} [%s] reading GPR 1\n
L2
ret.reg.read.K_DA_REG_NAME_SECURE_MODE
Table 5–185
\"%s\" not a special register
fn._ocd_exec_instr.rsr.ddr.data_reg
;
AXbooster_print_boosters_detailed
astris_ide_get_pid
{%s} set=%u (sh=%u), way=%u (sh=%u)
~MA
AXcpu_cache_cleaninv
astris_dpabort
name %d
MemberBegin
vector
PPM
_write_memory_fast
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
AXcpu_getinfo
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
EXPLORE_JTAGAP
CypressFlasher_CCG3
error %s reading DAP MMFR0
[CACHEOP] %d, 0x%016llx, %d\n
M23
astris_create_ap_slave
[%s] chipinfo is NULL
AXdebug_auth_get_dft_timer_count
param.shift.invalid.out_of_range
Caught a portal that we dont have a status map for: %d
OSLAR_EL1
{%s} already collected %s, skipping
fn._ocd_reg_r.DDR
ASTRIS_ERR_NOTEXPLORED
ASTRIS_ERR_PENDING
{%s} connectName[local host]
Taking gateway control failed
Failed to exec MRS to bounce sysreg into scratch register. scratch=%d, sysreg=0x%X, regname=%s
INVALID KIS VERSION
internal.clear-auth.chip == NULL
Could Not Erase
fn._ocd_exec_instr.s16i.r1.r0
Probe %s USB-C location is %s
GetSize() >= count * sizeof(T)
rhs.IsString()
AXportal_t Struct Is NULL
_get_bpaddr_hw
vaddr
Crash level
BeginValue
outCount != 0
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
fn._write_cpu_reg_file.regval
param.length.invalid.null
op_RFDD_encode
Probe %s removed before port determined\n
\t%s (%s)\n
{%s:%s@%d} [%s] reading CPSR(1)\n
error %s reading DAP MPIDR
{%s:%s@%d} [%s] Setting WP length not currently supported: %u\n
param.tgt->ap.null
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
backtrace
runBlock
receiving response
static_cast<void*>(this) != static_cast<void const*>(&rhs)
preflash_type
Took an exception in EL%u, esr = 0x%08llx, category = 0x%llx\n
AMAuthInstallRequestSendSync
write_register
instruction size too large
{%s} 0 words requested for read at address 0x%016llX
astris_server_connect
CPU Subsystem: %s\n
DCS12
{%s} [%s] m_exception_level=%u\n
Set Requests in INTERRUPT
_get_arch_hw
ASTRIS_ERR_USB_EXPIRED
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
HOSTID bit not set\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
couldn't read TTBR1
fn._ocd_exec_instr.rsr
Connect using RSD not supported\n
MEMAP_APB
ObjectEmpty
_read_memory_slow
low word
_a64cpu_write_vfpreg_hw
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Table 5–155
performing direct connect by port number
Unique required when more than one probe identified by
mxwrap-address
chip-index
{%s::%s@%d [%s]} Error %s: flushing HW state
   DPv3 baseptr is not valid (%X)\n
Creating a S1 Flasher to Acquire\n
wrstn-partition-number
Dart Coastguarded CPU: %s\n
using multi-target booster products_%s.plist
{%s:%s@%d} [%s] writing WCR %d\n
ELR_EL3
Busy
Error %s connecting to probe server
is.Peek() == 'n'
{%s:%s@%d} [%s] doing JTAG scan\n
{%s} Debug Base: %08X
Creating a 4200L Flasher to Erase\n
path
astris_kis_get_bypass_info
ret.ipc_poll_lock_status.write.ipc_lock
{%s:%s@%d} [%s] writing DTRRX(first)\n
cpu object is NULL
fn._write_general_reg.regval
Issuing request to Probe Map Server: %s
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
Number too big to be stored in double.
Failed to find a product plist for this soc %s
Failed to populate portal info
Debug Base: 0x%llX\n
[%s] {%s->%s} END handling exception
{%s:%s@%d} [%s] second read of CMDSTAT failed\n
XTENSAcpu_t
ASTRIS_ERR_JTAGERROR
Found another target for the plist\n
wir-size
ret.rx-full.mddtrrx
cpu_readmem
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
DEBUG CLOCK OFF
Invalid instruction breakpoint index %d
generic probed USB error
INIT
Miss exponent in number.
PrettyPrefix
/usr/local/share/astris/boosterpack
--> 0x%02x = %s
products_
ret._a64cpu_read_sysreg_hw
_resume_translation_hw
{%s} _pre_halt_hw result = %s
Unable to connect to probe server
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
sso_user.conn == NULL
WARNING
diyfp.h
Failed to get KIS STM Probename\n
Did Not Find Any Boosters For: %s \n
CPU DBG Ack: 0x%llx\n
DBGWRAP_FULL
ret.restore_el.read
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
_init_bpwp
Error %d(%s) executing instruction 0x%08X
{%s::%s} [%s] length=%u when width=%d
/System/Library/PrivateFrameworks/MobileDevice.framework
Clocking To 48Mhz\n
Register file 1
XTENSA
source != __null
_a64cpu_read_gpr_hw_impl
{%s::%s@%d} [FALSE] CRm out of range [0x%08x]\n
{%s:%s@%d} [%s] Failed To Enable BP Unit: %s\n
param.info
fn._ocd_exec_instr.wsr.ddr.data_reg
{%s} Batch attitude key created for %p thread %#llx key %lu
MMID
ASTRIS_ERR_NOAP
AuthDebug::authenticate_probe - no need to authenticate\n
reset_connect_state
basic_string
lower.safe.aarch32=notsupported
{%s:%s@%d} [%s] Failed to get PID: %s\n
Table 5–152
cpu_resume
IsNumber()
param.conn.connected == false
Creating a PSOC6 2M Flasher to Acquire\n
dcm
{%s:%s@%d} [%s] setting DTR MODE to STALL (first abort)\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
!!!! Critical Error: ARM64-specific _sstep method not currently supported !!!!\n
Register file 28
_set_bpwp
ASTRIS_ERR_USB_NODEVICE
ret.write_hang_breadcrumb
fn._ocd_reg_w.DIR0EXEC.instr_32
CHAINERR
PROBED_USB_RSP_ERROR
Successfully connected to
param.num_data_bp_regs.invalid.1
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
error trying to unlock MSR %s
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
UNKNOWN CODE
target not in appropriate state for action
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
ret._cleanup_hw
Connect
_get_el_implemented
AXcpu_hwwp_disable
CCOUNT
Table 5–156
fn._setup_instr_bp.bp_state
%d.%drc%d
%s SoC created
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
op_ROTW_encode
EndObject
32 
{%s} Failed to resume %s: %s
param.reg_index.invalid
Connecting to server, %s:%d
addMember.engineer.message
Gathered Info:\n%s
[1500] Using %s.plist
Section 1 Offset: 0x%llX\n
{%s@%d} Connection to server failed, error=%d (%s)
The document is empty.
GetDouble
%s Bridge @ 0x%09llx-0x%09llx: %s
DISPEXT
[RESUME] Chip %x\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
HardwareBreak
ret.cpu.nmi()
Gateway is KIS, seeing what probe this is\n
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
authenticate_probe
ret.nonce_generation.timedout
Register file 43
%s: %s\n
{%s@%d} Received %d bytes when requested %d bytes [%s].
read_resp_payload_via_sock
DISCONNECT
cpu_go
1500 IR Commands:
Failed to populate component info
 MEM-AP %X is hung\n
symbol.check.loaded.AMAuthInstallSupportDictionarySetInteger32Ptr == NULL
%d:%d%s
SoC BM Not Found, Bailing\n
Failed to init from cpu desc armv7m cpu: %s \n
%s at offset %zu
disabled
{%s} 0 words from probe when %d words left to read for address 0x%016llX
_a64cpu_encode_aarch64_add_imm
** \tTatsu AuthDebug Triage | All     **\n
Table 5–134
fn._ocd_reg_r.dsr.dsr
pnav_create_probelist
Failed to create Xtensa CPU %s \n
ret.read.edscr.masked
   Setting up AP IDR %08X\n
internal.clear-auth.chip->soc == NULL
Min Component - %s\n
EL2t
n APB Access Port.
parameter val is NULL
JTAG Slave Unavailable
{%s:%s@%d} [%s] writing DTRRX\n
fc_retries=%d
Absent
m_loaded_framework == NULL
{%s:%s@%d} [%s] Read DWT Func %u\n
CSTF
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
read_settings
Value Types Are Not Strings\n
BoosterManager.Utility
targetid/instance must both be set or both be unset
{%s=>%s} null reference to AXconn_t record, `conn`
internal.is_dft_authenticated.chip->soc == NULL
ICOUNTLEVEL
RF14
fn._ocd_reg_r.OCD.DEVID
Both debug and xbs versions are set, maybe a bug: %s
{%s:%s@%d} [%s] switching register set\n
{%s->%s}
DBREAKC0
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
ide_checker_diagnostic
{%s} unaligned %d-byte access at address 0x%09llx
ret._a64cpu_raise_el_hw.el=2.to_read_hcr
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
M4
Table 5–154
[%s] {%s->%s} clear async abort
Failed to write transfer register (EDDTRTX) the value to write
   ROM entry %d (level %u): AVOIDED\n
ret.astris_create_cstr_from_cfstr
_write_general_reg
%s.console
abort
can't find pid in response\n
Failed to find a plist for this soc %s
astris_batch_attitude_attach
[AstrisAsync] Pausing Async Mode\n
dbgwrap halt failed, falling back to classic method
, indicating an unrecognized ARM Cortex-M core
_read_reg
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
{%s:%s@%d} [%s] \tCould Not Write Request To Get Silicon ID\n\n
Standard level
ASTRIS_ERR_INVAL
A
AXcpu_hwbp_info
EPC7
M2
fn.is_halted.setup_bp
regval is NULL.
REG
cpu_cache_info
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
ASTRIS_ERR_IGNORED
{%s} error %d(%s) reading data from the connection (at recv)
cpu_mmu_configure
disable
check.el.after.exception_hanlder
process_status_transition
MISC0
Table Size: %d\n
ret.current_state_aarch64
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
{%s:%s@%d} [%s] Failed To Erase Flash Before Programming\n\n
reg_name (\"%s\") not present.
ERROR!! write binary data parameters invalid\n
PROBED_USB_REQ_TIMEOUT
shared_ != 0
Failed To Initialize Logging\n
--> master     size=%3d localwrstn=%d debug=%d
{%s->%s} exec: encode_mrs(scratch=%d, sysreg=0x%X (%s), regname=%s, %d)\n
param.reg.invalid.outofrange
fn._read_special_reg.dbreaka1
command timed out
kick
cpu_sstep
dbgarch
[1500] Error parsing v2 bridges
Failed to sync prefs at beginning
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Error %d (%s) while expanding ~ for Astris log file base\n
Failed to convert %s key @ index %d
{%s} timed out waiting for cpu to halt during collect
load_framework
astris_command_async
setCategoryValue: path='%.*s'
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
~A
, and bits [15:4] are 0xC24 indicating Cortex-M4 core
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
[FLUSH]\n
lower_el.el2.tge=set
[HALTED] dfsr = 0x%08x\n
   MEM-AP not enabled\n
{%s:%s@%d} [%s] setting GPR 0\n
{%s:%s@%d} [%s] writing DRCR (STICKY)\n
General register 1
RF49
Invalid parameter exec_path = %d
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
UWB
[SSTEP] using BP %d\n
VBAR: %#llx\n
{%s::%s@%d} [FALSE] aarch64\n
[ARCH32] Failed to read transfer register (EDDTRTX)
_cleanup_hw
param.width.invalid
spsr_el1
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
[CLEANUP]\n
Fabric access is blocked. Expected if production unit, won't explore further.
Could not write system request (SROM_SYSREQ_BIT | SROM_CMD_SET_IMO_48_MHz) error %s
_ocd_reg_dsr_w
fn._ocd_reg_r.ddr.value
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
Info_
Begin
{%s@%d} Connection to server rejected, error=%d (%s)
KICKINFO
message
String
RegionStart
(system_reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) != 0
AXcpu_swbp_insert
, and bits [15:4] are 0xC27 indicating Cortex-M7 core
MASK ERROR
swdackdelay
_read_cpu_reg_file
ASTRIS_ERR_PORTAL_STATUS
SLEEPCTL
astris_soc_release
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
{%s->%s} [is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
bpcr
ret.storePairForPref
?? 
framework_url == NULL
{%s:%s@%d} [%s] Could Not Re-Acquire After Resetting: %s\n\n
op_XSR_encode
AXcpu_mmu_get_mair
v%s.%s
Connected to Probe Map Server
Skipping CPU %s at 0x%llx: not present in IDE\n
operator[]
ParseStream
AXjtag_explore failure - %s (%d)
internal.clear_probe_auth.chip == NULL
value=0x%8.8X
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c
[1500] run_steps: unknown instruction '%s'
No version information found in booster: %s
_a64cpu_lower_el_hw
astris_handle_romentry
PARTNO_DAPLITE
ret.pka.verify.status.err
param.cpu_name.invalid.NULL
Connection to server accepted
XBSRelease
Adding new booster path: %s\n
AuthDbg,ChipID
MAC16 data register 2
cpu-address
AMCNP_GFX
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT && != SP\n
Error:ASTRIS_ERR_BADPARAM(-29)
Enabling USB Gateway
psr-size
Channel configuration missing
result.extract_table_info==
param.reg_name.!match
Unknown Subcommand
[%s] Executing instruction=%llx
api.is_prod.chip == NULL
Instruction break 0 address
Page table virtual address
_set_single_step
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp
cpu_lacc_count_remove
param.cpu==NULL
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
n unrecognized non-ARM Debug Port.
MR3
fn._ocd_exec_instr.rsr.2
ACQ_SAMPLE_SPI
set.probe_name
param.bundle_url==NULL
param.chip->conn == NULL
{%s:%s@%d} [%s] getting GPR 0 (ARB)\n
, indicating this is a Cortex-A9 core
{%s:%s@%d} [%s] Clock To 48Mhz Command Failed\n
General register 11
EL1h
param.no_ap
MSR
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
R11
%s on %s
NUB
[%s] {%s->%s} Transitioning to exception level %u.\n
spsr_select
[PREFS] Key: %s - Val: %s
IBREAKENABLE
RF13
cpu_status
Logger is null
DBG_CPU: %s\n
ARM64cpu_t
AXjtagap_explore
Low level
Invalid character [0x%02X] received from Probe Map Server
master-localwrstn
    IDR[23:17] is 0x%03X (Designer Identity).\n
_pre_resume_hw
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
{%s} _resume_hw result = %s
EPS7
length=%u, width=%d
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
Already connected to
Schema parse error
cpu-ps-register
AXcpu_mmu_get_page_shift
astris_memap_lmflash
, indicating Component Class == Generic IP component
RF62
CortexM33
current != kRegexInvalidRange
Could Not Allocate Info Keys Array
astris_preferences_cpu_monitor_list
Register file 55
result.booster_api_vers==NULL
_sw_breakpoint_insert
DBREAKC1
Wait indication while connecting to
TRST
value
{%s} [EDSCR_RXFULL !is_64] exec: encode_mrs(0, MDDTRRX_EL0, false)\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
Variables not setup
CTI
Table 5–165
op=%d
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
couldn't read TTBR0
Breakpoint Size: %d
{%s:%s@%d} [%s] failed to read CMD/STAT\n
ASTRIS_ERR_TGTLOST
ret.switch_taps
gmtime() returned NULL, using epoch time
ret.explore_table == NULL
ret._a64cpu_read_sysreg_hw.hcr_el2
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_rawjtag.cpp
fn._read_cpu_reg_file.regval
fn._write_special_reg.dbreaka0.address
(%s)
astris_json_logger_get
unable to obtain sysap
CCG Acquire Sequence Failed - %s (%d)
ret.astris_ide_get_dbgwrap_base
set.wp.len > 4 && addr & 0x7 != 0
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
fn._ocd_exec_instr.rsr.ddr.regidx_restore
%s/%s
Previously dumped the process tree, skipping
15002APB
!!!! CPU Key %s is INVALID !!!!\n
ITO
{%s} Failed to single-step %s: %s
AXI Error
no device when sending request
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_components.cpp
SCTLR_ELx
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Invalid num_regs = %u. Windowed register option required.
User
_a64cpu_reset_catch
{%s} handle ROM entry %d (level %u): %08x
CypressFlasher_4100S
Register file 35
Vector Base
_insert_breakpoint
ARMV7M
dr ->
_memory_set_base
SWDFlasher.CCG
{%s:%s@%d} [%s] writing ITR\n
SUCCESS
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
AXcpu_readreg_vals
```
