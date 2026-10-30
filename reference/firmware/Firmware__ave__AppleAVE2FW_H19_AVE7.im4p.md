# `Firmware/ave/AppleAVE2FW_H19_AVE7.im4p`

- File size: 12,915 bytes
- IM4P: Tag: IM4P  Type: ave7  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder7`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave7
  Version:      1
  Data:         13 kB (12892 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 12,892 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (118) [FW]

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
00002088  RTKit-3491.release
000022d5  stk_fail
000022de  !Mthd:%p
00002714  not set
00002be0  _AVE_ISR_HWResults
00002bf3  _AVE_ISR_WakeUp
00002c03  _AVE_MCPUInit
00002c11  _AVE_RV_CtxExecute
00002c24  _AVE_RV_Main
00002c31  _AVE_VLC_InsertAvcSliceHeader
00002c4f  _AVE_VLC_InsertHevcSliceHeader
00002c6e  _BitReverseTable256
00002c82  _ProcessHwResults
00002c94  _RTK_DEV_ICU
00002ca1  _RTK_abort
00002cac  _RTK_arch_exception_handler
00002cc8  _RTK_arch_fault_handler
00002ce0  _RTK_arch_idle
00002cef  _RTK_arch_reset_handler
00002d07  _RTK_client_version_string
00002d22  _RTK_dev_rvic_bare_dispatch_v2_1
00002d43  _RTK_disable_all_interrupts
00002d5f  _RTK_enable_all_interrupts
00002d7a  _RTK_exit
00002d84  _RTK_halt
00002d8e  _RTK_interrupt_attach
00002da4  _RTK_interrupt_enable
00002dba  _RTK_interrupt_set_type
00002dd2  _RTK_platform_init
00002de5  _RTK_restore_all_interrupts
00002e01  _RTK_riscv32i_start
00002e15  _RTK_spinlock_lock
00002e2e  _UpdateFwData
00002e3c  __MergedGlobals_gv_iCtxStarted
00002e5b  ___stack_chk_fail
00002e6d  ___stack_chk_guard
00002e80  ___stack_chk_guard_setup
00002e99  __hart_context_pointer
00002eb0  __rtk_arch_dummy_handler
00002ec9  __rtk_arch_exception
00002ede  __rtk_arch_interrupt
00002ef3  __rtk_arch_load_unrelocated_word
00002f14  __rtk_arch_resume
00002f26  __rtk_arch_vector_table
00002f3e  __rtk_arch_warm_boot
00002f53  __rtk_crt_init_stack
00002f68  __rtk_crt_init_stack_base
00002f82  __rtk_crt_init_stack_len
00002f9b  __rtk_crt_init_stack_top
00002fb4  __rtk_crt_irq_stack
00002fc8  __rtk_crt_irq_stack_base
00002fe1  __rtk_crt_irq_stack_len
00002ff9  __rtk_crt_irq_stack_top
00003011  __rtk_dev_bad_method
00003026  __rtk_patch__aslr_dst
0000303c  __rtk_patch__aslr_slide
00003054  __rtk_patch__aslr_src
0000306a  __rtk_patch__dseg_relocate
00003085  __rtk_patch__rtk_rebase_end
000030a1  __rtk_patch__rtk_rebase_start
000030bf  __rtk_patch__rtk_runtime_size
000030dd  __rtk_patch__rtk_stack_guard
000030fa  __rtk_patch__rtk_text_size
00003115  __rtk_patch_tunables_size
0000312f  __rtk_patch_tunables_start
0000314a  __rtk_riscv_switch
0000315d  __rtk_unexpected_reset
00003174  __rtk_version_string
00003189  _bitReverse
00003195  _gMemoryAllocator
000031a7  _gv_iCtxStarted
000031b7  _insertBitsLsb
000031c6  _longjmp
000031d5  _memcpy
000031dd  _memmove
000031e6  _memset
000031ee  _numtoue
000031f7  _rv_hb_ctx
00003202  _rv_hb_sleep_count
00003215  _rv_hb_wake_count
00003227  _rv_resume_flag
00003237  _rvic_icu
00003241  _sSharedMem
0000324d  radr://5614542
```
