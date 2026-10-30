# `Firmware/avd/AppleAVDFW_H19P.im4p`

- File size: 107,464 bytes
- IM4P: Tag: IM4P  Type: avdf  Version: 280d6e11
- BuildManifest components that use it: `Ap,AVD`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         avdf
  Version:      280d6e11
  Data:         107 kB (107432 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 107,432 bytes
- Format: raw binary

## Strings (190) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000024  __TEXT
00000054  __vectors
00000064  __TEXT
00000098  __fw_rel_vn
000000a8  __TEXT
000000dc  __text
000000ec  __TEXT
00000120  __const
00000130  __TEXT
00000164  _rtk_patchbay
00000174  __TEXT
000001a8  __cstring
000001b8  __TEXT
000001ec  __constructor
000001fc  __TEXT
00000238  __DATA
00000268  __shared
00000278  __DATA
000002ac  _rtk_power
000002bc  __DATA
000002f0  __data
00000300  __DATA
00000334  __mod_init_func
00000344  __DATA
00000378  __zerofill
00000388  __DATA
000009b9  &NaJa "Ja@"Ja
00000e09  dVeTfTg
000084fd  dg!Afh!
000088ed  v@F1FZF
00008b13  t@F!FZF
00008ff7  a)hAa)l
000092f6  RR RRR,<A
0000d626   Chb(iQF
0000e890  RTKSTACKGKTS
0000e8ed  stk_fail
00019a7c  _FaultISR
00019a86  _IntDefaultHandler
00019a99  _NmiISR
00019aa1  _RTK_abort
00019aac  _RTK_arch_aslr_fault_handler
00019ac9  _RTK_arch_reset_handler
00019ae1  _RTK_armv7m_start
00019af3  _RTK_enable_all_interrupts
00019b0e  _RTK_exit
00019b18  _RTK_halt
00019b22  _Vectors
00019b2b  ___stack_chk_fail
00019b3d  ___stack_chk_guard
00019b50  ___stack_chk_guard_setup
00019b69  __rtk_crt_init_stack
00019b7e  __rtk_crt_init_stack_base
00019b98  __rtk_crt_init_stack_len
00019bb1  __rtk_crt_init_stack_top
00019bca  __rtk_crt_irq_stack
00019bde  __rtk_crt_irq_stack_base
00019bf7  __rtk_crt_irq_stack_len
00019c0f  __rtk_crt_irq_stack_top
00019c27  __rtk_patch__aslr_slide
00019c3f  __rtk_patch__dseg_relocate
00019c5a  __rtk_patch__rtk_rebase_end
00019c76  __rtk_patch__rtk_rebase_start
00019c94  __rtk_patch__rtk_runtime_size
00019cb2  __rtk_patch__rtk_stack_guard
00019ccf  __rtk_patch__rtk_text_size
00019cea  __rtk_stack_watermark
00019d00  __rtk_unexpected_reset
00019d17  _adsDataCommand
00019d27  _adsDataLoopCommand
00019d3b  _adsFifoFullness
00019d4c  _adsISR
00019d54  _adsReady
00019d5e  _adsReset
00019d68  _adsSample
00019d73  _adsSubSample
00019d81  _arm_resume_address
00019d95  _arm_resume_flag
00019da6  _armv7m_maskable_basepri
00019dbf  _armv7m_non_maskable_priority
00019ddd  _avcPipeDone
00019dea  _avdFifo
00019df3  _avp0AbortISR
00019e01  _avp0CmdISR
00019e0d  _avp0DoneISR
00019e1a  _avp0ErrorISR
00019e28  _avp1AbortISR
00019e36  _avp1CmdISR
00019e42  _avp1DoneISR
00019e4f  _avp1ErrorISR
00019e5d  _avp2AbortISR
00019e6b  _avp2CmdISR
00019e77  _avp2DoneISR
00019e84  _avp2ErrorISR
00019e92  _avp3AbortISR
00019ea0  _avp3CmdISR
00019eac  _avp3DoneISR
00019eb9  _avp3ErrorISR
00019ec7  _avpDone
00019ed0  _avp_qmat_coeff_max_insn_cnt
00019eed  _avxPipeDone
00019efa  _checkAndReportError
00019f0f  _clearDmacPendingInterrupt
00019f2a  _debugCount
00019f36  _dmaErrorISR
00019f43  _firmware_release_version
00019f5d  _firmware_version
00019f6f  _getADSInfo
00019f7b  _get_mcw_dsid_ops_response
00019f96  _handleAbort
00019fa3  _handleBsErr
00019fb0  _hevcPipeDone
00019fbe  _hvp0AbortISR
00019fcc  _hvp0CmdISR
00019fd8  _hvp0DoneISR
00019fe5  _hvp0ErrorISR
00019ff3  _hvp1AbortISR
0001a001  _hvp1CmdISR
0001a00d  _hvp1DoneISR
0001a01a  _hvp1ErrorISR
0001a028  _hvp2AbortISR
0001a036  _hvp2CmdISR
0001a042  _hvp2DoneISR
0001a04f  _hvp2ErrorISR
0001a05d  _hvp3AbortISR
0001a06b  _hvp3CmdISR
0001a077  _hvp3DoneISR
0001a084  _hvp3ErrorISR
0001a092  _hvpDone
0001a09b  _hvp_qmat_coeff_max_insn_cnt
0001a0b8  _inbox0NEISR
0001a0c5  _initADS
0001a0ce  _initAVP
0001a0d7  _initHVP
0001a0e0  _initHW
0001a0e8  _initLVP
0001a0f1  _initOVP
0001a0fa  _lvpAbortISR
0001a107  _lvpCmdISR
0001a112  _lvpDone
0001a11b  _lvpDoneISR
0001a127  _lvpErrorISR
0001a13a  _mcpuirq_nvic_enable
0001a14f  _mcwErrorISR
0001a15c  _mcwISR
0001a164  _memcpy
0001a16c  _memmove
0001a175  _memset
0001a17d  _nextADS
0001a186  _nextAVP
0001a18f  _nextAvcVPS
0001a19b  _nextAvxVPS
0001a1a7  _nextHVP
0001a1b0  _nextHevcVPS
0001a1bd  _nextLVP
0001a1c6  _nextOVP
0001a1cf  _nextVpxVPS
0001a1db  _outbox0EISR
0001a1e8  _ovp0AbortISR
0001a1f6  _ovp0CmdISR
0001a202  _ovp0DoneISR
0001a20f  _ovp0ErrorISR
0001a21d  _ovp1AbortISR
0001a22b  _ovp1CmdISR
0001a237  _ovp1DoneISR
0001a244  _ovp1ErrorISR
0001a252  _ovp2AbortISR
0001a260  _ovp2CmdISR
0001a26c  _ovp2DoneISR
0001a279  _ovp2ErrorISR
0001a287  _ovpDone
0001a290  _pipeAbortISR
0001a29e  _pipeBreakpointISR
0001a2b1  _pipeCmdISR
0001a2bd  _pipeDone
0001a2c7  _pipeDoneISR
0001a2d4  _processSetProperty
0001a2e8  _program_dma_bfrconfig
0001a2ff  _recordErrorStatus
0001a312  _sharedMem
0001a31d  _startAVP
0001a327  _startAvcVPS
0001a334  _startAvxVPS
0001a341  _startFrame
0001a34d  _startHVP
0001a357  _startHevcVPS
0001a365  _startLVP
0001a36f  _startOVP
0001a379  _startVpxVPS
0001a386  _vpxPipeDone
0001a393  _waitUntilKPSReady
```
