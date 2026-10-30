# `Firmware/ave/AppleAVE2FW_H19_AVE4.im4p`

- File size: 12,207 bytes
- IM4P: Tag: IM4P  Type: ave4  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder4`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave4
  Version:      1
  Data:         12 kB (12184 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 12,184 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit-3491.release`

## Strings (116) [FW]

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
00002010  RTKit-3491.release
00002255  stk_fail
0000225e  !Mthd:%p
00002464  not set
00002938  _AVE_ISR_HWResults
0000294b  _AVE_ISR_WakeUp
0000295b  _AVE_MCPUInit
00002969  _AVE_RV_CtxExecute
0000297c  _AVE_RV_Main
00002989  _AVE_RV_ProcessHwResults
000029a2  _RTK_DEV_ICU
000029af  _RTK_abort
000029ba  _RTK_arch_exception_handler
000029d6  _RTK_arch_fault_handler
000029ee  _RTK_arch_idle
000029fd  _RTK_arch_reset_handler
00002a15  _RTK_client_version_string
00002a30  _RTK_dev_rvic_bare_dispatch_v2_1
00002a51  _RTK_disable_all_interrupts
00002a6d  _RTK_enable_all_interrupts
00002a88  _RTK_exit
00002a92  _RTK_halt
00002a9c  _RTK_interrupt_attach
00002ab2  _RTK_interrupt_enable
00002ac8  _RTK_interrupt_set_type
00002ae0  _RTK_platform_init
00002af3  _RTK_restore_all_interrupts
00002b0f  _RTK_riscv32i_start
00002b23  _RTK_spinlock_lock
00002b3c  __MergedGlobals_gv_iCtxStarted
00002b5b  ___stack_chk_fail
00002b6d  ___stack_chk_guard
00002b80  ___stack_chk_guard_setup
00002b99  __hart_context_pointer
00002bb0  __rtk_arch_dummy_handler
00002bc9  __rtk_arch_exception
00002bde  __rtk_arch_interrupt
00002bf3  __rtk_arch_load_unrelocated_word
00002c14  __rtk_arch_resume
00002c26  __rtk_arch_vector_table
00002c3e  __rtk_arch_warm_boot
00002c53  __rtk_crt_init_stack
00002c68  __rtk_crt_init_stack_base
00002c82  __rtk_crt_init_stack_len
00002c9b  __rtk_crt_init_stack_top
00002cb4  __rtk_crt_irq_stack
00002cc8  __rtk_crt_irq_stack_base
00002ce1  __rtk_crt_irq_stack_len
00002cf9  __rtk_crt_irq_stack_top
00002d11  __rtk_dev_bad_method
00002d26  __rtk_patch__aslr_dst
00002d3c  __rtk_patch__aslr_slide
00002d54  __rtk_patch__aslr_src
00002d6a  __rtk_patch__dseg_relocate
00002d85  __rtk_patch__rtk_rebase_end
00002da1  __rtk_patch__rtk_rebase_start
00002dbf  __rtk_patch__rtk_runtime_size
00002ddd  __rtk_patch__rtk_stack_guard
00002dfa  __rtk_patch__rtk_text_size
00002e15  __rtk_patch_tunables_size
00002e2f  __rtk_patch_tunables_start
00002e4a  __rtk_riscv_switch
00002e5d  __rtk_unexpected_reset
00002e74  __rtk_version_string
00002e89  _gMemoryAllocator
00002e9b  _gv_iCtxStarted
00002eab  _gv_sSavedCUInterEn
00002ebf  _gv_sSavedCUIntraEn
00002ed3  _gv_sSavedCUSkipEn
00002ee6  _gv_sSavedPUEn
00002ef5  _gv_sSavedSkipMode
00002f08  _longjmp
00002f17  _memcpy
00002f1f  _memmove
00002f28  _memset
00002f30  _rv_hb_ctx
00002f3b  _rv_hb_sleep_count
00002f4e  _rv_hb_wake_count
00002f60  _rv_resume_flag
00002f70  _rvic_icu
00002f7a  _sSharedMem
00002f86  radr://5614542
```
