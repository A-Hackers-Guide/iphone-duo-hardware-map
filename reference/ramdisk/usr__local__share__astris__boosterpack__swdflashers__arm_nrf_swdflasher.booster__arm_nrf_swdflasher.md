# `/usr/local/share/astris/boosterpack/swdflashers/arm_nrf_swdflasher.booster/arm_nrf_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,820,432 bytes.

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
{%s} Failed to get watchpoint mask for %s: %s
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Error %d (%s) opening history save file
NRFFlasher: performing verify at addr (0x%08llX) of len (%zu)\n
%s probe[%s] from Probe Map Server [local host]
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
  Nested path: parent='%s', child='%s'
AXconn_t Struct Is NULL
No version information found in booster: %s
--> localwrstn size=%3d debug=%d
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
Failed to sync prefs at end
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
NRF54LFlasher: performing CTRL-AP ERASEALL\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
Start Page: %d\n
   DPv3 bus is %u bits wide\n
      Read of JTAG-AP port %u PSTA failed with %s\n
tckrate_check returned error %s
{%s::%s} EDSCR with TXU set - unable to recover.\n
{%s::%s} [%s] error %s writing SCTLR_ELx
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
   {%s} Enabling debug unit\n
Probe %s Device Does Not Have LocationID
{%s@%d} Failed to find cached response
Setting bypass channel to: %d\n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
Unable to allocate memory for big response
Using Built In SoCs\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
[%s] E2H is set, virtualization is supported\n
Result while reading first entry: %s , entry val 0: 0x%X\n
TatsuServer Found: %s\n
Failed to convert CFArray to C Array\n
{%s} %s did not match any valid host
product-name: %s\n
{%s} Unable to read CPSR
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
Switch back to primate KIS: %s\n
Error status from AMAuthInstallSsoEnablePtr = %i
{%s:%s@%d} Critical error encountered:
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
%#09llx-%#09llx: %s\n
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Found form-factor specific channel %u for device '%s'
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
NRF53Flasher: CTRL-AP ERASEALL failed\n
[AsyncSnapshot] No snapshots collected\n
[AstrisAsync] Async mode %s
Result while reading second entry: %s , entry val 1: 0x%X\n
NRF_Flasher_t: writeflash failed: NULL connection and/or data param\n
Dart Dart Type: %s\n
Cannot create complex descriptions from NULL info\n
About to call fault reg latch, min_operating_el: %d\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
   Debug Port: Trying SELECT %X\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
{%s} error: %s
We are Deallocating\n
\t%s (%s)\n
New format for cip gen register, unsupported: %d\n
==== Exception Trace ====\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
register    %-15s %3u     \"%-s\"\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Could Not Find a DCM Portal
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
[%s] {%s->%s} clear async abort
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
   Debug Port has unknown type\n
choice: %d\n
NRF54LFlasher: AHB-AP ERASEALL success\n
Sending DYN Bypas Channel Set: %d
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
{%s} host:%s, flags:0x%08x
Asked To Read A Negative Register Index
Could Not Find Any Boosters\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[CACHEOP] %d, 0x%016llx, %d\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
[KIS] Portal Status: 0x%X\n
Asked To Write To A Negative Register Index
NRF53Flasher: performing AHB-AP %d ERASEALL\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
ERROR!! Couldn't save %s binary data\n
{%s} unable to allocate probeInfo
NRF54LFlasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
{%s::%s} %s pre_resumed\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
kext connect name %s\n
Probe %s selected
{%s@%d} socket connection is not available
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
CPU Core Number: %i\n
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
{%s} _resume_hw result = %s
[%s]\n
   DPv3 baseptr is not valid (%X)\n
{%s} FAILURE - NULL parameter
Probe %s with unknown status %s dropped from available list
{%s::%s} HDE not set on %s. Will re-enable.
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
NRF_Flasher_t: cannot readflash: APPROTECT is enabled\n
Both debug and xbs versions are set, maybe a bug: %s
Failed to get PMU Name
[%s] TGE is set so we traping to EL2\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
NRFFlasher: AHB-AP ERASE PAGES success\n
Spew change. old=0x%016llX, new=0x%016X
Could Not Allocate Booster Location Array
[1500] v2 plist missing required field 'taps'
[AstrisAsync] Discarding %zu completed command(s)\n
   Debug Port: SELECT %X: SKIPPING\n
ERROR!! write binary data parameters invalid\n
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
Init objects failed
--> extrawrstn %d
** Add the --with-force option or use the explore_override console command **\n\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
Replacing key with value
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
!*!*!* Lightning header facing up.                                                    !*!*!*
In Readflash\n
Could Not Get BoosterManagerUtility\n
{%s->%s} ERROR=%d(%s)
{%s} valid response from bridge
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
Required Key-Value is a string, and not an array. Old booster found: %s\n
Could Not Match A Booster for %s\n
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
NRF53Flasher: APPROTECT is %s\n
{%s} asc status=%d being reported as Unknown
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
Booster Value is Not String\n
Booster System Is Not Initialized Bailing\n
NRFFlasher: read %d bytes from target. Comparing...\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Old ProbeDaemon does not support this command
relay_set: %s = CMD_ERR (%s)
Failed to init from cpu desc armv7m cpu: %s \n
[KIS] Register Index: %llu\n
unable to obtain sysap
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
Found an async abort pending; clearing it\n
NRF53Flasher: word-aligned length (%zu)\n
[AstrisAsync] Failed to restart Async batch\n
NRFFlasher: performing AHB-AP ERASE PAGES\n
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
## armcpu: success status even though not all bytes written\n
{%s} Error looking up architecture (%s)
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
{%s::%s} creating placeholder for CPU: name=%s
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} Unable to read SP_EL0
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
Invalid current AP (%d), adopting APTABLE (%d)
   --> IDR: %08X\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
{%s} no matching 1500-to-* bridge
After powerup CMDSTAT=%08X\n
    %s(): %s
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
   {%s} (DP): status=0x%X(%s) - %s\n
{%s@%d} Received %d bytes when requested %d bytes [%s].
Astris Source Version: %s\n
Failed To Initialize Logging\n
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
AP is NULL
   Setting up AP IDR %08X\n
{%s} Unrecognized component: %08X, class %02X\n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
{%s} unsupported bridge type for %s
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
codeblock
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
   Created Fake Debug Port Debug Port
%s %3d'b%s\n
[1500] No %s.plist resource found
Failed to aquire Debug port.\n
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
Creating NRFFlasher: Chip: ID(%d) PID(%d) flags(0x%08X) IDE-base-addr(0x%08llX)\n
Failed to instantiate %s\n
%s\n
X00 Part
Increasing length by: %d\n
{%s} bridge returned SLVERR
Unable to convert plist file name to CFString: %s\n
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
Can't get hardware model - failed to allocate data buffer
\t\tARMv6 debug CPU xxx ID\n
Cached async_replay capability version: %u
NRFFlasher: timed-out waiting for NVMC ready\n
{%s@%d} Drain empty on decr [%s].
Full JSON that failed validation:\n%s
JsonLogger: Schema loaded successfully for category '%.*s'
Found another target for the plist\n
Complex CPU Name: %s\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
[%s] chipinfo is NULL
NRF_Flasher_t: unable to obtain sysap\n
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
   JTAG-AP: Identification = %08X\n
Successfully Authenticated Probe\n
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_53\n
Initialized %d 1500 bridges\n
{%s=>%s} AXconn_t has more than one chip
{%s::%s} failed: %s
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
[REMBP] bp%d\n
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
{%s} Exploring with option: %s\n
[1500] run_steps: unknown instruction '%s'
%s NOT configured\n
Preferences does not exists: %s, creating one.\n
Passed NULL booster without custom plist\n
Unable to allocate memory for next part of big response
{%s@%d} Found cached response
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
There is no CTRL-AP on the debug port\n
CPU %s not found or already removed from the map
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
[READ] cop %d -> 0x%08x\n
{%s} category=%d
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
 MEM-AP %X is hung\n
{%s} no chip found
HOSTID bit not set\n
[%s] {%s->%s} Transitioning to exception level %u.\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
Probe %s status: Busy
In Preflash\n
Could Not Allocate All Boosters Array
Component Group Offset: 0x%X\n
[AstrisAsync] Deactivate while async is not active!\n
[CLEANUP]\n
   CPUID: 0x%08X\n
Xtensa Option reg_file_size: %d
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_54\n
{%s}ERR: bypass_device_name is NULL\n
Min Component - %s\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
In Postflash\n
Passed NULL plist file\n
[SSTEP] bvr=%08x bcr=%08x\n
{%s::%s} error %s writing EDSCR %s
outstanding=%zu
ERROR: nothing to do; resuming address translation for %s without previously suspending it
X06 Part
AXconn or json_out are NULL
Failed to convert %s key @ index %d
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
batch_cmd_count: %d
Creating NRF53Flasher: Chip: ID(%d) PID(%d) flags(0x%08X)\n
replay_counter=%lu, last_replay=%d
{%s} Component ID read fail for 0x%llx (%s)
Can't get hardware model - failed to allocate data string
{%s} %s
NRF_Flasher_t: preflash: APPROTECT enabled: skipping quiesce(), cpuStatus() check\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
NRFFlasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
JsonLogger: Created with default schema version '%s'
We are Allocating\n
There is no debug port associated with this chip.
first read of CMDSTAT may fail if external reset occurred
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
Failed to convert kisHubLoc %s to unsigned long long
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
couldn't find CPU1. this is expected sometimes.
{%s} Failed to extract IDCODE from table (%d); continuing anyway
[%s] EL @ end of Collect: %d\n
{%s} %s DC cache already clean since last halt, skipping flush
replay_counter=%lu
{%s} _pre_halt_hw result = %s
{%s} host name(RSD): %s\n
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
Failed to create Xtensa CPU %s \n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s} %s DC cache clean complete, marking as clean
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
Failed to access new_cpu status
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
[AstrisAsync] Resume when not paused!\n
AP[%d]: unknown type\n
Successfully Authenticated\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
NRFFlasher: pageSizeBytes (%d) codeSizePages (%d) codeSizeBytes (%d)\n
Probe Map comm error %d(%s) %s
{%s@%d} Unknown CS command error [%d]
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Cannot create DART descriptions from NULL info\n
VBAR: %#llx\n
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Error %d (%s) opening cmd snapshost save file
Cleaning up Each Booster Manager\n
{%s->%s} m_exception_level=%u
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Xtensa Option num_high_pri_intr: %d
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
CPU Supported in Integration: %s\n
Unable to read GPR 28
[AstrisAsync] Activating async...\n
[AstrisAsync] Resuming Async Mode\n
Connecting to server, %s:%d
[PAR] Failed KIS Portal Access Preflight =%s (%d)
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
Going To Create Generic Xtensa Core, name=\"%s\".\n
SOC_t::{%s} CPU_t group=%d when group 0 expected
Section 1 Offset: 0x%llX\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
[INIT]\n
NRFFlasher: performing CTRL-AP ERASEALL\n
KIS translator version : %d\n
NRF53Flasher: comparing last partial %lu byte word\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
max_scan_bits is low: %d
\t[MATCH_SKIP] skipping entry
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
--> misc_wdr   size=%3d wirtestporten=%d
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
%s Bridge @ 0x%09llx-0x%09llx: %s
Portal Group Offset: 0x%X Entries: %d\n
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
read failed, using old cached as base: 0x%x
Probe (port=%d) with unknown status %s dropped from available list
KIS Readvals putting back the value
using standard products.plist for %s
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
{%s} DAP command nwords=%d trimmed to %lu\n
Probe %s removed prior to kick\n
NRF54LFlasher: CTRL-AP ERASEALL successful\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
Sprocket probe, for now I guess we will just say yes...\n
[%s] Booster System Is Not Initialized\n
NRFFlasher: CTRL-AP ERASEALL attempt %d\n
setCategoryValue: path='%.*s'
AXjtag_explore failure - %s (%d)
{astris_probed_print_events} not supported in this build configuration
Extract Offset: 0x%X for %d\n
{%s::%s} halting %s\n
{%s->%s} (top) current_el=%d
Subsystem Monitor Key does not exists: %s\n
!!!! DART Key %s is INVALID !!!!\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} L2 cache operation completed [%s]
[AstrisAsync] Barrier before pause\n
[KIS] Register Read/Write/Wrote: %d\n
NRF_Flasher_t: performing eraseflash\n
Could Not Get Bundle Out Array of Found Boosters\n
[1500] Error parsing TAP description
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
NRF53Flasher: checking APPROTECT status\n
Could not find portal by select %d, while interpreting result\n
{%s} no response from bridge
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
   Debug Port: SELECT %X: DISABLED\n
NRFFlasher: performing flash to addr (0x%08llX) of len (%zu)\n
NRFFlasher: flash success\n
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
%2d) %s %s [Busy]%s\n
{%s} connectName[%s]
Invalid Bundle: %s
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
[RESUME] Chip %x\n
Invalid current AP (%d), adopting latest (%d)
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
Failed to explore chip: %d
{%s=>%s} null reference to AXchip_t[0]
NRF54LFlasher: CTRL-AP ERASEALL failed\n
The debug port associated with this chip has not been explored\n
## dpw 0x%02X 0x%08X\n
{%s} ROMTABLE (nest=%d)\n
CPU Monitor key does not exists for: %s\n
unable to create connection
{%s[select]} timeout while waiting for data from the connection
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
gmtime() returned NULL, using epoch time
NRF_Flasher_t: AXjtag_srst assert failure - %s (%d)
XBS Version Modified: %s -> %s\n
DCCCTRL = %08X   res=%d\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
[KIS] Words (Read/Write/Wrote): %d\n
[%s] %d -> 0x%08x\n
[READ] cop64 %d -> 0x%016llx\n
## armcpu: bad status even though all bytes read (%d)\n
[AstrisAsync] Pausing Async Mode\n
   Debug Port: SELECT %X: AVOIDED\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
replayPreflight
Failed AP read of R_MEMAP_CSW res: %i
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
%2d) %s %s%s\n
Connected toProbe Map Server (single_port) 
Gathered Info:\n%s
Error returned from explore_pid
{%s@%d} neither socket nor kext connection available
comparing against match entry %d: %s
[1500] TAP key is not a valid integer
## dpr 0x%02X failed (%s)\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
Original Content: 0x%08x
{%s} status=%d being reported as Unknown
NRFFlasher: detected part code (0x%08X)\n
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
[1500] %s step %d missing required field 'instr'
{%s::%s} [%s] unsupported width %d
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
Connected to Probe Map Server
{%s::%s} creating AP slave: name=%s
Invalid value for 'entry' tuple element - can't index
{%s} (end) current_el is now %d
\n
successfully updated DEMCR
NRF53Flasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
AXmemap_readvals failure - %s
CPU AP-Type: %d\n
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s} Error setting up jtag-ap target (%s)
Original Length: %d\n
CPU Monitor[%i]: %s\n
{%s} hostname:%s, flags:0x%08x
CPU Subsystem: %s\n
--> wrstn_wir2 size=%3d dpcsoc=%d
{%s} [%s] m_exception_level=%u\n
## armcpu: success status even though not all bytes read\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
{%s} flags:0x%08x
Could not find TAP at index %d to attach 1500 bridge to\n
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
NRF53Flasher: addr (0x%08llX) is not in writeable portion of flash\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
Connection to server accepted
NRF54LFlasher: performing AHB-AP ERASEALL\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
NRF_Flasher_t: eraseFlash failed: NULL connection param\n
Enabling USB Gateway
Booster:\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
## dpw 0x%02X failed (%s)\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
Failed explore before forced KIS reset: %s\n
NRFFlasher: checking APPROTECT status\n
Value Types Are Not Strings\n
[READ] %d -> %08x\n
[AstrisAsync] Got ASYNC_RESTART response!
AP[%d]: MEM_AP_AXI\n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
Xtensa Option dbg_intr_level: %d
Set custom PSD json file: %s
NRF53Flasher: failed to aquire Debug port\n
{%s} calling _collect_hw on %s
** Unauthorized User/Network or ECID **\n
{%s} Found extra info in = %s, chopping string
Awaiting next chunk of big response
NRF54LFlasher: setting RRAMC base to 0x%08llX for nRF54L15\n
{%s} 0 words from probe when %d words left to read for reg %d
Table Size: %d\n
{%s} Failed to extract component info from table (%d); continuing anyway
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
NRF53Flasher: AHB-AP %d ERASEALL success\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
PKA Base: 0x%llX\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
Could Not Find Any Loaded Boosters of Type: %s\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
{%s} unable to find single_port probedaemon on port %d
{%s} drain_packets=%d [%s]
NRF54LFlasher: configured RRAMC config register with bits 8-13 set to all ones (0x%08X)\n
Generated JSON (first 500 chars):\n%.500s%s
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
## ARM32cpu_t::read_register %u\n
{%s::%s} write OK but took %d tries
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
connection created
{%s} %sing word #%d at address 0x%09llx: %s
Invalid SoC Booster. SoC Booster Requires PID\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s} %s resumed\n
{%s} %s status is '%s' [Status Read %d times]\n
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
[Auth Debug] Ticket Active, Debug Interface Locked\n
Astris Version Set: %s
\t\t%s\n
[1500] TAP %d missing required field 'chip-index' or 'irlen'
Target ID: 0x%X\n
Unable to read FP
{%s=>%s} no soc reference; falling back to direct cpu method
The log file has been updated with all available diagnostics.\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
{%s@%d} Failed to send probe command (error %d).
invalid IR command '%s'
{%s} bridge returned an error
Did Not Find Any Boosters For: %s \n
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} %s resumed\n
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
   {%s} Read AP's R_MEMAP_CSW\n
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
Match Count is Zero. This is invalid.
bypass-config-name: %s\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
{%s} timed out waiting for cpu to halt during collect
%s
[1500] v2 plist missing required field 'bridges'
{%s} Thread %#llx clearing key %lu
{%s} Failed to resume %s: %s
Fabric access is blocked. Expected if production unit, won't explore further.
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
NRFFlasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
%s: chip was NULL when attempting to release soc
AXjtag_srst deassert failure - %s (%d)
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
NRFFlasher: CTRL-AP ERASEALL attempt %d successful\n
response == NONE; failed to get kis target info\n
{%s}#%02X %s [%s]
%s SoC created
JsonLogger: Writing category '%.*s' to '%s'
Cleaning up Main Booster Object\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
AP[%d]: MEM_AP_AHB\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
Can't get OS build version - failed to open ReadStream
CPU DBG Ack: 0x%llx\n
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
Buffer is NULL
{%s::%s} read OK but took %d tries
NRF53Flasher: performing AHB-AP ERASE PAGES\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
NRF_Flasher_t: AXjtag_srst deassert failure - %s (%d)
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
process (%s) (%d) path: %s
%d%%\n
failed read from DEMCR - %s
Length is 0
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
{%s} %s: |%s|-|%s|
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
Kick has been requested by probe server
{%s} no TAP detected that supports 1500
Got an error writing 0x%X the DCM Control Register: %s
CPU Supported in Runtime: %s\n
DBGSTATUS = %08X   res=%d\n
NRF53Flasher: writing partial %lu byte last word\n
Breakpoint Enabled: %s
{%s} 0 words requested for read at address 0x%016llX
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
Raising to EL2 cause in Guest\n
DBGCTRL = %08X   res=%d\n
{%s} unmodified-probe_match = %s
no system bus AP present when expected
=== Loaded %s Boosters ===\n
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Unable to create pthread key for conenction. errno=%d %s.
HOSTID=0x%x which is invalid, skipping orientation check
Issuing request to Probe Map Server: %s
DEMCR write failure - %s (%d)
     ARM %s breakpoints: %u\n
NRF53Flasher: JTAG re-explore after net core enable successful\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
caller=%s, async=%d, iterations=%lu
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Can't get hardware model - failed to get property
Probe Map comm error %d(%s) %s [%s]
Cannot create CPU descriptions from NULL info\n
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
Portal Status, Changing STATUS and CMD/STAT to reflect
DEMCR read failure - %s (%d)
{%s::%s@%d [%s]} Error %s: checking exception
Invalid APTABLE (%d), so using most restrictive
{%s} setting up nameless target (address=0x%llx)
Hang Description:\n%s\n
Skipping CPU %s at 0x%llx: not present in IDE\n
SoC does NOT support IDE Explore\n
NRF_Flasher_t: cannot writeflash: APPROTECT is enabled\n
{%s} Error setting up memap target (%s)
Not Creating CPU: %s\n
In Eraseflash\n
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Found probe memory transfer in progress; clearing EDSCR.MA.\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
Xtensa Option ocd_address: 0x%llx
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s} read ESR EL1|EL2|EL3 (%d)
Hardware model: %s
connection about to be destroyed
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
dropping empty probeInfo (port=%u)
{%s=>%s} AXconn_t has no chips
relay_set: %s -> %d
error trying to unlock MSR %s
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
   DPv3 BASEPTR0 is 0x%08X\n
=== Ending Gather and Clear ===
{%s} Failed to extract CID from table (%d); continuing anyway
Error %d(%s) executing instruction 0x%08X
NRFFlasher: verify success\n
Could Not Get BoosterManager\n
--> debug      size=%3d acsr=%d
USER %s(%04u): %s(): %s
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
NRFFlasher: wrote %zu bytes\n
Failed to sync prefs at beginning
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
[%s] CPU BM Not Found, Bailing\n
Breakpoint Index: %d
CPU has no regions, maybe powered off?\n
Warning: chip exploration did not complete successfully (%s)\n
{%s} Error %d(%s) sending message
Required key: %s @ index %d is NULL\n
Protocol Version: 0x%X\n
Invalid file name: \"%s\". File names must not start with '.'
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
Aligned Address: %llx
NRF53Flasher: operating on APP core\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
NRFFlasher: JTAG re-explore after CTRL-AP ERASEALL failed\n
{%s::%s@%d [%s]} Error %s: resuming HW
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
[HALT] Chip %x\n
Probe %s removed before port determined\n
CPU: %s halting debug is now %s\n
Invalid Size Given for AP AP=%d Size=%d
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
[KIS] CMD: %s \n
Adding new booster path: %s\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
   ROM entry %d (level %u): AVOIDED\n
[PREFS] Key: %s - Val: NULL
NRFFlasher: CTRL-AP ERASEALL attempt %d failed\n
Could Not Allocate Mutable Dictionary For BoosterMangers
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} set=%u (sh=%u), way=%u (sh=%u)
Breakpoint Address: 0x%llx
Created Connection - : %s
{%s@%d} {%s[select]} %d(%s) [RETRYING]
\t[MATCH_FOUND] identified chip: %s
JsonLogger: Wrote %zu bytes to '%s'
NRF_Flasher_t: performing writelash to addr(0x%08llX) len (%u)\n
AXportal_t Is Not Valid Type - %d
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
{%s} probe_match = %s
NRF54LFlasher: flash success\n
Failed To Instantiate SOC From Booster\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
NRF53Flasher: detected part code (0x%08X)\n
[AstrisAsync] Deactivating async...\n
{%s} Unrecognized Component: %08X (class %u)
!!!! CPU Key %s is INVALID !!!!\n
error %s checking for data abort(uint32_t)
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s::%s} ITE is not set: 0x%X\n
NRF53Flasher: timed-out waiting for CTRL-AP ready\n
caller=%s, async=%d
Async is disabled for localhost connection
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Could Not Allocate Loaded Booster Array
[1500] IR command '%s' missing required field 'opcode'
error %s reading DAP PFR1
{%s} FAILURE - max length exceeded
{%s} FAILURE - malloc error
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
Probe %s Device Server listening on port %d
{%s} halting %s\n
{%s} Component ID read fail on romtable (%s)
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
ERROR!! Wrote %zd bytes, expected %zd\n
[KIS] Address: 0x%llX\n
NRF53Flasher: operating on NET core\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
The debug port associated with this chip has not been explored.
[1500] %s step %d: unknown instruction '%s'
{%s::%s@%d [%s]} Error %s: collecting HW
Unable to read LR
{%s::%s} [%s] !bpwp_initted, retrying init
   Debug Port not responding (%s)\n
Optional Key: CPUMonitor not in preferences
Using 10pin connector skipping orientation check
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s} 0 words from probe when %d words left to read for address 0x%016llX
NRFFlasher: addr (0x%08llX) is not in writeable portion of flash\n
{%s} probe_host = %s
%s probe[%s] from Probe Map Server [%s]
[COLLECT] Chip %x\n
NRF53Flasher: performing flash to addr (0x%08llX) of len (%zu)\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
%s probe[*] from Probe Map Server [local host]
NRF54LFlasher: verify success\n
Probe Type (%d) FW Version: %s does not support KIS.
DHCSR write failure - %s (%d)
{%s::%s} ERROR %d(%s) pre_resuming %s\n
[%s] {%s->%s} END handling exception
Type 'jebdump' to do scan/mem dump\n
%s given a NULL conn object
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
CPU AP-Select: %d\n
[1500] TAP %d missing required field 'ir-cmds'
{%s::%s} EDSCR in unexpected state. Returning %s.\n
Unable to read GPR %d
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
read_dbg failed to access R_v7M_CLIDR
{%s} Debug Base: %08X
Setting CPU %s is_boot_core to %d\n
There is no debug port associated with this chip\n
Bundle: %s NOT FOUND\n
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
Groups %d\n
Error %d(%s) executing instruction 0x%08X FAST
NRF53Flasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
Initialized Logging - %s
NRF54LFlasher: addr (0x%08llX) is not in writeable portion of flash\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
   JEDEC ID: 0x%08X\n
unable to identify chip
Init dbgwrap obj failed
end rev is not of expected format; skipping cpu_desc override\n
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
NRF_Flasher_t: checkAPProtect failed: %s (%d)
[AstrisAsync] Discarding response due to ASYNCSKIP state!
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
{%s} found single_port probedaemon on port %d
Probe %s USB-C location is %s
checking if relay \"%s\" is valid
haskis bit not set\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
Could not enable KIS SoC Access\n
  Error path [%s]\n
NRF_Flasher_t: AXjtag_explore failure - %s (%d)
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
probe event: %s
pc:  0x%16s cpsr: 0x%16s %s\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
{%s} ROMTABLE (dbgbase=0x%llx)
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
Koko probe, for now I guess we will just say yes...\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
coalesced-target: %s\n
[MEM] Uncompleted; DSCR = %08x\n
NRF53Flasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
dbgwrap halt failed, falling back to classic method
Failed to create optional file. Not fatal, moving on
{%s} match any probe [localhost]
** CPU %s requires forced explore override flag on this SoC **\n
error %s reading DAP MMFR0
Initial DSPSR_EL0: 0x%llx
{%s::%s} [%s] MMU not active - returning %s
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
ERROR: unable to suspend translation for %s
{%s} Error reading CPUID (%s)
   {%s} Probe requires overrun detect mode.\n
%s: []\n
   Debug Base: %08X\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
Gateway Version: 0x%X\n
component group %d\n
[INS_WP] 0x%016llx x %d\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
      Explore of JTAG-AP port %u failed with %s\n
start rev and/or end rev is NULL; skipping cpu_desc override\n
register lookup by name not supported when Astris is statically linked
AuthDebug::authenticate_probe - no need to authenticate\n
{%s@%d} gethostbyname failed, error=%d (%s)
no debug bus AP present when expected; after sysap is NULL
Cannot create SoC [unknown chip identity (%d)]
CPU Typehint: %s\n
{%s::%s} timeout while waiting for EDSCR ITE
type_hint not NULL, but creating a placeholder, this is off
   {%s} select %u port %u: %u chip%s\n
{%s} already connected
AXjtag_srst assert failure - %s (%d)
Complex CPU ID: %d\n
Failed to convert %s key @ index %d to a number with base of %d\n
Board ID: 0x%X\n
Unknown number of groups in the explore table; can't parse group attributes
runBlock
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
      Select port %u: AVOIDED\n
{%s->%s}
iter=%lu
SOC AP[%d]: JTAG_AP\n
Switch to primate res: %s\n
Going to do imago workaround\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Error %s connecting to server %s:%s [RETRYING]
Disconnected from Probe Map Server
{%s} unaligned %d-byte access at address 0x%09llx
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
[REM_WP] wp%d\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
** \tTatsu AuthDebug Triage | All     **\n
Probe %s removed during selection process
{%s} unable to allocate probe name
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
We are in clean up\n
dfu-Type: %s\n
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
NRF53Flasher: flash success\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
Failed to read IDE through DAP\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
=== Starting Gather and Clear ===
{%s} FIFO full, try again
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s} %s status failed. error: %d (%s)
{%s} failed (%s)
Complex Type: %s\n
Early dbgwrap base extracted: 0x%llx\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
{%s->%s} START handling exception
## dpr 0x%02X -> 0x%08X\n
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
Error closing %s [%d]
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
Width: %d not supported
\tPrologue Aligned Read Failed
{%s} PRIMECELL [DONE]
probetimeout retrying access...\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
Connect using RSD not supported\n
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
X12 Part
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
Awaiting response from Probe Map Server
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
[1500] Error parsing bridge '%s': missing required field 'select'
     0x%016llx: ERROR\n
AP[%d]: JTAG_AP (Exploring Later) \n
      AXap_write of R_JTAGAP_PSTA failed with error %s
{%s} probe_port = %d
received %zd bytes from Probe Map Server when have %zu
NRF54LFlasher: Writing %zu bytes in %zu chunks of %zu bytes\n
--> cmd        addrsize=%d datasize=%d
Please answer y=yes or n=no.\n
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s} [%s] error (%s) getting number of HW BPs
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
SSO info present but SSO disabled.
{%s} checking for single_port probe daemon on port %d
In Writeflash\n
Complex Address: 0x%llX\n
{astris_probed_print_events_from_json} not supported in this build configuration
TAP IDCODE: 0x%X\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
Successfully Authenticated DFT\n
Probe %s status: Idle
relay_get: %s = CMD_ERR (%s)
Unable to read SP
AP Only Explore was asked for, stopping here
   MEM-AP not enabled\n
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
NRF54LFlasher: checking APPROTECT status\n
NRF54LFlasher: verify mismatch: read back word number %d val (0x%08X) does not match expected val (0x%08X)\n
CPU (%s) has explore flag of: 0x%llx which is not set\n
getOrCreateValue: addMember failed, returning doc root
{%s} explore with exploreflags 0x%X complete [%d chip%s]
NRFFlasher: JTAG re-explore after CTRL-AP ERASEALL successful\n
{%s@%d} Unable to create socket
NRF54LFlasher: setting RRAMC base to 0x%08llX for nRF54L20\n
Booster Info:\n%s
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
Connected to Probe Device Server [Default Log]
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
SSO with no prompt being used
CPU with %s Not Created via Name
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
!!!! FILE RADAR: Don't know how to compare two values\n
Magic does not match: %#x vs %#x\n
Found %d APs
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
Can't get hardware model - failed to find matching IOService
Probe Map name of probe %d is: %s
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
No 1500 bridges specified\n
TargetSel Before Disable: 0x%x
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Initializing Booster Layer\n
CPU ASC Offset: %d\n
Die-Count: %d Current-Die: %d Die-Type: %d
[SSTEP] using BP %d\n
KIS Chip Found, Doing KIS Explore Setup
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
pmu-name: %s\n
[MEM] Aborted; DSCR = %08x\n
1: ARM64_SYSOP_ATS12E1R\n
NRFFlasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
Failed to convert kisLoc %s to unsigned long long
no system bus AP present with AHB, trying AHB5
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
1500 IR Commands:
Debug Clock Already Enabled
NRF_Flasher_t: APPROTECT enabled: doing CTRL-AP ERASEALL\n
Failed to get DFU Type
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
Probe %s with unknown kick response %s
{%s@%d} Connection to server failed, error=%d (%s)
NRF_Flasher_t: preflash failed: NULL connection param\n
Could Not Find Any Boosters of Type: %s\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
collect_responses
[AstrisAsync] replayConditionalCheck: condition hit!\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Failed to get Bypass Config
VBAR: %#x\n
NRF53Flasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
[ANAMOLY] Could not find AXcpu_t object for CPU\n
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s} Failed to extract die infofrom table (%d); continuing anyway
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
=== Found %s Boosters ===\n
%s constructed
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
\t[MATCH_TARGETID] FAIL <= unable to find DP
Could Not Create Dictionary From Booster: %s
Wrong width, should be either 4 or 8\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s} read %d words from probe when %d words requested
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
NRF_Flasher_t: APPROTECT disabled: doing AHB-AP ERASEALL\n
=== Detailed %s Boosters ===\n
!!!! Complex CPU Key %s is INVALID !!!!\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[WRITE] %d -> %08X\n
NRF53Flasher: wrote %zu bytes\n
   Debug Port: SELECT %X; error: %s, retrying..\n
Probe Map comm: request[%s], response[%s]
Size or Count provided are 0.
User created bundle found, ignoring version checking via plist
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
OK: address translation resumed for %s successfully
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
Creating CPU Returned: %s\n
Failed to convert CFString to C String.
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
     ARM %s debug CPU rev %d\n
\tReading left over chunk expected 0x%x got 0x%x\n
{%s} explore with exploreflags 0x%X completed with error [%s]
New Length: %d\n
{%s} strsep empty so match any probe [localhost]
Matched Booster: %s\n
error %s reading DAP MPIDR
{%s::%s} [%s] error %s reading SCTLR_ELx
NRF53Flasher: codeSizeBytes (%d)\n
{%s} collect result = %s
{%s} Failed to get breakpoint count for %s: %s
AP given is not a MEMAP
\tAligned Read Failed
{%s} bridge timed out
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
   {%s} APB/AXI address for target setup = 0x%llx\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
Caught a portal that we dont have a status map for: %d
NRF54LFlasher: word-aligned length (%zu)\n
Found the RTXCID Structure!\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
Xtensa Option non_tie_ranges: %zu range(s)
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
[1500] Error parsing bridge '%s': missing required field 'tap'
[INSWP] 0x%08llx wp%d rdwr=%X\n
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Can't get OS build version - failed to allocate buffer
Hang Radar Info:\n%s\n
Dumping Process Tree
{%s} Batch attitude key created for %p thread %#llx key %lu
can't find bid in response\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
Values Not The Type We Expected. Expected: Number and String\n
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
probetimeout retry failed logging as hang\n
SWDACKDELAY relay write failed\n
relay_get: %s = ERR
Logging Context Is NULL\n
Chip Revision: 0x%X\n
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
Failed AP write of R_MEMAP_CSW res: %i newval %i
Error status from AMAuthInstallSsoInitializePtr = %i
Production Fused Device\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
[READ] %d -> 0x%08x\n
{%s} restored el is now %d
NRF53Flasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
ERROR: unable to resume translation for %s
NRFFlasher: word-aligned length (%zu)\n
Setting STOP CLOCK to TRUE
{%s} error %s at line %d
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
[DCC] Grabbing DTR failed: %s\n\n
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
## apr %u 0x%08X -> 0x%08X\n
OS build version: %s
can't find pid in response\n
Could not find TAP at chip-index %d for v2 1500 config\n
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Complex Name: %s\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Creating CPU With Name: %s\n
Debug Base: 0x%llX\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
Highest EL: %d, -- Min Op EL: %d
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
using multi-target booster products_%s.plist
{%s->%s} current EL (%d) already == target EL.\n
Hang Address: 0x%016llx\n
{%s@%d} IOServiceClose failed, err = 0x%08x
Creating NRF54LFlasher: Chip: ID(%d) PID(%d) flags(0x%08X)\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s=>%s} null reference to CPU_t object, `cpu->state`
{%s} connectName[local host]
{%s} %d(%s) [RETRYING]
Dart CPU SID(s): %s\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
Can't get OS build version - failed to create plist
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Unable to read PC
{%s::%s} [%s] length=%u when width=%d
NRF53Flasher: AHB-AP ERASE PAGES success\n
100%%\n
Breakpoint Size: %d
SSO is DISABLED\n
Error Reading Device Production-Fusing\n
Found match - bypass_device: %s; channel: %d\n
%s: not supported.\n
{%s=>%s} null reference to AXconn_t record, `conn`
Can't get OS build version - failed to create URL
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
KIS Preflight No Need To Write to AP CSW
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
{%s::%s} ERROR %d(%s) resuming %s\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
[1500] Error parsing v2 bridges
Die Config Disabled\n
CPU %s already in the map with status: %d
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s} probe device server closed the connection while trying to read data (at recv)
--> master     size=%3d localwrstn=%d debug=%d
## ARM32cpu_t::read_register 64 bit 0x%x\n
[REM_HWBP] bp%d\n
{%s} Failed to get breakpoint mask for %s: %s
Xtensa Option options: 0x%x
{%s[recv]} %d(%s) [RETRYING]
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
[FLUSH]\n
WARNING, reserved / slide bits not zero! Zeroing out!\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
Previous authentication in-flight, wait for it to finish\n
Xtensa Core %s NOT configured\n
Can't get hardware model - failed to convert to C string
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
{%s::%s} EDSCR with RXO set - unable to recover.\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
Using Built In CPUs\n
{%s} handle ROM entry %d (level %u): %08x
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
Request Dict:\n%s
NRFFlasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
Dart Coastguarded CPU: %s\n
{%s:%s}: cpu powered off: unable to access a register for this CPU
2: ARM64_SYSOP_ATS12E1R\n
Going To Create Generic ARMV8\n
{%s} Reading base 0x%llx entry's component ID
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
AXmemap_nrfidentifyfamily: identified AXNRF_FAMILY_52\n
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
Required Key-Value is a string, and not an array. Old booster found\n
\t%s\n
     0x%016llx: 0x%04x      %s\n
NRF53Flasher: timed-out waiting for NVMC ready\n
JsonLogger: Loading schema for category '%.*s' from '%s'
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
Failed to allocate space for table!
{%s::%s@%d [%s]} Error %s: flushing HW state
{%s} m_exception_level(%d) != current_el(%d)
Failed to convert primateHubLoc %s to unsigned long long
Successfully connected to server, %s:%d
Could Not Allocate Info Keys Array
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
failed write of 0x%08X to DEMCR - %s
astris_get_async_ver failed with error: %s
relay_get: %s = %d
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
NRF_Flasher_t: readflash failed: NULL connection and/or data param\n
1: ARM64_SYSOP_ATS12E1W\n
NRF53Flasher: performing CTRL-AP ERASEALL\n
[AstrisAsync] Pause when already paused!\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
Gateway is KIS, seeing what probe this is\n
AXportal_t Struct Is NULL
{%s::%s} [%s] MMU is already active - returning %s
## memapr %u 0x%016llX %d -> 0x%08X ...\n
{%s@%d} Unable to connect to server, %s:%d
{%s@%d} Received %d bytes when requested %d bytes.
Matched via Bundle ID\n
{%s} Failed to extract target ID from table (%d); continuing anyway
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
probing %s status\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
{%s@%d} Timeout while sending probe command.
[%s] Booster System Is Not Initialized Bailing\n
NRF_Flasher_t: cpuStatus failed\n
KIS Writevals putting back the value
Dart Base Address: 0x%llX\n
{%s} skipping dcache flush, cache already clean
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
{%s} Extracted CIP Gen Number from table  (%d)
Modified Word To Write: 0x%08x
Probe %s with unknown port response %s
Taking gateway control failed
sending abort to clear a timeout\n
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
Can't get hardware model - failed to create string
{%s@%d} Probe reported connection lost [PROBEEOF].
No 1500 bridges or TAPs specified (v2 plist)\n
NRF_Flasher_t: performing readflash from addr(0x%08llX) of len (%u)\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
[PREFS] Key: %s - Val: ??
Had an error during transfer: %s
Trying to use size of 8 on not AXI bus
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
JsonLogger: Creating new category '%.*s'
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
X09 Part
Subsystem Monitor[%i]: %s\n
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
NRF54LFlasher: performing flash to addr (0x%08llX) of len (%zu)\n
unknown match criteria type: %d
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
Exception %d Stack Trace
==== User Error Messages ====\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
   Debug Port: SELECT %X: SKIPPING (%s)\n
   {%s} Clearing HNONSEC on AP \n
## apw %u 0x%08X 0x%08X\n
[KIS] Portal ID: %d\n
BoosterManager Types:\n
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
Unable to disassemble_at_addr 0x%016llx
[AstrisAsync] Barrier hit!\n
NRFFlasher: writing partial %lu byte last word\n
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
We Are Matching Development Booster\n
Pages %d\n
{%s} _pre_resume_hw result = %s
{%s} empty response string provided
Kick off the current process using probe %s? (y|n)\n
NRF53Flasher: CTRL-AP ERASEALL successful\n
{%s} probeList has probeCount of zero
{%s} drop ProbeName %s
NRF54LFlasher: performing verify at addr (0x%08llX) of len (%zu)\n
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
Turning Debug Clock On
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
Probe Map Server Information: %s
Banana split probe, for now I guess we will just say yes...\n
DEMCR: 0x%08X -> 0x%08X
{%s} wrote %d words to probe when %d words provided in request
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
NRFFlasher: AHB-AP ERASEALL success\n
We are done with clean up\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
Too many portals, we are at portal: %d while max is %d\n
Stepping Stone Final =  %#x\n
## armcpu: bad status even though all bytes written (%d)\n
[AstrisAsync] replay preflight: Async not active!\n
SoC has been setup using standard instantiation (setup result=%s)
{%s@%d} Connection to server rejected, error=%d (%s)
Booster Bundle: %s\n
Chip %x Status = %d\n
[REMWP] wp%d\n
NRF53Flasher: read %d bytes from target. Comparing...\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
NRFFlasher: APPROTECT is %s\n
CPU Die: %d\n
UPDATE cop64 %d -> 0x%016llx\n
NRF53Flasher: performing verify at addr (0x%08llX) of len (%zu)\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
[%s] AP, DP, or chip given is NULL
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
{%s} already collected %s, skipping
NRFFlasher: timed-out waiting for CTRL-AP ready\n
Invalid character [0x%02X] received from Probe Map Server
comparing against match entry [pid] %d: %s\n
SoC BM Not Found, Bailing\n
could not perform cpu_preflight
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
!*!*!* ****************************************************************************** !*!*!*
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
NRF54LFlasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
Translate Stage Chosen: %d\n
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
%s [RETRYING]
{%s} probe [%s] added to list
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
{%s} NOMEM
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
[1500] Error parsing bridge: %s
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
{%s=>%s} AXconn_t has no SoC object
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
NRF54LFlasher: comparing last partial %lu byte word\n
We are at max iterations, still didnt get full JSON
Die Config Disabled
Can't find descriptor for group - can't index\n
{%s::%s@%d [%s]} Error %s: synchronizing context
[ARM64 INS_WP] 0x%016llx x %d\n
Explore: %u chip%s\n
NRF54LFlasher: read %d bytes from target. Comparing...\n
Complex CPM Offset: 0x%llX\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
{%s} pmgr status=%d being reported as Unknown
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
[Auth Debug] Disabled\n
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Problematic JSON value:\n%s
Complex ID: %d\n
[1500] Error parsing IR command: %s
{%s::%s} NULL parameter
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Choose a device: 
{%s} error %d(%s) reading data from the connection (at recv)
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
Proceeding with full explore instead of instantiation
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
NRF_Flasher_t: unable to obtain CTRL-AP\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
[AsyncSnapshot] #%zu: %s\n
   Debug base is in legacy format\n
## memapw %u 0x%016llX 0x%08X\n
      Select port %u: already explored..re-exploring\n
{%s} %s: |%s|
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
Could not find bundle () in given array: %s\n
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
{%s} Failed to extract ECID from table (%d); continuing anyway
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
      Select of JTAG-AP port %u failed with %s\n
[ARM32cpu_t::_read_register64] 0x%08x\n
{%s} Failed to single-step %s: %s
[Auth Debug] External Debug Interfaces Open\n
AuthDebugWithTimer_t destructor \n
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
{%s[select]} %d(%s) [RETRYING]
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
NRF54LFlasher: detected part code (0x%08X)\n
Valid Portal
2: ARM64_SYSOP_ATS12E1W\n
Failed to create CPU %s - %s\n
CPU state %d
     0x%016llx: 0x%08x    %s\n
[AstrisAsync] Activate while async is already active!\n
{%s} _halt_hw result = %s
OK: address translation suspended for %s successfully
{%s} host = %s
ERR: conn->nchips != 0; looks like chip is explored\n
Stop Clock: %s\n
EICE chip %x initialized\n
{%s}#%02X cmd: %s, resp: %s
{%s} invalid data width %d bytes
CPU Name: %s\n
CPU Address: 0x%llX\n
Error %d (%s) while expanding ~ for Astris history save\n
NRF54LFlasher: unknown part code 0x%08X, defaulting RRAMC base to 0x%08llX\n
error %s checking for data abort(first)
Unable to read CPSR
     ARM %s watchpoints: %u\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
Probe %s Device Not Connected on USB-C Port
sent %zd bytes to Probe Map Server when sending %zu
{%s@%d} Timeout while attempting connect to server
[1500] Using %s.plist
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
Portal Group Base: 0x%llX \n
[%s] cop %d -> 0x%08x\n
{%s::%s} [%s] error %s from _synchronize_context.
SoC not identified by IDCODE - enumerating instead of instantiating
      Read of JTAG-AP port %u CSW failed with %s\n
NRFFlasher: performing AHB-AP ERASEALL\n
--> 0x%02x = %s
DBG_CPU: %s\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
{%s::%s} creating CPU
{%s::%s@%d [%s]} Error %s: initializing cache parameters
Error while trying to authorize: %d - %s\n
Failed to get KIS translator version\n
{%s} Failed to extract portal info from table (%d); continuing anyway
Map is empty, not removing CPU %s
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
NRF_Flasher_t: performing preflash\n
Gathered:\n
Gathered Value is Not Number\n
error %s checking for data abort
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
\tTatsu AuthDebug Triage | All\n
[PREFS] Key: %s - Val: %s
start rev is not of expected format; skipping cpu_desc override\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Initializing (%s) Booster's Astris API\n
NRF53Flasher: verify success\n
%s status is '%s'\n
   {%s} Before powerup CMDSTAT=%08X\n
Optional Key: SubsystemMonitor not in preferences
Failed to convert primateLoc %s to unsigned long long
{%s} handle ROM entry
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
NRF54LFlasher: DP: flags(0x%08X) num-APs(%d) AP: select(%d) IDR(0x%08X) flags(0x%08X)\n
NRF54LFlasher: verify mismatch: byte num %d val (0x%08X) of last word does not match expected val (0x%08X)\n
Before astris_kis_init_dp, CMDSTAT=%08X\n
[1500] TAP %d: irlen must be > 0 (got %d)
\tReading left over chunk 0x%x @ 0x%llx\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
{%s@%d} Probe response payload read when no payload indicated.
write to CMD/STAT failed - %s
Unable to register assert upcall %s (Insufficient memory)
Selecting polling method %s
{%s} Class 9 ROMTABLE (nest=%d)\n
Xtensa Option num_wp: %d
NRFFlasher: UICR addr (0x%08llX) + word-aligned len (%zu) extend past UICR region end (0x%08llX)\n
Got an error reading the DCM Control Register: %s
[1500] Detected plist version %d
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
{%s::%s} waiting for EDSCR ITE
Variables not setup
SoC has been setup using standard instantiation (setup result=%d)
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
Failed to read ide_table from KIS explore
[%s] %d -> %08x\n
{%s::%s} cpu powered off: failed init() %s
{%s:%s@%d} Critical error [radar already requested]
%s probe[*] from Probe Map Server [%s]
{%s@%d} Unknown CS code [%u]
{%s} bridge returned DECERR
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
\tLeft To Read (%d) < width (%d).\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Exc Cause: 0x%x - Exc Vaddr: 0x%x
Can't get OS build version - failed to get build version
NRF_Flasher_t: check APPROTECT failed\n
CPU Explore: 0x%llX\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
no debug bus AP present when expected
!!!! Complex Key %s is INVALID !!!!\n
{%s} Failed to extract PID from table (%d); continuing anyway
[HALTED] dfsr = 0x%08x\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
{%s} select success without file descriptor set
Could Not Find Booster Entry Function: %s\n
CPU PS-Register: 0x%llX\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
## memapr %u 0x%016llX -> 0x%08X\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
Multi target booster, checking for %s.plist\n
{%s} Failed to get watchpoint count for %s: %s
Probe %s LocationID Info is %s
NRF54LFlasher: codeSizeBytes (%d)\n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Xtensa Option num_bp: %d
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
Failed to find a plist for this soc %s
    INFO(%u,%d): %s(%04u): %s(): %s
Error happened when reading edscr. Retry #%i\n
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
[AstrisAsync] astris_async_override_disable_async: conn is NULL
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
NRFFlasher: comparing last partial %lu byte word\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
Exploring IDE in JTAG\n
%s construction failed
Can't get OS build version - failed to create ReadStream
Previously dumped the process tree, skipping
AXmemap_nrfidentifyfamily: targetID = 0x%x, partNumber = 0x%x\n
There is no system bus access port on the debug port
--> psr        size=%3d bit=%d
Failed to find a product plist for this soc %s
Result while reading third entry: %s , entry val 2: 0x%X\n
AP[%d]: MEM_AP_APB\n
Dart Name: %s\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
Async is disabled for current seesion
\tLeft Over Chunk Read Failed\n
{%s} DEVARCH read fail in CoreSight component (%s)
## apw %u 0x%08X 0x%08X ...(%d)\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
Connected to Probe Device Server [Log File %s]
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
{%s} Error reading PID (%s)
SoC must have a DAP
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
astris_memap_bus_write
FlamingoSWD
unable to identify chip
[KIS] Address: 0x%llX\n
BT_PHY
param.reg.invalid.outofrange
addr=0x%8.8X, index=%d, size=%u, flags=%udata=%u, enabled=%u
NRF54LFlasher: setting RRAMC base to 0x%08llX for nRF54L20\n
cpu_lacc_pc_status
NRF_Flasher_t: APPROTECT enabled: doing CTRL-AP ERASEALL\n
OSLAR_EL1
{%s:%s@%d} [%s] NRF53Flasher: failed to erase flash at 0x%08llX\n
read_resp_cmd_via_sock
DCS_BC2
ret._a64cpu_raise_el_hw.el=2.to_read_hcr
far_el3
cpu did not stop. OCD.DSR=0x%8.8X
default
{%s:%s@%d} [%s] unable to read command response\n
CPU.ARMv7
kob
NRF54LFlasher: failed to calloc readBackBuf
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Output
schema_version
WrProt
ret.wait_ite_set
Failed to safe raise to EL=%d
RF42
/
receiving response
USER
Connecting to server, %s:%d
The surrogate pair in string is invalid.
WCR0_EL1+index
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
NONE
AXJTAG_EXPLORE_SEP_NOPWRGATE
ret.nonce_generation.timedout
{%s} %s did not match any valid host
HENRY
astris_batch_attitude_cop
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
SPSR_EL3
ret._setup_bp
ret.reg.read.K_DA_REG_NAME_ACTIVE
Exception occured after executing MRS to bounce through scratch register
Loop-end address
%s/%s
ret.rx-full.mddtrrx
\"%s\" not an implemented register
fn._read_special_reg.srn.regval
Previously dumped the process tree, skipping
HTTP transaction running in background
cpu_lacc_count_remove
astris_kis_poll_cfg_reg
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
AXcpu_status_pmgr
value=0x%8.8X
AXconn_get_pid_bid
DEBUG
ETM
result.read_vals(portal_group)==
ESR_EL2
L1_DATA
M
ViewSWD
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
We are Deallocating\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
User
tokens_ == 0
Reserve
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s:%s@%d} [%s] NRF53Flasher: nRF part code 0x%08X is not supported\n
cpu_cache_cleaninv
String
{%s::%s@%d [%s]} Error %s: checking exception
astris_user_default_copy_nickname_for_primate
astris_handle_romentry
X09 Part
EXCSAVE6
Register file 42
ASTRIS_ERR_NOTPRESENT
{%s} %d(%s) [RETRYING]
RegionStart
{%s:%s@%d} [%s] Setting WP length not currently supported: %u\n
General register 1
consistent debug root reg undef
NRF_Flasher_t: checkAPProtect failed: %s (%d)
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
{%s:%s@%d} [%s] executing MCRR\n
{%s::%s} failed: %s
connection about to be destroyed
SAM2
DOCK-CH-DATA
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
RF39
FWUPDATE
couldn't find CPU1. this is expected sometimes.
AXbooster_print_all_booster_managers
Request Dict:\n%s
check_timer_and_clear_timeouts
PROBED_USB_RSP_TIMEOUT
API.
:
PROBED_ASYNCSKIP
MEMAP_APB
ret.dock_disconnect_mode
Could Not Get BoosterManager\n
{%s:%s@%d} [%s] doing JTAG scan (DSCR)\n
GROUP
   Debug Port not responding (%s)\n
write_memblock_dbgwrap
arch_hw=%d
host_to_components
AXchip_find_dap
Data break 1 address
file/object not found
_update_register64
Exception virtual address
MMID
?
Could Not Find a DCM Portal
SWDFlasher
AFT
ret.read.gpr_0
EXPLORE_NO_TAP_RESET
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
createSOC
b
result.dbgap==NULL
astris_cpu.cpp
SSO is DISABLED\n
Data TLB configuration
u64toa
UserCreated
jtag_get_soc
{%s:%s@%d} [%s] NRFFlasher: failed to read size(%d) count(%d) from addr (0x%08llX)\n
Using 10pin connector skipping orientation check
INIT
v8@?0
\t%s (%s)\n
cpu-apselect
{%s:%s@%d} [%s] doing IR scan (DIDR INTEST)\n
{%s->%s} exec: aarch64_add_imm(scratch=%d, REG_SP)\n
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
m_regstate.a64r_dspsr_el0
A
[
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
AuthDebug_t::init failed (AuthDebugWithTimer_t)
Kick required to connect: Busy probe
source[i] == '/'
Put
baseReg
{%s:%s@%d} [%s] NRF53Flasher: verify failed: addr(0x%08llX) + word-aligned len (%zu) is not in any writeable regions\n
axlog_assert_upcall
XBS Version Modified: %s -> %s\n
AXbooster_interface_create_soc
{%s} Component ID read fail on romtable (%s)
ret.reg.read.K_DA_REG_NAME_PKA_BASE_HI
#KIS
checking if relay \"%s\" is valid
ARC
encodings.h
Had an error during transfer: %s
Section 1 Offset: 0x%llX\n
{%s::%s} EDSCR with TXU set - unable to recover.\n
...
s != 0
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
fn._ocd_reg_r.dsr
(%s) %s
' written at document root (failed to create parent object '
Stringify
Groups %d\n
failed to read memory
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Table 5–177
set.astris_version
Failed to read DCM GPIO (0x%x)
{%s->%s} START handling exception
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
AXdebug_auth_is_dft_authenticated
Failed to get Bypass Config
{%s:%s@%d} [%s] NRF53Flasher: cannot erase UICR\n
fn._ocd_exec_instr.l32i.r1.r0
ASTRIS_ERR_TGTSTATE
Schema validation failed at: %s (keyword: %s)
   Debug Port: SELECT %X: AVOIDED\n
R1
Register file 35
Table 5–147
GetState
basic_string
dart-type
match-info
OUTEN_RESTART
ret.reg.write.K_DA_REG_NAME_NONCE_1
Memory error check register
fn._ocd_reg_w.ddr.t1_save
fn._read_special_reg.dbreaka1
Required key: %s @ index %d is NULL\n
DCS_BC0
[MEM] Uncompleted; DSCR = %08x\n
HDE
{%s->%s} TGE is set, can't go lower to EL1
Unable to restore EL0
{%s} exec: IC_IVAU_X1_ENC\n
EXPLORE_NOPWRGATE
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
Failed to write in DSPSR_EL0 into SPSR_EL%d before changing Exception Level. (reg_val=0x%08llX)
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
param.val.invalid.>max
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
No probes
ret.buildCategoryJson
There is no system bus access port on the debug port
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
RF52
fn._ocd_exec_instr.WSR.DDR.R1
CortexA72
\t[MATCH_TARGETID] FAIL <= unable to find DP
ASC
KIS translator version : %d\n
cpu_translate
appendToArray
{%s:%s@%d} [%s] executing MSR\n
[ARM64] exec(DCPSX_BASE_ENC)
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
## dpr 0x%02X failed (%s)\n
General register 0
RF2
ARM7
init_astris_api
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
could not perform cpu_preflight
Already connected to
Misc_Rtx117x_t
[PREFS] Key: %s - Val: %s
{%s:%s@%d} [%s] NRF54LFlasher: flash failed: addr(0x%08llX) + word-aligned len (%zu) do not fit in any writeable regions\n
The document root must not be followed by other values.
KIS
astris_kis_cfg_writevals_swd
## ARM32cpu_t::read_register %u\n
astris_cpu_get_cl4_debug_signpost
RF11
{%s} error %d(%s) reading data from the connection (at recv)
getOrCreateArray
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
ret.read.edscr.masked
virtual int ARMv7mcpu_t::_resume_hw(bool)
generic error injected by probed
{%s} FIFO full, try again
{%s:%s@%d} [%s] doing JTAG scan\n
ParrotSWD
cpu_cache_info
{%s} [!is_64] exec: ISB_SY_ENCODING\n
AXcpu_lacc_count_read
???
Booster Value is Not String\n
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
createCPU
Failed AP read of R_MEMAP_CSW res: %i
astris_soc_check_debug_root
AXchip_get_board_rev
ADI
param.bundle_url==NULL
instruction size too large
: [
L2
ret.get.da
ASTRIS_ERR_FAILURE
%s %s\n
dart-coastguarded-cpu
{%s} Extracted CIP Gen Number from table  (%d)
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_COUNTER2
SWD KIS Command is NOT Multiple of 8
KIS-SIM
Apple
_resume_translation_hw
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
SCOMPARE1
GetDouble
recordTargetCoreInfo
\nPKA Command Verify Error In Check-Response (status = 0x%08x, should be 0)\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
{%s} already collected %s, skipping
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
AVE
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
BLK
AXchip_fromreset
  Nested path: parent='%s', child='%s'
wir-wrstn
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
astris_cpu_raise_el
Table 5–155
tar
to
cpu_readreg
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
ret.home_url == NULL
AXmemap_nrfidentifyfamily: targetID = 0x%x, partNumber = 0x%x\n
NRF54LFlasher: comparing last partial %lu byte word\n
{%s:%s@%d} [%s] executing STCpi(uint32_t)\n
AuthDbg,EnAppleDebugExternal
fn._tie_read_word32.last
var.bp.invalid
%s/%s-%s%s%s.bin
PARTNO_KIS
Successfully Authenticated Probe\n
Key is null
newpos == 0 || path_[newpos - 1] == '/'
astris_ide_get_soc_stop_clock
100%%\n
probe
_create_cpus
--> wrstn_wir2 size=%3d dpcsoc=%d
{%s} Failed to extract ECID from table (%d); continuing anyway
New format for cip gen register, unsupported: %d\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
JTAG
AXchip_getinfo
Table 5–180
Table 5–170
NRF_Flasher_t: cannot readflash: APPROTECT is enabled\n
ret.cfg.read.swd
AXcpu_hwbp_enable
SWD
MAC16 data register 1
Table 5–149
RF50
param.s0.invalid.!=0
%s on %s
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
NRF53Flasher: performing CTRL-AP ERASEALL\n
operation not supported
{%s} already connected
APF
{%s} %s status is '%s' [Status Read %d times]\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Double exception PC
fn._read_pc
Failed to convert %s key @ index %d
ret.memap.write
X00 Part
General register 9
AXconn_probelist
Error:ASTRIS_ERR_BADPARAM(-29)
co_coredump
dart-cpu-sid
timeout or watchdog expired
opcode
Failed calling AppleSOC_t::switch_taps\n
1.0
{%s::%s} [%s] unsupported width %d
Breakpoint Enabled: %s
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
fn._reg_desc_lookup_by_name
var.m_debug_interrupt_level.invalid.outofrange
environment variable not found
Booster:\n
reg_name (\"%s\") not implemented, missing Xtensa option.
Parameter length = %u > 4.
[AstrisAsync] replay preflight: Async not active!\n
virtual_memory_bytes
{%s} unaligned %d-byte access at address 0x%09llx
mxwrap-address
unable to raise to EL1 (to suspend translation)
** Unauthorized User/Network or ECID **\n
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
time out reported by probe
NRFFlasher: addr (0x%08llX) is not in writeable portion of flash\n
root_ != 0
result.extract_table_info==
{%s->%s}[cached] %s[0x%X] = 0x%08llX
   JTAG-AP: Identification = %08X\n
EPS4
reg_srn=%u, \"%s\", regval=0x%8.8X
Parameter len = %d > 64.
unable to transfer command to/from remote probe
{%s} match any probe [localhost]
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
OS build version: %s
Component is not present
codepoint <= 0x10FFFF
Failed to write DCM GPIO (0x%x): 0x%x
Could Not Create Dictionary From Booster: %s
result.booster_api_vers==NULL
AXexplore_enable_cpu_pattern
internal.is_probe_authenticated.chip->soc == NULL
fn._ocd_reg_r.ddr.memval_tgt_32
unpack_response
Error status from AMAuthInstallSsoInitializePtr = %i
R5
param.reg_name.invalid.unimplemented
Warning: Default logging location requested when running as root (using [%s])\n
APPLE_SUBTYPE_UNKNOWN
virtual int ARMv6cpu_t::_halt_hw()
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
{%s} bridge returned DECERR
instance
_write_memory_fast
*
Previous attempt to connect to probe failed: %d (%s). Retrying...
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
ARMV7
sending abort to clear a timeout\n
{%s::%s@%d [%s]} Error %s: collecting HW
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
Failed to setup wp=%d
ret.m_lam.paccess_read
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
{%s:%s@%d} [%s] writing DTRRX(first)\n
EDRCR
Error Reading Device Production-Fusing\n
is_external_open
AXconn_probed_command
{%s} read ESR EL1|EL2|EL3 (%d)
high
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
internal.is_dft_authenticated.chip->soc == NULL
SWDRESET
shared_->refcount > 0
AXconn_t Struct Is NULL
{%s} Unable to read CPSR
AXcpu_lacc_pc_status
AXmemap_read_modify_write
No 1500 bridges or TAPs specified (v2 plist)\n
cpu-address
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
\tAligned Read Failed
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
dr-length
CTI_OUT_EN0
far_el2
Primate-Null
AXchip_is_prod_fused
RF24
Register file 3
Register file 39
KIS-STM
NRF54LFlasher: addr (0x%08llX) + word-aligned len (%zu) do not fit in flash of size (%d)\n
_get_arch_hw
Std
no device when sending request
Product Name: 
PMS
%s construction failed
astris_user_default_copy_boardname_for_primate
HardwareBreak
RF1
ASTRIS_ERR_DISABLED
Got an error reading the DCM Control Register: %s
D0-PKA
defaults.board.not_connected
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
NRF_Flasher_t: performing eraseflash\n
LAM
{%s} Failed to extract component info from table (%d); continuing anyway
AXdp_write_with_recovery
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
ASTRIS_ERR_INVALCOMMAND
????
{%s} host:%s, flags:0x%08x
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
%d.%dbeta%d
data_.o.size > 0
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
fn._read_snr.excvaddr
Memory Access Port
no debug bus AP present when expected; after sysap is NULL
RSM
CPU.ARMv6
AXcpu_status_name_detailed
Instruction break 1 address
fn._write_special_reg
empty USB packet encountered
Choose a device: 
debug-size
/var/log/astrisclient
ProductBuildVersion
{%s:%s@%d} [%s] NRF54LFlasher: written count(%d) does not match expected count(%d)\n
x != 0
fn.missing_entry_function
[ARM32cpu_t::_read_register64] 0x%08x\n
storeNicknameForKey
api.is_prod.chip == NULL
op_S16I_encode
DCS11
Unable to disassemble_at_addr 0x%016llx
High level 4 exception PS
Register file 51
%s Bridge @ 0x%09llx-0x%09llx: %s
Debug-Components
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
no SOC object available
xtensa-non-tie-range-name
Invalid file name: \"%s\". File names must be at least %d characters long.
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
(addr=0x%llx)
AXjtag_explore
{%s:%s@%d} [%s] NRFFlasher::verify() failed\n
RPM
instr != 0
{%s[select]} %d(%s) [RETRYING]
AMCP1
AXexplore_enable_cpu
disabled
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
PRID
NRF54LFlasher: AHB-AP ERASEALL success\n
{%s} valid response from bridge
CoreSight
_resume_hw
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
Table 5–185
Table 5–181
{%s::%s} waiting for EDSCR ITE
%s/%s%s.bin
info
un-sel-sib-network
{%s} Reading base 0x%llx entry's component ID
Register file 14
regidx_save=%u
_setup_instr_bp
Creating CPU With Name: %s\n
Probe Map comm error %d(%s) %s
CortexA9
cpu_hwbp_enable
{%s:%s@%d} [%s] moving DBGDTRTX to GPR 0\n
{%s::%s@%d} [FALSE] system_reg[0x%08X] & REGID_MASK != 0\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
ASTRIS_ERR_ASYNC_BARRIER
postconnect
respone == None
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
!!!! Critical Error: Thread %#llx key %lu losing when suspended for info %p - NOT ALLOWED !!!!\n
fn.local
ASTRIS_ERR_PROBEERROR
[KIS] Portal ID: %d\n
astris_cpu_status
PROBED
cpu_mmu_walk
AXbooster_get_loaded_boosters
Failed to read ide_table from KIS explore
Failed to read: ESR_EL%d
op_DSYNC_encode
%x.%02x%s
mempool-base
itoa.h
result.read_vals==
{%s:%s@%d} [%s] updating PC\n
DCCCTRL = %08X   res=%d\n
astris_setup_memap_target
Error status from AMAuthInstallSsoSetStealthModePtr = %i
pnav_create_probelist
ARM11
CPU Explore: 0x%llX\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
copyNicknameForKey
ret.generate_nonce_and_send_request
Can't get OS build version - failed to create URL
%s.%s
{%s:%s@%d} [%s] timed out waiting for reg_index %d to equal: ((0x%08X & 0x%08X) == 0x%08X)\n
ret.astris_disassemble_at_addr
RMX
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armv7mcpu.cpp
failed to write memory
Replacing key with value
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
AP[%d]: JTAG_AP (Exploring Later) \n
RASID
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
{%s::%s} read OK but took %d tries
Failed to read reg_addr=0x%llx val=0x%llx
ret.storeNicknameForKey
INVALID
SoC has been setup using standard instantiation (setup result=%s)
{%s} drain_packets=%d [%s]
ARMV6
AXchip_get_chip_id
%s:%s
DOCK-CH-CONFIG
{%s:%s@%d} Took an exception that took us to exception level[%d] other than 1, 2, 3?\n
SSO with no prompt being used
ret.m_lam.paccess_write
Table 5–167
Can't get OS build version - failed to get build version
{%s} 0 words from probe when %d words left to read for reg %d
implementer
symbol.check.loaded.AMAuthInstallLogSetHandlerPtr == NULL
Table 5–162
astris_select_probe
armv7m-region-type
fn._ocd_exec_instr.wsr.reg_srn.r0
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
ASTRIS_ERR_USB_NODEVICE
host_get_probematch
CPU.ARM32
ITLBCFG
op_SDDR32_encode
!*!*!* Lightning header facing up.                                                    !*!*!*
Select == %d
Short Packet
Size or Count provided are 0.
{%s:%s@%d} [%s] getting GPR\n
DDR
Unique required when %d probes
setup_transaction_objects
{%s:%s@%d} [%s] setting DTR mode to STALL\n
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
AMAuthInstallSsoInitialize
Register file 5
cpu_mmu_walk_detailed
Could Not Find The Entry Function: %s
## memapr %u 0x%016llX -> 0x%08X\n
allocator_
astris_exc_bread_test_2
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
createKeyWithPrimate
fn._ocd_reg_r.ddr.t1_save
op_LDDR32_encode
AXconn_hostname
set.hostname
NRF_Flasher_t: readflash failed: NULL connection and/or data param\n
[1500] No %s.plist resource found
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
astris_poll_cmdstat
High level 5 exception PC
op_RSYNC_encode
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
VBAR: %#llx\n
ret._a64cpu_read_sysreg_hw.hcr_el2
{%s:%s@%d} [%s] executing MRRC\n
PoodleSWD
CTI_INT_ACK
AP[%d]: unknown type\n
TIMEOUT
OCDID
Begin
%d:%d%s
In Eraseflash\n
dest_reg < 32 || dest_reg == 31
virtual int CPU_t::halt()
param.tgt->ap->dp.null
{%s} explore with exploreflags 0x%X completed with error [%s]
Idle
koko
NRF54LFlasher: checking APPROTECT status\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp
fn.exit
!!!! Critical Error: suspended batch attitude for info %p trying to cop - NOT ALLOWED !!!!\n
ERROR!! Couldn't save %s binary data\n
%02u:%02u:%02u:%06u|%s <%s> %s
Probe %s USB-C location is %s
{%s@%d} Connection to server rejected, error=%d (%s)
booster
index slot not enabled
HardwareWatch
Trying to use size of 8 on not AXI bus
{%s} Error setting up memap target (%s)
internal.is_authenticated.debut_auth == NULL
RF23
stack.h
[AstrisAsync] Activate while async is already active!\n
ret.CFReadStreamCreateWithFile
Register file 21
Discon
HIFI3_2
length=%u, width=%d
Successfully connected to server, %s:%d
{%s->%s} m_exception_level=%u
AXcpu_resume
cpu previous instr. 0x%8.8X not halted after 3 checks. OCD.DSR = 0x%8.8X
{%s} set=%u (sh=%u), way=%u (sh=%u)
(system_reg & (0x40000000 | 0x80000000)) != 0
configure_mmu failed
RF12
{%s:%s@%d} [%s] NRF54LFlasher: verify failed: buf and/or passed provided is NULL\n
{%s:%s@%d} [%s] getting GPR (diff mode)\n
2: ARM64_SYSOP_ATS12E1R\n
completedAcmds
No Success after retry on wait
lower_el.check.el = target_el
CortexM23
!!!! Critical Error: Took an exception that took us to exception level[%d] other than 1, 2, 3? !!!!\n
{%s} exec: DC_CISW_X1_ENC\n
{%s} error: %s
Gateway is KIS, seeing what probe this is\n
ret.reg.write.K_DA_REG_NAME_NONCE_3
HostInfo
cpu_getinfo
level_stack_.GetSize() >= sizeof(Level)
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
fn.__ocd_reg_w.ddr
Invalid instruction breakpoint index %d
a
ASTRIS_ERR_NOTFOUND
{%s:%s@%d} [%s] NRF54LFlasher: nRF part code 0x%08X is not supported\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
EvalQuantifier
ret.modify.edscr.~a
   {%s} Clearing HNONSEC on AP \n
param.no_ap
authenticate
PROBED_SLEEPING
RESPONSE_CMD
NRFFlasher: timed-out waiting for CTRL-AP ready\n
AXportal_t Is Not Valid Type - %d
MCORE
{%s:%s@%d} [%s] executing MCR\n
NRF53Flasher: APPROTECT is %s\n
soc is NULL
fn._ocd_reg_w.ddr.wb_next_u32
Astris Source Version: %s\n
ret.die_count == NULL
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
[Timeout running ARM7 scan list]
{%s} Error setting up jtag-ap target (%s)
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
{%s} NOMEM
Listing
[KIS] Register Index: %llu\n
{%s:%s@%d} [%s] failed to read cfg reg: %d\n
{%s:%s@%d} [%s] writing OSLAR (oslk)\n
defaults.create.key.outofmem
Table 5–179
Base of current AR window
_read_mem
cpu-aptype
misc-wirtestporten
astris_ide_get_revision
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
ret.read.stepping_stone
Cant find Debug Auth Registers. Auth not supported
ApBoardID
Hifi3
MMX
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
ret.reg.write.K_DA_REG_NAME_CHIPID
fn._ocd_exec_instr.xsr.ddr.t1.1
ASTRIS_ERR_BLOCKED
Wait indication while connecting to
file_type
IDE
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/logging/astris_except_classes.cpp
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
astris_memap_lmflash
EXPLORE_ONE_DIE
!!!! Complex Key %s is INVALID !!!!\n
read.dspsr_el0 NOT CACHED
R15
Register file 2
MAC16 Data register 3
R7
Can't get hardware model - failed to get property
FAULT
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s->%s} exec: encode_mrs(scratch=%d, sysreg=0x%X (%s), regname=%s, %d)\n
<rev>
Only Auth-Debug, Auth-DFT and Probe-Auth are currently supported.\n
%d.%drelease
complex-id
[%s] {%s->%s} END handling exception
ret.write.spsr_elx
stat
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
Tc1500_t
Sprocket probe, for now I guess we will just say yes...\n
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
Complex Name: %s\n
{%s:%s@%d} [%s] reading LOCKSTATUS\n
{%s:%s@%d} current_el[%d] == 1|2|3\n
NRF53Flasher: JTAG re-explore after net core enable successful\n
symbol.check.loaded.AMAuthInstallSupportDictionarySetInteger32Ptr == NULL
_insert_breakpoint
ASTRIS_ERR_EMPTY
{%s:%s@%d} [%s] NRFFlasher::flash() failed\n
DCS_BC7
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s:%s@%d} [%s] writing OSLAR (oslsr)\n
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
ASTRIS_ERR_OK
{%s:%s@%d} [%s] NRFFlasher: flash failed: addr(0x%08llX) + word-aligned len (%zu) do not fit in any writeable regions\n
No connection attempt description
sel-partition
Failed to write reg_addr=0x%llx val=0x%llx
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
EPC7
Register file 26
Portal Status has an error
Probe %s Device Does Not Have LocationID
Size
nullptr == file_path_cfstr
Failed to populate component info
Invalid content key, %d
[%s] %d -> %08x\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
internal.get-timer-count.chip->soc == NULL
MISC2
No probes were found matching
[1500] %s step %d: unknown instruction '%s'
{%s:%s@%d} [%s] doing JTAG scan (DIDR)\n
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
{%s} Failed to get watchpoint count for %s: %s
RF15
{%s} %s
NRF54LFlasher: COMPLETE! Wrote 
is.Peek() == 'n'
param.conn==NULL
{%s::%s} [%s] length=%u when width=%d
fn._write_special_reg.reg_srn
Could not find portal by select %d, while interpreting result\n
IDLE
ACQ_SETUP
diagnostic_checks
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
ret.is_current_state_aarch64
_read_memory_fast_try_with_chunk
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
M33
NRF53Flasher: performing AHB-AP %d ERASEALL\n
ASTRIS_ERR_PORTAL_STATUS
{%s:%s@%d} [%s] NRFFlasher: failed to read register 0x%08llX\n
select_v2
Found match - bypass_device: %s; channel: %d\n
spr-regs
ret.lower.after.read.aarch64hw
{%s::%s@%d [%s]} Error %s: initializing cache parameters
[AsyncSnapshot] #%zu: %s\n
read_settings
RF28
Sending DYN Bypas Channel Set: %d
Got an error writing 0x%X the DCM Control Register: %s
astris_ide_print_platform_info
elr_el3
Invalid num_regs = %u. Windowed register option required.
NRF54LFlasher
{%s:%s@%d} [%s] NRF54LFlasher: waitForNVMCReady() failed\n
Logger is null
NUB
PRORES
{%s} halting %s\n
M7F
PARTNO_SWDP_M23
nullptr == file_url
result.read_vals(table)==
{%s:%s@%d} [%s] DEMCR write failed: %s\n
NRFFlasher: timed-out waiting for NVMC ready\n
AXbooster_refresh
dart-apf-address
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
EL1h
AXcpu_getinfo
message
PARTNO_SWDP
ACQ_SAMPLE_I2C
Matched Booster: %s\n
{%s:%s@%d} [%s] scanning out\n
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
fn._write_window_base.wb_save
revive
darts
init_hw.pid0
AXcpu_cache_info
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
   Setting up AP IDR %08X\n
RF62
_read_cpu_reg_file
fn.params
fn._ocd_reg_w.ddr.tgt_32
command timed out
{%s:%s@%d} [%s] reading PRSR (!lsr)\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
AXcpu_hwbp_info
swdackdelay
op_L16UI_encode
AXconn_conndesc
Invalid encoding in string.
BoosterManager.SOC
astris_ide_get_deid
Reset
{%s} setting up nameless target (address=0x%llx)
astris_jtag_get_pipe_cycles
EXPLORE_IDENTIFY_ONLY
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
internal.clear-auth.debut_auth == NULL
[1500] Error parsing v2 bridges
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_STATUS
fn._ocd_exec_instr.rsr.2
IOPlatformExpertDevice
{%s} Found extra info in = %s, chopping string
preconnect
Old ProbeDaemon does not support this command
socs_supported
Could Not Allocate Mutable Dictionary For BoosterMangers
sdom
CS-CTI
ret.read.rtxcid
{%s} PRIMECELL [DONE]
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
!Base::level_stack_.template Top<typename Base::Level>()->inArray
_read_register32
{%s::%s@%d} [FALSE] dest_reg[%d] < 15\n
--> 0x%02x = %s
couldn't read TCR
ret.write_reponse_and_check_authentication
Table 5–163
regex.h
result.read_vals(group0)==
astris_exc_bread_test
sso_user.conn == NULL
RF18
RF36
!!!! DART Key %s is INVALID !!!!\n
Failed to read transfer register (EDDTRTX)
ENABLED
AUD
SLEEPING
{%s::%s} error %s writing EDSCR %s
{%s::%s} cpu powered off: failed init() %s
internal.clear_probe_auth.debug_auth == NULL
%s probe[*] from Probe Map Server [local host]
AXchip_switch_taps
Map is empty, not removing CPU %s
unswitch_regset
memAPErasePages
max_scan_bits is low: %d
UNKNOWN_KIS_ERROR
already connected
ParseStream
!!!! Complex CPU Key %s is INVALID !!!!\n
True
Can't find descriptor for group - can't index\n
before_deactivate_in_runBlock
astris_memap_bus_read
UNKNOWN_PORTAL_ERROR
AXconn_destroy
Connected toProbe Map Server (single_port) 
CPU Supported in Integration: %s\n
astris_command_async
{%s@%d} Drain empty on decr [%s].
DCM
cpu-typehint
_a64cpu_encode_mrs
hwwp_insert
Thread pointer
operandStack.GetSize() >= sizeof(Frag) * 2
wir-tdo
APCIE_ANS0
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm64cpu.cpp
_a64cpu_write_sysreg_hw
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
probeNicknames
FindMember
.chip_id
astris_ide_refresh_boardid
{%s} restored el is now %d
{%s:%s@%d} [%s] NRFFlasher::init() failed\n
{%s} %s: |%s|-|%s|
Not Creating CPU: %s\n
AXcpu_lacc_bp_status
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
Early dbgwrap base extracted: 0x%llx\n
BP
     0x%016llx: 0x%04x      %s\n
## memapw %u 0x%016llX 0x%08X\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Register file 12
fn._read_special_reg.debugcause
ret.cfg_write(R_DCM_GPIO).deassert
AXdebug_auth_get_probe_timer_count
fn._tie_read_word32
{%s} select success without file descriptor set
prettywriter.h
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
%s: []\n
AXcpu_cleaninv_dcache
probe matching %s on host %s
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
```
