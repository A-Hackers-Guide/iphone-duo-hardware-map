# `Firmware/AppleLPM/AppleLPM.v68.release.im4p`

- File size: 1,925,273 bytes
- IM4P: Tag: IM4P  Type: alpm  Version: 1
- BuildManifest components that use it: `Ap,LowPowerMode`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         alpm
  Version:      1
  Data:         1.9 MB (1925248 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 1,925,248 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `RTKit: %s - Client: %s`
- `RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release`

## Strings (1,235) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000a49  wwwwwww
000035cc  qiqx "
0000403f  TOik8P
0000406f  TCin8Qiq8
00005f7c  aY,xHY)x
0000a7e8  h"Dyi&Dy
0000efa0  bbB9`J
00013b43  Th3EyH
00013feb  Thg@9H
000140b7  Thg@9H
00014f55  X`x+xkx
000207d7  Q_AIkA
00029e0b  yib@9*
0002a3c3  Thf@9h
00035bb8  RTKSTACK
00035d01  Qkkbal
00035fbf  -0123456789abcdef0123456789ABCDEF
0003606c  SPMIv02
00036090  RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release
000360cf  afklib
000360d6  afklib
000360dd  afklib
000360ea  afklib
000360f1  stk_fail
000360fa  [ALPM|AFK_client:%s] 
00036113  AppleLPM Main System Start
0003612f  TAGAKCFBII
0003613a  ROIFJPWMQO
00036145  RSQFGUUGIA
00036150  JPGNPABFXZ
0003615b  GKWJXVBSPA
00036166  BWFSZNBMFF
00036171  disp0-service
00036188  DCP TRUSTED
00036194  DCP2 TRUSTED
000361a1  DCP2 workloop
000361af  DCP workloop
000361bc  JFILNNFDSD
000361cb  System reboot to OS
000361e0  System shutdown to OFF
00036207  arabext
00036219  tamldec
0003623a  A8KALPLWOD
00036245  MNA)KIWHD1
00036250  CKAJS9jKAS
0003625b  KJAS81joau
00036266  ALNAUJAPK!
00036271  LA]JMZU*AH
0003627c  AKLW!!IAJN
00036287  LAM!@USNAQ
00036292  ZZAKWND*A!
0003629d  PLAO(AK@S)
000362a8  N7WBPMKXRF
000362b3  POB(LJVIG2
000362be  XMBLU8hMBT
000362c9  MLBT93kqcw
000362d4  BMOVCWBQL@
000362df  WB]KNBV*CI
000362ea  BWNX!!JBKP
000362f5  MBO!@VTODR
00036300  AACKXPF*C!
0003630b  QNBP(BM@U)
00036316  PNUXYTZZTS
00036321  UQQMCPKHDK
0003632c  ZPIAJKGAXA
00036337  BTRWNJDKXR
00036342  VHKNWLLVNM
0003634d  KOAAMFGOST
00036358  FFKFCPZZAT
00036363  Device Charging
00036374  Silent Check
00036389  invalid distance too far back
000363a7  invalid distance code
000363bd  invalid literal/length code
000363d9  incorrect header check
000363f0  unknown compression method
0003640b  invalid window size
0003641f  unknown header flags set
00036438  header crc mismatch
0003644c  invalid block type
0003645f  invalid stored block lengths
0003647c  too many length or distance symbols
000364a0  invalid code lengths set
000364b9  invalid bit length repeat
000364d3  invalid code -- missing end-of-block
000364f8  invalid literal/lengths set
00036514  invalid distances set
0003652a  incorrect data check
0003653f  incorrect length check
00036556  need dictionary
00036566  stream end
00036571  file error
0003657c  stream error
00036589  data error
00036594  insufficient memory
000365a8  buffer error
000365b5  incompatible version
000365ca  !MIDR: 0x%x
000365d6  ~CsPTR
000365dd  !ROf %#lx %#x
000365eb  MMU out of tables: %zu,%zu
00036606  MMU private: s:%llx!=%llx b:%llx!=%llx
0003662d  MMU VA sz %u 0=%zu 1=%zu
00036646  MMU private !fit: b:%lx<%lx s:%lx>%lx
0003666c  MMU gptbat !map: p=%zx, v=%lx, sz=%zu, st=%x
00036699  MMU uat_handoff !map: p=%zx, v=%lx, sz=%zu, st=%x
000366cb  MMU sh<ps: %llu > %llu
000366e2  Page Table !vm export: %x
000366fc  GPTBAT !vm export: %x
00036712  PPL handoff !vm export: %x
0003672d  MMU invalid page size: %x
00036747  !ASLRHeapAlign
00036756  <null>
00036760  ThIntr:%u,%u,%u,%u
00036773  ThLock:%p
0003677d  !Mthd:%p
00036786  set_framebuffer called with static framebuffer!
000367b6  mme:0x%x
000367bf  SPMI:%d (%d,%#X,%u)
000367d3  SPMI Fatal Error: %s Blocked
000367f0  Transfer
000367f9  HW Q Reset
00036804  Filter Modification
00036818  VmOv %d %d
00036823  !vm nodes
0003682d  Unbalanced transients
00036849  RTKit: %s - Client: %s
00036862  Crashlog for %s
00036873  Clog hdr len: %u<%lu
00036889  Clog hdr len %u>%lu
0003689e  Clog hdr sig %#x!=%#x
000368b5  Clog hdr ver %u!=%u
000368ca  Incomplete log, crashed during logging (%x)
000368f7  End header mismatch, possible corruption logSize=%zd %p %p
00036936  unknown exception %#0x
0003694d   - nested %s @ %#010llx
00036965   - nested unknown %#x @ %#010llx
00036986  Sig %#0x ver %#0x - %u > remaining %lu
000369ad  Section Sig %#0x ver %#0x %u<%lu
000369de  Unhandled SWI
000369ec  PREFETCH ABORT
000369fb  DATA ABORT
00036a06  SERROR
00036a0d  HARDFAULT
00036a1d  NMI FIQ
00036a25  AP-requested crash
00036a38  Non-fatal crashlog
00036a4b  Stack guard fault
00036a5d  Stack check fault
00036a6f  Mailbox error
00036a7d  Recoverable Panic
00036a8f  Force Reset
00036a9b  Unknown exception
00036aad  CXXnew:%zu
00036ab8  CXXnew[]:%zu
00036ac5  !Heapblk:%p
00036ad1  MBI queue overflow:%s
00036ae7  rtbuddy
00036aef  !xition: %x to SLEEP
00036b04  RTBM: %s failed msg: 0x%016llx (%x)
00036b28  RTBUDDY(%s): Watchdog error. Expected=%u, received=%u
00036b5e  RTB: %s syslog 0x%016llx (%x)
00036b8f  afk_messenger_init_acipc
00036ba8  handler_ready_acipc
00036bbc  options & IOPK_IOP_BEHAVIOR_ACIPC
00036bde  handler_ready_ack_acipc
00036bf6  handle_update_tx
00036c07  %s: updated wrptr:0x%x
00036c1e  handle_update_rx
00036c2f  %s: updated rdptr:0x%x
00036c46  afk_client_init
00036c56  AFK_CLIENT_MB_INITIATOR != type && AFK_CLIENT_MB_LISTENER != type
00036c98  NULL != client
00036ca7  afk_client_add_endpoint
00036cbf  NULL != ep
00036cca  kIOReturnSuccess == rv && NULL != ep->tp
00036cf3  %s: messenger_init error!
00036d0e  %s: EP Setup Timeout!
00036d25  afk_interface_init
00036d38  %s: IF Init Timeout!
00036d4e  NULL != cif
00036d5a  %s: afk_interface_init client %p '%s' (%i)
00036d86  afk_interface_send_command
00036da1  NULL != response
00036db2  handle_message
00036dc1  msg_len >= sizeof(*header)
00036ddc  %s: SeqNum:%i ifnum:%i len:%i
00036dfb  header->totalMsgSize == msg_len - sizeof(*header)
00036e2d  payloadLen >= sizeof(*intHdr)
00036e51  header->totalMsgSize == ep->split_message_len
00036e7f  ep->split_message_len - ep->split_message_offset >= payloadLen
00036ebe  header->totalMsgSize >= sizeof(InterfaceHeader)
00036eee  NULL != ep->split_message
00036f08  payloadLen >= sizeof(*ifHdr)
00036f25  handle_internal_message
00036f3d  %s: Unknown internal pktType received (%i)
00036f69  handle_client_message
00036f7f  %s: Unknown ifNum received:%i (%i %i, %lx)
00036fab  %s: pktCat:%i pktType:%i len:%i
00036fcc  %s: Received unknown message category %x
00036ff6  handle_internal_interface_message
00037018  %s: Received kIOPPacketTypePublishReport name:'%s' if:%x
00037052  %s: Received kAFKPacketType_OpenInterface
0003707d  %s: Unknown internal interface pktType received (%i)
000370b3  handle_command_message
000370ca  msg_len >= sizeof(*commHeader)
000370e9  !commHeader->oobHeader
00037100  NULL != handle
0003710f  handle_report_message
00037125  %s: handle_report_message cif:%p packetType:0x%x length:0x%x
00037163  handle_response_message
0003717b  NULL != cif->responses
00037192  NULL != response->next
000371a9  resp_len <= response->response_len
000371cc  state_cb
000371d5  %s: Error publishing interface
000371f5  send_packet
00037201  %s: Sending packet category: %d, type: 0x%x, len: %d seqnum: %d ifnum: %d
0003724c  %s: EP Paused
0003725b  create_interface
0003726c  NULL != interface
0003727e  afk_msgr_msg_send
00037290  kIOReturnSuccess == rv
000372a7  %s send cmd:%x arg:%llx state:%d msg:0x%llx
000372d3  afk_msgr_msg_recv_cb
000372e8  __builtin_bswap32(IOP_PACKET_MAGIC_V2) == magic
00037318  afk_msgr_ringbuffer_assume_subrange_cb
0003733f  total_offset >= static_offset
0003735d  afk_msgr_ringbuffer_release_subrange_cb
00037385  afk_msgr_ringbuffer_abort
000373a5  afk_msgr_after_ready_ack
000373be  kIOReturnSuccess == err
000373d6  messenger->config.rxQueueLen && messenger->config.txQueueLen
00037413  afk_msgr_handle_command
0003742b  %s: Message received for deinit'ed client
00037455  %s: afk_messenger_int not started (cmd %x)
00037480  %s recv state:%d cmd:0x%x
0003749a  %s: unexpected: msg=%016llx cmd: %x
000374be  afk_msgr_handle_here_buf_addr
000374dc  0 != messenger->remoteSize && 0 != remote_addr
0003750b  afk_msgr_handle_req_buf
00037523  messenger->config.allocator
0003753f  capacity
00037548  bufferLen >= capacity * AFK_TAGGED_BUFFER_SIZE_SCALE
0003757d  afk_msgr_handle_here_buf
00037596  NULL != (void*)remote_addr
000375b1  afk_msgr_enqueue
000375c2  %s: Transport not established (curr %x)
000375ea  kIOReturnBadArgument != rv
00037605  valid && size <= UINT32_MAX
00037621  kIOReturnSuccess == result
0003763c  perform_command
0003764c  messenger->state == handlers[i].startState
00037677  handler_ready
00037685  %s: AFK_PROTOCOLCMD_READY : protocol 0x%x options 0x%x
000376bc  afk_msgr_handle_ready_ack
000376d6  AFK_PROTOCOLCMD_READY_ACK : protocol 0x%x options 0x%x
0003770d  afk_messenger_init_standard
00037729  ASSERT %s:%d
00037737  NULL != mess
00037744  iop_ringbuffer.h
000377b5  e6kUU}
00037a5e  (&%aRfMJ
000388a5  7{YZea
0003896e  'raHC7
00039da0  *KliWBrW^$
0003a2b1  Xxlp[r
0003ae85  E29'8^fnoU
0003b1c5  %A}zrAG
0003b47a  `vcg155
0003b4ab  ;wfvfv
0003bb9c  fbG=(-I
0003bcb9  EaV'q~
0003c32c  ^dzjAFs
0003c336  sGo3SO
0003c420  ikPotaU
0003c578  kXy0S==
0003c9e6  ?*JHP9
0003ca9c  vCgt!Imc7
0003cbd4  `p8lXS,
0003d1ad  2u%dra
0003d407  E"ldHA
0003d882  3.@;VWaYD
0003d8e4  t)LEr#
0003d8eb  <lYD-uW
0003dc74  AsDh0I
0003de79  kjc$z*
0003e36f  -nbJ>L
0003e70f  },V~KHa'ozA
0003f2d7  XFk~,wT*
0003f76b  U-c-PBl
0003fe4a  lzok:t
0003ff0d  B'bMaG1
00040169  &xDeyo
00040291  1ACc:>3
000408f4  c^g~vygE
00040a85  i,fFCK
00040dc9  HImm )A
00041177  oKwGzl
00041358  _OLfsS
00041ad5  cJgC.l=
00041bae  LpS7Z5<
00042b11  7Wyh#]D
00043e74  xtiA@8r
00044652  3eR;}fUZ
000447bc  #/OmT9
000447c8  &ZqmW]a
000452c5  Q&nYa0
00045751  XbryEB
00045e0e  k+'[MBE
00045f7b  Rnoo8N
00046090  FPpDa+
000461d0  E/a1gQq?
00046415  H[#dRA
00046558  JHEu>lT
0004737e  f@ubaG
0004741a  OaKb#b
00047f38  bNuH H
00048465  lgVSqj
00048948  $joG@ONf
0004911f  WA2VZi
00049945  0*dK4\CnA
0004a3f7  !}6GSg
0004a6c2  &])qat1i
0004acfe  {6Yeb"T
0004b210  |\A)!Vk/3=uNq4
0004b73b  eWvR~7\
0004b854  F/gIhk
0004bc4a  ~KbnwoC
0004c171  E*4mXz
0004c2b1  X:tQC?
0004c32c  TiN@m9
0004d68f  VQEBc:>
0004dc8b  1[FHpo
0004df50  pC<iMMOS
0004e228  kXEw<<
0004e3de  *h NPa
0004e570  TX7NrgK
0004e63d  :AwRl_J
0004f127  +EZDS}B0
0004f2e0  \fZbjs
0004f866  4YZd=+g
0004f8dc  ?hTqZRP
0004fd2a  Q<TzEW&Mm+2#<o
00050569  LL##.sFn
000507d6  A_B ocD
0005102a  n'Ecy/Gy
00051588  sgggwV{
0005186b  B|cIt8
00051cb1  ,1iuv;
000524d2  anc241
00052f75  -eaVC>
0005339c  z}hVGb
000533ff  r:,DnS\>
00054420  .CkQB7
0005496a  RkOT68
0005568c  5FnZlM
00055ab9  IO!bGfN
0005604d  vB%\xWQ
0005670a  AwV*Os
000567d3  HlI?Kbk
00056a9b  QfE"S4
00056abc  9Gqx@B,
00056dfb  mLW/mL
00057ca5  M*YLZY
00058714  "l\bRQ)K
00058abf  IIuR.'
00058b67  1.wnE/hM
00058f65  yGS]!F|
000599a6  &uSi7i
00059f0b  o`dvUO
0005aaa3  Gz^qwv
0005b61b  ZvD1)R
0005b661  ItC/H8R
0005b794  DZi-0#4U
0005b925  !TyZhd
0005c235  M:xbbs
0005c3a7  ],*lxb
0005cb77  tGoAU8
0005cd7b  *OLeEo
0005d4a2  xqWm>I]D
0005d6f6  b-(jKF
0005e112  =cavd6`
0005e686  N&vbNq
0005f5e9  :eul-X+
0005f994  g&3eNw
0005f9cd  @q0DfoqQc\
00060588  TOukn0
0006102f  dWttqS<
000627f3  Y{lTWz
00062804  cc<f|mlcl
00062b55  FQf ._
00062c3d  "=7NrX
00062e08  CRo>v\
00063061  ;XxN3!
000634d7  2;KOIV
00063a19  iR@iyYoA
00063a6c  Y{BAdr
0006413d  8)SsXl
00064345  X7oRIz9Xn
000657e7  d~.[Dbt
00065af7  LlEq+s5}
00065c59  6GOfAVzO
00065cba  hexU-v
00065d27  k^`dka]
000664cb  ndbd=~
0006674d  krIj!V
00067cb5  %-Bnal
00067cf6  Jxe)U,K
00068314  *XxKVi-
000685ad  OJk76\!
00068bae  KWlk~s
00068eba  2DFK\I
0006900f  rxNSX2
0006926d  Hdjp#I
00069add  _2Tmem
00069f28  0dJ`aBLR
0006a217  IB}pPg
0006a674  k4tjL>
0006a69d  '4(KMey
0006a992  Zln`a8$X
0006adc1  !d8GqL
0006b004  *jx$?LwZ)
0006b04e  Bajk4!
0006b0f9  'jAfP\
0006c422  nzZlAT
0006c4b9  kXfAqa
0006c8c1  )$-7HwX
0006cbf7  7PkbCT
0006ce36  Mblvb:
0006d095  cvMM:^l}
0006d148  tfz0;2
0006d15e  =cbv`<Lk
0006d966  #mvP9|La
0006dc79  2&FOPa{
0006dd9d  E7#LiA=
0006dfa9  sQFVnM
0006e00d  qzJ-zvx
0006ec51  #IrSePe
0006f818  'Z7vfHGr
0006fea5  EJk[<vDL
0007018d  n3rvg}
000709b0  enPZcE.p
00071247  ,X*qbO
000715b6  "('FOXP
00071904  *Gac2MN
00071e23  NHzA7cH_
000722ad  6ULbl$
00072310  vJGi7!
00072d8d  "I2kJR]
000735c3  /k*xzB
00073f3a  wGxkC#
000741f1  "T_eKQ.W
0007436f  "PID8k
00074ff9  _eHv7%
0007508a  4/'SWl
00075475  oSs$ZcBu
000759ca  IIP61d
00075fe1  U]xUh9
00076006  LGS3Kvt
0007608c  mIXBdw
00076d0b  XcsXP@I
00076e27  l*3b<tTLO
00077c05  E+IySY
000785c3  `IJU-3
000786eb  VcEm=(i
000789f3  VPiJ1RY
00079799  CuTjhRA
00079d45  wHiKT^
0007a3c2  jiI'd8o
0007a56a  nobrv5
0007adbf  ;A2oQRn
0007b369  `\ob{cQoo
0007b961  hCMq_M@
0007bd20  cKO'R?l
0007c904  J\buc<
0007cc18  _zWb-%
0007d166  ^1rfn^
0007d693  IxX|ek
0007dc12  Cd;QzH4'q
0007dc2a  aPHW.A
0007dc76  $SmCSzx
0007dcbc  dG+MfrPZ
0007df63  "oQyN(h
0007e6c3  ESC|t&
0007ebda  Q7Gdbd+
0007f721  :KRN.KF
0007fb65  /ixhxK<
0007fdbe  edb>6q~
0007ffed  Q',gWc0
0008080e  BXk(hP
00081823  |+8\Dgn
00081a69  %Jeqfl
000820f4  kWPz)Coa=
000824e8  ?w)vqJ
000826dc  Z}lTWv
00082c54  fnPy7&Y
00083cbe  oUCC|:
00084170  jdr;(.
0008427d  E2xphx
00084722  r:E*wDD~U
00084b81  tOSCgwb
00085994  0@ PII
00085a57  &u1Yet
00085a5e  QYBk;b
00085adb  SYn=09&
0008602a  A*E@pQd
00086ee6  V>]ggk
00088144  FFO6r1
00088fd8  >S0AIj
0008a19c  3.yvW9
0008aa55  s4R(Pid
0008adff  kC'oUb
0008c015  S&lVVI
0008cd5b  'Avcw|
0008cd95  vcf)R+
0008d022  IVhhud
0008d2a5  ZDSF$h
0008d3b3  -7tEp=
0008d3f0  He<y<IIx
0008d5ec  k.LUtK
0008d651  2yIw@3
0008dbfe  hpN05K
0008dfa8  _xDIVT
0008e406  F#oimi9|
0008ee04  '_W}TsW
0008fb37  wCLZ0C
0008fc80  _,CzS`g
0009009c  Cywdi}*
000902aa  WsoYCF
00090b1e  )LxS`l
00090eb3  S9{zKKrZ
000914a8  8Y!eur
00091593  $r&xil
000916b1  gfggsXl
000916d2  7?Rdg 
00092493  8?fln`%5L\E)
00092b5a  q>IWo6
00092cab  -\Dbm2
000931f5  FLQG%3.
00093c07  j*5RWj
0009406f  OUx)|cg
0009422e  &)6Gab
00094492  .13NYK
000946a5  nto,Z'>
00094f5c  <P_(otn
00095130  %HHsO*v,
000953f3  d/UWsT
000954f1  kk7ReyG
000957d6  @CGFKqE
00095982  RwSRE.
00095dc9  OBbgS3`
0009612d  XXm#|+,R
00096613  Uknv$h
0009663d  gDE`fw
000966e5  ;l\bby*
00096893  ]Tqq%aJt0
000968bd  !^:S}2fRT
00096ca3  +luD<X
00096f1d  f.:mfn
0009701f  xc;@NqP=
0009743f  MLpvm$:TC
0009774a  QeC0GP
00097c6a  ;YoA]swOm
000980ed  ,5'9ZnCZf
00099256  MPa2xx
000994ea  :\0NwFn
00099b2d  *&8,ElL
00099f15  @<8EFS
0009abad  Q*bHcM
0009b3a0  !'J.Wtbr
0009c0a0  iQA>Q,
0009c525  v{uFUG
0009c707  k%Tca3|c
0009c8d1  3=0CRC
0009d107  qe@VTMwg
0009d7de  1VITzubW)U
0009efcd  MPuuJ@
0009fa32  gfv}fg67
0009fa61  oEDIVT
000a0039  8xbtGGz
000a0c24  .8JFq7
000a1316  /Rbb<{
000a159c  {ApX$\
000a1732  `eYDWz
000a17dd  obSUXaE
000a27be  CJl&K:
000a2c30  ePvq6m;Y
000a471e  WuA.EkS
000a4bad  ?gOijf
000a5a1e  lrvdH?
000a5cd1  _Zsss)
000a64a3  >PR8kCpY
000a6569  aJfAMU
000a6bf5  pNL,#c-
000a71a5  v%wSAo
000a81d3  bRD[2j}5F[
000a86b5  jni%Bhw
000a94d8  i<Pzi0
000a9a05  _w}uwu
000a9bb5  Y>Hoq&
000a9d2e  "g;XOi.
000a9f56  e3 npw
000aa79c  s\jDvt
000aa9e6  Yz-Jyfz
000aaa48  G(Isqv
000ab2fc  xzC8&TV
000ab47a  o;YOq9
000ab4d4  o=fhh-B
000ac097  oVA-.2
000ac2ed  =]EHp7
000acf36  O_zMvc$
000ad636  yMB+%s
000ad973  b7:^YIi
000adc15  2TJw+ =
000addb4  !cJG@>
000aebd0  vQ1YSys{
000aeff6  1?5pEnbG
000af6a0  Q7YE!ayNKVb
000af8eb  {5xBqV
000afb47  0?\Gyw
000b09d5  ,FKV~[
000b0b2d  iLI*x-r
000b0cf6  ]Y8xVdw}fx
000b16b5  TtRnnbH+
000b179d  pGzSRD
000b1a93  &Ash8K
000b1ba1  8sXI4v
000b1e3f  G6hgYL
000b26f6  5a4eFS
000b2c2d  fLH]&I
000b2d84  e!-Poh
000b32a1  MyHM>A
000b37e2  - #KPG
000b3f57  9HUpI)}
000b3fa5  V(oieWa
000b46e3  0kRPru
000b4a24  0oIh.2
000b4d7b  _FBldx
000b585c  pD[LsZ
000b58b4  |;>DyI
000b590e  xrogaK
000b5d02  \ego|I
000b62d6  C7kaHH
000b6390  djf=@s 
000b6477  r,ed`peb`h
000b6b45  Vxe7OF2
000b78d6  ybg-P,d#
000b817f  .354LRw
000b8517  7465onAY
000b8735  5R]hcE
000b892d  gWc;F)
000b894d  zVJ.ee
000b8db7  %QKhSi
000b94d6  MHSL#p
000b9b1b  HR kHZ@L#
000b9bd7  ($ RhBr
000b9dee  D.MEQu
000b9f2b  nWnJU3N
000b9f33  E%emV@`v[}
000ba20f  vjqA#7
000ba53b  @U#WwSI
000ba814  $>i-GAp
000bad75  N`mHm %
000bb419  ~dg@VKce
000bc425  s;FhrT
000bdf06  sFLTV"
000be957  kY/mTc/
000be9d5  BpQ!iu!T
000bed0c  4{ibZS
000befc2  <X38tDr
000bf4de  ENf(MVs
000bf9d2  -QMhce
000c08fb  qvS}}1O
000c0967  =Rmh[e
000c0b13  >f$k eAL
000c12af  5QMh\U
000c17eb  9qJL:o
000c213b  aWTj`Q
000c2334  _dJt;D
000c2cc8  1bMEq~E
000c37b2  dsM_4o
000c3f96  rkho.Hv{(
000c4728  ayYH>"L
000c4f53  rMU@pa
000c54e4  DPF=G0
000c5a7e  mIFQLm
000c5ca4  ulQ|P4
000c6ddc  z6xuvn
000c6fc3  QtPrSi
000c7472  jNvNT9
000c763c  AABm'A
000c82c8  =Sih\U
000c83f4  ,hmxzX
000c8a2b  olsBrE
000c8b21  RTti:8
000c8d76  qu[mftv
000c91dd  `(Hbq`>$
000c927e  xASgt[[RKR
000c9905  mQ]HSa
000c9954  `ABAQg
000c9fb0  ggKWk\
000ca3a1  AP8'iAA
000ca416  <TUV]s
000cab9b  [p~zwI
000cac27  :;]wgn
000cb558  IolBs\!
000cb715  j:BjHB
000cb903  -Q]HSq
000cb9b9  HuH}@C(
000cbaa4  ueqEx2
000cbb92  2j oCs
000cc241  PQr8]2hnVA
000cc919  H/5WKGN
000ccdd4  ximSxy
000cd1fa  V@5kSz
000cd905  xyo'53
000cdbb1  UVVa}xJm9
000ce6ec  AbE:K[
000cf9ff  /_^>hpmx
000cfba2  wfvwvgf
000cfcaa  IsLHuu
000d00c9  guRea5%K
000d00dc  &Lwr=M]
000d028c  kTCgP7
000d050d  cM+ROq
000d08eb  UbhbFY
000d12de  ? PBBF
000d1642  6/xfz 4$O
000d198a  86HzJ;Y
000d1da4  XGn#2H%
000d1dd0  gD6bhf
000d21ca  bGR>GYE
000d24a6  C]D5.akQ
000d2926  ZH!NZh!
000d358b  TP2_BFl
000d3bd0  q/WxHd
000d3beb  srbtwi
000d3db6  gwR(~x
000d3e79  w_Eyg]
000d44c3  8|o4eUU
000d52b5  >NGWhR
000d56b2  yZQ3|it
000d5c3d  Q3SqhP
000d5ee9  SRo-BFk
000d6382  gJp<`s
000d65e3  xDNe?b
000d6932  gC>}MAg
000d6b92  tDlqxR
000d701f  `6fvg1
000d78a8  hCMc<Sh-
000d7b25  $vsm`<d$
000d7c80  \?ffkC
000d7daf  BEB"T8F
000d8dde  FwSd\;6
000d91ca  ]&OVv_
000d94c1  jQt$TL
000dabe7  RJqe?KI
000db140  FYCCNl
000db190   ZEM``
000db98a  vr/PBs
000db9cd  ZAE?4g;
000dbbad  q;bWL*
000dc499  =N&Ygw
000dc605  UXl>KUYF
000dc6f0  +GKvLp
000dcb68  DY,PPg^
000dd068  Povd1:
000dd220  k9'Mte
000dd836  ooZ<bV
000ddf1d  jG3BtA
000de2a6  AjT<IB
000de473  bTN1.q
000de9ad  qcka6{
000debf3  #lmZ^YDU
000ded77  NOI9(|
000df326  (htsG*@
000df640  'yjj+`
000dff2a  D=UVCl^}
000e007f  S|chNU
000e01e4  $LN>LXJ
000e031a  vFZR=^
000e0710  gODHxT
000e0805  WKDGve
000e085a  ).EIh`
000e1294  57Njju\W
000e1581  4Ath0}
000e178c  g{@kgyV
000e185d  hH_buT
000e1fbc  YkG_,$
000e2875  azbvgzg
000e2890  9gfvwvwf
000e2c97  {Q&fkbPF
000e3558  dtm_"2
000e384e  >EQJb`
000e4665  AMv(Mr
000e476d  HNzB._
000e4c6b  Qri;8`}
000e5329  +,*aXq
000e5cb5  oHB\nn
000e5e80  cH_4.Rcc
000e618a  A[IFPe
000e64fe  JgX|P"
000e7611  qS$pCK
000e7b95  B|[Wwlh
000e7c0e  lp>GDa
000e7efd  %eoGD 
000e7f52  l,sMc]o
000e8965  [ DzGL
000e9ce4  Io_awuO
000eb061  N0PwS1
000eb1f2  iYE73[m
000eb390  wQW6lP
000eb64b  KgVp<s
000ec05b  vpcx61
000ec2e7  XUI=X 
000ec710  OL}m$tZX|
000ec751  8,N"XBS9v]
000ecf2c  O+3Gms
000ecfc7  Vifw_)`E
000ed6b6  rhKo?u
000ed849  p'gPTf
000ed9f3  QcUH$B
000ede78  `1Avx(
000ee368  %Z'zWm
000eeac0  #ojBhTk
000eedc8  b_-urD
000eee47  dTSnl0
000ef47e  NPq'$@
000ef521  BiL5$[c!d
000f00a2  COt1pF
000f0236  `:fzgs2
000f07c4  P;CCAP
000f1432  cgq=Y"a
000f1deb  CubzFAc4'
000f1f04  `LFjZF
000f24d2  &_soI!
000f2bc0  ttG18M
000f2ca1  scz0{:F
000f3b36  ,:)bBZd
000f3c7f  (aTeby
000f3f4f  Q C<XTn
000f56f9  6orQq.
000f657f  E'siFg
000f6a6b  6(-LZyt
000f6eda  ynTmxv
000f72f3  lMeR;fi
000f79ea  yfOwUw
000f7b32  UHICYh
000f85a3  }>NMKOL
000f87f2  "VXSXH
000f8f66  xz?jvD
000f90cc  +hMXOM
000f922b  Kzib5i
000f93ae  ggg#]_
000f95c6  \wO:ddN
000fa710  oG!p%NtQ
000fb184  IXK|X_
000fb765  s4gsl=r.
000fbc1f  a^ZscVkpS*
000fccf8  _u.uaY\g
000fd85b  -{2=Str
000fdbc4  $A)~ROEc
000fde93  ;'tbPD1
000fe016  bISHloR
000fe811  -ZQGLbQ
000fe952  ;@;DIc
000ff7d7  tu`Sgn
001005d9  Z{L\gvg
00101812  q}.VJU
00101e9e  ,vjTA)c1
00102887  VMS2o,
001028b5  B;pWiu
00102d4b  q)FBq=
00102ea9  QbK#QU
0010326b  IuMmMmOeQ
001032a3  ufvvgwf
00103362  npBE%^
00103a25  aU6QAiN
00103cdf  eTraUu@k
00103dc5  OzXP2j)i
001040e2  DG#VfU`Nc
00104888  oYnj%P
0010507f  UnF/<D 
001053af  2%?pWt
001059f6  %`wvu/
00105e58  (M+gUp
00106008  Ok$kcxi
0010672a  TCk-?S{f
0010697f  xyhSgn
00106bc3  (ZOk8 j
00107119  d6]DgQGb
00107867  YEp'*_&
001079cf  {U}TwU
00107c54  VnTUhT
00108056  %psQoksL
00109867  SeF8>$A
0010a9fd  N#xHd-W
0010acf6  yVy^~`
0010c10b  Z>7?}ugV
0010c1f1  p}uFPd;_!
0010cb54  Lr'5LgdtL"CJ
0010d059  <Iq./%FbBk
0010d295  "I8GKB8}kgAH
0010d415  F`pIh}
0010db09  R*WuZ1
0010e934  dPkcN!
0010ee24  )|hht9c
0010f323  A<]NIw`
0010f5a5  uD]#YWS
0010f618  ;P[OaS9
0010f73d  oKjPNP7
0010fe2a  N).ShJ
001102b8  fODmnl
0011075f  tiyLfSav
0011105c  ZdNdnT`
00111eb9  ez'Q+wrT
0011222a  -W]oQg
0011349e  $4Ulp_
001139a5  PwLUr"
00113f1d  lRJ\O]J
00114691   P&RSl
00114e6a  {pcO_x
00115224  @PdcA/
00115810  QLVeL9
00115844  (}Bwgs
001165c2  ^=nvMG
001167ad  Q{0Qtc:
00116900  '5dTq^
00116f3f  rnB5t6
00116f49  )BUD._
00117223  5s"gJd=
001175f1  6^hrOs
00117bbf  hlbM{M
0011848f  _;mzE`:
00119016  2x<B{nOI
0011906d  +TxBx[
0011a294  PP!KTnE
0011a317  Ydz$P[?@
0011af8a  iuP:^L
0011b52b  9t(csi`
0011c425  nwAh!g
0011d064  L:LmK((
0011d33b  8LHrI7u*wA
0011e2fa  L[7uwI
0011e36d  qrK=E#
0011e442  ]MIc/l/
0011e45b  GGo/` 
0011e5c4  ElllL=
0011fac9  6c,pmB
001209f6  '80pPE
00120b32  *"uNif
0012157a  UF-2AkJ
00121793  ZhzV:]m
00121b19  Svv2yc
00121c9b  MQIf$y}
00121ccb  _DUuil"l
00122720  @qsP*"
00122fe4  PYV-bY
0012304f  1!LAV~~
0012306c  :@muAm
00123cea  ~!lnim
00123ddc  )fssq+
001240cd  qGKfwe
001242f1  7^CUG:9
0012437d  .PlM\<
00124cfd  YHXG[>UY
00125166  nuSE7qW'w
0012526a  t+WzF@(Y
00125274  !P<Fol
00125982  'mmB*y
00125a58  LCBr<e
00125c9f  )&pRYEd
00126977  P\ecaa
00126bcd  >rKRA2>.1\
00126ed3  |OqHqK
001280d8  <TxhXF%
001283bc  =onot>
001298f6  k+b>Spx
00129dbb  k"goDP
00129eb1  @K}IjB
0012ac77  kef8ey
0012b2df  aLtk1;
0012b666  mJdK&3
0012bafd  58huLY
0012c790  7\* qKH[
0012c91c  2pSDXs
0012cf54  zJbP^\#b
0012d26d  CjP79vb[MM-
0012d2e1  hxh0gp
0012d566  (:Q0bbm
0012e99f  X4,erC
0012f1e1  ^wwq%]w
0012fa73  ^NLCBB
0013029a  HZn,Y.
00130c01  7LHyyuh
001313ec  fGPjRH
0013165a  ZcqPQ.
001319bf  cst73O
00133685  CTj(!K
00133942  'Y=hnU
0013414f  kyvRg<
001346d6  cdIV4z
0013496f  {Dig=r
00134d1e  6cGnFw
001357a7  mzN7^~o
0013633f   aZX9U
001368da  *teN$s
00136dfe  iXIB(N
00136eb9  CLZU H
001372cf  0/\nlM
001376b3  asUuIM-W
00137e49  a0xkQu;
00138584  I=MkrY#S
001386be  .GtwjY
0013912e  E9?Tkp
0013964d  5,Rqxj<
00139da5  NKQ`T4
00139e35  QCO`44
0013b012  SkZ9c:
0013b857  5HeC`/
0013bb4b  _GlR8sh[
0013bd5a  ?5 cLS
0013c3f3  QvH6SI
0013c491  kXL}&,
0013cdd7  3q2GPv
0013db46  Xle>({$
0013e1ed  & >7Adu~a
0013e80a  p^$+aAdv
0013eb61  {:XIA:l
0013f055  J`jdYT
0013f3ed  j%rtB%B
0013f5f9  {ffqkd
00140aa2  )qQiK{U9
00140d44  DmrBTa
0014108d  ITc;H\
001411a2  :RgQj`r/|
0014127d  ~uvjPN
0014150c  xQqIin
0014162b  fvn~aq
00141e0b  mdS*Ndg
001423c9  Eqg7}W@_
00142525  ,jiasL
0014306a  qlgz@[
0014439e  ZV8OcU
0014456e  FdV7Uc
00146537  {!\.EtR
00146c08  Cdt[ma
001471ac  i~#Z7jNEQu
001475d2  ^u$kkL
0014a8c9  [4OOjS
0014a9e8  "XIx9+
0014bde2  A_)djp
0014bf6a  LKY*NP
0014c0f9  Gv[8uJZ|
0014c18e  %`IzE$^
0014c363  {S:wWI
0014c761  s}3u"pvX
0014c9d4  ojni%B[
0014cb27  xFm]DP
0014dd3d  U*umuO
0014ecca  MkT1EGL
0014f0e3  o8tHX:$v
0014f34e  ^MmXhM
0014f434  PLNRunp}
0014f7c7  Fsr[oz
0014f7e3  `qIL-3
00150652  @+NebM
0015089e  COXES%i!
00150b9e  4,PHE9
00150f50  )sOR+`
001511c6  WPUGkC*
001515e5  FwZ&a2
001529e8  xrs8[/
00152c5c  pmMrOP
00152ded  1PHF+uE8
00153a7b  MCfh8o
001555f5  #_HCEI
0015582f  xFs5%^
001558ab  bnsHL)
00155bab  ~'kAmj
0015609f  7I'XOh
001568f6  O6LMME:?
00156b85  a&SZV^Q)
00156c7b  ]abrj|
00157314  6qNX=j
00157b34  Ca/cND@
00158689  X:MoeAI
00158add  k-Brk`om
0015927c  CVp`D\
001594bf  ln\fl.EfoZ
001596e6  xZlh2';
00159965  @`KSlOk
00159d5b  ^f?eoK.%
0015a998  .j'mGy
0015b0cb  LL?:DpIr
0015b4b4  moK,c:
0015bbd8  NTD-M;
0015bd16  YzH:@>
0015cd93  @Qwh'1
0015d090  )ROK&-
0015d557  }pB$opq
0015e109  Wkw?rf@\c0c
0015e84e  _XnnLU
0015e88c  dMU*315
0015ec57  M3WYU]S
0015f0a3  fth+Z.
0015f0b9  j^.?`UEupd
0015fbb9  \Wnwn0C
0016001c  DXfB'j
0016011d  xGN(/Z
00160607  8{tJkI
00160ad3  A4vHhr
001612d2  frEy{"
00161bf0  6Mwp;1
00163138  JCM:tx~
00164154  A3MihqA
00164cf1  p"<arm
00165196  boL@Kk
001658bb  &rtB[g
00165d4c  *D|BLl
00165e84  $j1S+9vvq
00165f66  f'1tIo
001663a4  QA8BEK
0016645c  w'9Pub
001672f8  bGY_5K{
0016762e  'GxD7s}
00167657  fySk(>~
00167965  %4mJl@
00167abc  |Eal9k
00167b7d  /ZB8MNP
00167cdc  Aj=dZW
00168ad7  W@KeUuMm
001695ab  Ex<KUM,
001697b5  wfC=UiT
00169879  `s'8PPeL
00169bd3  uq(oD+ZwT
00169fb9  yknCG&
0016ac3c  'GXX3 
0016ae48  YbLULX
0016bb31  'JqE2v
0016c232  vnNU3!
0016c6a4  ihEKEG`
0016c842  GV;HCv
0016cbe0  jCIp$#
0016d357  ?VBrUO
0016d41a  !`THi8M
0016d90a  H/gjG1
0016dd73  mc'uQW
0016dd8e  h2@GUu`f^l
0016e03d  KBb)!l{
0016e7de  6zArl3m
0016ec14  #bro3q
0016ece2  Kfwq`=c
0016f486  cvRo =FZ
0016f987  _BQaKX
0016f9d1  Rmh|*[
0016feed  sgpr>smKVs}
00170a36  C7kaHH
00170af0  djf=@s 
00170bd7  r,ed`peb`h
001712a5  Vxe7OF2
00172036  ybg-P,d#
001728df  .354LRw
00172c77  7465onAY
00172e95  5R]hcE
0017308d  gWc;F)
001730ad  zVJ.ee
00173517  %QKhSi
00173c36  MHSL#p
0017427b  HR kHZ@L#
00174337  ($ RhBr
0017454e  D.MEQu
0017468b  nWnJU3N
00174693  E%emV@`v[}
0017496f  vjqA#7
00174c9b  @U#WwSI
00174f74  $>i-GAp
001754d5  N`mHm %
00175b79  ~dg@VKce
00176b85  s;FhrT
00178666  sFLTV"
001790b7  kY/mTc/
00179135  BpQ!iu!T
0017946c  4{ibZS
00179722  <X38tDr
00179c3e  ENf(MVs
0017a132  -QMhce
0017b05b  qvS}}1O
0017b0c7  =Rmh[e
0017b273  >f$k eAL
0017ba0f  5QMh\U
0017bf4b  9qJL:o
0017c89b  aWTj`Q
0017ca94  _dJt;D
0017d428  1bMEq~E
0017df12  dsM_4o
0017e6f6  rkho.Hv{(
0017ee88  ayYH>"L
0017f6b3  rMU@pa
0017fc44  DPF=G0
001801de  mIFQLm
00180404  ulQ|P4
0018153c  z6xuvn
00181723  QtPrSi
00181bd2  jNvNT9
00181d9c  AABm'A
00182a28  =Sih\U
00182b54  ,hmxzX
0018318b  olsBrE
00183281  RTti:8
001834d6  qu[mftv
0018393d  `(Hbq`>$
001839de  xASgt[[RKR
00184065  mQ]HSa
001840b4  `ABAQg
00184710  ggKWk\
00184b01  AP8'iAA
00184b76  <TUV]s
001852fb  [p~zwI
00185387  :;]wgn
00185cb8  IolBs\!
00185e75  j:BjHB
00186063  -Q]HSq
00186119  HuH}@C(
00186204  ueqEx2
001862f2  2j oCs
001869a1  PQr8]2hnVA
00187079  H/5WKGN
00187534  ximSxy
0018795a  V@5kSz
00189698  not set
001d0000  RTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACKRTKSTACK
001d6038  __TEXT
001d6058  __DATA
```
