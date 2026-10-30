# `/usr/lib/libAppleHIDSWDFlash.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,379,776 bytes.

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
complex-name
[%s] {%s->%s} clear async abort
soc is NULL
ApChipID
IBREAKA0
R0
sending request
CDPUL
PAR_EL1
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
ARMv7mcpu_t
AXcpu_swbp_remove
COHERENT
ICOUNTLEVEL
RF8
_read_internal
[ARCH32] Failed to exec MRS to move contents of MDDTRRX (containing val to write) into scratchscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
fn._write_general_reg
fn._init_configuration.w2.audio.HIFI3_2
fn._read_special_reg.ibreakenable
sr=%u,ar=%u,opcode=0x%6.6X
Error %d (%s) while expanding ~ for Astris log file base\n
:usb
process_bypass_device
latching: EL%d
EXPLORE_WITH_SEP_DEBUG
Register file 9
_read_pc
\t[MATCH_MEMAP] FAIL <= unable to select AP by type: 0x%X
CalibrationReadModifyWrite
UNKNOWN CMD
instr
axi-regs
Hang Radar Info:\n%s\n
relay_set: %s = CMD_ERR (%s)
LAM
      AXap_read of R_JTAGAP_PSTA failed with error %s
Misc_CortexM
Debug Clock Already Enabled
L2 unified cache
EXPLORE_PWRGATE
AuthDebugWithTimer_t::need_to_authenticate_dft super returned true (need)\n
Can't get hardware model - failed to convert to C string
     ARM %s breakpoints: %u\n
astris_setup_memap_target
fn._ocd_exec_instr.rsr.ddr.t2
CopyFrom
{%s} [exception_level(%d) != current(%d)] exec: DRPS_ENC\n
symbol.check.loaded.AMAuthInstallSsoSetAppleConnectInfoPtr == NULL
_setup_bp
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
normal
ASTRIS_ERR_STOPCLOCK
INIT
getOrCreateObject.messages
[%s] AP, DP, or chip given is NULL
ASTRIS_ERR_DISABLED
MiniSWD (USB Comm)
reader.h
ParseTrue
param.info
ASTRIS_ERR_TOOMANY
{%s:%s@%d} [%s] reading PRSR (lsr)\n
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
{%s=>%s} null reference to SOC_t object, `cpu->tgt->chip->soc`
MESR
TRANSLATION_ERR_L1
GetSize() >= sizeof(T)
[MEM] Uncompleted; DSCR = %08x\n
{%s:%s@%d} [%s] executing MOV (diff mode)\n
Unable to read GPR %d
x28: 0x%016llx fp:  0x%16s lr:  0x%16s sp:  0x%16s\n
Failed to sync prefs at beginning
Trying to use size of 8 on not AXI bus
RF35
path
Firmware written doesn't match firmware read back
We Are Matching Development Booster\n
armv7m-region-offset
_a64cpu_read_edscr_masked
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
{%s} status=%d being reported as Unknown
invalid host name or port
{%s:%s@%d} [%s] unable to drain response\n
Complex Address: 0x%llX\n
value
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
ret._a64cpu_el_fault_reg_latch
Invalid width = %d bits.  Must be 8, 16, or 32.
CreateParallelValidator
EXPLORE
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
cpus
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
{%s::%s} [%s] error %s reading instruction (using system ap) [VA=0x%016llX, len=%d]
AMAuthInstallSsoSetStealthMode
Instruction break enable bits
fn._write_special_reg.ibreaka1.address
Caught a portal that we dont have a status map for: %d
.astris_version
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
RF12
Can't get OS build version - failed to open ReadStream
cpu_getinfo
Atomic Oper, Control
param.len.invalid.>64
Could Not Find Any Loaded Boosters of Type: %s\n
CRYPTO
_sstep
gpr < 15
CPU.ARM
Modified Word To Write: 0x%08x
Switch back to primate KIS: %s\n
Parameter length = %u > 4.
%s
offset = %d
ret.astris_ide_get_dbgwrap_base
clear_probe_authentication
Table 5–161
xfer_length=%u
Beginning of set
{%s} unable to find single_port probedaemon on port %d
virtual int CPU_t::resume(bool)
fn._ocd_exec_instr.xsr.ddr.t1
reg.ocd.dsr.stopped.invalid.cpu_running
!!!!!!!!!! Please enter the following commands to set proper permissions:\n
kon
Failed to convert kisLoc %s to unsigned long long
{%s@%d} Timeout while attempting connect to server
entry.exception_test_1
{%s:%s@%d} [%s] executing VMOVR\n
unable to read memory (using system ap)
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
\tLeft Over Chunk Read Failed\n
ClassName
DCS_BC5
AXjtagap_explore
--> localwrstn size=%3d debug=%d
GFX
{%s} Thread %#llx key %lu copping when not attached to info %p - IMPLIED ATTACH
Chip %x Status = %d\n
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Table 5–178
fn._ocd_reg_w.dsr.regval
{%s@%d} IOServiceClose failed, err = 0x%08x
BoosterPublicAPI
cpu-xtensa-num-bp
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
IOPlatformExpertDevice
connection created
{%s@%d} {%s[select]} %d(%s) [RETRYING]
prettywriter.h
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
{%s=>%s} null reference to AXtgt_t record, `cpu->tgt`
RF28
Register file 53
%s.%s
Please run one of the following commands to collect a jebdump:\nFrom Astris Console: jebdump\nOR\nNew Astris Session: astris %s  --xpl aponly --script /dev/stdin {} <<< \"::astris::jebscantools::jebdump\"\nCreate a radar with the jebdump zi
general error reported by probe
AXcpu_getmode
AXchip_get_stm_dockch_list
AXcpu_cleaninv_dcache
enable_timer_ovr
Short Packet
%s_%d
15002APB
{%s} Error KIS Size < 4: count: %d xferbytes: %d total_bytes: %llu
AuthDebugWithTimer_t destructor \n
## dpr 0x%02X -> 0x%08X\n
32 
AXcpu_hwwp_enable
ParseNull
Invalid CPU Booster. CPU Boosters Require DBG Arch To Be Set\n
darts
m_core_api_serial_queue
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_c_api.cpp
_a64cpu_write_vfpreg_hw
Warning: Default logging location requested when running as root (using [%s])\n
Probe %s removed during selection process
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
1.0
AXconn_kis_get_stm_probename
AMCNP_GFX
astris_memap_debug_writebuf
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
sso_user.conn == NULL
!Base::hasRoot_
pmu-name
!!!! Critical Error: batch attitude thread must be active when checking usage !!!!\n
{%s:%s@%d} [%s] writing CSSELR[L1-D]\n
Replacing key with value
Variables not setup
Connection aborted: kick required for probe %s.  Received eof in stdin
is.Peek() == '{'
personality[%s] missing
fn._ocd_exec_instr.rsr.reg_srn.t1
LCDCTL
...
CPU Core Number: %i\n
cpu-xtensa-num-intr
Failed to find a product plist for this soc %s
RF57
PROBED_USB_REQ_TIMEOUT
cpu_hwwp_enable
UNKNOWN
{%s=>%s} null reference to AXcpu_t record, `cpu`
NONE
{%s} UNKNOWN (type_hint present): name=%s, base=0x%llx, type_hint=%s
XACT
Top
{%s:%s@%d} [%s] doing IR scan (DTRTX INTEST)\n
localhost with name matching %s
IRSCAN
Invalid object or key for engineer array
AXportal_reset_dcm
baseReg
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
AXdebug_auth_get_probe_timer_count
Table 5–129
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
Creating NXP Flasher\n
mempool-dmem-offset-reg
NUB
Magic does not match: %#x vs %#x\n
copyNickname
Unable to register assert upcall %s (Insufficient memory)
Misc_NoSoC
{%s:%s@%d} [%s] getting GPR 0 (switched)\n
{%s::%s@%d} [FALSE] src_gpr[0x%08X] & SYSREG_TYPE_MASK == 0\n
{%s} Failed to get watchpoint mask for %s: %s
_log_setup_thread_specific
NOTEXPLORED
setup_booster_soc
sib-network-wrstn-reset
AXcpu_collect
EDDTRRX
     0x%016llx: ERROR\n
HIFI3_1
fn._ocd_reg_w.ddr.1
EpilogueProperties
{%s:%s@%d} [%s] updating CPSR\n
internal.get-timer-count.chip->soc == NULL
DBREAKC0
RF13
RASID
connection about to be destroyed
instance
Xtensa Option num_wp: %d
target power is OFF
MEMAP_APB
ret._release_gateway_control
co_coredump
{%s::%s} prsr = 0x%08X - need to clear OSLK.\n
_a64cpu_lower_el_hw
x%i:  0x%016llx x%i:  0x%016llx x%i: 0x%016llx x%i: 0x%016llx\n
hwbp_enable
BT_MAC
{%s:%s@%d} [%s] writing DSCR\n
A
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
MAC16 data register 1
RF17
ASTRIS_ERR_ASYNCSKIP
Probe %s with unknown port response %s
Failed to get KIS translator version\n
{%s:%s@%d} [%s] executing LDCpi\n
[%s] cop %d -> 0x%08x\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
Error detected
cpu_lacc_bp_status
dtoa
get_soc_resource_filepath
IMX
Failed to raise EL to %d to read register: 0x%llx
base_reg < 15
{%s} MEMAP accesses using KIS >= 4 bytes size * count must have start and end address 4 byte aligned (addr=0x%llx, size * count=%lld)
Table 5–149
[1500] %s step %d: unknown instruction '%s'
read-back (sys AP) did not contain SW BP instruction
AXcpu_readmem
Tarsier
CortexA8
\tAligned Read Failed
Table 5–160
Register file 16
JTAG chain not yet explored
[%s] %s
PKA Base: 0x%llX\n
Invalid parameter exec_path = %d
ARM64 SWBP not supported in T32 mode
couldn't read TCR
Failed to write reg_addr=0x%llx val=0x%llx
RF62
fn._resume
Full JSON that failed validation:\n%s
fn._read_pc
\t[MATCH_TARGETID] FAIL <= unable to find DP
Passed NULL booster without custom plist\n
M3_ROM
ret.test.2.0
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
virtual int ARM7cpu_t::_resume_hw(bool)
RESUME
AXcpu_nmi
Xtensa Option reg_file_size: %d
preflash routine returned error
astris_ide_get_cps_fsm
{%s:%s@%d} [%s] reading BVR %d\n
1
AXcpu_lacc_pipe_set
IDE ACCESS OUT OF BOUNDS
target is probably resetting
Connection aborted: kick required by probe server
[KIS] Words (Read/Write/Wrote): %d\n
Table 5–170
KIS-Null
SRSTM
Async is disabled for current seesion
EXPLORE_NO_TAP_RESET
host_get_port
koko
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Error Reading Device Production-Fusing\n
Append
bypass-config-name: %s\n
Portal Group Offset: 0x%X Entries: %d\n
ret.getCpuEnableStatus
[%s] CPU BM Not Found, Bailing\n
AXcpu_lacc_bp_status
no SOC object available
CIP Type: 0x%08X (%s) - Aperature Size: %d MB\n
astris_ide_get_pid
{%s::%s@%d [%s]} Error %s: pre_resuming HW
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
Buttercup
{%s} pmgr status=%d being reported as Unknown
AuthDebugWithTimer_t::need_to_authenticate_helper timer less than 1 day [0x%0X] (need)\n
products_
CTI_CTL
defaults.board.not_connected
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Table 5–168
ASTRIS_ERR_TGTSTATE
ASTRIS_ERR_FDSETOVERFLOW
cpu_resume
[KIS] Portal Status: 0x%X\n
CPU at Index: %d has to specify only one AP Type or AP Select\n
gpr=%d
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
{%s} found single_port probedaemon on port %d
OPEN
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
_a64cpu_encode_ldrstr_postinc
astris_cpu_mmu_get_config
setup_bp.not_halted
cpu_hwbp_enable
operandStack.GetSize() >= sizeof(Frag) * 2
Looking for form-factor channel: form_factor='%s', key='%s' for device '%s'
AMCP3
{%s:%s@%d} [%s] executing STRHpi\n
Astris-%d.%d.%d~%d
cpu_sstep
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Get
typehint
CSE
{%s::%s} [%s] BP_INSERT failed: failed to set halting debug
{%s} DEVARCH read fail in CoreSight component (%s)
usb
{%s} flags:0x%08x
CortexA5
SkipProperties
{%s} Thread %#llx clearing key %lu
{%s:%s@%d} [%s] reading PRSR (!oslsr)\n
error %s reading DAP MMFR0
Failed to explore chip: %d
fn._read_cfg_reg_0
no data when data expected
{%s} %s
MemoryBlock_t
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
read_dbg failed to access R_v7M_CLIDR
[AsyncSnapshot] ===== START DUMPING %zu SNAPSHOTS =====\n
ASTRIS_ERR_NOTFOUND
COMMIT
connecting to selected probe (single_port)
(%s)
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
OCD.DSR=0x%8.8X
_%04d-%02d-%02d_%02d.%02d.%02d
SRST
translate_par_with_stage
AuthDbg,BoardID
CS-ETB
DBGWRAP_PAUTH
{%s:%s@%d} [%s] reading DFAR\n
{%s} [EDSCR_RXFULL is_64] exec: encode_mrs(0, MDDTR_EL0, true)\n
_a64cpu_check_edscr_err
{%s::%s} [%s] MMU not active - returning %s
Successfully Authenticated\n
{%s} Failed to extract ECID from table (%d); continuing anyway
%s:0x%llx:%u:%u
fn._ocd_reg_r.ddr.t1_save
astris_ide_explore_release
{%s:%s@%d} [%s] updating DFSR\n
AXarm7_dbgread
[AstrisAsync] Deactivate while async is not active!\n
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
%s/%s%s.bin
Awaiting response from Probe Map Server
astris_ba_uses_attitude
AXarm7_dbgscan
setCategoryValue: path='%.*s'
Failed to find member after adding to document
ret.astris_get_dbgwrap_sys_addr.astris_soc_get_applesoc
mempool-base
opcode
## ARM32cpu_t::read_register %u\n
{%s:%s@%d} [%s] getting GPR 0 (COP)\n
   ROM entry %d (level %u): AVOIDED\n
M1
RF0
RF37
ret.transfer.half_duplex
_a64cpu_set_singlestep
JTAG IN CONTROL
reg_addr_offset=0x%4.4X, m_ocd_base_address=0x%8.8X
param.addr_reg.invalid.>15
pnav_drop_probe
' written at document root (failed to create parent object '
Miss exponent in number.
SETTHREAD
internal.is_probe_authenticated.debug_auth == NULL
op_SDDR32_encode
{%s} host name(RSD): %s\n
%s_probe
GetHashCode
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
AXdebug_auth_clear_sso_user
General register 7
The debug port associated with this chip has not been explored.
Could Not Allocate Booster Location Array
read_register
DESIGNER_APPL
Page table virtual address
special reg. number %u not present
param.reg_name.invalid.<0
%s\n
cpu-dbgwrap-offset
{%s:%s@%d} [%s] doing JTAG scan (DTRTX)\n
Astris-%d.%d~%d
_check_exception
hwbp_insert
%s (addr=0x%llx)
Register file 13
LOSTCONN
is.Peek() == 'n'
soc-name
data-size
ret.cpu.nmi()
Instruction break 0 address
SOC_t::{%s} null reference to AXcacheinfo_t record, `info`
.user
cpu-xtensa-options
Address offset, addr_lo, addr_hi: 0x%X, 0x%X, 0x%X\n
fn._insert_data_breakpoint
_setup_instr_bp
KIS
Section 5.3.6
Error!! Invalid Directory path (%s): errno %d, strerror \"%s\"\n
Unable to allocate memory for next part of big response
_update_register32
astris_memap_bus_write
internal.get-timer-count.chip == NULL
General register 8
Can't get hardware model - failed to allocate data string
End of set
invalid aod-type
DEMCR write failure - %s (%d)
{%s:%s@%d} [%s] setting GPR 0 (CPSR)\n
{%s:%s@%d} [%s] performing single step\n
]
astris_cpu_status
   Debug Port: Trying SELECT %X\n
unexpected req_type argument
{%s::%s} EDSCR with RXO set - recovered (retries=%d).\n
INTDIS
Instruction count level
Register file 62
Unable to connect after multiple attempts:\n%s,\n%s
BYPASSCH
Problematic JSON value:\n%s
EndObject
eam
DCS_BC2
preconnect
{%s@%d} Astris encountered too many open files while creating probe connection socket.\n    File descriptor returned from socket() call is %d, while FD_SETSIZE is %d.\n    Astris relies on synchronous I/O multiplexing via select() call, thu
Clear
dtoa.h
fn.exit ERROR
_sw_breakpoint_remove
Table 5–137
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
ret.dock_disconnect_mode
read
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
mxwrap-address
virtual int ARMv7cpu_t::_resume_hw(bool)
{%s::%s} [%s] BP_INSERT _insert_breakpoint[%d] failed (%s)
fn._read_special_reg.dbreaka1
_return_from_debug_interrupt
setResult
lower.safe.el=invalid
[ARCH32] Failed to exec MSR to move scratch containing sysreg to MDDTRTX.scratch=%d, sysreg=0x%X, regname=%s
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
HardwareWatch
OCDID
/System/Library/CoreServices/SystemVersion.plist
TCP send
elapsed_seconds
Failed to write JSON
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
_set_bpwp
fn._ocd_exec_instr.TIECompleteRead
cpu_mmu_get_config
ret.cfg_write(R_DCM_GPIO)
dcm
PRORES
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
sso_user.sso_user == NULL
v8@?0
preflash-type
ADI
ASTRIS_ERR_INVALCOMMAND
diagnostic_checks
description
SOC
using standard products.plist for %s
MR0
General register 15
op_XSR_encode
XSTAT
param.subsystem == NULL
astris_explore_enable_subsystem
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
mmu_init
[AstrisAsync] Deactivating async...\n
AXcpu_translate_par
GROUP
Imago
{%s} Failed to extract IDCODE from table (%d); continuing anyway
reading address: 0x%llx
We got data abort reading CPU address: 0x%llx
 %02X
Table 5–151
cpu_translate
Key is null
=== Found %s Boosters ===\n
/
armv7m-region-type
AMAuthInstallCreate
cpu not halted
PROBED_SLEEPING
itoa.h
Multi target booster, checking for %s.plist\n
ret.restore_el.read
_clean_invalidate_l2cache_setway
astris_create_ap_slave
AXchip_find_dap
param.reg_name.invalid
fn._ocd_exec_instr.l8ui.r1.r0
WARNING
xtensa-non-tie-range-base
CPU.ARMv6
{%s::%s} ERROR %d(%s) pre_resuming %s\n
AuthDebugWithTimer_t::need_to_authenticate super returned true (need)\n
ITLBCFG
No Success after retry on wait
probe [port %u] on host %s
Tiny-Core
R8
param.bp_index.invalid.outofrange
createClientList
result.astris_identify_load_booster
{%s:%s@%d} [%s] checking for data abort\n
localhost
ARMV7EM
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llX) - reg_count=%d - val=0x%X
AstrisArmProbeServer-3679.40.30~172 (RavePopB tools)
tc1500
check.el.after.exception_hanlder
astris_memap_lmflash
Invalid category
[%s] Executing instruction=%llx
_a64cpu_raise_el_hw_safe
Unaligned Read @ 0x%llx Width: %d Bytes: %d
Invalid reg_index %u
ret.check.offset_for_content
[%s] L1 icache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s:%s@%d} [%s] executing MRRC\n
SCTLR_ELx
DCRSET
reg_srn=%u, \"%s\", regval=0x%8.8X
!*!*!* Lightning header facing up.                                                    !*!*!*
AuthDebug_t::need_to_authenticate_dft DBG_RO_AUTH_ACTIVE reg: 0x%X\n
HTTP transaction running in background
Exception occured after executing MRS to bounce through scratch register
EXPLORE_WITH_SISP
Probe %s with unknown kick response %s
cpu_lacc_count_insert
Parent key is not an object
ParseStringToStream
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
LMFLASH
Not Creating CPU: %s\n
transact
FPB
Failed to read transfer register (EDDTRTX)
CPU has no regions, maybe powered off?\n
MAC16 Data register 1
%s %s\n
cpu_get_cl4_debug_signpost
** Add the --with-force option or use the explore_override console command **\n\n
{%s::%s@%d} [FALSE] gpr[%d] < GPR_COUNT\n
!!!! Critical Error: (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0 !!!!\n
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
Kick has been requested by probe server
1970-01-01T00:00:00Z
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
TRST
level_stack_.GetSize() >= sizeof(Level)
ret.is_current_state_aarch64
consumedAcmds
_reg_desc_lookup_by_name
Hardware model: %s
UserCreated
M4F
EXPLORE_WITHOUT_PIO_SAFEGUARDS
deleteClientFromList
{%s} invalid data width %d bytes
!!!! DART Key %s is INVALID !!!!\n
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
SoC
astris_setup_jtagap_target
SoC BM Not Found, Bailing\n
token.GetUint64() <= SizeType(~0)
explore_pid
RF40
ARC
loadSchemaForCategory
We are Deallocating\n
{%s} Thread %#llx key %lu resuming when not suspended for info %p - IGNORED
{%s::%s} read OK but took %d tries
da_base == 0
debug-acsr
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
param.tgt->ap.null
AXjtag_spixact
Original Length: %d\n
R12
[ARCH32] Failed to read transfer register (EDDTRTX)
init_hw.read.fpb.rev
AXcpu_writemem
   {%s} Clearing HNONSEC on AP \n
RF25
status=%u, flags=%u, DSR=0x%8.8X, DCR=0x%8.8X
Only Auth-Debug, Auth-DFT and Probe-Auth are currently supported.\n
_cleanup_hw
{%s} probe_match = %s
write.sysreg.el_check
{%s->%s} START handling exception
ret._mmu_init
AXmemap_readvals failure - %s
Form-factor specific channel not found, falling back to generic channel for device '%s'
{%s:%s@%d} [%s] unswitching register set\n
## dpw 0x%02X 0x%08X\n
_write_special_reg
astris_json_logger_delete
{%s:%s@%d} [%s] writing ITR\n
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
fn._ocd_reg_w.DIR0EXEC.instr_32
astris_jtag_scan_stay_gotorti_impl
MAC16 Data register 2
General register 2
connection not currently open
{%s}#%02X cmd: %s, resp: %s
?
extra-wrstn
DBGWRAP_LITE
WindowStart
fn.param.name.null
ASTRIS_ERR_DISASM
Unique required when more than one probe identified by
{%s} bridge returned an error
Booster:\n
CPU.ARM7
regidx_restore=%u
ASTRIS_ERR_NOAP
\t[MATCH_TARGETID] %s <= AXdp_read(ap, 0x%08X, &value)
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
Failed to populate portal info
astris_user_default_remove_all_boardnames
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
ARMV4
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/socs/astris_explore_override.cpp
Failed to safe raise to EL=%d
_a64cpu_encode_mrs
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS == 1 (expired)\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_COUNTER1
DDR
KIS-SIM
cpu_hwwp_info
sel-sib-network
socnames
ret.clearing-async
Generated JSON (first 500 chars):\n%.500s%s
str != 0 || len == 0u
dfu-type
[%s] %d -> %08x\n
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
ret.reg.write.K_DA_REG_NAME_AUTH_TIMER_LOCAL_LOAD
AXconn_kick
Invalid escape character in string.
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
fn._ocd_exec_instr.l32i.r1.r0
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
{%s} Batch attitude of %p thread %#llx key %lu is to be destroyed
%s probe[*] from Probe Map Server [%s]
is.Peek() == '['
cpu-address
{%s:%s@%d} [%s] reading PRSR\n
[%s] error reading EDSCR
ENABLED
{%s} Failed to get breakpoint mask for %s: %s
{%s} 0 words requested for read at address 0x%016llX
DPAP
{%s:%s@%d} [%s] updating ADFSR\n
L2
primateLoc
UNKNOWN 
CPU %s already in the map with status: %d
exit.exception_test_0
[AstrisAsync] replay preflight: replay_counter %lu, barrier_hit %u, last_replay %u, last_batch_size %zu, completed_commands %zu\n
sstep
BT_PHY
baseAddr
ocd_base_address = 0x%8.8X is not 4 KByte aligned
astris_batch_attitude_lose
Took an exception in EL%u, esr = 0x%08llx, category = 0x%llx\n
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
Invalid encoding in string.
cpu-explore-flag
enable
CLIDR
Length is 0
   {%s} Read AP's R_MEMAP_CSW\n
VECBASE
_get_arch_hw
Xtensa Core %s NOT configured\n
DOCK-CH-CONFIG
!!!! Critical Error: Error %d(%s) deleting info %p batch_attitude_key !!!!\n
ASTRIS_ERR_PORTAL_STATUS
PROBED_USB_RSP_NODEVICE
{%s:%s@%d} [%s] reading PRSR (!lsr)\n
{%s} %s resumed\n
authenticate_dft
setTargetOS
[REMBP] bp%d\n
Table 5–150
_write_window_base
operation not supported
reset_connect_state
source != __null
aod_type
far_el1
gpr < 32
{%s} astris_command(JTAG,EXPLORE) successful after %d tries
astris_soc_check_debug_root
wir-tdo
dpb-size
{%s} asc status=%d being reported as Unknown
pid
AXjtag_srst deassert failure - %s (%d)
_clean_dcache_vaddr
{%s::%s} [%s] !bpwp_initted, retrying init
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
cpu_mmu_walk_detailed
astris_ide_get_deid
astris_ide_get_cpu_halt_group
cpu_mode
size >= SIZEOF_SHARED_DATA + SIZEOF_CHUNK_HEADER
current != kRegexInvalidRange
{%s} FIFO full, try again
class_var.m_interface_name==NULL
Stop Clock: %s\n
no MEMAP access
ASTRIS_ERR_MISSINGPARAM
Unable to connect to
ret.fromreset
{%s::%s@%d [%s]} Error %s: resuming HW
n't
General register 9
{%s:%s@%d} Critical error encountered:
connecting to probe by port number
Kicking
Img4DecodeGetPayload failed: %@
AXcpu_clean_dcache
ASTRIS_ERR_EXPIRED
cpu_status
Couldnt MSR: 0x%llx
fn._setup_instr_bp.bp_state
_create_cpus
AXdebug_auth_get_timer_count
fn.unsupoorted
fn._ocd_exec_instr.rfdo
Can't get hardware model - failed to allocate data buffer
set.chip_id
   Mem-AP Sel %u ROM Base %08X (cfg = %08X)\n
ret.reg.read.K_DA_REG_NAME_PRODUCTION_MODE
X06 Part
R7
Probe Map Server Information: %s
pointer.h
AVE
SPSR_ELx
_clean_invalidate_dcache_vaddr
EICE chip %x initialized\n
fn._ocd_reg_r.dsr
ObjectEmpty
_a64cpu_clear_async
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
PARTNO_DAPLITE
SWD KIS Command is NOT Multiple of 8
Hang Address: 0x%016llx\n
already connected
HENRY
Dock-Channels
handle_pending_async_aborts
{%s::%s} [%s] INS_SWBP %s [VA=0x%016llX, index=%d]\n
param.tgt.null
~/Library/Application Support/Astris/astris_prefs.plist
val =0x%X is too large for 32 bit unsigned.
Invalid data breakpoint index %d
XBS Version Modified: %s -> %s\n
~A
!!!! Critical ERROR: current_el[%d] != m_exception_level[%d] after exeption handling
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
AXdebug_auth_clear_probe_auth
COMPARE1
Table 5–157
Input
Could Not Create Dictionary From Booster: %s
PropertyValue
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
EDITR
dest_reg < 32 || dest_reg == 31
   Debug base is in legacy format\n
Server Response Does Not Countain Ticket\n
AXdebug_auth_is_dft_authenticated
astris_ide_get_boardid
wb_u32=%u
_insert_instr_breakpoint
debug_info
INVPARM
PROBED_USB_INUSE
cpu_writereg_vals
GetSize() >= count * sizeof(T)
True
[%s] {%s->%s} END handling exception
_a64cpu_el_fault_reg_latch
High level 3 exception PC
param.num_addr_bp_regs.invalid.2
v%s.%s
Kick error while communicating with probe server
type >= kNullType && type <= kNumberType
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
ret.write.msr_lock_reg
Hang Description:\n%s\n
[1500] %s step %d missing required field 'instr'
Protocol Version: 0x%X\n
resolve_debug_components
GPR
Table 5–184
{%s} [%s] m_exception_level=%u\n
Probe %s status: Idle
Complex CPU ID: %d\n
[ARM64 INS_WP] wp%d wvr=%016llx wcr=%08x\n
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
fn._gen_debug_interrupt
address=0x%8.8X,page_id=%u
{%s} Failed to extract PID from table (%d); continuing anyway
ret.createKey
INVALID KIS VERSION
RF16
ASTRIS_ERR_CPUHALTED
Incorrect hex digit after \\u escape in string.
AXcpu_mmu_get_tsz
probe on host %s
{%s@%d} {%s[select]} ret=%d(%s) waiting for connection to complete
BoosterManager.Utility
couldn't read TTBR1
\t%s\n
{%s} write[ED64] of %s @ address 0x%016llX [%s] ERROR %d(%s)
AXcpu_lacc_count_clear
Gateway is KIS, seeing what probe this is\n
Table 5–166
R10
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger_components.cpp
imgExtractPersonalities failed
result.read.memap.s2r_fsm
[INSWP] 0x%08llx wp%d rdwr=%X\n
AXcpu_status
RF56
ERR
instruction size too large
{%s} explore with exploreflags 0x%X complete [%d chip%s]
New Length: %d\n
op_LDDR32_encode
pnav_req_rsp_probemap
ARMV7
Connection is NULL, might not have found something to connect to.\n
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
enable_test
AMAuthInstallSsoInitialize
MemoryPoolAllocator
Values Not The Type We Expected. Expected: Number and String or Number and Number\n
[1500] v2 plist missing required field 'bridges'
AXexplore_set_explicit_mode
ERROR!! Wrote %zd bytes, expected %zd\n
Not Enough Payload For Specified Bits To Shift In OR Write Data Length Mismatch
time out reported by probe
META
SCANDEBUG
{%s} read ESR EL1|EL2|EL3 (%d)
astris_handle_romentry
stdout
relay
_a64cpu_is_current_state_aarch64_hw
_remove_data_breakpoint
SWD_BYPASS_REGS
internal.clear_probe_auth.debug_auth == NULL
ParseStream
Failed to connect to AppleAstrisGpioProbe kext %x
resolve_portals
Main
SCOMPARE1
fn._ocd_exec_instr.rsr
{%s:%s@%d} [%s] getting GPR 0\n
api.is_prod.debug_auth == NULL
cpu_getmode
CPU DBG Ack: 0x%llx\n
DISPDFR
PARTNO_ARM7TDMI
Failed calling AppleSOC_t::dock_disconnect_mode\n
AlignBuffer
Dart Coastguarded CPU: %s\n
CTI_OUT_EN0
SPSR_EL3
{%s} error %s from astris_command(JTAG,EXPLORE) - retrying
SSO info present but SSO disabled.
param.wb.invalid.>wb_max
{%s[select]} ret=%d(%s) waiting for data from the connection (at select)
RESPONSE_PAYLOAD
match-info
CG
haskis
AXcpu_translate
param.reg_name.invalid.unimplemented
General register 12
address=0x%8.8X, len=%u, rdwr=%d
{%s->%s} current EL (%d) already == target EL.\n
ATS1Eop
internal.enable-timer-ovr.chip->soc == NULL
Unknown Command
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
probe matching %s on host %s
{%s} bridge returned DECERR
Portal Config Write
{%s} %s Halting is NOT set. BP/WP wont work. (dscr = 0x%08X) \n
{%s:%s@%d} m_exception_level[%d] == 0|1|2|3\n
completedAcmds
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
TRANSLATION_ERR_L3
{%s:%s@%d} [%s] Unable to allocate drain payload.\n
spsr_el1
ret.memap.read
{%s} FAILURE - max length exceeded
ide_checker
AXbooster_print_loaded_boosters
PFR0_LO
{%s} FAILURE - NULL parameter
ret.alloc.soc_key == NULL
MISC3
RF52
param.num_data_bp_regs.invalid.2
{%s@%d} resp is too large to fit into max packet size (%zd > %zd)
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
EXPLORE_DAPONLY
fn._ocd_reg_w.ddr.address
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
message
DCS14
%d > %d
{%s} Failed to upgrade placeholder for %s (res=%s, new_cpu=%p); marking as powered off
{%s} creating CPU (name=%s, arch=0x%X, ID=0x%X, IMPLEMENTOR=0x%03X, PART=0x%03X)
Literal base
R1
RF36
ASTRIS_ERR_EENOTFOUND
Could Not Get BoosterManager\n
reset-network
RF46
pon
SPIXACT
GETRELAY
rhs.GetType() == kObjectType
SID
AuthDbg,EnProbeFuncExternal
IBREAKENABLE
CopyPart
index < rangeCount_
tap
astris_user_default_set_boardname
Mask condition met in conditional operation
Put
[KIS] Address: 0x%llX\n
{%s::%s@%d} [FALSE] reg[0x%08X] & SYSREG_REGID_MASK < NUM_ENCODINGS\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armcpu.cpp
AXjtag_scanout
dbgwrap
{%s@%d} Connection to server failed, error=%d (%s)
read_via_sock
Portal Group Base: 0x%llX \n
_clean_l2cache_setway
{%s::%s@%d} [FALSE] instr[0x%08X] & MSR_MRS_BASE_MASK == 0\n
{%s} cleaning coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
MEMAP
DIAGS
AXchip_fromreset
ret.exec.mrs.sysreg->scratch
{%s::%s} [%s] secondary error %s invalidating instruction cache [VA=0x%016llX]
ExcCatch
AMAuthInstallLogSetHandler
Error level
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
_D
BoosterManager.SOC
Restoring to exception level %u. - SPSR_ELx=0x%x - DSPSR=0x%llx\n
storeNickname
AP[%d]: MEM_AP_AXI\n
ASTRIS v%s%s [%s]
list
Failed to read ide_table from KIS explore
astris_explore_enabler_del_cpu
Found an async abort pending; clearing it\n
Only Auth-Debug, DFT-Auth and Probe-Auth are currently supported.\n
ASTRIS_ERR_OK
astris_json_logger_delete_all
CalibrationLength
AXbooster_get_all_boosters
[INS_WP] 0x%016llx x %d\n
AXdp_write_with_recovery
internal.clear-auth.chip->soc == NULL
Prefix
DEMCR read failure - %s (%d)
ret.lower.after.read.aarch64hw
internal.is_authenticated.debut_auth == NULL
{%s} host:%s, flags:0x%08x
Issuing request to Probe Map Server: %s
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
cpu_mmu_get_tsz
{%s:%s@%d} [%s] reading CPSR(2)\n
nothing written
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
fn._write_pc
param.shift.invalid.out_of_range
ASTRIS_ERR_NOCPU
astris_command
missing property aod-type
{%s:%s@%d} [%s] switching register set\n
[AstrisAsync] replayConditionalCheck: Discarding completed commands!\n
[iter %lu] after_codeblock_execution
AXjtag_setclr
JTAG level control
{%s} DAP command nwords=%d trimmed to %lu\n
In Preflash\n
AP[%d]: unknown type\n
ETM
Error returned from explore_pid
IBREAKA1
MISC2
SWDFlashRead failed: 0x%08x\n
%s: Didn't find client in dictionary
_write_memory_fast_try
runBlock
AXchip_is_prod_fused
_ocd_reg_dcr_clr
SoC clocks are stopped. No MEMAPs allowed 
Complex Type: %s\n
_read_gpr
CPU[%s] Read Reg: %d
Register file 31
operation still in progress
ASTRIS_ERR_VARNOTFOUND
L1_DATA
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
.name
SWDFlasher.API
Invalid character [0x%02X] received from Probe Map Server
addMember
{%s:%s@%d} Restoring from exception level[%d] other than 1,2 or 3\n
param.conn.connected == false
{%s} Failed to single-step %s: %s
Loop count
connected
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
cpu_cleaninv_l2cache
AddState
{%s:%s@%d} [%s] setting GPR 0\n
{%s->%s} exec: aarch64_add_imm(REG_SP, scratch=%d)\n
EICE
astris_poll_cmdstat
   {%s} Explore index 0 < 0xf00 [step 4] (rombase=0x%llx)\n
reg.ocd.dsr.invalid.not_cleared
fn.AXmemap_write.address.regval.
IOCFUnserializeWithSize returned non-dictionary of class: %@
Invalid bp = %u. Should be in range 0..1.
ERROR!! write binary data parameters invalid\n
relay_set: %s -> %d
DISCONNECT
dbgfifo
\n!!!!!!!!!! No Astris log file in use for this session !!!!!!!!!!\n\n
{%s->%s} [is_64] exec: DRPS current_el(%d) -> target_el=%d \n
## apr %u 0x%08X %d -> 0x%08X ...\n
Invalid special reg. number %u
mismatch detected
{%s} %s did not match any valid host
In Readflash\n
irlen
%04X:
ASTRIS_ERR_BLOCKED
ACQ_STARTSTOP
device==IO_OBJECT_NULL
Missing property aagp-name
low word
[AstrisAsync][COMPARE] acmd2->cmdbuf:\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
cpu_resume_translation
is_ecid_zero
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
Preferences does not exists: %s, creating one.\n
DBREAKC1
ban
{%s:%s@%d} [%s] unable to transfer command\n
Setting bypass channel to: %d\n
wir-wrstn
{\"max_events\":%u,\"events\":[%s]}
ret._a64cpu_read_vfpreg_hw
hwbp_disable
fn.var.exec_path.invalid
local host
Failed to read DCM GPIO (0x%x)
soc-pid
Complex ID: %d\n
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
{%s::%s} halting %s\n
Failed to write SPS_EL%d
Register file 30
{%s::%s@%d} [FALSE] postinc[%d] < MAX_IMM\n
Target ID: 0x%X\n
{%s:%s@%d} [%s] executing LDRBpi(1,0,1)\n
{%s::%s} [%s] WP_INSERT failed, failed to set halting debug
fn._ocd_reg_r.ddr.memval_tgt_32
ASTRIS_ERR_INVAL
param.portal_base == 0
DLOPEN ERROR: %s \n
AuthDbg,TicketIdentifier
fn._ocd_reg_dcr_set.debug_interrupt_msk
UNKNOWN_PORTAL_ERROR
wrstn-partition-number
%#09llx-%#09llx: %s\n
Failed to find a plist for this soc %s
ret.read.edscr.after-drain
Register file 14
Register file 49
SLEEPING
ret.reg.read.K_DA_REG_NAME_PKA_BASE_LO
Didnt match any service/parent for AppleAstrisGpioProbe
fn._ocd_reg_w.ddr.t2_save
astris_json_logger_delete_category
setTiming
CPU ASC Offset: %d\n
Failed to restore EL to %d after writting register: 0x%llx
{%s} _halt_hw result = %s
Type 'jebdump' to do scan/mem dump\n
ret.pka.nonce.status.err
%s.console.%s
Bug detected
ASTRIS_ERR_PROBECOMMAND
-
get_page_shift
{%s::%s} [%s] WP_DISABLE _set_bpwp[%d] failed (%s)
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_dapcmds.cpp
op_ISYNC_encode
Connection aborted while choosing probe
{%s@%d} Unable to create socket
XPROG
!!!! Critical Error: Thread %#llx key %lu suspending when already suspended for info %p - IGNORED !!!!\n
[AstrisAsync] replay preflight: Async not active!\n
AXcpu_cache_info
???
fn._ocd_reg_r.ddr.tgt_32
setToolInfo
{%s->%s} current EL (%d) already >= target EL (%d).\n
framework_url == NULL
Instruction TLB configuration
Thread pointer
end
APF
Invalid object or key for addMember
%s:%s
astris_remove_loaded_cpu_boosters
{%s:%s@%d} [%s] reading OSLSR\n
dest_gpr < 32
JTAG
#ch-
SoC must have a DAP
RaspberryPi3_BCM2837
There is no debug port associated with this chip.
Gathered Value is Not Number\n
{%s} MEMAP accesses using KIS > 1 byte and <=4 bytes size * count must not cross 4 byte alignment(addr=0x%llx, size * count=%lld)
RF4
MINISWD
sib-network-psr-reset
fn._write_special_reg.dbreakc1
HOSTID=0x%x which is invalid, skipping orientation check
Connected to Probe Device Server [Default Log]
{%s@%d} Attempt to read response when rsp_drain_packets=%d.
IOCFUnserializeWithSize failed: %@
Groups %d\n
!!!! Critical Error: Error %d(%s) destroying info %p mutex !!!!\n
{%s->%s} exec: encode_msr(%s=0x%X, scracth=%d, %d)\n
SubsystemMonitor
INTENABLE
_read_cpu_reg_file
*
dart-coastguarded-cpu
_init_hw
{%s:%s@%d} [%s] setting GPR 1 (todo 2)\n
dest_reg < 15
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
Misc register 1
fn._read_general_reg.regval
xtensa-non-tie-range-name
required_el > _a64cpu_get_highest_el()
Requesting %u > 4 while address is NOT doubleword aligned
   {%s} APB/AXI address for target setup = 0x%llx\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
start rev and/or end rev is NULL; skipping cpu_desc override\n
{%s=>%s} no soc reference; falling back to direct cpu method
EXPLORE_JTAG_NO_BOUNDARY_SCAN
internal.authenticate_probe.chip->soc == NULL
Kick failed: probe no longer hosted by probe server
locationids
MiscCortex_t
document.h
ret._a64cpu_read_gpr_cached
{%s} couldn't set thread specific - %s\n
data_.o.size > 0
AXcpu_cache_cleaninv
astris_findidcode
a
Unable to connect to %s - %s
stat
MISMATCH
DISP_L
DCS12
astris_setup_placeholder
AXdebug_auth_authenticate
Long Packet
component
[1500] TAP key is not a valid integer
EXC_TRACE(exc_throw): %s(%04u): %s(): %s: %s\n
_a64cpu_lower_el_hw_safe
symbol.check.loaded.AMAuthInstallCreatePtr == NULL
MISC1
getOrCreateValue
ret.write_sysreg_hw.spsr_el
EL0t
{%s->%s} exec: encode_mrs(scratch=%d, sysreg=0x%X (%s), regname=%s, %d)\n
%s - runBlock
{%s} calling _collect_hw on %s
load_framework_at_path
{%s:%s@%d} [%s] %s halt failed: %s\n
=== Detailed %s Boosters ===\n
{%s:%s@%d} [%s] reading SPSR\n
AXcpu_swbp_insert
AXdp_read_with_recovery
Invalid Size Given for AP AP=%d Size=%d
Table 5–173
fn._ocd_reg_r.OCD.DEVID
{%s} [%s] EDSCR with ITO set - recovered (retries=%d).\n
astris_explore_ap_mem
MAC16 data register 3
fn._ocd_exec_instr.TIEWriteProtectedI
Temporary level
Corruption detected selecting probe from probe server
cpu_mmu_walk
{%s} no matching 1500-to-* bridge
{%s->%s} exec: encode_mov_vfp_to_gpr(scratch=%d, sysreg=0x%X, %d)\n
General register 11
15002AXI
mempool-size
MTP
ret.read.rtxcid
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT || == SP\n
ret.CFPropertyListCreateWithStream
Memory error PC register
op_RFDD_encode
{%s:%s@%d} [%s] DEMCR read failed: %s\n
{%s:%s@%d} [%s] writing DTRRX(uint32_t)\n
{%s:%s@%d} [%s] Setting WP length not currently supported: %u\n
Register file 59
{%s} drain_packets=%d [%s]
{%s} %s status is '%s' [Status Read %d times]\n
EXCSAVE3
!level_stack_.template Top<Level>()->inArray
Realloc
{%s} 0 words from probe when %d words left to read for reg %d
{%s:%s@%d} [%s] executing MCRR\n
[AstrisAsync] ASYNC_CONFIG not supported (version=%u)\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (0: debug-auth expired)\n
CalibrationOffset
{%s::%s} [%s] unsupported width %d
_update_register64
tckrate_check returned error %s
param.invalid.reg_file_index.outofrange
writer.h
from != 0
(addr=0x%llx)
EXPLORE_LOST
PTEVADDR
ASTRIS_ERR_USB_NODEVICE
DCS_BC1
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
{%s} (end) current_el is now %d
defaults.create.key.no_probe
AuthDebug_t::need_to_authenticate_probe ACTIVE reg: 0x%X\n
CPU3
result.read_vals(portal_group)==
Increasing length by: %d\n
read_settings
Accept
false
DISPEXT
matches_enabled_cpu_patterns - pattern: [%s] caused exception\n
KIS translator version : %d\n
APPLE_SUBTYPE_UNKNOWN
Connection is null
Failed to open schema file
Chip Revision: 0x%X\n
Successfully Authenticated DFT\n
DSR
Register file 19
coalesced-target
EXPLORE_GENTLY
PARTNO_1176JZFS
internal.clear_probe_auth.chip->soc == NULL
apb-regs
explore_min
Register file 46
result.alloc_table==NULL
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
Portal Status, Changing STATUS and CMD/STAT to reflect
cpu_collect
s != 0
Could Not Find Any Boosters of Type: %s\n
ASC_ECORE_ROM
Wake
AP Only Explore, failed to init soc, SoC probably does not support AP Only Identification
type_hw=%d
fn._ocd_reg_w.ddr.t1_save
INVCHIP
host_to_components
wrstn-pipes
ret.enableAll
read_page_descriptor
EXPLORE_ONE_DIE
Error %s connecting to server %s:%s [RETRYING]
GenericRegexSearch
Product Name: 
{%s:%s@%d} [%s] getting GPR 0 (ARB)\n
AXmemap_read_get_field
n >= 0 && n <= 308
output_type
aod-type
IDE
NC
Ring ASID values
AXexplore_enable_cpu_pattern
Invalid file name: \"%s\". File names must not start with '.'
_exec
fn.remove_epcn_epsn
{%s} bridge returned SLVERR
ret.board.copyPairForPref
before_deactivate_in_runBlock
fn._read_special_reg.ibreaka1
Missing a name for object member.
wpcr
{%s:%s@%d} [%s] Read DWT Comp %u\n
PS
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/xtensa_cpu/xtensa_cpu.cpp
AXconn_create
Idle
%s [RETRYING]
{%s@%d} socket connection is not available
[AstrisAsync] replay preflight: Replay still paused from last iteration. Resuming...\n
op_L16UI_encode
ASTRIS_ERR_CPUNOTHALTED
general-purpose failure
TCP recv
Failed to write DCM GPIO (0x%x): 0x%x
Could Not Allocate Loaded Booster Array
!!!! Critical Error: m_exception_level[%d] == 0|1|2|3 !!!!\n
EL1h
PARTNO_KIS
CPU with %s Not Created via Name
fn._write_special_reg.dbreaka0.address
default
EXPLORE_JTAGONLY
USB connection not currently open
Skipping CPU %s at 0x%llx: not present in IDE\n
!*!*!* Lightning probe orientation is wrong. Explore will fail, DFU won't work right. !*!*!*
Connection aborted: kick required for probe %s
[READ] cop %d -> 0x%08x\n
defaults.create.key.outofmem
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
AXdebug_auth_is_authenticated
result.extract_dbgwrap_base==
%2d) %s %s [Busy]%s\n
ret.AXmemap_read.board_id
Failed to exec DCPS in order to move EL up to %d
Data break 0 address
HTTP transaction failed
preflash_type
result.read_vals==
A32
{%s::%s@%d} [FALSE] base_reg[%d] < GPR_COUNT\n
Width: %d not supported
RF43
required parameter is missing
MISC
calOverrides[%@] isn't an NSData: %@
{%s} no TAP detected that supports 1500
CPU0
!!!! Critical Error: Took an exception that took us to exception level[%d] other than 1, 2, 3? !!!!\n
astris_apwrite
Unable to get version info from %s [error %s]
getOrCreateArray
SCODEC
{%s:%s@%d} [%s] reading CCSIDR[L2]\n
EDDTRTX
index slot not enabled
fn._ocd_reg_r.dsr.1
Arm
Failed to write register: 0x%llx val: 0x%llx
PARTNO_SWDP_M7
{%s:%s@%d} [%s] failed to setup connect\n
{%s->%s} [is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_ACTUAL_LOAD
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
fn._write_mem
Memory Access Port
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
astris_dpwrite
## apw %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
fn._collect_snr.excvaddr
probe refused to process the command
AXchip_get_chip_id
{%s::%s} HDE not set on %s. Will re-enable.
virtual int CPU_t::halt()
write_memory_dbgwrap
=== Ending Gather and Clear ===
AXbooster_interface_create_soc
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
AXcpu_writereg_vals
load_framework
StringEqual
AXdisassemble_at_addr
GRP_0
## memapw %u 0x%016llX 0x%08X ...(%d)\n
Subsystem Monitor[%i]: %s\n
generic probed USB error
CHAINERR
ret.modify.edscr.~ma
Error status from AMAuthInstallSsoEnablePtr = %i
kick
ret.relay.get.haskis
Adding new booster path: %s\n
dpb-misc-id
!!!! Critical Error: exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this... !!!!\n
\n!!!!!!!!!! Error: %d (%s) opening log file %s !!!!!!!!!!\n
RTP
fn._ocd_reg_w.ddr.reg_val
Invalid SoC Booster. SoC Booster Requires PID\n
failed write of 0x%08X to DEMCR - %s
OCD Debug data register
host %s
JSON
cpu-runtimes
exit.exception_test_1
{%s:%s@%d} [%s] reading GPR 1\n
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, &d, %d, false, %d)\n
SoC not identified by IDCODE - enumerating instead of instantiating
which_wp=%d
\"%s\" not an implemented register
status
GitHashDebug
Raising to EL2 cause in Guest\n
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
%u
ArcEM
no system bus AP present with AHB, trying AHB5
Failed to instantiate %s\n
Values Not The Type We Expected. Expected: Number and String\n
InterfaceLocked
OCD ID register
Program counter
Register file 54
environment variable not found
[AstrisAsync][COMPARE] MISMATCH: cs_flags - acmd1=0x%02X, acmd2=0x%02X\n
{%s} Error setting up jtag-ap target (%s)
COMPARE0
param.ocd_base_address.invalid.unaligned
connection to probe is lost
ViewSWD
Invalid port provided by probe server
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
Failed to convert %s key @ index %d to a number with base of %d\n
Lost
probe [port %u] on localhost
{%s} Failed to extract chip debug base from table (%d); continuing anyway
High level 6 exception PC
Section 5.2
RF27
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
%s%s
_a64cpu_write_gpr_hw
{%s} %s DC cache clean complete, marking as clean
EmulatorSWD
%Y-%m-%dT%H:%M:%S
SMX
AMCP2
EDSCR
!!!! Critical Error: current_el[%d] <  %d !!!!\n
AMAuthInstallSsoEnable
[1500] TAP %d missing required field 'ir-cmds'
result.read_vals(table_info)==
ret.reg.write.K_DA_REG_NAME_NONCE_2
_ocd_enable
_ocd_exec_instr
{%s:%s@%d} [%s] executing MCR\n
[INIT_HWBP] m_bp_avail=0x%X, m_bp_enabled=0x%X, m_bp_rsvd=0x%X
RF45
fn._ocd_reg_w.ddr.tgt_32
Probe %s status: Busy
regex_.IsValid()
{%s:%s@%d} [%s] setting DTR MODE to FAST\n
Failed to read register: 0x%llx
EPS7
fn._ocd_exec_instr.wsr
\"%s\" not a special register
ret.astris_soc_get_applesoc
using multi-target booster products_%s.plist
ret.state_valid_entry_exit
ret.raise_el.read
SWD
ApBoardID
Invalid Nonce - probably need to do ProbeAuth or EAM-authentication and retry AuthDebug\n
Can't get OS build version - failed to create plist
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_user_default.cpp
ret.reg.write.K_DA_REG_NAME_NONCE_3
Register file 29
RF63
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
{%s@%d} Unable to connect to server, %s:%d
{%s:%s@%d} [%s] Unable to increment set of packets to be drained.\n
CPU Subsystem: %s\n
{%s::%s} [%s] error %s writing SCTLR_ELx
OK: address translation suspended for %s successfully
High level 2 exception PC
fn._write_special_reg.srn.regval
wa
%s-%06d
Probe %s Device Server listening on port %d
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
dspsr_el0
probe %s [port %u] on localhost
Failed to convert kisHubLoc %s to unsigned long long
KIS-STM
GetCachedPowerByIndex
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis.cpp
CPU Name: %s\n
[HALT] Chip %x\n
AXcpu_lacc_count_insert
end rev is not of expected format; skipping cpu_desc override\n
TargetSel Before Disable: 0x%x
{%s} unaligned %d-byte access at address 0x%09llx
GPR_1
xfer_acmd_via_kext
cpu_clean_dcache
partnum
CPU PS-Register: 0x%llX\n
Failed to resolve platform details
error %s checking for data abort
ret.current_state_aarch64
fn._ocd_reg_r.ddr.regidx_save
Could not find TAP at chip-index %d for v2 1500 config\n
{%s} Failed to extract die infofrom table (%d); continuing anyway
{%s:%s@%d} [%s] executing STRpi\n
_clean_invalidate_dcache_setway
[REM_WP] wp%d\n
%d.%drelease
{%s} probe_port = %d
xres = %p, table = %p, key = %d
{%s:%s@%d} [%s] doing JTAG scan (DIDR)\n
DEMCR: 0x%08X -> 0x%08X
fn._ocd_reg_w.dcrset.regval
Error
IsObject()
{%s::%s} EDSCR in unexpected state. Returning %s.\n
Error while trying to authorize: %d - %s\n
Failed to create CPU %s - %s\n
{%s:%s@%d}\nFABRIC HANG DETECTED. JEBDUMP REQUIRED.\nContext: %s\nSoC: %s Rev: %s Address: 0x%016llx\nDescription: %s
{%s:%s@%d} [%s] failed to get kis target info\n
User created bundle found, ignoring version checking via plist
fn._ocd_reg_r.ddr.t2_save
Choose a device: 
Img4DecodeInit failed: %@
to
{%s:%s@%d} [%s] writing LOCKACCESS\n
ret.modify.edscr.~MA
_ocd_reg_dcr_r
1500 IR Commands:
AUD
fn._read_special_reg.ibreakenable.reg_bp_enables
param.as.invalid.>15
Status
{%s:%s@%d} [%s] handling pending async aborts\n
ret.CFURLCreateCopyAppendingPathComponent
fn._ocd_reg_w.ddr.wb_next_u32
fn._write_special_reg.ibreaka0.address
Error %d (%s) opening cmd snapshost save file
~
Gathered:\n
Min Component - %s\n
[AstrisAsync] AstrisAsyncSyncGuard ENTER: Async already paused...\n
Breakpoint Address: 0x%llx
{%s} hostname:%s, flags:0x%08x
cpu_swbp_insert
getOrCreateValue: addMember failed, returning doc root
ret.get_soc_resource_filepath
!!!! FILE RADAR: Don't know how to compare two values\n
CPU Address: 0x%llX\n
astris_addr_which_die
AMAuthInstallGetLocalizedStatusString
Register file 41
ASTRIS_ERR_FAILURE
Portal Access Read
UWB
Start Page: %d\n
EL1t
{%s::%s} [%s] BP_ENABLE _set_bpwp[%d] failed (%s)
Table 5–174
Memory error PS register
RF61
bits
_insert_breakpoint
fn._write_mem.bp_info
ParrotSWD
Unique required when multiple probes
VBAR: %#llx\n
AXcpu_hwwp_info
DEPC
Sprocket
PROBED
CortexR5
SWDFlashRead failed: 0x%08x
ret._setup_bp
AXcpu_go
porpath
internal.authenticate.debut_auth == NULL
AMAuthInstallApSetParameters
Table 5–156
param.reg_name.!match
Could Not Get Bundle Out Array of Found Boosters\n
armv7m-region-axim-end
ret.dbgap.memap_read
address=0x%8.8X
Target was lost while connecting to
postconnect
!!!! Critical Error:  dspsr_el0 NOT DIRTY !!!!\n
virtual int ARMv7mcpu_t::_resume_hw(bool)
cpu_suspend_translation
cpu_lacc_pipe
Unknown error.
CPU Explore: 0x%llX\n
master-debug
check_dcc
address=0x%8.8X, regval=0x%8.8X
!!!!!!!!!!   $ sudo chmod 0775 %s\n
param.invalid.content-type
ret.enableCpu
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
_resume_translation_hw
AXjtag_transmitraw
astris_dump_exploreflags
{%s} drop ProbeName %s
astris_command_async
revive
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
{%s:%s@%d} [%s] going to RTI\n
file
name.IsString()
SBR
RF15
????
AXconn_identify_soc_collateral
AXconn_port
set.os
Got an error writing 0x%X the DCM Control Register: %s
(instr & ARM64_MSR_MRS_BASE_MASK) == 0
M4
reg_name (\"%s\") not implemented, missing Xtensa option.
fn._ocd_exec_instr.wsr.ddr.t2
soc or sysap not available
line
0123456789abcdef
span
_get_bpcr_hw
{%s} exec: DRPS_ENC\n
i8@?0
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
param.no_dp
ASTRIS_ERR_OUTOFMEMORY
Client already present in dictionary %x
instruction=0x%llx
src_reg < 32 || src_reg == 31
GetUri
[SSTEP] using BP %d\n
ARM64cpu_t
ret.clear.async
fn._read_special_reg.reg_srn
probe
cpu_cache_cleaninv
astris_command_lock
_get_num_hwbp_hw
_handle_exception_for_el
Booster System Is Not Initialized Bailing\n
Unable to create pthread key for conenction. errno=%d %s.
{%s:%s@%d} [%s] failed preconnect\n
astris_write_hang_crumb
xtensa-non-tie-range-size
HardwareStep
Astris default logging context
AuthDebugWithTimer_t::check_timer_and_clear_timeouts status: 0x%X\n
fn._ocd_exec_instr.rotw.+16
xfer=%u, xfer_length=%u, address=0x%8.8X
CortexM23
init_astris_api
PAYLOAD_OVERFLOW
AXconn_copy_nickname
AXcpu_resume_translation
\tTatsu AuthDebug Triage | All\n
response == NONE; failed to get kis target info\n
{%s@%d} Inconsistency in response payload handling (addr=%p, size=%d, cs_length=%d, rcvd=%d).
For production parts make sure you have allow_swd_updates=1 set in your boot-args
check_and_clear_cpu_msr_lock
EPC6
fn._tie_read_word32.last
{%s@%d} Probe reported connection lost [PROBEEOF].
{%s:%s@%d} [%s] unable to read command response\n
cpu_lacc_status_remove
Creating STM Flasher\n
boot-core
{%s:%s@%d} [%s] writing BCR %d\n
Failed to execute DRPS, in order to restore PSTATE after exception
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
fn._write_mem.length.incorrect
No probes were found matching
{%s} %d(%s) [RETRYING]
ARM32cpu_t
Unable to read LR
Going To Create Generic Xtensa Core, name=\"%s\".\n
astris_cpu_get_cl4_debug_signpost
UNKNOWN_DAPSTAT
[Auth Debug] Ticket Active, Debug Interface Locked\n
%s v%s%s [%s]
Koko
_a64cpu_write_gpr_cached
EL3h
RESPONSE_CMD
could not get runtime env
Unable to read SP
com.apple.astris
## dpw 0x%02X failed (%s)\n
internal.clear_probe_auth.chip == NULL
Level-1 exception PC
Table 5–155
UNKNOWN_KIS_ERROR
Misc_CortexM_AHB5
CPU state %d
astris_ide_refresh_boardid
_a64cpu_read_vfpreg_hw
_suspend_translation_hw
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
Early dbgwrap base extracted: 0x%llx\n
ret.ito.clear_edscr_err
Failed to read: ESR_EL%d
!!!! Critical Error: el[%d] == m_exception_level[%d] !!!!\n
astris_jtag_scan_gotorti_impl
ret.reg.write.K_DA_REG_NAME_ECID0
Ticket Data is NULL\n
AXdebug_auth_authenticate_probe
ANE_SYS
_a64cpu_read_edscr
_init_configuration_by_name
=== Starting Gather and Clear ===
Missing a comma or ']' after an array element.
setEnvironmentInfo
Could not find bundle () in given array: %s\n
NXP
_a64cpu_read_gpr_cached
AXconn_probelist
JSON structure error: key '
j1500i
{%s:%s@%d} [%s] writing BVR %d\n
2: ARM64_SYSOP_ATS12E1W\n
{%s:%s@%d} [%s] executing MOV\n
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
intack
General register 1
{%s} write reg_val=0x%08llX to SPSR_EL%d (current_el=%d)
AXmemap_read_modify_write
Update
DESIGNER_ARM
fn._read_special_reg.ibreaka0
no error
ASTRIS_ERR_MASKERR
{%s::%s@%d} [FALSE] OP2 out of range [0x%08x]\n
fn._ocd_exec_instr.rsr.ddr.t1
read.dspsr_el0 NOT CACHED
_clean_dcache_setway
ret.reg.write.K_DA_REG_NAME_AUTH_VALID_CLEAR
General register 0
CPU is halted
ASTRIS_ERR_ASYNC_BARRIER
set_or_replace
[AstrisAsync] Activating async...\n
{%s} Failed to get watchpoint count for %s: %s
AXJTAG_EXPLORE_FC_JTAGAP
Could Not Find The Astris Init Function (%s) in %s
AXbooster_get_all_boostermanagers
Booster Value is Not String\n
[FLUSH]\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
[AstrisAsync][COMPARE] MISMATCH: cmdbuf contents differ (length=%d)\n
W
ret.dbgap.memap_write
dfu-Type: %s\n
{%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
ret.read.ecid
\nPKA Command Verify Error In Check-Response (v.5 - status = 0x%08x, should be 0)\n
op_RSR_encode
TRANSLATION_ERR_L2
Probe
NXP_RT117x
result.read.dbgwrap_base==
EPIREAD
virtual_memory_bytes
Schema validation failed:\n  Schema location: %s\n  Document location: %s\n  Failed keyword: %s
fn.local
Going to do imago workaround\n
AuthDbg,EnAppleDebugExternal
ret.reg.write.K_PKA_REG_NAME_DBG_INPUT_START
Optional Key: CPUMonitor not in preferences
EPC2
LITBASE
fn._ocd_reg_r.dsr.dsr
AXbooster_print_boosters_detailed
Accumulator high bits
param.regval.invalid.null
Astris-%d~%d
explore_pid_swd
[INS_WP] wp%d wvr=%016llx wcr=%08x\n
Set custom PSD json file: %s
addTimingPhase
param.conn==NULL
Failed to read reg_addr=0x%llx
## apr %u 0x%08X (%d) failed: err=%s, status=%s, cmdstat=%x\n
MR2
astris_json_set_address
expFrac <= 0
ret.test.2.1
CPU: %s halting debug is now %s\n
_a64cpu_encode_aarch64_add_imm
ret.reg.write.K_DA_REG_NAME_NONCE_0
internal.authenticate.chip == NULL
kisLoc
In Eraseflash\n
DCS15
SEQ-ID=0x%X - KIS-CMD-FLAG=0x%X - JTAG-SLAVE=0x%X - SHIFT-LENGTH=0x%X
ASTRIS_ERR_USB_EMPTY
[SSTEP] bvr=%08x bcr=%08x\n
_read_general_reg_by_name
!!!!!!!!!!   $ sudo chown $USER %s\n
%d%s
Error %s connecting to probe server
Please answer y=yes or n=no.\n
astris_command_complete_cache
AIDInterface
[%s] %d -> 0x%08x\n
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
Production Fused Device\n
model
{%s} unmodified-probe_match = %s
SCAN
cpu_hwbp_remove
FirmwareSkip
[KIS] Register Read/Write/Wrote: %d\n
Pages %d\n
GenericStringRef
KF-ETM
operator()
AXLOG
connecting to Ethernet probe
Misc_Rtx117x
PMGR_CTI_MUX_REGS
{%s} IDCODE %08X (designer=%04X, partno=%04x) not recognized as an ARM TAP/DAP\n
performing direct connect by port number
Connection aborted: kick required to probe server
Init dbgwrap obj failed
Parse
MISC0
ASTRIS_ERR_NOSOC
index < data_.a.size
dr ->
PMGR_OCLA_REGS
_get_wpaddr_hw
TBMLocked
AXspmi_read_bus
AuthDebug::authenticate_probe - no need to authenticate\n
 (%s)
{%s} probe device server closed the connection while trying to read data (at recv)
SWDFlashErase
[READ] cop64 %d -> 0x%016llx\n
ret.ito.read.edscr
{%s->%s} EL2 not implemented
## apr %u 0x%08X -> 0x%08X\n
R14
regex.h
calOverrides isn't a dictionary: %@
development
Selecting polling method %s
Connected to Probe Device Server [Log File %s]
Unable to connect (single_port) to probe server
backtrace
The document is empty.
Stringify
AXportal_t Is Not Valid Type - %d
{%s::%s} [%s] error %s reading SCTLR_ELx
Clear requests in INTERRUPT
param.width.invalid
op_S16I_encode
MAX_KISSWD
ret.astris_disassemble_at_addr
_init_registers
ASTRIS_ERR_PROBEINUSE
Base::level_stack_.GetSize() >= sizeof(typename Base::Level)
DCM
PKA Command Verify Completed, No Errors, but Enable Valid Not Set
fn.loop.xfer
RSM
localwrstn-debug
OK
Shift-amount register
var.bp.invalid
regval is NULL.
spr
{%s::%s} EDSCR has MA set (dscr = 0x%08X). Clearing.\n
ret.write.spsr_elx
[REM_HWBP] bp%d\n
{%s} Reading base 0x%llx entry's component ID
Double exception PC
checking if relay \"%s\" is valid
Connect using RSD not supported\n
MemberEnd
m_regstate.a64r_dspsr_el0
ARMDAP
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
Chip identification failed
root_ != 0
Gateway Version: 0x%X\n
result.extract_table_info==
2: ARM64_SYSOP_ATS12E1R\n
fn._write_cpu_reg_file.regval
L1_INSTRUCTION
Status/State
{%s@%d} Drain empty on decr [%s].
Asked To Read A Negative Register Index
{%s->%s} [!is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
fn._ocd_exec_instr.wsr.ddr.data_reg
unable to identify chip
param.conn.enable_explorer == NULL
ret.clear_authentication
decr_drain_packets
complex-cpus
{%s} Thread %#llx key %lu losing when not attached to info %p - IMPLIED ATTACH
ret.previous_authenticate.timedout
M
{%s:%s@%d} [%s] doing IR scan (DTRTX SCAN_N)\n
ret._a64cpu_lower_el_hw_safe
[%s] chipinfo is NULL
RF2
_setup_data_bp
Error while trying to disassemble memory
AXconn_hostname
{%s} Found extra info in = %s, chopping string
{%s::%s} timeout while waiting for EDSCR ITE
recoverable
!(calTotalLength(%@)<kCalibrationMaxLength(%@))
init
{%s:%s@%d} [%s] Address must be aligned to length\n
CalibrationData
AXcpu_sstep
{%} exec: encode_hint(NOP)\n
[INSBP] bp%d addr=%08llx fpr=%08X\n
Probe %s removed prior to kick\n
appendToArray.timing_phase
Failed to convert %s key @ index %d
0
HCR_EL2
AXcpu_suspend_translation
{%s} Failed to extract SoC Stop Clock Info from table (%d); continuing anyway
{%s:%s@%d} [%s] executing MRS (switched)\n
EL2h
Generation of the nonce timedout\n
BoosterManager
at 0x%llx
acc
internal.is_authenticated.chip == NULL
read_dcc
param.info.invalid.null
Crash level
%d.%dbeta%d
diyfp.h
_read_memory_fast
AXspmi_write_bus
AuthDebugWithTimer_t::need_to_authenticate_helper auth-debug is not active (no need)\n
RF24
param.at.invalid.>15
ret._a64cpu_raise_el_hw.after_cached_fault_reg_latch
copyBoardNameForPrimate
{%s} _pre_halt_hw result = %s
AuthDebug_t::init failed (AuthDebugWithTimer_t)
Schema parse error
bypass-configs
AuthDebugWithTimer_t::need_to_authenticate_helper exit true (error - need)\n
R6
fn._write_special_reg
fn._ocd_reg_w.ddr.regval_save
invalid command
Got an error reading the DCM Control Register: %s
BoosterManager.SWDFlash
Lowering from exception level[%d] other than 1, 2, 3 [%d]?
get_ecid
no system bus AP present when expected
AX1500_listbridges
{%s::%s} error %s writing EDSCR %s
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
probe on localhost
relay_get: %s = CMD_ERR (%s)
hid-fw-personality
SETCLR
JsonLogger: Created with default schema version '%s'
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/util/astris_json_logger.cpp
schema.h
Probe Type (%d) FW Version: %s does not support KIS.
Debug-Components
{%s} L2 cache operation completed [%s]
read memory
AXcpu_hwwp_disable
{%s} strsep empty so match any probe [localhost]
unable to obtain sysap
CPU Die: %d\n
Breakpoint Enabled: %s
   {%s} (DP): status=0x%X(%s) - %s\n
EXCSAVE1
Transaction
ret.cfg_write(R_DCM_GPIO).deassert
{%s:%s@%d} [%s] reading PRSR (oslk)\n
{%s->%s} [!aarch64] exec: encode_mrs(%s=%d[%s], MDDTRRX_EL0, %d)\n
DBGCTRL = %08X   res=%d\n
[PREFS] Key: %s - Val: NULL
Register file 51
setTargetInfo
{%s:%s@%d} [%s] timed out waiting for reg_index %d to equal: ((0x%08X & 0x%08X) == 0x%08X)\n
_a64cpu_read_aarch64_sp_hw
_write_executable_memory
{%s::%s} [%s] length=%u when width=%d
ret.storePairForPref
PowerOff
astris_preferences_cpu_monitor_list
usbcport
error trying to unlock MSR %s
CCOUNT
astris_get_dbgwrap_sys_addr
Malloc
astris_get_soc_resource_filepath
sdom
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
{%s} Failed to extract die addr locationfrom table (%d); continuing anyway
_a64cpu_write_sysreg_hw
m_bp_details
fn._ocd_reg_r.dsr.2
implementer
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
PowerGated
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
sso_user.sso_data == NULL
fn._clear_portal_status
ASTRIS_ERR_NOTPRESENT
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c
AXconn_create failed
ret.faul_reg_latch
failed to write memory
   JEDEC ID: 0x%08X\n
ProbeNav
astris_write_halt_all_crumb
None
3679.40.30b172
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_booster_api.cpp
ret.get_current_el.initial
read.dlr_el0 NOT CACHED
{%s->%s} [aarch64] exec: encode_mrs(%s=%d[%s], MDDTR_EL0, %d)\n
Primate-Hub-Null
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/disassembly/astris_disassemble.cpp
L3
api.is_prod.chip->soc == NULL
Unknown Subcommand
process (%s) (%d) path: %s
FWUPDATE
AXconn_connect_kext failure - %s
{%s:%s@%d} current_el[%d] <  %d\n
ret.nonce_generation.timedout
fn._ocd_reg_r.DDR
INVALID 
PushUnsafe
cpu-name
AuthBase_t::init failed (AuthDebug_t)
Register file 40
probe matching %s on localhost
cpu_halt
[%s] TGE is set so we traping to EL2\n
param.invalid_gpr
param.tgt->ap->dp.null
fn._collect_snr.exccause
dlr_el0
ret._set_wpaddr_hw
unable to write memory (using system ap)
Low level
collect-probemap
index < stateCount_
[AstrisAsync] Async mode %s
ret.reg.read.K_PKA_REG_NAME_DBG_VERSION
Selecting
BeginValue
Missing key: %s
{%s::%s@%d} [FALSE] gpr[%d] < T32_GPR_COUNT\n
      Read of JTAG-AP port %u CSW failed with %s\n
String
Booster Bundle: %s\n
{%s:%s@%d} [%s] reading DTRTX\n
OK: address translation resumed for %s successfully
{%s} Component ID read fail for 0x%llx (%s)
## memapw %u 0x%016llX 0x%08X\n
Subsystem Monitor Key does not exists: %s\n
cpu did not stop. OCD.DSR=0x%8.8X
clzll
Dart Dart Type: %s\n
CS-CTI
EL3t
create_using_builtin
no USB device
(Last: %s) (%s)
astris_json_logger_get
block-unpiped-shift-wr-force2zero
ARM7
Both debug and xbs versions are set, maybe a bug: %s
address-size
We are Allocating\n
ret.drain.half-duplex
[AsyncSnapshot] No snapshots collected\n
OCD debug status register
Dumping Process Tree
Address formatting failed
dr <-
Die Config Disabled\n
~MA
astris_jtag_get_pipe_cycles
AuthDebugUseSSO
Write Data Length Mismatch
{%s::%s} write OK but took %d tries
High level exception save location
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
astris_batch_attitude_suspend
ret.read.esdcr.nolog
no enable slot available
memap_bus_write
nameBuffer_ == 0
swdovrrun
CPU Monitor key does not exists for: %s\n
Table 4-63
Register file 7
fn._ocd_reg_r.ddr
ASTRIS_ERR_IGNORED
ISP_L
ret.getSubsystemEnableStatus
PCORE
ITM
{%s:%s@%d} Took an exception that took us to exception level[%d] other than 1, 2, 3?\n
%016llx
Previous authentication in-flight, wait for it to finish\n
Register file 45
param.booster_bundle==NULL
entry.exception_test_0
ESR_EL2
SCTLR__ELx
    INFO(%u,%d): %s(%04u): %s(): %s
%-16s
RF29
param.reg_name.invalid.null
quiesce
storeBoardName
Failed to access new_cpu status
lldb
CPU AP-Type: %d\n
Going To Create Generic ARMV7m, but typehint is present (%s)\n
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
cpu_lacc_pc_status
param.bundle_url==NULL
{astris_probed_print_events_from_json} not supported in this build configuration
result.init==
[INIT_HWWP] m_wp_avail=0x%X, m_wp_enabled=0x%X, m_wp_rsvd=0x%X
spmi
set.wp.len = not supported
fn._init_configuration_by_name.failed
ASTRIS_ERR_NOMEM
_get_num_hwwp_hw
write.dlr_el0 NOT CACHED
get_tsz
RF19
%s/Library/Logs/Astris
  Error path [%s]\n
{%s@%d} Issued request ID #%02X, received response ID #%02X [MISMATCH].
APPLETYPE_UNKNOWN
ret.modify.edscr.~a
CPU_t
   Debug Port: SELECT %X: DISABLED\n
param.m_ap == NULL && param.m_lam == NULL
THREADPTR
exit.exception_test_2
astris_cpu_mmu_configure
%d:%d%s
L1CRT
astris_ide_get_revision
{%s:%s@%d} [%s] executing MRC\n
DISP_R
AXcpu_hwbp_info
ASTRIS_ERR_MISMATCH
Eval
{%s:%s@%d} [%s] executing MSR\n
cache_op
WARNING, reserved / slide bits not zero! Zeroing out!\n
AuthDbg,ECID
Successfully Authenticated Probe\n
data_.f.flags & kUint64Flag
GPR[cached]
EXPLORE_NOCLEAN
empty request encountered
getPersonalityNameFromRegistryEntry failed
_a64cpu_read_gpr_hw
Connected
command timed out
Unable to process command while connecting to
write.reg.not cached
{%s::%s} [%s] error %s verifying SW BP instr (CPU) [VA=0x%016llX, len=%d]
jtag_get_soc
General register 3
DCS_BC6
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
astris_cpu_raise_el
CPU[%s] Write Reg: %d Val: 0x%llx
Reset
Result while reading first entry: %s , entry val 0: 0x%X\n
Register file 47
Connection aborted: kick required to probe server. Received eof in stdin
AXcpu_resume
No windowed register option.
fn._tie_read_word32.first
PoodleSWD
VERSION
MAP_CMD
CPU2
[1500] Detected plist version %d
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
PROBED_ASYNCSKIP
cpu_readmem
is.Peek() == 'f'
{%s:%s@%d} [%s] executing MRS\n
_set_wpaddr_hw
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
Failed to exec MSR to move contents of scratch (containing val to write) into sysregscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
!HasParseError()
_a64cpu_assert_rw_matches_hw
AP[%d]: MEM_AP_APB\n
max_scan_bits is low: %d
PortBridgeSWD
panic_diagnostic
i
soc-revisions
register lookup by name not supported when Astris is statically linked
ASTRIS_ERR_ANOMALY
SWDFlashWrite failed: 0x%08x\n
Could Not Find Booster Entry Function: %s\n
    %s(): %s
astris_update_ap_slave
param.op.invalid
var.bp_index.invalid.outofrange
op_S32I_encode
empty USB packet encountered
Asked To Write To A Negative Register Index
Passed NULL plist file\n
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
{%s:%s@%d} GRPS[0] cached\n
{%s::%s} EDSCR with RXO set - unable to recover.\n
      Select of JTAG-AP port %u failed with %s\n
General register 10
PROBED_USB_RSP_TIMEOUT
{%s->%s} ERROR=%d(%s)
PORTAL ERR PENDING
Table 5–175
cpu instr. 0x%8.8X not halted after 3 checks. OCD.DSR = 0x%8.8X
Standard level
ASTRIS_ERR_NOPORTAL
DCS11
error %s reading DAP PFR1
AXcpu_status_asc
Parameter len = %d > 64.
(0x%08llX) %s
Category name is null
GetDouble
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
ret.read.edscr.start
{%s} Failed to get breakpoint count for %s: %s
Table 5–164
ICOUNT
{%s@%d} IOConnectCallStructMethod failed, err = 0x%08x
.os
Bad personality name data: %@
internal.enable-timer-ovr.chip == NULL
addr_reg=%u,page_id=%u,data_reg=%u,opcode=0x%6.6X
No version information found in booster: %s
%s%s\n
{%s:%s@%d} Nested exceptions... get someone to debug this.\n
MASK ERROR
fn._collect_snr.ps
fn._ocd_exec_instr.xsr.ddr.t1.2
%s: failed to create dictionary
## memapr %u 0x%016llX -> 0x%08X\n
OCD control register, clear
Register file 24
{%s:%s@%d} [%s] doing IR scan (DTRRX EXTEST)\n
{%s::%s@%d [%s]} Error %s: collecting HW
SUCCESS
virtual int ARM7cpu_t::_halt_hw()
   Debug Port: SELECT %X: SKIPPING\n
port_%d
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
probe %s on host %s
Probe Map comm error %d(%s) %s [%s]
param.portal.dcm == NULL
BP
[%s]\n
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
AXcpu_halt
Table 5–181
{%s} Thread %#llx key %lu should have detached from info %p - IMPLIED DETACH
current_el[%d] != target_el[%d]
KIS_RSP_OK
%s-%06X
EPS3
{%s:%s@%d} [%s] writing PAR[64]\n
{%s::%s} [%s] INS_SWBP failed: failed to set halting debug
Memory error virtual addr register
0 == Base::level_stack_.template Top<typename Base::Level>()->valueCount % 2
{%s} Directly-connected CoreSight component (dbgbase=0x%llx)
EXPLORE_WITH_AVE
RF42
clzll.h
AMCP0
far_el2
SoC has been setup using standard instantiation (setup result=%d)
SWDACKDELAY relay read failed %s. We are assuming probe %d does not support it\n
jtag_cmd
MAIN_DEBUG_ROM
HWERR
HF3
failed to create log dump file
hardware error reported by probe
out of memory
result.read_vals(version)==
astris_user_default_copy_nickname_for_primate
primateHubLoc
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
param.halt_group == NULL
{%s:%s@%d} [%s] getting GPR 0 (CPSR)\n
ret._a64cpu_read_sysreg_hw.hcr_el2
[%s] EL @ end of Collect: %d\n
[COLLECT] Chip %x\n
AMAuthInstallSsoSetAppleConnectInfo
cs_type:0x%x
dbgwrap halt failed, falling back to classic method
ASTRIS_ERR_USB_NOTOPEN
Target is not a JSON object
Requested to write %d words, instead %d were written (Requested: %d != Actual: %d)\n
Exception
Failed to read IDE through DAP\n
Port
{%s:%s@%d} [%s] getting GPR\n
[HALTED] dfsr = 0x%08x\n
{%s} handle ROM entry %d (level %u): %08x
AXdebug_auth_get_dft_timer_count
cpu_hwwp_disable
Failed to get PMU Name
targetid
{%s::%s} creating placeholder for CPU: name=%s
     ARM %s watchpoints: %u\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_cpu.cpp
AXchip_get_board_rev
select
%s (addr=0x%llx -> val: 0x%x)
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
read_resp_payload_via_sock
ret.write_hang_breadcrumb
Found %d APs
internal.is_authenticated.chip->soc == NULL
internal.enable-test.chip->soc == NULL
astris_identify_load_booster
{%s} d=%016llx valid=%llu errs=%llu%llu%llu%llu
SPSR_EL1
{%s::%s} [%s] error %s writing SW BP instr [PA=0x%016llX, len=%d]
astris_user_default_copy_nickname
MR3
ChimpSWD
XTENSA
Booster Info:\n%s
DSP
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
AuthDebugWithTimer_t constructor(2) - CIP_GEN_NUMBER 0x%08X\n
AuthDebugWithTimer_t::need_to_authenticate_helper current COUNTER: 0x%X (req_type %d)\n
Invalid Bundle: %s
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
param.conn.user_defaults == NULL
{%s} host = %s
ret.get_current_el
instr != 0
DBGSTATUS = %08X   res=%d\n
defaults.nickname.not_connected
astris_user_default_set_nickname
kis_target_info %s
AXcpu_hwbp_insert
Memory error check register
AXconn_get_pid_bid
CoreSight
cpu-armv7m-imem-size
ApProductionMode
AstrisSWD
Probe %s removed before port determined\n
Failed To Instantiate SOC From Booster\n
Failed to create SoC or no booster
setTargetIdentifiers
{%s::%s@%d [%s]} Error %s: synchronizing context
MECR
RF11
```
