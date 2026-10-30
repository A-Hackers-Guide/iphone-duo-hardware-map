# `/usr/local/share/astris/boosterpack/swdflashers/arm_adi_swdflasher.booster/arm_adi_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,751,600 bytes.

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

## Strings (6,725)

First 2,500 of 6,725.
```
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Booster Info:\n%s
Pages %d\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
No 1500 bridges specified\n
Failed To Instantiate SOC From Booster\n
{%s} already collected %s, skipping
{%s} FAILURE - max length exceeded
{%s:%s@%d} Critical error [radar already requested]
Probe (port=%d) with unknown status %s dropped from available list
[1500] run_steps: unknown instruction '%s'
[1500] v2 plist missing required field 'taps'
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
SoC BM Not Found, Bailing\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
[COLLECT] Chip %x\n
codeblock
{%s} unable to allocate probeInfo
%s SoC created
Required Key-Value is a string, and not an array. Old booster found\n
pmu-name: %s\n
Gateway Version: 0x%X\n
{%s::%s} %s resumed\n
{%s::%s} cpu powered off: failed init() %s
{%s} pmgr status=%d being reported as Unknown
signature was NULL
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Required key: %s @ index %d is NULL\n
{%s::%s} [%s] MMU not active - returning %s
   {%s} APB/AXI address for target setup = 0x%llx\n
can't find pid in response\n
AXconn or json_out are NULL
{%s} %s
Passed NULL plist file\n
CPU Core Number: %i\n
[AstrisAsync] Discarding %zu completed command(s)\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
      Select port %u: AVOIDED\n
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
setCategoryValue: path='%.*s'
     0x%016llx: ERROR\n
[INIT]\n
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
[PAW] Failed KIS Portal Access Preflight =%s (%d)
\n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
** Unauthorized User/Network or ECID **\n
Programming...\n
AXportal_t Struct Is NULL
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
Subsystem Monitor[%i]: %s\n
{%s@%d} Failed to find cached response
Dart Dart Type: %s\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
ERROR: unable to suspend translation for %s
{%s=>%s} AXconn_t has no chips
%s construction failed
%2d) %s %s [Busy]%s\n
CPU Die: %d\n
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
{%s} Error setting up jtag-ap target (%s)
{%s} flags:0x%08x
probe event: %s
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
KIS translator version : %d\n
Please answer y=yes or n=no.\n
Cannot create SoC [unknown chip identity (%d)]
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} Failed to get watchpoint count for %s: %s
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Using Built In SoCs\n
[%s] cop %d -> 0x%08x\n
{%s} Unable to read SP_EL0
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
Spew change. old=0x%016llX, new=0x%016X
{%s} probe_port = %d
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
{%s@%d} socket connection is not available
{%s@%d} Unknown CS code [%u]
!!!! DART Key %s is INVALID !!!!\n
error %s reading DAP MPIDR
outstanding=%zu
{%s} 0 words from probe when %d words left to read for address 0x%016llX
{%s@%d} Timeout while sending probe command.
comparing against match entry [pid] %d: %s\n
SoC does NOT support IDE Explore\n
Did Not Find Any Boosters For: %s \n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s::%s} creating placeholder for CPU: name=%s
USER %s(%04u): %s(): %s
1: ARM64_SYSOP_ATS12E1W\n
2: ARM64_SYSOP_ATS12E1W\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
Taking gateway control failed
AXjtag_srst deassert failure - %s (%d)
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
Banana split probe, for now I guess we will just say yes...\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
[SSTEP] bvr=%08x bcr=%08x\n
[ARM32cpu_t::_read_register64] 0x%08x\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
{%s} valid response from bridge
[1500] IR command '%s' missing required field 'opcode'
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
[AstrisAsync] Got ASYNC_RESTART response!
Breakpoint Enabled: %s
Fabric access is blocked. Expected if production unit, won't explore further.
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
{%s} explore with exploreflags 0x%X complete [%d chip%s]
\t%s (%s)\n
Values Not The Type We Expected. Expected: Number and String\n
[1500] Using %s.plist
{%s::%s} [%s] error %s reading SCTLR_ELx
AP is NULL
\tPrologue Aligned Read Failed
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
Portal Status, Changing STATUS and CMD/STAT to reflect
[KIS] CMD: %s \n
[1500] %s step %d: unknown instruction '%s'
Groups %d\n
[%s] {%s->%s} Transitioning to exception level %u.\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
Kick off the current process using probe %s? (y|n)\n
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
Found form-factor specific channel %u for device '%s'
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
{%s} Unable to read CPSR
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
{%s@%d} Unable to create socket
start rev is not of expected format; skipping cpu_desc override\n
Logging Context Is NULL\n
[PAR] Failed KIS Portal Access Preflight =%s (%d)
     ARM %s breakpoints: %u\n
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s::%s} EDSCR with TXU set - unable to recover.\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
  Error path [%s]\n
Probe %s Device Server listening on port %d
Exception %d Stack Trace
[%s] TGE is set so we traping to EL2\n
CPU: %s halting debug is now %s\n
\tReading left over chunk 0x%x @ 0x%llx\n
AP[%d]: unknown type\n
[Auth Debug] Disabled\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
DEMCR: 0x%08X -> 0x%08X
Going To Create Generic ARMV7m, but typehint is present (%s)\n
%s @ 0x%08llX : read failed/n
comparing against match entry %d: %s
Could not find TAP at index %d to attach 1500 bridge to\n
Not Creating CPU: %s\n
Start Page: %d\n
{%s::%s} failed: %s
{%s} (end) current_el is now %d
   DPv3 BASEPTR0 is 0x%08X\n
SWDACKDELAY relay write failed\n
checking if relay \"%s\" is valid
haskis bit not set\n
There is no system bus access port on the debug port
DBGSTATUS = %08X   res=%d\n
[HALTED] dfsr = 0x%08x\n
[AstrisAsync] Barrier before pause\n
[AstrisAsync] replay preflight: Async not active!\n
Can't get OS build version - failed to open ReadStream
Can't get OS build version - failed to get build version
invalid IR command '%s'
HOSTID bit not set\n
Cleaning up Each Booster Manager\n
{%s::%s} timeout while waiting for EDSCR ITE
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
Probe %s Device Not Connected on USB-C Port
start rev and/or end rev is NULL; skipping cpu_desc override\n
Debug Base: 0x%llX\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Optional Key: CPUMonitor not in preferences
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Error while trying to authorize: %d - %s\n
Probe %s LocationID Info is %s
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
{%s[recv]} %d(%s) [RETRYING]
{%s::%s} HDE not set on %s. Will re-enable.
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
ERROR!! Wrote %zd bytes, expected %zd\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
Can't get hardware model - failed to allocate data string
     0x%016llx: 0x%04x      %s\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
Board ID: 0x%X\n
CPU %s not found or already removed from the map
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
Failed to get PMU Name
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
Subsystem Monitor Key does not exists: %s\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
!*!*!* ****************************************************************************** !*!*!*
no system bus AP present when expected
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
Type 'jebdump' to do scan/mem dump\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
JsonLogger: Writing category '%.*s' to '%s'
{%s} no response from bridge
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
Failed to read ide_table from KIS explore
Breakpoint Size: %d
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
Caught a portal that we dont have a status map for: %d
Probe Map comm error %d(%s) %s
Unable to convert plist file name to CFString: %s\n
[KIS] Portal Status: 0x%X\n
Size or Count provided are 0.
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s} L2 cache operation completed [%s]
{%s} no chip found
{%s} hostname:%s, flags:0x%08x
{%s} probe_match = %s
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
Xtensa Option reg_file_size: %d
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
--> debug      size=%3d acsr=%d
[MEM] Uncompleted; DSCR = %08x\n
Length is 0
Dart Base Address: 0x%llX\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
{%s::%s} [%s] !bpwp_initted, retrying init
relay_get: %s = CMD_ERR (%s)
KIS Preflight No Need To Write to AP CSW
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
Stepping Stone Final =  %#x\n
{%s} Error looking up architecture (%s)
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
using multi-target booster products_%s.plist
%s constructed
Probe %s with unknown port response %s
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Invalid Bundle: %s
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
Too many portals, we are at portal: %d while max is %d\n
    INFO(%u,%d): %s(%04u): %s(): %s
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
Could Not Allocate Booster Location Array
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
Error status from AMAuthInstallSsoEnablePtr = %i
Can't get hardware model - failed to find matching IOService
{%s} unmodified-probe_match = %s
Connected to Probe Device Server [Default Log]
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
error %s checking for data abort
Unable to read LR
KIS Chip Found, Doing KIS Explore Setup
\nSaved %s binary data to %s\nWrote %lu bytes\n
bypass-config-name: %s\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
   JEDEC ID: 0x%08X\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
[SSTEP] using BP %d\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} timed out waiting for cpu to halt during collect
## apw %u 0x%08X 0x%08X ...(%d)\n
Xtensa Core %s NOT configured\n
--> misc_wdr   size=%3d wirtestporten=%d
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Matched via Bundle ID\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
Previous authentication in-flight, wait for it to finish\n
JsonLogger: Created with default schema version '%s'
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
XBS Version Modified: %s -> %s\n
--> cmd        addrsize=%d datasize=%d
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
Hang Description:\n%s\n
Successfully connected to server, %s:%d
Creating CPU Returned: %s\n
{%s} %s resumed\n
{%s::%s@%d [%s]} Error %s: collecting HW
Error %d (%s) opening cmd snapshost save file
{%s}#%02X %s [%s]
{%s} 0 words from probe when %d words left to read for reg %d
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
Failed explore before forced KIS reset: %s\n
[AstrisAsync] Activating async...\n
{%s} Error setting up memap target (%s)
Unable to create pthread key for conenction. errno=%d %s.
Could not find TAP at chip-index %d for v2 1500 config\n
SOC_t::{%s} CPU_t group=%d when group 0 expected
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
Die Config Disabled\n
Invalid file name: \"%s\". File names must be at least %d characters long.
   {%s} Read AP's R_MEMAP_CSW\n
PKA Base: 0x%llX\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
ERROR!! write binary data parameters invalid\n
Created Connection - : %s
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s::%s} ITE is not set: 0x%X\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
{%s} %sing word #%d at address 0x%09llx: %s
In Postflash\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s@%d [%s]} Error %s: flushing HW state
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
{%s=>%s} null reference to AXconn_t record, `conn`
Original Length: %d\n
Failed to convert %s key @ index %d to a number with base of %d\n
{astris_probed_print_events} not supported in this build configuration
[INSBP] bp%d addr=%08llx fpr=%08X\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
## apr %u 0x%08X -> 0x%08X\n
Failed to explore chip: %d
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
[READ] %d -> %08x\n
## armcpu: success status even though not all bytes read\n
{%s} checking for single_port probe daemon on port %d
Connected to Probe Device Server [Log File %s]
{%s} Error %d(%s) sending message
Skipping CPU %s at 0x%llx: not present in IDE\n
Gathered Info:\n%s
CPU PS-Register: 0x%llX\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
WARNING, reserved / slide bits not zero! Zeroing out!\n
## memapr %u 0x%016llX -> 0x%08X\n
SSO with no prompt being used
Can't get hardware model - failed to allocate data buffer
Replacing key with value
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s} ROMTABLE (nest=%d)\n
signature: 0x%08X
Error closing %s [%d]
Dart Name: %s\n
Invalid current AP (%d), adopting APTABLE (%d)
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
unable to obtain sysap
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
[PREFS] Key: %s - Val: %s
{%s} Failed to extract die infofrom table (%d); continuing anyway
[FLUSH]\n
Aligned Address: %llx
Failed to sync prefs at end
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
%s: []\n
probetimeout retry failed logging as hang\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Match Count is Zero. This is invalid.
Booster Value is Not String\n
Map is empty, not removing CPU %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
Bundle: %s NOT FOUND\n
{%s->%s} m_exception_level=%u
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
Chip %x Status = %d\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
[PREFS] Key: %s - Val: NULL
Found match - bypass_device: %s; channel: %d\n
write to CMD/STAT failed - %s
Complex CPU ID: %d\n
%s\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
[INSWP] 0x%08llx wp%d rdwr=%X\n
Could not find portal by select %d, while interpreting result\n
{%s[select]} %d(%s) [RETRYING]
%s status transitioned: %d ('%s') -> %d ('%s')\n
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
couldn't find CPU1. this is expected sometimes.
Booster:\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
replay_counter=%lu, last_replay=%d
      Select of JTAG-AP port %u failed with %s\n
Could Not Allocate Loaded Booster Array
[1500] Error parsing IR command: %s
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
CPU (%s) has explore flag of: 0x%llx which is not set\n
dfu-Type: %s\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
{%s} asc status=%d being reported as Unknown
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
OS build version: %s
JsonLogger: Schema loaded successfully for category '%.*s'
Could Not Find Any Boosters of Type: %s\n
BoosterManager Types:\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
[READ] cop64 %d -> 0x%016llx\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
   Debug Port: Trying SELECT %X\n
X09 Part
ERROR!! Couldn't save %s binary data\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
[%s] chipinfo is NULL
[AstrisAsync] Complete Queue callback returned %d (%s)\n
Buffer is NULL
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
Valid Portal
CPU AP-Select: %d\n
Complex ID: %d\n
Complex Address: 0x%llX\n
--> localwrstn size=%3d debug=%d
Failed to find a plist for this soc %s
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s@%d [%s]} Error %s: checking exception
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
Booster System Is Not Initialized Bailing\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
## dpr 0x%02X -> 0x%08X\n
AP[%d]: MEM_AP_AXI\n
Could Not Allocate Mutable Dictionary For BoosterMangers
Die-Count: %d Current-Die: %d Die-Type: %d
[AstrisAsync] replayConditionalCheck: condition hit!\n
{%s} connectName[local host]
relay_get: %s = %d
{%s} set=%u (sh=%u), way=%u (sh=%u)
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
Failed to create optional file. Not fatal, moving on
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
{%s@%d} Connection to server rejected, error=%d (%s)
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
%s NOT configured\n
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} error: %s
%s %3d'b%s\n
{%s::%s} creating AP slave: name=%s
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
Init objects failed
TargetSel Before Disable: 0x%x
AXportal_t Is Not Valid Type - %d
Invalid current AP (%d), adopting latest (%d)
AP[%d]: MEM_AP_APB\n
Probe %s USB-C location is %s
%#09llx-%#09llx: %s\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Request Dict:\n%s
Failed to get DFU Type
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
Stop Clock: %s\n
read_dbg failed to access R_v7M_CLIDR
Using Built In CPUs\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
Debug Clock Already Enabled
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s:%s}: cpu powered off: unable to access a register for this CPU
[%s] {%s->%s} END handling exception
[ARM64 INS_WP] 0x%016llx x %d\n
[AsyncSnapshot] #%zu: %s\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
Initial DSPSR_EL0: 0x%llx
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
Cached async_replay capability version: %u
Width: %d not supported
{%s} %s status failed. error: %d (%s)
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
      Read of JTAG-AP port %u CSW failed with %s\n
{%s} host name(RSD): %s\n
SoC must have a DAP
Setting CPU %s is_boot_core to %d\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
Error %d (%s) opening history save file
Min Component - %s\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
{%s} FIFO full, try again
CPU Explore: 0x%llX\n
Complex Name: %s\n
Chip Revision: 0x%X\n
{%s::%s@%d [%s]} Error %s: resuming HW
Unable to read CPSR
## apr %u 0x%08X %d -> 0x%08X ...\n
New Length: %d\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
{%s} status=%d being reported as Unknown
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
getOrCreateValue: addMember failed, returning doc root
CPU ASC Offset: %d\n
product-name: %s\n
{%s->%s} current EL (%d) already == target EL.\n
{%s::%s} error %s writing EDSCR %s
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
[1500] TAP key is not a valid integer
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Invalid Size Given for AP AP=%d Size=%d
{%s} host:%s, flags:0x%08x
Got an error reading the DCM Control Register: %s
==== User Error Messages ====\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
--> 0x%02x = %s
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
In Readflash\n
successfully updated DEMCR
Async is disabled for localhost connection
## memapw %u 0x%016llX 0x%08X ...(%d)\n
Xtensa Option num_wp: %d
=== Starting Gather and Clear ===
--> master     size=%3d localwrstn=%d debug=%d
Could Not Get BoosterManagerUtility\n
!!!! FILE RADAR: Don't know how to compare two values\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Complex Type: %s\n
Complex CPU Name: %s\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
failed write of 0x%08X to DEMCR - %s
[AstrisAsync] Discarding response due to ASYNCSKIP state!
register lookup by name not supported when Astris is statically linked
{%s} Extracted CIP Gen Number from table  (%d)
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
{%s} probeList has probeCount of zero
{%s} bridge returned SLVERR
{%s} failed (%s)
Xtensa Option options: 0x%x
Can't get OS build version - failed to create plist
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Could Not Get BoosterManager. Need To Call AXbooster_init\n
[%s] %d -> 0x%08x\n
\t\tARMv6 debug CPU xxx ID\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
Variables not setup
SOC AP[%d]: JTAG_AP\n
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
Sprocket probe, for now I guess we will just say yes...\n
[1500] Error parsing bridge '%s': missing required field 'select'
Die Config Disabled
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
   Debug Port: SELECT %X: DISABLED\n
Init dbgwrap obj failed
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Invalid file name: \"%s\". File names must not start with '.'
{%s} read ESR EL1|EL2|EL3 (%d)
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
AP[%d]: MEM_AP_AHB\n
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
SoC has been setup using standard instantiation (setup result=%d)
{%s} Error reading PID (%s)
Failed to convert CFArray to C Array\n
Probe %s removed during selection process
Old ProbeDaemon does not support this command
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
There is no debug port associated with this chip.
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
Raising to EL2 cause in Guest\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Error %s connecting to server %s:%s [RETRYING]
relay_get: %s = ERR
{%s} Failed to resume %s: %s
   {%s} Clearing HNONSEC on AP \n
!!!! CPU Key %s is INVALID !!!!\n
Failed to sync prefs at beginning
caller=%s, async=%d, iterations=%lu
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
Awaiting next chunk of big response
{%s@%d} Drain empty on decr [%s].
{%s@%d} Unknown CS command error [%d]
AXconn_t Struct Is NULL
DEMCR write failure - %s (%d)
Could Not Allocate All Boosters Array
Dart CPU SID(s): %s\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
[%s] EL @ end of Collect: %d\n
Error %d(%s) executing instruction 0x%08X
{%s->%s} (top) current_el=%d
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s->%s} ERROR=%d(%s)
{%s} %s DC cache already clean since last halt, skipping flush
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
{%s} Exploring with option: %s\n
Could Not Match A Booster for %s\n
CPU Address: 0x%llX\n
CPU Supported in Integration: %s\n
{%s} Failed to extract CID from table (%d); continuing anyway
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
X06 Part
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
\t0x%08llX...\n
coalesced-target: %s\n
[REMWP] wp%d\n
VBAR: %#x\n
\tLeft To Read (%d) < width (%d).\n
   DPv3 baseptr is not valid (%X)\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
{%s@%d} neither socket nor kext connection available
[KIS] Words (Read/Write/Wrote): %d\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[INS_WP] 0x%016llx x %d\n
     ARM %s debug CPU rev %d\n
   {%s} Enabling debug unit\n
{%s} already connected
Probe Map comm error %d(%s) %s [%s]
no debug bus AP present when expected
** \tTatsu AuthDebug Triage | All     **\n
CPU Monitor key does not exists for: %s\n
!*!*!* Lightning header facing up.                                                    !*!*!*
{%s} Found extra info in = %s, chopping string
{%s@%d} Received %d bytes when requested %d bytes.
Problematic JSON value:\n%s
==== Exception Trace ====\n
[MEM] Aborted; DSCR = %08x\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
dbgwrap halt failed, falling back to classic method
Successfully Authenticated Probe\n
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
TatsuServer Found: %s\n
Xtensa Option dbg_intr_level: %d
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
component group %d\n
[CLEANUP]\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
AP[%d]: JTAG_AP (Exploring Later) \n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
{%s} Debug Base: %08X
Modified Word To Write: 0x%08x
[AstrisAsync] Completing all async commands. Initial err = %d\n
{%s} Error reading CPUID (%s)
%s @ 0x%08llX : 0x%08X/n
Abnormal %s termination: Assert Area Mask = 0x%016llX
JsonLogger: Loading schema for category '%.*s' from '%s'
We Are Matching Development Booster\n
{%s} Failed to extract PID from table (%d); continuing anyway
   Debug Base: %08X\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
process (%s) (%d) path: %s
Failed to create CPU %s - %s\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
[READ] cop %d -> 0x%08x\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
[AstrisAsync] Barrier hit!\n
OK: address translation resumed for %s successfully
{%s} FAILURE - malloc error
X00 Part
{%s} bridge returned an error
Both debug and xbs versions are set, maybe a bug: %s
\t\t%s\n
{%s} calling _collect_hw on %s
   Debug Port: SELECT %X: SKIPPING\n
   MEM-AP not enabled\n
Connected to Probe Map Server
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
Successfully Authenticated\n
Hardware model: %s
%s probe[*] from Probe Map Server [%s]
Booster Bundle: %s\n
Passed NULL booster without custom plist\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
{%s=>%s} no soc reference; falling back to direct cpu method
SoC not identified by IDCODE - enumerating instead of instantiating
   ROM entry %d (level %u): AVOIDED\n
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
Error - eraseflash failed.\n
{%s} [%s] m_exception_level=%u\n
Highest EL: %d, -- Min Op EL: %d
Failed to access new_cpu status
Error status from AMAuthInstallSsoSetStealthModePtr = %i
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
dropping empty probeInfo (port=%u)
Unknown number of groups in the explore table; can't parse group attributes
[%s] %d -> %08x\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
unknown match criteria type: %d
In Preflash\n
AXmemap_readvals failure - %s
{%s::%s} %s pre_resumed\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
unknown chip id: 0x%x\n
{%s} unable to allocate probe name
[KIS] Portal ID: %d\n
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s::%s} waiting for EDSCR ITE
Unable to read SP
{%s} Component ID read fail for 0x%llx (%s)
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
%s: chip was NULL when attempting to release soc
Going To Create Generic ARMV8\n
OK: address translation suspended for %s successfully
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
CPU state %d
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
{%s} handle ROM entry
      Select port %u: already explored..re-exploring\n
[PREFS] Key: %s - Val: ??
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
[%s] m_dc_max_level %d, m_ic_max_level %d\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
{%s@%d} Timeout while attempting connect to server
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
no system bus AP present with AHB, trying AHB5
[1500] Error parsing bridge '%s': missing required field 'tap'
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
probetimeout retrying access...\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
Probe %s selected
%s probe[*] from Probe Map Server [local host]
Failed to convert kisLoc %s to unsigned long long
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
can't find bid in response\n
Awaiting response from Probe Map Server
relay_set: %s = CMD_ERR (%s)
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
KIS Readvals putting back the value
Cleaning up Main Booster Object\n
CPU Typehint: %s\n
[HALT] Chip %x\n
## armcpu: bad status even though all bytes read (%d)\n
   DPv3 bus is %u bits wide\n
{%s} host = %s
{%s} probe_host = %s
{%s} read %d words from probe when %d words requested
=== Ending Gather and Clear ===
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
{%s} empty response string provided
Failed To Init Booster's Astris API In: %s with %s (%d)\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
Found the RTXCID Structure!\n
## armcpu: success status even though not all bytes written\n
{%s@%d} Probe reported connection lost [PROBEEOF].
ADI Preflash\n
** Add the --with-force option or use the explore_override console command **\n\n
[AstrisAsync] Pausing Async Mode\n
\tLeft Over Chunk Read Failed\n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
Invalid SoC Booster. SoC Booster Requires PID\n
New format for cip gen register, unsupported: %d\n
[READ] %d -> 0x%08x\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
%s status is '%s'\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
We are Deallocating\n
{%s} halting %s\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
{%s} skipping dcache flush, cache already clean
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
Error - reflash failed.\n
choice: %d\n
Probe %s removed prior to kick\n
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
--> extrawrstn %d
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
[RESUME] Chip %x\n
Invalid APTABLE (%d), so using most restrictive
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
[%s] E2H is set, virtualization is supported\n
{%s} Reading base 0x%llx entry's component ID
Previously dumped the process tree, skipping
Issuing request to Probe Map Server: %s
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s} %d(%s) [RETRYING]
Asked To Write To A Negative Register Index
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
type_hint not NULL, but creating a placeholder, this is off
{%s@%d} IOServiceOpen failed, err = 0x%08x
%2d) %s %s%s\n
{%s@%d} Found cached response
Asked To Read A Negative Register Index
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
{%s} _pre_halt_hw result = %s
AP Only Explore was asked for, stopping here
{%s} Class 9 ROMTABLE (nest=%d)\n
Setting bypass channel to: %d\n
Found another target for the plist\n
SoC has been setup using standard instantiation (setup result=%s)
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Failed to create Xtensa CPU %s \n
  Nested path: parent='%s', child='%s'
ADI Postflash\n
   Debug Port not responding (%s)\n
{%s} probe [%s] added to list
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
CPU Supported in Runtime: %s\n
[AsyncSnapshot] No snapshots collected\n
{%s} Failed to single-step %s: %s
Breakpoint Address: 0x%llx
{%s} PRIMECELL [DONE]
Error Reading Device Production-Fusing\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
[KIS] Address: 0x%llX\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
iter=%lu
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
Probe %s Device Does Not Have LocationID
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
Production Fused Device\n
Preferences does not exists: %s, creating one.\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s}ERR: bypass_device_name is NULL\n
ERROR: unable to resume translation for %s
Erasing...\n
Failed to get KIS translator version\n
pc:  0x%16s cpsr: 0x%16s %s\n
[AstrisAsync] Resuming Async Mode\n
Failed to read IDE through DAP\n
Could Not Find Any Loaded Boosters of Type: %s\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
** CPU %s requires forced explore override flag on this SoC **\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[%s] CPU BM Not Found, Bailing\n
Failed to convert kisHubLoc %s to unsigned long long
{%s} %s: |%s|-|%s|
{%s} category=%d
{%s} m_exception_level(%d) != current_el(%d)
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
{%s} %s did not match any valid host
%s probe[%s] from Probe Map Server [local host]
%s Bridge @ 0x%09llx-0x%09llx: %s
Failed to get Bypass Config
{%s} Failed to get breakpoint mask for %s: %s
Breakpoint Index: %d
[1500] Error parsing bridge: %s
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
[REM_WP] wp%d\n
replayPreflight
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
Unable to read PC
replay_counter=%lu
Initialized Logging - %s
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
{%s} NOMEM
Complex CPM Offset: 0x%llX\n
Cannot create DART descriptions from NULL info\n
Could Not Create Dictionary From Booster: %s
Value Types Are Not Strings\n
## ARM32cpu_t::read_register %u\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s} [%s] MMU is already active - returning %s
Probe %s removed before port determined\n
{%s} invalid data width %d bytes
Invalid value for 'entry' tuple element - can't index
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
 MEM-AP %X is hung\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Hang Address: 0x%016llx\n
Set custom PSD json file: %s
{%s[select]} timeout while waiting for data from the connection
In Eraseflash\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
%s: not supported.\n
{%s} _pre_resume_hw result = %s
Warning: chip exploration did not complete successfully (%s)\n
Astris Version Set: %s
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
{%s@%d} Received %d bytes when requested %d bytes [%s].
{%s} Thread %#llx clearing key %lu
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
   {%s} Before powerup CMDSTAT=%08X\n
[Auth Debug] External Debug Interfaces Open\n
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
gmtime() returned NULL, using epoch time
%s
Error returned from explore_pid
{%s->%s}
Async is disabled for current seesion
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
[1500] No %s.plist resource found
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
{%s} Unrecognized component: %08X, class %02X\n
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
We are in clean up\n
Could Not Find Any Boosters\n
[1500] Error parsing v2 bridges
error %s checking for data abort(first)
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
Failed to convert primateLoc %s to unsigned long long
Astris Source Version: %s\n
Gateway is KIS, seeing what probe this is\n
{%s=>%s} null reference to AXchip_t[0]
Error status from AMAuthInstallSsoInitializePtr = %i
Sending DYN Bypas Channel Set: %d
Result while reading second entry: %s , entry val 1: 0x%X\n
Result while reading first entry: %s , entry val 0: 0x%X\n
We are at max iterations, still didnt get full JSON
DBG_CPU: %s\n
Error %d(%s) executing instruction 0x%08X FAST
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
[AstrisAsync] Deactivating async...\n
max_scan_bits is low: %d
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Using 10pin connector skipping orientation check
{%s::%s} [%s] error %s writing SCTLR_ELx
[AstrisAsync] Pause when already paused!\n
AP given is not a MEMAP
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
Selecting polling method %s
Unable to allocate memory for next part of big response
Kick has been requested by probe server
{%s} %s: |%s|
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
{%s} _halt_hw result = %s
\tAligned Read Failed
Exploring IDE in JTAG\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
connection created
Initialized %d 1500 bridges\n
EICE chip %x initialized\n
{%s} Component ID read fail on romtable (%s)
Xtensa Option non_tie_ranges: %zu range(s)
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
JsonLogger: Wrote %zu bytes to '%s'
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
   --> IDR: %08X\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
{%s=>%s} AXconn_t has more than one chip
Could Not Find a DCM Portal
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
Probe Map Server Information: %s
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Initializing (%s) Booster's Astris API\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
DBGCTRL = %08X   res=%d\n
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
The log file has been updated with all available diagnostics.\n
unable to identify chip
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
Explore: %u chip%s\n
Could Not Get BoosterManager\n
--> psr        size=%3d bit=%d
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
[WRITE] %d -> %08X\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
[Auth Debug] Ticket Active, Debug Interface Locked\n
Can't get hardware model - failed to create string
=== Found %s Boosters ===\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
[1500] %s step %d missing required field 'instr'
   Debug Port has unknown type\n
Extract Offset: 0x%X for %d\n
batch_cmd_count: %d
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
      AXap_write of R_JTAGAP_PSTA failed with error %s
Can't get OS build version - failed to create ReadStream
Could not find bundle () in given array: %s\n
Failed to find a product plist for this soc %s
{%s->%s} START handling exception
{%s::%s} [%s] error %s from _synchronize_context.
Can't get hardware model - failed to convert to C string
Error %d (%s) while expanding ~ for Astris history save\n
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[%s] AP, DP, or chip given is NULL
Xtensa Option num_bp: %d
unable to create connection
{%s} drain_packets=%d [%s]
Got an error writing 0x%X the DCM Control Register: %s
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
No 1500 bridges or TAPs specified (v2 plist)\n
## armcpu: bad status even though all bytes written (%d)\n
   CPUID: 0x%08X\n
Probe Map name of probe %d is: %s
Connecting to server, %s:%d
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
!!!! Complex Key %s is INVALID !!!!\n
{%s} %s DC cache clean complete, marking as clean
{%s::%s} [%s] length=%u when width=%d
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
read failed, using old cached as base: 0x%x
\t%s\n
Failed to convert %s key @ index %d
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s} collect result = %s
Increasing length by: %d\n
{%s} drop ProbeName %s
{%s} probe device server closed the connection while trying to read data (at recv)
Multi target booster, checking for %s.plist\n
Section 1 Offset: 0x%llX\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
## memapr %u 0x%016llX %d -> 0x%08X ...\n
Probe Map comm: request[%s], response[%s]
DCCCTRL = %08X   res=%d\n
[AstrisAsync] Deactivate while async is not active!\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
   {%s} select %u port %u: %u chip%s\n
DHCSR write failure - %s (%d)
   JTAG-AP: Identification = %08X\n
%s probe[%s] from Probe Map Server [%s]
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
## memapw %u 0x%016llX 0x%08X\n
Switch back to primate KIS: %s\n
{%s}#%02X cmd: %s, resp: %s
AXjtag_srst assert failure - %s (%d)
{%s::%s} [%s] error (%s) getting number of HW BPs
   Debug Port: SELECT %X: SKIPPING (%s)\n
Result while reading third entry: %s , entry val 2: 0x%X\n
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
[%s] Booster System Is Not Initialized\n
{%s} bridge returned DECERR
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
sending abort to clear a timeout\n
Generated JSON (first 500 chars):\n%.500s%s
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
Original Content: 0x%08x
Can't get hardware model - failed to get property
Choose a device: 
1500 IR Commands:
[KIS] Register Read/Write/Wrote: %d\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
No version information found in booster: %s
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
could not perform cpu_preflight
{%s} setting up nameless target (address=0x%llx)
Proceeding with full explore instead of instantiation
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Going to do imago workaround\n
The debug port associated with this chip has not been explored.
Initializing Booster Layer\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
Failed to allocate space for table!
astris_get_async_ver failed with error: %s
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
{%s} connectName[%s]
[KIS] Register Index: %llu\n
CPU DBG Ack: 0x%llx\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
Unable to disassemble_at_addr 0x%016llx
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
Found %d APs
tckrate_check returned error %s
Xtensa Option ocd_address: 0x%llx
!!!! Complex CPU Key %s is INVALID !!!!\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
## dpr 0x%02X failed (%s)\n
Hang Radar Info:\n%s\n
%s given a NULL conn object
{%s} error %s at line %d
CPU Subsystem: %s\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s::%s} ERROR %d(%s) resuming %s\n
Error happened when reading edscr. Retry #%i\n
In Writeflash\n
CPU %s already in the map with status: %d
INFO: %s(%04u): %s(): err=%s(%d): %s\n
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
[%s] Booster System Is Not Initialized Bailing\n
{%s} no matching 1500-to-* bridge
caller=%s, async=%d
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
We are Allocating\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
     0x%016llx: 0x%08x    %s\n
   Setting up AP IDR %08X\n
X12 Part
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
Koko probe, for now I guess we will just say yes...\n
Early dbgwrap base extracted: 0x%llx\n
[AstrisAsync] Async mode %s
{%s=>%s} null reference to AXcpu_t record, `cpu`
Failed to init from cpu desc armv7m cpu: %s \n
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
Could Not Find Booster Entry Function: %s\n
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
1: ARM64_SYSOP_ATS12E1R\n
2: ARM64_SYSOP_ATS12E1R\n
Probe %s with unknown kick response %s
Enabling USB Gateway
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
{%s@%d} Connection to server failed, error=%d (%s)
TAP IDCODE: 0x%X\n
Can't find descriptor for group - can't index\n
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
{%s} Failed to extract ECID from table (%d); continuing anyway
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
{%s} bridge timed out
Adding new booster path: %s\n
{%s} Failed to extract portal info from table (%d); continuing anyway
error trying to unlock MSR %s
{%s} Failed to get watchpoint mask for %s: %s
\tReading left over chunk expected 0x%x got 0x%x\n
Connect using RSD not supported\n
Connection to server accepted
{%s::%s} NULL parameter
[%s]\n
Disconnected from Probe Map Server
{%s} unaligned %d-byte access at address 0x%09llx
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s} _resume_hw result = %s
Failed AP write of R_MEMAP_CSW res: %i newval %i
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
connection about to be destroyed
Connected toProbe Map Server (single_port) 
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
CPU has no regions, maybe powered off?\n
   Debug Port: SELECT %X; error: %s, retrying..\n
{%s} DEVARCH read fail in CoreSight component (%s)
{%s} wrote %d words to probe when %d words provided in request
Could not enable KIS SoC Access\n
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
error %s reading DAP MMFR0
{%s=>%s} null reference to CPU_t object, `cpu->state`
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Failed AP read of R_MEMAP_CSW res: %i
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
SSO is DISABLED\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
{%s::%s} EDSCR with RXO set - unable to recover.\n
   {%s} (DP): status=0x%X(%s) - %s\n
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
\t[MATCH_FOUND] identified chip: %s
Done.\n
register    %-15s %3u     \"%-s\"\n
{%s@%d} IOServiceClose failed, err = 0x%08x
\t[MATCH_SKIP] skipping entry
Could Not Allocate Info Keys Array
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
Unable to read FP
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
probing %s status\n
HOSTID=0x%x which is invalid, skipping orientation check
%s [RETRYING]
sent %zd bytes to Probe Map Server when sending %zu
--> wrstn_wir2 size=%3d dpcsoc=%d
Cannot create complex descriptions from NULL info\n
[1500] TAP %d: irlen must be > 0 (got %d)
{%s::%s} read OK but took %d tries
   Debug base is in legacy format\n
\t[MATCH_TARGETID] FAIL <= unable to find DP
{%s::%s} creating CPU
Protocol Version: 0x%X\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
[AstrisAsync] Resume when not paused!\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
Wrong width, should be either 4 or 8\n
Switch to primate res: %s\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Successfully Authenticated DFT\n
Probe %s status: Busy
{%s@%d} Failed to send probe command (error %d).
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
We are done with clean up\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
      Read of JTAG-AP port %u PSTA failed with %s\n
{%s} unable to find single_port probedaemon on port %d
[DCC] Grabbing DTR failed: %s\n\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
[AstrisAsync] Failed to restart Async batch\n
Optional Key: SubsystemMonitor not in preferences
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
failed read from DEMCR - %s
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
Trying to use size of 8 on not AXI bus
{%s} FAILURE - NULL parameter
Failed to convert primateHubLoc %s to unsigned long long
end rev is not of expected format; skipping cpu_desc override\n
[1500] Error parsing TAP description
error %s checking for data abort(uint32_t)
Translate Stage Chosen: %d\n
SSO info present but SSO disabled.
relay_set: %s -> %d
Setting STOP CLOCK to TRUE
Portal Group Offset: 0x%X Entries: %d\n
   Debug Port: SELECT %X: AVOIDED\n
   Created Fake Debug Port Debug Port
AuthDebugWithTimer_t destructor \n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Creating CPU With Name: %s\n
JsonLogger: Creating new category '%.*s'
KIS Writevals putting back the value
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
[CACHEOP] %d, 0x%016llx, %d\n
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
{%s} no TAP detected that supports 1500
Before astris_kis_init_dp, CMDSTAT=%08X\n
=== Detailed %s Boosters ===\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
{%s} error %d(%s) reading data from the connection (at recv)
{%s::%s} [%s] unsupported width %d
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
Can't get OS build version - failed to create URL
response == NONE; failed to get kis target info\n
Unable to read GPR 28
first read of CMDSTAT may fail if external reset occurred
AuthDebug::authenticate_probe - no need to authenticate\n
Probe %s with unknown status %s dropped from available list
=== Loaded %s Boosters ===\n
CPU AP-Type: %d\n
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s} %s status is '%s' [Status Read %d times]\n
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
{%s=>%s} AXconn_t has no SoC object
{%s:%s@%d} Critical error encountered:
Probe %s status: Idle
AXjtag_explore failure - %s (%d)
UPDATE cop64 %d -> 0x%016llx\n
{%s::%s} write OK but took %d tries
{%s} handle ROM entry %d (level %u): %08x
{%s} match any probe [localhost]
{%s@%d} Unable to connect to server, %s:%d
{%s@%d} Probe response payload read when no payload indicated.
Failed to instantiate %s\n
   {%s} Probe requires overrun detect mode.\n
      Explore of JTAG-AP port %u failed with %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
Failed to convert CFString to C String.
Gathered:\n
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Unable to register assert upcall %s (Insufficient memory)
kext connect name %s\n
{%s@%d} gethostbyname failed, error=%d (%s)
[ANAMOLY] Could not find AXcpu_t object for CPU\n
Turning Debug Clock On
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Dart Coastguarded CPU: %s\n
    %s(): %s
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s} 0 words requested for read at address 0x%016llX
{%s} unsupported bridge type for %s
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
Failed To Initialize Logging\n
Matched Booster: %s\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
[REM_HWBP] bp%d\n
{%s} Failed to get breakpoint count for %s: %s
## apw %u 0x%08X 0x%08X\n
About to call fault reg latch, min_operating_el: %d\n
## dpw 0x%02X 0x%08X\n
Component Group Offset: 0x%X\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
VBAR: %#llx\n
[%s] {%s->%s} clear async abort
ERROR: nothing to do; resuming address translation for %s without previously suspending it
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
{%s} strsep empty so match any probe [localhost]
ERR: conn->nchips != 0; looks like chip is explored\n
Probe Type (%d) FW Version: %s does not support KIS.
error %s reading DAP PFR1
Found an async abort pending; clearing it\n
runBlock
{%s} ROMTABLE (dbgbase=0x%llx)
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
Had an error during transfer: %s
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
{%s} DAP command nwords=%d trimmed to %lu\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
Xtensa Option num_high_pri_intr: %d
{%s} select success without file descriptor set
Full JSON that failed validation:\n%s
Could Not Get Bundle Out Array of Found Boosters\n
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
[1500] v2 plist missing required field 'bridges'
[1500] TAP %d missing required field 'ir-cmds'
{astris_probed_print_events_from_json} not supported in this build configuration
Table Size: %d\n
Target ID: 0x%X\n
Magic does not match: %#x vs %#x\n
Cannot create CPU descriptions from NULL info\n
[1500] Detected plist version %d
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Can't get OS build version - failed to allocate buffer
Dumping Process Tree
Gathered Value is Not Number\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
CPU with %s Not Created via Name
DEMCR read failure - %s (%d)
{%s::%s} halting %s\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s} found single_port probedaemon on port %d
After powerup CMDSTAT=%08X\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
     ARM %s watchpoints: %u\n
[AstrisAsync] Activate while async is already active!\n
no debug bus AP present when expected; after sysap is NULL
CPU Name: %s\n
using standard products.plist for %s
Portal Group Base: 0x%llX \n
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s@%d [%s]} Error %s: synchronizing context
Unable to read GPR %d
{%s} explore with exploreflags 0x%X completed with error [%s]
Invalid character [0x%02X] received from Probe Map Server
User created bundle found, ignoring version checking via plist
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[REMBP] bp%d\n
collect_responses
## dpw 0x%02X failed (%s)\n
{%s} Unrecognized Component: %08X (class %u)
CPU Monitor[%i]: %s\n
{%s} restored el is now %d
\tTatsu AuthDebug Triage | All\n
received %zd bytes from Probe Map Server when have %zu
Unable to allocate memory for big response
cleanup
astris_ide_get_pid
{%s:%s@%d} [%s] FEEPROL write failed: %s\n
Register file 7
fn._ocd_exec_instr.wsr.WindowBase.r0_r12
fn._ocd_exec_instr.wsr.reg_srn.t1
!!!!!!!!!!   $ sudo chmod 0775 %s\n
astris_clear_user_die_select
_is_halted
FEEADR0H
Requires OCD option for >1 data breakpoint regs.
\tAligned Read Failed
{%s} NOMEM
error %s reading DAP MMFR0
check.el.after.exception_hanlder
W
Error Reading Device Production-Fusing\n
<unnamed>
fn._collect_snr.excvaddr
ASTRIS_ERR_PENDING
DLOPEN ERROR: %s \n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
fn._read_special_reg.icountlevel
%s v%s%s [%s]
PERSEIS
v8@?0
Failed calling AppleSOC_t::dock_disconnect_mode\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
Level-1 exception save location
xfer_acmd_via_kext
createSOC
{%s:%s@%d} [%s] reading ADFSR\n
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT && != SP\n
{%s::%s} read OK but took %d tries
%016llx
param.length.invalid.null
ASTRIS_ERR_WAIT
Probe %s USB-C location is %s
setTargetOS
BoosterManager.Utility
address =0x%X is too large for 32 bit unsigned.
fn._ocd_reg_dsr_clear_and_validate
\n
AXcpu_hwwp_insert
Low level
plist
{%s} Thread %#llx clearing key %lu
Async is disabled for localhost connection
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
{%s} valid response from bridge
{%s:%s@%d} [%s] writing BVR %d\n
param.regval.null
reg_name not specified.
AX1500_transact
AXcpu_readreg
AP[%d]: MEM_AP_AHB\n
addMember
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
PARTNO_SWDP_M33
Misc register 1
AXconn_showname
{%s} match any probe [localhost]
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
HardwareBreak
RF27
%s (%d)
ASTRIS_ERR_TIMEOUT
{%s:%s@%d} [%s] AIRCR write failed: %s\n
products_
MAC16 data register 2
ObjectEmpty
ret.restoring_el_after_raising_to_read_hcr
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
AXcpu_status
VECBASE
sending request
GetCachedPowerByIndex
{%s:%s@%d} [%s] executing MSR\n
dest_reg < 15
Bug detected
Hang Radar Info:\n%s\n
Probe %s selected
ret.chip == NULL
: [
Long Packet
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
file_type
setProbeInfo
PRORES
result.read.memap.s2r_fsm
_a64cpu_read_gpr_cached
base_reg < 15
fn._ocd_exec_instr.rsr.2
remote probe is currently in use
astris_command_complete_cache
CPU3
RXO
setway_reg
astris_init_dp
buf != 0
target power is OFF
Unable to process command while connecting to
!level_stack_.template Top<Level>()->inArray
PAM
resolve_portals
FAR_EL2
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
m_bp_details
internal.is_probe_authenticated.chip->soc == NULL
RF13
[%s] Booster System Is Not Initialized Bailing\n
MMX
ret.pka.verify.status.err
Kick failed: probe no longer hosted by probe server
read_resp_payload_via_sock
Using Built In SoCs\n
tokens_ == 0
{%s:%s@%d} [%s] getting GPR (diff mode)\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
M4
.chip_id
Debug-Components
_a64cpu_write_gpr_hw
bpcr
astris_setup_jtagap_target
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
ASTRIS_ERR_OUTOFMEMORY
pnav_drop_probe
RESPONSE_PAYLOAD_DONE
_get_num_hwbp_hw
JSON string output is null
A
DESIGNER_ARM
ret.clear_probe_authentication
_ocd_exec_instr
Status
Exo
alloc_drain_payload
cpu_cache_info_group0
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
{%s:%s@%d} [%s] setting DTR MODE to STALL\n
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
is.Peek() == '['
wir-wirshiften
result.read.dbgwrap_base==
AP[%d]: unknown type\n
Explore: %u chip%s\n
/\\
DCS_BC1
!!!! Critical Error: exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
param.ocd_base_address.invalid.unaligned
No Success after retry on wait
DISPSEC
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
   Debug Port: SELECT %X; error: %s, retrying..\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
DCRCLR
fn._init_configuration_by_name.failed
fn._read_special_reg.ibreaka1
cpu_getmode
AFT
astris_command_lock
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
internal.is_authenticated.debut_auth == NULL
Misc register 0
/System/Library/CoreServices/SystemVersion.plist
astris_json_logger_get
astris_json_logger_to_json_string
ret.cfg_read(R_DCM_GPIO)
localwrstn-debug
Found the RTXCID Structure!\n
AXcpu_lacc_count_read
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
AXconn_connect_kext
CortexM23
Lost
AXdebug_auth_get_timer_count
cpu_lacc_count_read
')
{%s:%s@%d} !(prsr[0x%08X] & DLK)\n
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
{%s:%s@%d} [%s] FEESTA read failed: %s\n
Invalid parameter exec_path = %d
Kick has been requested by probe server
param.chip.soc == NULL
{%s:%s@%d} [%s] doing JTAG scan (DIDR)\n
ret.read.rtxcid
_suspend_translation_hw
   {%s} select %u port %u: %u chip%s\n
get_ecid
from
ret.switch_taps
Accept
fn._read_general_reg.regval
kis_target_info %s
Could Not Get BoosterManager\n
X12 Part
{%s:%s@%d} [%s] config_write_enable failed: %s\n
message
u64toa
NRF
DCS_BC5
ret.getCpuEnableStatus
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
astris_jtag_scan_stay_gotorti_impl
Optional Key: SubsystemMonitor not in preferences
Error
query_events
ret.alloc.soc_key == NULL
fn._ocd_exec_instr.wsr
{%s} connectName[local host]
Unable to connect to probe server
panic
addMember.user
engineer
EDRCR
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
cpu_translate_with_stage
{%s} bridge returned an error
{%s} %sing word #%d at address 0x%09llx: %s
Protocol Version: 0x%X\n
astris_ide_get_dbgwrap_base
[DCC] Grabbing DTR failed: %s\n\n
Failed to read reg_addr=0x%llx
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
write_memblock_dbgwrap
armv7m-region-name
SP_EL0
AXLOG
%s %s
no error
bad parameter(s) specified
required parameter is missing
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
ret.clear_edscr_err
Instruction break enable bits
unable to identify chip
{\"max_events\":%u,\"events\":[%s]}
result.read_vals(table_info)==
fn._ocd_reg_r.dsr.regval_raw
{%s} %s did not match any valid host
CortexM7
NotNullStrLen
ret.reg.write.K_DA_REG_NAME_AUTH_VALID_CLEAR
OCD control register, clear
RF7
CPU1
clzll.h
False
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s:%s@%d} [%s] writing DTRRX\n
~MA
[AstrisAsync] Discarding %zu completed command(s)\n
{%s} ROMTABLE (dbgbase=0x%llx)
enter_user_key
Table 5–170
[%s] %d -> 0x%08x\n
_a64cpu_read_aarch64_sp_hw
{%s} explore with exploreflags 0x%X completed with error [%s]
Generic
Kick required to connect: Busy probe
ret.handle_exception.read_sysreg_hw.esr_el
Error %d (%s) opening cmd snapshost save file
Stringify
index < 87
check_and_clear_cpu_msr_lock
TGTOFF
IDE
AP given is not a MEMAP
   JTAG-AP: Identification = %08X\n
{%s} read %d words from probe when %d words requested
/var/log/astrisclient
wa
Error %d (%s) opening history save file
????
Could Not Find Any Loaded Boosters of Type: %s\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
va
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
AuthDbg,TicketIdentifier
ret.reg.write.K_PKA_REG_NAME_DBG_STATUS
param.reg.invalid.outofrange
param.len.invalid.>64
ISP_L
symbol.check.loaded.AMAuthInstallRequestSendSyncPtr == NULL
cpu did not stop. OCD.DSR=0x%8.8X
PlayerSWD
Probe
Failed to write DCM GPIO (0x%x): 0x%x
{%s} Class 9 ROMTABLE (nest=%d)\n
Found another target for the plist\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_dapcmds.cpp
class_var.m_interface_name==NULL
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
CPU.ARM
unable to read memory (permission checks suspended)
EPC7
fn._read_mem
_init_configuration
Can't get OS build version - failed to create URL
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
{%s:%s@%d} [%s] moving reg to cop\n
Data break 1 control
RF1
halted=%d
ASTRIS_ERR_VARNOTFOUND
DCS_BC6
Component Group Offset: 0x%X\n
esr_el2
ret.reg.read.K_DA_REG_NAME_SECURE_DOMAIN
param.reg_name.INVALID
par
AXbooster_get_loaded_boosters
mempool-base
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
ICOUNTLEVEL
host %s
IDLE
_a64cpu_lower_el_hw_safe
      Read of JTAG-AP port %u CSW failed with %s\n
authenticate
Register file 58
Communication error occurred while connecting to
AXconn or json_out are NULL
Unable to connect after multiple attempts:\n%s,\n%s
Probe Map comm: request[%s], response[%s]
DEDICATED
fn._write_special_reg.ibreakenable
address=0x%8.8X, regval=0x%8.8X
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/logging/astris_except_classes.cpp
astris_user_default_remove_all_nicknames
DP
erase_all
%2d) %s %s [Busy]%s\n
Initializing (%s) Booster's Astris API\n
{%s:%s@%d} [%s] Read DWT Comp %u\n
_init_registers
{%s} no matching 1500-to-* bridge
AMCNP_GFX
(reg & (0x40000000 | 0x80000000)) != 0
host is going to sleep
connected-listing
GetSize() >= sizeof(T)
{%s::%s} EDSCR with TXU set - unable to recover.\n
{%s->%s} START handling exception
Enabled
R15
RF54
DCS_BC3
internal.enable-test.chip == NULL
Cycle count
DBGCTRL = %08X   res=%d\n
ret.reg.write.K_DA_REG_NAME_CHIPID
AMAuthInstallSupportDictionarySetInteger64
status=%u, flags=%u, DSR=0x%8.8X, DCR=0x%8.8X
acc
Debug Base: 0x%llX\n
astris_ide_get_revision
_init_params
wpcr
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
resolve_debug_components
KIS translator version : %d\n
{%s}#%02X %s [%s]
CopyFrom
haskis
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
astris_setup_memap_target
EXPLORE_ONE_DIE
Register file 12
Warning: Default logging location requested when running as root (using [%s])\n
Portal Status, Changing STATUS and CMD/STAT to reflect
{%s} Error setting up jtag-ap target (%s)
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
Register file 52
invalid parameter
memap_bus_read
astris_json_logger_delete_category
{%s} m_exception_level(%d) != current_el(%d)
{%s} DAP command nwords=%d trimmed to %lu\n
AXchip_find_dap
COMPARE1
probe matching %s on host %s
NOP
cpu_hwwp_info
{%s:%s@%d} [%s] timed out waiting for reg_index %d to equal: ((0x%08X & 0x%08X) == 0x%08X)\n
_a64cpu_el_fault_reg_latch
param.tgt->ap->dp->chip.null
{%s} Component ID read fail on romtable (%s)
PORTAL ERR PENDING
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
AXJTAG_EXPLORE_SEP_NOPWRGATE
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
{%} exec: encode_hint(NOP)\n
M3
ret.pka.verify.timed_out
ATOMCTL
High level 3 exception PS
PORTAL_STS_MULTIPLE_BITS_SET
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Number too big to be stored in double.
AXcpu_translate_par
fn._ocd_reg_w.ddr.1
ASTRIS_ERR_IFSTATE
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Section 1 Offset: 0x%llX\n
consumedAcmds
read memory
m_loaded_framework == NULL
MiscCortex_t
virtual int ARMv7cpu_t::_resume_hw(bool)
config.invalid.no_window_reg_option
AXbooster_print_all_booster_managers
connected
ret._a64cpu_write_sysreg_hw
AXconn_copy_nickname
Discon
AP[%d]: JTAG_AP (Exploring Later) \n
{%s} FAILURE - max length exceeded
Banana split probe, for now I guess we will just say yes...\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
astris_remove_loaded_soc_boosters
ret.enableCpu
{%s:%s@%d} [%s] reading DFAR\n
init_hw.pid0
is_external_open
Table 5–175
Invalid value.
write_register
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
Done.\n
Mask condition met in conditional operation
LOSTCONN
cpu
Port
%#09llx-%#09llx: %s\n
gpr < 15
Register file 36
_write_general_reg
UNKNOWN_CODE
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
@rpath/%s.framework/%s
OUTEN_RESTART
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
fn._ocd_exec_instr.wsr.ddr.t1.2
AXbreadcrumbs_read
Booster:\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
ERROR: unable to resume translation for %s
{%s:%s@%d} [%s] failed to read CMD/STAT\n
{%s} Unrecognized Component: %08X (class %u)
astris_memap_bus_read
param.buffer.invalid.null
Can't get OS build version - failed to get build version
val < 4294967295U
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
ASTRIS_ERR_ANOMALY
ASTRIS_ERR_FDSETOVERFLOW
dart-name
ARM7
IsObject()
mxwrap-address
AXcpu_translate_with_dart
fn._setup_data_bp.wp_state
buffer != 0
Dart CPU SID(s): %s\n
!!!! Critical Error: Nested exceptions... get someone to debug this. !!!!\n
MR0
Turning Debug Clock On
config_write_enable
Register file 59
{%s} connectName[%s]
--> extrawrstn %d
\t\tARMv6 debug CPU xxx ID\n
AXcpu_status_asc
connection about to be destroyed
Awaiting next chunk of big response
{%s@%d} gethostbyname failed, error=%d (%s)
BoosterPublicAPI
Astris Source Version: %s\n
--> 0x%02x = %s
result.read_vals(group_info)==
MASK ERROR
AuthDbg,BoardID
{%s} timed out waiting for cpu to halt during collect
X09 Part
[Auth Debug] Disabled\n
{%s:%s@%d} [%s] executing MCRR\n
ret._a64cpu_el_fault_reg_latch
{%s} already collected %s, skipping
Ring ASID values
Schema file is empty
name <= nameBuffer_ + length
!Base::level_stack_.template Top<typename Base::Level>()->inArray
[1500] Detected plist version %d
CRYPTO
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
failed read from DEMCR - %s
Vector Base
End
=== Ending Gather and Clear ===
ban
fn._ocd_reg_w.ddr.t1_save
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
cpu_read_dcc
ide_checker_diagnostic
ret.enableSubsystem
Failed to exec MRS to bounce sysreg into scratch register. scratch=%d, sysreg=0x%X, regname=%s
ERROR: unable to suspend translation for %s
RF43
lldb
HIDBridgeSWD
!hasRoot_
_a64cpu_encode_ldrstr_postinc
Memory error check register
param.address.invalid.>max
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s} Failed to extract CID from table (%d); continuing anyway
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
vaddr
[AstrisAsync] replay preflight: Async not active!\n
New
first read of CMDSTAT may fail if external reset occurred
jtag_get_soc
internal.enable-test.chip->soc == NULL
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
EICE
Table 5–133
AXI-ERROR=0x%X - AXI-XACTION-FLAG=0x%X - ADDRESS=0x%llX
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
PongoSWD
Product Name: 
vers_gateway < 2
Table 5–153
Not Enough Payload For Specified Bits To Shift In OR Write Data Length Mismatch
var.m_debug_interrupt_level.invalid.outofrange
probe refused to process the command
%s:
High level 2 exception PC
Table 5–147
ret.home_url == NULL
PROBED_ERROR
{%s} probe_port = %d
Unable to connect (single_port) to probe server
Malloc
[%s] {%s->%s} END handling exception
Invalid num_regs = %u. Should be 16, 32, or 64.
_reg_desc_lookup_by_name
Astris
host_to_components
EndObject
ViewSWD
Failed to init booster
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Passed NULL booster without custom plist\n
cpu-group
sdom
Target ID: 0x%X\n
astris_batch_attitude_relax
astris_cpu_status
{%s=>%s} AXconn_t has no SoC object
ret.init_params.raise_to_min
virtual int CPU_t::collect(int)
astris_create_ap_slave
unpack_response
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
CTI_CTL
[%s] error reading EDSCR
clear_authentication
fn._ocd_reg_w.ddr.value
Portal Status has an error
{%s->%s} current EL (%d) already >= target EL (%d).\n
Die Addr Info LSB: %d Mask: 0x%016llX\n
[1500] run_steps: unknown instruction '%s'
ret.wait_ite_set
ret.state_valid_entry_exit
AXcpu_mmu_get_tsz
Exploring IDE in JTAG\n
data_reg=%u,opcode=0x%6.6X
Register file 32
dfu-Type: %s\n
DBG_CPU: %s\n
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
ret.raise_el.write
!!!! Critical Error: {%s->%s} EL3 not implemented !!!!\n
astris_memap_debug_writebuf
Table 5–168
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
Successfully Authenticated DFT\n
param.op.invalid
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
TAP-Only
cpu_hwwp_disable
APF
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_explore.cpp
     ARM %s watchpoints: %u\n
NoSOC
write.reg.not cached
CLIDR
astris_explore_romtable
   {%s} Enabling debug unit\n
vvvvvvvvvvvvvvvvvvvv DUMP OF HISTORY LOG vvvvvvvvvvvvvvvvvvvv
ignore_dapcmd_error
SRST
str != 0 || len == 0u
astris_ide_is_component_present_at_addr
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
collect-probemap
Failed to get KIS translator version\n
write.dspsr_el0 NOT CACHED
SCTLR__ELx
op_RFDD_encode
uri.h
Logging Context Is NULL\n
process_bypass_device
DCS14
AUSB_REGS
i8@?0
internal.is_authenticated.chip->soc == NULL
:usb
INIT
{%s} unsupported bridge type for %s
{%s:%s@%d} [%s] FEEADR1L write failed: %s\n
%s given a NULL conn object
Kicking
regex_.IsValid()
Map is empty, not removing CPU %s
AXdebug_auth_enable_timer_ovr
DISCONNECT
description
{%s:%s@%d} [%s] reading PRSR (!oslk)\n
     0x%016llx: 0x%08x    %s\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
Xtensa Option num_high_pri_intr: %d
%02X 
fn.entry
get
CPU[%s] Read Reg: %d
ret.get.da
Preferences does not exists: %s, creating one.\n
#ch-
RF40
fn._ocd_exec_instr.TIEWriteProtectedI
ConsistDbg
ARMDAP
Result while reading first entry: %s , entry val 0: 0x%X\n
ASTRIS_ERR_DISASM
SPIXACT
Initialized %d 1500 bridges\n
RF37
_ocd_reg_r
astris_write_halt_all_crumb
is.Peek() == 'f'
{%s:%s@%d} [%s] writing OSLAR (oslk)\n
{%s:%s@%d} [%s] reading BCR %d\n
Failed to explore chip: %d
Data TLB configuration
Spew change. old=0x%016llX, new=0x%016X
could not get runtime env
GetUri
get_soc_resource_filepath
AXexplore_enable_cpu_pattern
ret.fromreset
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
!Base::hasRoot_
_pre_resume_hw
!!!! Critical Error:  dspsr_el0 NOT DIRTY !!!!\n
Table 5–188
Could not find portal by select %d, while interpreting result\n
FACTSERNO
wrstn-pipes
address-size
_status_hw
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_armdap.cpp
 (%s)
SoC BM Not Found, Bailing\n
1.0
spsr_el2
OK
init.m_symbol_table == NULL
Probe (port=%d) with unknown status %s dropped from available list
DCS12
PARTNO_ARM7TDMI
%s.console
No portal under found for that type
{%s@%d} socket connection is not available
AMCNP
dest_reg < 32 || dest_reg == 31
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
{%s:%s@%d} [%s] FEEKEY write failed: %s\n
RF11
end
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
RF52
reg_name (\"%s\") not present.
op_ISYNC_encode
ASTRIS_ERR_NOTEXPLORED
probe matching %s on localhost
nullptr == soc_bm
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
[%s] Executing instruction=%llx
_clean_invalidate_l2cache_setway
AXdebug_auth_clear_auth
read_settings
{%s:%s@%d} [%s] erase_page failed @ 0x%08llX: %s\n
RESPONSE_PAYLOAD
param.booster_handle==NULL
baseReg
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
var._tgt.invalid.null
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ASTRIS_ERR_PROBEERROR
JsonLogger: Writing category '%.*s' to '%s'
AuthBase_t::load_framework failed
Probe %s LocationID Info is %s
/socs
cpu-xtensa-ocd-base
DFR0_LO
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
Xtensa Option num_bp: %d
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
UNDEFINED
result.read.portal.s2r_fsm
Accumulator low bits
SSO with no prompt being used
{%s:%s@%d} [%s] FEECON write failed: %s\n
parameter val is NULL
ASTRIS_ERR_PROBEEOF
Astris-%d.%d~%d
{%s:%s@%d} [%s] checking DCC\n
%s NOT configured\n
M2
XSTAT
Category is null
Missing a comma or ']' after an array element.
Found match - bypass_device: %s; channel: %d\n
AMAuthInstallSsoEnable
Register file 45
op_ROTW_encode
kis_stm_name %s %d
localhost
** Unauthorized User/Network or ECID **\n
ret.reg.read.K_DA_REG_NAME_SECURE_MODE
ret.reg.write.K_DA_REG_NAME_NONCE_1
Memory error status register
cpu-ascdebug-offset
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
unswitch_regset
{%s:%s@%d} [%s] getting GPR 0 (CPSR)\n
EDBVR0+index
   Debug Base: %08X\n
operator[]
{%s::%s} ERROR %d(%s) pre_resuming %s\n
ret.exec.drps
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
      Explore of JTAG-AP port %u failed with %s\n
is_ecid_zero
[PREFS] Key: %s - Val: NULL
param.reg_name.invalid.unimplemented
default
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
IBREAKENABLE
MEPC
Memory error virtual addr register
Another application is connected to
probe on localhost
Probe %s removed prior to kick\n
wir-tdo
explore_min
AXcpu_lacc_status_remove
FEEPROL 
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
result.ide==NULL
{%s:%s@%d} [%s] reading CPSR(1)\n
     ARM %s breakpoints: %u\n
param.conn.user_defaults == NULL
[PREFS] Key: %s - Val: ??
Could Not Allocate Memory
cpu_status
astris_kis_get_bypass_info
AXbooster_get_all_boostermanagers
wir-wrstn
low word
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
Unaligned Read @ 0x%llx Width: %d Bytes: %d
{%s} Debug Base: %08X
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Table 5–184
fn._ocd_reg_r.DSR
PROBED_USB_RSP_NODEVICE
hid
[%s] {%s->%s} Transitioning to exception level %u.\n
Unable to disassemble_at_addr 0x%016llx
{%s} _halt_hw result = %s
AXcpu_mmu_walk_detailed
ASTRIS_ERR_PORTAL_STATUS
PROBED
cpu_readreg_vals
_create_cpus
cpu-armv7m-base-offset
[1500] v2 plist missing required field 'taps'
astris_ide_get_cps_fsm
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
{%s::%s} [%s] error %s writing SCTLR_ELx
Tarsier
dcm
We are done with clean up\n
lower.safe.aarch32=notsupported
nothing written
(%s) %s
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
!!!! Critical Error: GRPS[1] cached !!!!\n
Waiting for previous in-flight authentication to finish\n
Sprocket
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
[1500] TAP %d missing required field 'ir-cmds'
Efficient-Core
CTI_OUT_EN1
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
AuthDbg,Ticket
cpu_mmu_walk
%s: chip was NULL when attempting to release soc
astris_get_die_count
TXU
AXcpu_collect
relay_set: %s -> %d
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
Production Fused Device\n
Table 5–164
ASTRIS_ERR_TOOMANY
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Failed to instantiate %s\n
CPU disabled by SW, not accessable
m_core_api_serial_queue
Register file 25
Toto
{%s} bridge returned SLVERR
DLR_EL0
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, &d, %d, false, %d)\n
[RESUME] Chip %x\n
SSTEP
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Register file 19
ocd_base_address = 0x%8.8X is not 4 KByte aligned
select_v2
astris_exc_bread_test_2
Raising to EL2 cause in Guest\n
{%s:%s@%d} [%s] FEEADR1 write failed: %s\n
Invalid data breakpoint index %d
Using 10pin connector skipping orientation check
Invalid port provided by probe server
Misc_CortexM
{%s:%s@%d} [%s] performing single step\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
Could Not Find Any Boosters of Type: %s\n
param.invalid_gpr
pc:  0x%16s cpsr: 0x%16s %s\n
ret.createKeyWithPrimate
wb
Hardware model: %s
{%s::%s@%d} [FALSE] gpr[%d] != SP\n
R1
{%s} unaligned %d-byte access at address 0x%09llx
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
MISC2
Exc Cause: 0x%x - Exc Vaddr: 0x%x
no device when sending request
CortexA8
ret.set_spmi_interface
CPUMonitor
Unique required when %d probes
%s probe[%s] from Probe Map Server [local host]
Creating CPU With Name: %s\n
wrstn-size
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
EXPLORE_JTAG_NO_BOUNDARY_SCAN
FEEADRAH
_get_type_hw
fn._ocd_exec_instr.xsr.ddr.t1
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
%s at offset %zu
fn._ocd_exec_instr.rsr.reg_srn.t1
%s-%06d
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
astris_batch_attitude_destroy
_set_bpcr_hw
AXdebug_auth_authenticate
SCAN
--> debug      size=%3d acsr=%d
[AstrisAsync] Completing all async commands. Initial err = %d\n
astris_setup_placeholder
fn._ocd_reg_r.ddr.regidx_save
## apr %u 0x%08X %d -> 0x%08X ...\n
DESIGNER_ARMDAP
opcode=0x%6.6X
USB connection not currently open
LMFLASH
KIS Preflight No Need To Write to AP CSW
{%s::%s} %s pre_resumed\n
Failed to write transfer register (EDDTRTX) the value to write
{%s::%s@%d} [FALSE] system_reg[0x%08X] & REGID_MASK != 0\n
M
DPAP
[1500] v2 plist missing required field 'bridges'
[1500] TAP %d missing required field 'chip-index' or 'irlen'
ret._a64cpu_raise_el_hw.after_cached_fault_reg_latch
internal.get-timer-count.debut_auth == NULL
DBREAKA0
primateHubLoc
KIS-Null
cpu_go
The debug port associated with this chip has not been explored.
      Read of JTAG-AP port %u PSTA failed with %s\n
_tie_read_word32
getOrCreateObject.diagnostic_checks
VectorCatch
{%s:%s@%d} [%s] bad hostname\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_booster_api.cpp
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s:%s@%d} [%s] writing DSCR\n
{%s} halting %s\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
ret.relay.get.haskis
{%s:%s@%d} [%s] getting GPR 0\n
error %s reading DAP MPIDR
Exception virtual address
M1
APCIE
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
unable to read memory (using system ap)
max_scan_bits is low: %d
{%s:%s@%d} [%s] wait_for_cmd_aborted failed: %s\n
Table 5–173
RF48
AXI Error
nullptr == file_url
## dpw 0x%02X failed (%s)\n
RF2
{%s::%s@%d} [FALSE] src_gpr[0x%08X] < GPR_COUNT\n
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
AXchip_get_chip_id
CTI_GATE
ret.write_sysreg_hw.spsr_el
symbol_array == NULL
ACCHI
_read_general_reg
gor
%s %s\n
TCP recv
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
ret.exec.msr.scratch->mddtr
AXcpu_getinfo
ACC-CTI
{%s::%s@%d} [FALSE] val[0x%08llX] < UINT32_MAX\n
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
mmu_init
OCD Debug data register
cpu-xtensa-dbg-intr
astris_kis_poll_cfg_reg
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
EXPLORE_GENTLY
get_chipid
param.shift.invalid.out_of_range
dest_gpr <= 15
CCOUNT
fn._ocd_reg_r.dsr.2
Got an error reading the DCM Control Register: %s
exit.exception_test_2
{%s:%s@%d} GRPS[0] cached\n
{%s::%s@%d} [FALSE] OP2 out of range [0x%08x]\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
probing %s status\n
astris_jtagap_explore_port
fn._write_mem.bp_info
%s:%s
(system_reg & (0x40000000 | 0x80000000)) != 0
{%s::%s} [%s] MMU is already active - returning %s
param.bp_info.invalid.null
Idle
EXPLORE
astris_batch_attitude_resume
aarch64
createCPU
respone == None
Failed to find a product plist for this soc %s
ASTRIS_ERR_BADHOST
stat
{%s::%s} creating CPU
sel-partition
[%s] TGE is NOT set. Traping to EL1 allowed.\n
Lowering exception in AARCH32 Mode NOT SUPPORTED
_a64cpu_assert_rw_matches_hw
{%s} [!is_64] exec: ISB_SY_ENCODING\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
MESR
wb=%u
bits
%s constructed
fn._ocd_reg_w.regval
ERROR!! write binary data parameters invalid\n
TLR
SLEEPCTL
start_time
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
AXbreadcrumbs_clear
Invalid escape character in string.
PAR_EL1
COHERENT
L2
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
ICOUNT
Table 5–174
name=\"%s\")
ARMV4
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
Failed to exec DCPS in order to move EL up to %d
SoC has been setup using standard instantiation (setup result=%d)
swdackdelay
ret.m_lam.paccess_read
AuthDebugWithTimer_t destructor \n
fn._write_window_base.wb.wb_save
fn.var.exec_path.invalid
Async is disabled for current seesion
IRSCAN
level_stack_.GetSize() >= sizeof(Level)
RegionStart
pmu-name
AXcpu_translate_with_stage
Loop-end address
General register 4
General register 6
port_%d
cpu-xtensa-reg-size
1
high
Going To Create Generic Xtensa Core, name=\"%s\".\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
cpu_readreg
AXchip_switch_taps
ret.production_emulation
set.wp.len = not supported
{%s=>%s} AXconn_t has no chips
High level 5 exception PC
AXconn_port
Misc_NoSoC
complex-id
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
internal.is_authenticated.chip == NULL
Boolean regs./reg.file
EPS6
{%s} couldn't set thread specific - %s\n
XTENSA
function
lower_el.el2.noimplemented
AXcpu_hwbp_enable
Register file 63
fn._ocd_exec_instr.xsr.ddr.t1.1
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
cpu_lacc_bp_status
virtual int ARMv6cpu_t::read_dcc(int *, uint32_t *)
virtual int ARMv7cpu_t::_halt_hw()
_a64cpu_read_gpr_hw
{%s:%s@%d} [%s] reading CCSIDR[L1-I]\n
ret.reg.read.K_PKA_REG_NAME_DBG_VERSION
ret.CFURLCopyFileSystemPath
fn._ocd_reg_w.dsr.regval
probe %s [port %u] on localhost
{astris_probed_print_events_from_json} not supported in this build configuration
get_gpr
_flush_state_hw
(Last: %s)
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
RegionEnd
cpu-armv7m-imem-size
SP
_ocd_reg_dcr_r
TARGETSEL
Miss exponent in number.
phase
products
extract
!!!! Critical Error: (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0 !!!!\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
FEEADRA
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
x != 0
Got an error writing 0x%X the DCM Control Register: %s
DCS13
_sstep
```
