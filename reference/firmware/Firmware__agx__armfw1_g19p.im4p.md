# `Firmware/agx/armfw1_g19p.im4p`

- File size: 3,411,889 bytes
- IM4P: Tag: IM4P  Type: gf1f  Version: 1
- BuildManifest components that use it: `Ap,GFX1Firmware`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         gf1f
  Version:      1
  Data:         3.4 MB (3411864 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 3,411,864 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit: %s - Client: %s`
- `RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release`

## Strings (1,449) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000020  rkosftab
00000088  __TEXT
000000c8  __text
000000d8  __TEXT
00000118  __gxf_code
00000128  __TEXT
00000168  __gxf_code_pad
00000178  __TEXT
000001b8  __gxf_shr_code
000001c8  __TEXT
00000208  __const
00000218  __TEXT
00000258  _rtk_patchbay
00000268  __TEXT
000002a8  _rtk_tunables
000002b8  __TEXT
000002f8  __cstring
00000308  __TEXT
00000348  __init_offsets
00000358  __TEXT
00000398  __chain_starts
000003a8  __TEXT
000003f0  __DATA
00000430  __gxf_data
00000440  __DATA
00000480  __data
00000490  __DATA
000004d0  _rtk_init_stack
000004e0  __DATA
00000520  __const
00000530  __DATA
00000570  _rtk_irq_stack
00000580  __DATA
000005c0  _rtk_exc_stack
000005d0  __DATA
00000610  _rtk_boot_l1
00000620  __DATA
00000660  _rtk_boot
00000670  __DATA
000006b0  _rtk_mtab
000006c0  __DATA
00000700  _rtk_power
00000710  __DATA
00000750  _rtk_page_tables__DATA
000007a0  __mod_init_func
000007b0  __DATA
000007f0  _rtk_data_uuid
00000800  __DATA
00000840  _rtk_heap
00000850  __DATA
00000890  _rtk_threads
000008a0  __DATA
000008e0  __constructor
000008f0  __DATA
00000930  __zerofill
00000940  __DATA
00000988  __DATA_SHARED_RO
000009c8  _RTK_EXT_SHD_DTA__DATA_SHARED_RO
00000a20  __DATA_CONST
00004ac1  wwwwwww
0000845d  2C)B1Kzd0Iz
0000b9e3  THix8c
0000baba  @9jyhxI
0000bcde  @9Liw8
0000c45e  @9jyhxI
000117f6  %NcX N&
00017baf  Royjx0
0001db87  K.z(xnYl
00022164  iYix)%
000248b7  T-ih8nih8
00027e9f  TID@9?=
0002cbcf  Tiju8hC
0002d821  ylx/u@9o
0002d8bd  ylx/u@9o
0002d985  ykx?u@9k
0002d9c5  ykx-u@9m
00030c98  hSQ9(m
00030e7f  9hSQ9(
0003101c  hSQ9HQ
00031218  hSQ9hA
00031260  hSQ9(?
00031393  9hSQ9(
0003145c  hSQ9H/
00050fe0  8bunz8
000516b7  @fffff
000516be  q@fffffbv
000517a0  Assertion failure: tid overflow
0005180a  *AVz6@
0005188f  ?ajQap
000520dc  INVALID
000520eb  Marin-ASC1
000520fa  Tempest-ASC2
00052109  Tempest-ASC3
00052118  Tempest-ASC4
00052127  Tempest-ASC4.1
00052136  Tempest-ASC5
00052145  Tempest-ASC6
00052154  Tempest-ASC7
000521ae  Chinook-ASC2
000521bd  Chinook2-ASC3
000521cc  Chinook-ASC4
000521db  Chinook-ASC4.1
000521ea  Chinook-ASC5
000521f9  Chinook-ASC6
00052208  Chinook-ASC7
00052217  ACC E Core
00052226  ACC P Core
00052235  ASC Chinook
00052244  ASC Tempest
00052253  Scheduler ASC
0005226a  Power Management ASC
00052570  RTKSTACK
000525bc  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
0005300b  stk_fail
00053014  Invalid DM type %d for command type %d in %s
00053066  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
000530fe  Incorrect power sub-state for early wake
00053127  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
0005318d  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
000531db  %s: !!! Fatal Error: Unknown Power state mode!
0005322a  Picked new Quantum size::%llu, Frame based quantum period:%u
00053268  In order eviction check is unsupported when multiple normal completion queues are enabled.
000532c3  !!! Error: Unexpected scheduling pause timeout after %uus
000532fd  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
0005336a  %s: !!! Fatal Error: Unhandled : Invalid command type %d
000533d7  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
00053421  AGFHRBResume
0005342e  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
00053497  %s: CRE disabled by boot arg
000534b4  AGFACREInit
000534c0  %s: CRE has restored our registers
000534e3  %s: CRE has no restore data and will save registers this run.
00053521  %s: Moving out of critical section having saved %i registers
0005357a  %s: Moving out of critical section having verified %i registers
000535ba  %s: Entering CRE critical section for save
00053601  %s: Entering CRE critical section as CRE disabled
00053633  %s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celsius
000536c3  gfx_iop_msgs
000536d0  gfx_iop_ints
000536dd  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
0005370d  Bucket overflow:: timestamp %llu, frame interval %llu, bucket_size %llu, bucket %u, num buckets %llu
00053772  PTD write failed (%u, %u)
0005378c  PTD read failed unexpectedly with error code 0x%x.
000537bf  Invalid AON PTD Dev Instance, Was AON PTD initialized?
000537f6  Failed to read %c%c%c%c. Read Status = 0x%x
00053822  Failed to Peek %c%c%c%c. Peek Status = 0x%x
0005384e  Failed to write %c%c%c%c. Write Status = 0x%x
0005387c  management
00053887  crashlog
00053890  gfx_msgs
00053899  gfx_ints
000538a2  Unsupported shared event agent index: %u
000538cb  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
00053909  agfInitDoorbells
0005391a  UMA FW id state has bad context ID. context_id: %d
0005394d  G18 Firmware initializing
00053967    FW Build variant: g19p
00053980    FW Build version: a0
00053997    FW Build running in SKSM Enabled mode
000539bf  VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)
00053a1d  Buffer size is too small to hold all counter values
00053a51  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
00053aa7  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
00053af6  _agfGL2DependentPollReg32
00053b10  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
00053b78  %s: !!! Fatal Error: Cre entry Index is greater than max GRT entries
00053bbd  AGFHALCREAddEntry
00053be4  Failed to enable CRE restore as sCRE hasn't been set up by iBoot.
00053c4a  CPMS tracing will not be supported on G18
00053c8c  agfGCPMSDisable
00053c9c  agfGCPMSEnable
00053cc7  PBState must be unbind, before being rebound to different PB state
00053d1f  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
00053d72  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
00053ddb  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
00053e2c  AON PTD Enable mask is 0 for mGPUS. Skipping!
00053e5a  AON PTD Enable mask is 0 for Fabric. Skipping!
00053e89  Total Csw histograms collected: %lld
00053eae  Initial Csw histogram timestamp: %#llx
00053ed5  Total Csw traces collected: %lld
00053ef6  Initial Csw trace timestamp: %#llx
00053f19  Total IVDM histograms collected: %lld
00053f3f  Initial IVDM histogram timestamp: %#llx
00053f67  Total IVDM traces collected: %lld
00053f89  Initial IVDM trace timestamp: %#llx
00053fad      Snapshot timestamp: %#llx
00053fcb      Bucket %u: %u
00053fdd      Number of samples: %u
00053ff7      Sample %u: %u
00054009  Unable to grab init data from host
0005402c  Host and FW Interface is mismatched, please ensure the versions are aligned.
00054079  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
000540d8  GPU temperature slew rate timer period: %u us
00054106  %s: !!! Fatal Error: Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
000541ae  Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
0005421f  Spurious GPU slew rate interrupt!
00054241  %s: !!! Fatal Error: Invalid DataMaster %u
00054285  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
000542dc   from 
000542e3  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
00054370  TP_VDM
00054377  TP_PDM
0005437e  TP_CDM
00054385  TP_RIA
0005438c  UFE_VDM0_CLQ
00054399  UFE_VDM1_CLQ
000543a6  UFE_PDM0_CLQ
000543b3  UFE_PDM1_CLQ
000543c0  UFE_PDM2_CLQ
000543cd  UFE_CDM0_CLQ
000543da  UFE_CDM1_CLQ
000543e7  UFE_CDM2_CLQ
000543f4  DPB0_TOTAL_ISS0
00054404  DPB1_TOTAL_ISS1
00054414  DPB0_AGEN
0005441e  DPB1_AGEN
00054428  DPB0_TOTAL_DISPATCH
0005443c  DPB1_TOTAL_DISPATCH
00054450  DPB0_F32
00054459  DPB1_F32
00054462  DPB0_SCIB
0005446c  DPB1_SCIB
00054476  DPB0_IC
0005447e  DPB1_IC
00054486  DPB0_PERM
00054490  DPB1_PERM
000544a8  DPB0_F16
000544b1  DPB1_F16
000544ba  DPB0_MXU_WORK
000544c8  DPB1_MXU_WORK
00054c25  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
00054c80  AGFAInitSequence unknown seq type %u
00054ca5  cold booted
00054cb1  Unknown ASC version
00054cc5  GFX %s %u %s FW %s! (%s)
00054cde  Oct 13 2026 23:31:54
00054cf3  GPU is not powered on after power kick!
00054d1b  agfMTRAlarmHandler
00054d2e  %s: !!! Fatal Error: MTR Alarm interrupts not handled!
00054d65  %s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware! chainID=%u
00054dcf  Failed to register cputrace handler
00054df3  agx_power
00054dfd  rif_shadow
00054e08  GPU is Powered On while we are about to Power down Fender
00054e42  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
00054e7f  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
00054ebc  %s: !!! Fatal Error: Error %x
00054eda  AGFASemaphoreSignal
00054eee  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
00054f60  Msg of type %u received, which can't be handled!
00054f91  %s: !!! Fatal Error: Unknown IOP msg type %d!
00054fd4  %s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx
0005503b  !MIDR: 0x%x
00055047  ~CsPTR
0005504e  !ROf %#lx %#x
0005505c  MMU private: s:%llx!=%llx b:%llx!=%llx
00055083  MMU VA sz %u 0=%zu 1=%zu
0005509c  MMU private !fit: b:%lx<%lx s:%lx>%lx
000550c2  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
000550ef  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
00055121  MMU sh<ps: %llu > %llu
00055138  Page Table !vm export: %x
00055152  GPTBAT !vm export: %x
00055168  PPL handoff !vm export: %x
00055183  !Mthd:%p
0005518c  !msgmbxint
00055197  !msgdoordashint
000551a7  mme:0x%x
000551b4  Duty cycle
000551c5  Sleep count
000551d1  Wake count
000551dc  Power state
000551e8  Free heap
000551f2  Total heap
000551fd  Peak heap alloc
0005520d  Used stack
00055218  Total stack
00055224  CPU count
00055235  <null>
0005523f  ThIntr:%u,%u,%u,%u
00055252  ThLock:%p
0005525c  MBI queue overflow:%s
00055272  VmOv %d %d
0005527d  rtk_ep_work
00055289  MGMT msg=0x%llx st=%x
0005529f  MGMT st=%x
000552ae  !clg: %08x
000552b9  !cpy: %08x
000552c4  Not implemented
000552d4  Message Log
000552e1  Invalid AP power: %d
000552fd  RTKit: %s - Client: %s
00055314  !Heapblk:%p
00055320  REDACTED
00055329  rtkptd.cpp
00055334  %s:%d Invalid parameter range[%d]
00055356  ptd_write
00055360  %s:%d Range =%d info not found
0005537f  %s:%d Invalid index[%d]
00055397  %s:%d Invalid handle
000553ac  %s:%d Bad write offset=0x%X
000553c8  %s:%d Invalid parameter range[%d] or data = NULL
000553f9  ptd_read
00055402  %s:%d Bad Read offset=0x%X error:0x%x
00055428  range_param_check
0005543a  %s:%d Unknown range[%d]
0007bf90  lCytuDTRT
0007bfe8  tnCplSTRe
0007c040  tnCkaWTRq
0007c098  tffOnOTR|
0007c0f0  EERFPHTR
0007c149  LLAPHTR
0007c1a0  KAEPPHTR
0007c1fa  UKTSTR
0007c252  AKTSTR
0007c2a8  UPCmuNTR
0007c448  not set
00114b04  _RTK_abort
00114b0f  _RTK_client_version_string
00114b2a  _RTK_dev_asc
00114b37  _RTK_dev_asc_config
00114b4b  _RTK_dev_cputrace_metadata
00114b66  _RTK_dev_pts_ptd
00114b77  _RTK_dev_pts_ptd_peek
00114b8d  _RTK_dev_timesync_0
00114ba1  _RTK_dev_wrapper_icu
00114bb6  _RTK_uppl_mapped_memory
00114bce  _SH_DATA_SEGS
00114be2  ___bzero
00114beb  ___powisf2
00114bf6  ___stack_chk_fail
00114c08  ___stack_chk_guard
00114c1b  ___stack_chk_guard_setup
00114c34  __arm_arch_hibernate_uat
00114c4d  __arm_arch_resume_uat
00114c63  __arm_cache_info
00114c74  __fp_context
00114c81  __hb_context
00114c8e  __mbi_routes
00114c9b  __mmu_config
00114ca8  __nmi_frame
00114cb4  __platform_bzero
00114cc5  __platform_memcmp
00114cd7  __platform_memmove
00114cea  __platform_memset
00114cfc  __rtk_arch_dead_loop
00114d11  __rtk_arch_exception
00114d26  __rtk_arch_fast_interrupt
00114d40  __rtk_arch_gxf_vector_abort
00114d5c  __rtk_arch_gxf_vectors
00114d73  __rtk_arch_interrupt
00114d88  __rtk_arch_interrupted_pc
00114da2  __rtk_arch_svc_handler
00114db9  __rtk_arch_vectors
00114dcc  __rtk_arch_wait_for_interrupt
00114dea  __rtk_arch_wait_for_interrupt_retention
00114e12  __rtk_arm_mmu_bits_per_level
00114e2f  __rtk_arm_mmu_page_shift
00114e48  __rtk_arm_mmu_page_size
00114e60  __rtk_arm_start_bootstrap_area
00114e7f  __rtk_armv8_bootstrap_page
00114e9a  __rtk_armv8_l1_bootstrap
00114eb3  __rtk_astris_island
00114ec7  __rtk_cache_clean
00114ed9  __rtk_cache_clean_invalidate
00114ef6  __rtk_cache_info_init
00114f0c  __rtk_crashlog_is_local
00114f24  __rtk_crashlog_local_buffer
00114f40  __rtk_crashlog_requested_size
00114f5e  __rtk_crt_exc_stack
00114f72  __rtk_crt_exc_stack_base
00114f8b  __rtk_crt_exc_stack_len
00114fa3  __rtk_crt_exc_stack_top
00114fbb  __rtk_crt_expect_boot_args
00114fd6  __rtk_crt_init_stack
00114feb  __rtk_crt_init_stack_base
00115005  __rtk_crt_init_stack_len
0011501e  __rtk_crt_init_stack_top
00115037  __rtk_crt_irq_stack
0011504b  __rtk_crt_irq_stack_base
00115064  __rtk_crt_irq_stack_len
0011507c  __rtk_crt_irq_stack_top
00115094  __rtk_crt_mmu_addr_space_size_log2
001150b7  __rtk_crt_mmu_gxf_stack
001150cf  __rtk_crt_mmu_gxf_stack_size
001150ec  __rtk_crt_mmu_gxf_user_va_bits
0011510b  __rtk_crt_mmu_gxf_version
00115125  __rtk_crt_mmu_tables
0011513a  __rtk_crt_mmu_ttbr1_private_space_size
00115161  __rtk_crt_mmu_ttbr_select_bitmap
00115182  __rtk_crt_mmu_uat
00115194  __rtk_current_threads
001151aa  __rtk_dcache_clean_invalidate_whole
001151ce  __rtk_dcache_clean_whole
001151e7  __rtk_dev_bad_method
001151fc  __rtk_gxf_entry
0011520c  __rtk_gxf_initialized
00115222  __rtk_ior
0011522c  __rtk_mbi_max_route
00115240  __rtk_mbi_routes_array
00115257  __rtk_mmu_gxf_config
0011526c  __rtk_mmu_gxf_config_swift
00115287  __rtk_mmu_map
00115295  __rtk_mmu_region_disable
001152ae  __rtk_mmu_switch_region_base
001152cb  __rtk_mmu_tlb_invalidate_all
001152e8  __rtk_mmu_unmap
001152f8  __rtk_mmu_update_mapping
00115311  __rtk_mmu_virt_to_phys
00115328  __rtk_pac_safe_interrupts_disable
0011534a  __rtk_pac_safe_interrupts_restore
0011536c  __rtk_patch_RTK_cpu_physical_address
00115391  __rtk_patch_RTK_cpu_wrapper_physical_address
001153be  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
001153ef  __rtk_patch_RTK_io_base
00115407  __rtk_patch_RTK_io_size
0011541f  __rtk_patch_RTK_lock_legacy
0011543b  __rtk_patch_RTK_mc_remote_alignment
0011545f  __rtk_patch_RTK_pe_i_can_has_debugger
00115485  __rtk_patch_RTK_platform_flags
001154a4  __rtk_patch_RTK_soc
001154b8  __rtk_patch_RTK_soc_revision
001154d5  __rtk_patch__aslr_slide
001154ed  __rtk_patch__aslr_slide_src
00115509  __rtk_patch__breakeven_pv
00115523  __rtk_patch__chain_starts
0011553d  __rtk_patch__dseg_copy_length
0011555b  __rtk_patch__dseg_relocate
00115576  __rtk_patch__dseg_virt_source
00115594  __rtk_patch__mkey_cfg_address
001155b2  __rtk_patch__pac_entropy
001155cb  __rtk_patch__page_table_base
001155e8  __rtk_patch__page_table_size
00115605  __rtk_patch__rtk_dev_timebase_offset
0011562a  __rtk_patch__rtk_runtime_size
00115648  __rtk_patch__rtk_stack_guard
00115665  __rtk_patch__zerofill_length
00115682  __rtk_patch__zerofill_start
0011569e  __rtk_patch_armv8_ignorenthint
001156bd  __rtk_patch_armv8_single_issue_neon
001156e1  __rtk_patch_armv8_timer_frequency
00115703  __rtk_patch_gxf_private_phy_space_base
0011572a  __rtk_patch_gxf_private_phy_space_size
00115751  __rtk_patch_mmu_ttbr1_private_space_size
0011577a  __rtk_patch_page_table_virt_base
0011579b  __rtk_patch_tunables_size
001157b5  __rtk_patch_tunables_start
001157d0  __rtk_patch_uat_gptbat_base
001157ec  __rtk_patch_uat_gptbat_size
00115808  __rtk_patch_uat_ppl_shared_base
00115828  __rtk_patch_uat_ppl_shared_l2_phys
0011584b  __rtk_platform_asc_retained_tunables_block
00115876  __rtk_platform_asc_tunables_block
00115898  __rtk_power
001158a4  __rtk_sign_initial_thread_state
001158c4  __rtk_stack_watermark
001158da  __rtk_thread_entry
001158ed  __rtk_thread_list
001158ff  __rtk_thread_list_size
00115916  __rtk_unexpected_reset
0011592d  __rtk_uppl_client_dispatch
00115948  __rtk_version_string
0011595d  _arm_do_whole_dcache
00115972  _arm_fp_context
00115982  _arm_fp_context_addr
00115997  _arm_hb_context
001159a7  _arm_hb_context_addr
001159bc  _arm_hb_sleep_count
001159d0  _arm_hb_wake_count
001159e3  _arm_resume_flag
001159f4  _armv8_timebase
00115a0a  _bzero
00115a11  _gCrashLog
00115a1c  _gMemoryAllocator
00115a2e  _gxf_code_pad_sym
00115a40  _memcmp
00115a48  _memcpy
00115a50  _memmove
00115a59  _memset
00115a61  _mmu_get_page_table
00115a75  _mmu_get_tt_info
00115a8b  _vm_regions
00115a97  dcache_op_poc
00115aa5  new_rtk_start_anywhere_uatv2
00115af0  __TEXT
00115b30  __text
00115b40  __TEXT
00115b80  __gxf_code
00115b90  __TEXT
00115bd0  __gxf_code_pad
00115be0  __TEXT
00115c20  __gxf_shr_code
00115c30  __TEXT
00115c70  __const
00115c80  __TEXT
00115cc0  _rtk_patchbay
00115cd0  __TEXT
00115d10  _rtk_tunables
00115d20  __TEXT
00115d60  __cstring
00115d70  __TEXT
00115db0  __init_offsets
00115dc0  __TEXT
00115e00  __chain_starts
00115e10  __TEXT
00115e58  __DATA
00115e98  __gxf_data
00115ea8  __DATA
00115ee8  __data
00115ef8  __DATA
00115f38  _rtk_init_stack
00115f48  __DATA
00115f88  __const
00115f98  __DATA
00115fd8  _rtk_irq_stack
00115fe8  __DATA
00116028  _rtk_exc_stack
00116038  __DATA
00116078  _rtk_boot_l1
00116088  __DATA
001160c8  _rtk_boot
001160d8  __DATA
00116118  _rtk_mtab
00116128  __DATA
00116168  _rtk_power
00116178  __DATA
001161b8  _rtk_page_tables__DATA
00116208  __mod_init_func
00116218  __DATA
00116258  _rtk_data_uuid
00116268  __DATA
001162a8  _rtk_heap
001162b8  __DATA
001162f8  _rtk_threads
00116308  __DATA
00116348  __constructor
00116358  __DATA
00116398  __zerofill
001163a8  __DATA
001163f0  __DATA_SHARED_RO
00116430  _RTK_EXT_SHD_DTA__DATA_SHARED_RO
00116488  __DATA_CONST
0011a529  wwwwwww
0011dec5  2C)B1Kzd0Iz
0012144b  THix8c
00121522  @9jyhxI
00121746  @9Liw8
00121ec6  @9jyhxI
00127092  %NcX N&
0012d44b  Royjx0
00133423  K.z(xnYl
00137a00  iYix)%
0013a153  T-ih8nih8
0013d73b  TID@9?=
0014246b  Tiju8hC
001430bd  ylx/u@9o
00143159  ylx/u@9o
00143221  ykx?u@9k
00143261  ykx-u@9m
00146534  hSQ9(m
0014671b  9hSQ9(
001468b8  hSQ9HQ
00146ab4  hSQ9hA
00146afc  hSQ9(?
00146c2f  9hSQ9(
00146cf8  hSQ9H/
00166a48  8bunz8
0016711f  @fffff
00167126  q@fffffbv
00167208  Assertion failure: tid overflow
00167272  *AVz6@
001672f7  ?ajQap
00167b44  INVALID
00167b53  Marin-ASC1
00167b62  Tempest-ASC2
00167b71  Tempest-ASC3
00167b80  Tempest-ASC4
00167b8f  Tempest-ASC4.1
00167b9e  Tempest-ASC5
00167bad  Tempest-ASC6
00167bbc  Tempest-ASC7
00167c16  Chinook-ASC2
00167c25  Chinook2-ASC3
00167c34  Chinook-ASC4
00167c43  Chinook-ASC4.1
00167c52  Chinook-ASC5
00167c61  Chinook-ASC6
00167c70  Chinook-ASC7
00167c7f  ACC E Core
00167c8e  ACC P Core
00167c9d  ASC Chinook
00167cac  ASC Tempest
00167cbb  Scheduler ASC
00167cd2  Power Management ASC
00167fd8  RTKSTACK
00168024  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
00168a73  stk_fail
00168a7c  Invalid DM type %d for command type %d in %s
00168ace  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
00168b66  Incorrect power sub-state for early wake
00168b8f  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
00168bf5  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
00168c43  %s: !!! Fatal Error: Unknown Power state mode!
00168c92  Picked new Quantum size::%llu, Frame based quantum period:%u
00168cd0  In order eviction check is unsupported when multiple normal completion queues are enabled.
00168d2b  !!! Error: Unexpected scheduling pause timeout after %uus
00168d65  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
00168dd2  %s: !!! Fatal Error: Unhandled : Invalid command type %d
00168e3f  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
00168e89  AGFHRBResume
00168e96  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
00168eff  %s: CRE disabled by boot arg
00168f1c  AGFACREInit
00168f28  %s: CRE has restored our registers
00168f4b  %s: CRE has no restore data and will save registers this run.
00168f89  %s: Moving out of critical section having saved %i registers
00168fe2  %s: Moving out of critical section having verified %i registers
00169022  %s: Entering CRE critical section for save
00169069  %s: Entering CRE critical section as CRE disabled
0016909b  %s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celsius
0016912b  gfx_iop_msgs
00169138  gfx_iop_ints
00169145  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
00169175  Bucket overflow:: timestamp %llu, frame interval %llu, bucket_size %llu, bucket %u, num buckets %llu
001691da  PTD write failed (%u, %u)
001691f4  PTD read failed unexpectedly with error code 0x%x.
00169227  Invalid AON PTD Dev Instance, Was AON PTD initialized?
0016925e  Failed to read %c%c%c%c. Read Status = 0x%x
0016928a  Failed to Peek %c%c%c%c. Peek Status = 0x%x
001692b6  Failed to write %c%c%c%c. Write Status = 0x%x
001692e4  management
001692ef  crashlog
001692f8  gfx_msgs
00169301  gfx_ints
0016930a  Unsupported shared event agent index: %u
00169333  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
00169371  agfInitDoorbells
00169382  UMA FW id state has bad context ID. context_id: %d
001693b5  G18 Firmware initializing
001693cf    FW Build variant: g19p
001693e8    FW Build version: b0
001693ff    FW Build running in SKSM Enabled mode
00169427  VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)
00169485  Buffer size is too small to hold all counter values
001694b9  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
0016950f  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
0016955e  _agfGL2DependentPollReg32
00169578  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
001695e0  %s: !!! Fatal Error: Cre entry Index is greater than max GRT entries
00169625  AGFHALCREAddEntry
0016964c  Failed to enable CRE restore as sCRE hasn't been set up by iBoot.
001696b2  CPMS tracing will not be supported on G18
001696f4  agfGCPMSDisable
00169704  agfGCPMSEnable
0016972f  PBState must be unbind, before being rebound to different PB state
00169787  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
001697da  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
00169843  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
00169894  AON PTD Enable mask is 0 for mGPUS. Skipping!
001698c2  AON PTD Enable mask is 0 for Fabric. Skipping!
001698f1  Total Csw histograms collected: %lld
00169916  Initial Csw histogram timestamp: %#llx
0016993d  Total Csw traces collected: %lld
0016995e  Initial Csw trace timestamp: %#llx
00169981  Total IVDM histograms collected: %lld
001699a7  Initial IVDM histogram timestamp: %#llx
001699cf  Total IVDM traces collected: %lld
001699f1  Initial IVDM trace timestamp: %#llx
00169a15      Snapshot timestamp: %#llx
00169a33      Bucket %u: %u
00169a45      Number of samples: %u
00169a5f      Sample %u: %u
00169a71  Unable to grab init data from host
00169a94  Host and FW Interface is mismatched, please ensure the versions are aligned.
00169ae1  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
00169b40  GPU temperature slew rate timer period: %u us
00169b6e  %s: !!! Fatal Error: Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
00169c16  Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
00169c87  Spurious GPU slew rate interrupt!
00169ca9  %s: !!! Fatal Error: Invalid DataMaster %u
00169ced  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
00169d44   from 
00169d4b  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
00169dd8  TP_VDM
00169ddf  TP_PDM
00169de6  TP_CDM
00169ded  TP_RIA
00169df4  UFE_VDM0_CLQ
00169e01  UFE_VDM1_CLQ
00169e0e  UFE_PDM0_CLQ
00169e1b  UFE_PDM1_CLQ
00169e28  UFE_PDM2_CLQ
00169e35  UFE_CDM0_CLQ
00169e42  UFE_CDM1_CLQ
00169e4f  UFE_CDM2_CLQ
00169e5c  DPB0_TOTAL_ISS0
00169e6c  DPB1_TOTAL_ISS1
00169e7c  DPB0_AGEN
00169e86  DPB1_AGEN
00169e90  DPB0_TOTAL_DISPATCH
00169ea4  DPB1_TOTAL_DISPATCH
00169eb8  DPB0_F32
00169ec1  DPB1_F32
00169eca  DPB0_SCIB
00169ed4  DPB1_SCIB
00169ede  DPB0_IC
00169ee6  DPB1_IC
00169eee  DPB0_PERM
00169ef8  DPB1_PERM
00169f10  DPB0_F16
00169f19  DPB1_F16
00169f22  DPB0_MXU_WORK
00169f30  DPB1_MXU_WORK
0016a68d  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
0016a6e8  AGFAInitSequence unknown seq type %u
0016a70d  cold booted
0016a719  Unknown ASC version
0016a72d  GFX %s %u %s FW %s! (%s)
0016a746  Oct 13 2026 23:37:55
0016a75b  GPU is not powered on after power kick!
0016a783  agfMTRAlarmHandler
0016a796  %s: !!! Fatal Error: MTR Alarm interrupts not handled!
0016a7cd  %s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware! chainID=%u
0016a837  Failed to register cputrace handler
0016a85b  agx_power
0016a865  rif_shadow
0016a870  GPU is Powered On while we are about to Power down Fender
0016a8aa  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
0016a8e7  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
0016a924  %s: !!! Fatal Error: Error %x
0016a942  AGFASemaphoreSignal
0016a956  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
0016a9c8  Msg of type %u received, which can't be handled!
0016a9f9  %s: !!! Fatal Error: Unknown IOP msg type %d!
0016aa3c  %s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx
0016aaa3  !MIDR: 0x%x
0016aaaf  ~CsPTR
0016aab6  !ROf %#lx %#x
0016aac4  MMU private: s:%llx!=%llx b:%llx!=%llx
0016aaeb  MMU VA sz %u 0=%zu 1=%zu
0016ab04  MMU private !fit: b:%lx<%lx s:%lx>%lx
0016ab2a  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
0016ab57  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
0016ab89  MMU sh<ps: %llu > %llu
0016aba0  Page Table !vm export: %x
0016abba  GPTBAT !vm export: %x
0016abd0  PPL handoff !vm export: %x
0016abeb  !Mthd:%p
0016abf4  !msgmbxint
0016abff  !msgdoordashint
0016ac0f  mme:0x%x
0016ac1c  Duty cycle
0016ac2d  Sleep count
0016ac39  Wake count
0016ac44  Power state
0016ac50  Free heap
0016ac5a  Total heap
0016ac65  Peak heap alloc
0016ac75  Used stack
0016ac80  Total stack
0016ac8c  CPU count
0016ac9d  <null>
0016aca7  ThIntr:%u,%u,%u,%u
0016acba  ThLock:%p
0016acc4  MBI queue overflow:%s
0016acda  VmOv %d %d
0016ace5  rtk_ep_work
0016acf1  MGMT msg=0x%llx st=%x
0016ad07  MGMT st=%x
0016ad16  !clg: %08x
0016ad21  !cpy: %08x
0016ad2c  Not implemented
0016ad3c  Message Log
0016ad49  Invalid AP power: %d
0016ad65  RTKit: %s - Client: %s
0016ad7c  !Heapblk:%p
0016ad88  REDACTED
0016ad91  rtkptd.cpp
0016ad9c  %s:%d Invalid parameter range[%d]
0016adbe  ptd_write
0016adc8  %s:%d Range =%d info not found
0016ade7  %s:%d Invalid index[%d]
0016adff  %s:%d Invalid handle
0016ae14  %s:%d Bad write offset=0x%X
0016ae30  %s:%d Invalid parameter range[%d] or data = NULL
0016ae61  ptd_read
0016ae6a  %s:%d Bad Read offset=0x%X error:0x%x
0016ae90  range_param_check
0016aea2  %s:%d Unknown range[%d]
001919f8  lCytuDTRT
00191a50  tnCplSTRe
00191aa8  tnCkaWTRq
00191b00  tffOnOTR|
00191b58  EERFPHTR
00191bb1  LLAPHTR
00191c08  KAEPPHTR
00191c62  UKTSTR
00191cba  AKTSTR
00191d10  UPCmuNTR
00191eb0  not set
0022a56c  _RTK_abort
0022a577  _RTK_client_version_string
0022a592  _RTK_dev_asc
0022a59f  _RTK_dev_asc_config
0022a5b3  _RTK_dev_cputrace_metadata
0022a5ce  _RTK_dev_pts_ptd
0022a5df  _RTK_dev_pts_ptd_peek
0022a5f5  _RTK_dev_timesync_0
0022a609  _RTK_dev_wrapper_icu
0022a61e  _RTK_uppl_mapped_memory
0022a636  _SH_DATA_SEGS
0022a64a  ___bzero
0022a653  ___powisf2
0022a65e  ___stack_chk_fail
0022a670  ___stack_chk_guard
0022a683  ___stack_chk_guard_setup
0022a69c  __arm_arch_hibernate_uat
0022a6b5  __arm_arch_resume_uat
0022a6cb  __arm_cache_info
0022a6dc  __fp_context
0022a6e9  __hb_context
0022a6f6  __mbi_routes
0022a703  __mmu_config
0022a710  __nmi_frame
0022a71c  __platform_bzero
0022a72d  __platform_memcmp
0022a73f  __platform_memmove
0022a752  __platform_memset
0022a764  __rtk_arch_dead_loop
0022a779  __rtk_arch_exception
0022a78e  __rtk_arch_fast_interrupt
0022a7a8  __rtk_arch_gxf_vector_abort
0022a7c4  __rtk_arch_gxf_vectors
0022a7db  __rtk_arch_interrupt
0022a7f0  __rtk_arch_interrupted_pc
0022a80a  __rtk_arch_svc_handler
0022a821  __rtk_arch_vectors
0022a834  __rtk_arch_wait_for_interrupt
0022a852  __rtk_arch_wait_for_interrupt_retention
0022a87a  __rtk_arm_mmu_bits_per_level
0022a897  __rtk_arm_mmu_page_shift
0022a8b0  __rtk_arm_mmu_page_size
0022a8c8  __rtk_arm_start_bootstrap_area
0022a8e7  __rtk_armv8_bootstrap_page
0022a902  __rtk_armv8_l1_bootstrap
0022a91b  __rtk_astris_island
0022a92f  __rtk_cache_clean
0022a941  __rtk_cache_clean_invalidate
0022a95e  __rtk_cache_info_init
0022a974  __rtk_crashlog_is_local
0022a98c  __rtk_crashlog_local_buffer
0022a9a8  __rtk_crashlog_requested_size
0022a9c6  __rtk_crt_exc_stack
0022a9da  __rtk_crt_exc_stack_base
0022a9f3  __rtk_crt_exc_stack_len
0022aa0b  __rtk_crt_exc_stack_top
0022aa23  __rtk_crt_expect_boot_args
0022aa3e  __rtk_crt_init_stack
0022aa53  __rtk_crt_init_stack_base
0022aa6d  __rtk_crt_init_stack_len
0022aa86  __rtk_crt_init_stack_top
0022aa9f  __rtk_crt_irq_stack
0022aab3  __rtk_crt_irq_stack_base
0022aacc  __rtk_crt_irq_stack_len
0022aae4  __rtk_crt_irq_stack_top
0022aafc  __rtk_crt_mmu_addr_space_size_log2
0022ab1f  __rtk_crt_mmu_gxf_stack
0022ab37  __rtk_crt_mmu_gxf_stack_size
0022ab54  __rtk_crt_mmu_gxf_user_va_bits
0022ab73  __rtk_crt_mmu_gxf_version
0022ab8d  __rtk_crt_mmu_tables
0022aba2  __rtk_crt_mmu_ttbr1_private_space_size
0022abc9  __rtk_crt_mmu_ttbr_select_bitmap
0022abea  __rtk_crt_mmu_uat
0022abfc  __rtk_current_threads
0022ac12  __rtk_dcache_clean_invalidate_whole
0022ac36  __rtk_dcache_clean_whole
0022ac4f  __rtk_dev_bad_method
0022ac64  __rtk_gxf_entry
0022ac74  __rtk_gxf_initialized
0022ac8a  __rtk_ior
0022ac94  __rtk_mbi_max_route
0022aca8  __rtk_mbi_routes_array
0022acbf  __rtk_mmu_gxf_config
0022acd4  __rtk_mmu_gxf_config_swift
0022acef  __rtk_mmu_map
0022acfd  __rtk_mmu_region_disable
0022ad16  __rtk_mmu_switch_region_base
0022ad33  __rtk_mmu_tlb_invalidate_all
0022ad50  __rtk_mmu_unmap
0022ad60  __rtk_mmu_update_mapping
0022ad79  __rtk_mmu_virt_to_phys
0022ad90  __rtk_pac_safe_interrupts_disable
0022adb2  __rtk_pac_safe_interrupts_restore
0022add4  __rtk_patch_RTK_cpu_physical_address
0022adf9  __rtk_patch_RTK_cpu_wrapper_physical_address
0022ae26  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
0022ae57  __rtk_patch_RTK_io_base
0022ae6f  __rtk_patch_RTK_io_size
0022ae87  __rtk_patch_RTK_lock_legacy
0022aea3  __rtk_patch_RTK_mc_remote_alignment
0022aec7  __rtk_patch_RTK_pe_i_can_has_debugger
0022aeed  __rtk_patch_RTK_platform_flags
0022af0c  __rtk_patch_RTK_soc
0022af20  __rtk_patch_RTK_soc_revision
0022af3d  __rtk_patch__aslr_slide
0022af55  __rtk_patch__aslr_slide_src
0022af71  __rtk_patch__breakeven_pv
0022af8b  __rtk_patch__chain_starts
0022afa5  __rtk_patch__dseg_copy_length
0022afc3  __rtk_patch__dseg_relocate
0022afde  __rtk_patch__dseg_virt_source
0022affc  __rtk_patch__mkey_cfg_address
0022b01a  __rtk_patch__pac_entropy
0022b033  __rtk_patch__page_table_base
0022b050  __rtk_patch__page_table_size
0022b06d  __rtk_patch__rtk_dev_timebase_offset
0022b092  __rtk_patch__rtk_runtime_size
0022b0b0  __rtk_patch__rtk_stack_guard
0022b0cd  __rtk_patch__zerofill_length
0022b0ea  __rtk_patch__zerofill_start
0022b106  __rtk_patch_armv8_ignorenthint
0022b125  __rtk_patch_armv8_single_issue_neon
0022b149  __rtk_patch_armv8_timer_frequency
0022b16b  __rtk_patch_gxf_private_phy_space_base
0022b192  __rtk_patch_gxf_private_phy_space_size
0022b1b9  __rtk_patch_mmu_ttbr1_private_space_size
0022b1e2  __rtk_patch_page_table_virt_base
0022b203  __rtk_patch_tunables_size
0022b21d  __rtk_patch_tunables_start
0022b238  __rtk_patch_uat_gptbat_base
0022b254  __rtk_patch_uat_gptbat_size
0022b270  __rtk_patch_uat_ppl_shared_base
0022b290  __rtk_patch_uat_ppl_shared_l2_phys
0022b2b3  __rtk_platform_asc_retained_tunables_block
0022b2de  __rtk_platform_asc_tunables_block
0022b300  __rtk_power
0022b30c  __rtk_sign_initial_thread_state
0022b32c  __rtk_stack_watermark
0022b342  __rtk_thread_entry
0022b355  __rtk_thread_list
0022b367  __rtk_thread_list_size
0022b37e  __rtk_unexpected_reset
0022b395  __rtk_uppl_client_dispatch
0022b3b0  __rtk_version_string
0022b3c5  _arm_do_whole_dcache
0022b3da  _arm_fp_context
0022b3ea  _arm_fp_context_addr
0022b3ff  _arm_hb_context
0022b40f  _arm_hb_context_addr
0022b424  _arm_hb_sleep_count
0022b438  _arm_hb_wake_count
0022b44b  _arm_resume_flag
0022b45c  _armv8_timebase
0022b472  _bzero
0022b479  _gCrashLog
0022b484  _gMemoryAllocator
0022b496  _gxf_code_pad_sym
0022b4a8  _memcmp
0022b4b0  _memcpy
0022b4b8  _memmove
0022b4c1  _memset
0022b4c9  _mmu_get_page_table
0022b4dd  _mmu_get_tt_info
0022b4f3  _vm_regions
0022b4ff  dcache_op_poc
0022b50d  new_rtk_start_anywhere_uatv2
0022b558  __TEXT
0022b598  __text
0022b5a8  __TEXT
0022b5e8  __gxf_code
0022b5f8  __TEXT
0022b638  __gxf_code_pad
0022b648  __TEXT
0022b688  __gxf_shr_code
0022b698  __TEXT
0022b6d8  __const
0022b6e8  __TEXT
0022b728  _rtk_patchbay
0022b738  __TEXT
0022b778  _rtk_tunables
0022b788  __TEXT
0022b7c8  __cstring
0022b7d8  __TEXT
0022b818  __init_offsets
0022b828  __TEXT
0022b868  __chain_starts
0022b878  __TEXT
0022b8c0  __DATA
0022b900  __gxf_data
0022b910  __DATA
0022b950  __data
0022b960  __DATA
0022b9a0  _rtk_init_stack
0022b9b0  __DATA
0022b9f0  __const
0022ba00  __DATA
0022ba40  _rtk_irq_stack
0022ba50  __DATA
0022ba90  _rtk_exc_stack
0022baa0  __DATA
0022bae0  _rtk_boot_l1
0022baf0  __DATA
0022bb30  _rtk_boot
0022bb40  __DATA
0022bb80  _rtk_mtab
0022bb90  __DATA
0022bbd0  _rtk_power
0022bbe0  __DATA
0022bc20  _rtk_page_tables__DATA
0022bc70  __mod_init_func
0022bc80  __DATA
0022bcc0  _rtk_data_uuid
0022bcd0  __DATA
0022bd10  _rtk_heap
0022bd20  __DATA
0022bd60  _rtk_threads
0022bd70  __DATA
0022bdb0  __constructor
0022bdc0  __DATA
0022be00  __zerofill
0022be10  __DATA
0022be58  __DATA_SHARED_RO
0022be98  _RTK_EXT_SHD_DTA__DATA_SHARED_RO
0022bef0  __DATA_CONST
0022ff91  wwwwwww
0023387d  2C)B1Kzd0Iz
00236d17  THix8c
00236dee  @9jyhxI
00237012  @9Liw8
00237792  @9jyhxI
0023c95e  %NcX N&
00242d1b  Royjx0
00248d5f  K.z(xnYl
0024d360  iYix)%
0024fab3  T-ih8nih8
0025309b  TID@9?=
00257dcb  Tiju8hC
00258969  ylx/u@9o
00258a05  ylx/u@9o
00258acd  ykx?u@9k
00258b0d  ykx-u@9m
0025bde0  hSQ9(m
0025bfc7  9hSQ9(
0025c164  hSQ9HQ
0025c360  hSQ9hA
0025c3a8  hSQ9(?
0025c4db  9hSQ9(
0025c5a4  hSQ9H/
0027c4b0  8bunz8
0027cb87  @fffff
0027cb8e  q@fffffbv
0027cc70  Assertion failure: tid overflow
0027cd1f  ?KinWc.
0027d604  INVALID
0027d613  Marin-ASC1
0027d622  Tempest-ASC2
0027d631  Tempest-ASC3
0027d640  Tempest-ASC4
0027d64f  Tempest-ASC4.1
0027d65e  Tempest-ASC5
0027d66d  Tempest-ASC6
0027d67c  Tempest-ASC7
0027d6d6  Chinook-ASC2
0027d6e5  Chinook2-ASC3
0027d6f4  Chinook-ASC4
0027d703  Chinook-ASC4.1
0027d712  Chinook-ASC5
0027d721  Chinook-ASC6
0027d730  Chinook-ASC7
0027d73f  ACC E Core
0027d74e  ACC P Core
0027d75d  ASC Chinook
0027d76c  ASC Tempest
0027d77b  Scheduler ASC
0027d792  Power Management ASC
0027da98  RTKSTACK
0027dae4  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
0027e533  stk_fail
0027e53c  Invalid DM type %d for command type %d in %s
0027e58e  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
0027e626  Incorrect power sub-state for early wake
0027e64f  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
0027e6b5  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
0027e703  %s: !!! Fatal Error: Unknown Power state mode!
0027e752  Picked new Quantum size::%llu, Frame based quantum period:%u
0027e790  In order eviction check is unsupported when multiple normal completion queues are enabled.
0027e7eb  !!! Error: Unexpected scheduling pause timeout after %uus
0027e825  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
0027e892  %s: !!! Fatal Error: Unhandled : Invalid command type %d
0027e8ff  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
0027e949  AGFHRBResume
0027e956  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
0027e9bf  %s: CRE disabled by boot arg
0027e9dc  AGFACREInit
0027e9e8  %s: CRE has restored our registers
0027ea0b  %s: CRE has no restore data and will save registers this run.
0027ea49  %s: Moving out of critical section having saved %i registers
0027eaa2  %s: Moving out of critical section having verified %i registers
0027eae2  %s: Entering CRE critical section for save
0027eb29  %s: Entering CRE critical section as CRE disabled
0027eb5b  %s: !!! Fatal Error: GPU SoCHot interrupt received. Enabled sensor mask = %.16llx. Alarm%u Threshold = %u celsius
0027ebeb  gfx_iop_msgs
0027ebf8  gfx_iop_ints
0027ec05  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
0027ec35  Bucket overflow:: timestamp %llu, frame interval %llu, bucket_size %llu, bucket %u, num buckets %llu
0027ec9a  PTD write failed (%u, %u)
0027ecb4  PTD read failed unexpectedly with error code 0x%x.
0027ece7  Invalid AON PTD Dev Instance, Was AON PTD initialized?
0027ed1e  Failed to read %c%c%c%c. Read Status = 0x%x
0027ed4a  Failed to Peek %c%c%c%c. Peek Status = 0x%x
0027ed76  Failed to write %c%c%c%c. Write Status = 0x%x
0027eda4  management
0027edaf  crashlog
0027edb8  gfx_msgs
0027edc1  gfx_ints
0027edca  Unsupported shared event agent index: %u
0027edf3  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
0027ee31  agfInitDoorbells
0027ee42  UMA FW id state has bad context ID. context_id: %d
0027ee75  G18 Firmware initializing
0027ee8f    FW Build variant: g19a
0027eea8    FW Build version: a0
0027eebf    FW Build running in SKSM Enabled mode
0027eee7  VCM perf state change timeout after %uus (VCM_PERF_STATE_CONTROL = %x)
0027ef45  Buffer size is too small to hold all counter values
0027ef79  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
0027efcf  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
0027f01e  _agfGL2DependentPollReg32
0027f038  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
0027f0a0  %s: !!! Fatal Error: Cre entry Index is greater than max GRT entries
0027f0e5  AGFHALCREAddEntry
0027f10c  Failed to enable CRE restore as sCRE hasn't been set up by iBoot.
0027f172  CPMS tracing will not be supported on G18
0027f1b4  agfGCPMSDisable
0027f1c4  agfGCPMSEnable
0027f1ef  PBState must be unbind, before being rebound to different PB state
0027f247  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
0027f29a  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
0027f303  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
0027f354  AON PTD Enable mask is 0 for mGPUS. Skipping!
0027f382  AON PTD Enable mask is 0 for Fabric. Skipping!
0027f3b1  Total Csw histograms collected: %lld
0027f3d6  Initial Csw histogram timestamp: %#llx
0027f3fd  Total Csw traces collected: %lld
0027f41e  Initial Csw trace timestamp: %#llx
0027f441  Total IVDM histograms collected: %lld
0027f467  Initial IVDM histogram timestamp: %#llx
0027f48f  Total IVDM traces collected: %lld
0027f4b1  Initial IVDM trace timestamp: %#llx
0027f4d5      Snapshot timestamp: %#llx
0027f4f3      Bucket %u: %u
0027f505      Number of samples: %u
0027f51f      Sample %u: %u
0027f531  Unable to grab init data from host
0027f554  Host and FW Interface is mismatched, please ensure the versions are aligned.
0027f5a1  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
0027f600  GPU temperature slew rate timer period: %u us
0027f62e  %s: !!! Fatal Error: Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
0027f6d6  Slew Rate Event! IP Block=GPU MTR_TOP=0 Sensor=MTR_THERMAL%u Direction=%s Temperature=%u.%06uC MaxDelta=%u.%02uC
0027f747  Spurious GPU slew rate interrupt!
0027f769  %s: !!! Fatal Error: Invalid DataMaster %u
0027f7ad  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
0027f804   from 
0027f80b  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
0027f898  TP_VDM
0027f89f  TP_PDM
0027f8a6  TP_CDM
0027f8ad  TP_RIA
0027f8b4  UFE_VDM0_CLQ
0027f8c1  UFE_VDM1_CLQ
0027f8ce  UFE_PDM0_CLQ
0027f8db  UFE_PDM1_CLQ
0027f8e8  UFE_PDM2_CLQ
0027f8f5  UFE_CDM0_CLQ
0027f902  UFE_CDM1_CLQ
0027f90f  UFE_CDM2_CLQ
0027f91c  DPB0_TOTAL_ISS0
0027f92c  DPB1_TOTAL_ISS1
0027f93c  DPB0_AGEN
0027f946  DPB1_AGEN
0027f950  DPB0_TOTAL_DISPATCH
0027f964  DPB1_TOTAL_DISPATCH
0027f978  DPB0_F32
0027f981  DPB1_F32
0027f98a  DPB0_SCIB
0027f994  DPB1_SCIB
0027f99e  DPB0_IC
0027f9a6  DPB1_IC
0027f9ae  DPB0_PERM
0027f9b8  DPB1_PERM
0027f9d0  DPB0_F16
0027f9d9  DPB1_F16
0027f9e2  DPB0_MXU_WORK
0027f9f0  DPB1_MXU_WORK
0028014d  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
002801a8  AGFAInitSequence unknown seq type %u
002801cd  cold booted
002801d9  Unknown ASC version
002801ed  GFX %s %u %s FW %s! (%s)
00280206  Oct 13 2026 23:41:56
0028021b  GPU is not powered on after power kick!
00280243  agfMTRAlarmHandler
00280256  %s: !!! Fatal Error: MTR Alarm interrupts not handled!
0028028d  %s: !!! Fatal Error: Received MTR Alarm interrupt from GPU but no match found in MTR hardware! chainID=%u
002802f7  Failed to register cputrace handler
0028031b  agx_power
00280325  rif_shadow
00280330  GPU is Powered On while we are about to Power down Fender
0028036a  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
002803a7  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
002803e4  %s: !!! Fatal Error: Error %x
00280402  AGFASemaphoreSignal
00280416  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
00280488  Msg of type %u received, which can't be handled!
002804b9  %s: !!! Fatal Error: Unknown IOP msg type %d!
002804fc  %s: !!! Fatal Error: Unrecognized recovery power cycle event 0x%llx
00280563  !MIDR: 0x%x
0028056f  ~CsPTR
00280576  !ROf %#lx %#x
00280584  MMU private: s:%llx!=%llx b:%llx!=%llx
002805ab  MMU VA sz %u 0=%zu 1=%zu
002805c4  MMU private !fit: b:%lx<%lx s:%lx>%lx
002805ea  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
00280617  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
00280649  MMU sh<ps: %llu > %llu
00280660  Page Table !vm export: %x
0028067a  GPTBAT !vm export: %x
00280690  PPL handoff !vm export: %x
002806ab  !Mthd:%p
002806b4  !msgmbxint
002806bf  !msgdoordashint
002806cf  mme:0x%x
002806dc  Duty cycle
002806ed  Sleep count
002806f9  Wake count
00280704  Power state
00280710  Free heap
0028071a  Total heap
00280725  Peak heap alloc
00280735  Used stack
00280740  Total stack
0028074c  CPU count
0028075d  <null>
00280767  ThIntr:%u,%u,%u,%u
0028077a  ThLock:%p
00280784  MBI queue overflow:%s
0028079a  VmOv %d %d
002807a5  rtk_ep_work
002807b1  MGMT msg=0x%llx st=%x
002807c7  MGMT st=%x
002807d6  !clg: %08x
002807e1  !cpy: %08x
002807ec  Not implemented
002807fc  Message Log
00280809  Invalid AP power: %d
00280825  RTKit: %s - Client: %s
0028083c  !Heapblk:%p
00280848  REDACTED
00280851  rtkptd.cpp
0028085c  %s:%d Invalid parameter range[%d]
0028087e  ptd_write
00280888  %s:%d Range =%d info not found
002808a7  %s:%d Invalid index[%d]
002808bf  %s:%d Invalid handle
002808d4  %s:%d Bad write offset=0x%X
002808f0  %s:%d Invalid parameter range[%d] or data = NULL
00280921  ptd_read
0028092a  %s:%d Bad Read offset=0x%X error:0x%x
00280950  range_param_check
00280962  %s:%d Unknown range[%d]
002a7460  lCytuDTR
002a74b8  tnCplSTR
002a7510  tnCkaWTR
002a7568  tffOnOTR
002a75c0  EERFPHTR
002a7619  LLAPHTR
002a7670  KAEPPHTR
002a76ca  UKTSTR
002a7722  AKTSTR
002a7778  UPCmuNTR
002a7918  not set
0033ffd4  _RTK_abort
0033ffdf  _RTK_client_version_string
0033fffa  _RTK_dev_asc
00340007  _RTK_dev_asc_config
0034001b  _RTK_dev_cputrace_metadata
00340036  _RTK_dev_pts_ptd
00340047  _RTK_dev_pts_ptd_peek
0034005d  _RTK_dev_timesync_0
00340071  _RTK_dev_wrapper_icu
00340086  _RTK_uppl_mapped_memory
0034009e  _SH_DATA_SEGS
003400b2  ___bzero
003400bb  ___powisf2
003400c6  ___stack_chk_fail
003400d8  ___stack_chk_guard
003400eb  ___stack_chk_guard_setup
00340104  __arm_arch_hibernate_uat
0034011d  __arm_arch_resume_uat
00340133  __arm_cache_info
00340144  __fp_context
00340151  __hb_context
0034015e  __mbi_routes
0034016b  __mmu_config
00340178  __nmi_frame
00340184  __platform_bzero
00340195  __platform_memcmp
003401a7  __platform_memmove
003401ba  __platform_memset
003401cc  __rtk_arch_dead_loop
003401e1  __rtk_arch_exception
003401f6  __rtk_arch_fast_interrupt
00340210  __rtk_arch_gxf_vector_abort
0034022c  __rtk_arch_gxf_vectors
00340243  __rtk_arch_interrupt
00340258  __rtk_arch_interrupted_pc
00340272  __rtk_arch_svc_handler
00340289  __rtk_arch_vectors
0034029c  __rtk_arch_wait_for_interrupt
003402ba  __rtk_arch_wait_for_interrupt_retention
003402e2  __rtk_arm_mmu_bits_per_level
003402ff  __rtk_arm_mmu_page_shift
00340318  __rtk_arm_mmu_page_size
00340330  __rtk_arm_start_bootstrap_area
0034034f  __rtk_armv8_bootstrap_page
0034036a  __rtk_armv8_l1_bootstrap
00340383  __rtk_astris_island
00340397  __rtk_cache_clean
003403a9  __rtk_cache_clean_invalidate
003403c6  __rtk_cache_info_init
003403dc  __rtk_crashlog_is_local
003403f4  __rtk_crashlog_local_buffer
00340410  __rtk_crashlog_requested_size
0034042e  __rtk_crt_exc_stack
00340442  __rtk_crt_exc_stack_base
0034045b  __rtk_crt_exc_stack_len
00340473  __rtk_crt_exc_stack_top
0034048b  __rtk_crt_expect_boot_args
003404a6  __rtk_crt_init_stack
003404bb  __rtk_crt_init_stack_base
003404d5  __rtk_crt_init_stack_len
003404ee  __rtk_crt_init_stack_top
00340507  __rtk_crt_irq_stack
0034051b  __rtk_crt_irq_stack_base
00340534  __rtk_crt_irq_stack_len
0034054c  __rtk_crt_irq_stack_top
00340564  __rtk_crt_mmu_addr_space_size_log2
00340587  __rtk_crt_mmu_gxf_stack
0034059f  __rtk_crt_mmu_gxf_stack_size
003405bc  __rtk_crt_mmu_gxf_user_va_bits
003405db  __rtk_crt_mmu_gxf_version
003405f5  __rtk_crt_mmu_tables
0034060a  __rtk_crt_mmu_ttbr1_private_space_size
00340631  __rtk_crt_mmu_ttbr_select_bitmap
00340652  __rtk_crt_mmu_uat
00340664  __rtk_current_threads
0034067a  __rtk_dcache_clean_invalidate_whole
0034069e  __rtk_dcache_clean_whole
003406b7  __rtk_dev_bad_method
003406cc  __rtk_gxf_entry
003406dc  __rtk_gxf_initialized
003406f2  __rtk_ior
003406fc  __rtk_mbi_max_route
00340710  __rtk_mbi_routes_array
00340727  __rtk_mmu_gxf_config
0034073c  __rtk_mmu_gxf_config_swift
00340757  __rtk_mmu_map
00340765  __rtk_mmu_region_disable
0034077e  __rtk_mmu_switch_region_base
0034079b  __rtk_mmu_tlb_invalidate_all
003407b8  __rtk_mmu_unmap
003407c8  __rtk_mmu_update_mapping
003407e1  __rtk_mmu_virt_to_phys
003407f8  __rtk_pac_safe_interrupts_disable
0034081a  __rtk_pac_safe_interrupts_restore
0034083c  __rtk_patch_RTK_cpu_physical_address
00340861  __rtk_patch_RTK_cpu_wrapper_physical_address
0034088e  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
003408bf  __rtk_patch_RTK_io_base
003408d7  __rtk_patch_RTK_io_size
003408ef  __rtk_patch_RTK_lock_legacy
0034090b  __rtk_patch_RTK_mc_remote_alignment
0034092f  __rtk_patch_RTK_pe_i_can_has_debugger
00340955  __rtk_patch_RTK_platform_flags
00340974  __rtk_patch_RTK_soc
00340988  __rtk_patch_RTK_soc_revision
003409a5  __rtk_patch__aslr_slide
003409bd  __rtk_patch__aslr_slide_src
003409d9  __rtk_patch__breakeven_pv
003409f3  __rtk_patch__chain_starts
00340a0d  __rtk_patch__dseg_copy_length
00340a2b  __rtk_patch__dseg_relocate
00340a46  __rtk_patch__dseg_virt_source
00340a64  __rtk_patch__mkey_cfg_address
00340a82  __rtk_patch__pac_entropy
00340a9b  __rtk_patch__page_table_base
00340ab8  __rtk_patch__page_table_size
00340ad5  __rtk_patch__rtk_dev_timebase_offset
00340afa  __rtk_patch__rtk_runtime_size
00340b18  __rtk_patch__rtk_stack_guard
00340b35  __rtk_patch__zerofill_length
00340b52  __rtk_patch__zerofill_start
00340b6e  __rtk_patch_armv8_ignorenthint
00340b8d  __rtk_patch_armv8_single_issue_neon
00340bb1  __rtk_patch_armv8_timer_frequency
00340bd3  __rtk_patch_gxf_private_phy_space_base
00340bfa  __rtk_patch_gxf_private_phy_space_size
00340c21  __rtk_patch_mmu_ttbr1_private_space_size
00340c4a  __rtk_patch_page_table_virt_base
00340c6b  __rtk_patch_tunables_size
00340c85  __rtk_patch_tunables_start
00340ca0  __rtk_patch_uat_gptbat_base
00340cbc  __rtk_patch_uat_gptbat_size
00340cd8  __rtk_patch_uat_ppl_shared_base
00340cf8  __rtk_patch_uat_ppl_shared_l2_phys
00340d1b  __rtk_platform_asc_retained_tunables_block
00340d46  __rtk_platform_asc_tunables_block
00340d68  __rtk_power
00340d74  __rtk_sign_initial_thread_state
00340d94  __rtk_stack_watermark
00340daa  __rtk_thread_entry
00340dbd  __rtk_thread_list
00340dcf  __rtk_thread_list_size
00340de6  __rtk_unexpected_reset
00340dfd  __rtk_uppl_client_dispatch
00340e18  __rtk_version_string
00340e2d  _arm_do_whole_dcache
00340e42  _arm_fp_context
00340e52  _arm_fp_context_addr
00340e67  _arm_hb_context
00340e77  _arm_hb_context_addr
00340e8c  _arm_hb_sleep_count
00340ea0  _arm_hb_wake_count
00340eb3  _arm_resume_flag
00340ec4  _armv8_timebase
00340eda  _bzero
00340ee1  _gCrashLog
00340eec  _gMemoryAllocator
00340efe  _gxf_code_pad_sym
00340f10  _memcmp
00340f18  _memcpy
00340f20  _memmove
00340f29  _memset
00340f31  _mmu_get_page_table
00340f45  _mmu_get_tt_info
00340f5b  _vm_regions
00340f67  dcache_op_poc
00340f75  new_rtk_start_anywhere_uatv2
```
