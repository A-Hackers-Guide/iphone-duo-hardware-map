# `/usr/local/share/astris/boosterpack/swdflashers/arm_adi_swdflasher.booster/arm_adi_swdflasher`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,751,600 bytes.

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
AXarm7_dbgread
at 0x%llx
R0
param.info.invalid.null
ARM7
_clean_invalidate_dcache_vaddr
\nPKA Command Verify Error In Check-Response (status = 0x%08x, should be 0)\n
required parameter is missing
pnav_create_probelist
{%s@%d} gethostbyname failed, error=%d (%s)
Missing a closing quotation mark in string.
Koko probe, for now I guess we will just say yes...\n
hwbp_disable
fn._write_special_reg.ibreaka1.address
MEMAP_APB
{%s:%s@%d} [%s] executing STCpi\n
write.dlr_el0 NOT DIRTY
RXO
dropping empty probeInfo (port=%u)
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
createCPUPlaceholder
cpu_swbp_info
fn._ocd_exec_instr.rsr.ddr.t1
BoosterPublicAPI
Required Key-Value is a string, and not an array. Old booster found\n
!!!! Critical Error: m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15 !!!!\n
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
fn._ocd_reg_r.DDR
pnav_single_port_req_rsp_probemap: could not allocate probe-relay buffer
astris_command_async
{%s:%s@%d} [%s] setting DTR MODE to STALL\n
RF24
*
%s (%d)
PongoSWD
received %zd bytes from Probe Map Server when have %zu
MMX
MISC1
Low level
CreateParallelValidator
{%s::%s} [%s] error %s writing SCTLR_ELx
AP[%d]: MEM_AP_AHB\n
MR3
_remove_watchpoint
fn._ocd_exec_instr.wsr.ddr.t1
AXJTAG_EXPLORE_SEP_NOPWRGATE
FEECON 
LBEG
Component is not present
{%s} empty response string provided
ret._setup_bp
AuthDbg,EnAppleDebugExternal
astris_setup_placeholder
Optional Key: CPUMonitor not in preferences
param.regval.null
AXjtagap_explore
param.m_ap == NULL && param.m_lam == NULL
WindowBase
Error
{%s} unmodified-probe_match = %s
ret.buildCategoryJson
AXbooster_refresh
complex-type
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
High level 7 exception PC
ASTRIS_ERR_PROBED
ret.production_emulation
ObjectEmpty
param.chip->conn == NULL
ret._a64cpu_read_sysreg_hw
astris_dpwrite
ASTRIS_ERR_PROBEEOF
CortexA8
TAP IDCODE: 0x%X\n
BCR0_EL1+index
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
Error status from AMAuthInstallSsoEnablePtr = %i
AXdebug_auth_authenticate_dft
Register file 44
GitHashDebug
authenticate
ret.reg.write.K_PKA_REG_NAME_DBG_CMD
Exc Cause: 0x%x - Exc Vaddr: 0x%x
End
CPU is not halted
{%s} hostname:%s, flags:0x%08x
Connected to Probe Device Server [Log File %s]
{%s} %sing word #%d at address 0x%09llx: %s
AXJTAG_EXPLORE_FC_JTAGAP
Memory error PS register
Probe %s with unknown kick response %s
TLR
MAIN_DEBUG_ROM
R14
RF14
reg_name (\"%s\") not implemented, missing Xtensa option.
from != 0
NUB
KF-ETM
AXcpu_readmem
{%s} Debug Base: %08X
Loop-end address
RF40
RF55
OCD Debug data register
newpos <= pathpos
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
astris_apwrite
is_ecid_zero
fn._ocd_exec_instr.WSR.DDR.R1
Generated JSON (first 500 chars):\n%.500s%s
spsr_el2
MSR
astris_user_default_set_nickname
astris_json_logger_to_json_string
ret.clear.edscr-error
sso_user.sso_user == NULL
%02u:%02u:%02u:%06u|%s <%s> %s\n
Probe Map Server Information: %s
Invalid port[%s] for probe %s provided by probe server
DEMCR write failure - %s (%d)
DISP_R
AXexplore_enable_cpu_pattern
Register file 26
Complex Type: %s\n
Die-Count: %d Current-Die: %d Die-Type: %d\n
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
{%s:%s@%d} [%s] executing MRC\n
(system_reg & (0x40000000 | 0x80000000)) != 0
    %s(): %s
~INTDIS
got a translation error translating VA to PA
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
#KIS
start
createSOC
AXportal_dfu_dcm
cleanup_astris_api
set_or_replace
M4
wait_inflight_auth
param.op.invalid.outofrange
Miss exponent in number.
, 
chip == NULL
Failed to sync prefs at beginning
framework_url == NULL
PROBED_USB_REQ_NODEVICE
%d%s
2: ARM64_SYSOP_ATS12E1W\n
DBGCTRL = %08X   res=%d\n
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
internal.is_dft_authenticated.chip->soc == NULL
Table 5–152
Before astris_kis_init_dp, CMDSTAT=%08X\n
class_var.m_interface_name==NULL
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
fn._init_configuration.w2.audio.HIFI3_1
regval is NULL.
info
Probe %s Device Does Not Have LocationID
CortexM3
ERR: conn->nchips != 0; looks like chip is explored\n
Misc register 2
Koko
KIS_DOCK
ir-cmds
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
{%s=>%s} AXconn_t has no SoC object
{%s@%d} Unable to allocate drain payload buffer of %d bytes.
setCategoryValue: path='%.*s'
passed
Target is not a JSON object
Could Not Get BoosterManager. Need To Call AXbooster_init\n
fn._write_special_reg.dbreaka1.address
relay_set: %s = CMD_ERR (%s)
read_via_sock
Init dbgwrap obj failed
WFI
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
sso_user.sso_data == NULL
MISC
stack_.GetSize() == sizeof(ValueType)
Failed To Init Booster's Astris API In: %s with %s (%d)\n
{%s:%s@%d} [%s] executing VMOVW\n
Failed to exec MRS to bounce sysreg into scratch register. scratch=%d, sysreg=0x%X, regname=%s
{%s:%s@%d} [%s] Read DWT Comp %u\n
Loop-begin address
Kick error while communicating with probe server
Init objects failed
[MEM] Uncompleted; DSCR = %08x\n
Error - reflash failed.\n
THREADPTR
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
Primate-Hub-Null
Could Not Create Dictionary From Booster: %s
Failed to get DFU Type
{%s::%s@%d} [FALSE] val[0x%08llX] < UINT32_MAX\n
{%s} ROMTABLE (nest=%d)\n
astris_clear_user_die_select
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
AMAuthInstallLogSetHandler
fn.AXmemap_write.address.regval.
setAddress
ParseTrue
static_cast<void*>(this) != static_cast<void const*>(&rhs)
products
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
%s @ 0x%08llX : 0x%08X/n
setup_wp.not_halted
armv7m-region-range
Previously dumped the process tree, skipping
IsObject()
MemberCount
{%s:%s@%d} [%s] reading DFAR\n
EL3h
CPU.ARMv7m%s
M23
DBREAKC1
target is probably resetting
AXexplore_enable_cpu
[ARCH32] Failed to write transfer register (EDDTRTX) the value to write
COHERENT
{%s} Class 9 ROMTABLE (nest=%d)\n
Table 5–170
.start_time
probetimeout retry failed logging as hang\n
symbol.check.loaded.AMAuthInstallLogSetHandlerPtr == NULL
Fault Error on Run-SWD Subcommand
!*!*!* Please make sure cable is plugged into the target with the arrows on           !*!*!*
Cannot create SoC [unknown chip identity (%d)]
hwbp_remove
EPS4
JTAG level control
operandStack.GetSize() >= sizeof(Frag)
SWDFlash
misc-size
{%s} Failed to get watchpoint count for %s: %s
AXcpu_lacc_pipe_set
Debug Port
kisHubLoc
ARMV6M
Board ID: 0x%X\n
astris_cpu_get_cl4_debug_signpost
astris_dump_exploreflags
probe [port %u] on host %s
_is_halted
%s (addr=0x%llx)
Dart Base Address: 0x%llX\n
Stop Clock: %s\n
{%s::%s@%d} [FALSE] instr[0x%08X] & MSR_MRS_BASE_MASK == 0\n
CSE
da_base == 0
Misc register 0
Register file 57
INVPARM
aod_type
%s%s\n
exit.exception_test_2
INVALID
internal_dft.is_authenticated.debug_auth == NULL
AMAuthInstallSsoInitialize
PROBED_USB_NOTOPEN
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
CPU Supported in Runtime: %s\n
fn.exit ERROR
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
{%s:%s@%d} [%s] FEECON read failed: %s\n
EXPLORE_APONLY
MISC3
Beginning of set
Category name is null
appendToArray.error
!!!! Critical Error: current_el[%d] <  %d !!!!\n
diyfp.h
sdom
PRORES
fn._ocd_reg_dsr_w.dsr_status_to_clear
Failed to convert primateHubLoc %s to unsigned long long
GetString
ret.state_valid_entry_exit
[INS_HWBP] bp%d bvr=%016llx bcr=%08x\n
Halt
internal.clear-auth.chip->soc == NULL
FEESET 
End of set
explore-level
ret.test1
Mask condition met in conditional operation
getOrCreateValue
getOrCreateArray
!!!! Complex CPU Key %s is INVALID !!!!\n
Failed to get Bypass Config
PMS
   --> IDR: %08X\n
ASTRIS_ERR_HTTP_FAILURE
Logger is null
i32toa
itoa.h
STM
CS-CTI
ret.test.2.1
{%s:%s@%d} [%s] doing IR scan\n
{%s::%s@%d [%s]} Error %s: checking exception
[%s] error  reading EDSCR
ret.clear_dft_authentication
M3
Failed explore before forced KIS reset: %s\n
write_memory_dbgwrap
Table 5–149
????
Connection to server accepted
elr_el1
RF9
Xtensa Option reg_file_size: %d
fn._ocd_exec_instr.xsr.ddr.t1.2
AXchip_dock_disconnect_mode
ide_checker
{%s:%s@%d} [%s] getting GPR (diff mode)\n
_a64cpu_write_gpr_cached
_a64cpu_assert_state_valid_entry_exit
Register file 7
ASTRIS_ERR_ASYNCSKIP
%d:%d%s
DLOPEN ERROR: %s \n
internal.get-timer-count.chip == NULL
Subsystem Monitor[%i]: %s\n
Call-window start bits
var.num_loops.invalid.>3.prev_instr
Probe %s removed before port determined\n
USER
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
device
ADI
chip->ide_table == NULL
AXarm7_dbgscan
DEBUG CLOCK OFF
SoC
Too many portals, we are at portal: %d while max is %d\n
symbol.check.loaded.AMAuthInstallSetSigningServerURLPtr == NULL
Connection aborted while choosing probe
exploreCPU
virtual_memory_bytes
USER %s(%04u): %s(): %s
{%s::%s} [%s] !bpwp_initted, retrying init
fn._ocd_reg_r
{%s} host name(RSD): %s\n
localhost with name matching %s
Could Not Find Any Boosters of Type: %s\n
ITO
astris_user_default_copy_nickname
Kick has been requested by probe server
{%s} no chip found
{%s:%s@%d} [%s] writing WCR %d\n
write_memblock_dbgwrap
val.check.content
!!!! Critical Error: current_el[%d] == 1|2|3 !!!!\n
AuthDbg,Ticket
Table 5–157
cpu_hwwp_disable
ret.clearing-async
fn._ocd_exec_instr.rsr.ddr.r0_r12
Failed to create CPU %s - %s\n
regex.h
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
Error %d(%s) executing instruction 0x%08X FAST
ECID
{%s} bridge returned SLVERR
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
ASTRIS_ERR_VARNOTFOUND
failed to read consistent debug root register, fabric may be hung
ret.astris_ide_get_dbgwrap_base
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
{%s::%s} [%s] BP_DISABLE _set_bpwp[%d] failed (%s)
ApSecurityMode
HIFI3_1
Connection aborted: kick required by probe server
buf != 0
Cannot create DART descriptions from NULL info\n
UWB
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
_write_cpu_reg_file
LCDCTL
   Created Fake Debug Port Debug Port
RF43
protocol version is too old
BananaSplit
getOrCreateObject.messages
Extract Offset: 0x%X for %d\n
[Auth Debug] Disabled\n
ret.authdebug.is_prod
fn._ocd_exec_instr.rsr.2
_remove_data_breakpoint
PROBED_LOSTCONN
Astris-%d.%d~%d
Connected toProbe Map Server (single_port) 
Booster Value is Not String\n
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
param.length.invalid.null
astris_select_probe
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
ChimpSWD
ISP_R
{%s:%s@%d} [%s] executing MRS\n
Another application is connected to
MemberEnd
set_gpr
RF16
fn._reg_desc_lookup_by_name
fn._ocd_exec_instr.rsr.reg_srn.t1
ACQ_SAMPLE_I2C
set.target_os
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
_write_memory_fast
internal.is_probe_authenticated.chip == NULL
probed
process (%s) (%d) path: %s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
PAYLOAD_OVERFLOW
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
dart-name
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
cpu_translate_par
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Took an exception in EL%u, esr = 0x%08llx, category = 0x%llx\n
base_reg < 32
{%s:%s@%d} [%s] writing CSSELR[L1-D]\n
{%s:%s@%d} [%s] program failed: %s\n
%s.console.%s
ARMV4
wrstn-partition-number
After powerup CMDSTAT=%08X\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_explore.cpp
_get_num_hwwp_hw
ret.reg.write.K_DA_REG_NAME_AUTH_KEEP_DECISION
fn._ocd_reg_r.OCD.DEVID
op_DSYNC_encode
/socs
cpu-die
read.dlr_el0 NOT CACHED
{%s} Create CPU placeholder at 0x%llx (name=%s, arch=0x%X, ID=0x%X)
EXPLORE_DAPONLY
_set_single_step
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
   Debug base is in legacy format\n
PARTNO_SWDP_SOC600
param.as.invalid.>15
invalid command
Successfully connected to
ARMDAP
SCANDEBUG
first read of CMDSTAT may fail if external reset occurred
ret.reg.read.K_DA_REG_NAME_SECURE_MODE
ret.nonce_generation.timedout
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
backtrace
  Error path [%s]\n
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
cpu-name
_status_hw
{%s:%s@%d} [%s] getting GPR 0 (COP)\n
## armcpu: bad status even though all bytes read (%d)\n
Update
engineer
dtoa.h
ITM
ENABLED
{%s} explore with exploreflags 0x%X complete [%d chip%s]
fn._write_window_base.wb_save
Exception
RF50
param.reg_name.!match
cpu not halted
%s given a NULL conn object
socnames
[Partnum] Values Not The Type We Expected. Expected: Number and Array\n
ret.read.edscr.masked.beginning
Lowering exception in AARCH32 Mode NOT SUPPORTED
%-16s
MAX_KISSWD
MSP
intack
Connected
General register 10
Long Packet
var.reg_srn.invalid.>=256
AXexplore_enable_all_cpus
{%s::%s} ERROR %d(%s) pre_resuming %s\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
fn.is_halted.setup_bp
%s.console
stackTop_
_
ret._a64cpu_read_gpr_cached
AXcpu_lacc_count_read
{%s=>%s} AXconn_t has more than one chip
reset_connect_state
sending abort to clear a timeout\n
{%s:%s@%d} [%s] doing IR scan (DTRTX INTEST)\n
messages
Die Addr Info LSB: %d Mask: 0x%016llX\n
{%s} [%s] EDSCR with ITO set - unable to recover.\n
Invalid Size Given for AP AP=%d Size=%d
!!!! Cannot explore via Buttercup. Only relay commands and Reset can be passed to it. Try to connect by selecting KIS instead of Buttercup !!!!\n
fn._setup_instr_bp.bp_state
performing direct connect by port number
MiscCortex_t
Key is null
BP
partnum
Requesting %u > 4 while address is NOT doubleword aligned
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_armdap.cpp
cpu_collect
ParseString
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
CDPDL
!!!! Critical Error: batch attitude cannot be suspended when checking usage !!!!\n
Unknown
{%s:%s@%d} [%s] timeout waiting for cmd idle\n
_%04d-%02d-%02d_%02d.%02d.%02d
AXI-ERROR=0x%X - AXI-XACTION-FLAG=0x%X - ADDRESS=0x%llX
connection created
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
DISP_L
DWT
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
before_deactivate_in_runBlock
HIFI3_2
ret.fromreset
AXchip_production_emulation_enable
{%s:%s@%d} [%s] setting DTR MODE to FAST\n
param.addr_reg.invalid.>15
{%s} connectName[%s]
We are at max iterations, still didnt get full JSON
PARTNO_SWDP_M0P2
fn._ocd_exec_instr.wsr.reg_srn.r0
op_TIEWriteProtectedI_encode
SCAN
We are Allocating\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
AXcpu_translate_with_dart
astris_memap_lmflash
SWD
enable_test
fn.unsupoorted
_set_bpwp
!!!! Critical Error: Nested exceptions... get someone to debug this. !!!!\n
fn._ocd_exec_instr.TIEInitiateReadProtectedI
ERROR!! Couldn't save %s binary data\n
cpu_mmu_get_tsz
cpu_lacc_bp_status
addMember.engineer.message
!level_stack_.template Top<Level>()->inArray
[READ] %d -> %08x\n
ret.reg.write.K_PKA_REG_NAME_DBG_INPUT_START
param.regval.invalid.null
Warning: Default logging location requested when running as root (using [%s])\n
Corruption detected selecting probe from probe server
R9
{\"max_events\":%u,\"events\":[%s]}
dart-cpu-sid
master-debug
far_el3
AXcpu_writemem_width
ret.reg.write.K_DA_REG_NAME_ECID0
fn._ocd_reg_w.DIR0EXEC.instr_32
AXcpu_hwwp_enable
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
Misc_NoSoC
...
AXbooster_print_boosters
KIS-Null
probeBoardNames
: [
## dpr 0x%02X -> 0x%08X\n
Unaligned Read @ 0x%llx Width: %d Bytes: %d
{%s:%s@%d} [%s] FEEADR1 write failed: %s\n
{%s:%s@%d} m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15\n
result.alloc_table==NULL
astris_explore_enabler_add_cpu
darts
AP[%d]: unknown type\n
_read_reg
_a64cpu_raise_el_hw_safe
[Chipnames] Values Not The Type We Expected. Expected: String and Array\n
preconnect
from
ACQ_SAMPLE_SPI
cleanup
function
RTP
Unable to read LR
## apw %u 0x%08X 0x%08X ...(%d)\n
_return_from_debug_interrupt
(%s) %s
ARMV8
ret.astris_set_user_die_select.astris_soc_get_applesoc
u64toa
[ANAMOLY] Could not find AXcpu_t object for CPU\n
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
PKA Base: 0x%llX\n
Interrupt enable bits
{%s} Found extra info in = %s, chopping string
{%s@%d} Unable to create socket
operandStack.GetSize() >= sizeof(Frag) * 2
!!!! Cannot explore via koko. Only relay commands can be passed to it. Try to connect by selecting KIS instead of Koko !!!!\n
MEPS
Register file 19
Register file 28
var.devid.INVALID
Complex Name: %s\n
error trying to unlock MSR %s
Failed to setup bp=%d
%s%d
Connection aborted: kick required to probe server
Failed to write SPS_EL%d
AuthDbg,EnSecureTestExternal
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ENABLE_PKA_VALID reg: 0x%X\n
Protocol Version: 0x%X\n
ret.explore_table == NULL
      JTAG-AP port %u PSTA(0x%08X) is set...clearing\n
ret.drain.half-duplex
{%s::%s} [%s] error (%s) getting number of HW WPs
\tAligned Read Failed
{%s} handle ROM entry
%02d:%02d:%02d:%06ld|%s <%s> %s
Misc_CortexM
!!!! Critical Error: ARM64-specific _sstep method not currently supported !!!!\n
{%s} FAILURE - malloc error
Table 5–153
Status/State
Connecting to server, %s:%d
astris_json_logger_delete_all
Setting WP length not currently supported: %u
fn._ocd_exec_instr.rsr.ddr.addr_reg
fn._ocd_reg_w.ddr.value
Size
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
SoftwareBreak
   ROM entry %d (level %u): AVOIDED\n
internal.enable-timer-ovr.chip == NULL
Accumulator high bits
Table 5–135
regidx_save=%u
probe %s on localhost
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
MA
Unable to disassemble_at_addr 0x%016llx
cpu_getinfo
CTI_OUT_EN0
%016llx
{%s} Error looking up architecture (%s)
{%s} MEMAP accesses using KIS connection must be in whole 4-byte words (count=%d, size=%d, count*size=%d)
## memapw %u 0x%016llX 0x%08X ...(%d)\n
_handle_exception_for_el
clear_dft_authentication
fn._remove_instr_breakpoint.which_bp
ASTRIS_ERR_PENDING
Parent key is not an object
XSTAT
{%s::%s} failed: %s
OCD control register, clear
cpu-xtensa-ocd-base
_init_params
error %s reading DAP MMFR0
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
astris_preferences_cpu_monitor_list
{%s} Batch attitude key created for %p thread %#llx key %lu
Portal Access Read
NXP
high word
%s: []\n
Section 5.1
ASTRIS_ERR_JTAGERROR
Could Not Find Any Loaded Boosters of Type: %s\n
unswitch_regset
Stepping Stone Final =  %#x\n
R
MMID
ARMV7
Error Reading Device Production-Fusing\n
AXdebug_auth_enable_timer_ovr
fn._write_mem
Imago
{%s:%s@%d} [%s] reading PRSR (!lsr)\n
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
ret.nop
   Debug Port not responding (%s)\n
AuthBase_t::init failed (AuthDebug_t)
AMAuthInstallSsoSetStealthMode
{%s:%s@%d} [%s] FEEADR1L write failed: %s\n
fn._ocd_reg_r.DSR
cpu-explore-flag
AP[%d]: MEM_AP_APB\n
X12 Part
fn._ocd_exec_instr.rsr.ddr.t1.1
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
far_el1
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
{%s} Reading base 0x%llx entry's component ID
{%s=>%s} AXconn_t has no chips
RF13
IDLE
Setting STOP CLOCK to TRUE
file_type
CRYPTO
SPSR_EL2
_cache_op_l2
RF58
fn._collect_snr.excvaddr
a
ASTRIS_ERR_NOTOPEN
dbgwrap
SMX
ret.dlr_el0
Register file 18
OCD.DSR=0x%8.8X
{%s@%d} IOServiceOpen failed, err = 0x%08x
Single_port connection to probe server unavailable
SWDRESET
{%s::%s} [%s] WP_INSERT rdwr(%d) >= KINDS(%d)
{%s} setting up nameless target (address=0x%llx)
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
UNKNOWN_PORTAL_ERROR
%s at offset %zu
vers_gateway < 2
[FLUSH]\n
_halt_hw
Failed to read: ESR_EL%d
Failed to update cached registers for EL=%d
{%s:%s@%d} [%s] FEEADR1H write failed: %s\n
op_S32I_encode
ASTRIS_ERR_EMPTY
AXbooster_interface_create_soc
[AstrisAsync][COMPARE] MISMATCH: cs_chip - acmd1=%u, acmd2=%u\n
AXcpu_resume
kisLoc
%2d) %s %s%s\n
cpu-address
astris_ide_is_component_present_at_addr
{%s:%s@%d} Restoring from exception level[%d] other than 1,2 or 3\n
CPU Address: 0x%llX\n
wrstn-size
{%s} halting %s\n
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
{%s} 0 words requested for read at address 0x%016llX
PARTNO_DAPLITE
Server Response Does Not Countain Ticket\n
EPC2
!!!! Critical Error: exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
Trying to use size of 8 on not AXI bus
AuthDebug_t::need_to_authenticate_probe PROBE_STATUS reg: 0x%X\n
SWDONLY
gmtime() returned NULL, using epoch time
Could not find bundle () in given array: %s\n
fn._remove_data_breakpoint.which_wp
{%s:%s@%d} [%s] failed to setup connect\n
fn._write_special_reg.reg_srn
param.ar.invalid.>15
cpu_go
** CPU %s requires forced explore override flag on this SoC **\n
Register file 14
Register file 55
AUD
Section 1 Offset: 0x%llX\n
[DCC] Grabbing DTR failed: %s\n\n
postinc < ARM64_LDRSTR_POSTINC_MAX_IMM
(crm & ~ARM64_HINT_CRM_MAX) == 0
RF51
')
[Timeout running ARM7 scan list]
Instruction count
Unable to create pthread key for conenction. errno=%d %s.
kob
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
PARTNO_1176JZFS
OCD control register, set
op_RFDD_encode
CortexM4
0 == level_stack_.template Top<Level>()->valueCount % 2
CreateSchema
Could Not Get Bundle Out Array of Found Boosters\n
ret.get_current_el.initial
%s status transitioned: %d ('%s') -> %d ('%s')\n
IOPlatformExpertDevice
IDE
successfully updated DEMCR
MR0
TARGETSEL
Found probe memory transfer in progress; clearing EDSCR.MA.\n
ret.reg.write.K_DA_REG_NAME_AUTH_TIMER_STATUS
PRID
Error %s connecting to server %s:%s [RETRYING]
astris_ide_get_dbgwrap_aperature
all
[READ] cop %d -> 0x%08x\n
{%s::%s} %s resumed\n
Replacing key with value
AXcpu_lacc_count_clear
can't find pid in response\n
ISP_L
(op2 & ~ARM64_HINT_OP2_MAX) == 0
MAC16 Data register 2
GETSETTCK
Full JSON that failed validation:\n%s
Failed to setup wp=%d
MASK ERROR
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
{%s:%s@%d} [%s] unable to transfer command\n
Passed NULL booster without custom plist\n
astris_ide_get_pid
PARTNO_JTAGDP
{%s} write[CTI32] of %s @ address 0x%016llX = 0x%08X [%s]
EICE chip %x initialized\n
CPU Monitor key does not exists for: %s\n
_reg_desc_lookup_by_index
fn._ocd_reg_w.ddr.t1_save
%s/%s
{%s:%s@%d} [%s] moving COPROC reg to GPR 0\n
{%s} m_exception_level(%d) != current_el(%d)
to
Did Not Find Any Boosters For: %s \n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/disassembly/astris_disassemble.cpp
{%s::%s} waiting for EDSCR ITE
hwbp_insert
param.tgt->ap.null
[Auth Debug] Auth Disabled - External Debug Interfaces Closed\n
cpu_hwbp_disable
{%s:%s@%d} [%s] erase_all failed: %s\n
%s - runBlock
PARTNO_HUGO
Error status from AMAuthInstallSsoSetAppleConnectInfoPtr = %i
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Table 5–133
ret.raise_el.read
AMAuthInstallSupportDictionarySetBoolean
abort
probe %s [port %u] on localhost
{%s} probe advertised csv_maxbuf=%u > client max %u; clamping
alloc_drain_payload
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_preferences.cpp
astris_batch_attitude_cop
Can't get OS build version - failed to create ReadStream
kis_stm_name %s %d
   {%s} Before powerup CMDSTAT=%08X\n
ret.reg.write.K_DA_REG_NAME_AUTH_VALID_CLEAR
Invalid num_regs = %u. Windowed register option required.
XBS version mismatched: %s (Expected: %s vs  Actual: %s)
ASC_ECORE_ROM
JsonLogger: Wrote %zu bytes to '%s'
{%s} error %s at line %d
AXcpu_mmu_get_tsz
internal.enable-timer-ovr.debut_auth == NULL
%s: %s\n
astris_soc_release
LAM
write_reponse_and_check_authentication
var.num_loops.invalid>3.curr_instr
no MEMAP access
ASTRIS_ERR_PROBECOMMAND
Probe %s Device Not Connected on USB-C Port
IsNumber()
{%s:%s@%d} [%s] reading PAR[64]\n
Table 5–129
Previous attempt to connect to probe failed: %d (%s). Retrying...
cpu_lacc_count_clear
set.astris_version
tdi-wsi
result.ide ==NULL
astris_setup_ap_mem
param.no_ap
ret.CFReadStreamOpen
_insert_instr_breakpoint
ADI Preflash\n
ACC
{%s:%s@%d} [%s] scanning out (DIDR)\n
Unable to read GPR 28
\tPrologue Aligned Read Failed
DESIGNER_APPL
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
Register file 52
AXcpu_cleaninv_dcache
   Debug Port: SELECT %X: AVOIDED\n
setTargetOS
RSM
Arm
{%s::%s@%d [%s]} Error %s: initializing cache parameters
[AstrisAsync] Barrier before pause\n
Data break 0 address
cpu-xtensa-num-intr
{%s::%s@%d [%s]} Error %s: writing 0x%llX to register ID 0x%X
[AstrisAsync][COMPARE] MISMATCH: cmdlen - acmd1=%d, acmd2=%d\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
reg_srn=%u, \"%s\", regval=0x%8.8X
fn.params
KobaSWD
AXcpu_hwbp_insert
wb_u32=%u
TAP-Only
{%s@%d} Probe response payload read when no payload indicated.
.os
\n
_a64cpu_read_gpr_cached
EXPLORE_NO_TAP_RESET
s0=%d,ar=%d
CopyFrom
New format for cip gen register, unsupported: %d\n
{%s->%s} exec: encode_msr(MDDTR_EL0, scratch=%d, true)\n
OFFLINE
AMAuthInstallRequestSendSync
ASTRIS_ERR_NOPORTAL
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Unaligned Access
u32toa
[SSTEP] bvr=%08x bcr=%08x\n
Invalid current AP (%d), adopting latest (%d)
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
%s probe[*] from Probe Map Server [local host]
{%s:%s@%d} [%s] executing MSR\n
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
probeNicknames
param.reg_name.invalid.null
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
{%s:%s@%d} [%s] performing single step\n
PORTAL ERR PENDING
RESPONSE_CMD
_read_memory_slow
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
ret.astris_create_cstr_from_cfstr
ICOUNT
USB connection not currently open
[AstrisAsync] REPLAY DIVERGENCE: Command issued during last replay! Handling synchronously...\n
get_gpr
ret.write.msr_lock_reg
Reset
get_ecid
Table 5–163
relay_set: %s -> %d
schema_version
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis.cpp
param.booster_bundle==NULL
set
Lock field set in 0x%llx = 0x%llx, clearing bits 0x%llx\n
KIS-HUB-NULL
APPLE_SUBTYPE_UNKNOWN
cpu_writereg
setResult
index slot not enabled
read_settings
Table 5–179
Register file 53
%s/%s%s.bin
wa
{%s:%s@%d} [%s] reading CCSIDR[L2]\n
%s: not supported.\n
AXconn_connect_kext
[%s] %s
ret.createKeyWithPrimate
Loop count
BYPASSCH
m_core_api_serial_queue
{%s::%s} [%s] error %s writing SW BP instr [VA=0x%016llX, len=%d]
[M3XLAT] base=%llx in=%llx out=%llx ret=%d region=%s\n
PARTNO_SWDP_M23
signature was NULL
Please answer y=yes or n=no.\n
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
read-back (sys AP) failed
astris_user_default_remove_all_nicknames
cpu object is NULL
{%s} DEVARCH read fail in CoreSight component (%s)
command timed out
ASTRIS_ERR_NOTFOUND
User created bundle found, ignoring version checking via plist
wir-size
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
param.cpu_reg_file_size.invalid.2
EmulatorSWD
{%s:%s@%d} MIN_EL(sysreg)[%d] <= m_exception_level[%d]\n
EXCSAVE5
RF45
=== Starting Gather and Clear ===
NRF
Dock-Channels
init_hw.set.fpb.en
Register file 6
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
pointer.h
{%s} Extracted CIP Gen Number from table  (%d)
CopyPart
_update_register64
virtual int ARMv7cpu_t::_resume_hw(bool)
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
fn.AXmemap_read.address.regval
%u
kick
source != __null
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
line
{%s} [%s] m_exception_level=%u\n
ret._set_wpaddr_hw
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
cpu_read_dcc
ApProductionMode
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
%s_%s
MODE
select
[1500] TAP %d: irlen must be > 0 (got %d)
DCS_BC1
{%s[recv]} %d(%s) [RETRYING]
set.user
wrstn-pipes
AXconn_set_nickname
   Debug Port: SELECT %X: DISABLED\n
Register file 38
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_soc.cpp
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
pointer.IsValid()
_a64cpu_read_vfpreg_hw
disabled
Register file 49
\"%s\" not a regular register
ENUM
deinit
{%s:%s@%d} [%s] reading CCSIDR\n
Failed to find whether addr in DRAM; falling back to 4 bytes transfer\n
%s v%s%s [%s]
ESR_EL2
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm7cpu.cpp
addr = 0x%llx
Unable to register assert upcall %s (Insufficient memory)
response == NONE; failed to get kis target info\n
{%s@%d} Received %d bytes when requested %d bytes.
description
ret._a64cpu_read_vfpreg_hw
{%s:%s@%d} [%s] failed to read CMD/STAT\n
LOSTCONN
Wait indication while connecting to
{%s} no TAP detected that supports 1500
Form-factor specific channel not found, falling back to generic channel for device '%s'
    EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
TIMEOUT
AuthDebug::authenticate_probe - no need to authenticate\n
{%s} [%s] EDSCR with ITO set - ERR while waiting ITE.\n
Done.\n
fn._read_general_reg.regval
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
cpu_writereg_vals
CPU Core Number: %i\n
_read_register32
{%s:%s@%d} [%s] doing IR scan (DTRRX EXTEST)\n
{%s:%s@%d} [%s] Setting WP length not currently supported: %u\n
i8@?0
PARTNO_SWDP
JTAG error while communicating with
Awaiting next chunk of big response
init_hw.read.fpb.rev
Setting CPU %s is_boot_core to %d\n
writer.h
relay
astris_batch_attitude_destroy
{%s::%s} EDSCR with RXO set - unable to recover.\n
!!!! Critical Error: Took an exception that took us to exception level[%d] other than 1, 2, 3? !!!!\n
{%s} masked read at 0x%016llX failed: %s (mask=0x%08X, expected=0x%08X)
Memory error virtual addr register
Processor Id
[1500] v2 plist missing required field 'bridges'
copyBoardNameForPrimate
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
fn._ocd_exec_instr.rsr
cpu_swbp_insert
op_RFDO_encode
{%s:%s@%d} [%s] reading GPR 0\n
query_events
str != 0 || len == 0u
GetHashCode
Failed to write register: 0x%llx val: 0x%llx
ret.modify.edscr.~MA
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
AXcpu_readreg_vals
astris_memap_debug_writebuf
EXPLORE_WITH_AUDIO
AXchip_is_prod_fused
AMCNP_GFX
(dest_gpr & (0x40000000 | 0x80000000)) == 0
ret.m_lam.paccess_write
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_STATUS
RF44
No windowed register option.
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
astris_explore_enabler_get_cpu_status
_write_executable_memory
CPU.ARM7
com.apple.astris
RF3
fn._tie_read_word32.first
ADI Postflash\n
Target was lost while connecting to
init_hw.read.dhcr
connection not currently open
APCIE_REGS
Magic does not match: %#x vs %#x\n
DLR_EL0
hwwp_disable
ASTRIS_ERR_IGNORED
AXconn_conndesc
/swdflashers
ret.exec.mrs.sysreg->scratch
AXcpu_suspend_translation
symbol.check.loaded.AMAuthInstallSupportDictionarySetBooleanPtr == NULL
PoodleSWD
esr_el3
param.invalid_gpr
_a64cpu_write_gpr_hw
ret.board.copyPairForPref
param.invalid.reg_file_index.outofrange
AXbreadcrumbs_read
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
Min Component - %s\n
{%s:%s@%d} [%s] writing OSLAR (oslsr)\n
AXdebug_auth_clear_sso_user
%02X 
HardwareStep
param.bp_index.invalid.outofrange
SoC clocks are stopped. No MEMAPs allowed 
{%s} checking for single_port probe daemon on port %d
cpu_mmu_walk
cpu did not stop. OCD.DSR=0x%8.8X
v8@?0
explore
port_%d
cpu_mmu_configure
SOC
## dpr 0x%02X failed (%s)\n
{%s[select]} %d(%s) [RETRYING]
{%s:%s@%d} [%s] handling pending async aborts\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
RF11
cpu_hwbp_info
ret.enableSubsystem
MEPC
15002APB
(instr & ARM64_MSR_MRS_BASE_MASK) == 0
{%s} %s status is '%s' [Status Read %d times]\n
n't
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
ret.previous_authenticate.timedout
Unable to get version info from %s [error %s]
wir2-tdo
enable
{%s} [exception_level(%d) != current(%d)] exec: DRPS_ENC\n
{%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
symbol.check.loaded.AMAuthInstallCreatePtr == NULL
get_chip_id
Table 5–167
fn.var.exec_path.invalid
[%s] EL @ end of Collect: %d\n
Atomic Oper, Control
op_SDDR32_encode
Miss fraction part in number.
CPU PS-Register: 0x%llX\n
wir-tdo
FAR_EL1
EDRCR
user
vvvvvvvvvvvvvvvvvvvv DUMP OF HISTORY LOG vvvvvvvvvvvvvvvvvvvv
connection about to be destroyed
{%s::%s} EDSCR in unexpected state. Returning %s.\n
internal.clear-auth.chip == NULL
koko
comparing against match entry %d: %s
%s Bridge @ 0x%09llx-0x%09llx: %s
In Postflash\n
ELR_EL3
RF15
ECORE
Failed AP read of R_MEMAP_CSW res: %i
Register file 27
op_XSR_encode
{%s:%s@%d} [%s] failed to select probe\n
HOSTID=0x%x which is invalid, skipping orientation check
CortexM33
setCategoryValue
EXCEPTION(check) %p EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
_read_gpr
astris_command_complete
src_reg < 32 || src_reg == 31
R7
fn._ocd_reg_w.dcrset.regval
span
Failed to restore EL to %d after writting register: 0x%llx
AXdebug_auth_set_sso_user
Subsystem Monitor Key does not exists: %s\n
{%s:%s@%d} [%s] timeout waiting for cmd abort\n
INFO: %s(%04u): %s(): err=%s(%d): %s\n
{%s:%s@%d} [%s] reading GPR 1\n
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
EDSCR
_ocd_reg_dsr_w
Error while trying to authorize: %d - %s\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, scratch=%d, %d)\n
L1C
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
_set_bpcr_hw
failed read from DEMCR - %s
no SOC object available
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
index != kRegexInvalidState
dart-apf-address
_set_wpcr_hw
{%s->%s} [!aarch64] exec: encode_mrs(scratch=%d, MDDTRRX_EL0, %d)\n
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
     ARM %s debug CPU rev %d\n
read memory
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
astris_dpread
DBGWRAP_LITE
Highest EL: %d, -- Min Op EL: %d
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
address=0x%8.8X, len=%u, rdwr=%d
ProbeNav
CPU Explore: 0x%llX\n
[COLLECT] Chip %x\n
[AstrisAsync] Resuming Async Mode\n
Production Fused Device\n
INVMODE
param.conn.user_defaults == NULL
{%s} _halt_hw result = %s
astris_apread
param.address.invalid.>max
AXchip_get_stm_dockch_list
Schema parse error
[1500] No %s.plist resource found
probe
ArcEM
stack.h
Exception %d Stack Trace
EXPLORE_WITHOUT_PIO_SAFEGUARDS
ICOUNTLEVEL
_write_pc
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
m->name.IsString()
Asked To Read A Negative Register Index
complex-name
ret.ito.read.edscr
lower_el.el2.tge=set
RF4
%s %3d'b%s\n
D0-PKA
get_page_shift
AXcpu_writemem
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Xtensa Option non_tie_ranges: %zu range(s)
PORTAL_STS_MULTIPLE_BITS_SET
!*!*!* ****************************************************************************** !*!*!*
Empty
Portal Config Read
_set_halting
EL2h
{%s=>%s} null reference to AXchip_t record, `cpu->tgt->chip`
astris_memap_bus_read
Register file 40
var.reg_srn.invalid.not_present
ASTRIS_ERR_NOCPU
Failed to get KIS STM Probename\n
_insert_watchpoint
ret.clear_authentication
{%s:%s@%d} [%s] unable to drain response\n
{%s@%d} Drain empty on decr [%s].
cpu_get_cl4_debug_signpost
cpu_lacc_pipe
ASC
write_register
_write_general_reg
Unknown Subcommand
root_ != 0
j1500d
Value Types Are Not Strings\n
Info_
[1500] Error parsing TAP description
ret.reg.read.K_DA_REG_NAME_PKA_BASE_HI
General register 13
fn._ocd_exec_instr.s16i.r1.r0
CortexA53
UNKNOWN 
ret.enableCpu
ret.clear_edscr_err
## apw %u 0x%08X 0x%08X\n
Begin
(data_.f.flags & kUint64Flag) != 0
Logging Context Is NULL\n
[%s] E2H is set, virtualization is supported\n
!!!! Critical Error: exception other than an abort (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
{%s->%s}
RF41
Specified host %s did not resolve to valid host
grape_cs
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
Blocked
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
Literal base
ide_checker_diagnostic
haskis
Failed to find a product plist for this soc %s
ret.enableAll
VBAR: %#llx\n
Register file 48
var.m_debug_interrupt_level.invalid.outofrange
Gateway Version: 0x%X\n
exit.exception_test_0
{%s:%s@%d} [%s] doing IR scan (DIDR INTEST)\n
configure_mmu failed
fn._read_mem
Hang Radar Info:\n%s\n
DBREAKC0
AXI Error
ASTRIS_ERR_INVAL
==== Exception Trace ====\n
{%s} category=%d
EDECR
[AstrisAsync] REPLAY DIVERGENCE: Unused command responses on async deactivate!\n
EXPLORE_WITH_AVE
LEND
halted=%d
Schema validation failed
~
We got data abort reading CPU address: 0x%llx
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
astris_kis_clear_status_registers
resolve_platform_details
ESR_EL1
ret.transfer.half_duplex
Impeded
Register file 35
type >= kNullType && type <= kNumberType
CLIDR
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
ret.m_lam.paccess_read
Cause of last debug exception
EPC4
%s probe[%s] from Probe Map Server [%s]
ARMV7EM
{%s:%s@%d} [%s] executing MRRC\n
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
_read_general_reg
RegionStart
(reset-network)
[PREFS] Key: %s - Val: %s
No connection attempt description
{%s@%d} Unknown CS command error [%d]
CPU %s not found or already removed from the map
ret.storePairForPref
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
FEECON  
FEECMD  
COMPARE0
wrstn-dpcsoc
result.read_vals==
AP
Dumping Process Tree
Probe Map name of probe %d is: %s
Clear (1<<1)
_clean_dcache_vaddr
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - ADDRESS=0x%llX
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
JTAG chain not yet explored
Probe Map comm error %d(%s) %s [%s]
xfer_acmd_via_sock
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
AXcpu_writereg
AXcpu_resume_translation
{%s=>%s} null reference to AXconn_t record, `conn`
internal.get-timer-count.chip->soc == NULL
{%s:%s@%d} [%s] get_chip_id failed: %s\n
loadSchemaForCategory
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
no board info file loaded
poo
bits
dpb-tpser-id
Gone
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
@rpath/%s.framework/%s
nullptr == file_url
{%s:%s@%d} [%s] reading CPSR(2)\n
setProbeInfo
[%s] TGE is NOT set. Traping to EL1 allowed.\n
{%s:%s@%d} exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this...\n
[AstrisAsync] ASYNC_CONFIG sent (dispatch=%d independentPkts=%d)\n
Main
{%s} DAP command nwords=%d trimmed to %lu\n
fn.remove_epcn_epsn
AXconn_destroy
%d.%drc%d
Unknown kick response[%s] (for probe %s) from probe server
_resume_translation_hw
failed to read memory
Table 5–173
GetSize() >= count * sizeof(T)
BeginValue
wrstn-reg
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
EPS7
plist
Failed To Instantiate SOC From Booster\n
outCount != 0
ret.dfu.dcm.reset
{astris_probed_print_events_from_json} not supported in this build configuration
{%s::%s} [%s] DTRRXfull_l is 1, DTR will be ignored
v%s.%s
Debug Clock Already Enabled
Table 5–186
[CMD] %02u:%02u:%02u:%06u|%s <%s> %s\n
No Success after retry on wait
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
rhs.GetType() == kObjectType
Tc1500_t
{%s:%s@%d} [%s] DEMCR read failed: %s\n
_read_spsr
Transaction
SOC_t::{%s=>%s} null reference to CPU_t object, `cpu->state`
OCLA_IP_REGS
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
logger already initialized
ret.getSubsystemEnableStatus
Error - eraseflash failed.\n
fn._ocd_exec_instr.rsr.ddr.t2
GetAllocator
Matched via Bundle ID\n
Xtensa Option options: 0x%x
ASTRIS_ERR_RESETTING
REG
XTENSA
{%s} Thread %#llx key %lu detaching from info %p when not attached - IGNORED
{%s->%s} exec: aarch64_add_imm(scratch=%d, REG_SP)\n
[AstrisAsync] Deactivate while async is not active!\n
op_WSR_encode
{%s@%d} neither socket nor kext connection available
astris_remove_loaded_soc_boosters
Complex CPU ID: %d\n
go
IDE ACCESS OUT OF BOUNDS
invalid environment variable
Error %d (%s) %s %s probe server
TRST
GenericValue
AXbooster_interface_init_astris_api
{%s::%s@%d} [FALSE] src_gpr[%d] <= 15\n
Need to be connected to set nickname
param.no_dp
DESIGNER_ARMDAP
RF10
primateHubLoc
{%s:%s@%d} [%s] unswitching register set\n
Error %d(%s) executing instruction 0x%08X
RF39
fn._ocd_exec_instr.xsr.ddr.t1
ret.dock_disconnect_mode
is.Peek() == 'f'
target not in appropriate state for action
ASTRIS_ERR_NODEVICE
{%s:%s@%d} [%s] DEMCR write failed: %s\n
{%s:%s@%d} [%s] moving DBGDTRTX to GPR 0\n
{%s:%s@%d} [%s] updating DFAR\n
DSPSR_EL0
\tReading left over chunk expected 0x%x got 0x%x\n
RF2
%s %s
Sprocket
revive
master-localwrstn
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
Fabric access is blocked. Expected if production unit, won't explore further.
Unable to connect to probe server
kick_req %s
{%s@%d} socket connection is not available
AXdebug_auth_get_probe_timer_count
Value is null
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
astris_explore_enabler_init
UNKNOWN_DAPSTAT
Invalid reg_index %u
HostInfo
APEXPLORE
RISCV
{%s} skipping dcache flush, cache already clean
write to CMD/STAT failed - %s
low
Only Auth-Debug, Auth-DFT and Probe-Auth are currently supported.\n
Memory error status register
Master BoosterManager
virtual int ARM7cpu_t::_halt_hw()
   DPv3 bus is %u bits wide\n
We are Deallocating\n
Dart Coastguarded CPU: %s\n
_get_bpaddr_hw
{%s} set=%u (sh=%u), way=%u (sh=%u)
symbol.check.loaded.AMAuthInstallSsoSetAppleConnectInfoPtr == NULL
config_write_enable
Cycle number to inter.
Prompt
init_astris_api
result.read_vals(version)==
set_dtrmode
FEESIGL
ASTRIS_ERR_NODATA
SLEEPCTL
Logger output is null
getOrCreateValue: addMember failed, returning doc root
{%s:%s@%d} [%s] executing MCR\n
   JEDEC ID: 0x%08X\n
api.is_prod.chip->soc == NULL
Misc register 3
Table 5–188
_reg_desc_lookup_by_name
Failed to init from cpu desc armv7m cpu: %s \n
fn.local
Failed to find member after adding to document
.name
CPU Typehint: %s\n
CoreSight
ERROR!! Wrote %zd bytes, expected %zd\n
Kicking
--> debug      size=%3d acsr=%d
%s:%s
fn.missing_entry_function
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
astris_kis_poll_cfg_reg
Failed to fetch if we are in ARM64 or AARCH32
document.h
3679.40.30b172
write.sysreg.el_check
_a64cpu_set_singlestep
EXCSAVE4
Table 4-63
{%s:%s@%d} [%s] bad hostname\n
Eval
Failed to read transfer register (EDDTRTX)
which_wp=%d
\t[MATCH_APR] FAIL <= unable to select AP by type: 0x%X
{%s:%s@%d} [%s] failed to write CMD/STAT\n
{%s} no response from bridge
CTI_CTL
Table 5–180
PSD
SWDFlasher.ADI
haskis bit not set\n
Both debug and xbs versions are set, maybe a bug: %s
read-back (sys AP) did not contain SW BP instruction
{%s::%s} [%s] error %s from _synchronize_context.
[HALTED] dfsr = 0x%08x\n
internal.is_authenticated.chip == NULL
astris_json_set_address
cpus
{%s:%s@%d} GRPS[0] cached\n
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
Kick required to connect: Busy probe
 
astris_ide_get_from_chip
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
Table 5–159
VECBASE
M
Awaiting response from Probe Map Server
ARM11
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
get_mair
Modified Word To Write: 0x%08x
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
internal.authenticate_dft.chip->soc == NULL
EXCSAVE6
Category not found
encodings.h
1500 IR Commands:
{%s} %s resumed\n
{%s} timed out waiting for cpu to halt during collect
GenericSchemaDocument
.success
Found the RTXCID Structure!\n
ARM64 SWBP not supported in T32 mode
SOC_t::{%s} CPU_t group=%d when group 0 expected
cpu_cache_info
rhs.IsString()
Product Name: 
dr ->
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
{%s} Failed to get watchpoint mask for %s: %s
MAC16 data register 0
fn._init_configuration.w2.audio.HIFI3_2
CPU with %s Not Created via Name
fn._ocd_reg_r.ddr.regval
fn._ocd_exec_instr.TIEWriteProtectedI
unknown match criteria type: %d
mempool-size
Failed to raise EL to %d to read register: 0x%llx
erase_page
fn._ocd_exec_instr.xsr.ddr.t1.1
file/object not found
ret.rx-full.mddtr
EL1h
fn._ocd_reg_r.ddr.value
{%s} Failed to extract portal info from table (%d); continuing anyway
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
Successfully Authenticated\n
_read_cpu_reg_file_all
Parameter len = %d > 64.
op_S16I_encode
pnav_connect_probemap
ret.astris_disassemble_at_addr
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
Variables not setup
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
Failed to read DCM GPIO (0x%x)
{%s:%s@%d} [%s] scanning out (DSCR)\n
[%s] EDSCR masked read error bits set: 0x%08X (mask=0x%08X, expected=0x%08X)
EDWXVR0+index
read_dbg failed to access R_v7M_CLIDR
Discon
ret.spmi_write
EXPLORE_JTAGAP
Chip Revision: 0x%X\n
/System/Library/CoreServices/SystemVersion.plist
pid
BitboxSWD
shared_ != 0
internal.is_authenticated.debut_auth == NULL
%s\n%s [%s]
check_dcc
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
[%s] chipinfo is NULL
RdProt
value
!!!! Critical Error: GRPS[0] cached !!!!\n
{%s::%s} [%s] error (%s) getting number of HW BPs
~/Library/Application Support/Astris/astris_prefs.plist
out of memory
M0
fn._ocd_reg_r.dsr.regval_raw
{%s} %s
message
complex-base-address
T32
{%s} collect result = %s
Warning: chip exploration did not complete successfully (%s)\n
SWD KIS Command is NOT Multiple of 8
is.Peek() == '['
required
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
{%s:%s@%d} [%s] executing MOV\n
ret.read.edscr
Level-1 exception PC
param.width.invalid
init
MemoryBlock_t
{%s:%s@%d} [%s] wait_for_cmd_aborted failed: %s\n
no data when data expected
no USB device
Port
ParseNumber
%s%s
[%s] {%s->%s} END handling exception
_suspend_translation_hw
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
Table 5–175
Invalid parameter exec_path = %d
ASTRIS_ERR_BADPROTOCOL
TXU
unable to raise to EL1 (to suspend translation)
{%s} Error setting up memap target (%s)
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
Register file 10
applesoc == nullptr
psr-size
FEEAENH
SAM2
virtual int ARMv6cpu_t::_resume_hw(bool)
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, %s=%d, %d)\n
_check_exception
{%s:%s@%d} [%s] FEECON write failed: %s\n
EXCSAVE1
var.bp_index.invalid.outofrange
set.os
{%s:%s@%d} [%s] reading PRSR (lsr)\n
op0: %d op1: %d CRn: %d CRm: %d op2: %d el: %d
VBAR: %#x\n
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
Going To Create Generic ARMV8\n
FEEPROH 
_cleanup_hw
address=0x%8.8X
\"%s\" not a special register
Can't get OS build version - failed to create URL
ASTRIS_ERR_CPUHALTED
XINIT
vector
ret.write.editr
src_gpr <= 15
_ocd_reg_dsr_clear_and_validate
cpu
Unique required when more than one probe identified by
info-probemap
[INSBP] bp%d addr=%08llx fpr=%08X\n
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
fn._ocd_reg_r.dsr.1
usb
CPU-level (general and architecture-specific)
ret.read_all_breadcrumbs
DCS14
{%s:%s@%d} [%s] executing VMOVR\n
<rev>
Table 5–148
astris_soc_check_debug_root
defaults.nickname.too_long
 (
{%s} Failed to extract IDCODE from table (%d); continuing anyway
ret.is_current_state_aarch64
{%s:%s@%d} current_el[%d] <  %d\n
Previous authentication in-flight, wait for it to finish\n
{%s:%s@%d} [%s] wait_for_cmd_idle failed: %s\n
UNKNOWN_CODE
SPI
(system_reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) != 0
   {%s} Enabling debug unit\n
reg_file_index = %u >= m_cpu_reg_file_size = %u
AXchip_get_chip_variant
error %s checking for data abort(first)
M2
RF54
param.op.AXCPU_WP_ENABLE.unsupported
Error level
{%s@%d} IOServiceClose failed, err = 0x%08x
!!!! Critical Error: Error %d(%s) deleting info %p batch_attitude_key !!!!\n
Failed to safe raise to EL=%d
Table 5–166
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
PARTNO_ARM7TDMI
fn._read_special_reg.ibreakenable.reg_bp_enables
%Y-%m-%dT%H:%M:%S
{%s:%s@%d} Critical error [radar already requested]
Corrupted list getting to selected probe(%d) {i=%d, count=%d}
_create_cpus
{%s} [%s] EDSCR with ITO set - recovered (retries=%d).\n
wait_for_cmd_aborted
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
ASTRIS_ERR_EENOTFOUND
name %d
Failed to create SoC or no booster
GenericStringRef
CPU Supported in Integration: %s\n
Early dbgwrap base extracted: 0x%llx\n
{%s->%s} TGE is set, can't raise to EL1
[AstrisAsync] Got ASYNC_RESTART response!
RF32
as=%u,opcode=0x%6.6X
UNKNOWN_KIS_ERROR
KanziSWD
PowerOff
{%s:%s@%d} [%s] FEEPROH write failed: %s\n
{%s@%d} Failed to find cached response
cpu_lacc_pc_status
{%s:%s@%d} !(prsr[0x%08X] & DLK)\n
ret.read.gpr_1
[AstrisAsync] ASYNC_CONFIG rejected by server, async batch cancelled: %s\n
Using Built In CPUs\n
param.wb.invalid.>wb_max
CortexM0
astris_ide_get_dbgwrap_base
AXcpu_hwbp_enable
Error occured during nonce command (v.5)
Failed To Initialize Logging\n
Delayed
EXCSAVE2
EXCVADDR
fn._ocd_reg_w.ddr.address
ASTRIS_ERR_OUTOFMEMORY
{%s} probe_host = %s
AMCP2
AXdebug_auth_get_timer_count
issue_cmd
sr=%u,ar=%u,opcode=0x%6.6X
Invalid object or key for addMember
{%s} IDCODE %08X found; designer=%s, partno=%s, flags=%08x\n
environment variable not found
%c
Unknown error.
Size or Count provided are 0.
In Eraseflash\n
time out reported by probe
unable to create connection
mempool-dmem-offset-reg
error %s checking for data abort(uint32_t)
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
!!!! Cannot explore via sprocket. Only relay commands can be passed to it. Try to connect by selecting KIS instead !!!!\n
No version information found in booster: %s
baseReg
ARMv7mcpu_t
_setup_data_bp
Unique required when %d probes
Accept
fn._ocd_reg_r.DCR
!!!! Critical Error: m_exception_level[%d] == 0|1|2|3 !!!!\n
ret._a64cpu_read_sysreg_hw.hcr_el2
set.wp.len = not supported
FEEPROH
xfer=%u, xfer_length=%u, address=0x%8.8X
fn._write_special_reg.dbreaka0.address
Unknown number of groups in the explore table; can't parse group attributes
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
AXcpu_flush_icache
Could not enable KIS SoC Access\n
DHCSR write failure - %s (%d)
astris_ba_uses_attitude
L1 dcache
createKeyWithPrimate
cpu-aptype
AXcpu_mmu_walk_detailed
EXPLORE_WITH_SEP_DEBUG
AXconn_probed_query_events
KongSWD
GetDouble
{%s:%s@%d} [%s] writing PAR[64]\n
param.tgt->ap->dp->chip.null
astris_explore_romtable
Register file 34
fn._ocd_exec_instr.wsr
Connected to Probe Map Server
AddMember
{%s} no matching 1500-to-* bridge
[REMBP] bp%d\n
Off
{%s:%s@%d} [%s] FEECMD write failed: %s\n
RF52
connect
Prefix
param.booster_handle==NULL
About to call fault reg latch, min_operating_el: %d\n
_a64cpu_read_gpr_hw
Exploring IDE in JTAG\n
(addr=0x%llx)
ret.reg.read.K_DA_REG_NAME_ACTIVE
MINISWD
sys_pwr_up
_a64cpu_encode_ldrstr_postinc
sel-sib-network
targetid/instance must both be set or both be unset
_invalidate_icache_all
## armcpu: Didn't read the right amount: wanted %u got %u (%08llX-%08llX)\n
fn._read_special_reg.icount
cpu_lacc_count_insert
panic
LCC
AXcpu_getmode
param.data_reg.invalid.>15
Can't get hardware model - failed to allocate data string
kext connect name %s\n
Failed calling AppleSOC_t::switch_taps\n
Missing a comma or ']' after an array element.
ACC-CTI
AuthDbg,Nonce
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
generated_files
JsonLogger: Schema loaded successfully for category '%.*s'
Got an error writing 0x%X the DCM Control Register: %s
The debug port associated with this chip has not been explored.
framework
storeNickname
{%s} asc status=%d being reported as Unknown
astris_init_ap_mem
addr_reg=%u,page_id=%u,data_reg=%u,opcode=0x%6.6X
address=0x%8.8X,page_id=%u
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
{%s::%s} [%s] REM_SWBP %s [VA=0x%016llX, index=%d]
L3
   DPv3 baseptr is not valid (%X)\n
code
Run
TatsuServer
AXdebug_auth_enable_test
RF53
Failed to exec MSR to move contents of scratch (containing val to write) into sysregscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
astris_booster_cleanup
armv7m-region-name
TOOMANY
[1500] Error parsing IR command: %s
{%s:%s@%d} [%s] reading CCSIDR[L1-D]\n
value=0x%8.8X
%@
cpu_translate_with_stage
{%s->%s} TGE is set, can't go lower to EL1
## apr %u 0x%08X -> 0x%08X\n
ret.reg.read.K_PKA_REG_NAME_DBG_STATUS
Table 5–168
Astris default logging context
transact
false
{%s:%s@%d} [%s] reading DTRTX\n
{%s:%s@%d} [%s] checking for data abort\n
ret._setup_wp
AXdebug_auth_is_authenticated
PROBED_USB_REQ_EMPTY
Astris-%d~%d
High level 3 exception PC
KIS translator version : %d\n
parse_soc_info_from_booster
AXbreadcrumbs_clear
astris_json_logger_delete_category
cpu-armv7m-regions
astris_explore_enable_subsystem
EDPRSR_AON
hwwp_enable
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
   Debug Port: SELECT %X: SKIPPING (%s)\n
PushBack
mxwrap-address
[1500] %s step %d: 'bits' and 'value' are mutually exclusive
CPU %s already in the map with status: %d
## ARM32cpu_t::read_register %u\n
{%s=>%s} null reference to AXchip_t[0]
fn.ocd.debugcause.di.incorrect
!HasParseError()
defaults.nickname.not_connected
astris_jtag_scan_stay_gotorti_impl
MESAVE
AXconn_kick
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
hostid
--> wrstn_wir2 size=%3d dpcsoc=%d
{%s::%s} read OK but took %d tries
CPUMonitor
ASTRIS_ERR_INVALCOMMAND
Parse
PARTNO_KIS
PKA Command Verify Completed, No Errors, but Probe Valid Not Set
General register 2
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
%Y-%m-%dT%H:%M:%SZ
MEM1500
cpu-xtensa-num-bp
!!!! Complex Key %s is INVALID !!!!\n
Cannot create complex descriptions from NULL info\n
write.dspsr_el0 NOT DIRTY
CPU_t
Register file 31
Error closing %s [%d]
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
write.reg.not cached
AMAuthInstallApSetParameters
{%s:%s@%d} [%s] Error - %s\n
R11
interface not in appropriate state for action
Misc register 1
XTENSAcpu_t
fn._ocd_reg_dsr_clear_and_validate
version
First Couldnt
EDBXVR0+index
[%s] AP, DP, or chip given is NULL
Using 10pin connector skipping orientation check
Error while %s:\n  Unable to connect to %s - %s
astris_ide_get_cpu_halt_group
param.cpu_name == NULL
ret.get_current_el
{%s:%s@%d} aarch64[%d] == believed_64bit[%d]\n
ASYNC
RASID
fn._write_window_base.wb.wb_save
Standard
{%s:%s@%d} [%s] setting DTR mode to STALL\n
Failed to raise EL to %d to write register: 0x%llx
param.reg.invalid.outofrange
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
%s probe[%s] from Probe Map Server [local host]
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
{%s:%s@%d} [%s] FEEPROL write failed: %s\n
fn._read_general_reg
{%s} unable to allocate probeInfo
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
{%s:%s@%d} [%s] FEESIGL read failed: %s\n
Program counter
RF27
kan
{%s} invalid data width %d bytes
Had an error during transfer: %s
[1500] Error parsing bridge '%s': missing required field 'select'
{%s::%s} [%s] WP_INSERT _insert_watchpoint[%d] failed (%s)
porpath
FEEADRAH
RF37
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s:%s@%d} [%s] setting GPR 0 (CPSR)\n
{%s} [EDSCR_RXFULL is_64] exec: encode_mrs(0, MDDTR_EL0, true)\n
Register file 36
DBG_WRAP_REGS
spsr_el3
INTERRUPT
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
{%s} unable to find single_port probedaemon on port %d
bundle_id
BoosterManager.SWDFlash
cpu-integrations
[AstrisAsync] Completing all async commands. Initial err = %d\n
IsValid()
channel-%s
-
fn._ocd_exec_instr.rsr.ddr.t1.2
connected
entry.exception_test_0
Cant find Debug Auth Registers. Auth not supported
internal.authenticate_dft.debug_auth == NULL
wb=%u
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
ret.relay.get.hostid
--> misc_wdr   size=%3d wirtestporten=%d
{%s:%s@%d} [%s] doing JTAG scan (DSCR data)\n
astris_user_default_remove_all_boardnames
MISC2
remote EEPROM not found
Failed to convert primateLoc %s to unsigned long long
_a64cpu_raise_el_hw
Level-1 exception save location
astris_cpu_raise_el
AXcpu_cache_cleaninv
EXPLORE_FULL
{%s::%s} [%s] length=%u when width=%d
astris_cpu_lower_el
authenticate_probe
astris_preferences_subsystem_monitor_list
FEEKEY  
{%s@%d} Found cached response
JAM
latching: EL%d
[WRITE] %d -> %08X\n
fn._ocd_reg_r.dsr
invalid parameter
{%s} %d(%s) [RETRYING]
soc-rev-num
Error reading thingy
error %s reading DAP PFR1
Original Content: 0x%08x
copyNicknameForKey
GetStringLength
DCM
Initializing Booster Layer\n
_invalidate_icache_vaddr
fn._ocd_reg_w.dsr.regval
{%s} flags:0x%08x
tar
{%s::%s} [%s] Breakpoint Insertion Failed %s [VA=0x%016llX, PA=0x%016llX bp-index=%d size=%d saved data=0x%08x] returning %d (%s)
Wrong width, should be either 4 or 8\n
Raw level
Set custom PSD json file: %s
dart-base-address
failed to determine breakpoint instruction
{%s=>%s} null reference to CPU_t object, `cpu->state`
DEPC
;
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
Probe
spsr_el1
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, &d, %d, false, %d)\n
error %s checking for data abort
!!!! Critical Error: aarch64[%d] == believed_64bit[%d] !!!!\n
virtual int ARM7cpu_t::_resume_hw(bool)
Invalid Xtensa CPU OCD.DEVID = 0x%8.8X. Should be 0x%8.8X (LE) or 0x%8.8X (BE)
astris_ide_get_bootid
{%s:%s@%d} [%s] moving reg to cop\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
target power is OFF
cpu-runtimes
AVD
Requested Register Requires EL: %d - Highest EL: %d
{%s} exec: DC_CISW_X1_ENC\n
--> psr        size=%3d bit=%d
low word
     ARM %s breakpoints: %u\n
fn._tie_write_word32
CPU disabled by SW, not accessable
connecting to probe by port number
Cannot create CPU descriptions from NULL info\n
SMC
M4F
astris_ide_get_deid
ret.reg.read.K_DA_REG_NAME_PRODUCTION_MODE
Section 5.2
RF61
fn._ocd_exec_instr.rsr.ddr.regidx_restore
cpu-armv7m-imem-size
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
Base of current AR window
EPIREAD
\t[MATCH_TARGETID] FAIL <= unable to find DP
{%s:%s@%d} [%s] getting GPR 0 (diff mode)\n
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
uri.h
DCS11
_read_memory_fast
## dpw 0x%02X failed (%s)\n
FPGAINIT
axi-regs
{%s::%s@%d} [FALSE] gpr[%d] < T32_GPR_COUNT\n
Clear requests in INTERRUPT
assert
Setting bypass channel to: %d\n
result.offset_from_content== -1
astris_ide_get_soc_stop_clock
{%s} Failed to get breakpoint count for %s: %s
COMPARE2
No probes were found matching
end rev is not of expected format; skipping cpu_desc override\n
Unable to convert plist file name to CFString: %s\n
explore_pid_kis
{%s::%s@%d} [FALSE] instr[0x%08X] != 0\n
AXchip_find_dap
{%s->%s} (top) current_el=%d
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
param.op.invalid
[CACHEOP] %d, 0x%016llx, %d\n
AP[%d]: MEM_AP_AXI\n
ApSecurityDomain
ret.reg.read.K_DA_REG_NAME_SECURE_DOMAIN
General register 11
fn.loop.xfer
param.invalid.content-type
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
astris_batch_attitude_detach
General register 9
%d.%dbeta%d
par
_with_cpu_thunk
Component Group Offset: 0x%X\n
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s:%s@%d} [%s] getting GPR 1\n
{%s}#%02X cmd: %s, resp: %s
co_coredump
level_stack_.template Top<Level>()->inArray
ASC_TCORE_ROM
{%s:%s@%d} [%s] writing WVR %d\n
ret._mmu_init
dbgwrap halt failed, falling back to classic method
PowerGated
AXcpu_lacc_count_remove
op_LDDR32_encode
no error
armv7m-region-axim-start
match-info
{%s:%s@%d} (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_adiflash.cpp
General register 5
astris_server_read
SRSTM
Realloc
writ
Failed to convert %s key @ index %d to a number with base of %d\n
localhost
{%s@%d} cmd is too large to fit into max packet size (%zd > %zd)
cpu_cleaninv_l2cache
opcode
{%s::%s@%d [%s]} Error %s: invalidating instruction cache
enable_timer_ovr
Can't get OS build version - failed to get build version
GEN
n <= m
output_type
set.success
[AstrisAsync] astris_async_override_disable_async: conn is NULL
AXcpu_status_asc
read_memory_dbgwrap
Error %d (%s) opening cmd snapshost save file
psr-partition-number
astris_ide_get_revision
{%s::%s@%d [%s]} Error %s: synchronizing context
_clean_invalidate_dcache_setway
DCS10
## ARM32cpu_t::read_register 64 bit 0x%x\n
AXjtag_explore
max_scan_bits is low: %d
INTENABLE
Register file 12
AXbooster_get_all_boostermanagers
M33
High level 5 exception PC
ret._cleanup_hw
ANE_SYS
[KIS] Register Read/Write/Wrote: %d\n
Could Not Get SWDFlash Booster Manager. Need To Call AXbooster_init\n
AXbooster_get_all_boosters
[AstrisAsync] Pausing Async Mode\n
Table 5–134
=== Found %s Boosters ===\n
Could Not Find The Astris Init Function (%s) in %s
_a64cpu_lower_el_hw
_a64cpu_restore_el_and_spsr
generate_nonce_and_send_request
Cycle count
RF36
Bug detected
ret.restoring_el_after_raising_to_read_hcr.raise_to_min
Invalid hostname or port specified as
Base::level_stack_.GetSize() >= sizeof(typename Base::Level)
DOCK-CH-AGENT0-STATUS
{%s:%s@%d} [%s] setting GPR 0\n
{%s} [is_64] exec: encode_msr(MDDTR_EL0, 0, %d)\n
Register file 59
ASTRIS_ERR_PROBETIMEOUT
INIT
Complex CPM Offset: 0x%llX\n
{%s::%s@%d [%s]} Error %s: collecting HW
MMUV8
timestamp
Failed to open file for writing
Missing a comma or '}' after an object member.
strfunc.h
recoverable
offset = %d
ret.ite.read.edscr
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
astris_jtag_scan_gotorti_impl
get_chipid
_write_special_reg_by_name
ret.write_hang_breadcrumb
EL0t
{%s} L2 cache operation completed [%s]
{%s} pmgr status=%d being reported as Unknown
AXcpu_lacc_status_insert
op_ISYNC_encode
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
Could Not Find The Astris Booster Cleanup Function (%s) in %s; this might be fine.
[ARM64] exec(DCPSX_BASE_ENC)
{%s:%s@%d} [%s] FEESIGH read failed: %s\n
There is no debug port associated with this chip.
_a64cpu_write_aarch64_sp_hw
MAC16 data register 1
opcode=0x%6.6X
Required key: %s @ index %d is NULL\n
AMCNP
{%s:%s@%d} [%s] setting GPR 1\n
_sw_breakpoint_remove
ERROR: nothing to do; suspending address translation for %s while already previously suspended
astris_jtagap_explore_port
ret.clear_probe_authentication
AMAuthInstallSsoEnable
_write_internal
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, %d, %d, true, %d)\n
CG
EXPLORE_ONE_DIE
ASTRIS_ERR_TGTLOST
size >= abuf - ubuf
CPU Subsystem: %s\n
L1 icache
EL3t
appendToArray.timing_phase
_a64cpu_is_current_state_aarch64_hw
[AstrisAsync] replay preflight: Async not active!\n
swdovrrun
Xtensa Core %s NOT configured\n
Kick off the current process using probe %s? (y|n)\n
start rev and/or end rev is NULL; skipping cpu_desc override\n
cpu_suspend_translation
AXbooster_print_boosters_detailed
_a64cpu_el_fault_reg_latch
Translate Stage Chosen: %d\n
failed to write memory
FEEAENL 
RF29
{astris_probed_print_events} not supported in this build configuration
virtual int ARMv7mcpu_t::_halt_hw()
AXcpu_swbp_info
_read_pc
access to target is blocked
{%s@%d} Unable to connect to server, %s:%d
RaspberryPi3_t
[ARM32cpu_t::_update_register64] 0x%08x\n
set.wp.len > 4 && addr & 0x7 != 0
sending request
astris_get_hang_crumb
Found an async abort pending; clearing it\n
ret.read.esdcr.nolog
{%s::%s} [%s] error %s reading SCTLR_ELx
FEEADR1L
Apple Fabric Timeout
jtag_cmd
Programming...\n
Parity Error on RUN-SWD Subcommand
Probe (port=%d) with unknown status %s dropped from available list
dart-type
{%s::%s@%d [%s]} Error %s: cleaning and invalidating l2cache: set=%u, way=%u
EPS3
_get_arch_hw
Probe %s selected
list
{%s} valid response from bridge
Probe %s USB-C location is %s
token.GetUint64() <= SizeType(~0)
ret.cfg_write(R_DCM_GPIO).deassert
Failed to get PMU Name
Boolean regs./reg.file
fn._write_mem.bp_info
Probe %s status: Busy
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
AMCP1
Can't get hardware model - failed to find matching IOService
Successfully connected to server, %s:%d
ARC
Found match - bypass_device: %s; channel: %d\n
{%s} [!is_64] exec: ISB_SY_ENCODING\n
[AstrisAsync] Activating async...\n
setTiming
armv7m-region-base-address
m_bp_details
RELAY
cpu_lacc_count_read
\t%s (%s)\n
Found another target for the plist\n
read_register
are_any_bp_wp_set
GROUP
AXmemap_read_modify_write
@AuthDbg,Ticket
MAC16 data register 3
There is no system bus access port on the debug port
Booster Bundle: %s\n
{%s:%s@%d} [%s] unable to read response payload\n
Dart Name: %s\n
result.read.portal.s2r_fsm
{%s:%s@%d} [%s] moving DTRTX to GPR\n
ret.spmi_read
Could not load needed symbols, please make sure HomeDiagnostics is installed\n
Table 5–177
Portal Status has an error
{%s} strsep empty so match any probe [localhost]
AXjtag_srst deassert failure - %s (%d)
[SSTEP] using BP %d\n
[REMWP] wp%d\n
EPC6
Warning
CPU3
buffer != 0
result.AXproduct_copy_bypass_info_for_bid
Match Count is Zero. This is invalid.
lower.safe.aarch32=notsupported
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_ACTUAL_LOAD
address-size
   Debug Base: %08X\n
exit
{%s} connectName[local host]
ARM32cpu_t
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} Component ID read fail for 0x%llx (%s)
{%s} FAILURE - NULL parameter
X09 Part
data_.f.flags & kUint64Flag
Gathered:\n
astris_explore_enabler_destroy
astris_setup_memap_target
Table 5–181
port
dart-coastguarded-cpu
content = %p
%04X:
Register file 22
expFrac <= 0
extract
{%s:%s@%d} [%s] writing DTRRX(first)\n
Invalid APTABLE (%d), so using most restrictive
virtual int ARMv7mcpu_t::_resume_hw(bool)
NONE
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
specified CPU is not available
{%s} Failed to extract target ID from table (%d); continuing anyway
_rw_preflight
cache_op
[INIT]\n
ret.alloc.soc_key == NULL
CPU is halted
host_get_port
cpu_hwwp_info
ret.read.stepping_stone
[AstrisAsync] Async mode %s
addr_reg=%u,page_id=%u,opcode=0x%6.6X
JTAGONLY
Selecting
{%s:%s@%d} [%s] reading WVR %d\n
Buttercup
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
_check_abort
gpr=%d
{%s:%s@%d} Took an exception that took us to exception level[%d] other than 1, 2, 3?\n
KIS Chip Found, Doing KIS Explore Setup
Register file 63
Toto
Initialized %d 1500 bridges\n
{%s:%s@%d} [%s] executing MSR (switched)\n
read memory (permission checks suspended)
Accumulator low bits
Failed to clear OCD.DSR status bits 0x%8.8XOCD.DSR = 0x%8.8X
%s/Library/Logs/Astris
ASTRIS_ERR_NOAP
.json
APCIE_ANS1
astris_get_die_count
{%s} [EDSCR_RXFULL !is_64] exec: encode_mrs(0, MDDTRRX_EL0, false)\n
elr_el3
lower_el.check.el = target_el
MISC0
Table 5–182
RF38
soc-name
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
AXmemap_read64(desc) failed
AXcpu_sstep
Too many address breakpoint regs (%u). Maximum is 2.
ret._a64cpu_raise_el_hw.after_cached_fault_reg_latch
baseAddr
[CLEANUP]\n
AXcpu_translate
AXjtag_scanout
ret.dbgap.memap_write
var.bp.invalid
cpu_hwbp_insert
{%s@%d} Timeout while attempting connect to server
Target ID: 0x%X\n
Lowering from exception level[%d] other than 1, 2, 3 [%d]?
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
{%s} Error reading PID (%s)
{%s:%s@%d} [%s] Cannot obtain the device identification\n
High level exception save location
fn._ocd_reg_w.ddr.regval_save
param.op.AXCPU_WP_DISABLE.unsupported
elr_el2
Request Dict:\n%s
internal.clear_probe_auth.chip == NULL
Table 5–147
_ocd_enable
op_ESYNC_encode
Probe %s removed during selection process
Unable to restore EL0
   {%s} (DP): status=0x%X(%s) - %s\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
MAC16 Data register 1
cpu_clean_dcache
[1500] run_steps: unknown instruction '%s'
Result while reading first entry: %s , entry val 0: 0x%X\n
clear_probe_authentication
Memory Access Port
CortexA72
current != kRegexInvalidRange
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
copyNicknameForPrimate
{%s} Unrecognized Component: %08X (class %u)
      Select port %u: AVOIDED\n
{%s:%s@%d} [%s] wait_for_cmd_end failed: %s\n
ret.switch_taps
index < stateCount_
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
Debug Base: 0x%llX\n
defaults.create.key.outofmem
New Length: %d\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
schema.h
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
!!!! Critical Error: !(prsr[0x%08X] & DLK) !!!!\n
TXU|RXO and Error Is Not Data Abort, Lets Move On\n
astris_dpabort
EXPLORE_PWRGATE
RF57
_write_general_reg_by_name
AXdisassemble_at_phys_addr
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
Breakpoint Enabled: %s
AXdebug_auth_supported
_init_configuration
fn._read_special_reg.dbreakc0
setTargetInfo
WrProt
target_el <= 3 && target_el >= 0
   {%s} Clearing HNONSEC on AP \n
AMAuthInstallSetSigningServerURL
fn._write_general_reg.regval
cpu_translate
get
ret.handle_exception.read_sysreg_hw.esr_el
AXcpu_hwwp_info
bypass-config-name
Connect
DCS_BC2
{%s} exec: DC_CIVAC_X1_ENC\n
_gen_debug_interrupt
[!ARM64] exec(DCPSX_BASE_ENC)
[INSWP] 0x%08llx wp%d rdwr=%X\n
[AstrisAsync] Discarding response due to ASYNCSKIP state!
```
