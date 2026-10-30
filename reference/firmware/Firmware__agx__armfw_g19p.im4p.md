# `Firmware/agx/armfw_g19p.im4p`

- File size: 3,460,945 bytes
- IM4P: Tag: IM4P  Type: gfxf  Version: 1
- BuildManifest components that use it: `GFX`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         gfxf
  Version:      1
  Data:         3.5 MB (3460920 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 3,460,920 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit: %s - Client: %s`
- `RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release`

## Strings (1,276) [FW]

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
00015b33  NBX nB
0001766c  vzA9yZA9u
0001777a  @9jyhxI
0001797a  @9Liz8J
000180fe  @9jyhxI
0001a12f  K.z(xnYl
0001d26d  2C)B1Kzd0Iz
0001eb68  iYix)%
000263a5  ylx/u@9o
00026441  ylx/u@9o
00026509  ykx?u@9k
00026549  ykx-u@9m
000295d8  ji-xji,x
0004cfe0  8bunz8
0004d6b0  Assertion failure: tid overflow
0004e2b4  INVALID
0004e2c3  Marin-ASC1
0004e2d2  Tempest-ASC2
0004e2e1  Tempest-ASC3
0004e2f0  Tempest-ASC4
0004e2ff  Tempest-ASC4.1
0004e30e  Tempest-ASC5
0004e31d  Tempest-ASC6
0004e32c  Tempest-ASC7
0004e386  Chinook-ASC2
0004e395  Chinook2-ASC3
0004e3a4  Chinook-ASC4
0004e3b3  Chinook-ASC4.1
0004e3c2  Chinook-ASC5
0004e3d1  Chinook-ASC6
0004e3e0  Chinook-ASC7
0004e3ef  ACC E Core
0004e3fe  ACC P Core
0004e40d  ASC Chinook
0004e41c  ASC Tempest
0004e42b  Scheduler ASC
0004e442  Power Management ASC
0004e658  RTKSTACK
0004e6a4  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
0004f0f3  stk_fail
0004f0fc  AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
0004f15d  %s: !!! Fatal Error: AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
0004f1f2  agf_timer_usc_inst_cf is set to %d, FW will do periodic USC instructions cache flush for testing
0004f253  Invalid DM type %d for command type %d in %s
0004f2a5  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
0004f33d  %s: !!! Fatal Error: SFE_Tier3 detected!!
0004f387  %s: !!! Fatal Error: Thor Hammer Mode detected!! clique_wait_timedout: %u, thm_tier3_active: %u, dpb_watchdog_active: %u, ul1c_watchdog_active: %u, ria_watchdog_active: %u, srs_watchdog_active: %u, ttm_watchdog_active: %u
0004f465  unexpected command type (%d) indicated by SKU in %s
0004f4bf  CDM context store took too long (latency = %u us, threshold = %u us, req time %llu, complete time %llu)
0004f527  %s: !!! Fatal Error: Lockup Detection: legacy mode not supported when Lockup Hints interrupts are enabled: try using the agf_lockup_hint_irqs=0 boot-arg
0004f5dd  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
0004f643  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
0004f691  In order eviction check is unsupported when multiple normal completion queues are enabled.
0004f6ec  Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx
0004f747  -> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)
0004f7a0  %s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx
0004f841  NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x
0004f8a9  Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx
0004f908  KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx
0004f98f  !!! Error: Unexpected scheduling pause timeout after %uus
0004f9c9  %s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p
0004fa41  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
0004faae  %s: !!! Fatal Error: Unhandled : Invalid command type %d
0004fae7  Unimplemented. AGFAGXInterruptPMThresholdHandler
0004fb18  Context Restore Timed Out! QueueId %u
0004fb72  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
0004fbbc  AGFHRBResume
0004fbc9  Context Store Timed Out! DM %u, QueueId %u
0004fbf4  %s: !!! Fatal Error: Unknown state = %d
0004fc32  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
0004fc9b  %s: !!! Fatal Error: Unrecognized gtp discard mode
0004fcce  AGFPMOOMHandler
0004fcde  %s: !!! Fatal Error: Deferred TSQ buffer has no free space!
0004fd3e  gfx_iop_msgs
0004fd4b  gfx_iop_ints
0004fd58  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
0004fd88  Failed to allocate new ring entry
0004fdaa  management
0004fdb5  crashlog
0004fdbe  gfx_msgs
0004fdc7  gfx_ints
0004fdd0  Unsupported shared event agent index: %u
0004fdf9  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
0004fe37  agfInitDoorbells
0004fe48  gfx_msr
0004fe50  AGFSignalPagePoolStarved(TopSlotsStarvedMask=%#llx)
0004fe84  AGFSignalPagePoolStarved(found ppid=%i)
0004feac  Error: PPID Starved: %i
0004fec4  Error: Topslots starved=%#llx
0004fee2  %s: !!! Fatal Error: Error: Got a starvation interrupt with no irritator enabled
0004ff4c  Starved: CS on SMA Oom for queues = %#llx-%#llx
0004ff7c  UMA FW id state has bad context ID. context_id: %d
0004ffaf  G18 Firmware initializing
0004ffc9    FW Build variant: g19p
0004ffe2    FW Build version: a0
0004fff9    FW Build running in SKSM Enabled mode
00050045     USC Pipe %u State Overview
00050063  AGX_CR_USC_VDM_SERV: 0x%llx
0005007f  AGX_CR_USC_PDM_SERV: 0x%llx
0005009b  AGX_CR_USC_CDM_SERV: 0x%llx
000500b7  AGX_CR_USC_VDM_DEBUG_STATUS: 0x%llx
000500db  AGX_CR_USC_PDM_DEBUG_STATUS: 0x%llx
000500ff  AGX_CR_USC_CDM_DEBUG_STATUS: 0x%llx
00050123  Buffer size is too small to hold all counter values
00050157  %s: !!! Fatal Error: unexpected indexing type (%d) for register range 0x%x
000501be  Unexpected page fault requestor (%u)
000501e3  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
00050249  CPMS tracing will not be supported on G18
00050273  PBState must be unbind, before being rebound to different PB state
000502e8  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
00050339  Unable to grab init data from host
0005035c  Host and FW Interface is mismatched, please ensure the versions are aligned.
000503a9  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
00050408  _agfGL2DependentPollReg32
00050422  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
0005048a  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
000504dd  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
00050546  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
0005059c  %s: !!! Fatal Error: Invalid DataMaster %u
000505e0  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
00050637   from 
0005063e  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
00050e3b  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
00050e96  cold booted
00050ea2  Unknown ASC version
00050eb6  GFX %s %u %s FW %s! (%s)
00050ecf  Oct 13 2026 23:27:16
00050ee4  GPU is not powered on after power kick!
00050f0c  Failed to register cputrace handler
00050f30  agx_scheduler
00050f3e  agx_recovery
00050f4b  agx_sampler
00050f57  agx_pwr_metrics_server
00050f6e  GPU is Powered On while we are about to Power down Fender
00050fa8  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
00050fe5  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
00051022  %s: !!! Fatal Error: Error %x
00051040  AGFASemaphoreSignal
00051054  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
000510c6  Msg of type %u received, which can't be handled!
000510f7  %s: !!! Fatal Error: Unknown IOP msg type %d!
0005113a  %s: !!! Fatal Error: Unexpected recovery type %llu!
0005118b  %s: !!! Fatal Error: Unknown message received (event = %llu)
000511e6  %s: !!! Fatal Error: Invalid Power Server Kick %llu
00051235  %s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx
00051276  agfaRemotePowerKick
0005128a  !MIDR: 0x%x
00051296  ~CsPTR
0005129d  !ROf %#lx %#x
000512ab  MMU private: s:%llx!=%llx b:%llx!=%llx
000512d2  MMU VA sz %u 0=%zu 1=%zu
000512eb  MMU private !fit: b:%lx<%lx s:%lx>%lx
00051311  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
0005133e  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
00051370  MMU sh<ps: %llu > %llu
00051387  Page Table !vm export: %x
000513a1  GPTBAT !vm export: %x
000513b7  PPL handoff !vm export: %x
000513d2  !Mthd:%p
000513db  !msgmbxint
000513e6  !msgdoordashint
000513f6  mme:0x%x
00051403  Duty cycle
00051414  Sleep count
00051420  Wake count
0005142b  Power state
00051437  Free heap
00051441  Total heap
0005144c  Peak heap alloc
0005145c  Used stack
00051467  Total stack
00051473  CPU count
00051484  <null>
0005148e  ThIntr:%u,%u,%u,%u
000514a1  ThLock:%p
000514ab  MBI queue overflow:%s
000514c1  VmOv %d %d
000514cc  rtk_ep_work
000514d8  MGMT msg=0x%llx st=%x
000514ee  MGMT st=%x
000514fd  !clg: %08x
00051508  !cpy: %08x
00051513  Not implemented
00051523  Message Log
00051530  Invalid AP power: %d
0005154c  RTKit: %s - Client: %s
00051563  !Heapblk:%p
0005156f  REDACTED
00078038  lCytuDTR
00078090  tnCplSTR
000780e8  tnCkaWTR
00078140  tffOnOTR
00078198  EERFPHTR
000781f1  LLAPHTR
00078248  KAEPPHTR
000782a2  UKTSTR
000782fa  AKTSTR
00078350  UPCmuNTR
000784f0  not set
00078b00  RTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACK
00118af4  _RTK_abort
00118aff  _RTK_client_version_string
00118b1a  _RTK_dev_asc
00118b27  _RTK_dev_asc_config
00118b3b  _RTK_dev_cputrace_metadata
00118b56  _RTK_dev_pts_ptd
00118b67  _RTK_dev_pts_ptd_peek
00118b7d  _RTK_dev_timesync_0
00118b91  _RTK_dev_wrapper_icu
00118ba6  _RTK_uppl_mapped_memory
00118bbe  _SH_DATA_SEGS
00118bd2  ___bzero
00118bdb  ___stack_chk_fail
00118bed  ___stack_chk_guard
00118c00  ___stack_chk_guard_setup
00118c19  __arm_arch_hibernate_uat
00118c32  __arm_arch_resume_uat
00118c48  __arm_cache_info
00118c59  __fp_context
00118c66  __hb_context
00118c73  __mbi_routes
00118c80  __mmu_config
00118c8d  __nmi_frame
00118c99  __platform_bzero
00118caa  __platform_memcmp
00118cbc  __platform_memmove
00118ccf  __platform_memset
00118ce1  __rtk_arch_dead_loop
00118cf6  __rtk_arch_exception
00118d0b  __rtk_arch_fast_interrupt
00118d25  __rtk_arch_gxf_vector_abort
00118d41  __rtk_arch_gxf_vectors
00118d58  __rtk_arch_interrupt
00118d6d  __rtk_arch_interrupted_pc
00118d87  __rtk_arch_svc_handler
00118d9e  __rtk_arch_vectors
00118db1  __rtk_arch_wait_for_interrupt
00118dcf  __rtk_arch_wait_for_interrupt_retention
00118df7  __rtk_arm_mmu_bits_per_level
00118e14  __rtk_arm_mmu_page_shift
00118e2d  __rtk_arm_mmu_page_size
00118e45  __rtk_arm_start_bootstrap_area
00118e64  __rtk_armv8_bootstrap_page
00118e7f  __rtk_armv8_l1_bootstrap
00118e98  __rtk_astris_island
00118eac  __rtk_cache_clean
00118ebe  __rtk_cache_clean_invalidate
00118edb  __rtk_cache_info_init
00118ef1  __rtk_crashlog_is_local
00118f09  __rtk_crashlog_local_buffer
00118f25  __rtk_crashlog_requested_size
00118f43  __rtk_crt_exc_stack
00118f57  __rtk_crt_exc_stack_base
00118f70  __rtk_crt_exc_stack_len
00118f88  __rtk_crt_exc_stack_top
00118fa0  __rtk_crt_expect_boot_args
00118fbb  __rtk_crt_init_stack
00118fd0  __rtk_crt_init_stack_base
00118fea  __rtk_crt_init_stack_len
00119003  __rtk_crt_init_stack_top
0011901c  __rtk_crt_irq_stack
00119030  __rtk_crt_irq_stack_base
00119049  __rtk_crt_irq_stack_len
00119061  __rtk_crt_irq_stack_top
00119079  __rtk_crt_mmu_addr_space_size_log2
0011909c  __rtk_crt_mmu_gxf_stack
001190b4  __rtk_crt_mmu_gxf_stack_size
001190d1  __rtk_crt_mmu_gxf_user_va_bits
001190f0  __rtk_crt_mmu_gxf_version
0011910a  __rtk_crt_mmu_tables
0011911f  __rtk_crt_mmu_ttbr1_private_space_size
00119146  __rtk_crt_mmu_ttbr_select_bitmap
00119167  __rtk_crt_mmu_uat
00119179  __rtk_current_threads
0011918f  __rtk_dcache_clean_invalidate_whole
001191b3  __rtk_dcache_clean_whole
001191cc  __rtk_dev_bad_method
001191e1  __rtk_gxf_entry
001191f1  __rtk_gxf_initialized
00119207  __rtk_ior
00119211  __rtk_mbi_max_route
00119225  __rtk_mbi_routes_array
0011923c  __rtk_mmu_gxf_config
00119251  __rtk_mmu_gxf_config_swift
0011926c  __rtk_mmu_map
0011927a  __rtk_mmu_region_disable
00119293  __rtk_mmu_switch_region_base
001192b0  __rtk_mmu_tlb_invalidate_all
001192cd  __rtk_mmu_unmap
001192dd  __rtk_mmu_update_mapping
001192f6  __rtk_mmu_virt_to_phys
0011930d  __rtk_pac_safe_interrupts_disable
0011932f  __rtk_pac_safe_interrupts_restore
00119351  __rtk_patch_RTK_cpu_physical_address
00119376  __rtk_patch_RTK_cpu_wrapper_physical_address
001193a3  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
001193d4  __rtk_patch_RTK_io_base
001193ec  __rtk_patch_RTK_io_size
00119404  __rtk_patch_RTK_lock_legacy
00119420  __rtk_patch_RTK_mc_remote_alignment
00119444  __rtk_patch_RTK_pe_i_can_has_debugger
0011946a  __rtk_patch_RTK_platform_flags
00119489  __rtk_patch_RTK_soc
0011949d  __rtk_patch_RTK_soc_revision
001194ba  __rtk_patch__aslr_slide
001194d2  __rtk_patch__aslr_slide_src
001194ee  __rtk_patch__breakeven_pv
00119508  __rtk_patch__chain_starts
00119522  __rtk_patch__dseg_copy_length
00119540  __rtk_patch__dseg_relocate
0011955b  __rtk_patch__dseg_virt_source
00119579  __rtk_patch__mkey_cfg_address
00119597  __rtk_patch__pac_entropy
001195b0  __rtk_patch__page_table_base
001195cd  __rtk_patch__page_table_size
001195ea  __rtk_patch__rtk_dev_timebase_offset
0011960f  __rtk_patch__rtk_runtime_size
0011962d  __rtk_patch__rtk_stack_guard
0011964a  __rtk_patch__zerofill_length
00119667  __rtk_patch__zerofill_start
00119683  __rtk_patch_armv8_ignorenthint
001196a2  __rtk_patch_armv8_single_issue_neon
001196c6  __rtk_patch_armv8_timer_frequency
001196e8  __rtk_patch_gxf_private_phy_space_base
0011970f  __rtk_patch_gxf_private_phy_space_size
00119736  __rtk_patch_mmu_ttbr1_private_space_size
0011975f  __rtk_patch_page_table_virt_base
00119780  __rtk_patch_tunables_size
0011979a  __rtk_patch_tunables_start
001197b5  __rtk_patch_uat_gptbat_base
001197d1  __rtk_patch_uat_gptbat_size
001197ed  __rtk_patch_uat_ppl_shared_base
0011980d  __rtk_patch_uat_ppl_shared_l2_phys
00119830  __rtk_platform_asc_retained_tunables_block
0011985b  __rtk_platform_asc_tunables_block
0011987d  __rtk_power
00119889  __rtk_sign_initial_thread_state
001198a9  __rtk_stack_watermark
001198bf  __rtk_thread_entry
001198d2  __rtk_thread_list
001198e4  __rtk_thread_list_size
001198fb  __rtk_unexpected_reset
00119912  __rtk_uppl_client_dispatch
0011992d  __rtk_version_string
00119942  _arm_do_whole_dcache
00119957  _arm_fp_context
00119967  _arm_fp_context_addr
0011997c  _arm_hb_context
0011998c  _arm_hb_context_addr
001199a1  _arm_hb_sleep_count
001199b5  _arm_hb_wake_count
001199c8  _arm_resume_flag
001199d9  _armv8_timebase
001199ef  _bzero
001199f6  _gCrashLog
00119a01  _gMemoryAllocator
00119a13  _gxf_code_pad_sym
00119a25  _memcmp
00119a2d  _memcpy
00119a35  _memmove
00119a3e  _memset
00119a46  _mmu_get_page_table
00119a5a  _mmu_get_tt_info
00119a70  _vm_regions
00119a7c  dcache_op_poc
00119a8a  new_rtk_start_anywhere_uatv2
00119ad0  __TEXT
00119b10  __text
00119b20  __TEXT
00119b60  __gxf_code
00119b70  __TEXT
00119bb0  __gxf_code_pad
00119bc0  __TEXT
00119c00  __gxf_shr_code
00119c10  __TEXT
00119c50  __const
00119c60  __TEXT
00119ca0  _rtk_patchbay
00119cb0  __TEXT
00119cf0  _rtk_tunables
00119d00  __TEXT
00119d40  __cstring
00119d50  __TEXT
00119d90  __init_offsets
00119da0  __TEXT
00119de0  __chain_starts
00119df0  __TEXT
00119e38  __DATA
00119e78  __gxf_data
00119e88  __DATA
00119ec8  __data
00119ed8  __DATA
00119f18  _rtk_init_stack
00119f28  __DATA
00119f68  __const
00119f78  __DATA
00119fb8  _rtk_irq_stack
00119fc8  __DATA
0011a008  _rtk_exc_stack
0011a018  __DATA
0011a058  _rtk_boot_l1
0011a068  __DATA
0011a0a8  _rtk_boot
0011a0b8  __DATA
0011a0f8  _rtk_mtab
0011a108  __DATA
0011a148  _rtk_power
0011a158  __DATA
0011a198  _rtk_page_tables__DATA
0011a1e8  __mod_init_func
0011a1f8  __DATA
0011a238  _rtk_data_uuid
0011a248  __DATA
0011a288  _rtk_heap
0011a298  __DATA
0011a2d8  _rtk_threads
0011a2e8  __DATA
0011a328  __constructor
0011a338  __DATA
0011a378  __zerofill
0011a388  __DATA
0011a3d0  __DATA_SHARED_RO
0011a410  _RTK_EXT_SHD_DTA__DATA_SHARED_RO
0011a468  __DATA_CONST
0011e509  wwwwwww
0012f57b  NBX nB
001310b4  vzA9yZA9u
001311c2  @9jyhxI
001313c2  @9Liz8J
00131b46  @9jyhxI
00133b77  K.z(xnYl
00136cb5  2C)B1Kzd0Iz
001385b0  iYix)%
0013fded  ylx/u@9o
0013fe89  ylx/u@9o
0013ff51  ykx?u@9k
0013ff91  ykx-u@9m
00143020  ji-xji,x
00166a28  8bunz8
001670f8  Assertion failure: tid overflow
00167cfc  INVALID
00167d0b  Marin-ASC1
00167d1a  Tempest-ASC2
00167d29  Tempest-ASC3
00167d38  Tempest-ASC4
00167d47  Tempest-ASC4.1
00167d56  Tempest-ASC5
00167d65  Tempest-ASC6
00167d74  Tempest-ASC7
00167dce  Chinook-ASC2
00167ddd  Chinook2-ASC3
00167dec  Chinook-ASC4
00167dfb  Chinook-ASC4.1
00167e0a  Chinook-ASC5
00167e19  Chinook-ASC6
00167e28  Chinook-ASC7
00167e37  ACC E Core
00167e46  ACC P Core
00167e55  ASC Chinook
00167e64  ASC Tempest
00167e73  Scheduler ASC
00167e8a  Power Management ASC
001680a0  RTKSTACK
001680ec  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
00168b3b  stk_fail
00168b44  AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
00168ba5  %s: !!! Fatal Error: AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
00168c3a  agf_timer_usc_inst_cf is set to %d, FW will do periodic USC instructions cache flush for testing
00168c9b  Invalid DM type %d for command type %d in %s
00168ced  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
00168d85  %s: !!! Fatal Error: SFE_Tier3 detected!!
00168dcf  %s: !!! Fatal Error: Thor Hammer Mode detected!! clique_wait_timedout: %u, thm_tier3_active: %u, dpb_watchdog_active: %u, ul1c_watchdog_active: %u, ria_watchdog_active: %u, srs_watchdog_active: %u, ttm_watchdog_active: %u
00168ead  unexpected command type (%d) indicated by SKU in %s
00168f07  CDM context store took too long (latency = %u us, threshold = %u us, req time %llu, complete time %llu)
00168f6f  %s: !!! Fatal Error: Lockup Detection: legacy mode not supported when Lockup Hints interrupts are enabled: try using the agf_lockup_hint_irqs=0 boot-arg
00169025  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
0016908b  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
001690d9  In order eviction check is unsupported when multiple normal completion queues are enabled.
00169134  Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx
0016918f  -> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)
001691e8  %s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx
00169289  NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x
001692f1  Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx
00169350  KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx
001693d7  !!! Error: Unexpected scheduling pause timeout after %uus
00169411  %s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p
00169489  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
001694f6  %s: !!! Fatal Error: Unhandled : Invalid command type %d
0016952f  Unimplemented. AGFAGXInterruptPMThresholdHandler
00169560  Context Restore Timed Out! QueueId %u
001695ba  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
00169604  AGFHRBResume
00169611  Context Store Timed Out! DM %u, QueueId %u
0016963c  %s: !!! Fatal Error: Unknown state = %d
0016967a  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
001696e3  %s: !!! Fatal Error: Unrecognized gtp discard mode
00169716  AGFPMOOMHandler
00169726  %s: !!! Fatal Error: Deferred TSQ buffer has no free space!
00169786  gfx_iop_msgs
00169793  gfx_iop_ints
001697a0  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
001697d0  Failed to allocate new ring entry
001697f2  management
001697fd  crashlog
00169806  gfx_msgs
0016980f  gfx_ints
00169818  Unsupported shared event agent index: %u
00169841  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
0016987f  agfInitDoorbells
00169890  gfx_msr
00169898  AGFSignalPagePoolStarved(TopSlotsStarvedMask=%#llx)
001698cc  AGFSignalPagePoolStarved(found ppid=%i)
001698f4  Error: PPID Starved: %i
0016990c  Error: Topslots starved=%#llx
0016992a  %s: !!! Fatal Error: Error: Got a starvation interrupt with no irritator enabled
00169994  Starved: CS on SMA Oom for queues = %#llx-%#llx
001699c4  UMA FW id state has bad context ID. context_id: %d
001699f7  G18 Firmware initializing
00169a11    FW Build variant: g19p
00169a2a    FW Build version: b0
00169a41    FW Build running in SKSM Enabled mode
00169a8d     USC Pipe %u State Overview
00169aab  AGX_CR_USC_VDM_SERV: 0x%llx
00169ac7  AGX_CR_USC_PDM_SERV: 0x%llx
00169ae3  AGX_CR_USC_CDM_SERV: 0x%llx
00169aff  AGX_CR_USC_VDM_DEBUG_STATUS: 0x%llx
00169b23  AGX_CR_USC_PDM_DEBUG_STATUS: 0x%llx
00169b47  AGX_CR_USC_CDM_DEBUG_STATUS: 0x%llx
00169b6b  Buffer size is too small to hold all counter values
00169b9f  %s: !!! Fatal Error: unexpected indexing type (%d) for register range 0x%x
00169c06  Unexpected page fault requestor (%u)
00169c2b  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
00169c91  CPMS tracing will not be supported on G18
00169cbb  PBState must be unbind, before being rebound to different PB state
00169d30  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
00169d81  Unable to grab init data from host
00169da4  Host and FW Interface is mismatched, please ensure the versions are aligned.
00169df1  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
00169e50  _agfGL2DependentPollReg32
00169e6a  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
00169ed2  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
00169f25  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
00169f8e  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
00169fe4  %s: !!! Fatal Error: Invalid DataMaster %u
0016a028  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
0016a07f   from 
0016a086  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
0016a883  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
0016a8de  cold booted
0016a8ea  Unknown ASC version
0016a8fe  GFX %s %u %s FW %s! (%s)
0016a917  Oct 13 2026 23:35:04
0016a92c  GPU is not powered on after power kick!
0016a954  Failed to register cputrace handler
0016a978  agx_scheduler
0016a986  agx_recovery
0016a993  agx_sampler
0016a99f  agx_pwr_metrics_server
0016a9b6  GPU is Powered On while we are about to Power down Fender
0016a9f0  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
0016aa2d  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
0016aa6a  %s: !!! Fatal Error: Error %x
0016aa88  AGFASemaphoreSignal
0016aa9c  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
0016ab0e  Msg of type %u received, which can't be handled!
0016ab3f  %s: !!! Fatal Error: Unknown IOP msg type %d!
0016ab82  %s: !!! Fatal Error: Unexpected recovery type %llu!
0016abd3  %s: !!! Fatal Error: Unknown message received (event = %llu)
0016ac2e  %s: !!! Fatal Error: Invalid Power Server Kick %llu
0016ac7d  %s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx
0016acbe  agfaRemotePowerKick
0016acd2  !MIDR: 0x%x
0016acde  ~CsPTR
0016ace5  !ROf %#lx %#x
0016acf3  MMU private: s:%llx!=%llx b:%llx!=%llx
0016ad1a  MMU VA sz %u 0=%zu 1=%zu
0016ad33  MMU private !fit: b:%lx<%lx s:%lx>%lx
0016ad59  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
0016ad86  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
0016adb8  MMU sh<ps: %llu > %llu
0016adcf  Page Table !vm export: %x
0016ade9  GPTBAT !vm export: %x
0016adff  PPL handoff !vm export: %x
0016ae1a  !Mthd:%p
0016ae23  !msgmbxint
0016ae2e  !msgdoordashint
0016ae3e  mme:0x%x
0016ae4b  Duty cycle
0016ae5c  Sleep count
0016ae68  Wake count
0016ae73  Power state
0016ae7f  Free heap
0016ae89  Total heap
0016ae94  Peak heap alloc
0016aea4  Used stack
0016aeaf  Total stack
0016aebb  CPU count
0016aecc  <null>
0016aed6  ThIntr:%u,%u,%u,%u
0016aee9  ThLock:%p
0016aef3  MBI queue overflow:%s
0016af09  VmOv %d %d
0016af14  rtk_ep_work
0016af20  MGMT msg=0x%llx st=%x
0016af36  MGMT st=%x
0016af45  !clg: %08x
0016af50  !cpy: %08x
0016af5b  Not implemented
0016af6b  Message Log
0016af78  Invalid AP power: %d
0016af94  RTKit: %s - Client: %s
0016afab  !Heapblk:%p
0016afb7  REDACTED
00191a80  lCytuDTR
00191ad8  tnCplSTR
00191b30  tnCkaWTR
00191b88  tffOnOTR
00191be0  EERFPHTR
00191c39  LLAPHTR
00191c90  KAEPPHTR
00191cea  UKTSTR
00191d42  AKTSTR
00191d98  UPCmuNTR
00191f38  not set
00192548  RTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACK
0023253c  _RTK_abort
00232547  _RTK_client_version_string
00232562  _RTK_dev_asc
0023256f  _RTK_dev_asc_config
00232583  _RTK_dev_cputrace_metadata
0023259e  _RTK_dev_pts_ptd
002325af  _RTK_dev_pts_ptd_peek
002325c5  _RTK_dev_timesync_0
002325d9  _RTK_dev_wrapper_icu
002325ee  _RTK_uppl_mapped_memory
00232606  _SH_DATA_SEGS
0023261a  ___bzero
00232623  ___stack_chk_fail
00232635  ___stack_chk_guard
00232648  ___stack_chk_guard_setup
00232661  __arm_arch_hibernate_uat
0023267a  __arm_arch_resume_uat
00232690  __arm_cache_info
002326a1  __fp_context
002326ae  __hb_context
002326bb  __mbi_routes
002326c8  __mmu_config
002326d5  __nmi_frame
002326e1  __platform_bzero
002326f2  __platform_memcmp
00232704  __platform_memmove
00232717  __platform_memset
00232729  __rtk_arch_dead_loop
0023273e  __rtk_arch_exception
00232753  __rtk_arch_fast_interrupt
0023276d  __rtk_arch_gxf_vector_abort
00232789  __rtk_arch_gxf_vectors
002327a0  __rtk_arch_interrupt
002327b5  __rtk_arch_interrupted_pc
002327cf  __rtk_arch_svc_handler
002327e6  __rtk_arch_vectors
002327f9  __rtk_arch_wait_for_interrupt
00232817  __rtk_arch_wait_for_interrupt_retention
0023283f  __rtk_arm_mmu_bits_per_level
0023285c  __rtk_arm_mmu_page_shift
00232875  __rtk_arm_mmu_page_size
0023288d  __rtk_arm_start_bootstrap_area
002328ac  __rtk_armv8_bootstrap_page
002328c7  __rtk_armv8_l1_bootstrap
002328e0  __rtk_astris_island
002328f4  __rtk_cache_clean
00232906  __rtk_cache_clean_invalidate
00232923  __rtk_cache_info_init
00232939  __rtk_crashlog_is_local
00232951  __rtk_crashlog_local_buffer
0023296d  __rtk_crashlog_requested_size
0023298b  __rtk_crt_exc_stack
0023299f  __rtk_crt_exc_stack_base
002329b8  __rtk_crt_exc_stack_len
002329d0  __rtk_crt_exc_stack_top
002329e8  __rtk_crt_expect_boot_args
00232a03  __rtk_crt_init_stack
00232a18  __rtk_crt_init_stack_base
00232a32  __rtk_crt_init_stack_len
00232a4b  __rtk_crt_init_stack_top
00232a64  __rtk_crt_irq_stack
00232a78  __rtk_crt_irq_stack_base
00232a91  __rtk_crt_irq_stack_len
00232aa9  __rtk_crt_irq_stack_top
00232ac1  __rtk_crt_mmu_addr_space_size_log2
00232ae4  __rtk_crt_mmu_gxf_stack
00232afc  __rtk_crt_mmu_gxf_stack_size
00232b19  __rtk_crt_mmu_gxf_user_va_bits
00232b38  __rtk_crt_mmu_gxf_version
00232b52  __rtk_crt_mmu_tables
00232b67  __rtk_crt_mmu_ttbr1_private_space_size
00232b8e  __rtk_crt_mmu_ttbr_select_bitmap
00232baf  __rtk_crt_mmu_uat
00232bc1  __rtk_current_threads
00232bd7  __rtk_dcache_clean_invalidate_whole
00232bfb  __rtk_dcache_clean_whole
00232c14  __rtk_dev_bad_method
00232c29  __rtk_gxf_entry
00232c39  __rtk_gxf_initialized
00232c4f  __rtk_ior
00232c59  __rtk_mbi_max_route
00232c6d  __rtk_mbi_routes_array
00232c84  __rtk_mmu_gxf_config
00232c99  __rtk_mmu_gxf_config_swift
00232cb4  __rtk_mmu_map
00232cc2  __rtk_mmu_region_disable
00232cdb  __rtk_mmu_switch_region_base
00232cf8  __rtk_mmu_tlb_invalidate_all
00232d15  __rtk_mmu_unmap
00232d25  __rtk_mmu_update_mapping
00232d3e  __rtk_mmu_virt_to_phys
00232d55  __rtk_pac_safe_interrupts_disable
00232d77  __rtk_pac_safe_interrupts_restore
00232d99  __rtk_patch_RTK_cpu_physical_address
00232dbe  __rtk_patch_RTK_cpu_wrapper_physical_address
00232deb  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
00232e1c  __rtk_patch_RTK_io_base
00232e34  __rtk_patch_RTK_io_size
00232e4c  __rtk_patch_RTK_lock_legacy
00232e68  __rtk_patch_RTK_mc_remote_alignment
00232e8c  __rtk_patch_RTK_pe_i_can_has_debugger
00232eb2  __rtk_patch_RTK_platform_flags
00232ed1  __rtk_patch_RTK_soc
00232ee5  __rtk_patch_RTK_soc_revision
00232f02  __rtk_patch__aslr_slide
00232f1a  __rtk_patch__aslr_slide_src
00232f36  __rtk_patch__breakeven_pv
00232f50  __rtk_patch__chain_starts
00232f6a  __rtk_patch__dseg_copy_length
00232f88  __rtk_patch__dseg_relocate
00232fa3  __rtk_patch__dseg_virt_source
00232fc1  __rtk_patch__mkey_cfg_address
00232fdf  __rtk_patch__pac_entropy
00232ff8  __rtk_patch__page_table_base
00233015  __rtk_patch__page_table_size
00233032  __rtk_patch__rtk_dev_timebase_offset
00233057  __rtk_patch__rtk_runtime_size
00233075  __rtk_patch__rtk_stack_guard
00233092  __rtk_patch__zerofill_length
002330af  __rtk_patch__zerofill_start
002330cb  __rtk_patch_armv8_ignorenthint
002330ea  __rtk_patch_armv8_single_issue_neon
0023310e  __rtk_patch_armv8_timer_frequency
00233130  __rtk_patch_gxf_private_phy_space_base
00233157  __rtk_patch_gxf_private_phy_space_size
0023317e  __rtk_patch_mmu_ttbr1_private_space_size
002331a7  __rtk_patch_page_table_virt_base
002331c8  __rtk_patch_tunables_size
002331e2  __rtk_patch_tunables_start
002331fd  __rtk_patch_uat_gptbat_base
00233219  __rtk_patch_uat_gptbat_size
00233235  __rtk_patch_uat_ppl_shared_base
00233255  __rtk_patch_uat_ppl_shared_l2_phys
00233278  __rtk_platform_asc_retained_tunables_block
002332a3  __rtk_platform_asc_tunables_block
002332c5  __rtk_power
002332d1  __rtk_sign_initial_thread_state
002332f1  __rtk_stack_watermark
00233307  __rtk_thread_entry
0023331a  __rtk_thread_list
0023332c  __rtk_thread_list_size
00233343  __rtk_unexpected_reset
0023335a  __rtk_uppl_client_dispatch
00233375  __rtk_version_string
0023338a  _arm_do_whole_dcache
0023339f  _arm_fp_context
002333af  _arm_fp_context_addr
002333c4  _arm_hb_context
002333d4  _arm_hb_context_addr
002333e9  _arm_hb_sleep_count
002333fd  _arm_hb_wake_count
00233410  _arm_resume_flag
00233421  _armv8_timebase
00233437  _bzero
0023343e  _gCrashLog
00233449  _gMemoryAllocator
0023345b  _gxf_code_pad_sym
0023346d  _memcmp
00233475  _memcpy
0023347d  _memmove
00233486  _memset
0023348e  _mmu_get_page_table
002334a2  _mmu_get_tt_info
002334b8  _vm_regions
002334c4  dcache_op_poc
002334d2  new_rtk_start_anywhere_uatv2
00233518  __TEXT
00233558  __text
00233568  __TEXT
002335a8  __gxf_code
002335b8  __TEXT
002335f8  __gxf_code_pad
00233608  __TEXT
00233648  __gxf_shr_code
00233658  __TEXT
00233698  __const
002336a8  __TEXT
002336e8  _rtk_patchbay
002336f8  __TEXT
00233738  _rtk_tunables
00233748  __TEXT
00233788  __cstring
00233798  __TEXT
002337d8  __init_offsets
002337e8  __TEXT
00233828  __chain_starts
00233838  __TEXT
00233880  __DATA
002338c0  __gxf_data
002338d0  __DATA
00233910  __data
00233920  __DATA
00233960  _rtk_init_stack
00233970  __DATA
002339b0  __const
002339c0  __DATA
00233a00  _rtk_irq_stack
00233a10  __DATA
00233a50  _rtk_exc_stack
00233a60  __DATA
00233aa0  _rtk_boot_l1
00233ab0  __DATA
00233af0  _rtk_boot
00233b00  __DATA
00233b40  _rtk_mtab
00233b50  __DATA
00233b90  _rtk_power
00233ba0  __DATA
00233be0  _rtk_page_tables__DATA
00233c30  __mod_init_func
00233c40  __DATA
00233c80  _rtk_data_uuid
00233c90  __DATA
00233cd0  _rtk_heap
00233ce0  __DATA
00233d20  _rtk_threads
00233d30  __DATA
00233d70  __constructor
00233d80  __DATA
00233dc0  __zerofill
00233dd0  __DATA
00233e18  __DATA_SHARED_RO
00233e58  _RTK_EXT_SHD_DTA__DATA_SHARED_RO
00233eb0  __DATA_CONST
00237f51  wwwwwww
00248edf  NBX nB
0024aa18  vzA9yZA9u
0024ab26  @9jyhxI
0024ad26  @9Liz8J
0024b4aa  @9jyhxI
0024d4db  K.z(xnYl
00250619  2C)B1Kzd0Iz
00251e04  iYix)%
00259641  ylx/u@9o
002596dd  ylx/u@9o
002597a5  ykx?u@9k
002597e5  ykx-u@9m
0025c874  ji-xji,x
00280470  8bunz8
00280b40  Assertion failure: tid overflow
00281744  INVALID
00281753  Marin-ASC1
00281762  Tempest-ASC2
00281771  Tempest-ASC3
00281780  Tempest-ASC4
0028178f  Tempest-ASC4.1
0028179e  Tempest-ASC5
002817ad  Tempest-ASC6
002817bc  Tempest-ASC7
00281816  Chinook-ASC2
00281825  Chinook2-ASC3
00281834  Chinook-ASC4
00281843  Chinook-ASC4.1
00281852  Chinook-ASC5
00281861  Chinook-ASC6
00281870  Chinook-ASC7
0028187f  ACC E Core
0028188e  ACC P Core
0028189d  ASC Chinook
002818ac  ASC Tempest
002818bb  Scheduler ASC
002818d2  Power Management ASC
00281ae8  RTKSTACK
00281b34  RTKit_armv8_lightning_Oz_flto_pac-3514.40.18.release
00282583  stk_fail
0028258c  AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
002825ed  %s: !!! Fatal Error: AGFHALTestForCompressionErrors found AGX_CR_DCMP_ERROR != 0!: dcmp_error(%d) dm(%d) kickSlot(%d)
00282682  agf_timer_usc_inst_cf is set to %d, FW will do periodic USC instructions cache flush for testing
002826e3  Invalid DM type %d for command type %d in %s
00282735  Warning: Received AFR perf state override when AGF_FEATURE_SUPPORT_AGXAFRCLKGEN and AGF_FEATURE_SUPPORT_AFR_PSTATE_GLB_CTRL are not enabled in firmware
002827cd  %s: !!! Fatal Error: SFE_Tier3 detected!!
00282817  %s: !!! Fatal Error: Thor Hammer Mode detected!! clique_wait_timedout: %u, thm_tier3_active: %u, dpb_watchdog_active: %u, ul1c_watchdog_active: %u, ria_watchdog_active: %u, srs_watchdog_active: %u, ttm_watchdog_active: %u
002828f5  unexpected command type (%d) indicated by SKU in %s
0028294f  CDM context store took too long (latency = %u us, threshold = %u us, req time %llu, complete time %llu)
002829b7  %s: !!! Fatal Error: Lockup Detection: legacy mode not supported when Lockup Hints interrupts are enabled: try using the agf_lockup_hint_irqs=0 boot-arg
00282a6d  WARNING: Waiting for space to add statistics! Consider resizing buffer or adjust interrupt heuristics
00282ad3  Invalid Index in Scheduler State! (queue_table_index %d) (pid_table_index %d)
00282b21  In order eviction check is unsupported when multiple normal completion queues are enabled.
00282b7c  Dumping parents of KSM kick queue entry (Queue=%u, TS=0x%010llx). Valid parent mask=0x%llx
00282bd7  -> Parent index [%2u] : queue=%03u, ts=0x%010llx. Last completed TS=0x%010llx (valid=%d)
00282c30  %s: !!! Fatal Error: All parents of KSM kick queue entry (Queue=%u, TS=0x%010llx) not received. Valid parent mask=0x%llx
00282cd1  NOP command KSM kick queue %u : Last completed TS=0x%llx. Current TS=0x%llx. Stamp index=%u, Stamp=0x%x
00282d39  Received command type (%u) in KSM completion queue entry. payload0 = 0x%llx. payload1 = 0x%llx
00282d98  KSM kick queue %u / dm %u / state %u: Out of order completion within a queue. Last completed TS=0x%llx. Current TS=0x%llx. Delta=%#llx
00282e1f  !!! Error: Unexpected scheduling pause timeout after %uus
00282e59  %s: !!! Fatal Error: Recovery: Dependent skip kick call must be for 3D. Queue=%u KickEntry=%p
00282ed1  %s: !!! Fatal Error: kAGFIChannelCommandTypePMRebuild must not be received in SKSM
00282f3e  %s: !!! Fatal Error: Unhandled : Invalid command type %d
00282f77  Unimplemented. AGFAGXInterruptPMThresholdHandler
00282fa8  Context Restore Timed Out! QueueId %u
00283002  %s: !!! Fatal Error: Resume called for reason %d with auto resume enabled
0028304c  AGFHRBResume
00283059  Context Store Timed Out! DM %u, QueueId %u
00283084  %s: !!! Fatal Error: Unknown state = %d
002830c2  %s: !!! Fatal Error: %s : queue %#llx-%#llx must not be disabled %#llx-%#llx
0028312b  %s: !!! Fatal Error: Unrecognized gtp discard mode
0028315e  AGFPMOOMHandler
0028316e  %s: !!! Fatal Error: Deferred TSQ buffer has no free space!
002831ce  gfx_iop_msgs
002831db  gfx_iop_ints
002831e8  Slow IOP message: 0x%x 0x%x 0x%llx elapsed=%llu
00283218  Failed to allocate new ring entry
0028323a  management
00283245  crashlog
0028324e  gfx_msgs
00283257  gfx_ints
00283260  Unsupported shared event agent index: %u
00283289  %s: !!! Fatal Error: Failed to find doorbell link for IOP %d!
002832c7  agfInitDoorbells
002832d8  gfx_msr
002832e0  AGFSignalPagePoolStarved(TopSlotsStarvedMask=%#llx)
00283314  AGFSignalPagePoolStarved(found ppid=%i)
0028333c  Error: PPID Starved: %i
00283354  Error: Topslots starved=%#llx
00283372  %s: !!! Fatal Error: Error: Got a starvation interrupt with no irritator enabled
002833dc  Starved: CS on SMA Oom for queues = %#llx-%#llx
0028340c  UMA FW id state has bad context ID. context_id: %d
0028343f  G18 Firmware initializing
00283459    FW Build variant: g19a
00283472    FW Build version: a0
00283489    FW Build running in SKSM Enabled mode
002834d5     USC Pipe %u State Overview
002834f3  AGX_CR_USC_VDM_SERV: 0x%llx
0028350f  AGX_CR_USC_PDM_SERV: 0x%llx
0028352b  AGX_CR_USC_CDM_SERV: 0x%llx
00283547  AGX_CR_USC_VDM_DEBUG_STATUS: 0x%llx
0028356b  AGX_CR_USC_PDM_DEBUG_STATUS: 0x%llx
0028358f  AGX_CR_USC_CDM_DEBUG_STATUS: 0x%llx
002835b3  Buffer size is too small to hold all counter values
002835e7  %s: !!! Fatal Error: unexpected indexing type (%d) for register range 0x%x
0028364e  Unexpected page fault requestor (%u)
00283673  ERROR: AGFHALParameterBufferSaveFreeList flush failed for %u - setting rebuild
002836d9  CPMS tracing will not be supported on G18
00283703  PBState must be unbind, before being rebound to different PB state
00283778  PIO poll%s%s finally succeeded after %uus [type:%d reg:0x%x value:0x%x max:%uus]
002837c9  Unable to grab init data from host
002837ec  Host and FW Interface is mismatched, please ensure the versions are aligned.
00283839  Host-mapped FW allocations are disabled, but FW only supports enabled (init_data_addr=0x%llx)!
00283898  _agfGL2DependentPollReg32
002838b2  %s: !!! Fatal Error: %s : Poll timeed out. Caller timeout value = %u uSec. Timeout floor set to %u uSec
0028391a  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus]
0028396d  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%x got:0x%x max:%uus], continue wait
002839d6  %s: !!! Fatal Error: RSA ID not assigned for thread ID %u
00283a2c  %s: !!! Fatal Error: Invalid DataMaster %u
00283a70  PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]
00283ac7   from 
00283ace  ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait
002842cb  %s: !!! Fatal Error: No matching thread found for thread ID 0x%lx
00284326  cold booted
00284332  Unknown ASC version
00284346  GFX %s %u %s FW %s! (%s)
0028435f  Oct 13 2026 23:40:12
00284374  GPU is not powered on after power kick!
0028439c  Failed to register cputrace handler
002843c0  agx_scheduler
002843ce  agx_recovery
002843db  agx_sampler
002843e7  agx_pwr_metrics_server
002843fe  GPU is Powered On while we are about to Power down Fender
00284438  Transitioning from RTK_POWER_SLEEP to RTK_POWER_NAP directly
00284475  Transitioning from RTK_POWER_NAP to RTK_POWER_SLEEP directly
002844b2  %s: !!! Fatal Error: Error %x
002844d0  AGFASemaphoreSignal
002844e4  %s: !!! Fatal Error: Attempt to signal a remote semaphore from an interrupt context. %d
00284556  Msg of type %u received, which can't be handled!
00284587  %s: !!! Fatal Error: Unknown IOP msg type %d!
002845ca  %s: !!! Fatal Error: Unexpected recovery type %llu!
0028461b  %s: !!! Fatal Error: Unknown message received (event = %llu)
00284676  %s: !!! Fatal Error: Invalid Power Server Kick %llu
002846c5  %s: !!! Fatal Error: Unrecognized remote power kick value 0x%llx
00284706  agfaRemotePowerKick
0028471a  !MIDR: 0x%x
00284726  ~CsPTR
0028472d  !ROf %#lx %#x
0028473b  MMU private: s:%llx!=%llx b:%llx!=%llx
00284762  MMU VA sz %u 0=%zu 1=%zu
0028477b  MMU private !fit: b:%lx<%lx s:%lx>%lx
002847a1  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
002847ce  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
00284800  MMU sh<ps: %llu > %llu
00284817  Page Table !vm export: %x
00284831  GPTBAT !vm export: %x
00284847  PPL handoff !vm export: %x
00284862  !Mthd:%p
0028486b  !msgmbxint
00284876  !msgdoordashint
00284886  mme:0x%x
00284893  Duty cycle
002848a4  Sleep count
002848b0  Wake count
002848bb  Power state
002848c7  Free heap
002848d1  Total heap
002848dc  Peak heap alloc
002848ec  Used stack
002848f7  Total stack
00284903  CPU count
00284914  <null>
0028491e  ThIntr:%u,%u,%u,%u
00284931  ThLock:%p
0028493b  MBI queue overflow:%s
00284951  VmOv %d %d
0028495c  rtk_ep_work
00284968  MGMT msg=0x%llx st=%x
0028497e  MGMT st=%x
0028498d  !clg: %08x
00284998  !cpy: %08x
002849a3  Not implemented
002849b3  Message Log
002849c0  Invalid AP power: %d
002849dc  RTKit: %s - Client: %s
002849f3  !Heapblk:%p
002849ff  REDACTED
002ab4c8  lCytuDTR
002ab520  tnCplSTR
002ab578  tnCkaWTR
002ab5d0  tffOnOTR
002ab628  EERFPHTR
002ab681  LLAPHTR
002ab6d8  KAEPPHTR
002ab732  UKTSTR
002ab78a  AKTSTR
002ab7e0  UPCmuNTR
002ab980  not set
002abf90  RTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACK
0034bf84  _RTK_abort
0034bf8f  _RTK_client_version_string
0034bfaa  _RTK_dev_asc
0034bfb7  _RTK_dev_asc_config
0034bfcb  _RTK_dev_cputrace_metadata
0034bfe6  _RTK_dev_pts_ptd
0034bff7  _RTK_dev_pts_ptd_peek
0034c00d  _RTK_dev_timesync_0
0034c021  _RTK_dev_wrapper_icu
0034c036  _RTK_uppl_mapped_memory
0034c04e  _SH_DATA_SEGS
0034c062  ___bzero
0034c06b  ___stack_chk_fail
0034c07d  ___stack_chk_guard
0034c090  ___stack_chk_guard_setup
0034c0a9  __arm_arch_hibernate_uat
0034c0c2  __arm_arch_resume_uat
0034c0d8  __arm_cache_info
0034c0e9  __fp_context
0034c0f6  __hb_context
0034c103  __mbi_routes
0034c110  __mmu_config
0034c11d  __nmi_frame
0034c129  __platform_bzero
0034c13a  __platform_memcmp
0034c14c  __platform_memmove
0034c15f  __platform_memset
0034c171  __rtk_arch_dead_loop
0034c186  __rtk_arch_exception
0034c19b  __rtk_arch_fast_interrupt
0034c1b5  __rtk_arch_gxf_vector_abort
0034c1d1  __rtk_arch_gxf_vectors
0034c1e8  __rtk_arch_interrupt
0034c1fd  __rtk_arch_interrupted_pc
0034c217  __rtk_arch_svc_handler
0034c22e  __rtk_arch_vectors
0034c241  __rtk_arch_wait_for_interrupt
0034c25f  __rtk_arch_wait_for_interrupt_retention
0034c287  __rtk_arm_mmu_bits_per_level
0034c2a4  __rtk_arm_mmu_page_shift
0034c2bd  __rtk_arm_mmu_page_size
0034c2d5  __rtk_arm_start_bootstrap_area
0034c2f4  __rtk_armv8_bootstrap_page
0034c30f  __rtk_armv8_l1_bootstrap
0034c328  __rtk_astris_island
0034c33c  __rtk_cache_clean
0034c34e  __rtk_cache_clean_invalidate
0034c36b  __rtk_cache_info_init
0034c381  __rtk_crashlog_is_local
0034c399  __rtk_crashlog_local_buffer
0034c3b5  __rtk_crashlog_requested_size
0034c3d3  __rtk_crt_exc_stack
0034c3e7  __rtk_crt_exc_stack_base
0034c400  __rtk_crt_exc_stack_len
0034c418  __rtk_crt_exc_stack_top
0034c430  __rtk_crt_expect_boot_args
0034c44b  __rtk_crt_init_stack
0034c460  __rtk_crt_init_stack_base
0034c47a  __rtk_crt_init_stack_len
0034c493  __rtk_crt_init_stack_top
0034c4ac  __rtk_crt_irq_stack
0034c4c0  __rtk_crt_irq_stack_base
0034c4d9  __rtk_crt_irq_stack_len
0034c4f1  __rtk_crt_irq_stack_top
0034c509  __rtk_crt_mmu_addr_space_size_log2
0034c52c  __rtk_crt_mmu_gxf_stack
0034c544  __rtk_crt_mmu_gxf_stack_size
0034c561  __rtk_crt_mmu_gxf_user_va_bits
0034c580  __rtk_crt_mmu_gxf_version
0034c59a  __rtk_crt_mmu_tables
0034c5af  __rtk_crt_mmu_ttbr1_private_space_size
0034c5d6  __rtk_crt_mmu_ttbr_select_bitmap
0034c5f7  __rtk_crt_mmu_uat
0034c609  __rtk_current_threads
0034c61f  __rtk_dcache_clean_invalidate_whole
0034c643  __rtk_dcache_clean_whole
0034c65c  __rtk_dev_bad_method
0034c671  __rtk_gxf_entry
0034c681  __rtk_gxf_initialized
0034c697  __rtk_ior
0034c6a1  __rtk_mbi_max_route
0034c6b5  __rtk_mbi_routes_array
0034c6cc  __rtk_mmu_gxf_config
0034c6e1  __rtk_mmu_gxf_config_swift
0034c6fc  __rtk_mmu_map
0034c70a  __rtk_mmu_region_disable
0034c723  __rtk_mmu_switch_region_base
0034c740  __rtk_mmu_tlb_invalidate_all
0034c75d  __rtk_mmu_unmap
0034c76d  __rtk_mmu_update_mapping
0034c786  __rtk_mmu_virt_to_phys
0034c79d  __rtk_pac_safe_interrupts_disable
0034c7bf  __rtk_pac_safe_interrupts_restore
0034c7e1  __rtk_patch_RTK_cpu_physical_address
0034c806  __rtk_patch_RTK_cpu_wrapper_physical_address
0034c833  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
0034c864  __rtk_patch_RTK_io_base
0034c87c  __rtk_patch_RTK_io_size
0034c894  __rtk_patch_RTK_lock_legacy
0034c8b0  __rtk_patch_RTK_mc_remote_alignment
0034c8d4  __rtk_patch_RTK_pe_i_can_has_debugger
0034c8fa  __rtk_patch_RTK_platform_flags
0034c919  __rtk_patch_RTK_soc
0034c92d  __rtk_patch_RTK_soc_revision
0034c94a  __rtk_patch__aslr_slide
0034c962  __rtk_patch__aslr_slide_src
0034c97e  __rtk_patch__breakeven_pv
0034c998  __rtk_patch__chain_starts
0034c9b2  __rtk_patch__dseg_copy_length
0034c9d0  __rtk_patch__dseg_relocate
0034c9eb  __rtk_patch__dseg_virt_source
0034ca09  __rtk_patch__mkey_cfg_address
0034ca27  __rtk_patch__pac_entropy
0034ca40  __rtk_patch__page_table_base
0034ca5d  __rtk_patch__page_table_size
0034ca7a  __rtk_patch__rtk_dev_timebase_offset
0034ca9f  __rtk_patch__rtk_runtime_size
0034cabd  __rtk_patch__rtk_stack_guard
0034cada  __rtk_patch__zerofill_length
0034caf7  __rtk_patch__zerofill_start
0034cb13  __rtk_patch_armv8_ignorenthint
0034cb32  __rtk_patch_armv8_single_issue_neon
0034cb56  __rtk_patch_armv8_timer_frequency
0034cb78  __rtk_patch_gxf_private_phy_space_base
0034cb9f  __rtk_patch_gxf_private_phy_space_size
0034cbc6  __rtk_patch_mmu_ttbr1_private_space_size
0034cbef  __rtk_patch_page_table_virt_base
0034cc10  __rtk_patch_tunables_size
0034cc2a  __rtk_patch_tunables_start
0034cc45  __rtk_patch_uat_gptbat_base
0034cc61  __rtk_patch_uat_gptbat_size
0034cc7d  __rtk_patch_uat_ppl_shared_base
0034cc9d  __rtk_patch_uat_ppl_shared_l2_phys
0034ccc0  __rtk_platform_asc_retained_tunables_block
0034cceb  __rtk_platform_asc_tunables_block
0034cd0d  __rtk_power
0034cd19  __rtk_sign_initial_thread_state
0034cd39  __rtk_stack_watermark
0034cd4f  __rtk_thread_entry
0034cd62  __rtk_thread_list
0034cd74  __rtk_thread_list_size
0034cd8b  __rtk_unexpected_reset
0034cda2  __rtk_uppl_client_dispatch
0034cdbd  __rtk_version_string
0034cdd2  _arm_do_whole_dcache
0034cde7  _arm_fp_context
0034cdf7  _arm_fp_context_addr
0034ce0c  _arm_hb_context
0034ce1c  _arm_hb_context_addr
0034ce31  _arm_hb_sleep_count
0034ce45  _arm_hb_wake_count
0034ce58  _arm_resume_flag
0034ce69  _armv8_timebase
0034ce7f  _bzero
0034ce86  _gCrashLog
0034ce91  _gMemoryAllocator
0034cea3  _gxf_code_pad_sym
0034ceb5  _memcmp
0034cebd  _memcpy
0034cec5  _memmove
0034cece  _memset
0034ced6  _mmu_get_page_table
0034ceea  _mmu_get_tt_info
0034cf00  _vm_regions
0034cf0c  dcache_op_poc
0034cf1a  new_rtk_start_anywhere_uatv2
```
