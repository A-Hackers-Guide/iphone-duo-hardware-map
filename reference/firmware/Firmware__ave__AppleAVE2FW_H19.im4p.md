# `Firmware/ave/AppleAVE2FW_H19.im4p`

- File size: 2,737,129 bytes
- IM4P: Tag: IM4P  Type: avef  Version: 1
- BuildManifest components that use it: `AVE`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         avef
  Version:      1
  Data:         2.7 MB (2737104 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 2,737,104 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- `./RTKit/ffw/CBuffer.cpp`
- `./RTKit/ffw/CChannelManager.cpp`
- `./RTKit/ffw/CController.cpp`
- `./RTKit/ffw/CEnvironment.cpp`
- `./RTKit/ffw/CFSM.cpp`
- `./RTKit/ffw/CFilter.cpp`
- `./RTKit/ffw/CGPIOManager.cpp`
- `./RTKit/ffw/CIOObject.cpp`
- `./RTKit/ffw/CISRManager.cpp`
- `./RTKit/ffw/CLoggerInterProcessor.cpp`
- `./RTKit/ffw/CMMU.cpp`
- `./RTKit/ffw/CMailboxPool.cpp`
- `./RTKit/ffw/CObject.cpp`
- `./RTKit/ffw/CPipe.cpp`
- `./RTKit/ffw/CQueuePool.cpp`
- `./RTKit/ffw/CRTOSObjectPool.cpp`
- `./RTKit/ffw/CResourcePool.cpp`
- `./RTKit/ffw/CRoot.cpp`
- `./RTKit/ffw/CScopedLock.cpp`
- `./RTKit/ffw/CSemaphorePool.cpp`
- `./RTKit/ffw/CSharedMemory.cpp`
- `./RTKit/ffw/CSharedMemoryHeap.cpp`
- `./RTKit/ffw/CSharedMemoryHost.cpp`
- `./RTKit/ffw/CSignalPool.cpp`
- `./RTKit/ffw/CTaskPool.cpp`
- `./RTKit/ffw/CTerminalOut.cpp`
- `./RTKit/ffw/CTimerManager.cpp`
- `./RTKit/ffw/CTimerPool.cpp`
- `./RTKit/platform/common/CDockChannel.cpp`
- `./RTKit/platform/common/CFakeChannel.cpp`
- `./RTKit/platform/common/CPlatformEnvironment.cpp`
- `./RTKit/platform/common/CPlatformGPIOManager.cpp`
- `./RTKit/platform/common/CPlatformISRManager.cpp`
- `./RTKit/platform/common/CRealChannel.cpp`
- `./RTKit/platform/common/ChannelTable.cpp`
- `./RTKit/platform/common/FakeChannelTable.cpp`
- `./RTKit/platform/common/IOP/AVE_IOP_panda.cpp`
- `./RTKit/platform/common/RealChannelTableTarget.cpp`
- `Copyright (c) Apple Inc. All Rights Reserved.`
- `RTKit: %s - Client: %s`
- `RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release`

## Strings (4,808) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.
First 4,000 of 4,808.

```
00000028  __TEXT
00000068  __text
00000078  __TEXT
000000b8  __const
000000c8  __TEXT
00000108  __cstring
00000118  __TEXT
00000158  __init_offsets
00000168  __TEXT
000001a8  __chain_starts
000001b8  __TEXT
00000200  __DATA
00000240  _rtk_patchbay
00000250  __DATA
00000290  __data
000002a0  __DATA
000002e0  _rtk_mtab
000002f0  __DATA
00000330  __const
00000340  __DATA
00000380  _rtk_power
00000390  __DATA
000003d0  __gxf_data
000003e0  __DATA
00000420  _rtk_tunables
00000430  __DATA
00000470  __mod_init_func
00000480  __DATA
000004c0  _rtk_init_stack
000004d0  __DATA
00000510  _rtk_irq_stack
00000520  __DATA
00000560  _rtk_exc_stack
00000570  __DATA
000005b0  _rtk_boot
000005c0  __DATA
00000600  _rtk_page_tables__DATA
00000650  __noinit
00000660  __DATA
000006a0  _rtk_data_uuid
000006b0  __DATA
000006f0  _rtk_heap
00000700  __DATA
00000740  _rtk_threads
00000750  __DATA
00000790  __constructor
000007a0  __DATA
000007e0  __zerofill
000007f0  __DATA
00000838  __DATA_CONST
000049b9  wwwwwww
0000aa5c  MAW9KyE
0000bafa  @9*M@8kNq
00010b11  Z@)hVq
000185ee  C8hdE9-
00018e5e  I8hDB99
00018e7c  yTB9~O@8w
0001c92d  j/8Pin
00020dce  anm1@)
000399e8  ibA9hb
000399f7  9ir@yhB
00039a5b  9hv@yiF
00039ad7  9hz@yiJ
00039b53  9h~@yiN
0003bd09  kj8iJA
0003d4d7  RJik8+
0003e690  IE@9JA@9hkh
0003f16e  @9*M@8kNq
0003ffff  rKi@9M
00041ec1  JE9iVA
00041ed1  BK9hRq
00045f24  _!1kAq
0004f1a5  "@9iZr
0004f23f  R(ihxh5
00051260  ghf8whu8
00051288  whu8yhx8
000512dc  ghf8whu8
00051304  yhx8whu8
00051375  hu8ghf8
00051381  hx8xhx8
00051b3c  Jyhxhyh
0005303b  5jVA9_
000613f0  jz`ykr`y
00063f50  nFOyoS@9
00066363  ThFj9(
00067877  TiFj9I
00067d6f  ThFj9h
00068463  TjW@9_!
00077ec0  BX`xcX`xD
00078cf4  K1D)Mic
00078f18  K1D)Mic
000923f7  4hzA9i
000a436e  NzB9JzI
000a5b3c  p^@ytZ@y
000a5b5b  Tpn@ytj@y
000a5c4f  5j&Ayp"Ay$
000a5c83  Tp&Ays"Ay1
000a5d8f  q"9Izb9Nz
000a9dd3  Rmi,8?
000aa709  B@yivS
000aa715  F@yivS
000aaeed  B@yivS
000aaef9  F@yivS
000ab729  B@yivS
000ab735  F@yivS
000abea8  pAW9nyE
000ad375  B@yjvS
000ad381  F@yjvS
000ae6a9  B@yivS
000ae6b5  F@yivS
000ae855  B@yivS
000ae861  F@yivS
000c5e84  li(8hbM
000e0fb9  ydx"h 
000e0fed  ycx"x$
000e1025  yex"x#
000e5b97  6iZF9&
00128dc7  H(HHHHHHHHHHH
00128dd7  H(HHHHHHHHHHH
00128df7  H(HHHHHHHHHHH
00128e07  H(HHHHHHHHHHH
00128e28   (     (0((((((00000000888888@@@@@HHHHHHHHHH
00128e68   (     (0((((((00000000888888@@@@@HHHHHHHHHH
00128e9d   H0(0HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
00128edd   H0(0HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
00128f1d   H0(0HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
00128f5d   H0(0HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
00128fb2  (@00@PPPppx
00128fe2  (@00@PPPppx
0012901b  (0((((0@00000@P@@@@@@PPPPPPPP``````pppppxxxxxxxxxx
0012905b  (0((((0@00000@P@@@@@@PPPPPPPP``````pppppxxxxxxxxxx
001291bb  $8..8BBBVV`
001291eb   0((0888HHP
001291fb  ,H::HVVVrr
00129237  $),)$/66/AFAXXs
001292b7  $),)$/66/AFAXXs
00129337  $),)$/66/AFAXXs
00129e7e  YAl?tAT
00129eae  YBl?tBT
0012a052  YAl?tAT
0012a082  YBl?tBT
0012b0f2  q?nhr?
0013868f  ?8bunz8
001393f0  8bunz8
00139b50  UUUUUU
0013a2e8  RTKSTACK
0013a2fc  RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release
0013a330  tTxEhTTR
0013a340  tTDPhTTR
0013ace4  stk_fail
0013ad00  BUF_H2T
0013ad08  BUF_T2H
0013ad10  ASSERT: %s:%d %s
0013ad21  ./AppleAVE2FW/Legacy/CAVCControllerCommon.cpp
0013ad4f  clientBuffer != NULL
0013ad64  ASSERT: %s %s
0013ad72  CAVCController
0013ad81  clientBufferAvailableSize >= kClientBufferSize
0013adb0  %s::%s Enter
0013adbd  ResetBetweenPasses
0013add0  %s::%s Exit %d
0013ade4  StartLRME
0013adee  %s::%s Exit
0013adfa  %s:%d HiMode: %d TID: %d %d
0013ae37  %s:%d FrameType: %d FrameNum: %lld POC: %d qp: %d
0013ae69  EncCommParams.slices_per_frame <= AVE_SLICE_ACTIVE_MAX_NUM
0013aea4  PipePrepareParam
0013aeb5  pPicParams->sBufPFSet.sMultiPassStats.iAddr != 0
0013aee6  %s::%s:%d fid:%d fnum:%d fDr:%d qp:%d
0013af0c  %s::%s:%d Qp = %d, init qpm26 = %d, slice_qp_delta = %d, rc flag = %d
0013af52  %s::%s:%d #[%d] SNRMode %d bFlatAreaLowQpEn %d bExtremeLumaQPModEn %d
0013af98  pPicParams
0013afa3  ProcessPipeStart
0013afb4  %s::%s:%d %s | No slice header buffer! %p
0013afde  pPicParams->sBufPFSet.sSliceHeader.iAddr != 0
0013b00c  %s::%s:%d %s | No enough memory for slice header! %p %d %d
0013b047  pPicParams->sBufPFSet.sSliceHeader.iSize >= (((64) + (32) - 1) & ~((32) - 1))
0013b095  StartPipe
0013b09f  PipeDone
0013b0a8  SetTranscode
0013b0b5  EncCommParams.encoder_addr_entropy[0][EncCommParams.transcode_buffer_id].saIBuf[AVE_BufIdx_Header].iAddr != 0
0013b123  (EncCommParams.encoder_addr_entropy[0][EncCommParams.transcode_buffer_id].saIBuf[AVE_BufIdx_Header].iAddr&(64-1)) == 0
0013b19a  EncCommParams.encoder_addr_src_nbr_data != 0
0013b1c7  EncCommParams.curr_bitstream_addr_dst != 0
0013b1f2  EncCommParams.encoder_addr_dst_nbr_data != 0
0013b21f  StartTranscode
0013b22e  TranscodeDone
0013b23c  ProcessInit
0013b248  %s::%s InitEncodingParameters failed %d
0013b29b  ProcessLRMEDone
0013b2ab  frame done : %d, currMbRow:%d, pic_height_in_mbs:%d
0013b2e9  ProcessLRMEStart
0013b310  ProcessPipeDone
0013b320  %s fid=%d
0013b32b  PIPE done, override frame_done due to no static context switch
0013b36b  ProcessAvcPipeDone currMbRow %d pic_height_in_mbs %d frame_enc_state.frame_done %d
0013b3bf  frame not done!
0013b3d0  frame done!
0013b3dd  %s::%s decodeOrder=%d numIntra=%d numInter=%d numSkip=%d IntraSumSatd=%u, InterSumSatd=%u
0013b44c  %s::%s:%d Transcode Error! code 0x%08x value 0x%08x
0013b480  %s::%s:%d Encoder %lld frame_num %d size %d
0013b4ac  %s::%s:%d currMbRow %d pic_height_in_mbs %d frame_done %d
0013b4e6  *** frame %d bin count violation %d max %d rawMbBits %d picSizeInMbs %d numBytes %d ***
0013b53f  *** bin count violation insert %d CABAZ zero words
0013b573  bitstream size overflow, buffer size: %d, bitstream size: %d
0013b5b1  %s::%s Enter %p %p
0013b5db  %s::%s:%d %s | NULL video context!!! %p
0013b603  pInitParams != __null
0013b619  EncCommParams.pPerfBuffer
0013b633  [PERF] client %llu dump buffer %p (allocated)
0013b662  [PERF] XXXX client[%llu] dump buffer %p
0013b68b  EncCommParams.primo_core_idx = %d
0013b6ad  fchou_debug: bLowerQP4MbEn=%d
0013b6cc  fchou_debug: bFlatAreaLowQpEn=%d bExtremeLumaQPModEn=%d
0013b705  QPMod debug: iFeature=0x%x
0013b721  %s::%s:%d bFlatAreaLowQpEn is enable incorrectly %d %d
0013b758  cdai_debug: bFlatAreaLowQpEn=%d
0013b779  fchou_debug: EncCommParams.skip_mode = %d EncCommParams.skip_coeff_cancel = %d
0013b7c9  %s::%s:%d %s | failed to allocate memory
0013b7f2  EncCommParams.pCbp0CntPrv != __null
0013b816  EncCommParams.encoder_addr_entropy[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr %016llx, size 0x%x
0013b873  %s::%s:%d %p MCTF LFSRef buffers num %d
0013b89b  %s::%s:%d MCTF output buffers num %d
0013b8c0  clientBufferAvailableSize >= sizeof(*hRateControl[AVE_BASE_LAYER])
0013b903  laDebug: cqp %d
0013b914  Try to enable segment encoding but has no enough frames: %d
0013b950  %s::%s:%d: ResumableEncoding = %d - %d, %d
0013b97b  clientBufferAvailableSize >= sizeof(H264VideoEncoderDPB)
0013b9b4  %s::%s:%d %s | Failed to initialize DPB %d
0013b9df  ret == 0
0013b9e8  %s::%s:%d: AVE version = 0x%x
0013ba06  %s::%s:%d %s | No SPS or PPS %d
0013ba26  psPSInfo->iNum > 0
0013ba39  %s::%s:%d PSInfo num %d PS header bits count %d
0013ba69  %s::%s:%d %s | Failed to initialize scaling list registers %d
0013baa7  %s::%s Exit %p %llu %p %d
0013baef  EncCommParams.sAlgCfg.sComm.iFrameRate > 0
0013bb1a  %s::%s:%d bpp=%d.%02d bitrate=%d framerate=%d
0013bb48  %s::%s Enter %d %d
0013bb75  %s::%s Exit %d %d
0013bb87  F %d SliceType %d qp %d prevqp %d LowerDeltaQP %d totalLowQPMB %d totalLowQPMBHasCBP %d
0013bbe0  nRemWords > 0
0013bc09  nRemWords <= BITMAP_16X16_BUF_SIZE_IN_WORDS
0013bc35  (Write cbp0 flag) F %d, sliceType %d VTId %d accumcbp0Cnts %d  
0013bc76  ===== process cbp0Cnt, bCbp0CntBufReset = %d 
0013bcc1  (Flag Calculation) F %d, sliceType %d VTID %d accumcbp0Cnts %d NumTemporalLayers %d 
0013bd2d  GetSliceHeaderForFW
0013bd41  %s::%s getPPSHeaderForFW count (%d) > length (%d)
0013bd73  %s::%s:%d PSInfo num %d
0013bda2  %s::%s:%d i %d eType %d iLayerID %d iOffset %d iSize %d
0013bdda  %s::%s pipe_frame_id %d coded_data_hdr 0x%p, sz = %lu
0013be11  CollectDataFromCpus
0013be25  Detected Running Contexts:%d, Hw:%d
0013be49  %s:%s EncCommParams.use_CAVLC_bits %d
0013be6f  %s::%s Enter transcode_frame_id %d coded_data_hdr 0x%p
0013bebf  EncCommParams.slice_count < AVE_SLICE_ACTIVE_MAX_NUM
0013bef4  EncCommParams.slice_count >= 1
0013bf13  EncCommParams.slice_count > 0
0013bf31  %s::%s:%d slice count %d
0013bf4a  %s::%s:%d slice %d offset %d size %d
0013bf6f  %s::%s:%d fid:%d fnum:%d fDr:%d bitsFromTranscode:%d
0013bfa4  slice_count = %d
0013bfb6  width: %d
0013bfc1  height: %d
0013bfcd  number of slices: %d
0013bfe3  eRCMode %d
0013bfef  skip mode: %d (0: normal, 1: natural skip, 2: adaptive)
0013c028  DCT coefficient cancellation mode: %d (0: normal, 1: natural skip, 2: adaptive)
0013c079  search range: %d
0013c08a  Disable all intra modes in intra slices: %d(i.e., code macro-blocks in I slices as I_PCM).
0013c0e6  sBufSet.saCodedData[%d].iAddr:%016llx
0013c10d  sBufSet.saCodedData[%d].iSize:0x%x
0013c131  p_apscoded_dataHeader[%d]:%016llx
0013c154  sBufSet.saDPB[%d][0].iAddr:%016llx
0013c178  sBufSet.saEntropyCoding[%d][%d].saIBuf[AVE_BufIdx_Data].iAddr:%016llx
0013c1bf  p_apsSrcNbrInfo:%016llx
0013c1d8  p_apsSrcNbrPixels:%016llx
0013c1f3  p_apsSrcNbrData:%016llx
0013c20c  ----SPS----
0013c218  SPS profile_idc %d
0013c22b  SPS level_idc %d
0013c23c  SPS constraint_set0_flag %d
0013c258  SPS constraint_set1_flag %d
0013c274  SPS constraint_set2_flag %d
0013c290  SPS constraint_set3_flag %d
0013c2ac  SPS constraint_set4_flag %d
0013c2c8  SPS constraint_set5_flag %d
0013c2e4  SPS seq_parameter_set_id %d
0013c300  SPS chroma_format_idc %d
0013c319  SPS separate_colour_plane_flag %d
0013c33b  SPS bit_depth_luma_minus8 %d
0013c358  SPS bit_depth_chroma_minus8 %d
0013c377  SPS qpprime_y_zero_transform_bypass_flag %d
0013c3a3  SPS eScalingMatrixMode %d
0013c3bd  SPS log2_max_frame_num_minus4 %d
0013c3de  SPS pic_order_cnt_type %d
0013c3f8  SPS log2_max_pic_order_cnt_lsb_minus4 %d
0013c421  SPS iMaxNumRefFrames %d
0013c439  SPS gaps_in_frame_num_value_allowed_flag %d
0013c465  SPS pic_width_in_mbs_minus1 %d
0013c484  SPS pic_height_in_map_units_minus1 %d
0013c4aa  SPS frame_mbs_only_flag %d
0013c4c5  SPS direct_8x8_inference_flag %d
0013c4e6  SPS frame_cropping_flag %d
0013c501  SPS frame_crop_left_offset %d
0013c51f  SPS frame_crop_right_offset %d
0013c53e  SPS frame_crop_top_offset %d
0013c55b  SPS frame_crop_bottom_offset %d
0013c57b  ----VUI----
0013c587  SPS VUI.vui_parameters_present_flag %d
0013c5ae  SPS VUI.aspect_ratio_info_present_flag %d
0013c5d8  SPS VUI.overscan_info_present_flag %d
0013c5fe  SPS VUI.video_signal_type_present_flag %d
0013c628  SPS VUI.video_format %d
0013c640  SPS VUI.video_full_range_flag %d
0013c661  SPS VUI.colour_description_present_flag %d
0013c68c  SPS VUI.colour_primaries %d
0013c6a8  SPS VUI.transfer_characteristics %d
0013c6cc  SPS VUI.matrix_coefficients %d
0013c6eb  SPS VUI.timing_info_present_flag %d
0013c70f  SPS VUI.num_units_in_tick %d
0013c72c  SPS VUI.time_scale %d
0013c742  SPS VUI.fixed_frame_rate_flag %d
0013c763  SPS VUI.nal_hrd_parameters_present_flag %d
0013c78e  SPS VUI.vcl_hrd_parameters_present_flag %d
0013c7b9  SPS VUI.pic_struct_present_flag %d
0013c7dc  SPS VUI.bitstream_restriction_flag %d
0013c802  ----PPS----
0013c80e  PPSParams.seq_parameter_set_id %d
0013c830  PPSParams.entropy_coding_mode_flag %d
0013c856  PPSParams.bottom_field_pic_order_in_frame_present_flag %d
0013c890  PPSParams.num_slice_groups_minus1 %d
0013c8b5  PPSParams.num_ref_idx_l0_default_active_minus1 %d
0013c8e7  PPSParams.num_ref_idx_l1_default_active_minus1 %d
0013c919  PPSParams.weighted_pred_flag %d
0013c939  PPSParams.weighted_bipred_idc %d
0013c95a  PPSParams.pic_init_qp_minus26 %d
0013c97b  PPSParams.pic_init_qs_minus26 %d
0013c99c  PPSParams.chroma_qp_index_offset[%d] %d
0013c9c4  PPSParams.second_chroma_qp_index_offset[%d] %d
0013c9f3  PPSParams.deblocking_filter_control_present_flag %d
0013ca27  PPSParams.constrained_intra_pred_flag %d
0013ca50  PPSParams.redundant_pic_cnt_present_flag %d
0013ca7c  PPSParams.transform_8x8_mode_flag %d
0013caa1  PPSParams.pic_scaling_matrix_present_flag %d
0013cace  SHParams.nal_unit_type %d
0013cae9  SHParams.slice_type %d
0013cb01  SHParams.colour_plane_id %d
0013cb1e  SHParams.num_ref_idx_active_override_flag %d
0013cb4c  SHParams.num_ref_idx_l0_active_minus1 %d
0013cb76  SHParams.num_ref_idx_l1_active_minus1 %d
0013cba0  SHParams.no_output_of_prior_pics_flag %d
0013cbca  pInPicParams.sBufPFSet.sCodedData.iAddr %08x
0013cbf8  pInPicParams.sBufPFSet.sCodedHeader.iAddr[%d] %08x
0013cc2c  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_A].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cca4  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_B].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cd1c  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_A].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cd94  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_B].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013ce0c  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_A].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013ce86  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_B].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cf00  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_A].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cf7a  pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_B].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
0013cff4  pInPicParams.sBufPFSet.SrcNbrInfo %016llx
0013d01f  pInPicParams.sBufPFSet.SrcNbrPixels %016llx
0013d04c  ui16_I_MbCnt[%d] is %d
0013d064  ui16_Inter_MbCnt[%d] is %d
0013d080  ui32_InterSumSatd[%d] is %d
0013d09d  ui32_IntraSumSatd[%d] is %d
0013d0ba  ui16_Skipped_MbCnt[%d] is %d
0013d0d8  ui32_BestInterSumSatd is %d
0013d0f5  ui32_BestIntraSumSatd is %d
0013d112  ui32_InterNonSkippedSumSatd is %d
0013d135  ui32_QpyInter is %d
0013d14a  ui32_QpyIntra is %d
0013d15f  DebugStats
0013d16a  coded_data_hdr->sSliceInfo.iNum < AVE_SLICE_ACTIVE_MAX_NUM
0013d1c6  %s::%s:%d %p wrong entropy coding mode flag %d
0013d1f5  %s:%d %s | wrong scaling matrix mode %p %llu %d
0013d225  InitScalingListRegs
0013d239  sps.eScalingMatrixMode >= ScalingMatrixMode_Flat && sps.eScalingMatrixMode <= ScalingMatrixMode_ExplicitHighComp
0013d2aa  %s::%s:%d %s | scaling matrix mode not support %p %llu %d
0013d2e4  psSL != __null
0013d2f3  psSL->ScalingList4x4[0][i] >= 6
0013d313  psSL->ScalingList4x4[1][i] >= 6
0013d333  psSL->ScalingList4x4[2][i] >= 6
0013d353  psSL->ScalingList4x4[3][i] >= 6
0013d373  psSL->ScalingList4x4[4][i] >= 6
0013d393  psSL->ScalingList4x4[5][i] >= 6
0013d3b3  psSL->ScalingList8x8[0][i] >= 6
0013d3d3  psSL->ScalingList8x8[2][i] >= 6
0013d3f3  psSL->ScalingList8x8[4][i] >= 6
0013d413  psSL->ScalingList8x8[1][i] >= 6
0013d433  psSL->ScalingList8x8[3][i] >= 6
0013d453  psSL->ScalingList8x8[5][i] >= 6
0013d473  ProcessLRMERCStart
0013d486   + CAVEController::ProcessLRMERCStart, lrmeRCPassNum: %d
0013d4c0  SetLRMERC
0013d4ca  StartLRMERC
0013d4d6  ProcessLRMERCDone
0013d4e8  ManageDPB
0013d4f2  LUT: %d, %d, %d, %d, %d
0013d520  %s::%s:%d F %d sliceQp %d, avgVarFiltered %d avgVarIdx %d avgLuma %d avgLumaIdx %d iAdjQP %d reCenterQp %d qpModPosStr %d.%02d qpModNegStr %d.%02d minQp %d maxQp %d
0013d5c5  %s:%d %s | wrong parameters %p %d %p
0013d5ea  AVE_CreateSliceMapRows
0013d601  (psSliceMap != __null) && (eDevCapType >= 0) && (eDevCapType < AVE_DevCap_Type_Max) && (piSliceMapRows != __null)
0013d673  %s:%d %s | fail to get DevCap %p %d %p %d
0013d69d  pDevCap != __null
0013d6af  %s::%s Enter %p %p %p %d %d %d
0013d6e3  ./AppleAVE2FW/Legacy/CAVECommonController.cpp
0013d711  static_cast<int32_t>(clientBufferAvailableSize) >= static_cast<char*>(clientBuffer) - static_cast<char*>(clientBuffer_)
0013d789  %s::%s Exit %p %p %p %d %d %d
0013d7a7  ~CAVECommonController
0013d7bd  %s::%s Enter %d
0013d7d8  %s::%s Enter %p
0013d7ee  %s::%s Exit %p %d
0013d800  %s::%s Enter %p %d
0013d813  HMESCDone
0013d81d  %s::%s Exit %p %d %d
0013d832  LRMEDone
0013d83b  DMVDone
0013d843  LRMERCDone
0013d868  TranscodeError
0013d877  ProcessChipReset
0013d89e  GetFrameType
0013d8ab  RateControl Reset!!
0013d8bf  %s::%s Enter %zu
0013d8d0  CmdProcessor
0013d8dd  %s::%s:%d invalid encoding command %zu
0013d904  ProcessStop
0013d910  %s: CtxGo clear polled %u times
0013d930  get transcode error
0013d947  ProcessPixHistogram
0013d95b  %s::%s srcPicIdx %d wSum %d 
0013d978  count %d 
0013d982  imgDC %d 
0013d98c  normDC %d
0013d996  distortion >= 0
0013d9a6  searchHistogram
0013d9b6  depth == 8 || depth == 10
0013d9d0  scaleHistogram
0013d9df  wp->luma_log2_weight_denom <= 7
0013d9ff  finalizeWeightsSEs
0013da12  wp->chroma_log2_weight_denom <= 7
0013da34  SetPSContext
0013da41  %s::%s:%d no PSInfo
0013da55  %s::%s Enter %d %d %d
0013da80  %s::%s:%d Frame #%d idx[%d] LRME stats %d %d
0013daad  %s::%s Exit %d %d %d
0013dac2  CollectDataFromLrme
0013dad6  %s::%s:%d FrmNum %d frame_id (%d) coded_data_hdr 0x%llx, FT %d
0013db25  %s::%s:%d SadSumZero[%d], CostSum[%d]: %d, %d
0013db54  %s::%s:%d BinWeightedMVHrzSum[%d], BinWeightedMVVrtSum[%d], ZeroMVBinCnt[%d]: (%d, %d, %d)
0013dbb0  %s::%s:%d MotionHistPeaks[%d][%d]: (%d, %d) BinCount %d
0013dbff  %s::%s:%d %p unsupported encoder type %d
0013dc28  %s::%s:%d wrong coded data header %p
0013dc4d  %s::%s Exit %p
0013dc5c  %s::%s:%d: ResumableEncodingLA = %d - %d, %d, %d - %d, %d, %d
0013dc9a  InitRCParameters
0013dcab  %s::%s lookahead_frames=%d
0013dcc6  CreateRateControl
0013dcd8  %s::%s RCMode %d CRFScale %d
0013dcf5  %s::%s:%d invalid parameter
0013dd11  clientBufferAvailableSize >= m_numRCFrameStats * sizeof(*m_psRCFrameStats)
0013dd5c  clientBufferAvailableSize >= AVE_RateControl_sc_iMaxPlacementBufferSize
0013dda4  m_pcRC != NULL
0013ddc8  clientBufferAvailableSize >= sizeof(*hMctfCtrl) + CMCTFController::kClientBufferSize
0013de1d  MCTFController
0013de2c  AVE_WARN: MCTFController already created!!
0013de70  hMctfCtrl != NULL
0013de82  MCTF_GetPastCmdCounterInfo
0013de9d  MCTFModeHMESCDone
0013deaf  MCTFModeLRMEDone
0013dec0  MCTFModeLRMERCDone
0013ded3  MCTFModePipeDone
0013dee4  (iFwDataBufAddr != 0) && ((iFwDataBufAddr & 127) == 0)
0013df1b  PrepareROIFlags
0013df2b  %s::%s:%d ROI[%d]: 0 size
0013df45  %s::%s:%d ROI[%d]: (%d %d) (%d %d)
0013df68  EncCommParams.sANFDInfo.saEntry[i].sRect.iWidth > 0
0013df9c  EncCommParams.sANFDInfo.saEntry[i].sRect.iHeight > 0
0013dfd1  %s::%s:%d PIP[%d]: 0 size
0013dfeb  %s::%s:%d PIP[%d]: (%d %d) (%d %d)
0013e00e  EncCommParams.sPIPInfo.saEntry[i].sBBox.iWidth > 0
0013e041  EncCommParams.sPIPInfo.saEntry[i].sBBox.iHeight > 0
0013e075  %s::%s:%d PIPInMBs[%d]: (%d %d) (%d %d)
0013e09d  %s::%s:%d %lld FirstFrame %d
0013e0ba  setFirstFrame
0013e0c8  %s::%s:%d %lld frameInfo[%d].iFrameNum %d
0013e0f2  SetFrameNum
0013e0fe  MCTF PIODMA error:%d:[%d][%d] Dst: 0x%llx (Size:%d), Src: 0x%llx (Size:%d)
0013e149  %s:%d %lld %d | %d %d %d
0013e162  GetThroughputMode
0013e174  CandGen
0013e17c  SrcStats
0013e185  MeSetup
0013e18d  SrcRelay
0013e196  ModeDecison
0013e1a2  ReconChroma
0013e1be  iN > 0 && iN <= m_iCurSize
0013e1d9  FetchNthFrameInfo
0013e1eb  %s: Frame:%u (NF:%u) : %d -> %d
0013e20b  SetExecStage
0013e218  iFrmPosPlus1 > 0
0013e241  iLayerID < m_iNumViews
0013e272  %s:%d sROI: (%d %d) (%d %d)
0013e28e  SetROI
0013e295  %s:%d ROIInMBs: (%d %d) (%d %d)
0013e2b5  %s:%d ROIMark: 0x%01X 0x%01X 0x%01X 0x%01X
0013e2e0  %s:%d ROIInWUs: (%d %d) (%d %d)
0013e356  SetPIPCorner
0013e363  MaxPicOrderCntLsb %d
0013e378  hierarchicalMode %d
0013e38c  hevc_md5_lambda %d
0013e39f  hevc_bef_lambda %d
0013e3b2  lowerDeltaQpMode %d
0013e3c6  ultraFlatMbDeltaQP %d
0013e3dc  NULL video context!!!
0013e3f3  ui32Width: %d
0013e401  ui32Height: %d
0013e410  EnableSelStatsFlags: %d
0013e428  iBFrames: %d
0013e435  LowDelay: %d
0013e442  PerfFeature: 0x%x
0013e454  search_range: %d
0013e465  disable_skip_mode: %d
0013e47b  pix_pck: %d
0013e487  input_bitdepth: %d
0013e49a  iMaxNumRefFrames: %d
0013e4af  fCRFScale: %d.%03d
0013e4c2  iBitrate: %d
0013e4cf  iMaxKeyFrameInterval: %d
0013e4e8  iStrictKeyFrameInterval: %d
0013e504  iTotalFrameCnt: %d
0013e517  iExpectedFrameRate: %d
0013e52e  eRCMode: %d
0013e53a  AVE_QPMOD iFeature: 0x%x
0013e553  sLambdaMod.iFeature: 0x%x
0013e56d  RealTime: %d
0013e57a  pSessionCfg->sEnc.sAlgCfg.sGOP.iFeature 0x%x
0013e5a7  pSessionCfg->sEnc.sAlgCfg.sGOP.iaNumOfFrame[AVE_FrameType_B] %d
0013e5e7  LowDelay %d
0013e5f3  pSessionCfg->sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer %d
0013e629  pSessionCfg->sEnc.sAlgCfg.sGOP.iAdaptDelay %d
0013e657  RefSpacingP %d
0013e666  RefSpacingB0 %d
0013e676  RefSpacingB1 %d
0013e686  MaxPicOrderCntLsb N/A
0013e69c  SPSparams.sps_video_parameter_set_id %d
0013e6c4  SPSparams.sps_max_sub_layers_minus1 %d
0013e6eb  SPSparams.sps_seq_parameter_set_id %d
0013e711  SPSparams.chroma_format_idc %d
0013e730  SPSparams.PTL.eProfile %d
0013e74a  level %d
0013e753  SPSparams.separate_colour_plane_flag %d
0013e77b  SPSparams.pic_width_in_luma_samples %d
0013e7a2  SPSparams.pic_height_in_luma_samples %d
0013e7ca  SPSparams.picHeightInCtbsY %d
0013e7e8  SPSparams.picWidthInCtbsY %d
0013e805  SPSparams.ConfWindowParamsconformance_window_flag %d
0013e83a  SPSparams.ConfWindowParams.conf_win_left_offset %d
0013e86d  SPSparams.ConfWindowParams.conf_win_right_offset %d
0013e8a1  SPSparams.ConfWindowParams.conf_win_top_offset %d
0013e8d3  SPSparams.ConfWindowParams.conf_win_bottom_offset %d
0013e908  SPSparams.bit_depth_luma_minus8 %d
0013e92b  SPSparams.bit_depth_chroma_minus8 %d
0013e950  SPSparams.log2_max_pic_order_cnt_lsb_minus4 %d
0013e97f  SPSparams.sps_sub_layer_ordering_info_present_flag %d
0013e9b5  SPSparams.log2_min_luma_coding_block_size_minus3 %d
0013e9e9  SPSparams.sps_max_dec_pic_buffering_minus1[%d] %d
0013ea1b  sps_max_num_reorder_pics[%d] %d
0013ea3b  sps_max_latency_increase_plus1[%d] %d
0013ea61  SPSparams.log2_diff_max_min_luma_coding_block_size %d
0013ea97  SPSparams.log2_min_transform_block_size_minus2 %d
0013eac9  SPSparams.log2_diff_max_min_transform_block_size %d
0013eafd  SPSparams.max_transform_hierarchy_depth_inter %d
0013eb2e  SPSparams.max_transform_hierarchy_depth_intra %d
0013eb5f  SPSparams.scaling_list_enabled_flag %d
0013eb86  SPSparams.sps_scaling_list_data_present_flag %d
0013ebb6  SPSparams.amp_enabled_flag %d
0013ebd4  SPSparams.sample_adaptive_offset_enabled_flag %d
0013ec05  SPSparams.pcm_enabled_flag %d
0013ec23  SPSparams.pcm_sample_bit_depth_luma_minus1 %d
0013ec51  SPSparams.pcm_sample_bit_depth_chroma_minus1 %d
0013ec81  SPSparams.log2_min_pcm_luma_coding_block_size_minus3 %d
0013ecb9  SPSparams.log2_diff_max_min_pcm_luma_coding_block_size %d
0013ecf3  SPSparams.pcm_loop_filter_disabled_flag %d
0013ed1e  SPSparams.long_term_ref_pics_present_flag %d
0013ed4b  SPSparams.num_long_term_ref_pics_sps %d
0013ed73  SPSparams.lt_ref_pic_poc_lsb_sps[%d] %d
0013ed9b  used_by_curr_pic_lt_sps_flag[%d] %d
0013edbf  SPSparams.sps_temporal_mvp_enabled_flag %d
0013edea  SPSparams.strong_intra_smoothing_enabled_flag %d
0013ee1b  SPSparams.sps_extension_present_flag %d
0013ee43  SPSparams.iFWCreatesHeader %d
0013ee61  SPSparams.epc %d
0013ee73  ----VUI----
0013ee7f  SPSparams.sVUI.vui_parameters_present_flag %d
0013eead  SPSparams.sVUI.aspect_ratio_info_present_flag %d
0013eede  SPSparams.sVUI.aspect_ratio_idc %d
0013ef01  SPSparams.sVUI.sar_width %d
0013ef1d  SPSparams.sVUI.sar_height %d
0013ef3a  SPSparams.sVUI.overscan_info_present_flag %d
0013ef67  SPSparams.sVUI.video_signal_type_present_flag %d
0013ef98  SPSparams.sVUI.video_format %d
0013efb7  SPSparams.sVUI.video_full_range_flag %d
0013efdf  SPSparams.sVUI.colour_description_present_flag %d
0013f011  SPSparams.sVUI.colour_primaries %d
0013f034  SPSparams.sVUI.transfer_characteristics %d
0013f05f  SPSparams.sVUI.matrix_coeffs %d
0013f07f  SPSparams.sVUI.chroma_loc_info_present_flag %d
0013f0ae  SPSparams.sVUI.chroma_sample_loc_type_top_field %d
0013f0e1  SPSparams.sVUI.chroma_sample_loc_type_bottom_field %d
0013f117  SPSparams.sVUI.neutral_chroma_indication_flag %d
0013f148  SPSparams.sVUI.field_seq_flagg %d
0013f16a  SPSparams.sVUI.frame_field_info_present_flag %d
0013f19a  SPSparams.sVUI.default_display_window_flag %d
0013f1c8  SPSparams.sVUI.vui_timing_info_present_flag %d
0013f1f7  SPSparams.sVUI.bitstream_restriction_flag %d
0013f224  SPSparams.sVUI.tiles_fixed_structure_flag %d
0013f251  SPSparams.sVUI.motion_vectors_over_pic_boundaries_flag %d
0013f28b  SPSparams.sVUI.restricted_ref_pic_lists_flag %d
0013f2bb  SPSparams.sVUI.min_spatial_segmentation_idc %d
0013f2ea  SPSparams.sVUI.max_bytes_per_pic_denom %d
0013f314  SPSparams.sVUI.max_bits_per_min_cu_denom %d
0013f340  SPSparams.sVUI.log2_max_mv_length_horizontal %d
0013f370  SPSparams.sVUI.log2_max_mv_length_vertical %d
0013f39e  SPSparams.sVUI.default_display_window.def_disp_win_bottom_offset %d
0013f3e2  SPSparams.sVUI.default_display_window.def_disp_win_top_offset %d
0013f423  SPSparams.sVUI.default_display_window.def_disp_win_right_offset %d
0013f466  SPSparams.sVUI.default_display_window.def_disp_win_left_offset %d
0013f4a9  ----PPS----
0013f4b5  PPSParams.pps_pic_parameter_set_id %d
0013f4db  PPSParams.pps_seq_parameter_set_id %d
0013f501  PPSParams.dependent_slice_segments_enabled_flag %d
0013f534  PPSParams.output_flag_present_flag %d
0013f55a  PPSParams.num_extra_slice_header_bits %d
0013f583  PPSParams.sign_data_hiding_enabled_flag %d
0013f5ae  PPSParams.cabac_init_present_flag %d
0013f5d3  PPSParams.init_qp_minus26 %d
0013f5f0  PPSParams.transform_skip_enabled_flag %d
0013f619  PPSParams.cu_qp_delta_enabled_flag %d
0013f63f  PPSParams.diff_cu_qp_delta_depth %d
0013f663  PPSParams.pps_cb_qp_offset[%d] %d
0013f685  PPSParams.pps_cr_qp_offset[%d] %d
0013f6a7  PPSParams.pps_slice_chroma_qp_offsets_present_flag %d
0013f6dd  PPSParams.weighted_bipred_flag %d
0013f6ff  PPSParams.transquant_bypass_enabled_flag %d
0013f72b  PPSParams.tiles_enabled_flag %d
0013f74b  PPSParams.entropy_coding_sync_enabled_flag %d
0013f779  PPSParams.num_tile_columns_minus1 %d
0013f79e  PPSParams.num_tile_rows_minus1 %d
0013f7c0  PPSParams.uniform_spacing_flag %d
0013f7e2  PPSParams.loop_filter_across_tiles_enabled_flag %d
0013f815  PPSParams.pps_loop_filter_across_slices_enabled_flag %d
0013f84d  PPSParams.deblocking_filter_override_enabled_flag %d
0013f882  PPSParams.pps_deblocking_filter_disabled_flag %d
0013f8b3  PPSParams.pps_beta_offset_div2 %d
0013f8d5  PPSParams.pps_tc_offset_div2 %d
0013f8f5  PPSParams.pps_scaling_list_data_present_flag %d
0013f925  PPSParams.lists_modification_present_flag %d
0013f952  PPSParams.log2_parallel_merge_level_minus2 %d
0013f980  PPSParams.slice_segment_header_extension_present_flag %d
0013f9b9  PPSParams.pps_extension_flag %d
0013f9d9  PPSParams.pps_extension_6bits %d
0013f9fa  PPSParams.log2_max_transform_skip_block_size_minus2 %d
0013fa31  PPSParams.cross_component_prediction_enabled_flag %d
0013fa66  PPSParams.chroma_qp_offset_list_enabled_flag %d
0013fa96  PPSParams.diff_cu_chroma_qp_offset_depth %d
0013fac2  PPSParams.chroma_qp_offset_list_len_minus1 %d
0013faf0  PPSParams.log2_sao_offset_scale_luma %d
0013fb18  PPSParams.log2_sao_offset_scale_chroma %d
0013fb42  PPSParams.iFWCreatesHeader %d
0013fb60  PPSParams.epc %d
0013fb71  SHParams.first_slice_segment_in_pic_flag %d
0013fb9e  SHParams.slice_pic_parameter_set_id %d
0013fbc6  SHParams.dependent_slice_segment_flag %d
0013fbf0  SHParams.slice_segment_address %d
0013fc13  SHParams.pic_output_flag %d
0013fc30  SHParams.slice_pic_order_cnt_lsb %d
0013fc55  SHParams.short_term_ref_pic_set_sps_flag %d
0013fc82  SHParams.short_term_ref_pic_set_idx %d
0013fcaa  SHParams.num_long_term_sps %d
0013fcc9  SHParams.num_long_term_pics %d
0013fce9  SHParams.lt_idx_sps[%d] %d
0013fd05  SHParams.poc_lsb_lt[%d] %d
0013fd21  SHParams.used_by_curr_pic_lt_flag[%d] %d
0013fd4b  SHParams.delta_poc_msb_present_flag[%d] %d
0013fd77  SHParams.delta_poc_msb_cycle_lt[%d] %d
0013fd9f  SHParams.slice_temporal_mvp_enabled_flag %d
0013fdcc  SHParams.slice_sao_luma_flag %d
0013fded  SHParams.slice_sao_chroma_flag %d
0013fe10  SHParams.ref_pic_list_mod.ref_pic_list_modification_flag_l0 %d
0013fe50  SHParams.ref_pic_list_mod.list_entry_l0[%d] %d
0013fe80  SHParams.ref_pic_list_mod.ref_pic_list_modification_flag_l1 %d
0013fec0  SHParams.ref_pic_list_mod.list_entry_l1[%d] %d
0013fef0  SHParams.mvd_l1_zero_flag %d
0013ff0e  SHParams.cabac_init_flag %d
0013ff2b  SHParams.collocated_from_l0_flag %d
0013ff50  SHParams.collocated_ref_idx %d
0013ff70  SHParams.wp.luma_log2_weight_denom %d
0013ff97  SHParams.wp.chroma_log2_weight_denom %d
0013ffc0  SHParams.wp.delta_chroma_log2_weight_denom %d
0013ffef  ----RPS----
0013fffc  ----RPS SHORT TERM----
00140014  RPSparams.strps.num_short_term_ref_pic_sets  %d
00140045  RPSparams.strps.rps[%d].inter_ref_pic_set_prediction_flag %d
00140083  RPSparams.strps.rps[%d].delta_idx_minus1 %d
001400b0  RPSparams.strps.rps[%d].delta_rps_sign  %d
001400dc  RPSparams.strps.rps[%d].abs_delta_rps_minus1  %d
0014010e  RPSparams.strps.rps[%d].num_negative_pics  %d
0014013d  RPSparams.strps.rps[%d].num_positive_pics  %d
0014016c  RPSparams.strps.rps[%d].NumNegativePics  %d
00140199  RPSparams.strps.rps[%d].NumPositivePics  %d
001401c6  RPSparams.strps.rps[%d].NumDeltaPocs  %d
001401f0  RPSparams.strps.rps[%d].used_by_curr_pic_flag[%d]  %hhu
00140229  RPSparams.strps.rps[%d].use_delta_flag[%d]  %hhu
0014025b  RPSparams.strps.rps[%d].delta_poc_s0_minus1[%d]  %d
00140290  RPSparams.strps.rps[%d].used_by_curr_pic_s0_flag[%d]  %hhu
001402cc  RPSparams.strps.rps[%d].delta_poc_s1_minus1[%d]  %d
00140301  RPSparams.strps.rps[%d].UsedByCurrPicS0[%d]  %hhu
00140334  RPSparams.strps.rps[%d].used_by_curr_pic_s1_flag[%d]  %hhu
00140370  RPSparams.strps.rps[%d].UsedByCurrPicS1[%d]  %hhu
001403a3  RPSparams.strps.rps[%d].DeltaPocS0[%d]  %d
001403cf  RPSparams.strps.rps[%d].DeltaPocS1[%d]  %d
001403fb  ----RPS LONG TERM----
00140412  RPSparams.ltrpslong_term_ref_pics_present_flag  %d
00140446  RPSparams.num_long_term_ref_pics_sps  %d
00140470  RPSparams.ltrps.lt_ref_pic_poc_lsb_sps[%d] %d
0014049f  used_by_curr_pic_lt_sps_flag[%d] %d
001404c4  pInPicParams.sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data] %016llx
0014051c  pInPicParams.sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data] %016llx
00140576  pInPicParams.sRecon.Colocated %016llx
0014059d  pInPicParams.sBufPFSet.sRefColocated %016llx
001405cb  cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx
00140612  pInPicParams.sBufPFSet.sSrcNbrData %016llx
0014063e  sBufPFSet.saEntropyCoding[%d][%d]:%016llx
00140669  ./AppleAVE2FW/Legacy/CDebugPrints.cpp
0014068f  coded_data_hdr->sSliceInfo.iNum
001406af  %s: CtxGo is still Busy (0x%x)!
001406cf  %s: Everything is not yet idle(0x%x)!
0014074e  HW_BLOCK: FwWr | FwRv | FwRd | FwTr | HwWr | HwRd | FwRdy | FwDm      | WuGo | CfgCnt | PendWus
00140808  CGen:      %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140858  CGen:      %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
001408a7  SStats:    %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
001408f7  SStats:    %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140946  MESetup:   %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140996  MESetup:   %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
001409e5  SRelay:    %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140a35  SRelay:    %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140a84  ModDec:    %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140ad4  ModDec:    %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140b23  Rcr:       %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140b73  Rcr:       %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140bc2  DbLf:      %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140c12  DbLf:      %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140c61  Vlc:       %4d | %4d | %4d | %4d | %4d | %4d | %4d | 0x%08x | %4d |  %4d  | %4d
00140cb1  Vlc:       %4d | %4d | 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x
00140d00      HW_BLOCK: A     NumWus    FwRecvd       FwRd     FwInTr       HwTr       HwWr    InFwCfg
00140d91      HW_BLOCK: A     NumWus    FwRecvd       FwRd       HwRd       HwTr       HwWr    D F E C/CfgCnt
00140e2a  REG_READ(0x):               EmemCfg       FwDm                  WuGo                     
00140eb5  CHEVCController
00140ec7  ./AppleAVE2FW/Legacy/CDMAController.cpp
00140eef  4<=iPicWidth/16 && iPicWidth/16<=1024
00140f15  ConfigHMESCRdDMA
00140f26  4<=iPicHeight/16 && iPicHeight/16<=1024
00140f4e  ((iCtxInitRow*16)&(128-1)) == 0
00140f6e  iCtxInitRow/(128/16) <= 127
00140f8a  1<=val && val<=128
00140f9d  1<=val&& val<=128
00140faf  1<=iSrcPicWidth && iSrcPicWidth<=65536
00140fd6  1<=iSrcPicHeight && iSrcPicHeight<=65536
00140fff  addr != 0
00141009  (addr&(64-1)) == 0
0014101c  (val&(64-1)) == 0
0014102e  m_psEncCommParams->padding_value_luma <= ((1<<m_psEncCommParams->input_bitdepth)-1)
00141082  val <= ((1<<m_psEncCommParams->input_bitdepth)-1)
001410b4  cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0
001410f9  (cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr&(128-1)) == 0
00141148  (addr&(128-1)) == 0
0014115c  1<=m_psEncCommParams->width && m_psEncCommParams->width<=65536
0014119b  1<=m_psEncCommParams->height && m_psEncCommParams->height<=65536
001411dc  COFController
001411ea  ./AppleAVE2FW/Legacy/COFController.cpp
00141211  pClientBuffer != NULL
00141227  iClientBufferAvailableSize >= kClientBufferSize
00141257  %s::%s: pOFInitCmd is NULL
00141272  %s::%s: pInitParams is NULL
0014128e  EncCommParams.pEventTraceBuffer
001412ae  EncCommParams.chroma_format <= EncCommParams.input_chroma_format
001412ef  EncCommParams.low_res_pipe_sync_mode
00141314  m_psLRMEFSSequeneceInits
0014132d  m_psLRMEFSFrameInits
00141342  m_psLRMERSSequeneceInits
0014135b  m_psLRMERSFrameInits
001413ce  %s::%s Enter %p, %d-%d-%d
001413e8  AcquireBuffers
001413f7  %s::%s: Enter, %d-%d-%d
0014140f  ConfigHMESCDMALuma
00141422  L: HMESCSRCPIXRD_CTXCFG_SRCADDR = 0x%llx
0014144b  iAddr != 0
00141456  (iAddr & (64 - 1)) == 0
0014146e  L: HMESCSRCPIXRD_CTXCFG_STRIDE = %d, compressedIN = %d
001414a5  (iVal & (64 - 1)) == 0
001414bc  (cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr & (128 - 1)) == 0
0014150f  L: HMEDMA_SPRHME_RMACMPCHANNELCFG_HDRADDR = 0x%llx
00141542  cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0
00141585  (cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & (128 - 1)) == 0
001415d6  L: HMEDMA_SPRHME_RMACMPCHANNELCFG_CMPADDR = 0x%llx
00141609  L: HMEDMA_SPRHME_RMACMPCHANNELCFG_STRIDE = %d
00141637  L: HMESRCPIXRDAGU_SRCAGU_STRIDE = %d
0014165c  pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0
001416b9  (pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr & (128 - 1)) == 0
00141724  L: HMEDMA_HMESC_WMACMPCHANNELCFG_HDRADDRLOW[%d] = 0x%llx
0014175d  pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0
001417b8  (pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & (128 - 1)) == 0
00141821  L: HMEDMA_HMESC_WMACMPCHANNELCFG_CMPADDRLOW[%d] = 0x%llx
0014185a  L: HMEDMA_HMESC_WMACMPCHANNELCFG_STRIDE(%d) = %d
0014188b  ProcessHMESCStart
0014189d  StartHMESC
001418a8  HMESCAlgorithmSetup
001418bc  ProcessHMESCDone
001418cd  %s::%s Enter, frame ID = %d
001418e9  ProcessLrmeResults
001418fc  %s::%s Enter, Frame ID = %d
00141918  %s::%s Enter %p %d %d
0014192e  CDMVController
0014193d  ./AppleAVE2FW/Legacy/CDMVController.cpp
00141965  %s::%s exit
00141971  %s::%s:%d NULL video context
0014198e  ProcessDMVDone
0014199d  ProcessDMVStart
001419cd  %s::%s EXIT
001419d9  StartDMV
001419e2  %s: iRSPass = %d, iTraversalMode = %d, iReverseOrder =%d
00141a37  %s: iRefIdx = %d
00141a5f  ./AppleAVE2FW/Legacy/CHEVCControllerCommon.cpp
00141a8e  %s::%s:%d MaxKeyFrameInterval %d FrameRate %d MaxKeyFrameIntervalDuration %f
00141adb  %s::%s:%d RC framerate %s%lld.%02lld
00141b02  %s::%s Enter %d %p
00141b15  program_sh_rps_for_ltref
00141b2e  cur_sh_rps->num_negative_pics > 0 || cur_sh_rps->num_positive_pics > 0
00141b75  %s::%s Exit %d %p
00141b87  %s::%s Enter %d %p %d
00141b9d  program_sh_rps_hierarchical
00141bb9  %s::%s:%d %llu F %d POC %d numTemporalLayers %d cur_temporalId %d max_ref_pic_temporalId %d %d %d
00141c1b  %s::%s:%d %llu F %d POC %d ref_poc %d
00141c41  Update last CRA POC %d
00141c59  %s::%s:%d %llu F %d Type %d POC %d | %d %d | %d %hhu %d %hhu
00141c96  %d | %d %d | %d %d | %hhu %d %hhu %d 
00141cbc  %s::%s:%d  %llu F %d Type %d POC %d | %d %d | S0 %d %hhu %d %hhu | S1 %d %hhu
00141d0a  %d %d %d %d %d %d %d %hhu %d %hhu %d %hhu 
00141d35  %s::%s Exit %d %p %d
00141d4a  ptr->inter_ref_pic_set_prediction_flag == 0
00141d76  update_sps_rps_internal_variables
00141d98  %s::%s:%d NumNegativePics %d, NumPositivePics %d
00141dc9  %s::%s:%d ptr->UsedByCurrPicS0[%d] %hhu
00141df1  %s::%s:%d NumPocStCurrBefore %d NumPocStFoll %d NumPocStCurrAfter %d
00141e36  %s::%s:%d %d PocStCurrBefore %d PocStFoll %d
00141e63  %s::%s:%d %d PocStCurrAfter %d
00141e82  pPicParams != NULL && cPicMgmtParams.IsCompressed()
00141eb6  %s::%s Enter GOP_M %d iLayerID %d frame_num %d last_idr_display_order %d
00141eff  SetRpsVars
00141f0a  calc_rps
00141f13  %s::%s:%d NumPicTotalCurr %d EncCommParams.iLayerIdx %d
00141f4b  %s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS0 %hhu DeltaPocS0 %d
00141f8f  %s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS1 %hhu DeltaPocS1 %d
00141fd3  %s::%s:%d pPicParams->sFrameInfo.iLayerID %d
00142000  %s::%s:%d ROIDebug EncCommParams sRect i (iX, iY, iWidth, iHeight): %d %d %d %d %d
00142053  %s::%s:%d ROIDebug pPicParams sRect i (iX, iY, iWidth, iHeight, iBase): %d %d %d %d %d %d
001420ad  %s::%s:%d ROIDebug EncCommParams sANFDRect_blk i (iConfidence, iRoll, iYaw): %d %d %d %d
00142106  %s::%s:%d PIP sRect (%d, %d, %dx%d)
0014212a  %s::%s:%d pPicParams->sFrameInfo.PicOrderCntVal %d
0014215d  %s::%s:%d %llu F %d %d %d %d
0014218d  %s::%s:%d IBDebug GOP_M %d ibPeriod %d ibStartIdx %d ibSampleTwo %d ibSampleThree %d
001421e2  %s::%s:%d fid:%d fnum:%d fDr:%d qp:%d var %llu
00142211  %s::%s:%d fr %d slice_type %d, qp_val %d, slice_cb/cr_present %d slice_qp_delta %d slice_cb/cr_qp %d %d pps_cb/cr_qp %d %d
0014228c  ProcessPipeDone currMbRow %d pic_height_in_mbs %d frame_done %d
001422cd  %s::%s:%d updateRateControl EncodeOrder %d
001422f8  %s::%s:%d Encoder %lld frame_num %d size %d
00142325  %s::%s:%d currMbRow %d pic_height_in_mbs %d frame_done %d
00142360  %s::%s:%d bitstream size overflow, buffer size: %d, bitstream size: %d
001423a7  %s::%s:%d bitsFromTranscode %d frame num %d thisslicelen %d
001423e3  %s::%s:%d xcode Done curr_slice_number %d
0014240d  nextCoef == ScalingList[i]
00142428  nextCoef >= 6 && nextCoef <= 255
00142464  hevc_pps->scaling_list_data.scaling_list_delta_coef[sizeId][matrixId][i] >= -128 && hevc_pps->scaling_list_data.scaling_list_delta_coef[sizeId][matrixId][i] <= 127
00142508  %s::%s:%d clipCropDebug: spsWidthHeight %d,%d spsCropRightBottom %d,%d validMBWidthHeight %d,%d originalMBWidthHeight %d,%d
00142584  GetPicCropInfoFlag
00142597  [PERF] XXXX client[%llu] EncCommParams.pFwProfile %p
001425cd  (pSessionCfg->iHwFeature & AVE_HW_FEATURE_LRME_PIPE_SYNC) == 0
0014260c  %s:%s EncCommParams.use_CAVLC_bits %d RCiFeature %llu, CommiFeature %llu
00142655  (EncCommParams.width <= HEVC_STILL_IMAGE_MAX_WIDTH) && (EncCommParams.height <= HEVC_STILL_IMAGE_MAX_HEIGHT)
001426c2  EncCommParams.height <= HEVC_STILL_IMAGE_MAX_WIDTH
001426f5  %s::%s:%d MCTF LFSRef buffers num %d
0014271a  clientBufferAvailableSize >= sizeof(*hRateControl[i])
00142750  %s::%s:%d Try to enable segment encoding but has no enough frames: %d
00142796  %s::%s:%d sAlgCfg.sGOP.iFeature 0x%x, numTemporalLayers %d
001427d1  clientBufferAvailableSize >= sizeof(H265VideoEncoderDPB)
0014280a  %s::%s:%d Failed to initialize DPB %d
00142830  %s::%s:%d eWorkType %d FW creates header %d %d
0014285f  %s::%s:%d invalid sps and pps iFWCreatesHeader %d %d %d
00142897  %s::%s:%d PPS Info: %d, %d, %d
001428b6  %s::%s:%d clientID %llu pps Num %d header %d bits %d bytes i %d PPS ID %d numView %d
0014290b  %s::%s:%d clientID %llu PPS count %d PS num %d View num %d
00142946  %s::%s:%d clientID %llu pps Num %d header %d bits %d bytes i %d PPS ID %d PPS count %d
0014299d  %s::%s:%d clientID %llu PSInfo num %d
001429c3  %s::%s:%d clientID %llu idx %d eType %d iLayerID %d iOffset %d iSize %d
00142a0b  %s::%s:%d clientID %llu pInitParams->sPSInfo.iNum %d header [%d] eType %d iLayerID %d iOffset %d iSize %d
00142a75  %s::%s:%d No PS available %d %d %d
00142a98  %s::%s:%d total PS bits %d
00142ab3  %s::%s Exit %p %p %d
00142ac8  SetTranscodeCommon
00142adb  %s::%s:%d SQPMod: F %d SliceType %d qp %d prevqp %d LowerDeltaQP %d totalLowQPMB %d totalLowQPMBHasCBP %d
00142b45  nRemWords <= BITMAP_BLOCK_BUF_SIZE_IN_WORDS
00142b71  (Write cbp0 flag) F %d, sliceType %d  VTId %d 
00142ba1  %s::%s AccCbp0Cnts: F %d, Mode %d, IB %d %d %d; cbpReset %d, %d; LowerDeltaQP %d %d totalLowQPMB %d
00142c05  FLLB (accumCbp0Cnts) %d
00142c1d  slice %d: I %d P %d S %d Sad %d %d B %d
00142c46  %d VarSum %llu VarMax %d VarMin %d
00142c69  %s::%s:%d pipe_context_id %d coded_data_hdr %p
00142cae  %s::%s:%d !slice_strps.short_term_ref_pic_set_sps_flag %d
00142ce8  cRPS.CurrRpsIdx %d
00142cfb  %s::%s:%d NumPicTotalCurr %d nuh_layer_id %d
00142d28  shPos < AVE_SLICE_ACTIVE_MAX_NUM
00142d49  %s::%s:%d %s | No slice header buffer! %p %d
00142d76  EncCommParams.sSliceHeader.iAddr != 0
00142d9c  %s::%s:%d %s | No enough memory for slice header! %p %d %d %d
00142dda  (uint32_t)psSliceOffsetBuf[AVE_BufIdx_Header].iOffset + (((1152) + (32) - 1) & ~((32) - 1)) <= (uint32_t)EncCommParams.sSliceHeader.iSize
00142e64  %s::%s:%d Row: %d, numEntryPointOffsets: %d offset_len_minus1 %d
00142ea6  %s::%s:%d slice bytes: %d
00142ec0  %s::%s:%d copy slice header %d to 0x%08llx size %d
00142ef4  %s::%s:%d transcode_context_id %d coded_data_hdr %p
00142f28  slice count %d
00142f38  size count %d
00142f47  refIdxRc %d rcPass %d frame_done %d
00142f6b  %s::%s:%d Jnd (%d, %d), minQp %d maxQp %d
00142f95  %s::%s:%d PIP QP %d 0x%x
00142fae  SAQPMod: iLowerDeltaQP %d, iMaxLowerDeltaQP %d!
00142fde  %s:%d %s | wrong parameters %p
00142ffd  %s::%s:%d F %d ratio_PB %s%lld.%02lld P_cnt %d B_cnt %d max_delta_qp %d
00143045  GetMaxLowerDeltaQP
00143058  %s::%s:%d F %d final_max_delta_qp %d
0014307d  (Read cbp0 flag) F %d  %d accumCbp0Cnts %d  sliceType %d  VTId %d
001430c0  %s::%s:%d F %d qp %d prevqp %d LowerDeltaQP %d totalLowQPMB %d meMem.extra.LowerDeltaQP %d meMem.extra.maxLowerDeltaQP %d IsThisFrameMarkedAsNonReference=%d
00143172  %s::%s F %d LowerDeltaQPMode %d, ApplyStaticAreaQP %d
001431a8  ProcessPipeReset
001431b9   - CAVCommonController::ProcessPipeReset
001431e3  setLRME
001431eb  ./AppleAVE2FW/Legacy/CAVCController_H18.cpp
00143217  l0_ref_num = %d, l1_ref_num = %d
00143239  m_iHMEFSRefNum <= 2
0014324d  %s::%s:%d F %d QPMod range [%d, %d]
00143272  calcQpModRange
00143281  Frame #%d: prevFrameSumOfVariance %d avgVar %d from driver
001432bd  %s::%s:%d BITBOX frame %d | estimateAvgVar: pre_avgVar: %d avgVarEstimated: %d
0014330c  calcAvgVar
00143317  %s (H18)::%s Enter
0014332a  ConfigureMCPUs
00143339  EncCommParams.use_mcpus
00143351  setPipe
0014335d  EncCommParams.enc_type == AVE_EncType_AVC
00143387  EncCommParams.depth == 8
001433a0  8<=EncCommParams.pic_width_in_mbs && EncCommParams.pic_width_in_mbs<=512
001433e9  4<=EncCommParams.pic_height_in_mbs && EncCommParams.pic_height_in_mbs<=512
00143434  64<=adjusted_context_height_in_mbs*16 && adjusted_context_height_in_mbs*16<=8192
00143485  ((EncCommParams.encode_row_init*16)&(64-1)) == 0
001434b6  1<=EncCommParams.width && EncCommParams.width<=65536
001434eb  1<=EncCommParams.height && EncCommParams.height<=65536
00143522  EncCommParams.input_bitdepth==8 || EncCommParams.input_bitdepth==10 || EncCommParams.input_bitdepth==12
0014358a  EncCommParams.ref_compress
001435a5  -12<=pps.chroma_qp_index_offset[EncCommParams.slicePPSIdIdx] && pps.chroma_qp_index_offset[EncCommParams.slicePPSIdIdx]<=12
00143621  -12<=pps.second_chroma_qp_index_offset[EncCommParams.slicePPSIdIdx] && pps.second_chroma_qp_index_offset[EncCommParams.slicePPSIdIdx]<=12
001436ab  EncCommParams.padding_value_luma <= ((1<<EncCommParams.input_bitdepth)-1)
001436f5  val <= ((1<<EncCommParams.input_bitdepth)-1)
00143722  cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr != 0
00143769  (cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr&(128-1)) == 0
001437ba  EncCommParams.encoder_addr_src_nbr_pixels != 0
001437e9  (EncCommParams.encoder_addr_src_nbr_pixels&(64-1)) == 0
00143821  (EncCommParams.bfrSizeNbrPixels&(64-1)) == 0
0014384e  EncCommParams.encoder_addr_dst_nbr_info != 0
0014387b  (EncCommParams.encoder_addr_dst_nbr_info&(64-1)) == 0
001438b1  (EncCommParams.bfrSizeNbrInfo&(64-1)) == 0
001438dc  EncCommParams.encoder_addr_dst_nbr_pixels != 0
0014390b  (EncCommParams.encoder_addr_dst_nbr_pixels&(64-1)) == 0
00143943  pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0
0014399e  (pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr&(128-1)) == 0
00143a03  pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0
00143a5c  (pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr&(128-1)) == 0
00143abf  val <= 65536
00143acc  pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr != 0
00143b29  (pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr&(128-1)) == 0
00143b90  pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr != 0
00143beb  (pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr&(128-1)) == 0
00143c50  EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr != 0
00143cb7  (EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr&(64-1)) == 0
00143d27  EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize != 0
00143d8e  (EncCommParams.encoder_addr_entropy[i][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize&(64-1)) == 0
00143dfe  EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Header].iAddr != 0
00143e67  (EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Header].iAddr&(64-1)) == 0
00143ed9  %s::%s Enter 
00143ee7  setHMESC
00143ef0  ((EncCommParams.encode_row_init*16)&(128-1)) == 0
00143f22  EncCommParams.encode_row_init/(128/16) <= 127
00143f50  1<=AVE_ALIGN_UP(EncCommParams.pic_width_in_mbs, 128/16)/(128/16) && AVE_ALIGN_UP(EncCommParams.pic_width_in_mbs, 128/16)/(128/16)<=128
00143fd7  1<=AVE_ALIGN_UP(adjusted_context_height_in_mbs, 128/16)/(128/16) && AVE_ALIGN_UP(adjusted_context_height_in_mbs, 128/16)/(128/16)<=128
0014405e  4<=EncCommParams.pic_width_in_mbs*16/4 && EncCommParams.pic_width_in_mbs*16/4<=4096
001440b2  4<=EncCommParams.pic_height_in_mbs*16/4 && EncCommParams.pic_height_in_mbs*16/4<=4096
00144108  (pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr&(128-1)) == 0
0014416f  (pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr&(128-1)) == 0
001441d4  (AVE_HMESCWR_PLANE_LUMA_WDT(EncCommParams.width, 2)) <= 65536
00144212  AVE_HMESCWR_PLANE_LUMA_HGT(EncCommParams.height, 2) <= 65536
0014424f  %s::%s Exit 
00144271  %s::%s:%d %s | wrong parameter
00144290  psEncCmd != __null
001442a3  SetLRMERCPerRef
001442b3  SetLRMERCPerPass
001442c4  setLRME EncCommParams.context_height_in_mb = %d 
001442f6  %s::%s:%d WorkType %d FrameType %d QP %d searchRange %d iLambda %d
00144339  ./AppleAVE2FW/Legacy/CHEVCController_H18.cpp
00144366  l0_ref_num == 1
00144376  l1_ref_num == 0
00144386  %s::%s:%d %d Frame %d: Overflow %d qpModLevel %d
001443b7  AVE_RC_FEATURE_LOW_BITRATE_STREAMING: normalized_bpp %d.%02d, minNegativeRange %d
0014440a  %s::%s:%d F %d QPMod level %d, range [%d, %d]
00144439  %s::%s (H18) Enter
0014444c  MCPU CBP0 Setting: %d
00144466  EncCommParams.slicePPSIdIdx < AVE_PPS_MAX_NUM
00144494  EncCommParams.enc_type == AVE_EncType_HEVC
001444bf  EncCommParams.depth==8 || EncCommParams.depth==10
001444f1  AVE_ALIGN_UP(EncCommParams.width, 64) >= 128
0014451e  adjusted_context_height_in_mbs*16 >= 64
00144546  8<=EncCommParams.width/16 && EncCommParams.width/16<=4095
00144580  4<=EncCommParams.height/16 && EncCommParams.height/16<=4095
001445bc  0<=EncCommParams.pic_width_in_mbs && EncCommParams.pic_width_in_mbs<=4096
00144606  0<=adjusted_context_height_in_mbs && adjusted_context_height_in_mbs<=4096
00144650  %s::%s: RdColo: %d, WrColo: %d, %d-%d-%d, 0x%llx-0x%llx
00144688  F %d, Slice %d Reset %d Apply %d
001446a9  (EncCommParams.ePixelConvType >= AVE_PixelConvType_None) && (EncCommParams.ePixelConvType <= AVE_PixelConvType_Custom)
00144720  paScalingList != NULL
00144736  paScalingList[0] != NULL
0014474f  paScalingList[3] != NULL
00144768  paScalingList[1] != NULL
00144781  paScalingList[2] != NULL
0014479a  paScalingList[4] != NULL
001447b3  paScalingList[5] != NULL
001447cc  EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr != 0
00144833  (EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr & (64 - 1)) == 0
001448a7  EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize != 0
0014490e  (EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iSize & (64 - 1)) == 0
00144982  (EncCommParams.encoder_addr_entropy[0][EncCommParams.pipe_buffer_id].saIBuf[AVE_BufIdx_Data].iAddr&(64-1)) == 0
001449f2  l0_ref_num = %d, l1_ref_num = %d
00144a13  setHMESC EncCommParams.context_height_in_mb = %d 
00144a46  1<=AVE_ALIGN_UP(iPicWidth, 128)/128 && AVE_ALIGN_UP(iPicWidth, 128)/128<=128
00144a93  1<=AVE_ALIGN_UP(iCtxHeight, 128/16)/(128/16) && AVE_ALIGN_UP(iCtxHeight, 128/16)/(128/16)<=128
00144af2  4<=iPicWidth/4 && iPicWidth/4<=4096
00144b16  4<=iPicHeight/4 && iPicHeight/4<=4096
00144b3c  AVE_HMESCWR_PLANE_LUMA_WDT(iPicWidth, iLevel) <= 65536
00144b73  PopFront MCTF %d %d %d %d
00144b8d  ./AppleAVE2FW/Legacy/CMCTFControllerCommon.cpp
00144bbc  pcRefFrameInfo->m_bIsCompressInput || pcRefFrameInfo->GetExecStage() >= MCTF_Stage_Scaled
00144c16  GetRefCompInfo
00144c25  MCTF PIODMA error:%d:[%d][%d] Dst: 0x%llx (Size:%d), Src: 0x%llx (Size:%d) CopySize:%u
00144c7c  Applying gating for frame: %d
00144c9a  %s::%s:%d %p bufIdx %u AvgMvX = %d, AvgMvY = %d
00144ce1  %s::%s:%d %p bufIdx %u AvgSADY = %d AvgSADUV = %d
00144d13   FS Stats F %d-%d-%d; V %d-%d-%d; APL: %d-%d-%d
00144d43   Pipe Stats F %d-%d; V %d-%d; APL: %d-%d, G:%u
00144d72  PopFront() when MctfFrameQueue is empty!
00144d9b  PopFront() for a frame in stage : %d expected to be in Output
00144dd9  m_iNumFilteredFramesAtHead
00144df4  PopFront
00144dfd  m_iNumFilteredFramesAtHead == 0
00144e1d  PopFront: F %d Q state %d, %d, %d
00144e3f  CMCTFController
00144e4f  %s Constructor!!
00144e60  ./AppleAVE2FW/Legacy/CMCTFController_H18.cpp
00144e8d  +ProcessInit
00144e9a  eMCTFMode %d, UserParams %d
00144eb6  MCTF InitSession:Latency Mode:%d, Num next refs:%d (Cfg:%d), RampUp:%d
00144efd  MCTF Params: %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d
00144f40  Resolution %d, %d
00144f52  ERR: MCTF mode doesn't support Scaled Source for LRME
00144f88  cPicMgmtParams.GetScaledPlaneBuf(AVE_BufIdx_Luma).saIBuf[AVE_BufIdx_Data].iAddr == 0
00144fdd  EnqueueFrames
00144feb  (cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0
00145035  cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr != 0
0014507a  (cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0
001450c6  Strides: %d, %d
001450d6  (%d)COMP_SRC: 0x%llx, 0x%llx, 0x%llx, 0x%llx
00145103  %s::%s:%d Frame %d. num next refs: %d
00145129  1<=val && val<=255
0014513c  1<=val&& val<=255
0014514e  m_psEncCommParams->iaMCTFCompressedSrcLumaHdrAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM] != 0
001451b0  (m_psEncCommParams->iaMCTFCompressedSrcLumaHdrAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM]&(128-1)) == 0
0014521c  m_psEncCommParams->iaMCTFCompressedSrcLumaCmpAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM] != 0
0014527e  (m_psEncCommParams->iaMCTFCompressedSrcLumaCmpAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM]&(128-1)) == 0
001452ea  (%d)HME_L0_L: 0x%llx, 0x%llx
00145307  (m_psEncCommParams->iMCTFCompressedSrcLumaStride&(64-1)) == 0
00145345  m_psEncCommParams->iMCTFCompressedSrcLumaWidth <= 65536
0014537d  m_psEncCommParams->iMCTFCompressedSrcLumaHeight <= 65536
001453b6  m_psEncCommParams->mctf_LowResHdr[iBufIdx] != 0
001453e6  (m_psEncCommParams->mctf_LowResHdr[iBufIdx]&(128-1)) == 0
00145420  m_psEncCommParams->mctf_LowResBuffer[iBufIdx] != 0
00145453  (m_psEncCommParams->mctf_LowResBuffer[iBufIdx]&(128-1)) == 0
00145490  AVE_HMESCWR_PLANE_LUMA_WDT(m_psEncCommParams->width, 2) <= 65536
001454d1  AVE_HMESCWR_PLANE_LUMA_HGT(m_psEncCommParams->height, 2) <= 65536
00145528  m_psEncCommParams->iaMCTFCompressedSrcChromaHdrAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM]!= 0
0014558b  (m_psEncCommParams->iaMCTFCompressedSrcChromaHdrAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM]&(128-1)) == 0
001455f9  m_psEncCommParams->iaMCTFCompressedSrcChromaCmpAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM] != 0
0014565d  (m_psEncCommParams->iaMCTFCompressedSrcChromaCmpAddr[iScalerFrameNum % AVE_MCTF_HME_L0_BUF_NUM]&(128-1)) == 0
001456cb  (%d)HME_L0_C: 0x%llx, 0x%llx
001456e8  (m_psEncCommParams->iMCTFCompressedSrcChromaStride&(64-1)) == 0
00145728  m_psEncCommParams->iMCTFCompressedSrcChromaWidth <= 65536
00145762  m_psEncCommParams->iMCTFCompressedSrcChromaHeight <= 65536
0014579d  m_psEncCommParams->mctf_LowResChromaHdr[iBufIdx]!= 0
001457d2  (m_psEncCommParams->mctf_LowResChromaHdr[iBufIdx]&(128-1)) == 0
00145812  m_psEncCommParams->mctf_LowResChromaBuffer[iBufIdx] != 0
0014584b  (m_psEncCommParams->mctf_LowResChromaBuffer[iBufIdx]&(128-1)) == 0
0014588e  AVE_HMESCWR_PLANE_CHROMA_WDT(m_psEncCommParams->width, ChromaFmt_422, 2) <= 65536
001458e0  AVE_HMESCWR_PLANE_CHROMA_HGT(m_psEncCommParams->height, ChromaFmt_422, 2) <= 65536
00145933  pCurrFrmInfo != NULL
0014595d  1<=AVE_ALIGN_UP(m_psEncCommParams->width, 128)/128 && AVE_ALIGN_UP(m_psEncCommParams->width, 128)/128<=128
001459c8  1<=AVE_ALIGN_UP(m_psEncCommParams->height, 128)/128 && AVE_ALIGN_UP(m_psEncCommParams->height, 128)/128<=128
00145a35  4<=AVE_ALIGN_UP(m_psEncCommParams->width, 16)/4 && AVE_ALIGN_UP(m_psEncCommParams->width, 16)/4<=4096
00145a9b  4<=AVE_ALIGN_UP(m_psEncCommParams->height, 16)/4 && AVE_ALIGN_UP(m_psEncCommParams->height, 16)/4<=4096
00145b03  pcCurrFrmInfo != NULL
00145b2d  + %s::%d, refIdxRc = %d, rcPass = %d
00145b53  pcCurrFrmInfo->m_iFrameNumber == currFrameNum
00145b81  pcCurrFrmInfo != NULL && pcCurrFrmInfo->m_iFrameNumber == currFrameNum
00145bc8  %s Enter %p %p %d %lld
00145bdf  ConfigReadDMA
00145bed  m_psEncCommParams->iaMCTFCompressedSrcLumaCmpAddr[iCmpSrcBufIdx] == pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Luma].sCIBuf.saIBuf[AVE_BufIdx_Data].iAddr
00145c8b  m_psEncCommParams->iaMCTFCompressedSrcLumaHdrAddr[iCmpSrcBufIdx] == pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Luma].sCIBuf.saIBuf[AVE_BufIdx_Header].iAddr
00145d2b  m_psEncCommParams->iaMCTFCompressedSrcChromaCmpAddr[iCmpSrcBufIdx] == pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Chroma].sCIBuf.saIBuf[AVE_BufIdx_Data].iAddr
00145dcd  m_psEncCommParams->iaMCTFCompressedSrcChromaHdrAddr[iCmpSrcBufIdx] == pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Chroma].sCIBuf.saIBuf[AVE_BufIdx_Header].iAddr
00145e71  m_psEncCommParams->iMCTFCompressedSrcLumaStride == (size_t)pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Luma].sCIBuf.saIBuf[AVE_BufIdx_Data].iStride
00145f08  m_psEncCommParams->iMCTFCompressedSrcChromaStride == (size_t)pcCurrFrmInfo->m_sCompInput.saCPBuf[AVE_BufIdx_Chroma].sCIBuf.saIBuf[AVE_BufIdx_Data].iStride
00145fa3  iInputLumaHdrAddr != 0
00145fba  (iInputLumaHdrAddr&(128-1)) == 0
00145fdb  iInputLumaAddr != 0
00145fef  (iInputLumaAddr&(128-1)) == 0
0014600d  (iInputLumaStride&(64-1)) == 0
0014602c  iInputChromaHdrAddr != 0
00146045  (iInputChromaHdrAddr&(128-1)) == 0
00146068  iInputChromaAddr != 0
0014607e  (iInputChromaAddr&(128-1)) == 0
0014609e  (iInputChromaStride&(64-1)) == 0
001460bf  (F:%lld, FN:%d): Prev frame: %p (%d), Next frame: %p (%d)
001460f9  pInPicParams->sFrameInfo.eParamSetType >= AVE_MCTF_ParamSetType_Default && pInPicParams->sFrameInfo.eParamSetType < AVE_MCTF_ParamSetType_Max
00146187  %s: MCTFStrength Orig %d; New %d
001461a8  %s Exit %d
001461b7  %s Enter
001461c0  ConfigWriteDMA
001461cf  currFrameNum == pInPicParams->sFrameInfo.sGOPInfo.iFrameNum
0014620b  Clearing output MCTF buffer for F%d bufIdx%d
00146238  iBufAddr != 0
00146246  iLumaHdrAddr != 0
00146258  (iLumaHdrAddr&(128-1)) == 0
00146274  iLumaAddr != 0
00146283  (iLumaAddr&(128-1)) == 0
0014629c  outputLumaStride != 0
001462b2  (outputLumaStride & (64-1)) == 0
001462d3  iChromaHdrAddr != 0
001462e7  (iChromaHdrAddr&(128-1)) == 0
00146305  iChromaAddr != 0
00146316  (iChromaAddr&(128-1)) == 0
00146331  outputChromaStride != 0
00146349  (outputChromaStride & (64 - 1)) == 0
0014636e  %s:%d gating: from previous frame: %d  iMCTFStrengthStats = %d 
001463ae  SetMCTF
001463b6  %s:%d gating: after previous frame strength adjustment  frame: %d, iMCTFStrength = %d -> %d 
00146413  %s:%d gating: frame: %d  cap iMCTFStrength to 8
00146443  %s:%d after APL adjustment frame %d iMCTFStrength = %d -> %d
00146480  %s:%d: F %d    after scaling adjustment iMCTFStrength = %d iDynamicStrength = %d
001464d1  %s:%d: F %d iMCTFNumRefs = %d iMCTFAdjMask = 0x%08x, eParamSetType = %d
00146519  iGlobalAvgSAD <= UINT16_MAX
00146535  iGlobalAvgSAD = %d
00146548  HME RC CollectStats: bufIdx %d, RefIdx %d
00146572  HMERC_STATSRESULTS_SUMABSMVX 0x%x
00146594  HMERC_STATSRESULTS_SUMABSMVY 0x%x
001465b6  HMERC_STATSRESULTS_SUMSADY 0x%x
001465d6  HMERC_STATSRESULTS_SUMSADUV 0x%x
001465f7  m_psEncCommParams->eStfPipeConcurrentMode == AVE_ConcurrentMode_Chained || pCmd->frameType == IMG_MCTF_FILTERING
00146668  %s:%d F %d bGateOutCurrFrame %d iMCTFFilterStrength %d Gating En:%d
001466ac  m_psEncCommParams->eWorkType == AVE_WorkType_MCTF || pInPicParams->sRCUpdateData.bInputCompressed
0014670e  m_psEncCommParams->chroma_format >= ChromaFmt_420 && m_psEncCommParams->chroma_format <= ChromaFmt_444
00146775  SetMEPipe
0014677f  0<iNumRefs && iNumRefs<=4
00146799  %s::%s PipeBitDepth = %d, ChromaFormat = %d
001467c5  PushBack() when MctfFrameQueue %d is full!
001467f0  PushBack: F %d Q state %d, %d, %d
00146812  Received eGatingType = %d
0014682c  Applied eGatingType = %d
00146845  %s:%d pipe FilterStrength_APLD = %d, FilterStrength_gradient =%d
00146886  SetFilterGating
00146896  No MCTF gating is applied (eGatingType = %d)
001468c3  %s::%s:%d %u FilterStrength = %d 
001468e5  %s: m_iaFiltStrength[%u] = %d, Noise frame number:%u , First Noise frame:%d
00146931  %s: Frame:%u bufIdx %d
00146948  CollectLRFSStats
00146959  ./AppleAVE2FW/Legacy/CMCTFHelper_H18.cpp
00146982  m_psMgmtParams != NULL
00146999  GetPicMgmtParams
001469aa  %s::%s: Enter
001469b8  CGGMController
001469c7  ./AppleAVE2FW/Legacy/CGGMController.cpp
001469ef  %s::%s: Exit
001469fc  %s::%s: Enter %p
00146a0d  %s::%s: pGGMInitCmd is NULL
00146a40  pInVideoParams->input_bitdepth == 8 || pInVideoParams->input_bitdepth == 10
00146a8c  hevc_sps->bit_depth_luma_minus8 == 0 || hevc_sps->bit_depth_luma_minus8 == 2
00146ad9  EncCommParams.input_chroma_format == ChromaFmt_420
00146b0c  EncCommParams.chroma_format == ChromaFmt_420
00146b39  EncCommParams.pic_width_in_mbs >= 8 && EncCommParams.pic_height_in_mbs >= 4
00146b85  (EncCommParams.pic_width_in_mbs <= 1024 && EncCommParams.pic_height_in_mbs <= 512) || (EncCommParams.pic_width_in_mbs <= 512 && EncCommParams.pic_height_in_mbs <= 1024)
00146c2e  m_sGgmFrameInfo[%d]: L0: 0x%llx-0x%llx-0x%llx-0x%llx
00146c63  m_sGgmFrameInfo[%d]: L1: 0x%llx-0x%llx-0x%llx-0x%llx, 0x%llx-0x%llx
00146ca7  %s::%s: Exit %d
00146cb7  %s::%s: Enter %d, %d, %d
00146cd0  %s::%s: Frame: %d, SCIndex: %d, HMESCSRCPIXRD_CTXCFG_SRCADDR: 0x%llx
00146d15  %s::%s: Frame: %d, SCIndex: %d, HMESCSRCPIXRD_CTXCFG_STRIDE: %d, InputCompressed: %d
00146d6a  (iAddr & (128 - 1)) == 0
00146d83  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_SPRHME_RMACMPCHANNELCFG_HDRADDR: 0x%llx
00146dd2  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_SPRHME_RMACMPCHANNELCFG_CMPADDR: 0x%llx
00146e21  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_SPRHME_RMACMPCHANNELCFG_STRIDE: %d
00146e6b  %s::%s: Frame: %d, SCIndex: %d, HMESRCPIXRDAGU_SRCAGU_STRIDE: %d, InputCompressed: %d
00146ec1  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_HDRADDRLOW[1]: 0x%llx
00146f15  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_CMPADDRLOW[1]: 0x%llx
00146f69  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_STRIDE(1): %d
00146fb5  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_HDRADDRLOW[0]: 0x%llx
00147009  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_CMPADDRLOW[0]: 0x%llx
0014705d  %s::%s: Frame: %d, SCIndex: %d, HMEDMA_HMESC_WMACMPCHANNELCFG_STRIDE(0): %d
001470ad  %s::%s: Mode: %d, Frame: %d, Index: %d, GG: %d(%d), X: %d-%d, Y: %d-%d
0014710a  iGGIndex >= iGGNum && !psGGCoordISrc->bValid
00147137  pInPicParams
00147144  psGGMInfo
0014714e  %s::%s: Enter %p-%p, F-F-F-C: %lld-%d-%d-%d, %d-%d, 0x%llx
00147189  pInPicParams->sFrameInfo.sGOPInfo.iFrameNum == (uint32_t)m_iHMESCFrameNum
001471d3  %s::%s: SCIndex: %d, FrameInfo: %d-%d-%d-%d
001471ff  m_sGgmFrameInfo[iHMESCIndex].iGGNum > 0
00147227  m_sGgmFrameInfo[iHMESCIndex].iValidGGNum > 0
00147259  pGGMCmd
00147261  %s::%s: Enter %d
00147272  %s::%s: Enter, F-F-C: %d-%d-%d
00147291  %s::%s: Frame: %d, FSIndex: %d, GG: %d, X: %d-%d, Y: %d-%d
001472cc  SetHMEFSPerFrame
001472dd  %s::%s: Frame: %d, FSIndex: %d, GG: %d, X: %d-%d, Y: %d-%d, Ctx: %d-%d %d-%d
0014732a  SetHMEFSPerBBox
0014733a  iHMEFSResultAddr != 0
00147350  (iHMEFSResultAddr & (64 - 1)) == 0
00147373  %s::%s: Frame: %d, FSIndex: %d, GG: %d, FSResultAddr: 0x%llx
001473b0  %s::%s: Enter %p-%p, F-F-F-G: %lld-%d-%d-%d
001473dc  pInPicParams->sFrameInfo.sGOPInfo.iFrameNum == (uint32_t)m_iHMEFSFrameNum
00147426  %s::%s: Enter %p, %d
0014743b  %s::%s: Enter F-F-G: %d-%d-%d
00147459  %s::%s: Frame: %d, FSIndex: %d, GG: %d, GradMax: %d
0014748d  %s::%s: Frame: %d, RSIndex: %d, GG: %d, X: %d-%d, Y: %d-%d
001474c8  SetHMERSPerFrame
001474d9  %s::%s: Frame: %d, RSIndex: %d, GG: %d, X: %d-%d, Y: %d-%d, Ctx: %d-%d %d-%d
00147526  SetHMERSPerBBox
00147536  %s::%s: Frame: %d, RSRefIndex: %d, RSRef: %d, HmgMat: 0x%x-0x%x-0x%x 0x%x-0x%x-0x%x 0x%x-0x%x-0x%x
00147599  SetHMERSPerPass
001475a9  %s::%s: Frame: %d, RSRefIndex: %d, RSRef: %d, GG: %d, X: %d-%d, Y: %d-%d
001475f2  iHMERSResultAddr != 0
00147608  (iHMERSResultAddr & (64 - 1)) == 0
0014762b  %s::%s: Frame: %d, RSIndex: %d, RSRef: %d, RSResultAddr: 0x%llx
0014766b  %s::%s Enter %p-%p, F-F-F-G-P: %lld-%d-%d-%d-%d, %d
0014769f  %s::%s: HME RS frame number mismacthes: F-F-F-G-P: %lld-%d-%d-%d-%d, %d
001476e7  pInPicParams->sFrameInfo.sGOPInfo.iFrameNum == (uint32_t)m_iHMERSFrameNum
00147731  m_iHMERSFrameNum >= 2
00147747  %s::%s: Enter F-F-G-P: %d-%d-%d-%d
0014776a  %s::%s: Frame: %d, RSIndex: %d, GG: %d, DiffMax: %d
0014779e  %s::%s: Frame: %d, PipeIndex = %d, GG: %d, X: %d-%d, Y: %d-%d
001477dc  SetPipePerFrame
001477ec  %s::%s: Frame: %d, iPipeIndex: %d, PipeRef: %d, GG: %d, X: %d-%d, Y: %d-%d
00147837  %s::%s: Frame: %d, PipeIndex: %d, PipeRef: %d, HmgMat: 0x%x-0x%x-0x%x 0x%x-0x%x-0x%x 0x%x-0x%x-0x%x
0014789b  %s::%s: Frame: %d, PipeIndex: %d, Strides: %d-%d, %d-%d, InputCompressed: %d
001478e8  %s::%s: Frame: %d, PipeIndex: %d, YAddr: 0x%llx-0x%llx, UVAddr: 0x%llx-0x%llx
00147936  %s::%s: Frame: %d, PipeIndex: %d, PipeRef: 0, YAddr: 0x%llx-0x%llx, UVAddr: 0x%llx-0x%llx
00147990  %s::%s: Frame: %d, PipeIndex: %d, PipeRef: 1, YAddr: 0x%llx-0x%llx, UVAddr: 0x%llx-0x%llx
001479ea  %s::%s: Frame: %d, PipeIndex: %d, GG: %d, X: %d-%d, Y: %d-%d, Ctx: %d-%d %d-%d, %d-%d-%d-%d
00147a46  SetPipePerBBox
00147a55  %s::%s: Frame: %d, PipeIndex: %d, GG: %d, FSResultAddr: 0x%llx
00147a94  m_sGgmFrameInfo[iPipeIndex].iaBlurEnabled[m_iPipeCurGgInd] >= 0
00147ad4  iVal >= 0 && iVal <= 1024
00147aee  %s::%s: Enter %p-%p, F-F-F-G: %lld-%d-%d-%d %d
00147b1d  pInPicParams->sFrameInfo.sGOPInfo.iFrameNum == (uint32_t)m_iPipeFrameNum
00147b66  %s::%s: Frame: %d, PipeIndex: %d, GG: %d, Weights: %d, %d-%d-%d
00147ba6  %s::%s: Enter %p, %p, %d
00147bbf  %s:%d %s | wrong parameter %p %p
00147be0  AVE_AVC_SetPPS
00147bef  psSyntaxCfg != __null && psPPS != __null
00147c18  %s::%s:%d %s | wrong parameters %p %llu %p %p
00147c46  %s::%s Already initialized %p %llu
00147c69  %s::%s:%d %s | Failed to initialize picture parameter set class %p %llu %p %p
00147cb7  %s::%s:%d %s | Failed to set picture parameter set structure %p %llu %p %p
00147d02  %s::%s:%d is not initialized %p %llu %d %d
00147d2d  Uninit
00147d34  Generate
00147d3d  %s::%s:%d %s | too many PPS %p %d %d
00147d62  iNum <= 9
00147d6c  %s::%s:%d %s | fail to generate PPS %p %p %d %d %p %d
00147da2  %s::%s Exit %p %d %d %d
00147dba  AVE_AVC_PPS
00147dc6  AVE_AVC_SetSlice
00147dd7  psSyntaxPFCfg != __null && psSlice != __null
00147e04  %s::%s:%d %s | Failed to initialize slice header parameter set class %p %llu %p %p
00147e57  %s::%s:%d %s | Failed to set slice header parameter set structure %p %llu %p %p
00147ea7  %s::%s Enter %p %llu %p %p %p %d %p
00147ecb  %s::%s:%d %s | wrong parameters %p %llu %p %p %p %d %p
00147f02  psSPS != __null && psPPS != __null && piSH != __null && iBufSize > 0 && piSHNumOfBit != __null
00147f61  %s::%s:%d %s | fail to generate Slice %p %p %p %p %d %p %d
00147f9c  %s::%s Exit %p %p %p %d %p %d
00147fba  AVE_AVC_Slice
00147fc8  %s:%d %s | wrong parameter %p 0x%llx %p
00147ff0  AVE_AVC_SetSPS
00147fff  psSyntaxCfg != __null && psSPS != __null
00148028  %s::%s:%d %s | Failed to initialize sequence parameter set class %p %llu %p %p
00148077  %s::%s:%d %s | Failed to set sequence parameter set structure %p %llu %p 0x%llx %p
001480ca  %s::%s Enter %p %llu %p
001480e2  %s::%s:%d %s | wrong parameter %p %llu
00148109  psPSContext != __null
0014811f  %s::%s:%d %s | failed to generate SPS %p %llu %p
00148150  AVE_AVC_SPS
0014815c  %s::%s Enter %p %lld %d %d %d.%03d %d.%03d %d
0014818a  %s::%s:%d %s | fail to initialize FPS %p %lld %d %d %d.%03d %d.%03d %d %d
001481d4  %s::%s Exit %p %lld %d %d %d.%03d %d.%03d %d %d
00148204  %s::%s Enter %p %lld
00148219  %s::%s Exit %p %lld %d
00148230  GetInterval
0014823c  %s::%s Enter %p %lld %lld %d
00148259  Update
00148260  %s::%s:%d %s | Wrong parameter %p %lld %lld %d
0014828f  iFrameNum >= 0
0014829e  %s::%s:%d %s | Frame number out of range %p %lld %lld %d %lld
001482dc  iFrameNum <= m_iLastFrame && m_iLastFrame - iFrameNum < (3 + 2)
0014831c  %s::%s Exit %p %lld %lld %d %d
0014833b  %s::%s Enter %p %lld %lld 0x%llx 0x%x %p %p
00148367  Process
0014836f  %s::%s:%d %s | Wrong parameter %p %lld %lld 0x%llx 0x%x %p %p
001483ad  psKeyFrameHint != __null
001483c6  %s::%s:%d %s | fail to update FPS %p %lld %lld 0x%llx 0x%x %p %p %d
0014840a  %s::%s:%d %s | Wrong parameter %p %lld %lld 0x%llx 0x%x %p %p | %f %f %d %d
00148456  pPTS != __null && pPTS->iValue >= 0 && pPTS->iTimescale > 0
00148492  %s::%s:%d %s | fail to add PTS to FPS %p %lld %lld 0x%llx 0x%x %p %p %d
001484da  %s::%s:%d %p %lld Frame[%lld] op 0x%llx 0x%x PTS %lld | interval %d %d %d.%03d %d.%03d | status %lld %lld %lld %d | Hint %d 0x%x
0014855b  %s::%s Exit %p %lld %lld 0x%llx 0x%x %p %p %d
00148589  %s::%s:%d %s | fail to update FPS %p %lld %d %d %d.%03d %d.%03d %d %d
001485e6  AVE_KeyFrame
001485f3  %s Enter %d %d %d %p
00148608  AVE_PSInfo_Make
00148618  %s:%d %s | wrong PS type %d
00148634  AVE_PSType_None < eType && eType < AVE_PSType_Max
00148666  %s:%d %s | wrong layer ID %d
00148683  0 <= iLayerID && iLayerID < ((2) < ((63 + 1)) ? (2) : ((63 + 1)))
001486c5  %s:%d %s | not padded to bytes %d %d %d %p
001486f0  (iBits & 7) == 0
00148701  %s:%d %s | too many parameter sets %d %d %d %p %d
00148733  0 <= iNum && iNum < (1 + ((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (1 + 9 ))
0014877e  %s:%d %s | PS data overflows %d %d %d %p | %d %d %d %ld
001487b6  (psPSInfo->saBuf[iNum].sBuf.iOffset + psPSInfo->saBuf[iNum].sBuf.iSize) <= (int32_t)sizeof(psPSContext->iaPSData)
00148828  %s Exit %d %d %d %p %d
0014883f  %s:%d %s | wrong parameters %p %p
00148861  %s:%d %s | wrong parameter %d
0014887f  AVC_FindLevelIdc
00148890  (AVC_Level_Invalid < eLevel) && (eLevel < AVC_Level_Max)
001488c9  %s::%s:%d %s | wrong parameter %p %llu %p
001488f3  psPPS != __null
00148903  Write_pic_parameter_set_rbsp
00148920  pcSWriter != __null
00148934  %s::%s:%d %s | num slice groups not supported %p %llu %d
0014896d  m_psPPS->num_slice_groups_minus1 == 0
00148993  %s::%s:%d %p %llu failed to set RBSP %p %d %d %d %d
001489c7  %s::%s Enter %p %llu %d %d %d %p
001489e8  %s::%s:%d %s | fail to initialize syntax writer %p %p %p %d %d
00148a27  %s::%s:%d %p %llu failed to generate PPS %d %d %d %p %d
00148a5f  %s::%s Exit %p %llu %d %d %d %p %d
00148a82  %s::%s Enter %p %llu %p %d %d
00148aa0  %s::%s:%d %s | fail to generate PPS %p %p %d %d %d %d %d
00148ad9  %s::%s Exit %p %llu %p %d %d %d
00148af9  AVC_PPS
00148b01  AVC_FindProfileIdc
00148b14  (AVC_Profile_Invalid < eProfile) && (eProfile < AVC_Profile_Max)
00148b55  CAVLC 4:4:4 Intra
00148b67  Baseline
00148b70  Constrained Baseline
00148b8a  Extended
00148b98  High 10
00148ba0  High 4:2:2
00148bab  High 4:4:4
00148bb6  psSlice != __null
00148bc8  %s::%s:%d %s | fail to initialize syntax writer %p %llu %p %d %d
00148c09  %s::%s:%d %s | wong num ref idx active override flag %p %llu %d %d %d %d %d %d %d
00148c5b  Write_slice_header
00148c6e  bNumRefIdxActiveOverrideFlag == ((m_psSlice->num_ref_idx_active_override_flag) != 0)
00148cc3  %s::%s:%d %p %p %llu failed to generate slice header %d
00148cfb  %s::%s:%d %p %llu ref pic list reordering flag l0 %d
00148d30  Write_ref_pic_list_modification
00148d50  %s::%s:%d %p %llu modification of pic nums idc %d %d
00148d85  %s::%s:%d %p %llu abs diff pic num minus1 %d %d
00148db5  %s::%s:%d %p %llu long term pic num %d %d
00148ddf  %s::%s:%d %p %p %llu failed %d
00148dfe  Write_pred_weight_table
00148e16  %s::%s:%d %p %llu no output of prior pics flag %d
00148e48  Write_dec_ref_pic_marking
00148e62  %s::%s:%d %p %llu long term reference flag %d
00148e90  %s::%s:%d %p %llu adaptive ref pic marking mode flag %d
00148ec8  %s::%s:%d %p %llu memory management control operation 0x%x
00148f03  %s::%s:%d %p %llu difference of pic nums minus1 %d
00148f36  %s::%s:%d %p %llu long term pic num %d
00148f5d  %s::%s:%d %p %llu long term frame idx %d
00148f86  %s::%s:%d %p %llu max long term frame idx plus1 %d
00148fb9  AVC_Slice
00148fc3  psSPS != __null
00148fd3  %s::%s:%d %s | failed to allocate syntax writer %p %llu %p %p %d %d
00149017  %s::%s:%d %s | failed to write SPS RBSP %p %llu %p %p %d
00149050  %s::%s:%d %s | failed to make PS info %p %llu %d %p %d
00149087  Write_vui_parameters
0014909c  %s::%s:%d %p %llu failed to generate VUI %p %d
001490cb  Write_seq_parameter_set_rbsp
001490e8  %s::%s:%d %s | wrong scaling matrix mode %p %llu %d
0014911c  m_psSPS->eScalingMatrixMode >= ScalingMatrixMode_Flat && m_psSPS->eScalingMatrixMode <= ScalingMatrixMode_ExplicitHighComp
00149197  %s::%s:%d %s | offset for ref frame not supported %p %llu %d
001491d4  m_psSPS->num_ref_frames_in_pic_order_cnt_cycle == 0
00149208  %s::%s:%d %p %llu %p SPS bits %d (bytes %d)
00149234  %s::%s:%d %p %llu failed to set RBSP %p %d
0014925f  AVC_SPS
00149267  %s:%d %s | invalid level %d
00149283  AVC_FindMaxMvsPer2Mb
00149298  psLimit != __null
001492aa  AVC_FindMaxSubMbRectSize
001492c3  HEVC_FindLevelIdc
001492d5  (HEVC_Level_Invalid < eLevel) && (eLevel < HEVC_Level_Max)
00149310  HEVC_FindProfileIdc
00149324  (HEVC_Profile_Invalid < eProfile) && (eProfile < HEVC_Profile_Max)
00149367  Main 10
0014936f  Main Still
0014937a  Main RExt
00149384  MV-HEVC
0014938c  Monochrome
00149397  Monochrome 10
001493a5  Main 4:2:2 10
001493b3  Main 4:4:4
001493be  Main 4:4:4 10
001493cc  HEVC_FindTierFlag
001493de  (HEVC_Tier_Invalid < eTier) && (eTier < HEVC_Tier_Max)
00149415  %s::%s:%d %s | fail to initialize syntax writer %p %p %d
0014944e  %s::%s:%d vps_video_parameter_set_id %p %d
00149479  %s::%s:%d | failed to generate VPS %d %d
001494a2  %s::%s:%d | failed %d
001494b8  vps_encode_independent_layer_parameters
001494e0  %s::%s:%d %s | VUI pointer is null %p
00149506  vps_vui
0014950e  m_psVUI != __null
00149520  vps_extension
0014952e  %s::%s:%d %p bits %d (bytes %d)
0014954e  video_parameter_set_rbsp
00149567  HEVC_VPS
00149570  %s::%s Enter %p %lld %d %d %d
0014958e  %s::%s:%d %s | wrong parameters %p %lld %d %d %d
001495bf  0 < fps && fps < 100000 && num >= 0
001495e3  %s::%s:%d %s | failed to allocate memory of timestamp %p %lld %d %d %d
0014962a  m_psTime != __null
0014963d  %s::%s Exit %p %lld %d %d %d %d
0014965d  %s::%s:%d allocate bigger memory of timestamp %p %lld %d %d <- %d
0014969f  %s::%s:%d failed to allocate memory of timestamp %p %lld %d
001496db  %s::%s Exit %p %lld %d %d %d
001496f8  %s::%s:%d %lld %d - %lld %d %d | %lld.%03lld %lld.%03lld 
00149737  %s::%s:%d %s | wrong state %p %lld
0014975a  CalcRt
00149761  %s::%s:%d %p %lld %d %d | %d %lld %d - %d %lld %d | %d.%03d  %d.%03d
001497a6  CalcSlide
001497b0  %s::%s:%d %p %lld %d %d %d | %d %lld %d - %d %lld %d | %d.%03d %d.%03d
001497f7  CalcAvg
001497ff  CalcOverall
0014980b  %s::%s Enter %p %lld %p
00149827  %s::%s:%d %s | wrong state %p %lld %p
0014984d  %s::%s:%d %s | failed to calculate realtime FPS %p %lld %p
00149888  %s::%s:%d %s | failed to calculate sliding average FPS %p %lld %p
001498ca  %s::%s:%d %s | failed to calculate average FPS %p %lld %p
00149904  %s::%s Exit %p %lld %p %d
0014991e  AVE_FPS
00149926  RCMode %d
00149930  bitrate %d normalized_bpp %d.%03d
00149952  hrd_max_bit_rate %d hrd_cpb_size  %d.%03d hrd_cpb_initial_delay %d.%03d
0014999a  fCRFScale %d.%03d
001499ac  iRCFeature 0x%llx
001499be  lookahead_frames %d
001499d2  fps %d.%03d totalFrames %lld
001499ef  useScenecut %d
001499fe  bSegmentEncodingEnabled %d m_segmentVbvAdjust %d | %d | %d
00149a39  M %d N %d miniGopRC %d
00149a50  InitialQp %d InitialQpp %d InitialQpb %d
00149a79  MinQp %d MaxQp %d
00149a8b  %s::%s:%d invalid parameter %p %p %d %p
00149ab3  CreateInstance
00149ac2  %s::%s:%d unsupported RC mode %p %p %d %p %d
00149aef  HRD_Main
00149af8  %s::%s:%d [ABR] Frame %lld totalBits %d targetBits %d overflow %d
00149b3a  applyAbrFeedback
00149b4b  %s::%s:%d BITBOX SegmentEncoding VBV (%lld %lld) startLoop %d EndLoop %d curLoop %d
00149b9f  calcVbvLoopNum
00149bae  %s::%s:%d BITBOX iIsFirstFrame %d SegmentEncoding Enabled %d totalFrames %lld
00149bfc  applyVbvPlanning
00149c0d  HRD_VBVPlan_%d
00149c1c  %s::%s:%d HRD planning status: (%lld %lld) type %d HrdFullness Start %d.%03d End %d.%03d Min %d.%03d loop %d
00149c89  %s::%s:%d PTS gap: interval=%lld nominal=%lld excess=%lld accumulated=%lld
00149cd4  handleLargePTSGap
00149ce6  %s::%s:%d LA0 (%lld %lld) frameType %d tid %d dts %lld tscale %d past %d.%03d %d.%03d %d.%03d %d.%03d
00149d4c  processRateControl
00149d5f  %s::%s:%d BITBOX (%lld %lld) Frame[%lld] %lld %d %d | %d %d %d %d | %d.%03d | inter %d intra %d | %lld %lld %lld %d %d.%03d | LRvar %d.%03d
00149deb  %s::%s:%d UnPredIdx (%lld %lld) tid %d LayerID %dProc past %d.%03d %d.%03d %d.%03d %d.%03d
00149e46  %s::%s:%d LookAhead Update Past Frame Tid %d decodeOrder %lld LayerID %d unPredIdx %d.%03d 
00149ea2  %s::%s:%d F(%lld, %lld) Unexpected TimeScale changed from %d to %d
00149ee5  %s::%s:%d BITBOX (%lld %lld) type %d getQScale %d.%03d
00149f1c  %s::%s:%d BITBOX (%lld %lld) type %d ABR %d.%03d -> %d.%03d
00149f58  %s::%s:%d BITBOX (%lld %lld) type %d cqscale %d.%03d, qscale %d.%03d
00149f9d  %s::%s:%d qscale  %d.%03d
00149fb7  %s::%s:%d BITBOX (%lld %lld) type %d VbvPlanning %d.%03d -> %d.%03d
00149ffb  %s::%s:%d BITBOX (%lld %lld) type %d SliceType/Temporal Scaling %d.%03d -> %d.%03d
0014a04e  %s::%s:%d BITBOX (%lld %lld) minQP %d maxQP %d
0014a07d  %s::%s:%d BITBOX (%lld %lld) qscale %d.%03d qp %d
0014a0af  %s::%s:%d FixQp: %d
0014a0c4  %s::%s:%d BITBOX LrmeVarToVar (%lld, %lld) frameSumOfVar: %d, lowResVar: %d
0014a110  updateRateControl
0014a122  Caller is /Library/Caches/com.apple.xbs/18D7D940-DD36-41F0-9DE6-C2BC3B7AF53F/TemporaryDirectory.vLkS0U/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1019
0014a1c5  Caller is /Library/Caches/com.apple.xbs/18D7D940-DD36-41F0-9DE6-C2BC3B7AF53F/TemporaryDirectory.vLkS0U/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1024
0014a268  %s::%s:%d BITBOX (%lld %lld) HRD fullness %d underflow %d overflow %d bitsFromTranscode[%d] %lld
0014a2e5  %s::%s Enter, bit = %lld
0014a2fe  updateBitsFromCAVLC
0014a312  %s::%s:%d BITBOX (%lld %lld) cavlcBits %lld transcodeBits %lld estTranscodeBits %lld
0014a37f  HRD_CBRFiller
0014a38d  Caller is /Library/Caches/com.apple.xbs/18D7D940-DD36-41F0-9DE6-C2BC3B7AF53F/TemporaryDirectory.vLkS0U/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1072
0014a430  Caller is /Library/Caches/com.apple.xbs/18D7D940-DD36-41F0-9DE6-C2BC3B7AF53F/TemporaryDirectory.vLkS0U/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1084
0014a4d3  %s::%s:%d BITBOX (%lld %lld) HRD fullness %d underflow %d overflow %d filler %d bitsFromTranscode %lld
0014a53e  %s::%s %s decodeOrder=%lld c=%d filterIdx=%d unPredIdx=%d.%03d
0014a59d  %s::%s:%d UnPredIdx (Update) (%lld %lld) frameType %s tid %d past %d.%03d %d.%03d %d.%03d %d.%03d
0014a5ff  %s::%s cplx= %d.%03d cplxFiltered=%d.%03d
0014a629  updateCplxForZeroLA
0014a63d  %s::%s:%d BITBOX (%lld %lld) cavlcBits %lld transcodeBits %lld estTranscodeBits %lld modelParam %d
0014a6b6  %s::%s:%d MVHEVC (%lld %lld) pFrame.bitsFromCAVLC %lld pFrame.estimatedTranscodeBits %lld
0014a710  BITBOX (%lld %lld) totalBits %d, estTrancodeBits %lld
0014a747  updateDRLParams
0014a757  %s:%s Enter
0014a763  /Library/Caches/com.apple.xbs/18D7D940-DD36-41F0-9DE6-C2BC3B7AF53F/TemporaryDirectory.vLkS0U/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp
0014a810  %s:%s Enter %d
0014a81f  updateFixedQP
0014a82d  %s:%s Exit %d
0014a83b  updateBitRate
0014a849  %s::%s:%d BITBOX estimateBits (%lld, %lld) transcode: %lld, estTranscode: %lld, estBitsfromRC: %d
0014a8ab  update
0014a8b2  %s::%s cplxFiltered %d.%03d m_rateFactor %d.%03d
0014a8e3  getQScale
0014a8ed  %s::%s:%d m_rateFactor %d.%03d  m_cplxSum %d.%03d m_cplxCnt %d.%03d
0014a931  updateParams
0014a93e  %s::%s Enter %s %d %d %p %d %d %d
0014a965  %s::%s:%d %s Init iscbr %d %d %d %d %d.%03d %d.%03d, %d.%03d
0014a9a2  %s::%s Exit %s %d %d %p %d %d.%03d %d.%03d
0014a9cd  %s::%s:%d %s %s status: max_bitrate %d cpb_size %d.%06d, init_cpb_delay %d.%06d, t_af %d.%06d, t_c %d.%06d, t_scale %d, 1st_dts %lld
0014aa58  %s::%s:%d %s updated params: max_bitrate %d cpb_size %d.%03d
0014aa95  updateHrdParams
0014aaa5  %s::%s:%d Unexpected TimeScale change in timestamp %d %d %lld %p
0014aae6  updateHrdStatus
0014aaf6  %s::%s:%d %s numOfFrame %lld bits %d 1stdts %lld iTimescale %d iValue %lld hrd_t_c %d.%06d t_c %d.%06d
0014ab5d  %s::%s:%d BITBOX (%lld %lld) type %d M %d numP %d
0014ab8f  calcBaseQScale
0014ab9e  %s::%s:%d BITBOX (%lld %lld) type %d bits %d cplxFilter %d blur %d
0014abe1  %s::%s:%d BITBOX (%lld %lld) type %d bits %d cplxFilter %d sum %d snapshotlen %d
0014ac32  %s::%s:%d BITBOX (%lld %lld) type %d current blur %d.%06d filtered blur %d.%06d transcodeBits %d cplxFiltered %d.%06d
0014aca8  %s::%s: Enter, %lld
0014acd3  %s::%s: Exit, %d - %d, %d, %d
0014acf1  %s::%s: Enter, %d - %d, %d, %d
0014ad26  RateControl
0014ad4c  RQModel
0014ad6e  BlurRatio
0014ad78  %s::%d, alpah %d beta %d v %d output %d
0014ada0  predict
0014ada8  ./AppleAVE2FW/Firmware/Log/AVE_Log.cpp
0014adcf  gs_psCfg != NULL
0014ade0  AVE_Log_Init
0014aded  gs_pMutex != (RESOURCE)0
0014ae06  AVEIOP%d: 
0014ae11  %lld %d AVEIOP%d %s: 
0014ae2b  gs_psCfg_Default != NULL
0014ae44  AVE_Log_Default
0014ae70  ./AppleAVE2FW/Firmware/Utils/CAVEFilterBase.cpp
0014aea0  outputPipe[pin] != 0
0014aeb5  SendNotification
0014aec6  dataSize <= FFWMSG_DATA_SIZE
0014aeeb  UpdateFixedQP
0014aef9  - CRateControl::Init
0014af0e  got the qp:%08x
0014af1e  - CRateControl::RateControl
0014af3a  Accumulate
0014af45  - CRateControl::Accumulate
0014af60  UpdateBits
0014af6b  - CRateControl::UpdateBits
0014af86  %s::%s:%d Enter %d %d %d %d %d %d %d %d %d %d %d %d %d
0014afbd  ProcessRateControl
0014afd0  ./AppleAVE2FW/Firmware/Algorithm/RateControl/CRateControl.cpp
0014b00e  display_order >= m_pcRefManager->GetFirstFrameNum()
0014b042  F (%d %d): MiniGOP: %d %d %p | %d %d | %d %d
0014b070  %s::%s:%d Exit %d %d %d %d %d %d %d %d %d %d %d %d %d %d
0014b0a9  ProcessAccumulate
0014b0bb  - CRateControl::ProcessAccumulate
0014b0dd  ProcessUpdateBits
0014b0ef  Wrong engine type = %d!!! 
0014b10a  updateTempID
0014b134  chromaFormat >= 0 && chromaFormat <= 3
0014b15b  AVE_RC_CalculateDistortion
0014b176  %s::%s: Enter, %d - %d
0014b1a2  %s::%s: Exit, %d - %d, %d, %d %d %d %d %d %d
0014b1cf  %s::%s: Enter, %d - %d, %d, %d %d %d %d %d %d
0014b1fd  RestoreRCSegmentCtx
0014b211  CRateControl
0014b21e  ./AppleAVE2FW/Firmware/Algorithm/GOP/CFrameType.cpp
0014b252  ctrl->numTemporalLayers <= HEVC_AVE2_MAX_TLAYER
0014b282  m_ctx->iPrevFrameTemporalID[0] >= m_ctx->iPrevFrameTemporalID[1]
0014b2c3  AdjustTemporalID
0014b2df  AVE ERROR: FrameInfo == NULL
0014b2fc  display_order <= next_irap_display_order
0014b325  FrameType
0014b32f  next_irap_display_order <= next_scene_display_order
0014b363  ./AppleAVE2FW/Firmware/Algorithm/QPModulation/CStaticAreasLowQP.cpp
0014b3a7  ((uintptr_t)pCbp0CntBuf&(16-1)) == 0
0014b3e3  %s:%d DPB ERROR: %lld
0014b410  %s:%d DPB ERROR: %lld %d %d
0014b42c  DPB (%lld) WARNING (frame %d): selected IsThisFrameNonReference -> default IndexLTRFrameToBeReplaced (was %d) to invalid
0014b4a5  DPB (%lld) WARNING (frame %d): selected IsThisFrameNonReference -> default IsALongTermFrame (was true) to false
0014b515  DPB (%lld) WARNING (frame %d): selected IsThisFrameNonReference but current frame is intra frame. will not honor it
0014b589  DPB (%lld) WARNING (F %d): idx out of bound (IndexRefFrameToBeUsedL0a %d FrameNumberFromIDR %d num_refs %d) -> default to 0
0014b605  DPB (%lld) WARNING (frame %d): selected long term (%d) to be replaced but the frame passed is not long term -> default to short term
0014b68a  DPB (%lld) WARNING (frame %d): IndexLongTermReferenceFrameToBeReplaced >= m_num_ref_frame (%d >= %d) -> out of bound -> default to no replacement
0014b71c  DPBSanityCheck
0014b72b  DPB (%lld)  WARNING (frame %d): IndexLongTermReferenceFrameToBeReplaced selected (%d) is not long term -> default to no replacement
0014b7af  DPB (%lld) WARNING (frame %d): no more space for long term frames (m_context.num_ref_frame %d long %d); default this to short term
0014b832  RemoveDPBEntry
0014b856  InsertAfterDPBEntry
0014b86a  InsertEndDPBEntry
0014b87c  ./AppleAVE2FW/Firmware/Algorithm/Reference/CAVEDPB.cpp
0014b8b3  psRCFrameInfo->frameNumber >= m_iFirstFrameNum
0014b905  %s:%d DPB ERROR
0014b92a  ManageDPBBuffer
0014b93a  frameInfo.frameNumber >= m_iFirstFrameNum
0014b964  %s:%d DPB ERROR: %lld %d %d %d %d
0014b986  %s:%d DPB ERROR: %lld %d %d %d
0014b9a5  %s:%d DPB ERROR:
0014b9b6  %s::%s Enter %lld %d %d
0014b9e3  %s::%s:%d %lld %d %d
0014b9f8  %s::%s:%d %lld %d %d %d | %d %d | %d %d %d
0014ba23  %s::%s Exit %llu %d
0014ba53  %s::%s:%d DPB ERROR: %lld
0014ba6d  DPB ERROR: RemoveDPBEntry failed
0014baa4  %s:%d DPB ERROR L0: %d %lld %d %d %d %d %d
0014bacf  %s:%d DPB ERROR L1: %d %lld %d %d %d %d %d
0014bb23  GetValidRefByPoc
0014bb34  %s::%s Exit %lld %d %d %d
0014bb4e  %s:%d DPB ERROR: %u %d
0014bb7a  DPBFindFirstInvalid
0014bb8e  H265VideoEncoderDPB
0014bba2  %s::%s::%d bDrop=%d bitrate=%d Fps=%d aveNDR=0x%x nTL=%d nB=%d bBref=%d mode=%d
0014bbf2  ./AppleAVE2FW/Firmware/Algorithm/Reference/CAVERefManager.cpp
0014bc30  SetRCFrameInfo
0014bc3f  %s::%s:%d SetFrameInfo drl 0 %s%lld.%02lld %s%lld.%02lld
0014bc78  %s::%s Exit %p %p
0014bc8a  psFrameInfo->frameNumber >= m_iFirstFrameNum
0014bcb7  UpdatePTS
0014bcc1  RC2: %s: thisFrame %d previousFrame %d
0014bcfd  RC2: %s: fAveFps = %d = ExpectedFrameRate %d (iPTStimescale == 0 or F = 0)
0014bd48  AVE WARNING: sPTS.iTimescale changed current timescale = %d previous timescale - %d
0014bd9c  RC2: %s: F %d fAveFps %d (sPTS.iTimescale %d fFrameDuration %d, fAveFrameDuration %d)
0014bdf2  CAVERefManager
0014be01  ./AppleAVE2FW/Firmware/Device/Capability/AVE_DevCap.cpp
0014be39  pDevCap->psCEntry != __null
0014be55  AVE_DevCap_Find
0014be65  idx >= 0
0014be6e  AVE_DevCap_WorkType2Idx
0014be86  %s::%s:%d %s | Fail to find device capability (DevID: %d DevType: %d ChipType: %d DevRevision: %d Arch: %d SVE Num: %d NumPerGroup: %d DevSubIDFlag: 0x%llx) ret: %d
0014bf2b  %s::%s:%d %s | Fail to find device capability (TargetID: %d | DevID: %d DevType: %d ChipType: %d DevRevision: %d Arch: %d SVE Num: %d NumPerGroup: %d DevSubIDFlag: 0x%llx) ret: %d
0014bfdf  AVE_DevInfo
0014bfeb  %s::%s Enter %p %p %d %d %p
0014c007  CAVEPipeISRManager
0014c01a  %s::%s Exit %p %p %d %d %p
0014c035  --- CAVEPipeISRManager is destroyed
0014c05a  PRE CONDITION: %s:%d %s
0014c072  ./AppleAVE2FW/Firmware/Resource/HwBlock/CAVEPipeISRManager.cpp
0014c0b1  source < INT_NROF_VECTORS
0014c0d0  Unmask
0014c0d7  %s:%d Unexpected pipe mode mask. only one bit expected, Got: 0x%x
0014c11a  AvePipeDoneHandler
0014c12d  %s:%d Unhandled pipe_mode, Mask: 0x%x
0014c154  HevcPipeDoneHandler
0014c168  %s:%d XC buffer full!
0014c194  TranscodeHandler
0014c1a5  AVE Error:VLC buffer write full!
0014c1c7  AVE Error: AVC XC buffer write full!
0014c1ed  AVE Error: HEVC XC buffer write full!
0014c22b  DmaErrHandler
0014c239  %s::%s:%d Xcode AVC Debug Error 0x%x 0x%x
0014c27c  GetSlicePos
0014c288  %s::%s:%d sizeCnt = %d
0014c29f  GetSizeQueue
0014c2ac  len >= 4
0014c2ca  len (= %d) is not 4 bytes aligned, we may miss some information ! 
0014c30e  Offset (= %d) is not 4 bytes aligned, we may miss some information ! 
0014c355  %s::%s Enter %p %p %d %zu %p %zu %p %zu %p %zu %p %zu
0014c38b  CFlowControllerBase
0014c3b7  ./AppleAVE2FW/Firmware/HwCtrl/CFlowControllerBase.cpp
0014c3ed  CEnvironment::Instance()->GetShareBufSize() >= sizeof(union uCAveNotification) * TARGET_TO_HOST_BUFFER_SIZE
0014c459  cmdLog != 0
0014c465  FSMHMESC
0014c46e  fsmHmeSC != 0
0014c47c  FSMLRME
0014c484  fsmLrme != 0
0014c491  FSMDMV
0014c498  fsmDMV != 0
0014c4a4  FSMLRMERC
0014c4ae  fsmLrmeRC != 0
0014c4bd  FSMENCPIPE
0014c4c8  fsmEncPipe != 0
0014c4d8  FSMSTFPIPE
0014c4e3  fsmStfPipe != 0
0014c4f3  FSMTRANSCODE
0014c500  fsmTranscode != 0
0014c512  sHeartBeatParams.terminateSema != (SEMA)0
0014c551  sPP.terminateSema != (SEMA)0
0014c56e  AVE_PP
0014c575  g_psAVE_Hist != NULL
0014c58a  %s::%s Exit %p %p %d %zu %p %zu %p %zu %p %zu %p %zu
0014c5bf  ~CFlowControllerBase
0014c5d4  %s::%s:%d ENC: StartCount %d-%d-%d-%d, Idle %d-%d-%d-%d-%d
0014c60f  PrintHwClientStatus
0014c623  %s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld CTX %d-%d-%d-%d-%d
0014c663  hEncCmdQueue %d, cmd->client_id %lld
0014c688  %s::%s:%d HMESC %lld: StartCount %d-%d-%d-%d
0014c6b5  %s::%s:%d LRMEFS %lld: StartCount %d-%d-%d-%d
0014c6e3  %s::%s:%d LRMERC %lld: StartCount %d-%d-%d-%d
0014c711  %s::%s:%d Pipe %lld: StartCount %d-%d-%d-%d
0014c73d  %s::%s:%d xcode %lld: StartCount %d-%d-%d-%d
0014c76a  %s::%s:%d DMV: StartCount %d, Idle %d, Client %lld
0014c79d  %s::%s:%d MCTF: StartCount %d-%d-%d-%d, Idle %d-%d-%d-%d-%d-%d
0014c7dc  %s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld-%lld trigger: %d-%d-%d
0014c821  %s::%s:%d hMCTFCmdQueue %d, cmd->client_id %llu
0014c851  %s::%s:%d mctf_HMESC %lld: StartCount %d-%d-%d-%d
0014c883  %s::%s:%d mctf_LRMEFS %lld: StartCount %d-%d-%d-%d
0014c8b6  %s::%s:%d mctf_LRMERC %lld: StartCount %d-%d-%d-%d
0014c8e9  %s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d-%d
0014c91a  %s::%s:%d No command ready to process!
0014c95d  %s::%s:%d DMV HANG: %d %d
0014c977  %s::%s:%d HMESC HANG: %d %d
0014c993  %s::%s:%d LRME HANG: %d %d
0014c9ae  %s::%s:%d LRMERC HANG: %d %d
0014c9cb  %s::%s:%d PIPE HANG: %d %d
0014c9e6  %s::%s:%d XCODE HANG: %d, %d
0014ca04  %s::%s:%d Abnormal heart beat time!!! %lld %lld %lld %lld
0014ca3f  Error: HW HANG 0x%x
0014ca53  uClientIndex < AVE_FW_CONST::kMaxNumberOfClients
0014ca9c  hClientQueue.client(uClientIndex) != NULL
0014cac6  %s::%s:%d encCmdBufPool of client_idx %u is empty!
0014caf9  (uClientIndex < AVE_FW_CONST::kMaxNumberOfClients) && (pCmd != NULL)
0014cb59  %s::%s:%d Enter %d
0014cb6c  %s::%s:%d Try to release duplicated buffer in encCmdBufPool of client_idx %u!
0014cbba  %s::%s:%d  encCmdBufPool of client_idx %u is full!
0014cbee  %s::%s:%d Exit %d %d
0014cc03  FFWMSG_TYPE_GET(pMsg) == FFWMSG_TYPE_DATA
0014cc43  pNotificationMsg->id < NOTIFICATION_TOT
0014cc6b  %s::%s Enter %zu %p
0014cc7f  tmpHMESCCmd
0014cc8b  %s::%s:%d get NOTIFICATION_GET_HMESC_CONTINUE signal, for client %lld
0014ccd1  hClientQueue.GetIDFromIndex(ch) == tmpHMESCCmd->client_id
0014cd0b  CFSM::Get(fsmHmeSC) == GETTINGHMESCSTATS
0014cd34  %s::%s:%d get NOTIFICATION_GET_HMESC_STATS_DONE signal, for client %lld
0014cd7c  %s::%s:%d get NOTIFICATION_GET_DMV_STATS_DONE signal, for client %lld
0014cdc2  hClientQueue.GetIDFromIndex(ch) == sCurrDMVCmd.client_id
0014cdfb  CFSM::Get(fsmDMV) == GETTINGDMVSTATS
0014ce20  tmpLRMECmd
0014ce2b  %s::%s:%d get NOTIFICATION_GET_LRME_CONTINUE signal, for client %lld
0014ce70  hClientQueue.GetIDFromIndex(ch) == tmpLRMECmd->client_id
0014cea9  CFSM::Get(fsmLrme) == GETTINGLRMESTATS
0014ced0  %s::%s:%d get NOTIFICATION_GET_LRME_STATS_DONE signal, for client %lld
0014cf17  currPipeEncCmd.Get()
0014cf2c  %s::%s:%d get NOTIFICATION_GET_ENC_PIPE_CONTINUE signal, for client %lld
0014cf75  hClientQueue.GetIDFromIndex(ch) == currPipeEncCmd->client_id
0014cfb2  CFSM::Get(fsmEncPipe) == GETTINGENCPIPESTATS
0014cfdf  %s::%s:%d get NOTIFICATION_GET_ENC_PIPE_STATS_DONE signal, for client %lld
0014d030  tmpPIPECmd
0014d03b  %s::%s:%d get NOTIFICATION_GET_STF_PIPE_CONTINUE signal, for client %lld
0014d084  hClientQueue.GetIDFromIndex(ch) == tmpPIPECmd->client_id
0014d0bd  CFSM::Get(fsmStfPipe) == GETTINGSTFPIPESTATS
0014d0ea  %s::%s:%d get NOTIFICATION_GET_STF_PIPE_STATS_DONE signal, for client %lld
0014d135  currTranscodeEncCmd.Get()
0014d14f  %s::%s:%d get NOTIFICATION_GET_TRANSCODE_STATS_DONE signal, for client %lld
0014d19b  hClientQueue.GetIDFromIndex(ch) == currTranscodeEncCmd->client_id
0014d1dd  CFSM::Get(fsmTranscode) == GETTINGTRANSCODESTATS
0014d20e  %s::%s:%d %p get NOTIFICATION_GET_TRANSCODE_CONTINUE signal, for client %lld
0014d25b  tmpLRMERCCmd
0014d268  %s::%s:%d get NOTIFICATION_GET_LRMERC_CONTINUE signal, for client %lld
0014d2af  hClientQueue.GetIDFromIndex(ch) == tmpLRMERCCmd->client_id
0014d2ea  CFSM::Get(fsmLrmeRC) == GETTINGLRMERCSTATS
0014d315  %s::%s:%d get NOTIFICATION_GET_LRMERC_STATS_DONE signal, for client %lld
0014d35e  %s::%s Exit %zu %p %d
0014d374  %s::%s Enter %p %d %p
0014d38a  %s::%s:%d CMD %d %d | %d 0x%x | CID %llu CNT %llu
0014d3bc  insize == sizeof(struct sCAveCmdReset)
0014d3e3  insize == sizeof(struct sCAveCmdConfig)
0014d40b  insize == sizeof(struct sCAveCmdOpen)
0014d431  %s::%s:%d Not Supported EncType %d
0014d454  %s::%s:%d Not Supported Client Type %d
0014d47b  insize == sizeof(struct sCAveCmdStop)
0014d4a1  insize == sizeof(struct sCAveCmdFlush)
0014d4c8  insize == sizeof(struct sCAveCmdClose)
0014d4ef  insize == sizeof(struct sCAveCmdComplete)
0014d519  insize == sizeof(struct sCAveCmdPriority)
0014d543  insize == sizeof(struct sCAveCmdHalt)
0014d569  %s::%s Exit %p %d %p %d
0014d581  SignalProcessor
0014d591  hClientQueue.client(clientIndex) != NULL
0014d5ba  %s::%s:%d HMESC done!
0014d5d0  %s::%s:%d LRME done!
0014d5e5  %s::%s:%d DMV done!
0014d5f9  %s::%s:%d LRMERC done!
0014d610  %s::%s:%d Pipe done!
0014d625  %s::%s:%d AVC Transcode done!
0014d643  %s::%s:%d HEVC pipe done!
0014d65d  %s::%s:%d HEVC Transcode done!
0014d67c  %s::%s:%d Stf pipe done!
0014d695  %s::%s:%d Transcode Error!
0014d6b0  %s::%s :: Process PIO DMA Signal!
0014d6d2  ProcessQueue
0014d6df  client != NULL
0014d6ee  hCtrl != NULL
0014d6fc  client->WorkType() == AVE_WorkType_Enc
0014d723  currEncCmd.cmdQueueCmdIndex != 0
0014d744  stopCmd.client_id != CAVECommonController::kInvalidClientID
0014d780  clientIndex == hClientQueue.GetClientIndexFromID(stopCmd.client_id)
0014d7c4  resetCmd.client_id != CAVECommonController::kInvalidClientID
0014d801  resetCmd.pCmd != NULL
0014d817  %s::%s:%d RESET: hEncCmdQueue is supposed to be empty by now
0014d854  %s::%s:%d RESET: hEncCmdQueue is empty
0014d87b  %s::%s:%d RESET: DMV Cmd is supposed to be empty by now
0014d8b3  %s::%s:%d RESET: DMV Cmd is empty
0014d8d5  ##################### FIRST PASS #######################
0014d910  ##################### SECOND PASS #######################
0014d94a  %s::%s:%d StartCount %d-%d-%d-%d, HW %d-%d-%d-%d-%d
0014d97e  %s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld-%lld CTX %d-%d-%d-%d-%d
0014d9c3  %s::%s:%d MCTF_Client IDs %lld-%lld-%lld-%lld-%lld 
0014d9f7  %s::%s:%d Mctf_Cmds %p %p %p %p %p | %d %d %d %d | %d %d %d
0014da33  %s::%s:%d StartCount %d, HW %d, Client ID %lld
0014da62  %s::%s:%d Invalid State Change
0014da81  CmdQuickCallback
0014da92  rcLocal == 0
0014daa3  ProcessCmd_Config
0014dab5  Config %lld
0014dac1  AvePipeISRManager
0014dad3  hAvePipeISRManager
0014dae6  McpuController
0014daf5  hMcpuCtrl != NULL
0014db07  ProcessCmd_Open
0014db17  %s %lld %lld
0014db24  ProcessCmd_Start_AVC
0014db39  %s %lld %lld %d
0014db49  %s::%s:%d  Create client error: client_id: %lld, CAVE_CMD_AVC_INIT!!!
0014db90  %s::%s:%d  client is not registered: client_id: %lld, AVE_Cmd_Start!!!
0014dbd8  %s::%s Enter 0x%llx
0014dbec  ProcessCmd_Start_HEVC
0014dc02  %s::%s:%d create client error: client_id: %lld
0014dc31  %s::%s:%d client is not registered: client_id: %lld
0014dc65  %s::%s Enter %lld %d %p
0014dc7d  ProcessCmd_Start
0014dc8e  %s::%s:%d SVEMap Core Num %d Core Idx %d
0014dcb7  %s::%s:%d SVEMap Core %d | %d %d
0014dcd8  %s::%s:%d Client %llu Mode %d %d %d
0014dcfc  %s::%s Exit %lld %d %p %d
0014dd16  ProcessCmd_Stop
0014dd26  %s::%s:%d  client is not registered: client_id: %lld
0014dd5b  %s::%s:%d %lld %d %lld
0014dd72  ProcessCmd_Process_LRME
0014dd8a  %s::%s:%d client %lld is not registered
0014ddb2  pEncCmdBuf
0014ddbd  %s::%s:%d client %lld failed to enqueue
0014dde5  ProcessCmd_Process_DMV
0014ddfc  %s::%s clientIndex %d
0014de12  ProcessCmd_Process_GGM
0014de29  %s::%s:%d: Client %lld is not registered
0014de52  hClientQueue.GetClientPriority(iClientId, &iTmpPriority) == true
0014de93  %s::%s:%d: Adjust Priority %lld %lld %d %d %lld
0014dec3  hClientQueue.client(iClientIdx) != NULL
0014def1  %s::%s:%d: Client %lld failed to enqueue
0014df1a  %s::%s: Exit %llu %d
0014df2f  %s::%s Enter %p %d %p %d %d %lld %lld
0014df55  SendCommandToQueue
0014df68  %s %lld | %d %d %d | %d %d %d %d
0014df89  %s::%s:%d %lld | %lld %d %d %d %d | %lld | %d %d %d | %d %d %d %d
0014dfcb  %s::%s Exit %p %d %p %d %d %lld %lld %d
0014dff3  ProcessCmd_Process_AVC
0014e00a  %s::%s:%d client is not registered %lld %lld
0014e037  hClientQueue.GetClientPriority(pCmd->client_id, &tmpPriority) == true
0014e07d  %s::%s:%d adjust piority %lld %lld | %d %d
0014e0a8  %s::%s:%d  Failed to Queue AVE_Cmd_Process for client_id: %lld %lld
0014e0ec  %s %lld 
0014e0f5  %s::%s Exit %d %lld %lld %lld %d
0014e116  ProcessCmd_Process_HEVC
0014e12e  Adjust Piority, client_id: %lld, frm# %lld, adjust piority: %d, %d
0014e172  %s %lld %d 
0014e17e  %s::%s Exit %d %lld %lld
0014e197  ProcessCmd_Process_MCTF
0014e1af  %s::%s:%d Adjust Priority %lld %lld %d %d %lld
0014e1de  pClient != NULL
0014e1ee  %s::%s:%d Failed to Queue AVE_Cmd_Process for client_id: %lld %lld
0014e231  %s %lld %d
0014e23c  %s::%s Exit %d %lld %lld 
0014e256  hClientQueue.IsClientRegistered(client_id)
0014e281  FlushQueueForClient
0014e295  %s::%s Enter %lld %lld
0014e2ac  currCmd.client_id == client_id
0014e2cf  %s::%s:%d drop AVE_Cmd_Reset
0014e2ec  %s::%s:%d unexpected command ID:%d
0014e310  %s::%s Exit %lld %lld
0014e326  ProcessCmd_Flush
0014e337  ProcessCmd_Close
0014e348  %s::%s:%d %llu %lld
0014e35c  %s::%s:%d Failed to enqueue %lld
0014e37d  ProcessCmd_Complete
0014e391  %s::%s:%d client %lld is not registered %lld
0014e3be  %s %d %lld
0014e3c9  ProcessCmd_Priority
0014e3dd  %s::%s:%d %lld %lld %d
0014e3f4  ProcessCmd_Reset
0014e405  %s::%s:%d %lld %lld
0014e419  ProcessCmd_Halt
0014e42c  %s::%s: controller already deleted
0014e481  ProcessEncDone
0014e4a5  %s::%s Enter %lld | %d %d %d
0014e4c2  %s::%s:%d %lld | %d %d | %d %llu
0014e4e3  %s::%s Exit %lld | %d %d %d
0014e4ff  !client->m_saSrcFrameRefCount[idx].bActive
0014e53f  client->m_saSrcFrameRefCount[idx].iRefCount >= 0
0014e58a  %s::%s Enter %lld
0014e59c  RegisterClient
0014e5ab  %s::%s Exit %lld
0014e5bc  CreateClient
0014e5c9  NotifCh
0014e5d1  clientIndex < hClientQueue.NumOfClients()
0014e5fb  DestroyClient
0014e609  hClientQueue.NumOfClients() <= AVE_FW_CONST::kMaxNumberOfClients
0014e64a  Failed to remove client with index: %d
0014e672  %s Enter %d %lld %lld 0x%08x %d %d
0014e695  NotificationToHost
0014e6a8  %s::%s Enter %d %lld %lld 0x%08x %d %d
0014e6cf  %s::%s:%d PostCmdSynchronous
0014e6ec  %s TIMEOUT waiting host ACK %lld %d %lld time %lld %lld
0014e724  %s::%s:%d TIMEOUT waiting host ACK  %lld %d %lld time %lld %lld
0014e764  %s::%s Exit %d %lld %lld 0x%08x %d %d
0014e78a  %s Exit %d %lld %lld 0x%08x %d %d
0014e7ac  pStats
0014e7cc  %s:%d [RC Check] %p %d %p %p %d %lld %lld %d %d
0014e7fc  AVE_StoreRCFrameStats
0014e812  %s:%d Enqueue failed: queue is full
0014e836  Enqueue
0014e83e  %s:%d Dequeue failed: queue is empty
0014e863  Dequeue
0014e86b  %s::%s:%d hmesc_ready %d, client_id = %lld, Idle %d-%d-%d-%d-%d
0014e8c9  ./AppleAVE2FW/Firmware/HwCtrl/CAVEHWEnginesScheduler.cpp
0014e902  hmeSCClient != NULL
0014e916  %s::%s:%d cid %lld StartCount %d-%d-%d-%d-%d-%d fID %d
0014e94d  %s::%s:%d canStartHmeSC %d, bSC %d cid %lld fid %d iNum %d
0014e988  %s::%s:%d bypass enc hmesc (chained) %p frm %d %lld
0014e9bc  %s::%s:%d hmesc %p frm %d iNum %d %lld-%d
0014e9e6  %s::%s:%d bDMVReady %d, client_id %lld, Idle %d
0014ea2c  pDMVClient != NULL
0014ea3f  %s::%s:%d bCanStartDMV %d, bSC %d cid %lld StartCount %d
0014ea79  %s::%s:%d DMV %p iNum %d %lld-%d
0014ea9a  %s::%s:%d lrme_ready %d, client_id = %lld, Idle %d-%d-%d-%d
0014eaf5  lrmeClient != NULL
0014eb08  pipeClient != NULL
0014eb1b  %s::%s:%d cid %lld StartCount %d-%d-%d-%d-%d fID %d
0014eb4f  %s::%s:%d cid %lld Frame %d lrmeSyncStateReady %d %s  %d
0014eb8d  Single
0014eb94  %s::%s:%d F %d, canStart %d, Bypass %d frameType %d LID %d workType %d
0014ebdb  %s::%s:%d canStartLrme %d, bSC %d cid %lld fid %d iNum %d
0014ec15  %s::%s:%d lrme %p frm %d iNum %d %lld-%d %d %d %d
0014ec47  %s::%s:%d bypass lrmefs %p frm %d iNum %d %lld-%d %d %d
0014ec7f  lrmeClient->WorkType() == AVE_WorkType_Enc
0014ecaa  lrmeClient->IsMctfBasedEncode()
0014ecca  lrmeRCClient != NULL
0014ecfd  %s::%s:%d LRMERC %lld: StartCount %d-%d-%d-%d-%d fID %d
0014ed51  mctf_currPipeCmd
0014ed62  Conccurent Mode check : F:%d : %d
0014ed84  xcClient != NULL
0014ed95  %s::%s:%d Pipe %lld: StartCount %d-%d-%d-%d-%d fID %d
0014edcb  %s::%s:%d %lld %d %d %d %d %d
0014ede9  %s::%s:%d cid %lld iNum %d eWorkMode %d pipeSyncStateReady %d pSC %d pTSC:%d
0014ee36  Enc ConcurrentMode:%d
0014ee4c  Unexpected enc_type: %d. Cannot map to pipe mode
0014ee9a  %s::%s:%d Transcode %lld: StartCount %d-%d-%d-%d-%d fID %d
0014eeec  %s::%s:%d PostXCODE %lld: StartCount %d-%d-%d-%d-%d fID %d
0014ef27  %s::%s:%d frame_id:%d xc_done %d %d %d %d
0014ef51  %s::%s:%d frame_id:%d: canFinishTranscode %d, xCount %d, pxCount %d
0014ef96  %s::%s:%d current frame ids %d %d %d %d
0014efbe  %s::%s:%d Increased post XC frame ID: %d frame_done %d
0014eff5  DMVClient != NULL
0014f007  PostDMVProcess
0014f016  %s::%s:%d PostDMV %lld: StartCount %d
0014f03c  mctf_hmeSCClient != NULL
0014f073  %s::%s:%d mctf_HMESC %lld: StartCount %d-%d-%d-%d, noisy %d, type %d
0014f0b8  mctf_lrmeClient != NULL
0014f0ef  mctf_lrmeRCClient != NULL
0014f128  mctf_pipeClient != NULL
0014f15d  currPipeEncCmd
0014f16c  %s::%s:%d mctf_Pipe %lld: StartCount %d-%d-%d-%d ex %d-%d %d
0014f1a9  Stf ConcurrentMode:%d
0014f1bf  pInPicParams->sFrameInfo.sGOPInfo.iFrameType == IMG_MCTF_FILTERING
0014f202  bStageSet
0014f20c  mctf_pipeClient->WorkType() == AVE_WorkType_Enc
0014f23c  LowLatency MCTF + Encode not supported in AVE
0014f26a  mctf_pipeClient->WorkType() == AVE_WorkType_MCTF
0014f29b  StartPipe client = %lld, frame = %d, pipeStartCount = %d
0014f2d5  pHMEScClient != NULL
0014f307  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, HMEScClient %lld, Ready %d
0014f362  pLRMEFSClient != NULL
0014f396  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, LRMEFSClient %lld, Ready %d (%d %d/%d/%d)
0014f400  pLRMERCClient != NULL
0014f434  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, LRMERCClient %lld, Ready %d (%d %d/%d/%d)
0014f49e  pPipeClient != NULL
0014f4ce  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, PipeClient %lld, Ready %d (%d-%d %d/%d/%d %d/%d/%d)
0014f542  pXcClient != NULL
0014f571  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, XcClient %lld, Ready %d (%d), EncPipe %d StfPipe %d
0014f5e5  pPostXcClient != NULL
0014f612  %s:%d: HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame %d-%d, PostXCClient %lld, Ready %d (%d)
0014f672  %s:%d: GGM frame done, HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame %d-%d, PostXCClient %lld
0014f6d3  StartEventHMESC
0014f6e3  %s::%s Enter %lld %p %d
0014f6fb  %s::%s:%d controller already deleted
0014f721  %s:%d %lld %lld
0014f731  ret == AVE_OK
0014f73f  StartEventLRMEFS
0014f750  StartEventDMV
0014f75e  StartEventLRMERC
0014f76f  %s::%s client_id %lld, cmd %p, mctf %d
0014f79d  StartEventEncPipe
0014f7af  %s::%s client_id %lld, cmd %p
0014f7ce  StartEventStfPipe
0014f7e0  %s::%s client_id %lld, cmd %p, pipe_mode %d
0014f80d  currTranscodeEncCmd
0014f821  StartEventTranscode
0014f835  %s::%s Enter %lld, cmd %p
0014f84f  DoneEventHMESC
0014f85e  %s::%s: controller already deleted
0014f881  h->hClientQueue.client(clientIndex) != NULL
0014f8ad  h->hAvePipeISRManager
0014f8c3  DoneEventLRMEFS
0014f8d3  pTmpClient->WorkType() == AVE_WorkType_Enc
0014f8fe  pTmpClient->IsMctfBasedEncode()
0014f91e  DoneEventDMV
0014f92b  DoneEventLRMERC
0014f949  DoneEventEncPipe
0014f95a  DoneEventStfPipe
0014f96b  pTmpClient->WorkType() != AVE_WorkType_MCTF
0014f997  h->currTranscodeEncCmd
0014f9ae  DoneEventTranscode
0014f9c1  slice %d pos 0x%08x
0014f9d6  size %d queue 0x%08x
0014f9ec  GetStatsEventHMESC
0014f9ff  %s::%s:%d Increased HMESC frame ID %d
0014fa25  %s::%s Frame is not done
0014fa3e  GetStatsEventLRMEFS
0014fa52  %s::%s:%d Increased LRMEFS frame ID %d frame_done %d
0014fa87  GetStatsEventDMV
0014fa98  h->getDMVStatsDone.frame_done
0014fab6  %s::%s Frame is done
0014facb  GetStatsEventLRMERC
0014fadf  CFlowControllerBase::%s:: Frame is not done!
0014fb0d  LRMERC done: %d %d
0014fb35  Increased PIPE frame ID: %d
0014fb52  %s::%s:%d Frame is not done!
0014fb84  tmpPIPECmd->frameType == IMG_MCTF_FILTERING
0014fbb0  %s:%d: GGM frame done, HwFlag 0x%x, StartCount %d-%d-%d-%d-%d-%d, Frame: %d-%d, PipeClient %lld
0014fc27  Increased XC frame ID: %d
0014fc42  ProcessPIODMA
0014fc70  Error: Failed to Queue AVE_Cmd_Process for client_id: %lld
0014fcab  %u:NumFilteredFrames:%u
0014fcc3  hCtrl->MCTF_GetExecStage(pCmdBufOut) == MCTF_Stage_Filtered
0014fd21  bOutputStageSet
0014fd31  pFrameInfo->GetExecStage() >= MCTF_Stage_Filtered
0014fd63  pCmdCounterInfo->iFrameNum == hCtrl->MCTF_GetFrameNumber(pCmdBufOut)
0014fda8  rt == AVE_OK
0014fdb5  MCTFStopProcess
0014fdc5  WARN: Received PIO DMA Copy Error signal
0014fdef  FillFWFrameStats
0014fe00  FillMctfFrameStats
0014fe13  m_queue->m_sFifo[m_position].m_pCmdBuf != NULL || m_queue->m_sFifo[m_position].m_eExecStage >= MCTF_Stage_Output
0014fe84  GetCmdBuf
0014fe8e  %s:%d CtxSched shared memory init timeout
0014feb8  AVE_CSC_Init
0014fec5  %s:%d stopping CtxSched time out %d %d 0x%x
0014fef1  AVE_CSC_Uninit
0014ff00  ./AppleAVE2FW/Firmware/Resource/PIODMA/AVE_PIODMACtrl.cpp
0014ff3a  CmdStatusLookup[tag].pCmdsDoneHandle != NULL
0014ff67  SetCmdSequence
0014ff76  Heartbeat Status 0x%x
0014ff8c  %s Enter %p
0014ff98  AVE_ApplyTunables
0014ffaa  %s:%d %s | wrong parameters %p %d
0014ffcc  psCfg != __null
0014ffdc  %s:%d %s | wrong tunables %p %d %d
0014ffff  psRegCfg->iAddr != (uint32_t)(-1)
00150021  %s Exit %p %d
0015002f  %s Enter %d %d
0015003e  AVE_Tunables_Set
0015004f  %s Exit %d %d
0015005d  %s:%d: maxClientBufferSize = %d, %zu-%zu-%zu-%zu-%zu
00150092  GetClientBufferSize
001500a6  ./AppleAVE2FW/Common/Utils/CAVEPriorityQueue.cpp
001500d7  signalAvail
001500e3  sSignalDescriptor
001500f5  notificationSema != (SEMA)0
00150111  %s::%s Enter %llu %d %d
00150129  ReorderFrames
00150137  command
0015013f  command && AVE_CheckEncCmd(command->pCmd)
00150169  m_useFirmwareRC
00150179  %s::%s Exit %llu 
0015018b  %s::%s:%d Enqueue failed: queue is full
001501b3  frameInfo
001501bd  %s::%s: pEncCmd->iHwFlag = 0x%x, iPFHWFlag = 0x%x
001501ef  EnqueueMCTFCmdQ
001501ff  IsGreaterOrEqual(m_start, m_end + m_iQueueSize) == false
00150238  %s %d %d | %d %lld %lld | %p %d %d %d %d | %d %d 0x%x
0015026e  %s::%s:%d | %d %d | %llu %u %u | %d %llu %llu %p | %d %d %d | %d %d 0x%x | %d
001502bc  %s::%s:%d Dequeue failed: queue is empty
001502e5  Dequeue %d %lld %lld | %p %d %d %d | %d %d 0x%x
00150315  %s::%s:%d %llu %u %u | %d %llu %llu %p | %d %d %d | %d %d 0x%x
00150354  %s B->P %d %lld %lld | %p %d %d | %d %d 0x%x 
00150382  Complete
0015038b  %s::%s:%d Complete B->P %llu %d %d | %d %lld %lld | %p %d %d | %d %d 0x%x
001503d5  clientIndex < AVE_FW_CONST::kMaxNumberOfClients
00150405  CAVEClient
00150410  enc_type <= AVE_EncType_Max
0015042c  clientBufferAvailableSize >= kClientBufferSize[iWorkType - 1]
0015046a  AVCController
00150478  HEVCController
00150487  GGMController
00150495  OFController
001504a2  DMVController
001504b0  m_AVEController != NULL
001504c8  MCTFSetMask:Pending mask 0x%x frame %u positiom %u already set
00150507  MCTFClearMask:Pending mask 0x%x frame %u positiom %u not set
0015055d  Mark noise free frame as can execute
00150582  index < AVE_FW_CONST::kMaxNumberOfClients
001505ac  GetIDFromIndex
001505d1  %s::%s:%d Warning : Client %llu already registered
00150604  %s::%s:%d No more space for new client:%llu
00150630  m_client_ids[m_numberOfClients] == 0
00150655  %s::%s:%d Client %lld is not registered
0015067d  UnregisterClient
0015068e  clientIndex >= m_numberOfClientsCreated
001506b6  m_clients[clientIndex] == NULL
001506d5  %s::%s:%d Client %llu unregistered from m_client_ids[%u]
0015070f  %s::%s Enter %p %p %llx %d %d %lld %d %d
00150738  %s::%s%d Client %lld already exists
0015075c  m_clients[m_numberOfClientsCreated] == NULL
00150788  Driver doesn't provide enough buffer to Firmware!
001507ba  %s::%s:%d client_id: %lld, index: %d, total clients: %d
001507f2  %s::%s Exit %p %p %llx %d %d %lld %d %d %d
0015081d  %s::%s:%d Requested client index not found:%d
0015084b  %s::%s:%d client index:%d, total clients:%d
00150877  m_clients[clientIndex] != NULL
00150896  GetClientPriority
001508a8  SetClientPriority
001508d1  SetClientMCTFEncode
001508e5  %s::%s:%d Client not found: %lld
00150906  %s::%s:%d client_id %lld cmdID %d
00150928  %s::%s:%d No command queue available to dequeue
0015095d  %s %d %lld %lld | %p %d %d %d | %d %d 0x%x
00150988  %s::%s:%d %lld %d %llu %d
001509a2  %s::%s:%d Enter %lld %lld
001509bc  %s::%s:%d Client not found %lld
001509dc  %s::%s:%d Exit %lld %lld %d
001509f8  Client %lld, F %d Queue %d 
00150a14  ConvertP
00150a1d  %s::%s:%d Client %lld F %d Queue %d
00150a41  command != NULL && command->canExecute == true
00150a70  %s::%s:%d msc %d enc %d | %d %d | %d %d %d | %d
00150aa4  %s::%s:%d %s | Fail to dequeue frame %d
00150ae3  bDequeued
00150aed  %s::%s:%d %s | Failed to enqueue frame %lld
00150b19  bEnqueueResult
00150b28  CAVEClient::CommandQueue
00150b41  CAVEPriorityQueue
00150b53  %s:%d sub_pic_cpb_params_present_flag not supported!!
00150b89  hrd_parameters
00150b98  %s:%d  FwHeaderWrite Overwriting sps_temporal_id_nesting_flag to true.
00150bdf  seq_parameter_set_rbsp
00150bf6  ./AppleAVE2FW/Common/Utils/Hevc_headers.cpp
00150c22  m_sSPS.sVUI.vui_parameters_present_flag == true
00150c52  m_sPPS.num_extra_slice_header_bits == 0
00150c7a  ./AppleAVE2FW/Common/Utils/MappedMemory.cpp
00150ca6  paddr != 0
00150cb1  MappedMemory
00150cbe  size != 0
00150cc8  status == RTK_ST_OK && aligned_vaddr
00150ced  status == RTK_ST_OK
00150d01  m_vaddr
00150d09  HwToTarget
00150d14  %s Enter %p %d %d %p
00150d29  AVE_AVC_UpdatePOClsbSliceType
00150d47  %s:%d %s | wrong frame type  %p %p %d %d %d
00150d79  %s Exit %p %d %d %p %d
00150d90  %s:%d %s | wrong parameters %p %p %p
00150db5  AVE_AVC_PrepareSliceHeader
00150dd0  psPPS != __null && psCommonParams != __null && psSyntaxPFCfg != __null
00150e32  AVE_HEVC_Update_POClsb_SliceType
00150e53  %s:%d %s | wrong frame type %p %d %d %p %d
00150e7e  AVE_HEVC_PrepareSliceHeader
00150e9a  psPPS != __null && psCommonParams != __null && psSlice != __null
00150ef3  %s:%d %s | wrong slice type %d %p %d
00150f18  %s Enter %p %p %d %d %d %d %p %p
00150f55  %s Exit %p %p %d %d %d %d %p %p %d
00150f99  Setup_HEVC_I_Frame
00150fac  Setup_HEVC_CRA_Frame
00150fe5  Setup_HEVC_P_Frame
00150ff8  %s:%d %llu F %d %d
0015100b  %s:%d 0x%llx %d %d %d
0015104b  Setup_HEVC_B_Frame
0015107c  program_mvp_fw_regs
001510aa  ./AppleAVE2FW/Common/Utils/Slice_headers_util.cpp
001510e2  ./AppleAVE2FW/Common/Utils/SysUtil.cpp
00151109  *iIdx < AVE_HWE_EVENTS_MAX_NUM
00151128  AVE_EventTrace
00151137  AVE FW History Count: %lld
00151152  Index        Time         Client LogID  Line   FrameNum FrameType Debug info 
001511a0  %-12d %-12lld %-6d %-6d %-6d %-8d %-9d %s 
001511cb    Base addr: %p
001511e9  %s::%s Enter, %d 0x%x
001511ff  %s::%s Init MCPUs, %d 0x%x
0015121a  %s::%s Exit, %d 0x%x, %d
00151233  %s::%s Enter %d %d %d %p, 0x%x
00151258  %s::%s Start MCPUs, 0x%x
00151271  ./AppleAVE2FW/Firmware/Resource/MCPU/CAVEPipeMcpuController_Erebus.cpp
001512b8  %s::%s Exit %d %d %d %p, 0x%x %d
001512d9  %s::%s Enter, %d
001512ea  McpuInit
001512f3  MCPU_CandGen
00151300  MCPU_SrcStats
0015130e  MCPU_PipeSetup
0015131d  MCPU_SrcRelay
0015132b  MCPU_ModeDecision
0015133d  MCPU_ReconChroma
0015134e  MCPU_DebLf
00151359  MCPU_VLC
00151362  %s::%s Exit, %d
00151372  %s::%s Enter, 0x%x
00151385  %s::%s Stop MCPUs, 0x%x
0015139d  %s::%s Exit, 0x%x, %d
001513b3  %s::%s Enter %d %d %d %p
001513cc  StartAvePipe
001513d9  %s::%s Exit %d %d %d %p
001513f1  %s::%s Enter, %zu %zu %zu %p
0015140e  %s::%s Exit, %zu %zu %zu %p %d
00151448  %s::%s Exit, %d %d
00151472  ./AppleAVE2FW/Firmware/PMGR/AVE_PMGR_erebus.cpp
001514a2  AVE_PMGR_Set_erebus
001514b6  ./AppleAVE2FW/Firmware/Resource/CtxSched/AVE_CSC_ares.cpp
001514f0  RTK_ST_OK == status
00151504  AVE_CSC_InitMaibox_ares
0015151c  asc2cs_ipc
00151527  Halted Context Scheduler.
00151541  Msg %llu is not supported yet.
00151560  AVE_CSC_Mailbox_ISR
00151574  AVE_PMGR_Init
00151582  pDevInfo != __null
00151595  pPDMap != __null
001515a6  AVE_PMGR_Uninit
001515b6  AVE_PMGR_EnableDPM
001515c9  %s:%d %s | power management is not supported
001515f6  gs_sAVE_PMGR.psPDMap != NULL
00151613  AVE_PMGR_DisableDPM
00151627  %s Enter %p %d %d %d
0015163c  AVE_PMGR_SetPS
0015164b  %s Exit %p %d %d %d %d
00151662  %s Enter %d %d %d
00151674  SetPSDown
0015167e  %s Exit %d %d %d %d
00151692  SetPSDependencyDown
001516a6  %s Enter 0x%x %d %d
001516ba  CheckPeerDown
001516c8  %s Exit 0x%x %d %d %d
001516de  %s Enter %p %d
001516ed  CheckPDDepDown
001516fc  %s Exit %p %d %d
0015170d  %s Enter 0x%x %d
0015171e  CheckPSFlagDown
0015172e  %s Exit 0x%x %d %d
00151741  SetPSUp
00151749  SetPSDependencyUp
0015175b  CheckPDDepUp
00151768  CheckPSFlagUp
00151776  SetPowerState
00151784  %s:%d %s | wrong parameters %d %d
001517a6  pd < AVE_PMGR_PD_Max && ps < AVE_PMGR_PS_Max
001517d3  %s:%d %s | power domain %s is not supported/enabled %d %d %d
00151810  gs_sAVE_PMGR.piPDMap[pd] >= 0
0015182e  %s:%d set power time out %d 0x%x
0015184f  %s:%d %s | failed to set power state %s %s %d
0015187d  %s:%d set power state %s (%s <- %s)
001518a1  %s:%d keep power state %d %d
001518be  %s Exit %d %d %d
001518d6  MDINTRA
001518e1  MDINTER
001518f0  %s:%d Enter %d %d %d %d %d %d %d %d %d %d %p %d
00151920  AVE_Work_CalcHwPD
00151932  %s:%d Exit %d %d %d %d %d %d %d %d %d %d %p %d
00151961  %s Enter %p %p
00151970  AVE_DPM_Init
0015197d  pDevInfo != __null && pCfg != __null
001519a2  %s:%d %s | fail to init PSD %d
001519c1  %s:%d %s | fail to power on PSD %d
001519e4  %s:%d %s | no power domain mapping %p
00151a0a  %s:%d %s | fail to init PMGR %p %p
00151a2d  %s:%d %s | fail to enable DPM %p %p
00151a51  %s Exit %p %p %d
00151a62  AVE_DPM_Uninit
00151a71  %s:%d failed to disable PMGR %d
00151a91  %s:%d failed to uninit PMGR %d
00151ab0  %s:%d failed to power off %d
00151acd  %s:%d failed to destroy PSD %d
00151aec  %s Enter 0x%x
00151afa  AVE_DPM_TuneUpHw
00151b0b  %s:%d %s | fail to set power domain %d on
00151b35  %s Exit 0x%x %d
00151b45  AVE_DPM_TuneDownHw
00151b58  %s:%d %s | fail to set power domain %d off
00151b83  AVE_PSD_Init_ares
00151b95  %s:%d %s | fail to init PSD_AVE_SERVICE_CFG[0] %d
00151bc7  %s:%d %s | fail to init PSD_AVE_SERVICE_CFG[1] %d
00151bf9  %s Exit
00151c01  AVE_PSD_SetPS_ares
00151c14  slot < AVE_PSDSlot_Max && ps < AVE_PMGR_PS_Max
00151c43  %s enablePSDService %d %d %d
00151c60  %s:%d %s | fail to set power %d %d %d
00151c86  %s::%s Enter, id = %lu
00151c9e  CAvePipeMcpu
00151cab  ./AppleAVE2FW/MCPU/Image/common/CAvePipeMcpu_Erebus.cpp
00151ce3  %s::%s: MCPU ID error, cmp_mcpu_id = 0x%x, rd_mcpu_id = 0x%x
00151d21  %s::%s Exit, mid = %u
00151d37  %s::%s Enter, id = %zd, mid = %d
00151d58  ~CAvePipeMcpu
00151d66  %s::%s Exit, id = %zd, mid = %d
00151d86  %s::%s Enter, mid = %d
00151d9e  %s::%s Exit, mid = %d
00151db5  %s::%s Enter %d, %d %d 
00151dcd  StartUnit
00151dd7  %s::%s Exit %d, %d %d 
00151dee  bytes <= dmem_size_limit
00151e07  ReadDMem
00151e10  bytes <= imem_size_limit
00151e29  ReadIMem
00151e32  WriteDMem
00151e3c  WriteIMem
00151e5c  ./RTKit/ffw/CObject.cpp
00151e74  name != 0
00151e7e  OBJECT: %s child of %s
00151e96  OBJECT: %s
00151ea2    this = %p, children = %d, debug level = %d
00151ee3  ./RTKit/ffw/CRoot.cpp
00151ef9  instance == 0
00151f0d  ./RTKit/ffw/CRTOSObjectPool.cpp
00151f2d  tot == 0
00151f36  temp != 0
00151f40  RTK_queue_count(queue) == tot
00151f5e  object != NULL
00151f6d    pool = %d
00151f7a    in-use = %zu, watermark = %zu
00151f9b    free = %dzun
00151fab  ./RTKit/ffw/CResourcePool.cpp
00151fc9  maxres > 0
00151fd4  instance == NULL
00151fe5  instance != 0
00151ff3  ./RTKit/ffw/CQueuePool.cpp
0015200e  maxqueue > 1
0015201b  instance == nullptr
00152040  ./RTKit/ffw/CBuffer.cpp
00152058  POST CONDITION: %s:%d %s
00152071  ok == true
0015207c  Release
00152084  ./RTKit/ffw/CGPIOManager.cpp
001520a1  tot > 0
001520a9    GPIO registers = %zu
001520c1  ./RTKit/ffw/CSemaphorePool.cpp
001520e0  maxsema > 0
001520ec  Not occurred, cannot say anything about waiting
0015211c  Occurred, cannot say anything about waiting
00152148  ./RTKit/ffw/CTimerPool.cpp
00152163  maxtimers > 0
00152171  super::Available() == (int)super::Managed()
0015219d  ./RTKit/ffw/CTimerManager.cpp
001521bb  started == false
001521cc  ~CTimerManager
001521db    [handle = %lu]
001521ed    started = %s
001521fd  YES [indefinite]
0015220e    started = YES [%ld to go]
0015222b    call-back = %p
0015223d    started = NO
0015224d    max period [ns] = %ld
00152266    min period [ns] = %ld
0015227f  ./RTKit/ffw/CISRManager.cpp
0015229b  irqLine != 0
001522a8  CISRManager
001522b4  source < ISR_REG_ENTRY
001522cb    Interrupts enabled: %s
001522ec    IRQs lines = %d
001522ff    Line %d IRQs = %zu
00152315      [%02d][%02d] count = %zu - registered callbacks = %zu
00152350  ./RTKit/ffw/CFSM.cpp
00152365  mutex != (RESOURCE)0
0015237f  list == 0
0015238f  %s:%d Error
0015239b  Create
001523a4  Delete
001523ab  h->signature == CFSM_SIGNATURE
001523ca    [%03d] %p - %s - state: %s
001523e8  PostCallback
001523f9  EventProcess
00152406  TransitionProcess
00152418  ./RTKit/ffw/CMMU.cpp
0015242d  logEntry != 0
00152446  UNWIRED
0015244e  FAILED WIRING
0015245c  FAILED UNWIRING
0015246c    Buffers operations = %zu
00152488        Wired: successful = %zu, failed = %zu
001524b5      UnWired: successful = %zu, failed = %zu
001524e2    LOG: Last %zu operations [total = %zu]:
0015250d     %6zu : %16s : vir = &p, phy = &p, len = %#08x [%zu]
00152545    LOG: There no wiring/unwiring operations
00152571  ./RTKit/ffw/CSharedMemory.cpp
0015258f  CSharedMemory::chMan != 0
001525a9  CSharedMemory
001525b7  signal != 0
001525cb  Malloc
001525d2  rtk_rc == FFW_OK
001525e8  MallocSynchronous
001525fa    Total number of successful allocations = %zu
0015262a    Number of outstanding allocations = %zu
00152655  ./RTKit/ffw/CSharedMemoryHeap.cpp
00152677  CSharedMemoryHeap
00152689  heapSize != 0
00152697  ./RTKit/ffw/CSharedMemoryHost.cpp
001526b9  chMan != 0
001526c4  dieRequest != (SEMA)0
001526da  CSharedMemoryHost
001526ec  synchronize != (SEMA)0
00152703  task != 0
0015270d  rc == FFW_OK
0015271a  RTK_ST_IS_SUCCESS(rc)
00152730  rtkrc == RTK_ST_OK
00152743  task != (TASK)0
00152753  ~CSharedMemoryHost
0015277d  ./RTKit/ffw/CTaskPool.cpp
00152797  maxtask > 1
001527a3  CQueuePool::Instance() != 0
001527bf  descr.list != 0
001527cf  CTaskPool
001527d9  TASKTERMINATOR
001527e8  entry->stack != NULL
00152801  descr.lock != (RESOURCE)0
0015281b  rc == RTK_ST_OK
0015282b  ~CTaskPool
00152836  priority >= RTK_THREAD_PRIORITY_MIN
0015285a  priority <= RTK_THREAD_PRIORITY_MAX
0015287e  IDLETASK
00152887  res == RTK_ST_OK
00152898  SpawnPrivate
001528a5  stack_ptr != NULL
001528b7  ((uintptr_t)entry->stack & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0
001528f6  (stacksize & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0
00152927  newTask != RTK_THREAD_NONE
00152942  entry->used == true
00152956  TerminateCallback
00152968  Terminate
001529ad  Stack Base
001529f7    in-use = %d, watermark = %d
00152a16    free = %d
00152a23    exchanged = %d
00152a35  ./RTKit/ffw/CSignalPool.cpp
00152a51  maxsig > 0
00152a5c  available == tot
00152a6d    free = %zu
00152a7b    exchanged = %zu
00152a8e  ./RTKit/ffw/CPipe.cpp
00152aa4  messages > 0
00152ab7  watermark_queue.Count() == 0
00152ad4  filter == (class CObject *)0
00152af1  semaphore == (SEMA)0
00152b06  pMsg != 0
00152b10  FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgBuffRef)
00152b49  FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgData)
00152b7f  FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgCmd)
00152bb4    pool messages = %d
00152bca    downstream filter = %p [%s]
00152be9  <NONE>
00152bf0    messages:
00152bfd      posted = %zu
00152c0f      exchanged = %zu
00152c24      in-use = %zu, watermark = %zu
00152c47      free = %zu
00152c57    buffer ref messages:
00152c6f  triggerLevel <= capacity
00152c88  ./RTKit/ffw/CMailboxPool.cpp
00152ca5  maxmbox > 0
00152cb1  ./RTKit/ffw/CIOObject.cpp
00152ccb  priority != 0
00152cd9  (inputs > 0) || (outputs > 0)
00152cf7  CTaskPool::Instance() != 0
00152d12  CSemaphorePool::Instance() != 0
00152d32  inputPipe != 0
00152d41  CIOObject
00152d4b  outputPipe != 0
00152d5b  buffPool != 0
00152d69  CMailboxPool::Instance() != 0
00152d87  stacksize != 0
00152d96  cmdSema != (SEMA)0
00152daf  cmdMboxSema != (SEMA)0
00152dc6  dieSema != (SEMA)0
00152dd9  cmdMbox != (MBOX)0
00152dec  semaArray[index] != (SEMA)0
00152e08  pin < inputs
00152e15  pin < outputs
00152e23  pin < buffPools
00152e33    Thread = %#x, priority = %d
00152e52    Command Mailbox semaphore = %#04x [%s]
00152e7c    Command reply semaphore = %#04x [%s]
00152ea4    Semaphores
00152ec2    Started = %s
00152ed2    Commands issued = %zu, processed = %zu %s
00152eff  [currently processing one]
00152f1a    Command log [Last issued first]:
00152f53      No commands issued so far.
00152f73    Processed signals = %zu
00152f8e    Processed messages = %zu
00152faa    Processed buffers = %zu
00152fc5    Processed data messages = %zu
00152fe6    Processed in-line commands = %zu
0015300a    Dropped messages = %zu
00153024    Dropped buffers = %zu
0015303d    Delivered Messages = %zu
00153059    inputs = %zu, max = %zu
00153074      pin [%02d] - pipe = %p (%s)
00153095    outputs = %zu, max = %zu
001530b1    buffer pools = %zu, max = %zu
001530d2      pin [%02d] - pool = %p (%s)
001530f3  CmdTaskDie
001530fe  deferredCmdAck == false
00153116  CmdProcess
00153121  processedCmdCounter == 0
0015313a  processCmdOnly == true
00153156  InputProcess
00153163  MMUManager
0015316e  ./RTKit/ffw/CEnvironment.cpp
0015318b  CEnvironment
00153198  bootArgs != 0
001531a6  gpTimerArray != 0
001531b8  mboxPool != 0
001531c6  semaPool != 0
001531d4  resPool != 0
001531e1  queuePool != 0
001531f0  tree_resource != 0
00153203  heap_resource != 0
00153216  Restart count : %d
0015322a  Platform : mode = %s, ID = %#08x, HW = %08x.%08x
00153261  TARGET
00153268  System Clock : %zu Hz
0015327f  Data Cache Line Size: %u [%#x]
0015329f  Instruction Cache Line Size: %u 
001532c1  MMU Page Size: %zu bytes
001532db  Boot arguments entries : %u
00153337  Main memory :   base : %p
00153352                  size : %zu [%#08lx] [%zu.%zu MB]
00153384  Extra heap :    base : %p [phy = %p]
001533aa  Shared memory : base : %p 
001533c6  TEXT : %zu [%#zx] - text %zu, cstring  %zu, const %zu
001533fd  DATA : %zu [%#zx] - data %zu, bss %zu, common %zu, noinit %zu
0015343c  Heap free space : %zu [%#08zx]
0015345c  Heap allocated space : %zu [%#08zx]
00153481  Disclaimer : %s
00153492  Application : %s [%s]
001534a9  Release : %s
001534b7  FW version : %s
001534c8  Tool-chain : %s - %s [%s]
001534e3  CSharedMemory::Instance() != 0
00153502  ExtraHeapAdd
0015350f  extra_heap_base != 0
00153524  mboxPool == 0
00153532  MailboxPool
0015353e  queuePool == 0
0015354d  QueuePool
00153557  resPool == 0
00153564  ResourcePool
00153571  ResourceManager
00153581  heap_resource != (RESOURCE)0
0015359e  tree_resource != (RESOURCE)0
001535bb  semaPool == 0
001535c9  SemaphorePool
001535d7  sigPool == 0
001535e4  SignalPool
001535ef  taskPool == 0
001535fd  TaskPool
00153606  TimerPool
00153610  ./RTKit/ffw/CChannelManager.cpp
00153630  maxchannels != 0
00153641  array != 0
0015364c  CChannelManager
0015365c  dieRequest != 0
0015366c  rc == true
00153677  interruptTimerSignal != 0
00153691  array[index].inuse == false
001536ad  ~CChannelManager
001536be  array[index].ch == 0
001536d3  pool == ALIGN_DOWN(pool, (size_t)RTK_cache_get_line_size())
0015370f  entries > 0
0015371b  array[index].ch != 0
00153730  handle != 0
0015373c  Unregister
00153747  interruptTimer != 0
0015375b  DoorBellCadenceSet
0015376e  interruptTimer != NULL
00153785    Max channels = %d
0015379a    Thread priority = %d
001537b2    Signal semaphore = %#x
001537cc    Die request semaphore = %#x
001537eb    Doorbell cadence = %d us
00153818  [UNIDIRECTIONAL]
00153829      IOP ch = %p, slots = %d
00153846      tx = %ld [out = %d]
00153877  ./RTKit/ffw/CController.cpp
00153893  h2tchIOMan != 0
001538a3  semaArray[SIGNAL_CHANNEL_INTERNAL] != (SEMA)0
001538d1  cmdSynchronizationSema != (SEMA)0
001538f3  semaArray[SIGNAL_CHANNEL_COMMAND] != (SEMA)0
00153920  semaArray[SIGNAL_CHANNEL_T2H] != (SEMA)0
00153949  semaArray[SIGNAL_CHANNEL_PROCESS_QUEUE] != (SEMA)0
0015397c  semaArray[SIGNAL_CHANNEL_HEARTBEAT] != (SEMA)0
001539ab  semaArray[SIGNAL_CHANNEL_PERIODIC_PROCESS] != (SEMA)0
001539e1  signalAvail == true
001539f5  instance->ch != 0
00153a07  TaskWrapper
00153a13  instance->chT2H != 0
00153a28  CmdInternalProcess
00153a3b  CmdInternal
00153a73  TriggerProcessQueue
00153a87  PeriodicProcess
00153a97  message != 0
00153aa4  insize > 0
00153aaf  outsize != 0
00153abc  PostCmdSynchronous
00153acf  %s::%s:%d Error: ACK %d %d %d %p %p
00153af3  %s::%s:%d  Thread = %p, priority = %d
00153b1f  %s::%s:%d  chMan = %p, [%s], index = %zu
00153b4e  %s::%s:%d  chManT2H = %p, [%s], index = %zu
00153b7b  %s::%s:%d  Semaphores =
00153ba4  %s::%s:%d  Processed commands = %zu
00153bc9  %s::%s:%d  Processed signals = %zu
00153bed  CController
00153bf9  ./RTKit/ffw/CFilter.cpp
00153c11  ./RTKit/ffw/CTerminalOut.cpp
00153c2e  CTerminalOut
00153c3b  Output
00153c42  ./RTKit/ffw/CLoggerInterProcessor.cpp
00153c68  pool != (void *)0
00153c7a  Channel
00153c82  ./RTKit/ffw/CScopedLock.cpp
00153c9e  lock != nullptr
00153cae  CScopedLock
00153cba  Exception !! crash type %d
00153cd5  [Call stack]
00153ce2    0x%016llX
00153cee  [Registers]
00153cfa    pc    0x%016llX  psr   0x%016llX
00153d1d    far   0x%016llX  esr   0x%016llX
00153d40    lr    0x%016llX  sp    0x%016llX
00153d63  SCRATCH_REG32_RD: addr %016lx value %08x
00153d8c  SCRATCH_REG32_WR: addr %016lx value %08x
00153db5  ./RTKit/platform/common/CDockChannel.cpp
00153dde  RTK_ST_OK == tStatus
00153df3  RTK_DockChannel_init
00153e08  ./RTKit/platform/common/CFakeChannel.cpp
00153e31  CFakeChannel::chDescr
00153e47  CFakeChannel
00153e54  ./RTKit/platform/common/ChannelTable.cpp
00153e7d  sharedMem != 0
00153e8c  ChannelTableAlloc
00153e9e  SHAREDMALLOC
00153eab  TERMINAL
00153eb4  System Thread
00153ec7  ./RTKit/platform/common/CPlatformEnvironment.cpp
00153f0d  ISRManager
00153f18  IPIManager
00153f23  GPTimer0
00153f2c  gpTimerArray[0] != 0
00153f41  SharedMemoryHost
00153f52  SharedMemoryManager
00153f66  FSMMan
00153f6d  FW: AppleAVE2FW-%s
00153f8a  failed to get dev info
00153fa6  ./RTKit/platform/common/CPlatformGPIOManager.cpp
00153fd7  index < tot
00153fee    base address = %p
00154003  Register
0015400c  ./RTKit/platform/common/CPlatformISRManager.cpp
0015403c  source >= 0
00154048  id < INT_NROF_VECTORS
00154066  source < PLATFORM_INT_SOFTWARE_COUNT
001540a3  isr_man != NULL
001540b3  CPlatformISRManager
001540c7  %s:%d unsupported %p
001540dc  AVE_CallbackWrap
001540ed  ./RTKit/platform/common/CRealChannel.cpp
00154116  CRealChannel
00154123  ./RTKit/platform/common/FakeChannelTable.cpp
00154150  FakeChannelCreate
00154162  tot != 0
0015416b  ChManTarget
00154177  ChManHost
00154187  ./RTKit/platform/common/RealChannelTableTarget.cpp
001541d2  (shared_mem_paddr & (RTK_MMU_PAGE_SIZE - 1)) == 0
00154204  shared_mem_size != 0 && (shared_mem_size & (RTK_MMU_PAGE_SIZE - 1)) == 0
0015424d  status == RTK_ST_OK && memoryMappings->shared_mem_vaddr != NULL
0015428d  (extra_heap_paddr & (RTK_MMU_PAGE_SIZE - 1)) == 0
001542bf  (*extra_heap_size & (RTK_MMU_PAGE_SIZE - 1)) == 0
001542f1  status == RTK_ST_OK && memoryMappings->extra_heap_vaddr != NULL
00154331  channel_mem != 0
00154342  *extra_heap_size >= extra_heap_size_min
0015436a  entry != 0
00154375  ./RTKit/platform/common/IOP/AVE_IOP_panda.cpp
001543a3  AVE_IOP_Config_panda
001543b8  !MIDR: 0x%x
001543c4  ~CsPTR
001543cb  !ROf %#lx %#x
001543d9  MMU out of tables: %zu,%zu
001543f4  MMU private: s:%llx!=%llx b:%llx!=%llx
0015441b  MMU VA sz %u 0=%zu 1=%zu
00154434  MMU private !fit: b:%lx<%lx s:%lx>%lx
0015445a  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
00154487  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
001544b9  MMU sh<ps: %llu > %llu
001544d0  Page Table !vm export: %x
001544ea  GPTBAT !vm export: %x
00154500  PPL handoff !vm export: %x
0015451b  MMU invalid page size: %x
00154535  CXXnew:%zu
00154540  CXXnew[]:%zu
0015454d  RTKit: %s - Client: %s
00154564  !Mthd:%p
0015456d  !msgmbxint
00154578  !msgdoordashint
00154588  mme:0x%x
00154591  !Heapblk:%p
0015459d  ThIntr:%u,%u,%u,%u
001545b0  ThLock:%p
001545ba  Terminator
001545c5  VmOv %d %d
001545d0  !vm nodes
001545e2  Duty cycle
001545f3  Sleep count
001545ff  Wake count
0015460a  Power state
00154616  Free heap
00154620  Total heap
0015462b  Peak heap alloc
0015463b  Used stack
00154646  Total stack
00154652  CPU count
00154663  Thread time
0015466f  Performance
0015467b  IRQ disabled time
0015468d  !ASLRHeapAlign
0015469c  <null>
001546a6  CXXPureVirt
001546b2  rtk_ep_work
001546be  MGMT msg=0x%llx st=%x
001546d4  MGMT st=%x
001546e4  MBI queue overflow:%s
001546fa  Unbalanced transients
00154710  Invalid AP power: %d
00154726  rtkpsd_platform_default.cpp
00154742  %s: Invalid client
00154755  initClientConfig
00154766  Invalid numServiceSlots: 0x%x
00154784  %s:client not init
00154797  getServiceName
001547a6  %s: invalid param
001547b8  %s: Invalid slot pio index for client: %#x service: %#x
001547f0  %s: invalid id: %u
00154803  getResetSendPayload
00154817  %s: invalid payload ptr
0015482f  Client not initialized!!
00154848  Latency to P State Translation Failed
0015486e  Invalid slot pio index for client: %#x service: %#x
001548a2  %s: client not init
001548b6  initServiceConfig
001548c8  %s: Invalid initConfig
001548df  %s: serviceId 0x%x already initialized
00154906  getNumServiceSlots
00154919  getServiceConfig
0015492a  %s: Error Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
00154971  %s: Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
0015499c  rtkpsd_common.cpp
001549ae  %s: getServiceConfig(0x%x) err: 0x%x
001549d3  _initServiceDashboard
001549e9  %s: Unsupported service id: 0x%x
00154a0a  %s:RTK dev init(0x%x) fail: 0x%x
00154a2b  %s:RTK dev config(0x%x) fail: 0x%x
00154a4e  %s:RTK dev wake(0x%x) fail: 0x%x
00154a6f  %s: Not support PSD ACK mode: %d
00154a90  _stateChange
00154a9d  %s: Prev req pending service=0x%x wrVal=0x%x: 0x%x
00154ad0  %s: Prev reqs caused sem signal service=0x%x wrVal=0x%x: 0x%x
00154b0e  PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x) prevRdVal: (%#x) timeout after %llu usec
00154b80  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) sem wait err: (%#x)
00154bce  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) != rdVal: (%#x) err
00154c1c  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x)
00154c63  _getPowerStateVote
00154c76  %s: client=0x%x service=0x%x err: 0x%x
00154c9d  %s: clientId=0x%x serviceId=0x%x pstate=%d
00154cc8  %s: initClientConfig err: 0x%x
00154ce7  initPSDService
00154cf6  %s: initServiceConfig err: 0x%x
00154d16  %s: initServiceDashboard err: 0x%x
00154d39  %s: done clientId=0x%x serviceId=0x%x
00154d5f  %s: clientId=0x%x serviceId=0x%x active=%u ltr_usec=%u
00154d96  enablePSDService
00154da7  %s: getNumServiceSlots err: 0x%x
00154dc8  %s: invalid params
00154ddb  %s: stateChange(serviceId 0x%x) err: 0x%x
00154e05  %s: clientId=0x%x serviceId=0x%x
00154e26  getPSDServiceVote
00154e38  %s: _getPowerStateVote(serviceId 0x%x) err: 0x%x
00154e69  %s: Reset already initialized
00154e87  initPSDReset
00154e94  %s: routingEpId=0x%x
00154ea9  %s: Reset not initialized
00154ec3  sendPSDReset
00154ed0  %s: getResetSendPayload err: 0x%x
00154ef2  %s: Start - routingEpId=0x%x id=0x%x payload=0x%llx
00154f26  %s: MBI send msg timeout (routingEpId=0x%x id=0x%x)
00154f5a  %s: MBI send msg err (routingEpId=0x%x id=0x%x): 0x%x
00154f90  %s: MBI recv msg timeout (routingEpId=0x%x id=0x%x)
00154fc4  %s: MBI recv msg err (routingEpId=0x%x id=0x%x): 0x%x
00154ffa  %s: checkResetRcvdPayload err: 0x%x
0015501e  %s: Done - routingEpId=0x%x id=0x%x payload=0x%llx
00155058  setPSDLogLevel
00158240  Copyright (c) Apple Inc. All Rights Reserved.
00158272  iPhone OS
00158281  clang/clang++
00158294  release
0015829c  AppleAVE2FW-9013.55.1.debug
00158f50  tTxEhTTRc
00158fa8  tTDPhTTR{
00159110  lCytuDTR
00159168  tnCplSTR
001591c0  tnCkaWTR
00159218  tffOnOTR
00159270  EERFPHTR
001592c9  LLAPHTR 
00159320  KAEPPHTR+
0015937a  UKTSTR;
001593d2  AKTSTRF
00159428  UPCmuNTRR
0015dcb8  CPS_M2A
0015dd08  PACC_CLUSTER
0015dd58  EACC_CLUSTER
0015dda8  GPU_CLUSTER
0015ddf8  IBOOT_P0
0015de48  SIO_UART0
0015de98  SIO_UART1
0015dee8  SIO_UART2
0015df38  SIO_UART3
0015df88  SIO_UART4
0015dfd8  SIO_UART5
0015e028  SIO_I2C0
0015e078  SIO_I2C1
0015e0c8  SIO_I2C2
0015e118  SIO_I2C3
0015e168  SIO_I2C4
0015e1b8  SIO_QSPI
0015e208  SIO_SPI0
0015e258  SIO_SPI1
0015e2a8  SIO_SPI2
0015e2f8  SIO_SPI3
0015e348  SIO_SPI_DMASHIM
0015e398  SIO_UART_DMASHI
0015e3e8  IBOOT_DCP_SEC
0015e438  SIO_CPU_BLOCKIN
0015e488  SIO_AES
0015e4d8  ANE0_CPU_0
0015e528  ANE0_SYS_0
0015e578  ANE1_CPU_0
0015e5c8  ANE1_SYS_0
0015e618  ISP_CPU_BLOCKIN
0015e668  ISP_FE_0
0015e6b8  ISP_SENSE0
0015e708  ISP_SENSE1
0015e758  DISP_CPU_0
0015e7a8  DISP_SMB0_0
0015e7f8  DISP_SMB1_0
0015e848  DISP_DP_0
0015e898  DISPSEC_CPU_0
0015e8e8  DISPSEC_SMB0_0
0015e938  DISPSEC_SMB1_0
0015e988  DISPSEC_DP_0
0015e9d8  EDISP0_CPU_0
0015ea28  EDISP0_DP_0
0015eac8  MSR_BLOCKING
0015eb18  AVD_BLOCKING
0015eb68  AVE_CPU_BLOCKIN
0015ebb8  APCIE_GP
0015ec08  APCIE_GP0_0
0015ec58  PRORES
0015eca8  AON_ATC0_COMMON
0015ecf8  AON_ATC0_USB_AO
0015ed48  AON_ATC_USB
0015ed98  DBG_AVE_ALL
0015ede8  DBG_DISP_ALL
0015ee38  DBG_ISP_ALL
0015ee88  DBG_ANS_ALL
0015eed8  DBG_ANE_ALL
0015ef28  DBG_MISC_ALL
0015ef78  GPU_ASC0
0015efc8  GPU_ASC1
0015f018  APCIE_GP1_0
0015f068  IBOOT_DCP
0015f0b8  ANE0_CPU_BLOCKI
0015f108  ANE1_CPU_BLOCKI
0015f158  ANE0_BASE_0
0015f1a8  ANE1_BASE_0
0015f1f8  PIO_NONE_0
0015f248  PIO_NONE_1
0015f298  PIO_NONE_2
0015f2e8  IBOOT_DCP_EXT
0015f338  PIO_NONE_3
0015f388  DISP_CPU_1
0015f3d8  ANE0_CPU_1
0015f428  ANE1_CPU_1
0015f478  ISP_CPU_0
0015f4c8  DISPSEC_CPU_1
0015f518  APCIE_GP0_1
0015f568  APCIE_GP1_1
0015f5b8  DISP_CPU_2
0015f608  ANE0_CPU_2
0015f658  ANE1_CPU_2
0015f6a8  ISP_CPU_1
0015f6f8  DISPSEC_CPU_2
0015f748  APCIE_GP0_2
0015f798  APCIE_GP1_2
0015f7e8  ANE0_SYS_1
0015f838  ANE1_SYS_1
0015f888  ANE0_CPU_3
0015f8d8  ANE1_CPU_3
0015f978  DISP_CPU_3
0015f9c8  DISPSEC_CPU_3
0015fa18  SIO_CPU
0015fa68  DISP_CPU_4
0015fab8  DISP_PIPELINE
0015fb08  DISP_RCA
0015fb58  DISP_OLED
0015fba8  AON_DISP_DSG_PR
0015fbf8  DISP_SMB0_1
0015fc48  DISP_SMB1_1
0015fc98  DISP_DP_1
0015fce8  DISP_DBE
0015fd38  DISP_SPI
0015fd88  DISP_DP_PHY
0015fdd8  DISP_MIPI_0
0015fe28  AON_DISP_HPD_PR
0015fe78  EDISP0_CPU_1
0015fec8  EDISP0_DBE
0015ff18  PIO_NONE_4
0015ff68  EDISP0_DP_1
0015ffb8  PIO_NONE_5
00160008  ISP_CPU_2
00160058  ISP_STS0
001600a8  ISP_STS1
001600f8  ISP_DPRX
00160148  ISP_PEARL
00160198  ISP_CVD
001601e8  ISP_CLR
00160238  ISP_SECURE
00160288  ISP_FE_1
001602d8  ISP_BE
00160328  ANE0_CPU_4
00160378  ANE0_BASE_1
001603c8  ANE0_MPM
00160418  ANE1_CPU_4
00160468  ANE1_BASE_1
001604b8  ANE1_CPU_5
00160508  ANE1_BASE_2
00160558  ANE1_MPM
001605a8  ANE0_CPU_5
001605f8  ANE0_BASE_2
00160648  AVE_CPU
00160698  AVE_PIPE
00160788  DISPSEC_CPU_4
001607d8  DISPSEC_PIPELIN
00160828  DISPSEC_RCA
00160878  DISPSEC_OLED
001608c8  AON_DISPSEC_DSG
00160918  DISPSEC_SMB0_1
00160968  DISPSEC_SMB1_1
001609b8  DISPSEC_DP_1
00160a08  DISPSEC_DBE
00160a58  DISPSEC_SPI
00160aa8  DISP_SEC_DP_PHY
00160af8  DISP_MIPI_1
00160b48  AON_DISPSEC_HPD
0028b0a4  _AVC_qp2LambdaSSD
0028b0b6  _AVE_DevCap_Find
0028b0c7  _AVE_History_Add
0028b0d8  _AVE_History_Create
0028b0ec  _AVE_History_Destroy
0028b101  _AVE_History_Print
0028b114  _AVE_Log_CheckLevel
0028b128  _AVE_Log_Init
0028b136  _AVE_Log_Output
0028b146  _AVE_Log_Uninit
0028b156  _AVE_SNPrintf
0028b164  _AVE_VSNPrintf
0028b173  _BitReverseTable256
0028b187  _GetApplication
0028b197  _GetCompileMode
0028b1a7  _GetDisclaimer
0028b1b6  _GetRTKClientVersion
0028b1cb  _GetRelease
0028b1d7  _GetToolchainName
0028b1e9  _GetToolchainType
0028b1fb  _GetToolchainVersion
0028b210  _IOProcessorChannelCreate
0028b22a  _IOProcessorChannelDelete
0028b244  _IOProcessorChannelMessageAvailable
0028b268  _IOProcessorChannelReceive
0028b283  _IOProcessorChannelSend
0028b29b  _IOProcessorChannelStats
0028b2b4  _IOProcessorChannelUnidirectionalReceive
0028b2dd  _IOProcessorChannelUnidirectionalSend
0028b303  _IOProcessorInit
0028b314  _JM_Lambda_Qp2Quant
0028b32e  _PSD_AVE_SERVICE_CFG
0028b343  _RTK_DEV_ASC
0028b350  _RTK_DEV_ASCWRAP
0028b361  _RTK_DEV_ICU
0028b36e  _RTK_DEV_SAMSUNGUART_0
0028b385  _RTK_DEV_TIMEBASE
0028b397  _RTK_abort
0028b3a2  _RTK_are_interrupts_enabled
0028b3be  _RTK_cache_clean
0028b3cf  _RTK_cache_get_instruction_line_size
0028b3f4  _RTK_cache_get_line_size
0028b40d  _RTK_client_version_string
0028b428  _RTK_console_add_output_device
0028b447  _RTK_console_default
0028b45c  _RTK_crashlog_get_exception_info
0028b47d  _RTK_dcache_clean_whole
0028b495  _RTK_dcache_invalidate
0028b4ac  _RTK_dev_asc
0028b4b9  _RTK_dev_asc_config
0028b4cd  _RTK_dev_ascwrap_v8_dispatch
0028b4ea  _RTK_dev_configure_mmio
0028b502  _RTK_dev_cputrace_metadata
0028b51d  _RTK_dev_dockchannel0
0028b533  _RTK_dev_dockchannel2
0028b549  _RTK_dev_dockchannel3
0028b55f  _RTK_dev_dockchannel_dispatch
0028b57d  _RTK_dev_dockchannel_wrapper
0028b59a  _RTK_dev_dockchannel_wrapper_dispatch
0028b5c0  _RTK_dev_gpr
0028b5cd  _RTK_dev_map_registers
0028b5e4  _RTK_dev_messagebox_dashboard_dispatch
0028b60b  _RTK_dev_messagebox_mailbox_passive_outbox_outbox_dispatch
0028b646  _RTK_dev_platform
0028b658  _RTK_dev_psd_db
0028b668  _RTK_dev_samsunguart_0
0028b67f  _RTK_dev_samsunguart_dispatch
0028b69d  _RTK_dev_timesync_0
0028b6b1  _RTK_dev_wrapper_icu
0028b6c6  _RTK_disable_all_interrupts
0028b6e2  _RTK_disable_interrupts
0028b6fa  _RTK_enable_all_interrupts
0028b715  _RTK_enable_fiq
0028b725  _RTK_heap_add_pool
0028b738  _RTK_heap_free
0028b747  _RTK_heap_size
0028b756  _RTK_interrupt_attach
0028b76c  _RTK_interrupt_detach
0028b782  _RTK_interrupt_disable
0028b799  _RTK_interrupt_enable
0028b7af  _RTK_lock_init
0028b7be  _RTK_lock_lock
0028b7cd  _RTK_lock_unlock
0028b7de  _RTK_mbi_endpoint_attach
0028b7f7  _RTK_mbi_endpoint_enable_all
0028b814  _RTK_mbi_endpoint_send_msg
0028b82f  _RTK_mbi_log_create
0028b843  _RTK_mbi_route_create_from_physical_layer
0028b86d  _RTK_mbi_route_enable
0028b883  _RTK_mc_assume
0028b892  _RTK_mc_register_remote
0028b8aa  _RTK_mc_release
0028b8ba  _RTK_mc_release_transients
0028b8d5  _RTK_mc_unregister
0028b8e8  _RTK_mmu_get_page_size
0028b8ff  _RTK_platform_crashlog_complete
0028b91f  _RTK_platform_hibernate
0028b937  _RTK_platform_mbi_config
0028b950  _RTK_platform_power_off
0028b968  _RTK_queue_add
0028b977  _RTK_queue_count
0028b988  _RTK_queue_destroy
0028b99b  _RTK_queue_init
0028b9ab  _RTK_queue_remove
0028b9bd  _RTK_queue_try_add
0028b9d0  _RTK_queue_try_remove
0028b9e6  _RTK_restore_all_interrupts
0028ba02  _RTK_restore_interrupts
0028ba1a  _RTK_semaphore_init
0028ba2e  _RTK_semaphore_preallocate
0028ba49  _RTK_semaphore_signal
0028ba5f  _RTK_semaphore_try
0028ba72  _RTK_semaphore_uninit
0028ba88  _RTK_semaphore_wait
0028ba9c  _RTK_semaphore_wait_multiple
0028bab9  _RTK_semaphore_wait_timeout
0028bad5  _RTK_stack_guard_allocate
0028baef  _RTK_stack_guard_free
0028bb05  _RTK_terminator_thread_init
0028bb21  _RTK_thread_create
0028bb34  _RTK_thread_get_id_from_thread_pointer
0028bb5b  _RTK_thread_join
0028bb6c  _RTK_thread_preallocate_thread_lists
0028bb91  _RTK_timebase_get_time
0028bba8  _RTK_timer_call_after
0028bbbe  _RTK_timer_call_every
0028bbd4  _RTK_timer_cancel
0028bbe6  _RTK_tracekit_tracelist
0028bbfe  _RTK_vm_memory_map
0028bc11  _RTK_vm_virt_to_phys
0028bc26  _SH_DATA_SEGS
0028bc3a  __Z10TypeAdjustb19CChannelManagerType
0028bc60  __Z10approx_expd
0028bc71  __Z11AVE_Cfg_Getv
0028bc83  __Z11target_taskv
0028bc95  __Z12AVE_CSC_Initv
0028bca8  __Z12AVE_Cfg_Initv
0028bcbb  __Z12AVE_DPM_InitP11AVE_DevInfoPK10_S_AVE_Cfg
0028bce9  __Z12AVE_PSD_Initi
0028bcfc  __Z12AVE_WritePTLPK23S_HEVC_ProfileTierLevelbiP16AVE_SyntaxWriter
0028bd3e  __Z12log10_approxf
0028bd51  __Z13AVE_GetFwModev
0028bd65  __Z13AVE_PMGR_InitP11AVE_DevInfo
0028bd86  __Z13AVE_PSD_SetPS14_E_AVE_PSDSlot14_E_AVE_PMGR_PS
0028bdb9  __Z14AVE_AVC_SetPPSPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_PPS
0028bdf3  __Z14AVE_AVC_SetSPSPK21_S_AVE_Syntax_Cfg_AVCyP10_S_AVC_SPS
0028be2e  __Z14AVE_CSC_Uninitv
0028be43  __Z14AVE_DPM_Uninitv
0028be58  __Z14AVE_EventTraceP19_S_AVE_HWEventTracePi15_E_AVE_EngineID14_E_AVE_HWEModei15_E_AVE_HWEStatePKj
0028beba  __Z14AVE_IOP_Configv
0028becf  __Z14AVE_PMGR_SetPS14_E_AVE_PMGR_PD14_E_AVE_PMGR_PSb
0028bf04  __Z14AVE_PSD_Uninitv
0028bf19  __Z14RealChannelGetPKcPP15CChannelManagerPm
0028bf45  __Z14go_applicationv
0028bf5a  __Z15AVE_CheckDMVCmdPv
0028bf71  __Z15AVE_CheckEncCmdPv
0028bf88  __Z15AVE_CheckGGMCmdPv
0028bf9f  __Z15AVE_GetCurrTimev
0028bfb5  __Z15AVE_MCTFProfileP24sCAvePerfProfileInternali16_E_AVE_MCTFStats
0028bff8  __Z15AVE_PMGR_Uninitv
0028c00e  __Z15AVE_PSInfo_Make13_E_AVE_PSTypeiiP16_S_AVE_PSContext
0028c047  __Z15AVE_RegBlk_Dumpjii
0028c05f  __Z16AVC_FindLevelIdc12_E_AVC_Level
0028c083  __Z16AVC_scaling_listPKhiiP16AVE_SyntaxWriter
0028c0b1  __Z16AVE_AVC_SetSlicePK23_S_AVE_Syntax_PFCfg_AVCP12_S_AVC_Slice
0028c0f1  __Z16AVE_CheckLRMECmdPv
0028c109  __Z16AVE_CheckMCTFCmdPv
0028c121  __Z16AVE_DPM_TuneUpHwj
0028c138  __Z16AVE_EventProfileP24sCAvePerfProfileInternalii14_E_AVE_FwStats
0028c17b  __Z16AVE_Tunables_Set14_E_AVE_EncTypeb
0028c1a2  __Z16AVE_UpdateFwModej
0028c1b9  __Z17AVE_ApplyTunablesPK19_S_AVE_Tunables_Cfg
0028c1e7  __Z17AVE_CSC_EnableIRQii
0028c200  __Z17AVE_CSC_SM_Updatej
0028c218  __Z17AVE_CSC_Send_aresy
0028c230  __Z17AVE_Cfg_UpdateDPMj
0028c248  __Z17AVE_PSD_Init_aresi
0028c260  __Z17AVE_Work_CalcHwPD12_E_AVE_DevID15_E_AVE_WorkType14_E_AVE_EncTypeiiiiiiiPj
0028c2af  __Z17ChannelTableAllocm
0028c2c7  __Z17FakeChannelCreateP7CObjectiii
0028c2ea  __Z17HEVC_FindLevelIdc13_E_HEVC_Level
0028c310  __Z17HEVC_FindTierFlag12_E_HEVC_Tier
0028c335  __Z17RTK_crashlog_initj
0028c34d  __Z17RTK_endpoint_initjPK19_mbi_route_config_t
0028c37c  __Z17RealChannelCreateP7CObjectmP23ffwIOPChannelDescriptorbi
0028c3b9  __Z18AVC_FindProfileIdc14_E_AVC_Profile
0028c3e1  __Z18AVE_CSC_SM_IsReadyv
0028c3fa  __Z18AVE_CSC_Start_aresv
0028c413  __Z18AVE_DPM_TuneDownHwj
0028c42c  __Z18AVE_PMGR_EnableDPMv
0028c445  __Z18AVE_PSD_SetPS_ares14_E_AVE_PSDSlot14_E_AVE_PMGR_PS
0028c47d  __Z18AVE_TargetID2DevIDi
0028c496  __Z18AVE_Tunables_Resetv
0028c4af  __Z18ChannelTableCreatePvii
0028c4cb  __Z18DecideLowerQP4MbEnP13sCommonParams
0028c4f3  __Z19AVC_FindLevelLimits12_E_AVC_Level
0028c51a  __Z19AVE_CSC_LoadFW_aresv
0028c534  __Z19AVE_IOP_GetCurrTimev
0028c54e  __Z19AVE_PMGR_DisableDPMv
0028c568  __Z19AVE_PMGR_Get_erebus14_E_AVE_PMGR_PDP14_E_AVE_PMGR_PS
0028c5a2  __Z19AVE_PMGR_Set_erebus14_E_AVE_PMGR_PD14_E_AVE_PMGR_PS
0028c5db  __Z19AVE_PSD_Uninit_aresv
0028c5f5  __Z19AVE_RegBlk_FS_Resetv
0028c60f  __Z19AVE_RegBlk_MD_Resetv
0028c629  __Z19AVE_RegBlk_RC_Resetv
0028c643  __Z19AVE_UpdateTimeShiftx
0028c65d  __Z19ChannelTableSizeGetPmi
0028c679  __Z19GetClientBufferSizev
0028c693  __Z19HEVC_FindProfileIdc15_E_HEVC_Profile
0028c6bd  __Z20AVC_FindMaxMvsPer2Mb12_E_AVC_Level
0028c6e5  __Z20AVE_DevCap_FindPDMap12_E_AVE_DevID
0028c70d  __Z20AVE_IOP_Config_pandav
0028c728  __Z20AVE_MCTFProfileFirstP24sCAvePerfProfileInternali16_E_AVE_MCTFStats
0028c770  __Z20AVE_RegBlk_DMV_Resetv
0028c78b  __Z20AVE_RegBlk_FS_Configjjiiiiiiiiiiiiii
0028c7b5  __Z20AVE_RegBlk_Mcc_Resetv
0028c7d0  __Z20AVE_RegBlk_Ref_Resetv
0028c7eb  __Z20ChannelInterruptLockPv
0028c807  __Z20RTK_DockChannel_initv
0028c822  __Z21AVE_DevCap_FindDPMMap12_E_AVE_DevID15_E_AVE_WorkType14_E_AVE_EncType
0028c86c  __Z21AVE_EventProfileFirstP24sCAvePerfProfileInternalii14_E_AVE_FwStats
0028c8b4  __Z21AVE_RegBlk_DMV_ConfigP24_S_AVE_RegBlk_DMV_Config
0028c8ea  __Z21AVE_RegBlk_FS_Triggerj
0028c906  __Z21AVE_RegBlk_Mcc_Config15_E_AVE_PipeModejjjjjjj
0028c939  __Z21AVE_RegBlk_RC_Triggerj
0028c955  __Z22AVE_CSC_CheckIdle_aresv
0028c972  __Z22AVE_CSC_EnableIRQ_aresii
0028c990  __Z22AVE_CreateSliceMapRowsPK15_S_AVE_SliceMap18_E_AVE_DevCap_TypePh
0028c9d5  __Z22AVE_DPM_CalcDPMHwStatsjjjjjjjjjjjjj
0028c9fe  __Z22AVE_RegBlk_DMV_Triggerv
0028ca1b  __Z22AVE_RegBlk_FS_SetInputijjiiiyyi
0028ca40  __Z22AVE_RegBlk_MD_ConfigWPjjii
0028ca60  __Z22AVE_RegBlk_PelMe_Resetv
0028ca7d  __Z22AVE_RegBlk_RC_SetInputiiiiiiyyi
0028caa2  __Z22CalculateLowerMbQpFlagP13sCommonParamsjj
0028cad0  __Z22ChannelInterruptUnlockPv
0028caee  __Z22printRateControlParamsRK21RateControlParameters
0028cb23  __Z23AVE_CSC_InitMaibox_aresv
0028cb41  __Z23AVE_RegBlk_DMV_SetInputP23_S_AVE_RegBlk_DMV_Input
0028cb78  __Z23AVE_RegBlk_FS_SetOutput15_E_AVE_PipeModejjyi
0028cbaa  __Z23AVE_RegBlk_Mcc_ConfigWPjjiiii
0028cbcd  __Z23AVE_RegBlk_PelMe_Configjjjj
0028cbee  __Z23FakeChannelIndexHostGetPKc
0028cc0e  __Z23RealChannelCreateTargetP7CObjectimPPvPmS2_S3_PjS2_S4_S4_S4_S4_i
0028cc53  __Z24AVC_FindMaxSubMbRectSize12_E_AVC_Level
0028cc7f  __Z24AVE_CSC_GetSMStatus_aresv
0028cc9e  __Z24AVE_DevCap_FindHwFeature12_E_AVE_DevID
0028ccca  __Z24AVE_DevCap_FindSwFeature12_E_AVE_DevID
0028ccf6  __Z24AVE_MCTFProfileWithValueP24sCAvePerfProfileInternali16_E_AVE_MCTFStatsx
0028cd43  __Z24AVE_PMGR_CheckDMA_erebus14_E_AVE_PMGR_PS
0028cd71  __Z24AVE_RegBlk_DMV_SetOutputP24_S_AVE_RegBlk_DMV_Output
0028cdaa  __Z24AVE_RegBlk_FS_ResetStatsv
0028cdc9  __Z24RTK_thread_get_attributeP11_rtk_threadjPm
0028cdf8  __Z24RTK_thread_set_attributeP11_rtk_threadjm
0028ce26  __Z25AVE_EventProfileWithValueP24sCAvePerfProfileInternalii14_E_AVE_FwStatsx
0028ce73  __Z25AVE_PMGR_EnableDPM_erebusv
0028ce93  __Z25AVE_RegBlk_CandGen_ConfWU15_E_AVE_PipeModeijjjjj
0028cec9  __Z25AVE_RegBlk_CandGen_Config15_E_AVE_PipeModejjiiiyyjiy
0028cf03  __Z25AVE_RegBlk_PelMe_ConfigWPjjii
0028cf26  __Z25AVE_RegBlk_Ref_ConfigLuma15_E_AVE_PipeModeiiiiiiiiyyi
0028cf61  __Z25FakeChannelIndexTargetGetPKc
0028cf83  __Z25FakeChannelManagerHostGetPKc
0028cfa5  __Z25RealChannelIndexTargetGetPKc
0028cfc7  __Z26AVE_AVC_PrepareSliceHeaderPK10_S_AVC_PPSjiP13sCommonParamsP23_S_AVE_Syntax_PFCfg_AVC
0028d021  __Z26AVE_GenerateAVCHeaderStart18_E_AVC_NalUnitTypeP16AVE_SyntaxWriter
0028d068  __Z26AVE_PMGR_DisableDPM_erebusv
0028d089  __Z26AVE_PMGR_EnableIdle_erebusv
0028d0aa  __Z26AVE_RegBlk_CandGen_ResetWUv
0028d0cb  __Z26AVE_RegBlk_MD_ConfigOutput15_E_AVE_PipeModeiyj
0028d0ff  __Z27AVE_GenerateHEVCHeaderStart19_E_HEVC_NalUnitTypehhP16AVE_SyntaxWriter
0028d14a  __Z27AVE_HEVC_PrepareSliceHeaderPK11_S_HEVC_PPSjiibP13sCommonParamsP13_S_HEVC_Slice
0028d19e  __Z27AVE_RegBlk_PipeSetup_Configiiii
0028d1c3  __Z27AVE_RegBlk_Ref_ConfigChroma15_E_AVE_PipeModeiiiiiiiiyyi
0028d200  __Z27FakeChannelManagerTargetGetPKc
0028d224  __Z27RealChannelManagerTargetGetPKc
0028d248  __Z28AVE_CSC_SM_CollectXcAvcStatsPv
0028d26c  __Z29AVE_AVC_UpdatePOClsbSliceTypePK13sCommonParamsjiP23_S_AVE_Syntax_PFCfg_AVC
0028d2bc  __Z29AVE_CSC_SM_CollectXcHevcStatsPv
0028d2e1  __Z29AVE_CheckCmdNeedSyncMultiCorePv
0028d306  __Z30AVE_RegBlk_RefCache_ConfigLuma15_E_AVE_PipeModejjjjjj
0028d341  __Z32AVE_HEVC_Update_POClsb_SliceTypePK13sCommonParamsjiP13_S_HEVC_Slice
0028d38a  __Z32AVE_RegBlk_RC_SetCandidateConfigi
0028d3b1  __Z32AVE_RegBlk_RefCache_ConfigChroma15_E_AVE_PipeModejjjjj
0028d3ed  __ZN10CAVEClient11SetWorkModeE15_E_AVE_WorkMode
0028d41d  __ZN10CAVEClient12CommandQueue13ReorderFramesEjPNS_7CommandE
0028d45a  __ZN10CAVEClient12CommandQueue15EnqueueMCTFCmdQEjyyPvPNS_9FrameInfoEjj
0028d4a1  __ZN10CAVEClient12CommandQueue7DequeueEP15sCmdInformation
0028d4db  __ZN10CAVEClient12CommandQueue7EnqueueEjyyPvPNS_9FrameInfoEy
0028d518  __ZN10CAVEClient12CommandQueue8CompleteEj
0028d542  __ZN10CAVEClient12CommandQueue8ConvertPEj
0028d56c  __ZN10CAVEClient13UpdateFrameIDE17_E_AVE_FrameStageb
0028d5a1  __ZN10CAVEClient15GetCommandQueueE19_E_Proc_Mode_Queues
0028d5d9  __ZN10CAVEClient15SetUseFrameDropEb
0028d5fd  __ZN10CAVEClient17kClientBufferSizeE
0028d622  __ZN10CAVEClient17sSignalDescriptorC2EPKcP7CObjectj
0028d656  __ZN10CAVEClient21MCTF_SetPendingEncodeEj
0028d680  __ZN10CAVEClient21SetMCTFLowLatencyModeEb
0028d6aa  __ZN10CAVEClient22ProcessDirectFrameCmdsEi
0028d6d5  __ZN10CAVEClient22ResetSrcFrameRefCountsEv
0028d700  __ZN10CAVEClient23MCTF_CheckPendingEncodeEj
0028d72c  __ZN10CAVEClient23MCTF_ClearPendingEncodeEj
0028d758  __ZN10CAVEClient24GetCommandQueueToDequeueEv
0028d785  __ZN10CAVEClient8CalcHwPDE12_E_AVE_DevID15_E_AVE_WorkType14_E_AVE_EncTypeiiiiiii
0028d7d6  __ZN10CAVEClient8CompleteEj19_E_Proc_Mode_Queues
0028d807  __ZN10CAVEClient9FrameInfoC1Ejjjjjjj
0028d82c  __ZN10CAVEClientC2EPKcP7CObjectP12MappedMemoryPviyjjjjbP14AVE_PIODMACtrl
0028d875  __ZN10CFrameType15ResetMiniGopPosEv
0028d899  __ZN10CFrameType15UpdateFrameTypeEi14IMG_FRAME_TYPE
0028d8cd  __ZN10CFrameType15UpdateNextSceneER7MPQueueILi16E21_S_AVE_MultiPassStatsEj
0028d918  __ZN10CFrameType16AdjustTemporalIDEPK11RCFrameInfoj
0028d94c  __ZN10CFrameType16LookAheadBFramesER7MPQueueILi16E21_S_AVE_MultiPassStatsE14_E_AVE_EncType
0028d9a7  __ZN10CFrameType20SetTransitionToPOnlyEb
0028d9d0  __ZN10CFrameType4initEP21sCFrameTypeInitParams
0028d9ff  __ZN10CFrameType9FrameTypeEP11RCFrameInfoPjR7MPQueueILi16E21_S_AVE_MultiPassStatsE14_E_AVE_EncType
0028da62  __ZN10CFrameType9FrameTypeEP11RCFrameInfoPjR9AdaptiveBb
0028da9a  __ZN10CFrameTypeC1Ev
0028daaf  __ZN10CFrameTypeD1Ev
0028dac4  __ZN10CQueuePool6ReturnERP10_rtk_queue
0028daeb  __ZN10CQueuePool8instanceE
0028db06  __ZN10CQueuePoolC1EPKcP7CObjectm
0028db27  __ZN10CQueuePoolC2EPKcP7CObjectm
0028db48  __ZN10CQueuePoolD0Ev
0028db5d  __ZN10CQueuePoolD1Ev
0028db72  __ZN10CTimerPool8instanceE
0028db8d  __ZN10CTimerPoolC1EPKcP7CObjectm
0028dbae  __ZN10CTimerPoolC2EPKcP7CObjectm
0028dbcf  __ZN10CTimerPoolD0Ev
0028dbe4  __ZN10CTimerPoolD1Ev
0028dbf9  __ZN10CTimerPoolD2Ev
0028dc0e  __ZN10HEVC_Slice12slice_headerEP16AVE_SyntaxWriterRK11_S_HEVC_SPSRK11_S_HEVC_PPSP8HEVC_RPS19_E_HEVC_NalUnitTypej
0028dc7f  __ZN10HEVC_Slice17pred_weight_tableEP16AVE_SyntaxWriter
0028dcb7  __ZN10HEVC_Slice23generateSliceHeaderInKFERK11_S_HEVC_SPSRK11_S_HEVC_PPSP8HEVC_RPSPh
0028dd0c  __ZN11AVE_AVC_PPS4InitEyPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_PPS
0028dd4b  __ZN11AVE_AVC_PPS8GenerateEPKsiiP16_S_AVE_PSContext
0028dd7f  __ZN11AVE_AVC_PPSC1Ev
0028dd95  __ZN11AVE_AVC_PPSD1Ev
0028ddab  __ZN11AVE_AVC_SPS4InitEyPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_SPSy
0028ddeb  __ZN11AVE_AVC_SPS8GenerateEP16_S_AVE_PSContext
0028de1a  __ZN11AVE_AVC_SPSC1Ev
0028de30  __ZN11AVE_AVC_SPSD1Ev
0028de46  __ZN11AVE_DevInfo3GetEv
0028de5e  __ZN11AVE_DevInfo4InitEj12_E_AVE_DevIDiiyi
0028de89  __ZN11AVE_DevInfoD1Ev
0028de9f  __ZN11CController10CmdProcessEv
0028debf  __ZN11CController11CmdInternalEj
0028dee0  __ZN11CController11TaskWrapperEv
0028df01  __ZN11CController12CmdProcessorEPvjPj
0028df27  __ZN11CController15PeriodicProcessEv
0028df4c  __ZN11CController15SignalProcessorEPVm
0028df73  __ZN11CController18CmdInternalProcessEv
0028df9b  __ZN11CController18PostCmdSynchronousEPvjPj
0028dfc7  __ZN11CController19TriggerProcessQueueEv
0028dff0  __ZN11CController20CmdInternalProcessorEj
0028e01a  __ZN11CController22SignalProcessQueueSemaEv
0028e046  __ZN11CController27SignalProcessorSVEHeartBeatEv
0028e077  __ZN11CController4PostEPvj
0028e092  __ZN11CController4TaskEv
0028e0ab  __ZN11CController5SpawnEm
0028e0c5  __ZN11CController6SignalEPv
0028e0e1  __ZN11CControllerC2EPKcP7CObjectibP15CChannelManagermS5_m
0028e11b  __ZN11CControllerD0Ev
0028e131  __ZN11CControllerD1Ev
0028e147  __ZN11CControllerD2Ev
0028e15d  __ZN11CIPIManager8instanceE
0028e179  __ZN11CIPIManagerC2EPKcP7CObject
0028e19a  __ZN11CIPIManagerD0Ev
0028e1b0  __ZN11CIPIManagerD1Ev
0028e1c6  __ZN11CIPIManagerD2Ev
0028e1dc  __ZN11CISRManager10UnregisterEi
0028e1fc  __ZN11CISRManager14ServiceRoutineEm
0028e220  __ZN11CISRManager4MaskEi
0028e239  __ZN11CISRManager6UnmaskEi
0028e254  __ZN11CISRManager8RegisterEiPFiPvES0_
0028e27a  __ZN11CISRManager8instanceE
0028e296  __ZN11CISRManagerC2EPKcP7CObjecti
0028e2b8  __ZN11CISRManagerD0Ev
0028e2ce  __ZN11CISRManagerD1Ev
0028e2e4  __ZN11CISRManagerD2Ev
0028e2fa  __ZN11CObjectTree10InitializeEPFvPvES2_S0_
0028e325  __ZN11CObjectTree11mutexHandleE
0028e345  __ZN11CObjectTree4baseE
0028e35d  __ZN11CObjectTree8MutexGetE
0028e379  __ZN11CObjectTree9MutexGiveE
0028e396  __ZN11CObjectTreeC1EP7CObjectPS_
0028e3b7  __ZN11CObjectTreeC2EP7CObjectPS_
0028e3d8  __ZN11CObjectTreeD0Ev
0028e3ee  __ZN11CObjectTreeD1Ev
0028e404  __ZN11CObjectTreeD2Ev
0028e41a  __ZN11CScopedLockC1EPVmi
0028e433  __ZN11CScopedLockC2EPVmi
0028e44c  __ZN11CScopedLockD1Ev
0028e462  __ZN11CSignalPool6ReturnEv
0028e47d  __ZN11CSignalPool7AcquireEv
0028e499  __ZN11CSignalPool8instanceE
0028e4b5  __ZN11CSignalPoolC1EPKcP7CObjectm
0028e4d7  __ZN11CSignalPoolC2EPKcP7CObjectm
0028e4f9  __ZN11CSignalPoolD0Ev
0028e50f  __ZN11CSignalPoolD1Ev
0028e525  __ZN11RateControl11initRQModelEPv
0028e547  __ZN11RateControl11updateModelER10FrameStats
0028e574  __ZN11RateControl13updateBitRateExj
0028e598  __ZN11RateControl13updateFixedQPEi
0028e5bb  __ZN11RateControl14CreateInstanceERK21RateControlParametersP10FrameStatsiPv
0028e607  __ZN11RateControl15updateDRLParamsEjf
0028e62d  __ZN11RateControl16applyVbvPlanningEPK10FrameStatsif
0028e662  __ZN11RateControl17updateRateControlExiiPi
0028e68d  __ZN11RateControl18insertCBRFillerAVCEP17_S_AVE_FillerInfo13_E_AVE_RCModei
0028e6d8  __ZN11RateControl18processRateControlExx11_S_AVE_Timejjii
0028e712  __ZN11RateControl19insertCBRFillerHEVCEP17_S_AVE_FillerInfo13_E_AVE_RCModeiii
0028e760  __ZN11RateControl19updateBitsFromCAVLCExxi
0028e78b  __ZN11RateControl19updateCplxForZeroLAExd
0028e7b5  __ZN11RateControl21RestoreRCSegmentCtxLAERK22_S_AVE_RC_SegmentCtxLAx
0028e7fa  __ZN11RateControl21estimateTranscodeBitsER10FrameStats
0028e831  __ZN11RateControl22GenerateRCSegmentCtxLAEx
0028e85d  __ZN11RateControl23updateBitsFromTranscodeExxiPi
0028e88e  __ZN11RateControl24updateConstantRateFactorEd
0028e8bc  __ZN11RateControl27updateHRDUsingTranscodeBitsExiPi
0028e8f0  __ZN11RateControl31updateModeDistributionForZeroLAExiii
0028e928  __ZN11RateControl8validateERK21RateControlParameters
0028e95d  __ZN11RateControlC2ERK21RateControlParametersP10FrameStatsiPv
0028e99b  __ZN11RateControlD0Ev
0028e9b1  __ZN11RateControlD1Ev
0028e9c7  __ZN12AVE_KeyFrame11GetIntervalEv
0028e9e9  __ZN12AVE_KeyFrame22KeyFrameUpdateInternalEv
0028ea16  __ZN12AVE_KeyFrame4InitEyiiddi
0028ea35  __ZN12AVE_KeyFrame6UninitEv
0028ea51  __ZN12AVE_KeyFrame6UpdateEx16_E_AVE_FrameType
0028ea7f  __ZN12AVE_KeyFrame7ProcessExyjP11_S_AVE_TimeP19_S_AVE_KeyFrameHint
0028eac2  __ZN12AVE_KeyFrameC1Ev
0028ead9  __ZN12AVE_KeyFrameD1Ev
0028eaf0  __ZN12CAvePipeMcpu4InitEv
0028eb0a  __ZN12CAvePipeMcpu4StopEv
0028eb24  __ZN12CAvePipeMcpu5PauseEv
0028eb3f  __ZN12CAvePipeMcpu5ResetEv
0028eb5a  __ZN12CAvePipeMcpu5StartEv
0028eb75  __ZN12CAvePipeMcpu6ResumeEv
0028eb91  __ZN12CAvePipeMcpu8ReadDMemEjmPj
0028ebb2  __ZN12CAvePipeMcpu8ReadIMemEjmPj
0028ebd3  __ZN12CAvePipeMcpu9StartUnitEii
0028ebf3  __ZN12CAvePipeMcpu9WriteDMemEjPjm
0028ec15  __ZN12CAvePipeMcpu9WriteIMemEjPjm
0028ec37  __ZN12CAvePipeMcpuC1EPKcP7CObjectm
0028ec5a  __ZN12CAvePipeMcpuC2EPKcP7CObjectm
0028ec7d  __ZN12CAvePipeMcpuD0Ev
0028ec94  __ZN12CAvePipeMcpuD1Ev
0028ecab  __ZN12CAvePipeMcpuD2Ev
0028ecc2  __ZN12CEnvironment12ExtraHeapAddEv
0028ece5  __ZN12CEnvironment15ChannelMatchingEPFP15CChannelManagerPKcEPFmS3_E
0028ed29  __ZN12CEnvironment15ResourceManagerEv
0028ed4f  __ZN12CEnvironment4IdleEv
0028ed69  __ZN12CEnvironment6OSInitEv
0028ed85  __ZN12CEnvironment8ShutdownEv
0028eda3  __ZN12CEnvironment8instanceE
0028edc0  __ZN12CEnvironmentC2EPKcbmm
0028eddc  __ZN12CEnvironmentD0Ev
0028edf3  __ZN12CEnvironmentD1Ev
0028ee0a  __ZN12CEnvironmentD2Ev
0028ee21  __ZN12CFakeChannel12DoorBellRingEPv
0028ee45  __ZN12CFakeChannel12SignalManageEv
0028ee68  __ZN12CFakeChannel8ActivateEPFvPvES0_
0028ee8e  __ZN12CFakeChannelC1EPKcP7CObjectiPNS_12chDescriptorEm
0028eec5  __ZN12CFakeChannelC2EPKcP7CObjectiPNS_12chDescriptorEm
0028eefc  __ZN12CFakeChannelD0Ev
0028ef13  __ZN12CFakeChannelD1Ev
0028ef2a  __ZN12CGPIOManager8instanceE
0028ef47  __ZN12CGPIOManagerC2EPKcP7CObjectm
0028ef6a  __ZN12CGPIOManagerD0Ev
0028ef81  __ZN12CGPIOManagerD1Ev
0028ef98  __ZN12CGPIOManagerD2Ev
0028efaf  __ZN12CMailboxPool6ReturnERP9OSMAILBOX
0028efd6  __ZN12CMailboxPool8instanceE
0028eff3  __ZN12CMailboxPoolC1EPKcP7CObjectm
0028f016  __ZN12CMailboxPoolC2EPKcP7CObjectm
0028f039  __ZN12CMailboxPoolD0Ev
0028f050  __ZN12CMailboxPoolD1Ev
0028f067  __ZN12CRateControl10AccumulateEa9SliceTypejjP16sCRCStatPerFramehS0_
0028f0ab  __ZN12CRateControl10UpdateBitsEjjP16sCRCStatPerFrame6Engine
0028f0e7  __ZN12CRateControl11ProcessInitEPK14sCRCInitParams
0028f11a  __ZN12CRateControl11RateControlEa9SliceTypejjbjbbbjiS0_bb
0028f154  __ZN12CRateControl12Check_RCModeE13_E_AVE_RCMode
0028f185  __ZN12CRateControl12updateTempIDEtt
0028f1a9  __ZN12CRateControl13UpdateFixedQPEi
0028f1cd  __ZN12CRateControl15CalculateInitQPEy
0028f1f3  __ZN12CRateControl16computeCorrCoeffEPKjjj
0028f21e  __ZN12CRateControl17ProcessAccumulateEa9SliceTypejjP16sCRCStatPerFramehS0_
0028f269  __ZN12CRateControl17ProcessUpdateBitsEjjP16sCRCStatPerFrame6Engine
0028f2ac  __ZN12CRateControl18ProcessRateControlEa9SliceTypejjbjbbbjiS0_b
0028f2ec  __ZN12CRateControl19QpUpdateByMultipassE10qp_tuple_s
0028f321  __ZN12CRateControl19RestoreRCSegmentCtxERK20_S_AVE_RC_SegmentCtx
0028f362  __ZN12CRateControl19calculateComplexityEjjj9SliceTypeP16sCRCStatPerFrameS0_
0028f3ae  __ZN12CRateControl20AVE_CBR_InsertFillerEjjPK13_S_HEVC_Slice13_E_AVE_RCModeP17_S_AVE_FillerInfo
0028f40e  __ZN12CRateControl20GenerateRCSegmentCtxEjj
0028f43a  __ZN12CRateControl26AVE_RC_CalculateDistortionEP17_S_AVE_Distortionixxxxiii
0028f486  __ZN12CRateControl29getDataRateLimitQpModLevelMinEv
0028f4ba  __ZN12CRateControl4InitEPK14sCRCInitParamsh
0028f4e6  __ZN12CRateControl5ResetEb
0028f501  __ZN12CRateControlC1EP14CAVERefManager
0028f528  __ZN12CRateControlD0Ev
0028f53f  __ZN12CRateControlD1Ev
0028f556  __ZN12CRealChannel12SignalManageEv
0028f579  __ZN12CRealChannel16DoorBellCoalesceEv
0028f5a0  __ZN12CRealChannel21DoorBellRingThrottledEPv
0028f5cd  __ZN12CRealChannelC1EPKcP7CObjectibjPNS_12chDescriptorEm
0028f606  __ZN12CRealChannelC2EPKcP7CObjectibjPNS_12chDescriptorEm
0028f63f  __ZN12CRealChannelD0Ev
0028f656  __ZN12CRealChannelD1Ev
0028f66d  __ZN12CTerminalOut5PrintEPKc
0028f68a  __ZN12CTerminalOut6OutputEv
0028f6a6  __ZN12CTerminalOut6SignalEPv
0028f6c3  __ZN12CTerminalOutC1EPKcP7CObjectibbP15CChannelManagerm
0028f6fb  __ZN12CTerminalOutC2EPKcP7CObjectibbP15CChannelManagerm
0028f733  __ZN12CTerminalOutD0Ev
0028f74a  __ZN12CTerminalOutD1Ev
0028f761  __ZN12MappedMemory19g_bUseStaticMappingE
0028f78a  __ZN12MappedMemoryC1Emmb
0028f7a3  __ZN12MappedMemoryC2Emmb
0028f7bc  __ZN12MappedMemoryD1Ev
0028f7d3  __ZN13AVE_AVC_Slice4InitEyPK23_S_AVE_Syntax_PFCfg_AVCP12_S_AVC_Slice
0028f818  __ZN13AVE_AVC_Slice8GenerateEPK10_S_AVC_SPSPK10_S_AVC_PPSPhiPi
0028f857  __ZN13AVE_AVC_SliceC1Ev
0028f86f  __ZN13AVE_AVC_SliceD1Ev
0028f887  __ZN13CAVECommonDPB14DPBSanityCheckEPbS0_PiS1_S1_P27_S_AVE_RefManager_FrameInfo
0028f8d7  __ZN13CAVECommonDPB14RemoveDPBEntryEP17AVECommonDPBEntry
0028f910  __ZN13CAVECommonDPB14setRefPointersEP18AVE_PICMGMT_PARAMSP22ReferenceFrameInfoData
0028f963  __ZN13CAVECommonDPB16InitRefIndexInfoEi
0028f98b  __ZN13CAVECommonDPB17InsertEndDPBEntryEP17AVECommonDPBEntry
0028f9c7  __ZN13CAVECommonDPB17ResetRefIndexInfoEi
0028f9f0  __ZN13CAVECommonDPB19InsertAfterDPBEntryEP17AVECommonDPBEntryS1_
0028fa31  __ZN13CAVECommonDPB20InsertBeforeDPBEntryEP17AVECommonDPBEntryS1_
0028fa73  __ZN13CAVECommonDPB21DPBContextBookkeepingEb
0028faa0  __ZN13CAVECommonDPB22ProvideReferenceFramesEjP14_S_AVE_Buf_Setj
0028fae0  __ZN13CAVECommonDPB23InitPointerAndVariablesEv
0028fb0f  __ZN13CAVECommonDPB34GetIsThisFrameMarkedAsNonReferenceEPK11RCFrameInfoP14CAVERefManagerPi
0028fb6a  __ZN13CAVECommonDPBD0Ev
0028fb82  __ZN13CAVECommonDPBD1Ev
0028fb9a  __ZN13COFController10StartHMESCEP15sCmdInformationi
0028fbce  __ZN13COFController11ProcessInitEPv
0028fbf2  __ZN13COFController11StartLRMERCEP15sCmdInformationi
0028fc27  __ZN13COFController14AcquireBuffersEP18AVE_PICMGMT_PARAMS
0028fc61  __ZN13COFController15ProcessLRMEDoneEv
0028fc88  __ZN13COFController16ProcessHMESCDoneEv
0028fcb0  __ZN13COFController16ProcessLRMEStartEPv
0028fcd9  __ZN13COFController17ProcessHMESCStartEPv
0028fd03  __ZN13COFController17ProcessLRMERCDoneEv
0028fd2c  __ZN13COFController18ConfigHMESCDMALumaEP18AVE_PICMGMT_PARAMS
0028fd6a  __ZN13COFController18ProcessLRMERCStartEPv
0028fd95  __ZN13COFController18ProcessLrmeResultsEj
0028fdbf  __ZN13COFController19HMESCAlgorithmSetupEP15sCmdInformation
0028fdfb  __ZN13COFController20SetDefaultParametersEv
0028fe27  __ZN13COFController22InitEncodingParametersEPv
0028fe56  __ZN13COFController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
0028fea0  __ZN13COFController9StartLRMEEP15sCmdInformationi
0028fed2  __ZN13COFControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
0028ff0c  __ZN13COFControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
0028ff46  __ZN13COFControllerD0Ev
0028ff5e  __ZN13COFControllerD1Ev
0028ff76  __ZN13CResourcePool8PoolInitEv
0028ff95  __ZN13CResourcePool8instanceE
0028ffb3  __ZN13CResourcePoolC1EPKcP7CObjectm
0028ffd7  __ZN13CResourcePoolC2EPKcP7CObjectm
0028fffb  __ZN13CResourcePoolD0Ev
00290013  __ZN13CResourcePoolD1Ev
0029002b  __ZN13CSharedMemory12physicalBaseE
0029004e  __ZN13CSharedMemory17MallocSynchronousEmj
00290078  __ZN13CSharedMemory4FreeEPv
00290094  __ZN13CSharedMemory6MallocEmjP7CObject
002900bb  __ZN13CSharedMemory6SignalEPv
002900d9  __ZN13CSharedMemory8instanceE
002900f7  __ZN13CSharedMemoryC1EPKcP7CObjectP15CChannelManagermy
0029012e  __ZN13CSharedMemoryC2EPKcP7CObjectP15CChannelManagermy
00290165  __ZN13CSharedMemoryD0Ev
0029017d  __ZN13CSharedMemoryD1Ev
00290195  __ZN13CTimerManager12rtosInstanceE
002901b8  __ZN13CTimerManager14TimerIterationEPv
002901df  __ZN13CTimerManager4StopEv
002901fa  __ZN13CTimerManager5StartEjiPFvmPvES0_
00290221  __ZN13CTimerManagerC2EPKcP7CObjectjj
00290246  __ZN13CTimerManagerD0Ev
0029025e  __ZN13CTimerManagerD1Ev
00290276  __ZN13CTimerManagerD2Ev
0029028e  __ZN14AVE_PIODMACtrl10GroupErrorEj
002902b1  __ZN14AVE_PIODMACtrl11GetCmdGroupEP22_S_AVE_PIODMACmdStatus
002902ed  __ZN14AVE_PIODMACtrl14SetCmdSequenceEjyyjjjb
0029031a  __ZN14AVE_PIODMACtrl4InitEv
00290336  __ZN14AVE_PIODMACtrl5StartEjyjyjjj
00290359  __ZN14AVE_PIODMACtrl9GroupDoneEj
0029037a  __ZN14AVE_PIODMACtrlC1Ev
00290393  __ZN14AVE_PIODMACtrlD1Ev
002903ac  __ZN14CAVCController10DebugStatsEP14CODED_DATA_HDR
002903df  __ZN14CAVCController10StartHMESCEP15sCmdInformationi
00290414  __ZN14CAVCController10calcAvgVarEP18AVE_PICMGMT_PARAMS
0029044b  __ZN14CAVCController11ProcessInitEPv
00290470  __ZN14CAVCController11StartLRMERCEP15sCmdInformationi
002904a6  __ZN14CAVCController12LoadFWUTSCfgEv
002904cb  __ZN14CAVCController12SetTranscodeEP26CAVEControllerAvcEncodeCmd
0029050c  __ZN14CAVCController13TranscodeDoneEP26sCAveTranscodeDoneInternali
0029054f  __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice
0029059b  __ZN14CAVCController14StartTranscodeEP15sCmdInformationi
002905d4  __ZN14CAVCController14calcQpModRangeE9SliceTypeRhS1_
00290609  __ZN14CAVCController15ProcessLRMEDoneEv
00290631  __ZN14CAVCController15ProcessPipeDoneEv
00290659  __ZN14CAVCController16PipePrepareParamEPv
00290683  __ZN14CAVCController16ProcessHMESCDoneEv
002906ac  __ZN14CAVCController16ProcessLRMEStartEPv
002906d6  __ZN14CAVCController16ProcessPipeResetEv
002906ff  __ZN14CAVCController16ProcessPipeStartEPv
00290729  __ZN14CAVCController16SetLRMERCPerPassEPK18AVE_PICMGMT_PARAMS
00290767  __ZN14CAVCController17LegacyExtStatsMapEv
00290791  __ZN14CAVCController17PrepReconFwParamsEP18AVE_PICMGMT_PARAMSj
002907d0  __ZN14CAVCController17ProcessHMESCStartEPv
002907fb  __ZN14CAVCController17ProcessLRMERCDoneEv
00290825  __ZN14CAVCController18GetPicCropInfoFlagEv
00290850  __ZN14CAVCController18ProcessLRMERCStartEPv
0029087c  __ZN14CAVCController18ResetBetweenPassesE26sCAveInitCmdInternalParams
002908c2  __ZN14CAVCController19CollectDataFromCpusEb
002908ee  __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji
00290930  __ZN14CAVCController19HMESCAlgorithmSetupEP15sCmdInformation
0029096d  __ZN14CAVCController19InitScalingListRegsEv
00290999  __ZN14CAVCController20PrepSrcStatsFwParamsEP18AVE_PICMGMT_PARAMSPK12_S_AVC_Slicejj
002909ec  __ZN14CAVCController20ProcessTranscodeDoneEP30CAVEControllerTranscodeDoneCmd
00290a39  __ZN14CAVCController20SetDefaultParametersEv
00290a66  __ZN14CAVCController20SetLRMERCPerSrcFrameEPK26CAVEControllerAvcEncodeCmd
00290ab0  __ZN14CAVCController21InitFlatMbLowQPParamsEv
00290ade  __ZN14CAVCController21ProcessTranscodeResetEv
00290b0c  __ZN14CAVCController21ProcessTranscodeStartEPv
00290b3b  __ZN14CAVCController21SetRoundingOffsetRegsEji
00290b6a  __ZN14CAVCController22GatherSharedFrameStatsEP14CODED_DATA_HDRPvS2_
00290bae  __ZN14CAVCController22InitEncodingParametersEPv
00290bde  __ZN14CAVCController23InitCoeffCancelCostRegsEv
00290c0e  __ZN14CAVCController23UpdateFlatMbLowQPParamsEv
00290c3e  __ZN14CAVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd
00290c8f  __ZN14CAVCController25InitStaticAreaLowQPParamsEii
00290cc2  __ZN14CAVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDR9SliceTypej
00290d10  __ZN14CAVCController27UpdateStaticAreaLowQPParamsEj
00290d44  __ZN14CAVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP23_S_AVE_Syntax_PFCfg_AVC
00290dab  __ZN14CAVCController32ProcessRateControlAccumulateBitsEv
00290de4  __ZN14CAVCController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
00290e2f  __ZN14CAVCController7setLRMEEP26CAVEControllerAvcEncodeCmdP18AVE_PICMGMT_PARAMSj
00290e80  __ZN14CAVCController7setPipeEP26CAVEControllerAvcEncodeCmd
00290ebb  __ZN14CAVCController8PipeDoneEP15sCmdInformationi
00290eed  __ZN14CAVCController8setHMESCEP26CAVEControllerAvcEncodeCmdP18AVE_PICMGMT_PARAMSj
00290f3f  __ZN14CAVCController9DebugInitEv
00290f60  __ZN14CAVCController9ManageDPBEP18AVE_PICMGMT_PARAMSj
00290f96  __ZN14CAVCController9SetEncCmdEPK15sCmdInformationP26CAVEControllerAvcEncodeCmd
00290fe6  __ZN14CAVCController9SetLRMERCEPK26CAVEControllerAvcEncodeCmd
00291024  __ZN14CAVCController9StartLRMEEP15sCmdInformationi
00291057  __ZN14CAVCController9StartPipeEP15sCmdInformationi
0029108a  __ZN14CAVCControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
002910c5  __ZN14CAVCControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00291100  __ZN14CAVCControllerD0Ev
00291119  __ZN14CAVCControllerD1Ev
00291132  __ZN14CAVCControllerD2Ev
0029114b  __ZN14CAVEFilterBase16SendNotificationEmjPhh
00291178  __ZN14CAVEFilterBaseC2EPKcP7CObjectyibmm
002911a1  __ZN14CAVEFilterBaseD0Ev
002911ba  __ZN14CAVEFilterBaseD1Ev
002911d3  __ZN14CAVEFilterBaseD2Ev
002911ec  __ZN14CAVERefManager11UpdateStatsEj
00291210  __ZN14CAVERefManager14SetRCFrameInfoEPK11RCFrameInfoPK27_S_AVE_RefManager_FrameInfo
00291264  __ZN14CAVERefManager19UpdateFirstFrameNumEbj
00291291  __ZN14CAVERefManager20UpdateFPSAndDurationEbbdijj
002912c3  __ZN14CAVERefManager4InitEPK14sCRCInitParamsb
002912f1  __ZN14CAVERefManager5ResetEP11RCFrameInfo
0029131b  __ZN14CAVERefManager9UpdatePTSEP11RCFrameInfo
00291349  __ZN14CAVERefManager9UpdatePTSEP11RCFrameInfoP11_S_AVE_Timei
00291386  __ZN14CAVERefManagerC1Ev
0029139f  __ZN14CDMAController16ConfigHMESCRdDMAEP18AVE_PICMGMT_PARAMS
002913dc  __ZN14CDMAControllerC1Ev
002913f5  __ZN14CDMAControllerD1Ev
0029140e  __ZN14CDMVController11ProcessInitEPv
00291433  __ZN14CDMVController14ProcessDMVDoneEv
0029145a  __ZN14CDMVController15ProcessDMVStartEPv
00291483  __ZN14CDMVController20SetDefaultParametersEv
002914b0  __ZN14CDMVController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
002914fb  __ZN14CDMVController8StartDMVEP15sCmdInformationi
0029152d  __ZN14CDMVControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00291568  __ZN14CDMVControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
002915a3  __ZN14CDMVControllerD0Ev
002915bc  __ZN14CDMVControllerD1Ev
002915d5  __ZN14CGGMController10StartHMESCEP15sCmdInformationi
0029160a  __ZN14CGGMController11ProcessInitEPv
0029162f  __ZN14CGGMController11StartLRMERCEP15sCmdInformationi
00291665  __ZN14CGGMController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS
002916a1  __ZN14CGGMController14SetPipePerBBoxEP18AVE_PICMGMT_PARAMSP24_S_AVE_Session_GGM_PFCfg
002916f7  __ZN14CGGMController15ProcessLRMEDoneEv
0029171f  __ZN14CGGMController15ProcessPipeDoneEv
00291747  __ZN14CGGMController15SetHMEFSPerBBoxEP18AVE_PICMGMT_PARAMS
00291783  __ZN14CGGMController15SetHMERSPerBBoxEP18AVE_PICMGMT_PARAMS
002917bf  __ZN14CGGMController15SetHMERSPerPassEP18AVE_PICMGMT_PARAMS
002917fb  __ZN14CGGMController15SetPipePerFrameEP18AVE_PICMGMT_PARAMSP24_S_AVE_Session_GGM_PFCfg
00291852  __ZN14CGGMController16ProcessHMESCDoneEv
0029187b  __ZN14CGGMController16ProcessLRMEStartEPv
002918a5  __ZN14CGGMController16ProcessPipeResetEv
002918ce  __ZN14CGGMController16ProcessPipeStartEPv
002918f8  __ZN14CGGMController16SetHMEFSPerFrameEP18AVE_PICMGMT_PARAMSP24_S_AVE_Session_GGM_PFCfg
00291950  __ZN14CGGMController16SetHMERSPerFrameEP18AVE_PICMGMT_PARAMS
0029198d  __ZN14CGGMController17ProcessHMESCStartEPv
002919b8  __ZN14CGGMController17ProcessLRMERCDoneEv
002919e2  __ZN14CGGMController18ConfigHMESCDMALumaEP18AVE_PICMGMT_PARAMS
00291a21  __ZN14CGGMController18ProcessLRMERCStartEPv
00291a4d  __ZN14CGGMController19HMESCAlgorithmSetupEP15sCmdInformation
00291a8a  __ZN14CGGMController20ConfigHMESCDMAChromaEP18AVE_PICMGMT_PARAMS
00291acb  __ZN14CGGMController20SetDefaultParametersEv
00291af8  __ZN14CGGMController21FillAndAdjustBBoxInfoEP19_S_AVE_GGM_GGCoordIS1_iiib
00291b42  __ZN14CGGMController22InitEncodingParametersEPv
00291b72  __ZN14CGGMController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
00291bbd  __ZN14CGGMController8PipeDoneEP15sCmdInformationi
00291bef  __ZN14CGGMController9StartLRMEEP15sCmdInformationi
00291c22  __ZN14CGGMController9StartPipeEP15sCmdInformationi
00291c55  __ZN14CGGMControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00291c90  __ZN14CGGMControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00291ccb  __ZN14CGGMControllerD0Ev
00291ce4  __ZN14CGGMControllerD1Ev
00291cfd  __ZN14CSemaphorePool10SemaStatusEPVm
00291d22  __ZN14CSemaphorePool6ReturnERPVm
00291d43  __ZN14CSemaphorePool8PoolInitEv
00291d63  __ZN14CSemaphorePool8instanceE
00291d82  __ZN14CSemaphorePoolC1EPKcP7CObjectm
00291da7  __ZN14CSemaphorePoolC2EPKcP7CObjectm
00291dcc  __ZN14CSemaphorePoolD0Ev
00291de5  __ZN14CSemaphorePoolD1Ev
00291dfe  __ZN15CChannelManager10UnregisterEPv
00291e23  __ZN15CChannelManager11DoorBellSetEPFvPvES0_
00291e50  __ZN15CChannelManager15RegisterByIndexEmPFvPvES0_
00291e82  __ZN15CChannelManager16DoorBellCoalesceEv
00291eac  __ZN15CChannelManager16TimerISRCallBackEmPv
00291ed8  __ZN15CChannelManager18DoorBellCadenceSetEj
00291f04  __ZN15CChannelManager4InitEmPKc19CChannelManagerTypeP18ffwIOPMessageEntrym
00291f4f  __ZN15CChannelManager4StopEv
00291f6c  __ZN15CChannelManager4TaskEv
00291f89  __ZN15CChannelManager5SpawnEii
00291fa8  __ZN15CChannelManager5StartEv
00291fc6  __ZN15CChannelManager6SignalEPv
00291fe6  __ZN15CChannelManagerC2EPKcP7CObjectm
0029200c  __ZN15CChannelManagerD0Ev
00292026  __ZN15CChannelManagerD1Ev
00292040  __ZN15CChannelManagerD2Ev
0029205a  __ZN15CFlowController20McpuControllerCreateEPKcyi
0029208c  __ZN15CFlowController20McpuControllerDeleteEP26CAVEPipeMcpuControllerBase
002920d6  __ZN15CFlowController20PipeISRManagerCreateEPKcyiPPVm
0029210c  __ZN15CFlowController20PipeISRManagerDeleteEP22CAVEPipeISRManagerBase
00292152  __ZN15CFlowControllerC1EPKcP7CObjectiP15CChannelManagermS5_mS5_mS5_m
00292197  __ZN15CFlowControllerD0Ev
002921b1  __ZN15CFlowControllerD1Ev
002921cb  __ZN15CHEVCController10DebugStatsEP14CODED_DATA_HDR
002921ff  __ZN15CHEVCController10SetRpsVarsEjP25HEVC_SLICE_SHORT_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSPK22HEVC_SPS_LONG_TERM_RPSjh
00292276  __ZN15CHEVCController10StartHMESCEP15sCmdInformationi
002922ac  __ZN15CHEVCController10calcAvgVarEP18AVE_PICMGMT_PARAMS
002922e4  __ZN15CHEVCController11DebugEncodeEjP18AVE_PICMGMT_PARAMS
0029231e  __ZN15CHEVCController11ProcessInitEPv
00292344  __ZN15CHEVCController11StartLRMERCEP15sCmdInformationi
0029237b  __ZN15CHEVCController12LoadFWUTSCfgEv
002923a1  __ZN15CHEVCController13SaveXcContextEP28XcodeHevc_CtxCfg_CtxMemory_t
002923e6  __ZN15CHEVCController13TranscodeDoneEP26sCAveTranscodeDoneInternali
0029242a  __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS
00292467  __ZN15CHEVCController14StartTranscodeEP15sCmdInformationi
002924a1  __ZN15CHEVCController14calcQpModRangeEP18AVE_PICMGMT_PARAMSRhS2_
002924e2  __ZN15CHEVCController15ProcessLRMEDoneEv
0029250b  __ZN15CHEVCController15ProcessPipeDoneEv
00292534  __ZN15CHEVCController16PipePrepareParamEPv
0029255f  __ZN15CHEVCController16ProcessHMESCDoneEv
00292589  __ZN15CHEVCController16ProcessLRMEStartEPv
002925b4  __ZN15CHEVCController16ProcessPipeResetEv
002925de  __ZN15CHEVCController16ProcessPipeStartEPv
00292609  __ZN15CHEVCController16SetLRMERCPerPassEPK18AVE_PICMGMT_PARAMS
00292648  __ZN15CHEVCController17PrepReconFwParamsEP18AVE_PICMGMT_PARAMS
00292687  __ZN15CHEVCController17ProcessHMESCStartEPv
002926b3  __ZN15CHEVCController17ProcessLRMERCDoneEv
002926de  __ZN15CHEVCController18GetMaxLowerDeltaQPEj
0029270a  __ZN15CHEVCController18GetPicCropInfoFlagEv
00292736  __ZN15CHEVCController18ProcessLRMERCStartEPv
00292763  __ZN15CHEVCController18ResetBetweenPassesE26sCAveInitCmdInternalParams
002927aa  __ZN15CHEVCController18SetTranscodeCommonEv
002927d6  __ZN15CHEVCController18g_LastBlkSSDBufferE
00292801  __ZN15CHEVCController19CollectDataFromCpusEb
0029282e  __ZN15CHEVCController19HMESCAlgorithmSetupEP15sCmdInformation
0029286c  __ZN15CHEVCController19PrepareHDRdQPTablesEPa
0029289a  __ZN15CHEVCController20PrepSrcStatsFwParamsEP18AVE_PICMGMT_PARAMSPK13_S_HEVC_Slice
002928ed  __ZN15CHEVCController20ProcessTranscodeDoneEP30CAVEControllerTranscodeDoneCmd
0029293b  __ZN15CHEVCController20SetDefaultParametersEv
00292969  __ZN15CHEVCController20SetLRMERCPerSrcFrameEPK18AVE_PICMGMT_PARAMS
002929ac  __ZN15CHEVCController20StaticAreaInterApplyEPK18AVE_PICMGMT_PARAMSPjjj
002929f3  __ZN15CHEVCController20g_LastBlkSSDClientIDE
00292a20  __ZN15CHEVCController21ProcessTranscodeResetEv
00292a4f  __ZN15CHEVCController21ProcessTranscodeStartEPv
00292a7f  __ZN15CHEVCController21WriteSliceHeadersHevcEP30CAVEControllerTranscodeDoneCmd
00292ace  __ZN15CHEVCController22GatherSharedFrameStatsEP14CODED_DATA_HDRPv
00292b10  __ZN15CHEVCController22InitEncodingParametersEPv
00292b41  __ZN15CHEVCController23derive_rounding_offsetsEPtS0_
00292b76  __ZN15CHEVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd
00292bc8  __ZN15CHEVCController24FindStaticAreaActionModeEjjb
00292bfc  __ZN15CHEVCController24program_sh_rps_for_ltrefEiP23HEVC_SPS_SHORT_TERM_RPS
00292c48  __ZN15CHEVCController26GenerateScalingListDataPPSEP11_S_HEVC_PPS
00292c89  __ZN15CHEVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDR
00292ccd  __ZN15CHEVCController27UpdateStaticAreaLowQPParamsEP18AVE_PICMGMT_PARAMSjj
00292d18  __ZN15CHEVCController27program_sh_rps_hierarchicalEiP19HEVC_SHORT_TERM_RPSj
00292d64  __ZN15CHEVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP13_S_HEVC_Slice
00292dc2  __ZN15CHEVCController32ProcessRateControlAccumulateBitsEv
00292dfc  __ZN15CHEVCController33update_sps_rps_internal_variablesEP19HEVC_SHORT_TERM_RPS
00292e4c  __ZN15CHEVCController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
00292e98  __ZN15CHEVCController7setLRMEEP27CAVEControllerHevcEncodeCmdP18AVE_PICMGMT_PARAMSj
00292eeb  __ZN15CHEVCController7setPipeEP18AVE_PICMGMT_PARAMS
00292f1f  __ZN15CHEVCController8CleanMemEv
00292f40  __ZN15CHEVCController8PipeDoneEP15sCmdInformationi
00292f73  __ZN15CHEVCController8calc_rpsEhiP23HEVC_SPS_SHORT_TERM_RPSP19HEVC_SHORT_TERM_RPSPK22HEVC_SPS_LONG_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSj
00292ffb  __ZN15CHEVCController8setHMESCEP27CAVEControllerHevcEncodeCmdP18AVE_PICMGMT_PARAMSj
0029304f  __ZN15CHEVCController9DebugInitEP25CAVEControllerHevcInitCmd
0029308c  __ZN15CHEVCController9ManageDPBEP18AVE_PICMGMT_PARAMSj
002930c3  __ZN15CHEVCController9SetEncCmdEPK15sCmdInformationP27CAVEControllerHevcEncodeCmd
00293115  __ZN15CHEVCController9SetLRMERCEPK18AVE_PICMGMT_PARAMS
0029314c  __ZN15CHEVCController9StartLRMEEP15sCmdInformationi
00293180  __ZN15CHEVCController9StartPipeEP15sCmdInformationi
002931b4  __ZN15CHEVCControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
002931f0  __ZN15CHEVCControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
0029322c  __ZN15CHEVCControllerD0Ev
00293246  __ZN15CHEVCControllerD1Ev
00293260  __ZN15CMCTFController10StartHMESCEP15sCmdInformation
00293295  __ZN15CMCTFController11ProcessInitEPv
002932bb  __ZN15CMCTFController11StartLRMERCEP15sCmdInformation
002932f1  __ZN15CMCTFController13ConfigReadDMAEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoj
0029333e  __ZN15CMCTFController13EnqueueFramesEP18AVE_PICMGMT_PARAMSPv
0029337b  __ZN15CMCTFController14ConfigWriteDMAEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
002933c8  __ZN15CMCTFController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS
00293405  __ZN15CMCTFController14DequeueCommandEPPv
0029342f  __ZN15CMCTFController14GetRefCompInfoEbPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoS4_iPbPhS6_P17_S_AVE_CompBufExt
0029349d  __ZN15CMCTFController15EnableDebugCRCsEj
002934c6  __ZN15CMCTFController15ProcessLRMEDoneEv
002934ef  __ZN15CMCTFController15ProcessPipeDoneEP15sCmdInformation
00293529  __ZN15CMCTFController15SetFilterGatingEP14MCTF_FrameInfoPb
00293564  __ZN15CMCTFController15SetRefFrameInfoEPK18AVE_PICMGMT_PARAMSPP14MCTF_FrameInfoS4_
002935b7  __ZN15CMCTFController16CollectLRFSStatsEjj
002935e2  __ZN15CMCTFController16CollectPipeStatsEP14MCTF_FrameInfoPb
0029361e  __ZN15CMCTFController16ProcessHMESCDoneEP15sCmdInformation
00293659  __ZN15CMCTFController17CollectHMEScStatsEPK14MCTF_FrameInfo
00293695  __ZN15CMCTFController17GetRefCompOutInfoEPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoiP17_S_AVE_CompBufExt
002936fb  __ZN15CMCTFController17ProcessLRMERCDoneEP15sCmdInformation
00293737  __ZN15CMCTFController18ConfigHMESCDMALumaEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
00293788  __ZN15CMCTFController20ConfigHMESCDMAChromaEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
002937db  __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb
0029382f  __ZN15CMCTFController20SetLRMEFSPerSrcFrameEP18AVE_PICMGMT_PARAMS
00293871  __ZN15CMCTFController20SetLRMERCPerSrcFrameEPK18AVE_PICMGMT_PARAMS
002938b4  __ZN15CMCTFController22GetStrengthTuningStatsEP14MCTF_FrameInfoP24sMctfStrengthTuningStats
0029390f  __ZN15CMCTFController22InitEncodingParametersEPv
00293940  __ZN15CMCTFController25ResetFilterStrengthLookupEj
00293973  __ZN15CMCTFController28MakeCompressedBufCopy_PIODMAEPPK15_S_AVE_CIBufExtPA2_S2_PA2_Kji
002939ca  __ZN15CMCTFController7SetMCTFEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
00293a0f  __ZN15CMCTFController9SetMEPipeEP18AVE_PICMGMT_PARAMS
00293a45  __ZN15CMCTFController9StartLRMEEP15sCmdInformation
00293a78  __ZN15CMCTFController9StartPipeEP15sCmdInformation
00293aab  __ZN15CMCTFControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00293ae7  __ZN15CMCTFControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
00293b23  __ZN15CMCTFControllerD0Ev
00293b3d  __ZN15CMCTFControllerD1Ev
00293b57  __ZN15CRTOSObjectPool12ObjectReturnEPv
00293b7e  __ZN15CRTOSObjectPool13ObjectAcquireEPv
00293ba6  __ZN15CRTOSObjectPool4StopEv
00293bc3  __ZN15CRTOSObjectPool5StartEmm
00293be2  __ZN15CRTOSObjectPoolC2EPKcP7CObject
00293c07  __ZN15CRTOSObjectPoolD0Ev
00293c21  __ZN15CRTOSObjectPoolD1Ev
00293c3b  __ZN15CRTOSObjectPoolD2Ev
00293c55  __ZN16AVE_SyntaxWriter11AlignToByteEv
00293c7b  __ZN16AVE_SyntaxWriter14WriteBitNTimesEji
00293ca5  __ZN16AVE_SyntaxWriter14WriteStartCodeEv
00293cce  __ZN16AVE_SyntaxWriter16AlignToByteWith0Ev
00293cf9  __ZN16AVE_SyntaxWriter16AlignToByteWith1Ev
00293d24  __ZN16AVE_SyntaxWriter4InitEyPhib
00293d46  __ZN16AVE_SyntaxWriter5ResetEv
00293d65  __ZN16AVE_SyntaxWriter6WriteUEji
00293d86  __ZN16AVE_SyntaxWriter7WriteSEEi
00293da7  __ZN16AVE_SyntaxWriter7WriteUEEj
00293dc8  __ZN16AVE_SyntaxWriter8WriteBitEj
00293dea  __ZN16AVE_SyntaxWriterC1Ev
00293e05  __ZN16AVE_SyntaxWriterD1Ev
00293e20  __ZN16LinearRegression4initEffff
00293e41  __ZN16LinearRegression6updateEff
00293e62  __ZN17CAVEPriorityQueue12CreateClientEPKcP7CObjectyjiyjjP14AVE_PIODMACtrl
00293eac  __ZN17CAVEPriorityQueue13DestroyClientEj
00293ed5  __ZN17CAVEPriorityQueue14RegisterClientEy
00293eff  __ZN17CAVEPriorityQueue16UnregisterClientEy
00293f2b  __ZN17CAVEPriorityQueue17SetClientPriorityEyi
00293f59  __ZN17CAVEPriorityQueue17kClientBufferSizeE
00293f85  __ZN17CAVEPriorityQueue19SetClientMCTFEncodeEyb
00293fb5  __ZN17CAVEPriorityQueue22SetClientUseFirmwareRCEyb
00293fe8  __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEb
0029401c  __ZN17CAVEPriorityQueue4PeekEPjS0_PyS1_S0_PPvb
0029404b  __ZN17CAVEPriorityQueue5FlushEyyP15sCmdInformation
0029407e  __ZN17CAVEPriorityQueue7DequeueEP15sCmdInformationb
002940b2  __ZN17CAVEPriorityQueue7EnqueueEyyyjPvPN10CAVEClient9FrameInfoEj
002940f3  __ZN17CAVEPriorityQueue7IsEmptyEv
00294115  __ZN17CAVEPriorityQueue8CompleteEyj19_E_Proc_Mode_Queues
0029414e  __ZN17CAVEPriorityQueue8ConvertPEyj19_E_Proc_Mode_Queues
00294187  __ZN17CAVEPriorityQueue8FlushAllEv
002941aa  __ZN17CAVEPriorityQueueC1Ev
002941c6  __ZN17CAVEPriorityQueueD1Ev
002941e2  __ZN17CLRMEFSController11HwBlockDoneEPv
0029420a  __ZN17CLRMEFSController11HwBlockInitEPvS0_
00294235  __ZN17CLRMEFSController12ResetHwBlockEv
0029425d  __ZN17CLRMEFSController14FrameLevelInitEv
00294287  __ZN17CLRMEFSController15ConfigHwBlockGoEb
002942b2  __ZN17CLRMEFSController17SequenceLevelInitEv
002942df  __ZN17CLRMEFSController18ConfigHwBlockRdDMAEP18AVE_PICMGMT_PARAMS
00294321  __ZN17CLRMEFSController18ConfigHwBlockWrDMAEP18AVE_PICMGMT_PARAMS
00294363  __ZN17CLRMEFSController20ConfigRdDMALowResRefEP18AVE_PICMGMT_PARAMS
002943a7  __ZN17CLRMEFSController20ConfigRdDMALowResSrcEP18AVE_PICMGMT_PARAMS
002943eb  __ZN17CLRMERSController11HwBlockDoneEPv
00294413  __ZN17CLRMERSController11HwBlockInitEPvS0_
0029443e  __ZN17CLRMERSController12ResetHwBlockEv
00294466  __ZN17CLRMERSController14FrameLevelInitEv
00294490  __ZN17CLRMERSController15ConfigHwBlockGoEb
002944bb  __ZN17CLRMERSController17SequenceLevelInitEv
002944e8  __ZN17CLRMERSController18ConfigHwBlockRdDMAEP18AVE_PICMGMT_PARAMS
0029452a  __ZN17CLRMERSController18ConfigHwBlockWrDMAEP18AVE_PICMGMT_PARAMS
0029456c  __ZN17CLRMERSController22ConfigRdDMALowResRCRefEP18AVE_PICMGMT_PARAMS
002945b2  __ZN17CLRMERSController22ConfigRdDMALowResRCSrcEP18AVE_PICMGMT_PARAMS
002945f8  __ZN17CLRMERSController27ConfigRdDMALowResRCPrvRsltsEP18AVE_PICMGMT_PARAMS
00294643  __ZN17CLRMERSController31ConfigLowResMEConfigRCPerSourceEP18AVE_PICMGMT_PARAMS
00294692  __ZN17CMultiPassControl10InitializeEjjjjiiii
002946bf  __ZN17CMultiPassControl12MpAccumulateEjjjjiji
002946ed  __ZN17CMultiPassControl16QuantizeCplxHistEPKjPj
0029471d  __ZN17CMultiPassControl17InitCplxHistQuantEv
0029474a  __ZN17CMultiPassControl17TranslateQpOffsetEi
00294777  __ZN17CMultiPassControl19finalPassSceneLevelEv
002947a6  __ZN17CMultiPassControl22MpConstantQpAccumulateEjjjiji
002947dd  __ZN17CMultiPassControl22finalPassSequenceLevelEv
0029480f  __ZN17CMultiPassControl23FirstPassStatsLookaheadEP21_S_AVE_MultiPassStats
00294859  __ZN17CMultiPassControl24CollectMultiPassStats_RCEP13sCommonParams9SliceTypejjj
002948a9  __ZN17CMultiPassControl24MpFinalPassSceneBitratesEfb
002948de  __ZN17CMultiPassControl26CollectMultiPassStats_LRMEEP13sCommonParamsj
00294924  __ZN17CMultiPassControl26MpFinalPassUpdateSeqRcInfoEv
0029495a  __ZN17CMultiPassControl31CollectMultiPassStats_MCPUs_AVCEP13sCommonParamsjjPv
002949a8  __ZN17CMultiPassControl32CollectMultiPassStats_MCPUs_HEVCEP13sCommonParamsjjjjPv
002949f9  __ZN17CMultiPassControlC1Ev
00294a15  __ZN17CMultiPassControlD1Ev
00294a31  __ZN17CMultiPassControlD2Ev
00294a4d  __ZN17CSharedMemoryHeap4FreeEPv
00294a6d  __ZN17CSharedMemoryHeap4heapE
00294a8b  __ZN17CSharedMemoryHeap6MallocEmjP7CObject
00294ab6  __ZN17CSharedMemoryHeap8instanceE
00294ad8  __ZN17CSharedMemoryHeapC1EPKcP7CObjectPvm
00294b02  __ZN17CSharedMemoryHeapC2EPKcP7CObjectPvm
00294b2c  __ZN17CSharedMemoryHeapD0Ev
00294b48  __ZN17CSharedMemoryHeapD1Ev
00294b64  __ZN17CSharedMemoryHost18virtualBaseAddressE
00294b91  __ZN17CSharedMemoryHost4TaskEv
00294bb0  __ZN17CSharedMemoryHost6SignalEPv
00294bd2  __ZN17CSharedMemoryHost6cookieE
00294bf2  __ZN17CSharedMemoryHost8instanceE
00294c14  __ZN17CSharedMemoryHostC1EPKcP7CObjectibP15CChannelManagerm
00294c50  __ZN17CSharedMemoryHostC2EPKcP7CObjectibP15CChannelManagerm
00294c8c  __ZN17CSharedMemoryHostD0Ev
00294ca8  __ZN17CSharedMemoryHostD1Ev
00294cc4  __ZN17CSharedMemoryHostD2Ev
00294ce0  __ZN18CAVEPipeISRManager11GetSlicePosERjPj
00294d0b  __ZN18CAVEPipeISRManager12GetSizeQueueERjPj
00294d37  __ZN18CAVEPipeISRManager12TimerHandlerEPv
00294d61  __ZN18CAVEPipeISRManager13DmaErrHandlerEPvy
00294d8d  __ZN18CAVEPipeISRManager13PiodmaHandlerEPvy
00294db9  __ZN18CAVEPipeISRManager13ResetSlicePosEv
00294de3  __ZN18CAVEPipeISRManager14DMVDoneHandlerEPv
00294e0f  __ZN18CAVEPipeISRManager14ResetSizeQueueEv
00294e3a  __ZN18CAVEPipeISRManager15AxiErrorHandlerEPv
00294e67  __ZN18CAVEPipeISRManager15LRMEDoneHandlerEPv
00294e94  __ZN18CAVEPipeISRManager16HMESCDoneHandlerEPv
00294ec2  __ZN18CAVEPipeISRManager16TranscodeHandlerEPv
00294ef0  __ZN18CAVEPipeISRManager17AvcXcWrBfrHandlerEPv
00294f1f  __ZN18CAVEPipeISRManager17LRMERCDoneHandlerEPv
00294f4e  __ZN18CAVEPipeISRManager18AvePipeDoneHandlerEPv
00294f7e  __ZN18CAVEPipeISRManager19CveSeb5WrBfrHandlerEPv
00294faf  __ZN18CAVEPipeISRManager19HevcPipeDoneHandlerEPv
00294fe0  __ZN18CAVEPipeISRManager19HevcXc0WrBfrHandlerEPv
00295011  __ZN18CAVEPipeISRManager19HevcXc1WrBfrHandlerEPv
00295042  __ZN18CAVEPipeISRManager20HevcTranscodeHandlerEPv
00295074  __ZN18CAVEPipeISRManager20TranscodeDoneHandlerEPv
002950a6  __ZN18CAVEPipeISRManager21AveEncPipeDoneHandlerEPv
002950d9  __ZN18CAVEPipeISRManager21AveStfPipeDoneHandlerEPv
0029510c  __ZN18CAVEPipeISRManager24AvccavlcDecodeErrHandlerEPvy
00295143  __ZN18CAVEPipeISRManager24HevcTranscodeDoneHandlerEPv
00295179  __ZN18CAVEPipeISRManager7MaskAllEv
0029519c  __ZN18CAVEPipeISRManager8instanceE
002951bf  __ZN18CAVEPipeISRManagerC1EPKcP7CObjectyibPPVmP14AVE_PIODMACtrl
002951ff  __ZN18CAVEPipeISRManagerC2EPKcP7CObjectyibPPVmP14AVE_PIODMACtrl
0029523f  __ZN18CAVEPipeISRManagerD0Ev
0029525c  __ZN18CAVEPipeISRManagerD1Ev
00295279  __ZN18CAVEPipeISRManagerD2Ev
```
