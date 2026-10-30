# `Firmware/ave/AppleAVE2FW_H19_AVE0.im4p`

- File size: 10,387 bytes
- IM4P: Tag: IM4P  Type: ave0  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder0`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave0
  Version:      1
  Data:         10 kB (10364 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 10,364 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (113) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000024  __TEXT
00000054  __text
00000064  __TEXT
00000098  __const
000000a8  __TEXT
000000dc  _rtk_vtor
000000ec  __TEXT
00000120  _rtk_patchbay
00000130  __TEXT
00000164  __cstring
00000174  __TEXT
000001a8  _rtk_mtab
000001b8  __TEXT
000001ec  __constructor
000001fc  __TEXT
00000230  __rebase_info
00000240  __TEXT
0000027c  __DATA
000002ac  __shared
000002bc  __DATA
000002f0  __data
00000300  __DATA
00000334  __const
00000344  __DATA
00000378  _rtk_power
00000388  __DATA
000003cc  __DATA
00000400  __mod_init_func
00000410  __DATA
00000444  __zerofill
00000454  __DATA
00000490  __VTOR
000004c0  _rtk_vtor_patch
000004d0  __VTOR
000018c8  RTKit-3491.release
00001b15  stk_fail
00001b1e  !Mthd:%p
00001dd4  not set
00002264  _AVE_ISR_HWResults
00002277  _AVE_ISR_WakeUp
00002287  _AVE_MCPUInit
00002295  _AVE_RV_CtxExecute
000022a8  _AVE_RV_CtxSetup
000022b9  _AVE_RV_Main
000022c6  _ConfInputFwData
000022d7  _RTK_DEV_ICU
000022e4  _RTK_abort
000022ef  _RTK_arch_exception_handler
0000230b  _RTK_arch_fault_handler
00002323  _RTK_arch_idle
00002332  _RTK_arch_reset_handler
0000234a  _RTK_client_version_string
00002365  _RTK_dev_rvic_bare_dispatch_v2_1
00002386  _RTK_disable_all_interrupts
000023a2  _RTK_enable_all_interrupts
000023bd  _RTK_exit
000023c7  _RTK_halt
000023d1  _RTK_interrupt_attach
000023e7  _RTK_interrupt_enable
000023fd  _RTK_interrupt_set_type
00002415  _RTK_platform_init
00002428  _RTK_restore_all_interrupts
00002444  _RTK_riscv32i_start
00002458  _RTK_spinlock_lock
00002471  __MergedGlobals_gv_iCtxStarted
00002490  ___stack_chk_fail
000024a2  ___stack_chk_guard
000024b5  ___stack_chk_guard_setup
000024ce  __hart_context_pointer
000024e5  __rtk_arch_dummy_handler
000024fe  __rtk_arch_exception
00002513  __rtk_arch_interrupt
00002528  __rtk_arch_load_unrelocated_word
00002549  __rtk_arch_resume
0000255b  __rtk_arch_vector_table
00002573  __rtk_arch_warm_boot
00002588  __rtk_crt_init_stack
0000259d  __rtk_crt_init_stack_base
000025b7  __rtk_crt_init_stack_len
000025d0  __rtk_crt_init_stack_top
000025e9  __rtk_crt_irq_stack
000025fd  __rtk_crt_irq_stack_base
00002616  __rtk_crt_irq_stack_len
0000262e  __rtk_crt_irq_stack_top
00002646  __rtk_dev_bad_method
0000265b  __rtk_patch__aslr_dst
00002671  __rtk_patch__aslr_slide
00002689  __rtk_patch__aslr_src
0000269f  __rtk_patch__dseg_relocate
000026ba  __rtk_patch__rtk_rebase_end
000026d6  __rtk_patch__rtk_rebase_start
000026f4  __rtk_patch__rtk_runtime_size
00002712  __rtk_patch__rtk_stack_guard
0000272f  __rtk_patch__rtk_text_size
0000274a  __rtk_patch_tunables_size
00002764  __rtk_patch_tunables_start
0000277f  __rtk_riscv_switch
00002792  __rtk_unexpected_reset
000027a9  __rtk_version_string
000027be  _gMemoryAllocator
000027d0  _gs_iFwToPop
000027dd  _gv_iCtxStarted
000027ed  _longjmp
000027fc  _memcpy
00002804  _memmove
0000280d  _memset
00002815  _rv_hb_ctx
00002820  _rv_hb_sleep_count
00002833  _rv_hb_wake_count
00002845  _rv_resume_flag
00002855  _rvic_icu
0000285f  _sSharedMem
0000286b  radr://5614542
```
