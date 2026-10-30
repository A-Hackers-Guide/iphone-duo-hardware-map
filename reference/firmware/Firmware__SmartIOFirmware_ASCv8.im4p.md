# `Firmware/SmartIOFirmware_ASCv8.im4p`

- File size: 1,149,397 bytes
- IM4P: Tag: IM4P  Type: siof  Version: 1.0.0
- BuildManifest components that use it: `SIO`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         siof
  Version:      1.0.0
  Data:         1.1 MB (1149368 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 1,149,368 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- `RTKit: %s - Client: %s`
- `RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release`

## Strings (462) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000028  __TEXT
00000068  __text
00000078  __TEXT
000000b8  __cstring
000000c8  __TEXT
00000108  __const
00000118  __TEXT
00000158  __constructor
00000168  __TEXT
000001a8  __init_offsets
000001b8  __TEXT
000001f8  __chain_starts
00000208  __TEXT
00000250  __DATA
00000290  __const
000002a0  __DATA
000002e0  __data
000002f0  __DATA
00000330  __mod_init_func
00000340  __DATA
00000380  _rtk_init_stack
00000390  __DATA
000003d0  _rtk_irq_stack
000003e0  __DATA
00000420  _rtk_exc_stack
00000430  __DATA
00000470  _rtk_boot
00000480  __DATA
000004c0  _rtk_page_tables__DATA
00000510  _rtk_patchbay
00000520  __DATA
00000560  _rtk_mtab
00000570  __DATA
000005b0  _rtk_power
000005c0  __DATA
00000600  __gxf_data
00000610  __DATA
00000650  _rtk_tunables
00000660  __DATA
000006a0  _rtk_data_uuid
000006b0  __DATA
000006f0  _rtk_heap
00000700  __DATA
00000740  _rtk_threads
00000750  __DATA
00000790  __zerofill
000007a0  __DATA
000007e8  __DATA_CONST
000019d1  wwwwwww
0001d728  Fifo size request not valid
0001d744  Fifo allocation overflow %d:%d
0001d763  Attempt to reconfigure Shim %s(%d) fifo size
0001d790  Configuring Shim %s(%d) without a fifo
0001d7b7  Configuring Shim %s(%d) with trigger > fifo
0001d7e3  Configuring Shim %s(%d) with limit > fifo
0001d80d  Shim %s(%d) Timeout!
0001d823  Shim %s(%d) Unavailable
0001d845  Enabled
0001d84d  Disabled
0001d856  Current Page:
0001d868  Style: %d
0001d874  Data VA: 0x%08llx
0001d888  Data PA: 0x%016llx
0001d89d  Length: 0x%08x
0001d8ae  CompTime: 0x%016llx
0001d8c4  Owner: 0x%08llx
0001d8d6  Offset: 0x%08x
0001d8ee  Unknown device type: %d
0001d90c  Control
0001d914  Unknown
0001d921  AOP_MCA0_TX
0001d92d  AOP_MCA0_RX
0001d939  AOP_MCA1_TX
0001d945  AOP_MCA1_RX
0001d951  AOP_MCA2_TX
0001d95d  AOP_MCA2_RX
0001d969  AOP_MCA3_TX
0001d975  AOP_MCA3_RX
0001d981  SPI0_TX
0001d989  SPI0_RX
0001d991  SPI1_TX
0001d999  SPI1_RX
0001d9a1  SPI2_TX
0001d9a9  SPI2_RX
0001d9b1  SPI3_TX
0001d9b9  SPI3_RX
0001d9c1  SPI4_TX
0001d9c9  SPI4_RX
0001d9d1  SPI5_TX
0001d9d9  SPI5_RX
0001d9e1  MCA0_TX
0001d9e9  MCA0_RX
0001d9f1  MCA1_TX
0001d9f9  MCA1_RX
0001da01  MCA2_TX
0001da09  MCA2_RX
0001da11  MCA3_TX
0001da19  MCA3_RX
0001da21  MCA4_TX
0001da29  MCA4_RX
0001da31  MCA5_TX
0001da39  MCA5_RX
0001da41  MCA6_TX
0001da49  MCA6_RX
0001da51  MCA7_TX
0001da59  MCA7_RX
0001da61  MCA8_TX
0001da69  MCA8_RX
0001da71  MCA9_TX
0001da79  MCA9_RX
0001da81  UART0_TX
0001da8a  UART0_RX
0001da93  UART1_TX
0001da9c  UART1_RX
0001daa5  UART2_TX
0001daae  UART2_RX
0001dab7  UART3_TX
0001dac0  UART3_RX
0001dac9  UART4_TX
0001dad2  UART4_RX
0001dadb  UART5_TX
0001dae4  UART5_RX
0001daed  UART6_TX
0001daf6  UART6_RX
0001daff  UART7_TX
0001db08  UART7_RX
0001db11  UART8_TX
0001db1a  UART8_RX
0001db23  PDM0_RX
0001db2b  DPA0_TX
0001db33  DPA1_TX
0001db3b  DPA2_TX
0001db43  DPA3_TX
0001db4b  DPA4_TX
0001db53  MCA10_TX
0001db5c  MCA10_RX
0001db65  MCA11_TX
0001db6e  MCA11_RX
0001db77  AOP_LEAP0_TX
0001db84  AOP_LEAP0_RX
0001db91  AOP_LEAP1_TX
0001db9e  AOP_LEAP1_RX
0001dbab  AOP_LEAP2_TX
0001dbb8  AOP_LEAP2_RX
0001dbc5  AOP_LEAP3_TX
0001dbd2  AOP_LEAP3_RX
0001dbdf  AOP_LEAP4_TX
0001dbec  AOP_LEAP4_RX
0001dbf9  AOP_LEAP5_TX
0001dc06  AOP_LEAP5_RX
0001dc13  AOP_LEAP6_TX
0001dc20  AOP_LEAP6_RX
0001dc2d  AOP_LEAP7_TX
0001dc3a  AOP_LEAP7_RX
0001dc47  AOP_LEAP8_TX
0001dc54  AOP_LEAP8_RX
0001dc61  AOP_LEAP9_TX
0001dc6e  AOP_LEAP9_RX
0001dc7b  AOP_LEAP10_TX
0001dc89  AOP_LEAP10_RX
0001dc97  AOP_LEAP11_TX
0001dca5  AOP_LEAP11_RX
0001dcb3  AOP_LEAP12_TX
0001dcc1  AOP_LEAP12_RX
0001dccf  AOP_PDM0_RX
0001dcdb  Attempt to retrieve DMA buffer outside of segment list.
0001dd13  Endpoint Tag %d Overflows Response Buffer.
0001dd3e  Endpoint Index %d Overflows Response Buffer.
0001dd6b  Endpoint: %s Query - Page Offset should be zero but is %#.8x!
0001dda9  Endpoint: %s Stop - Page Offset should be zero but is %#.8x!
0001dde7  SegmentLoc: 0x%08llx
0001ddfe  Completed: 0x%08x
0001de12  Tag: %d
0001de1b  kStateUninitialized
0001de2f  kStateException
0001de3f  kStateInactive
0001de4e  kStateActive
0001de5b  kStatePaused
0001de68  Endpoint State %s
0001de7b  Pending Buffers: %d
0001de90  Segmenting Buffer
0001deaa  Segmenting Buffers: %d
0001dec2  Retiring Buffer
0001ded3  Completed Buffers: %d
0001deea  Completed Pages: %d
0001deff  bad shim device type %d
0001df17  Endpoint %s: attempted to send unsupported reply %d
0001df4b  Endpoint %s: attempt to send unsupported error %d
0001df7d  EP Message Log
0001dfa9  ---Active Endpoints---
0001dfc9  ---Inactive Endpoints---
0001dfe3  ---Unused Endpoints---
0001dffb  Out Of Range
0001e008  unknown map range %d
0001e01e  Attempt to configure shim %s but not mapped
0001e04b  non-external shim type %d
0001e066  Shim DMA unavailable error:
0001e082   MASK tx: 
0001e08d   (0x%08llx)
0001e099   MASK rx: 
0001e0a4   RAW tx: 
0001e0ae   RAW rx: 
0001e0b8   MASKED tx: 
0001e0c5   MASKED rx: 
0001e0e8  ShimType %lu is not valid
0001e103  Accessing the FIFO of %s Shim which is powered off: DMASHIM_SRAM_STATUS 0x%x
0001e151  Shim machine check: AXI_Error_Status 0x%08x  AWADDR 0x%08x AWID 0x%08x ARADDR 0x%08x ARID 0x%08x
0001e1b2  Device %d not mapped, pbase=%p
0001e1d2  PMGR_AON not mapped; skipping PS reg dump
0001e1fd  PS reg buffer not mapped; skipping PS reg dump
0001e22d  PMGR_AON[0x%x] = 0x%x
0001e244  Shim states:
0001e264  ---Unused Shims---
0001e28c  AOP-GP
0001e293  AOP-AUDIO
0001e2a9  AOP-LEAP
0001e2b2  AOP-MCA
0001e2ba  AOP-PDM
0001e2c2  Size of PIO map ranges is too small! requires at least %lu, have %lu
0001e308  Zero SIO registers passed for setup
0001e32d  Invalid SIO register buffer size: %lu
0001e354  Too many devices requested for type %d: %d
0001e380  Invalid tunable buffer size: %lu
0001e3a2  Invalid tunable size: %u
0001e3bc  management
0001e3c7  crashlog
0001e3d0  syslog
0001e3d7  kdebug
0001e3de  ioreporting
0001e3ea  smartio_msg
0001e3f6  SIO register block type %u invalid
0001e41a  SIO register type %u invalid
0001e438  Invalid SIO register offset
0001e455  activity counter %sflow: %x -> %x
0001e483  stk_fail
0001e48c  MBI queue overflow:%s
0001e4a2  CXXPureVirt
0001e4ae  ThIntr:%u,%u,%u,%u
0001e4c1  ThLock:%p
0001e4cb  VmOv %d %d
0001e4d6  CXXnew:%zu
0001e4e1  rtk_ep_work
0001e4ed  MGMT msg=0x%llx st=%x
0001e503  MGMT st=%x
0001e512  !clg: %08x
0001e51d  Not implemented
0001e52d  Message Log
0001e539  !kb reg:%x
0001e545  !Heapblk:%p
0001e551  Unbalanced transients
0001e567  Invalid AP power: %d
0001e583  RTKit: %s - Client: %s
0001e59a  !ASLRHeapAlign
0001e5a9  <null>
0001e5b3  !MIDR: 0x%x
0001e5bf  ~CsPTR
0001e5c6  !ROf %#lx %#x
0001e5d4  MMU out of tables: %zu,%zu
0001e5ef  MMU private: s:%llx!=%llx b:%llx!=%llx
0001e616  MMU VA sz %u 0=%zu 1=%zu
0001e62f  MMU private !fit: b:%lx<%lx s:%lx>%lx
0001e655  GPTBAT !vm export: %x
0001e66b  PPL handoff !vm export: %x
0001e686  MMU invalid page size: %x
0001e6a0  !Mthd:%p
0001e6a9  !msgmbxint
0001e6b4  !msgdoordashint
0001e6c4  mme:0x%x
0001e6d5  Duty cycle
0001e6e6  Sleep count
0001e6f2  Wake count
0001e6fd  Power state
0001e709  Free heap
0001e713  Total heap
0001e71e  Peak heap alloc
0001e72e  Used stack
0001e739  Total stack
0001e745  CPU count
0001e756  Thread time
0001e762  Performance
0001e76e  IRQ disabled time
0001e844  RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release
0001e8a0  RTKSTACKtTxEhTTR
0001e8b8  tTDPhTTR
0001fff8  not set
00020560  tTxEhTTRV
000205b8  tTDPhTTRn
00020610  lCytuDTR
00020668  tnCplSTR
000206c0  tnCkaWTR
00020718  tffOnOTR
00020770  EERFPHTR
000207c9  LLAPHTR
00020820  KAEPPHTR
0002087a  UKTSTR.
000208d2  AKTSTR9
00020928  UPCmuNTRE
00117a64  _RTK_DEV_ASC
00117a71  _RTK_DEV_ASCWRAP
00117a82  _RTK_DEV_TIMEBASE
00117a94  _RTK_DEV_WRAPPER_CONFIG
00117aac  _RTK_abort
00117ab7  _RTK_cache_clean
00117ac8  _RTK_cache_clean_invalidate
00117ae4  _RTK_cache_get_line_size
00117afd  _RTK_client_version_string
00117b18  _RTK_crashlog_get_crashlog_type
00117b38  _RTK_crashlog_register_handler
00117b57  _RTK_dev_asc
00117b64  _RTK_dev_asc_config
00117b78  _RTK_dev_ascwrap_v8_dispatch
00117b95  _RTK_dev_configure_mmio
00117bad  _RTK_dev_cputrace_metadata
00117bc8  _RTK_dev_is_mapped
00117bdb  _RTK_dev_kdebug_mbi_dispatch
00117bf8  _RTK_dev_map_registers
00117c0f  _RTK_dev_messagebox_mailbox_dispatch
00117c34  _RTK_dev_syslog_mbi_dispatch
00117c51  _RTK_dev_timesync_0
00117c65  _RTK_dev_wrapper_icu
00117c7a  _RTK_disable_interrupts
00117c92  _RTK_enable_all_interrupts
00117cad  _RTK_endpoint_init_default_workloop
00117cd1  _RTK_endpoint_workloop
00117ce8  _RTK_interrupt_attach
00117cfe  _RTK_interrupt_enable
00117d14  _RTK_io_reporting_init
00117d2b  _RTK_kdebug_init
00117d3c  _RTK_mbi_endpoint_attach
00117d55  _RTK_mbi_endpoint_receive_msg
00117d73  _RTK_mbi_endpoint_send_msg
00117d8e  _RTK_mbi_log_create
00117da2  _RTK_mbi_route_create_from_physical_layer
00117dcc  _RTK_mgmt_init_with_options
00117de8  _RTK_mgmt_wait_for_route_ready
00117e07  _RTK_mmu_map
00117e14  _RTK_mmu_unmap
00117e23  _RTK_platform_register_reporters
00117e44  _RTK_power_enable
00117e56  _RTK_power_prevent_nap
00117e6d  _RTK_power_register_callback
00117e8a  _RTK_power_set_nap_mode
00117ea2  _RTK_restore_interrupts
00117eba  _RTK_semaphore_init
00117ece  _RTK_semaphore_signal
00117ee4  _RTK_semaphore_wait
00117ef8  _RTK_syslog_init
00117f09  _RTK_thread_create
00117f1c  _RTK_vm_allocate_virtual_space
00117f3b  _RTK_vm_map_memory
00117f4e  _SH_DATA_SEGS
00117f62  __Z17RTK_crashlog_initj
00117f7a  __Znwm
00117f81  ___bzero
00117f8a  ___cxa_pure_virtual
00117f9e  ___stack_chk_fail
00117fb0  ___stack_chk_guard
00117fc3  ___stack_chk_guard_setup
00117fdc  __arm_arch_hibernate
00117ff1  __arm_arch_resume
00118003  __arm_cache_info
00118014  __fp_context
00118021  __hb_context
0011802e  __mbi_routes
0011803b  __mmu_config
00118048  __nmi_frame
00118054  __platform_bzero
00118065  __platform_memmove
00118078  __platform_memset
0011808a  __rtk_arch_dead_loop
0011809f  __rtk_arch_exception
001180b4  __rtk_arch_fast_interrupt
001180ce  __rtk_arch_interrupt
001180e3  __rtk_arch_interrupted_pc
001180fd  __rtk_arch_svc_handler
00118114  __rtk_arch_vectors
00118127  __rtk_arch_wait_for_interrupt
00118145  __rtk_arch_wait_for_interrupt_retention
0011816d  __rtk_arm_start_bootstrap_area
0011818c  __rtk_astris_island
001181a0  __rtk_crt_mmu_addr_space_size_log2
001181c3  __rtk_crt_mmu_ttbr1_private_space_size
001181ea  __rtk_crt_mmu_ttbr_select_bitmap
0011820b  __rtk_current_threads
00118221  __rtk_dev_bad_method
00118236  __rtk_ior
00118240  __rtk_kdebug_record
00118254  __rtk_mbi_max_route
00118268  __rtk_mbi_routes_array
0011827f  __rtk_pac_safe_interrupts_disable
001182a1  __rtk_pac_safe_interrupts_restore
001182c3  __rtk_patch_RTK_cpu_physical_address
001182e8  __rtk_patch_RTK_cpu_wrapper_physical_address
00118315  __rtk_patch_RTK_dev_ascwrap_platform_inits_route
00118346  __rtk_patch_RTK_io_base
0011835e  __rtk_patch_RTK_io_size
00118376  __rtk_patch_RTK_lock_legacy
00118392  __rtk_patch_RTK_mc_remote_alignment
001183b6  __rtk_patch_RTK_pe_i_can_has_debugger
001183dc  __rtk_patch_RTK_platform_flags
001183fb  __rtk_patch_RTK_soc
0011840f  __rtk_patch_RTK_soc_revision
0011842c  __rtk_patch__aslr_slide
00118444  __rtk_patch__aslr_slide_src
00118460  __rtk_patch__breakeven_pv
0011847a  __rtk_patch__chain_starts
00118494  __rtk_patch__dseg_copy_length
001184b2  __rtk_patch__dseg_relocate
001184cd  __rtk_patch__dseg_virt_source
001184eb  __rtk_patch__mkey_cfg_address
00118509  __rtk_patch__pac_entropy
00118522  __rtk_patch__page_table_base
0011853f  __rtk_patch__page_table_size
0011855c  __rtk_patch__rtk_dev_timebase_offset
00118581  __rtk_patch__rtk_runtime_size
0011859f  __rtk_patch__rtk_stack_guard
001185bc  __rtk_patch__zerofill_length
001185d9  __rtk_patch__zerofill_start
001185f5  __rtk_patch_armv8_ignorenthint
00118614  __rtk_patch_armv8_single_issue_neon
00118638  __rtk_patch_armv8_timer_frequency
0011865a  __rtk_patch_mmu_ttbr1_private_space_size
00118683  __rtk_patch_page_table_virt_base
001186a4  __rtk_patch_tunables_size
001186be  __rtk_patch_tunables_start
001186d9  __rtk_patch_uat_gptbat_base
001186f5  __rtk_patch_uat_gptbat_size
00118711  __rtk_patch_uat_ppl_shared_base
00118731  __rtk_patch_uat_ppl_shared_l2_phys
00118754  __rtk_platform_asc_retained_tunables_block
0011877f  __rtk_platform_asc_tunables_block
001187a1  __rtk_power
001187ad  __rtk_scheduler_init
001187c2  __rtk_sign_initial_thread_state
001187e2  __rtk_stack_watermark
001187f8  __rtk_thread_entry
0011880b  __rtk_thread_list
0011881d  __rtk_thread_list_size
00118834  __rtk_unexpected_reset
0011884b  __rtk_uppl_client_dispatch
00118866  __rtk_version_string
0011887b  _arm_do_whole_dcache
00118890  _arm_fp_context
001188a0  _arm_fp_context_addr
001188b5  _arm_hb_context
001188c5  _arm_hb_context_addr
001188da  _arm_hb_sleep_count
001188ee  _arm_hb_wake_count
00118901  _arm_resume_address
00118915  _arm_resume_flag
00118926  _armv8_timebase
00118936  _bzero
0011893d  _gMemoryAllocator
0011894f  _memcpy
00118957  _memmove
00118960  _memset
00118968  _snprintf
00118972  _strlcat
0011897b  _vm_regions
00118987  _vsnprintf
00118992  dcache_op_poc
001189a0  rtk_start_anywhere_4k
```
