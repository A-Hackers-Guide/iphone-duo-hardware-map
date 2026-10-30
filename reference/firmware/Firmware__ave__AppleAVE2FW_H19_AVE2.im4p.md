# `Firmware/ave/AppleAVE2FW_H19_AVE2.im4p`

- File size: 11,863 bytes
- IM4P: Tag: IM4P  Type: ave2  Version: 1
- BuildManifest components that use it: `Ap,AppleVideoEncoder2`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ave2
  Version:      1
  Data:         12 kB (11840 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 11,840 bytes
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
00000ad4  BERObN
00001fc8  RTKit-3491.release
00002215  stk_fail
0000221e  !Mthd:%p
000023d4  not set
0000284c  _AVE_ISR_HWResults
0000285f  _AVE_ISR_WakeUp
0000286f  _AVE_MCPUInit
0000287d  _AVE_RV_Main
0000288a  _RTK_DEV_ICU
00002897  _RTK_abort
000028a2  _RTK_arch_exception_handler
000028be  _RTK_arch_fault_handler
000028d6  _RTK_arch_idle
000028e5  _RTK_arch_reset_handler
000028fd  _RTK_client_version_string
00002918  _RTK_dev_rvic_bare_dispatch_v2_1
00002939  _RTK_disable_all_interrupts
00002955  _RTK_enable_all_interrupts
00002970  _RTK_exit
0000297a  _RTK_halt
00002984  _RTK_interrupt_attach
0000299a  _RTK_interrupt_enable
000029b0  _RTK_interrupt_set_type
000029c8  _RTK_platform_init
000029db  _RTK_restore_all_interrupts
000029f7  _RTK_riscv32i_start
00002a0b  _RTK_spinlock_lock
00002a24  _UpdateFwData
00002a32  __MergedGlobals_gv_iCtxStarted
00002a51  ___stack_chk_fail
00002a63  ___stack_chk_guard
00002a76  ___stack_chk_guard_setup
00002a8f  __hart_context_pointer
00002aa6  __rtk_arch_dummy_handler
00002abf  __rtk_arch_exception
00002ad4  __rtk_arch_interrupt
00002ae9  __rtk_arch_load_unrelocated_word
00002b0a  __rtk_arch_resume
00002b1c  __rtk_arch_vector_table
00002b34  __rtk_arch_warm_boot
00002b49  __rtk_crt_init_stack
00002b5e  __rtk_crt_init_stack_base
00002b78  __rtk_crt_init_stack_len
00002b91  __rtk_crt_init_stack_top
00002baa  __rtk_crt_irq_stack
00002bbe  __rtk_crt_irq_stack_base
00002bd7  __rtk_crt_irq_stack_len
00002bef  __rtk_crt_irq_stack_top
00002c07  __rtk_dev_bad_method
00002c1c  __rtk_patch__aslr_dst
00002c32  __rtk_patch__aslr_slide
00002c4a  __rtk_patch__aslr_src
00002c60  __rtk_patch__dseg_relocate
00002c7b  __rtk_patch__rtk_rebase_end
00002c97  __rtk_patch__rtk_rebase_start
00002cb5  __rtk_patch__rtk_runtime_size
00002cd3  __rtk_patch__rtk_stack_guard
00002cf0  __rtk_patch__rtk_text_size
00002d0b  __rtk_patch_tunables_size
00002d25  __rtk_patch_tunables_start
00002d40  __rtk_riscv_switch
00002d53  __rtk_unexpected_reset
00002d6a  __rtk_version_string
00002d7f  _gMemoryAllocator
00002d91  _gv_iCtxStarted
00002da1  _gv_iHwRsltsRdy
00002db1  _longjmp
00002dc0  _memcpy
00002dc8  _memmove
00002dd1  _memset
00002dd9  _rv_hb_ctx
00002de4  _rv_hb_sleep_count
00002df7  _rv_hb_wake_count
00002e09  _rv_resume_flag
00002e19  _rvic_icu
00002e23  _sSharedMem
00002e2f  radr://5614542
```
