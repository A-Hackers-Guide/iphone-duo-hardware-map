# `usr/standalone/firmware/S6TUUP1/iPad16,3_SDC_A2.bin`

- File size: 8,388,608 bytes

## Payload [FW]

- Size after IM4P unwrap / decompression: 8,388,608 bytes
- Format: raw binary

## Strings (269) [FW]

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
```
