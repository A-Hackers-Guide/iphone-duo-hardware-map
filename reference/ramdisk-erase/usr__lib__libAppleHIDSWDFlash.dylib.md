# `/usr/lib/libAppleHIDSWDFlash.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,379,776 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 4000)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libAppleHIDSWDFlash.dylib (compatibility version 1.0.0, current version 10110.4.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (2 classes, 0 protocols)

Classes: `AHSFProperty`, `AHSFSpuInterface`

## Strings (6,806)

First 2,500 of 6,806.
```
TXU
Wait indication while connecting to
setEnvironmentInfo
_a64cpu_write_aarch64_sp_hw
EXPLORE_WITHOUT_PIO_SAFEGUARDS
Exo
cpu_cache_info
RF9
ASTRIS_ERR_MISMATCH
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
{%s->%s} [!aarch64] exec: encode_mrs(%s=%d[%s], MDDTRRX_EL0, %d)\n
Reset
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
_write_executable_memory
High level 7 exception PS
SETRELAY
1.0
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
fn._write_special_reg.ibreakenable
HDE
[REM_WP] wp%d\n
AP
Exception virtual address
R10
fn._ocd_reg_r.ddr.regidx_save
ASTRIS_ERR_TGTOFF
ASTRIS_ERR_PROBECOMMAND
[1500] %s step %d missing required field 'instr'
DCS_BC0
ret.is_current_state_aarch64
mismatch detected
MEMAP_APB
_with_cpu_thunk
ret.production_emulation
CalibrationReadModifyWrite
apb-regs
!!!! Critical Error: GRPS[0] cached !!!!\n
ELR_EL1
TIMEOUT
connecting to selected probe (single_port)
createCPUPlaceholder
GetHashCode
DOCK-CH-AGENT0-STATUS
{%s} Failed to extract CIP Gen Number from table (%d); continuing anyway
_write_spsr
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
Double exception PC
RF14
cpu
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
UNKNOWN
/usr/local/share/astris/boosterpack
ret.reg.write.K_DA_REG_NAME_PROBE_STATUS
internal.enable-test.debut_auth == NULL
halted=%d
fn._read_special_reg.ibreakenable.reg_bp_enables
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
MemberBegin
bypass-config-name: %s\n
FPB
_a64cpu_clear_async
{%s::%s} [%s] WP_INSERT _find_bpwp(0) failed
AXcpu_writemem_width
Trying to use size of 8 on not AXI bus
SSO is DISABLED\n
Complex Name: %s\n
src_gpr < 32
ret.createKey
op_TIEInitiateReadProtectedI_encode
{%s} host name(RSD): %s\n
SWDFlashWrite
MMX
Groups %d\n
astris_explore_enabler_add_cpu
{%s:%s@%d} [%s] updating DFSR\n
{%s->%s} [!is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
AXcpu_hwbp_info
EPC3
CTI_OUT_EN0
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
Result while reading first entry: %s , entry val 0: 0x%X\n
OCD control register, set
Loop-begin address
lldb
Failed to connect to AppleAstrisGpioProbe kext %x
dcm
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
ATOMCTL
High level 7 exception PC
fn._read_general_reg
v%s.%s
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
ERR: conn->nchips != 0; looks like chip is explored\n
Failed to exec MSR to move contents of scratch (containing val to write) into sysregscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
createKey
!!! FILE RADAR: Failed To Instantiate built in CPU for %s !!!\n\n
Failed to init booster
ret.fromreset
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
storeNicknameForKey
virtual int CPU_t::resume(bool)
param.regval.null
{%s} DEVARCH read fail in CoreSight component (%s)
TCP recv
AXbooster_refresh
=== Detailed %s Boosters ===\n
cpu-xtensa-reg-size
Debug Port
EDECR
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
[%s] AP, DP, or chip given is NULL
/usr/local/share/astris/schemas
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
{%s} asc status=%d being reported as Unknown
MEVADDR
No connection attempt description
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
Failed calling AppleSOC_t::switch_taps\n
Both debug and xbs versions are set, maybe a bug: %s
param.no_ap
Error %s connecting to probe server
{%s@%d} Unknown CS code [%u]
JTAGAP
Failed to populate component info
Warning: chip exploration did not complete successfully (%s)\n
DEPC
ret.drain.half-duplex
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
!HasParseError()
[PAR] Failed KIS Portal Access Preflight =%s (%d)
{%s:%s@%d} [%s] doing IR scan (DTRRX SCAN_N)\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
panic_diagnostic
Creating Flasher For An Unknown AOD Type: %d\n
In Postflash\n
handle_pending_async_aborts
ARM64 SWBP not supported in T32 mode
AXcpu_lacc_count_remove
AXchip_find_dap
RF61
Invalid reg_index %u
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
ASTRIS_ERR_NOSOC
/
M
ESR_EL1
Breakpoint Size: %d
_remove_instr_breakpoint
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s::%s} [%s] error %s reading SCTLR_ELx
RESUME
{%s} ROMTABLE (dbgbase=0x%llx)
RF0
fn.local
\n!!!!!!!!!! Error: %d (%s) opening log file %s !!!!!!!!!!\n
Probe Map comm error %d(%s) %s [%s]
batch_cmd_count: %d
ARM64cpu_t
_cache_op_l2
astris_init_dp
Processor status
_ocd_reg_dsr_clear_and_validate
%c
MISMATCH
SUCCESS
internal.authenticate_dft.chip->soc == NULL
Stop Clock Active
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
CPU1
ret.clear.edscr-error
Register file 45
CopyPart
!(calTotalLength(%@)<kCalibrationMaxLength(%@))
_read_register64
fn._write_special_reg
ASTRIS_ERR_PROBEHWERR
IsValid()
GetUri
soc-pid
astris_ide_refresh_boardid
_a64cpu_raise_el_hw_safe
param.conn.connected == false
{%s} Failed to get breakpoint mask for %s: %s
PARTNO_SWDP_SOC600
locationids
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
Generation of the nonce timedout\n
RF30
stderr
primateLoc
result.read.dbgwrap_base==
ESR_EL3
[AstrisAsync] astris_async_override_disable_async: conn is NULL
X00 Part
EXCSAVE2
PORTAL_STS_MULTIPLE_BITS_SET
koko
Failed to write transfer register (EDDTRTX) the value to write
Failed to write SPS_EL%d
RF4
memap_bus_read
hid-fw-personality
probeBoardNames
Table 5–175
0 == Base::level_stack_.template Top<typename Base::Level>()->valueCount % 2
{%s:%s@%d} [%s] reading PRSR (!lsr)\n
[%s] cop %d -> 0x%08x\n
Highest EL: %d, -- Min Op EL: %d
HostInfo
connecting directly by port number
Required key: %s @ index %d is NULL\n
result.read_vals(version)==
ret.rx-full.mddtrrx
Request Dict:\n%s
AXdebug_auth_is_dft_authenticated
fn._ocd_reg_w.dcrclr.regval
target is probably resetting
{%s}#%02X %s [%s]
ret.CFReadStreamOpen
Memory error save register
Table 5–149
CPU is halted
getOrCreateArray
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
High level 5 exception PS
{%s:%s@%d} [%s] reading CCSIDR[L1-I]\n
hid
ACQ_SAMPLE_I2C
Failed to instantiate %s\n
cpu_go
param.booster_bundle==NULL
RegionStart
dest_reg < 32 || dest_reg == 31
param.conn.user_defaults == NULL
AXjtag_explore
Only Auth-Debug, DFT-Auth and Probe-Auth are currently supported.\n
Table 5–130
Could Not Get BoosterManager\n
implementer
!!!! Critical Error: m_exception_level[%d] == 0|1|2|3 !!!!\n
read_dbg failed to access R_v7M_CLIDR
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
Register file 29
param.val.invalid.>max
KanziSWD
createClientList
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
ret.exec.drps
XINIT
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, %s=%d, %d)\n
copyNicknameForKey
Setting STOP CLOCK to TRUE
AXcpu_flush_icache
bad parameter(s) specified
Didnt match any service/parent for AppleAstrisGpioProbe
DBG_CPU: %s\n
Xtensa Option options: 0x%x
resolve_debug_components
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
   CPUID: 0x%08X\n
_%04d-%02d-%02d_%02d.%02d.%02d
Error %d (%s) %s %s probe server
setup_booster_soc
Miss fraction part in number.
!hasRoot_
Gathered Info:\n%s
result.extract_table_info==
astris_user_default_remove_all_boardnames
LEND
fn._tie_read_word32.first
fn._read_snr.excvaddr
cpu-apselect
Run
ret.CFReadStreamCreateWithFile
ASTRIS_ERR_NODP
Selecting polling method %s
sys_pwr_up
Bundle: %s NOT FOUND\n
{%s} Failed to extract component info from table (%d); continuing anyway
{%s} skipping dcache flush, cache already clean
fn._read_pc
version
read failed, using old cached as base: 0x%x
symbol.check.loaded.AMAuthInstallSupportDictionarySetInteger32Ptr == NULL
str != 0 || len == 0u
{%s} write[ED64] of %s @ address 0x%016llX = 0x%016llX [%s]
USB connection not currently open
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
writer.h
respone == None
booster
content = %p
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
   Debug Port: SELECT %X: AVOIDED\n
_read_special_reg_by_name
[ANAMOLY] Could not find AXcpu_t object for CPU\n
n >= 0 && n <= 308
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm64cpu.cpp
_a64cpu_get_current_el_hw
probe %s [port %u] on localhost
Stringify
{%s} no matching 1500-to-* bridge
base-addr: 0x%016llX present: %d comp-id: 0x%X - loc-id: 0x%X - feature-id: 0x%X - subsys-id: 0x%X - midr: 0x%X - type: 0x%X
read.dlr_el0 NOT CACHED
%04X:
INVALID
could not perform cpu_preflight
~/Library/Application Support/Astris/astris_prefs.plist
Register file 25
pmu-name: %s\n
{%s:%s@%d} [%s] reading PRSR (oslk)\n
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
{%s} retries of astris_command(JTAG,EXPLORE) unsuccessful (last error=%s)
PROBED_ERROR
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
{%s::%s} %s pre_resumed\n
EXPLORE_IDENTIFY_ONLY
Failed to exec MRS to bounce sysreg into scratch register. scratch=%d, sysreg=0x%X, regname=%s
[AsyncSnapshot] No snapshots collected\n
AXconn_connect_kext
CortexM0
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
_write_memory_slow
Impeded
ASTRIS_ERR_BADENV
sib-network-psr-reset
INVALID KIS VERSION
Register file 10
_read_general_reg_by_name
reg_file_index = %u >= m_cpu_reg_file_size = %u
Abnormal %s termination: Assert Area Mask = 0x%016llX
%2d) %s %s [Busy]%s\n
' written at document root (failed to create parent object '
TAP IDCODE: 0x%X\n
_halt_hw
_a64cpu_read_gpr_hw_impl
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
%02u:%02u:%02u:%06u|%s <%s> %s\n
Write Data Length Mismatch
cpu_hwbp_info
output_type
missing property aod-type
bridges
M3_ROM
Gateway Version: 0x%X\n
[ARM32cpu_t::_read_register64] 0x%08x\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
process_status_transition
AXcpu_mmu_get_mair
!([calBlob length](%@)>=blobLength(%@))
ret.getCpuEnableStatus
{%s->%s} START handling exception
{%s} failed (%s)
AMAuthInstallLogSetHandler
Connected to Probe Device Server [Default Log]
document.h
result.alloc_table==NULL
EXPLORE_WITH_SEP_DEBUG
internal.is_probe_authenticated.chip->soc == NULL
PROBED
!!!! Critical Error: Error %d(%s) deleting info %p batch_attitude_key !!!!\n
{%s} [%s] EDSCR with ITO set - ERR while waiting ITE.\n
ret.reg.read.K_DA_REG_NAME_PKA_BASE_HI
Portal Config Read
PKA Base: 0x%llX\n
unexpected req_type argument
TOOMANY
KIS-STM
wrstn-partition-number
ASC-CTI
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
ApProductionMode
HIFI3_2
Dart Base Address: 0x%llX\n
localwrstn-debug
spsr_select
_synchronize_context
Accumulator low bits
Register file 48
ASTRIS_ERR_NOTUNIQUE
astris_server_read
reset_dcm: %s
[PCR]: failed (%s : %d) id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s} [!is_64] exec: ISB_SY_ENCODING\n
[%s] %d -> %08x\n
{%s} Batch attitude key created for %p thread %#llx key %lu
setTargetIdentifiers
type >= kNullType && type <= kNumberType
mempool-size
spr-regs
{%s:%s@%d} [%s] scanning out (DSCR)\n
L1 icache
AXcpu_mmu_get_tsz
astris_setup_ap_mem
unable to identify chip
No 1500 bridges or TAPs specified (v2 plist)\n
=== Found %s Boosters ===\n
false
{%s:%s@%d} [%s] doing JTAG scan (DSCR)\n
Cycle number to inter.
SCOMPARE1
fn._ocd_reg_w.ddr.value
cpu_hwwp_disable
Unable to read FP
[iter %lu] after_replay_preflight_and_collect
internal.is_dft_authenticated.chip->soc == NULL
{%s@%d} Received %d bytes when requested %d bytes.
Astris Source Version: %s\n
CPU.ARM64
L3
ret.spmi_read
clear_dft_authentication
{%s:%s@%d} [%s] unable to read response payload\n
 (%s)
CPU Explore: 0x%llX\n
[AstrisAsync] Activating async...\n
PROBETIMEOUT WHILE WRITTING\n
%s [RETRYING]
Failed to create Xtensa CPU %s \n
ret.board.copyPairForPref
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
SSO info present but SSO disabled.
OCD.DSR=0x%8.8X
op_WSR_encode
JsonLogger: Created with default schema version '%s'
Register file 36
WindowStart
Xtensa Option reg_file_size: %d
ASTRIS_ERR_LOSTCONN
--> master     size=%3d localwrstn=%d debug=%d
[AstrisAsync] Deactivating async...\n
astris_memap_debug_writebuf
Can't get OS build version - failed to create ReadStream
{%s@%d} Connection to server failed, error=%d (%s)
JTAGPORT
[DCC] Grabbing DTR failed: %s\n\n
{%s:%s@%d} [%s] writing DRCR (STICKY)\n
     ARM %s breakpoints: %u\n
[iter %lu] after_codeblock_execution
index != kRegexInvalidState
AXbooster_print_boosters
{%s::%s} EDSCR with TXU set - unable to recover.\n
AuthDebug_t::init failed (AuthDebugWithTimer_t)
ClassType
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
astris_cpu_trampoline
_write_cpu_reg_file
XPROG
CPS
APCIE_REGS
1970-01-01T00:00:00Z
ir-cmds
error %s reading DAP PFR1
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
ret.modify.edscr.~MA
internal.enable-timer-ovr.debut_auth == NULL
ApChipID
ret.reg.write.K_DA_REG_NAME_NONCE_3
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
cpu-dbgwrap-status
astris_explore_enabler_init
{%s:%s@%d} [%s] Read DWT Func %u\n
Gathered:\n
Unable to convert plist file name to CFString: %s\n
Extract Offset: 0x%X for %d\n
ret._mmu_init
no enable slot available
Register file 5
Register file 52
PROBED_USB_INUSE
armv7m-region-name
astris_ide_get_boardid
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
[AsyncSnapshot] #%zu: %s\n
SSO with no prompt being used
fn._read_special_reg.ibreaka1
fn._read_special_reg.dbreakc0
!*!*!* ****************************************************************************** !*!*!*
Could Not Find Any Boosters\n
armv7m-region-axim-start
First Couldnt
{%s->%s} exec: encode_msr(%s=0x%X, scracth=%d, %d)\n
{%s::%s@%d} [FALSE] src_gpr[0x%08X] < GPR_COUNT\n
Original Content: 0x%08x
fn._read_general_reg.regval
TRANSLATION_ERR_L1
_a64cpu_encode_msr
code
ELR_EL2
_read_pc
Failed to convert kisHubLoc %s to unsigned long long
AXbreadcrumbs_clear
!Base::level_stack_.template Top<typename Base::Level>()->inArray
%Y-%m-%dT%H:%M:%SZ
Could Not Allocate Booster Location Array
AXcpu_lacc_pipe_set
AP given is not a MEMAP
astris_create_ap_slave
{%s} FAILURE - max length exceeded
Error while trying to authorize: %d - %s\n
AuthDbg,SecurityMode
_cleanup_hw
result.booster_api_vers==NULL
CoreSight
Invalid special reg. number %u
reg.ocd.dsr.invalid.not_cleared
misc-size
ret.lower.after.read.aarch64hw
swdackdelay
fn.unsupoorted
specified CPU is not available
{%s:%s@%d} [%s] reading ADFSR\n
[REMWP] wp%d\n
ASTRIS_ERR_BADPARAM
cpu_hwwp_info
Terminate parsing due to Handler error.
addTimingPhase
AMCP2
print_debug_regs
Error:ASTRIS_ERR_BADPARAM(-29)
GetAllocator
cpu-address
ret.reg.write.K_PKA_REG_NAME_DBG_STATUS
Status/State
Error closing %s [%d]
schema_version
[1500] TAP %d missing required field 'chip-index' or 'irlen'
data-size
==== Exception Trace ====\n
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
cpu_lacc_status_remove
Parse
SWDFlashRead failed: 0x%08x\n
cpu-armv7m-regions
      Select port %u: already explored..re-exploring\n
AXdebug_auth_enable_test
General register 6
probe [port %u] on host %s
SOC_t::{%s} CPU_t group=%d when group 0 expected
buffer != 0
{%s::%s} error %s writing EDSCR %s
: [
{%s:%s@%d} [%s] write to CMD/STAT failed\n
sso_user.conn == NULL
_write_reg
ASTRIS_ERR_PROBED
{%s@%d} gethostbyname failed, error=%d (%s)
source != __null
No %s entry was found, checking for %s...\n
param.conn.chip  == NULL
{%s::%s} cpu powered off: failed init() %s
RF29
{%s[select]} %d(%s) [RETRYING]
EndObject
[1500] run_steps: unknown instruction '%s'
PROBED_USB_REQ_EMPTY
KobaSWD
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
--> debug      size=%3d acsr=%d
{%s::%s} cpu powered off: _set_corenpdnrq(true) != ASTRIS_ERR_OK
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, scratch=%d, %d)\n
AXcpu_sstep
EXPLORE_WITH_AUDIO
High level 4 exception PC
MECR
%s:
ASC_ECORE_ROM
{%s:%s@%d} [%s] unable to transfer command\n
Schema validation failed at: %s (keyword: %s)
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s:%s@%d} [%s] doing JTAG scan (DTRRX)\n
pc:  0x%16s cpsr: 0x%16s %s\n
{%s=>%s} no soc reference; falling back to direct cpu method
{%s} Error reading PID (%s)
no AP (Access Port)
PrettyPrefix
entry.exception_test_2
{%s:%s@%d} [%s] executing MRC\n
_a64cpu_lower_el_hw_safe
base_reg < 15
{%s} unmodified-probe_match = %s
end
IODeviceTree
true
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
CCSIDR
[AstrisAsync] Complete Queue callback returned %d (%s)\n
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
   {%s} Before powerup CMDSTAT=%08X\n
ret.reg.write.K_DA_REG_NAME_AUTH_TIMER_STATUS
AXcpu_hwbp_insert
ApSecurityMode
EXCCAUSE
RF59
fn._reg_desc_lookup_by_name
BoosterManager
!!! Critical Error msr_cache[%d] IS NOT cached !!!
EDDTRTX
Result while reading third entry: %s , entry val 2: 0x%X\n
## apw %u 0x%08X 0x%08X\n
ret.get_hang_crumb
internal.is_authenticated.chip->soc == NULL
codepoint <= 0x10FFFF
{%s:%s@%d} [%s] setting DTR MODE to STALL\n
PARTNO_SWDP_M7
internal.clear-auth.chip->soc == NULL
AXconn_probelist
{%s:%s@%d} [%s] getting GPR 0\n
ret.state_valid_entry_exit
{%s} Failed to get watchpoint mask for %s: %s
      Select port %u: AVOIDED\n
ExampleKey
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
Invalid bp = %u. Should be in range 0..1.
KIS Timeout
{%s::%s@%d} [FALSE] system_reg[0x%08X] & REGID_MASK != 0\n
{%s} read %d words from probe when %d words requested
param.invalid.reg_file_index.outofrange
reg_addr_offset=0x%4.4X, m_ocd_base_address=0x%8.8X
ARMV4
## armcpu: bad status even though all bytes written (%d)\n
ASTRIS_ERR_STOPCLOCK
Selecting
cpu_hwbp_disable
Invalid Bundle: %s
!!!! Critical Error: Thread %#llx key %lu relaxing attitude for %p when not attached - NOT ALLOWED !!!!\n
{%s:%s@%d} [%s] updating CPSR\n
intack
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_ACTUAL_LOAD
register    %-15s %3u     \"%-s\"\n
fn._ocd_reg_w.ddr.t2_save
astris_kis_clear_status_registers
None
{%s:%s@%d} [%s] DEMCR write failed: %s\n
Register file 0
_remove_data_breakpoint
CPU-level (general and architecture-specific)
kan
Invalid value.
uri.h
Could Not Allocate All Boosters Array
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
Table 5–181
reset_connect_state
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
[1500] v2 plist missing required field 'bridges'
Preferences does not exists: %s, creating one.\n
RF21
fn._write_special_reg.dbreaka1.address
  Error path [%s]\n
{%s::%s} EDSCR in unexpected state. Returning %s.\n
fn._ocd_exec_instr.rsr.reg_srn.t1
CTI_CH_PULSE
{%} exec: encode_hint(NOP)\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
unable to read memory (using system ap)
R5
{%s} error: %s
fn._collect_snr.excvaddr
classic
GetString
Portal Group Offset: 0x%X Entries: %d\n
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
dspsr_el0
Failed to raise EL to %d to read register: 0x%llx
ExampleValue
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
fn._ocd_exec_instr.rsr.ddr.data_reg
Failed to convert primateHubLoc %s to unsigned long long
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
Koko
cpu_hwwp_insert
is.Peek() == 'n'
{%s:%s@%d} [%s] writing DTRRX\n
%s status transitioned: %d ('%s') -> %d ('%s')\n
load_framework
is_ecid_zero
KICKINFO
connecting to selected probe
choice: %d\n
Problematic JSON value:\n%s
required
SCODEC
dest_gpr <= 15
init_hw.read.dhcr
ACCHI
fn._ocd_reg_r.ddr.regval
ASTRIS v%s%s [%s]
Ring ASID values
IOPlatformExpertDevice
{%s} select success without file descriptor set
psr-bit
group=%d
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
{%s:%s@%d} [%s] writing WCR %d\n
GPR
Xtensa Option num_high_pri_intr: %d
ASTRIS_ERR_USB_NOTOPEN
.start_time
IOCFUnserializeWithSize failed: %@
{%s:%s@%d} [%s] getting GPR\n
AuthDebug::authenticate_probe - no need to authenticate\n
pid
cpu_readreg
personality[%s] missing
AXdebug_auth_clear_auth
Too many address breakpoint regs (%u). Maximum is 2.
param.wb.invalid.>wb_max
fn._ocd_exec_instr.rsr.ddr.regidx_restore
Memory Access Port
operandStack.GetSize() >= sizeof(Frag)
{%s:%s@%d} [%s] writing CSSELR\n
Could not enable KIS SoC Access\n
RF2
PCORE
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
timestamp
Cleaning up Main Booster Object\n
ret._handle_exception_for_el
lower_el.el2.noimplemented
got a fatal error translating VA to PA
storeNickname
High level 2 exception PC
No windowed register option.
{%s:%s@%d} GRPS[1] cached\n
ret._set_wpcr_hw
xfer_acmd_via_kext
ret.explore_table == NULL
{%s} [is_64] exec: encode_msr(MDDTR_EL0, 0, %d)\n
address=0x%8.8X, len=%u, rdwr=%d
ASTRIS_ERR_VARNOTFOUND
[1500] No %s.plist resource found
{%s:%s@%d} [%s] writing DRCR\n
UPDATE cop64 %d -> 0x%016llx\n
Probe is not KIS or KIS-STM or kis translator version < 3 so returning NOTSUPPORTED
probed USB transaction timer expired
Kick has been requested by probe server
astris_get_hang_crumb
set.target_os
result.astris_identify_load_booster
We are done with clean up\n
!!!! Critical Error: aarch64[%d] == believed_64bit[%d] !!!!\n
high
sso_user.sso_user == NULL
Dart Dart Type: %s\n
spsr_el2
couldn't read TTBR1
<rev>
Memory error PS register
AddMember
RF33
createKeyWithPrimate
param.reg_name.INVALID
Creating Cypress Flasher\n
IMX
result.extract_dbgwrap_base==
astris_explore_enabler_get_subsystem_status
{%s:%s@%d} [%s] reading BCR %d\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
EPS5
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
AXspmi_write_bus
ret.rx-full.mddtr
Lowering exception in AARCH32 Mode NOT SUPPORTED
Disabled
Optional Key: SubsystemMonitor not in preferences
target power is OFF
operation not supported
Init dbgwrap obj failed
  Nested path: parent='%s', child='%s'
MTP
exit.exception_test_0
Successfully connected to server, %s:%d
comparing against match entry %d: %s
DCS12
32 
_get_type_hw
axlog_assert_upcall
CalibrationOverrides
param.portal_base == 0
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
R6
param.bp_index.invalid.outofrange
fn._ocd_reg_r.dsr.dsr
{%s::%s@%d [%s]} Error %s: synchronizing context
Failed to read transfer register (EDDTRTX)
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
Table 5–137
TGTOFF
MSR
!!!! Critical Error: suspended batch attitude for info %p trying to cop - NOT ALLOWED !!!!\n
ret.restore_el.write
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
OCD Debug data register
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
Hang Address: 0x%016llx\n
0123456789abcdef
BoosterManager.CPU
astris_explore_enabler_del_cpu
{%s@%d} Unable to connect to server, %s:%d
M3
param.width.invalid
ASTRIS_ERR_NOMEM
BoosterManager.SOC
[SSTEP] bvr=%08x bcr=%08x\n
{%s} exec: DC_CVAC_X1_ENC\n
write_memblock_dbgwrap
Coproc, enable bits
ASTRIS_ERR_NODATA
Could not find TAP at index %d to attach 1500 bridge to\n
buildCategoryJson
{%s} bridge timed out
Table 5–164
Corruption detected selecting probe from probe server
No 1500 bridges specified\n
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
DBGCTRL = %08X   res=%d\n
com.apple.astris
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
AppleAstrisGpioProbe
{%s:%s@%d} [%s] doing JTAG scan (DTRTX)\n
Error occured during nonce command (v.5)
Requires OCD option for >1 address breakpoint regs.
_write_window_base
invalid environment variable
AXchip_get_chip_variant
## armcpu: bad status even though all bytes read (%d)\n
fn._ocd_exec_instr.TIEInitiateReadProtectedI
ASTRIS_ERR_CPUHALTED
stack_.GetSize() == sizeof(ValueType)
DEMCR write failure - %s (%d)
_check_exception
AXcpu_writemem
!!!!!!!!!!   $ sudo chmod 0775 %s\n
buf != 0
{%s} read[CTI32] of %s @ address 0x%016llX ERROR %d(%s)
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
Failed to Identify & Explore Chip via KIS: %d (%s)\n
CPU.ARMv7m%s
/tmp/astris_probetimeout_hang_%s%s.log
cpu_lacc_status_insert
ret.chip == NULL
{%s} Thread %#llx key %lu detaching from info %p when lock owner - IMPLIED BATCH END
Discon
op=%d
index < rangeCount_
{%s:%s@%d} [%s] going to RTI\n
ret.read.esdcr.nolog
ADI
SWD
ret.reg.read.K_DA_REG_NAME_SECURE_MODE
fn._write_mem.bp_info
a
astris_setup_connect
quit
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
{%s:%s@%d} [%s] reading DIDR\n
Table 5–167
IBREAKA1
j1500i
GitHashDebug
AXbooster_interface_create_swdflasher
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
_clean_invalidate_l2cache_setway
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armcpu.cpp
RF58
Invalid num_regs = %u. Windowed register option required.
Could Not Create Dictionary From Booster: %s
{%s} Failed to extract IDCODE from table (%d); continuing anyway
Invalid content key, %d
   Debug Port not responding (%s)\n
General register 2
ERROR!! Couldn't save %s binary data\n
stdout
ASTRIS_ERR_NOCPU
{%s} bridge returned DECERR
hostid
Complex ID: %d\n
defaults.create.key.no_probe
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
port_%d
Clear
ParseRange
Failed to exec DCPS in order to move EL up to %d
Error status from AMAuthInstallSsoSetStealthModePtr = %i
Unknown kick response[%s] (for probe %s) from probe server
decr_drain_packets
BADCODE
Multi target booster, checking for %s.plist\n
{\"max_events\":%u,\"events\":[%s]}
Translate Stage Chosen: %d\n
runBlock
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
M4F
enable_timer_ovr
Data TLB configuration
firmware version is too old DEPRECATED
checking if relay \"%s\" is valid
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
SoC has been setup using standard instantiation (setup result=%d)
PORTAL UNAVAILABLE
param.cpu_reg_file_size.invalid.1
TCP send
15002AXI
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
[READ] %d -> %08x\n
reg.!ocd.dsr.stopped
op_XSR_encode
ret.dfu.dcm.reset
virtual int ARM7cpu_t::_halt_hw()
couldn't read TCR
Parity Error on RUN-SWD Subcommand
pnav_connect_probemap
{%s:%s@%d} [%s] executing MOV (diff mode)\n
{%s} 0 words requested for read at address 0x%016llX
reg_name not specified.
TRANSLATION_ERR_L2
CortexA53
GenericRegexSearch
%08x: %s\n
--> 0x%02x = %s
bypass-configs
{%s::%s@%d [%s]} Error %s: checking exception
swdovrrun
ret.reg.write.K_DA_REG_NAME_AUTH_VALID_CLEAR
op_TIEWriteProtectedI_encode
15002APB
astris_exc_bread_test
EDITR
UNKNOWN_DAPSTAT
DPAP
Failed calling AppleSOC_t::dock_disconnect_mode\n
astris_ide_get_cps_fsm
Proceeding with full explore instead of instantiation
param.ocd_base_address.invalid.unaligned
#ch-
   DPv3 bus is %u bits wide\n
KIS Chip Found, Doing KIS Explore Setup
fn._read_special_reg.ibreaka0
port
{%s::%s} %s resumed\n
(addr=0x%llx)
ret.clear_probe_authentication
Register file 9
{%s} unable to find single_port probedaemon on port %d
Invalid value for 'entry' tuple element - can't index
init_hw.set.dhcsr.en
General register 12
ASTRIS_ERR_PROBEINUSE
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
%s: %s\n
Kick required to connect: Busy probe %s
AXchip_get_stm_dockch_list
ATS1Eop
WindowBase
Creating NXP Flasher\n
j1500i2
Failed to read DCM GPIO (0x%x)
wir-wrstn
{%s:%s@%d} [%s] executing MOV\n
AP[%d]: JTAG_AP (Exploring Later) \n
General register 13
Register file 4
Can't get OS build version - failed to create URL
EmulatorSWD
Probe Map Server Information: %s
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
AXcpu_lacc_status_remove
AuthDebugWithTimer_t destructor \n
_write_general_reg
DIAGS
{%s::%s} creating placeholder for CPU: name=%s
Missing property aagp-name
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
ret.reg.write.K_DA_REG_NAME_NONCE_0
astris_gather_poral_error_info
DCS_BC4
Failed to write register: 0x%llx val: 0x%llx
AXchip_is_prod_fused
Logger output is null
[AstrisAsync] Barrier before pause\n
AXdebug_auth_get_dft_timer_count
Error while %s:\n  %s %s
cpu-xtensa-ocd-base
m_loaded_framework == NULL
RdProt
unknown
dart-base-address
{%s} [exception_level(%d) != current(%d)] exec: DRPS_ENC\n
IBREAKA0
reg_name (\"%s\") not present.
Error %d (%s) opening cmd snapshost save file
Astris-%d~%d
APPLETYPE_UNKNOWN
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
read_dcc
bp_index=%d
more than one when unique required
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
cleanup
CreateSchema
For production parts make sure you have allow_swd_updates=1 set in your boot-args
aod_type
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
{%s:%s@%d} {%s->%s} EL3 not implemented\n
{%s} _resume_hw result = %s
\tPrologue Aligned Read Failed
Xtensa Option num_bp: %d
Misc_Rtx117x
(reset-network)
_collect_hw
Async barrier encountered
cpu_get_cl4_debug_signpost
cpu_swbp_remove
cpu_lacc_count_remove
MiscCortex_t
ISP_L
 %02X
AMAuthInstallGetLocalizedStatusString
SPIXACT
logger already initialized
Got an error reading the DCM Control Register: %s
soc-rev-num
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s->%s} m_exception_level=%u
{%s} Found extra info in = %s, chopping string
{%s->%s}[cached] %s[0x%X] = 0x%08llX
AXcpu_hwwp_disable
[1500] Using %s.plist
CRYPTO
resolve_platform_details
astris_memap_bus_write
fn._ocd_reg_w.ddr.1
Apple Fabric Timeout
Astris timedout waiting for ITE during CPU Memory Read. Last EDSCR: 0x%X\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
Misc register 2
Register file 30
already connected
encodings.h
_read_register32
PowerGated
   {%s} Read AP's R_MEMAP_CSW\n
EXPLORE_JTAG_NO_BOUNDARY_SCAN
wb=%u
Malloc
appendToArray
_resume_hw
[ARCH32] Failed to exec MRS to move contents of MDDTRRX (containing val to write) into scratchscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
[REMBP] bp%d\n
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
_tie_read_word32
Unable to connect to %s - %s
spr
CDPUL
PMGR_OCLA_REGS
Unable to register assert upcall %s (Insufficient memory)
Probe %s Device Server listening on port %d
Length is 0
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
EPS6
fn._ocd_reg_r
normal
cpu-ps-register
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
defaults.create.key.outofmem
internal.clear-auth.debut_auth == NULL
Data break 0 address
AXcpu_resume_translation
   DPv3 baseptr is not valid (%X)\n
name %d
Probe Map comm error %d(%s) %s
DSP
ret.nop
set.user
{%s:%s@%d} [%s] reading GPR 1\n
[%s] error reading EDSCR with mask
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
astris_memap_masked_read
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
write.dspsr_el0 NOT DIRTY
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
op_RSR_encode
Cleaning up Each Booster Manager\n
EDBXVR0+index
defaults.nickname.not_connected
https://gs.apple.com:443
param._tgt.invalid.null
%d.%drc%d
{%s} error %s at line %d
CS-CTI
[FLUSH]\n
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
[COLLECT] Chip %x\n
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_dapcmds.cpp
ICOUNTLEVEL
{%s:%s@%d} [%s] reading LOCKSTATUS\n
configure_mmu failed
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
Wake
address=0x%8.8X,page_id=%u
assert
generic probed USB error
%x.%02x%s
General register 5
Register file 2
%d:%d%s
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Could not find TAP at chip-index %d for v2 1500 config\n
cpu_lacc_pipe
Schema file is empty
shared_ != 0
Register file 49
PROBED_USB_REQ_TIMEOUT
host %s
Register file 14
memory_read
We are Allocating\n
get_current_mmu_regs
Table 5–174
exit.exception_test_2
{%s:%s@%d} [%s] reading WVR %d\n
esr_el3
EL3h
connect-probemap
outstandingAcmds
## dpw 0x%02X 0x%08X\n
chimp
%02X 
DCS10
EXPLORE
_pre_resume_hw
far_el1
High level 5 exception PC
EPS7
Disconnected from Probe Map Server
incr_drain_packets
RTP
Debug Base: 0x%llX\n
{%s::%s} [%s] successfully translated [VA=0x%016llX, PA=0x%016llX]
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
L2
X06 Part
wb
ERROR: nothing to do; resuming address translation for %s without previously suspending it
HardwareBreak
fn._ocd_exec_instr.l16ui.r1.r0
%s %s:l=%u,c=0x%X,i=0x%X,f=0x%X
s
internal.clear_probe_auth.chip == NULL
PC
RF43
ASTRIS_ERR_DISASM
#KIS
ARMDAP
allocators.h
poo
ret.enableSubsystem
write.reg.not cached
## armcpu: success status even though not all bytes written\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
RF10
fn._resume
Std
dpb-size
PS
Section 5.3.6
(Last: %s) (%s)
cpu_hwwp_enable
CPU Name: %s\n
SPSR_EL1
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
[HALTED] dfsr = 0x%08x\n
AXcpu_cache_cleaninv
authenticate_dft
Register file 11
Previous attempt to connect to probe failed: %d (%s). Retrying...
ASTRIS_ERR_USB_EMPTY
no system bus AP present with AHB, trying AHB5
{%s} 0 words from probe when %d words left to read for reg %d
astris_user_default_set_nickname
hwbp_enable
AXdp_read_with_recovery
astris
Standard level
AXconn_destroy
Probe removed prior to kick: probe %s
CalibrationRequired
DCS_BC5
AuthDbg,EnProbeFuncExternal
%s probe[*] from Probe Map Server [%s]
cpu_cache_info_group0
astris_json_logger_delete
virtual_memory_bytes
AXconn_get_pid_bid
{%s} drain_packets=%d [%s]
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
{%s::%s@%d} [FALSE] aarch64\n
PARTNO_SWDP_M23
OCDID
_write_special_reg_by_name
Unable to get version info from %s [error %s]
invalid aod-type
astris_get_die_count
ocd_base_address = 0x%8.8X is not 4 KByte aligned
_ocd_reg_dcr_r
interface not in appropriate state for action
[%s] EL @ end of Collect: %d\n
Unspecific syntax error.
{%s} bridge returned SLVERR
mempool-dmem-offset-reg
astris_batch_attitude_cop
{%s:%s@%d} [%s] getting GPR 0 (COP)\n
{%s::%s@%d} [FALSE] base_reg[%d] < 15\n
Going To Create Generic Xtensa Core, name=\"%s\".\n
internal.get-timer-count.chip->soc == NULL
EXCSAVE1
fn._ocd_enable.true
%s%d
read_resp_cmd_via_sock
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
Memory map ID
param.reg_name.invalid.null
fn._ocd_reg_w.ddr.tgt_32
Listing
ret.dspsr_el0
_ocd_reg_dsr_w
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
Setting CPU %s is_boot_core to %d\n
result.ide ==NULL
write.dspsr_el0 NOT CACHED
General register 0
GetState
_is_halted
createCPU
astris_memap_debug_readbuf
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
tar
Choose a device: 
explore
Failed to allocate space for table!
{%s:%s@%d} [%s] Read DWT Comp %u\n
m_bp_details
EXPLORE_NOCLEAN
astris_findidcode
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Cause of last debug exception
ISP_R
Chip Revision: 0x%X\n
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
CPU has no regions, maybe powered off?\n
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
fn.ocd.debugcause.di.incorrect
Connected to Probe Map Server
Error Reading Device Production-Fusing\n
Instruction count level
Table 5–188
cpu_lacc_pc_status
cpu-dbgwrap-offset
AVD
no MEMAP access
DCS11
@AuthDbg,Ticket
UNKNOWN_PORTAL_ERROR
%s (%d)
virtual int ARMv7cpu_t::_resume_hw(bool)
PTEVADDR
dart-apf-address
{%s:%s@%d} m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX\n
{%s::%s} [%s] length=%u when width=%d
Using Built In CPUs\n
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
cpu_lacc_count_clear
addError
/socs
entry.exception_test_0
{%s:%s@%d} [%s] writing BVR %d\n
{%s::%s} [%s] %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
copyNicknameForPrimate
Level-1 exception PC
CTI_OUT_EN1
[%s] CPU BM Not Found, Bailing\n
ERROR: unable to resume translation for %s
AXdebug_auth_enable_timer_ovr
fn._setup_instr_bp.bp_state
fn._ocd_exec_instr.wsr.ddr.t2
fn._ocd_reg_r.ddr.value
cpu_readmem
%#09llx-%#09llx: %s\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armv7mcpu.cpp
AXcpu_writereg
api.is_prod.chip == NULL
{%s} already connected
GenericSchemaDocument
AXbooster_interface_create_cpu
--> misc_wdr   size=%3d wirtestporten=%d
{%s::%s@%d} [FALSE] CRm out of range [0x%08x]\n
   {%s} Clearing HNONSEC on AP \n
DEBUG_AUTH_REGS
{%s:%s@%d} [%s] reading CPSR(2)\n
{%s} category=%d
bpcr
{%s} Failed to single-step %s: %s
AXcpu_getmode
no error
m->name.IsString()
Booster Bundle: %s\n
{%s:%s@%d} [%s] moving DSB to GPR 0\n
%s construction failed
level_stack_.template Top<Level>()->inArray
CACHE
0
AXchip_get_board_variant
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
cpu-xtensa-num-wp
m_num_high_pri_interrupts=%u
fn.AXmemap_write.address.regval.
No MEMAP access while connecting to
cpu_readreg_vals
s.Peek() == '\\\"'
DSPSR_EL0
Failed to read reg_addr=0x%llx val=0x%llx
get_mair
Connection aborted: kick required to probe server. Received eof in stdin
astris_set_user_die_select
(data_.f.flags & kUint64Flag) != 0
failed write of 0x%08X to DEMCR - %s
AXcpu_detailed_status
{%s:%s@%d}\nFABRIC HANG DETECTED. JEBDUMP REQUIRED.\nContext: %s\nSoC: %s Rev: %s Address: 0x%016llx\nDescription: %s
ASTRIS_ERR_WAIT
{%s@%d} neither socket nor kext connection available
CPU Supported in Integration: %s\n
astris_batch_attitude_suspend
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
ASTRIS_ERR_TGTSTATE
STATUS
AXchip_get_chip_id
reset-network
DISP_L
Clear requests in INTERRUPT
fn._ocd_exec_instr.rfdd
too many of something
GenericStringRef
AuthBase_t::init failed (AuthDebug_t)
[1500] %s step %d: unknown instruction '%s'
wir-tdo
{%s:%s@%d} [%s] writing DTRRX(first)\n
[READ] cop64 %d -> 0x%016llx\n
JTAG
PARTNO_ARM7TDMI2
ASTRIS_ERR_BADHOST
\t[MATCH_FOUND] identified chip: %s
Img4DecodeGetPayload failed: %@
dbgarch
{%s} Thread %#llx key %lu attaching to info %p when already attached - IGNORED
{%s} halting %s\n
astris_preferences_cpu_monitor_list
kisHubLoc
cpu_getinfo
True
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
ret.reg.write.K_DA_REG_NAME_BOARDID
RF52
Shift-amount register
WrProt
DFR0_LO
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
UNKNOWN 
ret.a64cpu_raise_el_hw_safe
{%s:%s@%d} [%s] Setting WP length not currently supported: %u\n
m_wp_details
Register file 21
tap
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
Failed to write reg_addr=0x%llx val=0x%llx
Failed to read: ESR_EL%d
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
setCategoryValue
==== User Error Messages ====\n
DESIGNER_ARM
need_to_authenticate_helper
param.op.AXCPU_WP_ENABLE.unsupported
Probe %s Device Not Connected on USB-C Port
Failed to write JSON
JsonLogger: Wrote %zu bytes to '%s'
SWDFlashRead failed: 0x%08x
{%s} invalid data width %d bytes
Complex CPU ID: %d\n
Stop Clock: %s\n
~A
storeBoardName
param.cpu_reg_file_size.invalid.2
:
socs_supported
span
%s - runBlock
astris_cpu_status
ret.read.ecid
Table 5–184
RF57
APF
UserCreated
--> cmd        addrsize=%d datasize=%d
Cannot create CPU descriptions from NULL info\n
{%s::%s@%d [%s]} Error %s: collecting HW
EDRCR
op0: %d op1: %d CRn: %d CRm: %d op2: %d el: %d
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm7cpu.cpp
AXarm7_dbgread
copyBoardNameForKey
Failed to explore chip: %d
AXdebug_auth_authenticate
Vector Base
cpu_mmu_walk_detailed
device==IO_OBJECT_NULL
dlr_el0
ret.write_sysreg_hw.spsr_el
%s status is '%s'\n
New Length: %d\n
RF22
set.os
STM
[1500] TAP %d missing required field 'ir-cmds'
fn._read_special_reg.SRN_WindowBase
JTAG chain not yet explored
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
host_to_components
.user
CPU state %d
[1500] Error parsing v2 bridges
PowerOff
AMAuthInstallCreate
Table 5–158
param.reg_name.invalid
OS build version: %s
{%s::%s} [%s] error (%s) getting number of HW BPs
X09 Part
PrologueProperties
switch_regset
_clean_invalidate_dcache_vaddr
astris_cpu_mmu_get_config
Type 'jebdump' to do scan/mem dump\n
General register 14
Access Port
TGTSTAT
cpu-xtensa-options
result.read_vals(table_info)==
lower.safe.el=invalid
Register file 61
ASTRIS_ERR_BLOCKED
KIS translator version : %d\n
param.sys_addr == nullptr
Number too big to be stored in double.
match-info
AVE
hwwp_enable
fn._write_window_base.wb.wb_save
ASTRIS_ERR_ASYNC_BARRIER
vector
Should be run as root (uid = %d)
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_booster_api.cpp
channel
fn._ocd_exec_instr.TIECompleteRead
fn.entry
Unable to read SP
     0x%016llx: ERROR\n
AXdebug_auth_authenticate_probe
MAC16 data register 2
host_get_probematch
PongoSWD
{%s:%s@%d} [%s] unable to read command response\n
Got an error writing 0x%X the DCM Control Register: %s
We are in clean up\n
darts
wir-size
{%s:%s@%d} [%s] updating DFAR\n
{%s:%s@%d} [%s] doing IR scan (DSCR EXTEST)\n
ret.current_state_aarch64
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
astris_kis_cfg_writevals_swd
{%s:%s@%d} [%s] executing VMOVW\n
{%s} read ESR EL1|EL2|EL3 (%d)
AP[%d]: MEM_AP_AHB\n
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
{%s} Unrecognized Component: %08X (class %u)
read_settings
host_get_port
CPU at Index: %d has to specify only one AP Type or AP Select\n
virtual int CPU_t::collect(int)
internal.enable-test.chip->soc == NULL
Unable to connect after multiple attempts:\n%s,\n%s
failed to read consistent debug root register, fabric may be hung
GetSize() >= sizeof(T)
set.hostname
wir2-tdo
AUD
hwbp_insert
Waiting for previous in-flight authentication to finish\n
DEBUGCAUSE
R0
param.as.invalid.>15
Can't get hardware model - failed to get property
explore_pid_swd
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
RF55
fn._ocd_reg_r.DCR
fn._write_special_reg.dbreakc1
environment variable not found
INVCHIP
[1500] Error parsing bridge '%s': missing required field 'select'
%s constructed
{%s::%s} [%s] unsupported width %d
Sleep
{%s} unable to allocate probeInfo
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
/cpus
_a64cpu_encode_aarch64_add_imm
IOCFUnserializeWithSize returned non-dictionary of class: %@
CalibrationData
MMUV8
Going to do imago workaround\n
_write_special_reg
{%s:%s@%d} [%s] bad hostname\n
tdi-wsi
Can't get OS build version - failed to allocate buffer
UNKNOWN CODE
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
spsr_el3
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
EXPLORE_GENTLY
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_c_api.cpp
{%s} (end) current_el is now %d
Sprocket
NOP
{%s:%s@%d} [%s] getting GPR 0 (CPSR)\n
symbol.check.loaded.AMAuthInstallSupportDictionarySetInteger64Ptr == NULL
 (
Too many portals, we are at portal: %d while max is %d\n
entry.exception_test_1
{%s:%s@%d} [%s] setting GPR\n
internal.authenticate_probe.chip->soc == NULL
Table 5–157
LAM
AXconn_kis_get_stm_probename
AXcpu_status_pmgr
ASTRIS_ERR_CPUNOTHALTED
invalid command
astris_identify_load_booster
get
{%s::%s} EDSCR ERR (0x%X) while waiting for EDSCR ITE
AXdebug_auth_is_authenticated
_return_from_debug_interrupt
{%s} setting up nameless target (address=0x%llx)
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
/System/Library/PrivateFrameworks/MobileDevice.framework
Table 5–132
RF11
usb
APCIE_ANS0
result.extract_group_info==
WCR0_EL1+index
ExcCatch
MR3
%s.console.%s
host is going to sleep
PROBED_USB_REQ_ERROR
explore-level
AXexplore_enable_all_cpus
{%s} L2 cache operation completed [%s]
symbol.check.loaded.AMAuthInstallSsoEnablePtr == NULL
EPC1
Table 5–131
param.val.invalid.null
EDBVR0+index
PARTNO_1176JZFS
Table 5–162
MISC2
R7
options=0x%8.8X, #addr_bp=%u, #data_bp=%u,deb_int_lvl=%u
127.0.0.1
CortexA9
AXbooster_print_boosters_detailed
_status_hw
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
{%s=>%s} AXconn_t has no chips
fn._ocd_reg_dsr_w.dsr_status_to_clear
products_
ARM32cpu_t
required parameter is missing
RESPONSE_NO_PAYLOAD
RegionEnd
ret._a64cpu_read_gpr_cached
wb_u32=%u
cpu_writemem
{%s} no TAP detected that supports 1500
astris_ide_get_dbgwrap_base
_a64cpu_read_edscr_masked
index slot not enabled
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
fn._ocd_reg_dcr_clr.dcr_enable_ocd
ASTRIS_ERR_RESETTING
ASTRIS_ERR_MASKERR
ret._cleanup_hw
setCategoryValue: path='%.*s'
GetStringLength
Register file 63
## ARM32cpu_t::read_register %u\n
{%s} read[ED32] of %s @ address 0x%016llX ERROR %d(%s)
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
ret.switch_taps
CPU %s not found or already removed from the map
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
cpu_hwbp_insert
{%s} Failed to extract die infofrom table (%d); continuing anyway
Invalid file name: \"%s\". File names must be at least %d characters long.
[AstrisAsync] Resuming Async Mode\n
Switch back to primate KIS: %s\n
remote probe closed connection
SCANDEBUG
SPSR_EL2
*
Not Creating CPU: %s\n
cpu-die
Table 5–169
MMID
fn._ocd_exec_instr.wsr.ddr.t1.2
general error reported by probe
No portal under found for that type
addMember.user
%s: Didn't find client in dictionary
cpu-runtimes
value
ASC
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
{%s} ROMTABLE (nest=%d)\n
Invalid Size Given for AP AP=%d Size=%d
EXPLORE_DAPONLY
xtensa-non-tie-range-size
M = 0x%llX, S_UP = 0x%X, S_DOWN = 0x%X\n
copyNickname
AXcpu_read_dcc
{%s} Component ID read fail for 0x%llx (%s)
{%s} explore with exploreflags 0x%X complete [%d chip%s]
which_wp=%d
param.sr.invalid.>255
hardware error reported by probe
BitboxSWD
CPU3
[INIT]\n
EXCSAVE7
ASTRIS_ERR_BADPROTOCOL
{%s:%s@%d} [%s] {%s} port[%u] specification no longer supported\n
Old ProbeDaemon does not support this command
cpu_clean_l2cache
soc or sysap not available
EDWVR0+index
op_L16UI_encode
unable to transfer command to/from remote probe
AXconn_conndesc
{%s:%s@%d} [%s] updating ADFSR\n
WFI
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
No Success after retry on wait
connection created
Failed to create SoC or no booster
{%s:%s}: cpu powered off: unable to access a register for this CPU
astris_arm64cpu.cpp
{%s} status=%d being reported as Unknown
Table 5–186
fn._ocd_reg_r.dcrclr.regval_raw
Failed to write DCM GPIO (0x%x): 0x%x
--> extrawrstn %d
mempool-base
{%s:%s@%d} [%s] writing SPSR\n
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, %d, %d, true, %d)\n
RF19
Register file 56
Previously dumped the process tree, skipping
{%s:%s@%d} [%s] reading CPSR(1)\n
{%s:%s@%d} [%s] flushing state\n
Magic does not match: %#x vs %#x\n
RF37
ASTRIS_ERR_ANOMALY
Pop
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger.cpp
/\\
Could Not Get BoosterManager. Need To Call AXbooster_init\n
{%s} Error setting up memap target (%s)
Table 5–152
var.reg_srn.invalid.>=256
astris_get_dbgwrap_sys_addr
IsArray()
In Writeflash\n
dfu-type
%s (addr=0x%llx -> val: 0x%x)
ChimpSWD
{%s:%s@%d} [%s] moving COPROC reg to GPR 0\n
ret.init_params.raise_to_min
AXcpu_halt
Failed to read IDE through DAP\n
{%s:%s@%d} [%s] getting GPR 0 (switched)\n
OK: address translation resumed for %s successfully
Invalid object or key for addMember
Matched via Bundle ID\n
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
ret.nick.copyPairForPref
RF56
from != 0
param.dbgap  == NULL
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
AXcpu_lacc_count_clear
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
!!! Please File A Radar With macOS Sysdiagnose Against Component !!!:\n
ASTRIS_ERR_BADFIRMWARE
ASTRIS_ERR_NOBOARDINFO
block-unpiped-shift-wr-force2zero
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
/var/log/astrisclient
%s.%s
data_.o.size > 0
IONameMatch
symbol.check.loaded.AMAuthInstallSupportDictionarySetBooleanPtr == NULL
Table 5–159
IsObject()
Found another target for the plist\n
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
virtual int ARMv7mcpu_t::_halt_hw()
fn._ocd_reg_r.DDR
op_S32I_encode
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
basic_string
BoosterPublicAPI
Processor Id
HIFI3_1
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
USER
FirmwareOffset
AXdisassemble_at_phys_addr
chip == NULL
error trying to unlock MSR %s
_suspend_translation_hw
     ARM %s watchpoints: %u\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
EXPLORE_JTAGONLY
astris_user_default_copy_boardname_for_primate
INVMODE
Error %s connecting to server %s:%s [RETRYING]
memap_bus_write
x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx x%i:  0x%016llx\n
[AstrisAsync] collect_responses - cmd.cs_type: 0x%04X; cmd.cs_id: %d; resp.cs_id: %d; ret_val: %d; remaining: %zu
fn._ocd_reg_r.dsr.1
fn._init_configuration.w2.audio.HIFI3_2
Failed to convert CFString to C String.
[HALT] Chip %x\n
probetimeout retry failed logging as hang\n
Table 5–171
Probe Type (%d) FW Version: %s does not support KIS.
Connect
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_explore.cpp
_a64cpu_write_vfpreg_hw
ret._setup_bp
AXcpu_swbp_remove
PARTNO_HUGO
%s given a NULL conn object
{astris_probed_print_events_from_json} not supported in this build configuration
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
ret.ito.clear_edscr_err
{%s::%s@%d} [FALSE] dest_reg[%d] < 15\n
[AstrisAsync] Discarding %zu completed command(s)\n
ICOUNT
RF15
OUTEN_RESTART
AXconn_copy_nickname
Register file 16
We Are Matching Development Booster\n
ret.read.edscr.start
AXcpu_cache_info
## dpr 0x%02X failed (%s)\n
Invalid category name
LCC
{%s::%s} [%s] failed SW BP check [PA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
astris_apread
ret.clear_dft_authentication
internal.is_authenticated.chip == NULL
UNKNOWN_CS_CODE
SoC clocks are stopped. No MEMAPs allowed 
string_view::substr
%s
Register file 7
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
DESIGNER_APPL
symbol_array == NULL
astris_json_logger_init
Stepping Stone Final =  %#x\n
soc is NULL
{%s@%d} Probe response payload read when no payload indicated.
ARMV7EM
SBR
DCS_BC1
Early dbgwrap base extracted: 0x%llx\n
{%s:%s@%d} [%s] executing MCRR\n
Required Key-Value is a string, and not an array. Old booster found\n
Basic
Channel configuration missing
_get_el_implemented
fn._ocd_exec_instr.WSR.DDR.R1
probe matching %s on host %s
collect-probemap
Could Not Get Bundle Out Array of Found Boosters\n
L1CRT
_init_hw
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
dest_reg < 32 && dest_reg != 31
read back of modified data did not match
Table 5–176
Table 5–160
socnames
GFX
param.halt_group == NULL
gpr < 32
ret.home_url == NULL
shift=%d,opcode=0x%6.6X
Bug
{%s} host = %s
{%s}ERR: bypass_device_name is NULL\n
cpm-offset
!!!! Critical Error:  dspsr_el0 NOT DIRTY !!!!\n
DEMCR: 0x%08X -> 0x%08X
{%s} PRIMECELL [DONE]
Register file 58
fn._ocd_reg_w.ddr.address
data_reg=%u,opcode=0x%6.6X
SoC
[AstrisAsync][COMPARE] MISMATCH: cmdbuf - NULL buffer(s) with cmdlen=%d - acmd1->cmdbuf=%p, acmd2->cmdbuf=%p\n
AXcpu_lacc_status_insert
{%s} FAILURE - malloc error
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
addMember
M7
Table 5–155
(0x%08llX) %s
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
NotNullStrLen
astris_ide_get_pid
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
{%s:%s@%d} [%s] updating PC\n
fn._collect_snr.ps
MISC
diagnostic_checks
StringEqual
Valid Portal
Complex Address: 0x%llX\n
{%s::%s@%d} [FALSE] gpr[%d] < GPR_COUNT\n
Can't get hardware model - failed to create string
PropertyID
framework
{%s} exec: IC_IVAU_X1_ENC\n
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
{%s@%d} Unknown CS command error [%d]
AMCP0
!!!! Critical Error: batch attitude thread trying to lock - CAN'T LOCK !!!!\n
gor
no system bus AP present when expected
{%s} Extracted CIP Gen Number from table  (%d)
AXexplore_set_explicit_mode
ASTRIS_ERR_PROBETIMEOUT
Probe
cpu-explore-flag
_D
Unable to read GPR %d
hwwp_disable
astris_jtag_get_pipe_cycles
Instruction break 1 address
RF17
Register file 34
astris_ide_get_deid
regidx_restore=%u
INVPARM
cpu_cache_clean
ret.write_hang_breadcrumb
setProbeInfo
{%s} FIFO full, try again
!!!! Critical Error: !(prsr[0x%08X] & DLK) !!!!\n
MISC0
.hostname
Register file 44
SLEEPING
Kicking
Communication failure with probe server
{%s:%s@%d} [%s] moving reg to cop\n
!!!! Critical Error: el[%d] == m_exception_level[%d] !!!!\n
fn._tie_write_word32
probe %s on localhost
%s-%06X
CPU Typehint: %s\n
[ARM32cpu_t::_update_register64] 0x%08x\n
GLBEN
ret.read.msr_lock_reg
Failed to fetch if we are in ARM64 or AARCH32
Can't get OS build version - failed to get build version
Probe %s status: Idle
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
AXdp_write_with_recovery
PROBED_LOSTCONN
disable
ret.memap.write
   {%s} (DP): status=0x%X(%s) - %s\n
MEPS
Output
AddState
\n
Apple
{%s} %s status failed. error: %d (%s)
NC
AMAuthInstallSupportDictionarySetBoolean
{%s} strsep empty so match any probe [localhost]
addMember.engineer
{%s} Unable to read SP_EL0
Lowering from exception level[%d] other than 1, 2, 3 [%d]?
[AstrisAsync] Pause when already paused!\n
general-purpose failure
Explore flags indicate IDENTIFY_ONLY; bypassing _preinit_hw phase
ide_checker
ParseFalse
duration_ms
NRF
Die-Count: %d Current-Die: %d Die-Type: %d
A32
astris_dpread
RF41
_read_cpu_reg_file
fn._write_window_base
astris_select_probe
ret._release_gateway_control
JSON
x != 0
_set_wpaddr_hw
Invalid current AP (%d), adopting latest (%d)
astris_user_default_copy_nickname_for_primate
JTAG IN CONTROL
DCS_BC2
AXcpu_hwwp_enable
fn._ocd_reg_r.ddr.t1_save
fn._ocd_exec_instr.rsr.ddr.t1.1
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
Table 5–136
PORTAL_STS_OK
ParseNull
Could Not Find The Astris Init Function (%s) in %s
{%s} m_exception_level(%d) != current_el(%d)
hwwp_insert
param.no_dp
relay_set: %s -> %d
{%s} unaligned %d-byte access at address 0x%09llx
{%s:%s@%d} m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15\n
Delayed
remote probe is currently in use
fastsimSWD
PPM
{%s:%s@%d} [%s] checking for data abort\n
ITO
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
astris_jtag_set_pipe_cycles
ret.m_lam.paccess_read
/System/Library/CoreServices/SystemVersion.plist
PlayerSWD
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
config.invalid.no_window_reg_option
Missing a colon after a name of object member.
Encode
ret.storeNicknameForKey
param.chip->conn == NULL
param.info.invalid.null
ASTRIS_ERR_USB_PROBED
{%s} NOMEM
kob
Unknown error.
Turning Debug Clock On
param.num_data_bp_regs.invalid.2
var.m_debug_interrupt_level.invalid.outofrange
complex-cpu-id
ret.read.stepping_stone
baseReg
got a translation error translating VA to PA
Register file 51
fn._collect_snr.exccause
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
complex-name
AXcpu_readreg
COMPARE2
type_hw=%d
kis_stm_name %s %d
da_base == 0
Optional Key: CPUMonitor not in preferences
Standard
{%s} flags:0x%08x
Failed to find member after adding to document
Could Not Allocate Mutable Dictionary For BoosterMangers
DCS13
AXarm7_dbgscan
Error status from AMAuthInstallSsoEnablePtr = %i
RELAY
PAM
BT_MAC
param.tgt->ap->dp.null
DCRCLR
probe matching %s on localhost
astris_err_from_cs_type
Misc_CortexM
CPU2
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
AXJTAG_EXPLORE_SEP_NOPWRGATE
???
fn._read_special_reg
astris_write_hang_crumb
%s at offset %zu
{%s::%s} [%s] MMU is already active - returning %s
Booster:\n
failed to read memory; can't confirm breakpoint set
_remove_breakpoint
Parameter len = %d > 64.
op_S16I_encode
probe [port %u] on localhost
?
is.Peek() == '{'
We are at max iterations, still didnt get full JSON
astris_ide_get_bootid
_a64cpu_lower_el_hw
ret.CFURLCreateCopyAppendingPathComponent
length=%u, width=%d
DLOPEN ERROR: %s \n
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
internal.enable-timer-ovr.chip->soc == NULL
query_events
 
SAM2
[%s] %s
DCS_BC6
_read_mem
ret.clear.async
AXjtag_srst deassert failure - %s (%d)
Wat!: 0x%llx
[%s] error reading EDSCR
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
ret._a64cpu_lower_el_hw_safe
ret._set_wpaddr_hw
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Invalid instruction breakpoint index %d
Firmware image read from device
!!!! Complex Key %s is INVALID !!!!\n
result.read_vals(portal_group)==
result.offset_from_content== -1
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
PROBED_USB_NOTOPEN
JsonLogger: Loading schema for category '%.*s' from '%s'
{%s::%s} Timed out trying to clear EDSCR.TXFULL (dscr = 0x%08X). Continuing.\n
EPS2
m >= MemberBegin() && m < MemberEnd()
Dart Coastguarded CPU: %s\n
astris_batch_attitude_detach
{%s:%s@%d} [%s] reading CCSIDR[L1-D]\n
{%s} Failed to resume %s: %s
kext connect name %s\n
TRST
Passed NULL booster without custom plist\n
{%s} explore with exploreflags 0x%X completed with error [%s]
Xtensa Option ocd_address: 0x%llx
Missing a name for object member.
astris_batch_attitude_lose
Call-window start bits
Error %d (%s) opening history save file
ENUM
cpu-subsystem
ASTRIS_ERR_INVAL
param.chip.soc == NULL
SMX
{%s} exec: DC_CIVAC_X1_ENC\n
RF40
Enabled
Register file 12
CPU Core Number: %i\n
param.ticket_data == NULL
HTTP transaction running in background
ObjectEmpty
sib-network-wrstn-reset
FAR_EL2
astris_apwrite
ret.reg.write.K_DA_REG_NAME_NONCE_2
%d%s
stack.h
chip-index
DOCK-CH-DATA
[%s] {%s->%s} END handling exception
messages
Banana split probe, for now I guess we will just say yes...\n
ret.exec.msr.scratch->mddtr
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
ret.reg.read.K_PKA_REG_NAME_DBG_VERSION
FirmwareOverride
[1500] Detected plist version %d
[!ARM64] exec(DCPSX_BASE_ENC)
DDR
astris_batch_attitude_attach
astris_clear_user_die_select
calOverrides[%@] isn't an NSData: %@
Register file 40
UNKNOWN_KIS_ERROR
%s %s\n
required_el > _a64cpu_get_highest_el()
Table 5–151
Register file 6
Specified host %s did not resolve to valid host
Failed to find a product plist for this soc %s
Die Config Disabled\n
EDWXVR0+index
DEDICATED
default
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
RemoveMember
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
fn._ocd_exec_instr.l8ui.r1.r0
Error %d (%s) while expanding ~ for Astris log file base\n
ret.astris_soc_get_applesoc
Cached async_replay capability version: %u
Dart Name: %s\n
{%s} Thread %#llx clearing key %lu
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
EPS4
{%s} probe_port = %d
deleteClientFromList
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
EDDTRRX
{%s} exec: DRPS_ENC\n
ret.reg.write.K_DA_REG_NAME_ENABLE_PKA_VALID
fn._ocd_reg_w.ddr.regval_save
coredump
[%s] Executing instruction=%llx
[Auth Debug] External Debug Interfaces Open\n
cpu_sstep
{%s:%s@%d} [%s] getting GPR (diff mode)\n
## ARM32cpu_t::read_register 64 bit 0x%x\n
read.dspsr_el0 NOT CACHED
Error happened when reading edscr. Retry #%i\n
astris_user_default_set_nickname_for_key
Async is disabled for current seesion
AXlog_init_with_ctx: lock could not be obtained
CPU disabled by SW, not accessable
CFG
ret.nonce_generation.timedout
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
{%s} probe_host = %s
{%s} %s: |%s|-|%s|
xfer_acmd_via_sock
Passed NULL plist file\n
L1_DATA
Key initialization for oslog API failed! %s\n
Initial DSPSR_EL0: 0x%llx
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Register file 47
which_bp=%d
Portal Status, Changing STATUS and CMD/STAT to reflect
AMCNP
M33
SOC_t::{%s} Attempting to perform a bus write outside of safe area on an aponly explore (addr: 0x%llx select: %d)
setTargetOS
get_soc_resource_filepath
AMAuthInstallSsoEnable
CCOUNT
M2
=== Starting Gather and Clear ===
Can't find descriptor for group - can't index\n
OUTEN_DBG
Switch to primate res: %s\n
fn._ocd_exec_instr.xsr.ddr.t1.1
{%s} probe device server closed the connection while trying to read data (at recv)
.astris_version
reading address: 0x%llx
EXPLORE_WITH_DISPLAY
CPUMonitor
RF25
par
FlamingoSWD
SLEEPCTL
Connection is NULL, might not have found something to connect to.\n
UNKNOWN CMD
Could Not Find Booster Entry Function: %s\n
dpb-tpser-id
KF-ETM
Exception occured after executing MSR to write into sysreg
base_reg < 32
astris_json_logger_to_json_string
dart-coastguarded-cpu
misc-wirtestporten
AXcpu_readmem
Register file 53
fn._write_general_reg
ret.astris_set_user_die_select.astris_soc_get_applesoc
tokens_ == 0
xtensa-non-tie-range-name
{%s:%s@%d} [%s] reading PRSR (lsr)\n
GRP_0
_is_bpwp_initialized
fn._write_mem.length.incorrect
CreateParallelValidator
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
INTCLEAR
CSPDATA
!!!! Critical Error: Error %d(%s) destroying info %p cmdmutex !!!!\n
{%s:%s@%d} [%s] reading OSLSR\n
internal.get-timer-count.debut_auth == NULL
fn._ocd_exec_instr.TIEWriteProtectedI
Skipping CPU %s at 0x%llx: not present in IDE\n
After powerup CMDSTAT=%08X\n
{%s:%s@%d} [%s] executing MSR (switched)\n
[AstrisAsync] Async mode %s
LBEG
Memory error check register
{%s@%d} Probe reported connection lost [PROBEEOF].
read_via_sock
cpu-aptype
param.m_ap == NULL && param.m_lam == NULL
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
MISC3
no data when data expected
[KIS] Words (Read/Write/Wrote): %d\n
ret._a64cpu_read_sysreg_hw.hcr_el2
AXjtag_transmitraw
_ocd_reg_w
SkipProperties
ARMv7mcpu_t
      Read of JTAG-AP port %u CSW failed with %s\n
param.op.AXCPU_WP_DISABLE.unsupported
[KIS] CMD: %s \n
Gathered Value is Not Number\n
Dock-Channels
ret.read.edscr.masked.beginning
ONEWIRE
{%s:%s@%d} [%s] executing MSR\n
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
Unable to read GPR 28
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
pointer.h
{%s:%s@%d} [%s] executing MRRC\n
SCTLR__ELx
M4
   MEM-AP not enabled\n
{%s} found single_port probedaemon on port %d
EPIREAD
AXbooster_interface_create_soc
{%s} handle ROM entry
AXjtagap_explore
Invalid num_regs = %u. Should be 16, 32, or 64.
reg.ocd.dsr.stopped.invalid.cpu_running
dtoa.h
dr ->
SCS
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s->%s} TGE is set, can't raise to EL1
]
{%s} Failed to get breakpoint count for %s: %s
EPC6
EndArray
mxwrap-address
Level-1 exception save location
Awaiting response from Probe Map Server
i32toa
Failed to get cal data for %@
read.sysreg.el_check
low
Instruction break 0 address
ConsistDbg
Connecting to server, %s:%d
REG
gmtime() returned NULL, using epoch time
     0x%016llx: 0x%08x    %s\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s} 0 words from probe when %d words left to read for address 0x%016llX
debug_info
TRANSLATION_ERR_L3
INIT
CPU ASC Offset: %d\n
xres = %p, table = %p, key = %d
COMMIT
gpr=%d
CPU.ARM
ClassName
result.read_vals(group_info)==
_memory_set_base
ASTRIS_ERR_EMPTY
{%s:%s@%d} [%s] unable to drain response\n
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
Need to be connected to set nickname
Table 5–165
info
cpu_status
outCount != 0
complex-cpu-name
Board ID: 0x%X\n
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_armdap.cpp
CPU with %s Not Created via Name
Tarsier
L2 unified cache
astris_preferences_subsystem_monitor_list
fn.params
Target is not a JSON object
Failed to convert %s key @ index %d
copyBoardNameForPrimate
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
addr=0x%8.8X, index=%d, size=%u, flags=%udata=%u, enabled=%u
param.shift.invalid.out_of_range
s0=%d,ar=%d
%s v%s%s [%s]
connection about to be destroyed
INVALID 
!!!! Critical Error: current_el[%d] <  %d !!!!\n
{%s::%s@%d} [FALSE] src_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
CPU_t
%s%s\n
!!!! Critical Error: (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0 !!!!\n
is_external_open
Category name is null
Failed to execute DRPS, in order to restore PSTATE after exception
_invalidate_icache_all
get_page_shift
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
Memory error virtual addr register
fn._write_special_reg.ibreaka0.address
param.bp_info.invalid.null
PMU: 
CTI_INT_ACK
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
fn._ocd_reg_dcr_set.dcr_enable_ocd
probe
Invalid port provided by probe server
Port
AXbreadcrumbs_read
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
Asked To Read A Negative Register Index
DWT
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
fn._remove_data_breakpoint.which_wp
%s/Library/Logs/Astris
Generic
fc_retries=%d
General register 4
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
   Debug Port: SELECT %X; error: %s, retrying..\n
Kick off the current process using probe %s? (y|n)\n
VERSION
astris_batch_attitude_destroy
AXjtag_spixact
instance
Failed to populate portal info
ret.restore_el.read
n't
%02d:%02d:%02d:%06ld|%s <%s> %s
=== Ending Gather and Clear ===
ASTRIS_ERR_MISSINGPARAM
Created Connection - : %s
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
{%s:%s@%d} [%s] doing IR scan (DIDR SCAN_N)\n
failed read from DEMCR - %s
{%s} _pre_resume_hw result = %s
authenticate
Requires OCD option for >1 data breakpoint regs.
reg_srn=%u, \"%s\", regval=0x%8.8X
%s probe[*] from Probe Map Server [local host]
using standard products.plist for %s
param.reg_index.invalid
_setup_data_bp
wrstn-reg
write.dlr_el0 NOT CACHED
internal.authenticate.chip == NULL
Too many open files
{%s@%d} Unable to create socket
cpu_cleaninv_l2cache
imgExtractPersonalities failed
preflash routine returned error
ret.dbgap.memap_write
generate_nonce_and_send_request
Register file 3
Register file 31
RF60
_insert_instr_breakpoint
{%s->%s} EL2 not implemented
%-16s
AXcpu_resume
fn._insert_instr_breakpoint.address
writeToFile
Eval
IDE
Failed to sync prefs at end
Explore: %u chip%s\n
End
Probe %s LocationID Info is %s
{%s:%s@%d} [%s] doing JTAG scan\n
ret.read.gpr_0
R
init.m_symbol_table == NULL
Data break 1 address
_setup_instr_bp
[KIS] Register Read/Write/Wrote: %d\n
AXbooster_get_all_boostermanagers
write_register
Buffer is NULL
The log file has been updated with all available diagnostics.\n
ASTRIS_ERR_USB_EXPIRED
Invalid hostname or port specified as
{%s} error %d(%s) reading data from the connection (at recv)
\t[MATCH_TARGETID] FAIL <= unable to find DP
PORTAL ERR PENDING
{%s:%s@%d} Critical error [radar already requested]
CortexM33
0 == level_stack_.template Top<Level>()->valueCount % 2
pointer.IsValid()
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s:%s@%d} [%s] doing IR scan (DSCR SCAN_N)\n
!!!! Critical Error: {%s->%s} EL3 not implemented !!!!\n
unable to write memory (using system ap)
astris_cpu_mmu_configure
internal.is_dft_authenticated.chip == NULL
fn._ocd_exec_instr.rsr.ddr.t1.2
sending request
CalibrationSkip
ENABLED
Can't get OS build version - failed to open ReadStream
invalid parameter
Creating CPU Returned: %s\n
.
complex-cpus
dart-type
## apr %u 0x%08X %d -> 0x%08X ...\n
PortBridgeSWD
file
EpilogueProperties
b
bits
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
internal.is_probe_authenticated.chip == NULL
parameter val is NULL
MINISWD
IsString()
[AstrisAsync] replay preflight: Async not active!\n
{%s} calling _collect_hw on %s
AXcpu_abandon
Register file 13
!!!! Critical Error: Restoring from exception level[%d] other than 1,2 or 3 !!!!\n
_a64cpu_msr_mrs_encoding_for_sysreg_id
wait_inflight_auth
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
BP
couldn't read TTBR0
mmu_init
cpu_collect
{%s:%s@%d} [%s] setting DTR MODE to FAST\n
EL2h
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
AXcpu_hwwp_remove
fn.is_halted.setup_bp
AXconn_identify_soc_collateral
Creating ADI Flasher\n
{%s:%s@%d} [%s] executing MCR\n
{%s->%s} exec: encode_mov_vfp_to_gpr(scratch=%d, sysreg=0x%X, %d)\n
param.tgt->ap->dp->chip.null
HWERR
RF47
unable to obtain sysap
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
Error occured during nonce command
fn._read_snr.exccause
Creating Nordic Flasher\n
AXbooster_print_all_booster_managers
_rw_preflight
Unable to read PC
nothing written
```
