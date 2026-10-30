# `usr/standalone/firmware/DP865/X2232_LGD_BUNDLE_LC8.bin`

- File size: 32,088,064 bytes

## Payload [FW]

- Size after IM4P unwrap / decompression: 32,088,064 bytes
- Format: raw binary

## Strings (4,335) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.
First 4,000 of 4,335.

```
0010010f  bklc1C
00100163  cabl1C
001001b7  dis01t
0010023c  dis11t
001002c1  dis21t
00100346  dis31t
001003cb  frmc1C
0010041f  tcon1t
001004a4  trin1C
001006a5  MANP1p
00100726  OBJP1&
00100837  ~+?Abz+
00103542  ahi`!h
0010398b  fJF)F F&`NF
00103be7   pGpGpGpG8
00103eb8  SIGRTMEM: Out of heap memory
00103ed8  : Heap memory corrupted
00104060  READ OTP ADDRE:%2x
00104074  READ OTP VALUE:%2x
00104088  READ OTP TCON_EERROR Time Out!
001041bc  WRITE OTP
001041c8  Write OTP TCON_EERROR Time Out!
0010446d  qHF*F#F
00104665  qHF*F#F
00104940  OTP Unlock TCON_EERROR!
00104e31  !i`ihX"b
00104ed3   h`hhX!a
00105039  !i`ihX"b
001050db   h`hhX!a
001065d8  CLEAR SYSIRQ(H) :%x
001065f0  RCVD SYSIRQ CLR(0x%X) WOT EN , EN:0x%X
00106618  Clearing FW SYSIRQ : 0x%X
00106634  CLEAR SYSIRQ MASK: NULL PTR
00106764  SYS IRQ REG MASK NULL PTR
0010680c  EN SYSIRQ : %d
0010681c  EN SYSIRQ(HOST NOT REG) : %d
0010683c  INVLD SYSIRQ SET  : %d
00106900  TCON_UARP_AllHeadersAndMetaDataComplete()
001069e0  TCON_UARP_ApplyStagedAssets()
00106b00  Save Signed Manifest:
00106b45  @pGTCON_UARP_AssetProcessingNotification2()
00106ba5  @pGTCON_UARP_AssetProcessingNotificationAck()
00106c48  TCON_UARP_AssetReady()
00106d94  TCON_UARP_HWVersion()
001070f8  TCON_UARP_MfrName()
00107148  TCON_UARP_ModelName()
001071cc  TCON_UARP_OTP_FusingType()
0010761c  TCON_UARP_PayloadData() 4cc: %s, Offset: %d, len: %d
001078f8  TCON_UARP_PayloadDataComplete2()
0010791c  CRC32:  0x%08x
0010792c  Payload Hash Match: Fail)
00107948  Payload Hash Match: Pass)
001079f0  TCON_UARP_PayloadMetaDataTLV() tlvType: 0x%08x
00107a80  TCON_UARP_PayloadReady()
00107af8  TCON_UARP_OTP_PROD()
00107bc4  TCON_UARP_RescindAllAssets()
00107c5c  TCON_UARP_OTP_SDOM()
00107c74  SDOM: 0x%08x, SDomain: %d
00107ce4  securityMode: %d
00107d80  TCON_UARP_SendMessage() buf: 0x%08x, len: %d
00107db0  urp_q_tx_buf: 0x%08x
00107dc8  [ERROR] UARP_TX_BUF_Q: FULL
00107e24  TCON_UARP_SNo()
00107f9e  8FIF"F
00107fb0  asset_numPayloads: %d
00107fc8  uarpPlatformEndpointAssetQueryNumberOfPayloads(): Error
0010804c  TCON_UARP_Vendor()
00108bb5  [ERR]: 
00108bc0  WDOG Bite Error
00108c44  NVM DeviceID : 0x%x
00108c58  Failed to initialize DMA driver: 0x%x
00108c80  Failed to initialize NMI: 0x%x
00108e58  DispSHA2Pass
00108e68  BlfwSHA2Pass
00108e78  FcfwSHA2Pass
00108e88  TrinSHA2Pass
00108e98  CablSHA2Pass
00108ed1  x2ysy4z
001091b9  New APICmd: %02x %02x %02x %02x %02x %02x
001091e4  api_rcvd_to_process_time_us: %llu
00109209  tcon_time_us: %llu
0010921c  Soft Resetting Banyan
0010935f  `&i%afi
0010942d  e n%f`nef
00109540  dma timeout
0010954c  dma error
00109558  dma_failed status: 0x%08x, 0x443C8030: 0x%08x
00109588  dma failed
00109c6c  flash erase address: 0x%08x, size: 0x%08x
00109e60  flash ID not supported, use W25Q01NWTBIQ as default
00109e94  mode not availabe for current flash
0010a13d  nonce: 0x%2x%2x%2x%2x bnch: 
0010a5b0  earse_flash Err
0010a780  API RD INVLD SYSIRQ BUF SIZE :%d
0010a8ac  Start g_mem_address: 0x%08x
0010adb1  [ERR]: 
0010adbc  MCU: %d, SHA256 Failed
0010b1dc  BootldrStart
0010b1f0  %s Version 0x%x 
0010b204  Bootloader
0010b210  Failed setting PLL
0010b224  BSP Init Failed
0010b234  FW_Image: 0x%08x
0010b248  u8FW_LOAD_DIS: 0x%02x
0010b260  RecoveryMode
0010b270  BootldrDone
0010b2f8  API MNG INVLD SYSIRQ OPT :%d
0010b77c  PROD UnProgrammed!
0010b790  PROD Programmed!
0010b7a4  PROD_prog_status: 0x%x, 0x%x, 0x%x
0010b864  SDOM UnProgrammed!
0010b878  SDOM Programmed!
0010b88c  SDOM_prog_status: 0x%x, 0x%x, 0x%x
0010b91c  Program PROD Pass!
0010b930  Program PROD Fail!
0010b9b4  Program SDOM Pass!
0010b9c8  Program SDOM Fail!
0010bafd  SHA256: 
0010be3c  SETINFO_SUBCMD_OTP
0010be50  SETINFO_SDOM_PROG
0010be64  SETINFO_PROD_PROG
0010c154  RdAPI Status: 0x%02x
0010c3f0  API MNG INVLD SYSIRQ SUBCMD :%d
0010c4bc  read_packet_addr: 0x%08x, len: %d
0010c598  API Status: %02x
0010c5ac  API Error: %02x
0010c5c0  tcon_time_us: %llu
0010c7d9  **SHA Failed**
0010ca95  h!`Aha`
0010cab4  urp_q_pop: wrap
0010cac5  urp_send_msg_pop: addr: 0x%08x, len: %d
0010cb40  urp_q_push: wrap
0010cb55  urp_new_msg_push addr: 0x%08x, len:%d 
0010d324  PFYF"F
0010d5e0  uarpFree() mem: 0x%08x
0010d998  5"@FIF5%
0010ddaf  0(F!FBF
0010ddf1  0(F!FBF
0010ddff  G(F!FBF
0010df00  5"@FIF5%
0010e688   F1F*FCF
0010e6a2   F1F*FCF
0010e88a  XFAF2F
0010e9e0  XFAF"F
0010ea6e  XFAF"F
0010eb3c  ( XFAF
0010ec2c  XFAFRF
0010ec3f  "XFAF#F
0010ec5e  XFAF*F;F
0010ed20  XFAFJF
0010ed6d  "XFAFSF
0010ee6b  "XFAF+F
0010eeaa  XFAF"F
0010eebc  XFAF2FKF
0010ef02  XFAF*F
0010efc3  "XFAF+F
0010efd7  FXFAF*F#F
0010f02e  XFAF2F
0010f0ac  XFAF"F
0010f13e  HPXFAF#F
0010f222  XFAF:F
0010f327  FXFAF"F
0010f3ae  XFAF*F
0010f414  XFAF:F
0010f4a0  [h;ach
0010f4ee  XFAFJF^
0010f4f8  XFAF:F
0010f510  XFAF2F
0010f54a  XFIFRF
0010fffd  [INFO]: 
00110008  write_uarp_api_callback()
001107b0  WrAPI Status: 0x%02x
00111358  0123456789ABCDEF@0X
0011136c  0123456789abcdef@0x
001117d0  uarpZalloc() mem: 0x%08x, len:%d
001117f2  TCON_UARP_AssetMetaDataComplete() numPayloads:%d
00111825  [INFO]: 
0011182e  TCON_UARP_PayloadMetaDataComplete()
00111852  NVM_W_ADDR:  0x%08x, size: %d
00111870  TCON_UARP_SuperBinaryOffered(): numPayloads: %d, superbinary version: %d.%d.%d.%d
001118c7  TCON_UARP_PayloadDataComplete2 payloadIndex: 0x%04x
001118fb  NVM_W_ADDR:  0x%08x
0011190f  Bufaddr: 0x%08x
00111921  g_mem_address: 0x%08x
00111939  count_loop : %d
0011194a  FW Hash Check Failed
00111960  In DFU Recovery Mode
00111977  [ERR]: 
0011197f  CablSHA2Err
0011198b  TrinSHA2Err
00111997  DispSHA2Err
001119a3  FcfwSHA2Err
001119af  BlfwSHA2Err
001119be  FW_POINTER:  0x%08x
001119d2  TLV: 0x%04x, size: 0x%08x
001119ec  g_flash_address: 0x%08x
00111a04  API MNG INVLD SYSIRQ BUF SIZE :%d
00111a2d  flash erase_flash64k address: 0x%08x, size: 0x%08x
00111a61  flash erase_flash4k address: 0x%08x, size: 0x%08x
00111a94  SPI_Sector64KErase_FIFO0 Err
00111ab1  SPI_SectorErase_FIFO0 Err
00111acb  erase_flash64k Err
00111ade  erase_flash4k Err
00111af0  Expected Size: %08x
00111b05  RdBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00111b59  WrBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00111bad  RdBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00111c01  WrBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00111c55  SYS IRQ RD MASK NULL PTR
00111d4d  @PD8FPD
00111d55  FPD|FPD
00111d75  FPD #PD
00111d7d  FPD`#PD
00131558  pGpGpG8
001316ac  ahi`!h
00131dcf  fJF)F F&`NF
00132bbc  SIGRTMEM: Out of heap memory
00132bdc  : Heap memory corrupted
00132e83  (/FDF0F
00132ea3  F8F!FRF[F(
00132ed3  ((FAFRF[F
00132f68  calculated SVCLK too small: %f
00132f88  htotal is 0
00133254  READ OTP ADDRE:%2x
00133268  READ OTP VALUE:%2x
0013327c  READ OTP TCON_EERROR Time Out!
00133484  WRITE OTP
00133490  Write OTP TCON_EERROR Time Out!
001335b7  D ``hah
001336c7  P(`hhih
001338d0  Scaler Status: 0x%02x
0013420c  refresh rate: %f
00134220  htotal 0
00134323  <IFBF[F
0013469c  [LBA] INVALID BLCK ID TO CHECK %d
001346c0  [LBA] INVALID SIZE FOR %d, received : %d, expected : %d
001347e0  RCVD INVALID BLOCK FOR SIZE : %d
00134995  TailIndex : %d
001349a5  New TailIndex : %d
001349b8  LBA HDR WRITE FAIL : %d , BLCK:%d
001349dc  LBA BLK INIT BLOCKID : %d :: ADDR : 0x%x
00134a08  LBA HDR CONST FAIL : %d
00134b80  L2P START
00134b8c  L2PStart   
00134b98  LBA INIT FAIL :%d
00134bac  LBA SHOULD NEVER COME HERE
00134bc8  LBA INVALID HEADER : %d
00134be0  LBA FREE TAIL:%d
00134bf4  L2PDone    
00134c00  L2P DONE
00134d80  Skip ERASE PREV ASSIGNED ADDRESS: 0x%x
00134df0  LBA FREE Q FULL : %d
00134ff4  LBA READ OFFSET IS 0, SHOULD NEVER COME HERE 
00135024  LBA RD FAIL : %d
00135038  LBA RD INVALID CALCULATED ADDR : 0x%x :: BLOCKID : %d
0013525c  !FBFKF
00135452  !FRFCF
00135774  OTP Unlock TCON_EERROR!
00135841  [ERR]: 
0013584c  GetPNGData Error
00135d58  PNG FileSize: 0x%x
00135d6c  width x height: %d x %d
00135d84  PNG_test with error: %d
00135d9c  PNG File Too Big
00136281  !i`ihX"b
00136323   h`hhX!a
00136481  !i`ihX"b
00136523   h`hhX!a
0013691c  scaler_ddp_attribt_not_stable
0013693c  master dp unstable irq
00136954  slave dp unstable irq
00136d3c  DSC enable not same in master and slave: %d, %d
00137068  get link rate TCON_EERROR
00137084  link rate: %f
00137094  resolution: %d x %d
001370ac  WET: 0x%08x
001370bc  WET is 0
001370c8  pixel clock:%f MHz
001370dc  WET not available
00137734  CLEAR SYSIRQ(H) :%x
0013774c  RCVD SYSIRQ CLR(0x%X) WOT EN , EN:0x%X
00137774  Clearing FW SYSIRQ : 0x%X
00137790  CLEAR SYSIRQ MASK: NULL PTR
00137904  SYS IRQ RD MASK INVALID ID
001379cc  SYS IRQ REG MASK NULL PTR
00137a54  EN SYSIRQ : %d
00137a64  EN SYSIRQ(HOST NOT REG) : %d
00137a84  INVLD SYSIRQ SET  : %d
00137b34  TCON_UARP_AllHeadersAndMetaDataComplete()
00137cb4  TCON_UARP_ApplyStagedAssets()
00137cd5  nonce: 0x%8x bnch: 
00137cf5  pFlags: 0x%4x
00137d4c  TCON_UARP_AssetMetaDataComplete() numPayloads:%d
00137de8  Save Signed Manifest:
00137e30  TCON_UARP_AssetProcessingNotification2()
00137e8c  TCON_UARP_AssetProcessingNotificationAck()
00137ef0  TCON_UARP_AssetReady()
00138028  TCON_UARP_HWVersion()
001383f8  TCON_UARP_MfrName()
00138444  TCON_UARP_ModelName()
001384c4  TCON_UARP_OTP_FusingType()
00138794  TCON_UARP_PayloadData() 4cc: %s, Offset: %d, len: %d
00138a00  TCON_UARP_PayloadDataComplete2()
00138a24  CRC32:  0x%08x
00138a34  Payload Hash Match: Fail)
00138a50  Payload Hash Match: Pass)
00138a98  TCON_UARP_PayloadMetaDataComplete()
00138b04  TCON_UARP_PayloadMetaDataTLV() tlvType: 0x%08x
00138b7c  TCON_UARP_PayloadReady()
00138bf0  TCON_UARP_OTP_PROD()
00138ca8  TCON_UARP_RescindAllAssets()
00138d34  TCON_UARP_OTP_SDOM()
00138d4c  SDOM: 0x%08x, SDomain: %d
00138dbc  securityMode: %d
00138e4c  TCON_UARP_SendMessage() buf: 0x%08x, len: %d
00138e7c  urp_q_tx_buf: 0x%08x
00138e94  [ERROR] UARP_TX_BUF_Q: FULL
00138eec  TCON_UARP_SNo()
0013903e  HFQF"F
00139050  asset_numPayloads: %d
00139068  uarpPlatformEndpointAssetQueryNumberOfPayloads(): Error
001390e8  TCON_UARP_Vendor()
00139775  GpGJn"
00139fa1  [ERR]: 
00139fac  WDOG Bite Error
0013a1cd  BLAPI: UpdatedLUMInBuf Pass
0013a1ed  BLAPI: UpdatedLUMInBuf Fail
0013a3b4  BLS_Sloper Update
0013a3c8  bls_sloper_time: %d
0013a3dc  BLS_Sloper Done
0013a3ec  BLS_Sloper Update Fail
0013a706  ;iYDWh
0013ab98  cal_wet
0013ade0  cal_wfm
0013ae65  [INFO]: 
0013ae70  SHA2 Input src_addr: 0x%8x size: 0x%8x
0013b058  SDP hwidth error: %d
0013b070  vheight not same in master and slave %d,%d
0013b09c  DDP hwidth error: %d
0013b21b  x2ysy4z
0013b34d  New APICmd: %02x %02x %02x %02x %02x %02x
0013b378  api_rcvd_to_process_time_us: %llu
0013b39d  tcon_time_us: %llu
0013b3b0  Soft Resetting Banyan
0013b5fc  start copy: latest dyncfg indx: %d, addr: %x
0013b62c  dyncfg_sha256_check: Pass
0013b649  g_dyncfg_validity_flags: %llu
0013b728  skip loading: DEP_CAL
0013b740  start copy: DEP_CAL_FC_LUTs
0013b75c  copy DEP_CAL_FC_LUTs failed
0013b778  copy DEP_CAL_INFO failed
0013b794  copy DEP_CAL_BL_LUTs failed
0013b86c  skip loading: LUT_0x180-0x189
0013b88c  start copy: LUT_0x%04x
0013b8a4  copy LUT_0x%04x failed
0013b938  Skip loading from nvm
0013bb14  skip loading: psf0-2
0013bb2c  start copy: psf0
0013bb40  copy psf0 failed
0013bb54  start copy: psf1
0013bb68  copy psf1 failed
0013bb7c  start copy: psf2
0013bb90  copy psf2 failed
0013bdf8  start copy: tcon luts
0013be10  copy tcon luts failed
0013be28  tconlutsFail
0013be38  tconlutsPass
0013be48  start copy: BL luts
0013be5c  copy BL luts failed
0013be70  blfwlutsFail
0013be80  blfwlutsPass
0013c8b4  ?hEaEbEcEdEeEf
0013c995  P?hhahbhchdhehf
0013d67c  0x44700504: 0x%x, timeout: %d
0013d69c  DDRx64 Init Done
0013d6b0  DDR Status: 0x%02x
0013d6c4  DDRInitFail
0013d6d1  [ERR]: 
0013d6dc  DDRx64 Init Failed
0013dccb  QAapGp
0013dd5f  `&i%afi
0013de2d  e n%f`nef
0013df40  dma timeout
0013df4c  dma error
0013df58  dma_failed status: 0x%08x, 0x443C8030: 0x%08x
0013df88  dma failed
0013ea53  bjPjX"
0013ea64  Video: Live
0013ea70  DPCD00107: 0x%02x DPCD001B0: 0x%02x, DPCD02020: 0x%02x
0013ee30  Unplugged, DP0 Aux_N DET=0
0013ee4c  Unplugged, DP1 Aux_N DET=0
0013eefc  BOARD_EVB
0013ef08  BOARD_TBB
0013f084  Preset load tcon %d dyncfg
0013f96c  flash erase address: 0x%08x, size: 0x%08x
0013fb58  time_sec: %d
0013fb68  temp_time: %d
001408a8  WPC in 0D
001408b4  OVD in 0D
001408c0  WPC, OVD in 0D
001408d0  PRC 1DT: 0x%04x
00140b30  flash ID not supported, use W25Q01NWTBIQ as default
00140b64  mode not availabe for current flash
00140db9  h1`)h!`iha`
00140dcb  `)i!aiiaa
00140df5  ` i(a`iha
00140e41  nonce: 0x%2x%2x%2x%2x bnch: 
0014151c  GET_LOG_COUNT: %d
00141531  [ERR]: 
0014153c  save_log failed due to NVM Read Error
00141564  NVM_LOG_COUNT: %d
001417d9  ObjTag: 0x%08x tag: 0x%08x
001417f4  exp_hash: 
00141980  IPC_HP_MSG_Q
00141a0c  IPC_NP_MSG_Q
00141d30  8F1Fbh
00142535  i=aUi}a
00142545  j=bUj}b
001427c4  DP0 Link Trained
001427d8  DP Cable: Unplugged
001427ec  DP Attrib: Stable
00142800  DDP Mode: %d
00142810  SetSrcAttr fail or attrib not stable, set to freerun
00142848  Cal SVCLK Fail
0014289c  ALL_H: Power Down Panel
001428b4  SPF_N: Power Down Panel
00142a60  DPCD600: 0x%02x
00142a70  HPD DeAssert
00142a80  Start DPCD600 time check
00142a9c  Start DPCD600 check cancel
00142ab8  Attrib: 0x%08x
00142ac8  Start DPCD600 time check done
00142d00  dpcd202 =1
00142d0c  dpcd202 =0
00142d18  g_dpcd427: 0x%02x, dpcd4f1: 0x%02x
00143008  DEP_CAL_HASH: SLOT: %d LUT_0x%04x failed
001430f4  USR_CAL_HASH: SLOT: %d LUT_0x%04x failed
00143322  Bb*`jhB
00143b57   BaBi*
00143f90  earse_flash Err
00144138  0F)FCF
00144146  f20F)FCF
0014534c  (PhaxyA
001457a5  [INFO]: 
001457b0  IPC(%d -> %d): 0x%02x, size: 0x%04x
001457d4  start copy: default dyncfg indx: 0
001457f8  copy default dyncfg failed
00145815  g_dyncfg_validity_flags: %llu
00145856  pGRiHy
00145c37  0Ha0yMi)F
00145cd4  API RD INVLD SYSIRQ BUF SIZE :%d
00145f30  start g_tcon_dram_address: 0x%08x
00145fa0  Start g_mem_address: 0x%08x
0014606e  T`CiThc
00146077  $T`CiTh
001461da  SaHjSi`
001461e3  #SaHjSi
001465d3  !y`yhh
0014671d  b:byjO
00146731  Aybyjb
00146739  Aybyj!
001468d3  b:dzl{l
00146eb0  init_scaler_enable1
00147135  26:>QQQQQQF  
00147608  SETINFO_SUBCMD_OTP
0014761c  SETINFO_SDOM_PROG
00147630  SETINFO_PROD_PROG
001477c9  [INFO]: 
001477d4  IPC(%d -> %d): 0x%02x, size: 0x%04x
00147836  ByKaKi#
0014796c  copy cpld from nvm to dram
00147988  copy cpld from nvm to dram failed
001479ac  stream cpld data...
001479c0  finish cpld program...
00147d85  0Ha0yMi)F
00147de4  ERROR: REMAIN BYTES:%d
00147f11  h!`Qha`
001480db  h!`Aha`
00148128  npq_pop: wrap
00148139  new_msg_pop: 0x%08x
00148197  `ahA`*h
001481b4  npq_push: wrap
001481c5  new_msg_push: 0x%08x
00148251  hp_new_msg ch: 0x%02x
001482a9  np_new_msg src: %d ch: 0x%02x
001482f2   F2FCF
00148366  (F1FBF
0014847a  AFJF+F
001484c8  Wait IPC(%d <- %d): 0x%02x
001484e4  IPC(%d <- %d): 0x%02x Recvd
0014865c  allow_user_cal: %d
00148670  calibration_space: %d
00148688  calib_header_id: 0x%x, lut_id: 0x%0x
001486b0  pp_ccm_header_id: 0x%x, lut_id: 0x%0x
00148a54  default_bl_led_zone_value: 0x%08x
00148b7e  >FRF1F
00148c45  [ERR]: 
00148c8b  qps0pp
00148c94  dp0_edid_displayid_size: %d
00148ceb  qps0pp
00148cf4  dp1_edid_displayid_size: %d
00148f04  dram_config sha256 failed
00148f20  DramCfgFail
00148f2c  DramCfgPass
00148f38  dram_config_hdr: 0x%08x
00148f50  dram_config_ver: 0x%08x
00148f68  dram_config_entries: 0x%08x
001491c0  User DepCal: Slot: %d
001491d8  Skip loading User DepCal: Slot: %d
001491fc  Factory DepCal: Slot: %d
00149218  Skip loading Factory DepCal: Slot: %d
001492bc  IndCaldone 
001492c8  DepCalHash 
001492d4  DepCaldone 
001492e0  psfdone    
00149302  8hFY F
00149404  1dql Cb
001496b8  tcon_config_hdr: 0x%08x
001496d0  tcon_config_ver: 0x%08x
001496e8  tcon_config_entries: 0x%08x
00149704  TconCfgFail
00149710  TconCfgPass
0014971c  Skip loading tcon_config
00149738  Apply P2 Panel Timing!
00149864  g_policy_flags: 0x%08x
001499b6  8FAFJF
00149a24  8`(D!FJF
00149c6f  ! DPE@
00149dc6  @F1FRF
00149df6  @F1FRF
00149e6c  YF2FSF
00149e90  YF2FSF
00149f86  YF2FSF
0014a048  decodeGeneric_exit
0014a2f2  "hci(F
0014aad4  lodepng_inflatev
0014aae8  lodepng_inflatev_error
0014ad78  (FaFBF
0014af1c  Erasing DB NVM Power Cycle Info Section
0014af44  pwrcyl_log_in_dbnvm: %d pwron_time_in_mins: %d
0014af74  total_power_on_time: %d
0014af94  ResetNow
0014b104  Options -> Error Checking Standard: SHA256
0014b130  Payload Size: %d bytes
0014b148  Payload Type: 0x%04x
0014b160  Payload LUT ID: 0x%04x
0014b178  Payload Version: %d.%d
0014b1e4  LUT address: 0x%08x
0014b374  Target SHA256: 
0014b38c  Target CRC: 0x%08x
0014b3a0  Compute CRC Size: %d
0014b3b8  Compute CRC: 0x%08x
0014bdac  8F1FBFKF
0014be95  "(FQF>h
0014bec2  @F1FZFKF
0014bf96  XF1FBFKF
0014c136  8F1FBFKF
0014c1b0  manage_factory_cal: sub_cmd=%x
0014c1d0  manage_factory_cal cm ind volatile last slice,[%d 0x%x]
0014c27c  API MNG INVLD SYSIRQ OPT :%d
0014c31c  manage_user_cal: sub_cmd=%x
0014d65d  hZaJhZe
0014d68d  hZaJhZe
0014d950  MBC Lost Lock
0014ddd8  PROD UnProgrammed!
0014ddec  PROD Programmed!
0014de00  PROD_prog_status: 0x%x, 0x%x, 0x%x
0014dec8  SDOM UnProgrammed!
0014dedc  SDOM Programmed!
0014def0  SDOM_prog_status: 0x%x, 0x%x, 0x%x
0014df84  Program PROD Pass!
0014df98  Program PROD Fail!
0014e01c  Program SDOM Pass!
0014e030  Program SDOM Fail!
0014e098  payload num: 0x%08x
0014e0b0  payload_id: 0x%08x
0014e0c4  payload_size: 0x%08x
0014e0dc  payload_global_addr_ptr: 0x%08x
0014e7be  Src MCU:%d, addr: 0x%08x
0014e7d8  Dst MCU:%d
0014e7e4  IPC Opcode:0x%02x
0014e7f8  Priority: %d, CHID: %d
0014e810  MsgSize: %d
0014e820  Msg: 0x%08x
0014e83c  FWCookie: 0x%x
0014e84c  Wait DB CLR
0014eb84  PNG_Decode[%d]: Start
0014eb9c  PNG_Decode[%d]: Success
0014ebb4  PNG_Decode[%d]: Error
0014ec34  PLS Fault: 0x%04x, Trigger Shutdown!
0014ecc8  PMIC Fault 0x%02x, 0x%02x, Trigger Shutdown!
0014f358  HPD DeAssert
0014f659  SHA256: 
0014f6b3  ohhxhhhhh
0014f954  SETINFO_SUBCMD_OTP
0014f968  SETINFO_SDOM_PROG
0014f97c  SETINFO_PROD_PROG
00150298  total_telemetry_in_dbnvm: %d, index: %x
001502c0  new_telemetry_in_dbnvm: 0x%08x
00151599   pGa pG-
00151798  PFAF2F
00151891   pGJ pG-
00151cd4  RdAPI Status: 0x%02x
00151dd4  CPLD Read: %d
001520d8  I2C Rd: Failed
001521ac  read_factory_cal: sub_cmd=%x
001525c0  Reading BLOCK : %d : offset : %d
001525f0  DONE READING JOURNAL DATA : %d
001526c4  RC GetInfo: %d
001526d4  I2C Rd: Failed
00152754  API MNG INVLD SYSIRQ SUBCMD :%d
0015280c  read_packet_addr: 0x%08x, len: %d
00152888  read_user_cal: sub_cmd=%x
00152cac  start copy: default dyncfg indx: %d, addr: %x 
00152cdc  copy default dyncfg failed
00152cf8  default_dyncfg_sha256_check: Fail
00152d1c  DynCfgFail
00152e6d  LED Aging Not Found in Journal
00152e8d  LED_Aging_Hash_Check: Fail
00152ea9  LED_Aging_Hash_Check: Pass
0015378c  save_log failed due to NVM Read Error
001537b4  NVM_LOG_COUNT: %d
001537c8  save_log failed due to NVM Erase Error
001537f0  save_log failed due to NVM Write Error
001539a5  Pending Data Size: %d
001539bd  Journal Write Error
00153acd  g_reset_counter: %d
00153b5e  4 CXBPO
00153c62  @BBPBXCX
00154079  Wge#e'h&h
00154189  ahb)b(h
00154850  API Status: %02x
00154864  API Error: %02x
00154878  tcon_time_us: %llu
00154e28  refresh_rate: %f, no_of_vblank: 0x%08x
00155179  **SHA Failed**
001556c0  wait for cdi vblank start timed out...
001556e9  sync_exit: %llu
0015599c  Fail: mmu_reset: 0x%x
001559b4  Fail: mmu_enable_disable: 0x%x
001559d4  Fail: mmu_remove_entry: 0x%x
001559f4  Fail: mmu_add_entry: 0x%x
00156211  h!`Aha`)h
00156230  urp_q_pop: wrap
00156241  urp_send_msg_pop: addr: 0x%08x, len: %d
001562bb  `*hahA`P
001562cc  urp_q_push: wrap
001562e1  urp_new_msg_push addr: 0x%08x, len:%d 
00157282  PFYF"F
0015745a  pGuarpFree() mem: 0x%08x
001577e0  5"@FIF5%
00157af1  0(F!FBF
00157b33  0(F!FBF
00157b41  G(F!FBF
00157c34  5"@FIF5%
00158184   F1F*FCF
0015819e   F1F*FCF
0015835a  XFAF2F
0015846b  FXFAF"F
001584a8  , XFAF
001585a0  XFAFRF
001585b3  "XFAF#F
001585d2  XFAF*F;F
00158698  XFAFJF
001586e9  "XFAFSF
001587b5  "XFAF+F
001587f4  XFAF"F
00158806  XFAF2FKF
00158850  XFAF"FO
00158892  XFAF*F
001589ac  XFAF"F
00158a40  XFAF"F
00158b54  XFAF:F
00158bea  XFAF2F
00158c8e  XFAFJF0
00158cf2  XFAF*F
00158d2b  "XFAF+F
00158d3d  FXFAF*F#F
00158d7e  HPXFAF#F
00158da2  XFAF:F
00158dae  XFAF:F
00158dc2  XFAF2F
00158e52  XFIFRF
001595b0  uarpZalloc() mem: 0x%08x, len:%d
00159659  [INFO]: 
00159664  write_uarp_api_callback()
00159a84  Scaled: Htotal %d Hwidth %d Vheight %d
00159aac  Scaler Disabled: Htotal %d Hwidth %d Vheight %d
00159c8c  status_verify_cal()
00159ca0  manage_factory_cal cm dep last slice,[%d 0x%x]
00159cd0  payload_lut_id: 0x%04x
00159ce8  Verify Status: %d
0015a1bc  zsXC!`)h``
0015a468  WrAPI Status: 0x%02x
0015a558  CPLD Write: %d
0015a8d0  Device Write: %d
0015a8e4  I2C Wr: Failed
0015aba8  RCVD SIZE : %d
0015abb8  Writing BLOCK : %d : offset : %d
0015abdc  DONE WRITING JOURNAL DATA : %d
0015ac8c  RC Write: %d
0015ac9c  I2C Wr: Failed
0015ad38  0F!F:FCF
0015ad98  9FBFSF
0015b153  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
0015c7d8  0123456789ABCDEF@0X
0015c7ec  0123456789abcdef@0x
0015c811  0123456789abcdefxp
0015c824  0123456789ABCDEFXP
0015ca68  UUUUUU
0015d535  Qkkbal
0015d7f3  -NVM DeviceID : 0x%x
0015d809  CDPwrLo     
0015d816  RCRstEnd    
0015d823  MainPwrLo    
0015d831  HiChkFail   
0015d83e  LoChkFail   
0015d84b  HiChkPass   
0015d858  LoChkPass   
0015d865  RCRstStart  
0015d873  [INFO]: 
0015d87d  [ERR]: 
0015d885  CDPwrPGFail 
0015d892  MnPwrPGFail 
0015d89f  CDPwrPGPass 
0015d8ac  MnPwrPGPass 
0015d8b9  Failed to create Global Timer: TIMER_INST_0
0015d8e5  Failed to create Local Timer: TIMER_INST_1
0015d910  Failed to enable MLBDSP HB
0015d92b  MLBDSP HB Enabled
0015d93d  DefaultPDone
0015d94a  MLBDSPHBFail
0015d957  FC WDOG Bite Error
0015d96a  CABL WDOG Bite Error
0015d97f  TRIN WDOG Bite Error
0015d994  MLBDSPHBPass
0015d9a1  Failed to initialize NMI: 0x%x
0015d9c0  Failed to initialize IPC HP Queue: 0x%x
0015d9e8  Failed to initialize IPC NP Queue: 0x%x
0015da10  Failed to initialize DMA driver: 0x%x
0015da36  Failed to initialize WDOG driver: 0x%x
0015da5d  Failed to initialize UART driver: 0x%x
0015da84  Failed to initialize Doorbell driver: 0x%x
0015daaf  MLBDSP Ver: 0x%02x
0015dac2  IPC(%d -> %d): 0x%02x, size: 0x%04x
0015dae7  Switch UUID: 
0015daf5  IPC(%d -> %d), IPC_BLS_2DT_DATA
0015db15  IPC(%d -> %d), IPC_API_RD_CMD
0015db33  IPC(%d -> %d), IPC_API_WR_CMD
0015db51  IPC(%d -> %d), IPC_LED_AGING
0015db6e  IPC(%d -> %d), IPC_BLU_FAULT_INFO
0015db90  IPC(%d -> %d), IPC_OPCODE_SDP
0015dbae  IPC(%d -> %d), IPC_API_RD_RESP
0015dbcd  IPC(%d -> %d), IPC_GEN_RESP
0015dbea  lbuf_int_latency: %lld in usec
0015dc0a  duration_of_final_frame in usec: %llu
0015dc31  g_cdi_poweroff_time_ticks: %llu
0015dc52  g_lbuf_vbstart_global_time_ticks: %llu
0015dc7a  start_time_ticks: %llu
0015dc92  g_lbuf_vbstart_time_ticks: %llu
0015dcb2  FWCookie[%d]: 0x%x, lbuf_cookie: 0x%x
0015dcd8  ERR : %s
0015dce2  prc_header_id: 0x%x, lut_id: 0x%0x
0015dd06  ctp_ccm_header_id: 0x%x, lut_id: 0x%0x
0015dd2e  pwm_gain_header_id: 0x%x, lut_id: 0x%0x
0015dd57  start slot: %d hash: LUT_0x%04x
0015dd78  Apply P1 Panel Timing!
0015dd8f  copy FC luts failed
0015dda3  copy trinity luts failed
0015ddc1  trinlutsFail
0015ddce  fcfwlutsFail
0015dddb  FWCfgSHAErr
0015dde7  start copy: DEP_CAL_BL_LUTs
0015de03  FWCfgSHAPass
0015de10  DynCfgPass
0015de1b  trinlutsPass
0015de28  fcfwlutsPass
0015de35  start copy: FC luts
0015de49  start copy: trinity luts
0015de62  loading scaler_luts
0015de76  EOTF_MAP: 0x%08x
0015de87  pre_scaler_lut_dram_start_addr: 0x%08x, size: 0x%08x exp_crc: 0x%08x
0015decc  post_scaler_lut_dram_start_addr: 0x%08x, size: 0x%08x exp_crc: 0x%08x
0015df12  Exit DDR retention PASS
0015df2b  Exit DDR Failed, Retry
0015df43  PDStart     
0015df50  PDComplete  
0015df5d  RC_RST_DONE!
0015df6a  retention pre step FAIL!
0015df83  retention assert FAIL!
0015df9a  retention pre step PASS!
0015dfb3  retention assert PASS!
0015dfca  In retention mode!
0015dfdd  Not in retention mode!
0015dff4  Enter or Exit retention mode!
0015e012  enter_dram_retention_done!
0015e02d  exit_dram_retention_done!
0015e047  Enter dram retention for PD
0015e063  DDREXRETDONE
0015e070  RETPOSCAFAIL
0015e07d  RETPOSACFAIL
0015e08a  RETPOSRDFAIL
0015e097  RETPOSWDFAIL
0015e0a4  RETPOSRLFAIL
0015e0b1  RETPOSWRFAIL
0015e0c4  DDR Deassert PASS
0015e0d6  RETPOSCAPASS
0015e0e3  RETPOSACPASS
0015e0f0  RETPOSRDPASS
0015e0fd  RETPOSWDPASS
0015e10a  RETPOSRLPASS
0015e117  RETPOSWRPASS
0015e124  DB_STRAP_OUTER_LO_ENABLE Fail
0015e142  CDPWR_PG Fail
0015e150  MAINPWR_PG Fail
0015e160  DDR Deassert Fail
0015e173  all_mcu_off_time: %llu
0015e18b  pd_seq_time: %llu
0015e19e  cdi_to_mainpwr_time: %llu
0015e1b9  rc_rst_time: %llu
0015e1cb  BoardID : 0x%02x, VendorID : 0x%02x, HWCID0 : 0x%02x, HWCID1: 0x%02x
0015e210  DDR Status: 0x%02x
0015e223  ecid[3:0]: 0x%08x
0015e235  ecid[7:4]: 0x%08x
0015e247  RegRd: 0x%08x = 0x%08x
0015e25e  Reg: 0x%08x = 0x%08x
0015e273  RegWr: 0x%08x = 0x%08x
0015e28a  TAIL : %d, HEAD: %d, Count : %d 
0015e2ac  FAIL : %d
0015e2b7  NO MORE FREE BLKS : %d
0015e2cf  LBA WR SUCESS BLK ID :%d, Size : %d, ADDR: 0x%0x
0015e301  LBA RD NULL ADDR
0015e312  LBA WR NULL ADDR
0015e323  LBA RD INVLD  BLOCKID : %d
0015e33e  LBA WR INVLD  BLOCKID : %d
0015e359  LBA INIT BLOCK FAIL WR  BLOCKID : %d
0015e37e  LBA WD INVALID F ADDR : 0x%x :: BLOCKID : %d
0015e3ab  LBA HEADER INVALID : %d
0015e3c3  LBA RD INVLD SIZE : %d
0015e3da  LBA FREE Q EMPTY : %d
0015e3f0  INVALID PREV ASSIGNED ADDRESS, COULD BE NEW ALLOC ID: %d
0015e429  FAILED TO ERASE PREVIOUS ADDRESS : %x, blockid:%d
0015e45b  ERROR: FAIL READ ADDR : %x
0015e476  ERASE PREV ASSIGNED ADDRESS: 0x%x
0015e498  LBA WR FAILED BLK ID :%d, Size : %d, ADDR: 0x%0x
0015e4ca  g_reset_counter: %d
0015e4e0  g_dyncfg_validity_flags: %llu
0015e4fe  DPCD202: 0x%02x, 0x%02x
0015e516  FaultIndex: %d
0015e525  NVM_LOG_COUNT: %d, ADDR: 0x%08x
0015e545  REG_SHARED_0 : 0x%x
0015e55a  BuildL2P    
0015e567  PANELUP    
0015e573  PnlSeqEnd   
0015e580  DDRRetExit  
0015e58d  DDRExitFail 
0015e59a  PnlSeqStart 
0015e5a7  ASSERT_SYSIRQ
0015e5b5  Stage: %d
0015e5c3  DispFWStart
0015e5d0  pu_seq_time: %llu
0015e5e2  ChipID: 0x%08x, DispFW Version: 0x%x, LC: 0x%x
0015e611  Failed to initialize MMU driver: 0x%x
0015e637  Lib Version - Scaler: 0x%08x, HDCP: 0x%08x Analog: 0x%08x
0015e671  DDR Status: 0x%08x
0015e684  flash erase_flash64k address: 0x%08x, size: 0x%08x
0015e6b8  flash erase_flash4k address: 0x%08x, size: 0x%08x
0015e6eb  SPI_Sector64KErase_FIFO0 Err
0015e708  SPI_SectorErase_FIFO0 Err
0015e722  erase_flash64k Err
0015e735  erase_flash4k Err
0015e747  Expected Size: %08x
0015e75c  RdBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0015e7b0  WrBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0015e804  RdBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0015e858  WrBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0015e8ac  Fail: mmu_enable_disable (1): 0x%x
0015e8cf  Skip loading dram_config
0015e8e8  SYS IRQ RD MASK NULL PTR
0015e901  Wet failed at dp out, wet value = 0x%x
0015e929  WET changes: 0x%08x, 0x%08x, 0x%08x
0015e94e  scaler fail, set to freerun: 0x44008074: 0x%08x
0015e97f  Wet failed at dp out, wet value = 0x%08x
0015e9a9  Attrib not stable, set to freerun-1
0015e9cd  Attrib not stable, set to freerun-3
0015e9f1  Attrib not stable, set to freerun-4
0015ea15  Scaler Started but not locked!
0015ea34  Attrib Not Stable, set to freerun-5
0015ea58  DP Cable: Plugged
0015ea6a  Scaler Locked
0015ea78  DP RX Config Done
0015ea8a  Scaler Error
0015ea97  restart mode condition hit
0015eab2  HPD Assert
0015eabe  tcon_time_us: %llu
0015ead1  scaler finish 0: %x
0015eae5  dpcd427: 0x%02x, dpcd4f1: 0x%02x
0015eb06  Set to Freerun, DP Attrib: Not Stable 0x440000B4 0x%08x
0015eb3e  Attrib: 0x%08x
0015eb60  bpp: 0x%08x
0015eb6c  Set SVCLK to %f MHz
0015eb80  SCL->SCL_REG_SCL_CTRL16.field.SCL_REG_43: 0x%02x
0015ebb2  SCL->SCL_REG_SCL_CTRL16.field.SCL_REG_44: 0x%02x
0015ebe4  Input total hwidth is not supported!
0015ec09  scaler_ddp_msa_not_matching
0015ec25  scaler_ddp_video_train_fail
0015ec41  BER error: %d
0015ec50  margin status error: 0x%02x
0015ec6d  Link rate error
0015ecb9  UV for idx: %d
0015ecc9  start_lut_slice %d : end_lut_slice %d
0015ecf0  final_start_lut_slice %d : final_end_lut_slice %d
0015ed23  illegal gain
0015ed31  Time off found to be %d, for given sample of %x and samples in LUT: %x, %x, %x
0015ed81  Sample: %d, 0x%x
0015ed93  pot gain: 0x%x
0015eda3  Readback ADC CFG register: 0x%x
0015edc4  RCDone     
0015edd0  RCStart    
0015eddc  Loading default RC Cal!
0015edf4  Aging: Trigger RC Self-Cal!
0015ee10  Updating RC Self-Cal to Journal!
0015ee31  fc_notify_power_on!
0015ee45  rc_single_shot error, cancel lut generation!
0015ee73  Initializing RC Timer...
0015ee8c  soc_timer_status: 0x0202
0015eea5  soc_timer_status: 0x0303
0015eebe  soc_off: %d, rc_off: %d
0015eed6  initial current_gain_setting: 0x%x timer_idx: %d
0015ef07  Check RC Aging
0015ef16  default_rc_lut_sha256_check: Fail
0015ef38  RcLutCfgFail
0015ef45  Read Values out of LUT boundaries
0015ef67  RcLutCfgPass
0015ef74  sampled: %x
0015ef80  initial: %x
0015ef8c  sim gain: %x
0015ef99  idx: %x
0015efa1  Wrote ADC CFG register: 0x%x, 0x%x
0015efc4  initial adc_arr cfg[0]: 0x%x cfg[1]: 0x%x
0015efee  adc gain: 0x%x
0015effd  Readback ADC CFG register: 0x%x
0015f01d  Init ADC CFG register: 0x%x
0015f039  Init POT register: 0x%x
0015f051  soc_timeoff_reg: 0x%08x
0015f084  data: 0x%04x
0015f091  BLS CPLD0  DeviceID:  0x%08X
0015f0af  BLS CPLD1  DeviceID:  0x%08X
0015f0cd  CPLD DeviceID:  0x%08X
0015f0e5  CPLD Set Config Addr to 0
0015f0ff  I2C WrRd: Failed
0015f110  I2C Wr: Failed
0015f11f  CPLD Erase Failed
0015f131  CPLD Enter Background Mode
0015f14c  CPLD Exit Config Mode
0015f162  CPLD Exit Program Mode
0015f179  CPLD Erase Done
0015f189  CPLD Program Done
0015f19b  CPLD Erase Not Done
0015f1af  CPLD Reset Config
0015f1c4  CPLD Erase Start
0015f1d5  CPLD ProgDone Timedout
0015f1ec  CPLD Erase Timedout
0015f200  CPLD Program Timedout
0015f216  CPLD Busy Timeout
0015f228  Erase Status 0x%08x
0015f23c  DBCalEnd    
0015f249  DBCalStart  
0015f256  DB_NVM_CAL_End, Result: %d
0015f271  DB_NVM_CAL_Start
0015f282  DB_NVM_Status: 0x%02x
0015f298  Bufaddr: 0x%08x
0015f2aa  g_tcon_dram_address: 0x%08x
0015f2c8  g_mem_address: 0x%08x
0015f2e1  ipc_status: 0x%02x 
0015f2f6  ipc_result: 0x%08x 
0015f30a  manage_factory_cal cm ind last slice,[%d 0x%x]
0015f33a  manage_factory_cal psf volatile last slice,[%d 0x%x]
0015f370  manage_factory_cal cm dep volatile last slice,[%d 0x%x]
0015f3a9  manage_factory_cal psf last slice,[%d 0x%x]
0015f3d6  slot: %d, id: %d
0015f3e8  flash address: 0x%08x, size: 0x%08x
0015f40d  64k_block#:%d size: 0x%08x
0015f429  flash address: 0x%08x
0015f440  dram address: 0x%08x
0015f456  Options -> Error Checking Standard: CRC32
0015f480  Header Version: %d.%d
0015f496  Options -> Enable Integrity Check: No
0015f4bc  Options -> Enable Integrity Check: Yes
0015f4e3  LUT allocated Size: %d bytes
0015f500  LUT actual Size: %d bytes
0015f51a  Consumers: 0x%02x
0015f52c  Header ID: 0x%04x
0015f53e  LUT id: 0x%04x
0015f54d  GetInfo UsrAddr: 0x%04x: 0x%08x
0015f56d  SetInfo UsrAddr: 0x%04x: 0x%08x
0015f58d  data: %x
0015f596  dram_addr: 0x%08x
0015f5a8  API MNG INVLD SYSIRQ BUF SIZE :%d
0015f5cb  TLV: 0x%04x, size: 0x%08x
0015f5e5  g_flash_address: 0x%08x
0015f5fd  NVM_W_ADDR:  0x%08x, size: %d
0015f61b  TCON_UARP_SuperBinaryOffered(): numPayloads: %d, superbinary version: %d.%d.%d.%d
0015f66d  TCON_UARP_PayloadDataComplete2 payloadIndex: 0x%04x
0015f6a1  NVM_W_ADDR:  0x%08x
0015f701  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
0015fa00  ,0PDRZ
0015fb81  #PD(FPD$
0015fc7f  btfwb 
0015fccc  rm0JNT$pldR/
0015fcf4  <%pcdcJ3
002a191b  fJF)F F&`NF
002a2574  %HxDT8
002a258c  !HxDT8
002a26bc  ahi`!h
002a274f  `+F2FIF8F
002a2964  pGpGpGpG8
002a2b14  SIGRTRED: Redirect: can't open: 
002a2c24  SIGRTMEM: Out of heap memory
002a2c44  : Heap memory corrupted
002a2de4  [ERROR]:[AH FB] INVLD LKP VALUE :[%d] = %d
002a3154  [INFO]:FF : SKIP (%x)
002a316c  [INFO]:FF :%x
002a3268  [WARN]:BLBIST : ALRDY %d
002a3350  [ERROR]:BLBIST: INVALID CUR %d, %d 
002a33dc  [INFO]:[BLPWR] LED PG LOW
002a33f8  [ERROR]:[BLPWR] PWR BRD DEINIT FAIL: %d
002a3460  [WARN]:[BLFW]] : BLSS DISABLED 
002a3554  [INFO]:BLCPWR:BLC READY : %d
002a3574  [ERROR]:BLCPWR:BLC NOT READY (FATAL) : %d
002a35a0  [ERROR]:BLCPWR:GET IO STATE TIMEOUT : %d
002a36b0  [ERROR]:[VLED PG] GET STATE FAIL : %d
002a36d8  [INFO]:[VLED PG] : VLED PG:%d T:%d
002a36fc  [ERROR]:[VLED PG] FAIL : TIMEOUT, BLSS SHUTDOWN
002a3934  [ERROR]:[BLAPI] ADC REG WRITE FAIL %d
002a395c  [ERROR]:[BLAPI] ADC REG READ FAIL %d
002a3984  [INFO]:[BLAPI] INVALID CMD (ADC RW) :%d
002a3a0b  #'+-26:>EIN
002a3ac0  [ERROR]:[BLAPI] AH DBG LOG : INVALID OPTION :%d
002a3af4  [INFO]:[BLAPI] UNKNOWN AH DEBUG CMD (BLU AH) :%d
002a3b84  [INFO]:[BLAPI] INVALID CMD (BIST ENABLE) :%d
002a3c10  [ERROR]:[BLAPI] BLU CAL INIT FAIL %d
002a3c38  [WARN]:[BLAPI] BLU CAL READ NOT SUPPORTED %d
002a3d38  [ERROR]:[BLAPI] BLU REG WRITE FAIL %d
002a3d60  [ERROR]:[BLAPI] BLU WR INVALID WR BUF
002a3d88  [ERROR]:[BLAPI] BLU REG READ FAIL %d
002a3deb  ?EKQW]ciou{{{~
002a3f64  [ERROR]:[BL SLPR] BLSLOPER NOT SUPPORTED in X2232
002a4074  [ERROR]:[BLAPI] DAC REG WRITE FAIL %d
002a409c  [ERROR]:[BLAPI] DAC REG READ FAIL %d
002a40c4  [INFO]:[BLAPI] INVALID CMD (DAC RW) :%d
002a4100  [INFO]:[BLAPI] RCVD UNSUPPORTED API %d
002a416c  [INFO]:[BLAPI] INVALID CMD (BLFW_API_GetConvOut) :%d
002a41a4  [ERROR]:[BLAPI] BLFW_API_GetConvOut INVALID BUF SIZE %d
002a4310  [INFO]:[BLAPI] INVALID CMD (AGING STATS) : %d
002a4340  [ERROR]:[BLAPI] LED AGING STATS INVALID BUF SIZE
002a4498  [BLFWAPI] SUCCESS %d, Size : %d
002a4604  [ERROR]:[API] BL BIST PTRN %d NOT SUPPORTED
002a4634  [INFO]:[BLAPI] INVALID CMD (SET BIST PATTRN ) :%d
002a46a8  [INFO]:[BLAPI] INVALID CMD (THRML STAT) :%d
002a46d8  [ERROR]:[BLAPI] THERMAL STATS INVALID BUF SIZE %d
002a4824  [ERROR]:[API] LUM IN BUF NULL
002a4844  [INFO]:[BLAPI] INVALID CMD (UPDATE LUM IN ) :%d
002a4878  [ERROR]:[API] LUM IN INVALID ZONES :%d
002a499c  [WARN]:[BLAPI] ZONE BRGT UNUSE ZONEID %d
002a49c8  [INFO]:[BLAPI] INVALID CMD (ZONE BRIGHTNESS) :%d
002a4b20  [ERROR]:UNIQUE ID IS READ ONLY CMD
002a4ccc  [INFO]:[BLU] UNIQ ID : 
002a4ce4  [INFO]:[BLU] UNIQ ID RD FAIL %d
002a4d08  [ERROR]:[BLU] EXIT USR TST MODE NOT ALLOWED , BL_EN : %d
002a4dec  [ERROR]:[DCS] COMM CHECK FAIL : %d
002a4ef2  @0(DNA
002a5028  DMA BUSY
002a5034  INVALID SIZE
002a5234  [ERROR]:BLSS_GetConvOut Loc Mismatch, xLoc: %d:%d, yLoc: %d:%d
002a5274  BLSS_GetConvOut: %llu, %d, %d
002a5304  [ERROR]:DRBL INIT FAIL
002a531c  [ERROR]:DRBL CFG FAIL
002a5334  [ERROR]:IPC INIT LOW QUEUE FAIL
002a5498  [ERROR]:[IPC] UNKNOWN IPC %d
002a54b8  [INFO]:[IPC] LUT ID: 0x%X, size : %d
002a54e0  [ERROR]:[HIPC] NOT SUPPORT: %X
002a5740  [ERROR]:[IPC] OPCODE %d NOT SUPPORTED:%d
002a576c  [INFO]:[IPC] LUT ID: 0x%X
002a5788  [ERROR]:[IPC] BLS LUT LOAD 0x%x FAILED:%d
002a5c38  [WARN]:[INIT] NO LPA : SKIP SML/LRG BRH
002a5c60  [WARN]:[INIT] NO LPA : SKIP BLU
002a5c80  [WARN]:[INIT] NO LPA : SKIP BLU CFG
002a5d8c  [ERROR]:[INIT] IOCFG INIT FAIL :: %d
002a5db4  [INFO]:[INIT] BL GPIO IOCFG INIT DONE
002a5ddc  [ERROR]:MAIN:BL I2C IOCFG INIT FAIL :: %d
002a5fac  [WARN]:[INIT] NO LPA CONNECTED, BL DISABLE
002a5fd8  [INFO]:TRINITY CONNECTED
002a5ff4  [INFO]:TRINITY DISCONNECTED
002a6010  [INFO]:LUMIN BUF : 0x%X
002a60ec  [ERROR]:[INIT]:UART INIT FAIL :: %d
002a6114  [INFO]:[INIT]: UART INIT DONE
002a6134  [ERROR]:BL GTIMER INST FAIL :: %d
002a6158  [INFO]:BL GTIMER INST DONE 
002a6234  [ERROR]:MSGQ 0 MSG SIZE
002a624c  [ERROR]:MSGQ NULL MSGS
002a6264  [ERROR]:MSGQ NULL
002a6398  MAPPER FAILED
002a63a8  [ERROR]:BLFW INIT FAILED
002a63c4  [INFO]:[BLFW] INIT DONE
002a63e0  [ERROR]:[INIT] BLK ID FAIL : %d 
002a6404  [INFO]:[INIT] BLK ID DONE : %d 
002a662c  Size :%x
002a6635   Source Address : %x
002a664a  , destination Address: %x
002a67ac  [WARN]:I2C INIT: RE INIT %d
002a67cc  [ERROR]:I2C INIT: INV SPEED %d
002a67ec  [ERROR]:I2C INIT: INV INTF %d
002a69f0  [ERROR]:[I2C] SEM NOT AVAIL(RD)
002a6bc0  [ERROR]:I2C WRITE: INV SIZE %d
002a6be0  [ERROR]:I2C WRITE: INV INTF %d
002a6c58  [ERROR]:I2C : ADC READ FAIL: %d
002a6d28  [ERROR]:I2C : DAC READ REG FAIL: %d
002a6e14  [ERROR]:Failed to powetdown DAC : %d
002a7088  DAC BUSY :%x
002a7098  [ERROR]:DAC : INIT I2C WRT FAIL : %d
002a70c0  [ERROR]:I2C : ADC INIT WRT FAIL: %d
002a70e8  [ERROR]:MAIN: BL PWR BRD INIT FAIL :: %d
002a71b0  [ERROR]:I2C : SLG READ REG FAIL: %d
002a71fa  *aAhjiG
002a7490  [API] THRML STAT FAIL 
002a74e4  [INFO]:[KNEEPOINT] 1 ENTRY INIT
002a78e0  Overriding LAS values
002a78f8  LAS_LAC_IDs: %d, %d, ProcTime(min,max): %d, %d, CRC32: 0x%x
002a7965   pGLAS Override Copy Done 
002a7adc  [INFO]:[AGING]: Valid: %d, CRC32: 0x%x
002a7c8c  [ERROR]:[LEDAGING] : T LUT HEADER %X
002a7cb4  [ERROR]:[LEDAGING] :  C LUT HEADER %X
002a7cdc  [ERROR]:LEDAGING: STATS DIS 
002a7d98  [ERROR]:[PRFGAIN] LUT LOAD FAIL : %d
002a7ed4  [ERROR]:[PWMGAIN]: CUR ALRDY ENABLED
002a8034  [INFO]:[GAIN] : LOADING LUT
002a8050  [ERROR]:[GAIN] : PENDING LUT LOAD
002a8074  [ERROR]:[GAIN] : DMA INIT FAILED
002a8208  [ERROR]:[PWMOFFSET] :: CAL LUT HEADER FAIL
002a8234  [ERROR]:[PWMOFFSET] LUT LOAD FAIL : %d
002a8424  [ERROR]:PWRLMT: LOAD LUT FAIL : %d
002a84f0  [ERROR]:[ROWSTGR] : LOAD LUT FAIL :%d
002a8700  [ERROR]:SLPR: FAIL TEMP LUT %d
002a8720  [ERROR]:SLPR: FAIL RATIOS LUT %d
002a8787  pbFtF4
002a87b4  [ERROR]:[SLPR VT] INVALID PARAM IN MAPPING
002a87e0  [ERROR]:[SLPR VT] REMAP NOT AVAIL
002a8868  [ERROR]:[SLPR] TEMP INVALD PARAM
002a8a30  [INFO]:[THERMAL_STATS] :: DIS
002a8bb4  [ERROR]:[X-TALK] : ELEC MAP HEADER %X
002a8bdc  [ERROR]:[X-TALK] ELEC MAP LUT LOAD FAIL : %d
002a8c69  bK HbB
002a8db2  )F"FcF
002a8dcc  [ERROR]:BLU CfgVal RegRead (%d, %d) FAIL: %d
002a954c  [ERROR]:PWRBRD : DAC UPDATE FAIL %d
002a9570  [ERROR]:PWRBRD : DAC TRIGGER FAIL %d
002a9824  BLU Cfg Validation Fail: 0x%x
002a9844  BLU Cfg Validation Success: %llu ns
002a9b58  [ERROR]:[DCS]%d : POLL OVFLOW : %d
002a9b7c  [ERROR]:[DCS]%d : POLL SPILL : %d
002a9ba0  [ERROR]:[DCS]%d : POLL TOUT : %d
002a9d98  SHARE:%p
002a9da4  [INFO]:BLU CFG SZ(DRAM) : %d
002a9dc4  [ERROR]:BLU INIT FAIL : CFG %d : %d
002a9dec  [INFO]:[BLU] DRV STRNGTH VER PASS
002a9fb8  [ERROR]:BLU INIT FAIL : IDENTIFY PACKET
002a9fe0  [ERROR]:[BLU] :: INIT DRV STRNTH FAIL : %d
002aa0b4  #*1;EOY
002aa180  [INFO]:DCS : INIT  %d :  %d 
002aa1a0  [WARN]:DCS : INIT POLLIN INVALD INTF: %d
002aa1cc  [ERROR]:DCS : INIT FAIL %d
002aa404  [ERROR]:Failed to IO Config DCS interface:%d
002aa5d0  [ERROR]:Invalid DCS interface (%d) received TH Timer init
002aa724  [ERROR]:[DCS] : LARGE BRANCH READ FAIL: %d, %d
002aa754  Large Branch LUT Validation Success: %llu ns
002aa84c  [INFO]:BLU CAL CFG SZ(DRAM) : %d
002aa870  [ERROR]:BLU CAL INIT FAIL : CFG %d : %d
002aa89c  [ERROR]:[DSC] CAL INVALID PARAM %d
002aa9f4  [ERROR]:[LRG BRNCH] :: CAL LUT HEADER FAIL
002aaa20  [ERROR]:[LRG BRNCH]: REG WRITE FAIL INTF %d, BLU %d
002aaa58  [INFO]:[BLU] LRG BRNC DONE
002aaba8  [ERROR]:[SMLBRNCH] :: CAL LUT HEADER FAIL
002aabd4  [ERROR]:[SML BRNCH]: REG WRITE FAIL INTF %d, BLU %d
002aac0c  [INFO]:[BLU] SMALL BRNC DONE
002aae84  [ERROR]:%d, %d
002aae94  [ERROR]:READ CAL: Failed to read data, %d
002aaec0  [ERROR]:[DCS] CAL RD SUP 4 byte only, %d
002aaeec  [ERROR]:READ CAL: Null Pointer
002ab034  [ERROR]:READ REG: Failed to read data, %d
002ab060  [ERROR]:[DCS] REG RD SUP %d byte only, %d
002ab08c  [ERROR]:READ REG: Invalid input param
002ab1f8  [ERROR]:[DCS] SEND DONE FAIL: %d 
002ab21c  [ERROR]:[DCS] SEND BYTE FAIL : %d
002ab2ec  [ERROR]:Failed to send INQuiry packet, %d
002ab318  [ERROR]:INQ: CRC not matching  (exp) %02X != %02X (rec)
002ab654  [ERROR]:[DCS] SR START CLR FAIL %d = 0x%X
002ab680  [ERROR]:[DCS] SR START DONE FAIL %d
002ab6a8  [WARN]:[DCS] ::RFIFO UFLOW : INTF %d
002ab804  [ERROR]:[DCS] : SML BRANCH READ FAIL: %d, %d
002ab834  [ERROR]:[DCS] : SML BRANCH VER FAIL: %d, %d
002ab994  [ERROR]:Invalid DCS interface (%d) received WR packet
002ab9cc  [ERROR]:REG WRITE: Invalid BLU ID:%d
002ab9f4  [ERROR]:REG WRITE: Null Pointer data
002ac12b  eAm4"b
002ac177  #5GYk}
002ac308  [ERROR]:DCS IO cfg should never reach here:%d
002ac338  [ERROR]:INVALID DCS Interface to configure IO, %d
002ac418  [ERROR]:IOCFG: I2C : %d
002ac490  LED Aging Disabled or Shutdown Received
002ac500  aRef: %f, beta: %f, ipcThr: %llu, compThr: %llu, mask: 0x%x
002ac7a0  [ERROR]:[THRML STAT] BUF OVFLOW
002ac884  [ERROR]:[ZMAP] : LUT HEADER FAIL%X
002ac8a8  [ERROR]:[ZMAP] LUT LOAD FAIL : %d
002acd10  [ERROR]:%s: DMA_TO_MEM0_DC_ERROR FAIL
002acd38  [ERROR]:%s: DMA_FRM_MEM0_DC_ERROR FAIL
002acdb8  [INFO]:[DMA]PWM GAIN LUT LOADED
002acdd8  [ERROR]:%s: DMA_TO_MEM1_DC_ERROR FAIL
002ace00  [ERROR]:%s: DMA_FRM_MEM1_DC_ERROR FAIL
002acec8  CH1 CONFIG FAIL
002ad56e  0a[FATAL][IPC] : INVLD MCU ID : %d
002ad870  [ERROR]:[MAIN] PRE INIT FAIL:%d
002ad894  [INFO]:[MAIN] PRE INIT COMPLETE
002ad8b8  [ERROR]:INIT TASK FAIL
002ad8d0  [ERROR]:[MAIN] :: BLSS FAILED
002ad97b  `pGH`pG
002ade5f  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
002af408  pG0123456789ABCDEF@0X
002af41e  0123456789abcdef@0x
002af6de  @D:STDERR
002af6e8  :STDIN
002af6ef  :STDOUT
002af7ac  [INFO]:Boot Time Policy RegVal: 0x%x 
002af7d3  [MAIN] : FW %d.%d.%d.%d[%d]
002af7f0  [INFO]:HEALTH SIZE : 0x%x, %llu
002af811  [INFO]:BL BOOT Time : %llu
002af82d  [INFO]:INIT TASK COMPLETED
002af848  [WARN]:BLSS LUMIN BUF : 0x%X
002af866  [ERROR]:MAIN: PWR BRD DAC IOCFG FAIL :: %d
002af892  [ERROR]:[INIT]: DMA INIT FAIL :: %d
002af8b7  [ERROR]:MAIN: PWR BRD DAC I2C INIT FAIL :: %d
002af8e6  [ERROR]:MAIN: PWR BRD ADC I2C INIT FAIL :: %d
002af915  [ERROR]:[INIT]: IPC INIT FAIL :: %d
002af93a  [ERROR]:MAIN: BL BLIF INIT FAIL :: %d
002af961  [ERROR]:[INIT]: MMU INIT FAIL :: %d
002af986  [ERROR]:[INIT] LUM BUF NOT READ : %u
002af9ac  [ERROR]:MAIN:BL STATIC LUTS NOT AVAIL ::
002af9d5  [ERROR]:[INIT] BL PWR BRD FAILED
002af9f6  [INFO]:[INIT]: DMA INIT DONE
002afa13  [INFO]:[INIT]: IPC INIT DONE
002afa30  [INFO]:MAIN: BL BLIF INIT DONE
002afa4f  [INFO]:[INIT]: MMU INIT DONE
002afa6c  [INIT] CAL LUT PUSH Q FAIL
002afa87  [ERROR]:[INIT] BL PWR BRD INIT FAIL
002afaab  [INIT] CAL LUT PUSHED TO Q
002afac6  [ERROR]:I2C : DAC WRT FAIL: %d
002afae6  [ERROR]:I2C : ADC WRT FAIL: %d
002afb06  DAC STATUS :%x
002afb16  [ERROR]:MAIN:BL CDPWR_EN  FAIL == 0 
002afb3b  [INFO]:MAIN: BL PWR BRD INIT DONE
002afb5d  [ERROR]:[PWMGAIN] :: CAL LUT HEADER FAIL
002afb86  [ERROR]:[PWMGAIN] :: CAL LUT NOT AVAIL : MMU FAIL
002afbb8  [ERROR]:[AH] : COEFF LUT HEADER FAIL%X
002afbe0  [ERROR]:[AH] : Z2G LUT HEADER FAIL%X
002afc06  [ERROR]:[AH] COEF LUT LOAD FAIL : %d
002afc2c  [ERROR]:[AH] Z2G LUT LOAD FAIL : %d
002afc51  [ERROR]:[LUMPROFILE] : LUT HEADER %X
002afc77  [ERROR]:[SLPR] : TEMP LUT HEADER %X
002afc9c  [ERROR]:[SLOPER] TEMP LUT LOAD FAIL : %d
002afcc6  [ERROR]:[SLOPER] LUT LOAD FAIL : %d
002afceb  [ERROR]:[ROWSTGR] :  LUT HEADER FAIL %X
002afd14  [ERROR]:[ROWSTGR] LUT LOAD FAIL : %d
002afd3a  [ERROR]:[PLIMIT] LUT LOAD FAIL ID:%p
002afd60  [ERROR]:[PWRLMTR] : PR LIMIT LUT HEADER %d  %X
002afd8f  [INFO]:[IPC] BLS LUT 0x%x LOAD DONE
002afdb4  [ERROR]:IPC LMSG HDLR FAIL : %d
002afdd5  [ERROR]:[IPC] RD OPCODE %d FAILED:%d
002afdfb  [ERROR]:[IPC] WR OPCODE %d FAILED:%d
002afe21  [ERROR]:[IPC] BLS 2DT %d FAILED:%d
002afe45  [INFO]:IPC LMSG HDLR DONE : %u
002afe65  [ERROR]:[MCU STATUS] FAIL TO GET ADDR 
002afe8c  [ERROR]:[IPC] UNSUPRTD LUT ID : 0x%X
002afeb1   or ADDR : 0x%X
002afec1  dma_ch0_cb
002afecc  dma_ch1_cb
002afed7  [ERROR]:WDOG :: FAIL EARLY
002afef2  [ERROR]:[API] INVLD CMD : %X
002aff10  [ERROR]:[BLFWAPI] FAIL %d, RET : %d
002aff35  [ERROR]:[BLAPI] ZONE BRGT INVALID ZONE ID %d
002aff63  [ERROR]:[BLAPI] LUM IN INVALID BUF ID %d
002aff8d  [ERROR]:[BLAPI] ZONE BRGT INVALID BUF ID %d
002affba  [ERROR]:[BLAPI] DAC REG WRITE/READ INVALID BUF SIZE %d
002afff2  [ERROR]:[BLAPI] ADC REG WRITE/READ INVALID BUF SIZE %d
002b002a  [ERROR]:[BLAPI] BLU REG WRITE/READ INVALID BUF SIZE %d
002b0062  [ERROR]:[BLAPI] BIST ENABLE INVALID BUF SIZE %d
002b0093  [ERROR]:[BLAPI] LUM IN INVALID BUF SIZE %d
002b00bf  [ERROR]:[BLAPI] ZONE BRGTNESS INVALID BUF SIZE %d
002b00f2  [ERROR]:[BLAPI] AH DBG INVL DCS INTF %d
002b011b  [INFO]:[BLAPI] INVALID CMD (BLU AH) :%d
002b0144  [INFO]:[BLAPI] INVALID CMD (BLU RW) :%d
002b016d  [ERROR]:[BLFW API] INVALID BLOCK ID :%d
002b0196  [WARN]:READ REG: CRC not matching  (exp) %02X != %02X (rec)
002b01d3  [ERROR]:INQ: Invalid DCS interface (%d)
002b01fc  [ERROR]:[DCS] : LARGE BRANCH VER FAIL: %d, %d
002b022b  [ERROR]:REG WRITE: Invalid data size(%d) : %d
002b025a  [ERROR]:[BLU] RD UNIQ ID FAIL , INVALID DCS ID : %d
002b028f  [ERROR]:[BLU] RD UNIQUE FAIL , INVALID BLU ID : %d
002b02c3  [ERROR]:Invalid InterfaceID : %d
002b02e5  [ERROR]:[BLU] USR TST MODE NOT ALLOWED , BL_EN : %d
002b031a  [ERROR]:[BLU] RD UNIQUE NOT ALLOWED , BL_EN : %d
002b034c  [ERROR]:[DCS]%d : POLL CRC ERR : %d
002b0371  [INFO]:DCS : IDENTIFY :: %d
002b038e  [ERROR]:[ERROR] IGNORING DCSIF ID: %d
002b03b5  [WARN]:INVLD: DCS interface Poll Config: %d
002b03e2  [ERROR]:Failed to send identify Packet to interface:%d : Error: %d
002b0426  [ERROR]:Invalid dcs interface received Send Bytes: %d
002b045d  [WARN]:[DCS] ::RFIFO OVFL : INTF %d
002b0482  [WARN]:[DCS] :: CRC ERROR : INTF %d
002b04a7  [WARN]:[DCS] :: RD TIMEOUT : INTF %d
002b04cd  [ERROR]:REG WRITE: Failed to send packet , error:%d
002b0502  [ERROR]:Invalid DCS interface (%d) received
002b052f  Small Branch LUT Validation Success: %llu ns
002b055d  [ERROR]:[BLU] DRV STRNGTH FAIL :%d =  %x
002b0587  [ERROR]:[DCS]%d : BLU FAULT : 0x%x
002b05ab  [ERROR]:IPC_OPCODE_BLU_FAULT_INFO Triggered: %d ms, dcs_mask: 0x%x
002b05ef  [ERROR]:BLU CfgVal FAIL (%d, %d):  addr: 0x%x, actual: 0x%x, exp: 0x%x
002b063d  [ERROR]:Invalid input param(DCS: Send Receive Bytes)
002b0672  [ERROR]:[BLU] Reading UID FAIL
002b0691  [DCS]LRG BRCH CAL NOT AVAIL
002b06ad  [DCS]SML BRCH CAL NOT AVAIL
002b06c9  [ERROR]:READ CAL: Invalid input param
002b06ef  [ERROR]:READ REG: Null Pointer
002b070e  [ERROR]:I2C Read: INV SIZE %d
002b072d  [ERROR]:I2C Read: INV INTF %d
002b074c  [ERROR]:I2C READ: INVALID INTF , STATUS : %d 
002b077a  [ERROR]:[I2C] SEM NOT AVAIL(WR)
002b079a  [INFO]:FB: %X
002b1278  8?61$#*-pw~ylkbeHOFATSZ]
002b12e0  WPY^KLEBohafst}z
002b1310  ing`ur{|QV_XMJCD
002b1328  !&/(=:34NI@GRU\[vqx
002b133c  jmdc>907"%,+
002b1526  JDHqIDDqID@rID|
002b1536  JDPqIDLqIDDrID
002b154e  JD`qIDPrID
002d3793  fJF)F F&`NF
002d382c  *** assertion failed: 
002d3844  , file 
002d384c  , line 
002d441c  %HxDT8
002d4434  !HxDT8
002d4514  ahi`!h
002d46d0  SIGABRT: Abnormal termination
002d47d3   pGpGpGpG8
002d49f7  `+F2FIF8F
002d4aec  SIGRTRED: Redirect: can't open: 
002d4c20  SIGRTMEM: Out of heap memory
002d4c40  : Heap memory corrupted
002d5089  Hard Fault!: MCU
002d5f90  CC dma_transfer(%d) FAIL: %d
002d64c6  -AHhIi
002d65c6  -AHhIi
002d6724  WDOG Bite Error
002d67dc  System Exited: %d
002d807b  y'z!yfzby
002d82b7  y&z!yby
002d867c  Src: %d Dst: %d Opcode: 0x%02x, Prio: %d, Size: %d
002d86b0  SET_LIMIT 0x%06X 0x%X
002d86c8  Mismatched cookie from Cabal (0x%08X, local 0x%08X)
002d86fc  RR was zero
002d909e  PJHhPp
002d9ac5  D 0)FXEO
002db542  Wa_FcE
002db57a  Wb_FcE
002db5b2  Wc_FcE
002db760  dma_transfer(ROW CH1) FAIL: %d
002db780  dma_transfer(ALD CH0) FAIL: %d
002db882  -B|hSh
002db944   2L`JbM
002dbe00  NP Entry: %d Exit: %d
002dbe18  ERR : %s
002dbe24  IPC_NP_MSG_Q
002dc49a  xaxiQF 
002dc9b0  parse_ipc_opcode_mdata_msg FAIL: %d
002ddb2b  V~`nho
002ddd10  Unknown HP IPC from 0x%x
002de55b  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
002de971   pGa!O
002def14  0123456789ABCDEF@0X
002def28  0123456789abcdef@0x
002def4d  0123456789abcdefxp
002def60  0123456789ABCDEFXP
002df17d  [FATAL]: 
002df188  [INFO]: 
002df1b4  t2d_fwk_init FAIL: %d
002df1ca  bsp_init FAIL: %d
002df1dc  T2D BOOT DONE: Free Heap: %d, Free Stack: %d, Time (ns): %llu
002df21a  T2D-MCU Firmware, Version (Major, Minor, Release): %d.%d.%d, v0x%08x
002df25f  mcu_step_trace %d
002df271  IPC(%d, %d), IPC_API_RD_RESP
002df28f  IPC(%d, %d), IPC_GEN_RESP
002df2ab  [ERR]: 
002df2b3  Mismatched cookie from FCFW (0x%08X, local 0x%08X)
002df2e6  WRN: Unrecognized Block ID (0x%x)
002df308  WRN: Version mismatch for BID (0x%x)
002df32d  Warning: mean_p_photo_target is not zero but AA_target is zero, would divide by zero.
002df383  ../../../algos/trinity2d_utils.c
002df3a4  WRN: Destination for BID (0x%x) too small
002df3ce  !(numerator ^ denominator) || denominator
002df3f8  GET_LIMIT 0x%06X 0x%X %u
002df411  IPC_API_WR_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, BLOCK_ID(OP1): 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
002df479  IPC_API_RD_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, OP1: 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
002df4d7  IPC_API_WR_CMD: Cust Info: ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
002df513  IPC_OPCODE_API_RD_RESP: Status: 0x%x
002df538  IPC_OPCODE_GEN_RESP: Status: 0x%x
002df55a  IPC(%d -> %d): 0x%02x, size: 0x%04x
002df5d9  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
00335787  fJF)F F&`NF
00336698  %HxDT8
003366b0  !HxDT8
003367da  ahi`!h
00336a1b   pGpGpGpG8
00336c3f  `+F2FIF8F
00336d34  SIGRTRED: Redirect: can't open: 
00336e04  SIGRTMEM: Out of heap memory
00336e24  : Heap memory corrupted
00337081  [ERR]: 
0033708d  Hard Fault!: MCU
00337939  [ERR]: 
00337944  WDOG Bite Error
00337975  [ERR]: 
00337980  System Exited: %d
00337d9c  Failed to initialize UART driver: 0x%x
00337dc4  Failed to initialize WDOG driver: 0x%x
00337dec  Failed to initialize DMA driver: 0x%x
00338381  [FATAL]: 
00338bbc  waiting for first vblank end...
00338bdc  work loop start
00338bec  queue_pop FAIL, %d
00338cb0  stat processing queue init failed
00338cd4  ipc queue init failed
00338d58  new CE str: 0x%X
00338e93  PBibPA
00338f38  (F)FJF5`
00339199  y1Fbi+F
003392bc  cabal ipc handler opcode %x
003392d8  failed to setup debug api read response with error 0x%X
00339310  ipc data in dram!
00339324  unhandled ipc opcode: 0x%x
00339604  SYS TRACE FAILURE: %X.%u : size (%u) buff(%p) - TCON_ERR(%u)
00339644  system trace packet buffer is null
00339689  [INFO]: 
00339694  sys trace status set to: %u
003396ec  ?hEaEbEcEdEeEf
003397cd  P?hhahbhchdhehf
00339c28  get ltm data entries %u from %p
00339c48  get ltm output config cells(%u) bins(%u)
00339c74  unknown read api: 0x%x
00339e30  set ltm output row to %u
00339e4c  clear event trace buffer
00339e68  event trace enabled: %u
00339e80  unknown write api: 0x%x
00339fdc  <DAF F:F
0033a06d  FXFQFJFDD
0033a530  %s: DMA_TO_MEM0_DC_ERROR FAIL
0033a550  %s: DMA_FRM_MEM0_DC_ERROR FAIL
0033b550  Failed to initialize Frame Timing driver: 0x%x
0033b580  Failed to initialize HW STATS driver: 0x%x
0033b5ac  Failed to initialize 1 way dma driver: 0x%x
0033bd44  unexpected high priority IPC irq
0033bddc  unexpected low priority IPC irq
0033c0ac  AFRFKF
0033cb89  [ERR]: 
0033cb94  ERROR 0x%X @ %s
0033cba5  [INFO]: 
0033cbb0  no errors @ %s
0033cd21  [ERR]: 
0033cd2c  queue_pop FAIL, %d
0033cded  [INFO]: 
0033cdf8  SCENE INFO: cut %u fade in %u fade out %u
0033cf7d  [ERR]: 
0033cf88  ipc (%x) priority mismatch: %x v %x
0033cfad  [INFO]: 
0033cfb8  submit normal priority IPC %x
0033de31  [ERR]: 
0033de3c  set ipc ltm row index (%u) larger than max row index (%u)
0033e464  zr1`)hPCp`
0033e8bb  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
0033f103  "SFXF!F
0033f194  "J!KPF
0033f1a5  J K0FAF
0033f234  5"0FaF
0033f511  F2FCF)F
0033f548  QJRK8FQF
0033f5fd  F*F3F8FQF
0033f744  BFSF(F1F
0033f7a6  *FXF!F
0033f7f3  "[F8FAF
0033f81b  "[F8FAF
00340672  pG0123456789ABCDEF@0X
00340688  0123456789abcdef@0x
0034070f  ?>UUUUU
00340748  0123456789abcdefxp
0034075b  0123456789ABCDEFXP
003419e4  boot error %d occurred at %dd
00341a04  [MSG]: 
00341a0d  [FATAL]: 
00341a17  RELEASE
00341a1f  ENGINEERING
00341a2b  fw initialize complete: Free Heap: %d, Free Stack: %d
00341a61  Cabal Firmware, Version: %d.%d.%d
00341a83  hw initialize complete
00341a9a  cabal %s build %d @ %s %s
00341ab5  [ERR]: 
00341abd  Failed to create Global Timer: TIMER_INST_0
00341ae9  Failed to create Local Timer: TIMER_INST_1
00341b14  Failed to initialize NMI: 0x%x
00341b33  Failed to initialize Doorbell driver: 0x%x
00341b5e  Failed to initialize HW Accelerator's driver: 0x%x
00341b91  CC: ltm_cc_theta_lut_size_in_words (%d) > CCLTHETALUT_CCL_THETA_LUT size (%d)
00341bdf  dma_ch0_cb
00341bea  ERROR! Division by 0!
00341c01  [INFO]: 
00341c0a  heartbeat (%.2fs)
00341c1c  HWA ltm cells per row and bins per cell is no longer what we expected
00341c62  hw stats config does not match post mcu hw block config - amb rows per frame: %u v. %u
00341cb9  algo config does not match hw stats config - amb rows per frame: %u v. %u
00341d03  algo config does not match hw stats config - sch rows per frame: %u v. %u
00341d4d  hw stats config does not match post mcu hw block config - cas rows per frame: %u v. %u
00341da4  hw stats config does not match post mcu hw block config - amb cells per row: %u v. %u
00341dfa  algo config does not match hw stats config - amb cells per row: %u v. %u
00341e43  algo config does not match hw stats config - sch cells per row: %u v. %u
00341e8c  hw stats config does not match post mcu hw block config - cas cells per row: %u v. %u
00341ee2  static cfg IPC data size (%u) does not match excpted size (%u)
00341f21  DUMPING SCH FRAME
00341f33  DUMPING AMB %i
00341f42  DUMPING SCH %i
00341f51  DUMPING CAS %i
00341f60  IPC static cfg read handler rsp size %i
00341f88  dumping amb global stats
00341fa1  amb global stat handler start
00342019  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
003435c4  Sep 24 2025
003977cf  fJF)F F&`NF
00398414  %HxDT8
0039842c  !HxDT8
003985de  ahi`!h
00398bac  pGpGpGpG8
00398df7  `+F2FIF8F
00398eec  SIGRTRED: Redirect: can't open: 
00398fbc  SIGRTMEM: Out of heap memory
00398fdc  : Heap memory corrupted
0039903c  Invalid Operation
00399050  Divide By Zero
00399060  Overflow
0039906c  Underflow
00399078  Inexact Result
00399088  SIGFPE: Arithmetic exception: 
00399a48  PLS VBE2VBE Fault
00399a5c  PLS INIT2INIT Fault
00399a88  NMI IRQ
00399fe8  DSC_ENC_ERR (%d): %llu, 0x%x
0039a008  FB_BUS_ACCESS_ERR: %d
0039a020  FB_OVERFLOW: %d
0039a030  FB_UNDERFLOW_ERR: %d
0039a048  FB_NO_ADDR_NODE: %d
0039a05c  FB Address Not Found
0039a1b0  Input Pipe MUX State Change Event Rcvd: %llu
0039a1e0  Panel Pipe MUX State Change Event Rcvd: %llu
0039a334  PR NFQ Push Fail
0039a35c   `%kfk
0039a4ec  INP: PFE Rcvd (%d): %llu
0039a508  Panel Pipe Partial Frame Event Rcvd: %llu
0039a534  CT Pipe Partial Frame Event Rcvd: %llu
0039ae2c  BSC_PSF0_UNDER_FLOW_INT_FC_STATUS: %llu
0039ae54  BSC_PSF1_UNDER_FLOW_INT_FC_STATUS: %llu
0039ae7c  BSC_PSF2_UNDER_FLOW_INT_FC_STATUS: %llu
0039b9ac  PP: DG_LUT_UPDATE_ERR_INT_FC_STATUS: %llu
0039b9d8  PP: DG_LUT_LOAD_ERR_INT_FC_STATUS: %llu
0039ba00  PP: VRR_DET_RRR_TIMEOUT_INT_FC_STATUS: %llu
0039be34  PC VID CH0 CRC Fail
0039be48  PC VID CH0 Overlap
0039be5c  PC VID CH0 SFOQ Push Fail
0039be78  PC VID CH1 CRC Fail
0039be8c  PC VID CH1 Overlap
0039bea0  PC VID CH1 SFOQ Push Fail
0039bf18  WDOG Bite Error
0039bf44  System Exited: %d
0039c9c0  PC CFH CH%d, Error: 0x%x
0039cf40  CTP Desciptor Prep Fail: 0x%x
0039d280  PLA EG LUT GEN: Invalid Gamma
0039da94  Invalid DMA0 Trfr Parameters
0039db18  %s: DMA_TO_MEM0_DC_ERROR FAIL
0039db38  %s: DMA_FRM_MEM0_DC_ERROR FAIL
0039dbbc  %s: DMA_TO_MEM1_DC_ERROR FAIL
0039dbdc  %s: DMA_FRM_MEM1_DC_ERROR FAIL
0039e7c7  cJkMc"
0039e831  cAkEc!
0039eb59  `JhM`@
0039ec93  F(FIF@
0039fd9c  LP IPC Queue Push Failed: %d
003a0710  FS Algo No OP ID
003a0724  Scheduled PT violates minimum end time requirement
003a0758  Unspported Input Event, %d
003a094c  rc_timer_status: 0x%x
003a0964  duration_of_final_frame: %u
003a0980  cav_at_pwr_off[0]: %f
003a0998  cav_at_pwr_off[1]: %f
003a09b0  cav_at_pwr_off[2]: %f
003a09c8  cav_at_pwr_off[3]: %f
003a0bd4  `DpD@DHDH
003a0c28  Min Setup Time is Greater than Default: %d
003a1431  F(F1FJF;F
003a1524  is_dp_src_connected: %d
003a153c  DynCfg Switch InProgress
003a1558  IPC(1, 0), SDP_BASED_DYN_CFG_SWITCH_REQ, pri: 0, ch_id: %d
003a1688  PSF0 CRC Error
003a1698  PSF1 CRC Error
003a16a8  PSF2 CRC Error
003a179d  [FATAL]: 
003a1840  FCFW Version: 0x%x, Build Date: 0x%x
003a1868  FCFW Fatal Err Enable Mask: 0x%x
003a1b1c  %s: FS_OPMODE_2BUFFER
003a1b34  P_Pipe
003a1b3c  CT_Pipe
003a1e86  &D1DYD)D
003a1f38  PSF Actual (%d) Prefetch Time Exceeds the Budget (%d)!
003a1fc0  WARNING: Ignore un-supported IPC cmd, dropping
003a253a  8FIF2F
003a292f  FAF*F;F
003a2dfc  Unexpected: Only PRF or NF Expected
003a2e20  InCorrect PowerON Data
003a2e38  First Frame Can't be Panel Replay Frame, Dropping PR event
003a2ec8  Invalid SF Obj, Drop Repeat Req
003a2f28  NR DeadLine Timer CbQ Push Fail
003a2f84  PC CFG CH (%d) ABORT or ERR: 0x%x
003a2fa8  PC CFG DC Fail
003a3074  CFG Ch Done Event CB: Q push fail: %d
003a3170  fs_fwk_pc_vid_ch_cb: Invalid arguments
003a3220  SWBIST BufQ Push Fail
003a3db6  8@)FJF
003a4084  FS in Recursive Loop
003a4480  Expecting PP Pipe Overlap, Cookie: 0x%x: %llu, %llu
003a44b4  PP Overlap Schedule
003a44c8  Unexpected vid_ch_active_access_cntr: %d
003a473c  SWBIST NF Obj Alloc Fail
003a4758  SWBIST NFQ Push Fail
003a4d98  REG_FW13_DISABLE_CABAL: Disable Cabal
003a4dc0  REG_FW13_DISABLE_TRINITY: Disable Trinity
003a4dec  REG_FW13_DISABLE_DITHER: Disable Dither
003a546a   xax*F
003a5550  WPC LUT Ver (%d) & ChipID (0x%x) Don't Match, Disable WPC Block
003a5590  WPC LUT Ver (%d) & ChipID (0x%x) Match
003a55b8  IP2 Cfg FAIL: 0x%x
003a585f  &0FAFRFKF
003a5874  SW BIST State: Not in ACTIVE state (%d)
003a589c  SWBIST Start: Expected: %llu, Actual: %llu
003a58c8  Default Frame for last one
003a5e7d  aph"j`
003a5e85  ""bhhbj`
003a5fcb  apj"j`
003a5fd3  ""bhjbj`
003a70c4  %FpEtF8
003a74ff  FPFIF"F;F
003a7521  FXFAFJF#F
003a7564  PFYFJF;F
003a75b3  F8FAF"F3F
003a75c3  FHFQF"F3F
003a75d5  FYF:F+F
003a7dc4  No NF after Preemptive Repeat
003a7ee4  Error in preparing P_PIPE descriptor cfg: 0x%x
003a8164  IPC(%d, %d), OPCODE: 0x%x, Size: %d, CH_ID: %d, Pri: %d
003a819c  Generic Response not supported for T2D, C2D & BL MCUs
003a87d4  Fail to allocate cfg channel
003a8868  %s: PC CFG (%d): IN_PROGRESS
003a8888  pc_cfg_utils_wait_dc_immediate
003a88a8  PC Cfg (%d) Load FAIL
003a8c98  #ybyYC
003a9038  pc_submit_cfg_descriptor: Cfg Ch BUSY or Not Allocated
003a91c4  PC VID RD CH SFOQ Push Fail
003a9760  Enable Frame Buffer: %llu
003aa0f0  qb(zqj`
003aac49  F@FIF:FSF
003aad0f  F F)FKF
003aad37  FPFYFBFKF
003aad7d  F(F9FRF[F
003aadf6  8F1FRF[F
003ab089  FHFYF*F3F
003ab0ce  2FSF5F
003ab10c  8FAFJF[F
003ab25f  F8F!FZF+F
003ab279  F FAFKF
003ab326  RFKFWF
003abf03  `hiji"
003ac340  Queue POP FAIL, %d
003ac505  x'y!xbx
003ac700  IPC_OPCODE_API_RD_RESP: Status: 0x%x
003ac74f  x/y)xjx
003ad48c  IPC_API_WR_CMD: Cust Info: ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
003ad4c8  CD EDR Override: 0x%x
003ad4e0  FCFW_API_BID_SET_ST_LOG_EN_FILTER: %d
003ad548  IPC_OPCODE_SDP_BASED_DYN_CFG_SWITCH_FAIL
003ada08  LUT_ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
003ada94  rx_ipc_handler_mcu_up_evt: MCU_ID: %d, Version: 0x%x
003adacc  BLU Fault Rcvd: 0%x
003adb3a  AF2FSF
003adb88  IPC_OPCODE_TCON_TO_FC_POWER_ON
003adc20  IPC(1, 0), fs_fwk_send_power_off_info, pri: 1, ch_id: %d
003adc9c  IPC_OPCODE_START_LUMIN_BUF_UPDATE
003adce8  IPC_OPCODE_STOP_LUMIN_BUF_UPDATE
003adec8  IPC_VT_DATA: 0x%x, PRC: %d, PrimCal: %d
003ae12c  Invalid CFG CH IDX, Skipping Pipe Scheduling
003ae15c  Unexpected output frame duration, 0x%p
003ae184  Pipe Cfg Q is busy, cfg_ch_idx: %d, Q-depth: %d
003ae7ec  WARNING: counter has overflowed, more than 16,777,215 cycles
003aea3b  F@FIF"F+F
003aea82   F)FRF[F
003aeac3  F8FAFRF#F
003aebb7  F0F9F"FKF
003b1468  0123456789ABCDEF@0X
003b147c  0123456789abcdef@0x
003b14a1  0123456789abcdefxp
003b14b4  0123456789ABCDEFXP
003b1791  [INFO]: 
003b179b  [ERR]: 
003b17a3  FCFW: Entering WorkLoop: FS_OPMODE_PASS_THROUGH
003b17d3  FCFW: Entering WorkLoop: FS_OPMODE_2BUFFER
003b17fe  Static Cfg Loading Time (us): %d
003b181f  fs_fwk_static_cfg FAIL: %d
003b183a  bsp_init FAIL: %d
003b184c  FCFW Boot Fail
003b185b  FCFW BOOT DONE: Free Heap: %d, Free Stack: %d, Boot Time: %d hticks
003b189f  FCFW Boot Success: %llu
003b18b7  SysTick Cntr Overflow
003b18cd  FC FW: Waiting for Static Cfg Availability in DRAM!: 0x%llx
003b1909  FCFW: Invalid Header @ Static Cfg LUT: 0x%llx
003b1937  FC FW: Waiting for Power ON API from TCON FW0x%llx
003b196b  Hard Fault!: MCU
003b197c  Default_Handler_wrapper
003b1995  Stack Free: %d bytes
003b19ab  Heap Free: %d bytes
003b1a09  Faulting PC: 0x%08x
003b1a1e  BFAR: 0x%08x
003b1a2c  MMFAR: 0x%08x
003b1a47  AFSR: 0x%08x
003b1a55  CFSR: 0x%08x
003b1a63  HFSR: 0x%08x
003b1a71  PSR: 0x%08x
003b1a7d  psf0_delay %d, psf1_delay %d, psf2_delay: %d, psf2_delay_1: %d, 
003b1abe  Unsupported PID, %d 
003b1ad3  CA exceeds limits!
003b1ae6  WARNING: FCFW_API_BID_HM_FRAME_SCHD, Payload Size MisMatch (%d, %d)
003b1b2a  REG_FW13_DISABLE_PANEL_PIPE: Disable Panel Pipe Blocks (Except Dither)
003b1b71  CTP: Cookie mis-match (0x%x, 0x%x)
003b1b94  TCON_CMN_LUT_ID_DYN_CFG_UUID: InCorrect Size: Rcvd: %d, Atleast Needed: 4
003b1bde  PC VID CH2 NFO ALLOC FAIL
003b1bf8  DMA1 Error: %d, TRFR FAIL
003b1c12  DMA CH0: WPC 2DT LUM LOSS LUT Load FAIL
003b1c3a  ca/[%0.4f], pt/[%lld]
003b1c50  dma_ch0_cb
003b1c5b  dma_ch1_cb
003b1c66  FCFW_API_BID_PIPELINE_BLOCK_DISABLE: BID - 0x%x, is_disable - %d
003b1ca7  NF Ticks: 0x%llx, is_pr_frame: %d, host_fid: 0x%x, hw_fid: 0x%x, src: %d
003b1cf0  FCMCU_LUT_ID_PIPELINE_DYN_CFG: InCorrect Size: Rcvd: %d, Needed: %d
003b1d34  TCON_CMN_LUT_ID_FW_DYN_CFG: InCorrect Size: Rcvd: %d, Needed: %d
003b1d75  TCON_LUT_ID_CM_DEP_CALIB_INFO_POSTCAL: InCorrect Size: Rcvd: %d, Needed: %d
003b1dc1  CMD_CALIB_SWITCH: ltlrr: 0x%x, utlrr: 0x%x, lturr: 0x%x, uturr: 0x%x, idx: %d, size: %d
003b1e19  Dropping Natural Frame during DynCfg Switch: %d
003b1e49  IPC (%d -> %d): GEN_RSP: Status: 0x%x, CH_ID: %d, Pri: %d
003b1e83  P_PIPE Process: schd_obj Q push fail: %d
003b1eac  CT_PIPE Process: schd_obj Q push fail: %d
003b1ed6  cam_hle_adm: %d
003b1ee6  elapsed_time_since_last_pwr_off_s: %d
003b1f0c  fs_fwk_sw_bist_init: Q push fail: %d, limits the number of free sequences: %d
003b1f5a  fcfw_pipeline_algo_feature_disable_mask_t: %d
003b1f88  GBLS Output: 0, GBLS Input: %d
003b1fa7  FCFW_API_BID_FS_INP_PIPE_CTRL: is_disable: %d @ %d
003b1fda  %s (LM: %d, FT: %d, is_rgb: %d, P: %d, fH: %d, opID: %d): FW_COOKIE: 0x%x, Vid START: %llu ns, LTM Rd: %d, LED Rd: %d, EOTF: %d, RR: %3.2f, 0x%p, BL: %d,%d, CE: %d,%d
003b2081  SBSeq ID: %d, DataQ Push Failed
003b20a1  REG_FW13_DISABLE_FRAME_REPEAT: Disable Frame Repeat Mode
003b20da  fs_fwk_set_curr_op_mode
003b20f2  Invalid NF Obj Handle
003b2108  No Natural Frame to Schedule
003b2125  UnSupported FrameType
003b213b  WDOG Bite
003b2145  worst_case_residual_ca_level_at_last_power_off: %f
003b2178  SBSeq ID: %d, Q-OVERFLOW, Dropping
003b219b  Waiting for PC VID CH2 MUX Switch
003b21bd  SF Obj Alloc Fail
003b21cf  PC VID CH2 NFQ Push Fail
003b21e8  PC VID CH0 Done SFOQ Push Fail
003b2207  PC VID CH1 Done SFOQ Push Fail
003b2226  REG_FW13_P1BU_POLICY: Use 3:1 FB DSC Compression
003b2257  %s (LM: %d, FT: %d, is_rgb: %d, P: %d): FW_COOKIE: 0x%x, Vid START: %llu ns, LTM Wr: %d, LED Wr: %d, 0x%p
003b22c1  REG_FW13_DISABLE_GLOBAL_BL_SLOPER: Disable Global BL Sloper
003b22fd  Invalid DMA1 Trfr Parameters
003b231a  EOTF Change (%d, %d), GBLS Reset
003b233b  Drop New Repeat Frame Req as Old NRF is not consumed yet
003b2374  fs_fwk_natural_and_pr_frame_process_cb: Invalid CB Argument
003b23b0  BSC_ERR_RW_BUBBLE_FC_STATUS: %llu
003b23d2  BSC_PSF0_IN_UDF_FC_STATUS: %llu
003b23f2  BSC_PSF1_IN_UDF_FC_STATUS: %llu
003b2412  BSC_PSF2_IN_UDF_FC_STATUS: %llu
003b2432  BSC_PSF2_FIFO_UDF_FC_STATUS: %llu
003b2454  BSC_GLB_FIFO_UDF_FC_STATUS: %llu
003b2475  BSC_LED1_FIFO_OVF_FC_STATUS: %llu
003b2497  BSC_PSF2_FIFO_OVF_FC_STATUS: %llu
003b24b9  BSC_GLB_FIFO_OVF_FC_STATUS: %llu
003b24da  BSC_FW_TRIGGER_PSF0_MISS_FC_STATUS: %llu
003b2503  BSC_FW_TRIGGER_PSF1_MISS_FC_STATUS: %llu
003b252c  BSC_FW_TRIGGER_PSF2_MISS_FC_STATUS: %llu
003b2555  CTP: DG_LUT_LOAD_ERR_INT_FC_STATUS: %llu
003b257e  CTP: DG_LUT_UPDATE_ERR_INT_FC_STATUS: %llu
003b25a9  BSC_PSF0_WRS_BELOW_FC_STATUS: %llu
003b25cc  FC_VCOM_OVC_IRQ_STATUS: %llu
003b25e9  FC_OD_DE_BIG_IRQ_STATUS: %llu
003b2607  FC_OD_FRAME_BIG_IRQ_STATUS: %llu
003b2628  FC_OD_DE_SMALL_IRQ_STATUS: %llu
003b2648  FC_OD_FRAME_SMALL_IRQ_STATUS: %llu
003b266b  FC_OD_CRC_ERR_IRQ_STATUS: %llu
003b268a  FC_OD_WR_OF_ERR_IRQ_STATUS: %llu
003b26ab  FC_OD_RD_BUS_ERR_IRQ_STATUS: %llu
003b26cd  FC_OD_WR_BUS_ERR_IRQ_STATUS: %llu
003b26ef  FC_OVC_LINECOUNT_IRQ_STATUS: %llu
003b2711  CTP: VRR_DET_RRR_TIMEOUT_INT_STATUS: %llu
003b273b  Shorter Natural Frame! Dropping Next Frame: %d, CurrT: %llu, PrevT: %llu
003b2784  CT Pipe MUX State Change Event Rcvd: %llu
003b27ae  Un-supported BlockID: 0%x
003b27c8  FCFW_API_BID_SET_DG_SCALE_FAC: 0x%x, 0x%x
003b27f2  IPC_API_WR_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, BLOCK_ID(OP1): 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
003b285a  IPC_API_RD_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, OP1: 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
003b28b8  Using Static Cfg for LUT ID: 0x%x
003b28da  Using Independent Cal for LUT ID: 0x%x
003b2901  FCFW_API_BID_FS_CTRL_LATENCY_MODE: 0x%x
003b2929  CH0 CRC (%d):: ERR: 0x%x, 0x%x, Exp: 0x%x, 0x%x, SEC: 0x%x, COOKIE: 0x%x
003b2972  CH1 CRC (%d):: ERR: 0x%x, 0x%x, Exp: 0x%x, 0x%x, SEC: 0x%x, COOKIE: 0x%x
003b29bb  FCFW_API_BID_C2DFW_FEATURE_DISABLE: 0x%x
003b29e4  FCFW_API_BID_T2DFW_FEATURE_DISABLE: 0x%x
003b2a0d  ALS: 0x%x, BL LVL: 0x%x, WHITE LVL: 0x%x, CE: 0x%x, DIM: 0x%x, SLOPER: 0x%x, MASK: 0x%x
003b2a65  DMA CH0: PP DG MT0 Load FAIL: 0x%x
003b2a88  DMA CH0: CTP DG MT0 Load FAIL: 0x%x
003b2aac  DMA CH0: FW STATIC CFG Load FAIL: 0x%x
003b2ad3  DMA CH0: OVD LUT Load FAIL: 0x%x
003b2af4  IP2 CfgDone FAIL: 0x%x
003b2b0b  IP3 CfgDone FAIL: 0x%x
003b2b22  IP4 CfgDone FAIL: 0x%x
003b2b39  IP9 CfgDone FAIL: 0x%x
003b2b50  IP3 Cfg FAIL: 0x%x
003b2b63  IP4 Cfg FAIL: 0x%x
003b2b76  IP9 Cfg FAIL: 0x%x
003b2b89  dyn_cfg_switch_commit FAIL: 0x%x
003b2baa  FCFW_API_BID_FS_CTRL_PIPE_DISABLE: CTP: 0x%x, PP: 0x%x
003b2be1  BL Lvl: 0x%x, CE Fact: 0x%x, White Lvl: 0x%x, ALS Lux: 0x%x, Mask: 0x%x
003b2c29  %s, Error Status: 0x%x, GTicks: 0x%llx
003b2c89  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
003b4d95  #PD(GPD$GPDxGPD
003b4da5  #PD0GPD,GPD|GPD
003b4dbd  CPD8GPD
003b4dc9  sPDHGPD
003b4dd1  GPD4GPD
003b4df1  GPDhGPD
003b4dfd  GPDlGPD
003b4e0d  GPD@#PD
003b4e15  GPD`GPD
003f103c  K(&#hPG
003f151f  01w@xSC
003f1c16  upmS\E4
003f26bf  c.BPLI
003f4157  ScI#O6
003f491b  JM>CnR
003f4aa4  ixKy)]
003f4ada  !_(Bhi
003f4c30  @UlX1*r9P
003f54e6  Z$0Yzh
003f56c3  q$yJfE4
003f5c27  08/jSr
003f626d  J1)KLE<"H
003f639d  X\5aQb0G
003f6fbd  LBL@NBLBL@NBLF
003f75dc  HLRrDs
003f76e5  VRD$p$&#
003f79a0  jhSa]'
003f7a41  H6RSe!6X
003f890b  pveQO6
003f8a12  192nBx
003f8ac5  Ikp1L9
003f99e5  ^"NFu,)
003f9b58  LhX9&-.%
003fa4df  |-&=bYQD
003fa736  %DhDSM
003fa99e  bYDSM*
003faf12  '#D1 BLBL@N
003fb032  d3h\FYl
003fb0f3  2zYDlR}&R
003fb485  ,:JLNryb
003fb672  i)eDNC
003fb77d  ZLJZX3
003fbd0c  LBLBLaF
003fbd21  LBLBhd$
003fcaea  pL@N@NBLBL
003fcd86  l6)`hLR#B
003fd9bf  SDp,0p84
003fe6c6  M10&`cDC<
003fe8ab  $JBC;p
003fe8e1  HI2ifJ
003fee5f  uY?KvW
005003a5  FnGOH,I
0050048f  y1ySyty
0050049f  z-zJzfz
005013a5  FnGOH,I
0050148f  y1ySyty
0050149f  z-zJzfz
0050f073  l."pKPA
00521073  l."pKPA
005d5429  Apple Display
005d56cb  Apple Display
005d5c29  Apple Display
005d5dcb  Apple Display
005ed013  hofmd{b
005f0688  T@pDUU
005f0698  \@pDJJ
005f06a0  `@pDVV
005f06b8  l@pDHH
005f0711  @pDUUUU
005f0721  @pDUUUU
005f08c8  tApDB`QQxApD
005f0a09  BpD    
005f0a11  BpD    
005f0e88  TDpDUU
005f0e98  \DpDJJ
005f0ea0  `DpDVV
005f0eb8  lDpDHH
005f0f11  DpDUUUU
005f0f21  DpDUUUU
005f10c8  tEpDB`QQxEpD
005f1209  FpD    
005f1211  FpD    
005f1688  THpDUU
005f1698  \HpDJJ
005f16a0  `HpDVV
005f16b8  lHpDHH
005f1711  HpDUUUU
005f1721  HpDUUUU
005f18c8  tIpDB`QQxIpD
005f1a09  JpD    
005f1a11  JpD    
005f1e88  TLpDUU
005f1e98  \LpDJJ
005f1ea0  `LpDVV
005f1eb8  lLpDHH
005f1f11  LpDUUUU
005f1f21  LpDUUUU
005f20c8  tMpDB`QQxMpD
005f2209  NpD    
005f2211  NpD    
005f2688  TPpDUU
005f2698  \PpDJJ
005f26a0  `PpDVV
005f26b8  lPpDHH
005f2711  PpDUUUU
005f2721  PpDUUUU
005f28c8  tQpDB`QQxQpD
005f2a09  RpD    
005f2a11  RpD    
005f2e88  TTpDUU
005f2e98  \TpDJJ
005f2ea0  `TpDVV
005f2eb8  lTpDHH
005f2f11  TpDUUUU
005f2f21  TpDUUUU
005f30c8  tUpDB`QQxUpD
005f3159  UpDphRC
005f3209  VpD    
005f3211  VpD    
005f3688  TXpDUU
005f3698  \XpDJJ
005f36a0  `XpDVV
005f36b8  lXpDHH
005f3711  XpDUUUU
005f3721  XpDUUUU
005f38c8  tYpDB`QQxYpD
005f3a09  ZpD    
005f3a11  ZpD    
005f3e88  T\pDUU
005f3e98  \\pDJJ
005f3ea0  `\pDVV
005f3eb8  l\pDHH
005f3f11  \pDUUUU
005f3f21  \pDUUUU
005f40c8  t]pDB`QQx]pD
005f4f01  dpD   
005f56c8  thpDP&
005f582e  @?(ipD?
005f5836  ??,ipD
005f5840  0ipD??
005f8688  T@pDUU
005f8698  \@pDJJ
005f86a0  `@pDVV
005f86b8  l@pDHH
005f8711  @pDUUUU
005f8721  @pDUUUU
005f88c8  tApDB`QQxApD
005f8a09  BpD    
005f8a11  BpD    
005f8e88  TDpDUU
005f8e98  \DpDJJ
005f8ea0  `DpDVV
005f8eb8  lDpDHH
005f8f11  DpDUUUU
005f8f21  DpDUUUU
005f90c8  tEpDB`QQxEpD
005f9209  FpD    
005f9211  FpD    
005f9688  THpDUU
005f9698  \HpDJJ
005f96a0  `HpDVV
005f96b8  lHpDHH
005f9711  HpDUUUU
005f9721  HpDUUUU
005f98c8  tIpDB`QQxIpD
005f9a09  JpD    
005f9a11  JpD    
005f9e88  TLpDUU
005f9e98  \LpDJJ
005f9ea0  `LpDVV
005f9eb8  lLpDHH
005f9f11  LpDUUUU
005f9f21  LpDUUUU
005fa0c8  tMpDB`QQxMpD
005fa209  NpD    
005fa211  NpD    
005fa688  TPpDUU
005fa698  \PpDJJ
005fa6a0  `PpDVV
005fa6b8  lPpDHH
005fa711  PpDUUUU
005fa721  PpDUUUU
005fa8c8  tQpDB`QQxQpD
005faa09  RpD    
005faa11  RpD    
005fae88  TTpDUU
005fae98  \TpDJJ
005faea0  `TpDVV
005faeb8  lTpDHH
005faf11  TpDUUUU
005faf21  TpDUUUU
005fb0c8  tUpDB`QQxUpD
005fb159  UpD`qBS
005fb209  VpD    
005fb211  VpD    
005fb688  TXpDUU
005fb698  \XpDJJ
005fb6a0  `XpDVV
005fb6b8  lXpDHH
005fb711  XpDUUUU
005fb721  XpDUUUU
005fb8c8  tYpDB`QQxYpD
005fba09  ZpD    
005fba11  ZpD    
005fbe88  T\pDUU
005fbe98  \\pDJJ
005fbea0  `\pDVV
005fbeb8  l\pDHH
005fbf11  \pDUUUU
005fbf21  \pDUUUU
005fc0c8  t]pDB`QQx]pD
005fcf01  dpD   
005fd6c8  thpDP&
005fd82e  @?(ipD?
005fd836  ??,ipD
005fd840  0ipD??
0060010f  bklc1C
00600163  cabl1C
006001b7  dis01t
0060023c  dis11t
006002c1  dis21t
00600346  dis31t
006003cb  frmc1C
0060041f  tcon1t
006004a4  trin1C
006006a5  MANP1p
00600726  OBJP1&
00600837  ~+?Abz+
00603542  ahi`!h
0060398b  fJF)F F&`NF
00603be7   pGpGpGpG8
00603eb8  SIGRTMEM: Out of heap memory
00603ed8  : Heap memory corrupted
00604060  READ OTP ADDRE:%2x
00604074  READ OTP VALUE:%2x
00604088  READ OTP TCON_EERROR Time Out!
006041bc  WRITE OTP
006041c8  Write OTP TCON_EERROR Time Out!
0060446d  qHF*F#F
00604665  qHF*F#F
00604940  OTP Unlock TCON_EERROR!
00604e31  !i`ihX"b
00604ed3   h`hhX!a
00605039  !i`ihX"b
006050db   h`hhX!a
006065d8  CLEAR SYSIRQ(H) :%x
006065f0  RCVD SYSIRQ CLR(0x%X) WOT EN , EN:0x%X
00606618  Clearing FW SYSIRQ : 0x%X
00606634  CLEAR SYSIRQ MASK: NULL PTR
00606764  SYS IRQ REG MASK NULL PTR
0060680c  EN SYSIRQ : %d
0060681c  EN SYSIRQ(HOST NOT REG) : %d
0060683c  INVLD SYSIRQ SET  : %d
00606900  TCON_UARP_AllHeadersAndMetaDataComplete()
006069e0  TCON_UARP_ApplyStagedAssets()
00606b00  Save Signed Manifest:
00606b45  @pGTCON_UARP_AssetProcessingNotification2()
00606ba5  @pGTCON_UARP_AssetProcessingNotificationAck()
00606c48  TCON_UARP_AssetReady()
00606d94  TCON_UARP_HWVersion()
006070f8  TCON_UARP_MfrName()
00607148  TCON_UARP_ModelName()
006071cc  TCON_UARP_OTP_FusingType()
0060761c  TCON_UARP_PayloadData() 4cc: %s, Offset: %d, len: %d
006078f8  TCON_UARP_PayloadDataComplete2()
0060791c  CRC32:  0x%08x
0060792c  Payload Hash Match: Fail)
00607948  Payload Hash Match: Pass)
006079f0  TCON_UARP_PayloadMetaDataTLV() tlvType: 0x%08x
00607a80  TCON_UARP_PayloadReady()
00607af8  TCON_UARP_OTP_PROD()
00607bc4  TCON_UARP_RescindAllAssets()
00607c5c  TCON_UARP_OTP_SDOM()
00607c74  SDOM: 0x%08x, SDomain: %d
00607ce4  securityMode: %d
00607d80  TCON_UARP_SendMessage() buf: 0x%08x, len: %d
00607db0  urp_q_tx_buf: 0x%08x
00607dc8  [ERROR] UARP_TX_BUF_Q: FULL
00607e24  TCON_UARP_SNo()
00607f9e  8FIF"F
00607fb0  asset_numPayloads: %d
00607fc8  uarpPlatformEndpointAssetQueryNumberOfPayloads(): Error
0060804c  TCON_UARP_Vendor()
00608bb5  [ERR]: 
00608bc0  WDOG Bite Error
00608c44  NVM DeviceID : 0x%x
00608c58  Failed to initialize DMA driver: 0x%x
00608c80  Failed to initialize NMI: 0x%x
00608e58  DispSHA2Pass
00608e68  BlfwSHA2Pass
00608e78  FcfwSHA2Pass
00608e88  TrinSHA2Pass
00608e98  CablSHA2Pass
00608ed1  x2ysy4z
006091b9  New APICmd: %02x %02x %02x %02x %02x %02x
006091e4  api_rcvd_to_process_time_us: %llu
00609209  tcon_time_us: %llu
0060921c  Soft Resetting Banyan
0060935f  `&i%afi
0060942d  e n%f`nef
00609540  dma timeout
0060954c  dma error
00609558  dma_failed status: 0x%08x, 0x443C8030: 0x%08x
00609588  dma failed
00609c6c  flash erase address: 0x%08x, size: 0x%08x
00609e60  flash ID not supported, use W25Q01NWTBIQ as default
00609e94  mode not availabe for current flash
0060a13d  nonce: 0x%2x%2x%2x%2x bnch: 
0060a5b0  earse_flash Err
0060a780  API RD INVLD SYSIRQ BUF SIZE :%d
0060a8ac  Start g_mem_address: 0x%08x
0060adb1  [ERR]: 
0060adbc  MCU: %d, SHA256 Failed
0060b1dc  BootldrStart
0060b1f0  %s Version 0x%x 
0060b204  Bootloader
0060b210  Failed setting PLL
0060b224  BSP Init Failed
0060b234  FW_Image: 0x%08x
0060b248  u8FW_LOAD_DIS: 0x%02x
0060b260  RecoveryMode
0060b270  BootldrDone
0060b2f8  API MNG INVLD SYSIRQ OPT :%d
0060b77c  PROD UnProgrammed!
0060b790  PROD Programmed!
0060b7a4  PROD_prog_status: 0x%x, 0x%x, 0x%x
0060b864  SDOM UnProgrammed!
0060b878  SDOM Programmed!
0060b88c  SDOM_prog_status: 0x%x, 0x%x, 0x%x
0060b91c  Program PROD Pass!
0060b930  Program PROD Fail!
0060b9b4  Program SDOM Pass!
0060b9c8  Program SDOM Fail!
0060bafd  SHA256: 
0060be3c  SETINFO_SUBCMD_OTP
0060be50  SETINFO_SDOM_PROG
0060be64  SETINFO_PROD_PROG
0060c154  RdAPI Status: 0x%02x
0060c3f0  API MNG INVLD SYSIRQ SUBCMD :%d
0060c4bc  read_packet_addr: 0x%08x, len: %d
0060c598  API Status: %02x
0060c5ac  API Error: %02x
0060c5c0  tcon_time_us: %llu
0060c7d9  **SHA Failed**
0060ca95  h!`Aha`
0060cab4  urp_q_pop: wrap
0060cac5  urp_send_msg_pop: addr: 0x%08x, len: %d
0060cb40  urp_q_push: wrap
0060cb55  urp_new_msg_push addr: 0x%08x, len:%d 
0060d324  PFYF"F
0060d5e0  uarpFree() mem: 0x%08x
0060d998  5"@FIF5%
0060ddaf  0(F!FBF
0060ddf1  0(F!FBF
0060ddff  G(F!FBF
0060df00  5"@FIF5%
0060e688   F1F*FCF
0060e6a2   F1F*FCF
0060e88a  XFAF2F
0060e9e0  XFAF"F
0060ea6e  XFAF"F
0060eb3c  ( XFAF
0060ec2c  XFAFRF
0060ec3f  "XFAF#F
0060ec5e  XFAF*F;F
0060ed20  XFAFJF
0060ed6d  "XFAFSF
0060ee6b  "XFAF+F
0060eeaa  XFAF"F
0060eebc  XFAF2FKF
0060ef02  XFAF*F
0060efc3  "XFAF+F
0060efd7  FXFAF*F#F
0060f02e  XFAF2F
0060f0ac  XFAF"F
0060f13e  HPXFAF#F
0060f222  XFAF:F
0060f327  FXFAF"F
0060f3ae  XFAF*F
0060f414  XFAF:F
0060f4a0  [h;ach
0060f4ee  XFAFJF^
0060f4f8  XFAF:F
0060f510  XFAF2F
0060f54a  XFIFRF
0060fffd  [INFO]: 
00610008  write_uarp_api_callback()
006107b0  WrAPI Status: 0x%02x
00611358  0123456789ABCDEF@0X
0061136c  0123456789abcdef@0x
006117d0  uarpZalloc() mem: 0x%08x, len:%d
006117f2  TCON_UARP_AssetMetaDataComplete() numPayloads:%d
00611825  [INFO]: 
0061182e  TCON_UARP_PayloadMetaDataComplete()
00611852  NVM_W_ADDR:  0x%08x, size: %d
00611870  TCON_UARP_SuperBinaryOffered(): numPayloads: %d, superbinary version: %d.%d.%d.%d
006118c7  TCON_UARP_PayloadDataComplete2 payloadIndex: 0x%04x
006118fb  NVM_W_ADDR:  0x%08x
0061190f  Bufaddr: 0x%08x
00611921  g_mem_address: 0x%08x
00611939  count_loop : %d
0061194a  FW Hash Check Failed
00611960  In DFU Recovery Mode
00611977  [ERR]: 
0061197f  CablSHA2Err
0061198b  TrinSHA2Err
00611997  DispSHA2Err
006119a3  FcfwSHA2Err
006119af  BlfwSHA2Err
006119be  FW_POINTER:  0x%08x
006119d2  TLV: 0x%04x, size: 0x%08x
006119ec  g_flash_address: 0x%08x
00611a04  API MNG INVLD SYSIRQ BUF SIZE :%d
00611a2d  flash erase_flash64k address: 0x%08x, size: 0x%08x
00611a61  flash erase_flash4k address: 0x%08x, size: 0x%08x
00611a94  SPI_Sector64KErase_FIFO0 Err
00611ab1  SPI_SectorErase_FIFO0 Err
00611acb  erase_flash64k Err
00611ade  erase_flash4k Err
00611af0  Expected Size: %08x
00611b05  RdBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00611b59  WrBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00611bad  RdBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00611c01  WrBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
00611c55  SYS IRQ RD MASK NULL PTR
00611d4d  @PD8FPD
00611d55  FPD|FPD
00611d75  FPD #PD
00611d7d  FPD`#PD
00631558  pGpGpG8
006316ac  ahi`!h
00631dcf  fJF)F F&`NF
00632bbc  SIGRTMEM: Out of heap memory
00632bdc  : Heap memory corrupted
00632e83  (/FDF0F
00632ea3  F8F!FRF[F(
00632ed3  ((FAFRF[F
00632f68  calculated SVCLK too small: %f
00632f88  htotal is 0
00633254  READ OTP ADDRE:%2x
00633268  READ OTP VALUE:%2x
0063327c  READ OTP TCON_EERROR Time Out!
00633484  WRITE OTP
00633490  Write OTP TCON_EERROR Time Out!
006335b7  D ``hah
006336c7  P(`hhih
006338d0  Scaler Status: 0x%02x
0063420c  refresh rate: %f
00634220  htotal 0
00634323  <IFBF[F
0063469c  [LBA] INVALID BLCK ID TO CHECK %d
006346c0  [LBA] INVALID SIZE FOR %d, received : %d, expected : %d
006347e0  RCVD INVALID BLOCK FOR SIZE : %d
00634995  TailIndex : %d
006349a5  New TailIndex : %d
006349b8  LBA HDR WRITE FAIL : %d , BLCK:%d
006349dc  LBA BLK INIT BLOCKID : %d :: ADDR : 0x%x
00634a08  LBA HDR CONST FAIL : %d
00634b80  L2P START
00634b8c  L2PStart   
00634b98  LBA INIT FAIL :%d
00634bac  LBA SHOULD NEVER COME HERE
00634bc8  LBA INVALID HEADER : %d
00634be0  LBA FREE TAIL:%d
00634bf4  L2PDone    
00634c00  L2P DONE
00634d80  Skip ERASE PREV ASSIGNED ADDRESS: 0x%x
00634df0  LBA FREE Q FULL : %d
00634ff4  LBA READ OFFSET IS 0, SHOULD NEVER COME HERE 
00635024  LBA RD FAIL : %d
00635038  LBA RD INVALID CALCULATED ADDR : 0x%x :: BLOCKID : %d
0063525c  !FBFKF
00635452  !FRFCF
00635774  OTP Unlock TCON_EERROR!
00635841  [ERR]: 
0063584c  GetPNGData Error
00635d58  PNG FileSize: 0x%x
00635d6c  width x height: %d x %d
00635d84  PNG_test with error: %d
00635d9c  PNG File Too Big
00636281  !i`ihX"b
00636323   h`hhX!a
00636481  !i`ihX"b
00636523   h`hhX!a
0063691c  scaler_ddp_attribt_not_stable
0063693c  master dp unstable irq
00636954  slave dp unstable irq
00636d3c  DSC enable not same in master and slave: %d, %d
00637068  get link rate TCON_EERROR
00637084  link rate: %f
00637094  resolution: %d x %d
006370ac  WET: 0x%08x
006370bc  WET is 0
006370c8  pixel clock:%f MHz
006370dc  WET not available
00637734  CLEAR SYSIRQ(H) :%x
0063774c  RCVD SYSIRQ CLR(0x%X) WOT EN , EN:0x%X
00637774  Clearing FW SYSIRQ : 0x%X
00637790  CLEAR SYSIRQ MASK: NULL PTR
00637904  SYS IRQ RD MASK INVALID ID
006379cc  SYS IRQ REG MASK NULL PTR
00637a54  EN SYSIRQ : %d
00637a64  EN SYSIRQ(HOST NOT REG) : %d
00637a84  INVLD SYSIRQ SET  : %d
00637b34  TCON_UARP_AllHeadersAndMetaDataComplete()
00637cb4  TCON_UARP_ApplyStagedAssets()
00637cd5  nonce: 0x%8x bnch: 
00637cf5  pFlags: 0x%4x
00637d4c  TCON_UARP_AssetMetaDataComplete() numPayloads:%d
00637de8  Save Signed Manifest:
00637e30  TCON_UARP_AssetProcessingNotification2()
00637e8c  TCON_UARP_AssetProcessingNotificationAck()
00637ef0  TCON_UARP_AssetReady()
00638028  TCON_UARP_HWVersion()
006383f8  TCON_UARP_MfrName()
00638444  TCON_UARP_ModelName()
006384c4  TCON_UARP_OTP_FusingType()
00638794  TCON_UARP_PayloadData() 4cc: %s, Offset: %d, len: %d
00638a00  TCON_UARP_PayloadDataComplete2()
00638a24  CRC32:  0x%08x
00638a34  Payload Hash Match: Fail)
00638a50  Payload Hash Match: Pass)
00638a98  TCON_UARP_PayloadMetaDataComplete()
00638b04  TCON_UARP_PayloadMetaDataTLV() tlvType: 0x%08x
00638b7c  TCON_UARP_PayloadReady()
00638bf0  TCON_UARP_OTP_PROD()
00638ca8  TCON_UARP_RescindAllAssets()
00638d34  TCON_UARP_OTP_SDOM()
00638d4c  SDOM: 0x%08x, SDomain: %d
00638dbc  securityMode: %d
00638e4c  TCON_UARP_SendMessage() buf: 0x%08x, len: %d
00638e7c  urp_q_tx_buf: 0x%08x
00638e94  [ERROR] UARP_TX_BUF_Q: FULL
00638eec  TCON_UARP_SNo()
0063903e  HFQF"F
00639050  asset_numPayloads: %d
00639068  uarpPlatformEndpointAssetQueryNumberOfPayloads(): Error
006390e8  TCON_UARP_Vendor()
00639775  GpGJn"
00639fa1  [ERR]: 
00639fac  WDOG Bite Error
0063a1cd  BLAPI: UpdatedLUMInBuf Pass
0063a1ed  BLAPI: UpdatedLUMInBuf Fail
0063a3b4  BLS_Sloper Update
0063a3c8  bls_sloper_time: %d
0063a3dc  BLS_Sloper Done
0063a3ec  BLS_Sloper Update Fail
0063a706  ;iYDWh
0063ab98  cal_wet
0063ade0  cal_wfm
0063ae65  [INFO]: 
0063ae70  SHA2 Input src_addr: 0x%8x size: 0x%8x
0063b058  SDP hwidth error: %d
0063b070  vheight not same in master and slave %d,%d
0063b09c  DDP hwidth error: %d
0063b21b  x2ysy4z
0063b34d  New APICmd: %02x %02x %02x %02x %02x %02x
0063b378  api_rcvd_to_process_time_us: %llu
0063b39d  tcon_time_us: %llu
0063b3b0  Soft Resetting Banyan
0063b5fc  start copy: latest dyncfg indx: %d, addr: %x
0063b62c  dyncfg_sha256_check: Pass
0063b649  g_dyncfg_validity_flags: %llu
0063b728  skip loading: DEP_CAL
0063b740  start copy: DEP_CAL_FC_LUTs
0063b75c  copy DEP_CAL_FC_LUTs failed
0063b778  copy DEP_CAL_INFO failed
0063b794  copy DEP_CAL_BL_LUTs failed
0063b86c  skip loading: LUT_0x180-0x189
0063b88c  start copy: LUT_0x%04x
0063b8a4  copy LUT_0x%04x failed
0063b938  Skip loading from nvm
0063bb14  skip loading: psf0-2
0063bb2c  start copy: psf0
0063bb40  copy psf0 failed
0063bb54  start copy: psf1
0063bb68  copy psf1 failed
0063bb7c  start copy: psf2
0063bb90  copy psf2 failed
0063bdf8  start copy: tcon luts
0063be10  copy tcon luts failed
0063be28  tconlutsFail
0063be38  tconlutsPass
0063be48  start copy: BL luts
0063be5c  copy BL luts failed
0063be70  blfwlutsFail
0063be80  blfwlutsPass
0063c8b4  ?hEaEbEcEdEeEf
0063c995  P?hhahbhchdhehf
0063d67c  0x44700504: 0x%x, timeout: %d
0063d69c  DDRx64 Init Done
0063d6b0  DDR Status: 0x%02x
0063d6c4  DDRInitFail
0063d6d1  [ERR]: 
0063d6dc  DDRx64 Init Failed
0063dccb  QAapGp
0063dd5f  `&i%afi
0063de2d  e n%f`nef
0063df40  dma timeout
0063df4c  dma error
0063df58  dma_failed status: 0x%08x, 0x443C8030: 0x%08x
0063df88  dma failed
0063ea53  bjPjX"
0063ea64  Video: Live
0063ea70  DPCD00107: 0x%02x DPCD001B0: 0x%02x, DPCD02020: 0x%02x
0063ee30  Unplugged, DP0 Aux_N DET=0
0063ee4c  Unplugged, DP1 Aux_N DET=0
0063eefc  BOARD_EVB
0063ef08  BOARD_TBB
0063f084  Preset load tcon %d dyncfg
0063f96c  flash erase address: 0x%08x, size: 0x%08x
0063fb58  time_sec: %d
0063fb68  temp_time: %d
006408a8  WPC in 0D
006408b4  OVD in 0D
006408c0  WPC, OVD in 0D
006408d0  PRC 1DT: 0x%04x
00640b30  flash ID not supported, use W25Q01NWTBIQ as default
00640b64  mode not availabe for current flash
00640db9  h1`)h!`iha`
00640dcb  `)i!aiiaa
00640df5  ` i(a`iha
00640e41  nonce: 0x%2x%2x%2x%2x bnch: 
0064151c  GET_LOG_COUNT: %d
00641531  [ERR]: 
0064153c  save_log failed due to NVM Read Error
00641564  NVM_LOG_COUNT: %d
006417d9  ObjTag: 0x%08x tag: 0x%08x
006417f4  exp_hash: 
00641980  IPC_HP_MSG_Q
00641a0c  IPC_NP_MSG_Q
00641d30  8F1Fbh
00642535  i=aUi}a
00642545  j=bUj}b
006427c4  DP0 Link Trained
006427d8  DP Cable: Unplugged
006427ec  DP Attrib: Stable
00642800  DDP Mode: %d
00642810  SetSrcAttr fail or attrib not stable, set to freerun
00642848  Cal SVCLK Fail
0064289c  ALL_H: Power Down Panel
006428b4  SPF_N: Power Down Panel
00642a60  DPCD600: 0x%02x
00642a70  HPD DeAssert
00642a80  Start DPCD600 time check
00642a9c  Start DPCD600 check cancel
00642ab8  Attrib: 0x%08x
00642ac8  Start DPCD600 time check done
00642d00  dpcd202 =1
00642d0c  dpcd202 =0
00642d18  g_dpcd427: 0x%02x, dpcd4f1: 0x%02x
00643008  DEP_CAL_HASH: SLOT: %d LUT_0x%04x failed
006430f4  USR_CAL_HASH: SLOT: %d LUT_0x%04x failed
00643322  Bb*`jhB
00643b57   BaBi*
00643f90  earse_flash Err
00644138  0F)FCF
00644146  f20F)FCF
0064534c  (PhaxyA
006457a5  [INFO]: 
006457b0  IPC(%d -> %d): 0x%02x, size: 0x%04x
006457d4  start copy: default dyncfg indx: 0
006457f8  copy default dyncfg failed
00645815  g_dyncfg_validity_flags: %llu
00645856  pGRiHy
00645c37  0Ha0yMi)F
00645cd4  API RD INVLD SYSIRQ BUF SIZE :%d
00645f30  start g_tcon_dram_address: 0x%08x
00645fa0  Start g_mem_address: 0x%08x
0064606e  T`CiThc
00646077  $T`CiTh
006461da  SaHjSi`
006461e3  #SaHjSi
006465d3  !y`yhh
0064671d  b:byjO
00646731  Aybyjb
00646739  Aybyj!
006468d3  b:dzl{l
00646eb0  init_scaler_enable1
00647135  26:>QQQQQQF  
00647608  SETINFO_SUBCMD_OTP
0064761c  SETINFO_SDOM_PROG
00647630  SETINFO_PROD_PROG
006477c9  [INFO]: 
006477d4  IPC(%d -> %d): 0x%02x, size: 0x%04x
00647836  ByKaKi#
0064796c  copy cpld from nvm to dram
00647988  copy cpld from nvm to dram failed
006479ac  stream cpld data...
006479c0  finish cpld program...
00647d85  0Ha0yMi)F
00647de4  ERROR: REMAIN BYTES:%d
00647f11  h!`Qha`
006480db  h!`Aha`
00648128  npq_pop: wrap
00648139  new_msg_pop: 0x%08x
00648197  `ahA`*h
006481b4  npq_push: wrap
006481c5  new_msg_push: 0x%08x
00648251  hp_new_msg ch: 0x%02x
006482a9  np_new_msg src: %d ch: 0x%02x
006482f2   F2FCF
00648366  (F1FBF
0064847a  AFJF+F
006484c8  Wait IPC(%d <- %d): 0x%02x
006484e4  IPC(%d <- %d): 0x%02x Recvd
0064865c  allow_user_cal: %d
00648670  calibration_space: %d
00648688  calib_header_id: 0x%x, lut_id: 0x%0x
006486b0  pp_ccm_header_id: 0x%x, lut_id: 0x%0x
00648a54  default_bl_led_zone_value: 0x%08x
00648b7e  >FRF1F
00648c45  [ERR]: 
00648c8b  qps0pp
00648c94  dp0_edid_displayid_size: %d
00648ceb  qps0pp
00648cf4  dp1_edid_displayid_size: %d
00648f04  dram_config sha256 failed
00648f20  DramCfgFail
00648f2c  DramCfgPass
00648f38  dram_config_hdr: 0x%08x
00648f50  dram_config_ver: 0x%08x
00648f68  dram_config_entries: 0x%08x
006491c0  User DepCal: Slot: %d
006491d8  Skip loading User DepCal: Slot: %d
006491fc  Factory DepCal: Slot: %d
00649218  Skip loading Factory DepCal: Slot: %d
006492bc  IndCaldone 
006492c8  DepCalHash 
006492d4  DepCaldone 
006492e0  psfdone    
00649302  8hFY F
00649404  1dql Cb
006496b8  tcon_config_hdr: 0x%08x
006496d0  tcon_config_ver: 0x%08x
006496e8  tcon_config_entries: 0x%08x
00649704  TconCfgFail
00649710  TconCfgPass
0064971c  Skip loading tcon_config
00649738  Apply P2 Panel Timing!
00649864  g_policy_flags: 0x%08x
006499b6  8FAFJF
00649a24  8`(D!FJF
00649c6f  ! DPE@
00649dc6  @F1FRF
00649df6  @F1FRF
00649e6c  YF2FSF
00649e90  YF2FSF
00649f86  YF2FSF
0064a048  decodeGeneric_exit
0064a2f2  "hci(F
0064aad4  lodepng_inflatev
0064aae8  lodepng_inflatev_error
0064ad78  (FaFBF
0064af1c  Erasing DB NVM Power Cycle Info Section
0064af44  pwrcyl_log_in_dbnvm: %d pwron_time_in_mins: %d
0064af74  total_power_on_time: %d
0064af94  ResetNow
0064b104  Options -> Error Checking Standard: SHA256
0064b130  Payload Size: %d bytes
0064b148  Payload Type: 0x%04x
0064b160  Payload LUT ID: 0x%04x
0064b178  Payload Version: %d.%d
0064b1e4  LUT address: 0x%08x
0064b374  Target SHA256: 
0064b38c  Target CRC: 0x%08x
0064b3a0  Compute CRC Size: %d
0064b3b8  Compute CRC: 0x%08x
0064bdac  8F1FBFKF
0064be95  "(FQF>h
0064bec2  @F1FZFKF
0064bf96  XF1FBFKF
0064c136  8F1FBFKF
0064c1b0  manage_factory_cal: sub_cmd=%x
0064c1d0  manage_factory_cal cm ind volatile last slice,[%d 0x%x]
0064c27c  API MNG INVLD SYSIRQ OPT :%d
0064c31c  manage_user_cal: sub_cmd=%x
0064d65d  hZaJhZe
0064d68d  hZaJhZe
0064d950  MBC Lost Lock
0064ddd8  PROD UnProgrammed!
0064ddec  PROD Programmed!
0064de00  PROD_prog_status: 0x%x, 0x%x, 0x%x
0064dec8  SDOM UnProgrammed!
0064dedc  SDOM Programmed!
0064def0  SDOM_prog_status: 0x%x, 0x%x, 0x%x
0064df84  Program PROD Pass!
0064df98  Program PROD Fail!
0064e01c  Program SDOM Pass!
0064e030  Program SDOM Fail!
0064e098  payload num: 0x%08x
0064e0b0  payload_id: 0x%08x
0064e0c4  payload_size: 0x%08x
0064e0dc  payload_global_addr_ptr: 0x%08x
0064e7be  Src MCU:%d, addr: 0x%08x
0064e7d8  Dst MCU:%d
0064e7e4  IPC Opcode:0x%02x
0064e7f8  Priority: %d, CHID: %d
0064e810  MsgSize: %d
0064e820  Msg: 0x%08x
0064e83c  FWCookie: 0x%x
0064e84c  Wait DB CLR
0064eb84  PNG_Decode[%d]: Start
0064eb9c  PNG_Decode[%d]: Success
0064ebb4  PNG_Decode[%d]: Error
0064ec34  PLS Fault: 0x%04x, Trigger Shutdown!
0064ecc8  PMIC Fault 0x%02x, 0x%02x, Trigger Shutdown!
0064f358  HPD DeAssert
0064f659  SHA256: 
0064f6b3  ohhxhhhhh
0064f954  SETINFO_SUBCMD_OTP
0064f968  SETINFO_SDOM_PROG
0064f97c  SETINFO_PROD_PROG
00650298  total_telemetry_in_dbnvm: %d, index: %x
006502c0  new_telemetry_in_dbnvm: 0x%08x
00651599   pGa pG-
00651798  PFAF2F
00651891   pGJ pG-
00651cd4  RdAPI Status: 0x%02x
00651dd4  CPLD Read: %d
006520d8  I2C Rd: Failed
006521ac  read_factory_cal: sub_cmd=%x
006525c0  Reading BLOCK : %d : offset : %d
006525f0  DONE READING JOURNAL DATA : %d
006526c4  RC GetInfo: %d
006526d4  I2C Rd: Failed
00652754  API MNG INVLD SYSIRQ SUBCMD :%d
0065280c  read_packet_addr: 0x%08x, len: %d
00652888  read_user_cal: sub_cmd=%x
00652cac  start copy: default dyncfg indx: %d, addr: %x 
00652cdc  copy default dyncfg failed
00652cf8  default_dyncfg_sha256_check: Fail
00652d1c  DynCfgFail
00652e6d  LED Aging Not Found in Journal
00652e8d  LED_Aging_Hash_Check: Fail
00652ea9  LED_Aging_Hash_Check: Pass
0065378c  save_log failed due to NVM Read Error
006537b4  NVM_LOG_COUNT: %d
006537c8  save_log failed due to NVM Erase Error
006537f0  save_log failed due to NVM Write Error
006539a5  Pending Data Size: %d
006539bd  Journal Write Error
00653acd  g_reset_counter: %d
00653b5e  4 CXBPO
00653c62  @BBPBXCX
00654079  Wge#e'h&h
00654189  ahb)b(h
00654850  API Status: %02x
00654864  API Error: %02x
00654878  tcon_time_us: %llu
00654e28  refresh_rate: %f, no_of_vblank: 0x%08x
00655179  **SHA Failed**
006556c0  wait for cdi vblank start timed out...
006556e9  sync_exit: %llu
0065599c  Fail: mmu_reset: 0x%x
006559b4  Fail: mmu_enable_disable: 0x%x
006559d4  Fail: mmu_remove_entry: 0x%x
006559f4  Fail: mmu_add_entry: 0x%x
00656211  h!`Aha`)h
00656230  urp_q_pop: wrap
00656241  urp_send_msg_pop: addr: 0x%08x, len: %d
006562bb  `*hahA`P
006562cc  urp_q_push: wrap
006562e1  urp_new_msg_push addr: 0x%08x, len:%d 
00657282  PFYF"F
0065745a  pGuarpFree() mem: 0x%08x
006577e0  5"@FIF5%
00657af1  0(F!FBF
00657b33  0(F!FBF
00657b41  G(F!FBF
00657c34  5"@FIF5%
00658184   F1F*FCF
0065819e   F1F*FCF
0065835a  XFAF2F
0065846b  FXFAF"F
006584a8  , XFAF
006585a0  XFAFRF
006585b3  "XFAF#F
006585d2  XFAF*F;F
00658698  XFAFJF
006586e9  "XFAFSF
006587b5  "XFAF+F
006587f4  XFAF"F
00658806  XFAF2FKF
00658850  XFAF"FO
00658892  XFAF*F
006589ac  XFAF"F
00658a40  XFAF"F
00658b54  XFAF:F
00658bea  XFAF2F
00658c8e  XFAFJF0
00658cf2  XFAF*F
00658d2b  "XFAF+F
00658d3d  FXFAF*F#F
00658d7e  HPXFAF#F
00658da2  XFAF:F
00658dae  XFAF:F
00658dc2  XFAF2F
00658e52  XFIFRF
006595b0  uarpZalloc() mem: 0x%08x, len:%d
00659659  [INFO]: 
00659664  write_uarp_api_callback()
00659a84  Scaled: Htotal %d Hwidth %d Vheight %d
00659aac  Scaler Disabled: Htotal %d Hwidth %d Vheight %d
00659c8c  status_verify_cal()
00659ca0  manage_factory_cal cm dep last slice,[%d 0x%x]
00659cd0  payload_lut_id: 0x%04x
00659ce8  Verify Status: %d
0065a1bc  zsXC!`)h``
0065a468  WrAPI Status: 0x%02x
0065a558  CPLD Write: %d
0065a8d0  Device Write: %d
0065a8e4  I2C Wr: Failed
0065aba8  RCVD SIZE : %d
0065abb8  Writing BLOCK : %d : offset : %d
0065abdc  DONE WRITING JOURNAL DATA : %d
0065ac8c  RC Write: %d
0065ac9c  I2C Wr: Failed
0065ad38  0F!F:FCF
0065ad98  9FBFSF
0065b153  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
0065c7d8  0123456789ABCDEF@0X
0065c7ec  0123456789abcdef@0x
0065c811  0123456789abcdefxp
0065c824  0123456789ABCDEFXP
0065ca68  UUUUUU
0065d535  Qkkbal
0065d7f3  -NVM DeviceID : 0x%x
0065d809  CDPwrLo     
0065d816  RCRstEnd    
0065d823  MainPwrLo    
0065d831  HiChkFail   
0065d83e  LoChkFail   
0065d84b  HiChkPass   
0065d858  LoChkPass   
0065d865  RCRstStart  
0065d873  [INFO]: 
0065d87d  [ERR]: 
0065d885  CDPwrPGFail 
0065d892  MnPwrPGFail 
0065d89f  CDPwrPGPass 
0065d8ac  MnPwrPGPass 
0065d8b9  Failed to create Global Timer: TIMER_INST_0
0065d8e5  Failed to create Local Timer: TIMER_INST_1
0065d910  Failed to enable MLBDSP HB
0065d92b  MLBDSP HB Enabled
0065d93d  DefaultPDone
0065d94a  MLBDSPHBFail
0065d957  FC WDOG Bite Error
0065d96a  CABL WDOG Bite Error
0065d97f  TRIN WDOG Bite Error
0065d994  MLBDSPHBPass
0065d9a1  Failed to initialize NMI: 0x%x
0065d9c0  Failed to initialize IPC HP Queue: 0x%x
0065d9e8  Failed to initialize IPC NP Queue: 0x%x
0065da10  Failed to initialize DMA driver: 0x%x
0065da36  Failed to initialize WDOG driver: 0x%x
0065da5d  Failed to initialize UART driver: 0x%x
0065da84  Failed to initialize Doorbell driver: 0x%x
0065daaf  MLBDSP Ver: 0x%02x
0065dac2  IPC(%d -> %d): 0x%02x, size: 0x%04x
0065dae7  Switch UUID: 
0065daf5  IPC(%d -> %d), IPC_BLS_2DT_DATA
0065db15  IPC(%d -> %d), IPC_API_RD_CMD
0065db33  IPC(%d -> %d), IPC_API_WR_CMD
0065db51  IPC(%d -> %d), IPC_LED_AGING
0065db6e  IPC(%d -> %d), IPC_BLU_FAULT_INFO
0065db90  IPC(%d -> %d), IPC_OPCODE_SDP
0065dbae  IPC(%d -> %d), IPC_API_RD_RESP
0065dbcd  IPC(%d -> %d), IPC_GEN_RESP
0065dbea  lbuf_int_latency: %lld in usec
0065dc0a  duration_of_final_frame in usec: %llu
0065dc31  g_cdi_poweroff_time_ticks: %llu
0065dc52  g_lbuf_vbstart_global_time_ticks: %llu
0065dc7a  start_time_ticks: %llu
0065dc92  g_lbuf_vbstart_time_ticks: %llu
0065dcb2  FWCookie[%d]: 0x%x, lbuf_cookie: 0x%x
0065dcd8  ERR : %s
0065dce2  prc_header_id: 0x%x, lut_id: 0x%0x
0065dd06  ctp_ccm_header_id: 0x%x, lut_id: 0x%0x
0065dd2e  pwm_gain_header_id: 0x%x, lut_id: 0x%0x
0065dd57  start slot: %d hash: LUT_0x%04x
0065dd78  Apply P1 Panel Timing!
0065dd8f  copy FC luts failed
0065dda3  copy trinity luts failed
0065ddc1  trinlutsFail
0065ddce  fcfwlutsFail
0065dddb  FWCfgSHAErr
0065dde7  start copy: DEP_CAL_BL_LUTs
0065de03  FWCfgSHAPass
0065de10  DynCfgPass
0065de1b  trinlutsPass
0065de28  fcfwlutsPass
0065de35  start copy: FC luts
0065de49  start copy: trinity luts
0065de62  loading scaler_luts
0065de76  EOTF_MAP: 0x%08x
0065de87  pre_scaler_lut_dram_start_addr: 0x%08x, size: 0x%08x exp_crc: 0x%08x
0065decc  post_scaler_lut_dram_start_addr: 0x%08x, size: 0x%08x exp_crc: 0x%08x
0065df12  Exit DDR retention PASS
0065df2b  Exit DDR Failed, Retry
0065df43  PDStart     
0065df50  PDComplete  
0065df5d  RC_RST_DONE!
0065df6a  retention pre step FAIL!
0065df83  retention assert FAIL!
0065df9a  retention pre step PASS!
0065dfb3  retention assert PASS!
0065dfca  In retention mode!
0065dfdd  Not in retention mode!
0065dff4  Enter or Exit retention mode!
0065e012  enter_dram_retention_done!
0065e02d  exit_dram_retention_done!
0065e047  Enter dram retention for PD
0065e063  DDREXRETDONE
0065e070  RETPOSCAFAIL
0065e07d  RETPOSACFAIL
0065e08a  RETPOSRDFAIL
0065e097  RETPOSWDFAIL
0065e0a4  RETPOSRLFAIL
0065e0b1  RETPOSWRFAIL
0065e0c4  DDR Deassert PASS
0065e0d6  RETPOSCAPASS
0065e0e3  RETPOSACPASS
0065e0f0  RETPOSRDPASS
0065e0fd  RETPOSWDPASS
0065e10a  RETPOSRLPASS
0065e117  RETPOSWRPASS
0065e124  DB_STRAP_OUTER_LO_ENABLE Fail
0065e142  CDPWR_PG Fail
0065e150  MAINPWR_PG Fail
0065e160  DDR Deassert Fail
0065e173  all_mcu_off_time: %llu
0065e18b  pd_seq_time: %llu
0065e19e  cdi_to_mainpwr_time: %llu
0065e1b9  rc_rst_time: %llu
0065e1cb  BoardID : 0x%02x, VendorID : 0x%02x, HWCID0 : 0x%02x, HWCID1: 0x%02x
0065e210  DDR Status: 0x%02x
0065e223  ecid[3:0]: 0x%08x
0065e235  ecid[7:4]: 0x%08x
0065e247  RegRd: 0x%08x = 0x%08x
0065e25e  Reg: 0x%08x = 0x%08x
0065e273  RegWr: 0x%08x = 0x%08x
0065e28a  TAIL : %d, HEAD: %d, Count : %d 
0065e2ac  FAIL : %d
0065e2b7  NO MORE FREE BLKS : %d
0065e2cf  LBA WR SUCESS BLK ID :%d, Size : %d, ADDR: 0x%0x
0065e301  LBA RD NULL ADDR
0065e312  LBA WR NULL ADDR
0065e323  LBA RD INVLD  BLOCKID : %d
0065e33e  LBA WR INVLD  BLOCKID : %d
0065e359  LBA INIT BLOCK FAIL WR  BLOCKID : %d
0065e37e  LBA WD INVALID F ADDR : 0x%x :: BLOCKID : %d
0065e3ab  LBA HEADER INVALID : %d
0065e3c3  LBA RD INVLD SIZE : %d
0065e3da  LBA FREE Q EMPTY : %d
0065e3f0  INVALID PREV ASSIGNED ADDRESS, COULD BE NEW ALLOC ID: %d
0065e429  FAILED TO ERASE PREVIOUS ADDRESS : %x, blockid:%d
0065e45b  ERROR: FAIL READ ADDR : %x
0065e476  ERASE PREV ASSIGNED ADDRESS: 0x%x
0065e498  LBA WR FAILED BLK ID :%d, Size : %d, ADDR: 0x%0x
0065e4ca  g_reset_counter: %d
0065e4e0  g_dyncfg_validity_flags: %llu
0065e4fe  DPCD202: 0x%02x, 0x%02x
0065e516  FaultIndex: %d
0065e525  NVM_LOG_COUNT: %d, ADDR: 0x%08x
0065e545  REG_SHARED_0 : 0x%x
0065e55a  BuildL2P    
0065e567  PANELUP    
0065e573  PnlSeqEnd   
0065e580  DDRRetExit  
0065e58d  DDRExitFail 
0065e59a  PnlSeqStart 
0065e5a7  ASSERT_SYSIRQ
0065e5b5  Stage: %d
0065e5c3  DispFWStart
0065e5d0  pu_seq_time: %llu
0065e5e2  ChipID: 0x%08x, DispFW Version: 0x%x, LC: 0x%x
0065e611  Failed to initialize MMU driver: 0x%x
0065e637  Lib Version - Scaler: 0x%08x, HDCP: 0x%08x Analog: 0x%08x
0065e671  DDR Status: 0x%08x
0065e684  flash erase_flash64k address: 0x%08x, size: 0x%08x
0065e6b8  flash erase_flash4k address: 0x%08x, size: 0x%08x
0065e6eb  SPI_Sector64KErase_FIFO0 Err
0065e708  SPI_SectorErase_FIFO0 Err
0065e722  erase_flash64k Err
0065e735  erase_flash4k Err
0065e747  Expected Size: %08x
0065e75c  RdBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0065e7b0  WrBsy0 Status: 0x%02x, 0x44000404: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0065e804  RdBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0065e858  WrBsy1 Status: 0x%02x, 0x44000408: 0x%08x, IntStatus: 0x%08x, IntStatusIRQ: 0x%08x
0065e8ac  Fail: mmu_enable_disable (1): 0x%x
0065e8cf  Skip loading dram_config
0065e8e8  SYS IRQ RD MASK NULL PTR
0065e901  Wet failed at dp out, wet value = 0x%x
0065e929  WET changes: 0x%08x, 0x%08x, 0x%08x
0065e94e  scaler fail, set to freerun: 0x44008074: 0x%08x
0065e97f  Wet failed at dp out, wet value = 0x%08x
0065e9a9  Attrib not stable, set to freerun-1
0065e9cd  Attrib not stable, set to freerun-3
0065e9f1  Attrib not stable, set to freerun-4
0065ea15  Scaler Started but not locked!
0065ea34  Attrib Not Stable, set to freerun-5
0065ea58  DP Cable: Plugged
0065ea6a  Scaler Locked
0065ea78  DP RX Config Done
0065ea8a  Scaler Error
0065ea97  restart mode condition hit
0065eab2  HPD Assert
0065eabe  tcon_time_us: %llu
0065ead1  scaler finish 0: %x
0065eae5  dpcd427: 0x%02x, dpcd4f1: 0x%02x
0065eb06  Set to Freerun, DP Attrib: Not Stable 0x440000B4 0x%08x
0065eb3e  Attrib: 0x%08x
0065eb60  bpp: 0x%08x
0065eb6c  Set SVCLK to %f MHz
0065eb80  SCL->SCL_REG_SCL_CTRL16.field.SCL_REG_43: 0x%02x
0065ebb2  SCL->SCL_REG_SCL_CTRL16.field.SCL_REG_44: 0x%02x
0065ebe4  Input total hwidth is not supported!
0065ec09  scaler_ddp_msa_not_matching
0065ec25  scaler_ddp_video_train_fail
0065ec41  BER error: %d
0065ec50  margin status error: 0x%02x
0065ec6d  Link rate error
0065ecb9  UV for idx: %d
0065ecc9  start_lut_slice %d : end_lut_slice %d
0065ecf0  final_start_lut_slice %d : final_end_lut_slice %d
0065ed23  illegal gain
0065ed31  Time off found to be %d, for given sample of %x and samples in LUT: %x, %x, %x
0065ed81  Sample: %d, 0x%x
0065ed93  pot gain: 0x%x
0065eda3  Readback ADC CFG register: 0x%x
0065edc4  RCDone     
0065edd0  RCStart    
0065eddc  Loading default RC Cal!
0065edf4  Aging: Trigger RC Self-Cal!
0065ee10  Updating RC Self-Cal to Journal!
0065ee31  fc_notify_power_on!
0065ee45  rc_single_shot error, cancel lut generation!
0065ee73  Initializing RC Timer...
0065ee8c  soc_timer_status: 0x0202
0065eea5  soc_timer_status: 0x0303
0065eebe  soc_off: %d, rc_off: %d
0065eed6  initial current_gain_setting: 0x%x timer_idx: %d
0065ef07  Check RC Aging
0065ef16  default_rc_lut_sha256_check: Fail
0065ef38  RcLutCfgFail
0065ef45  Read Values out of LUT boundaries
0065ef67  RcLutCfgPass
0065ef74  sampled: %x
0065ef80  initial: %x
0065ef8c  sim gain: %x
0065ef99  idx: %x
0065efa1  Wrote ADC CFG register: 0x%x, 0x%x
0065efc4  initial adc_arr cfg[0]: 0x%x cfg[1]: 0x%x
0065efee  adc gain: 0x%x
0065effd  Readback ADC CFG register: 0x%x
0065f01d  Init ADC CFG register: 0x%x
0065f039  Init POT register: 0x%x
0065f051  soc_timeoff_reg: 0x%08x
0065f084  data: 0x%04x
0065f091  BLS CPLD0  DeviceID:  0x%08X
0065f0af  BLS CPLD1  DeviceID:  0x%08X
0065f0cd  CPLD DeviceID:  0x%08X
0065f0e5  CPLD Set Config Addr to 0
0065f0ff  I2C WrRd: Failed
0065f110  I2C Wr: Failed
0065f11f  CPLD Erase Failed
0065f131  CPLD Enter Background Mode
0065f14c  CPLD Exit Config Mode
0065f162  CPLD Exit Program Mode
0065f179  CPLD Erase Done
0065f189  CPLD Program Done
0065f19b  CPLD Erase Not Done
0065f1af  CPLD Reset Config
0065f1c4  CPLD Erase Start
0065f1d5  CPLD ProgDone Timedout
0065f1ec  CPLD Erase Timedout
0065f200  CPLD Program Timedout
0065f216  CPLD Busy Timeout
0065f228  Erase Status 0x%08x
0065f23c  DBCalEnd    
0065f249  DBCalStart  
0065f256  DB_NVM_CAL_End, Result: %d
0065f271  DB_NVM_CAL_Start
0065f282  DB_NVM_Status: 0x%02x
0065f298  Bufaddr: 0x%08x
0065f2aa  g_tcon_dram_address: 0x%08x
0065f2c8  g_mem_address: 0x%08x
0065f2e1  ipc_status: 0x%02x 
0065f2f6  ipc_result: 0x%08x 
0065f30a  manage_factory_cal cm ind last slice,[%d 0x%x]
0065f33a  manage_factory_cal psf volatile last slice,[%d 0x%x]
0065f370  manage_factory_cal cm dep volatile last slice,[%d 0x%x]
0065f3a9  manage_factory_cal psf last slice,[%d 0x%x]
0065f3d6  slot: %d, id: %d
0065f3e8  flash address: 0x%08x, size: 0x%08x
0065f40d  64k_block#:%d size: 0x%08x
0065f429  flash address: 0x%08x
0065f440  dram address: 0x%08x
0065f456  Options -> Error Checking Standard: CRC32
0065f480  Header Version: %d.%d
0065f496  Options -> Enable Integrity Check: No
0065f4bc  Options -> Enable Integrity Check: Yes
0065f4e3  LUT allocated Size: %d bytes
0065f500  LUT actual Size: %d bytes
0065f51a  Consumers: 0x%02x
0065f52c  Header ID: 0x%04x
0065f53e  LUT id: 0x%04x
0065f54d  GetInfo UsrAddr: 0x%04x: 0x%08x
0065f56d  SetInfo UsrAddr: 0x%04x: 0x%08x
0065f58d  data: %x
0065f596  dram_addr: 0x%08x
0065f5a8  API MNG INVLD SYSIRQ BUF SIZE :%d
0065f5cb  TLV: 0x%04x, size: 0x%08x
0065f5e5  g_flash_address: 0x%08x
0065f5fd  NVM_W_ADDR:  0x%08x, size: %d
0065f61b  TCON_UARP_SuperBinaryOffered(): numPayloads: %d, superbinary version: %d.%d.%d.%d
0065f66d  TCON_UARP_PayloadDataComplete2 payloadIndex: 0x%04x
0065f6a1  NVM_W_ADDR:  0x%08x
0065f701  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
0065fa00  ,0PDRZ
0065fb81  #PD(FPD$
0065fc7f  btfwb 
0065fccc  rm0JNT$pldR/
0065fcf4  <%pcdcJ3
007a191b  fJF)F F&`NF
007a2574  %HxDT8
007a258c  !HxDT8
007a26bc  ahi`!h
007a274f  `+F2FIF8F
007a2964  pGpGpGpG8
007a2b14  SIGRTRED: Redirect: can't open: 
007a2c24  SIGRTMEM: Out of heap memory
007a2c44  : Heap memory corrupted
007a2de4  [ERROR]:[AH FB] INVLD LKP VALUE :[%d] = %d
007a3154  [INFO]:FF : SKIP (%x)
007a316c  [INFO]:FF :%x
007a3268  [WARN]:BLBIST : ALRDY %d
007a3350  [ERROR]:BLBIST: INVALID CUR %d, %d 
007a33dc  [INFO]:[BLPWR] LED PG LOW
007a33f8  [ERROR]:[BLPWR] PWR BRD DEINIT FAIL: %d
007a3460  [WARN]:[BLFW]] : BLSS DISABLED 
007a3554  [INFO]:BLCPWR:BLC READY : %d
007a3574  [ERROR]:BLCPWR:BLC NOT READY (FATAL) : %d
007a35a0  [ERROR]:BLCPWR:GET IO STATE TIMEOUT : %d
007a36b0  [ERROR]:[VLED PG] GET STATE FAIL : %d
007a36d8  [INFO]:[VLED PG] : VLED PG:%d T:%d
007a36fc  [ERROR]:[VLED PG] FAIL : TIMEOUT, BLSS SHUTDOWN
007a3934  [ERROR]:[BLAPI] ADC REG WRITE FAIL %d
007a395c  [ERROR]:[BLAPI] ADC REG READ FAIL %d
007a3984  [INFO]:[BLAPI] INVALID CMD (ADC RW) :%d
007a3a0b  #'+-26:>EIN
007a3ac0  [ERROR]:[BLAPI] AH DBG LOG : INVALID OPTION :%d
007a3af4  [INFO]:[BLAPI] UNKNOWN AH DEBUG CMD (BLU AH) :%d
007a3b84  [INFO]:[BLAPI] INVALID CMD (BIST ENABLE) :%d
007a3c10  [ERROR]:[BLAPI] BLU CAL INIT FAIL %d
007a3c38  [WARN]:[BLAPI] BLU CAL READ NOT SUPPORTED %d
007a3d38  [ERROR]:[BLAPI] BLU REG WRITE FAIL %d
007a3d60  [ERROR]:[BLAPI] BLU WR INVALID WR BUF
007a3d88  [ERROR]:[BLAPI] BLU REG READ FAIL %d
007a3deb  ?EKQW]ciou{{{~
007a3f64  [ERROR]:[BL SLPR] BLSLOPER NOT SUPPORTED in X2232
007a4074  [ERROR]:[BLAPI] DAC REG WRITE FAIL %d
007a409c  [ERROR]:[BLAPI] DAC REG READ FAIL %d
007a40c4  [INFO]:[BLAPI] INVALID CMD (DAC RW) :%d
007a4100  [INFO]:[BLAPI] RCVD UNSUPPORTED API %d
007a416c  [INFO]:[BLAPI] INVALID CMD (BLFW_API_GetConvOut) :%d
007a41a4  [ERROR]:[BLAPI] BLFW_API_GetConvOut INVALID BUF SIZE %d
007a4310  [INFO]:[BLAPI] INVALID CMD (AGING STATS) : %d
007a4340  [ERROR]:[BLAPI] LED AGING STATS INVALID BUF SIZE
007a4498  [BLFWAPI] SUCCESS %d, Size : %d
007a4604  [ERROR]:[API] BL BIST PTRN %d NOT SUPPORTED
007a4634  [INFO]:[BLAPI] INVALID CMD (SET BIST PATTRN ) :%d
007a46a8  [INFO]:[BLAPI] INVALID CMD (THRML STAT) :%d
007a46d8  [ERROR]:[BLAPI] THERMAL STATS INVALID BUF SIZE %d
007a4824  [ERROR]:[API] LUM IN BUF NULL
007a4844  [INFO]:[BLAPI] INVALID CMD (UPDATE LUM IN ) :%d
007a4878  [ERROR]:[API] LUM IN INVALID ZONES :%d
007a499c  [WARN]:[BLAPI] ZONE BRGT UNUSE ZONEID %d
007a49c8  [INFO]:[BLAPI] INVALID CMD (ZONE BRIGHTNESS) :%d
007a4b20  [ERROR]:UNIQUE ID IS READ ONLY CMD
007a4ccc  [INFO]:[BLU] UNIQ ID : 
007a4ce4  [INFO]:[BLU] UNIQ ID RD FAIL %d
007a4d08  [ERROR]:[BLU] EXIT USR TST MODE NOT ALLOWED , BL_EN : %d
007a4dec  [ERROR]:[DCS] COMM CHECK FAIL : %d
007a4ef2  @0(DNA
007a5028  DMA BUSY
007a5034  INVALID SIZE
007a5234  [ERROR]:BLSS_GetConvOut Loc Mismatch, xLoc: %d:%d, yLoc: %d:%d
007a5274  BLSS_GetConvOut: %llu, %d, %d
007a5304  [ERROR]:DRBL INIT FAIL
007a531c  [ERROR]:DRBL CFG FAIL
007a5334  [ERROR]:IPC INIT LOW QUEUE FAIL
007a5498  [ERROR]:[IPC] UNKNOWN IPC %d
007a54b8  [INFO]:[IPC] LUT ID: 0x%X, size : %d
007a54e0  [ERROR]:[HIPC] NOT SUPPORT: %X
007a5740  [ERROR]:[IPC] OPCODE %d NOT SUPPORTED:%d
007a576c  [INFO]:[IPC] LUT ID: 0x%X
007a5788  [ERROR]:[IPC] BLS LUT LOAD 0x%x FAILED:%d
007a5c38  [WARN]:[INIT] NO LPA : SKIP SML/LRG BRH
007a5c60  [WARN]:[INIT] NO LPA : SKIP BLU
007a5c80  [WARN]:[INIT] NO LPA : SKIP BLU CFG
007a5d8c  [ERROR]:[INIT] IOCFG INIT FAIL :: %d
007a5db4  [INFO]:[INIT] BL GPIO IOCFG INIT DONE
007a5ddc  [ERROR]:MAIN:BL I2C IOCFG INIT FAIL :: %d
007a5fac  [WARN]:[INIT] NO LPA CONNECTED, BL DISABLE
007a5fd8  [INFO]:TRINITY CONNECTED
007a5ff4  [INFO]:TRINITY DISCONNECTED
007a6010  [INFO]:LUMIN BUF : 0x%X
007a60ec  [ERROR]:[INIT]:UART INIT FAIL :: %d
007a6114  [INFO]:[INIT]: UART INIT DONE
007a6134  [ERROR]:BL GTIMER INST FAIL :: %d
007a6158  [INFO]:BL GTIMER INST DONE 
007a6234  [ERROR]:MSGQ 0 MSG SIZE
007a624c  [ERROR]:MSGQ NULL MSGS
007a6264  [ERROR]:MSGQ NULL
007a6398  MAPPER FAILED
007a63a8  [ERROR]:BLFW INIT FAILED
007a63c4  [INFO]:[BLFW] INIT DONE
007a63e0  [ERROR]:[INIT] BLK ID FAIL : %d 
007a6404  [INFO]:[INIT] BLK ID DONE : %d 
007a662c  Size :%x
007a6635   Source Address : %x
007a664a  , destination Address: %x
007a67ac  [WARN]:I2C INIT: RE INIT %d
007a67cc  [ERROR]:I2C INIT: INV SPEED %d
007a67ec  [ERROR]:I2C INIT: INV INTF %d
007a69f0  [ERROR]:[I2C] SEM NOT AVAIL(RD)
007a6bc0  [ERROR]:I2C WRITE: INV SIZE %d
007a6be0  [ERROR]:I2C WRITE: INV INTF %d
007a6c58  [ERROR]:I2C : ADC READ FAIL: %d
007a6d28  [ERROR]:I2C : DAC READ REG FAIL: %d
007a6e14  [ERROR]:Failed to powetdown DAC : %d
007a7088  DAC BUSY :%x
007a7098  [ERROR]:DAC : INIT I2C WRT FAIL : %d
007a70c0  [ERROR]:I2C : ADC INIT WRT FAIL: %d
007a70e8  [ERROR]:MAIN: BL PWR BRD INIT FAIL :: %d
007a71b0  [ERROR]:I2C : SLG READ REG FAIL: %d
007a71fa  *aAhjiG
007a7490  [API] THRML STAT FAIL 
007a74e4  [INFO]:[KNEEPOINT] 1 ENTRY INIT
007a78e0  Overriding LAS values
007a78f8  LAS_LAC_IDs: %d, %d, ProcTime(min,max): %d, %d, CRC32: 0x%x
007a7965   pGLAS Override Copy Done 
007a7adc  [INFO]:[AGING]: Valid: %d, CRC32: 0x%x
007a7c8c  [ERROR]:[LEDAGING] : T LUT HEADER %X
007a7cb4  [ERROR]:[LEDAGING] :  C LUT HEADER %X
007a7cdc  [ERROR]:LEDAGING: STATS DIS 
007a7d98  [ERROR]:[PRFGAIN] LUT LOAD FAIL : %d
007a7ed4  [ERROR]:[PWMGAIN]: CUR ALRDY ENABLED
007a8034  [INFO]:[GAIN] : LOADING LUT
007a8050  [ERROR]:[GAIN] : PENDING LUT LOAD
007a8074  [ERROR]:[GAIN] : DMA INIT FAILED
007a8208  [ERROR]:[PWMOFFSET] :: CAL LUT HEADER FAIL
007a8234  [ERROR]:[PWMOFFSET] LUT LOAD FAIL : %d
007a8424  [ERROR]:PWRLMT: LOAD LUT FAIL : %d
007a84f0  [ERROR]:[ROWSTGR] : LOAD LUT FAIL :%d
007a8700  [ERROR]:SLPR: FAIL TEMP LUT %d
007a8720  [ERROR]:SLPR: FAIL RATIOS LUT %d
007a8787  pbFtF4
007a87b4  [ERROR]:[SLPR VT] INVALID PARAM IN MAPPING
007a87e0  [ERROR]:[SLPR VT] REMAP NOT AVAIL
007a8868  [ERROR]:[SLPR] TEMP INVALD PARAM
007a8a30  [INFO]:[THERMAL_STATS] :: DIS
007a8bb4  [ERROR]:[X-TALK] : ELEC MAP HEADER %X
007a8bdc  [ERROR]:[X-TALK] ELEC MAP LUT LOAD FAIL : %d
007a8c69  bK HbB
007a8db2  )F"FcF
007a8dcc  [ERROR]:BLU CfgVal RegRead (%d, %d) FAIL: %d
007a954c  [ERROR]:PWRBRD : DAC UPDATE FAIL %d
007a9570  [ERROR]:PWRBRD : DAC TRIGGER FAIL %d
007a9824  BLU Cfg Validation Fail: 0x%x
007a9844  BLU Cfg Validation Success: %llu ns
007a9b58  [ERROR]:[DCS]%d : POLL OVFLOW : %d
007a9b7c  [ERROR]:[DCS]%d : POLL SPILL : %d
007a9ba0  [ERROR]:[DCS]%d : POLL TOUT : %d
007a9d98  SHARE:%p
007a9da4  [INFO]:BLU CFG SZ(DRAM) : %d
007a9dc4  [ERROR]:BLU INIT FAIL : CFG %d : %d
007a9dec  [INFO]:[BLU] DRV STRNGTH VER PASS
007a9fb8  [ERROR]:BLU INIT FAIL : IDENTIFY PACKET
007a9fe0  [ERROR]:[BLU] :: INIT DRV STRNTH FAIL : %d
007aa0b4  #*1;EOY
007aa180  [INFO]:DCS : INIT  %d :  %d 
007aa1a0  [WARN]:DCS : INIT POLLIN INVALD INTF: %d
007aa1cc  [ERROR]:DCS : INIT FAIL %d
007aa404  [ERROR]:Failed to IO Config DCS interface:%d
007aa5d0  [ERROR]:Invalid DCS interface (%d) received TH Timer init
007aa724  [ERROR]:[DCS] : LARGE BRANCH READ FAIL: %d, %d
007aa754  Large Branch LUT Validation Success: %llu ns
007aa84c  [INFO]:BLU CAL CFG SZ(DRAM) : %d
007aa870  [ERROR]:BLU CAL INIT FAIL : CFG %d : %d
007aa89c  [ERROR]:[DSC] CAL INVALID PARAM %d
007aa9f4  [ERROR]:[LRG BRNCH] :: CAL LUT HEADER FAIL
007aaa20  [ERROR]:[LRG BRNCH]: REG WRITE FAIL INTF %d, BLU %d
007aaa58  [INFO]:[BLU] LRG BRNC DONE
007aaba8  [ERROR]:[SMLBRNCH] :: CAL LUT HEADER FAIL
007aabd4  [ERROR]:[SML BRNCH]: REG WRITE FAIL INTF %d, BLU %d
007aac0c  [INFO]:[BLU] SMALL BRNC DONE
007aae84  [ERROR]:%d, %d
007aae94  [ERROR]:READ CAL: Failed to read data, %d
007aaec0  [ERROR]:[DCS] CAL RD SUP 4 byte only, %d
007aaeec  [ERROR]:READ CAL: Null Pointer
007ab034  [ERROR]:READ REG: Failed to read data, %d
007ab060  [ERROR]:[DCS] REG RD SUP %d byte only, %d
007ab08c  [ERROR]:READ REG: Invalid input param
007ab1f8  [ERROR]:[DCS] SEND DONE FAIL: %d 
007ab21c  [ERROR]:[DCS] SEND BYTE FAIL : %d
007ab2ec  [ERROR]:Failed to send INQuiry packet, %d
007ab318  [ERROR]:INQ: CRC not matching  (exp) %02X != %02X (rec)
007ab654  [ERROR]:[DCS] SR START CLR FAIL %d = 0x%X
007ab680  [ERROR]:[DCS] SR START DONE FAIL %d
007ab6a8  [WARN]:[DCS] ::RFIFO UFLOW : INTF %d
007ab804  [ERROR]:[DCS] : SML BRANCH READ FAIL: %d, %d
007ab834  [ERROR]:[DCS] : SML BRANCH VER FAIL: %d, %d
007ab994  [ERROR]:Invalid DCS interface (%d) received WR packet
007ab9cc  [ERROR]:REG WRITE: Invalid BLU ID:%d
007ab9f4  [ERROR]:REG WRITE: Null Pointer data
007ac12b  eAm4"b
007ac177  #5GYk}
007ac308  [ERROR]:DCS IO cfg should never reach here:%d
007ac338  [ERROR]:INVALID DCS Interface to configure IO, %d
007ac418  [ERROR]:IOCFG: I2C : %d
007ac490  LED Aging Disabled or Shutdown Received
007ac500  aRef: %f, beta: %f, ipcThr: %llu, compThr: %llu, mask: 0x%x
007ac7a0  [ERROR]:[THRML STAT] BUF OVFLOW
007ac884  [ERROR]:[ZMAP] : LUT HEADER FAIL%X
007ac8a8  [ERROR]:[ZMAP] LUT LOAD FAIL : %d
007acd10  [ERROR]:%s: DMA_TO_MEM0_DC_ERROR FAIL
007acd38  [ERROR]:%s: DMA_FRM_MEM0_DC_ERROR FAIL
007acdb8  [INFO]:[DMA]PWM GAIN LUT LOADED
007acdd8  [ERROR]:%s: DMA_TO_MEM1_DC_ERROR FAIL
007ace00  [ERROR]:%s: DMA_FRM_MEM1_DC_ERROR FAIL
007acec8  CH1 CONFIG FAIL
007ad56e  0a[FATAL][IPC] : INVLD MCU ID : %d
007ad870  [ERROR]:[MAIN] PRE INIT FAIL:%d
007ad894  [INFO]:[MAIN] PRE INIT COMPLETE
007ad8b8  [ERROR]:INIT TASK FAIL
007ad8d0  [ERROR]:[MAIN] :: BLSS FAILED
007ad97b  `pGH`pG
007ade5f  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
007af408  pG0123456789ABCDEF@0X
007af41e  0123456789abcdef@0x
007af6de  @D:STDERR
007af6e8  :STDIN
007af6ef  :STDOUT
007af7ac  [INFO]:Boot Time Policy RegVal: 0x%x 
007af7d3  [MAIN] : FW %d.%d.%d.%d[%d]
007af7f0  [INFO]:HEALTH SIZE : 0x%x, %llu
007af811  [INFO]:BL BOOT Time : %llu
007af82d  [INFO]:INIT TASK COMPLETED
007af848  [WARN]:BLSS LUMIN BUF : 0x%X
007af866  [ERROR]:MAIN: PWR BRD DAC IOCFG FAIL :: %d
007af892  [ERROR]:[INIT]: DMA INIT FAIL :: %d
007af8b7  [ERROR]:MAIN: PWR BRD DAC I2C INIT FAIL :: %d
007af8e6  [ERROR]:MAIN: PWR BRD ADC I2C INIT FAIL :: %d
007af915  [ERROR]:[INIT]: IPC INIT FAIL :: %d
007af93a  [ERROR]:MAIN: BL BLIF INIT FAIL :: %d
007af961  [ERROR]:[INIT]: MMU INIT FAIL :: %d
007af986  [ERROR]:[INIT] LUM BUF NOT READ : %u
007af9ac  [ERROR]:MAIN:BL STATIC LUTS NOT AVAIL ::
007af9d5  [ERROR]:[INIT] BL PWR BRD FAILED
007af9f6  [INFO]:[INIT]: DMA INIT DONE
007afa13  [INFO]:[INIT]: IPC INIT DONE
007afa30  [INFO]:MAIN: BL BLIF INIT DONE
007afa4f  [INFO]:[INIT]: MMU INIT DONE
007afa6c  [INIT] CAL LUT PUSH Q FAIL
007afa87  [ERROR]:[INIT] BL PWR BRD INIT FAIL
007afaab  [INIT] CAL LUT PUSHED TO Q
007afac6  [ERROR]:I2C : DAC WRT FAIL: %d
007afae6  [ERROR]:I2C : ADC WRT FAIL: %d
007afb06  DAC STATUS :%x
007afb16  [ERROR]:MAIN:BL CDPWR_EN  FAIL == 0 
007afb3b  [INFO]:MAIN: BL PWR BRD INIT DONE
007afb5d  [ERROR]:[PWMGAIN] :: CAL LUT HEADER FAIL
007afb86  [ERROR]:[PWMGAIN] :: CAL LUT NOT AVAIL : MMU FAIL
007afbb8  [ERROR]:[AH] : COEFF LUT HEADER FAIL%X
007afbe0  [ERROR]:[AH] : Z2G LUT HEADER FAIL%X
007afc06  [ERROR]:[AH] COEF LUT LOAD FAIL : %d
007afc2c  [ERROR]:[AH] Z2G LUT LOAD FAIL : %d
007afc51  [ERROR]:[LUMPROFILE] : LUT HEADER %X
007afc77  [ERROR]:[SLPR] : TEMP LUT HEADER %X
007afc9c  [ERROR]:[SLOPER] TEMP LUT LOAD FAIL : %d
007afcc6  [ERROR]:[SLOPER] LUT LOAD FAIL : %d
007afceb  [ERROR]:[ROWSTGR] :  LUT HEADER FAIL %X
007afd14  [ERROR]:[ROWSTGR] LUT LOAD FAIL : %d
007afd3a  [ERROR]:[PLIMIT] LUT LOAD FAIL ID:%p
007afd60  [ERROR]:[PWRLMTR] : PR LIMIT LUT HEADER %d  %X
007afd8f  [INFO]:[IPC] BLS LUT 0x%x LOAD DONE
007afdb4  [ERROR]:IPC LMSG HDLR FAIL : %d
007afdd5  [ERROR]:[IPC] RD OPCODE %d FAILED:%d
007afdfb  [ERROR]:[IPC] WR OPCODE %d FAILED:%d
007afe21  [ERROR]:[IPC] BLS 2DT %d FAILED:%d
007afe45  [INFO]:IPC LMSG HDLR DONE : %u
007afe65  [ERROR]:[MCU STATUS] FAIL TO GET ADDR 
007afe8c  [ERROR]:[IPC] UNSUPRTD LUT ID : 0x%X
007afeb1   or ADDR : 0x%X
007afec1  dma_ch0_cb
007afecc  dma_ch1_cb
007afed7  [ERROR]:WDOG :: FAIL EARLY
007afef2  [ERROR]:[API] INVLD CMD : %X
007aff10  [ERROR]:[BLFWAPI] FAIL %d, RET : %d
007aff35  [ERROR]:[BLAPI] ZONE BRGT INVALID ZONE ID %d
007aff63  [ERROR]:[BLAPI] LUM IN INVALID BUF ID %d
007aff8d  [ERROR]:[BLAPI] ZONE BRGT INVALID BUF ID %d
007affba  [ERROR]:[BLAPI] DAC REG WRITE/READ INVALID BUF SIZE %d
007afff2  [ERROR]:[BLAPI] ADC REG WRITE/READ INVALID BUF SIZE %d
007b002a  [ERROR]:[BLAPI] BLU REG WRITE/READ INVALID BUF SIZE %d
007b0062  [ERROR]:[BLAPI] BIST ENABLE INVALID BUF SIZE %d
007b0093  [ERROR]:[BLAPI] LUM IN INVALID BUF SIZE %d
007b00bf  [ERROR]:[BLAPI] ZONE BRGTNESS INVALID BUF SIZE %d
007b00f2  [ERROR]:[BLAPI] AH DBG INVL DCS INTF %d
007b011b  [INFO]:[BLAPI] INVALID CMD (BLU AH) :%d
007b0144  [INFO]:[BLAPI] INVALID CMD (BLU RW) :%d
007b016d  [ERROR]:[BLFW API] INVALID BLOCK ID :%d
007b0196  [WARN]:READ REG: CRC not matching  (exp) %02X != %02X (rec)
007b01d3  [ERROR]:INQ: Invalid DCS interface (%d)
007b01fc  [ERROR]:[DCS] : LARGE BRANCH VER FAIL: %d, %d
007b022b  [ERROR]:REG WRITE: Invalid data size(%d) : %d
007b025a  [ERROR]:[BLU] RD UNIQ ID FAIL , INVALID DCS ID : %d
007b028f  [ERROR]:[BLU] RD UNIQUE FAIL , INVALID BLU ID : %d
007b02c3  [ERROR]:Invalid InterfaceID : %d
007b02e5  [ERROR]:[BLU] USR TST MODE NOT ALLOWED , BL_EN : %d
007b031a  [ERROR]:[BLU] RD UNIQUE NOT ALLOWED , BL_EN : %d
007b034c  [ERROR]:[DCS]%d : POLL CRC ERR : %d
007b0371  [INFO]:DCS : IDENTIFY :: %d
007b038e  [ERROR]:[ERROR] IGNORING DCSIF ID: %d
007b03b5  [WARN]:INVLD: DCS interface Poll Config: %d
007b03e2  [ERROR]:Failed to send identify Packet to interface:%d : Error: %d
007b0426  [ERROR]:Invalid dcs interface received Send Bytes: %d
007b045d  [WARN]:[DCS] ::RFIFO OVFL : INTF %d
007b0482  [WARN]:[DCS] :: CRC ERROR : INTF %d
007b04a7  [WARN]:[DCS] :: RD TIMEOUT : INTF %d
007b04cd  [ERROR]:REG WRITE: Failed to send packet , error:%d
007b0502  [ERROR]:Invalid DCS interface (%d) received
007b052f  Small Branch LUT Validation Success: %llu ns
007b055d  [ERROR]:[BLU] DRV STRNGTH FAIL :%d =  %x
007b0587  [ERROR]:[DCS]%d : BLU FAULT : 0x%x
007b05ab  [ERROR]:IPC_OPCODE_BLU_FAULT_INFO Triggered: %d ms, dcs_mask: 0x%x
007b05ef  [ERROR]:BLU CfgVal FAIL (%d, %d):  addr: 0x%x, actual: 0x%x, exp: 0x%x
007b063d  [ERROR]:Invalid input param(DCS: Send Receive Bytes)
007b0672  [ERROR]:[BLU] Reading UID FAIL
007b0691  [DCS]LRG BRCH CAL NOT AVAIL
007b06ad  [DCS]SML BRCH CAL NOT AVAIL
007b06c9  [ERROR]:READ CAL: Invalid input param
007b06ef  [ERROR]:READ REG: Null Pointer
007b070e  [ERROR]:I2C Read: INV SIZE %d
007b072d  [ERROR]:I2C Read: INV INTF %d
007b074c  [ERROR]:I2C READ: INVALID INTF , STATUS : %d 
007b077a  [ERROR]:[I2C] SEM NOT AVAIL(WR)
007b079a  [INFO]:FB: %X
007b1278  8?61$#*-pw~ylkbeHOFATSZ]
007b12e0  WPY^KLEBohafst}z
007b1310  ing`ur{|QV_XMJCD
007b1328  !&/(=:34NI@GRU\[vqx
007b133c  jmdc>907"%,+
007b1526  JDHqIDDqID@rID|
007b1536  JDPqIDLqIDDrID
007b154e  JD`qIDPrID
007d3793  fJF)F F&`NF
007d382c  *** assertion failed: 
007d3844  , file 
007d384c  , line 
007d441c  %HxDT8
007d4434  !HxDT8
007d4514  ahi`!h
007d46d0  SIGABRT: Abnormal termination
007d47d3   pGpGpGpG8
007d49f7  `+F2FIF8F
007d4aec  SIGRTRED: Redirect: can't open: 
007d4c20  SIGRTMEM: Out of heap memory
007d4c40  : Heap memory corrupted
007d5089  Hard Fault!: MCU
007d5f90  CC dma_transfer(%d) FAIL: %d
007d64c6  -AHhIi
007d65c6  -AHhIi
007d6724  WDOG Bite Error
007d67dc  System Exited: %d
007d807b  y'z!yfzby
007d82b7  y&z!yby
007d867c  Src: %d Dst: %d Opcode: 0x%02x, Prio: %d, Size: %d
007d86b0  SET_LIMIT 0x%06X 0x%X
007d86c8  Mismatched cookie from Cabal (0x%08X, local 0x%08X)
007d86fc  RR was zero
007d909e  PJHhPp
007d9ac5  D 0)FXEO
007db542  Wa_FcE
007db57a  Wb_FcE
007db5b2  Wc_FcE
007db760  dma_transfer(ROW CH1) FAIL: %d
007db780  dma_transfer(ALD CH0) FAIL: %d
007db882  -B|hSh
007db944   2L`JbM
007dbe00  NP Entry: %d Exit: %d
007dbe18  ERR : %s
007dbe24  IPC_NP_MSG_Q
007dc49a  xaxiQF 
007dc9b0  parse_ipc_opcode_mdata_msg FAIL: %d
007ddb2b  V~`nho
007ddd10  Unknown HP IPC from 0x%x
007de55b  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
007de971   pGa!O
007def14  0123456789ABCDEF@0X
007def28  0123456789abcdef@0x
007def4d  0123456789abcdefxp
007def60  0123456789ABCDEFXP
007df17d  [FATAL]: 
007df188  [INFO]: 
007df1b4  t2d_fwk_init FAIL: %d
007df1ca  bsp_init FAIL: %d
007df1dc  T2D BOOT DONE: Free Heap: %d, Free Stack: %d, Time (ns): %llu
007df21a  T2D-MCU Firmware, Version (Major, Minor, Release): %d.%d.%d, v0x%08x
007df25f  mcu_step_trace %d
007df271  IPC(%d, %d), IPC_API_RD_RESP
007df28f  IPC(%d, %d), IPC_GEN_RESP
007df2ab  [ERR]: 
007df2b3  Mismatched cookie from FCFW (0x%08X, local 0x%08X)
007df2e6  WRN: Unrecognized Block ID (0x%x)
007df308  WRN: Version mismatch for BID (0x%x)
007df32d  Warning: mean_p_photo_target is not zero but AA_target is zero, would divide by zero.
007df383  ../../../algos/trinity2d_utils.c
007df3a4  WRN: Destination for BID (0x%x) too small
007df3ce  !(numerator ^ denominator) || denominator
007df3f8  GET_LIMIT 0x%06X 0x%X %u
007df411  IPC_API_WR_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, BLOCK_ID(OP1): 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
007df479  IPC_API_RD_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, OP1: 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
007df4d7  IPC_API_WR_CMD: Cust Info: ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
007df513  IPC_OPCODE_API_RD_RESP: Status: 0x%x
007df538  IPC_OPCODE_GEN_RESP: Status: 0x%x
007df55a  IPC(%d -> %d): 0x%02x, size: 0x%04x
007df5d9  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
00835787  fJF)F F&`NF
00836698  %HxDT8
008366b0  !HxDT8
008367da  ahi`!h
00836a1b   pGpGpGpG8
00836c3f  `+F2FIF8F
00836d34  SIGRTRED: Redirect: can't open: 
00836e04  SIGRTMEM: Out of heap memory
00836e24  : Heap memory corrupted
00837081  [ERR]: 
0083708d  Hard Fault!: MCU
00837939  [ERR]: 
00837944  WDOG Bite Error
00837975  [ERR]: 
00837980  System Exited: %d
00837d9c  Failed to initialize UART driver: 0x%x
00837dc4  Failed to initialize WDOG driver: 0x%x
00837dec  Failed to initialize DMA driver: 0x%x
00838381  [FATAL]: 
00838bbc  waiting for first vblank end...
00838bdc  work loop start
00838bec  queue_pop FAIL, %d
00838cb0  stat processing queue init failed
00838cd4  ipc queue init failed
00838d58  new CE str: 0x%X
00838e93  PBibPA
00838f38  (F)FJF5`
00839199  y1Fbi+F
008392bc  cabal ipc handler opcode %x
008392d8  failed to setup debug api read response with error 0x%X
00839310  ipc data in dram!
00839324  unhandled ipc opcode: 0x%x
00839604  SYS TRACE FAILURE: %X.%u : size (%u) buff(%p) - TCON_ERR(%u)
00839644  system trace packet buffer is null
00839689  [INFO]: 
00839694  sys trace status set to: %u
008396ec  ?hEaEbEcEdEeEf
008397cd  P?hhahbhchdhehf
00839c28  get ltm data entries %u from %p
00839c48  get ltm output config cells(%u) bins(%u)
00839c74  unknown read api: 0x%x
00839e30  set ltm output row to %u
00839e4c  clear event trace buffer
00839e68  event trace enabled: %u
00839e80  unknown write api: 0x%x
00839fdc  <DAF F:F
0083a06d  FXFQFJFDD
0083a530  %s: DMA_TO_MEM0_DC_ERROR FAIL
0083a550  %s: DMA_FRM_MEM0_DC_ERROR FAIL
0083b550  Failed to initialize Frame Timing driver: 0x%x
0083b580  Failed to initialize HW STATS driver: 0x%x
0083b5ac  Failed to initialize 1 way dma driver: 0x%x
0083bd44  unexpected high priority IPC irq
0083bddc  unexpected low priority IPC irq
0083c0ac  AFRFKF
0083cb89  [ERR]: 
0083cb94  ERROR 0x%X @ %s
0083cba5  [INFO]: 
0083cbb0  no errors @ %s
0083cd21  [ERR]: 
0083cd2c  queue_pop FAIL, %d
0083cded  [INFO]: 
0083cdf8  SCENE INFO: cut %u fade in %u fade out %u
0083cf7d  [ERR]: 
0083cf88  ipc (%x) priority mismatch: %x v %x
0083cfad  [INFO]: 
0083cfb8  submit normal priority IPC %x
0083de31  [ERR]: 
0083de3c  set ipc ltm row index (%u) larger than max row index (%u)
0083e464  zr1`)hPCp`
0083e8bb  ~}|{zyxwvvutsrqqponnmllkjjihhgffeddccbaa``__^^]]\\[[ZZYYXXWWVVUUUTTSSRRRQQPPPOOONNMMMLLLKKKJJJIIIHHHGGGGFFFEEEDDDDCCCCBBBBAAA
0083f103  "SFXF!F
0083f194  "J!KPF
0083f1a5  J K0FAF
0083f234  5"0FaF
0083f511  F2FCF)F
0083f548  QJRK8FQF
0083f5fd  F*F3F8FQF
0083f744  BFSF(F1F
0083f7a6  *FXF!F
0083f7f3  "[F8FAF
0083f81b  "[F8FAF
00840672  pG0123456789ABCDEF@0X
00840688  0123456789abcdef@0x
0084070f  ?>UUUUU
00840748  0123456789abcdefxp
0084075b  0123456789ABCDEFXP
008419e4  boot error %d occurred at %dd
00841a04  [MSG]: 
00841a0d  [FATAL]: 
00841a17  RELEASE
00841a1f  ENGINEERING
00841a2b  fw initialize complete: Free Heap: %d, Free Stack: %d
00841a61  Cabal Firmware, Version: %d.%d.%d
00841a83  hw initialize complete
00841a9a  cabal %s build %d @ %s %s
00841ab5  [ERR]: 
00841abd  Failed to create Global Timer: TIMER_INST_0
00841ae9  Failed to create Local Timer: TIMER_INST_1
00841b14  Failed to initialize NMI: 0x%x
00841b33  Failed to initialize Doorbell driver: 0x%x
00841b5e  Failed to initialize HW Accelerator's driver: 0x%x
00841b91  CC: ltm_cc_theta_lut_size_in_words (%d) > CCLTHETALUT_CCL_THETA_LUT size (%d)
00841bdf  dma_ch0_cb
00841bea  ERROR! Division by 0!
00841c01  [INFO]: 
00841c0a  heartbeat (%.2fs)
00841c1c  HWA ltm cells per row and bins per cell is no longer what we expected
00841c62  hw stats config does not match post mcu hw block config - amb rows per frame: %u v. %u
00841cb9  algo config does not match hw stats config - amb rows per frame: %u v. %u
00841d03  algo config does not match hw stats config - sch rows per frame: %u v. %u
00841d4d  hw stats config does not match post mcu hw block config - cas rows per frame: %u v. %u
00841da4  hw stats config does not match post mcu hw block config - amb cells per row: %u v. %u
00841dfa  algo config does not match hw stats config - amb cells per row: %u v. %u
00841e43  algo config does not match hw stats config - sch cells per row: %u v. %u
00841e8c  hw stats config does not match post mcu hw block config - cas cells per row: %u v. %u
00841ee2  static cfg IPC data size (%u) does not match excpted size (%u)
00841f21  DUMPING SCH FRAME
00841f33  DUMPING AMB %i
00841f42  DUMPING SCH %i
00841f51  DUMPING CAS %i
00841f60  IPC static cfg read handler rsp size %i
00841f88  dumping amb global stats
00841fa1  amb global stat handler start
00842019  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
008435c4  Sep 24 2025
008977cf  fJF)F F&`NF
00898414  %HxDT8
0089842c  !HxDT8
008985de  ahi`!h
00898bac  pGpGpGpG8
00898df7  `+F2FIF8F
00898eec  SIGRTRED: Redirect: can't open: 
00898fbc  SIGRTMEM: Out of heap memory
00898fdc  : Heap memory corrupted
0089903c  Invalid Operation
00899050  Divide By Zero
00899060  Overflow
0089906c  Underflow
00899078  Inexact Result
00899088  SIGFPE: Arithmetic exception: 
00899a48  PLS VBE2VBE Fault
00899a5c  PLS INIT2INIT Fault
00899a88  NMI IRQ
00899fe8  DSC_ENC_ERR (%d): %llu, 0x%x
0089a008  FB_BUS_ACCESS_ERR: %d
0089a020  FB_OVERFLOW: %d
0089a030  FB_UNDERFLOW_ERR: %d
0089a048  FB_NO_ADDR_NODE: %d
0089a05c  FB Address Not Found
0089a1b0  Input Pipe MUX State Change Event Rcvd: %llu
0089a1e0  Panel Pipe MUX State Change Event Rcvd: %llu
0089a334  PR NFQ Push Fail
0089a35c   `%kfk
0089a4ec  INP: PFE Rcvd (%d): %llu
0089a508  Panel Pipe Partial Frame Event Rcvd: %llu
0089a534  CT Pipe Partial Frame Event Rcvd: %llu
0089ae2c  BSC_PSF0_UNDER_FLOW_INT_FC_STATUS: %llu
0089ae54  BSC_PSF1_UNDER_FLOW_INT_FC_STATUS: %llu
0089ae7c  BSC_PSF2_UNDER_FLOW_INT_FC_STATUS: %llu
0089b9ac  PP: DG_LUT_UPDATE_ERR_INT_FC_STATUS: %llu
0089b9d8  PP: DG_LUT_LOAD_ERR_INT_FC_STATUS: %llu
0089ba00  PP: VRR_DET_RRR_TIMEOUT_INT_FC_STATUS: %llu
0089be34  PC VID CH0 CRC Fail
0089be48  PC VID CH0 Overlap
0089be5c  PC VID CH0 SFOQ Push Fail
0089be78  PC VID CH1 CRC Fail
0089be8c  PC VID CH1 Overlap
0089bea0  PC VID CH1 SFOQ Push Fail
0089bf18  WDOG Bite Error
0089bf44  System Exited: %d
0089c9c0  PC CFH CH%d, Error: 0x%x
0089cf40  CTP Desciptor Prep Fail: 0x%x
0089d280  PLA EG LUT GEN: Invalid Gamma
0089da94  Invalid DMA0 Trfr Parameters
0089db18  %s: DMA_TO_MEM0_DC_ERROR FAIL
0089db38  %s: DMA_FRM_MEM0_DC_ERROR FAIL
0089dbbc  %s: DMA_TO_MEM1_DC_ERROR FAIL
0089dbdc  %s: DMA_FRM_MEM1_DC_ERROR FAIL
0089e7c7  cJkMc"
0089e831  cAkEc!
0089eb59  `JhM`@
0089ec93  F(FIF@
0089fd9c  LP IPC Queue Push Failed: %d
008a0710  FS Algo No OP ID
008a0724  Scheduled PT violates minimum end time requirement
008a0758  Unspported Input Event, %d
008a094c  rc_timer_status: 0x%x
008a0964  duration_of_final_frame: %u
008a0980  cav_at_pwr_off[0]: %f
008a0998  cav_at_pwr_off[1]: %f
008a09b0  cav_at_pwr_off[2]: %f
008a09c8  cav_at_pwr_off[3]: %f
008a0bd4  `DpD@DHDH
008a0c28  Min Setup Time is Greater than Default: %d
008a1431  F(F1FJF;F
008a1524  is_dp_src_connected: %d
008a153c  DynCfg Switch InProgress
008a1558  IPC(1, 0), SDP_BASED_DYN_CFG_SWITCH_REQ, pri: 0, ch_id: %d
008a1688  PSF0 CRC Error
008a1698  PSF1 CRC Error
008a16a8  PSF2 CRC Error
008a179d  [FATAL]: 
008a1840  FCFW Version: 0x%x, Build Date: 0x%x
008a1868  FCFW Fatal Err Enable Mask: 0x%x
008a1b1c  %s: FS_OPMODE_2BUFFER
008a1b34  P_Pipe
008a1b3c  CT_Pipe
008a1e86  &D1DYD)D
008a1f38  PSF Actual (%d) Prefetch Time Exceeds the Budget (%d)!
008a1fc0  WARNING: Ignore un-supported IPC cmd, dropping
008a253a  8FIF2F
008a292f  FAF*F;F
008a2dfc  Unexpected: Only PRF or NF Expected
008a2e20  InCorrect PowerON Data
008a2e38  First Frame Can't be Panel Replay Frame, Dropping PR event
008a2ec8  Invalid SF Obj, Drop Repeat Req
008a2f28  NR DeadLine Timer CbQ Push Fail
008a2f84  PC CFG CH (%d) ABORT or ERR: 0x%x
008a2fa8  PC CFG DC Fail
008a3074  CFG Ch Done Event CB: Q push fail: %d
008a3170  fs_fwk_pc_vid_ch_cb: Invalid arguments
008a3220  SWBIST BufQ Push Fail
008a3db6  8@)FJF
008a4084  FS in Recursive Loop
008a4480  Expecting PP Pipe Overlap, Cookie: 0x%x: %llu, %llu
008a44b4  PP Overlap Schedule
008a44c8  Unexpected vid_ch_active_access_cntr: %d
008a473c  SWBIST NF Obj Alloc Fail
008a4758  SWBIST NFQ Push Fail
008a4d98  REG_FW13_DISABLE_CABAL: Disable Cabal
008a4dc0  REG_FW13_DISABLE_TRINITY: Disable Trinity
008a4dec  REG_FW13_DISABLE_DITHER: Disable Dither
008a546a   xax*F
008a5550  WPC LUT Ver (%d) & ChipID (0x%x) Don't Match, Disable WPC Block
008a5590  WPC LUT Ver (%d) & ChipID (0x%x) Match
008a55b8  IP2 Cfg FAIL: 0x%x
008a585f  &0FAFRFKF
008a5874  SW BIST State: Not in ACTIVE state (%d)
008a589c  SWBIST Start: Expected: %llu, Actual: %llu
008a58c8  Default Frame for last one
008a5e7d  aph"j`
008a5e85  ""bhhbj`
008a5fcb  apj"j`
008a5fd3  ""bhjbj`
008a70c4  %FpEtF8
008a74ff  FPFIF"F;F
008a7521  FXFAFJF#F
008a7564  PFYFJF;F
008a75b3  F8FAF"F3F
008a75c3  FHFQF"F3F
008a75d5  FYF:F+F
008a7dc4  No NF after Preemptive Repeat
008a7ee4  Error in preparing P_PIPE descriptor cfg: 0x%x
008a8164  IPC(%d, %d), OPCODE: 0x%x, Size: %d, CH_ID: %d, Pri: %d
008a819c  Generic Response not supported for T2D, C2D & BL MCUs
008a87d4  Fail to allocate cfg channel
008a8868  %s: PC CFG (%d): IN_PROGRESS
008a8888  pc_cfg_utils_wait_dc_immediate
008a88a8  PC Cfg (%d) Load FAIL
008a8c98  #ybyYC
008a9038  pc_submit_cfg_descriptor: Cfg Ch BUSY or Not Allocated
008a91c4  PC VID RD CH SFOQ Push Fail
008a9760  Enable Frame Buffer: %llu
008aa0f0  qb(zqj`
008aac49  F@FIF:FSF
008aad0f  F F)FKF
008aad37  FPFYFBFKF
008aad7d  F(F9FRF[F
008aadf6  8F1FRF[F
008ab089  FHFYF*F3F
008ab0ce  2FSF5F
008ab10c  8FAFJF[F
008ab25f  F8F!FZF+F
008ab279  F FAFKF
008ab326  RFKFWF
008abf03  `hiji"
008ac340  Queue POP FAIL, %d
008ac505  x'y!xbx
008ac700  IPC_OPCODE_API_RD_RESP: Status: 0x%x
008ac74f  x/y)xjx
008ad48c  IPC_API_WR_CMD: Cust Info: ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
008ad4c8  CD EDR Override: 0x%x
008ad4e0  FCFW_API_BID_SET_ST_LOG_EN_FILTER: %d
008ad548  IPC_OPCODE_SDP_BASED_DYN_CFG_SWITCH_FAIL
008ada08  LUT_ID: 0x%x, SIZE: 0x%x, ADDR: 0x%x
008ada94  rx_ipc_handler_mcu_up_evt: MCU_ID: %d, Version: 0x%x
008adacc  BLU Fault Rcvd: 0%x
008adb3a  AF2FSF
008adb88  IPC_OPCODE_TCON_TO_FC_POWER_ON
008adc20  IPC(1, 0), fs_fwk_send_power_off_info, pri: 1, ch_id: %d
008adc9c  IPC_OPCODE_START_LUMIN_BUF_UPDATE
008adce8  IPC_OPCODE_STOP_LUMIN_BUF_UPDATE
008adec8  IPC_VT_DATA: 0x%x, PRC: %d, PrimCal: %d
008ae12c  Invalid CFG CH IDX, Skipping Pipe Scheduling
008ae15c  Unexpected output frame duration, 0x%p
008ae184  Pipe Cfg Q is busy, cfg_ch_idx: %d, Q-depth: %d
008ae7ec  WARNING: counter has overflowed, more than 16,777,215 cycles
008aea3b  F@FIF"F+F
008aea82   F)FRF[F
008aeac3  F8FAFRF#F
008aebb7  F0F9F"FKF
008b1468  0123456789ABCDEF@0X
008b147c  0123456789abcdef@0x
008b14a1  0123456789abcdefxp
008b14b4  0123456789ABCDEFXP
008b1791  [INFO]: 
008b179b  [ERR]: 
008b17a3  FCFW: Entering WorkLoop: FS_OPMODE_PASS_THROUGH
008b17d3  FCFW: Entering WorkLoop: FS_OPMODE_2BUFFER
008b17fe  Static Cfg Loading Time (us): %d
008b181f  fs_fwk_static_cfg FAIL: %d
008b183a  bsp_init FAIL: %d
008b184c  FCFW Boot Fail
008b185b  FCFW BOOT DONE: Free Heap: %d, Free Stack: %d, Boot Time: %d hticks
008b189f  FCFW Boot Success: %llu
008b18b7  SysTick Cntr Overflow
008b18cd  FC FW: Waiting for Static Cfg Availability in DRAM!: 0x%llx
008b1909  FCFW: Invalid Header @ Static Cfg LUT: 0x%llx
008b1937  FC FW: Waiting for Power ON API from TCON FW0x%llx
008b196b  Hard Fault!: MCU
008b197c  Default_Handler_wrapper
008b1995  Stack Free: %d bytes
008b19ab  Heap Free: %d bytes
008b1a09  Faulting PC: 0x%08x
008b1a1e  BFAR: 0x%08x
008b1a2c  MMFAR: 0x%08x
008b1a47  AFSR: 0x%08x
008b1a55  CFSR: 0x%08x
008b1a63  HFSR: 0x%08x
008b1a71  PSR: 0x%08x
008b1a7d  psf0_delay %d, psf1_delay %d, psf2_delay: %d, psf2_delay_1: %d, 
008b1abe  Unsupported PID, %d 
008b1ad3  CA exceeds limits!
008b1ae6  WARNING: FCFW_API_BID_HM_FRAME_SCHD, Payload Size MisMatch (%d, %d)
008b1b2a  REG_FW13_DISABLE_PANEL_PIPE: Disable Panel Pipe Blocks (Except Dither)
008b1b71  CTP: Cookie mis-match (0x%x, 0x%x)
008b1b94  TCON_CMN_LUT_ID_DYN_CFG_UUID: InCorrect Size: Rcvd: %d, Atleast Needed: 4
008b1bde  PC VID CH2 NFO ALLOC FAIL
008b1bf8  DMA1 Error: %d, TRFR FAIL
008b1c12  DMA CH0: WPC 2DT LUM LOSS LUT Load FAIL
008b1c3a  ca/[%0.4f], pt/[%lld]
008b1c50  dma_ch0_cb
008b1c5b  dma_ch1_cb
008b1c66  FCFW_API_BID_PIPELINE_BLOCK_DISABLE: BID - 0x%x, is_disable - %d
008b1ca7  NF Ticks: 0x%llx, is_pr_frame: %d, host_fid: 0x%x, hw_fid: 0x%x, src: %d
008b1cf0  FCMCU_LUT_ID_PIPELINE_DYN_CFG: InCorrect Size: Rcvd: %d, Needed: %d
008b1d34  TCON_CMN_LUT_ID_FW_DYN_CFG: InCorrect Size: Rcvd: %d, Needed: %d
008b1d75  TCON_LUT_ID_CM_DEP_CALIB_INFO_POSTCAL: InCorrect Size: Rcvd: %d, Needed: %d
008b1dc1  CMD_CALIB_SWITCH: ltlrr: 0x%x, utlrr: 0x%x, lturr: 0x%x, uturr: 0x%x, idx: %d, size: %d
008b1e19  Dropping Natural Frame during DynCfg Switch: %d
008b1e49  IPC (%d -> %d): GEN_RSP: Status: 0x%x, CH_ID: %d, Pri: %d
008b1e83  P_PIPE Process: schd_obj Q push fail: %d
008b1eac  CT_PIPE Process: schd_obj Q push fail: %d
008b1ed6  cam_hle_adm: %d
008b1ee6  elapsed_time_since_last_pwr_off_s: %d
008b1f0c  fs_fwk_sw_bist_init: Q push fail: %d, limits the number of free sequences: %d
008b1f5a  fcfw_pipeline_algo_feature_disable_mask_t: %d
008b1f88  GBLS Output: 0, GBLS Input: %d
008b1fa7  FCFW_API_BID_FS_INP_PIPE_CTRL: is_disable: %d @ %d
008b1fda  %s (LM: %d, FT: %d, is_rgb: %d, P: %d, fH: %d, opID: %d): FW_COOKIE: 0x%x, Vid START: %llu ns, LTM Rd: %d, LED Rd: %d, EOTF: %d, RR: %3.2f, 0x%p, BL: %d,%d, CE: %d,%d
008b2081  SBSeq ID: %d, DataQ Push Failed
008b20a1  REG_FW13_DISABLE_FRAME_REPEAT: Disable Frame Repeat Mode
008b20da  fs_fwk_set_curr_op_mode
008b20f2  Invalid NF Obj Handle
008b2108  No Natural Frame to Schedule
008b2125  UnSupported FrameType
008b213b  WDOG Bite
008b2145  worst_case_residual_ca_level_at_last_power_off: %f
008b2178  SBSeq ID: %d, Q-OVERFLOW, Dropping
008b219b  Waiting for PC VID CH2 MUX Switch
008b21bd  SF Obj Alloc Fail
008b21cf  PC VID CH2 NFQ Push Fail
008b21e8  PC VID CH0 Done SFOQ Push Fail
008b2207  PC VID CH1 Done SFOQ Push Fail
008b2226  REG_FW13_P1BU_POLICY: Use 3:1 FB DSC Compression
008b2257  %s (LM: %d, FT: %d, is_rgb: %d, P: %d): FW_COOKIE: 0x%x, Vid START: %llu ns, LTM Wr: %d, LED Wr: %d, 0x%p
008b22c1  REG_FW13_DISABLE_GLOBAL_BL_SLOPER: Disable Global BL Sloper
008b22fd  Invalid DMA1 Trfr Parameters
008b231a  EOTF Change (%d, %d), GBLS Reset
008b233b  Drop New Repeat Frame Req as Old NRF is not consumed yet
008b2374  fs_fwk_natural_and_pr_frame_process_cb: Invalid CB Argument
008b23b0  BSC_ERR_RW_BUBBLE_FC_STATUS: %llu
008b23d2  BSC_PSF0_IN_UDF_FC_STATUS: %llu
008b23f2  BSC_PSF1_IN_UDF_FC_STATUS: %llu
008b2412  BSC_PSF2_IN_UDF_FC_STATUS: %llu
008b2432  BSC_PSF2_FIFO_UDF_FC_STATUS: %llu
008b2454  BSC_GLB_FIFO_UDF_FC_STATUS: %llu
008b2475  BSC_LED1_FIFO_OVF_FC_STATUS: %llu
008b2497  BSC_PSF2_FIFO_OVF_FC_STATUS: %llu
008b24b9  BSC_GLB_FIFO_OVF_FC_STATUS: %llu
008b24da  BSC_FW_TRIGGER_PSF0_MISS_FC_STATUS: %llu
008b2503  BSC_FW_TRIGGER_PSF1_MISS_FC_STATUS: %llu
008b252c  BSC_FW_TRIGGER_PSF2_MISS_FC_STATUS: %llu
008b2555  CTP: DG_LUT_LOAD_ERR_INT_FC_STATUS: %llu
008b257e  CTP: DG_LUT_UPDATE_ERR_INT_FC_STATUS: %llu
008b25a9  BSC_PSF0_WRS_BELOW_FC_STATUS: %llu
008b25cc  FC_VCOM_OVC_IRQ_STATUS: %llu
008b25e9  FC_OD_DE_BIG_IRQ_STATUS: %llu
008b2607  FC_OD_FRAME_BIG_IRQ_STATUS: %llu
008b2628  FC_OD_DE_SMALL_IRQ_STATUS: %llu
008b2648  FC_OD_FRAME_SMALL_IRQ_STATUS: %llu
008b266b  FC_OD_CRC_ERR_IRQ_STATUS: %llu
008b268a  FC_OD_WR_OF_ERR_IRQ_STATUS: %llu
008b26ab  FC_OD_RD_BUS_ERR_IRQ_STATUS: %llu
008b26cd  FC_OD_WR_BUS_ERR_IRQ_STATUS: %llu
008b26ef  FC_OVC_LINECOUNT_IRQ_STATUS: %llu
008b2711  CTP: VRR_DET_RRR_TIMEOUT_INT_STATUS: %llu
008b273b  Shorter Natural Frame! Dropping Next Frame: %d, CurrT: %llu, PrevT: %llu
008b2784  CT Pipe MUX State Change Event Rcvd: %llu
008b27ae  Un-supported BlockID: 0%x
008b27c8  FCFW_API_BID_SET_DG_SCALE_FAC: 0x%x, 0x%x
008b27f2  IPC_API_WR_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, BLOCK_ID(OP1): 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
008b285a  IPC_API_RD_CMD: API Info: CMD: 0x%x, SUBCMD: 0x%x, OP1: 0x%x, OP2: 0x%x, LSB: 0x%x, MSB: 0x%x
008b28b8  Using Static Cfg for LUT ID: 0x%x
008b28da  Using Independent Cal for LUT ID: 0x%x
008b2901  FCFW_API_BID_FS_CTRL_LATENCY_MODE: 0x%x
008b2929  CH0 CRC (%d):: ERR: 0x%x, 0x%x, Exp: 0x%x, 0x%x, SEC: 0x%x, COOKIE: 0x%x
008b2972  CH1 CRC (%d):: ERR: 0x%x, 0x%x, Exp: 0x%x, 0x%x, SEC: 0x%x, COOKIE: 0x%x
008b29bb  FCFW_API_BID_C2DFW_FEATURE_DISABLE: 0x%x
008b29e4  FCFW_API_BID_T2DFW_FEATURE_DISABLE: 0x%x
008b2a0d  ALS: 0x%x, BL LVL: 0x%x, WHITE LVL: 0x%x, CE: 0x%x, DIM: 0x%x, SLOPER: 0x%x, MASK: 0x%x
008b2a65  DMA CH0: PP DG MT0 Load FAIL: 0x%x
008b2a88  DMA CH0: CTP DG MT0 Load FAIL: 0x%x
008b2aac  DMA CH0: FW STATIC CFG Load FAIL: 0x%x
008b2ad3  DMA CH0: OVD LUT Load FAIL: 0x%x
008b2af4  IP2 CfgDone FAIL: 0x%x
008b2b0b  IP3 CfgDone FAIL: 0x%x
008b2b22  IP4 CfgDone FAIL: 0x%x
008b2b39  IP9 CfgDone FAIL: 0x%x
008b2b50  IP3 Cfg FAIL: 0x%x
008b2b63  IP4 Cfg FAIL: 0x%x
008b2b76  IP9 Cfg FAIL: 0x%x
008b2b89  dyn_cfg_switch_commit FAIL: 0x%x
008b2baa  FCFW_API_BID_FS_CTRL_PIPE_DISABLE: CTP: 0x%x, PP: 0x%x
008b2be1  BL Lvl: 0x%x, CE Fact: 0x%x, White Lvl: 0x%x, ALS Lux: 0x%x, Mask: 0x%x
008b2c29  %s, Error Status: 0x%x, GTicks: 0x%llx
008b2c89  @@@@@@@@@AAAAA@@@@@@@@@@@@@@@@@@
008b4d95  #PD(GPD$GPDxGPD
008b4da5  #PD0GPD,GPD|GPD
008b4dbd  CPD8GPD
008b4dc9  sPDHGPD
008b4dd1  GPD4GPD
008b4df1  GPDhGPD
008b4dfd  GPDlGPD
008b4e0d  GPD@#PD
008b4e15  GPD`GPD
008f103c  K(&#hPG
008f151f  01w@xSC
008f1c16  upmS\E4
008f26bf  c.BPLI
008f4157  ScI#O6
008f491b  JM>CnR
008f4aa4  ixKy)]
008f4ada  !_(Bhi
008f4c30  @UlX1*r9P
008f54e6  Z$0Yzh
008f56c3  q$yJfE4
008f5c27  08/jSr
008f626d  J1)KLE<"H
008f639d  X\5aQb0G
008f6fbd  LBL@NBLBL@NBLF
008f75dc  HLRrDs
008f76e5  VRD$p$&#
008f79a0  jhSa]'
008f7a41  H6RSe!6X
008f890b  pveQO6
008f8a12  192nBx
008f8ac5  Ikp1L9
008f99e5  ^"NFu,)
008f9b58  LhX9&-.%
008fa4df  |-&=bYQD
008fa736  %DhDSM
008fa99e  bYDSM*
008faf12  '#D1 BLBL@N
008fb032  d3h\FYl
008fb0f3  2zYDlR}&R
008fb485  ,:JLNryb
008fb672  i)eDNC
008fb77d  ZLJZX3
008fbd0c  LBLBLaF
008fbd21  LBLBhd$
008fcaea  pL@N@NBLBL
008fcd86  l6)`hLR#B
008fd9bf  SDp,0p84
008fe6c6  M10&`cDC<
008fe8ab  $JBC;p
008fe8e1  HI2ifJ
008fee5f  uY?KvW
00a003a5  FnGOH,I
00a0048f  y1ySyty
00a0049f  z-zJzfz
00a013a5  FnGOH,I
00a0148f  y1ySyty
00a0149f  z-zJzfz
00a0f073  l."pKPA
00a21073  l."pKPA
00ad5429  Apple Display
00ad56cb  Apple Display
00ad5c29  Apple Display
00ad5dcb  Apple Display
00aed013  hofmd{b
00af0688  T@pDUU
00af0698  \@pDJJ
00af06a0  `@pDVV
00af06b8  l@pDHH
00af0711  @pDUUUU
00af0721  @pDUUUU
00af08c8  tApDB`QQxApD
00af0a09  BpD    
00af0a11  BpD    
00af0e88  TDpDUU
```
