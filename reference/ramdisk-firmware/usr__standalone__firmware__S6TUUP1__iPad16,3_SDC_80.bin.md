# `usr/standalone/firmware/S6TUUP1/iPad16,3_SDC_80.bin`

- File size: 8,388,608 bytes

## Payload [FW]

- Size after IM4P unwrap / decompression: 8,388,608 bytes
- Format: raw binary

## Strings (719) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
0000404d  Apple Display
000201c2  TIMESTAMP : %s
000201d8  D:abv_r
000201f2  D:ppsync_off
00020200  D:ppsync_on
0002020d  D:abv_f
00020216  D:abv hold %d
00020244  b_e %dus
00020275  D:w nvm
0002027e  D:g nvm
00020287  D:m nvm
00020290  D:none nvm
0002029c  D:rdmode %d
000202a9  E:[%d]crc %x %x
000202ba  D:header 0x%x
000202c9  D:header 0x%x  crc 0x%x, 0x%x
000202e8  D:nvm_load_dis 0x%x
000202fd  E:wrong type1
0002030c  E:tcon_cfg type1 error
00020324  D:[%d]disable
00020333  D:[%d]begin  0x%x, 0x%x
0002034c  D:NVM_SDC2 nvm_addr 0x%x
00020366  D:NVM_SDC2 0x%x -> 0x%x (0x%x)
00020386  E:NVM_SDC2 chksum %02x, %02x
000203a4  D:[%d]begin  0x%x, 0x%x  rd=%d
000203c4  D:[%d]begin  (0x%x, 0x%x), 0x%x  rd=%d
000203ec  E:[%d]invalid addr(0x%x, 0x%x)
0002040c  E:[%d]invalid len(0x%x, 0x%x)
000205f6  D:reload
00020600  D:reload %dus
0002060f  D:init on 0x%x
0002061f  E:PARA timeout
0002062f  E:MEM timeout
0002064e  D:lut_s
00020657  D:lut_e
00020698  D:SKIP %d(%d)  
000206a9  D:LOAD %d(%d)  0x%x, 0x%x @%dus
000206ca  E:invalid %d(%d)  0x%x, 0x%x
000206e8  E:invalid %d(%d) ck 0x%x, 0x%x
00020708  E:[%d] chksum %02x, %02x
0002072c  $%&'D:ip15 size  mon(%d,%d)
00020749  sdc_vb_fall
00020755  sdc_vb_bias
00020761  mbist G0 s
00020774  mbist G1 s
00020787  mbist G2 s
0002079a  mbist G3 s
000207b5  drv_dmac0
000207bf  UUP1FW_%s
000207ca  D:ver %08x
000207db  boot_main
00020868  rt_clock_drv
0002089c  rt_pad_drv
000208e8  TIMER ISR0 NULL ARGS
000208fe  rt_frt_drv0
0002090a  rt_frt_drv1
00020916  rt_frt_drv2
00020922  rt_frt_drv3
00020960  rt_uart_drv0
0002099b  E:timeout %d
000209b2  E:wrlen(%d)>fifo_cnt(%d)
000209cc  D:ACC_BLK : write_ok : %d, abort : %d, check : %d
000209ff  D:addr:0x%x, len:%d
00020a14  D:HOST : rd_nack_stop:%d, nack_first:%d, nack_only:%d
00020a4b  D:COM : rd_nack_stop:%d, nack_first:%d, nack_only:%d
00020a81  D:stat : 0x%x
00020a90  D:sts : %d
00020a9c  E:IP stuck (state#6)
00020ab2  D:trans end
00020abf  D:stop timer
00020acd  D:leader%d locked
00020ae0  D:set timer %dus
00020af2  D:interrupt:0x%x
00020b04  D:isr_r
00020b0d  D:i2cm_init
00020b1a  E:m_busy
00020b24  D:ioctl done
00020b32  D:exec_post:sts=%d, pend=0x%x
00020b51  E:e:ABORT
00020b5c  E:e:NACK
00020b66  E:e:NO DEV
00020b72  E:e:timeout
00020b7f  e:done
00020b87  e:incomplete
00020b95  e:else
00020b9d  D:done(sts=%d)
00020bad  D:NOSTOP : %d,  START_ONLY : %d, NOSTART:%d
00020bda  D:s_i2cm_start_only_t
00020bf1  D:s_i2cm_devaddr_only_t
00020c0a  D:s_i2cm_offset_only_t
00020c22  D:s_i2cm_standard_read_t
00020c3c  D:s_i2cm_standard_write_t
00020c57  D:isr_p : write_read_req
00020c71  D:sem_dis1
00020c7d  D:sem_dis0
00020c89  D:leader%d released
00020c9e  D:isr_p : bus_req. sem holder : %d
00020cc2  D:isr_p : clear_buf_req
00020cdb  D:isr_p
00020ce4  rt_i2c_m_drv0
00020cf4  i2cm_prepare_standard_write
00020d10  i2cm_prepare_standard_read
00020d2b  i2cm_prepare_offset_only
00020d44  i2cm_prepare_devaddr_only
00020d5e  i2cm_prepare_start_only
00020d76  i2cm_post_standard_read
00020d8e  i2cm_post_start_only
00020da3  i2cm_post_common
00020db9  i2cm_post_devaddr_only
00020dd0  rt_i2c_master_ioctl
00020de4  rt_i2c_master_ioctl_transfer
00020e01  rt_i2c_master_init
00020e86  rt_i2c_master_exec_post
00020e9e  rt_i2c_master_exec_pre
00020ee0  rt_i2c_master_exec_pend
00020f2f  D:fail pull rxfifo
00020f43  D:trans_abort!
00020f53  D:slave done (invalid cnt : %d)
00020f74  D:fail push txfifo
00020f88  D:isr: slave_addr_match
00020fa1  D:invalid addr (RD,WR)!
00020fba  D:subaddr: 0x%x
00020fcb  D:invalid addr (WR)!
00020fe1  D:isr: rxfifo_almost_full
00020ffc  D: fail to push to txfifo
00021017  D:isr: txfifo_almost_empty
00021033  rt_i2c_s_drv0
00021044  rt_i2c_slave_init
0002107c  [SPIM]
00021083  [%d]timeout1 %d
00021094  [%d]timeout2 %d
000210a5  D:[%d][%d]lock
000210b5  spi_sem
000210bd  E:%s timeout
000210cb  E:DMA timeout
000210da  D:[%d][%d]unlock
000210f6  S0_BUSY
0002110d  FIFOREAD
00021116  rt_spi_m_drv0
0002112b  rt_spi_master_init
0002120c  [SPMI]
00021213  D:***SPMI Get data from slave, data len = %d, stat = 0x%x
0002125c  D:***SPMI Get data from slave = 0x%x
00021282  D:set_clk(%d) dy_u(%d)
0002129a  E:DYN:M_BUSY
000212a8  E:acc_blk abnormal
000212bc  D:leader(%d) is locked
000212d4  D:spmi_check_retry :: en(%d), 0x%x
000212f8  D:host%d retry start
0002130e  D:Post:%d,0x%x
00021325  D:TX_START_INT Pended.
0002133d  D:TX_START_INT Pend Done.
00021358  D:BUS_REQ_INT Pended.
0002136f  D:leader(%d) is released
00021389  D:len_opt(%d).len(%d) from ers
000213a9  E:fifo length error with opt 0, %d, %d
000213d1  E:dec cmd error line=%d
000213ea  E:dec cmd error line=%d, _p->wrptr(%d), _t_opt(%d), _t_len(%d)
0002142a  E:dec cmd error:UNSPT_CMD(0x%x) line=%d
00021453  D:decode cmd error, exec_pre return
00021478  E:acc blked(%d)!!!
0002148c  D:before trans, core stat = [0x%x, 0x%x], timeout(%d), sclk_div(%d)
000214d1  D:fifo ptr rd(%d,%d)wr(%d,%d)slv(%d,%d)
000214fa  D:trans cnt=%d
0002150a  rt_spmi_s_drv0
00021519  D:dev_drv:: irq_n = %d, irq_p_n = %d temporally.
00021550  rt_spmi_init
0002155d  spmi_init
00021622  D:edp_indir_isr wr(%d) rd(%d)
00021641  rt_edp_drv
00021670  [DMAC] ERROR : timeout
00021688  [DMAC] ERROR : Input Size is 0
000216a8  [DMAC] ERROR : Input Size is over %d
000216fa  D:i2c[%d->%d] spi[%d->%d]
00021715  D:protect %d %d %d %d
0002172c  D:[nvm16]0x%8x=0x%04x
00021743  D:[nvm8]0x%8x=0x%02x
00021759  D:[i2c]addr32 0x%x
0002176d  D:[i2c]a:0x%x[valid:%d]
00021786  D:[nvm32]0x%8x=0x%08x
0002179d  D:[auxr]a:0x%x
000217ad  D:[auxw]a:0x%x
000217e3  rt_indir_drv
00021a73   0123456789abcdefghijklmnopqrstuvwxyz
00021abe  <NULL>
00021ac5  Oops~ Null handler
00021ad9  handler1
00021ae2  handler2
00021aeb  handler3
00021b79  FpGpGpG
00021d5d  y#p Kax
0002286f  AkF'J'O
00022936  #NjF#I
00022a08  (OjF(F&I
00022ad9  s#NjF#I
00022cdd  %1=$$IUam$$$$x
00022f0d   0FjF)I
00023f12  )FbhyH
000246be  "&),)/1469;=?ACEGIKMORUWY\^^^^^^`behjlj
0002470e  RppG#K
00024a66   ''..99999999999999@GNUUZZZZZZZ^bimmmm.K
00024bd1  Cce$K%J
000253fa  "F!FsH
0002541a  "F!FnH
0002542e  tKgOtN
00025636  EHELFN
00025a5d  `pGpGpGpGpGpGpGpGpGpGpG7
00026621   pGpGpGpG
00026637   pGpGpGpGpGp
00026e94  QAidjl
00027066  QBrdslC
0002706f  3sdchrl
00027120  QFfdmhal
000271c8  QBbdrhclb
000271d5  "cdclb
000271e1  #ccclC
00027256  xcgjcb/K
000272bf  scbclC
000272d9  3cdclC
000278c3  2jdjlo
000278cb  Bjd"z2
000279cd  skbkhC
000279fd  #+gklC
00027a05  3kdklg
00027eba  ABLIMH
00027edb  r#hZbZhB
00028944  (FZibd
00028bbb  "1Fcj(F
00028d5e  0F[jcb
000290ec  2FIF3H
000293f8  1 Zpch
00029438  #bJFd!(F
000295f4  JF[FPF
00029ad0  2FAFXF
0002a184  8"NIKH
0002b60c  KpS{<F
0002bdf2  !Dku)a*u3p;x
0002be55  +(a*uku
0002be61  #kuk}3p
0002d3c4  ZFIF@F
0002d84f  3KapG@K
001b40a1  4!%Isn
001b40fc  30UPUEZ
001b41c9  0ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggjjjjkkkkmmmmooooqqqqvvvvwwww{{{{
001b4871  bbbbbbbb
001b487a  bbbbbbbb
001b4883  bbbbbbbb
001b488c  bbbbbbbb
001b4895  bbbbbbbb
001b489e  bbbbbbbb
001b48a7  bbbbbbbb
001b48b0  bbbbbbbb
001b48b9  bbbbbbbb
001b48c2  bbbbbbbb
001b48cb  bbbbbbbb
001b48d4  bbbbbbbb
001b48dd  bbbbbbbb
001b48e6  bbbbbbbb
001b48ef  bbbbbbbb
001b48f8  bbbbbbbb
001b4911  dddddddd
001b4923  dddddddd
001b4935  dddddddd
001b4947  dddddddd
001b4959  dddddddd
001b496b  dddddddd
001b497d  dddddddd
001b498f  dddddddd
001b5923  WWWttt
001f0574  [Y,AZkQL(
001f0813  2T;<)(BGjR
001f0f8b  V*0lXT
001f1339  C!bHhNI
001f1a34  HhN9c.%e
001f2133  ~rDH<:
001f21c3  (|KXQprb
001f25c3  rLs7<j
001f2ac0  FIKf[[
001f2fd3  HQh#dLX
001f2ff0  xP4FZE
001f36d5  >fsSfB
001f3b1a  ("plyR
001f3de3  Fm>jlK3
001f430e  6LWBJX}
001f45cd  Fdf|H=
001f4613  pdF";8
001f4cae  G2BLXS))
001f4f0f  DNZFBG
001f5ffc  %"h\"PDJ
001f604e  "dvdBL
001f67ce  G&XJK3
001f68e1  H#LXbP
001f6947  N0BXCdnG
001f6e69  xDYdNH
001f76fe  cfuC$J
001f7728  .1LEpG
001f7740  NxA(\xCdC
001f78a4  !SSd#$
001f7a96  DhHH!E
001f82bd  phP0ke
001f8ac8  Q&trH"p
001f96ae  RL&dtE
001f98a4  J%"BHz
001fa3f8  8g,ngfv
001faada  GBhtT!S
001fae03  rDY$LE
001fae67  tyShtdM
001fb138  TfLDWFnJ
001fb2f2  HI"`GrA
001fb6ce  1hXHDL!
001fb982  rfiAOHX
001fbac7  m7vcql
001fbaf2  "FXzp0
001fbcfb  bNGD-"
001fbea8  s,GBR)
001fbeaf  dZ1LIE
001fc3ee  (bRb1g
001fccc5  S6}`GJL
001fccd8  >".jXK
001fcede  ^"/IHI
001fd01d  PdJJ0a
001fd0b7  |1(b$GaL
001fd15a  5!`FaBG
001fd16f  DYD"32fm
001fd216  BJh1)$
001fd24a  dfq"PQ
001fda7e  b,WXEG'.ga
001fdb25  d:dtrKS
001fdcc6  >LOa55
001fdd4a  (bir7L
001fdeb1  J8Bhp6v
001fe1f8  3,\hdJ
001fe461  JX"SbD
001fe5ca  Cs7#"&^eqX
001fe820  4KY(hRP
001fedba  !$TBVx
001fee07  |W9%vnE
001fefb0  1"$1NYQ
001ff192  $HdMdnXH
001ff447  Ien%5db
001ffbf4  &98bIp
001fff6e  ;"@Rmm
00200254  J0TLJ03
00200370  Q7P*XMC
002003a1  pFs)' 
00200636  dHP^|A
002015e4  "Blp#Mf
0020187f  dnK"t&8a
00201af7  [2Hffw
002020a3  !LtH,x
002021c5  YxT:4L
00202302  bxf/"f
002024c3  GEU.^e
002029b5  bTJ?,b
00202ceb  IBi3RG
00202e44  %!9xDdb
00202f8c  zcE2_,
0020352d  .[&,pgG.\ 
00203c21  $HFa@K
002043b1  mTJ>3D,N<x
002044e4  r,FdXJ
00204b28  .0bPC!
00204bfd  P6~poAq
00204de1  ,BQL#3
00204ee3  Ls.kyT
002055ba  BpF.~*?
002055d0  >J8LDD
002056c1  <"MBXdH3
002057aa  +B( hrP
00205b16  ,&GhTS
00205e50  76t%bFb
00205fc6  DLI2rP
002065f7  HI1DAG
0020688a  XIFdY"H
00207129  ]FDr(?
00207206  DAcKPbG!r
0020724c  6hRE<b
0020745d  6)dHYD
002077fa  JNH6H\
002079d2  IG,%KIF
00207cc5  B2BXdL
002081bd  yrX$IImHy
002081ec  1J3.-FFB
00208dd6  !("&S9dLq
00208ecb  =BbXxA
00209048  Jxa(t$$
00209d9d  GFXc*E
00209ea8  d~ZXJ>g
00209ec9   bxq&2
0020a074  g,H9?CLC!d\1
0020a1d7  J2dXhbPa
0020a1f4  \2:"BQj)
0020a651  dCpbdL
0020a713  yqk3&$
0020ad90  xsahfw
0020b5ac  tj%NPs
0020b5b8  ICsI$-
0020b5e0  QQB>;!
0020b689  qQPXf:x
0020b6be  ^GFR+,
0020b6d3  -!SSH~
0020bcbd  dlhBk`
0020bfaa  LbP:b,\
0020c0c7  Ffxc3BcF,1
0020c1d4  aIF%53
0020c40c  3tRb,IP
0020c424  DTF2q$
0020c85f  Qq$DQfL
0020d449  >GDlfa
0020d493  <(JLH>
0020d49c  HS"ayp!
0020d750  RG8DDA
0020dbbb  MdY"G!P
0020e3b9  XFH#)E
0020e3ea  a90aIM(
0020e416  Ibc#g%f,
0020e8f5  bt8fFl
0020ea4e  $faDFHp
0020f12f  .><IBD "
0020f369  pqGJ\E
0020f9f7  c)pfxW
0020fde1  H.FabF
0020fe15  [%4Zjx
00210431  JHC8dL
00210b48  "XTMdC
00210bb1  GtT@i$}$O
00210dc8  V]$B2FXT#
0021164d  E&yCSM
002116b8  IBHXQ`b-
00211ffa  aR$"mJP
00212167  YpaX\P
0021237a  <zs69DdXBk"G
0021281d  ,a+BfC
00212878  Z,tXYa]i
00212917  DQu6Ytv
00212da4  ^pbIc(
00213053  n&flP'
002130dc  !"`HHj
0021322a  DYd]e$\A
0021349b  ,jbCC`
00213535  HF(adf
002137df  B,$hjR
002139af  )! dZr
0021412e  <JfbT[
002142b6  S"daTZ
0021434f  `ASj7N<#
0021439b  fve$#*
002147ce  dX9shd^
0021492c  DIv$tHT3
00214ad0  ^9HFqs
00215256  B&vFs<
00216642  yD<ThC1
0021676e  K9,DDF
00216d5b  fYc~96~v
00216e36  LTQP(x
00216f27  $.8bPg
00216f5c  E<rHDc-
00217147  <&v|IGD
00217542  H!aMDP
002176c2  IFB"HJ
00217897  W\EtLE(
00217f20  =< bad(H
002182e6  fqH~ga
002185fd  <}8BII
00218702  QcC4l"a*5
00218744  T%DvXA
002187b2  >\rSDt]
00218b09  a,4SRL
00218fda  Ef)pEBT
0021945a  E=$Qhu
002196ae  Tjs.XL"
002196f9  zpqJLE
00219eee  $HxDf$
00219f01  0B5VFf,
0021a1a4  sEPMc3"7
0021a270  CHBd\2
0021a74d  "pbJEvwj
0021aca4  ddxFgX
0021acc9  s\g,YpNP
0021ad14  d7<#BqP
0021b090  \aDH2e
0021b16b  $BYxBIO
0021b773  faDN\ 
0021b787  "AC0PbA#
0021b79b  Dff,I1
0021b951  r:(bRc
0021c240  .$zIfLIBg,0 
0021d424  fdH0(D8
0021d965  c,%bPa
0021db35  cSOxcO
0021df84  dZx3-#
0021e6ab  1hfc)M
0021e71a  "P8Tmg
0021e8cf  tXEB]"
0021e9cb  ,"*ffnP
0021ee3c  J"DNXx
0021ef59  DLx`XbY
0021f0bb  8*KgqOBLK
0021f282  !fREB|H
0021f52b  :bMd~1
0021f5ad  8CpbK2xD
0021f94a  fXQ0hP$I
0021fa5a   mHL-F@
0021fe15  AbHH:X
002204b4  Zli~\2Q"
0022090f  &Fy"Rhffr
00220d48  +<!TXB
00220ed9  GxdJ4c'
0022139d  GHs$Fj
00221463  "qgbrR
002214a6  !fCFC3
002216a6  ft9IbB
002218ff  fk1Xxa
002222b2  ,tlfZw
002222c3  !BHf["
002226bd  njxc:"
00222886  XDN(P4
002228ce  QH|TpR
00223104  2dlze 
002237dc  ",FDN05
002238db  "Lqr.%
0022488b  S[d%PYql
0022581e  9BrXJ|
0022600d  BDXaQ(c
00226045  FDnd,a
00226944  fdLJ38
00226c5e  1fXrc83E
00227317  s&~XTS
0022758f  (1QrDIiTB
00227719  RDT1 a
00227a75  "2.ffL
00227c9f   TFT1,
00227d43  "Hg6GAHU
00228076  `aAxWrX
00228329  $I4LFE
00228b13  $CDBbB
0022933d  F,GBB>*B
00229347  C9P9BvH
002293a9  LHBb4Q
002293ee  IxQ!L!
00229b9b  bRp2,b
0022a11f  ,(PHbTAB2
0022a20f  JLBKG5)T
0022a2f6  v0bPr&%
0022a781  A0DIC]
0022a9b6  !Qfb2!"`
0022af3a  #RffJL
0022afd0  T3FaC"
0022b541  DHr>#b
0022b98f  1(aTFe
0022bf17  (x(Yax\
0022c03d  zpb`De
0022c0b2  j|lkki
0022c1be  lD#vFA
0022c1fe  5NGEIF
0022c4cd  tlf]c!yi
0022c8c1  i#'BfH 
0022c8d7  QQAgb*
0022ca12  DZJ{,0s
0022caef  f(slyq
0022cceb  DxsP)1
0022cfd0  2br;BbLI
0022d14e  Fve$Yu
0022d343  Cjb$9cS
0022d49a   fHI1I
0022d7a2  fNX)r'
0022d9ce  (pgZ 2
0022da12  >Ffq$L
0022de78  .gBHsP
0022e24e  F*1 HDY$
0022e2ab  2DQff'
0022e829  RDFJHi
0022f11c  f88FRI&
0022f711  &=>GFX
0022f7d1  FDNFq%
0022fab2  $D8FBD
0023021e  dLT1%#
00230276  Sfqd<J
002304a3  XTR7.>f
0023071d  %xdZ%1
00230727  F|JsI!
00230cab  < ^FqJ$Z%
00230d67  LIhf\N2
00230ed7  8QbC.",Y
00230f59  (DR!bPd\
002310ed  "d.gcJ
00231151  2*t^xRFG
002312fc  QED2DY
002313d7  3JDRHq
0023141b  dXD|!Y
0023149e  K!1PHK
00231654  1cdtrF
00231aa5  bPBAq+
00232334  gXfX3S
00232abf  VppK3a
00232f87  2ZDJZ|#"
00232ff1  bDLHQbR
002330f0  XrMKHqb
002332e3  `bJd,H
00233454  d4xfFd
00233c87  yf8Qpl
00233d86  q>ZfFyd:
00233f4b  t=HJh"A-
0023497f  4LVdKN
00234fee  "dLPf,b3
0023515d  SSgaV|
00235429  H1bYa(2
00235497  bZr$b-0
00235632  0GXQ)$K%,H
002356f3  HggfD2J
0023590b  dbar.$
00235aa9  b"FbPA
00235d72  Zgd*40
00235de7  2S&dLY
00235f04  H*Jls>
002363f8  ID8RFgo
0023674f  R,2bYrQ
002369cb  b$x9sMq
00236b16  0d.GFLi
00236ef1  tMdv0r
0023723b  sLhn<`
00237791  ,(AdX1Q
00237d24  1hXb&h
002385eb  01jjr0e
00238915  o=Q`DHT
00238bf2  s"cfT9(
00238c48  >^sLdB"
00238ce9  YLr&|H!C hQ$
00239222  KLe*|0
00239701  8K2Fia!
00239721  [!i"1"dnj
00239902  Y`8fyJv
00239acb  \NpU@,(
00239ae4   *nfDe
00239f93  )r@$XDR
0023a30d  J%4GSJ
0023a31c  8UdXIK
0023a4c3  >?3JAsS
0023aa92  bph\KB
0023ad76  ZMRf*1
0023b2d1  jDI0r2
0023b552  381FBs#u
0023b6de  "10fZGh<q
0023b9db  .\s&GHl
0023bc9d  ]:d9@W4Mdu0
0023be5c  #BfiF\
0023c0c2  #s!aNA
0023c364  &jlyb,Xi
0023c7f6  :$!FiH
0023c870  6JBs)$lrP
0023d01c  *(FacR
0023d3da  GDX!(t
0023d497  GxIKQo"bg
0023d8da  d!ArY%
0023da5e  &9bIq4Db
0023dcdf  %2HbZ(
0023e126  BHfZ~0
0023e25b  9(trB<$nCP
0023e387  ~8Adv\
0023e754  HTHNzJ|
0023f362  BYc3"Q 
0023f6c8  DZ#"BYxc
0023f936  Uf[Bjn{P)
0023fa93   GXN/32ZLL
00240007  I2R,KhJ
002406df  FCIlp2Y
00240e05  1(`FgI
00241b24  XFXa$F
00241bc6  BHh.4a
00241c2a  Dya&qDv0
0024242d  dNj$H,9
00242d99  (8aqf`
00242dbc  i4#r,*!$Y(WBH
00242df3  ,0jHH2:
002431d5  .aXDDDB
002434b7  HVj3Q!g
00243526  6.nvd<F
00243747  [$TAQE
00243819  Qdnx#DLY
0024382a  fCRJc$
00243c1d  ))6iHOC
00243ca5  GHx1b(
002442cd  xThQaD,M
002443a0  hDMQf9
00244464  dXt,d,
0024460f  1BYQ&D
002446c3  /AFdX`
00244733  K.\jIC!F
002447db  JjXO<u
00244ca0  ieLDYfY
00245553  MLXb$fA
0024586a  JfiFl\
00245ac3  51BYa>B
00246004  a9 YpH
002477ec  RDgBHCC
00247cc0  kBrF>B
002482b4  r,XDfc
002482f4  ,"Tifh
0024832a  2X"h8RLP
002483de  Ttvpp:,
0024889b  s,GHq#
00248aad  o$Mt~VTQ
00248d12  z;KxM=
0024998e  2d,4JTS!
0024a050  XJ(arQ
0024a0aa  fXR>+2
0024a479  vYx"DG
0024ad69  x@RMDL9
0024b1ff  .Fcjz%
0024b30f  AhL(3)$(
0024b6eb  "j2DLJ
0024b952  geF`BO
0024bd38  @d(yaR
0024be9e  b#.Xom
0024c4bc  0+-YVD
0024c5ad  BXdn\1JhE(L
0024c647  %#bK!dMK
0024ca68  dXJNZ|
0024cf49  R$J$gcK
```
