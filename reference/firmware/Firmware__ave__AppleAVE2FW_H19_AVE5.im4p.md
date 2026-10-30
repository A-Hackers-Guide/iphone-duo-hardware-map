# `Firmware/ave/AppleAVE2FW_H19_AVE5.im4p`

- File size: 11,911 bytes
- IM4P: Tag: IM4P  Type: ave5  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder5`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave5
  Version:      1
  Data:         12 kB (11888 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 11,888 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (112) [FW]

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
00001eb0  RTKit-3491.release
000020d5  stk_fail
000020de  !Mthd:%p
000023e4  not set
00002868  _AVE_ISR_HWResults
0000287b  _AVE_ISR_WakeUp
0000288b  _AVE_MCPUInit
00002899  _AVE_RV_CtxExecute
000028ac  _AVE_RV_Main
000028b9  _RTK_DEV_ICU
000028c6  _RTK_abort
000028d1  _RTK_arch_exception_handler
000028ed  _RTK_arch_fault_handler
00002905  _RTK_arch_idle
00002914  _RTK_arch_reset_handler
0000292c  _RTK_client_version_string
00002947  _RTK_dev_rvic_bare_dispatch_v2_1
00002968  _RTK_disable_all_interrupts
00002984  _RTK_enable_all_interrupts
0000299f  _RTK_exit
000029a9  _RTK_halt
000029b3  _RTK_interrupt_attach
000029c9  _RTK_interrupt_enable
000029df  _RTK_interrupt_set_type
000029f7  _RTK_platform_init
00002a0a  _RTK_restore_all_interrupts
00002a26  _RTK_riscv32i_start
00002a3a  _RTK_spinlock_lock
00002a53  _UpdateAdptB
00002a60  __MergedGlobals_gv_iCtxStarted
00002a7f  ___stack_chk_fail
00002a91  ___stack_chk_guard
00002aa4  ___stack_chk_guard_setup
00002abd  __hart_context_pointer
00002ad4  __rtk_arch_dummy_handler
00002aed  __rtk_arch_exception
00002b02  __rtk_arch_interrupt
00002b17  __rtk_arch_load_unrelocated_word
00002b38  __rtk_arch_resume
00002b4a  __rtk_arch_vector_table
00002b62  __rtk_arch_warm_boot
00002b77  __rtk_crt_init_stack
00002b8c  __rtk_crt_init_stack_base
00002ba6  __rtk_crt_init_stack_len
00002bbf  __rtk_crt_init_stack_top
00002bd8  __rtk_crt_irq_stack
00002bec  __rtk_crt_irq_stack_base
00002c05  __rtk_crt_irq_stack_len
00002c1d  __rtk_crt_irq_stack_top
00002c35  __rtk_dev_bad_method
00002c4a  __rtk_patch__aslr_dst
00002c60  __rtk_patch__aslr_slide
00002c78  __rtk_patch__aslr_src
00002c8e  __rtk_patch__dseg_relocate
00002ca9  __rtk_patch__rtk_rebase_end
00002cc5  __rtk_patch__rtk_rebase_start
00002ce3  __rtk_patch__rtk_runtime_size
00002d01  __rtk_patch__rtk_stack_guard
00002d1e  __rtk_patch__rtk_text_size
00002d39  __rtk_patch_tunables_size
00002d53  __rtk_patch_tunables_start
00002d6e  __rtk_riscv_switch
00002d81  __rtk_unexpected_reset
00002d98  __rtk_version_string
00002dad  _gMemoryAllocator
00002dbf  _gv_iCtxStarted
00002dcf  _gv_sSavedSkipMode
00002de2  _longjmp
00002df1  _memcpy
00002df9  _memmove
00002e02  _memset
00002e0a  _rv_hb_ctx
00002e15  _rv_hb_sleep_count
00002e28  _rv_hb_wake_count
00002e3a  _rv_resume_flag
00002e4a  _rvic_icu
00002e54  _sSharedMem
00002e60  radr://5614542
```
