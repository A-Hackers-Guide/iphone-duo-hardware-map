# `/usr/local/share/astris/boosterpack/swdflashers/arm_stm32l15xc_swdflasher.booster/arm_stm32l15xc_swdflasher`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,843,728 bytes.

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
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
Sending DYN Bypas Channel Set: %d
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[AstrisAsync] replay preflight: Async not active!\n
%s status is '%s'\n
Type 'jebdump' to do scan/mem dump\n
SoC not identified by IDCODE - enumerating instead of instantiating
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
connection about to be destroyed
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
UPDATE cop64 %d -> 0x%016llx\n
%s: not supported.\n
VBAR: %#llx\n
{%s:%s}: cpu powered off: unable to access a register for this CPU
{%s} Unable to read SP_EL0
[%s] AP, DP, or chip given is NULL
AXmemap_stmflash calling STM32L4xx::reflash()\n
   --> IDR: %08X\n
      Select port %u: AVOIDED\n
Connected to Probe Map Server
Failed to sync prefs at beginning
Invalid character [0x%02X] received from Probe Map Server
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
HOSTID bit not set\n
Booster:\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
Probe (port=%d) with unknown status %s dropped from available list
{%s} %s: |%s|-|%s|
Complex CPM Offset: 0x%llX\n
pmu-name: %s\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
[1500] Error parsing IR command: %s
batch_cmd_count: %d
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
   Debug Port: SELECT %X: SKIPPING (%s)\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
STM_FLASH_ACR: 0x%x\n
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
AXmemap_read failure - %s
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
[AstrisAsync] Deactivating async...\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
Flash Size %d KB\n
\t Sector %u failed: %s\n
{%s} skipping dcache flush, cache already clean
{%s@%d} gethostbyname failed, error=%d (%s)
comparing against match entry [pid] %d: %s\n
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
!!!! Complex CPU Key %s is INVALID !!!!\n
Portal Group Offset: 0x%X Entries: %d\n
error %s checking for data abort(uint32_t)
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
Can't get OS build version - failed to create ReadStream
Unable to create pthread key for conenction. errno=%d %s.
write to CMD/STAT failed - %s
%s Bridge @ 0x%09llx-0x%09llx: %s
Failed to find a plist for this soc %s
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
USER %s(%04u): %s(): %s
Unable to disassemble_at_addr 0x%016llx
      AXap_write of R_JTAGAP_PSTA failed with error %s
      Read of JTAG-AP port %u CSW failed with %s\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
Unable to read SP
[REMWP] wp%d\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
Xtensa Option options: 0x%x
{%s:%s@%d} Critical error [radar already requested]
!*!*!* Lightning header facing up.                                                    !*!*!*
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
{%s} no matching 1500-to-* bridge
Could Not Find Any Loaded Boosters of Type: %s\n
{%s::%s@%d [%s]} Error %s: flushing HW state
Unable to read FP
Xtensa Option reg_file_size: %d
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
start rev is not of expected format; skipping cpu_desc override\n
DEMCR write failure - %s (%d)
AXjtag_srst deassert failure - %s (%d)
CPU Explore: 0x%llX\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
{%s} _resume_hw result = %s
Successfully Authenticated\n
Gathered:\n
Early dbgwrap base extracted: 0x%llx\n
AP is NULL
Astris Version Set: %s
Connected to Probe Device Server [Log File %s]
Setting CPU %s is_boot_core to %d\n
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Asked To Write To A Negative Register Index
KIS Writevals putting back the value
{%s} Failed to extract CID from table (%d); continuing anyway
Unable to read CPSR
ERROR!! Couldn't save %s binary data\n
Created Connection - : %s
{%s} already connected
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
Table Size: %d\n
Failed to sync prefs at end
{%s} wrote %d words to probe when %d words provided in request
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
no system bus AP present when expected
Going To Create Generic ARMV8\n
Could not find portal by select %d, while interpreting result\n
Previously dumped the process tree, skipping
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
SSO with no prompt being used
STM_FLASH_KEYR: 0x%x\n
{%s::%s} creating placeholder for CPU: name=%s
using multi-target booster products_%s.plist
Hardware model: %s
{%s@%d} IOServiceOpen failed, err = 0x%08x
{%s} Found extra info in = %s, chopping string
Kick has been requested by probe server
## dpw 0x%02X failed (%s)\n
!!!! FILE RADAR: Don't know how to compare two values\n
     ARM %s breakpoints: %u\n
Invalid Size Given for AP AP=%d Size=%d
{%s} no chip found
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
Cannot create DART descriptions from NULL info\n
in stmflash api\n
Gathered Value is Not Number\n
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
Wrong width, should be either 4 or 8\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
Fast Programming Error is Set\n
{%s::%s} [%s] MMU is already active - returning %s
Error closing %s [%d]
error %s reading DAP PFR1
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
   DPv3 BASEPTR0 is 0x%08X\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
{%s}ERR: bypass_device_name is NULL\n
The debug port associated with this chip has not been explored.
   Debug Port: SELECT %X: DISABLED\n
SWDACKDELAY relay write failed\n
%s probe[%s] from Probe Map Server [%s]
\t\t%s\n
Portal Group Base: 0x%llX \n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
{%s} Error reading PID (%s)
AP[%d]: unknown type\n
\tFailure: status errors: 0x%08X\n
STM_FLASH_CR: 0x%x\n
Error %d (%s) opening history save file
{%s} invalid data width %d bytes
Failed to get Bypass Config
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
\tLeft To Read (%d) < width (%d).\n
Switch to primate res: %s\n
{%s} Error %d(%s) sending message
!!!! Complex Key %s is INVALID !!!!\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
   MEM-AP not enabled\n
=== Ending Gather and Clear ===
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
KIS Chip Found, Doing KIS Explore Setup
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
[1500] Error parsing TAP description
1: ARM64_SYSOP_ATS12E1W\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
Could Not Create Dictionary From Booster: %s
Booster Info:\n%s
Probe %s LocationID Info is %s
Bundle: %s NOT FOUND\n
[HALTED] dfsr = 0x%08x\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
%s status transitioned: %d ('%s') -> %d ('%s')\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
Subsystem Monitor Key does not exists: %s\n
Error %s connecting to server %s:%s [RETRYING]
Probe %s with unknown kick response %s
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
CPU Name: %s\n
CPU %s not found or already removed from the map
[ARM64 INS_WP] 0x%016llx x %d\n
ERROR: unable to resume translation for %s
AXmemap_stmflash calling STM32Lxxx::reflash(0x40023C00)\n
Successfully connected to server, %s:%d
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
SoC has been setup using standard instantiation (setup result=%s)
Failed to Identify & Explore Chip via KIS: %d (%s)\n
We are done with clean up\n
## armcpu: success status even though not all bytes read\n
DEMCR: 0x%08X -> 0x%08X
AP[%d]: JTAG_AP (Exploring Later) \n
## memapw %u 0x%016llX 0x%08X ...(%d)\n
{%s@%d} Unknown CS command error [%d]
start rev and/or end rev is NULL; skipping cpu_desc override\n
[READ] cop64 %d -> 0x%016llx\n
{%s[select]} %d(%s) [RETRYING]
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s} failed (%s)
{%s} explore with exploreflags 0x%X complete [%d chip%s]
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
%-16s @ 0x%08llX : 0x%08X\n
Before astris_kis_init_dp, CMDSTAT=%08X\n
\t%s\n
[1500] TAP %d: irlen must be > 0 (got %d)
[%s] E2H is set, virtualization is supported\n
Chip %x Status = %d\n
CPU DBG Ack: 0x%llx\n
Component Group Offset: 0x%X\n
{%s} Failed to extract PID from table (%d); continuing anyway
{%s} Failed to resume %s: %s
{%s} Exploring with option: %s\n
unable to create connection
Turning Debug Clock On
{%s@%d} {%s[select]} %d(%s) [RETRYING]
unknown match criteria type: %d
[AstrisAsync] Resume when not paused!\n
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s} Error setting up memap target (%s)
AP[%d]: MEM_AP_APB\n
Error - STM32%s reflash failed (%s).\n
Debug Clock Already Enabled
CPU Typehint: %s\n
Stop Clock: %s\n
{%s->%s} ERROR=%d(%s)
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
\tPrologue Aligned Read Failed
      Select of JTAG-AP port %u failed with %s\n
Failed to convert primateLoc %s to unsigned long long
[1500] Error parsing v2 bridges
WARNING, reserved / slide bits not zero! Zeroing out!\n
   Setting up AP IDR %08X\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
{%s} FAILURE - max length exceeded
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
coalesced-target: %s\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Failed to create CPU %s - %s\n
Failed To Instantiate SOC From Booster\n
Full JSON that failed validation:\n%s
Asked To Read A Negative Register Index
Invalid Bundle: %s
error trying to unlock MSR %s
   Debug Port not responding (%s)\n
[PREFS] Key: %s - Val: %s
Programming STM32Lxxx...\n
Dart Name: %s\n
Booster Value is Not String\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
Error happened when reading edscr. Retry #%i\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
{%s} bridge returned DECERR
Die Config Disabled
{%s} Unable to read CPSR
Invalid current AP (%d), adopting latest (%d)
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
{%s@%d} Timeout while sending probe command.
{%s} (end) current_el is now %d
Failed to convert CFArray to C Array\n
\t%4X: %8X %8X\n
Could Not Get Bundle Out Array of Found Boosters\n
{%s} Failed to extract ECID from table (%d); continuing anyway
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s} Thread %#llx clearing key %lu
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
Trying to use size of 8 on not AXI bus
   ROM entry %d (level %u): AVOIDED\n
      Select port %u: already explored..re-exploring\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
## apr %u 0x%08X %d -> 0x%08X ...\n
Optional Key: CPUMonitor not in preferences
Failed to read register to figure out flash address %s\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Failed to convert primateHubLoc %s to unsigned long long
Failed To Init Booster's Astris API In: %s with %s (%d)\n
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
Probe Map name of probe %d is: %s
{%s[select]} timeout while waiting for data from the connection
** CPU %s requires forced explore override flag on this SoC **\n
[%s] cop %d -> 0x%08x\n
\tCould not read the flash size. Using default 1MB size.\n
{%s} unable to allocate probe name
{%s} %d(%s) [RETRYING]
{%s} no TAP detected that supports 1500
[KIS] Register Read/Write/Wrote: %d\n
{astris_probed_print_events} not supported in this build configuration
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
[PREFS] Key: %s - Val: NULL
Couldnt figure out the size of flash, defaulting to 1MB\n
end rev is not of expected format; skipping cpu_desc override\n
Failed to create Xtensa CPU %s \n
unable to obtain sysap
{%s} category=%d
{%s} %s DC cache clean complete, marking as clean
Hang Description:\n%s\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
%s probe[*] from Probe Map Server [%s]
ERR: conn->nchips != 0; looks like chip is explored\n
CPU state %d
error %s reading DAP MPIDR
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
{%s} L2 cache operation completed [%s]
replay_counter=%lu, last_replay=%d
\tReading left over chunk expected 0x%x got 0x%x\n
codeblock
ERROR: unable to suspend translation for %s
   {%s} (DP): status=0x%X(%s) - %s\n
register    %-15s %3u     \"%-s\"\n
Can't get hardware model - failed to find matching IOService
%s given a NULL conn object
{%s} unmodified-probe_match = %s
{%s@%d} Probe reported connection lost [PROBEEOF].
We are Deallocating\n
Complex Address: 0x%llX\n
{%s} timed out waiting for cpu to halt during collect
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
Initialized %d 1500 bridges\n
JsonLogger: Schema loaded successfully for category '%.*s'
[KIS] CMD: %s \n
%#09llx-%#09llx: %s\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
[AsyncSnapshot] #%zu: %s\n
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Creating CPU Returned: %s\n
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
{%s::%s} EDSCR with RXO set - unable to recover.\n
SOC AP[%d]: JTAG_AP\n
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Using Built In SoCs\n
{%s::%s} creating AP slave: name=%s
WARNING: %d KB flash size detected.\n
--> extrawrstn %d
[1500] Error parsing bridge '%s': missing required field 'select'
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
{%s} Unrecognized Component: %08X (class %u)
Read error (%s) @ 0x%08llX - retrying.\n
Error %d (%s) while expanding ~ for Astris history save\n
{%s} host:%s, flags:0x%08x
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
Aligned Address: %llx
Async is disabled for current seesion
HOSTID=0x%x which is invalid, skipping orientation check
received %zd bytes from Probe Map Server when have %zu
Generated JSON (first 500 chars):\n%.500s%s
product-name: %s\n
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
** \tTatsu AuthDebug Triage | All     **\n
Init dbgwrap obj failed
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
## apw %u 0x%08X 0x%08X\n
New Length: %d\n
Could Not Allocate Mutable Dictionary For BoosterMangers
[SSTEP] using BP %d\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Can't get hardware model - failed to get property
Error %d (%s) opening cmd snapshost save file
Abnormal %s termination: Assert Area Mask = 0x%016llX
%2d) %s %s%s\n
--> cmd        addrsize=%d datasize=%d
no debug bus AP present when expected; after sysap is NULL
KIS Readvals putting back the value
Gathered Info:\n%s
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
{%s} _pre_halt_hw result = %s
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00,single)\n
ERROR!! write binary data parameters invalid\n
Unable to allocate memory for next part of big response
{%s} set=%u (sh=%u), way=%u (sh=%u)
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
Required Key-Value is a string, and not an array. Old booster found\n
Failed to convert %s key @ index %d
[%s] {%s->%s} clear async abort
TargetSel Before Disable: 0x%x
DHCSR write failure - %s (%d)
error %s checking for data abort(first)
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s::%s@%d [%s]} Error %s: checking exception
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
{%s} Error setting up jtag-ap target (%s)
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
{%s} bridge returned SLVERR
Start Address=0x%08llX....End Address=0x%08llX
Could Not Match A Booster for %s\n
Min Component - %s\n
{%s} m_exception_level(%d) != current_el(%d)
[REM_HWBP] bp%d\n
[INIT]\n
   Debug Port: SELECT %X: SKIPPING\n
\t Writing 0x%08llX...\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
{%s} Failed to get breakpoint count for %s: %s
\tCould not read the flash size. Using default 2MB size.\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[ARM32cpu_t::_read_register64] 0x%08x\n
\t\tARMv6 debug CPU xxx ID\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s::%s} ITE is not set: 0x%X\n
[RESUME] Chip %x\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
relay_get: %s = CMD_ERR (%s)
{%s::%s} timeout while waiting for EDSCR ITE
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
## apw %u 0x%08X 0x%08X ...(%d)\n
Programming STM32Hxxx...\n
[ANAMOLY] Could not find AXcpu_t object for CPU\n
{%s} Failed to extract target ID from table (%d); continuing anyway
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
[%s] %d -> 0x%08x\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
Warning: chip exploration did not complete successfully (%s)\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40022000)\n
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
Match Count is Zero. This is invalid.
Failed to get PMU Name
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
Error - STM32Fxxx reflash failed (%s).\n
%s probe[%s] from Probe Map Server [local host]
getOrCreateValue: addMember failed, returning doc root
Found another target for the plist\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
Using Built In CPUs\n
Length is 0
{%s} DAP command nwords=%d trimmed to %lu\n
   Created Fake Debug Port Debug Port
Probe %s with unknown status %s dropped from available list
Done.\n
AXportal_t Is Not Valid Type - %d
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
first read of CMDSTAT may fail if external reset occurred
{%s} error: %s
\t0x%08llX...\n
ERROR!! Wrote %zd bytes, expected %zd\n
\t[MATCH_FOUND] identified chip: %s
Write Failed: address=0x%08llX, length(in)=%lu, width=%d, length(out)=%d, result=%s\n
Could Not Find Booster Entry Function: %s\n
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
{%s::%s} EDSCR with TXU set - unable to recover.\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s=>%s} AXconn_t has no SoC object
{%s}#%02X %s [%s]
{%s@%d} Drain empty on decr [%s].
error %s checking for data abort
{%s->%s} m_exception_level=%u
{%s::%s@%d [%s]} Error %s: initializing cache parameters
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
[PREFS] Key: %s - Val: ??
We are in clean up\n
Exception %d Stack Trace
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
process (%s) (%d) path: %s
{%s} %s
{%s} select success without file descriptor set
Failed to instantiate %s\n
Sprocket probe, for now I guess we will just say yes...\n
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
failed read from DEMCR - %s
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
Complex Name: %s\n
AXconn_t Struct Is NULL
Successfully Authenticated DFT\n
Failed to create optional file. Not fatal, moving on
New format for cip gen register, unsupported: %d\n
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s::%s} ERROR %d(%s) pre_resuming %s\n
OS build version: %s
User created bundle found, ignoring version checking via plist
Magic does not match: %#x vs %#x\n
{%s} restored el is now %d
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
Probe %s status: Idle
!!!! DART Key %s is INVALID !!!!\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
[REM_WP] wp%d\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
Buffer is NULL
{%s} probe_port = %d
Programming (addr: 0x%08llX) Failed!!!
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
{%s} empty response string provided
AP given is not a MEMAP
{%s} Component ID read fail on romtable (%s)
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
    %s(): %s
failed write of 0x%08X to DEMCR - %s
probing %s status\n
CPU AP-Select: %d\n
[1500] %s step %d missing required field 'instr'
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
JsonLogger: Writing category '%.*s' to '%s'
Size or Count provided are 0.
Could Not Find Any Boosters\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s} Class 9 ROMTABLE (nest=%d)\n
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
STM_FLASH_WRPR: 0x%x\n
Dart CPU SID(s): %s\n
--> wrstn_wir2 size=%3d dpcsoc=%d
Error status from AMAuthInstallSsoInitializePtr = %i
SSO info present but SSO disabled.
{%s} drain_packets=%d [%s]
[KIS] Portal ID: %d\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
[AstrisAsync] Discarding %zu completed command(s)\n
{%s} status=%d being reported as Unknown
AXmemap_stmflash calling STM32F2xx::eraseflash\n
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Could Not Allocate Loaded Booster Array
Too many portals, we are at portal: %d while max is %d\n
EICE chip %x initialized\n
replay_counter=%lu
Error - STM32Lxxx reflash failed (%s).\n
Couldnt figure out the size of flash, defaulting to 2MB\n
Flash Sector Max %d\n
{%s} probe_host = %s
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
{%s::%s} cpu powered off: failed init() %s
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
{%s} Unrecognized component: %08X, class %02X\n
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
AXmemap_stmflash calling STM32F7xx::eraseflash\n
Xtensa Option non_tie_ranges: %zu range(s)
dfu-Type: %s\n
2: ARM64_SYSOP_ATS12E1R\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
\t[MATCH_SKIP] skipping entry
Taking gateway control failed
Found match - bypass_device: %s; channel: %d\n
Dart Dart Type: %s\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Old ProbeDaemon does not support this command
no debug bus AP present when expected
JsonLogger: Created with default schema version '%s'
{%s::%s} [%s] error %s from _synchronize_context.
Failed explore before forced KIS reset: %s\n
Optional Key: SubsystemMonitor not in preferences
{%s} Batch attitude key created for %p thread %#llx key %lu
There is no system bus access port on the debug port
Start Page: %d\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
STM_FLASH_AR: 0x%x\n
Can't get OS build version - failed to allocate buffer
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Could Not Find a DCM Portal
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
[AstrisAsync] Complete Queue callback returned %d (%s)\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
\tCould not get sector size for address: 0x%llX\n
Could Not Get BoosterManager\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Board ID: 0x%X\n
[FLUSH]\n
iter=%lu
ERROR: nothing to do; resuming address translation for %s without previously suspending it
Switch back to primate KIS: %s\n
In Preflash\n
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
{%s::%s} [%s] unsupported width %d
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
[%s] EL @ end of Collect: %d\n
Error %d(%s) executing instruction 0x%08X
[AstrisAsync] Barrier before pause\n
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
CPU Address: 0x%llX\n
Breakpoint Address: 0x%llx
Breakpoint Enabled: %s
PKA Base: 0x%llX\n
Unable to register assert upcall %s (Insufficient memory)
relay_get: %s = %d
Map is empty, not removing CPU %s
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
   Debug Port: SELECT %X; error: %s, retrying..\n
   {%s} APB/AXI address for target setup = 0x%llx\n
Flash Reg Adress 0x%llX\n
STM_FLASH_OBR: 0x%x\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
Value Types Are Not Strings\n
{%s::%s} write OK but took %d tries
     0x%016llx: 0x%08x    %s\n
      Explore of JTAG-AP port %u failed with %s\n
Xtensa Option dbg_intr_level: %d
Had an error during transfer: %s
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[MEM] Aborted; DSCR = %08x\n
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
  Error path [%s]\n
dropping empty probeInfo (port=%u)
Connected toProbe Map Server (single_port) 
DEMCR read failure - %s (%d)
{%s->%s}
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
AP Only Explore was asked for, stopping here
SoC must have a DAP
Koko probe, for now I guess we will just say yes...\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
DBGCTRL = %08X   res=%d\n
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
{%s} _halt_hw result = %s
Failed to access new_cpu status
Warning: spun for a long time (> %ld seconds)\n
Can't get hardware model - failed to create string
Programming Error is Set\n
[1500] IR command '%s' missing required field 'opcode'
{%s=>%s} AXconn_t has more than one chip
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Dumping Process Tree
{%s} match any probe [localhost]
{%s@%d} Unable to create socket
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s->%s} START handling exception
Original Content: 0x%08x
SSO is DISABLED\n
{%s} connectName[%s]
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
Failed to get KIS translator version\n
Failed to convert CFString to C String.
Increasing length by: %d\n
{%s} strsep empty so match any probe [localhost]
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
{%s::%s} waiting for EDSCR ITE
Translate Stage Chosen: %d\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} ROMTABLE (dbgbase=0x%llx)
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Failed to explore chip: %d
Flash Reg Adress is not set, using what is there\n
Xtensa Option num_high_pri_intr: %d
Failed to unlock flash\n
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s} Failed to extract die infofrom table (%d); continuing anyway
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
==== User Error Messages ====\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
{%s::%s} %s resumed\n
Unable to read PC
dbgwrap halt failed, falling back to classic method
Highest EL: %d, -- Min Op EL: %d
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
## dpr 0x%02X failed (%s)\n
{%s=>%s} null reference to AXchip_t[0]
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
unable to identify chip
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Complex Type: %s\n
%s NOT configured\n
Hang Radar Info:\n%s\n
{%s::%s} creating CPU
\t%s (%s)\n
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
=== Starting Gather and Clear ===
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
{%s=>%s} null reference to AXconn_t record, `conn`
{%s} probe_match = %s
%s
VBAR: %#x\n
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
{%s} Failed to extract IDCODE from table (%d); continuing anyway
Stepping Stone Final =  %#x\n
[HALT] Chip %x\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
Gateway is KIS, seeing what probe this is\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
Probe %s Device Not Connected on USB-C Port
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
We are at max iterations, still didnt get full JSON
%2d) %s %s [Busy]%s\n
Complex CPU Name: %s\n
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
Initial DSPSR_EL0: 0x%llx
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
{%s} %s DC cache already clean since last halt, skipping flush
Flash Size 0x%X KB\n
Can't get hardware model - failed to allocate data buffer
[KIS] Address: 0x%llX\n
Enabling USB Gateway
Form-factor specific channel not found, falling back to generic channel for device '%s'
Protocol Version: 0x%X\n
Going to do imago workaround\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
[Auth Debug] Ticket Active, Debug Interface Locked\n
\tWriting @ 0x%08llX...\n
[AstrisAsync] Pause when already paused!\n
{%s::%s} [%s] !bpwp_initted, retrying init
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Error status from AMAuthInstallSsoEnablePtr = %i
Preferences does not exists: %s, creating one.\n
Portal Status, Changing STATUS and CMD/STAT to reflect
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
Problematic JSON value:\n%s
{%s::%s} read OK but took %d tries
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
CPU Monitor key does not exists for: %s\n
Can't get OS build version - failed to open ReadStream
Initializing Booster Layer\n
bypass-config-name: %s\n
    INFO(%u,%d): %s(%04u): %s(): %s
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
[%s] CPU BM Not Found, Bailing\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
{%s@%d} neither socket nor kext connection available
{%s} unaligned %d-byte access at address 0x%09llx
invalid IR command '%s'
{%s} error %d(%s) reading data from the connection (at recv)
Die Config Disabled\n
{%s} read %d words from probe when %d words requested
Can't get hardware model - failed to convert to C string
Probe %s selected
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
Unknown number of groups in the explore table; can't parse group attributes
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
   Debug Port: Trying SELECT %X\n
## memapr %u 0x%016llX %d -> 0x%08X ...\n
\t Bank %u Sector %u...\n
  Nested path: parent='%s', child='%s'
[1500] TAP key is not a valid integer
[AstrisAsync] Pausing Async Mode\n
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
   {%s} Clearing HNONSEC on AP \n
Spew change. old=0x%016llX, new=0x%016X
{%s[recv]} %d(%s) [RETRYING]
End of Operation Bit Is Set - %s
In Postflash\n
[1500] Using %s.plist
{%s::%s} [%s] error %s reading SCTLR_ELx
replayPreflight
caller=%s, async=%d
Verification Mismatch starting at offset %d\n
{%s} probeList has probeCount of zero
Failed to convert %s key @ index %d to a number with base of %d\n
{astris_probed_print_events_from_json} not supported in this build configuration
Unable to read LR
{%s} setting up nameless target (address=0x%llx)
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
Connected to Probe Device Server [Default Log]
%s SoC created
[%s] Booster System Is Not Initialized\n
Could Not Find Any Boosters of Type: %s\n
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
Replacing key with value
[%s] chipinfo is NULL
{%s::%s} NULL parameter
type_hint not NULL, but creating a placeholder, this is off
Failed AP read of R_MEMAP_CSW res: %i
Subsystem Monitor[%i]: %s\n
comparing against match entry %d: %s
{%s} handle ROM entry %d (level %u): %08x
Invalid SoC Booster. SoC Booster Requires PID\n
Invalid file name: \"%s\". File names must not start with '.'
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s} %s status is '%s' [Status Read %d times]\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
AXmemap_stmflash calling STM32F4xx::reflash(0x40023C00)\n
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
No 1500 bridges specified\n
CPU %s already in the map with status: %d
[AstrisAsync] Activate while async is already active!\n
X09 Part
Xtensa Option num_wp: %d
Probe %s removed before port determined\n
setCategoryValue: path='%.*s'
DCCCTRL = %08X   res=%d\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
relay_set: %s = CMD_ERR (%s)
{%s} %s: |%s|
Failed to read ide_table from KIS explore
Found the RTXCID Structure!\n
{%s} [%s] m_exception_level=%u\n
[AstrisAsync] Resuming Async Mode\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Probe Map Server Information: %s
SOC_t::{%s} CPU_t group=%d when group 0 expected
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
[%s] {%s->%s} Transitioning to exception level %u.\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
Could not find TAP at index %d to attach 1500 bridge to\n
JsonLogger: Wrote %zu bytes to '%s'
In Eraseflash\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
[AstrisAsync] Got ASYNC_RESTART response!
{%s} hostname:%s, flags:0x%08x
{%s} found single_port probedaemon on port %d
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
{%s@%d} Received %d bytes when requested %d bytes [%s].
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[%s] {%s->%s} END handling exception
     ARM %s watchpoints: %u\n
Booster System Is Not Initialized Bailing\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
Probe %s removed during selection process
checking if relay \"%s\" is valid
Got an error writing 0x%X the DCM Control Register: %s
haskis bit not set\n
Astris Source Version: %s\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
About to call fault reg latch, min_operating_el: %d\n
[AsyncSnapshot] No snapshots collected\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
\tReading left over chunk 0x%x @ 0x%llx\n
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
{%s} %sing word #%d at address 0x%09llx: %s
Setting bypass channel to: %d\n
In Readflash\n
=== Loaded %s Boosters ===\n
!!!! CPU Key %s is INVALID !!!!\n
{%s} 0 words requested for read at address 0x%016llX
{%s::%s} failed: %s
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
     ARM %s debug CPU rev %d\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
{%s} Failed to single-step %s: %s
{%s} %s status failed. error: %d (%s)
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Failed to get DFU Type
      AXap_read of R_JTAGAP_PSTA failed with error %s
Previous authentication in-flight, wait for it to finish\n
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
\t Sector %u...\n
Probe %s removed prior to kick\n
\tAstris does not support page-erase beyond first %d KB of flash.\n
{%s} 0 words from probe when %d words left to read for reg %d
runBlock
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
Probe Map comm error %d(%s) %s [%s]
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
JsonLogger: Loading schema for category '%.*s' from '%s'
[AstrisAsync] Failed to restart Async batch\n
Async is disabled for localhost connection
Failed AP write of R_MEMAP_CSW res: %i newval %i
## memapr %u 0x%016llX -> 0x%08X\n
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
   Debug Port has unknown type\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
Successfully Authenticated Probe\n
CPU with %s Not Created via Name
\t Erasing 0x%08llX...\n
probe event: %s
Chip Revision: 0x%X\n
%s constructed
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
[Auth Debug] Disabled\n
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
AXmemap_readvals failure - %s
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
--> misc_wdr   size=%3d wirtestporten=%d
AP[%d]: MEM_AP_AHB\n
probetimeout retrying access...\n
{%s@%d} Connection to server rejected, error=%d (%s)
{%s=>%s} AXconn_t has no chips
chip is 0??\n
Please answer y=yes or n=no.\n
[PAW] Failed KIS Portal Access Preflight =%s (%d)
Could Not Allocate Booster Location Array
CPU at Index: %d has to specify only one AP Type or AP Select\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
[AstrisAsync] Deactivate while async is not active!\n
Matched via Bundle ID\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
{%s::%s} error %s writing EDSCR %s
[INSBP] bp%d addr=%08llx fpr=%08X\n
   Debug Port: SELECT %X: AVOIDED\n
Couldnt figure out the size of flash (we read: %d), using default\n
{%s} NOMEM
Could not find TAP at chip-index %d for v2 1500 config\n
\n
Gateway Version: 0x%X\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
%s construction failed
No 1500 bridges or TAPs specified (v2 plist)\n
Cannot create SoC [unknown chip identity (%d)]
Failed to read flash size at 0x%08llX : read failed\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
   JEDEC ID: 0x%08X\n
max_scan_bits is low: %d
Could not enable KIS SoC Access\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
There is no debug port associated with this chip.
XBS Version Modified: %s -> %s\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
Failed to read IDE through DAP\n
Failed to init from cpu desc armv7m cpu: %s \n
Cleaning up Each Booster Manager\n
Adding new booster path: %s\n
Failed to find a product plist for this soc %s
[1500] Error parsing bridge: %s
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
[%s]\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
CPU AP-Type: %d\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
Can't get OS build version - failed to create plist
{%s:%s@%d} Critical error encountered:
%s [RETRYING]
Probe %s with unknown port response %s
Probe %s USB-C location is %s
[1500] v2 plist missing required field 'bridges'
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
[READ] %d -> %08x\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} error %s at line %d
After powerup CMDSTAT=%08X\n
%s\n
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} %s pre_resumed\n
CPU has no regions, maybe powered off?\n
Flash unlocked...\n
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
Xtensa Core %s NOT configured\n
In Writeflash\n
1500 IR Commands:
[1500] v2 plist missing required field 'taps'
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
{%s} Failed to get watchpoint mask for %s: %s
   {%s} Before powerup CMDSTAT=%08X\n
Error Reading Device Production-Fusing\n
%d KB flash size detected.\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
error %s reading DAP MMFR0
Original Length: %d\n
AuthDebugWithTimer_t destructor \n
Xtensa Option num_bp: %d
STM32Hxxx flash programming status fault: 0x%08X\n
{%s@%d} Timeout while attempting connect to server
## ARM32cpu_t::read_register %u\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
{%s} handle ROM entry
couldn't find CPU1. this is expected sometimes.
[1500] TAP %d missing required field 'ir-cmds'
SoC does NOT support IDE Explore\n
[1500] Detected plist version %d
{%s} read ESR EL1|EL2|EL3 (%d)
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
{%s} Failed to get breakpoint mask for %s: %s
## dpw 0x%02X 0x%08X\n
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
[1500] run_steps: unknown instruction '%s'
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
\tErasing the entire chip and then programming a larger image may work,\n
CPU Die: %d\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Invalid APTABLE (%d), so using most restrictive
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Connect using RSD not supported\n
Programming STM32Fxxx...\n
AXconn or json_out are NULL
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
KIS Preflight No Need To Write to AP CSW
--> debug      size=%3d acsr=%d
   {%s} Read AP's R_MEMAP_CSW\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
{%s} ROMTABLE (nest=%d)\n
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
%s %3d'b%s\n
Failed to convert kisHubLoc %s to unsigned long long
sent %zd bytes to Probe Map Server when sending %zu
Probe Map comm: request[%s], response[%s]
Unable to convert plist file name to CFString: %s\n
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
OK: address translation resumed for %s successfully
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
{%s} host name(RSD): %s\n
Not Creating CPU: %s\n
{%s} halting %s\n
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
Can't get OS build version - failed to get build version
Initialized Logging - %s
AXportal_t Struct Is NULL
   Debug Base: %08X\n
## memapw %u 0x%016llX 0x%08X\n
AXmemap_stmflash calling STM32H7xx::eraseflash\n
{%s@%d} IOServiceClose failed, err = 0x%08x
Write Protection Error is Set\n
Failed to allocate space for table!
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
Error - STM32Hxxx reflash failed (%s).\n
KIS translator version : %d\n
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s::%s} [%s] error %s writing SCTLR_ELx
   DPv3 bus is %u bits wide\n
tckrate_check returned error %s
STM32Fxxx flash programming status fault: 0x%08X\n
%s probe[*] from Probe Map Server [local host]
We are Allocating\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
The log file has been updated with all available diagnostics.\n
Hang Address: 0x%016llx\n
Could Not Allocate All Boosters Array
CPU ASC Offset: %d\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
STM_FLASH_OPTKEYR: 0x%x\n
In %s, DEVICE ID: 0x%X\n
response == NONE; failed to get kis target info\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
Production Fused Device\n
[%s] Booster System Is Not Initialized Bailing\n
Both debug and xbs versions are set, maybe a bug: %s
Cannot create CPU descriptions from NULL info\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
Extract Offset: 0x%X for %d\n
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Die-Count: %d Current-Die: %d Die-Type: %d
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
Choose a device: 
Connecting to server, %s:%d
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s::%s} EDSCR in unexpected state. Returning %s.\n
\tTatsu AuthDebug Triage | All\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
AXjtag_explore failure - %s (%d)
Failed To Initialize Logging\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
[AstrisAsync] Activating async...\n
{%s::%s} [%s] error (%s) getting number of HW BPs
\tAligned Read Failed
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
{%s} connectName[local host]
{%s} no response from bridge
=== Found %s Boosters ===\n
Pages %d\n
DBG_CPU: %s\n
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
DBGSTATUS = %08X   res=%d\n
%s: []\n
{%s} Debug Base: %08X
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
   {%s} select %u port %u: %u chip%s\n
Can't get OS build version - failed to create URL
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
{%s} Extracted CIP Gen Number from table  (%d)
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
Exploring IDE in JTAG\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
Can't get hardware model - failed to allocate data string
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
=== Detailed %s Boosters ===\n
Booster Bundle: %s\n
component group %d\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
register lookup by name not supported when Astris is statically linked
{%s} pmgr status=%d being reported as Unknown
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
   Debug base is in legacy format\n
We Are Matching Development Booster\n
2: ARM64_SYSOP_ATS12E1W\n
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
Explore: %u chip%s\n
Request Dict:\n%s
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
Probe %s status: Busy
{%s@%d} socket connection is not available
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
caller=%s, async=%d, iterations=%lu
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
Programming STM32%s...\n
{%s} host = %s
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
%s: chip was NULL when attempting to release soc
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
Logging Context Is NULL\n
CPU Subsystem: %s\n
Complex ID: %d\n
--> master     size=%3d localwrstn=%d debug=%d
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
Found %d APs
CPU Supported in Runtime: %s\n
Target ID: 0x%X\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
[REMBP] bp%d\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
{%s} asc status=%d being reported as Unknown
Result while reading third entry: %s , entry val 2: 0x%X\n
** Unauthorized User/Network or ECID **\n
\tCould not get sector number for address: 0x%llX\n
Awaiting next chunk of big response
Matched Booster: %s\n
Modified Word To Write: 0x%08x
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
Passed NULL plist file\n
## armcpu: success status even though not all bytes written\n
Width: %d not supported
 MEM-AP %X is hung\n
      Read of JTAG-AP port %u PSTA failed with %s\n
Caught a portal that we dont have a status map for: %d
Selecting polling method %s
{%s@%d} Found cached response
[1500] %s step %d: unknown instruction '%s'
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
gmtime() returned NULL, using epoch time
==== Exception Trace ====\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
Probe Type (%d) FW Version: %s does not support KIS.
Could Not Get BoosterManagerUtility\n
Complex CPU ID: %d\n
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s} [%s] length=%u when width=%d
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
{%s} bridge timed out
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
{%s=>%s} null reference to AXcpu_t record, `cpu`
kext connect name %s\n
{%s} %s did not match any valid host
{%s} valid response from bridge
[MEM] Uncompleted; DSCR = %08x\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
pc:  0x%16s cpsr: 0x%16s %s\n
{%s} FAILURE - NULL parameter
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
After Programming (addr: 0x%08llX) Programming Error is Set: 0x%08X
Unable to allocate memory for big response
Could not find bundle () in given array: %s\n
\tWriting 0x%X bytes @ 0x%08llX...\n
En masse...\n
SoC BM Not Found, Bailing\n
[KIS] Register Index: %llu\n
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s::%s} ERROR %d(%s) resuming %s\n
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
could not perform cpu_preflight
{%s} DEVARCH read fail in CoreSight component (%s)
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
{%s} Failed to extract portal info from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: resuming HW
[AstrisAsync] Discarding response due to ASYNCSKIP state!
{%s} Component ID read fail for 0x%llx (%s)
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
X00 Part
STM_FLASH_SR: 0x%x\n
{%s::%s} halting %s\n
Error %d(%s) executing instruction 0x%08X FAST
X12 Part
Disconnected from Probe Map Server
Probe %s Device Does Not Have LocationID
{%s}#%02X cmd: %s, resp: %s
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
   JTAG-AP: Identification = %08X\n
Using 10pin connector skipping orientation check
Required Key-Value is a string, and not an array. Old booster found: %s\n
Invalid value for 'entry' tuple element - can't index
[READ] cop %d -> 0x%08x\n
read_dbg failed to access R_v7M_CLIDR
[%s] %d -> %08x\n
Result while reading first entry: %s , entry val 0: 0x%X\n
CPU Monitor[%i]: %s\n
Kick off the current process using probe %s? (y|n)\n
{%s} unsupported bridge type for %s
Could Not Allocate Info Keys Array
{%s::%s@%d [%s]} Error %s: synchronizing context
successfully updated DEMCR
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
## apr %u 0x%08X -> 0x%08X\n
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
Set custom PSD json file: %s
\tbut is not guaranteed on this device.\n
## dpr 0x%02X -> 0x%08X\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
Awaiting response from Probe Map Server
Skipping CPU %s at 0x%llx: not present in IDE\n
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
[AstrisAsync] Async mode %s
Result while reading second entry: %s , entry val 1: 0x%X\n
sending abort to clear a timeout\n
%-16s @ 0x%08llX : read failed\n
Dart Coastguarded CPU: %s\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
{%s} Error looking up architecture (%s)
no system bus AP present with AHB, trying AHB5
Creating CPU With Name: %s\n
Unable to read GPR 28
{%s} Failed to get watchpoint count for %s: %s
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
choice: %d\n
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
Banana split probe, for now I guess we will just say yes...\n
Groups %d\n
Found an async abort pending; clearing it\n
Cached async_replay capability version: %u
   {%s} Enabling debug unit\n
{%s} unable to find single_port probedaemon on port %d
{%s@%d} Unknown CS code [%u]
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
CPU PS-Register: 0x%llX\n
[READ] %d -> 0x%08x\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
{%s->%s} current EL (%d) already == target EL.\n
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
## armcpu: bad status even though all bytes read (%d)\n
OK: address translation suspended for %s successfully
{%s} Failed to extract component info from table (%d); continuing anyway
Error returned from explore_pid
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
astris_get_async_ver failed with error: %s
{%s} already collected %s, skipping
SoC has been setup using standard instantiation (setup result=%d)
{%s} Error reading CPUID (%s)
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
{%s} Reading base 0x%llx entry's component ID
can't find bid in response\n
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
{%s} unable to allocate probeInfo
{%s@%d} Unable to connect to server, %s:%d
Setting STOP CLOCK to TRUE
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
[DCC] Grabbing DTR failed: %s\n\n
[Auth Debug] External Debug Interfaces Open\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
{%s} FIFO full, try again
{%s=>%s} no soc reference; falling back to direct cpu method
AuthDebug::authenticate_probe - no need to authenticate\n
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
Debug Base: 0x%llX\n
[WRITE] %d -> %08X\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
connection created
{%s} probe [%s] added to list
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s} collect result = %s
\t Writing 0x%08llX failed: %s
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
Flash unlocked...(before erase)\n
** Add the --with-force option or use the explore_override console command **\n\n
{%s::%s} [%s] MMU not active - returning %s
Variables not setup
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
{%s@%d} Connection to server failed, error=%d (%s)
[CLEANUP]\n
   DPv3 baseptr is not valid (%X)\n
\t[MATCH_TARGETID] FAIL <= unable to find DP
Cannot create complex descriptions from NULL info\n
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
\tLeft Over Chunk Read Failed\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
{%s} PRIMECELL [DONE]
Init objects failed
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
TatsuServer Found: %s\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40022000)\n
JsonLogger: Creating new category '%.*s'
CPU Supported in Integration: %s\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
Invalid current AP (%d), adopting APTABLE (%d)
\tWhole chip...\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
{%s} flags:0x%08x
Probe %s Device Server listening on port %d
Got an error reading the DCM Control Register: %s
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
[1500] No %s.plist resource found
ERROR: nothing to do; suspending address translation for %s while already previously suspended
Breakpoint Index: %d
Connection to server accepted
read failed, using old cached as base: 0x%x
relay_set: %s -> %d
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
\t Erasing Page %d...\n
No version information found in booster: %s
--> localwrstn size=%3d debug=%d
Required key: %s @ index %d is NULL\n
AP[%d]: MEM_AP_AXI\n
{%s} explore with exploreflags 0x%X completed with error [%s]
can't find pid in response\n
[KIS] Words (Read/Write/Wrote): %d\n
BoosterManager Types:\n
--> 0x%02x = %s
{%s->%s} (top) current_el=%d
!*!*!* ****************************************************************************** !*!*!*
CPU (%s) has explore flag of: 0x%llx which is not set\n
Did Not Find Any Boosters For: %s \n
{%s} Failed to extract chip debug base from table (%d); continuing anyway
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
{%s} %s resumed\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
   {%s} Probe requires overrun detect mode.\n
probetimeout retry failed logging as hang\n
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
using standard products.plist for %s
Die Addr Info LSB: %d Mask: 0x%016llX\n
[SSTEP] bvr=%08x bcr=%08x\n
[%s] TGE is set so we traping to EL2\n
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
Cleaning up Main Booster Object\n
Multi target booster, checking for %s.plist\n
Found form-factor specific channel %u for device '%s'
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
{%s} calling _collect_hw on %s
Proceeding with full explore instead of instantiation
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Unsupported device identification 0x%03X\n
CPU Core Number: %i\n
--> psr        size=%3d bit=%d
Section 1 Offset: 0x%llX\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
Xtensa Option ocd_address: 0x%llx
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
{%s@%d} Received %d bytes when requested %d bytes.
[KIS] Portal Status: 0x%X\n
[INS_WP] 0x%016llx x %d\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
Failed to convert kisLoc %s to unsigned long long
{%s@%d} Failed to send probe command (error %d).
Mass Erase...\n
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s::%s@%d [%s]} Error %s: collecting HW
{%s::%s} HDE not set on %s. Will re-enable.
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s=>%s} null reference to CPU_t object, `cpu->state`
Erasing...\n
TAP IDCODE: 0x%X\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
   CPUID: 0x%08X\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
{%s} drop ProbeName %s
Issuing request to Probe Map Server: %s
{%s@%d} Probe response payload read when no payload indicated.
[PAR] Failed KIS Portal Access Preflight =%s (%d)
     0x%016llx: ERROR\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
Error - eraseflash failed.\n
AXjtag_srst assert failure - %s (%d)
Could Not Get BoosterManager. Need To Call AXbooster_init\n
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
Breakpoint Size: %d
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
outstanding=%zu
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
Exc Cause: 0x%x - Exc Vaddr: 0x%x
relay_get: %s = ERR
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
{%s} bridge returned an error
Passed NULL booster without custom plist\n
Can't find descriptor for group - can't index\n
[CACHEOP] %d, 0x%016llx, %d\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
Unable to read GPR %d
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
collect_responses
[AstrisAsync] Barrier hit!\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Probe Map comm error %d(%s) %s
{%s} probe device server closed the connection while trying to read data (at recv)
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
{%s@%d} Failed to find cached response
[1500] TAP %d missing required field 'chip-index' or 'irlen'
CPU: %s halting debug is now %s\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
X06 Part
Flash Address Max 0x%llX\n
Valid Portal
[1500] Error parsing bridge '%s': missing required field 'tap'
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
Dart Base Address: 0x%llX\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
[COLLECT] Chip %x\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
Raising to EL2 cause in Guest\n
     0x%016llx: 0x%04x      %s\n
{%s} _pre_resume_hw result = %s
Fabric access is blocked. Expected if production unit, won't explore further.
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
Using KIS-STM to flash, on some parts we might be too fast for this using KIS-STM
AXmemap_stmflash calling STM32F4xx::eraseflash\n
Initializing (%s) Booster's Astris API\n
Values Not The Type We Expected. Expected: Number and String\n
## armcpu: bad status even though all bytes written (%d)\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
Error while trying to authorize: %d - %s\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{%s} checking for single_port probe daemon on port %d
1: ARM64_SYSOP_ATS12E1R\n
{%s} FAILURE - malloc error
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
Error %d(%s) executing instruction 0x%08X
primateLoc
cpu_resume
Failed to read ide_table from KIS explore
fc_ite_checks=%d
Lowering from exception level[%d] other than 1, 2, 3 [%d]?
AP[%d]: unknown type\n
EXPLORE_IDENTIFY_ONLY
fn.stmflash.h7.unlock_flash.read.cr1
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_components.cpp
{%s:%s@%d} [%s] getting GPR\n
EDECR
Unknown
Successfully connected to
ONEWIRE
setProbeInfo
3679.40.30b172
[SSTEP] bvr=%08x bcr=%08x\n
probing %s status\n
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
%d.%drelease
RESPONSE_NO_PAYLOAD
ParseStream
result.read_vals(portal_group)==
ARMv7mcpu_t
ApChipID
Xtensa Option options: 0x%x
reset_dcm: %s
[1500] No %s.plist resource found
Result while reading first entry: %s , entry val 0: 0x%X\n
RF28
Invalid data breakpoint index %d
op_L32I_encode
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Main
stack.h
ANE_SYS
{%s} Exploring with option: %s\n
fn._read_special_reg.SRN_WindowBase.wb_save
Turning Debug Clock On
SoC
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s:%s@%d} [%s] reading BVR %d\n
RF62
_return_from_debug_interrupt
DCS_BC1
DCS_BC7
completedAcmds
symbol.check.loaded.AMAuthInstallRequestSendSyncPtr == NULL
{%s:%s@%d} [%s] Not idle prior to mass erase: %s\n
Unknown Command
poo
ChimpSWD
Hardware model: %s
{%s} NOMEM
received %zd bytes from Probe Map Server when have %zu
Astris Source Version: %s\n
cpu-ascdebug-offset
DBGWRAP_LITE
Failed to restore EL to %d after reading register: 0x%llx
Invalid current AP (%d), adopting latest (%d)
AXcpu_getmode
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
is_external_open
Could Not Allocate Info Keys Array
AMCP3
DEBUG CLOCK OFF
AuthDebug::authenticate_probe - no need to authenticate\n
param.info.invalid.null
ASTRIS_ERR_WAIT
empty request encountered
set.target_os
haskis
param.conn.enable_explorer == NULL
{%s:%s@%d} [%s] erase_page failed @ 0x%08llX: %s\n
cpu_readreg
result.read.dbgwrap_base==
ret.ite.read.edscr
{%s->%s} START handling exception
{%s::%s} timeout while waiting for EDSCR ITE
AXcpu_cache_clean
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_STATUS
_ocd_reg_dcr_clr
KobaSWD
UPDATE cop64 %d -> 0x%016llx\n
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s:%s@%d} [%s] Read DWT Comp %u\n
Could not load needed symbols, please make sure HomeDiagnostics is installed\n
ASTRIS_ERR_PROBEERROR
implementer
UWB
astris_user_default_set_nickname
open_flash
Processor Id
Clear
exit.exception_test_2
{%s:%s@%d} [%s] doing IR scan (DSCR EXTEST)\n
spsr_el3
AXcpu_writereg_vals
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
   {%s} (DP): status=0x%X(%s) - %s\n
Too many open files
alloc_drain_payload
reflash
Unable to allocate memory for next part of big response
AXmemap_readvals failure - %s
booster
wir2-tdo
internal.enable-timer-ovr.chip->soc == NULL
Memory error virtual addr register
hardware error reported by probe
Connection aborted: kick required by probe server
dst_ != 0
RSM
{%s->%s} exec: encode_msr(%s=0x%X (%s), scracth=%d, %d)\n
{%s} PRIMECELL [DONE]
{%s} host:%s, flags:0x%08x
astris_identify_load_booster
The document is empty.
master-debug
ARM64 SWBP not supported in T32 mode
fn._read_special_reg.ibreakenable
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
AXbooster_refresh
bits
_resume_translation_hw
ret.read.ecid
MEVADDR
resolve_portals
ret.modify.edscr.~MA
op_XSR_encode
KongSWD
AMCP2
astris_cpu_status
%s (addr=0x%llx)
ASTRIS_ERR_ANOMALY
Prefix
(data_.f.flags & kUint64Flag) != 0
X09 Part
{%s:%s@%d} [%s] Cannot initialize flash for erasure: %s\n
fn._read_special_reg.SRN_WindowBase
XACT
[1500] Error parsing bridge '%s': missing required field 'select'
PARTNO_SWDP_M0P1
AXchip_get_chip_variant
--> extrawrstn %d
Failed to restore EL to %d after writting register: 0x%llx
{%s} Component ID read fail for 0x%llx (%s)
Failed to convert kisLoc %s to unsigned long long
uri.h
M7F
copyNickname
{%s} _halt_hw result = %s
AXcpu_resume
DTLBCFG
astris_command
cpu_read_dcc
Failed to allocate JSON string
armv7m-region-axim-end
result.read_vals(version)==
_a64cpu_clear_async
ret.home_url == NULL
{%s:%s@%d} [%s] SR read (status) failed: %s\n
M7
\"%s\" not a regular register
DBGWRAP_FULL
astris_exc_bread_test_2
{%s->%s} [!is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
setway_reg
query_events
SEP
{%s:%s@%d} current_el[%d] == 1|2|3\n
LOSTCONN
Writing KEY2 During Unlock Sequence Failed\n
unable to identify chip
write.sysreg.el_check
\t\t%s\n
get_tsz
internal.clear-auth.debut_auth == NULL
[%s] EL @ end of Collect: %d\n
{%s::%s} %s resumed\n
   DPv3 baseptr is not valid (%X)\n
AXjtagap_explore
loadSchemaForCategory
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
{%s:%s@%d} [%s] Timeout waiting for flash idle: SR = 0x%08X\n\n
Setting bypass channel to: %d\n
ret.check.offset_for_content
Invalid GPR Given: %d > %D
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
MEMAP
CHAINERR
Error %d(%s) executing instruction 0x%08X FAST
Writevals: %s
encodings.h
wrstn-reg
fn._ocd_exec_instr.wsr.ddr.t2
CCSIDR
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
ASTRIS_ERR_NOAP
UNKNOWN CMD
We are done with clean up\n
{\"max_events\":%u,\"events\":[%s]}
param.conn==NULL
Table 5–179
write to CMD/STAT failed - %s
dart-cpu-sid
Failed to get Bypass Config
_get_wpcr_hw
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
[%s] m_dc_max_level %d, m_ic_max_level %d\n
MASK ERROR
Misc register 1
~/Library/Application Support/Astris/astris_prefs.plist
High level 5 exception PS
Table 5–155
ASTRIS_ERR_ASYNC_BARRIER
fn.stmflash.h7.mass_erase.write_key2
AXchip_get_stm_dockch_list
EndArray
armv7m-region-offset
Efficient-Core
dest_reg < 32 || dest_reg == 31
dbgwrap halt failed, falling back to classic method
NOTEXPLORED
local host
CortexM7
KIS Preflight No Need To Write to AP CSW
{%s::%s@%d} [FALSE] dest_gpr[%d] <= 15\n
{%s} error: %s
{%s@%d} Received %d bytes when requested %d bytes.
version
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
_ocd_reg_dsr_r
Probe %s status: Busy
Please answer y=yes or n=no.\n
?
shared_ != 0
CPU_t
PROBETIMEOUT WHILE WRITTING\n
ret.pka.verify.status.err
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_ACTUAL_LOAD
Table 5–188
reader.h
Could Not Find Booster Entry Function: %s\n
failed write of 0x%08X to DEMCR - %s
defaults.get.nickname.not_connected
\tTatsu AuthDebug Triage | All\n
internal.authenticate_dft.debug_auth == NULL
Register file 57
RF7
probe %s on host %s
cpu-xtensa-num-intr
{%s:%s@%d} [%s] Invalid device identification (0)\n
Table 5–168
RF63
Begin
Waiting for flash to idle before sector erase\n
KIS translator version : %d\n
PersiesSWD
15002AXI
DCS_BC6
False
ASTRIS_ERR_PORTAL_STATUS
m->name.IsString()
newpos == 0 || path_[newpos - 1] == '/'
Couldnt MSR: 0x%llx
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
authenticate_dft
INTERRUPT
_cleanup_hw
ASTRIS_ERR_DISABLED
Timeout waiting for flash idle: SR = 0x%08X\n
Invalid hostname or port specified as
{%s:%s@%d} [%s] CR write (clear) failed: %s\n
_gen_debug_interrupt
*
Probe %s Device Server listening on port %d
0123456789abcdef
ret.lower.after.read.aarch64hw
AXmemap_stmflash calling STM32F4xx::reflash(0x40023C00)\n
Interrupt enable bits
Table 5–150
_write_special_reg
_a64cpu_encode_mrs
ret.CFURLCreateCopyAppendingPathComponent
{%s:%s@%d} [%s] Writing PER in FLASH_CR failed during page erase: %s\n\n
primateHubLoc
_create_cpus
Stringify
Failed to allocate space for table!
{%s:%s@%d} [%s] executing MOV (diff mode)\n
check_and_clear_cpu_msr_lock
ret.write.msr_lock_reg
Unable to read CPSR
i8@?0
fn.stmflash.h7.program.writevals
{%s} checking for single_port probe daemon on port %d
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
RESUME
\tWriting @ 0x%08llX...\n
\tCould not get sector size for address: 0x%llX\n
RF43
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
{%s} connectName[%s]
cpu_lacc_status_insert
{%s:%s@%d} [%s] getting GPR 1\n
Data break 0 control
IsObject()
{%s} Error setting up memap target (%s)
ERROR!! write binary data parameters invalid\n
cpu
relay_get: %s = CMD_ERR (%s)
prettywriter.h
nullptr == file_url
{%s:%s@%d} [%s] setting GPR 1\n
{%s} DAP command nwords=%d trimmed to %lu\n
address=0x%8.8X, len=%u, rdwr=%d
fn._ocd_reg_r.ddr.memval_tgt_32
%s\n%s [%s]
Schema parse error
index < data_.a.size
\n
param.booster_handle==NULL
Basic
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
{%s} Failed to get breakpoint mask for %s: %s
GorillaSWD
GetString
itoa.h
dart-subsystem
{%s->%s} exec: encode_mrs(scratch=%d, MDDTR_EL0, true)\n
name=\"%s\")
fn._ocd_reg_r.ddr
fn._ocd_reg_r.regval
fn._read_special_reg.ibreaka0
co_coredump
!!!! FILE RADAR: Don't know how to compare two values\n
ret.ito.clear_edscr_err
param.address.invalid.>max
Temporary level
astris_cs_code_name
Failed to create SoC or no booster
ret.rx-full.mddtr
fn._collect_snr.exccause
EDBXVR0+index
astris_cfg_memap
dropping empty probeInfo (port=%u)
ACQ_STARTSTOP
!!!! DART Key %s is INVALID !!!!\n
result.read_vals(group_info)==
(system_reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) != 0
{%s::%s} [%s] MMU is already active - returning %s
WFI
VectorCatch
AuthDbg,EnSecureTestExternal
ASTRIS_ERR_OUTOFMEMORY
cpu-xtensa-num-wp
instr
_ocd_reg_w
user
PROBED_USB_RSP_ERROR
host %s with name matching %s
{%s@%d} Failed to find cached response
cpu_getmode
ACC
CPU %s not found or already removed from the map
MISC1
RF32
no data when data expected
passed
Generated JSON (first 500 chars):\n%.500s%s
codepoint <= 0x10FFFF
Cannot create DART descriptions from NULL info\n
ir-cmds
{%s::%s} waiting for EDSCR ITE
[AstrisAsync] Pause when already paused!\n
{%s} calling _collect_hw on %s
U5xx
astris_json_set_address
dart-name
AXdebug_auth_is_dft_authenticated
{%s@%d} Connection to server failed, error=%d (%s)
aod_type
Cannot create complex descriptions from NULL info\n
Table 5–184
Register file 23
probe matching %s on localhost
Probe Map comm error %d(%s) %s
start
writeToFile
RISCV
AXcpu_mmu_get_mair
{%s:%s@%d} [%s] PECR write (clean) failed: %s\n
wa
cpu_writereg_vals
Invalid encoding in string.
%Y-%m-%dT%H:%M:%SZ
component
RXO
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
Caught a portal that we dont have a status map for: %d
Could Not Find Any Boosters of Type: %s\n
{%s:%s@%d} [%s] doing JTAG scan (DSCR)\n
astris_memap_lmflash
L4xxx
shared_->refcount > 0
is.Peek() == 't'
DISP_L
DISP_R
ESR_EL2
_a64cpu_reset_catch
{%s} [!is_64] exec: ISB_SY_ENCODING\n
probeBoardNames
AMAuthInstallLogSetHandler
Long Packet
targetid/instance must both be set or both be unset
Unable to restore EL0
va
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
AP[%d]: MEM_AP_AXI\n
{%s:%s@%d} [%s] FLASH_CR PG read failed: %s\n
cpu_hwwp_insert
[%s] %s
DSP
      Read of JTAG-AP port %u PSTA failed with %s\n
Processor status
Probe Map comm error %d(%s) %s [%s]
Realloc
Enabling USB Gateway
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
param.op.AXCPU_WP_DISABLE.unsupported
BLK
tokens_ == 0
setTargetInfo
.start_time
Banana split probe, for now I guess we will just say yes...\n
createKey
ACCHI
ITM
{%s:%s@%d} m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX\n
Failed to sync prefs at end
Request Dict:\n%s
ret.auth.data == NULL
GetState
APCIE_ANS0
resolve_platform_details
param.ticket_data == NULL
normal
Unknown Subcommand
UNKNOWN_CS_CODE
STM32G031xx
Failed to execute DRPS, in order to restore PSTATE after exception
could not perform cpu_preflight
\tLeft Over Chunk Read Failed\n
Erasing A Page
{%s@%d} {%s[select]} %d(%s) [RETRYING]
astris_get_hang_crumb
{%s:%s@%d} [%s] moving reg to cop\n
elr_el3
write.dspsr_el0 NOT DIRTY
write.dlr_el0 NOT CACHED
op_RSR_encode
JsonLogger: Creating new category '%.*s'
astris_kis_poll_cfg_reg
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
General register 7
CortexA8
AlignBuffer
_collect_hw
{%s::%s@%d [%s]} Error %s: checking exception
%s SoC created
bypass-configs
DISPSEC
{%s:%s@%d} [%s] reading CCSIDR[L1-I]\n
PARTNO_JTAGDP
Register file 27
{%s[recv]} %d(%s) [RETRYING]
CPU at Index: %d has to specify only one AP Type or AP Select\n
CTI_OUT_EN0
ret.board.copyPairForPref
ret.pka.nonce.status.err
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
Reading FLASH_CR1 failed during unlock sequence\n
Another application is connected to
cpu_mmu_configure
sel-sib-network
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
AXcpu_flush_icache
Unaligned Read @ 0x%llx Width: %d Bytes: %d
DAP
LBEG
param.buffer.invalid.null
_%04d-%02d-%02d_%02d.%02d.%02d
soc-pid
{%s} [%s] EDSCR with ITO set - unable to recover.\n
R
{%s:%s@%d} [%s] \tFailure: @ 0x%08llX failed to verify\n\n
reg_addr_offset=0x%4.4X, m_ocd_base_address=0x%8.8X
wait_for_bank_flash_idle
Invalid port[%s] for probe %s provided by probe server
Unable to connect to probe server
=== Detailed %s Boosters ===\n
CACHE
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s:%s@%d} [%s] PWR_VOSR write failed: %s\n
param.num_addr_bp_regs.invalid.2
IsString()
{%s} Failed to extract component info from table (%d); continuing anyway
astris_update_ap_slave
some generic JTAG hardware fault
ASTRIS_ERR_TGTSTATE
cpu_mmu_get_page_shift
Data break 1 address
Clear requests in INTERRUPT
ASTRIS_ERR_NOTUNIQUE
receiving response
GetUri
RegionEnd
ret.read.sysreg.scratch.check_exception
setTargetIdentifiers
[%s] %d -> %08x\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
MEPS
Table 5–182
Memory Access Port
MISMATCH
[ANAMOLY] Could not find AXcpu_t object for CPU\n
result.read_vals==
res.setup_transaction_objects
_a64cpu_read_edscr
DBREAKA0
;
fn.stmflash.h7.eraseflash.unlock
host_to_components
kan
debug-acsr
CPU: %s halting debug is now %s\n
PARTNO_1176JZFS
da_base == 0
Output
[PAW] Failed KIS Portal Access Preflight =%s (%d)
param.cpu_name == NULL
param.subsystem == NULL
Need to be connected to set nickname
Using 10pin connector skipping orientation check
cpu_cache_info
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis.cpp
Portal Group Offset: 0x%X Entries: %d\n
ret.reg.read.K_PKA_REG_NAME_DBG_STATUS
debug_info
Port
Logger internal is null
Unable to disassemble_at_addr 0x%016llx
AXconn_identify_soc_collateral
{%s:%s@%d} [%s] \tCould not unlock flash before erase\n\n
KF-ETM
2: ARM64_SYSOP_ATS12E1R\n
hwwp_enable
Instruction count level
gmtime() returned NULL, using epoch time
\tAstris does not support page-erase beyond first %d KB of flash.\n
DEMCR write failure - %s (%d)
BoosterManager.SWDFlash
cpu_hwwp_remove
_a64cpu_read_sysreg_hw
{%s} exec: DC_CVAC_X1_ENC\n
   --> IDR: %08X\n
 (eng)
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
[READ] %d -> %08x\n
Section 5.2
Register file 63
XBS Version Modified: %s -> %s\n
astris_ide_get_pid
{%s::%s} [%s] MMU not active - returning %s
UNKNOWN 
result.read_vals(group0)==
%s NOT configured\n
\tAligned Read Failed
astris_memap_debug_writebuf
PROBED_SLEEPING
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
STM32G0A1xxx
wir-wrstn
MTP
{%s:%s@%d} [%s] writing ITR\n
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
SWD Slave Unavailable
Hang Radar Info:\n%s\n
ret.faul_reg_latch
{%s::%s} ERROR %d(%s) resuming %s\n
Highest EL: %d, -- Min Op EL: %d
Translate Stage Chosen: %d\n
astris_memap_bus_write
DESIGNER_ARM
HIFI3_2
stdout
{astris_probed_print_events_from_json} not supported in this build configuration
%02u:%02u:%02u.%06u|%s <%s> %s
\tFailure: only %u of %u write transfers were done\n
%d:%d%s
Failed to init from cpu desc armv7m cpu: %s \n
Dart Name: %s\n
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
AMAuthInstallSupportDictionarySetBoolean
Register file 10
file/object not found
No connection attempt description
info
AXchip_get_chip_id
\t Erasing 0x%08llX...\n
{%s:%s@%d} [%s] writing WCR %d\n
ParrotSWD
SWDFlasher
AXexplore_enable_cpu
write.dspsr_el0 NOT CACHED
fn._read_special_reg.dbreakc1
ASTRIS_ERR_INVALCOMMAND
PERSEIS
quiesce
CPU.ARM32
gpr != 31
Programming STM32%s...\n
OCD control register, set
AXLOG
%s %s:l=%u,c=0x%X,i=0x%X,f=0x%X
\t[MATCH_TARGETID] FAIL <= unable to find DP
Booster Info:\n%s
Programming STM32Fxxx...\n
_reg_desc_lookup_by_index
Failed to convert primateLoc %s to unsigned long long
SCANDEBUG
document.h
ir <-
[KIS] Words (Read/Write/Wrote): %d\n
PARTNO_SWDP_SOC600
fn._ocd_exec_instr.TIEWriteProtectedI
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
Complex Address: 0x%llX\n
gpr < 32
[AsyncSnapshot] #%zu: %s\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
R8
Corruption detected selecting probe from probe server
armv7m-region-axim-start
{%s::%s@%d} [FALSE] val[0x%08llX] < UINT32_MAX\n
_sw_breakpoint_remove
{%s:%s@%d} [%s] FLASH_WRPR1BR write failed: %s (continuing)\n
Table 5–137
%s-%06X
false
## armcpu: bad status even though all bytes read (%d)\n
Select == %d
ret.reg.write.K_PKA_REG_NAME_DBG_INPUT_START
target is probably resetting
{%s} hostname:%s, flags:0x%08x
{%s:%s@%d} [%s] \tFailure: only %u of %u read transfers were done (%s)\n\n
Section 1 Offset: 0x%llX\n
ARMV6M
{%s} FIFO full, try again
ret.dbgap.memap_read
fn.stmflash.h7.wait_bank_flash_idle.timeout
SoC must have a DAP
cpu_go
from != 0
{%s:%s@%d} [%s] executing MRRC\n
{%s} asc status=%d being reported as Unknown
op_SDDR32_encode
%s %3d'b%s\n
fn.stmflash.h7.unlock_flash.write.cr1.key2
pnav_filter_out_kis_stm
StringEqual
DEDICATED
fn._setup_instr_bp.bp_state
assert
opcode
{%s} Unrecognized Component: %08X (class %u)
fn.ocd.debugcause.di.incorrect
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
{%s:%s@%d} [%s] Address must be aligned to length\n
ASTRIS_ERR_NODATA
Error closing %s [%d]
Probe %s LocationID Info is %s
FWUPDATE
panic_diagnostic
New format for cip gen register, unsupported: %d\n
{%s:%s@%d} [%s] reading DTRTX\n
m_wp_details
RF39
fn.stmflash.h7.program.bank_id
comparing against match entry %d: %s
Invalid Xtensa CPU OCD.DEVID = 0x%8.8X. Should be 0x%8.8X (LE) or 0x%8.8X (BE)
failed to create log dump file
Dart Coastguarded CPU: %s\n
bid
ENABLED
\t Sector %u failed: %s\n
Register file 49
Probe
SPIXACT
Failed to open file for writing
astris_explore_enabler_init
ARM32cpu_t
Table 5–161
RF48
fn._ocd_exec_instr.wsr.ddr.t1
fn._ocd_exec_instr.wsr.ddr.data_reg
:
unable to transfer command to/from remote probe
result.booster_api_vers==NULL
param.invalid.content-type
Failed to Identify & Explore Chip via KIS: %d (%s)\n
EXCCAUSE
{%s} strsep empty so match any probe [localhost]
Miss fraction part in number.
AXcpu_go
remote probe is currently in use
Toto
DIAGS
unpack_response
Could Not Find a DCM Portal
pmu-name
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
\tFailure: region @ 0x%08llX failed to verify\n
Append
{%s} bridge returned SLVERR
{%s} _resume_hw result = %s
Listing
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
JSON
newpos <= pathpos
MEM1500
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
MAC16 Data register 0
RASID
Valid Portal
[KIS] Address: 0x%llX\n
{%s:%s@%d} [%s] getting GPR 0\n
{%s:%s@%d} [%s] moving COPROC reg to GPR 0\n
L3
{%s:%s@%d} [%s] End of Operation Check Failed, After Mass Erase\n\n
Literal base
fn._write_window_base
!!!! Critical Error:  dspsr_el0 NOT CACHED !!!!\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
ASTRIS_ERR_IFSTATE
fn.stmflash.h7.eraseflash.invalid_bank/sector
Unable to connect to %s - %s
parse_soc_info_from_booster
cpu_readmem
HCR_EL2
_write_memory_fast_try
%d.%drc%d
coredump
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Communication error occurred while connecting to
ret.read_all_breadcrumbs
Failed to raise EL to %d to write register: 0x%llx
Failed to write register: 0x%llx val: 0x%llx
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
R13
Register file 51
Unable to register assert upcall %s (Insufficient memory)
invalid command
operator[]
Failed to populate component info
   Debug Port has unknown type\n
{%s} FAILURE - NULL parameter
EXPLORE_GENTLY
PARTNO_SWDP_M23
symbol.check.loaded.AMAuthInstallApSetParametersPtr == NULL
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
cpu_cache_info_group0
Failed to convert CFString to C String.
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
{%s:%s@%d} [%s] PECR read (clear) failed: %s\n
AXconn_showname
Failed calling AppleSOC_t::switch_taps\n
.user
Failed to read flash size at 0x%08llX : read failed\n
End of Operation Bit Is Set - %s
GitHashDebug
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
!!!! Critical Error: GRPS[1] cached !!!!\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
NC
CCOUNT
GPR
     0x%016llx: ERROR\n
fn._ocd_reg_r.DDR
RESPONSE_PAYLOAD
getOrCreateArray
{%s} unsupported bridge type for %s
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
Xtensa Option non_tie_ranges: %zu range(s)
Connected to Probe Device Server [Default Log]
setCategoryValue
ParseString
Logging Context Is NULL\n
get_sw_info
{%s:%s@%d} Restoring from exception level[%d] other than 1,2 or 3\n
SUCCESS
HardwareStep
time out reported by probe
[ARCH32] Failed to exec MRS to move contents of MDDTRRX (containing val to write) into scratchscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
update
   Debug Port: SELECT %X: DISABLED\n
Ring ASID values
{%s@%d} Unable to create socket
Portal Group Base: 0x%llX \n
EL2h
[RESUME] Chip %x\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
is_ecid_zero
Failed to create optional file. Not fatal, moving on
low word
Table 5–163
Busy
Base::level_stack_.template Top<typename Base::Level>()->inArray
data-size
PowerOff
{%s:%s@%d} [%s] write to CMD/STAT failed\n
chip is 0??\n
mmu_init
FLASH_WRPR1BR
tar
set.success
Flash unlocked...(before erase)\n
Write Protection Error is Set\n
Component Group Offset: 0x%X\n
_exec
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
Table 5–134
General register 12
The debug port associated with this chip has not been explored.
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, &d, %d, false, %d)\n
   {%s} select %u port %u: %u chip%s\n
internal.enable-timer-ovr.debut_auth == NULL
{%s:%s@%d} [%s] \tCould not erase flash\n\n
{%s:%s@%d} [%s] FLASH_SR read failed while polling busy bit: %s\n\n
CSE
failed to read memory
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
Warning: spun for a long time (> %ld seconds)\n
{%s:%s@%d} [%s] \tCould not read the flash size\n\n
invalid environment variable
UNKNOWN
param.portal_base == 0
{%s::%s} write OK but took %d tries
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
ret._setup_wp
load_framework_at_path
Table 5–152
MiscCortex_t
We are in clean up\n
name
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
ret.m_lam.paccess_read
param.op.invalid
diagnostic_checks
AXconn_kis_get_stm_probename
write_register
{%s} already collected %s, skipping
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
address =0x%X is too large for 32 bit unsigned.
Invalid reg_index %u
/usr/local/share/astris/boosterpack
Register file 22
CS-ETB
ret.read.stepping_stone
RF33
fn._ocd_reg_r.DSR
var.bp.invalid
astris_json_logger_delete
addMember.description
ret.exec.drps
AXcpu_halt
{%s} ROMTABLE (nest=%d)\n
_get_arch_hw
applesoc == nullptr
Mass Erase...\n
fn._write_special_reg.ibreaka1.address
param.bp_info->size.invalid.>4
ARMV8M
get_page_shift
ret.clear_dft_authentication
write_reponse_and_check_authentication
ASTRIS_ERR_ISCONN
1.0
{%s::%s} error %s writing EDSCR %s
Warning: chip exploration did not complete successfully (%s)\n
AXdebug_auth_authenticate_dft
Misc_Rtx117x_t
Could Not Get BoosterManager. Need To Call AXbooster_init\n
--> master     size=%3d localwrstn=%d debug=%d
{%s} exec: DC_CIVAC_X1_ENC\n
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
[INIT]\n
Memory error PC register
special reg. number %u not present
fn._ocd_exec_instr.wsr.ddr.t1.1
MemoryBlock_t
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, %s=%d, %d)\n
AXcpu_swbp_insert
X00 Part
Register file 53
bp_index=%d
AXI Error
%x.%02x%s
Could Not Get BoosterManagerUtility\n
D0-PKA
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
ret.nop
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Register file 46
Created Connection - : %s
{%s:%s@%d} [%s] updating DFAR\n
{%s:%s@%d} [%s] doing JTAG scan (DIDR)\n
ret._release_gateway_control
GetType() == kNumberType
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
{%s:%s@%d} [%s] Programming failed: %s\n
DCS13
ASTRIS_ERR_BLOCKED
{%s@%d} Probe reported connection lost [PROBEEOF].
DISCONNECT
Value is null
{%s:%s@%d} [%s] reading PRSR (lsr)\n
src_reg < 32 || src_reg == 31
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
s
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
Successfully Authenticated DFT\n
NOP
{%s:%s@%d} [%s] moving DTRTX to GPR\n
ITO
AXmemap_read_get_field
Failed to explore chip: %d
{%s@%d} IOServiceClose failed, err = 0x%08x
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
irlen
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
Failed to safe raise to EL=%d
ret.createKeyWithPrimate
Cause of last exception
SAR
Invalid bp = %u. Should be in range 0..1.
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
PS
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
ret.dfu.dcm.reset
PMP
astris_ide_get_cpu_halt_group
handle_pending_async_aborts
Fabric access is blocked. Expected if production unit, won't explore further.
api.is_prod.chip == NULL
fn._ocd_exec_instr.rsr.ddr.addr_reg
Programming Error is Set\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
Going To Create Generic ARMV7m, but typehint is present (%s)\n
fn._ocd_exec_instr.rsr.ddr.r0_r12
MODE
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
Table 5–158
Debug Port
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
Data break 1 control
param.cpu_reg_file_size.invalid.1
wb=%u
connecting to selected probe (user-specified single_port)
SWDFlasher.STM32L15xC
_a64cpu_read_vfpreg_hw
ret.reg.read.K_DA_REG_NAME_SECURE_MODE
SWD KIS Command is NOT Multiple of 8
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_stmflash_h7xxx.cpp
fn.stmflash.h7.unlock_flash.write.cr2.key1
recoverable
[1500] TAP key is not a valid integer
_get_wpaddr_hw
Length is 0
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
AXmemap_stmerase
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
Enabled
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
ASTRIS_ERR_NOSOC
ret.astris_disassemble_at_addr
cpu-armv7m-base-offset
_a64cpu_write_sysreg_hw
[PREFS] Key: %s - Val: ??
str != 0 || len == 0u
cpu-runtimes
cpu-xtensa-non-tie-ranges
tap
astris_ide_get_revision
{%s:%s@%d} [%s] writing DRCR (STICKY)\n
Memory map ID
--> 0x%02x = %s
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
result.read.portal.s2r_fsm
{%s->%s} [aarch64] exec: encode_mrs(%s=%d[%s], MDDTR_EL0, %d)\n
copyNicknameForPrimate
EXPLORE_WITH_AUDIO
AXdebug_auth_clear_auth
op_S16I_encode
{%s} no TAP detected that supports 1500
M4F
%s constructed
{%s:%s@%d} [%s] reading DSCR\n
CSSELR
HTTP transaction running in background
{%s:%s@%d} [%s] failed preconnect\n
CTI_INT_ACK
init_hw.read.fpb.rev
AuthBase_t::init failed (AuthDebug_t)
Successfully Authenticated Probe\n
```
