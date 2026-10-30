# `/usr/local/share/astris/boosterpack/swdflashers/arm_stm32_swdflasher.booster/arm_stm32_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,843,744 bytes.

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
Initialized %d 1500 bridges\n
Failed to create Xtensa CPU %s \n
{%s} Failed to extract ECID from table (%d); continuing anyway
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
AP given is not a MEMAP
SSO is DISABLED\n
setCategoryValue: path='%.*s'
\t Erasing 0x%08llX...\n
Groups %d\n
     0x%016llx: 0x%04x      %s\n
DBGCTRL = %08X   res=%d\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
{%s@%d} IOServiceOpen failed, err = 0x%08x
!*!*!* ****************************************************************************** !*!*!*
We are Allocating\n
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
CPU: %s halting debug is now %s\n
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
type_hint not NULL, but creating a placeholder, this is off
{%s} Reading base 0x%llx entry's component ID
Successfully Authenticated\n
\t[MATCH_TARGETID] FAIL <= unable to find DP
User created bundle found, ignoring version checking via plist
=== Detailed %s Boosters ===\n
[1500] No %s.plist resource found
[%s] TGE is NOT set. Traping to EL1 allowed.\n
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
Xtensa Option num_high_pri_intr: %d
ERROR!! write binary data parameters invalid\n
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
[1500] Error parsing bridge '%s': missing required field 'select'
Found an async abort pending; clearing it\n
[HALT] Chip %x\n
[AstrisAsync] Deactivate while async is not active!\n
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
{%s} probe_match = %s
pc:  0x%16s cpsr: 0x%16s %s\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
{%s} _halt_hw result = %s
{%s} _resume_hw result = %s
DEMCR write failure - %s (%d)
!!!! FILE RADAR: Don't know how to compare two values\n
BoosterManager Types:\n
{%s} FAILURE - NULL parameter
Error - STM32%s reflash failed (%s).\n
{%s} host = %s
Error closing %s [%d]
{%s@%d} IOServiceClose failed, err = 0x%08x
\tErasing the entire chip and then programming a larger image may work,\n
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
{%s} halting %s\n
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
{%s} host:%s, flags:0x%08x
Explore flags indicate IDENTIFY_ONLY; bypassing _create_cpus and _postinit_hw phases
[CACHEOP] %d, 0x%016llx, %d\n
[REMWP] wp%d\n
{%s} ROMTABLE (dbgbase=0x%llx)
Set custom PSD json file: %s
{%s} no response from bridge
Found form-factor specific channel %u for device '%s'
[REM_HWBP] bp%d\n
{%s} connectName[local host]
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
DEMCR: 0x%08X -> 0x%08X
[AstrisAsync] Activate while async is already active!\n
%s: []\n
## dpw 0x%02X failed (%s)\n
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Complex CPU Name: %s\n
error %s checking for data abort(first)
SSO info present but SSO disabled.
{%s} strsep empty so match any probe [localhost]
%2d) %s %s [Busy]%s\n
{%s@%d} Received %d bytes when requested %d bytes [%s].
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
{%s::%s@%d [%s]} Error %s: flushing HW state
   Debug Port: SELECT %X; error: %s, retrying..\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
{%s} PRIMECELL [DONE]
   Debug Base: %08X\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
{%s} probe_port = %d
Die-Count: %d Current-Die: %d Die-Type: %d
WARNING, reserved / slide bits not zero! Zeroing out!\n
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
probetimeout retry failed logging as hang\n
Complex Name: %s\n
batch_cmd_count: %d
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
[AstrisAsync] replay preflight: Async not active!\n
\tTatsu AuthDebug Triage | All\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
connection created
{%s::%s} error %s writing EDSCR %s
X12 Part
AXmemap_stmflash calling STM32L4xx::reflash()\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
[Auth Debug] External Debug Interfaces Open\n
Request Dict:\n%s
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40022000)\n
DHCSR write failure - %s (%d)
CPU at Index: %d has to specify only one AP Type or AP Select\n
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s} Failed to extract IDE Group 2 address size from table (%d); continuing anyway
Result while reading first entry: %s , entry val 0: 0x%X\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
Could not enable KIS SoC Access\n
Error status from AMAuthInstallSsoEnablePtr = %i
{%s} (end) current_el is now %d
{%s} Error setting up jtag-ap target (%s)
{%s} Batch attitude key created for %p thread %#llx key %lu
Probe %s removed during selection process
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
[%s] {%s->%s} END handling exception
{%s} NOMEM
Probe %s status: Idle
relay_get: %s = ERR
unable to identify chip
[KIS] Portal ID: %d\n
Koko probe, for now I guess we will just say yes...\n
\n
## ARM32cpu_t::read_register %u\n
[READ] %d -> %08x\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
[Auth Debug] Ticket Active, Debug Interface Locked\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
2: ARM64_SYSOP_ATS12E1R\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
can't find pid in response\n
JsonLogger: Creating new category '%.*s'
[KIS] Register Read/Write/Wrote: %d\n
Failed To Init Booster's Astris API In: %s with %s (%d)\n
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
STM_FLASH_KEYR: 0x%x\n
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
\tLeft To Read (%d) < width (%d).\n
received %zd bytes from Probe Map Server when have %zu
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
   JTAG-AP: Identification = %08X\n
SoC not identified by IDCODE - enumerating instead of instantiating
AP[%d]: MEM_AP_AXI\n
=== Ending Gather and Clear ===
We are done with clean up\n
CPU AP-Type: %d\n
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
\tReading left over chunk 0x%x @ 0x%llx\n
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
no system bus AP present with AHB, trying AHB5
Found another target for the plist\n
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
\tAligned Read Failed
Probe %s LocationID Info is %s
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s} %s resumed\n
PKA Base: 0x%llX\n
Found match - bypass_device: %s; channel: %d\n
Probe Type (%d) FW Version: %s does not support KIS.
Dart CPU SID(s): %s\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
Unable to create pthread key for conenction. errno=%d %s.
Cleaning up Each Booster Manager\n
{%s} Extracted CIP Gen Number from table  (%d)
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
{%s} 0 words from probe when %d words left to read for address 0x%016llX
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
Couldnt figure out the size of flash, defaulting to 2MB\n
Probe %s removed before port determined\n
AXportal_t Struct Is NULL
Cleaning up Main Booster Object\n
outstanding=%zu
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
   Debug Port not responding (%s)\n
\tWriting 0x%X bytes @ 0x%08llX...\n
AXmemap_stmflash calling STM32Lxxx::reflash(0x40023C00)\n
{%s} empty response string provided
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
relay_get: %s = %d
Error - eraseflash failed.\n
Failed to convert primateHubLoc %s to unsigned long long
{%s@%d} Probe reported connection lost [PROBEEOF].
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
component group %d\n
%s constructed
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
      Select port %u: already explored..re-exploring\n
Previous attempt to connect to probe failed: %d (%s). Retrying...
{%s} %s did not match any valid host
Unable to allocate memory for big response
[1500] run_steps: unknown instruction '%s'
pmu-name: %s\n
Table Size: %d\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
[MEM] Uncompleted; DSCR = %08x\n
read failed, using old cached as base: 0x%x
Error %s connecting to server %s:%s [RETRYING]
{%s} probe [%s] added to list
Start Address=0x%08llX....End Address=0x%08llX
{%s::%s} OSLK did not clear (val = 0x%08X) [write_tries = %d].\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
{%s} setting up nameless target (address=0x%llx)
JsonLogger: Wrote %zu bytes to '%s'
{%s} [%s] m_exception_level=%u\n
{%s::%s} failed: %s
Init objects failed
Asked To Write To A Negative Register Index
[1500] TAP %d missing required field 'chip-index' or 'irlen'
Unknown number of groups in the explore table; can't parse group attributes
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40022000)\n
Cannot create DART descriptions from NULL info\n
[1500] TAP %d missing required field 'ir-cmds'
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
[AstrisAsync] Pausing Async Mode\n
ERROR: nothing to do; suspending address translation for %s while already previously suspended
ERROR: unable to suspend translation for %s
Failed to access new_cpu status
## dpr 0x%02X failed (%s)\n
CPU Core Number: %i\n
Failed to get DFU Type
Early dbgwrap base extracted: 0x%llx\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
Found %d APs
{%s} handle ROM entry
{%s=>%s} null reference to AXconn_t record, `conn`
[Auth Debug] Disabled\n
Start Page: %d\n
Invalid file name: \"%s\". File names must not start with '.'
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
Programming STM32Hxxx...\n
Using 10pin connector skipping orientation check
{%s->%s} current EL (%d) already == target EL.\n
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
Probe %s removed prior to kick\n
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
[%s] {%s->%s} Transitioning to exception level %u.\n
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
Read error (%s) @ 0x%08llX - retrying.\n
relay_get: %s = CMD_ERR (%s)
\t[MATCH_FOUND] identified chip: %s
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
failed read from DEMCR - %s
[AstrisAsync] Discarding %zu completed command(s)\n
HOSTID=0x%x which is invalid, skipping orientation check
Please answer y=yes or n=no.\n
{%s@%d} Found cached response
\tAstris does not support page-erase beyond first %d KB of flash.\n
Debug Clock Already Enabled
Error happened when reading edscr. Retry #%i\n
Successfully Authenticated DFT\n
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Highest EL: %d, -- Min Op EL: %d
{%s} %s status is '%s' [Status Read %d times]\n
{%s} FAILURE - malloc error
Error - STM32Lxxx reflash failed (%s).\n
Verification Mismatch starting at offset %d\n
Dumping Process Tree
VBAR: %#llx\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
Can't get hardware model - failed to convert to C string
KIS translator version : %d\n
** Add the --with-force option or use the explore_override console command **\n\n
2: ARM64_SYSOP_ATS12E1W\n
[AstrisAsync] Pause when already paused!\n
AP[%d]: MEM_AP_AHB\n
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
   DPv3 bus is %u bits wide\n
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
{%s} wrote %d words to probe when %d words provided in request
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
OS build version: %s
response == NONE; failed to get kis target info\n
{%s@%d} Timeout while sending probe command.
CPU ASC Offset: %d\n
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
   Debug Port has unknown type\n
!!!! DART Key %s is INVALID !!!!\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
Switch to primate res: %s\n
Awaiting next chunk of big response
[KIS] Portal Status: 0x%X\n
Target ID: 0x%X\n
{%s} DEVARCH read fail in CoreSight component (%s)
Error status from AMAuthInstallSetSigningServerURLPtr = %i
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
Gathered Info:\n%s
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
{%s@%d} Drain empty on decr [%s].
start rev and/or end rev is NULL; skipping cpu_desc override\n
   {%s} Clearing HNONSEC on AP \n
X00 Part
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
TatsuServer Found: %s\n
Previous authentication in-flight, wait for it to finish\n
ERROR!! Couldn't save %s binary data\n
{%s@%d} Failed to find cached response
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
[KIS] Address: 0x%llX\n
[1500] Error parsing IR command: %s
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
{%s} asc status=%d being reported as Unknown
\tCould not read the flash size. Using default 1MB size.\n
{%s}#%02X cmd: %s, resp: %s
AXmemap_read failure - %s
\t Sector %u...\n
Connection to server accepted
AXjtag_srst deassert failure - %s (%d)
{%s} Failed to extract die infofrom table (%d); continuing anyway
[FLUSH]\n
error %s reading DAP MMFR0
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
Portal Status, Changing STATUS and CMD/STAT to reflect
%s given a NULL conn object
using multi-target booster products_%s.plist
[AstrisAsync] Barrier hit!\n
ERROR: nothing to do; resuming address translation for %s without previously suspending it
   {%s} select %u port %u: %u chip%s\n
Subsystem Monitor Key does not exists: %s\n
{%s} host name(RSD): %s\n
Probe Map comm: request[%s], response[%s]
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
{%s} bridge returned an error
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
Gathered:\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Xtensa Option ocd_address: 0x%llx
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
WARNING: %d KB flash size detected.\n
Failed to get KIS translator version\n
Extract Offset: 0x%X for %d\n
## armcpu: bad status even though all bytes read (%d)\n
   Debug Port: SELECT %X: SKIPPING\n
## memapw %u 0x%016llX 0x%08X\n
Invalid Size Given for AP AP=%d Size=%d
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
    %s(): %s
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s} category=%d
[AstrisAsync] Barrier before pause\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
kext connect name %s\n
Old ProbeDaemon does not support this command
Error returned from explore_pid
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s} Unable to read SP_EL0
AP[%d]: JTAG_AP (Exploring Later) \n
%s probe[*] from Probe Map Server [local host]
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
no debug bus AP present when expected; after sysap is NULL
{%s} Unrecognized Component: %08X (class %u)
Subsystem Monitor[%i]: %s\n
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
{%s:%s@%d} Critical error [radar already requested]
Probe %s selected
Breakpoint Enabled: %s
{%s} 0 words requested for read at address 0x%016llX
Explore: %u chip%s\n
Xtensa Option dbg_intr_level: %d
Abnormal %s(%d) termination: Assert Area Mask = 0x%016llX
%s probe[*] from Probe Map Server [%s]
Probe %s Device Does Not Have LocationID
Done.\n
Flash Size %d KB\n
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
unknown match criteria type: %d
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
      Explore of JTAG-AP port %u failed with %s\n
Original Length: %d\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
setCategoryValue: getOrCreateObject failed for '%s', value will be written at document root instead of nested object
Initializing Booster Layer\n
!!!! CPU Key %s is INVALID !!!!\n
Warning: chip exploration did not complete successfully (%s)\n
STM_FLASH_OPTKEYR: 0x%x\n
Failed to convert kisLoc %s to unsigned long long
Exception %d Stack Trace
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
--> master     size=%3d localwrstn=%d debug=%d
{%s} Failed to extract chip debug base from table (%d); continuing anyway
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
{%s} Debug Base: %08X
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00,single)\n
AXmemap_stmflash calling STM32F2xx::eraseflash\n
{%s:%s@%d} Critical error encountered:
CPU state %d (stm_preflash)
Could Not Allocate Info Keys Array
Complex Type: %s\n
error trying to unlock MSR %s
AXmemap_stmflash calling STM32F7xx::eraseflash\n
Can't get OS build version - failed to open ReadStream
Hang Radar Info:\n%s\n
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
New format for cip gen register, unsupported: %d\n
Die Config Disabled\n
==== User Error Messages ====\n
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
{%s::%s} %s pre_resumed\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
Creating CPU Returned: %s\n
Could Not Get BoosterManager. Need To Call AXbooster_init\n
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
Going To Create Generic ARMV8\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
Skipping CPU %s at 0x%llx: not present in IDE\n
In Preflash\n
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
{%s} Thread %#llx clearing key %lu
Can't get hardware model - failed to get property
Initialized Logging - %s
Selecting polling method %s
gmtime() returned NULL, using epoch time
Passed NULL plist file\n
[1500] IR command '%s' missing required field 'opcode'
{%s=>%s} AXconn_t has no chips
{%s@%d} Unable to connect to server, %s:%d
Got an error writing 0x%X the DCM Control Register: %s
{%s} Failed to extract target ID from table (%d); continuing anyway
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
{%s::%s} [%s] length=%u when width=%d
Replacing key with value
{%s::%s} [%s] !bpwp_initted, retrying init
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
In Postflash\n
{%s} read[ED32] of %s @ address 0x%016llX = 0x%08X
{%s=>%s} null reference to AXchip_t[0]
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
STM_FLASH_CR: 0x%x\n
In %s, DEVICE ID: 0x%X\n
connection about to be destroyed
{%s} unable to allocate probeInfo
[%s] EL @ end of Collect: %d\n
[AstrisAsync] Failed to restart Async batch\n
Error Reading Device Production-Fusing\n
Preferences does not exists: %s, creating one.\n
{%s} Found extra info in = %s, chopping string
{%s} Component ID read fail for 0x%llx (%s)
## memapr %u 0x%016llX -> 0x%08X\n
CPU with %s Not Created via Name
HOSTID bit not set\n
Failed to read ide_table from KIS explore
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
X06 Part
AXmemap_readvals failure - %s
[1500] %s step %d missing required field 'instr'
Chip Revision: 0x%X\n
{%s} Thread %#llx key %lu freeing a suspended attitude for info %p
replay_counter=%lu, last_replay=%d
SOC AP[%d]: JTAG_AP\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
%s SoC created
AXjtag_srst assert failure - %s (%d)
[1500] Using %s.plist
[1500] Error parsing TAP description
[1500] Error parsing bridge '%s': missing required field 'tap'
{%s::%s@%d [%s]} Error %s: checking exception
[AstrisAsync] Deactivating async...\n
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
AuthDebugWithTimer_t::need_to_authenticate super returned false; continuing \n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
{%s} status=%d being reported as Unknown
   MEM-AP not enabled\n
Setting CPU %s is_boot_core to %d\n
Min Component - %s\n
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
{%s} Unable to read CPSR
{%s} explore with exploreflags 0x%X complete [%d chip%s]
      Select port %u: AVOIDED\n
Astris Version Set: %s
{%s} %s
--> extrawrstn %d
[WRITE] %d -> %08X\n
[TTBR_INDEX: %d] unknown granularity (0x%X) - using default page size
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
STM_FLASH_AR: 0x%x\n
Can't get OS build version - failed to allocate buffer
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
[PCW]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
The debug port associated with this chip has not been explored.
Too many portals, we are at portal: %d while max is %d\n
Failed to sync prefs at beginning
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
\tFailure: status errors: 0x%08X\n
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
Cannot create complex descriptions from NULL info\n
Xtensa Option reg_file_size: %d
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
## armcpu: bad status even though all bytes written (%d)\n
   Debug Port: SELECT %X: AVOIDED\n
## apr %u 0x%08X -> 0x%08X\n
%s\n
Complex ID: %d\n
{%s} Failed to extract IDCODE from table (%d); continuing anyway
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
{%s} collect result = %s
      Select of JTAG-AP port %u failed with %s\n
tckrate_check returned error %s
{%s} Failed to extract CID from table (%d); continuing anyway
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
Connected to Probe Map Server
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
CPU Address: 0x%llX\n
Complex Address: 0x%llX\n
USER %s(%04u): %s(): %s
   {%s} Probe requires overrun detect mode.\n
Production Fused Device\n
Init dbgwrap obj failed
[PAW] Failed KIS Portal Access Preflight =%s (%d)
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
!!!! Complex Key %s is INVALID !!!!\n
[ARM32cpu_t::_read_register64] 0x%08x\n
{%s} already collected %s, skipping
Flash Size 0x%X KB\n
[%s] Booster System Is Not Initialized\n
Value Types Are Not Strings\n
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
Unable to read PC
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
\t Writing 0x%08llX...\n
{%s::%s} write OK but took %d tries
Unable to read FP
Can't get hardware model - failed to allocate data buffer
Could Not Find Any Boosters of Type: %s\n
Failed to allocate space for table!
[SSTEP] using BP %d\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
[ARM64 INS_WP] 0x%016llx x %d\n
[CLEANUP]\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
{%s@%d} Timeout while attempting connect to server
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s@%d} {%s[select]} %d(%s) [RETRYING]
{%s} Error %d(%s) sending message
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
getOrCreateValue: addMember failed, returning doc root
Match Count is Zero. This is invalid.
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
Unable to read CPSR
collect_responses
{%s} Failed to get breakpoint count for %s: %s
Proceeding with full explore instead of instantiation
{%s} restored el is now %d
{%s::%s} timeout while waiting for EDSCR ITE
   {%s} APB/AXI address for target setup = 0x%llx\n
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
{%s} %s: |%s|
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
SoC BM Not Found, Bailing\n
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
Required key: %s @ index %d is NULL\n
Board ID: 0x%X\n
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
\t Erasing Page %d...\n
Failed to get Bypass Config
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s} failed (%s)
\tCould not read the flash size. Using default 2MB size.\n
STM_FLASH_OBR: 0x%x\n
choice: %d\n
AXconn_t Struct Is NULL
{%s::%s} NULL parameter
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
Breakpoint Size: %d
AP[%d]: MEM_AP_APB\n
[%s] chipinfo is NULL
In Eraseflash\n
## apr %u 0x%08X %d -> 0x%08X ...\n
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
=== Loaded %s Boosters ===\n
Adding new booster path: %s\n
--> 0x%02x = %s
   --> IDR: %08X\n
[INSWP] bp%d addr=%08llx dbreakc=%08X\n
Probe %s Device Not Connected on USB-C Port
{%s} pmgr status=%d being reported as Unknown
product-name: %s\n
Found the RTXCID Structure!\n
read_dbg failed to access R_v7M_CLIDR
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
{%s} FAILURE - max length exceeded
Increasing length by: %d\n
{%s} flags:0x%08x
invalid IR command '%s'
Bundle: %s NOT FOUND\n
Could Not Get Bundle Out Array of Found Boosters\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
error %s checking for data abort(uint32_t)
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
## apw %u 0x%08X 0x%08X\n
chip is 0??\n
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
JsonLogger: Created with default schema version '%s'
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
[ARM32cpu_t::_update_register64] 0x%08x\n
wrote val=0x%016llX -> sysreg=0x%X (%s), regname=%s 
[REMBP] bp%d\n
## memapr %u 0x%016llX %d -> 0x%08X ...\n
sending abort to clear a timeout\n
CPU Die: %d\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER\n
SSO with no prompt being used
{%s}#%02X %s [%s]
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s} set=%u (sh=%u), way=%u (sh=%u)
{%s::%s} ERROR %d(%s) resuming %s\n
caller=%s, async=%d, iterations=%lu
Programming STM32Fxxx...\n
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
{%s} DAP command nwords=%d trimmed to %lu\n
Choose a device: 
Dart Coastguarded CPU: %s\n
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
[READ] %d -> 0x%08x\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
{%s->%s}[cached] %s[0x%X] = 0x%08llX
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
Probe %s with unknown kick response %s
Issuing request to Probe Map Server: %s
Could Not Get BoosterManager\n
Component Group Offset: 0x%X\n
TAP IDCODE: 0x%X\n
 MEM-AP %X is hung\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
{%s::%s} waiting for EDSCR ITE
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
   {%s} (DP): status=0x%X(%s) - %s\n
%2d) %s %s%s\n
In Writeflash\n
Failed to get PMU Name
[%s] cop %d -> 0x%08x\n
{%s::%s@%d [%s]} Error %s: initializing cache parameters
[AstrisAsync] Discarding response due to ASYNCSKIP state!
{%s} timed out waiting for cpu to halt during collect
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
{%s} found single_port probedaemon on port %d
CPU state %d
XBS Version Modified: %s -> %s\n
--> debug      size=%3d acsr=%d
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
ERROR!! Wrote %zd bytes, expected %zd\n
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
Valid Portal
--> wrstn_wir2 size=%3d dpcsoc=%d
Die-Count: %d Current-Die: %d Die-Type: %d\n
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
SoC has been setup using standard instantiation (setup result=%d)
Failed AP read of R_MEMAP_CSW res: %i
Caught a portal that we dont have a status map for: %d
Booster:\n
Initializing (%s) Booster's Astris API\n
CPU Supported in Runtime: %s\n
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
SWDACKDELAY relay write failed\n
%s %3d'b%s\n
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
ERR: conn->nchips != 0; looks like chip is explored\n
Protocol Version: 0x%X\n
{%s->%s}
Failed to sync prefs at end
{%s[recv]} %d(%s) [RETRYING]
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
no debug bus AP present when expected
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
CPU PS-Register: 0x%llX\n
     0x%016llx: ERROR\n
DCCCTRL = %08X   res=%d\n
[AsyncSnapshot] No snapshots collected\n
Error %d (%s) opening cmd snapshost save file
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
We are Deallocating\n
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
caller=%s, async=%d
{%s} %s: |%s|-|%s|
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
{%s} error %s at line %d
[KIS] Register Index: %llu\n
\t\t%s\n
Failed to convert %s key @ index %d to a number with base of %d\n
{%s} %s DC cache clean complete, marking as clean
[1500] TAP %d: irlen must be > 0 (got %d)
Error %d(%s) executing instruction 0x%08X
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
{%s} unable to allocate probe name
{%s@%d} gethostbyname failed, error=%d (%s)
Modified Word To Write: 0x%08x
{%s::%s} [%s] BP_REMOVE m_bp_avail=0x%X, m_bp_rsvd=0x%X, index=%d
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
STM_FLASH_SR: 0x%x\n
Failed to convert primateLoc %s to unsigned long long
Kick has been requested by probe server
[1500] Detected plist version %d
[%s] TGE is set so we traping to EL2\n
{%s} bridge returned SLVERR
Dart Base Address: 0x%llX\n
==== Exception Trace ====\n
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
{%s} Error setting up memap target (%s)
Error while trying to authorize: %d - %s\n
Can't get hardware model - failed to create string
Failed to create CPU %s - %s\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
SoC has been setup using standard instantiation (setup result=%s)
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
Programming (addr: 0x%08llX) Failed!!!
Type 'jebdump' to do scan/mem dump\n
{%s} Component ID read fail on romtable (%s)
dfu-Type: %s\n
Going to do imago workaround\n
\t Writing 0x%08llX failed: %s
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
[%s] m_dc_max_level %d, m_ic_max_level %d\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
   Created Fake Debug Port Debug Port
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
Programming Error is Set\n
Matched via Bundle ID\n
{%s} Failed to extract portal info from table (%d); continuing anyway
Unable to read SP
OK: address translation resumed for %s successfully
Unable to register assert upcall %s (Insufficient memory)
{%s} probeList has probeCount of zero
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
     0x%016llx: 0x%08x    %s\n
{%s::%s} [%s] %s [VA=0x%016llX, bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
{%s::%s} [%s] BP_INSERT _find_bpwp(0) failed
Error %d (%s) opening history save file
Could Not Get BoosterManagerUtility\n
We Are Matching Development Booster\n
{%s} explore with exploreflags 0x%X completed with error [%s]
{%s@%d} socket connection is not available
\t\tARMv6 debug CPU xxx ID\n
{%s->%s} ERROR=%d(%s)
   DPv3 baseptr is not valid (%X)\n
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
in stmflash api\n
Error %d (%s) while expanding ~ for Astris history save\n
Could Not Find Any Boosters\n
    INFO(%u,%d): %s(%04u): %s(): %s:  %s
{%s::%s} [%s] unsupported width %d
{%s::%s} [%s] MMU is already active - returning %s
{%s@%d} Connection to server failed, error=%d (%s)
Could Not Allocate Loaded Booster Array
[%s] CPU BM Not Found, Bailing\n
%#09llx-%#09llx: %s\n
Stepping Stone Addrr = VBAR + OFFSET(%#llx) = %#llx\n
New Length: %d\n
Xtensa Core %s NOT configured\n
Can't get OS build version - failed to get build version
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s=>%s} AXconn_t has no SoC object
Flash unlocked...\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
AuthDebugWithTimer_t::need_to_authenticate_helper UNKNOWN REQ TYPE: %d\n
There is no debug port associated with this chip.
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
could not perform cpu_preflight
   ROM entry %d (level %u): AVOIDED\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
Connecting to server, %s:%d
{%s@%d} Connection to server rejected, error=%d (%s)
Did Not Find Any Boosters For: %s \n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
Probe %s with unknown status %s dropped from available list
comparing against match entry %d: %s
Variables not setup
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
AXmemap_stmflash calling STM32F4xx::eraseflash\n
{%s} invalid data width %d bytes
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s::%s} [%s] MMU not active - returning %s
[AstrisAsync] Complete Queue callback returned %d (%s)\n
      Read of JTAG-AP port %u PSTA failed with %s\n
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
Setting STOP CLOCK to TRUE
Can't find descriptor for group - can't index\n
Chip %x Status = %d\n
## armcpu: success status even though not all bytes read\n
[HALTED] dfsr = 0x%08x\n
\tPrologue Aligned Read Failed
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
Xtensa Option num_bp: %d
Before astris_kis_init_dp, CMDSTAT=%08X\n
CPU DBG Ack: 0x%llx\n
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
## dpr 0x%02X -> 0x%08X\n
Width: %d not supported
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
Could not find portal by select %d, while interpreting result\n
checking if relay \"%s\" is valid
{%s}ERR: bypass_device_name is NULL\n
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s->%s} (top) current_el=%d
Error status from AMAuthInstallSsoInitializePtr = %i
TargetSel Before Disable: 0x%x
Could Not Create Dictionary From Booster: %s
CPU Name: %s\n
Unable to disassemble_at_addr 0x%016llx
{%s=>%s} null reference to CPU_t object, `cpu->state`
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
Using KIS-STM to flash, on some parts we might be too fast for this using KIS-STM
Successfully connected to server, %s:%d
[KIS] CMD: %s \n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
{%s} drop ProbeName %s
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
[INIT]\n
   Debug base is in legacy format\n
Xtensa Option num_wp: %d
Failed to unlock flash\n
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
{%s@%d} timeout waiting for ARMDBGLSR_LOCK to clear (lsr=0x%08X)
     ARM %s debug CPU rev %d\n
astris_get_async_ver failed with error: %s
[%s] AP, DP, or chip given is NULL
## memapw %u 0x%016llX 0x%08X ...(%d)\n
X09 Part
{%s::%s} creating placeholder for CPU: name=%s
--> misc_wdr   size=%3d wirtestporten=%d
Gathered Value is Not Number\n
1: ARM64_SYSOP_ATS12E1R\n
Cached async_replay capability version: %u
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
[PREFS] Key: %s - Val: %s
Probe %s USB-C location is %s
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
!!!! Complex CPU Key %s is INVALID !!!!\n
Invalid value for 'entry' tuple element - can't index
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
Failed to find a product plist for this soc %s
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
DBGSTATUS = %08X   res=%d\n
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
Failed to instantiate %s\n
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
%s construction failed
{%s[select]} %d(%s) [RETRYING]
start rev is not of expected format; skipping cpu_desc override\n
CPU Supported in Integration: %s\n
Unable to read LR
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
AuthDebugWithTimer_t destructor \n
no system bus AP present when expected
KIS Readvals putting back the value
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
{%s} Failed to get watchpoint count for %s: %s
{%s} Failed to single-step %s: %s
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
\t%4X: %8X %8X\n
{%s} hostname:%s, flags:0x%08x
Unsupported device identification 0x%03X\n
\tbut is not guaranteed on this device.\n
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s} calling _collect_hw on %s
Can't get OS build version - failed to create ReadStream
{%s} valid response from bridge
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
    INFO(%u,%d): %s(%04u): %s(): %s
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
%s status is '%s'\n
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
{%s@%d} Failed to send probe command (error %d).
--> psr        size=%3d bit=%d
DBG_CPU: %s\n
Flash Reg Adress 0x%llX\n
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
{%s} bridge returned DECERR
%d KB flash size detected.\n
Values Not The Type We Expected. Expected: Number and String\n
We are at max iterations, still didnt get full JSON
Magic does not match: %#x vs %#x\n
[%s] E2H is set, virtualization is supported\n
[RESUME] Chip %x\n
Booster System Is Not Initialized Bailing\n
{%s} no matching 1500-to-* bridge
Erasing...\n
1: ARM64_SYSOP_ATS12E1W\n
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
{%s} error: %s
Hang Address: 0x%016llx\n
Creating CPU With Name: %s\n
{%s::%s} creating CPU
1500 IR Commands:
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
error %s reading DAP MPIDR
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Aligned Address: %llx
Length is 0
   Debug Port: SELECT %X: SKIPPING (%s)\n
Failed to convert CFString to C String.
[1500] Error parsing v2 bridges
Found probe memory transfer in progress; clearing EDSCR.MA.\n
runBlock
{%s} already connected
{%s@%d} Unable to create socket
{%s::%s} read OK but took %d tries
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
      Read of JTAG-AP port %u CSW failed with %s\n
{%s@%d} neither socket nor kext connection available
Required Key-Value is a string, and not an array. Old booster found: %s\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
codeblock
Breakpoint Address: 0x%llx
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
{%s} no TAP detected that supports 1500
Asked To Read A Negative Register Index
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
{%s::%s} EDSCR with TXU set - unable to recover.\n
probetimeout retrying access...\n
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
Required Key-Value is a string, and not an array. Old booster found\n
Buffer is NULL
{%s@%d} Received %d bytes when requested %d bytes.
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
Gateway is KIS, seeing what probe this is\n
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
%-16s @ 0x%08llX : 0x%08X\n
Using Built In CPUs\n
Flash Reg Adress is not set, using what is there\n
\tWhole chip...\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
[%s] Booster System Is Not Initialized Bailing\n
EICE chip %x initialized\n
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
Async is disabled for current seesion
Error - STM32Fxxx reflash failed (%s).\n
can't find bid in response\n
Connected to Probe Device Server [Log File %s]
DEMCR read failure - %s (%d)
Could Not Find Any Loaded Boosters of Type: %s\n
coalesced-target: %s\n
{%s} _pre_halt_hw result = %s
register lookup by name not supported when Astris is statically linked
Trying to use size of 8 on not AXI bus
Unaligned Read @ 0x%llx Width: %d Bytes: %d
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
KIS Preflight No Need To Write to AP CSW
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
[INS_WP] 0x%016llx x %d\n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
register    %-15s %3u     \"%-s\"\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
%s [RETRYING]
%s probe[%s] from Probe Map Server [local host]
Write Failed: address=0x%08llX, length(in)=%lu, width=%d, length(out)=%d, result=%s\n
AuthDebug_t::need_to_authenticate ACTIVE reg: 0x%X\n
{%s} connectName[%s]
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
Generated JSON (first 500 chars):\n%.500s%s
[SSTEP] bvr=%08x bcr=%08x\n
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
\tReading left over chunk expected 0x%x got 0x%x\n
max_scan_bits is low: %d
\tCould not get sector number for address: 0x%llX\n
{%s[select]} timeout while waiting for data from the connection
Failed To Instantiate SOC From Booster\n
No version information found in booster: %s
VBAR: %#x\n
Failed AP write of R_MEMAP_CSW res: %i newval %i
first read of CMDSTAT may fail if external reset occurred
Connected toProbe Map Server (single_port) 
After powerup CMDSTAT=%08X\n
{astris_probed_print_events} not supported in this build configuration
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
Can't get OS build version - failed to create URL
{%s} drain_packets=%d [%s]
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
\t[MATCH_SKIP] skipping entry
Could not find TAP at index %d to attach 1500 bridge to\n
Full JSON that failed validation:\n%s
Sprocket probe, for now I guess we will just say yes...\n
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
[READ] cop64 %d -> 0x%016llx\n
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
probing %s status\n
KIS Chip Found, Doing KIS Explore Setup
STM32Fxxx flash programming status fault: 0x%08X\n
\tCould not get sector size for address: 0x%llX\n
Mass Erase...\n
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
Both debug and xbs versions are set, maybe a bug: %s
%s
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Wrong width, should be either 4 or 8\n
   Debug Port: Trying SELECT %X\n
Had an error during transfer: %s
Could Not Allocate Booster Location Array
{%s} skipping dcache flush, cache already clean
[AstrisAsync] Resume when not paused!\n
{%s=>%s} AXconn_t has more than one chip
Error status from AMAuthInstallSsoSetStealthModePtr = %i
AXmemap_stmflash calling STM32F4xx::reflash(0x40023C00)\n
Can't get OS build version - failed to create plist
[PAR] Failed KIS Portal Access Preflight =%s (%d)
Could Not Allocate All Boosters Array
Dart Dart Type: %s\n
bypass-config-name: %s\n
{astris_probed_print_events_from_json} not supported in this build configuration
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
{%s} L2 cache operation completed [%s]
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
unable to obtain sysap
{%s::%s} %s resumed\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
[AstrisAsync] Activating async...\n
   Debug Port: SELECT %X: DISABLED\n
Programming STM32%s...\n
Flash Sector Max %d\n
Exc Cause: 0x%x - Exc Vaddr: 0x%x
[1500] TAP key is not a valid integer
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
dbgwrap halt failed, falling back to classic method
{%s} Failed to get watchpoint mask for %s: %s
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
En masse...\n
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
Probe %s Device Server listening on port %d
## ARM32cpu_t::read_register 64 bit 0x%x\n
## dpw 0x%02X 0x%08X\n
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
AuthDebug::authenticate_probe - no need to authenticate\n
  Error path [%s]\n
process (%s) (%d) path: %s
Connected to Probe Device Server [Default Log]
sent %zd bytes to Probe Map Server when sending %zu
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
Hardware model: %s
{%s} unable to find single_port probedaemon on port %d
Kick off the current process using probe %s? (y|n)\n
Probe Map comm error %d(%s) %s [%s]
KIS Writevals putting back the value
{%s::%s} [%s] error %s writing SCTLR_ELx
[AstrisAsync] Resuming Async Mode\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
Failed to init from cpu desc armv7m cpu: %s \n
Using Built In SoCs\n
{%s::%s@%d [%s]} Error %s: collecting HW
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Invalid current AP (%d), adopting APTABLE (%d)
{%s} %s DC cache already clean since last halt, skipping flush
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
{%s} Error reading CPUID (%s)
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
relay_set: %s = CMD_ERR (%s)
** Unauthorized User/Network or ECID **\n
STM_FLASH_WRPR: 0x%x\n
Previously dumped the process tree, skipping
Created Connection - : %s
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
SoC must have a DAP
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
SOC_t::{%s} CPU_t group=%d when group 0 expected
   DPv3 BASEPTR0 is 0x%08X\n
\tWriting @ 0x%08llX...\n
Programming STM32Lxxx...\n
Xtensa Option non_tie_ranges: %zu range(s)
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
comparing against match entry [pid] %d: %s\n
No 1500 bridges or TAPs specified (v2 plist)\n
Not Creating CPU: %s\n
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Probe %s status: Busy
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Cannot create SoC [unknown chip identity (%d)]
Booster Info:\n%s
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
Result while reading third entry: %s , entry val 2: 0x%X\n
Failed to convert CFArray to C Array\n
AXconn or json_out are NULL
Enabling USB Gateway
Complex CPU ID: %d\n
[MEM] Aborted; DSCR = %08x\n
{%s} _pre_resume_hw result = %s
{%s} Failed to resume %s: %s
{%s} Error looking up architecture (%s)
The log file has been updated with all available diagnostics.\n
unable to create connection
Pages %d\n
{%s::%s} ITE is not set: 0x%X\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
## armcpu: success status even though not all bytes written\n
{%s=>%s} null reference to AXcpu_t record, `cpu`
{%s} ROMTABLE (nest=%d)\n
{%s} %d(%s) [RETRYING]
CPU (%s) has explore flag of: 0x%llx which is not set\n
{%s} read ESR EL1|EL2|EL3 (%d)
OK: address translation suspended for %s successfully
AuthDebug_t::need_to_authenticate_probe - unsupported, so no need\n
Failed to read register to figure out flash address %s\n
%s probe[%s] from Probe Map Server [%s]
{%s} select success without file descriptor set
Problematic JSON value:\n%s
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
Astris Source Version: %s\n
Invalid SoC Booster. SoC Booster Requires PID\n
Debug Base: 0x%llX\n
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
[AsyncSnapshot] #%zu: %s\n
** \tTatsu AuthDebug Triage | All     **\n
{%s} 0 words from probe when %d words left to read for reg %d
[1500] v2 plist missing required field 'bridges'
x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
Async is disabled for localhost connection
{%s} Error reading PID (%s)
Unable to allocate memory for next part of big response
Sending DYN Bypas Channel Set: %d
There is no system bus access port on the debug port
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
%s: not supported.\n
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
Couldnt figure out the size of flash, defaulting to 1MB\n
Complex CPM Offset: 0x%llX\n
{%s::%s} cpu powered off: failed init() %s
Invalid character [0x%02X] received from Probe Map Server
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
%s: chip was NULL when attempting to release soc
JsonLogger: Writing category '%.*s' to '%s'
{%s} FIFO full, try again
[KIS] Words (Read/Write/Wrote): %d\n
We are in clean up\n
Logging Context Is NULL\n
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
[%s] {%s->%s} clear async abort
[%s]\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Failed to read flash size at 0x%08llX : read failed\n
=== Found %s Boosters ===\n
{%s->%s} m_exception_level=%u
CPU Monitor[%i]: %s\n
{%s} %sing word #%d at address 0x%09llx: %s
Portal Group Offset: 0x%X Entries: %d\n
Initial DSPSR_EL0: 0x%llx
AP is NULL
{%s@%d} Failed to read ROM table entry @ 0x%llx => 0x%08x; this really shouldn't happen since we must have already read behind this mem-ap to get here.
Can't get hardware model - failed to allocate data string
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
CPU Subsystem: %s\n
[1500] v2 plist missing required field 'taps'
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
[AstrisAsync] Completing all async commands. Initial err = %d\n
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
Failed explore before forced KIS reset: %s\n
Stop Clock: %s\n
About to call fault reg latch, min_operating_el: %d\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
[PREFS] Key: %s - Val: NULL
Portal Group Base: 0x%llX \n
failed write of 0x%08X to DEMCR - %s
\t0x%08llX...\n
SoC does NOT support IDE Explore\n
{%s} bridge timed out
{%s} unaligned %d-byte access at address 0x%09llx
Unable to convert plist file name to CFString: %s\n
[1500] %s step %d: unknown instruction '%s'
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
Failed to create optional file. Not fatal, moving on
Could Not Allocate Mutable Dictionary For BoosterMangers
error %s checking for data abort
{%s::%s} ERROR %d(%s) pre_resuming %s\n
{%s::%s@%d [%s]} Error %s: resuming HW
{%s->%s} START handling exception
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
probe event: %s
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
Die Config Disabled
Map is empty, not removing CPU %s
{%s::%s} halting %s\n
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
[%s] %d -> %08x\n
{%s::%s} [%s] error (%s) getting number of HW WPs
Could Not Find Booster Entry Function: %s\n
Booster Bundle: %s\n
Booster Value is Not String\n
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
{%s::%s} HDE not set on %s. Will re-enable.
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
{%s} %s status failed. error: %d (%s)
   {%s} Read AP's R_MEMAP_CSW\n
AXjtag_explore failure - %s (%d)
Matched Booster: %s\n
Gateway Version: 0x%X\n
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
[COLLECT] Chip %x\n
[REM_WP] wp%d\n
Flash Address Max 0x%llX\n
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
CPU %s already in the map with status: %d
Fabric access is blocked. Expected if production unit, won't explore further.
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
AP[%d]: unknown type\n
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
dropping empty probeInfo (port=%u)
Awaiting response from Probe Map Server
{%s} probe device server closed the connection while trying to read data (at recv)
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
%s NOT configured\n
      AXap_write of R_JTAGAP_PSTA failed with error %s
CPU Monitor key does not exists for: %s\n
Optional Key: SubsystemMonitor not in preferences
Flash unlocked...(before erase)\n
Turning Debug Clock On
Cannot create CPU descriptions from NULL info\n
[AstrisAsync] Got ASYNC_RESTART response!
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
{%s} match any probe [localhost]
{%s} unmodified-probe_match = %s
Disconnected from Probe Map Server
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
\t%s\n
{%s::%s@%d [%s]} Error %s: synchronizing context
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
{%s} error %d(%s) reading data from the connection (at recv)
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
[ANAMOLY] Could not find AXcpu_t object for CPU\n
Failed to find a plist for this soc %s
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
     ARM %s breakpoints: %u\n
     ARM %s watchpoints: %u\n
Switch back to primate KIS: %s\n
{%s@%d} Probe response payload read when no payload indicated.
{%s@%d} Unknown CS command error [%d]
Could not find TAP at chip-index %d for v2 1500 config\n
End of Operation Bit Is Set - %s
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
Warning: spun for a long time (> %ld seconds)\n
STM32Hxxx flash programming status fault: 0x%08X\n
Taking gateway control failed
couldn't find CPU1. this is expected sometimes.
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
Xtensa Option options: 0x%x
Passed NULL booster without custom plist\n
--> cmd        addrsize=%d datasize=%d
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
[AstrisAsync] replayConditionalCheck: condition hit!\n
Couldnt figure out the size of flash (we read: %d), using default\n
Multi target booster, checking for %s.plist\n
** CPU %s requires forced explore override flag on this SoC **\n
CPU has no regions, maybe powered off?\n
{%s} no chip found
[PREFS] Key: %s - Val: ??
Probe (port=%d) with unknown status %s dropped from available list
Banana split probe, for now I guess we will just say yes...\n
{%s} Failed to extract PID from table (%d); continuing anyway
{%s::%s} [%s] error %s from _synchronize_context.
Translate Stage Chosen: %d\n
Original Content: 0x%08x
replay_counter=%lu
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
AXportal_t Is Not Valid Type - %d
CPU Explore: 0x%llX\n
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
[Auth Debug] Ticket Not Active, Debug Interface Locked\n
\nSaved %s binary data to %s\nWrote %lu bytes\n
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
\t Bank %u Sector %u...\n
Size or Count provided are 0.
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
{%s} handle ROM entry %d (level %u): %08x
{%s} read %d words from probe when %d words requested
Spew change. old=0x%016llX, new=0x%016X
Probe Map name of probe %d is: %s
JsonLogger: Loading schema for category '%.*s' from '%s'
JsonLogger: Schema loaded successfully for category '%.*s'
{%s:%s}: cpu powered off: unable to access a register for this CPU
Error %d(%s) executing instruction 0x%08X FAST
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Successfully Authenticated Probe\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
{%s@%d} Unknown CS code [%u]
Could Not Match A Booster for %s\n
   {%s} Before powerup CMDSTAT=%08X\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
Probe %s with unknown port response %s
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
Could not find bundle () in given array: %s\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
replayPreflight
Hang Description:\n%s\n
!*!*!* Lightning header facing up.                                                    !*!*!*
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
[%s] %d -> 0x%08x\n
Invalid APTABLE (%d), so using most restrictive
   CPUID: 0x%08X\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
{%s} checking for single_port probe daemon on port %d
end rev is not of expected format; skipping cpu_desc override\n
Fast Programming Error is Set\n
--> localwrstn size=%3d debug=%d
Raising to EL2 cause in Guest\n
[AstrisAsync] astris_async_override_disable_async: conn is NULL
relay_set: %s -> %d
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
error %s reading DAP PFR1
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
[INSWP] 0x%08llx wp%d rdwr=%X\n
   JEDEC ID: 0x%08X\n
Can't get hardware model - failed to find matching IOService
Error - STM32Hxxx reflash failed (%s).\n
  Nested path: parent='%s', child='%s'
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
%s Bridge @ 0x%09llx-0x%09llx: %s
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
Breakpoint Index: %d
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
No 1500 bridges specified\n
[DCC] Grabbing DTR failed: %s\n\n
Result while reading second entry: %s , entry val 1: 0x%X\n
[READ] cop %d -> 0x%08x\n
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
[1500] Error parsing bridge: %s
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s::%s} [%s] error (%s) getting number of HW BPs
   {%s} Enabling debug unit\n
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
In Readflash\n
UPDATE cop64 %d -> 0x%016llx\n
Stepping Stone Final =  %#x\n
[AstrisAsync] Async mode %s
=== Starting Gather and Clear ===
%-16s @ 0x%08llX : read failed\n
Section 1 Offset: 0x%llX\n
Unable to read GPR 28
AP Only Explore was asked for, stopping here
{%s} probe_host = %s
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
{%s} m_exception_level(%d) != current_el(%d)
successfully updated DEMCR
{%s} Class 9 ROMTABLE (nest=%d)\n
\t Sector %u failed: %s\n
Connect using RSD not supported\n
write to CMD/STAT failed - %s
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s=>%s} no soc reference; falling back to direct cpu method
{%s} Exploring with option: %s\n
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
After Programming (addr: 0x%08llX) Programming Error is Set: 0x%08X
Got an error reading the DCM Control Register: %s
Failed to convert %s key @ index %d
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Setting bypass channel to: %d\n
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
Failed to explore chip: %d
Probe Map Server Information: %s
Write Protection Error is Set\n
Could Not Find a DCM Portal
Dart Name: %s\n
Invalid Bundle: %s
   Setting up AP IDR %08X\n
Probe Map comm error %d(%s) %s
{%s::%s} creating AP slave: name=%s
using standard products.plist for %s
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
{%s} Failed to get breakpoint mask for %s: %s
ERROR: unable to resume translation for %s
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Failed to convert kisHubLoc %s to unsigned long long
Failed To Initialize Logging\n
\t%s (%s)\n
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
{%s} unsupported bridge type for %s
haskis bit not set\n
CPU %s not found or already removed from the map
Unable to read GPR %d
Exploring IDE in JTAG\n
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
CPU AP-Select: %d\n
CPU Typehint: %s\n
STM_FLASH_ACR: 0x%x\n
AXmemap_stmflash calling STM32H7xx::eraseflash\n
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
{%s::%s} [%s] error %s reading SCTLR_ELx
Invalid current AP (%d), adopting latest (%d)
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
Failed to read IDE through DAP\n
{%s} Unrecognized component: %08X, class %02X\n
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
iter=%lu
\tLeft Over Chunk Read Failed\n
## apw %u 0x%08X 0x%08X ...(%d)\n
Optional Key: CPUMonitor not in preferences
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
No Success after retry on wait
%02X 
[1500] No %s.plist resource found
ACQ_STARTSTOP
Failed to convert CFArray to C Array\n
{%s:%s@%d} [%s] FLASH_CR PG read failed: %s\n
ret.read.vbar
write.dspsr_el0 NOT DIRTY
Failed to write reg_addr=0x%llx val=0x%llx
-
successfully updated DEMCR
fn._ocd_exec_instr.TIEInitiateReadProtectedI
_read_register32
ret._setup_wp
RF51
xfer_length=%u
ASTRIS_ERR_ASYNCSKIP
REG
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
_write_general_reg
DCS15
result.ide==NULL
ret.read.edscr.ma-mode
{%s:%s@%d} [%s] Could not read MCU_IDCODE\n\n
????
{%s} hostname:%s, flags:0x%08x
connect-probemap
revive
[1500] Error parsing IR command: %s
High level 4 exception PC
EXCSAVE1
Clear requests in INTERRUPT
_tie_read_word32
astris_get_dbgwrap_sys_addr
Logger output is null
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
Table 5–151
kisHubLoc
cpu-xtensa-reg-size
address-size
{%s::%s} [%s] unsupported width %d
ret.raise_el.read
astris_cpu.cpp
astris_cpu_lower_el
## apw %u 0x%08X 0x%08X\n
Connected
EL1t
astris_user_default_copy_boardname_for_primate
ret.auth.data == NULL
High level 2 exception PC
Probe %s removed before port determined\n
_init_hw
ASYNC
probetimeout retrying access...\n
AuthDebugWithTimer_t destructor \n
GetType() == kNumberType
{%s:%s@%d} [%s] reading DFAR\n
{%s} [!is_64] exec: encode_msr(MDDTRTX_EL0, 0, %d\n
_a64cpu_reset_catch
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
{%s} FAILURE - malloc error
X06 Part
Section 5.1
BADCODE
{%s} no matching 1500-to-* bridge
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
copyNicknameForKey
astris_memap_lmflash
{%s:%s@%d} [%s] \tFailure: region @ 0x%08llX failed to verify\n\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
AXportal_t Is Not Valid Type - %d
SSO with no prompt being used
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
AXbreadcrumbs_clear
astris_booster_cleanup
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
ret._a64cpu_write_sysreg_hw
{%s:%s@%d} [%s] FLASH_PECR write failed: %s\n
\"%s\" not an implemented register
op_S16I_encode
Can't get OS build version - failed to create plist
ASTRIS_ERR_ANOMALY
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
{%s:%s@%d} [%s] reading PAR[64]\n
[SSTEP] bvr=%08x bcr=%08x\n
ret._a64cpu_lower_el_hw_safe
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
AXdebug_auth_get_timer_count
cpu_mmu_get_tsz
ParseRange
Required Key-Value is a string, and not an array. Old booster found: %s\n
CPU Core Number: %i\n
Probe %s selected
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
AXcpu_suspend_translation
TatsuServer Found: %s\n
FLASH_WRPR2BR
RF35
type_hint not NULL, but creating a placeholder, this is off
   DPv3 BASEPTR0 is 0x%08X\n
pointer.IsValid()
astris_explore_enabler_get_subsystem_status
Exception occured after executing MRS to bounce through scratch register
Primate-Hub-Null
{%s@%d} Unknown CS code [%u]
cpu_lacc_count_read
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
Flash Reg Adress 0x%llX\n
[AstrisAsync] replay preflight: Async not active!\n
sso_user.conn == NULL
fn._ocd_exec_instr.l16ui.r1.r0
Begin
cpu
APCIE
ret.enableCpu
FLASH_WRPR2AR
Using KIS-STM to flash, on some parts we might be too fast for this using KIS-STM
_read_special_reg
fn._write_special_reg.ibreakenable
Can't find descriptor for group - can't index\n
~HDE
WFI
## dpr 0x%02X failed (%s)\n
AuthDebug::authenticate_probe - no need to authenticate\n
STM32F10x_LowDensity_FLASH
param.reg.invalid.outofrange
PROBED_SLEEPING
ret.cfg_write(R_DCM_GPIO).deassert
!!!! Critical Error: {%s->%s} EL3 not implemented !!!!\n
Gateway is KIS, seeing what probe this is\n
fn.remove_epcn_epsn
Issuing request to Probe Map Server: %s
Programming Error is Set\n
dart-type
~MA
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
R7
DBG_WRAP_REGS
Board ID: 0x%X\n
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
ret.alloc.soc_key == NULL
astris_get_hang_crumb
cpu-address
param.descr==NULL
DP
{%s} Unrecognized Component: %08X (class %u)
RF14
SWDONLY
{%s} checking for single_port probe daemon on port %d
DCS_BC1
{%s} _halt_hw result = %s
EPC3
write to CMD/STAT failed - %s
{%s:%s@%d} [%s] writing CSSELR\n
astris_setup_ap_mem
Warning: spun for a long time (> %ld seconds)\n
Probe %s with unknown port response %s
{%s@%d} Received %d bytes when requested %d bytes [%s].
select_v2
Before astris_kis_init_dp, CMDSTAT=%08X\n
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
fn._ocd_exec_instr.rsr.ddr.t1.2
KIS
CPU Subsystem: %s\n
process_bypass_device
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
Clear (1<<1)
DEDICATED
Proceeding with full explore instead of instantiation
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
exit.exception_test_2
handle_pending_async_aborts
RF32
bool
info-probemap
cpu_halt
FLASH_CR
m_bp_details
{%s:%s@%d} [%s] Buffer data to RAM failed: %s\n
in stmflash api\n
Page table virtual address
ocd_base_address = 0x%8.8X is not 4 KByte aligned
fn.stmflash.h7.wait_bank_flash_idle.read.sr_reg
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
explore-level
{%s:%s@%d} [%s] reading WCR %d\n
0
AXarm7_dbgread
RF37
Writing FLASH_CR2 failed during lock sequence\n
dbgwrap
GorillaSWD
{%s:%s@%d} [%s] FLASH_PEKEYR write (second) failed: %s\n
DSR
cleanup
dbgfifo
Pop
~
(system_reg & (0x40000000 | 0x80000000)) != 0
Booster System Is Not Initialized Bailing\n
AXcpu_readreg
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
{%s} Reading base 0x%llx entry's component ID
%s (%d)
dropping empty probeInfo (port=%u)
There is no debug port associated with this chip.
_a64cpu_encode_mrs
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
hwbp_remove
      Select of JTAG-AP port %u failed with %s\n
ret.reg.read.K_DA_REG_NAME_SECURE_DOMAIN
Error occured during nonce command (v.5)
internal.is_authenticated.chip->soc == NULL
invalid IR command '%s'
GPR[cached]
index slot not enabled
Width: %d not supported
Xtensa Option dbg_intr_level: %d
address=0x%8.8X, len=%u, rdwr=%d
{%s@%d} Unable to create socket
incr_drain_packets
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
{%s:%s@%d} [%s] executing VMOVR\n
CTI_CH_PULSE
{%s::%s@%d [%s]} Error %s: synchronizing context
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
 MEM-AP %X is hung\n
Ticket Data is NULL\n
address=0x%8.8X,page_id=%u
[RESUME] Chip %x\n
AXspmi_read_bus
U5xx
Table 5–132
_tie_write_word32
stack_.GetSize() == sizeof(ValueType)
--> wrstn_wir2 size=%3d dpcsoc=%d
targetid
{%s:%s@%d} [%s] writing CSSELR[L1-D]\n
AXdebug_auth_supported
recoverable
Size or Count provided are 0.
couldn't read TTBR1
param._tgt.invalid.null
PORTAL(ID: 0x%X): KIS-RESPONSE(0x%X)=%s - PORTAL-STATUS(0x%X)=%s - %s\n
regex_.IsValid()
Failed to read CR reg\n
Error %d (%s) opening history save file
uri.h
IMX
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
AMCP3
{%s} exec: IC_IALLU_ENC\n
EPS3
Table 5–149
Error %d (%s) while expanding ~ for Astris log file base\n
cpu_get_cl4_debug_signpost
json
AX1500_listbridges
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
ret.ito.clear_edscr_err
{%s} already collected %s, skipping
Table 5–152
Writing FLASH_CR1 failed during lock sequence\n
STM32G071xx
tc1500
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
RF55
HIFI3_2
not connected
[%s] Booster System Is Not Initialized\n
get_current_mmu_regs
%s construction failed
connected
CPU state %d (stm_preflash)
Found the RTXCID Structure!\n
!!!! Critical Error: GRPS[0] cached !!!!\n
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
{%s} Unable to read SP_EL0
{%s} restored el is now %d
## memapw %u 0x%016llX 0x%08X ...(%d)\n
result.read_vals(group_info)==
{%s->%s} (top) current_el=%d
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
Unable to read FP
{%s} %s DC cache already clean since last halt, skipping flush
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
Level-1 exception PC
fn._remove_data_breakpoint.which_wp
[1500] Error parsing bridge: %s
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
Failed to read transfer register (EDDTRTX)
Halt
symbol.check.loaded.AMAuthInstallSsoInitializePtr == NULL
Table 5–179
RF31
_write_general_reg_by_name
PROBED_USB_INUSE
astris_remove_loaded_soc_boosters
param.cpu==NULL
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
   {%s} Enabling debug unit\n
{%s} no chip found
Register file 57
var.bp.invalid
Probe Map Server Information: %s
{%s} bridge returned SLVERR
AuthDbg,TicketIdentifier
PKA Command Verify Completed, No Errors, but Enable Valid Not Set
AMAuthInstallCreate
Couldnt figure out the size of flash, defaulting to 2MB\n
backtrace
latching: EL%d
{%s} Unable to read CPSR
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
PROBED_USB_REQ_TIMEOUT
~A
Subsystem Monitor Key does not exists: %s\n
failed to create log dump file
SETCLR
JAM
AXexplore_enable_cpu
Verification Mismatch starting at offset %d\n
fn.stmflash.h7.lock_flash.read.cr2
setTargetIdentifiers
{%s:%s@%d} [%s] reading CPSR(1)\n
PROBED_USB_RSP_TIMEOUT
host_get_port
1970-01-01T00:00:00Z
setTargetOS
CPU
wir2-tdo
ret.reg.write.K_DA_REG_NAME_NONCE_0
MR1
u64toa
[1500] Using %s.plist
ENABLED
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
AXdebug_auth_authenticate
AXmemap_stmflash
op_RFDO_encode
Too many open files
{%s:%s@%d} [%s] Mismatch at offset %zu: expected 0x%02X vs actual 0x%02X\n\n
ATS1Eop
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
CPU Supported in Integration: %s\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
Dumping Process Tree
CPU3
CPU AP-Select: %d\n
astris_preferences_subsystem_monitor_list
HF3
complex-cpu-name
We are at max iterations, still didnt get full JSON
{%s->%s} exec: aarch64_add_imm(scratch=%d, REG_SP)\n
!!!! Critical Error: el[%d] == m_exception_level[%d] !!!!\n
Result while reading first entry: %s , entry val 0: 0x%X\n
probetimeout retry failed logging as hang\n
Status/State
Error level
Failed to write register: 0x%llx val: 0x%llx
AXconn_connect
{%s:%s@%d} [%s] executing MCRR\n
BCR0_EL1+index
EL3t
{%s} handle ROM entry
[REM_WP] wp%d\n
RF59
v8@?0
va
ret._mmu_init
Wake
param.reg_index.invalid
fn._write_mem.bp_info
PAR_EL1
ret.ito.read.edscr
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
current_el[%d] != target_el[%d]
astris_handle_romentry
value=0x%8.8X
DISPEXT
Unable to read PC
{%s} Error looking up architecture (%s)
   {%s} Before powerup CMDSTAT=%08X\n
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
cpu_hwbp_remove
RTP
fn._write_mem
wait_for_bank_flash_idle
un-sel-sib-network
ARMv7mcpu_t
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
{%s@%d} Connection to server rejected, error=%d (%s)
Misc_CortexM
virtual int ARMv7mcpu_t::_resume_hw(bool)
hwbp_insert
[%s] AP, DP, or chip given is NULL
Can't get hardware model - failed to create string
ASTRIS_ERR_BADPARAM
astris_explore_enable_subsystem
{%s:%s@%d} [%s] reading OSLSR\n
_a64cpu_restore_el_and_spsr
quit
astris_command_async
[AstrisAsync] REPLAY DIVERGENCE: Outstanding commands on async deactivate!\n
STM_FLASH_OPTKEYR: 0x%x\n
probe refused to process the command
pnav_filter_out_kis_stm
{%s::%s} halting %s\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
{%s} explore with exploreflags 0x%X complete [%d chip%s]
{%s:%s@%d} [%s] busy timeout after open: %s\n
High level 7 exception PC
General register 7
RF62
Unable to connect after multiple attempts:\n%s,\n%s
ret.ite.read.edscr
Probe Map comm: request[%s], response[%s]
{%s::%s} creating CPU
 
Failed to setup bp=%d
AXdebug_auth_clear_dft_auth
_insert_data_breakpoint
connecting to selected probe (user-specified single_port)
IDE
AuthDbg,ProductionMode
Invalid num_regs = %u. Windowed register option required.
;
Probe %s LocationID Info is %s
param.sys_addr == nullptr
Error reading thingy
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
Beginning of set
FLASH_SR2
ret.lower.after.read.aarch64hw
{%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
RF21
param.bp_info.invalid.null
RF49
val =0x%X is too large for 32 bit unsigned.
AXLOG
invalid command
Error while %s:\n  Unable to connect to %s - %s
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
extract
DBGWRAP_LITE
SWD
General register 2
op_RSR_encode
is.Peek() == 'n'
%s:%s
bypass-configs
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
{%s:%s@%d} [%s] reading LOCKSTATUS\n
spsr_select
EL2t
MEMAP
ret.reg.write.K_DA_REG_NAME_AUTH_KEEP_DECISION
nullptr == soc_bm
val < 4294967295U
_get_type_hw
which_bp=%d
Apple Fabric Timeout
classic
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
diyfp.h
ret.faul_reg_latch
(instr & ARM64_MSR_MRS_BASE_MASK) == 0
astris_user_default_copy_nickname_for_primate
OCD debug status register
RF0
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
New
Atomic Oper, Control
RF44
fn._ocd_exec_instr.s32i.r1.r0
ARM11
Invalid current AP (%d), adopting APTABLE (%d)
{%s:%s@%d} [%s] timeout waiting for R1RDY\n
fn._ocd_exec_instr.wsr.ddr.t1
ParrotSWD
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_stmflash_g071xx.cpp
_a64cpu_assert_state_valid_entry_exit
config_write_protection
{%s:%s@%d} [%s] FLASH_KEYR write (first) failed: %s\n
Table 5–147
status
firmware version is too old DEPRECATED
 (eng)
{%s:%s@%d} [%s] writing WVR %d\n
low word
{%s->%s} current EL (%d) already >= target EL (%d).\n
EXPLORE_JTAG_NO_BOUNDARY_SCAN
_insert_instr_breakpoint
HIDBridgeSWD
We Are Matching Development Booster\n
DBGWRAP_FULL
Failed to raise EL to %d to read register: 0x%llx
RF18
2.34.0
cpu_getinfo
EXPLORE_WITH_AVE
read_resp_payload_via_sock
DPAP
ret.astris_set_user_die_select.astris_soc_get_applesoc
PMS
** Add the --with-force option or use the explore_override console command **\n\n
{%s:%s@%d} [%s] going to RTI\n
xfer=%u, xfer_length=%u, address=0x%8.8X
param.sr.invalid.>255
%s: %s\n
astris_json_logger_to_json_string
{%s} [EDSCR_RXFULL is_64] exec: encode_mrs(0, MDDTR_EL0, true)\n
file/object not found
{%s} no TAP detected that supports 1500
cpu-dbgwrap-status
[1500] Error parsing v2 bridges
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} MEMAP accesses inhibited during explore (exploreflags=0x%X)
halted=%d
ret.AXmemap_read.board_id
SETRELAY
MCORE
astris_explore_enabler_del_cpu
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
{%s} Exploring with option: %s\n
need_to_authenticate_helper
duration_ms
mempool-base
[1500] TAP %d missing required field 'chip-index' or 'irlen'
{%s:%s@%d} [%s] writing DTRRX(uint32_t)\n
{%s:%s@%d} [%s] doing JTAG scan (DTRTX)\n
[AsyncSnapshot] No snapshots collected\n
OCD control register, set
fn._ocd_exec_instr.wsr.ddr.t1.1
sdom
First Couldnt
internal.authenticate_dft.chip == NULL
Can't get OS build version - failed to create ReadStream
GetHashCode
General register 4
MemberEnd
.user
base-addr: 0x%016llX present: %d comp-id: 0x%X - loc-id: 0x%X - feature-id: 0x%X - subsys-id: 0x%X - midr: 0x%X - type: 0x%X
A64
read_memory_dbgwrap
_init_configuration_by_name
fn._ocd_reg_w.regval
target power is OFF
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
fn.exit
[REMBP] bp%d\n
param.no_dp
      AXap_read of R_JTAGAP_PSTA failed with error %s
fn._read_special_reg.srn.regval
fn.AXmemap_write.address.regval.
ASTRIS_ERR_NOTOPEN
APPLE_SUBTYPE_UNKNOWN
cpu-group
psr-size
astris_explore_enabler_add_cpu
{%s:%s@%d} [%s] \tFailure: only %u of %u write transfers were done\n\n
STM_FLASH_CR: 0x%x\n
STM_FLASH_OBR: 0x%x\n
INVALID 
dfu-Type: %s\n
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s:%s@%d} [%s] timeout waiting for flash idle\n
address=0x%8.8X
param.reg_name.invalid.null
param.info.invalid.null
Problematic JSON value:\n%s
CPU Explore: 0x%llX\n
{%s:%s@%d} [%s] moving reg to cop\n
   Debug Port: SELECT %X; error: %s, retrying..\n
Register file 51
s.Peek() == '\\\"'
haskis bit not set\n
xtensa-non-tie-range-size
ret.getSubsystemEnableStatus
Update
   {%s} Probe requires overrun detect mode.\n
CPUMonitor
{%s:%s@%d} [%s] FLASH_CR MER write failed: %s\n
Instruction count level
   Debug Port has unknown type\n
SSO is DISABLED\n
EPC4
Register file 36
Table 5–169
param.op.invalid.outofrange
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
Unable to allocate memory for next part of big response
result.read_vals(component)==
{%s:%s@%d} [%s] busy timeout on lock (in): %s\n
PORTAL_STS_OK
anomaly detected
{%s@%d} Unknown CS command error [%d]
CHIPCNT
Could Not Get BoosterManagerUtility\n
Booster Bundle: %s\n
write_reponse_and_check_authentication
cpu instr. 0x%8.8X not halted after 3 checks. OCD.DSR = 0x%8.8X
fn.stmflash.h7.reflash.program
Probe removed prior to kick: probe %s
{%s} %s: |%s|
ir <-
Main
Probe Map name of probe %d is: %s
no system bus AP present when expected
{%s:%s@%d} {%s->%s} EL3 not implemented\n
{%s:%s@%d} [%s] CR write (clean) failed: %s\n
High level 6 exception PS
op_TIECompleteRead_encode
Table 5–134
{%s} select success without file descriptor set
CortexA53
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
transact
Failed to get PMU Name
unswitch_regset
## armcpu: success status even though not all bytes written\n
HardwareWatch
fn._read_special_reg.dbreakc0
UNKNOWN_CODE
\t[MATCH_MEMAP] %s <= ((0x%08X & 0x%X) == 0x%08X)
Debug Clock Already Enabled
chip-index
entry.exception_test_2
[%s] Executing instruction=%llx
[REMWP] wp%d\n
ExcCatch
JTAG
Error while trying to authorize: %d - %s\n
{%s:%s@%d} ARM64-specific _sstep method not currently supported\n
aarch64
Production Fused Device\n
\tWriting 0x%X bytes @ 0x%08llX...\n
Table 5–168
RF28
_init_registers
fn.stmflash.h7.program.writevals
L3
FWUPDATE
cpu_hwbp_insert
.name
set.start_time
cpu-armv7m-dmem-size
_is_halted
Cause of last exception
TOOMANY
%Y-%m-%dT%H:%M:%SZ
AXbooster_print_loaded_boosters
CPU AP-Type: %d\n
[ARM32cpu_t::_read_register64] 0x%08x\n
!!!! Critical Error: current_el[%d] == 1|2|3 !!!!\n
_a64cpu_read_edscr
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
required parameter is missing
!Base::hasRoot_
unable to obtain sysap
BT_PHY
{%s:%s@%d} [%s] writing WCR %d\n
virtual int ARMv7mcpu_t::_halt_hw()
{%s:%s@%d} [%s] SR write failed: %s\n
KobaSWD
AXchip_get_chip_id
typehint
fn.stmflash.h7.sector_erase.write.cr_reg.to_start
APCIE_REGS
astris_user_default_remove_all_nicknames
{%s:%s@%d} [%s] PWR_VOSR write failed: %s\n
Invalid reg_index %u
ASTRIS_ERR_TGTSTATE
Misc_Rtx117x_t
JsonLogger: Schema loaded successfully for category '%.*s'
_a64cpu_assert_rw_matches_hw
UNKNOWN_PORTAL_ERROR
fn.stmflash.h7.lock_flash.write.cr2
fn.stmflash.h7.mass_erase.flash_idle
end
cpu_cleaninv_dcache
high word
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
In %s, DEVICE ID: 0x%X\n
fn.stmflash.h7.reflash.read_verify
Sprocket probe, for now I guess we will just say yes...\n
fn.param.name.null
_init_configuration
as=%u,opcode=0x%6.6X
Warning: Default logging location requested when running as root (using [%s])\n
axi-regs
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
_reg_desc_lookup_by_name
%s/%s
fn.stmflash.h7.lock_flash.write.cr1
%d:%d%s
KanziSWD
XSTAT
ret.get_soc_resource_filepath
AUSB_REGS
Invalid file name: \"%s\". File names must not start with '.'
ret.dlr_el0
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
{%s} strsep empty so match any probe [localhost]
{%s}#%02X cmd: %s, resp: %s
{%s:%s@%d} [%s] doing IR scan (DIDR SCAN_N)\n
_a64cpu_encode_msr
read_dcc
Can't get OS build version - failed to get build version
target no longer responding
Skipped due to error in Async batch
pc:  0x%16s cpsr: 0x%16s %s\n
ret.CFReadStreamOpen
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
source != __null
level_stack_.template Top<Level>()->inArray
RegionStart
DISPSEC
\tReading left over chunk expected 0x%x got 0x%x\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
AXconn_probed_command
Register file 3
GitHashDebug
products_
astris_get_die_count
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
{%s:%s@%d} [%s] writing LOCKACCESS\n
{%s->%s} exec: encode_mrs(scratch=%d, sysreg=0x%X (%s), regname=%s, %d)\n
   Debug Port not responding (%s)\n
FLASH_ACR
{%s:%s@%d} [%s] Writing FLASH_CR failed during lock sequence: %s\n\n
Failed to read DCM GPIO (0x%x)
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
DCS14
==== Exception Trace ====\n
Could not find portal by select %d, while interpreting result\n
Long Packet
Logging Context Is NULL\n
Cleaning up Main Booster Object\n
_exec
_cache_op_l2
internal.authenticate_dft.debug_auth == NULL
DBREAKC0
fn._ocd_reg_dcr_set.dcr_enable_ocd
_ocd_exec_instr
AVE
Die-Count: %d Current-Die: %d Die-Type: %d
astris_ide_get_revision
switch_regset
{%s->%s} EL2 not implemented
[AstrisAsync] Activating async...\n
[AstrisAsync] Pause when already paused!\n
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
astris_batch_attitude_attach
_write_memory_slow
ret.read.stepping_stone
error trying to unlock MSR %s
astris_memap_masked_read
Switch to primate res: %s\n
internal.clear_probe_auth.debug_auth == NULL
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s:%s@%d} [%s] reading PC\n
{%s:%s@%d} [%s] reading GPR\n
internal.clear-auth.chip->soc == NULL
{%s:%s@%d} [%s] \tCould not unlock flash\n\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/xtensa_cpu/xtensa_cpu.cpp
op_L8UI_encode
%02u:%02u:%02u:%06u|%s <%s> %s
value
Stepping Stone Final =  %#x\n
   ROM entry %d (level %u): AVOIDED\n
AXmemap_stmflash calling STM32G0x1xx::reflash (DEV_ID 0X%03X)\n
parameter val is NULL
astris_stmflash_h7xxx.cpp
cpu_writereg_vals
sending abort to clear a timeout\n
Failed to convert %s key @ index %d to a number with base of %d\n
{%s->%s} [!aarch64] exec: encode_mrs(%s=%d[%s], MDDTRRX_EL0, %d)\n
BP
consumedAcmds
Fault Error on Run-SWD Subcommand
Invalid current AP (%d), adopting latest (%d)
_write_cpu_reg_file
response == NONE; failed to get kis target info\n
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
MemberBegin
GetStringLength
{%s->%s} exec: encode_msr(%s=0x%X, scracth=%d, %d)\n
No windowed register option.
_ocd_enable
no AP (Access Port)
ret.get_hang_crumb
{%s:%s@%d} [%s] Waiting for flash to idle before lock, failed\n\n
NONE
astris_cfg_memap
Xtensa Option non_tie_ranges: %zu range(s)
Standard
more than one when unique required
{%s} probe_port = %d
MEM1500
{%s:%s@%d} [%s] reading PRSR (lsr)\n
!!!! Critical Error:  dlr_el0 NOT CACHED !!!!\n
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
PMGR_OCLA_REGS
val.check.content
esr_el3
{%s:%s@%d} [%s] error flags set by erase (0x%08x): %s\n
memory_write
_gen_debug_interrupt
Invalid category
!!!! Complex CPU Key %s is INVALID !!!!\n
Failed to fetch if we are in ARM64 or AARCH32
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
sel-sib-network
Master BoosterManager
soc-revisions
_read_spsr
{%s::%s@%d [%s]} Error %s: resuming HW
src_gpr < 32
Waiting for flash to idle before page erase, failed\n
_check_exception
m_wp_details
AXmemap_read_modify_write
!!!! Cannot explore via banana split. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
wb_u32=%u
too many of something
Spew change. old=0x%016llX, new=0x%016X
ret.dspsr_el0
write.reg.not cached
swdackdelay
internal.is_probe_authenticated.debug_auth == NULL
DBREAKA0
operandStack.GetSize() >= sizeof(Frag) * 2
%-16s @ 0x%08llX : 0x%08X\n
{%s:%s@%d} [%s] getting GPR 0 (ARB)\n
[ARM64 INS_WP] 0x%016llx x %d\n
Type 'jebdump' to do scan/mem dump\n
Awaiting response from Probe Map Server
Malloc
cpu-xtensa-num-wp
probe event: %s
TMM
AXcpu_readmem
internal.enable-timer-ovr.chip->soc == NULL
ret.CFURLCreateCopyAppendingPathComponent
Error %s opening single_port connection to probe server
VERSION
cpu_go
Value Types Are Not Strings\n
ACC-CTI
GRP_0
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
_ocd_reg_dcr_clr
par
[ARM32cpu_t::_update_register64] 0x%08x\n
_get_wpaddr_hw
wpcr
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
AXcpu_hwbp_disable
param.num_data_bp_regs.invalid.2
invalid host name or port
ASTRIS_ERR_NOTFOUND
\tCould not get sector number for address: 0x%llX\n
%s_%s
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
Table 5–155
op_L32I_encode
taps
Gathered Value is Not Number\n
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
ASTRIS_ERR_HTTP_FAILURE
fn.stmflash.h7.wait_bank_flash_idle.timeout
RemoveMember
{%s:%s@%d} [%s] executing MSR\n
Unable to disassemble_at_addr 0x%016llx
param.tgt->ap->dp.null
CLOSE
CPU %s not found or already removed from the map
symbol_array == NULL
sector_erase
getOrCreateObject.diagnostic_checks
AXjtag_srst assert failure - %s (%d)
result.read_vals==
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
%s-%06X
Error %s connecting to probe server
result.read.memap.s2r_fsm
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
fn._write_special_reg.dbreakc0
{%s:%s@%d} Critical error encountered:
Hang Description:\n%s\n
stack.h
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
{%s:%s@%d} [%s] AIRCR write failed: %s\n
{%s} skipping dcache flush, cache already clean
AXcpu_lacc_count_read
WRBUF
AuthDbg,SecurityMode
internal.enable-timer-ovr.chip == NULL
MemoryPoolAllocator
KIS Readvals putting back the value
EDPRSR_AON
{%s} Error setting up jtag-ap target (%s)
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
Choose a device: 
cpu_hwwp_remove
ret.clear_all_breadcrumbs
[1500] %s step %d: unknown instruction '%s'
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
{%s:%s@%d} [%s] writeval: %s\n
CPENABLE
cpu_status
BoosterPublicAPI
SPSR_ELx
ret.exec.drps
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
TRANSLATION_ERR_L2
## armcpu: bad status even though all bytes written (%d)\n
UNKNOWN CODE
probe on host %s
%s%d
addMember.user
Could Not Create Dictionary From Booster: %s
error %s checking for data abort
RF52
ParseStream
soc-pid
com.apple.astris
astris_cpu_trampoline
<rev>
RF53
ASTRIS_ERR_PROBECOMMAND
fn.stmflash.h7.eraseflash.mass_erase
page_erase
armv7m-region-name
{%s::%s} EDSCR with RXO set - unable to recover.\n
gpr < 32
%04X:
{%s:%s@%d} [%s] wait_for_flash_idle failed: %s\n
fn._read_snr.excvaddr
ChimpSWD
param.cpu_name == NULL
Register file 42
Using Built In SoCs\n
{%s} [%s] m_exception_level=%u\n
ret.drain.half-duplex
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
PROBED_USB_REQ_ERROR
Invalid port provided by probe server
.chip_id
fn.entry
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
\t%4X: %8X %8X\n
fn.stmflash.h7.program.writevals.actual!=count
message
ParseStringToStream
Invalid Bundle: %s
SWD Slave Unavailable
fn.stmflash.g071.mass_erase.write.cr_reg
Found match - bypass_device: %s; channel: %d\n
ret.chip == NULL
get_page_shift
ECID is 0\n
ASTRIS_ERR_VARNOTFOUND
mach_absolute_time
Parse
Fast Programming Error is Set\n
EDSCR
ret.a64cpu_raise_el_hw_safe
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
ERR
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
hwwp_remove
ERROR: nothing to do; suspending address translation for %s while already previously suspended
kis_stm_name %s %d
%s%s
ret.modify.edscr.~a
write.dlr_el0 NOT CACHED
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
op0: %d op1: %d CRn: %d CRm: %d op2: %d el: %d
EXPLORE_SET_MODE
General register 11
ret.relay.get.haskis
%s (addr=0x%llx)
fn._read_cfg_reg_0
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Creating CPU Returned: %s\n
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
_sstep
{%s:%s@%d} [%s] Cannot obtain the (alternate) device identification\n
RF47
fn._read_special_reg.debugcause
tokens_ == 0
context.validators == 0
ret.home_url == NULL
{%s:%s@%d} [%s] FLASH_CR SER write failed: %s\n
High level 6 exception PC
level_stack_.GetSize() >= sizeof(Level)
AXmemap_stmflash calling STM32G0x1xx::eraseflash (DEV_ID 0X%03X)\n
param.num_data_bp_regs.invalid.1
ASTRIS_ERR_ISCONN
sent %zd bytes to Probe Map Server when sending %zu
ArcEM
cpu-dbgwrap-offset
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
ret.storeNicknameForKey
Flash Reg Adress is not set, using what is there\n
fn._ocd_reg_w.dcrclr.regval
{%s} bridge timed out
{%s:%s@%d} [%s] FLASH_CR START write failed: %s\n
Std
fn.stmflash.h7.unlock_flash.flash_idle
Misc_Rtx117x
AXchip_get_stm_dockch_list
```
