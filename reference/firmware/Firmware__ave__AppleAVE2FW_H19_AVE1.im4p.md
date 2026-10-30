# `Firmware/ave/AppleAVE2FW_H19_AVE1.im4p`

- File size: 17,563 bytes
- IM4P: Tag: IM4P  Type: ave1  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder1`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave1
  Version:      1
  Data:         18 kB (17540 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 17,540 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (120) [FW]

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
000034dc  RTKit-3491.release
00003715  stk_fail
0000371e  !Mthd:%p
000038fc  not set
00003de0  _AVE_HEIF_CtxSetup
00003df3  _AVE_HEIF_Process
00003e05  _AVE_HEIF_QPModByVar
00003e1a  _AVE_HEIF_QuadraHeifTuning
00003e35  _AVE_ISR_HWResults
00003e48  _AVE_ISR_WakeUp
00003e58  _AVE_MCPUInit
00003e66  _AVE_RV_CtxExecute
00003e79  _AVE_RV_CtxSetup
00003e8a  _AVE_RV_Main
00003e97  _ProcessHwResults
00003ea9  _RTK_DEV_ICU
00003eb6  _RTK_abort
00003ec1  _RTK_arch_exception_handler
00003edd  _RTK_arch_fault_handler
00003ef5  _RTK_arch_idle
00003f04  _RTK_arch_reset_handler
00003f1c  _RTK_client_version_string
00003f37  _RTK_dev_rvic_bare_dispatch_v2_1
00003f58  _RTK_disable_all_interrupts
00003f74  _RTK_enable_all_interrupts
00003f8f  _RTK_exit
00003f99  _RTK_halt
00003fa3  _RTK_interrupt_attach
00003fb9  _RTK_interrupt_enable
00003fcf  _RTK_interrupt_set_type
00003fe7  _RTK_platform_init
00003ffa  _RTK_restore_all_interrupts
00004016  _RTK_riscv32i_start
0000402a  _RTK_spinlock_lock
00004043  __MergedGlobals_gv_iCtxStarted
00004062  ___stack_chk_fail
00004074  ___stack_chk_guard
00004087  ___stack_chk_guard_setup
000040a0  __hart_context_pointer
000040b7  __rtk_arch_dummy_handler
000040d0  __rtk_arch_exception
000040e5  __rtk_arch_interrupt
000040fa  __rtk_arch_load_unrelocated_word
0000411b  __rtk_arch_resume
0000412d  __rtk_arch_vector_table
00004145  __rtk_arch_warm_boot
0000415a  __rtk_crt_init_stack
0000416f  __rtk_crt_init_stack_base
00004189  __rtk_crt_init_stack_len
000041a2  __rtk_crt_init_stack_top
000041bb  __rtk_crt_irq_stack
000041cf  __rtk_crt_irq_stack_base
000041e8  __rtk_crt_irq_stack_len
00004200  __rtk_crt_irq_stack_top
00004218  __rtk_dev_bad_method
0000422d  __rtk_patch__aslr_dst
00004243  __rtk_patch__aslr_slide
0000425b  __rtk_patch__aslr_src
00004271  __rtk_patch__dseg_relocate
0000428c  __rtk_patch__rtk_rebase_end
000042a8  __rtk_patch__rtk_rebase_start
000042c6  __rtk_patch__rtk_runtime_size
000042e4  __rtk_patch__rtk_stack_guard
00004301  __rtk_patch__rtk_text_size
0000431c  __rtk_patch_tunables_size
00004336  __rtk_patch_tunables_start
00004351  __rtk_riscv_switch
00004364  __rtk_unexpected_reset
0000437b  __rtk_version_string
00004390  _extremeDarkLumaDeltaQp
000043a8  _gMemoryAllocator
000043ba  _gs_iDbgOrder
000043c8  _gs_psaEMem
000043d4  _gv_iCtxStarted
000043e4  _longjmp
000043f3  _memcpy
000043fb  _memmove
00004404  _memset
0000440c  _rv_hb_ctx
00004417  _rv_hb_sleep_count
0000442a  _rv_hb_wake_count
0000443c  _rv_resume_flag
0000444c  _rvic_icu
00004456  _sSharedMem
00004462  _ultraFlatDeltaQp
00004474  radr://5614542
```
