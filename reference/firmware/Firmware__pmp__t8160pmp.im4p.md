# `Firmware/pmp/t8160pmp.im4p`

- File size: 737,305 bytes
- IM4P: Tag: IM4P  Type: pmpf  Version: 0
- BuildManifest components that use it: `PMP`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         pmpf
  Version:      0
  Data:         737 kB (737280 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 737,280 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- `RTKit: %s - Client: %s`
- `RTKit_armv8_chinook_Oz_flto-3514.40.18.release`

## Strings (422) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000028  __TEXT
00000068  __text
00000078  __TEXT
000000b8  __const
000000c8  __TEXT
00000108  __cstring
00000118  __TEXT
00000158  _rtk_mtab
00000168  __TEXT
000001a8  __constructor
000001b8  __TEXT
000001f8  __chain_starts
00000208  __TEXT
00000248  __text_end
00000258  __TEXT
000002a0  __DATA
000002e0  _rtk_boot
000002f0  __DATA
00000330  _rtk_page_tables__DATA
00000380  _rtk_init_stack
00000390  __DATA
000003d0  _rtk_irq_stack
000003e0  __DATA
00000420  _rtk_exc_stack
00000430  __DATA
00000470  __const
00000480  __DATA
000004c0  __data
000004d0  __DATA
00000510  _rtk_patchbay
00000520  __DATA
00000560  _rtk_boot_l1
00000570  __DATA
000005b0  _rtk_power
000005c0  __DATA
00000600  __gxf_data
00000610  __DATA
00000650  _rtk_tunables
00000660  __DATA
000006a0  __mod_init_func
000006b0  __DATA
000006f0  _rtk_data_uuid
00000700  __DATA
00000740  _rtk_heap
00000750  __DATA
00000790  __zerofill
000007a0  __DATA
000007e8  __ETEXT
00000828  __text
00000838  __ETEXT
00000880  __DATA_CONST
00001a61  wwwwwww
000082f5  8pn!8pnj
0000a69b  4hBO9h
0000a6cb  4iFO9j2B
0000b4aa  C-GAR-B
0000c493  TjBGyJ
0000c4d7  4j2GyJ
0000c4ef  4j6GyJ
0000cc80  h:Gyi>Gy(
0000cd38  i&Gyj!
0000d014  ghexthdxc
0000d0e8  FhdxGhcxB
0000d5c7  4h:Gyi>Gy(
0000f095  j|xhbD
00022690  HCQ9x2@9h
0002aff7  7hVA9(
0002b26f  7hVA9(
0003067f  ?8bunz8
00030a17  ?8bunz8
00030bd0  UUUUUU
0003130e  N@fffff
000313fb  K@d0I(knN
00031ad0  mc_ctrl_tracing
00031b04  mc_ctrl_policy
00031b38  mc_ctrl_win_count
00031b6c  mc_ctrl_dsid0_size
00031ba0  mc_ctrl_seed_rate
00031e90  pmptool-temp-sensor-config
00031ec0  pmptool-fast-die-lp-config
00031ef0  pmptool-fast-die-ce-map-config
00031f90  pmptool-config
00031ff0  tuning-version
00032100  RTKSTACK
00032179  RTKit_armv8_chinook_Oz_flto-3514.40.18.release
00032298  stk_fail
000322a7  lts-acsk-tddb-config
000322bc  tddb-ki
000322c4  tddb-af_t
000322ce  is-tddb
000322d6  is-tddb-inuse
000322e4  is-tddb-ovrd
000322f1  transistor
00032301  LS: %s Core %d %s IS ovrd (%s): 0x%llx
00032328  PMPTool
00032333  LS: %s TDDB ki ovrd (PMPTool): %f
00032355  LS: %s TDDB af_t ovrd (PMPTool): %f
00032379  lts-ctrl-%d-%d-%d-%s
0003238e  lts-ctrl-ts
0003239a  lts-ctrl-loop
000323a8  lts-config
000323b9  ppi-min
000323c1  lts-voltage
000323cd  lts-clpc-voltage
000323de  dtt_min
000323e6  dtt_max
00032409  vmax-reset
00032419  tmax-reset
00032424  ovrd-reset
0003242f  enbl-thrtl
0003243a  lts-ctrl-die-count
0003244d  lts-ctrl-loop-count
00032464  is-inuse
0003246d  is-ovrd
00032475  lts_ctrl: retrograde update
00032491  lts-ctrl-%s-%s
000324a0  lts-ctrl-%d-%d-%s
000324b2  lts-ctrl-%s
000324c8  double
000324cf  LTS_CTRL: Loops now running every %llu us
000324f9  LTS_CTRL: Params now publishing every %llu us
00032527  LTS_CTRL: Reset all overridden parameters.
00032552  LTS_CTRL: Fast Die Throttling %s.
00032574  enabled
0003257c  disbaled
00032585  LTS_CTRL: Max voltage overriden for %s loop: %d
000325b5  LTS_CTRL: Max voltage reset for %s loop
000325dd  LTS_CTRL: Max temperature overriden for %s loop: %d
00032611  LTS_CTRL: Max temperature reset for %s loop
0003263d  LTS_CTRL: Integrator state overriden using PMPTool for %s loop: 0x%llx
0003268a  dvfs-filter
00032696  %s-constraint-%s
000326a7  %s-constraint
000326ce  Core Block Slot
000326de  M$ Stall
000326e7  DRAM Stall
000326f4  DIE-TEMP
000326fd  PMP started!!!
00032720  F6_LOW
0003272a  F7_LOW
00032742  VMIN_NISP_NX
0003274f  VMIN_NISP_WX
0003275c  VMIN_WISP_NX
0003276e  VNOM_NISP
0003277d  VMAX_NISP
0003278c  VOVD_NISP
000327da  SOC-NI0
000327e7  ANEXL1
000327f8  SOC-NI1
00032800  ANS UP
00032807  ATC UP
0003280e  ATC DOWN
00032817  PCIE UP
0003281f  PCIE DOWNN
0003282a  PRORES UP
00032834  SEP UP
0003283b  SOC-NI2
00032843  ANEXL0 UP
0003284d  ANE1 UP
00032855  JPEG UP
0003285d  SBR UP
00032864  SIO UP
0003286b  SOC-NI3
000328a1  SOC-AON
000328a9  SOC-REST
000328c7  PRORES
000328d6  LIFETIME-SERVO
000328e5  lts-ctrl
000328ee  DCS-BW
000328f5  DCS-WR-BW
000328ff  AGX-DCS-BW
0003290a  AGX-AF-RD-BW
00032917  AGX-AF-WR-BW
00032924  ANE-DCS-BW
0003292f  ANE0-DCS-BW
0003293b  ANE1-DCS-BW
00032947  ANE0-AF-BW
00032952  ANE1-AF-BW
0003295d  ANE0-LINK0-AF-BW
0003296e  ANE0-LINK1-AF-BW
0003297f  ANE1-LINK0-AF-BW
00032990  ANE1-LINK1-AF-BW
000329a1  SOC-NI0-BW
000329ac  SOC-NI1-BW
000329b7  SOC-NI2-BW
000329c2  SOC-NI3-BW
000329cd  AFI-TOP-BW
000329d8  MEM-CACHE
000329e2  mem-cache
00032a15  DISP0_M3
00032a1e  DISP1_M3
00032a27  DISPEXT0
00032a30  DISPEXT0_M3
00032a3c  VOVD_NOISP
00032a47  Mem Latency
00032a57  #Mem Trans
00032a8a  AFI DCS
00032aa6  SOC-NI
00032abc  %s-threshold-%s
00032acc  %s-threshold
00032ad9  %s-thr-%s-%s-%s-%s
00032afa  fast-die-ctrl-loop
00032b0d  SOCHOT - Hot Hot Hot - 
00032b32  %s[win_snsr_id=%d]=%s/%d/%d 
00032b4f  Panic string formatting error observed!
00032b77  die%d-fast-die-loop-%s-%s
00032b91  die%d-temp-sensor-%s-%s
00032ba9  die%d-die-temp-ctrl-%s-%s
00032bc3  die%d-cpmu-acc-%d-%s
00032bde  temp-sensor
00032bea  offset
00032bf1  alarm1-temp
00032bfd  temp-sensor-version
00032c17  hs-target
00032c21  engage-delta
00032c2e  invalid-temp-offset
00032c42  max-valid-temp-lag
00032c55  Fast-Die CE
00032c66  fast-die-ctrl-loop-version
00032c81  fast-die-ctrl-ce-map
00032c96  Fast-Die Delay
00032caa  sochot-sensors
00032cb9  alpha-up
00032cc2  alpha-down
00032ccd  round-%d
00032cd6  gradient-%d
00032ce2  fast-die-ctrl-ts
00032cf3  fast-die-ctrl-ts-ms
00032d07  fast-die-ctrl-ts-avg-temp
00032d21  enable
00032d28  alarm0
00032d2f  alarm1
00032d36  avg-temp
00032d3f  acc-cpmu
00032d48  transition_all_domains_to_vmax_serial
00032d6e  transition_all_domains_to_vmin_serial
00032d94  transition_all_domains_to_vmax_parallel
00032dc1  dvfs->current_vector() == dvfs->target_vector()
00032df1  test/dvfs/dvfs_test.cpp
00032e09  j != max_retries
00032e2b  io.cpp
00032e32  scratch-trace-enable
00032e47  scratch-trace-filter-mask
00032e61  scratch-trace-filter-value
00032e7c  mc_quota_req_ptd_count
00032e93  mc_quota_rsp_ptd_count
00032eaa  mc_cmd_ptd_count
00032ebb  mc_cmd_ack_ptd_count
00032ed0  mc-dsid-ptd-config
00032ee3  mc-quota-policy
00032ef3  mc-cue-quota-cfg
00032f04  Grp %d
00032f0b  Group Quota
00032f1c  mc-cue-win-count
00032f2d  mc-cue-dsid0-quota
00032f40  mcache-stream
00032f4e  Grp%d Hits
00032f59  DSID Stats
00032f64  Grp%d Misses
00032f71  mc_ctrl_grp%02d_min_quota
00032f8b  mc_ctrl_grp%02d_max_quota
00032fa5  mc_ctrl_grp%02d_quota_incr
00032fc0  management
00032fcb  crashlog
00032fd4  syslog
00032fdb  kdebug
00032fe2  ioreporting
00032fee  pmp_ctrl
00032ffd  ptd-range
00033007  dvfs-domain
00033013  soc-device
0003301e  soc-device-ps-group
00033032  controller
0003303d  BWR latency threshold exceeded: %llu us (->%u)
00033070  pmc-max-bwr-latency-us
0003308d  Ceiling
0003309a  pm-ptd-ranges
000330a8  %s-monitor
000330b3  bwr-catch-up-factor
000330cd  PWC Window 0
000330f3  PMGR%u
000330fa  PWRS%u
00033101  STRESS
00033114  PMC %s Floor
00033121  PMC Keep Alive
00033139  PMC Driver
0003314a  PMC 2D State
00033157  COP %s
0003315e  PMC BWR latency
0003316e  RESOLVING
00033178  PMC RMBS
0003318a  Timeout waiting for PSD dashboard drain (dashboard %d)
000331c1  PTD abort: %s (%#llx)
000331d7  PMC panic: %#x
000331e6  PMC message error: %#x
000331fd  PMC message invalid: %#x
00033216  PMC message timeout: %#x pmc_gp_debug1 (pmc assert id) 0x%x
00033252  dvfs_constraint_disable
0003326a  pmc-voter-ceil-override-mask
0003328d  STRESS-0
00033296  STRESS-1
0003329f  STRESS-2
000332a8  STRESS-3
000332b1  THROT-ALL-SUM
000332bf  Q-TICKS-0
000332c9  Q-TICKS-1
000332d3  THROT-ACC-SUM
000332e1  THROT-GPU-SUM
000332ef  THROT-ANE-SUM
000332fd  THROT-SOC-SUM
0003330f  ORANGE
0003331c  GREENER
00033324  test_pmgr_soc_perf
00033337  pmgr_perf
00033341  pmgr_soc_perf->irq_status() == false
00033366  test/pmgr_perf/pmgr_perf_test.cpp
00033388  pmgr_soc_perf->state_change_ongoing() == false
000333b7  i != test_retries
000333c9  curr_state == state
000333dd  win0_power_gating
000333ef  win0_clock_gating
00033401  win0_wfi_only
0003340f  pmp_pwc
00033417  test/pmp_pwc/pmp_pwc_test.cpp
00033435  packet_config
00033447  win0_start_time_entry.new_data
00033466  test/ppc/ppc_test.cpp
0003347c  win0_start_time_entry.message
0003349a  win0_start_time_entry.timestamp
000334ba  win0_start_time_entry.message <= win0_start_time_entry.timestamp
000334fb  loopback
00033504  data_drop
00033516  !ptd->irq_status({i, 1})
0003352f  test/ptd/ptd_test.cpp
00033545  ptd->irq_status({i, 1})
0003355d  entry.timestamp >= ticks
00033576  exp %llu was %llu
00033588  entry.new_data
00033597  !entry.dropped
000335a6  ptd->irq_status({0, 1})
000335be  entry.dropped
000335cc  exp %u was %u
000335da  sync_win
000335e7  win0_start_tick0
000335f8  test/pwc/pwc_test.cpp
0003360e  win0_start_tick1 > win0_start_tick0
00033632  win1_start_tick0
00033643  win1_start_tick1 > win1_start_tick0
00033667  MAX(RD,WR)
0003367a  %u.%02uGB/s
00033686  %u.%uGB/s
00033690  %uGB/s
0003369c  DISPEXT
000336a4  DISPDFR
000336b0  SCODEC
000336cf  RT+GRT
000336ec  %s-dvfs-state-voltages
00033708  %s-p%u-min-%s-state
0003371c  %s-push-thr
00033739  Energy
00033749  Volt-Temp HM
0003376e  SOC-NI Util
0003377a  NON-RT
0003379a  !MIDR: 0x%x
000337a6  ~CsPTR
000337b3  !ROf %#lx %#x
000337c1  MMU out of tables: %zu,%zu
000337dc  MMU private: s:%llx!=%llx b:%llx!=%llx
00033803  MMU VA sz %u 0=%zu 1=%zu
0003381c  MMU private !fit: b:%lx<%lx s:%lx>%lx
00033842  GPTBAT !vm export: %x
00033858  PPL handoff !vm export: %x
00033877  Duty cycle
00033888  Sleep count
00033894  Wake count
0003389f  Power state
000338ab  Free heap
000338b5  Total heap
000338c0  Peak heap alloc
000338d0  Used stack
000338db  Total stack
000338e7  CPU count
000338f8  !Mthd:%p
00033901  !msgmbxint
0003390c  !msgdoordashint
0003391c  mme:0x%x
00033925  ThIntr:%u,%u,%u,%u
00033938  ThLock:%p
00033942  Invalid AP power: %d
0003395e  Unbalanced transients
00033974  <null>
0003397e  !Heapblk:%p
0003398a  RTKit: %s - Client: %s
000339a1  rtk_ep_work
000339ad  MGMT msg=0x%llx st=%x
000339c3  MGMT st=%x
000339d2  !clg: %08x
000339dd  Not implemented
000339ed  Message Log
000339f9  !kb reg:%x
00033a05  MBI queue overflow:%s
00033a1b  VmOv %d %d
00033a2f   failures 
00033a42   tests)
00033a55  0123456789abcdef
00033a66  mutex lock failed
00033a78  CXXnew[]:%zu
0004415a  @?fff?
0004d070  lCytuDTRw(
0004d0c8  tnCplSTR
0004d120  tnCkaWTR
0004d178  tffOnOTR
0004d1d0  EERFPHTR
0004d229  LLAPHTR
0004d280  KAEPPHTR
0004d2da  UKTSTR
0004d332  AKTSTR
0004d388  UPCmuNTR
0004d750  not set
000aae93  Rjj)8)
000b23cb  Thb@9`*
000b362a  @9oim8
```
