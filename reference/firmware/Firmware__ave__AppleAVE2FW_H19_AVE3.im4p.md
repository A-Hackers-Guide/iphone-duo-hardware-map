# `Firmware/ave/AppleAVE2FW_H19_AVE3.im4p`

- File size: 9,975 bytes
- IM4P: Tag: IM4P  Type: ave3  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder3`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave3
  Version:      1
  Data:         10 kB (9952 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 9,952 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (110) [FW]

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
00001888  RTKit-3491.release
00001ad5  stk_fail
00001ade  !Mthd:%p
00001c8c  not set
000020f8  _AVE_ISR_HWResults
0000210b  _AVE_ISR_WakeUp
0000211b  _AVE_MCPUInit
00002129  _AVE_RV_CtxExecute
0000213c  _AVE_RV_Main
00002149  _RTK_DEV_ICU
00002156  _RTK_abort
00002161  _RTK_arch_exception_handler
0000217d  _RTK_arch_fault_handler
00002195  _RTK_arch_idle
000021a4  _RTK_arch_reset_handler
000021bc  _RTK_client_version_string
000021d7  _RTK_dev_rvic_bare_dispatch_v2_1
000021f8  _RTK_disable_all_interrupts
00002214  _RTK_enable_all_interrupts
0000222f  _RTK_exit
00002239  _RTK_halt
00002243  _RTK_interrupt_attach
00002259  _RTK_interrupt_enable
0000226f  _RTK_interrupt_set_type
00002287  _RTK_platform_init
0000229a  _RTK_restore_all_interrupts
000022b6  _RTK_riscv32i_start
000022ca  _RTK_spinlock_lock
000022e3  __MergedGlobals_gv_iCtxStarted
00002302  ___stack_chk_fail
00002314  ___stack_chk_guard
00002327  ___stack_chk_guard_setup
00002340  __hart_context_pointer
00002357  __rtk_arch_dummy_handler
00002370  __rtk_arch_exception
00002385  __rtk_arch_interrupt
0000239a  __rtk_arch_load_unrelocated_word
000023bb  __rtk_arch_resume
000023cd  __rtk_arch_vector_table
000023e5  __rtk_arch_warm_boot
000023fa  __rtk_crt_init_stack
0000240f  __rtk_crt_init_stack_base
00002429  __rtk_crt_init_stack_len
00002442  __rtk_crt_init_stack_top
0000245b  __rtk_crt_irq_stack
0000246f  __rtk_crt_irq_stack_base
00002488  __rtk_crt_irq_stack_len
000024a0  __rtk_crt_irq_stack_top
000024b8  __rtk_dev_bad_method
000024cd  __rtk_patch__aslr_dst
000024e3  __rtk_patch__aslr_slide
000024fb  __rtk_patch__aslr_src
00002511  __rtk_patch__dseg_relocate
0000252c  __rtk_patch__rtk_rebase_end
00002548  __rtk_patch__rtk_rebase_start
00002566  __rtk_patch__rtk_runtime_size
00002584  __rtk_patch__rtk_stack_guard
000025a1  __rtk_patch__rtk_text_size
000025bc  __rtk_patch_tunables_size
000025d6  __rtk_patch_tunables_start
000025f1  __rtk_riscv_switch
00002604  __rtk_unexpected_reset
0000261b  __rtk_version_string
00002630  _gMemoryAllocator
00002642  _gv_iCtxStarted
00002652  _longjmp
00002661  _memcpy
00002669  _memmove
00002672  _memset
0000267a  _rv_hb_ctx
00002685  _rv_hb_sleep_count
00002698  _rv_hb_wake_count
000026aa  _rv_resume_flag
000026ba  _rvic_icu
000026c4  _sSharedMem
000026d0  radr://5614542
```
