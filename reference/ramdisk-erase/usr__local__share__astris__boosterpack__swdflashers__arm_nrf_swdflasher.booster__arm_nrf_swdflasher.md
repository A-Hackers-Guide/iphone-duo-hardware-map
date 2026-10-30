# `/usr/local/share/astris/boosterpack/swdflashers/arm_nrf_swdflasher.booster/arm_nrf_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,820,432 bytes.

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
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (6,972)

First 2,500 of 6,972.
```
[AstrisAsync] Got ASYNC_RESTART response!
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
   JTAG-AP: Identification = %08X\n
NRF54LFlasher: CTRL-AP ERASEALL failed\n
CPU Subsystem: %s\n
component group %d\n
Increasing length by: %d\n
Subsystem Monitor Key does not exists: %s\n
Probe %s removed before port determined\n
{%s} unable to allocate probe name
Gathered Info:\n%s
[1500] TAP %d missing required field 'chip-index' or 'irlen'
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
{%s} L2 cache operation completed [%s]
NRF53Flasher: timed-out waiting for NVMC ready\n
Breakpoint Index: %d
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
## apw %u 0x%08X 0x%08X ...(%d)\n
write to CMD/STAT failed - %s
Initializing Booster Layer\n
{%s->%s} ERROR=%d(%s)
[%s] {%s->%s} END handling exception
{%s} asc status=%d being reported as Unknown
%s construction failed
ERROR!! write binary data parameters invalid\n
NRFFlasher: performing flash to addr (0x%08llX) of len (%zu)\n
--> debug      size=%3d acsr=%d
Probe %s Device Does Not Have LocationID
{%s} connectName[%s]
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
Extract Offset: 0x%X for %d\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[ARM32cpu_t::_read_register64] 0x%08x\n
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} PRIMECELL [DONE]
NRFFlasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
Please answer y=yes or n=no.\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
NRF53Flasher: detected part code (0x%08X)\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Logging Context Is NULL\n
Die Config Disabled
%s NOT configured\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s} read %d words from probe when %d words requested
NRFFlasher: CTRL-AP ERASEALL attempt %d\n
NRF_Flasher_t: preflash: APPROTECT enabled: skipping quiesce(), cpuStatus() check\n
{%s} no matching 1500-to-* bridge
Exception %d Stack Trace
Initial DSPSR_EL0: 0x%llx
## memapw %u 0x%016llX 0x%08X\n
NRF54LFlasher: configured RRAMC config register with bits 8-13 set to all ones (0x%08X)\n
[KIS] Words (Read/Write/Wrote): %d\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
Awaiting next chunk of big response
Could Not Allocate All Boosters Array
[1500] Using %s.plist
[MEM] Aborted; DSCR = %08x\n
successfully updated DEMCR
{%s::%s} [%s] error (%s) getting number of HW WPs
[%s] AP, DP, or chip given is NULL
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
Setting STOP CLOCK to TRUE
DHCSR write failure - %s (%d)
There is no debug port associated with this chip\n
Gathered Value is Not Number\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
Async is disabled for localhost connection
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
NRF54LFlasher: setting RRAMC base to 0x%08llX for nRF54L20\n
[%s] %d -> 0x%08x\n
Creating NRF54LFlasher: Chip: ID(%d) PID(%d) flags(0x%08X)\n
Setting CPU %s is_boot_core to %d\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
VBAR: %#x\n
tckrate_check returned error %s
NRFFlasher: word-aligned length (%zu)\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
error %s reading DAP PFR1
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
{%s} collect result = %s
register lookup by name not supported when Astris is statically linked
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s::%s} timeout while waiting for EDSCR ITE
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
[AstrisAsync] Barrier before pause\n
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
NRFFlasher: checking APPROTECT status\n
Failed to create CPU %s - %s\n
Both debug and xbs versions are set, maybe a bug: %s
We Are Matching Development Booster\n
Unable to convert plist file name to CFString: %s\n
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} _pre_halt_hw result = %s
Init objects failed
--> master     size=%3d localwrstn=%d debug=%d
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
Dumping Process Tree
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
NRFFlasher: AHB-AP ERASE PAGES success\n
{%s@%d} Found cached response
NRF_Flasher_t: check APPROTECT failed\n
Protocol Version: 0x%X\n
{%s::%s} [%s] MMU is already active - returning %s
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
Unable to register assert upcall %s (Insufficient memory)
Asked To Write To A Negative Register Index
Portal Group Base: 0x%llX \n
{%s} category=%d
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
failed write of 0x%08X to DEMCR - %s
Async is disabled for current seesion
Failed to convert CFArray to C Array\n
sending abort to clear a timeout\n
==== Exception Trace ====\n
Stepping Stone Final =  %#x\n
[%s] E2H is set, virtualization is supported\n
collect_responses
[AstrisAsync] Pausing Async Mode\n
replay_counter=%lu, last_replay=%d
## dpw 0x%02X 0x%08X\n
{%s} FIFO full, try again
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
AP given is not a MEMAP
Can't get OS build version - failed to open ReadStream
{%s:%s@%d} Critical error encountered:
NRFFlasher: performing CTRL-AP ERASEALL\n
[KIS] Register Index: %llu\n
Could Not Create Dictionary From Booster: %s
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
CPU Monitor[%i]: %s\n
[PREFS] Key: %s - Val: %s
--> localwrstn size=%3d debug=%d
    %s(): %s
[%s] %d -> %08x\n
NRF53Flasher: flash success\n
      Read of JTAG-AP port %u PSTA failed with %s\n
Request Dict:\n%s
Too many portals, we are at portal: %d while max is %d\n
NRF53Flasher: verify success\n
probing %s status\n
   Debug base is in legacy format\n
Unable to create pthread key for conenction. errno=%d %s.
Debug Clock Already Enabled
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
NRF53Flasher: failed to aquire Debug port\n
{%s} Failed to get breakpoint count for %s: %s
Successfully Authenticated DFT\n
Xtensa Option dbg_intr_level: %d
=== Starting Gather and Clear ===
Koko probe, for now I guess we will just say yes...\n
Invalid current AP (%d), adopting APTABLE (%d)
NRF53Flasher: word-aligned length (%zu)\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
      Select of JTAG-AP port %u failed with %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
AXjtag_srst assert failure - %s (%d)
CPU Typehint: %s\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
Breakpoint Size: %d
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
{%s::%s} creating AP slave: name=%s
{%s} Failed to extract CID from table (%d); continuing anyway
{%s::%s} cpu powered off: failed init() %s
Failed to create optional file. Not fatal, moving on
Invalid character [0x%02X] received from Probe Map Server
Probe %s removed prior to kick\n
Got an error reading the DCM Control Register: %s
{%s} pmgr status=%d being reported as Unknown
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
{%s} setting up nameless target (address=0x%llx)
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
{%s} bridge returned SLVERR
%s Bridge @ 0x%09llx-0x%09llx: %s
Can't get OS build version - failed to create plist
Probe %s status: Idle
Probe %s USB-C location is %s
comparing against match entry [pid] %d: %s\n
CPU Core Number: %i\n
max_scan_bits is low: %d
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
AuthDebugWithTimer_t destructor \n
Previously dumped the process tree, skipping
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
choice: %d\n
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
Failed to read IDE through DAP\n
Failed explore before forced KIS reset: %s\n
{%s} error %d(%s) reading data from the connection (at recv)
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
AXmemap_readvals failure - %s
{%s::%s} EDSCR with RXO set - unable to recover.\n
Hang Description:\n%s\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
[READ] cop %d -> 0x%08x\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
Could Not Find Any Boosters of Type: %s\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
{%s} %s DC cache clean complete, marking as clean
NRF53Flasher: comparing last partial %lu byte word\n
X09 Part
%s %3d'b%s\n
%s\n
[1500] v2 plist missing required field 'bridges'
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
[AsyncSnapshot] #%zu: %s\n
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
{%s} host:%s, flags:0x%08x
{%s} probe_host = %s
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Found form-factor specific channel %u for device '%s'
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
Error status from AMAuthInstallSetSigningServerURLPtr = %i
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Enabling USB Gateway
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
[AstrisAsync] Activate while async is already active!\n
Exploring IDE in JTAG\n
%s [RETRYING]
{%s} %d(%s) [RETRYING]
CPU state %d
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
[AstrisAsync] Complete Queue callback returned %d (%s)\n
Setting bypass channel to: %d\n
!!!! Complex Key %s is INVALID !!!!\n
Debug Base: 0x%llX\n
Board ID: 0x%X\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s} Unrecognized component: %08X, class %02X\n
NRFFlasher: wrote %zu bytes\n
{%s} %s did not match any valid host
\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
New Length: %d\n
NRFFlasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
NRF54LFlasher: checking APPROTECT status\n
comparing against match entry %d: %s
getOrCreateValue: addMember failed, returning doc root
Complex ID: %d\n
Error returned from explore_pid
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
## memapw %u 0x%016llX 0x%08X ...(%d)\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
{%s::%s@%d [%s]} Error %s: collecting HW
[COLLECT] Chip %x\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
Connected to Probe Device Server [Log File %s]
{%s@%d} Unknown CS command error [%d]
Could not find TAP at index %d to attach 1500 bridge to\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Failed To Instantiate SOC From Booster\n
Could Not Find Any Loaded Boosters of Type: %s\n
{%s::%s} [%s] error %s from _synchronize_context.
Translate Stage Chosen: %d\n
codeblock
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
SoC not identified by IDCODE - enumerating instead of instantiating
Going to do imago workaround\n
{%s@%d} Failed to find cached response
NRF_Flasher_t: performing readflash from addr(0x%08llX) of len (%u)\n
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
\tLeft Over Chunk Read Failed\n
   {%s} Clearing HNONSEC on AP \n
{%s=>%s} null reference to AXchip_t[0]
[%s] Booster System Is Not Initialized Bailing\n
Cannot create SoC [unknown chip identity (%d)]
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
[1500] Error parsing bridge '%s': missing required field 'tap'
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
   {%s} Read AP's R_MEMAP_CSW\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Xtensa Option non_tie_ranges: %zu range(s)
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
\tAligned Read Failed
NRF_Flasher_t: cannot writeflash: APPROTECT is enabled\n
NRF_Flasher_t: performing preflash\n
TAP IDCODE: 0x%X\n
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
   Debug Port: Trying SELECT %X\n
{%s} match any probe [localhost]
SoC must have a DAP
Failed to allocate space for table!
[CACHEOP] %d, 0x%016llx, %d\n
Connecting to server, %s:%d
=== Found %s Boosters ===\n
[HALT] Chip %x\n
[AstrisAsync] Async mode %s
   Created Fake Debug Port Debug Port
Can't get OS build version - failed to get build version
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_54\n
{%s} Found extra info in = %s, chopping string
--> extrawrstn %d
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
Not Creating CPU: %s\n
[1500] run_steps: unknown instruction '%s'
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
{%s} calling _collect_hw on %s
## memapr %u 0x%016llX -> 0x%08X\n
X12 Part
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
We are in clean up\n
Successfully connected to server, %s:%d
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
There is no debug port associated with this chip.
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
Error %d(%s) executing instruction 0x%08X
{%s} Unrecognized Component: %08X (class %u)
{%s} Error %d(%s) sending message
--> cmd        addrsize=%d datasize=%d
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
   {%s} Enabling debug unit\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
NRFFlasher: detected part code (0x%08X)\n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
--> 0x%02x = %s
[AstrisAsync] Pause when already paused!\n
\t[MATCH_TARGETID] FAIL <= unable to find DP
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
{%s::%s@%d [%s]} Error %s: resuming HW
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
{%s} Failed to get watchpoint count for %s: %s
{%s} handle ROM entry %d (level %u): %08x
The log file has been updated with all available diagnostics.\n
NRF53Flasher: timed-out waiting for CTRL-AP ready\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
Error while trying to authorize: %d - %s\n
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
%2d) %s %s%s\n
\t[MATCH_FOUND] identified chip: %s
Taking gateway control failed
NRF_Flasher_t: preflash failed: NULL connection param\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
NRFFlasher: comparing last partial %lu byte word\n
KIS translator version : %d\n
Dart Base Address: 0x%llX\n
{%s} Failed to extract portal info from table (%d); continuing anyway
[%s] {%s->%s} clear async abort
Highest EL: %d, -- Min Op EL: %d
Error status from AMAuthInstallSsoEnablePtr = %i
!*!*!* Lightning header facing up.                                                    !*!*!*
Probe %s with unknown port response %s
KIS Writevals putting back the value
Failed To Initialize Logging\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
AP[%d]: MEM_AP_APB\n
{%s=>%s} null reference to AXconn_t record, `conn`
OS build version: %s
{%s[select]} %d(%s) [RETRYING]
NRF_Flasher_t: cpuStatus failed\n
Could Not Match A Booster for %s\n
coalesced-target: %s\n
error %s reading DAP MMFR0
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
{%s} already collected %s, skipping
   --> IDR: %08X\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
Target ID: 0x%X\n
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s} Failed to get breakpoint mask for %s: %s
NRFFlasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
Spew change. old=0x%016llX, new=0x%016X
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
no system bus AP present with AHB, trying AHB5
start rev and/or end rev is NULL; skipping cpu_desc override\n
Failed to get KIS translator version\n
Die Config Disabled\n
{%s} Error setting up jtag-ap target (%s)
   ROM entry %d (level %u): AVOIDED\n
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
NRF54LFlasher: word-aligned length (%zu)\n
Generated JSON (first 500 chars):\n%.500s%s
[MEM] Uncompleted; DSCR = %08x\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
Raising to EL2 cause in Guest\n
%s: []\n
response == NONE; failed to get kis target info\n
NRF_Flasher_t: unable to obtain sysap\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
{%s} probeList has probeCount of zero
Full JSON that failed validation:\n%s
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
Caught a portal that we dont have a status map for: %d
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
Problematic JSON value:\n%s
{%s} Failed to extract chip debug base from table (%d); continuing anyway
{%s} %s resumed\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
{%s@%d} Connection to server failed, error=%d (%s)
{%s} restored el is now %d
[AsyncSnapshot] No snapshots collected\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
      Select port %u: AVOIDED\n
Banana split probe, for now I guess we will just say yes...\n
{%s::%s} [%s] unsupported width %d
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
   {%s} Before powerup CMDSTAT=%08X\n
{%s} explore with exploreflags 0x%X completed with error [%s]
{%s} no response from bridge
Stop Clock: %s\n
Failed to aquire Debug port.\n
replay_counter=%lu
Fabric access is blocked. Expected if production unit, won't explore further.
Connected to Probe Map Server
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Kick has been requested by probe server
CPU AP-Type: %d\n
!!!! DART Key %s is INVALID !!!!\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
NRF54LFlasher: detected part code (0x%08X)\n
JsonLogger: Creating new category '%.*s'
In Preflash\n
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s=>%s} no soc reference; falling back to direct cpu method
X00 Part
NRFFlasher: writing partial %lu byte last word\n
Table Size: %d\n
{%s} Failed to extract ECID from table (%d); continuing anyway
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
{%s::%s} HDE not set on %s. Will re-enable.
[Auth Debug] Ticket Active, Debug Interface Locked\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
After powerup CMDSTAT=%08X\n
NRF53Flasher: performing flash to addr (0x%08llX) of len (%zu)\n
dbgwrap halt failed, falling back to classic method
{%s} Failed to get watchpoint mask for %s: %s
Explore: %u chip%s\n
no debug bus AP present when expected
No 1500 bridges or TAPs specified (v2 plist)\n
Required key: %s @ index %d is NULL\n
Invalid SoC Booster. SoC Booster Requires PID\n
   Debug Port has unknown type\n
Gateway is KIS, seeing what probe this is\n
Could not find portal by select %d, while interpreting result\n
Portal Status, Changing STATUS and CMD/STAT to reflect
Probe %s removed during selection process
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
New format for cip gen register, unsupported: %d\n
{%s::%s@%d [%s]} Error %s: synchronizing context
NRF53Flasher: AHB-AP %d ERASEALL success\n
[AstrisAsync] Deactivating async...\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
=== Loaded %s Boosters ===\n
Complex Address: 0x%llX\n
Gateway Version: 0x%X\n
error %s checking for data abort(uint32_t)
SWDACKDELAY relay write failed\n
Xtensa Core %s NOT configured\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Hang Address: 0x%016llx\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
read_dbg failed to access R_v7M_CLIDR
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
Init dbgwrap obj failed
Groups %d\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s=>%s} AXconn_t has more than one chip
CPU Monitor key does not exists for: %s\n
Unable to allocate memory for big response
ERROR: unable to resume translation for %s
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
NRFFlasher: timed-out waiting for NVMC ready\n
Set custom PSD json file: %s
Probe %s Device Not Connected on USB-C Port
Could Not Find a DCM Portal
{%s} set=%u (sh=%u), way=%u (sh=%u)
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s::%s} [%s] error %s reading SCTLR_ELx
Failed to Identify & Explore Chip via KIS: %d (%s)\n
unable to create connection
NRF54LFlasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
SoC BM Not Found, Bailing\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
Failed to read ide_table from KIS explore
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
About to call fault reg latch, min_operating_el: %d\n
1: ARM64_SYSOP_ATS12E1W\n
caller=%s, async=%d, iterations=%lu
NRFFlasher: performing AHB-AP ERASEALL\n
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
pmu-name: %s\n
2: ARM64_SYSOP_ATS12E1R\n
NRF53Flasher: CTRL-AP ERASEALL failed\n
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Failed to convert kisLoc %s to unsigned long long
{%s} %s: |%s|-|%s|
Could Not Allocate Loaded Booster Array
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
NRF_Flasher_t: AXjtag_srst deassert failure - %s (%d)
Chip Revision: 0x%X\n
Modified Word To Write: 0x%08x
Failed AP read of R_MEMAP_CSW res: %i
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s@%d} Probe reported connection lost [PROBEEOF].
Using Built In SoCs\n
No version information found in booster: %s
%s
{astris_probed_print_events} not supported in this build configuration
UPDATE cop64 %d -> 0x%016llx\n
Failed to access new_cpu status
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
{%s} host = %s
HOSTID=0x%x which is invalid, skipping orientation check
Did Not Find Any Boosters For: %s \n
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
%#09llx-%#09llx: %s\n
{%s} invalid data width %d bytes
Matched Booster: %s\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
Chip %x Status = %d\n
outstanding=%zu
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Portal Group Offset: 0x%X Entries: %d\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
==== User Error Messages ====\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Kick off the current process using probe %s? (y|n)\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
NRF54LFlasher: flash success\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
Dart Name: %s\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
runBlock
AP[%d]: MEM_AP_AXI\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
No 1500 bridges specified\n
[READ] %d -> %08x\n
NRF53Flasher: codeSizeBytes (%d)\n
{%s} wrote %d words to probe when %d words provided in request
Could not enable KIS SoC Access\n
{%s} select success without file descriptor set
CPU Explore: 0x%llX\n
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
Aligned Address: %llx
[INIT]\n
Hang Radar Info:\n%s\n
unknown match criteria type: %d
Skipping CPU %s at 0x%llx: not present in IDE\n
{%s} _resume_hw result = %s
NRF_Flasher_t: performing writelash to addr(0x%08llX) len (%u)\n
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
{%s} Unable to read SP_EL0
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
relay_get: %s = CMD_ERR (%s)
{%s@%d} Probe response payload read when no payload indicated.
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
Using Built In CPUs\n
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
{%s} unable to allocate probeInfo
Failed to explore chip: %d
%s status is '%s'\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
{%s} bridge returned an error
probetimeout retry failed logging as hang\n
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Subsystem Monitor[%i]: %s\n
Xtensa Option num_high_pri_intr: %d
Probe Map comm: request[%s], response[%s]
unable to obtain sysap
[PAR] Failed KIS Portal Access Preflight =%s (%d)
\t\t%s\n
Failed to get Bypass Config
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s} Failed to resume %s: %s
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
CPU Address: 0x%llX\n
Found an async abort pending; clearing it\n
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
NRF53Flasher: read %d bytes from target. Comparing...\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
{%s} error %s at line %d
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
batch_cmd_count: %d
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
JsonLogger: Wrote %zu bytes to '%s'
{%s} timed out waiting for cpu to halt during collect
SoC has been setup using standard instantiation (setup result=%s)
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
[1500] Error parsing IR command: %s
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
## ARM32cpu_t::read_register 64 bit 0x%x\n
In Readflash\n
{%s::%s} ERROR %d(%s) resuming %s\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Error status from AMAuthInstallSsoInitializePtr = %i
{%s@%d} neither socket nor kext connection available
NRF_Flasher_t: cannot readflash: APPROTECT is enabled\n
NRF_Flasher_t: AXjtag_explore failure - %s (%d)
{%s} Failed to extract die infofrom table (%d); continuing anyway
Invalid Size Given for AP AP=%d Size=%d
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
{%s} 0 words from probe when %d words left to read for reg %d
CPU ASC Offset: %d\n
--> wrstn_wir2 size=%3d dpcsoc=%d
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
KIS Chip Found, Doing KIS Explore Setup
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Could Not Find Any Boosters\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
## armcpu: bad status even though all bytes read (%d)\n
Probe %s status: Busy
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s} Unable to read CPSR
{%s::%s@%d [%s]} Error %s: checking exception
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Optional Key: CPUMonitor not in preferences
NRFFlasher: pageSizeBytes (%d) codeSizePages (%d) codeSizeBytes (%d)\n
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
      AXap_write of R_JTAGAP_PSTA failed with error %s
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Xtensa Option options: 0x%x
Can't get hardware model - failed to allocate data buffer
{%s} connectName[local host]
Successfully Authenticated Probe\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
Failed to convert primateHubLoc %s to unsigned long long
{%s} probe device server closed the connection while trying to read data (at recv)
NRF54LFlasher: read %d bytes from target. Comparing...\n
{%s} %sing word #%d at address 0x%09llx: %s
[1500] Error parsing v2 bridges
   Debug Port: SELECT %X: AVOIDED\n
Successfully Authenticated\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
NRF54LFlasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
Wrong width, should be either 4 or 8\n
Error closing %s [%d]
Connected to Probe Device Server [Default Log]
DBG_CPU: %s\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
Unable to read GPR 28
NRF53Flasher: addr (0x%08llX) is not in writeable portion of flash\n
{%s} Error looking up architecture (%s)
Probe Map Server Information: %s
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s->%s} (top) current_el=%d
[AstrisAsync] Barrier hit!\n
{%s} DAP command nwords=%d trimmed to %lu\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
In Writeflash\n
Could Not Allocate Mutable Dictionary For BoosterMangers
1500 IR Commands:
Failed to find a product plist for this soc %s
{%s:%s}: cpu powered off: unable to access a register for this CPU
## armcpu: success status even though not all bytes read\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
NRF53Flasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
{%s} probe [%s] added to list
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
Xtensa Option num_bp: %d
Error %d (%s) while expanding ~ for Astris history save\n
Initializing (%s) Booster's Astris API\n
{%s@%d} Drain empty on decr [%s].
CPU DBG Ack: 0x%llx\n
[REM_HWBP] bp%d\n
Result while reading third entry: %s , entry val 2: 0x%X\n
NRFFlasher: JTAG re-explore after CTRL-AP ERASEALL failed\n
{%s@%d} socket connection is not available
AXconn_t Struct Is NULL
error %s reading DAP MPIDR
type_hint not NULL, but creating a placeholder, this is off
{%s=>%s} AXconn_t has no chips
Optional Key: SubsystemMonitor not in preferences
NRF54LFlasher: comparing last partial %lu byte word\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
NRFFlasher: JTAG re-explore after CTRL-AP ERASEALL successful\n
Old ProbeDaemon does not support this command
NRF54LFlasher: performing AHB-AP ERASEALL\n
{%s} Failed to extract PID from table (%d); continuing anyway
{%s} failed (%s)
   DPv3 BASEPTR0 is 0x%08X\n
Connection to server accepted
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
CPU %s not found or already removed from the map
NRF53Flasher: operating on NET core\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
{%s} Error setting up memap target (%s)
Failed to convert primateLoc %s to unsigned long long
Creating CPU With Name: %s\n
{%s::%s} [%s] !bpwp_initted, retrying init
Probe %s LocationID Info is %s
NRF54LFlasher: setting RRAMC base to 0x%08llX for nRF54L15\n
The debug port associated with this chip has not been explored.
{%s::%s} halting %s\n
[%s] EL @ end of Collect: %d\n
OK: address translation suspended for %s successfully
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
{%s} 0 words requested for read at address 0x%016llX
Xtensa Option ocd_address: 0x%llx
NRFFlasher: addr (0x%08llX) is not in writeable portion of flash\n
Cleaning up Main Booster Object\n
Magic does not match: %#x vs %#x\n
NRF53Flasher: operating on APP core\n
   DPv3 bus is %u bits wide\n
## memapr %u 0x%016llX %d -> 0x%08X ...\n
{%s} FAILURE - NULL parameter
Selecting polling method %s
AXportal_t Is Not Valid Type - %d
USER %s(%04u): %s(): %s
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
Unable to read PC
[PREFS] Key: %s - Val: ??
{%s}#%02X cmd: %s, resp: %s
CPU Supported in Runtime: %s\n
Unable to read SP
Unable to disassemble_at_addr 0x%016llx
NRF53Flasher: performing AHB-AP ERASE PAGES\n
{%s} hostname:%s, flags:0x%08x
Early dbgwrap base extracted: 0x%llx\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
Unable to read FP
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
checking if relay \"%s\" is valid
NRF54LFlasher: codeSizeBytes (%d)\n
Could Not Find Booster Entry Function: %s\n
[REMBP] bp%d\n
Original Content: 0x%08x
Probe %s with unknown status %s dropped from available list
sent %zd bytes to Probe Map Server when sending %zu
Probe Type (%d) FW Version: %s does not support KIS.
{%s::%s} ITE is not set: 0x%X\n
Failed to sync prefs at end
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
NRFFlasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
User created bundle found, ignoring version checking via plist
CPU %s already in the map with status: %d
## apw %u 0x%08X 0x%08X\n
Switch to primate res: %s\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
AXmemap_nrfidentifyfamily: targetID = 0x%x, partNumber = 0x%x\n
Issuing request to Probe Map Server: %s
NRF_Flasher_t: APPROTECT enabled: doing CTRL-AP ERASEALL\n
Required Key-Value is a string, and not an array. Old booster found\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
{%s} 0 words from probe when %d words left to read for address 0x%016llX
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
Connect using RSD not supported\n
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
%s constructed
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
Choose a device: 
In Postflash\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
Previous authentication in-flight, wait for it to finish\n
gmtime() returned NULL, using epoch time
Required Key-Value is a string, and not an array. Old booster found: %s\n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
SOC AP[%d]: JTAG_AP\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
[Auth Debug] Disabled\n
{%s} already connected
AXconn or json_out are NULL
{%s} host name(RSD): %s\n
NRF_Flasher_t: eraseFlash failed: NULL connection param\n
Error %d(%s) executing instruction 0x%08X FAST
{%s::%s} [%s] length=%u when width=%d
astris_get_async_ver failed with error: %s
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
NRF_Flasher_t: performing eraseflash\n
Dart CPU SID(s): %s\n
   Debug Port not responding (%s)\n
=== Ending Gather and Clear ===
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
Complex CPM Offset: 0x%llX\n
## armcpu: success status even though not all bytes written\n
DEMCR: 0x%08X -> 0x%08X
NRF54LFlasher: performing CTRL-AP ERASEALL\n
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
      Select port %u: already explored..re-exploring\n
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
NRF54LFlasher: AHB-AP ERASEALL success\n
PKA Base: 0x%llX\n
Can't get hardware model - failed to get property
NRF54LFlasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
{%s} no chip found
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
dfu-Type: %s\n
using standard products.plist for %s
[REM_WP] wp%d\n
[Auth Debug] External Debug Interfaces Open\n
[1500] %s step %d: unknown instruction '%s'
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
Type 'jebdump' to do scan/mem dump\n
Warning: chip exploration did not complete successfully (%s)\n
Can't get hardware model - failed to find matching IOService
Can't get hardware model - failed to convert to C string
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
{%s} halting %s\n
[%s] TGE is set so we traping to EL2\n
KIS Readvals putting back the value
Failed to get PMU Name
Unable to read GPR %d
Result while reading first entry: %s , entry val 0: 0x%X\n
{%s} FAILURE - max length exceeded
CPU with %s Not Created via Name
We are Allocating\n
Had an error during transfer: %s
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
{%s@%d} Connection to server rejected, error=%d (%s)
{%s@%d} Unable to connect to server, %s:%d
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Failed To Init Booster's Astris API In: %s with %s (%d)\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s} [%s] m_exception_level=%u\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
NRF53Flasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
 MEM-AP %X is hung\n
[KIS] Register Read/Write/Wrote: %d\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
Invalid file name: \"%s\". File names must not start with '.'
{%s} Component ID read fail for 0x%llx (%s)
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
{%s=>%s} AXconn_t has no SoC object
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Complex CPU Name: %s\n
{%s} Extracted CIP Gen Number from table  (%d)
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
Can't get OS build version - failed to create URL
relay_get: %s = %d
Size or Count provided are 0.
Adding new booster path: %s\n
Failed to convert %s key @ index %d
SoC has been setup using standard instantiation (setup result=%d)
{%s} Error reading PID (%s)
## apr %u 0x%08X -> 0x%08X\n
Failed to instantiate %s\n
%s: not supported.\n
Variables not setup
{%s} ROMTABLE (nest=%d)\n
AP[%d]: MEM_AP_AHB\n
NRFFlasher: performing AHB-AP ERASE PAGES\n
Unable to allocate memory for next part of big response
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[DCC] Grabbing DTR failed: %s\n\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
SSO is DISABLED\n
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_52\n
There is no system bus access port on the debug port
BoosterManager Types:\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} Component ID read fail on romtable (%s)
{%s} flags:0x%08x
Using 10pin connector skipping orientation check
{%s} probe_match = %s
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
## armcpu: bad status even though all bytes written (%d)\n
  Error path [%s]\n
%s given a NULL conn object
NRF54LFlasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
%s SoC created
DEMCR write failure - %s (%d)
    INFO(%u,%d): %s(%04u): %s(): %s
{%s->%s}[cached] %s[0x%X] = 0x%08llX
NRF53Flasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
{%s:%s@%d} Critical error [radar already requested]
Failed to convert CFString to C String.
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
[%s] CPU BM Not Found, Bailing\n
Result while reading second entry: %s , entry val 1: 0x%X\n
\t[MATCH_SKIP] skipping entry
Turning Debug Clock On
Cleaning up Each Booster Manager\n
Gathered:\n
\tReading left over chunk 0x%x @ 0x%llx\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
register    %-15s %3u     \"%-s\"\n
Can't get hardware model - failed to create string
Hardware model: %s
Passed NULL booster without custom plist\n
[1500] TAP key is not a valid integer
[INS_WP] 0x%016llx x %d\n
NRF53Flasher: performing CTRL-AP ERASEALL\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
%2d) %s %s [Busy]%s\n
{%s@%d} {%s[select]} %d(%s) [RETRYING]
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
AXportal_t Struct Is NULL
{%s} Thread %#llx clearing key %lu
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} m_exception_level(%d) != current_el(%d)
{%s} (end) current_el is now %d
[%s]\n
{%s} ROMTABLE (dbgbase=0x%llx)
JsonLogger: Schema loaded successfully for category '%.*s'
Pages %d\n
[%s] cop %d -> 0x%08x\n
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
{%s->%s}
   {%s} Probe requires overrun detect mode.\n
{%s} drop ProbeName %s
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s} handle ROM entry
{%s@%d} Unable to create socket
{%s[select]} timeout while waiting for data from the connection
NRF54LFlasher: unknown part code 0x%08X, defaulting RRAMC base to 0x%08llX\n
end rev is not of expected format; skipping cpu_desc override\n
Failed to convert %s key @ index %d to a number with base of %d\n
[1500] Error parsing bridge '%s': missing required field 'select'
AXjtag_explore failure - %s (%d)
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
   Setting up AP IDR %08X\n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Complex Type: %s\n
We are at max iterations, still didnt get full JSON
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
[HALTED] dfsr = 0x%08x\n
NRF53Flasher: APPROTECT is %s\n
[AstrisAsync] Activating async...\n
Failed to init from cpu desc armv7m cpu: %s \n
{%s} valid response from bridge
Dart Dart Type: %s\n
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
[WRITE] %d -> %08X\n
NRF53Flasher: checking APPROTECT status\n
Awaiting response from Probe Map Server
Initialized %d 1500 bridges\n
[1500] TAP %d: irlen must be > 0 (got %d)
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
NRF53Flasher: AHB-AP ERASE PAGES success\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
[%s] chipinfo is NULL
Original Length: %d\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s::%s} EDSCR with TXU set - unable to recover.\n
Cached async_replay capability version: %u
{%s}#%02X %s [%s]
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
Astris Source Version: %s\n
Invalid current AP (%d), adopting latest (%d)
NRF53Flasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
{%s} unable to find single_port probedaemon on port %d
{%s[recv]} %d(%s) [RETRYING]
NRF54LFlasher: addr (0x%08llX) is not in writeable portion of flash\n
\t%s\n
error trying to unlock MSR %s
     0x%016llx: ERROR\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
X06 Part
kext connect name %s\n
TargetSel Before Disable: 0x%x
DEMCR read failure - %s (%d)
AXjtag_srst deassert failure - %s (%d)
Cannot create complex descriptions from NULL info\n
VBAR: %#llx\n
** Unauthorized User/Network or ECID **\n
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
Xtensa Option num_wp: %d
setCategoryValue: path='%.*s'
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s} drain_packets=%d [%s]
Failed to create Xtensa CPU %s \n
KIS Preflight No Need To Write to AP CSW
XBS Version Modified: %s -> %s\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s} read OK but took %d tries
NRF53Flasher: writing partial %lu byte last word\n
Buffer is NULL
Error %d (%s) opening cmd snapshost save file
Probe %s selected
invalid IR command '%s'
[KIS] Address: 0x%llX\n
{%s::%s} failed: %s
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
{%s} Exploring with option: %s\n
haskis bit not set\n
Could Not Allocate Booster Location Array
!!!! FILE RADAR: Don't know how to compare two values\n
[SSTEP] using BP %d\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
Error %s connecting to server %s:%s [RETRYING]
Probe Map comm error %d(%s) %s [%s]
!!!! CPU Key %s is INVALID !!!!\n
     0x%016llx: 0x%08x    %s\n
## dpw 0x%02X failed (%s)\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
NRF_Flasher_t: writeflash failed: NULL connection and/or data param\n
[1500] v2 plist missing required field 'taps'
{%s::%s} waiting for EDSCR ITE
NRF53Flasher: wrote %zu bytes\n
There is no CTRL-AP on the debug port\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
     0x%016llx: 0x%04x      %s\n
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
Going To Create Generic ARMV8\n
read failed, using old cached as base: 0x%x
      Explore of JTAG-AP port %u failed with %s\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
## ARM32cpu_t::read_register %u\n
   Debug Base: %08X\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
CPU (%s) has explore flag of: 0x%llx which is not set\n
CPU Supported in Integration: %s\n
Cannot create DART descriptions from NULL info\n
Can't find descriptor for group - can't index\n
Found the RTXCID Structure!\n
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
NRF53Flasher: JTAG re-explore after net core enable successful\n
CPU has no regions, maybe powered off?\n
Invalid value for 'entry' tuple element - can't index
100%%\n
Length is 0
Proceeding with full explore instead of instantiation
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
SSO with no prompt being used
Production Fused Device\n
Preferences does not exists: %s, creating one.\n
[1500] No %s.plist resource found
[1500] %s step %d missing required field 'instr'
error %s checking for data abort
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
ERROR: unable to suspend translation for %s
NRFFlasher: CTRL-AP ERASEALL attempt %d successful\n
{%s} found single_port probedaemon on port %d
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s::%s} %s pre_resumed\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} Failed to single-step %s: %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
NRFFlasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
received %zd bytes from Probe Map Server when have %zu
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[INSBP] bp%d addr=%08llx fpr=%08X\n
{%s} FAILURE - malloc error
dropping empty probeInfo (port=%u)
We are done with clean up\n
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
Creating NRFFlasher: Chip: ID(%d) PID(%d) flags(0x%08X) IDE-base-addr(0x%08llX)\n
{%s} empty response string provided
{%s} bridge returned DECERR
   DPv3 baseptr is not valid (%X)\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
[PREFS] Key: %s - Val: NULL
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
probe event: %s
Die-Count: %d Current-Die: %d Die-Type: %d
     ARM %s breakpoints: %u\n
JsonLogger: Created with default schema version '%s'
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[ARM64 INS_WP] 0x%016llx x %d\n
[AstrisAsync] Deactivate while async is not active!\n
\tLeft To Read (%d) < width (%d).\n
{%s} Class 9 ROMTABLE (nest=%d)\n
Complex Name: %s\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s} Batch attitude key created for %p thread %#llx key %lu
Could not find bundle () in given array: %s\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
{%s::%s} [%s] MMU not active - returning %s
Invalid APTABLE (%d), so using most restrictive
{%s} Error reading CPUID (%s)
      Read of JTAG-AP port %u CSW failed with %s\n
TatsuServer Found: %s\n
Sending DYN Bypas Channel Set: %d
Complex CPU ID: %d\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
connection created
%s probe[*] from Probe Map Server [local host]
NRF54LFlasher: performing flash to addr (0x%08llX) of len (%zu)\n
NRF54LFlasher: Writing %zu bytes in %zu chunks of %zu bytes\n
Failed to find a plist for this soc %s
[READ] %d -> 0x%08x\n
[READ] cop64 %d -> 0x%016llx\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
NRFFlasher: CTRL-AP ERASEALL attempt %d failed\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
     ARM %s debug CPU rev %d\n
Error Reading Device Production-Fusing\n
NRF54LFlasher: performing verify at addr (0x%08llX) of len (%zu)\n
NRF_Flasher_t: readflash failed: NULL connection and/or data param\n
CPU PS-Register: 0x%llX\n
{%s::%s} [%s] error (%s) getting number of HW BPs
Found %d APs
NRF_Flasher_t: unable to obtain CTRL-AP\n
{%s} status=%d being reported as Unknown
   MEM-AP not enabled\n
[KIS] Portal Status: 0x%X\n
Asked To Read A Negative Register Index
** CPU %s requires forced explore override flag on this SoC **\n
[RESUME] Chip %x\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
Error %d (%s) opening history save file
Probe %s with unknown kick response %s
relay_set: %s -> %d
unable to identify chip
start rev is not of expected format; skipping cpu_desc override\n
Could not find TAP at chip-index %d for v2 1500 config\n
{%s} skipping dcache flush, cache already clean
Can't get OS build version - failed to create ReadStream
NRFFlasher: timed-out waiting for CTRL-AP ready\n
Creating CPU Returned: %s\n
Could Not Allocate Info Keys Array
{%s::%s} %s resumed\n
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
DBGCTRL = %08X   res=%d\n
iter=%lu
ERROR!! Wrote %zd bytes, expected %zd\n
relay_set: %s = CMD_ERR (%s)
no system bus AP present when expected
[KIS] CMD: %s \n
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
DCCCTRL = %08X   res=%d\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Initialized Logging - %s
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
Failed to sync prefs at beginning
[AstrisAsync] replay preflight: Async not active!\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
{%s=>%s} null reference to AXcpu_t record, `cpu`
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
Astris Version Set: %s
Booster Info:\n%s
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
SSO info present but SSO disabled.
{%s} checking for single_port probe daemon on port %d
{%s} NOMEM
NRF54LFlasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
SoC does NOT support IDE Explore\n
Sprocket probe, for now I guess we will just say yes...\n
[AstrisAsync] Failed to restart Async batch\n
NRFFlasher: APPROTECT is %s\n
NRFFlasher: read %d bytes from target. Comparing...\n
Probe Map comm error %d(%s) %s
{%s@%d} Received %d bytes when requested %d bytes.
{%s@%d} Timeout while sending probe command.
{%s} DEVARCH read fail in CoreSight component (%s)
first read of CMDSTAT may fail if external reset occurred
{%s} bridge timed out
Invalid Bundle: %s
Booster Bundle: %s\n
Passed NULL plist file\n
Found another target for the plist\n
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
[AstrisAsync] Discarding %zu completed command(s)\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
[1500] Detected plist version %d
[1500] Error parsing TAP description
** Add the --with-force option or use the explore_override console command **\n\n
NRF53Flasher: CTRL-AP ERASEALL successful\n
replayPreflight
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
{%s} probe_port = %d
{%s} %s
EICE chip %x initialized\n
     ARM %s watchpoints: %u\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
\tReading left over chunk expected 0x%x got 0x%x\n
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
{%s} no TAP detected that supports 1500
[%s] Booster System Is Not Initialized\n
bypass-config-name: %s\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
%s probe[%s] from Probe Map Server [local host]
Probe (port=%d) with unknown status %s dropped from available list
Failed to convert kisHubLoc %s to unsigned long long
[ANAMOLY] Could not find AXcpu_t object for CPU\n
product-name: %s\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
2: ARM64_SYSOP_ATS12E1W\n
pc:  0x%16s cpsr: 0x%16s %s\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
Can't get hardware model - failed to allocate data string
The debug port associated with this chip has not been explored\n
{%s::%s} write OK but took %d tries
1: ARM64_SYSOP_ATS12E1R\n
Breakpoint Address: 0x%llx
{%s@%d} Received %d bytes when requested %d bytes [%s].
Breakpoint Enabled: %s
Before astris_kis_init_dp, CMDSTAT=%08X\n
Matched via Bundle ID\n
{%s->%s} current EL (%d) already == target EL.\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
NRF53Flasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
AuthDebug::authenticate_probe - no need to authenticate\n
{%s} unmodified-probe_match = %s
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
We are Deallocating\n
Min Component - %s\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
process (%s) (%d) path: %s
{%s::%s} NULL parameter
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Disconnected from Probe Map Server
SOC_t::{%s} CPU_t group=%d when group 0 expected
JsonLogger: Loading schema for category '%.*s' from '%s'
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
could not perform cpu_preflight
AP[%d]: unknown type\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
CPU Name: %s\n
Dart Coastguarded CPU: %s\n
Booster Value is Not String\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s::%s} error %s writing EDSCR %s
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
failed read from DEMCR - %s
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} Debug Base: %08X
{%s} strsep empty so match any probe [localhost]
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s->%s} START handling exception
{%s} %s status failed. error: %d (%s)
Width: %d not supported
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
%s: chip was NULL when attempting to release soc
## dpr 0x%02X -> 0x%08X\n
Could Not Get BoosterManagerUtility\n
CPU Die: %d\n
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
[SSTEP] bvr=%08x bcr=%08x\n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s} %s DC cache already clean since last halt, skipping flush
Replacing key with value
Could Not Get BoosterManager\n
Component Group Offset: 0x%X\n
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
[REMWP] wp%d\n
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
{%s} %s status is '%s' [Status Read %d times]\n
{%s=>%s} null reference to CPU_t object, `cpu->state`
probetimeout retrying access...\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
## dpr 0x%02X failed (%s)\n
CPU AP-Select: %d\n
using multi-target booster products_%s.plist
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
Unknown number of groups in the explore table; can't parse group attributes
{%s->%s} m_exception_level=%u
Unable to read LR
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
NRF_Flasher_t: AXjtag_srst assert failure - %s (%d)
Match Count is Zero. This is invalid.
Section 1 Offset: 0x%llX\n
Creating NRF53Flasher: Chip: ID(%d) PID(%d) flags(0x%08X)\n
NRFFlasher: verify success\n
can't find pid in response\n
Probe %s Device Server listening on port %d
OK: address translation resumed for %s successfully
Value Types Are Not Strings\n
{%s} unaligned %d-byte access at address 0x%09llx
\t%s (%s)\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
{%s} _pre_resume_hw result = %s
{%s} explore with exploreflags 0x%X complete [%d chip%s]
%s probe[%s] from Probe Map Server [%s]
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
   CPUID: 0x%08X\n
Connected toProbe Map Server (single_port) 
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Found match - bypass_device: %s; channel: %d\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
no debug bus AP present when expected; after sysap is NULL
[ARM32cpu_t::_update_register64] 0x%08x\n
Got an error writing 0x%X the DCM Control Register: %s
Multi target booster, checking for %s.plist\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
\tTatsu AuthDebug Triage | All\n
Xtensa Option reg_file_size: %d
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s::%s} creating CPU
{%s} _halt_hw result = %s
Values Not The Type We Expected. Expected: Number and String\n
--> psr        size=%3d bit=%d
NRF53Flasher: performing verify at addr (0x%08llX) of len (%zu)\n
{%s} %s: |%s|
Could Not Get Bundle Out Array of Found Boosters\n
Booster:\n
Error happened when reading edscr. Retry #%i\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
NRFFlasher: flash success\n
can't find bid in response\n
HOSTID bit not set\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
** \tTatsu AuthDebug Triage | All     **\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
Start Page: %d\n
error %s checking for data abort(first)
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
{%s::%s} [%s] error %s writing SCTLR_ELx
caller=%s, async=%d
{%s} Reading base 0x%llx entry's component ID
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
[KIS] Portal ID: %d\n
[1500] TAP %d missing required field 'ir-cmds'
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
[AstrisAsync] Resume when not paused!\n
AP is NULL
AP[%d]: JTAG_AP (Exploring Later) \n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
   {%s} select %u port %u: %u chip%s\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
Switch back to primate KIS: %s\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
NRFFlasher: AHB-AP ERASEALL success\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Probe Map name of probe %d is: %s
{%s@%d} Timeout while attempting connect to server
NRF54LFlasher: verify success\n
[1500] IR command '%s' missing required field 'opcode'
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
   Debug Port: SELECT %X; error: %s, retrying..\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
  Nested path: parent='%s', child='%s'
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
In Eraseflash\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
!!!! Complex CPU Key %s is INVALID !!!!\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
[FLUSH]\n
\t\tARMv6 debug CPU xxx ID\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
--> misc_wdr   size=%3d wirtestporten=%d
   JEDEC ID: 0x%08X\n
   {%s} (DP): status=0x%X(%s) - %s\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
ERROR!! Couldn't save %s binary data\n
%d%%\n
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_53\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
NRFFlasher: performing verify at addr (0x%08llX) of len (%zu)\n
JsonLogger: Writing category '%.*s' to '%s'
Bundle: %s NOT FOUND\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s} read ESR EL1|EL2|EL3 (%d)
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
Can't get OS build version - failed to allocate buffer
Created Connection - : %s
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
{%s@%d} Unknown CS code [%u]
ERR: conn->nchips != 0; looks like chip is explored\n
[%s] {%s->%s} Transitioning to exception level %u.\n
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
Trying to use size of 8 on not AXI bus
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
{%s} error: %s
!*!*!* ****************************************************************************** !*!*!*
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
couldn't find CPU1. this is expected sometimes.
[1500] Error parsing bridge: %s
   Debug Port: SELECT %X: SKIPPING\n
relay_get: %s = ERR
NRF54LFlasher: CTRL-AP ERASEALL successful\n
NRF_Flasher_t: APPROTECT disabled: doing AHB-AP ERASEALL\n
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
connection about to be destroyed
{%s::%s} creating placeholder for CPU: name=%s
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
Failed to get DFU Type
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
[AstrisAsync] Resuming Async Mode\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
NRF_Flasher_t: checkAPProtect failed: %s (%d)
Cannot create CPU descriptions from NULL info\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
Booster System Is Not Initialized Bailing\n
   Debug Port: SELECT %X: DISABLED\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
%s probe[*] from Probe Map Server [%s]
{%s@%d} gethostbyname failed, error=%d (%s)
{%s} unsupported bridge type for %s
{%s}ERR: bypass_device_name is NULL\n
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
DBGSTATUS = %08X   res=%d\n
NRF53Flasher: performing AHB-AP %d ERASEALL\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
[CLEANUP]\n
{%s@%d} Failed to send probe command (error %d).
CPU: %s halting debug is now %s\n
\tPrologue Aligned Read Failed
Valid Portal
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
Unable to read CPSR
AP Only Explore was asked for, stopping here
=== Detailed %s Boosters ===\n
Map is empty, not removing CPU %s
Section 5.1
_with_cpu_thunk
ITM
AXconn_set_nickname
Register file 44
\t[MATCH_TARGETID] FAIL <= unable to find DP
irlen
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_REGID_MASK < NUM_ENCODINGS\n
Invalid Xtensa CPU OCD.DEVID = 0x%8.8X. Should be 0x%8.8X (LE) or 0x%8.8X (BE)
_tie_read_word32
(0x%08llX) %s
astris_set_user_die_select
String
PMP
AXI-ERROR=0x%X - AXI-XACTION-FLAG=0x%X - ADDRESS=0x%llX
HardwareBreak
astris_jtag_set_pipe_cycles
hardware error reported by probe
ASTRIS_ERR_FAILURE
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm64cpu.cpp
ret.clear.edscr-error
{%s:%s@%d} current_el[%d] <  %d\n
internal.is_dft_authenticated.chip->soc == NULL
RF8
NRFFlasher: JTAG re-explore after CTRL-AP ERASEALL successful\n
Accept
{%s:%s@%d} m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15\n
[ARM64 INS_WP] 0x%016llx x %d\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
fn._gen_debug_interrupt
_reg_desc_lookup_by_name
{%s} host:%s, flags:0x%08x
Invalid file name: \"%s\". File names must be at least %d characters long.
full word
Set custom PSD json file: %s
ret.production_emulation
ASC-CTI
Found the RTXCID Structure!\n
[INS_WP] 0x%016llx x %d\n
_is_bpwp_initialized
astris_cpu_mmu_get_config
Result while reading third entry: %s , entry val 2: 0x%X\n
Table 5–180
LCOUNT
{%s:%s@%d} Critical error [radar already requested]
file/object not found
/
{%s} probe_host = %s
cpu_get_cl4_debug_signpost
cpu_hwwp_disable
Invalid value.
setTargetOS
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llX) - reg_count=%d - val=0x%X
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
ATS1Eop
\tPrologue Aligned Read Failed
\nPKA Command Verify Timed Out\n
stat
Portal Group Offset: 0x%X Entries: %d\n
ret.nop
high
fn._ocd_reg_r.dsr.dsr
astris_kis_clear_status_registers
Busy
NRF54LFlasher: performing verify at addr (0x%08llX) of len (%zu)\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
{%s} category=%d
fn.var.exec_path.invalid
value=0x%8.8X
{%s} probe_match = %s
wir-tdo
DISPDFR
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
[Auth Debug] External Debug Interfaces Open\n
setup_bp.not_halted
_insert_data_breakpoint
op_RSR_encode
TCP send
EDRCR
{%s} _pre_resume_hw result = %s
fn._ocd_exec_instr.rfdd
Unique required when multiple probes
pointer.IsValid()
param.conn.chip  == NULL
Stop Clock: %s\n
write.dlr_el0 NOT DIRTY
M0
ASTRIS_ERR_LOSTCONN
SWDONLY
result.AXproduct_copy_bypass_info_for_bid
value
_set_bpcr_hw
instruction size too large
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
MISC2
Vector Base
Failed to get PMU Name
{%s:%s@%d} [%s] scanning out (DSCR)\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s->%s} m_exception_level=%u
init_hw.read.dhcr
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
fn._ocd_reg_r.ddr.regidx_save
%s/Library/Logs/Astris
MAIN_DEBUG_ROM
Gone
fn._tie_read_word32.first
connection not currently open
{%s}#%02X %s [%s]
[ANAMOLY] Could not find AXcpu_t object for CPU\n
Unknown error.
Top
[1500] Error parsing IR command: %s
!!!! Critical Error: Error %d(%s) deleting info %p batch_attitude_key !!!!\n
{%s=>%s} null reference to AXconn_t record, `conn`
param.ticket_data == NULL
Register file 63
ASTRIS_ERR_EXPIRED
ASTRIS_ERR_EMPTY
Invalid SoC Booster. SoC Booster Requires PID\n
memAPEraseAll
ret.generate_nonce_and_send_request
THREADPTR
cpu_cache_info
ParseHex4
wrstn-pipes
cleanup_astris_api
_a64cpu_read_edscr_masked
{%s->%s} current EL (%d) already == target EL.\n
_init_registers
/var/log/astrisclient
/System/Library/CoreServices/SystemVersion.plist
general error reported by probe
channel-%s
_write_memory_fast
fn.param.name.null
Invalid data breakpoint index %d
complex-type
SMC
gpr < 15
fn._write_special_reg.ibreakenable
AXconn_conndesc
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
ret.reg.write.K_DA_REG_NAME_ECID0
NRF53Flasher: timed-out waiting for NVMC ready\n
ret.spmi_read
param.val.invalid.>max
s != 0
wir-wirshiften
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
EXCSAVE6
revive
astris_convert_addr_to_die
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
_read_reg
setTargetIdentifiers
/cpus
Failed to convert %s key @ index %d to a number with base of %d\n
[MEM] Aborted; DSCR = %08x\n
[%s] cop %d -> 0x%08x\n
{%s::%s@%d} [FALSE] gpr[%d] < T32_GPR_COUNT\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
Only Auth-Debug, DFT-Auth and Probe-Auth are currently supported.\n
{%s:%s@%d} [%s] checking for data abort\n
type_hint not NULL, but creating a placeholder, this is off
RESPONSE_CMD
EDSCR
failed to create log dump file
Sprocket
astris_get_soc_resource_filepath
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
spsr_select
fn._ocd_exec_instr.l16ui.r1.r0
parse_soc_info_from_booster
ret.AXmemap_read.board_id
{%s:%s@%d} Took an exception that took us to exception level[%d] other than 1, 2, 3?\n
{%s::%s@%d} [FALSE] aarch64\n
ret.reg.read.K_DA_REG_NAME_PKA_BASE_HI
strfunc.h
dest_reg < 15
Fabric access is blocked. Expected if production unit, won't explore further.
Disconnected from Probe Map Server
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
Groups %d\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
[PREFS] Key: %s - Val: NULL
Missing a name for object member.
fn.entry
framework
SUCCESS
ctrlAPEraseAll
   {%s} Read AP's R_MEMAP_CSW\n
ret.CFPropertyListCreateWithStream
Misc register 3
m >= MemberBegin() && m < MemberEnd()
PMU: 
res.setup_transaction_objects
_get_num_hwbp_hw
astris_jtag_scan_stay_gotorti_impl
fn._ocd_reg_w.ddr.tgt_32
DHCSR write failure - %s (%d)
Failed to read register: 0x%llx
ret.m_lam.paccess_write
Production Fused Device\n
AXdebug_auth_get_probe_timer_count
reg.ocd.dsr.invalid.not_cleared
pid
BananaSplit
{%s::%s@%d} [FALSE] src_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
{%s} exec: DC_CSW_X1_ENC\n
astris_init_ap_mem
[%s] chipinfo is NULL
COMPARE2
RF18
RF41
fn._ocd_reg_w.dcrclr.regval
{%s:%s@%d} [%s] getting GPR 0 (ARB)\n
AXcpu_cache_cleaninv
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
fn._tie_read_word32.last
param.ar.invalid.>15
ASTRIS_ERR_HTTP_FAILURE
Category is null
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
NRF_Flasher_t: cannot writeflash: APPROTECT is enabled\n
param.cpu_name.invalid.NULL
fn._ocd_reg_w.ddr.regval_save
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
file
[KIS] Address: 0x%llX\n
astris_explore_enabler_destroy
CPU.ARMv7m%s
Table 5–168
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
cpu_hwwp_enable
%s: chip was NULL when attempting to release soc
.start_time
{%s:%s@%d} [%s] performing single step\n
Subsystem Monitor[%i]: %s\n
fn._ocd_exec_instr.TIECompleteRead
No MEMAP access while connecting to
Probe %s status: Idle
cpu_lacc_status_insert
%s NOT configured\n
fn._ocd_reg_w.ddr.t2_save
is.Peek() == '{'
Failed to get DFU Type
Error reading thingy
{%s:%s@%d} [%s] writing ITR\n
NRF53Flasher: performing verify at addr (0x%08llX) of len (%zu)\n
hwbp_insert
fn._write_window_base
no SOC object available
{%s:%s@%d} [%s] NRF54LFlasher: flash failed: addr(0x%08llX) + word-aligned len (%zu) do not fit in any writeable regions\n
{%s:%s@%d} [%s] failed to read CMD/STAT\n
document.h
Banana split probe, for now I guess we will just say yes...\n
instruction=0x%llx
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT || == SP\n
Invalid reg_index %u
Error:ASTRIS_ERR_BADPARAM(-29)
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
CSPDATA
ETM
{%s:%s@%d} !(prsr[0x%08X] & DLK)\n
ret.get_current_el.initial
ret.test.2.0
NRF53Flasher: writing partial %lu byte last word\n
fastsimSWD
BoosterManager.Utility
{%s:%s@%d} [%s] NRFFlasher: read count(%d) does not match expected count(%d)\n
DPAP
astris_ide_get_bootid
n >= 0 && n <= 308
[1500] Error parsing v2 bridges
{%s:%s@%d} [%s] writing DRCR\n
ret._a64cpu_get_current_el_hw
{%s} _halt_hw result = %s
virtual int CPU_t::collect(int)
ret.CFURLCopyFileSystemPath
Processor Id
XTENSAcpu_t
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
DebugAuth
AXdebug_auth_get_timer_count
Data break 0 control
fn._ocd_reg_r.DSR
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
{%s} [!is_64] exec: encode_msr(MDDTRTX_EL0, 0, %d\n
IDE ACCESS OUT OF BOUNDS
AMAuthInstallApSetParameters
fn._ocd_reg_r
astris_soc_check_debug_root
write.dspsr_el0 NOT DIRTY
Length is 0
\nSaved %s binary data to %s\nWrote %lu bytes\n
One time initialization of oslog API failed!\n
SLEEPING
unable to identify chip
Cleaning up Main Booster Object\n
_get_num_hwwp_hw
esr_el3
PARTNO_SWDP_M7
ASTRIS_ERR_PENDING
--> extrawrstn %d
mempool-size
[INSWP] 0x%08llx wp%d rdwr=%X\n
hwwp_insert
authenticate_probe
MAC16 Data register 3
%x.%02x%s
chip->ide_table == NULL
{%s:%s@%d} [%s] doing JTAG scan (DTRRX)\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
%s (addr=0x%llx)
Table 5–184
Apple Fabric Timeout
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
%Y-%m-%dT%H:%M:%S
{%s} no response from bridge
AXexplore_enable_all_cpus
ARM64cpu_t
AXcpu_hwbp_remove
armv7m-region-axim-end
ret._a64cpu_raise_el_hw.el=2.to_read_hcr
<unnamed>
APCIE
Error %d(%s) executing instruction 0x%08X
~HDE
Unable to read FP
AXcpu_mmu_walk
MR0
_remove_breakpoint
{%s:%s@%d} [%s] NRFFlasher: flash failed: addr (0x%08llX) provided is not word-aligned\n
complex-cpus
gpr < 32
vaddr
connecting to Ethernet probe
AXconn_connect_kext
virtual int ARMv6cpu_t::read_dcc(int *, uint32_t *)
get_sw_info
probed
KIS-Null
setAddress
{%s:%s@%d} [%s] reading CCSIDR[L1-D]\n
PROBED_USB_RSP_ERROR
{%s:%s@%d} [%s] doing IR scan (DTRRX SCAN_N)\n
OUTEN_DBG
Result while reading first entry: %s , entry val 0: 0x%X\n
Register file 33
astris_json_logger_init
messages
TXU
read back of modified data did not match
symbol.check.loaded.AMAuthInstallSupportDictionarySetInteger32Ptr == NULL
ret.reg.write.K_DA_REG_NAME_NONCE_2
Table 5–133
{%s@%d} Unable to create socket
Parent key is not an object
DCS_BC4
ACC-CTI
{%s:%s@%d} [%s] reading PRSR (lsr)\n
SoC not identified by IDCODE - enumerating instead of instantiating
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
Gateway is KIS, seeing what probe this is\n
Previous authentication in-flight, wait for it to finish\n
Register file 54
astris_cpu_lower_el
soc is NULL
AXconn_destroy
Misc_Rtx117x_t
u64toa
AXbooster_interface_create_cpu
{%s} wrote %d words to probe when %d words provided in request
NRFFlasher: timed-out waiting for CTRL-AP ready\n
Connecting to server, %s:%d
{%s:%s@%d} {%s->%s} EL3 not implemented\n
_remove_data_breakpoint
Error detected
NRF54LFlasher: AHB-AP ERASEALL success\n
15002APB
master-size
DCS_BC0
_update_register32
{%s:%s@%d} [%s] NRF54LFlasher: failed to read RRAMC config register 0x%08llX\n
cpu_suspend_translation
psr-size
OUTEN_RESTART
internal.enable-timer-ovr.chip == NULL
MAC16 data register 2
fn._write_special_reg.dbreaka1.address
j1500d
CPU %s already in the map with status: %d
[SSTEP] using BP %d\n
{%s} skipping dcache flush, cache already clean
ret.getSubsystemEnableStatus
==== Exception Trace ====\n
   {%s} select %u port %u: %u chip%s\n
(Last: %s)
decr_drain_packets
SCANDEBUG
v8@?0
AXchip_get_stm_dockch_list
Failed To Initialize Logging\n
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
** Add the --with-force option or use the explore_override console command **\n\n
{%s:%s@%d} [%s] setting DTR MODE to FAST\n
hwwp_enable
param.wb.invalid.>wb_max
{%s:%s@%d} [%s] NRF54LFlasher: flash failed: addr (0x%08llX) provided is not word-aligned\n
hwwp_disable
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
MAC16 Data register 2
SWD Slave Unavailable
ASTRIS_ERR_RESETTING
ARMV6M
FindMember
Dart Name: %s\n
CDPDL
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
ignore_dapcmd_error
[KIS] Portal Status: 0x%X\n
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
ret.cpu.nmi()
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
{%s:%s@%d}\nFABRIC HANG DETECTED. JEBDUMP REQUIRED.\nContext: %s\nSoC: %s Rev: %s Address: 0x%016llx\nDescription: %s
AXbooster_print_boosters_detailed
GPR[cached]
completedAcmds
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
ret.pka.verify.status.err
{%s:%s@%d} [%s] NRFFlasher: waitForNVMCReady() failed\n
Probe %s USB-C location is %s
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
MemoryBlock_t
ParseNull
astris_command_lock
Replacing key with value
[%s] CPU BM Not Found, Bailing\n
\tLeft Over Chunk Read Failed\n
   JTAG-AP: Identification = %08X\n
default_schema_version is NULL
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s:%s@%d} [%s] AXmemap_nrfidentifyfamily: failed to select DP bank\n
{%s:%s@%d} [%s] failed preconnect\n
_create_cpus
NUB
component group %d\n
astris_ide_explore_release
ESR_EL2
{%s:%s@%d} [%s] Read DWT Comp %u\n
{%s} %s status is '%s' [Status Read %d times]\n
AXcpu_sstep
op_LDDR32_encode
DCM
CPU Supported in Runtime: %s\n
cpu-ascdebug-dbgack
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
CCSIDR
%s/%s%s.bin
CPU disabled by SW, not accessable
{%s@%d} neither socket nor kext connection available
Booster:\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
enable_timer_ovr
invalid parameter
command timed out
kick
ret._cleanup_hw
addMember.engineer
%#09llx-%#09llx: %s\n
CPU ASC Offset: %d\n
param.conn.enable_explorer == NULL
copyBoardNameForPrimate
NRF53Flasher: checking APPROTECT status\n
%s_%s
SETRELAY
Invalid object or key for engineer array
AXportal_t Is Not Valid Type - %d
CACHE
astris_apread
X12 Part
astris_gather_poral_error_info
IsArray()
data_.f.flags & kUint64Flag
{%s:%s@%d} [%s] reading PAR[64]\n
AuthBase_t::init failed (AuthDebug_t)
fn._reg_desc_lookup_by_name
Old ProbeDaemon does not support this command
symbol.check.loaded.AMAuthInstallLogSetHandlerPtr == NULL
param.portal_base == 0
AXcpu_readreg
ret.cfg_write(R_DCM_GPIO)
complexes
ret.pka.nonce.status.err
ASTRIS_ERR_NOBOARDINFO
{%s} Batch attitude key created for %p thread %#llx key %lu
{%s} hostname:%s, flags:0x%08x
cpu_writereg_vals
ret.enableCpu
{%s:%s@%d} [%s] reading DTRTX\n
ret.rx-full.mddtrrx
{%s:%s@%d} Restoring from exception level[%d] other than 1,2 or 3\n
_a64cpu_check_edscr_err
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
KobaSWD
SPIXACT
ir-cmds
AMCNP_GFX
param.conn == NULL
ret.enableAll
AXcpu_hwwp_enable
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
CPENABLE
KICKINFO
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
unswitch_regset
fn._ocd_exec_instr.rsr.ddr.t1.2
The log file has been updated with all available diagnostics.\n
cpu_cache_clean
Pop
setTiming
Exploring IDE in JTAG\n
Could not enable KIS SoC Access\n
Unable to get version info from %s [error %s]
astris_identify_load_booster
ParseStringToStream
CPU0
complex-name
Die Addr Info LSB: %d Mask: 0x%016llX\n
Invalid current AP (%d), adopting APTABLE (%d)
internal.clear_probe_auth.chip == NULL
???
%d%%\n
Booster Bundle: %s\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, scratch=%d, %d)\n
NRF53Flasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
{%s} Error setting up jtag-ap target (%s)
Register file 36
JTAG Slave Unavailable
Access Port
=== Detailed %s Boosters ===\n
!!!! Critical Error: Thread %#llx key %lu relaxing attitude for %p when not attached - NOT ALLOWED !!!!\n
[DCC] Grabbing DTR failed: %s\n\n
{%s} %s DC cache clean complete, marking as clean
PKA Command Verify Completed, No Errors, but Probe Valid Not Set
fn._ocd_reg_r.DDR
fn._write_special_reg.reg_srn
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
AuthDebug::authenticate_probe - no need to authenticate\n
internal.authenticate.chip == NULL
internal.is_probe_authenticated.debug_auth == NULL
ret.explore_table == NULL
result.ide ==NULL
{%s:%s@%d} (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0\n
get_page_shift
Table 5–132
Table 5–137
RF29
ASTRIS_ERR_USB_EMPTY
Gathered Value is Not Number\n
{%s:%s@%d} [%s] reading BVR %d\n
baseReg
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
SCTLR__ELx
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
AXdp_read_with_recovery
EXPLORE_WITH_SEP_DEBUG
ret._a64cpu_read_gpr_cached
{%s::%s} ITE is not set: 0x%X\n
[REM_HWBP] bp%d\n
Successfully Authenticated DFT\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
fn._ocd_exec_instr.wsr.ddr.t1.2
fn._ocd_reg_w.ddr.reg_val
-Lite
set
{%s} Unable to read CPSR
ret.reg.write.K_DA_REG_NAME_AUTH_TEST_ENABLE
ECID is 0\n
R11
Error level
Hang Description:\n%s\n
astris_err_from_cs_type
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
astris_memap_bus_write
Explore: %u chip%s\n
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_COUNTER1
astris_command_complete
LMFLASH
pointer.h
run_steps
CPU AP-Type: %d\n
switch_regset
cpu is NULL
_read_general_reg
register    %-15s %3u     \"%-s\"\n
ParrotSWD
DCS10
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
target_el <= 3 && target_el >= 0
Optional Key: SubsystemMonitor not in preferences
RF3
fn._ocd_exec_instr.wsr.ddr.r0_r12
No loggers container
The document is empty.
AXjtag_srst deassert failure - %s (%d)
ret.test1
AuthDbg,TicketIdentifier
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
arch_hw=%d
KIS Readvals putting back the value
The debug port associated with this chip has not been explored.
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
AXdebug_auth_clear_auth
OCD.DEBUGCAUSE = 0x%8.8X
DBG_WRAP_REGS
AuthDebugWithTimer_t destructor \n
OCD control register, clear
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
FPI2C
str != 0 || len == 0u
newpos == 0 || path_[newpos - 1] == '/'
bits
{%s:%s@%d} [%s] getting GPR (diff mode)\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
astris_json_logger_delete_all
The debug port associated with this chip has not been explored\n
[ARCH32] Failed to write transfer register (EDDTRTX) the value to write
AXcpu_nmi
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
astris_setup_ap_mem
PARTNO_ARM7TDMI
{%s} explore with exploreflags 0x%X complete [%d chip%s]
PARTNO_SWDP_M0
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
Increasing length by: %d\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_STATUS
Register file 26
fn._write_special_reg.srn.regval
#KIS
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
n't
NRFFlasher: performing AHB-AP ERASE PAGES\n
FlamingoSWD
BLK
Reserve
buf != 0
CreateSchema
products
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
AXcpu_lacc_status_insert
%d.%drc%d
cpu_resume_translation
{%s::%s@%d [%s]} Error %s: collecting HW
EL1t
[AstrisAsync] Barrier hit!\n
X09 Part
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
Register file 52
fn._read_snr.excvaddr
Corruption detected selecting probe from probe server
SID
[FLUSH]\n
SP
EPC3
Processor status
%s.%s.%s
reader.h
axi-regs
{%s->%s} ERROR=%d(%s)
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
astris_cfg_memap
%s probe[*] from Probe Map Server [local host]
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
AXbooster_refresh
ELR_EL2
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
OK: address translation resumed for %s successfully
astris_poll_cmdstat
RF39
IOPlatformExpertDevice
opcode
{%s} %s resumed\n
INVALID KIS VERSION
AXdebug_auth_clear_sso_user
AMAuthInstallSupportDictionarySetInteger32
Error
Bug detected
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_53\n
RSM
chip-index
TAP IDCODE: 0x%X\n
[ARCH32] Failed to read transfer register (EDDTRTX)
Unknown Subcommand
more than one when unique required
%s_probe
 (%s)
Info_
EXPLORE_DAPONLY
param.bp_state.invalid.null
koko
pnav_create_probelist
Creating NRF54LFlasher: Chip: ID(%d) PID(%d) flags(0x%08X)\n
sso_user.sso_data_length == 0
Hardware model: %s
Another application is connected to
Connection aborted while choosing probe
Please answer y=yes or n=no.\n
cpu_resume
Target ID: 0x%X\n
{%s:%s@%d} [%s] doing IR scan (DTRRX EXTEST)\n
param.length.invalid.null
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
{%s:%s@%d} [%s] NRF54LFlasher: verify failed: len param is 0\n
shared_->refcount > 0
psr-partition-number
      Select of JTAG-AP port %u failed with %s\n
RF7
APPLE_SUBTYPE_UNKNOWN
AddState
set.chip_id
_a64cpu_read_gpr_hw
CPU_t
AXcpu_hwwp_info
   JEDEC ID: 0x%08X\n
TatsuServer
param.width.invalid
Failed to raise EL to %d to read register: 0x%llx
check_and_clear_cpu_msr_lock
CSSELR
internal.clear-auth.debut_auth == NULL
Probe %s removed before port determined\n
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s:%s@%d} [%s] doing IR scan (DSCR EXTEST)\n
{%s::%s} read OK but took %d tries
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT && != SP\n
failed to read memory; can't confirm breakpoint set
bad parameter(s) specified
match-info
DEBUG
[REMWP] wp%d\n
   {%s} Clearing HNONSEC on AP \n
No windowed register option.
ASTRIS_ERR_BADPROTOCOL
TRST
Failed to populate component info
{%s:%s@%d} [%s] reading SPSR\n
ret.rx-full.mddtr
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
StringEqual
Chip Revision: 0x%X\n
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
DLR_EL0
ERR
AXcpu_mmu_get_mair
   DPv3 baseptr is not valid (%X)\n
AXJTAG_EXPLORE_SEP_NOPWRGATE
api.is_prod.debug_auth == NULL
AXbooster_get_loaded_boosters
EICE
Failed to setup wp=%d
AXjtag_transmitraw
PARTNO_1176JZFS
~/Library/Application Support/Astris/astris_prefs.plist
Table 5–148
Register file 20
** CPU %s requires forced explore override flag on this SoC **\n
Discon
op_L32I_encode
user
ASTRIS_ERR_ASYNCSKIP
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
ret.get_hang_crumb
ret.write.msr_lock_reg
fn._read_special_reg.icount
Invalid category name
json
index < rangeCount_
setResult
[1500] Using %s.plist
ret.state_valid_entry_exit
{%s::%s@%d} [FALSE] dest_reg[%d] < 15\n
astris_memap_debug_writebuf
MESR
Die-Count: %d Current-Die: %d Die-Type: %d\n
astris_setup_connect
Could Not Match A Booster for %s\n
AXjtag_spixact
Failed to create optional file. Not fatal, moving on
Table 5–152
CRYPTO
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
ret.getCpuEnableStatus
{%s} Failed to get breakpoint count for %s: %s
wait_inflight_auth
AXdebug_auth_enable_test
!*!*!* Lightning header facing up.                                                    !*!*!*
Awaiting next chunk of big response
ret.restore_el.read
RF36
_init_params
_exec
NRF53Flasher: operating on NET core\n
cpu_hwwp_info
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
RF59
NRFFlasher: performing AHB-AP ERASEALL\n
Debug Port
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
NRF53Flasher: performing AHB-AP %d ERASEALL\n
remote probe closed connection
unable to obtain sysap
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
check_timer_and_clear_timeouts
RegionEnd
read.dlr_el0 NOT CACHED
NRF53Flasher: failed to aquire Debug port\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
SubsystemMonitor
dtoa.h
[%s] {%s->%s} clear async abort
AXdebug_auth_clear_dft_auth
not connected
{%s:%s@%d} [%s] doing IR scan\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
waitForNVMCReady
Cause of last exception
_read_pc
xfer_acmd_via_sock
EL0t
%s %s
armv7m-region-name
{%s:%s@%d} [%s] moving COPROC reg to GPR 0\n
_a64cpu_is_current_state_aarch64_hw
Portal Config Read
Failed to init from cpu desc armv7m cpu: %s \n
targetid/instance must both be set or both be unset
unable to read memory (using system ap)
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
cpu_sstep
Efficient-Core
{%s::%s} ERROR %d(%s) pre_resuming %s\n
ret.ite.read.edscr
_clean_invalidate_dcache_vaddr
ret.astris_create_cstr_from_cfstr
Table 5–147
JTAGAP
AXbooster_interface_create_swdflasher
tc1500
aarch64
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
     ARM %s watchpoints: %u\n
{%s} FAILURE - max length exceeded
fn._ocd_exec_instr.xsr.ddr.t1.1
Generic
cpu-ps-register
_read_register64
ret.exec.mrs.sysreg->scratch
{%s} ROMTABLE (nest=%d)\n
write_memory_dbgwrap
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Unique required when %d probes
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
{%s::%s} EDSCR with TXU set - unable to recover.\n
!!!! Critical Error: MIN_EL(sysreg)[%d] <= m_exception_level[%d] !!!!\n
before_deactivate_in_runBlock
status=%u, flags=%u, DSR=0x%8.8X, DCR=0x%8.8X
gor
0123456789abcdef
M23
{%s:%s@%d} [%s] NRF53Flasher: JTAG re-explore after net core enable failed\n
[AsyncSnapshot] #%zu: %s\n
Table 5–181
NRFFlasher: performing flash to addr (0x%08llX) of len (%zu)\n
XACT
{%s} unable to allocate probeInfo
{%s::%s} creating AP slave: name=%s
Failed to allocate space for table!
exit.exception_test_0
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s} calling _collect_hw on %s
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
CPUMonitor
Xtensa Option options: 0x%x
extra-wrstn
CortexM23
Bundle: %s NOT FOUND\n
Gathered Info:\n%s
CPU Core Number: %i\n
MCORE
astris_explore_enabler_init
RF12
fn._read_special_reg.reg_srn
data_reg=%u,opcode=0x%6.6X
invalid command
pnav_connect_probemap
PERSEIS
comparing against match entry %d: %s
  Nested path: parent='%s', child='%s'
astris_exc_bread_test_1
Could Not Find The Astris Init Function (%s) in %s
NRF
AXdisassemble_at_phys_addr
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
AXdebug_auth_authenticate
Invalid special reg. number %u
AXconn or json_out are NULL
astris_kis_poll_cfg_reg
vers_gateway < 2
{%s} status=%d being reported as Unknown
ret.reg.write.K_DA_REG_NAME_AUTH_TIMER_STATUS
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
\t[MATCH_SKIP] skipping entry
Unspecific syntax error.
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
preconnect
cpu_lacc_pc_status
IMX
resolve_platform_details
Aligned Address: %llx
go
Original Length: %d\n
fn._read_special_reg.dbreakc1
In Preflash\n
explore-level
\tLeft To Read (%d) < width (%d).\n
get_chipid
Raw level
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_52\n
end rev is not of expected format; skipping cpu_desc override\n
JSON string output is null
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s:%s@%d} [%s] NRF53Flasher: failed to write at addr 0x%08llX\n
{%s} strsep empty so match any probe [localhost]
Get
{%s} Failed to extract PID from table (%d); continuing anyway
   Debug Port: SELECT %X: DISABLED\n
Memory error PS register
{%s@%d} Connection to server failed, error=%d (%s)
{%s@%d} Failed to send probe command (error %d).
addMember.user
_read_memory_fast_try_with_chunk
EDDTRRX
param.tgt->ap.null
      AXap_write of R_JTAGAP_PSTA failed with error %s
TARGETSEL
no debug bus AP present when expected; after sysap is NULL
Using Built In SoCs\n
{%s:%s@%d} [%s] executing MRRC\n
{%s:%s@%d} exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this...\n
SoC has been setup using standard instantiation (setup result=%s)
EPS4
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Choose a device: 
[AstrisAsync] Pause when already paused!\n
General register 4
fn._ocd_exec_instr.wsr.WindowBase.r0_r12
Can't get OS build version - failed to create plist
UNKNOWN CODE
{%s:%s@%d} [%s] NRFFlasher: waitForRRAMCReady() failed\n
fn._ocd_reg_r.ddr
Missing a comma or ']' after an array element.
sel-sib-network
{astris_probed_print_events} not supported in this build configuration
ret.init_params.raise_to_min
   {%s} (DP): status=0x%X(%s) - %s\n
Shift-amount register
{%s@%d} Probe response payload read when no payload indicated.
{%s:%s@%d} [%s] getting GPR 0 (diff mode)\n
{%s:%s@%d} [%s] writing CSSELR[L2]\n
astris_cpu.cpp
internal.enable-timer-ovr.chip->soc == NULL
M1
Target was lost while connecting to
NoSOC
output_type
Invalid value for 'entry' tuple element - can't index
Error returned from explore_pid
astris_batch_attitude_cop
_read_gpr
{%s::%s} [%s] error %s writing SCTLR_ELx
Exception occured after executing MRS to bounce through scratch register
```
