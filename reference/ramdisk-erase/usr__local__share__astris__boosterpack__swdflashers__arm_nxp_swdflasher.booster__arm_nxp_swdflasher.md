# `/usr/local/share/astris/boosterpack/swdflashers/arm_nxp_swdflasher.booster/arm_nxp_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,750,608 bytes.

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

## Strings (6,696)

First 2,500 of 6,696.
```
Gathered Info:\n%s
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
{%s@%d} Timeout while attempting connect to server
Die-Count: %d Current-Die: %d Die-Type: %d
[RESUME] Chip %x\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
{%s@%d} Received %d bytes when requested %d bytes.
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
CPU %s already in the map with status: %d
[DCC] Grabbing DTR failed: %s\n\n
Target ID: 0x%X\n
{%s} already collected %s, skipping
{%s} PRIMECELL [DONE]
AP[%d]: MEM_AP_AXI\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
=== Detailed %s Boosters ===\n
using multi-target booster products_%s.plist
[COLLECT] Chip %x\n
[REMWP] wp%d\n
Proceeding with full explore instead of instantiation
{%s} probe_port = %d
received %zd bytes from Probe Map Server when have %zu
{%s}#%02X cmd: %s, resp: %s
sending abort to clear a timeout\n
{%s} bridge returned DECERR
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
[AstrisAsync] Activate while async is already active!\n
[%s]\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
Modified Word To Write: 0x%08x
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
[PREFS] Key: %s - Val: NULL
wrote      0x%08X @ 0x%08llx\n
Unable to allocate memory for next part of big response
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
     0x%016llx: 0x%04x      %s\n
{%s=>%s} AXconn_t has no SoC object
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
AXconn_t Struct Is NULL
Debug Clock Already Enabled
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
{%s} Failed to extract IDCODE from table (%d); continuing anyway
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Extract Offset: 0x%X for %d\n
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
Probe Map name of probe %d is: %s
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
SOC_t::{%s} CPU_t group=%d when group 0 expected
We are in clean up\n
{%s::%s@%d [%s]} Error %s: collecting HW
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
Async is disabled for localhost connection
PKA Base: 0x%llX\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
Unable to register assert upcall %s (Insufficient memory)
We are done with clean up\n
Could Not Find Any Boosters of Type: %s\n
CPU Name: %s\n
{%s::%s} [%s] error %s from _synchronize_context.
Astris Version Set: %s
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
   DPv3 baseptr is not valid (%X)\n
Increasing length by: %d\n
{%s} %s: |%s|-|%s|
Complex CPM Offset: 0x%llX\n
{%s::%s@%d [%s]} Error %s: resuming HW
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s} status=%d being reported as Unknown
{%s} unmodified-probe_match = %s
Complex CPU ID: %d\n
caller=%s, async=%d
Unable to read FP
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
## ARM32cpu_t::read_register %u\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
Aligned Address: %llx
Failed to sync prefs at beginning
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
   Debug Port: SELECT %X: DISABLED\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
{%s:%s}: cpu powered off: unable to access a register for this CPU
1: ARM64_SYSOP_ATS12E1W\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
Selecting polling method %s
Error %s connecting to server %s:%s [RETRYING]
Connecting to server, %s:%d
=== Found %s Boosters ===\n
Error status from AMAuthInstallSsoEnablePtr = %i
Finished!\n
Error %d (%s) opening history save file
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
AXjtag_explore failure - %s (%d)
Gathered Value is Not Number\n
Booster Value is Not String\n
Request Dict:\n%s
{%s} probe_host = %s
unable to identify chip
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
Booster:\n
[1500] v2 plist missing required field 'bridges'
{%s::%s} EDSCR with TXU set - unable to recover.\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
Asked To Read A Negative Register Index
{%s::%s} ERROR %d(%s) pre_resuming %s\n
Error %d(%s) executing instruction 0x%08X FAST
caller=%s, async=%d, iterations=%lu
      Read of JTAG-AP port %u PSTA failed with %s\n
Can't get hardware model - failed to get property
Can't get OS build version - failed to create URL
[KIS] Address: 0x%llX\n
KIS Writevals putting back the value
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
AuthDebug::authenticate_probe - no need to authenticate\n
Created Connection - : %s
relay_get: %s = ERR
The debug port associated with this chip has not been explored.
   Setting up AP IDR %08X\n
Unsupported device (%s)\nJust going for it!\n
Xtensa Option reg_file_size: %d
Can't get hardware model - failed to allocate data buffer
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
{%s@%d} Connection to server rejected, error=%d (%s)
[FLUSH]\n
{%s} %s DC cache clean complete, marking as clean
replay_counter=%lu
{%s} ROMTABLE (dbgbase=0x%llx)
Bundle: %s NOT FOUND\n
{%s::%s} [%s] error %s writing SCTLR_ELx
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
Component Group Offset: 0x%X\n
{%s@%d} Unable to create socket
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
AXmemap_readvals failure - %s
{%s} handle ROM entry
Xtensa Option num_wp: %d
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
Section 1 Offset: 0x%llX\n
Probe %s status: Busy
no debug bus AP present when expected; after sysap is NULL
JsonLogger: Loading schema for category '%.*s' from '%s'
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Values Not The Type We Expected. Expected: Number and String\n
replay_counter=%lu, last_replay=%d
Buffer is NULL
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
{%s:%s@%d} Critical error [radar already requested]
%s [RETRYING]
Value Types Are Not Strings\n
Dart Coastguarded CPU: %s\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Replacing key with value
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
Probe %s with unknown status %s dropped from available list
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Match Count is Zero. This is invalid.
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
Failed to find a product plist for this soc %s
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Full JSON that failed validation:\n%s
Problematic JSON value:\n%s
{%s} invalid data width %d bytes
Probe Type (%d) FW Version: %s does not support KIS.
1500 IR Commands:
{%s} %s resumed\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
{%s} Reading base 0x%llx entry's component ID
Error Reading Device Production-Fusing\n
Failed to convert CFArray to C Array\n
CPU state %d
[1500] Using %s.plist
error trying to unlock MSR %s
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s@%d [%s]} Error %s: synchronizing context
SoC has been setup using standard instantiation (setup result=%d)
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
{%s} unable to find single_port probedaemon on port %d
      AXap_write of R_JTAGAP_PSTA failed with error %s
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
{%s} %s did not match any valid host
Invalid SoC Booster. SoC Booster Requires PID\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
{%s} Error setting up memap target (%s)
{%s} checking for single_port probe daemon on port %d
Connected to Probe Device Server [Default Log]
Probe %s Device Not Connected on USB-C Port
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
No 1500 bridges specified\n
Could Not Allocate Booster Location Array
Failed to find a plist for this soc %s
Result while reading third entry: %s , entry val 2: 0x%X\n
Invalid Size Given for AP AP=%d Size=%d
JsonLogger: Writing category '%.*s' to '%s'
Valid Portal
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
Required Key-Value is a string, and not an array. Old booster found: %s\n
We Are Matching Development Booster\n
[1500] TAP key is not a valid integer
DCCCTRL = %08X   res=%d\n
Connect using RSD not supported\n
Not Creating CPU: %s\n
Connection to server accepted
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s} no response from bridge
Could Not Allocate Mutable Dictionary For BoosterMangers
Unable to convert plist file name to CFString: %s\n
CPU Die: %d\n
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
[1500] run_steps: unknown instruction '%s'
Failed to get DFU Type
[Auth Debug] Ticket Active, Debug Interface Locked\n
Probe %s removed during selection process
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
probetimeout retry failed logging as hang\n
AuthDebugWithTimer_t destructor \n
Probe %s with unknown kick response %s
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
CPU AP-Select: %d\n
!!!! Complex Key %s is INVALID !!!!\n
Protocol Version: 0x%X\n
{%s} m_exception_level(%d) != current_el(%d)
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
--> misc_wdr   size=%3d wirtestporten=%d
Board ID: 0x%X\n
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
%s probe[%s] from Probe Map Server [%s]
Probe Map comm error %d(%s) %s [%s]
Failed to convert CFString to C String.
\t%s (%s)\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
New format for cip gen register, unsupported: %d\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
TargetSel Before Disable: 0x%x
Error status from AMAuthInstallSsoInitializePtr = %i
!*!*!* ****************************************************************************** !*!*!*
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
\t%s\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
   Debug Port: SELECT %X: AVOIDED\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
[AstrisAsync] Failed to restart Async batch\n
{%s} found single_port probedaemon on port %d
{%s} Error %d(%s) sending message
[1500] No %s.plist resource found
Can't find descriptor for group - can't index\n
{%s::%s} ITE is not set: 0x%X\n
Unable to read GPR %d
{%s->%s}
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
Error %d (%s) while expanding ~ for Astris history save\n
{%s@%d} Probe response payload read when no payload indicated.
[%s] Booster System Is Not Initialized\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
## armcpu: success status even though not all bytes written\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
{%s} ROMTABLE (nest=%d)\n
Successfully Authenticated\n
{%s@%d} neither socket nor kext connection available
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
[CLEANUP]\n
   Debug Port not responding (%s)\n
[1500] IR command '%s' missing required field 'opcode'
## ARM32cpu_t::read_register 64 bit 0x%x\n
ERROR: unable to suspend translation for %s
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
 MEM-AP %X is hung\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
Error during flashing: %d\n
Connected to Probe Device Server [Log File %s]
invalid IR command '%s'
KIS Readvals putting back the value
[1500] Error parsing TAP description
Found the RTXCID Structure!\n
2: ARM64_SYSOP_ATS12E1W\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
Did Not Find Any Boosters For: %s \n
No version information found in booster: %s
error %s checking for data abort
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
%s probe[*] from Probe Map Server [local host]
Choose a device: 
Passed NULL booster without custom plist\n
{%s::%s} [%s] error %s reading SCTLR_ELx
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
Failed to read IDE through DAP\n
{%s} Component ID read fail on romtable (%s)
{%s::%s} creating placeholder for CPU: name=%s
Initializing (%s) Booster's Astris API\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
      AXap_read of R_JTAGAP_PSTA failed with error %s
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
Failed to allocate space for table!
INFO: %s(%04u): %s(): err=%s(%d): %s\n
[AsyncSnapshot] #%zu: %s\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Preferences does not exists: %s, creating one.\n
connection about to be destroyed
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
Wrong width, should be either 4 or 8\n
Exploring IDE in JTAG\n
      Select of JTAG-AP port %u failed with %s\n
[READ] cop %d -> 0x%08x\n
successfully updated DEMCR
     ARM %s debug CPU rev %d\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
Unable to create pthread key for conenction. errno=%d %s.
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
{%s->%s} m_exception_level=%u
Unable to read SP
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
comparing against match entry %d: %s
Before astris_kis_init_dp, CMDSTAT=%08X\n
{%s} Extracted CIP Gen Number from table  (%d)
Die Addr Info LSB: %d Mask: 0x%016llX\n
About to call fault reg latch, min_operating_el: %d\n
{%s} Component ID read fail for 0x%llx (%s)
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
=== Ending Gather and Clear ===
can't find pid in response\n
choice: %d\n
SoC does NOT support IDE Explore\n
Found form-factor specific channel %u for device '%s'
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
failed write of 0x%08X to DEMCR - %s
{%s@%d} Found cached response
Failed to convert %s key @ index %d to a number with base of %d\n
Cannot create DART descriptions from NULL info\n
SoC BM Not Found, Bailing\n
Failed to instantiate %s\n
%s: chip was NULL when attempting to release soc
!!!! DART Key %s is INVALID !!!!\n
Groups %d\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s::%s} [%s] error (%s) getting number of HW BPs
Successfully Authenticated Probe\n
Xtensa Option num_high_pri_intr: %d
Can't get OS build version - failed to open ReadStream
{%s} %d(%s) [RETRYING]
%s
CPU Explore: 0x%llX\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
VBAR: %#llx\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
ERROR!! write binary data parameters invalid\n
Failed to convert %s key @ index %d
TAP IDCODE: 0x%X\n
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
No 1500 bridges or TAPs specified (v2 plist)\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s} calling _collect_hw on %s
[KIS] Register Index: %llu\n
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
There is no system bus access port on the debug port
Portal Group Base: 0x%llX \n
DBG_CPU: %s\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s::%s} EDSCR in unexpected state. Returning %s.\n
The log file has been updated with all available diagnostics.\n
[1500] Error parsing bridge '%s': missing required field 'select'
[MEM] Aborted; DSCR = %08x\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
Previous authentication in-flight, wait for it to finish\n
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
    INFO(%u,%d): %s(%04u): %s(): %s
{%s} [%s] m_exception_level=%u\n
Successfully connected to server, %s:%d
Die Config Disabled
[AstrisAsync] Async mode %s
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
probetimeout retrying access...\n
{%s} error %d(%s) reading data from the connection (at recv)
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
{%s} %s DC cache already clean since last halt, skipping flush
Xtensa Option num_bp: %d
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
{%s@%d} Drain empty on decr [%s].
{%s} %s: |%s|
{%s} Failed to get breakpoint mask for %s: %s
   {%s} Before powerup CMDSTAT=%08X\n
Failed to create optional file. Not fatal, moving on
{%s} drop ProbeName %s
relay_set: %s = CMD_ERR (%s)
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
haskis bit not set\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Breakpoint Size: %d
Spew change. old=0x%016llX, new=0x%016X
Sprocket probe, for now I guess we will just say yes...\n
Matched via Bundle ID\n
CPU Supported in Runtime: %s\n
{%s::%s} cpu powered off: failed init() %s
{%s} Debug Base: %08X
[%s] chipinfo is NULL
AXjtag_srst deassert failure - %s (%d)
Enabling USB Gateway
Warning: chip exploration did not complete successfully (%s)\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
{%s=>%s} AXconn_t has no chips
Could not find portal by select %d, while interpreting result\n
{%s} no matching 1500-to-* bridge
\tLeft Over Chunk Read Failed\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
{%s@%d} gethostbyname failed, error=%d (%s)
{%s::%s} creating AP slave: name=%s
CPU ASC Offset: %d\n
{%s} Failed to extract ECID from table (%d); continuing anyway
{%s} %s status is '%s' [Status Read %d times]\n
%s probe[%s] from Probe Map Server [local host]
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
   {%s} select %u port %u: %u chip%s\n
      Explore of JTAG-AP port %u failed with %s\n
process (%s) (%d) path: %s
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
## armcpu: bad status even though all bytes read (%d)\n
{%s} DAP command nwords=%d trimmed to %lu\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
BoosterManager Types:\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
%s construction failed
Failed to convert primateLoc %s to unsigned long long
{%s@%d} Unknown CS code [%u]
UPDATE cop64 %d -> 0x%016llx\n
{%s::%s} read OK but took %d tries
{%s} Unable to read SP_EL0
Unable to read GPR 28
[AstrisAsync] Deactivate while async is not active!\n
outstanding=%zu
SSO with no prompt being used
Setting CPU %s is_boot_core to %d\n
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
ERROR: unable to resume translation for %s
kext connect name %s\n
\t[MATCH_SKIP] skipping entry
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
   ROM entry %d (level %u): AVOIDED\n
Probe %s selected
[READ] cop64 %d -> 0x%016llx\n
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
AP given is not a MEMAP
\tReading left over chunk 0x%x @ 0x%llx\n
Result while reading first entry: %s , entry val 0: 0x%X\n
{%s} %sing word #%d at address 0x%09llx: %s
DHCSR write failure - %s (%d)
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
[AsyncSnapshot] No snapshots collected\n
{%s} Unrecognized component: %08X, class %02X\n
read failed, using old cached as base: 0x%x
no matching part (%s)\n
[KIS] CMD: %s \n
Could Not Match A Booster for %s\n
CPU Monitor key does not exists for: %s\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
{%s[select]} timeout while waiting for data from the connection
Using Built In SoCs\n
Failed to read ide_table from KIS explore
Raising to EL2 cause in Guest\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[AstrisAsync] replayConditionalCheck: condition hit!\n
Async is disabled for current seesion
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s@%d} socket connection is not available
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
astris_get_async_ver failed with error: %s
{%s} Failed to get watchpoint mask for %s: %s
{%s} Failed to single-step %s: %s
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Could not find TAP at chip-index %d for v2 1500 config\n
[1500] Error parsing bridge '%s': missing required field 'tap'
** \tTatsu AuthDebug Triage | All     **\n
Probe Map Server Information: %s
Probe %s LocationID Info is %s
[1500] Error parsing IR command: %s
[%s] {%s->%s} Transitioning to exception level %u.\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Unable to allocate memory for big response
%s Bridge @ 0x%09llx-0x%09llx: %s
{%s} Failed to extract PID from table (%d); continuing anyway
Chip %x Status = %d\n
[AstrisAsync] Pause when already paused!\n
AP[%d]: JTAG_AP (Exploring Later) \n
tckrate_check returned error %s
{%s=>%s} AXconn_t has more than one chip
no system bus AP present when expected
[1500] %s step %d: unknown instruction '%s'
==== Exception Trace ====\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
ERROR!! Couldn't save %s binary data\n
{%s} flags:0x%08x
{%s} host name(RSD): %s\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
Dumping Process Tree
Probe %s Device Server listening on port %d
\t[MATCH_TARGETID] FAIL <= unable to find DP
Could Not Get Bundle Out Array of Found Boosters\n
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
{%s::%s} waiting for EDSCR ITE
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
   {%s} Probe requires overrun detect mode.\n
max_scan_bits is low: %d
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
Type 'jebdump' to do scan/mem dump\n
Failed to explore chip: %d
Can't get hardware model - failed to find matching IOService
{%s} host:%s, flags:0x%08x
AXconn or json_out are NULL
KIS translator version : %d\n
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
{%s@%d} Failed to send probe command (error %d).
error %s reading DAP MMFR0
[%s] E2H is set, virtualization is supported\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Can't get hardware model - failed to convert to C string
unknown match criteria type: %d
Creating CPU Returned: %s\n
using standard products.plist for %s
{astris_probed_print_events} not supported in this build configuration
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
Logging Context Is NULL\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
## memapr %u 0x%016llX -> 0x%08X\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
Hang Description:\n%s\n
## armcpu: bad status even though all bytes written (%d)\n
Probe Map comm: request[%s], response[%s]
Required Key-Value is a string, and not an array. Old booster found\n
--> wrstn_wir2 size=%3d dpcsoc=%d
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s} restored el is now %d
{%s} 0 words from probe when %d words left to read for address 0x%016llX
{%s=>%s} null reference to AXconn_t record, `conn`
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
Found another target for the plist\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
   {%s} APB/AXI address for target setup = 0x%llx\n
KIS Chip Found, Doing KIS Explore Setup
Old ProbeDaemon does not support this command
Table Size: %d\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
Gateway is KIS, seeing what probe this is\n
can't find bid in response\n
{%s@%d} Failed to find cached response
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
Failed to create Xtensa CPU %s \n
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
read_dbg failed to access R_v7M_CLIDR
relay_set: %s -> %d
{%s@%d} Received %d bytes when requested %d bytes [%s].
start rev is not of expected format; skipping cpu_desc override\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
[CACHEOP] %d, 0x%016llx, %d\n
{%s} setting up nameless target (address=0x%llx)
   --> IDR: %08X\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
Preparing and erasing sectors %d to %d\n
Init objects failed
Complex Type: %s\n
Dart Name: %s\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
type_hint not NULL, but creating a placeholder, this is off
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
## memapr %u 0x%016llX %d -> 0x%08X ...\n
JsonLogger: Creating new category '%.*s'
--> master     size=%3d localwrstn=%d debug=%d
CPU: %s halting debug is now %s\n
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
[AstrisAsync] Completing all async commands. Initial err = %d\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
Error while trying to authorize: %d - %s\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
CPU Supported in Integration: %s\n
{%s} read ESR EL1|EL2|EL3 (%d)
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Translate Stage Chosen: %d\n
could not perform cpu_preflight
   {%s} Clearing HNONSEC on AP \n
{%s} Exploring with option: %s\n
%s SoC created
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
{%s} DEVARCH read fail in CoreSight component (%s)
Failed To Instantiate SOC From Booster\n
AP[%d]: unknown type\n
\tTatsu AuthDebug Triage | All\n
New Length: %d\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
[AstrisAsync] Deactivating async...\n
      Read of JTAG-AP port %u CSW failed with %s\n
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Multi target booster, checking for %s.plist\n
%s constructed
{%s::%s} error %s writing EDSCR %s
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
AP Only Explore was asked for, stopping here
## apr %u 0x%08X -> 0x%08X\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
Min Component - %s\n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
%s status is '%s'\n
In Preflash\n
Unable to read PC
AP[%d]: MEM_AP_APB\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Cannot create complex descriptions from NULL info\n
Unable to disassemble_at_addr 0x%016llx
ERROR!! Wrote %zd bytes, expected %zd\n
dropping empty probeInfo (port=%u)
Asked To Write To A Negative Register Index
Both debug and xbs versions are set, maybe a bug: %s
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s::%s@%d [%s]} Error %s: checking exception
{%s} Error setting up jtag-ap target (%s)
Original Content: 0x%08x
{%s} FAILURE - max length exceeded
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Early dbgwrap base extracted: 0x%llx\n
{%s} Failed to extract die infofrom table (%d); continuing anyway
   Debug Port: Trying SELECT %X\n
[1500] Error parsing v2 bridges
Map is empty, not removing CPU %s
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
Invalid file name: \"%s\". File names must be at least %d characters long.
     ARM %s breakpoints: %u\n
{%s} timed out waiting for cpu to halt during collect
{%s} error: %s
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
Could Not Find Any Boosters\n
[1500] TAP %d: irlen must be > 0 (got %d)
Highest EL: %d, -- Min Op EL: %d
   Created Fake Debug Port Debug Port
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Caught a portal that we dont have a status map for: %d
[1500] TAP %d missing required field 'ir-cmds'
{%s::%s} EDSCR with RXO set - unable to recover.\n
## dpw 0x%02X 0x%08X\n
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
{%s} 0 words from probe when %d words left to read for reg %d
SOC AP[%d]: JTAG_AP\n
Disconnected from Probe Map Server
[%s] Booster System Is Not Initialized Bailing\n
Initialized %d 1500 bridges\n
Could Not Get BoosterManagerUtility\n
Initializing Booster Layer\n
CPU Core Number: %i\n
coalesced-target: %s\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
Probe %s with unknown port response %s
%s: not supported.\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
Issuing request to Probe Map Server: %s
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
[Auth Debug] External Debug Interfaces Open\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
[PREFS] Key: %s - Val: ??
Can't get OS build version - failed to get build version
Invalid value for 'entry' tuple element - can't index
[AstrisAsync] Activating async...\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Can't get OS build version - failed to create plist
{%s::%s} creating CPU
--> localwrstn size=%3d debug=%d
component group %d\n
SoC not identified by IDCODE - enumerating instead of instantiating
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
  Error path [%s]\n
Kick has been requested by probe server
Complex ID: %d\n
{%s} match any probe [localhost]
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
Stop Clock: %s\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
[WRITE] %d -> %08X\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
[PREFS] Key: %s - Val: %s
Dart CPU SID(s): %s\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
{%s@%d} Connection to server failed, error=%d (%s)
SoC has been setup using standard instantiation (setup result=%s)
AXjtag_srst assert failure - %s (%d)
DEMCR write failure - %s (%d)
!!!! FILE RADAR: Don't know how to compare two values\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
[MEM] Uncompleted; DSCR = %08x\n
{%s} failed (%s)
Previously dumped the process tree, skipping
{%s} bridge returned an error
{%s} no TAP detected that supports 1500
Booster Info:\n%s
** Add the --with-force option or use the explore_override console command **\n\n
EICE chip %x initialized\n
   {%s} (DP): status=0x%X(%s) - %s\n
{%s} strsep empty so match any probe [localhost]
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
--> extrawrstn %d
Debug Base: 0x%llX\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
{%s=>%s} null reference to AXcpu_t record, `cpu`
   Debug Port: SELECT %X: SKIPPING\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
In Readflash\n
Dart Dart Type: %s\n
{%s::%s} [%s] MMU is already active - returning %s
iter=%lu
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
Found %s\n
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
{%s} empty response string provided
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Matched Booster: %s\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
sent %zd bytes to Probe Map Server when sending %zu
{%s@%d} Unable to connect to server, %s:%d
Could Not Create Dictionary From Booster: %s
{%s} pmgr status=%d being reported as Unknown
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
Invalid character [0x%02X] received from Probe Map Server
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Chip Revision: 0x%X\n
{%s} Failed to extract portal info from table (%d); continuing anyway
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
[REMBP] bp%d\n
Awaiting response from Probe Map Server
{%s} probe device server closed the connection while trying to read data (at recv)
{%s} _pre_halt_hw result = %s
Could Not Get BoosterManager\n
Invalid Bundle: %s
Booster Bundle: %s\n
Die Config Disabled\n
codeblock
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
[1500] Error parsing bridge: %s
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
[%s] {%s->%s} clear async abort
Invalid APTABLE (%d), so using most restrictive
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} unaligned %d-byte access at address 0x%09llx
[1500] %s step %d missing required field 'instr'
start rev and/or end rev is NULL; skipping cpu_desc override\n
Creating CPU With Name: %s\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
batch_cmd_count: %d
[SSTEP] bvr=%08x bcr=%08x\n
Invalid current AP (%d), adopting latest (%d)
{%s} explore with exploreflags 0x%X complete [%d chip%s]
Complex Name: %s\n
    %s(): %s
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
checking if relay \"%s\" is valid
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
Start Page: %d\n
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
XBS Version Modified: %s -> %s\n
CPU DBG Ack: 0x%llx\n
Complex CPU Name: %s\n
2: ARM64_SYSOP_ATS12E1R\n
     0x%016llx: 0x%08x    %s\n
{%s} %s status failed. error: %d (%s)
[%s] AP, DP, or chip given is NULL
Setting bypass channel to: %d\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s@%d} Timeout while sending probe command.
end rev is not of expected format; skipping cpu_desc override\n
Setting STOP CLOCK to TRUE
We are Allocating\n
\t\t%s\n
Invalid file name: \"%s\". File names must not start with '.'
[%s] %d -> 0x%08x\n
%s NOT configured\n
CPU (%s) has explore flag of: 0x%llx which is not set\n
[KIS] Words (Read/Write/Wrote): %d\n
\t\tARMv6 debug CPU xxx ID\n
{%s::%s} halting %s\n
[REM_WP] wp%d\n
{%s} _pre_resume_hw result = %s
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
Can't get hardware model - failed to allocate data string
[SSTEP] using BP %d\n
[AstrisAsync] Barrier before pause\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
{%s} hostname:%s, flags:0x%08x
Probe %s removed before port determined\n
{%s} valid response from bridge
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
[ARM32cpu_t::_update_register64] 0x%08x\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
{%s} error %s at line %d
Could not find bundle () in given array: %s\n
We are at max iterations, still didnt get full JSON
{%s::%s} failed: %s
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
Gathered:\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
Init dbgwrap obj failed
{%s->%s} ERROR=%d(%s)
## dpr 0x%02X -> 0x%08X\n
Trying to use size of 8 on not AXI bus
\tReading left over chunk expected 0x%x got 0x%x\n
{%s} Class 9 ROMTABLE (nest=%d)\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
%s given a NULL conn object
--> debug      size=%3d acsr=%d
Exception %d Stack Trace
error %s reading DAP PFR1
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
{%s} Found extra info in = %s, chopping string
{%s} select success without file descriptor set
Failed to init from cpu desc armv7m cpu: %s \n
[KIS] Portal Status: 0x%X\n
[%s] {%s->%s} END handling exception
Length is 0
CPU Monitor[%i]: %s\n
Gateway Version: 0x%X\n
{%s::%s} HDE not set on %s. Will re-enable.
[%s] CPU BM Not Found, Bailing\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
runBlock
Going to do imago workaround\n
register    %-15s %3u     \"%-s\"\n
Connected toProbe Map Server (single_port) 
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
[%s] TGE is set so we traping to EL2\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Could not find TAP at index %d to attach 1500 bridge to\n
Turning Debug Clock On
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
first read of CMDSTAT may fail if external reset occurred
Failed to convert kisHubLoc %s to unsigned long long
%2d) %s %s%s\n
Failed to get PMU Name
## apw %u 0x%08X 0x%08X ...(%d)\n
JsonLogger: Created with default schema version '%s'
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Could not enable KIS SoC Access\n
Subsystem Monitor Key does not exists: %s\n
Failed to convert kisLoc %s to unsigned long long
Awaiting next chunk of big response
Sending DYN Bypas Channel Set: %d
=== Loaded %s Boosters ===\n
error %s checking for data abort(uint32_t)
[HALT] Chip %x\n
unable to create connection
Error closing %s [%d]
Optional Key: SubsystemMonitor not in preferences
Required key: %s @ index %d is NULL\n
probe event: %s
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
1: ARM64_SYSOP_ATS12E1R\n
Unable to read LR
[INIT]\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Failed to get KIS translator version\n
{%s} Failed to extract CID from table (%d); continuing anyway
\tLeft To Read (%d) < width (%d).\n
Can't get OS build version - failed to create ReadStream
ERR: conn->nchips != 0; looks like chip is explored\n
[%s] cop %d -> 0x%08x\n
pmu-name: %s\n
Failed to get Bypass Config
DBGSTATUS = %08X   res=%d\n
   JEDEC ID: 0x%08X\n
Can't get OS build version - failed to allocate buffer
{%s} unable to allocate probe name
Size or Count provided are 0.
Got an error writing 0x%X the DCM Control Register: %s
In Writeflash\n
{%s} handle ROM entry %d (level %u): %08x
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
{%s=>%s} null reference to AXchip_t[0]
Error status from AMAuthInstallSetSigningServerURLPtr = %i
Failed to convert primateHubLoc %s to unsigned long long
{%s} bridge timed out
[READ] %d -> %08x\n
     ARM %s watchpoints: %u\n
Booster System Is Not Initialized Bailing\n
Breakpoint Address: 0x%llx
Failed AP read of R_MEMAP_CSW res: %i
## memapw %u 0x%016llX 0x%08X\n
{%s} explore with exploreflags 0x%X completed with error [%s]
Dart Base Address: 0x%llX\n
[%s] EL @ end of Collect: %d\n
Failed to access new_cpu status
   {%s} Enabling debug unit\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
SSO info present but SSO disabled.
Error %d (%s) opening cmd snapshost save file
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
CPU AP-Type: %d\n
Original Length: %d\n
Probe %s Device Does Not Have LocationID
{%s} unsupported bridge type for %s
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Error %d(%s) executing instruction 0x%08X
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
[AstrisAsync] Discarding response due to ASYNCSKIP state!
%s: []\n
probing %s status\n
   Debug Port: SELECT %X; error: %s, retrying..\n
   Debug base is in legacy format\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
In Eraseflash\n
[REM_HWBP] bp%d\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
Xtensa Core %s NOT configured\n
OS build version: %s
Hang Radar Info:\n%s\n
{%s} probe [%s] added to list
CPU Subsystem: %s\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} wrote %d words to probe when %d words provided in request
Explore: %u chip%s\n
{%s} already connected
Got an error reading the DCM Control Register: %s
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Error happened when reading edscr. Retry #%i\n
Using Built In CPUs\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
%s %3d'b%s\n
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
[ARM32cpu_t::_read_register64] 0x%08x\n
{%s} halting %s\n
{%s} unable to allocate probeInfo
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
{%s} probeList has probeCount of zero
Could Not Allocate All Boosters Array
Error returned from explore_pid
{%s->%s} current EL (%d) already == target EL.\n
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
{%s} collect result = %s
register lookup by name not supported when Astris is statically linked
AP is NULL
Production Fused Device\n
{%s} Failed to extract target ID from table (%d); continuing anyway
CPU %s not found or already removed from the map
{%s} L2 cache operation completed [%s]
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
[Auth Debug] Disabled\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Initialized Logging - %s
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
CPU has no regions, maybe powered off?\n
Subsystem Monitor[%i]: %s\n
Stepping Stone Final =  %#x\n
{%s::%s} [%s] MMU not active - returning %s
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
Result while reading second entry: %s , entry val 1: 0x%X\n
%2d) %s %s [Busy]%s\n
product-name: %s\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
[ANAMOLY] Could not find AXcpu_t object for CPU\n
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s} Error reading CPUID (%s)
CPU with %s Not Created via Name
JsonLogger: Wrote %zu bytes to '%s'
--> 0x%02x = %s
{%s::%s} write OK but took %d tries
Programming...\n
error %s reading DAP MPIDR
   Debug Port has unknown type\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
{%s::%s} [%s] length=%u when width=%d
## dpr 0x%02X failed (%s)\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
{%s} Error looking up architecture (%s)
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
[AstrisAsync] Pausing Async Mode\n
replayPreflight
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
{%s} NOMEM
%s probe[*] from Probe Map Server [%s]
{%s[recv]} %d(%s) [RETRYING]
Passed NULL plist file\n
bypass-config-name: %s\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Breakpoint Index: %d
   Debug Base: %08X\n
Xtensa Option options: 0x%x
{%s}#%02X %s [%s]
Cannot create SoC [unknown chip identity (%d)]
HOSTID bit not set\n
{%s} Thread %#llx clearing key %lu
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
\tPrologue Aligned Read Failed
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
Banana split probe, for now I guess we will just say yes...\n
Initial DSPSR_EL0: 0x%llx
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
## dpw 0x%02X failed (%s)\n
{%s} 0 words requested for read at address 0x%016llX
Switch back to primate KIS: %s\n
{%s} FAILURE - malloc error
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
USER %s(%04u): %s(): %s
{%s} FAILURE - NULL parameter
X00 Part
=== Starting Gather and Clear ===
couldn't find CPU1. this is expected sometimes.
CPU Address: 0x%llX\n
{%s::%s} timeout while waiting for EDSCR ITE
OK: address translation resumed for %s successfully
Found match - bypass_device: %s; channel: %d\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
Portal Status, Changing STATUS and CMD/STAT to reflect
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
[AstrisAsync] Resuming Async Mode\n
{%s} Failed to get watchpoint count for %s: %s
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
relay_get: %s = %d
{%s[select]} %d(%s) [RETRYING]
DEMCR: 0x%08X -> 0x%08X
[AstrisAsync] Complete Queue callback returned %d (%s)\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
SSO is DISABLED\n
X12 Part
AXportal_t Is Not Valid Type - %d
Koko probe, for now I guess we will just say yes...\n
** CPU %s requires forced explore override flag on this SoC **\n
Could Not Find a DCM Portal
[INS_WP] 0x%016llx x %d\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Astris Source Version: %s\n
%s\n
error %s checking for data abort(first)
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s::%s} [%s] !bpwp_initted, retrying init
write to CMD/STAT failed - %s
[PAW] Failed KIS Portal Access Preflight =%s (%d)
[ARM64 INS_WP] 0x%016llx x %d\n
     0x%016llx: ERROR\n
dbgwrap halt failed, falling back to classic method
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
We are Deallocating\n
Could Not Find Any Loaded Boosters of Type: %s\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
Adding new booster path: %s\n
** Unauthorized User/Network or ECID **\n
  Nested path: parent='%s', child='%s'
getOrCreateValue: addMember failed, returning doc root
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
Cleaning up Each Booster Manager\n
--> psr        size=%3d bit=%d
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s@%d} Unknown CS command error [%d]
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
Optional Key: CPUMonitor not in preferences
Xtensa Option ocd_address: 0x%llx
{%s} connectName[%s]
[KIS] Register Read/Write/Wrote: %d\n
Found an async abort pending; clearing it\n
{%s} Unable to read CPSR
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Portal Group Offset: 0x%X Entries: %d\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
[AstrisAsync] Got ASYNC_RESTART response!
Verify failed\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
{%s::%s} %s pre_resumed\n
User created bundle found, ignoring version checking via plist
[AstrisAsync] Barrier hit!\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
   CPUID: 0x%08X\n
\n
Unknown number of groups in the explore table; can't parse group attributes
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
VBAR: %#x\n
Cached async_replay capability version: %u
   {%s} Read AP's R_MEMAP_CSW\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
X06 Part
After powerup CMDSTAT=%08X\n
   DPv3 BASEPTR0 is 0x%08X\n
response == NONE; failed to get kis target info\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s} FIFO full, try again
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
{%s@%d} {%s[select]} %d(%s) [RETRYING]
gmtime() returned NULL, using epoch time
Could Not Get BoosterManager. Need To Call AXbooster_init\n
Too many portals, we are at portal: %d while max is %d\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
DEMCR read failure - %s (%d)
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
Connected to Probe Map Server
relay_get: %s = CMD_ERR (%s)
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
      Select port %u: AVOIDED\n
Probe %s removed prior to kick\n
KIS Preflight No Need To Write to AP CSW
!!!! Complex CPU Key %s is INVALID !!!!\n
[1500] Detected plist version %d
{%s::%s} [%s] unsupported width %d
   JTAG-AP: Identification = %08X\n
Taking gateway control failed
unable to obtain sysap
Failed To Initialize Logging\n
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Invalid current AP (%d), adopting APTABLE (%d)
[HALTED] dfsr = 0x%08x\n
{%s} read %d words from probe when %d words requested
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
{%s} probe_match = %s
Cleaning up Main Booster Object\n
==== User Error Messages ====\n
[READ] %d -> 0x%08x\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s->%s} START handling exception
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
--> cmd        addrsize=%d datasize=%d
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
[AstrisAsync] astris_async_override_disable_async: conn is NULL
Found %d APs
## apw %u 0x%08X 0x%08X\n
SWDACKDELAY relay write failed\n
Can't get hardware model - failed to create string
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
There is no debug port associated with this chip.
Could Not Find Booster Entry Function: %s\n
CPU Typehint: %s\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
DBGCTRL = %08X   res=%d\n
{%s=>%s} no soc reference; falling back to direct cpu method
Failed AP write of R_MEMAP_CSW res: %i newval %i
{%s} %s
   MEM-AP not enabled\n
[KIS] Portal ID: %d\n
Could Not Allocate Info Keys Array
Complex Address: 0x%llX\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
AP[%d]: MEM_AP_AHB\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
%#09llx-%#09llx: %s\n
Cannot create CPU descriptions from NULL info\n
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
[AstrisAsync] replay preflight: Async not active!\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Set custom PSD json file: %s
{%s::%s} ERROR %d(%s) resuming %s\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s} Error reading PID (%s)
{%s} host = %s
Probe Map comm error %d(%s) %s
SoC must have a DAP
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
Generated JSON (first 500 chars):\n%.500s%s
AXportal_t Struct Is NULL
!!!! CPU Key %s is INVALID !!!!\n
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
Breakpoint Enabled: %s
Xtensa Option dbg_intr_level: %d
Probe (port=%d) with unknown status %s dropped from available list
Failed to create CPU %s - %s\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} _halt_hw result = %s
{%s} Failed to resume %s: %s
read back  0x%08X @ 0x%08llx\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
\t[MATCH_FOUND] identified chip: %s
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
## apr %u 0x%08X %d -> 0x%08X ...\n
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Had an error during transfer: %s
Could Not Allocate Loaded Booster Array
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
Going To Create Generic ARMV8\n
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
OK: address translation suspended for %s successfully
{%s} no chip found
TatsuServer Found: %s\n
Xtensa Option non_tie_ranges: %zu range(s)
Probe %s USB-C location is %s
setCategoryValue: path='%.*s'
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
   DPv3 bus is %u bits wide\n
{%s:%s@%d} Critical error encountered:
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
Failed to sync prefs at end
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s} _resume_hw result = %s
Width: %d not supported
Switch to primate res: %s\n
{%s} bridge returned SLVERR
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
Probe %s status: Idle
no debug bus AP present when expected
[PAR] Failed KIS Portal Access Preflight =%s (%d)
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s} (end) current_el is now %d
[AstrisAsync] Resume when not paused!\n
connection created
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
[1500] v2 plist missing required field 'taps'
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
pc:  0x%16s cpsr: 0x%16s %s\n
{%s} category=%d
{%s} Failed to get breakpoint count for %s: %s
\tAligned Read Failed
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
{%s} drain_packets=%d [%s]
comparing against match entry [pid] %d: %s\n
{%s::%s} NULL parameter
Pages %d\n
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s} skipping dcache flush, cache already clean
Successfully Authenticated DFT\n
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
dfu-Type: %s\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s::%s} %s resumed\n
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
Failed explore before forced KIS reset: %s\n
X09 Part
Using 10pin connector skipping orientation check
Unable to read CPSR
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
Skipping CPU %s at 0x%llx: not present in IDE\n
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
JsonLogger: Schema loaded successfully for category '%.*s'
CPU PS-Register: 0x%llX\n
[%s] %d -> %08x\n
[AstrisAsync] Discarding %zu completed command(s)\n
collect_responses
no system bus AP present with AHB, trying AHB5
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
In Postflash\n
{%s} set=%u (sh=%u), way=%u (sh=%u)
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
Variables not setup
      Select port %u: already explored..re-exploring\n
Hang Address: 0x%016llx\n
{%s} connectName[local host]
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
failed read from DEMCR - %s
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
Kick off the current process using probe %s? (y|n)\n
Please answer y=yes or n=no.\n
{%s}ERR: bypass_device_name is NULL\n
{%s->%s} (top) current_el=%d
## armcpu: success status even though not all bytes read\n
{%s} asc status=%d being reported as Unknown
Fabric access is blocked. Expected if production unit, won't explore further.
Hardware model: %s
Magic does not match: %#x vs %#x\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
{%s} Unrecognized Component: %08X (class %u)
HOSTID=0x%x which is invalid, skipping orientation check
low word
CPU.ARM
Connection aborted while choosing probe
MISC
cpu_suspend_translation
astris_identify_load_booster
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
ret.m_lam.paccess_write
{%s:%s@%d}\nFABRIC HANG DETECTED. JEBDUMP REQUIRED.\nContext: %s\nSoC: %s Rev: %s Address: 0x%016llx\nDescription: %s
Form-factor specific channel not found, falling back to generic channel for device '%s'
entry.exception_test_2
_get_el_implemented
   Debug Base: %08X\n
authenticate
ret.CFURLCreateCopyAppendingPathComponent
val.check.content
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
ret.dlr_el0
hwwp_remove
fn._read_special_reg.ibreaka0
m_regstate.a64r_dspsr_el0
PARTNO_1176JZFS
start rev is not of expected format; skipping cpu_desc override\n
Debug Clock Already Enabled
/socs
cpu-runtimes
fn.is_halted.setup_bp
addr_reg=%u,page_id=%u,data_reg=%u,opcode=0x%6.6X
Error detected
ret.astris_create_cstr_from_cfstr
Register file 8
_reg_desc_lookup_by_index
(Last: %s)
MODE
Using Built In SoCs\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
Cause of last exception
User interaction
ARMV7M
Misc_Rtx117x_t
=== Found %s Boosters ===\n
cpu-typehint
bid
{%s:%s@%d} [%s] reading ADFSR\n
symbol.check.loaded.AMAuthInstallSsoEnablePtr == NULL
fn._ocd_reg_w.dsr.regval
xtensa-non-tie-range-size
_halt_hw
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
Busy
CurrentContext().valueSchema
SMX
explore
port
Primate-Hub-Null
AXconn_t Struct Is NULL
astris_batch_attitude_detach
PRORES
AXcpu_cleaninv_dcache
JTAG IN CONTROL
outCount != 0
[KIS] CMD: %s \n
_write_gpr
ERROR!! Couldn't save %s binary data\n
_pre_resume_hw
lower_el.el2.tge=set
{%s} checking for single_port probe daemon on port %d
0 == Base::level_stack_.template Top<typename Base::Level>()->valueCount % 2
Debug-Components
L1_INSTRUCTION
ret.get_hang_crumb
pointer.IsValid()
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
OUTEN_DBG
Verify failed\n
Register file 37
AXbooster_refresh
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
[INSWP] 0x%08llx wp%d rdwr=%X\n
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
[Auth Debug] Ticket Active, Debug Interface Locked\n
Section 5.2
AXI Error
BoosterManager Types:\n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
TRST
BoosterManager
{%s:%s@%d} [%s] writing ITR\n
PowerGated
sso_user.sso_user == NULL
No 1500 bridges specified\n
successfully updated DEMCR
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
Accumulator low bits
R10
{%s} unable to find single_port probedaemon on port %d
products_
astris_server_connect
Portal Access Read
(src_gpr & (0x40000000 | 0x80000000)) == 0
{%s} exec: DC_CSW_X1_ENC\n
n't
.hostname
cpu-integrations
{%s:%s@%d} [%s] writing CSSELR[L1-D]\n
AXmemap_read_modify_write
TIMEOUT
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
setEnvironmentInfo
## memapw %u 0x%016llX 0x%08X\n
LCDCTL
Bundle: %s NOT FOUND\n
CPU-level (general and architecture-specific)
_return_from_debug_interrupt
AXconn_destroy
select
AP[%d]: unknown type\n
internal.enable-timer-ovr.chip->soc == NULL
cpu
!!!! FILE RADAR: Don't know how to compare two values\n
fn.exit
[REM_HWBP] bp%d\n
PARTNO_SWDP_M0P1
internal.authenticate.chip->soc == NULL
KobaSWD
ret.get_current_el
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
{%s} pmgr status=%d being reported as Unknown
type_hint not NULL, but creating a placeholder, this is off
/swdflashers
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
{%s:%s@%d} [%s] setting GPR 0 (CPSR)\n
{%s:%s@%d} [%s] doing JTAG scan (DSCR data)\n
Error %d (%s) %s %s probe server
AXchip_get_chip_id
dtoa.h
AddState
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
read memory
ACCLO
MAC16 Data register 2
ASTRIS_ERR_NOTSUPPORTED
ret.read_all_breadcrumbs
{%s::%s@%d [%s]} Error %s: flushing HW state
## memapr %u 0x%016llX %d -> 0x%08X ...\n
ret.pka.verify.timed_out
ObjectEmpty
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_swdflash.cpp
AXbooster_print_loaded_boosters
AXbooster_interface_cleanup_astris_api
astris_ide_get_cps_fsm
astris_explore_enabler_add_cpu
PAR_EL1
???
cpu_translate_with_dart
param.invalid_gpr
ASTRIS_ERR_EXPIRED
Failed to convert %s key @ index %d to a number with base of %d\n
name
\tPrologue Aligned Read Failed
status=%u, flags=%u, DSR=0x%8.8X, DCR=0x%8.8X
fn._tie_read_word32
unknown
{%s:%s@%d} [%s] setting DTR MODE to STALL (first abort)\n
{%s} ROMTABLE (nest=%d)\n
   MEM-AP not enabled\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Can't get hardware model - failed to allocate data string
Failed to allocate JSON string
MemberBegin
ret.die_count == NULL
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
Breakpoint Enabled: %s
Table 5–162
buildCategoryJson
addTimingPhase
JsonLogger: Writing category '%.*s' to '%s'
USER
{%s:%s@%d} [%s] DEMCR write failed: %s\n
RASID
Xtensa Option reg_file_size: %d
{%s:%s@%d} [%s] unable to read command response\n
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
IDLE
socnames
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
reg_file_index = %u >= m_cpu_reg_file_size = %u
RESPONSE_CMD
GetHashCode
reader.h
armv7m-region-axim-end
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
AXdebug_auth_supported
LPC1758
Table 5–133
%s %s
ParseNumber
Probe Type (%d) FW Version: %s does not support KIS.
load_booster
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Accumulator high bits
SETCLR
function
Switch back to primate KIS: %s\n
write_memblock_dbgwrap
internal.authenticate_dft.debug_auth == NULL
Register file 1
Invalid Xtensa CPU OCD.DEVID = 0x%8.8X. Should be 0x%8.8X (LE) or 0x%8.8X (BE)
fn._ocd_exec_instr.rotw.+16
_write_special_reg
ASTRIS_ERR_IGNORED
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
CPS
General register 13
CSPDATA
FPI2C
XSTAT
  Nested path: parent='%s', child='%s'
ret._a64cpu_read_vfpreg_hw
RXO
symbol.check.loaded.AMAuthInstallSsoInitializePtr == NULL
X09 Part
LPC1787
fn.loop.xfer
Set custom PSD json file: %s
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
ret.modify.edscr.~a
M4
cpu_clean_l2cache
data_reg=%u,opcode=0x%6.6X
{%s[select]} %d(%s) [RETRYING]
IsValid()
{%s::%s} [%s] error %s from _synchronize_context.
ret.spmi_write
cpu did not stop. OCD.DSR=0x%8.8X
Table 5–138
Dart Coastguarded CPU: %s\n
AXexplore_enable_cpu_pattern
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
RF59
{%s} already connected
XPROG
passed
DCS_BC4
1
Dart Base Address: 0x%llX\n
{%s->%s} exec: encode_msr(%s=0x%X (%s), scracth=%d, %d)\n
      Explore of JTAG-AP port %u failed with %s\n
{%s::%s@%d} [FALSE] instr[0x%08X] & MSR_MRS_BASE_MASK == 0\n
ret.auth.data == NULL
_log_setup_thread_specific
{%s:%s@%d} [%s] executing MOV (diff mode)\n
Disconnected from Probe Map Server
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
AXarm7_dbgscan
HF3
%02d:%02d:%02d:%06ld|%s <%s> %s
localhost with name matching %s
CHIPCNT
JSON string output is null
haskis bit not set\n
astris_remove_loaded_cpu_boosters
PARTNO_SWDP_M0P2
fn._read_special_reg.ibreakenable.reg_bp_enables
ASTRIS_ERR_STOPCLOCK
_exec
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
astris_cpu_status
High level 5 exception PC
RF54
Warning
invalid environment variable
%s [RETRYING]
DCS_BC1
Table 5–178
astris_json_set_address
MSP
{%s::%s@%d} [FALSE] system_reg[0x%08X] & REGID_MASK != 0\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
LPC1786
Coproc, enable bits
Probe %s with unknown kick response %s
D0-PKA
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
get_sw_info
DP
fn._ocd_exec_instr.rfdo
writeToFile
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
   Setting up AP IDR %08X\n
   {%s} Enabling debug unit\n
LPC11C14
fn._ocd_reg_r.dsr
_ocd_reg_w
AuthBase_t::init failed (AuthDebug_t)
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_COUNTER
_read_mem
op_RSR_encode
Could not find TAP at chip-index %d for v2 1500 config\n
fn.entry
GFX
{%s:%s@%d} [%s] reading BCR %d\n
dlr_el0
Failed to raise EL to %d to read register: 0x%llx
Took an exception in EL%u, esr = 0x%08llx, category = 0x%llx\n
reset_connect_state
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
write_register
probeBoardNames
   Debug base is in legacy format\n
Parity Error on RUN-SWD Subcommand
Unknown Subcommand
spr
Single_port connection to probe server unavailable
cpu-dbgwrap-status
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
RELAY
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
!!!! Critical ERROR: current_el[%d] != m_exception_level[%d] after exeption handling
Trying to use size of 8 on not AXI bus
Error occured during nonce command (v.5)
LPC11U14
var.bp.invalid
DefaultConnectAddress
Booster:\n
APCIE
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
command timed out
(system_reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) != 0
R9
DCS_BC3
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
ret.read.stepping_stone
{%s} category=%d
failed write of 0x%08X to DEMCR - %s
GROUP
fn._setup_instr_bp.bp_state
=== Starting Gather and Clear ===
unswitch_regset
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
R12
remote probe closed connection
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
MCORE
_read_memory_slow
(instr & ARM64_MSR_MRS_BASE_MASK) == 0
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
TXU
{%s} handle ROM entry %d (level %u): %08x
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
message
=== Detailed %s Boosters ===\n
Raw level
{%s@%d} Probe response payload read when no payload indicated.
DISCONNECT
MemoryPoolAllocator
Failed To Init Booster's Astris API In: %s with %s (%d)\n
    INFO(%u,%d): %s(%04u): %s(): %s
internal.is_probe_authenticated.debug_auth == NULL
{%s@%d} socket connection is not available
## armcpu: bad status even though all bytes read (%d)\n
astris_jtag_scan_gotorti_impl
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
result.read.memap.s2r_fsm
{%s:%s@%d} [%s] writing WVR %d\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
RF19
Register file 3
CortexM3
cpu_sstep
generated_files
DWT
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
probeNicknames
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
RF62
locationids
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
m_bp_details
{%s:%s@%d} [%s] bad hostname\n
probe [port %u] on localhost
!level_stack_.template Top<Level>()->inArray
soc-name
Failed to safe raise to EL=%d
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
{%s::%s} [%s] unsupported width %d
EXCSAVE7
.user
ret.raise_el.read
copyBoardNameForPrimate
AXcpu_resume_translation
PROBETIMEOUT WHILE READING\n
CPU Name: %s\n
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
high
Unknown
{%s} %s: |%s|-|%s|
cpu_readmem
index < stateCount_
{%s} %sing word #%d at address 0x%09llx: %s
_a64cpu_read_gpr_cached
{%s:%s@%d} el[%d] == m_exception_level[%d]\n
error %s reading DAP MMFR0
SPSR_ELx
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
Failed to convert kisLoc %s to unsigned long long
incr_drain_packets
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
%s%d
SimulatorSWD
astris_write_hang_crumb
Failed to write DCM GPIO (0x%x): 0x%x
false
[1500] Error parsing IR command: %s
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s:%s@%d} [%s] writing OSLAR (oslsr)\n
astris_setup_placeholder
get_ecid
Register file 57
\t%s (%s)\n
Apple
--> cmd        addrsize=%d datasize=%d
Topology
hwbp_remove
   Debug Port: SELECT %X: SKIPPING\n
ApSecurityDomain
reg_name not specified.
Invalid file name: \"%s\". File names must be at least %d characters long.
no DP (Debug Port)
ASTRIS_ERR_FAILURE
ASTRIS_ERR_USB_PROBED
Component is not present
FACTSERNO
Failed to open file for writing
Address formatting failed
Pages %d\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
OFFLINE
param.bp_info.invalid.null
\"%s\" not an implemented register
fn._read_special_reg.srn.regval
start rev and/or end rev is NULL; skipping cpu_desc override\n
ret.cfg_write(R_DCM_GPIO).deassert
par_el1
fn._write_special_reg
param._tgt.invalid.null
base
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
sso_user.sso_data == NULL
Table 5–132
fn._reg_desc_lookup_by_name
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
Fabric access is blocked. Expected if production unit, won't explore further.
get_chipid
AMAuthInstallSupportDictionarySetInteger32
GETSETTCK
' written at document root (failed to create parent object '
{%s:%s@%d} [%s] executing MOV\n
index slot not enabled
LPC11U37
astris_cpu_trampoline
LPC1114
{%s} probe_port = %d
Probe %s removed before port determined\n
host %s
Successfully connected to server, %s:%d
CACHE
L2
Error Reading Device Production-Fusing\n
param.reg_name.invalid.null
OCD.DEBUGCAUSE = 0x%8.8X
%s (%d)
Probe %s status: Busy
Unable to connect to probe server
wir-dpcsoc
{%s:%s@%d} [%s] executing VMOVW\n
{%s:%s@%d} [%s] writing PAR[64]\n
SWDONLY
MiscCortex_t
AXjtag_srst assert failure - %s (%d)
_set_bpaddr_hw
!!!! Critical Error: !(prsr[0x%08X] & DLK) !!!!\n
{%s[select]} timeout while waiting for data from the connection
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
[KIS] Portal Status: 0x%X\n
AXbooster_get_all_boostermanagers
UserCreated
--> psr        size=%3d bit=%d
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
AXcpu_mmu_get_mair
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
fn._ocd_reg_r.dsr.2
Unable to convert plist file name to CFString: %s\n
Die Config Disabled\n
ret.restoring_el_after_raising_to_read_hcr
{%s::%s@%d [%s]} Error %s: pre_resuming HW
Connected to Probe Device Server [Default Log]
Failed calling AppleSOC_t::dock_disconnect_mode\n
set.user
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
{%s::%s} timeout while waiting for EDSCR ITE
Translate Stage Chosen: %d\n
astris_user_default_copy_boardname_for_primate
MASK ERROR
Not supported portal of type: 0x%X
hwwp_enable
@AuthDbg,Ticket
authenticate_dft
{%s:%s@%d} [%s] read cmdAddr failed: %s\n
Table 5–173
fn._read_special_reg.icount
Misc_NoSoC
psr-partition-number
%s
%s%s
Cleaning up Each Booster Manager\n
irlen
process_status_transition
OK
Not Enough Payload For Specified Bits To Shift In OR Write Data Length Mismatch
Efficient-Core
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
ret.read.gpr_1
[AstrisAsync] Discarding response due to ASYNCSKIP state!
cpu is NULL
symbol.check.loaded.AMAuthInstallCreatePtr == NULL
fn._remove_data_breakpoint.which_wp
connection created
ret._a64cpu_read_sysreg_hw
Level-1 exception save location
GETRELAY
[%s] Booster System Is Not Initialized Bailing\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
{%s} halting %s\n
ASTRIS_ERR_VARNOTFOUND
ASTRIS_ERR_MISSINGPARAM
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
appendToArray.error
!!!! Complex CPU Key %s is INVALID !!!!\n
master-size
createKeyWithPrimate
%s status transitioned: %d ('%s') -> %d ('%s')\n
s
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
ret.reg.read.K_DA_REG_NAME_PKA_BASE_LO
Register file 50
[KIS] Address: 0x%llX\n
%d
_get_bpcr_hw
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Update
Optional Key: CPUMonitor not in preferences
Invalid special reg. number %u
param.length.invalid.null
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llX) - reg_count=%d - val=0x%X
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
spsr_select
R8
fastsimSWD
FWUPDATE
cpu_cleaninv_l2cache
Full JSON that failed validation:\n%s
ACC-CTI
fn._collect_snr.exccause
{%s@%d} IOServiceOpen failed, err = 0x%08x
KIS translator version : %d\n
DESIGNER_ARM
addr=0x%8.8X, index=%d, size=%u, flags=%udata=%u, enabled=%u
param.booster_handle==NULL
2: ARM64_SYSOP_ATS12E1R\n
No probes
soc or sysap not available
stream.h
{%s} Failed to extract chip debug base from table (%d); continuing anyway
General register 5
fn._ocd_reg_r.ddr.value
astris_kis_clear_status_registers
Created Connection - : %s
typehint
cpu-dbgwrap-debug
CS-CTI
[AstrisAsync] Complete Queue callback returned %d (%s)\n
Going To Create Generic ARMV8\n
RF21
LOSTCONN
host_to_components
PongoSWD
JSON structure error: key '
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_preferences.cpp
_write_window_base
ASTRIS_ERR_ASYNC_BARRIER
dbgarch
[FLUSH]\n
Shift-amount register
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
GenericValue
[KIS] Portal ID: %d\n
UNKNOWN
cpu-xtensa-non-tie-ranges
OCLA_IP_REGS
[INS_WP] 0x%016llx x %d\n
{%s} %s did not match any valid host
read_via_sock
{%s} 0 words from probe when %d words left to read for reg %d
T32
internal.clear-auth.debut_auth == NULL
param.bp_state.invalid.null
KIS-HUB-NULL
{%s} FIFO full, try again
MAC16 Data register 1
RF3
Register file 53
comparing against match entry %d: %s
Temporary level
.os
xtensa-non-tie-range-name
{%s} Failed to extract IDCODE from table (%d); continuing anyway
ret.read.edscr.after-drain
completedAcmds
{%s} explore with exploreflags 0x%X completed with error [%s]
fn._ocd_reg_r
Koko
Probe %s selected
spsr_el2
CPU ASC Offset: %d\n
result.dbgap==NULL
!!!! Critical Error: Restoring from exception level[%d] other than 1,2 or 3 !!!!\n
[AstrisAsync] Deactivating async...\n
ret._cleanup_hw
[1500] Error parsing bridge '%s': missing required field 'tap'
EDRCR
AXcpu_hwbp_enable
no AP (Access Port)
{%s} _pre_halt_hw result = %s
{%s:%s@%d} Critical error encountered:
AXchip_fromreset
_read_gpr
dbgwrap halt failed, falling back to classic method
{%s} calling _collect_hw on %s
R3
unable to transfer command to/from remote probe
Already connected to
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
RF63
{%s::%s} creating CPU
write.dspsr_el0 NOT CACHED
MEPS
Skipped due to error in Async batch
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
ret.clear.async
Table 5–154
General register 12
fn._init_configuration_by_name.failed
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s} [EDSCR_RXFULL is_64] exec: encode_mrs(0, MDDTR_EL0, true)\n
init_hw.set.dhcsr.en
astris_memap_debug_readbuf
RF23
{%s} valid response from bridge
_suspend_translation_hw
SWDACKDELAY relay write failed\n
connection not currently open
Cannot create DART descriptions from NULL info\n
_a64cpu_reset_catch
%2d) %s %s [Busy]%s\n
AXdebug_auth_clear_sso_user
High level exception save location
Error closing %s [%d]
{%s::%s} [%s] error %s writing SCTLR_ELx
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
RF14
sstep
fn._ocd_exec_instr.wsr.reg_srn.t1
fn._ocd_reg_w.ddr.tgt_32
{%s:%s@%d} [%s] scanning out (DSCR)\n
AuthDbg,SecurityDomain
fn._gen_debug_interrupt
{%s@%d} Connection to server rejected, error=%d (%s)
exploreCPU
setToolInfo
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
SSO with no prompt being used
cpu_writereg_vals
set.probe_name
EXCSAVE4
MEVADDR
fn._ocd_reg_w.dcrset.regval
can't find pid in response\n
{%s} unmodified-probe_match = %s
Selecting
15002AXI
first read of CMDSTAT may fail if external reset occurred
getOrCreateValue: addMember failed, returning doc root
newpos <= pathpos
param.op.AXCPU_WP_ENABLE.unsupported
%s: chip was NULL when attempting to release soc
engineer
_resume_hw
hwwp_insert
   Debug Port: Trying SELECT %X\n
RF32
fn._ocd_exec_instr.wsr
[ARM64 INS_WP] 0x%016llx x %d\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
internal.authenticate_probe.chip->soc == NULL
resolve_debug_components
full word
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
SCTLR__ELx
EL3h
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
armv7m-region-type
1: ARM64_SYSOP_ATS12E1W\n
AXarm7_dbgread
RaspberryPi3_t
AXbreadcrumbs_read
write.dlr_el0 NOT DIRTY
PARTNO_ARM7TDMI
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
DSR
SRSTM
bypass-config-name: %s\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
memory_write
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
PC
is.Peek() == '['
fc_ite_checks=%d
AXcpu_readreg
   CPUID: 0x%08X\n
uri.h
ret.faul_reg_latch
Requested Register Requires EL: %d - Highest EL: %d
-
{%s=>%s} no soc reference; falling back to direct cpu method
Successfully Authenticated DFT\n
debug_info
MiniSWD (USB Comm)
--> master     size=%3d localwrstn=%d debug=%d
CPU[%s] Read Reg: %d
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
INVPARM
Invalid encoding in string.
prettywriter.h
darts
{%s:%s@%d} [%s] checking for data abort\n
_set_halting
High level 2 exception PS
jtag_cmd
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
   Debug Port has unknown type\n
panic_diagnostic
messages
dpb-tpser-id
GPR_1
virtual int ARM7cpu_t::_halt_hw()
{%s} skipping dcache flush, cache already clean
CPU has no regions, maybe powered off?\n
ASTRIS_ERR_TIMEOUT
kext connect name %s\n
Primate-Null
fn._write_mem
Cleaning up Main Booster Object\n
DISPEXT
entry.exception_test_0
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s:%s@%d} [%s] reading DFAR\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
astris_jtag_get_pipe_cycles
{%s:%s@%d} [%s] executing LDCpi\n
[%s] %d -> %08x\n
OCD Debug data register
RF33
fn._read_special_reg.ibreaka1
Can't get hardware model - failed to allocate data buffer
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
Key is null
%s\n
handle_pending_async_aborts
read-back (sys AP) failed
Unique required when %d probes
.rsd
{%s@%d} Received %d bytes when requested %d bytes.
Invalid Bundle: %s
Requesting %u > 4 while address is NOT doubleword aligned
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
symbol.check.loaded.AMAuthInstallSetSigningServerURLPtr == NULL
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
PROBED_USB_RSP_ERROR
cpu_lacc_status_insert
AUD
PORTAL UNAVAILABLE
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
fn._ocd_exec_instr.wsr.ddr.t1
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
PoodleSWD
cpu_translate
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
is_ecid_zero
poo
bundle_id
CDPUL
[ARCH32] Failed to exec MRS to move contents of MDDTRRX (containing val to write) into scratchscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
ITO
Probe (port=%d) with unknown status %s dropped from available list
fn._write_general_reg
Debug Base: 0x%llX\n
ARM64cpu_t
ASTRIS_ERR_EMPTY
Async barrier encountered
Probe %s USB-C location is %s
m->name.IsString()
\tReading left over chunk 0x%x @ 0x%llx\n
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
LPC1102
Register file 39
RF47
reg_name (\"%s\") not implemented, missing Xtensa option.
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
{%s:%s@%d} exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this...\n
High level 4 exception PC
RF35
OCD.DSR=0x%8.8X
#ch-
Register file 5
spsr_el3
\tAligned Read Failed
Could Not Allocate Mutable Dictionary For BoosterMangers
xres = %p, table = %p, key = %d
High level 3 exception PS
Invalid escape character in string.
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
dfu-Type: %s\n
param.subsystem == NULL
AXcpu_mmu_get_tsz
   Created Fake Debug Port Debug Port
Top
AXjtag_explore failure - %s (%d)
Could Not Find The Entry Function: %s
cpu-die
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
ret.clear_authentication
param.ticket_data == NULL
Hifi3
Could Not Find Any Boosters of Type: %s\n
_sw_breakpoint_insert
ret.cpu.nmi()
fn._ocd_exec_instr.rfdd
astris_conn_has_kis
HCR_EL2
_a64cpu_read_edscr_masked
## armcpu: success status even though not all bytes written\n
astris_user_default_copy_nickname
LPC1778
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
PMGR_OCLA_REGS
!!!! Critical Error: (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0 !!!!\n
AXconn_connect_kext
probe on host %s
postconnect
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
3679.40.30b172
un-sel-sib-network
{%s:%s@%d} [%s] getting GPR 0\n
[!ARM64] exec(DCPSX_BASE_ENC)
base_reg < 15
relay_get: %s = %d
{%s:%s@%d} [%s] checking DCC\n
AXcpu_hwwp_enable
LPC1112
TMM
{%s:%s@%d} [%s] executing MRS\n
CTI_CH_PULSE
Cycle number to inter.
Error %d (%s) while expanding ~ for Astris history save\n
AXconn_kick
{astris_probed_print_events} not supported in this build configuration
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
read memory (permission checks suspended)
Enabled
[1500] Using %s.plist
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
Register file 11
fn._ocd_reg_w.ddr.1
a
-Lite
{%s} probe_match = %s
could not get runtime env
Values Not The Type We Expected. Expected: Number and String\n
astris_explore_enabler_get_subsystem_status
[READ] cop %d -> 0x%08x\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
ret.reg.write.K_DA_REG_NAME_CHIPID
api.is_prod.chip->soc == NULL
ASTRIS_ERR_OK
AstrisSWD
DBGWRAP_PAUTH
astris_explore_enabler_del_cpu
_flush_state_hw
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
Aligned Address: %llx
{%s} %s status failed. error: %d (%s)
Atomic Oper, Control
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
Error returned from explore_pid
postinc < ARM64_LDRSTR_POSTINC_MAX_IMM
couldn't read TTBR1
createCPU
Invalid width = %d bits.  Must be 8, 16, or 32.
default
write.reg.not cached
[%s] {%s->%s} Transitioning to exception level %u.\n
DCCCTRL = %08X   res=%d\n
Invalid num_regs = %u. Should be 16, 32, or 64.
ASTRIS_ERR_HTTP_FAILURE
setResult
In Eraseflash\n
dspsr_el0
CTI_INT_ACK
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s} %s DC cache already clean since last halt, skipping flush
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Generation of the nonce timedout\n
Table 5–153
ocd_base_address = 0x%8.8X is not 4 KByte aligned
No loggers container
Complex CPU Name: %s\n
_check_abort
%-16s
M23
framework_url == NULL
AMAuthInstallSupportDictionarySetInteger64
LPC1111
RF31
complexes
[AstrisAsync] astris_async_override_disable_async: conn is NULL
ret.dbgap.memap_write
Register file 7
fn._ocd_exec_instr.rsr.ddr.t1
path
result.extract_group_info==
Switch to primate res: %s\n
OPEN
CortexM33
Could Not Get BoosterManager\n
implementer
ret.write.msr_lock_reg
cs_type:0x%x
AXchip_getinfo
** \tTatsu AuthDebug Triage | All     **\n
Register file 6
Can't get OS build version - failed to create URL
result.init==
AXdebug_auth_get_dft_timer_count
fn.AXmemap_write.address.regval.
UNKNOWN_CODE
memap_bus_write
Dart CPU SID(s): %s\n
CPU.ARM64
Unable to read CPSR
NC
op_TIEInitiateReadProtectedI_encode
Unable to allocate memory for big response
AXdisassemble_at_addr
cpu-group
SP
Need to be connected to set nickname
[AstrisAsync] Activating async...\n
probing %s status\n
{%s:%s@%d} [%s] prepare failed: %s\n
Table 5–172
{%s} Failed to extract portal info from table (%d); continuing anyway
{%s:%s@%d} [%s] writing DTRRX(uint32_t)\n
{%s::%s} ERROR %d(%s) resuming %s\n
!!!! Critical Error: exception other than an abort (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
RF22
PROBED_SLEEPING
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
version
{%s} [exception_level(%d) != current(%d)] exec: DRPS_ENC\n
[Auth Debug] Disabled\n
high level connection to probe [connect state/status]
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
getOrCreateValue
Base::level_stack_.template Top<typename Base::Level>()->inArray
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
abort
Spew change. old=0x%016llX, new=0x%016X
Unspecific syntax error.
SWDFlasher
cpu-xtensa-num-wp
SCODEC
RF2
ASTRIS_ERR_PROBEERROR
DCS10
get_current_mmu_regs
{%s} %s DC cache clean complete, marking as clean
unable to read memory (permission checks suspended)
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
PARTNO_KIS
param.len.invalid.>64
var._tgt.invalid.null
%s %3d'b%s\n
connecting to selected probe (single_port)
Probe %s with unknown port response %s
PushUnsafe
ret.reg.write.K_DA_REG_NAME_NONCE_3
check_timer_and_clear_timeouts
fn._ocd_reg_dsr_clear_and_validate
Main
preflash_type
{%s:%s@%d} [%s] scanning out\n
CTI_CTL
ret.drain.half-duplex
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
{%s} FAILURE - NULL parameter
No 1500 bridges or TAPs specified (v2 plist)\n
{%s::%s@%d [%s]} Error %s: checking exception
Failed to exec MSR to move scratch containing sysreg to MDDTR.scratch=%d, sysreg=0x%X, regname=%s
JTAG
LPC1764
fn._ocd_exec_instr.rsr.ddr.t1.1
couldn't find CPU1. this is expected sometimes.
DISPDFR
Register file 26
Connecting to server, %s:%d
Too many portals, we are at portal: %d while max is %d\n
regidx_save=%u
collect-probemap
AXportal_reset_dcm
EL2h
create_using_builtin
EPC7
coredump
{%s:%s@%d} current_el[%d] == 1|2|3\n
astris_memap_debug_writebuf
VECBASE
{%s} Found extra info in = %s, chopping string
result.ide==NULL
SPSR_EL3
internal.enable-test.chip->soc == NULL
Register file 34
%s_probe
APF
Append
_setup_wp
AuthDbg,Nonce
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Can't get hardware model - failed to find matching IOService
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
cpu_getinfo
Unable to restore EL0
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armcpu.cpp
resolve_platform_details
{%s::%s} halting %s\n
dest_gpr <= 15
probetimeout retrying access...\n
RF36
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
result.read_vals(table)==
{%s::%s} [%s] !bpwp_initted, retrying init
Table 5–180
Toto
applesoc == nullptr
ERROR: nothing to do; resuming address translation for %s without previously suspending it
astris_booster_cleanup
entry.exception_test_1
\tReading left over chunk expected 0x%x got 0x%x\n
IOService
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s=>%s} null reference to AXchip_t[0]
fn._write_special_reg.srn.regval
IsArray()
dart-coastguarded-cpu
misc-wirtestporten
Failed to explore chip: %d
ret.clear_dft_authentication
type == kStringType
fn.exit ERROR
FAR_EL1
sr=%u,ar=%u,opcode=0x%6.6X
fn._ocd_exec_instr.TIECompleteRead
access to target is blocked
{%s@%d} Failed to send probe command (error %d).
complex-base-address
fn._return_from_debug_interrupt
ARM7
SCANDEBUG
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
```
