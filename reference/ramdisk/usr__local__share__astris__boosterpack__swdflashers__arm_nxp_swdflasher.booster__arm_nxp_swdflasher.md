# `/usr/local/share/astris/boosterpack/swdflashers/arm_nxp_swdflasher.booster/arm_nxp_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,750,608 bytes.

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
VBAR: %#x\n
could not perform cpu_preflight
Proceeding with full explore instead of instantiation
{%s} Error %d(%s) sending message
--> psr        size=%3d bit=%d
2: ARM64_SYSOP_ATS12E1W\n
     ARM %s debug CPU rev %d\n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
SSO is DISABLED\n
X12 Part
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
AXmemap_readvals failure - %s
Failed to convert CFString to C String.
CPU Die: %d\n
   Debug Port has unknown type\n
{%s@%d} Unknown CS command error [%d]
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
Gathered:\n
Failed to convert %s key @ index %d
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
{%s} Failed to resume %s: %s
Failed AP write of R_MEMAP_CSW res: %i newval %i
Successfully connected to server, %s:%d
\t[MATCH_SKIP] skipping entry
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
Failed To Initialize Logging\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Can't get OS build version - failed to allocate buffer
Invalid SoC Booster. SoC Booster Requires PID\n
{%s:%s@%d} Critical error encountered:
{%s} empty response string provided
relay_get: %s = %d
{%s} bridge returned DECERR
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
Complex Address: 0x%llX\n
--> master     size=%3d localwrstn=%d debug=%d
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s} category=%d
ERROR: unable to suspend translation for %s
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
Debug Base: 0x%llX\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
Error happened when reading edscr. Retry #%i\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Previous authentication in-flight, wait for it to finish\n
Xtensa Option options: 0x%x
Xtensa Option reg_file_size: %d
CPU ASC Offset: %d\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Breakpoint Address: 0x%llx
Breakpoint Size: %d
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
{%s@%d} Timeout while attempting connect to server
Chip %x Status = %d\n
{%s} error: %s
{%s} explore with exploreflags 0x%X completed with error [%s]
Can't get OS build version - failed to create plist
can't find pid in response\n
\t%s (%s)\n
Die Addr Info LSB: %d Mask: 0x%016llX\n
[%s] {%s->%s} clear async abort
Unable to read GPR 28
[COLLECT] Chip %x\n
{%s} %s DC cache clean complete, marking as clean
Replacing key with value
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
[SSTEP] bvr=%08x bcr=%08x\n
replay_counter=%lu
Unaligned Read @ 0x%llx Width: %d Bytes: %d
\tAligned Read Failed
type_hint not NULL, but creating a placeholder, this is off
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
Required Key-Value is a string, and not an array. Old booster found\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s} Debug Base: %08X
CPU Monitor key does not exists for: %s\n
Can't get hardware model - failed to allocate data string
Failed to create Xtensa CPU %s \n
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
AXjtag_explore failure - %s (%d)
In Preflash\n
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
[1500] Error parsing TAP description
[RESUME] Chip %x\n
{%s} setting up nameless target (address=0x%llx)
{%s} unable to allocate probe name
{%s@%d} Unable to create socket
We are done with clean up\n
Failed to allocate space for table!
DCCCTRL = %08X   res=%d\n
{%s} already collected %s, skipping
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
AXjtag_srst assert failure - %s (%d)
[%s] Booster System Is Not Initialized\n
=== Loaded %s Boosters ===\n
Unable to allocate memory for big response
{%s@%d} {%s[select]} %d(%s) [RETRYING]
[1500] Error parsing IR command: %s
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
[%s] {%s->%s} Transitioning to exception level %u.\n
Result while reading first entry: %s , entry val 0: 0x%X\n
HOSTID=0x%x which is invalid, skipping orientation check
SoC does NOT support IDE Explore\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
JsonLogger: Wrote %zu bytes to '%s'
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s} Component ID read fail on romtable (%s)
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
{%s[recv]} %d(%s) [RETRYING]
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Highest EL: %d, -- Min Op EL: %d
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
   Debug Base: %08X\n
Probe %s USB-C location is %s
We are Allocating\n
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s} collect result = %s
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
\t[MATCH_TARGETID] FAIL <= unable to find DP
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[HALTED] dfsr = 0x%08x\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
{%s} Error reading CPUID (%s)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Pages %d\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
[AstrisAsync] Activate while async is already active!\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
      Select port %u: AVOIDED\n
Could not find portal by select %d, while interpreting result\n
\t[MATCH_FOUND] identified chip: %s
TAP IDCODE: 0x%X\n
Failed to sync prefs at end
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
{%s} ROMTABLE (dbgbase=0x%llx)
Probe %s Device Not Connected on USB-C Port
Could Not Find Any Loaded Boosters of Type: %s\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
process (%s) (%d) path: %s
Old ProbeDaemon does not support this command
{%s} unsupported bridge type for %s
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
Unable to create pthread key for conenction. errno=%d %s.
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Using Built In SoCs\n
{%s} DEVARCH read fail in CoreSight component (%s)
      AXap_write of R_JTAGAP_PSTA failed with error %s
Error status from AMAuthInstallSsoInitializePtr = %i
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
Please answer y=yes or n=no.\n
%s
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
{astris_probed_print_events_from_json} not supported in this build configuration
Groups %d\n
%s: not supported.\n
%s NOT configured\n
     ARM %s breakpoints: %u\n
{%s} handle ROM entry %d (level %u): %08x
{%s::%s} [%s] unsupported width %d
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
Gateway is KIS, seeing what probe this is\n
Probe Map comm error %d(%s) %s [%s]
Booster:\n
!!!! DART Key %s is INVALID !!!!\n
Error %d(%s) executing instruction 0x%08X FAST
pc:  0x%16s cpsr: 0x%16s %s\n
     0x%016llx: ERROR\n
{%s} %s status is '%s' [Status Read %d times]\n
** Unauthorized User/Network or ECID **\n
CPU with %s Not Created via Name
ERR: conn->nchips != 0; looks like chip is explored\n
Chip Revision: 0x%X\n
Can't get OS build version - failed to create ReadStream
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
relay_get: %s = CMD_ERR (%s)
JsonLogger: Schema loaded successfully for category '%.*s'
[KIS] Portal Status: 0x%X\n
Could Not Find a DCM Portal
haskis bit not set\n
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s} no matching 1500-to-* bridge
{%s} Failed to extract die infofrom table (%d); continuing anyway
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
{%s} FIFO full, try again
{%s::%s} failed: %s
{%s::%s@%d [%s]} Error %s: synchronizing context
{%s->%s}
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
   Debug Port: SELECT %X: AVOIDED\n
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
AXportal_t Struct Is NULL
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Breakpoint Enabled: %s
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Found %s\n
Can't get hardware model - failed to convert to C string
Setting STOP CLOCK to TRUE
[1500] run_steps: unknown instruction '%s'
{%s} calling _collect_hw on %s
Complex CPU ID: %d\n
Dart CPU SID(s): %s\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
Failed to convert CFArray to C Array\n
Initialized Logging - %s
Got an error reading the DCM Control Register: %s
[READ] cop64 %d -> 0x%016llx\n
1: ARM64_SYSOP_ATS12E1R\n
   {%s} Before powerup CMDSTAT=%08X\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
Probe %s removed during selection process
{%s::%s} ITE is not set: 0x%X\n
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s[select]} timeout while waiting for data from the connection
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
{%s::%s} %s pre_resumed\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
Subsystem Monitor[%i]: %s\n
response == NONE; failed to get kis target info\n
{%s} %s did not match any valid host
Awaiting response from Probe Map Server
Raising to EL2 cause in Guest\n
[REMBP] bp%d\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Had an error during transfer: %s
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
!*!*!* ****************************************************************************** !*!*!*
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
AP[%d]: MEM_AP_AHB\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
Successfully Authenticated\n
Spew change. old=0x%016llX, new=0x%016X
{%s@%d} IOServiceClose failed, err = 0x%08x
In Readflash\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
[AsyncSnapshot] No snapshots collected\n
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
{%s} 0 words requested for read at address 0x%016llX
The debug port associated with this chip has not been explored.
Invalid Bundle: %s
We Are Matching Development Booster\n
{%s::%s} NULL parameter
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
wrote      0x%08X @ 0x%08llx\n
Can't get hardware model - failed to allocate data buffer
Set custom PSD json file: %s
Dart Base Address: 0x%llX\n
{%s} Failed to single-step %s: %s
AP is NULL
Result while reading second entry: %s , entry val 1: 0x%X\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
Selecting polling method %s
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
Early dbgwrap base extracted: 0x%llx\n
{%s} _pre_resume_hw result = %s
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
=== Starting Gather and Clear ===
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Enabling USB Gateway
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Unable to read PC
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
{%s=>%s} no soc reference; falling back to direct cpu method
Error %d (%s) opening history save file
Probe %s selected
{%s} select success without file descriptor set
TargetSel Before Disable: 0x%x
{%s} bridge timed out
\t\t%s\n
Required key: %s @ index %d is NULL\n
product-name: %s\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
[AstrisAsync] Discarding response due to ASYNCSKIP state!
   MEM-AP not enabled\n
{%s::%s} waiting for EDSCR ITE
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
replayPreflight
   {%s} Probe requires overrun detect mode.\n
Invalid Size Given for AP AP=%d Size=%d
Error closing %s [%d]
%2d) %s %s%s\n
VBAR: %#llx\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Portal Status, Changing STATUS and CMD/STAT to reflect
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
!!!! Complex CPU Key %s is INVALID !!!!\n
{%s} L2 cache operation completed [%s]
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
Asked To Write To A Negative Register Index
Value Types Are Not Strings\n
--> extrawrstn %d
{%s::%s} [%s] MMU is already active - returning %s
     0x%016llx: 0x%08x    %s\n
[AstrisAsync] Pause when already paused!\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s} PRIMECELL [DONE]
{%s} failed (%s)
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
Could Not Allocate Info Keys Array
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Error returned from explore_pid
[READ] %d -> %08x\n
## dpw 0x%02X failed (%s)\n
Failed to read ide_table from KIS explore
{%s::%s} EDSCR with TXU set - unable to recover.\n
Unable to read CPSR
{%s} handle ROM entry
Finished!\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
We are Deallocating\n
!!!! CPU Key %s is INVALID !!!!\n
[1500] TAP %d missing required field 'ir-cmds'
CPU: %s halting debug is now %s\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
   Debug Port: SELECT %X: SKIPPING\n
--> 0x%02x = %s
astris_get_async_ver failed with error: %s
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
Failed AP read of R_MEMAP_CSW res: %i
SSO with no prompt being used
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
connection about to be destroyed
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
Min Component - %s\n
error %s checking for data abort(uint32_t)
Xtensa Option non_tie_ranges: %zu range(s)
Hang Radar Info:\n%s\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
CPU (%s) has explore flag of: 0x%llx which is not set\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
Debug Clock Already Enabled
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
Going To Create Generic ARMV8\n
   {%s} Enabling debug unit\n
KIS Chip Found, Doing KIS Explore Setup
Programming...\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
--> misc_wdr   size=%3d wirtestporten=%d
We are at max iterations, still didnt get full JSON
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
[READ] cop %d -> 0x%08x\n
DEMCR: 0x%08X -> 0x%08X
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
%s given a NULL conn object
relay_get: %s = ERR
Could Not Create Dictionary From Booster: %s
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
{%s} asc status=%d being reported as Unknown
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
%s SoC created
--> wrstn_wir2 size=%3d dpcsoc=%d
\t\tARMv6 debug CPU xxx ID\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
   Debug Port: Trying SELECT %X\n
Verify failed\n
unable to identify chip
[%s] Booster System Is Not Initialized Bailing\n
!!!! FILE RADAR: Don't know how to compare two values\n
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
[%s] EL @ end of Collect: %d\n
collect_responses
OS build version: %s
{%s} Failed to extract chip debug base from table (%d); continuing anyway
{%s} DAP command nwords=%d trimmed to %lu\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
## armcpu: bad status even though all bytes read (%d)\n
[REMWP] wp%d\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
AuthDebugWithTimer_t destructor \n
register    %-15s %3u     \"%-s\"\n
{%s@%d} neither socket nor kext connection available
Initialized %d 1500 bridges\n
[KIS] Register Read/Write/Wrote: %d\n
OK: address translation suspended for %s successfully
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
CPU %s not found or already removed from the map
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
no debug bus AP present when expected; after sysap is NULL
Could Not Find Booster Entry Function: %s\n
{%s::%s} HDE not set on %s. Will re-enable.
   DPv3 BASEPTR0 is 0x%08X\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
Kick has been requested by probe server
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
   Debug base is in legacy format\n
read back  0x%08X @ 0x%08llx\n
Issuing request to Probe Map Server: %s
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
[AstrisAsync] Resume when not paused!\n
      Read of JTAG-AP port %u PSTA failed with %s\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s@%d} Received %d bytes when requested %d bytes.
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
{%s=>%s} null reference to CPU_t object, `cpu->state`
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Could not find TAP at chip-index %d for v2 1500 config\n
[ARM32cpu_t::_read_register64] 0x%08x\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
Can't get hardware model - failed to create string
CPU Typehint: %s\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
[CACHEOP] %d, 0x%016llx, %d\n
ERROR: unable to resume translation for %s
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
max_scan_bits is low: %d
Error while trying to authorize: %d - %s\n
Hardware model: %s
Target ID: 0x%X\n
Die Config Disabled
Start Page: %d\n
{%s:%s}: cpu powered off: unable to access a register for this CPU
1: ARM64_SYSOP_ATS12E1W\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
{%s} host = %s
Failed to get KIS translator version\n
coalesced-target: %s\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s=>%s} null reference to AXchip_t[0]
Sending DYN Bypas Channel Set: %d
In Writeflash\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
Failed to sync prefs at beginning
{%s} explore with exploreflags 0x%X complete [%d chip%s]
      Select of JTAG-AP port %u failed with %s\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
%s\n
[%s] TGE is set so we traping to EL2\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
Found form-factor specific channel %u for device '%s'
{%s} Failed to extract portal info from table (%d); continuing anyway
Async is disabled for current seesion
AP[%d]: MEM_AP_AXI\n
## apr %u 0x%08X -> 0x%08X\n
Not Creating CPU: %s\n
[KIS] Register Index: %llu\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
AP[%d]: unknown type\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
Connected toProbe Map Server (single_port) 
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Complex ID: %d\n
Found an async abort pending; clearing it\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
{%s} read %d words from probe when %d words requested
Failed to convert primateLoc %s to unsigned long long
{%s} %d(%s) [RETRYING]
Could not find TAP at index %d to attach 1500 bridge to\n
{%s} set=%u (sh=%u), way=%u (sh=%u)
OK: address translation resumed for %s successfully
register lookup by name not supported when Astris is statically linked
## memapr %u 0x%016llX %d -> 0x%08X ...\n
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} Failed to extract CID from table (%d); continuing anyway
%s constructed
Error %d(%s) executing instruction 0x%08X
{%s} Class 9 ROMTABLE (nest=%d)\n
{%s@%d} Unknown CS code [%u]
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Got an error writing 0x%X the DCM Control Register: %s
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
Initializing Booster Layer\n
     ARM %s watchpoints: %u\n
read failed, using old cached as base: 0x%x
{%s=>%s} AXconn_t has no chips
{%s} probe_match = %s
{%s} unaligned %d-byte access at address 0x%09llx
Matched via Bundle ID\n
{%s} (end) current_el is now %d
%s: []\n
Optional Key: SubsystemMonitor not in preferences
{%s} connectName[local host]
{%s} valid response from bridge
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
Turning Debug Clock On
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Probe %s status: Idle
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
DHCSR write failure - %s (%d)
Could Not Find Any Boosters of Type: %s\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
CPU Monitor[%i]: %s\n
%s probe[%s] from Probe Map Server [%s]
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
[1500] %s step %d missing required field 'instr'
{%s} Thread %#llx clearing key %lu
   Debug Port not responding (%s)\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
Error status from AMAuthInstallSsoEnablePtr = %i
** Add the --with-force option or use the explore_override console command **\n\n
Type 'jebdump' to do scan/mem dump\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Probe Map name of probe %d is: %s
relay_set: %s -> %d
Complex Name: %s\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
probetimeout retry failed logging as hang\n
write to CMD/STAT failed - %s
Unable to read SP
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
X09 Part
Could Not Allocate Booster Location Array
Koko probe, for now I guess we will just say yes...\n
{%s} Extracted CIP Gen Number from table  (%d)
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
Invalid current AP (%d), adopting latest (%d)
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
{%s=>%s} AXconn_t has no SoC object
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
[AstrisAsync] Barrier before pause\n
{%s} %s: |%s|-|%s|
couldn't find CPU1. this is expected sometimes.
error %s reading DAP PFR1
2: ARM64_SYSOP_ATS12E1R\n
%s probe[%s] from Probe Map Server [local host]
{%s} no TAP detected that supports 1500
KIS Readvals putting back the value
Could Not Get BoosterManagerUtility\n
codeblock
Connected to Probe Device Server [Log File %s]
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
[AstrisAsync] Deactivating async...\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Xtensa Option dbg_intr_level: %d
{%s} Batch attitude key created for %p thread %#llx key %lu
CPU Core Number: %i\n
[1500] v2 plist missing required field 'taps'
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
[CLEANUP]\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
Trying to use size of 8 on not AXI bus
{%s} no chip found
Could Not Allocate All Boosters Array
Invalid current AP (%d), adopting APTABLE (%d)
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Probe %s Device Server listening on port %d
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Asked To Read A Negative Register Index
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
   Setting up AP IDR %08X\n
Failed to find a product plist for this soc %s
%s status transitioned: %d ('%s') -> %d ('%s')\n
{%s} probeList has probeCount of zero
Creating CPU With Name: %s\n
No version information found in booster: %s
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
Using Built In CPUs\n
SoC has been setup using standard instantiation (setup result=%s)
SoC not identified by IDCODE - enumerating instead of instantiating
Xtensa Core %s NOT configured\n
New format for cip gen register, unsupported: %d\n
   JTAG-AP: Identification = %08X\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Cannot create SoC [unknown chip identity (%d)]
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
{%s} Failed to extract PID from table (%d); continuing anyway
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
## apw %u 0x%08X 0x%08X\n
tckrate_check returned error %s
Previously dumped the process tree, skipping
%2d) %s %s [Busy]%s\n
AXconn_t Struct Is NULL
=== Found %s Boosters ===\n
[MEM] Uncompleted; DSCR = %08x\n
JsonLogger: Creating new category '%.*s'
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
\t%s\n
[1500] Error parsing v2 bridges
dfu-Type: %s\n
{%s::%s} write OK but took %d tries
{%s} Failed to get watchpoint mask for %s: %s
AP Only Explore was asked for, stopping here
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
{%s@%d} Probe response payload read when no payload indicated.
[AstrisAsync] astris_async_override_disable_async: conn is NULL
{%s} Component ID read fail for 0x%llx (%s)
{%s} wrote %d words to probe when %d words provided in request
      Explore of JTAG-AP port %u failed with %s\n
{%s} FAILURE - max length exceeded
start rev is not of expected format; skipping cpu_desc override\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[%s] m_dc_max_level %d, m_ic_max_level %d\n
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
{%s} unmodified-probe_match = %s
Found match - bypass_device: %s; channel: %d\n
CPU Subsystem: %s\n
Failed to convert %s key @ index %d to a number with base of %d\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
SWDACKDELAY relay write failed\n
Warning: chip exploration did not complete successfully (%s)\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
[ARM64 INS_WP] 0x%016llx x %d\n
[PREFS] Key: %s - Val: NULL
no matching part (%s)\n
Probe (port=%d) with unknown status %s dropped from available list
HOSTID bit not set\n
using multi-target booster products_%s.plist
{%s::%s} [%s] !bpwp_initted, retrying init
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
error %s checking for data abort(first)
--> cmd        addrsize=%d datasize=%d
{%s::%s} [%s] error %s reading SCTLR_ELx
EICE chip %x initialized\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Xtensa Option ocd_address: 0x%llx
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
Extract Offset: 0x%X for %d\n
{%s} %s status failed. error: %d (%s)
Exception %d Stack Trace
Initial DSPSR_EL0: 0x%llx
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
{%s::%s} [%s] MMU not active - returning %s
{%s} status=%d being reported as Unknown
AP given is not a MEMAP
Unable to register assert upcall %s (Insufficient memory)
unable to create connection
=== Detailed %s Boosters ===\n
Cannot create CPU descriptions from NULL info\n
[1500] IR command '%s' missing required field 'opcode'
UPDATE cop64 %d -> 0x%016llx\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
The log file has been updated with all available diagnostics.\n
Probe %s status: Busy
DBG_CPU: %s\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
Cannot create complex descriptions from NULL info\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s} drop ProbeName %s
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
Invalid APTABLE (%d), so using most restrictive
{%s} timed out waiting for cpu to halt during collect
Buffer is NULL
Both debug and xbs versions are set, maybe a bug: %s
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
     0x%016llx: 0x%04x      %s\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Error %d (%s) opening cmd snapshost save file
Error %s connecting to server %s:%s [RETRYING]
{%s} no response from bridge
Size or Count provided are 0.
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
[HALT] Chip %x\n
 MEM-AP %X is hung\n
{%s} Unrecognized Component: %08X (class %u)
{%s} FAILURE - NULL parameter
Multi target booster, checking for %s.plist\n
error %s reading DAP MMFR0
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
kext connect name %s\n
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
Did Not Find Any Boosters For: %s \n
XBS Version Modified: %s -> %s\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s::%s} [%s] error %s from _synchronize_context.
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
Probe %s with unknown status %s dropped from available list
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Complex Type: %s\n
Cannot create DART descriptions from NULL info\n
[FLUSH]\n
Wrong width, should be either 4 or 8\n
{%s} Exploring with option: %s\n
Setting CPU %s is_boot_core to %d\n
After powerup CMDSTAT=%08X\n
CPU Supported in Integration: %s\n
bypass-config-name: %s\n
[%s]\n
probing %s status\n
[Auth Debug] Disabled\n
Banana split probe, for now I guess we will just say yes...\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
[MEM] Aborted; DSCR = %08x\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
ERROR!! Couldn't save %s binary data\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
Exploring IDE in JTAG\n
probetimeout retrying access...\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
DBGSTATUS = %08X   res=%d\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
Failed explore before forced KIS reset: %s\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
%s probe[*] from Probe Map Server [%s]
{%s::%s} creating placeholder for CPU: name=%s
Stepping Stone Final =  %#x\n
{%s} Unrecognized component: %08X, class %02X\n
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
{%s}#%02X cmd: %s, resp: %s
Dart Name: %s\n
Unable to read LR
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
  Error path [%s]\n
Full JSON that failed validation:\n%s
We are in clean up\n
Required Key-Value is a string, and not an array. Old booster found: %s\n
{%s} Failed to extract target ID from table (%d); continuing anyway
[DCC] Grabbing DTR failed: %s\n\n
{%s->%s} m_exception_level=%u
[AstrisAsync] Failed to restart Async batch\n
** \tTatsu AuthDebug Triage | All     **\n
Error %d (%s) while expanding ~ for Astris history save\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
[REM_HWBP] bp%d\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
%s probe[*] from Probe Map Server [local host]
Failed to convert kisLoc %s to unsigned long long
Probe Type (%d) FW Version: %s does not support KIS.
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
Probe %s Device Does Not Have LocationID
{%s} unable to allocate probeInfo
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
Can't find descriptor for group - can't index\n
Successfully Authenticated Probe\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
    INFO(%u,%d): %s(%04u): %s(): %s
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
Valid Portal
User created bundle found, ignoring version checking via plist
CPU Supported in Runtime: %s\n
Hang Description:\n%s\n
Probe %s removed before port determined\n
JsonLogger: Created with default schema version '%s'
setCategoryValue: path='%.*s'
error %s checking for data abort
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
failed read from DEMCR - %s
[AstrisAsync] Got ASYNC_RESTART response!
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
SoC has been setup using standard instantiation (setup result=%d)
Logging Context Is NULL\n
[1500] Detected plist version %d
Die-Count: %d Current-Die: %d Die-Type: %d\n
Die-Count: %d Current-Die: %d Die-Type: %d
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
connection created
Booster Info:\n%s
using standard products.plist for %s
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
Creating CPU Returned: %s\n
Complex CPM Offset: 0x%llX\n
component group %d\n
[%s] %d -> %08x\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
   Debug Port: SELECT %X: DISABLED\n
   JEDEC ID: 0x%08X\n
Init dbgwrap obj failed
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
   {%s} select %u port %u: %u chip%s\n
Portal Group Base: 0x%llX \n
CPU %s already in the map with status: %d
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
Width: %d not supported
{%s} checking for single_port probe daemon on port %d
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
Async is disabled for localhost connection
{%s::%s} creating CPU
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
AXconn or json_out are NULL
{%s} Found extra info in = %s, chopping string
{%s::%s} ERROR %d(%s) resuming %s\n
Failed to explore chip: %d
\tTatsu AuthDebug Triage | All\n
PKA Base: 0x%llX\n
dropping empty probeInfo (port=%u)
sent %zd bytes to Probe Map Server when sending %zu
Connecting to server, %s:%d
comparing against match entry [pid] %d: %s\n
Setting bypass channel to: %d\n
Could Not Match A Booster for %s\n
Invalid file name: \"%s\". File names must not start with '.'
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
Production Fused Device\n
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
** CPU %s requires forced explore override flag on this SoC **\n
   {%s} Clearing HNONSEC on AP \n
Switch back to primate KIS: %s\n
{%s} probe_port = %d
{%s} probe [%s] added to list
{%s@%d} Connection to server failed, error=%d (%s)
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
unable to obtain sysap
{%s::%s@%d [%s]} Error %s: checking exception
Unable to read GPR %d
{%s} Error looking up architecture (%s)
## memapw %u 0x%016llX 0x%08X ...(%d)\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
Going to do imago workaround\n
=== Ending Gather and Clear ===
{%s} host name(RSD): %s\n
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
DEMCR read failure - %s (%d)
1500 IR Commands:
Match Count is Zero. This is invalid.
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
[AstrisAsync] Barrier hit!\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
[%s] %d -> 0x%08x\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
Original Content: 0x%08x
Can't get OS build version - failed to open ReadStream
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
In Eraseflash\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
CPU DBG Ack: 0x%llx\n
Probe Map comm error %d(%s) %s
Failed to get Bypass Config
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
[AsyncSnapshot] #%zu: %s\n
Failed to convert kisHubLoc %s to unsigned long long
Probe Map comm: request[%s], response[%s]
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
## dpw 0x%02X 0x%08X\n
\tReading left over chunk expected 0x%x got 0x%x\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
Could not enable KIS SoC Access\n
{%s} invalid data width %d bytes
!!!! Complex Key %s is INVALID !!!!\n
{%s} Unable to read SP_EL0
## armcpu: success status even though not all bytes written\n
In Postflash\n
Adding new booster path: %s\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s} drain_packets=%d [%s]
{%s} %s DC cache already clean since last halt, skipping flush
AuthDebug::authenticate_probe - no need to authenticate\n
Xtensa Option num_wp: %d
Xtensa Option num_high_pri_intr: %d
SOC_t::{%s} CPU_t group=%d when group 0 expected
Values Not The Type We Expected. Expected: Number and String\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
X06 Part
Caught a portal that we dont have a status map for: %d
Could Not Find Any Boosters\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s} Failed to extract component info from table (%d); continuing anyway
## ARM32cpu_t::read_register %u\n
{%s} _pre_halt_hw result = %s
## apw %u 0x%08X 0x%08X ...(%d)\n
[1500] TAP key is not a valid integer
{%s} halting %s\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
{%s} error %d(%s) reading data from the connection (at recv)
{%s@%d} Received %d bytes when requested %d bytes [%s].
{%s@%d} Failed to send probe command (error %d).
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
{%s} already connected
can't find bid in response\n
{%s->%s} START handling exception
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
There is no debug port associated with this chip.
BoosterManager Types:\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
[INS_WP] 0x%016llx x %d\n
Original Length: %d\n
Could not find bundle () in given array: %s\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
    %s(): %s
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Failed to Identify & Explore Chip via KIS: %d (%s)\n
{%s=>%s} null reference to AXconn_t record, `conn`
Probe %s with unknown kick response %s
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
{%s} Failed to get breakpoint count for %s: %s
[PREFS] Key: %s - Val: %s
no system bus AP present with AHB, trying AHB5
[ANAMOLY] Could not find AXcpu_t object for CPU\n
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
Unable to disassemble_at_addr 0x%016llx
   ROM entry %d (level %u): AVOIDED\n
{%s} found single_port probedaemon on port %d
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
caller=%s, async=%d, iterations=%lu
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
Failed to create optional file. Not fatal, moving on
Astris Version Set: %s
unknown match criteria type: %d
[1500] Using %s.plist
[1500] %s step %d: unknown instruction '%s'
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
{%s} Error reading PID (%s)
ERROR!! write binary data parameters invalid\n
{%s}#%02X %s [%s]
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
SOC AP[%d]: JTAG_AP\n
{%s} Reading base 0x%llx entry's component ID
SSO info present but SSO disabled.
Request Dict:\n%s
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Failed to create CPU %s - %s\n
{%s::%s} [%s] error %s writing SCTLR_ELx
%s %3d'b%s\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
{%s->%s} (top) current_el=%d
{%s->%s} ERROR=%d(%s)
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
{%s} Failed to get breakpoint mask for %s: %s
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
{%s} strsep empty so match any probe [localhost]
%s [RETRYING]
checking if relay \"%s\" is valid
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
Dart Coastguarded CPU: %s\n
Unknown number of groups in the explore table; can't parse group attributes
error trying to unlock MSR %s
{%s@%d} Failed to find cached response
No 1500 bridges or TAPs specified (v2 plist)\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[AstrisAsync] Resuming Async Mode\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
{%s} flags:0x%08x
There is no system bus access port on the debug port
[%s] E2H is set, virtualization is supported\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
Translate Stage Chosen: %d\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
Failed to convert primateHubLoc %s to unsigned long long
Choose a device: 
{%s@%d} Connection to server rejected, error=%d (%s)
Gateway Version: 0x%X\n
outstanding=%zu
gmtime() returned NULL, using epoch time
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Dart Dart Type: %s\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Optional Key: CPUMonitor not in preferences
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
{%s:%s@%d} Critical error [radar already requested]
start rev and/or end rev is NULL; skipping cpu_desc override\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
Booster Bundle: %s\n
Found %d APs
CPU state %d
[1500] No %s.plist resource found
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
TatsuServer Found: %s\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
{%s@%d} Unable to connect to server, %s:%d
Gathered Info:\n%s
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
{%s} _resume_hw result = %s
   Debug Port: SELECT %X: SKIPPING (%s)\n
{%s} Error setting up memap target (%s)
first read of CMDSTAT may fail if external reset occurred
   {%s} (DP): status=0x%X(%s) - %s\n
{%s::%s} read OK but took %d tries
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
{%s} hostname:%s, flags:0x%08x
invalid IR command '%s'
Failed to find a plist for this soc %s
{%s} match any probe [localhost]
Connected to Probe Map Server
Failed to init from cpu desc armv7m cpu: %s \n
CPU Name: %s\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
[AstrisAsync] Deactivate while async is not active!\n
AP[%d]: MEM_AP_APB\n
Probe %s LocationID Info is %s
Awaiting next chunk of big response
Connection to server accepted
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
Using 10pin connector skipping orientation check
relay_set: %s = CMD_ERR (%s)
Matched Booster: %s\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
[1500] Error parsing bridge '%s': missing required field 'tap'
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
Breakpoint Index: %d
Fabric access is blocked. Expected if production unit, won't explore further.
Before astris_kis_init_dp, CMDSTAT=%08X\n
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
{%s} Error setting up jtag-ap target (%s)
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Connected to Probe Device Server [Default Log]
[%s] cop %d -> 0x%08x\n
   DPv3 bus is %u bits wide\n
[%s] chipinfo is NULL
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Disconnected from Probe Map Server
KIS Writevals putting back the value
{%s::%s} %s resumed\n
## armcpu: success status even though not all bytes read\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
X00 Part
{%s} NOMEM
CPU PS-Register: 0x%llX\n
{%s} m_exception_level(%d) != current_el(%d)
[AstrisAsync] Discarding %zu completed command(s)\n
## memapw %u 0x%016llX 0x%08X\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
%s construction failed
Problematic JSON value:\n%s
[KIS] Portal ID: %d\n
{%s}ERR: bypass_device_name is NULL\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
batch_cmd_count: %d
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
\tReading left over chunk 0x%x @ 0x%llx\n
Error Reading Device Production-Fusing\n
Failed to instantiate %s\n
%#09llx-%#09llx: %s\n
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
Unable to read FP
\tLeft To Read (%d) < width (%d).\n
choice: %d\n
{%s::%s} cpu powered off: failed init() %s
{%s[select]} %d(%s) [RETRYING]
{%s@%d} socket connection is not available
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
{%s} Failed to get watchpoint count for %s: %s
ERROR!! Wrote %zd bytes, expected %zd\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
getOrCreateValue: addMember failed, returning doc root
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
USER %s(%04u): %s(): %s
{%s::%s@%d [%s]} Error %s: collecting HW
{%s} _halt_hw result = %s
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
Init objects failed
JsonLogger: Loading schema for category '%.*s' from '%s'
==== User Error Messages ====\n
Cached async_replay capability version: %u
end rev is not of expected format; skipping cpu_desc override\n
%s: chip was NULL when attempting to release soc
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
Failed to access new_cpu status
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
Explore: %u chip%s\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
{%s} host:%s, flags:0x%08x
Skipping CPU %s at 0x%llx: not present in IDE\n
Could Not Allocate Loaded Booster Array
Board ID: 0x%X\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
[INIT]\n
   CPUID: 0x%08X\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
Could Not Get BoosterManager\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
{%s@%d} Drain empty on decr [%s].
==== Exception Trace ====\n
{%s::%s} timeout while waiting for EDSCR ITE
## memapr %u 0x%016llX -> 0x%08X\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
Switch to primate res: %s\n
Error during flashing: %d\n
Magic does not match: %#x vs %#x\n
[REM_WP] wp%d\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
   DPv3 baseptr is not valid (%X)\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
AP[%d]: JTAG_AP (Exploring Later) \n
Increasing length by: %d\n
Unsupported device (%s)\nJust going for it!\n
{astris_probed_print_events} not supported in this build configuration
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Bundle: %s NOT FOUND\n
CPU Address: 0x%llX\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
\nSaved %s binary data to %s\nWrote %lu bytes\n
{%s} %s
probe event: %s
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
iter=%lu
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
Probe %s with unknown port response %s
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
AXportal_t Is Not Valid Type - %d
[PAR] Failed KIS Portal Access Preflight =%s (%d)
## dpr 0x%02X -> 0x%08X\n
   {%s} Read AP's R_MEMAP_CSW\n
Can't get OS build version - failed to create URL
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
Found another target for the plist\n
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
sending abort to clear a timeout\n
KIS Preflight No Need To Write to AP CSW
\n
CPU Explore: 0x%llX\n
{%s} read ESR EL1|EL2|EL3 (%d)
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
[%s] AP, DP, or chip given is NULL
Preparing and erasing sectors %d to %d\n
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
[1500] Error parsing bridge: %s
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
replay_counter=%lu, last_replay=%d
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
no debug bus AP present when expected
JsonLogger: Writing category '%.*s' to '%s'
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
[READ] %d -> 0x%08x\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
{%s} %sing word #%d at address 0x%09llx: %s
Booster Value is Not String\n
[ARM32cpu_t::_update_register64] 0x%08x\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
CPU has no regions, maybe powered off?\n
{%s=>%s} AXconn_t has more than one chip
New Length: %d\n
DEMCR write failure - %s (%d)
WARNING, reserved / slide bits not zero! Zeroing out!\n
{%s} FAILURE - malloc error
Initializing (%s) Booster's Astris API\n
Passed NULL plist file\n
{%s} Unable to read CPSR
DBGCTRL = %08X   res=%d\n
{%s::%s} [%s] error (%s) getting number of HW BPs
{%s@%d} gethostbyname failed, error=%d (%s)
{%s} error %s at line %d
   --> IDR: %08X\n
Failed to read IDE through DAP\n
Can't get hardware model - failed to find matching IOService
{%s} %s: |%s|
[1500] Error parsing bridge '%s': missing required field 'select'
[Auth Debug] External Debug Interfaces Open\n
Successfully Authenticated DFT\n
{%s@%d} Timeout while sending probe command.
Generated JSON (first 500 chars):\n%.500s%s
Sprocket probe, for now I guess we will just say yes...\n
%s Bridge @ 0x%09llx-0x%09llx: %s
Failed to get DFU Type
{%s} Failed to extract ECID from table (%d); continuing anyway
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
Unable to convert plist file name to CFString: %s\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[AstrisAsync] replay preflight: Async not active!\n
## dpr 0x%02X failed (%s)\n
Subsystem Monitor Key does not exists: %s\n
Dumping Process Tree
Failed To Instantiate SOC From Booster\n
Could Not Get Bundle Out Array of Found Boosters\n
CPU AP-Select: %d\n
## armcpu: bad status even though all bytes written (%d)\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s} probe device server closed the connection while trying to read data (at recv)
{%s} bridge returned SLVERR
[SSTEP] using BP %d\n
Length is 0
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
Modified Word To Write: 0x%08x
[%s] CPU BM Not Found, Bailing\n
\tPrologue Aligned Read Failed
Result while reading third entry: %s , entry val 2: 0x%X\n
Created Connection - : %s
Section 1 Offset: 0x%llX\n
[%s] {%s->%s} END handling exception
[AstrisAsync] replayConditionalCheck: condition hit!\n
[Auth Debug] Ticket Active, Debug Interface Locked\n
no system bus AP present when expected
Invalid value for 'entry' tuple element - can't index
{%s::%s@%d [%s]} Error %s: resuming HW
read_dbg failed to access R_v7M_CLIDR
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
{%s} probe_host = %s
Unable to allocate memory for next part of big response
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Portal Group Offset: 0x%X Entries: %d\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
successfully updated DEMCR
Aligned Address: %llx
!*!*!* Lightning header facing up.                                                    !*!*!*
Cleaning up Each Booster Manager\n
CPU AP-Type: %d\n
[AstrisAsync] Activating async...\n
\tLeft Over Chunk Read Failed\n
Probe %s removed prior to kick\n
Cleaning up Main Booster Object\n
[1500] v2 plist missing required field 'bridges'
{%s} skipping dcache flush, cache already clean
[AstrisAsync] Async mode %s
Xtensa Option num_bp: %d
{%s} ROMTABLE (nest=%d)\n
[KIS] CMD: %s \n
   Debug Port: SELECT %X; error: %s, retrying..\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
   Created Fake Debug Port Debug Port
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
{%s} bridge returned an error
Gathered Value is Not Number\n
Table Size: %d\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Probe Map Server Information: %s
AXjtag_srst deassert failure - %s (%d)
Map is empty, not removing CPU %s
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
received %zd bytes from Probe Map Server when have %zu
[KIS] Address: 0x%llX\n
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} unable to find single_port probedaemon on port %d
No 1500 bridges specified\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
      Select port %u: already explored..re-exploring\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
--> debug      size=%3d acsr=%d
Booster System Is Not Initialized Bailing\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
Can't get hardware model - failed to get property
Can't get OS build version - failed to get build version
comparing against match entry %d: %s
Astris Source Version: %s\n
Too many portals, we are at portal: %d while max is %d\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
Invalid character [0x%02X] received from Probe Map Server
Found probe memory transfer in progress; clearing EDSCR.MA.\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
{%s} %s resumed\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s} restored el is now %d
{%s::%s} [%s] length=%u when width=%d
runBlock
Connect using RSD not supported\n
      Read of JTAG-AP port %u CSW failed with %s\n
Preferences does not exists: %s, creating one.\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Taking gateway control failed
Could Not Allocate Mutable Dictionary For BoosterMangers
{%s} [%s] m_exception_level=%u\n
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
SoC BM Not Found, Bailing\n
Complex CPU Name: %s\n
error %s reading DAP MPIDR
  Nested path: parent='%s', child='%s'
Stop Clock: %s\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
{%s::%s} halting %s\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
{%s->%s} current EL (%d) already == target EL.\n
%s status is '%s'\n
[PREFS] Key: %s - Val: ??
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
failed write of 0x%08X to DEMCR - %s
caller=%s, async=%d
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
{%s} pmgr status=%d being reported as Unknown
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
--> localwrstn size=%3d debug=%d
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
About to call fault reg latch, min_operating_el: %d\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
dbgwrap halt failed, falling back to classic method
Kick off the current process using probe %s? (y|n)\n
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
pmu-name: %s\n
[WRITE] %d -> %08X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
{%s} connectName[%s]
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s::%s} creating AP slave: name=%s
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
KIS translator version : %d\n
{%s@%d} Found cached response
{%s} 0 words from probe when %d words left to read for reg %d
Failed to get PMU Name
{%s::%s} error %s writing EDSCR %s
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
Failed To Init Booster's Astris API In: %s with %s (%d)\n
[1500] TAP %d: irlen must be > 0 (got %d)
Component Group Offset: 0x%X\n
Found the RTXCID Structure!\n
[AstrisAsync] Pausing Async Mode\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
Passed NULL booster without custom plist\n
Die Config Disabled\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
Variables not setup
Hang Address: 0x%016llx\n
SoC must have a DAP
[KIS] Words (Read/Write/Wrote): %d\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Protocol Version: 0x%X\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
name <= nameBuffer_ + length
Append
FAR_EL2
astris_arm64cpu.cpp
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
SWD
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
error %s checking for data abort
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
CPU%d
ret.reg.write.K_DA_REG_NAME_NONCE_2
param.shift.invalid.out_of_range
Kick failed: probe no longer hosted by probe server
Failed to convert %s key @ index %d
{%s:%s@%d} ARM64-specific _sstep method not currently supported\n
Failed to read transfer register (EDDTRTX)
CCOUNT
axlog_assert_upcall
SETTHREAD
KICKINFO
index < rangeCount_
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s} exec: DC_CVAC_X1_ENC\n
fn._ocd_reg_w.ddr.1
{%s} hostname:%s, flags:0x%08x
%02d:%02d:%02d:%06ld|%s <%s> %s
set.astris_version
code
cpu-name
wir2-tdo
MCORE
ret.check.offset_for_content
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
par_el1
hwbp_enable
BR
M7
ret.storePairForPref
EXPLORE_DAPONLY
R5
_reg_desc_lookup_by_index
reg.ocd.dsr.invalid.not_cleared
KIS Timeout
PoodleSWD
[KIS] CMD: %s \n
AXbooster_interface_create_cpu
{%s} Extracted CIP Gen Number from table  (%d)
LPC1785
Successfully connected to
Unknown error.
soc-revisions
ASC_TCORE_ROM
disable
Breakpoint Size: %d
{%s} asc status=%d being reported as Unknown
LITBASE
reg_name (\"%s\") not implemented, missing Xtensa option.
ParseFalse
BoosterManager.CPU
Initial DSPSR_EL0: 0x%llx
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
R9
Error %d (%s) while expanding ~ for Astris log file base\n
cpu_writereg_vals
Misc register 1
L1C
{%s::%s@%d} [FALSE] gpr[%d] < GPR_COUNT\n
{%s::%s} [%s] !bpwp_initted, retrying init
Blocked
kisHubLoc
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, %d, %d, true, %d)\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} L2 cache operation completed [%s]
fn._ocd_exec_instr.wsr.ddr.t1
[AstrisAsync] Pause when already paused!\n
fn._read_special_reg.icountlevel
Astris
Low level
ASTRIS_ERR_FAILURE
Idle
AXconn_port
META
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
Primate-Hub-Null
Base::level_stack_.template Top<typename Base::Level>()->inArray
socs_supported
BT_MAC
_is_halted
DESIGNER_ARM
High level 2 exception PC
(Last: %s) (%s)
{%s} drain_packets=%d [%s]
_a64cpu_clear_async
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
unable to read memory (permission checks suspended)
ret.spmi_read
fn._ocd_reg_w.regval
:usb
maxDecimalPlaces >= 1
JAM
get
DISPSEC
ret.restoring_el_after_raising_to_read_hcr.raise_to_min
virtual int ARM7cpu_t::_resume_hw(bool)
## armcpu: bad status even though all bytes read (%d)\n
\tAligned Read Failed
Memory error virtual addr register
WARNING
astris_get_die_count
CPU has no regions, maybe powered off?\n
DCS_BC4
failed to write memory
L2
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_armdap.cpp
write_reponse_and_check_authentication
PROBED_SLEEPING
_get_wpaddr_hw
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
ConsistDbg
%s/%s%s.bin
ASTRIS_ERR_NODATA
Missing a closing quotation mark in string.
{%s:%s@%d} [%s] moving DBGDTRTX to GPR 0\n
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
astris_ide_get_dbgwrap_base
!!!! Critical Error:  dspsr_el0 NOT CACHED !!!!\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
EXPLORE_ONE_DIE
fn._ocd_reg_r.DSR
fn._ocd_reg_r.dsr.2
ASTRIS_ERR_NOTOPEN
CPU state %d
write to CMD/STAT failed - %s
General register 11
fn._insert_data_breakpoint
Die Addr Info LSB: %d Mask: 0x%016llX\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
R8
result.read_vals==
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
%s status transitioned: %d ('%s') -> %d ('%s')\n
SOC AP[%d]: JTAG_AP\n
{%s} Component ID read fail for 0x%llx (%s)
WRBUF
load_framework
Data break 1 control
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
fn._ocd_exec_instr.rsr.ddr.addr_reg
ASTRIS_ERR_IFSTATE
Toto
Logger output is null
!hasRoot_
virtual int ARMv7cpu_t::_halt_hw()
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
LPC1777
index < data_.a.size
%Y-%m-%dT%H:%M:%S
_write_memory_fast_try
GetStringLength
internal.is_probe_authenticated.chip == NULL
DBREAKA1
RF5
Created Connection - : %s
port_%d
cpu_cache_info_group0
{%s} category=%d
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm7cpu.cpp
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
{%s} _pre_resume_hw result = %s
{%s} FAILURE - malloc error
j1500i2
DISPDFR
New format for cip gen register, unsupported: %d\n
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
GetUint64
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
ret.drain.full-duplex
ASTRIS_ERR_OUTOFMEMORY
entry.exception_test_2
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
[Auth Debug] Ticket Active, Debug Interface Locked\n
LPC11U67
RESPONSE_CMD
param.is_present == NULL
SoC must have a DAP
fn.exit ERROR
!!!! Critical Error: ARM64-specific _sstep method not currently supported !!!!\n
ret._setup_wp
We Are Matching Development Booster\n
Stop Clock: %s\n
   Debug Port: SELECT %X: SKIPPING\n
address=0x%8.8X
Missing a name for object member.
n >= 0 && n <= 308
ISP
virtual int ARMv6cpu_t::_resume_hw(bool)
astris_user_default_remove_all_boardnames
0123456789abcdef
{%s} Failed to extract portal info from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
ERROR: nothing to do; resuming address translation for %s without previously suspending it
fn._read_special_reg.dbreaka0
default
Schema validation failed
Explore
Probe Type (%d) FW Version: %s does not support KIS.
unknown
param.conn.enable_explorer == NULL
PORTAL UNAVAILABLE
AMAuthInstallSupportDictionarySetBoolean
Table 5–177
EPS2
ERROR!! write binary data parameters invalid\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
%s (addr=0x%llx)
Increasing length by: %d\n
ACQ_SETUP
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_c_api.cpp
_write_general_reg
Could not find TAP at chip-index %d for v2 1500 config\n
Full JSON that failed validation:\n%s
astris_command_lock
_resume_translation_hw
AP Only Explore was asked for, stopping here
{%s:%s@%d} [%s] write cmd buffer failed: %s\n
Table 5–134
no device when sending request
DPAP
We are Allocating\n
Chip %x Status = %d\n
AXcpu_status_pmgr
\"%s\" not a special register
CS-CTI
{%s:%s@%d} [%s] reading WVR %d\n
Unable to disassemble_at_addr 0x%016llx
reset_connect_state
ACQ_SAMPLE_I2C
[AstrisAsync] Completing all async commands. Initial err = %d\n
hwwp_insert
astris_cpu_trampoline
m_loaded_framework == NULL
Error %d(%s) executing instruction 0x%08X FAST
spmi
CPU AP-Type: %d\n
channel-%s
copyBoardNameForKey
token.IsUint64()
result.extract_version==
[AstrisAsync] Resume when not paused!\n
{%s=>%s} AXconn_t has no SoC object
Too many data breakpoint regs (%u). Maximum is 2.
fn._collect_snr.pc
value
address-size
{%s:%s@%d} [%s] reading WCR %d\n
Invalid current AP (%d), adopting APTABLE (%d)
AXcpu_translate_par
internal.clear_probe_auth.chip->soc == NULL
/System/Library/PrivateFrameworks/MobileDevice.framework
CPU Die: %d\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
invalid command
GenericStringRef
set.probe_name
[READ] %d -> 0x%08x\n
enable_timer_ovr
Data break 0 control
Unspecific syntax error.
cpu-armv7m-dmem-size
KF-ETM
\t\tARMv6 debug CPU xxx ID\n
astris_jtag_scan_gotorti_impl
enable_test
op=%d
CPU3
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis.cpp
{%s:%s@%d} [%s] reading DTRTX\n
ret.read.stepping_stone
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
{%s} bridge timed out
AXbooster_interface_cleanup_astris_api
dart-apf-address
Connected to Probe Device Server [Log File %s]
cpu_status
[1500] Error parsing bridge: %s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm64cpu.cpp
Need to be connected to set nickname
{%s::%s} [%s] error (%s) getting number of HW BPs
astris_cpu_mmu_get_config
Error occured during nonce command (v.5)
FAULT
New
fn.ocd.debugcause.di.incorrect
No connection attempt description
unable to obtain sysap
wir-size
!!!! Critical Error: SYSREG TARGET_EL[%d] > CURRENT_EL[%d] !!!!\n
{%s} exec: DC_CSW_X1_ENC\n
CPU.ARMv7m%s
   Debug Base: %08X\n
astris_memap_bus_read
OK
[DCC] Grabbing DTR failed: %s\n\n
{%s:%s@%d} [%s] scanning out (DIDR)\n
Table 5–176
fn._read_special_reg.srn.regval
op_S8I_encode
HIDBridgeSWD
Could Not Create Dictionary From Booster: %s
Highest EL: %d, -- Min Op EL: %d
Table 5–154
psr-partition-number
ret.generate_nonce_and_send_request
_read_cpu_reg_file_all
Skipped due to error in Async batch
quit
Incorrect hex digit after \\u escape in string.
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
OCLA_IP_REGS
sib-network-wrstn-reset
Channel configuration missing
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
internal.is_authenticated.chip == NULL
astris
Error
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
elr_el3
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} Failed to get watchpoint mask for %s: %s
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
.success
.user
b
!!!! Critical Error: MIN_EL(sysreg)[%d] <= m_exception_level[%d] !!!!\n
ret.storeNicknameForKey
sso_user.sso_data_length == 0
General register 2
Register file 58
fn._read_special_reg.ibreaka0
Creating CPU Returned: %s\n
Table 5–165
ARMV6M
Chip identification failed
Malloc
MemoryBlock_t
GFX
HENRY
CLIDR
op0: %d op1: %d CRn: %d CRm: %d op2: %d el: %d
checking if relay \"%s\" is valid
cpu_flush_icache
TargetSel Before Disable: 0x%x
check_dcc
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armcpu.cpp
param.regval.null
ASTRIS_ERR_INVAL
{%s} Failed to get breakpoint count for %s: %s
fn._ocd_reg_dsr_w.dsr_status_to_clear
Value is null
true
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
consistent debug root reg undef
KIS Readvals putting back the value
1500 IR Commands:
%s given a NULL conn object
KIS-HUB-NULL
SOC_t
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
Efficient-Core
astris_exc_bread_test_1
{%s:%s@%d} [%s] executing LDRBpi(1,0,1)\n
failed to read memory; can't confirm breakpoint set
Register file 55
ASTRIS_ERR_NOPORTAL
Error %s opening single_port connection to probe server
DCS12
EDRCR
EL2t
wb_u32=%u
SoC BM Not Found, Bailing\n
xtensa-non-tie-range-name
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
addr_reg=%u,page_id=%u,opcode=0x%6.6X
Matched via Bundle ID\n
CFG
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_explore.cpp
astris_batch_attitude_lose
{%s:%s@%d} [%s] reading BVR %d\n
read-back (sys AP) failed
defaults.create.key.outofmem
   {%s} APB/AXI address for target setup = 0x%llx\n
Topology
Failed to restore EL to %d after reading register: 0x%llx
Absent
AXcpu_translate
Cant find Debug Auth Registers. Auth not supported
bad parameter(s) specified
Failed to init booster
AMCP3
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
Register file 6
ASTRIS_ERR_USB_PROBED
FPB
Off
DTLBCFG
{%s:%s@%d} Critical error encountered:
EPIREAD
AXcpu_translate_with_dart
load_framework_at_path
GETRELAY
appendToArray
NRF
Dart Base Address: 0x%llX\n
AXcpu_resume_translation
authenticate_dft
Cause of last exception
name=\"%s\")
JTAGONLY
Found match - bypass_device: %s; channel: %d\n
hwbp_disable
LPC1774
address=0x%8.8X, regval=0x%8.8X
connection about to be destroyed
%s constructed
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
EPS3
fn._remove_instr_breakpoint.which_bp
TRANSLATION_ERR_L1
OPEN
_ocd_reg_r
result.read_vals(table_info)==
Found probe memory transfer in progress; clearing EDSCR.MA.\n
_a64cpu_read_aarch64_sp_hw
ban
src_gpr <= 15
astris_cpu_mmu_configure
fn._write_special_reg.ibreakenable
PROBED_USB_REQ_EMPTY
setCategoryValue: path='%.*s'
Values Not The Type We Expected. Expected: Number and String\n
_a64cpu_lower_el_hw
internal.get-timer-count.chip->soc == NULL
fn._ocd_exec_instr.wsr.ddr.r0_r12
logger is NULL
Debug Clock Already Enabled
astris_explore_enabler_add_cpu
ASYNC
: [
fn._ocd_reg_r.dsr.1
Error %s connecting to probe server
DoCopyMembers
Failed to exec MSR to move scratch containing sysreg to MDDTR.scratch=%d, sysreg=0x%X, regname=%s
port
error %s reading DAP PFR1
Failed to write register: 0x%llx val: 0x%llx
fc_ite_checks=%d
MESR
APPLE_SUBTYPE_UNKNOWN
Skipping CPU %s at 0x%llx: not present in IDE\n
{%s:%s@%d} [%s] DEMCR read failed: %s\n
revive
We are in clean up\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
Can't get hardware model - failed to create string
Unaligned Read @ 0x%llx Width: %d Bytes: %d
Coproc, enable bits
dropping empty probeInfo (port=%u)
REG
MAP_CMD
{%s} FIFO full, try again
DCS15
result.read.portal.s2r_fsm
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
result.read_vals(version)==
\nPKA Command Verify Timed Out\n
cpu-dbgwrap-debug
astris_ide_explore_release
set.wp.len = not supported
_invalidate_icache_all
## memapw %u 0x%016llX 0x%08X\n
Portal Status, Changing STATUS and CMD/STAT to reflect
Failed to open schema file
{%s->%s} TGE is set, can't go lower to EL1
MEM1500
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Imago
ASTRIS_ERR_USB_NOTOPEN
info-probemap
getOrCreateValue
batch_cmd_count: %d
ELR_EL3
{%s::%s} creating placeholder for CPU: name=%s
AlignBuffer
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
SSTEP
Multi target booster, checking for %s.plist\n
JTAGPORT
pointer.IsValid()
{%s} %s DC cache clean complete, marking as clean
The log file has been updated with all available diagnostics.\n
%s/%s
can't find bid in response\n
BADCODE
diyfp.h
Table 5–185
RF7
parameter val is NULL
Enabling USB Gateway
ADI
{%s:%s@%d} [%s] executing MCRR\n
{%s:%s@%d} [%s] second read of CMDSTAT failed\n
RF55
interface not in appropriate state for action
connecting to probe by port number
KIS-SIM
CHIPCNT
Device name is required
astris_convert_addr_to_die
{%s:%s@%d} [%s] executing MRRC\n
LPC1766
ACQ_SAMPLE_SPI
In Readflash\n
mmu_init
L3
RF12
Invalid num_regs = %u. Should be 16, 32, or 64.
host_get_probematch
failed to read consistent debug root register, fabric may be hung
addMember.user
DISP_L
astris_apread
{%s:%s@%d} Critical error [radar already requested]
Complex CPM Offset: 0x%llX\n
CPU.ARMv6
Register file 47
general error reported by probe
to
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
CurrentContext().valueSchema
GenericRegexSearch
(crm & ~ARM64_HINT_CRM_MAX) == 0
armv7m-region-name
Failed to raise EL to %d to read register: 0x%llx
!!!! Critical Error: Restoring from exception level[%d] other than 1,2 or 3 !!!!\n
stdout
--> wrstn_wir2 size=%3d dpcsoc=%d
_a64cpu_write_gpr_cached
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
    INFO(%u,%d): %s(%04u): %s(): %s
low word
Exception virtual address
param.val.invalid.>max
2.34.0
CHAINERR
Connect using RSD not supported\n
Failed To Instantiate SOC From Booster\n
{%s} Failed to extract component info from table (%d); continuing anyway
(system_reg & (0x40000000 | 0x80000000)) != 0
internal.enable-timer-ovr.chip == NULL
High level 4 exception PS
cpu_lacc_count_insert
default_schema_version is NULL
BoosterManager.Utility
error %s reading DAP MPIDR
Lost
PKA Command Verify Completed, No Errors, but Probe Valid Not Set
Table 5–162
fn._read_mem
read-back (sys AP) did not contain SW BP instruction
CSSELR
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
ASTRIS_ERR_TGTSTATE
connecting to selected probe (user-specified single_port)
is.Peek() == 't'
%s:%s
Groups %d\n
{%s:%s@%d} [%s] handling pending async aborts\n
internal.is_probe_authenticated.debug_auth == NULL
duration_ms
--> localwrstn size=%3d debug=%d
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
astris_memap_debug_readbuf
AXdebug_auth_enable_test
Clear requests in INTERRUPT
MAC16 Data register 1
astris_explore_enabler_get_cpu_status
ret.cfg.read.swd
ret.read.edscr.ma-mode
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
is_external_open
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
COMPARE1
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Subsystem Monitor[%i]: %s\n
{%s} unable to allocate probeInfo
GitHashDebug
[1500] %s step %d: unknown instruction '%s'
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
unable to transfer command to/from remote probe
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
=== Detailed %s Boosters ===\n
L1CRT
ret.write_reponse_and_check_authentication
_read_cpu_reg_file
addr_reg=%u,page_id=%u,data_reg=%u,opcode=0x%6.6X
cpu_translate_with_dart
AXcpu_lacc_pc_status
Dumping Process Tree
ASTRIS_ERR_BADPARAM
{%s} Found extra info in = %s, chopping string
{%s:%s@%d} [%s] writing DSCR\n
[%s] {%s->%s} END handling exception
AXcpu_read_dcc
Memory error status register
Warn
_log_setup_thread_specific
  Nested path: parent='%s', child='%s'
...
{%s} unaligned %d-byte access at address 0x%09llx
_a64cpu_write_aarch64_sp_hw
AXconn_copy_nickname
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
write.dspsr_el0 NOT CACHED
{%s} Unable to read CPSR
%s %s:l=%u,c=0x%X,i=0x%X,f=0x%X
.name
 
(addr=0x%llx)
MAC16 data register 1
fn._ocd_exec_instr.rfdd
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s:%s@%d} [%s] moving reg to cop\n
INTDIS
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
SAR
fn._write_special_reg.dbreakc0
Setting STOP CLOCK to TRUE
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
esr_el3
Requested Register Requires EL: %d - Highest EL: %d
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT || == SP\n
clear_probe_authentication
AXdebug_auth_is_authenticated
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
param.bundle_url==NULL
{%s:%s@%d} [%s] setting GPR 1 (todo 2)\n
FAR_EL1
AXmemap_read64(desc) failed
_cleanup_hw
param.reg_name.!match
UserCreated
[%s] Executing instruction=%llx
Variables not setup
Register file 36
.json
SoftwareBreak
{%s=>%s} AXconn_t has more than one chip
Awaiting next chunk of big response
{%s@%d} Drain empty on decr [%s].
fn.missing_entry_function
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
[READ] cop64 %d -> 0x%016llx\n
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
UNKNOWN_CODE
[AstrisAsync] Async mode %s
{%s} Exploring with option: %s\n
fn.__ocd_reg_w.ddr
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
var.reg_srn.invalid.>=256
=== Starting Gather and Clear ===
')
{astris_probed_print_events} not supported in this build configuration
{%s->%s} exec: aarch64_add_imm(scratch=%d, REG_SP)\n
_write_executable_memory
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
Call-window start bits
Spew change. old=0x%016llX, new=0x%016X
Timeout occurred while connecting to
applesoc == nullptr
SCODEC
write_register
LPC1767
High level 5 exception PC
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
alloc_drain_payload
AX1500_listbridges
Dock-Channels
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
%s - runBlock
read memory
astris_jtag_get_pipe_cycles
{%s:%s@%d} [%s] load blx inst failed: %s\n
RF39
KIS Writevals putting back the value
armv7m-region-base-address
ECID is 0\n
Only Auth-Debug, Auth-DFT and Probe-Auth are currently supported.\n
ASTRIS_ERR_NOTEXPLORED
%d.%drelease
RF6
config.invalid.no_window_reg_option
USB connection not currently open
Probe %s Device Not Connected on USB-C Port
ret.clear_all_breadcrumbs
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
NXP
Invalid width = %d bits.  Must be 8, 16, or 32.
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
!!!! Critical Error: exception other than an abort (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
get_page_shift
Exploring IDE in JTAG\n
Connected toProbe Map Server (single_port) 
--> extrawrstn %d
{%s::%s} read OK but took %d tries
_a64cpu_assert_rw_matches_hw
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
TARGETSEL
No probes were found matching
setTargetInfo
addTimingPhase
transact
Could not find bundle () in given array: %s\n
[1500] Error parsing v2 bridges
jtag_get_soc
ret.clear_authentication
RF34
Failed calling AppleSOC_t::dock_disconnect_mode\n
[%s] {%s->%s} clear async abort
_a64cpu_encode_mrs
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp
%s %s\n
!!!! FILE RADAR: Don't know how to compare two values\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
Register file 42
!*!*!* Lightning header facing up.                                                    !*!*!*
cpu_cache_clean
EvalQuantifier
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
%s.%s.%s
stat
==== Exception Trace ====\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
astris_get_async_ver failed with error: %s
MR1
cpu_lacc_count_read
m_regstate.a64r_dspsr_el0
{%s::%s} [%s] MMU is already active - returning %s
_write_window_base
read_resp_cmd_via_sock
cpu_getinfo
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
gmtime() returned NULL, using epoch time
copyNicknameForKey
param.ar.invalid.>15
token.GetUint64() <= SizeType(~0)
AX1500_transact
Debug Base: 0x%llX\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
_set_wpaddr_hw
CPU[%s] Write Reg: %d Val: 0x%llx
Invalid value.
typehint
param.tgt->ap->dp->chip.null
EXPLORE_GENTLY
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
UNKNOWN 
cpu-dbgwrap-status
{%s:%s@%d} el[%d] == m_exception_level[%d]\n
[INS_WP] 0x%016llx x %d\n
Memory map ID
{%s} probe_host = %s
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
setTargetIdentifiers
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
cpu-apselect
Raising to EL2 cause in Guest\n
param.conn.connected == false
AXmemap_read_get_field
{%s} Error setting up memap target (%s)
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
cpu-ascdebug-dbgack
setup_transaction_objects
AXcpu_hwbp_insert
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
ASTRIS_ERR_ISCONN
AXconn_connect_kext
Category is null
{%s::%s} HDE not set on %s. Will re-enable.
astris_user_default_remove_all_nicknames
Wake
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
memory_write
translate_par_with_stage
   Debug Port: SELECT %X; error: %s, retrying..\n
AuthDebugUseSSO
DebugAuth
op_XSR_encode
Invalid escape character in string.
group=%d
RF49
fn._read_special_reg.dbreakc1
connecting to Ethernet probe
Error while trying to disassemble memory
{%s} connectName[local host]
GEN
## dpr 0x%02X failed (%s)\n
fn._read_special_reg
ASTRIS_ERR_DISASM
Kicking
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
fn._ocd_exec_instr.rsr.ddr.t1.2
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
CPU %s not found or already removed from the map
{%s:%s@%d} [%s] writing PAR[64]\n
{%s:%s@%d} [%s] going to RTI\n
SPSR_EL1
astris_remove_loaded_soc_boosters
virtual int CPU_t::collect(int)
internal.clear-auth.debut_auth == NULL
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
APCIE
UPDATE cop64 %d -> 0x%016llx\n
{%s:%s@%d} [%s] reading CCSIDR[L2]\n
%-16s
Failed to convert CFArray to C Array\n
Error reading thingy
_clean_dcache_vaddr
localhost
EXPLORE_IDENTIFY_ONLY
LPC11U37
RF4
wb
{%s} unable to find single_port probedaemon on port %d
Table 5–172
RF30
param.info.invalid.null
_ocd_reg_dsr_clear_and_validate
remote probe closed connection
probe matching %s on localhost
astris_server_send
from != 0
Got an error reading the DCM Control Register: %s
@rpath/%s.framework/%s
AXjtag_setclr
length=%u, width=%d
ProductBuildVersion
Table 5–152
(%s)
wait_inflight_auth
LPC1752
{%s[recv]} %d(%s) [RETRYING]
SCANDEBUG
cpu_lacc_pc_status
Pow10
Table 5–161
Register file 31
{%s}#%02X %s [%s]
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
read back of modified data did not match
EXPLORE_WITH_SISP
X09 Part
read back  0x%08X @ 0x%08llx\n
PROBED_LOSTCONN
{%s@%d} socket connection is not available
Die Config Disabled\n
high
Unable to restore EL0
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
{%s} Unrecognized Component: %08X (class %u)
astris_memap_masked_read
Interrupt request bits
{%s} %s
ret.relay.get.hostid
/swdflashers
product-name: %s\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
_write_memory_slow
internal.get-timer-count.debut_auth == NULL
Table 5–132
Misc register 2
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
unswitch_regset
LPC13
ChimpSWD
reset_dcm: %s
L1_DATA
AuthDebug_t::init failed (AuthDebugWithTimer_t)
DBREAKC1
RF8
{%s@%d} gethostbyname failed, error=%d (%s)
dest_gpr < 32
AXcpu_writemem_width
fn._read_snr.exccause
Info_
Debug-Components
Failed to write SPS_EL%d
{%s} Error looking up architecture (%s)
{%s:%s@%d} [%s] write to CMD/STAT failed\n
%s/Library/Logs/Astris
.start_time
SWDFlasher.NXP
Complex ID: %d\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[%s] error reading EDSCR
   JTAG-AP: Identification = %08X\n
astris_cfg_memap
LPC11U14
INTENABLE
dr ->
AXbooster_get_all_boostermanagers
DCS_BC1
CPU Monitor[%i]: %s\n
Register file 34
fn._ocd_exec_instr.rsr.ddr.t1.1
{%s} %s: |%s|-|%s|
astris_json_logger_delete_all
Required Key-Value is a string, and not an array. Old booster found: %s\n
extra-wrstn
process_bypass_device
{%s:%s@%d} [%s] writing DTRRX\n
{%s::%s@%d} [FALSE] instr[0x%08X] & MSR_MRS_BASE_MASK == 0\n
{%s::%s} timeout while waiting for EDSCR ITE
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
fn._tie_read_word32.last
astris_ide_print_platform_info
PARTNO_JTAGDP
MEVADDR
kisLoc
FPI2C
file_type
dest_reg < 32 || dest_reg == 31
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
_write_cpu_reg_file
%s.console
no data when data expected
{%s} %s did not match any valid host
message
type == kStringType
{%s} connectName[%s]
{%s:%s@%d} [%s] writing DTRRX(first)\n
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
_a64cpu_reset_catch
%s status is '%s'\n
ret.reg.read.K_DA_REG_NAME_PKA_BASE_LO
param.reg_name.invalid
, 
Invalid content key, %d
{%s:%s@%d} [%s] executing STCpi\n
pc:  0x%16s cpsr: 0x%16s %s\n
Register file 27
_init_registers
Error:ASTRIS_ERR_BADPARAM(-29)
{%s} probe device server closed the connection while trying to read data (at recv)
hwwp_remove
{%s} %s status failed. error: %d (%s)
Processor Id
AXconn_conndesc
Probe %s with unknown port response %s
15002SPR
{%s:%s@%d} [%s] getting GPR\n
[COLLECT] Chip %x\n
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
BoosterManager.SWDFlash
DBGWRAP_LITE
One time initialization of oslog API failed!\n
relay_set: %s = CMD_ERR (%s)
{%s:%s@%d} [%s] setting GPR 0\n
{%s:%s@%d} [%s] executing MSR (switched)\n
failed write of 0x%08X to DEMCR - %s
AuthDbg,BoardID
Register file 49
param.invalid.reg_file_index.outofrange
fn._ocd_exec_instr.rsr.ddr.data_reg
_get_num_hwwp_hw
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
ApProductionMode
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
ret.reg.write.K_DA_REG_NAME_NONCE_0
MISC3
Portal Config Read
got a fatal error translating VA to PA
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
OCD.DEBUGCAUSE = 0x%8.8X
{%s:%s@%d} [%s] unable to read command response\n
x != 0
LPC1111
EPIWRITE
complex-id
(src_gpr & (0x40000000 | 0x80000000)) == 0
{%s::%s@%d} [FALSE] dest_reg[%d] < 15\n
createKeyWithPrimate
PARTNO_DAPLITE
read_memory_dbgwrap
OCD control register, set
Error %d (%s) opening history save file
AXdisassemble_at_addr
psr-size
[RESUME] Chip %x\n
Register file 14
CPU is not halted
empty USB packet encountered
response == NONE; failed to get kis target info\n
Miss fraction part in number.
Match Count is Zero. This is invalid.
ANE_SYS
Failed to populate portal info
MMID
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Encode
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
name
     0x%016llx: 0x%04x      %s\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
Table 5–174
Table 5–188
{%s:%s@%d} [%s] doing IR scan (DTRRX EXTEST)\n
{%s} [EDSCR_RXFULL !is_64] exec: encode_mrs(0, MDDTRRX_EL0, false)\n
AXcpu_hwwp_enable
param.reg_name.INVALID
%d.%dbeta%d
host %s with name matching %s
STATUS
ret.astris_set_user_die_select.astris_soc_get_applesoc
--> cmd        addrsize=%d datasize=%d
ret.read.gpr_0
[PREFS] Key: %s - Val: %s
plist
AXconn_create
clzll.h
PMU: 
sending request
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
Size
_read_memory_slow
[PREFS] Key: %s - Val: ??
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
{%s:%s@%d} [%s] doing JTAG scan\n
Setting WP length not currently supported: %u
fn._ocd_reg_w.dcrset.regval
address=0x%8.8X,value=0x%8.8X,page_id=%u
DBGWRAP_PAUTH
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
RF2
RF25
RF35
kob
probe matching %s on host %s
chip == NULL
[CACHEOP] %d, 0x%016llx, %d\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
?
EXCSAVE1
set.chip_id
preflash_type
DSPSR_EL0
{%s::%s@%d [%s]} Error %s: synchronizing context
AXcpu_swbp_remove
AXcpu_abandon
AP[%d]: unknown type\n
RF19
fn._ocd_reg_w.ddr
Protocol Version: 0x%X\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
AXJTAG_EXPLORE_SEP_NOPWRGATE
{%s:%s@%d} [%s] %s halt failed: %s\n
Could Not Allocate Loaded Booster Array
Could Not Find The Astris Init Function (%s) in %s
psr-bit
Failed to read ide_table from KIS explore
enabled
before_deactivate_in_runBlock
DESIGNER_ARMDAP
%s\n
astris_batch_attitude_destroy
fc_retries=%d
api.is_prod.debug_auth == NULL
fn._read_special_reg.reg_srn
fn._init_configuration.w2.audio.HIFI3_1
regidx_save=%u
_remove_data_breakpoint
Switch to primate res: %s\n
EXPLORE_WITH_AUDIO
MTP
MSP
param.halt_group == NULL
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s:%s@%d} [%s] doing IR scan\n
astris_cpu_status
op_L32I_encode
```
