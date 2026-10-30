# `Firmware/dcp/t8160dcp_restore.im4p`

- File size: 3,016,667 bytes
- IM4P: Tag: IM4P  Type: dcpf  Version: 1
- BuildManifest components that use it: `RestoreDCP`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         dcpf
  Version:      1
  Data:         3.0 MB (3016631 bytes)
  Compression:  LZFSE
  Uncompressed: 17 MB (17039360 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 17,039,360 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `%s: RTKitPMGR cannot config LAPLL for device %d`
- `@(#)PROGRAM:AppleFirmwareKit  PROJECT:AppleFirmwareKit-743.40.4`
- `Apple Inc.`
- `AppleDCP-1317.40.16~1190-t8160dcp.RESTORE`
- `BUILD-INFO[390]:{"DisplayName":"roottask.IOP_ASC8.RELEASE","DisplayVersion":"1223.40.8~1601","BuildTime":"2026-10-03T15:46:14-0700","ProjectName":"pitayaOS","ProductName":"roottask.IOP_ASC8.RELEASE","SourceVersion":"1223.40.8","BuildVersion":"1601","BuildConfiguration":"RELEASE","BuildType":"Officia`
- `RTKit: %s - Client: %s`
- `RTKit_armv8_cl4_Oz_flto_pac-3514.40.18.release`
- `RTKit_release-3504.0.0.0.1.release`
- `Welcome to RTKitPMGR!: %s : t8160`
- `[AFK]DCP Firmware (firmware version:%s RTKit version:%s Variant:RESTORE)`
- `requested IRQ not found (i: %u, RTKit %s: %#x, cL4 %s: %#x)`

## Strings (17,778) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.
First 4,000 of 17,778.

```
00004159  hh8Jhh8?
0000577b  Toii8O
0000ee3b  4hBP9H
0000fd68  crashlog-message
0000fd79  dtm.c:240
0000fd83  coredump-server
0000fd93  coredump-regions
0000fda4  dtm.c:35
0000fdad  ascpower-static-message
0000fdc5  dtm.c:101
0000fdcf  psd-available
0000fddd  psd-p0-before-p6
0000fdee  psd-dashboard
0000fdfc  dtm.c:36
0000fe05  aop_fr
0000fe0c  pwr_state_trans
0000fe1c  offset
0000fe23  dtm.c:63
0000fe32  iop_common.c:356
0000fe43  iop_common.c:358
0000fe54  obj_iop_control.c:86
0000fe69  force_wakeup.c:35
0000fe7b  force_wakeup.c:51
0000fe8d  adt.c:192
0000fe97  adt.c:196
0000fea1  adt.c:198
0000feab  adt.c:209
0000feb5  adt.c:225
0000febf  adt.c:245
0000fece  adt.c:151
0000fed8  adt.c:178
0000fee2  adt.c:34
0000feeb  adt.c:36
0000fef4  bundle.c:156
0000ff01  bundle.c:73
0000ff0d  bundle.c:47
0000ff19  crashlog.c:113
0000ff28  irqmap.c:70
0000ff34  dtm.c:89
0000ff3d  cL4-kernel
0000ff48  dtm.c:254
0000ff52  chosen
0000ff59  dtm.c:258
0000ff63  quirks
0000ff6e  ascwrap
0000ff76  messagebox
0000ff86  wakeup-sources
0000ff99  iack-index
0000ffa4  kic-irq
0000ffac  crashlog-kernel
0000ffbc  dtm.c:409
0000ffc6  dtm.c:42
0000ffd8  legacy-irqs
0000ffe4  interrupts
0000ffef  aic-interrupts
0000fffe  dtm.c:137
00010008  dtm.c:44
00010011  crashlog-user
0001001f  dtm.c:383
00010029  dtm.c:41
00010032  irq.c:172
0001003c  irq.c:258
00010046  irq.c:284
00010050  irq.c:313
0001005a  irq.c:339
00010064  roottask.c:786
00010073  roottask.c:806
00010082  roottask.c:807
00010091  roottask.c:808
000100a0  roottask.c:809
000100af  roottask.c:810
000100be  roottask.c:849
000100cd  roottask.c:850
000100dc  roottask.c:865
000100eb  roottask.c:886
000100fa  roottask.c:899
00010109  roottask.c:910
00010118  roottask.c:913
00010127  roottask.c:925
00010136  roottask.c:927
00010145  roottask.c:929
00010154  roottask.c:934
00010163  roottask.c:936
00010172  roottask.c:938
00010181  roottask.c:940
00010190  roottask.c:945
0001019f  roottask.c:947
000101ae  roottask.c:949
000101bd  roottask.c:951
000101cc  roottask.c:956
000101db  roottask.c:958
000101ea  roottask.c:960
000101f9  roottask.c:965
00010208  roottask.c:967
00010217  roottask.c:969
00010226  roottask.c:973
00010235  roottask.c:994
00010244  roottask.c:995
00010253  roottask.c:998
00010262  roottask.c:1002
00010272  roottask.c:1028
00010282  roottask.c:1031
00010292  roottask.c:1042
000102a2  roottask.c:1055
000102b2  roottask.c:1057
000102c2  roottask.c:382
000102d1  roottask.c:390
000102e0  roottask.c:402
000102ef  roottask.c:456
000102fe  roottask.c:489
0001030d  roottask.c:494
0001031c  roottask.c:496
0001032b  roottask.c:497
0001033a  roottask.c:32
00010348  roottask.c:299
00010357  roottask.c:207
00010366  roottask.c:53
00010374  roottask.c:259
00010383  boot.c:108
0001038e  boot.c:110
00010399  boot.c:112
000103a4  boot.c:115
000103af  timer.c:19
000103ba  exception.c:249
000103ca  exception.c:256
000103da  exception.c:187
000103ea  exception.c:194
000103fa  exception.c:97
00010409  exception.c:111
00010419  exception.c:121
00010429  exception.c:49
00010438  exception.c:59
00010447  obj_arm64_space.c:1290
0001045e  obj_arm64_space.c:1296
00010475  obj_arm64_space.c:1298
0001048c  obj_arm64_space.c:1300
000104a3  obj_arm64_space.c:1302
000104ba  obj_arm64_space.c:1304
000104d1  obj_arm64_space.c:1312
000104e8  obj_arm64_space.c:1323
000104ff  obj_arm64_space.c:1338
00010516  obj_arm64_space.c:1390
0001052d  asc.c:34
00010536  asc.c:43
0001053f  ascwrap.c:45
0001054c  ascwrap.c:230
0001055a  mask.c:161
00010565  mask.c:103
00010570  mask.c:79
0001057a  mask.c:138
00010585  mask.c:169
00010590  mask.c:436
0001059b  msgbox.c:67
000105a7  msgbox.c:161
000105b4  msgbox.c:186
000105c1  msgbox.c:101
000105ce  msgbox.c:287
000105db  obj_plat_cache.c:203
000105f0  coreserver.c:249
00010601  coreserver.c:311
00010612  coreserver.c:50
00010622  coreserver.c:75
00010632  coreserver.c:220
00010643  coreserver.c:242
00010654  coreserver.c:205
00010665  signpost.c:44
00010673  obj_plat_debug_switch.c:235
0001068f  multimer.c:137
0001069e  obj_plat_multimer.c:95
000106b5  aic.c:38
000106be  aic.c:83
000106c7  aic.c:94
000106d0  region.c:21
000106dc  region.c:25
000106e8  region.c:27
000106f4  region.c:29
00010700  region.c:34
0001070c  region.c:36
00010718  region.c:44
00010724  region.c:68
00010730  region.c:70
0001073c  region.c:91
00010748  region.c:93
00010754  region.c:117
00010761  region.c:120
0001076e  region.c:123
0001077b  region.c:125
00010788  region.c:150
00010795  region.c:159
000107a2  region.c:186
000107af  region.c:195
000107bc  boot.c:58
000107c6  boot.c:60
000107d0  boot.c:62
000107da  boot.c:74
000107e4  boot.c:76
000107ee  boot.c:124
000107f9  boot.c:167
00010804  boot.c:184
0001080f  boot.c:29
00010819  boot.c:31
00010823  boot.c:33
0001082d  info.c:30
00010837  ftable.c:267
00010844  ftable.c:270
00010851  ftable.c:281
0001085e  ftable.c:283
0001086b  obj_untyped.c:340
0001087d  obj_untyped.c:342
0001088f  obj_untyped.c:344
000108a1  obj_untyped.c:351
000108b3  obj_untyped.c:21
000108c4  obj_untyped.c:24
000108d5  obj_cnode.c:210
000108e5  obj_cnode.c:218
000108f5  obj_tcb.c:1396
00010904  obj_tcb.c:1400
00010913  obj_tcb.c:1402
00010922  obj_tcb.c:1413
00010931  obj_tcb.c:1417
00010940  obj_tcb.c:1434
0001094f  obj_tcb.c:1441
0001095e  obj_tcb.c:1445
0001096d  obj_tcb.c:1447
0001097c  obj_tcb.c:1454
0001098b  obj_tcb.c:1458
0001099a  obj_tcb.c:1460
000109a9  obj_tcb.c:1467
000109b8  obj_tcb.c:173
000109c6  obj_ep.c:1061
000109d4  obj_notify.c:560
000109e5  obj_irq.c:210
000109f3  obj_irq.c:212
00010a01  obj_irq.c:219
00010a0f  obj_irq.c:248
00010a1d  obj_irq.c:45
00010a2a  obj_debug.c:184
00010a3a  obj_debug.c:38
00011028  __TEXT
00011068  __text
00011078  __TEXT
000110b8  __chain_starts
000110c8  __TEXT
00011108  __constructor
00011118  __TEXT
00011158  __init_offsets
00011168  __TEXT
000111a8  __const
000111b8  __TEXT
000111f8  __cstring
00011208  __TEXT
00011248  __thread_starts
00011258  __TEXT
000112a0  __DATA
000112e0  __const
000112f0  __DATA
00011330  __data
00011340  __DATA
00011380  __mod_init_func
00011390  __DATA
000113d0  __mod_term_func
000113e0  __DATA
00011420  __common
00011430  __DATA
00011480  __DATA
000114c0  __stack_area
000114d0  __DATA
00011518  __DATA_CONST
00011558  __mod_init_func
00011568  __DATA_CONST
000115b0  __LINKEDIT
0001cf1c  h2Ayv*
0002a951  lib uninitialized
0002abb8  BUILD-INFO[390]:{"DisplayName":"roottask.IOP_ASC8.RELEASE","DisplayVersion":"1223.40.8~1601","BuildTime":"2026-10-03T15:46:14-0700","ProjectName":"pitayaOS","ProductName":"roottask.IOP_ASC8.RELEASE","SourceVersion":"1223.40.8","BuildVersion
0002ad4f  roottask.IOP_ASC8.RELEASE 1223.40.8~1601 (Official), built 2026-10-03T15:46:14-0700
0002ada3  panic(app): 
0002adb0  Preempted
0002adba  Canceled
0002adc3  Truncated
0002adcd  CapInvalid
0002add8  SlotInvalid
0002ade4  MethodInvalid
0002adf2  ArgumentInvalid
0002ae02  OperationInvalid
0002ae13  PermissionInvalid
0002ae25  L4 error %s (val:%lu) at %s:%d
0002ae45  lib/public/pitayaos_platform/pitayaos_platform.c
0002ae76  lib/public/pitayaos_platform/pitayaos_platform_timer.c
0002aead  AAPL,phandle
0002aec5  rtkcl4cf
0002aece  invalid appconfig magic
0002aee6  invalid appconfig version
0002af00  invalid appconfig size
0002af17  lib/internal/roottask_console/pl011.c
0002af3d  handle->setup == 1
0002af50  lib/internal/roottask_console/s5l.c
0002af74  Assertion failed loc 0x%zx
0002af8f  (null)
0002af96  0123456789abcdef
0002afa7  vsnprintf.c
0002afb3  _insecure_random_buf.c
0002afca  memcpy.c
0002afd3  strlcat.c
0002afdd  strlcpy.c
0002afe7  strncpy.c
0002aff1  bzero.c
0002aff9  !security_assert: file %s:%d.
0002b018  fwrite.c
0002b021  stack check fail
0002b032  roottask/app/motorcycles/arch/arch.c
0002b057  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITAARCH")[0]) << 24) | ((uint32_t)(("PITAARCH")[1]) << 16) | ((uint32_t)(("PITAARCH")[2]) << 8) | ((uint32_t)(("PITAARCH")[3]))) << 32) | (((uint32_t)(("PITAARCH")[4]) << 24) | ((uin
0002b1ad  Found arch sidecar of version %x. Expected v%u but got v%u
0002b1e9  arch_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITAARCH")[0]) << 24) | ((uint32_t)(("PITAARCH")[1]) << 16) | ((uint32_t)(("PITAARCH")[2]) << 8) | ((uint32_t)(("PITAARCH")[3]))) << 32) | (((uint32_t)(("PITAARCH")[4]) << 24) | ((uin
0002b33f  /chosen/cputrace
0002b350  available
0002b35a  streaming
0002b364  aslr-data
0002b36e  pa-read
0002b376  pa-write
0002b37f  cputrace_handoff->cputrace_info.stream_size == reg_data.length
0002b3be  roottask/app/motorcycles/cputrace/cputrace.c
0002b3eb  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITACPUT")[0]) << 24) | ((uint32_t)(("PITACPUT")[1]) << 16) | ((uint32_t)(("PITACPUT")[2]) << 8) | ((uint32_t)(("PITACPUT")[3]))) << 32) | (((uint32_t)(("PITACPUT")[4]) << 24) | ((uin
0002b541  Found cputrace sidecar of version %x. Expected v%u but got v%u
0002b581  cputrace_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITACPUT")[0]) << 24) | ((uint32_t)(("PITACPUT")[1]) << 16) | ((uint32_t)(("PITACPUT")[2]) << 8) | ((uint32_t)(("PITACPUT")[3]))) << 32) | (((uint32_t)(("PITACPUT")[4]) << 24) | (
0002b6db  roottask/app/motorcycles/template/template.c
0002b708  Template Motorcycle request should never be called
0002b73c  Template Motorcycle patch should never be called
0002b76e  chosen/pitayaos-log-user
0002b787  (!((phys_size) & ((__typeof__((phys_size)))((1ULL << (((12)))) - 1))))
0002b7ce  roottask/app/motorcycles/logbuffer/logbuffer.c
0002b7fd  [logbuffer] Tried to find untyped for %llx
0002b829  (phys_addr >= logbuffer_untyped->base) && (phys_size <= logbuffer_untyped->size)
0002b87a  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITALOGS")[0]) << 24) | ((uint32_t)(("PITALOGS")[1]) << 16) | ((uint32_t)(("PITALOGS")[2]) << 8) | ((uint32_t)(("PITALOGS")[3]))) << 32) | (((uint32_t)(("PITALOGS")[4]) << 24) | ((uin
0002b9d0  Found logbuffer sidecar of version %x. Expected v%u but got v%u
0002ba11  logbuffer_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITALOGS")[0]) << 24) | ((uint32_t)(("PITALOGS")[1]) << 16) | ((uint32_t)(("PITALOGS")[2]) << 8) | ((uint32_t)(("PITALOGS")[3]))) << 32) | (((uint32_t)(("PITALOGS")[4]) << 24) | 
0002bb6c  [sidecar] logbuffer for app %lx has %d logs but only has space for %d
0002bbb3  !__builtin_add_overflow((logbuffer_span->va_base), (next_offset), &logbuffer_handoff->logs[log_index].va)
0002bc1d  !__builtin_add_overflow((next_offset), (((((((log_size) + ((__typeof__((log_size)))((1ULL << (((12)))) - 1)))) & ~((__typeof__((((log_size) + ((__typeof__((log_size)))((1ULL << (((12)))) - 1))))))((1ULL << ((((12))))) - 1)))))), &next_offse
0002bd10  roottask/app/motorcycles/test_harness/test_harness_motorcycle.c
0002bd50  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("TESTHRNS")[0]) << 24) | ((uint32_t)(("TESTHRNS")[1]) << 16) | ((uint32_t)(("TESTHRNS")[2]) << 8) | ((uint32_t)(("TESTHRNS")[3]))) << 32) | (((uint32_t)(("TESTHRNS")[4]) << 24) | ((uin
0002bea6  Found test_harness sidecar of version %x. Expected v%u but got v%u
0002beef  test_harness: test name '%s' (%u bytes) exceeds max name length (%u bytes)
0002bf3b  roottask/app/motorcycles/services/services.c
0002bf68  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITASERV")[0]) << 24) | ((uint32_t)(("PITASERV")[1]) << 16) | ((uint32_t)(("PITASERV")[2]) << 8) | ((uint32_t)(("PITASERV")[3]))) << 32) | (((uint32_t)(("PITASERV")[4]) << 24) | ((uin
0002c0be  Found services sidecar of version %x. Expected v%d but got v%d
0002c0fe  services_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITASERV")[0]) << 24) | ((uint32_t)(("PITASERV")[1]) << 16) | ((uint32_t)(("PITASERV")[2]) << 8) | ((uint32_t)(("PITASERV")[3]))) << 32) | (((uint32_t)(("PITASERV")[4]) << 24) | (
0002c258  shmem_allocation
0002c269  count <= sharedmem_handoff->max_buffer_entry_count
0002c29c  roottask/app/motorcycles/sharedmem/sharedmem.c
0002c2cb  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITASHMB")[0]) << 24) | ((uint32_t)(("PITASHMB")[1]) << 16) | ((uint32_t)(("PITASHMB")[2]) << 8) | ((uint32_t)(("PITASHMB")[3]))) << 32) | (((uint32_t)(("PITASHMB")[4]) << 24) | ((uin
0002c421  Found sharedmem sidecar of version %x. Expected v%u but got v%u
0002c462  sharedmem_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITASHMB")[0]) << 24) | ((uint32_t)(("PITASHMB")[1]) << 16) | ((uint32_t)(("PITASHMB")[2]) << 8) | ((uint32_t)(("PITASHMB")[3]))) << 32) | (((uint32_t)(("PITASHMB")[4]) << 24) | 
0002c5bd  sharedmem_handoff->buffer_entry_count <= sharedmem_handoff->max_buffer_entry_count
0002c610  shmem_subrange_allocation
0002c62a  count <= sharedmem_subrange_handoff->max_buffer_entry_count
0002c666  roottask/app/motorcycles/sharedmem/sharedmem_subrange.c
0002c69e  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("PITASHMR")[0]) << 24) | ((uint32_t)(("PITASHMR")[1]) << 16) | ((uint32_t)(("PITASHMR")[2]) << 8) | ((uint32_t)(("PITASHMR")[3]))) << 32) | (((uint32_t)(("PITASHMR")[4]) << 24) | ((uin
0002c7f4  Found sharedmem_subrange sidecar of version %x. Expected v%u but got v%u
0002c83e  sharedmem_subrange_handoff->header.magic == (((uint64_t)(((uint32_t)(("PITASHMR")[0]) << 24) | ((uint32_t)(("PITASHMR")[1]) << 16) | ((uint32_t)(("PITASHMR")[2]) << 8) | ((uint32_t)(("PITASHMR")[3]))) << 32) | (((uint32_t)(("PITASHMR")[4]) 
0002c9a2  sharedmem_subrange_handoff->buffer_entry_count <= sharedmem_subrange_handoff->max_buffer_entry_count
0002ca07  roottask/app/motorcycles/sharedmem/common.c
0002ca33  snprintf(this_compartment_path, sizeof(this_compartment_path), "%s/%s", compartments_root_path, compartment_name) < sizeof(this_compartment_path)
0002cac5  (status != PITAYAOS_SUCCESS) || (app_uid_size == sizeof(node_app_uid))
0002cb0f  snprintf(buffer, buffer_size, "%s", this_compartment_path) < buffer_size
0002cb58  DT node not found
0002cb6a  roottask/app/motorcycles/bundle_assets/bundle_assets.c
0002cba1  bundle_assets: app uid %lu has more than %u assets
0002cbd5  sidecar_handoff_ptr != ((void*)0)
0002cbf7  sidecar_handoff_ptr->magic == (((uint64_t)(((uint32_t)(("BNDLASTS")[0]) << 24) | ((uint32_t)(("BNDLASTS")[1]) << 16) | ((uint32_t)(("BNDLASTS")[2]) << 8) | ((uint32_t)(("BNDLASTS")[3]))) << 32) | (((uint32_t)(("BNDLASTS")[4]) << 24) | ((uin
0002cd4d  Found bundle_assets sidecar of version %x. Expected v%u but got v%u
0002cd92  bundle_assets: asset name '%s' (%zu bytes incl null) exceeds max %u for app uid %lu
0002cde7  entry_count < 8
0002cdf7  bundle_assets: no untyped covers asset '%s' phys=%llx size=%llx for app uid %lu
0002ce48  app_slot != 0
0002ce56  bundle_assets: mint failed for asset '%s' off=%llx size=%llx app uid %lu err=%d
0002cea7  sidecar_mapping.total_size >= sizeof(sidecar_handoff_header_t)
0002cee6  roottask/app/motorcycles/motorcycles.c
0002cf0d  segment_info.offset <= section_info.bundle_offset
0002cf3f  __sidecar
0002cf49  section_info.bundle_offset == 0
0002cf69  section_info.bundle_offset >= segment_info.offset
0002cf9b  roottask/app/common/application.c
0002cfbd  app%lu has 0 segments
0002cfd4  interface != ((void*)0)
0002cfec  type > APPLICATION_TYPE_DEFAULT && type < APPLICATION_TYPE_MAX
0002d02b  ipc_pid != 0
0002d038  (app->num_vcpus != 0) && (app->irq.dispatch != ((void*)0))
0002d073  !__builtin_sub_overflow((target_metadata_address), (start_metadata_page_address), &va_offset)
0002d0d1  Unknown contig policy %x for app pidx %lx
0002d0fc  app%lu: entry point 0x%lx is in non-executable span [0x%lx-0x%lx] with permissions 0x%x
0002d155  app%lu: entry point 0x%lx is not in any mapped span
0002d18a  roottask/app/common/cnode.c
0002d1a6  app->cnode.slot_count == app->cnode.type_array_entry_count
0002d1e1  app->cnode.slot_count < app->cnode.type_array_entry_count
0002d21b  slot >= app->cnode.base && slot < cap_limit
0002d247  slot >= app->cnode.base && slot < (app->cnode.base + (app->cnode.type_array_entry_count * ((L4_Word_t) (1ULL << (5)))))
0002d2bf  is_slot_index(base, count, slot)
0002d2e0  roottask/app/common/application_internal.h
0002d30b  roottask/app/common/contig.c
0002d328  __ETEXT
0002d330  No SHARED TEXT for app %u for contig policy
0002d35d  No ETEXT segment for app %u for contig policy
0002d38c  __DATA
0002d393  app->exc.levels > 0
0002d3a7  roottask/app/common/exceptions.c
0002d3c8  (app->exc.handlers != ((void*)0)) && (app->irq.dispatch != ((void*)0))
0002d40f  app->resource.frames == total_frames
0002d434  roottask/app/common/frame.c
0002d450  info_span != ((void*)0)
0002d468  roottask/app/common/info.c
0002d483  shared_frame_span != ((void*)0)
0002d4a3  roottask/app/common/ipc.c
0002d4bd  app->irq.dispatch[0].notify_cap != 0
0002d4e2  ipc_shared->slot_base != 0
0002d4fd  roottask/app/common/resource.c
0002d51c  macho TEXT base %#lx not large enough
0002d543  !__builtin_sub_overflow((initial_base), (dynamic_frame_size), &app->space.base)
0002d593  app->image.segments_filled < app->image.segments
0002d5c4  roottask/app/common/segment.c
0002d5e2  src.phys != (~((phys_t)(0)))
0002d5ff  src.virt == (~((word_t)(0)))
0002d61c  must invoke bundler using -include-bss flag
0002d649  dst.virt == (~((word_t)(0)))
0002d666  (src.size != 0) && (dst.size == 0)
0002d689  src.phys == (~((phys_t)(0)))
0002d6a6  (src.size == 0) && (dst.size != 0)
0002d6c9  dst.phys == (~((phys_t)(0)))
0002d6e6  !__builtin_sub_overflow((s->dst.virt), (app->slide), &segment_va)
0002d728  app->image.segments == app->image.segments_filled
0002d75a  mapped_address_space_size <= total_address_space_size
0002d790  untyped_cap != ((L4_Word_t) 0)
0002d7af  roottask/app/common/space.c
0002d7cb  page_count > 0
0002d7da  app %lu TEXT va must be > 0
0002d7f7  !__builtin_add_overflow((app->space.base), (app->slide), &app->space.base)
0002d842  !__builtin_add_overflow((app->space.alloc), (app->slide), &app->space.alloc)
0002d88f  !__builtin_add_overflow((app->space.alloc_end), (app->slide), &app->space.alloc_end)
0002d8e4  !__builtin_add_overflow((app->space.limit), (app->slide), &app->space.limit)
0002d931  !__builtin_add_overflow((app->image.entry), (app->slide), &app->image.entry)
0002d97e  !__builtin_add_overflow((app->image.s[i].dst.virt), (app->slide), &app->image.s[i].dst.virt)
0002d9db  (!((size) & ((__typeof__((size)))((1ULL << (((12)))) - 1))))
0002da18  (!((app->space.alloc) & ((__typeof__((app->space.alloc)))((1ULL << (((12)))) - 1))))
0002da6d  app->space.alloc + size <= app->space.alloc_end
0002da9d  (!((slide) & ((__typeof__((slide)))((1ULL << (((12)))) - 1))))
0002dadc  roottask/app/common/span.c
0002daf7  span >= span_first && span <= span_last
0002db1f  index < span->frame_count
0002db39  app->span.used == app->resource.spans
0002db5f  frame_count > 0
0002db6f  roottask/app/common/span_alloc.c
0002db90  (!((untyped.size) & ((__typeof__((untyped.size)))((1ULL << (((12)))) - 1)))) && untyped.size > 0
0002dbf1  app->span.array != ((void*)0)
0002dc0f  app->span.used < app->resource.spans
0002dc34  app->resource.spans == app->span.used
0002dc5a  roottask/app/common/span_map.c
0002dc79  span->type != L4_Type_Null && span->type <= (sizeof((L4_ObjectSizes)) / sizeof((L4_ObjectSizes)[0]))
0002dcde  span != ((void*)0)
0002dcf1  app->ipc_buffer_size != 0
0002dd0b  roottask/app/common/tcb.c
0002dd25  (app->main_tcb != ((void*)0)) && (app->thread != ((void*)0)) && (app->num_vcpus != 0)
0002dd7b  ipc_span != ((void*)0)
0002dd92  ipc_span->frames_allocated < ipc_span->frame_count
0002ddc5  roottask/app/common/untyped.c
0002dde3  L4_ObjectSizes[type] == ((L4_Word_t) (1ULL << (12)))
0002de18  untyped->limit < (untyped->base + untyped->size)
0002de49  invalid perms %c%c%c for untyped %#llx, %#llx
0002de78  managed_untyped->limit == (managed_untyped->base + managed_untyped->size)
0002dec2  unmanaged_untyped->limit == (unmanaged_untyped->base + unmanaged_untyped->size)
0002df12  compartments/roottask/pitaya-unmanaged
0002df39  %s not present or invalid
0002df54  %s not filled out (%#llx, %#llx)
0002df76  perm %c%c%c not valid for untyped creation
0002dfa2  compartments/roottask/num_vcpus
0002dfc2  roottask/app/common/vcpu.c
0002dfdd  app->num_vcpus <= bootinfo_cpu_count()
0002e004  app->main_tcb != ((void*)0)
0002e020  app->thread != ((void*)0)
0002e03a  app->exc.handlers != ((void*)0)
0002e05a  app->irq.dispatch != ((void*)0)
0002e07a  roottask/app/native/native.c
0002e097  app->logbuffer.num_entries < (sizeof((handoff->logbuffer_entries)) / sizeof((handoff->logbuffer_entries)[0]))
0002e105  APPCONFIG
0002e10f  app->num_vcpus != 0
0002e123  roottask/app/rtkit/rtkit.c
0002e13e  app->num_vcpus <= (((hosted_sidecar_vcpu_t *)(vcpu_sidecar))->v_1_0.num_vcpus)
0002e18d  (segment != ((void*)0)) && (section_va != ((void*)0))
0002e1c3  Unexpected segment: %s
0002e1db  __appconfig
0002e1e7  appconfig_section != ((void*)0)
0002e207  appconfig_data.pdef != ((void*)0)
0002e229  appconfig_data.appconfig != ((void*)0)
0002e250  segment != ((void*)0) && section != ((void*)0)
0002e27f  !__builtin_sub_overflow((section->addr), (segment->vmaddr), &section_offset)
0002e2cc  process-id
0002e2d7  Failed to parse %s appconfig- %s
0002e2f9  native
0002e300  _irq_sidecar
0002e30d  irq->version == ((((1) & 0xFFF) << 4) | (((0) & 0xF) << 0))
0002e349  ptr != ((void*)0)
0002e35b  !__builtin_add_overflow(((int64_t)appconfig->appconfig), (ptr_offset_from_appconfig_section), &roottask_ptr_va)
0002e3cb  app->exc.levels > 0 && app->exc.levels <= 3
0002e3f7  appconfig->vcpu_info != ((void*)0)
0002e41a  pid %u: invalid irq_dispatch_priority %u, values must be between %u and %u inclusive
0002e46f  pid %u: invalid control priority %u, values must be between %u (irq dispatch priority) and %u inclusive
0002e4d7  pid %u: invalid exc_dispatch_priority %u, values must be between %u and %u inclusive
0002e52c  debug_cap != 0
0002e53b  appconfig->fixed_caps.debug != ((void*)0)
0002e565  cache_cap != 0
0002e574  kernel_cache_cap != 0
0002e58a  appconfig->fixed_caps.cache != ((void*)0)
0002e5b4  tcb_cap != 0
0002e5c1  appconfig->fixed_caps.self_tcb != ((void*)0)
0002e5ee  (vectors != ((void*)0)) && (irq_caps != ((void*)0))
0002e622  app->irq.proxy_tcb_caps != ((void*)0)
0002e648  requested IRQ not found (i: %u, RTKit %s: %#x, cL4 %s: %#x)
0002e689  appconfig->fixed_caps.irq_tcb != ((void*)0)
0002e6b5  appconfig->fixed_caps.irq_notification != ((void*)0)
0002e6ea  appconfig->fixed_caps.exc_ep((exc_level), appconfig) != ((void*)0)
0002e72d  appconfig->fixed_caps.exc_tcb((exc_level), appconfig) != ((void*)0)
0002e771  appconfig->fixed_caps.nmi_notification != ((void*)0)
0002e7a6  appconfig->fixed_caps.l2_notification != ((void*)0)
0002e7da  appconfig->fixed_caps.nmi_master_notification != ((void*)0)
0002e816  bind-serror
0002e822  bootinfo_irq_serror_slot() != 0
0002e842  appconfig->fixed_caps.idle_notification != ((void*)0)
0002e878  timer != ((L4_Word_t) 0)
0002e891  timer_irq != ((L4_Word_t) 0)
0002e8ae  timer_slot != 0
0002e8be  appconfig->fixed_caps.timer != ((void*)0)
0002e8e8  appconfig->fixed_caps.timer_irq != ((void*)0)
0002e916  appconfig->fixed_caps.power_notification != ((void*)0)
0002e94d  appconfig->fixed_caps.power != ((void*)0)
0002e977  bootinfo_cpmu_slot() == 0
0002e991  appconfig->pagetracker_va_start != ((void*)0)
0002e9bf  appconfig->pagetracker_va_region_size != ((void*)0)
0002e9f3  channel != ((void*)0)
0002ea09  app != ((void*)0)
0002ea1b  appconfig->data_const_regions_count != ((void*)0)
0002ea4d  appconfig->data_const_regions(region_index, appconfig) != ((void*)0)
0002ea92  pagetracker-impl.inc.h
0002eaab  PGT_ERROR_ALREADY_MAPPED
0002eac4  PGT_ERROR_VA_OUT_OF_RANGE
0002eade  PGT_ERROR_MAPPING_TOO_BIG
0002eaf8  PGT_ERROR_NO_SPLITTING
0002eb0f  PGT_ERROR_MAP_MODES_NOT_COMPATIBLE
0002eb32  PGT_ERROR_NOT_MAPPED
0002eb47  PGT_ERROR_ALLOCATION_FORBIDDEN
0002eb66  PGT_ERROR_UNTYPED_CREATE_FAILED
0002eb86  PGT_ERROR_OUT_OF_CAP_SLOTS
0002eba1  PGT_ERROR_OUT_OF_FRAMEISH_SLOTS
0002ebc1  PGT_ERROR_OUT_OF_TABLE_SLOTS
0002ebde  PGT_ERROR_CANT_REMAP_PARTIAL
0002ebfb  unknown pgt_error_t value
0002ec15  build/inc/RTK_hosted/pagetracker/pagetracker-impl.inc.h
0002ec4d  !pgt_assert_success (%s): %s:%d
0002ec6d  !parent table when importing
0002ec8a  duplicate import
0002ec9b  too many tables imported
0002ecb4  untyped (%s) !aligned
0002ecca  untyped (%s) !size
0002ecdd  untyped (%s) !cap_slot
0002ecf4  roottask/app/rtkit/pt_setup.c
0002ed12  pt_setup_state(app) != 0
0002ed2b  pt_setup_state(app) != ((void*)0)
0002ed4d  ai != ((void*)0)
0002ed5e  build/inc/RTK_hosted/pagetracker/pagetracker-basics.h
0002ed94  !pgt_assert (%s:%d)
0002eda8  !mode %#x
0002edb2  pagetracker-bits.h
0002edc5  overflow
0002edce  pa=0x%llx size=0x%llx cap_slot_idx=0x%x
0002edf6  build/inc/RTK_hosted/pagetracker/pagetracker-bits.h
0002ee2a  !tree depth
0002ee36  !space +future_untyped_count
0002ee53  !tree index
0002ee5f  untyped (%s) overlaps with (%s)
0002ee7f  pt_setup_state(app)->limits.future_table_count > 0
0002eeb2  pdef != ((void*)0)
0002eec5  app != ((void*)0) && ai != ((void*)0) && span != ((void*)0)
0002ef01  %s called with invalid type %s
0002ef21  import_table_span
0002ef33  L4_Type_Null
0002ef40  L4_Type_Root
0002ef4d  L4_Type_Zombie
0002ef5c  L4_Type_Untyped
0002ef6c  L4_Type_CNode
0002ef7a  L4_Type_Tcb
0002ef86  L4_Type_Ep
0002ef91  L4_Type_Reply
0002ef9f  L4_Type_Notify
0002efae  L4_Type_Irq
0002efba  L4_Type_Debug
0002efc8  L4_Type_Arm64_PageTableLevel2
0002efe6  L4_Type_Arm64_PageTableLevel1
0002f004  L4_Type_Arm64_PageTableLevel0
0002f022  L4_Type_Arm64_FrameLevel2
0002f03c  L4_Type_Arm64_FrameLevel1
0002f056  L4_Type_Arm64_FrameLevel0
0002f070  L4_Type_IOP_Timer
0002f082  L4_Type_Plat_Cache
0002f095  L4_Type_Plat_AscPower
0002f0ab  L4_Type_Plat_DebugSwitch
0002f0c4  L4_Type_IOP_Control
0002f0d8  L4_Type_Plat_Asc
0002f0e9  app != ((void*)0) && ai != ((void*)0) && frame != ((void*)0)
0002f126  frame->type == L4_Type_CNode
0002f143  import_frame
0002f150  Unable to satisfy untyped: %llx/%llx
0002f175  __MACHO
0002f18b  roottask/lib/libbundleparser/bundle_parser.c
0002f1b8  Failed to find segment %s for app %llu
0002f1e0  component != ((void*)0)
0002f1f8  entry != ((void*)0) && data_out != ((void*)0) && data_size_out != ((void*)0)
0002f245  /compartments/
0002f254  compartments_ctx.valid
0002f26b  roottask/lib/libbundleparser/dt_extractor.c
0002f297  [DT] The name of compartment %u exceeds our buffer size. It needs to be at least 0x%lx bytes
0002f2f4  [DT] Error %ld extracting compartment %u
0002f31d  compartment_node_ctx.valid == 1
0002f33d  metadata
0002f346  private-dt-mapped
0002f358  secure-compartment
0002f36b  /segments
0002f375  -segment-asset-
0002f385  length <= 8
0002f391  roottask/include/lib/bundle_parser.h
0002f3bc  is-pie
0002f3c3  entry-point
0002f3cf  status != PITAYAOS_ERROR_SMALL_BUFFER
0002f3fa  reference/
0002f405  Failed to find reference node in DT for pid  %llx under macho segment %s
0002f44f  vm-prot
0002f457  file-size
0002f461  binary-id
0002f46b  virtual-addr
0002f478  virtual-size
0002f485  record-number
0002f493  segment-name
0002f4a0  sections
0002f4a9  offset
0002f4b0  /compartments/roottask/nmi_irq_interrupt
0002f4d9  Failed to correctly apply NMI IRQ(%d) contained in DT = %lu
0002f516  compartments/roottask/nmi_first_crash_override
0002f545  (!((crashlog_va) & ((__typeof__((crashlog_va)))((1ULL << (((12)))) - 1))))
0002f590  roottask/lib/libcrashlog/crashlog.c
0002f5b4  _global_crashlog->num_agents >= 2
0002f5d6  !__builtin_sub_overflow((_global_crashlog->size), (multi_crashlog_agent->offset), &multi_crashlog_size)
0002f63e  !__builtin_add_overflow(((uintptr_t)(_multi_crashlog)), (roottask_crashlog_agent->offset), (uintptr_t *)&_crashlog)
0002f6b2  !__builtin_sub_overflow(((uintptr_t)_multi_crashlog), ((uintptr_t)_global_crashlog), &multi_crashlog_offset)
0002f71f  !__builtin_add_overflow((multi_crashlog_offset), (agent_info->offset), &current_entry_offet)
0002f77c  !__builtin_add_overflow((_global_crashlog_phys_addr), (current_entry_offet), &crashlog_entry_pa)
0002f7dd  !__builtin_add_overflow((app_crashlog_untyped.base), (entry_size), &app_crashlog_untyped.limit)
0002f83d  !__builtin_add_overflow((_global_crashlog_untyped_slice.untyped_offset), (current_entry_offet), &entry_untyped_offset)
0002f8b4  (cputrace_metadata_va != 0) && (!((cputrace_metadata_va) & ((__typeof__((cputrace_metadata_va)))((1ULL << (((12)))) - 1)))) && (region_size > 0)
0002f945  roottask/lib/libcputrace/cputrace.c
0002f969  !__builtin_add_overflow(((uintptr_t)_system_info), (region_size), &_max_address)
0002f9ba  !__builtin_add_overflow(((uintptr_t)_system_info), (sizeof(cputrace_system_info_t)), &_next_address)
0002fa1f  _next_address <= _max_address
0002fa3d  !__builtin_add_overflow((num_apps), (1), &num_apps)
0002fa71  !__builtin_add_overflow((total_size), (sizeof(cputrace_app_info_t)), &total_size)
0002fac3  !__builtin_add_overflow((_next_address), (sizeof(cputrace_app_info_t)), &_next_address)
0002fb1b  (app != ((void*)0)) && (_next_address <= _max_address)
0002fb52  !__builtin_add_overflow((num_images), (1), &num_images)
0002fb8a  !__builtin_add_overflow((total_size), (sizeof(cputrace_image_info_t)), &total_size)
0002fbde  !__builtin_add_overflow((_next_address), (sizeof(cputrace_image_info_t)), &_next_address)
0002fc38  roottask/lib/libeventgate/eventgate.c
0002fc5e  Too many panic callbacks registered
0002fc83  We already passed this type: %x vs %x
0002fcaa  bit_count == 1
0002fcb9  Eventgate shutdown did not shutdown the system
0002fce9  magic-flipper-rtc-addr
0002fd00  magic-flip-point
0002fd11  roottask/lib/libhashtable/hashtable.c
0002fd37  table->table == ((void*)0)
0002fd52  table->table != ((void*)0)
0002fd6d  swap_count < table.capacity
0002fd89  We iterated over the whole hashtable and were unable to insert %llx
0002fdcd  ipc.head == ((void*)0)
0002fde4  roottask/lib/libipc/ipc.c
0002fdfe  ipc channel id/cpid/spid %lu/%lu/%lu %s %s %s
0002fe2d  memory
0002fe3a  node != ((void*)0)
0002fe4d  mismatched
0002fe58  roottask/lib/libirq/irq.c
0002fe72  (logbuffer_va != 0) && (!((logbuffer_va) & ((__typeof__((logbuffer_va)))((1ULL << (((12)))) - 1)))) && (logbuffer_region_size > 0)
0002fef5  roottask/lib/liblogbuffer/logbuffer.c
0002ff1b  !__builtin_add_overflow((logbuffer_va), (logbuffer_region_size), &logbuffer_va_top)
0002ff6f  (_log_entries_base_va + next_offset) <= logbuffer_va_top
0002ffa8  !__builtin_add_overflow((next_offset), (((((((log_entry->size) + ((__typeof__((log_entry->size)))((1ULL << (((12)))) - 1)))) & ~((__typeof__((((log_entry->size) + ((__typeof__((log_entry->size)))((1ULL << (((12)))) - 1))))))((1ULL << ((((12
000300b7  !__builtin_add_overflow((app_log_entries_total_size), (((((((this_entry->size) + ((__typeof__((this_entry->size)))((1ULL << (((12)))) - 1)))) & ~((__typeof__((((this_entry->size) + ((__typeof__((this_entry->size)))((1ULL << (((12)))) - 1)))
000301e8  !__builtin_sub_overflow((_log_entries_base_va), ((uintptr_t)_system_log_header), &log_entries_offset_from_header)
0003025a  !__builtin_add_overflow((log_entries_offset_from_header), (app_log_entries_lowest_offset), &this_app_log_entries_offset)
000302d3  !__builtin_add_overflow((_global_logbuffer_untyped->base), (this_app_log_entries_offset), &this_app_log_entries_base)
00030349  !__builtin_add_overflow((app_logbuffer_untyped.base), (app_logbuffer_untyped.size), &app_logbuffer_untyped.limit)
000303bb  /compartments
000303cf  snprintf(dt_path, sizeof(dt_path), "%s/%s", compartments_root_path, compartment_name) < sizeof(dt_path)
00030437  appUID
0003043e  (status == PITAYAOS_SUCCESS) && (app_uid_size == sizeof(app_uid))
00030480  pitayaos-logs-
00030491  strlcat(dt_path, "/", sizeof(dt_path)) < sizeof(dt_path)
000304ca  strlcat(dt_path, compartment_child_name, sizeof(dt_path)) < sizeof(dt_path)
00030516  strlcat(dt_path, log_entry_name, sizeof(dt_path)) < sizeof(dt_path)
0003055a  log-name
00030563  (status == PITAYAOS_SUCCESS) && (log_entry_8cc_size == sizeof(log_entry_8cc))
000305b6  (status == PITAYAOS_SUCCESS) && (log_entry_size_size == sizeof(log_entry_size))
00030606  !__builtin_add_overflow((total_buffer_size_for_app_uid), (((((((this_entry->size) + ((__typeof__((this_entry->size)))((1ULL << (((12)))) - 1)))) & ~((__typeof__((((this_entry->size) + ((__typeof__((this_entry->size)))((1ULL << (((12)))) - 1
0003073d  !"Mach-O validation failed"
00030759  roottask/lib/libmachoparser/macho-parser.c
00030784  (pidx >= 2) && (pidx < (2 + nmi.app_notify_count))
000307b7  roottask/lib/libnmi/nmi.c
000307d1  %s NMI, pidx: %lu
000307e4  timeout
000307ec  nmi.app_notify_next < nmi.app_notify_count
00030817  application_count > 0 && application_count <= ((((sizeof(L4_Word_t) * 8) - 4)) / 2)
0003086b  coredump-server
0003087b  chosen/stop-clocks-enabled
00030896  nmi-timeout-seconds
000308aa  nmi.timeout_seconds > 0
000308c2  (ret == ((L4_Error_t) (8))) || (ret == (((((L4_Word_t) (0))) << 8) | (((L4_Word_t) (((L4_Error_t) (0)))))))
0003092e  external
00030937  roottask
00030940  watchdog
0003094d  %lu unexpected
0003095c  nmi_exc_endpoint != 0
00030972  roottask/lib/libnmi/exc.c
0003098c  pidx != 0
00030996  thread_exc_ep != 0
000309a9  unhandled exception from tcb %lx '%s' PIDX %u
000309d7  power_state_debug_buffer != ((void*)0)
000309fe  roottask/lib/libpower/power.c
00030a1c  get_state_machine_current_state() == STATE_WAIT_FOR_PARTICIPATION_COUNT
00030a64  CONTRACT VIOLATION!
00030a78  (current_fsm_state == STATE_CALCULATE_VOTES) || (current_fsm_state == STATE_WAIT_FOR_PARTICIPATION_COUNT)
00030ae2  current_state == STATE_WAIT_FOR_PARTICIPATION_COUNT
00030b16  /compartments/roottask/power-management/idle-timeout-init
00030b50  /compartments/roottask/power-management/idle-timeout-min
00030b89  /compartments/roottask/power-management/idle-timeout-default
00030bc6  /compartments/roottask/power-management/cl4-retention-autodetect
00030c07  chosen/psd-available
00030c1c  /compartments/roottask/power-management/power-num-debug-buffer-entries
00030c63  notification_bit_num < ((2) + (power_resources.app_count * (2)))
00030ca4  notification_bit_num >= (2)
00030cc0  app_selector <= (((sizeof(L4_Word_t) * 8) - (2)) / (2))
00030cf8  %s app%lu (non-participating) sent a power notification
00030d31  %s app[%lu] lowest_state(%#x): only DRAM_OFF and FORCED_REQUEST flags can be set
00030d83  %s app%lu cur_state(%#x) must == subsystem-ON state(%#x)
00030dbd  %s app%lu cur_state (%#x) notification must >= for LEAST_ON in state (%u)
00030e08  %s app%lu curr_state(%#x) must == req_state(%#x) for forced-req
00030e49  %s app%lu lowest_state(%#x) forced-flag must == 0 for >= LEAST_ON curr_state notification
00030ea4  %s app%lu curr_state(%#x) must == req_state(%#x) on wake
00030ede  %s app%lu curr_state(%#x) notification received on wake
00030f17  %s app[%lu] sent a current_state update during wake
00030f4c  %s app%lu declined forced-req
00030f6b  %s app%lu declined req with invalid curr_state(%#x), exp_state(%#x)
00030fb0  transition_maps[i].state_func != ((void*)0)
00030fdc  %s participating app%lu curr_state(%#x) at boot = IGNORE
00031016  get_state_machine_current_state() == STATE_CALCULATE_VOTES
00031051  %s app%lu forced-req!=prev req(%#x)
00031076  get_state_machine_current_state() == STATE_WAIT_FOR_APPS_IDLE
000310b4  get_state_machine_forced_request_flag() == 0
000310e1  (current_fsm_state == STATE_WAIT_FOR_POWER_STATE_TRANSITIONS) || (current_fsm_state == STATE_WAIT_FOR_WAKE_TRANSITIONS)
00031159  get_state_machine_forced_request_flag() == 1
00031186  get_state_machine_current_state() == STATE_BROADCAST_POWER_STATE_CHANGE
000311ce  get_state_machine_current_state() == STATE_DO_HW_POWER_STATE_CHANGE
00031212  %s app%lu woke by irq during forced-req
0003123b  %s app%lu woke early with invalid curr_state(%#x), exp_state(%#x)
0003127e  (ret == (((((L4_Word_t) (0))) << 8) | (((L4_Word_t) (((L4_Error_t) (0))))))) || (ret == (((((L4_Word_t) (0))) << 8) | (((L4_Word_t) (((L4_Error_t) (1)))))))
0003131b  get_state_machine_current_state() == STATE_BROADCAST_WAKE
00031355  power.participating_apps_bitfield == 0
0003137c  /compartments/roottask/power-management/power-service-enabled
000313ba  irq_notification != 0 && power_index < power_resources.app_count
000313fb  roottask/lib/libpower/power_setup.c
0003141f  power_resources.app_notify_cap_array != 0
00031449  primary_slot != 0 && power_index < power_resources.app_count
00031486  power_resources.power_shared_page.va != 0
000314b0  application_count > 0 && application_count <= (((sizeof(L4_Word_t) * 8) - (2)) / (2))
00031506  ((word_t)((1ULL << (12)))) >= (application_count * sizeof(cl4_power_tcb_info_t))
00031557  power_resources.idle_timer_irq_cap != 0
0003157f  roottask/lib/libservices/services.c
000315a3  Got message %x but failed to find app by pidx %d
000315d5  App pidx %ld has reported twice with return code of %d and overwriting %d
00031620  One or more apps failed, panicking
00031644  roottask.IOP_ASC8.RELEASE
0003168a  roottask/src/boot.c
0003169e  space_alloc != ((void*)0) && address_count > 0
000316cd  type <= (sizeof((L4_ObjectSizes)) / sizeof((L4_ObjectSizes)[0])) && L4_ObjectSizes[type] == ((L4_Word_t) (1ULL << (12)))
00031746  space_alloc != ((void*)0) && slot != 0
0003176d  space_alloc->next < space_alloc->limit
00031794  space_alloc->type <= (sizeof((L4_ObjectSizes)) / sizeof((L4_ObjectSizes)[0])) && L4_ObjectSizes[space_alloc->type] == ((L4_Word_t) (1ULL << (12)))
00031827  pitayaos_hashtable_u64_init(&bootinfo.irq.table)
00031858  bootinfo.reclaimed_frame_count > 0
0003187b  frames_found == bootinfo.reclaimed_frame_count
000318aa  pitayaos_hashtable_u64_deinit(&bootinfo.irq.table)
000318dd  (!((requested_size) & ((__typeof__((requested_size)))((1ULL << (((12)))) - 1))))
0003192e  (!((base_unmanaged) & ((__typeof__((base_unmanaged)))((1ULL << (((12)))) - 1))))
0003197f  Failed to get untyped for %llx %llx
000319a4  !__builtin_sub_overflow((boot_untyped->base + boot_untyped->size), (boot_untyped->limit), &remaining)
00031a0a  unmanaged untyped (%#llx, %#llx) OOM. %#llx requested, %#llx remaining
00031a52  boot_untyped->base <= untyped.base
00031a75  _cnode_alloc.next < _cnode_alloc.limit
00031a9c  index < (((word_t)(sizeof(bootinfo.timer) / sizeof((bootinfo.timer)[0]))))
00031ae7  cap_array != ((void*)0)
00031aff  _space_alloc.next < _space_alloc.limit
00031b26  !__builtin_add_overflow((base), (bootinfo.untyped_unmanaged[i].size), &limit)
00031b74  !__builtin_add_overflow((phys), (min_size), &desired_end)
00031bae  !__builtin_sub_overflow((phys), (untyped->base), &slice.untyped_offset)
00031bf6  !__builtin_sub_overflow((untyped->size), (slice.untyped_offset), &slice.slice_size)
00031c4a  index < bootinfo.untyped_unmanaged_count
00031c73  size > 0
00031c7c  (!((phys_addr) & ((__typeof__((phys_addr)))((1ULL << (((12)))) - 1))))
00031cc3  While mapping %llx/%lx we failed to find a cap for %llx
00031cfc  !__builtin_add_overflow((next_allocation_va), (((L4_Word_t) (1ULL << (12)))), &allocation_limit)
00031d5d  !__builtin_add_overflow((allocation_limit), (((L4_Word_t) (1ULL << (12)))), &allocation_limit)
00031dbc  raw_addr != ((void*)0)
00031dd3  thread != ((void*)0)
00031de8  size != 0 && (!((size) & ((__typeof__((size)))((1ULL << (((12)))) - 1))))
00031e32  size <= (bootinfo.untyped.size - used)
00031e59  type <= (sizeof((L4_ObjectSizes)) / sizeof((L4_ObjectSizes)[0]))
00031e9a  type_requires_entire_frame(type)
00031ebb  !type_requires_entire_frame(type)
00031edd  type_allocator->next < type_allocator->limit
00031f0a  created == 0
00031f17  !__builtin_sub_overflow((*pa), (untyped->base), &offset)
00031f50  untyped_slice.slot != ((L4_Word_t) 0)
00031f76  created == 1
00031f83  mapped == 0
00031f8f  mapped == 1
00031f9b  roottask/src/bootinfo_entry.c
00031fb9  L4_BootInfo_Space_GetAsid(entry) != ((L4_Asid_t) -1)
00031fee  bootinfo->untyped_unmanaged_filled < bootinfo->untyped_unmanaged_count
00032035  index < (((L4_Word_t) (sizeof(bootinfo->timer) / sizeof((bootinfo->timer)[0]))))
00032086  _regions != ((void*)0)
0003209d  roottask/src/bundle.c
000320b3  variable_base > 0
000320c5  app_segment != ((void*)0)
000320df  graceful_shutdown_opt_out
000320f9  __COMPONENTNAME
00032109  contig-policy-override
00032120  contig-policy
0003212e  __COMPONENTTYPE
0003213e  component_type != ((void*)0)
00032163  bundle offset %#lx not present in bundle regions
00032195  /bundle/bundle-regions
000321ac  _region_count > 0
000321be  bundle_regions_ctx.valid == 1
000321dc  bundle_parser_get_app_macho_meta(app_uid) != ((void*)0)
00032214  __DATA_CONST
00032221  OSK_01
00032228  OSK_02
0003222f  OSK_03
00032236  OSK_04
0003223d  OSK_05
00032244  OSK_06
00032250  app_type != ((void*)0)
0003226f  status == PITAYAOS_SUCCESS
0003228a  region_ctx.valid == 1
000322a0  bundle-offset
000322ae  bundle-size
000322ba  physical-addr
000322ce  (NULL)
000322d5  0123456789ABCDEF
000322e6  %s assert: (%s) %s:%d
000322fd  assert: (%s) %s:%d
00032311  roottask/src/debug.c
00032326  assert: (%s)
0003235a  L4_ErrorPreempted
0003236c  L4_ErrorCanceled
0003237d  L4_ErrorTruncated
0003238f  L4_ErrorCapInvalid
000323a2  L4_ErrorSlotInvalid
000323b6  L4_ErrorMethodInvalid
000323cc  L4_ErrorArgumentInvalid
000323e4  L4_ErrorOperationInvalid
000323fd  L4_ErrorPermissionInvalid
00032417  Unknown
0003241f  %s %s != L4_Success -> (val: %lu) %s:%d
00032448  %s != L4_Success -> (val: %lu) %s:%d
0003246e  %s != L4_Success -> (val: %lu)
00032494  Implemented
000324a0  Initialized
000324ac  Invalid Parameters
000324c5  Small Buffer
000324d2  End of Resource
000324e2  Generic
000324ea  Message 
000324f3  Receive
000324fb  Incorrect
0003250b  %s %s%s != Success -> %s:%d
00032528  %s%s != Success -> %s:%d
00032542  %s%s != Success
00032553  panic(pitayaOS): 
00032565  roottask/src/dt_helpers.c
0003257f  app_uid >= BUNDLE_KERNEL_UID
0003259c  dt_suffix != ((void*)0)
000325b4  value_out != ((void*)0)
000325cc  dt_suffix_len <= 32
000325e0  comp != ((void*)0)
000325f3  Trying to create context from %zx %zx
0003261a  prop_name != ((void*)0) && value_out != ((void*)0)
0003264d  roottask/src/ipc_buffer.c
00032667  (buffer_size != 0) && (!((buffer_size) & ((__typeof__((buffer_size)))((1ULL << ((((3 + 6))))) - 1))))
000326cd  allocator != ((void*)0) && allocator->alloc_func != ((void*)0)
0003270c  allocator->buffer_size != 0
00032728  roottask/src/launch.c
0003273e  __MACHOHEADERLC
0003274e  __TEXT
00032755  text_segment.offset != 18446744073709551615ULL
00032784  No macho header found for uid %lu
000327a7  app != ((void*)0) && app_mapping != ((void*)0) && app_pid > 0
000327e5  app_mapping != ((void*)0)
000327ff  macho != ((void*)0)
00032813  app != ((void*)0) && app_mapping != ((void*)0)
00032842  heap_size
0003284c  heap_size_str == ((void*)0)
00032868  emit-code-coverage
0003287b  uuid != ((void*)0)
0003288e  roottask/src/main.c
000328a2  (user_entropy_0 != 0) && (user_entropy_1 != 0)
000328d1  arm,pl011
000328db  apple,dockchannel
000328ed  apple,s5l-uart
000328fc  console,null
00032920  compatible
0003292f  Not implemented yet
00032944  physical_addr[0] != 0 && physical_addr[1] != 0
00032973  pitaya_console_register_pl011(uart_va, physical_addr[1])
000329ac  pitaya_console_register_s5l(uart_va, physical_addr[1])
000329e3  chosen/crashlog-user
000329f8  chosen/cputrace/aslr-data
00032a12  chosen/roottask-profile
00032a2a  Could not find crashlog untyped at %llx
00032a6e  roottask/include/roottask.h
00032a90  roottask/src/shim.c
00032aa4  roottask/src/thread.c
00032aba  (L4_Word_t)(stack_top) % 16 == 0
00032adb  liblibc_threading_ready() == 1
00032afa  Not reachable
00032b09  config->entry.sync != ((void*)0) || config->entry.async != ((void*)0)
00032b4f  config->entry.async == ((void*)0) || (((config->flags) & ((1UL << 1))) != 0)
00032b9c  !(((config->flags) & ((1UL << 1))) != 0) || config->entry.async != ((void*)0)
00032bea  (((ep->flags) & ((1UL << 31))) != 0)
00032c0f  pitayaos_platform_self() == ep->threadcap
00032c39  stack_size > 0
00032c48  ep->async_entry != ((void*)0)
00032c66  ep->sync_entry != ((void*)0)
00032c83  application_count > 0
00032c99  roottask/src/usage.c
00032cae  _reclaimed_size == 0
00032cc3  (!((reclaimed_mem) & ((__typeof__((reclaimed_mem)))((1ULL << (((12)))) - 1))))
00032d12  !__builtin_sub_overflow((_milestone_entries[i].usage.managed_used), (_reclaimed_size), &_milestone_entries[i].usage.managed_used)
00032d94  !__builtin_sub_overflow((bootinfo_untyped_limit()), (bootinfo_untyped_base() + _reclaimed_size), &managed_used)
00032e04  (milestone < MEMORY_USAGE_MILESTONE_MAX) && (milestone > MEMORY_USAGE_MILESTONE_INVALID) && (_milestone_entries[milestone].filled == 0)
00032e8c  _milestone_entries[milestone - 1].filled == 1
00032eba  (_application_entries_total != 0) && (_application_entries_filled < _application_entries_total)
00032f1a  !__builtin_sub_overflow((managed_size), (managed_used), &managed_free)
00032f71  name_len <= 10
00032f80  backed
00032f87  shared
00032f8e  contig
00032f95  pos contig
00032fa0  managed
00032fa8  stack_area_size % sizeof(uint64_t) == 0
000333b4  H&SmJ.TmL6UmN>VmB
00033aff  <8bunz8
00037e69  haNGja
00037f34   haNAha
00038211  haNSjaN
0003908d  haN%ja
00039104  RhaNbja
0003a798  Kht8k!
0003a7f8  Qht81"
0003a9e8  kil8k!
0003ab38  kim8k!
0003ac04  kil8k!
00057987  Q_AIka
0005f6fb  qH(EzK
0005fc5f  7hVA9h
0005fc67  6hZA9(
0006119c  _h(8Hhw
000611e4  _h(8Hhw
00061523  JTig8q
00070692  @9|N@yaR@y`
00075b9c  hFB9iBB9
00075f7f  TLa@9-
00075fb3  T{FA9iBA90
000760ef  ThNA9H
000761f3  4hBA9uB
00079e3b  TaBA9b"D
0007b598  xBAyyFAyz^Ay{bAy
000846b7  7hFA9H
00091720  hFC9]y
0009a713  ThnP9(
0009b467  RhnP9h
0009b773  7hBHy)
000a31f7  ThFR9P
000afffb  TUX@)X
000c755f  6hrK9H
000c7985  bG9hbK9
000c79f6  \8hbK9
001212df  Rb2Hzi6
0012d38f  4hBB9H
00134817  4hBB9H
0013a8db  4hbF9H
0013abe0  ibF9hv
0013af07  4hbF9H
0013c126  G9JAB9
0013c266  C9JAB9,
00156f20  )Ih8HIh8
00157027  Rmij8J
001570b3  9mii8)
001571c7  9lii8)
00157717  RLii8)
0017855f  2Lh(8Mih8
0017d816  Y8hfI9(!
00184016  ]8ibU9
00195c08  hBp9x_
001b289a  @9hBH8
001e86fb  Thb@9h
001f1787  ylyix)
001f1c29  sJyn.S)
001f2bc3  ThBA9h
001f40e0  hJh8I{h
001f5584  ,klx,k-xL
001f6049  zhxi*@
001f6831  {uxi*@
002005ce  @9-Q@xjA
002052d6  @yoy-x
002054fe  @yoy-x
00205ab3  TMy)x{vCy
00205d7b  TMy)xu
0020601f  Tny*xn
002060ff  *azCy|
002062c3  Tny*xnzCy
002082a3  T*QBx_
002082c3  T*QBx_
0020c5a1  yvxJyvx)
0020d8ff  TpvYyoRly
0020d912  YyoVly?
0020d91f  T`zYyoZly
0020d932  Yyobly?
0020da30  pvYy`zYyq
0020dcae  DygJVy
0020dcbe  Eyg&Ey
0020dcce  EygRVy
0020dcde  EygZVy
0020df76  Byg"By
0020df9c  gnCyfJVy
0020dfab  Tt~CyfNVy
0020dfbb  TurCyfRVy
0020dfce  CyfZVy
0020e0cc  gnCyurCyt~Cyv
0020eb34  oylxninx
0020eb53  4iYixj
0020ef33  4'RBxE
00210136  PyuvCyjzCy8
002101a1  {nxQ{nx
002101ff  RNyhxoyhx
002102c1  {nxQ{nx
0021031f  RNyhxoyhx
0021245e  fyv~Yy|
002124bb  R/{mxp{mx
0021251f  R.ylxOylx
00212c83  TanBy",
00213003  Qhzxx 
002131ab  TMAry.Ary
0021320b  TMAry.Ary
00213271  AryNAry
002132f3  TnAryOAry
00213359  AryNAry
0021339d  AryoAry
00213421  ArypAry
0021350d  ArypAry
0021359b  T+AryLAry
002135bb  T+AryLAry
002135db  TLArymAry
0021362f  T+AryLAry
00213647  T+AryLAry
00213667  TKAry,Ary
0021367f  TLArymAry
002136a1  Ary+Ary_
002136bf  TlAryMAry
002136f9  ArynAry
00213715  ArylAry_
00213999  ArylAry?
002139ed  AryJAry
00213a11  AryJAry
00213a4d  AryJAry
00213a9d  ArykAry
00213af9  ArymAry
00213e49  Bry1Bry
00213f01  AryQAry
00213f41  AryQAry
00213f59  Ary+Ary_
00213fd1  Ary+Ary_
002140c5  AryLAry
002140e5  Ary-Ary
00214141  ArylAry_
00214161  Ary+Ary_
00214181  AryKAry?
00214199  Ary+Ary_
00214231  Ary-Ary
0021437d  Ary+Ary_
00214395  Ary+Ary_
002143cb  T+AryLAry
002143ed  Ary+Ary_
00214633  TLAry.Ary
0021467d  Ary+Ary_
00214695  Ary+Ary_
002146b5  Ary-Ary
002146f9  AryOAry
002147f1  AryLAry
00214821  ArylAry_
00214841  Ary+Ary_
0021485d  AryOAry
0021487d  AryKAry?
00214895  Ary+Ary_
002148dd  Ary+Ary_
002148f9  Ary+Ary_
002149ad  AryNAry
00214a4d  AryPAry
002156db  9KIE9?
00215ed7  9KIE9?
00217ec7  TMABy.ABy
00217f1b  TMABy.ABy
00217f75  AByNABy
00217fe7  TnAByOABy
00218041  AByNABy
00218081  AByoABy
002180f5  ABypABy
002181c5  ABypABy
0021824f  T+AByLABy
0021826f  T+AByLABy
0021828f  TLABymABy
002182e3  T+AByLABy
002182fb  T+AByLABy
0021831b  TKABy,ABy
00218333  TLABymABy
00218355  ABy+ABy_
00218373  TlAByMABy
002183ad  ABynABy
002183c9  ABylABy_
00218629  ABylABy?
00218675  AByJABy
00218699  AByJABy
002186d1  AByJABy
0021871d  ABykABy
00218775  ABymABy
002189f5  ABy0ABy
00218b25  ABy0ABy
00218b5d  ABy+ABy_
00218bc1  ABy+ABy_
00218ca5  AByLABy
00218cc5  ABy-ABy
00218d15  ABylABy_
00218d35  ABy+ABy_
00218d55  AByKABy?
00218d6d  ABy+ABy_
00218df1  ABy-ABy
00218efd  ABy+ABy_
00218f15  ABy+ABy_
00218f4b  T+AByLABy
00218f6d  ABy+ABy_
00219143  TLABy.ABy
00219185  ABy+ABy_
0021919d  ABy+ABy_
002191bd  ABy-ABy
002191f9  AByOABy
002192e1  AByLABy
00219311  ABylABy_
00219331  ABy+ABy_
0021934d  AByOABy
0021936d  AByKABy?
00219385  ABy+ABy_
002193cd  ABy+ABy_
002193e9  ABy+ABy_
00219485  AByNABy
00219515  AByOABy
0022c1f3  7hFa9H
0024466c  ibB9jb
0025335c  Jiv8h&
002730f4  irJ9hf@
00277b7b  7h{xx){xxJ{xx
002866ed  kt8Zyt
002ac1eb  7hnG9(
002adefc  Qio8Bi`8Aip8?
002adf58  Bin8@io8
002b4b29  yjxny*x
002b589b  RNyhx.y(xnyh
002b5938  +yhxKy(xk
002b68cc  Lyixly)x)
002b7e83  RoyixOy)x
002b7f2f  R,yhxLy(x
002b7feb  R+yhxkz(x
002c48db  RhB!9-Y
002cb473  RhB!9G>
002d189f  RhB!9<%
002d3bf4  kil8KA
002d642c  kil8KA
002e139f  RadanBdan
002e1464  lyhx,y(
002e6758  hkv8)'@
002e792c  hR]yiV]yk
002ef844  Hq@yIy@yJ
002f41f8  HGAyICAy*}
002f446b  *+{hxl[@
002f4a9b  =0FAy BJ
002f5700  kyzxk}
002f5948  )ytxjZ@
002f6007  TiFD9h"@
002f6213  TiFD9h"@
002f6797  TiFD9j"@
002f81e3  *VXfx7
0030265c  4UA)WaA)
003026b0  5]A)ZmA)
003051b0  )Q_9JQs93
003076db  R-yhxNyhx
00307743  RNyixoyix)
0030a01c  4UA)WaA)
0030c57b  6h"Byi
00319c5b  Rmyix.
00319efb  RmyjxN
00319fcf  Rmyix.
0031c648  jBDyiFDy
0031ea93  TirR9?
00320227  Rcyj|c
00320283  Rcyj|c
00320cef  Tcyd|c
00320e9f  TIyCy_
00321f9c  jBDyiFDy
0032445f  TirR9?
0032543f  Rcyj|c
0032549b  Rcyj|c
00325b4f  Tcyd|c
00325cff  TIyCy_
003288b1  khx){v
00329020  /ko8pyj
0032afa0  jzByK}
0032b497  *hrC9j
0032b9c4  h:Byv>ByiFBywIj
0032c0a7  5jvByJ5
0032c0ff  TjrByJ5
0032c59f  TirC9?
0032c9e3  TirC9?
0032eecb  R.yhxNy(
0032f3b3  ThrC9)
0032f414  hBE9iNA
0032fb27  Tv~Byw
00330d84  jzByK}
003310b4  jJByK}
003315b3  *hrC9j
00331adb  TvjByynBywzBy
00331af4  v:Byy>BywFBy
00331b10  v:Byy>BywvBy`
003321fb  5jvByJ5
00332253  TjrByJ5
003326f3  TirC9?
00332cef  TirC9?
00334b97  RkjkxjjjxJ}
00334c7f  Rijixhjhx`B
00334edb  R.yhxNy(
0033502f  Rkjkxj}
0033507f  ROyixoy)
00335103  Rijixhjhx`B
0033559f  ThrC9)
00335600  hBE9iNA
0033592f  Rjjjxijix)}
00335ac3  RkjkxjjjxJ}
00335c37  RjjjxijixS
00335c8b  Rjjjxijix)}
00335e13  RkjkxjjjxJ}
00335f83  Rjjjxijix+
00335fd7  Rjjjxijix)}
00336153  Tv~Byw
00346d18  *yjxB@
00371944  WaA)ZmB)Ji@9
0038488b  Rij989
0038ad3c  jZGyk^Gy)
00398080  v]A)zmB)km@9
0039f5c0  k<Ayl 
0039f7c3  yj<Ayi$
00424da7  Thr@9I
0043bc5f  ?8bunz8
0043c3bf  ?UUUUUU
0043c427  ?bXM`8q
0043d1f0  8bunz8
0043d960  UUUUUU
0043fcad  G1@(knN
0043fcf4  DispTarget150_D90
004400b0  DispTargetP61
004400be  DispTargetS61
004400cc  power_enable
004400d9  tb-transport-wl
004400e9  trusted-route-wl
004400fa  hid-route-wl
00440107  hid-transport-wl
00440118  hid-device-wl
00440126  endpointWL
00440131  system-server-wl
00440142  hpd-server-wl
00440150  hpd-down-wl
0044015c  hpd-up-wl
00440166  dcpexpert-service
00440178  system
0044017f  AFKDiagnostics
0044018e  HeapUsage
00440198  ThreadInfo
004401a3  compartment
004401af  system-epic
004401bb  test-service
004401c8  test-epic
004401d2  display-clock-manager
004401e8  pmgr-dcp0-service
004401fa  pmgr-dcp1-service
0044020c  pmgr-dcpext0-service
00440221  mcw-service-sec
00440231  mcw-service
0044023d  dptx-generic-sdp-count
00440254  disp0-service
00440262  disp0-epic
0044026d  disp1-service
0044027b  dispext0-service
0044028c  brightness-service-v6x
004402a3  cb-ap-to-dcp-service-v6x
004402bc  cb-ap-to-dcp-service-epic
004402d6  brightness-service-v68p
004402ee  cb-ap-to-dcp-service-v68p
00440308  brightness-service-v68s
00440320  cb-ap-to-dcp-service-v68s
0044033a  brightness-service-v68s-doe1
00440357  cb-ap-to-dcp-service-v68s-d1
00440374  brightness-service-x3200
0044038d  transportType
0044039b  cb-ap-to-dcp-service-x3200
004403b6  transport-stub
004403c5  controller-pmu-frontend
004403dd  brightness-service-v61p
004403f5  cb-ap-to-dcp-service-v61p
0044040f  brightness-service-v61s
00440427  cb-ap-to-dcp-service-v61s
00440441  cbroot-service
00440450  cbxtalk-service
00440460  cbgenx-service
0044046f  cbrootservice-epic
00440482  cb-x3200-telemetry-zEDC
0044049a  cbtelemetry-X3200-service
004404b8  dcp-trusted-client
004404cb  aon-hpd-down-tb-client
004404e2  gpio-service
004404ef  dispsec-spi
00440503  nesos-driver
00440510  tcon-service
0044051d  tcon-epic
00440527  bim-epic
00440530  tcon-iboot
0044053b  disp-health-mon-tb-client
00440555  tcon-iboot-tb-proxy
00440569  dcpav-dptx0-root-nub
0044057e  dcpav-dptx0-root-service
00440597  dbv-sdp-channel-index
004405ad  hdcp_fuse_mask
004405bc  dcpav-dptx0-core0-nub
004405d2  dcpav-dptx0-port0-nub
004405e8  dcpav-sac-controller
004405fd  dcpav-dptx-sec-root-nub
00440615  dcpav-dptx-sec-root-service
00440631  dcpav-dptx-sec-core0-nub
0044064a  dcpav-dptx-sec-port0-nub
00440663  dcpav-dptx1-root-nub
00440678  dcpav-dptx1-root-service
00440691  dcpav-dptx1-core0-nub
004406a7  dcpav-dptx1-remote-port0-nub
004406c4  aon-hpd-up-tb-server
004406d9  dcpexpert-epic
004406e8  endpoints
004406f2  generate-route-config
00440708  trusted-route
00440716  dptx-monitor-tb-if-client
00440730  disp-health-mon-tb-if-client
0044074d  aon-hpd-down-tb-if-client
00440767  aon-hpd-up-tb-if-server
0044077f  dcptrustedclient-tb-interface
0044079d  brightness-util-tb-client
004407b7  tcon-iboot-tb-interface
004407cf  tcon-debug-tb-interface
004407e7  tcon-epic-tb
004407f4  tcon-bim-tb-interface
0044080a  bim-epic-tb
00440816  {&RTK_platform_mbi_config}
00440831  ap-route
0044083a  afkdcp-smc-service-ep
00440850  afksmc-service
0044085f  afkdcppsec-smc-service-ep
00440879  powerlog-service
0044088a  powerlog-epic
00440898  md-manager
004408a3  aop-route-dcp0
004408b2  aop-route-dcp1
004408c1  aop-test
004408ca  aop-test-control-epic
004408e0  pwr-cntr-untrusted-v6x
004408f7  pwr-cntr-untrusted-v68-pri
00440912  pwr-cntr-untrusted-v68-sec
00440932  display-manager
00440948  alscolorxtalk
00440956  als-dcp-frontend
00440967  als-dcp-frontend-sec
0044097c  dcp-control
00440988  dcp-sec-control
00440998  dptx-monitor-tb-ep
004409ab  disp-health-mon-tb-ep
004409c1  aon-hpd-tb-down-ep
004409d4  aon-hpd-tb-up-ep
004409e5  dcptrustedclient-tb-ep
004409fc  brightness-util-tb-ep
00440a12  tcon-iboot-tb-ep
00440a23  tcon-debug-tb-ep
00440a34  tcon-bim-tb-ep
00440a43  management-ep
00440a51  syslog-ep
00440a5b  kdebug-ep
00440a65  tracekit-ep
00440a71  oslog-ep
00440a7a  report-ep
00440a84  iomfb-link
00440a8f  tcon-ep
00440a97  bim-ep
00440a9e  system-ep
00440aae  dcpexpert-ep
00440abb  disp0-ep
00440ac4  dcpav-controller-ep
00440ad8  dcpav-power-ep
00440ae7  dcpav-sac-ep
00440af4  dcpav-device-ep
00440b04  dcpav-service-ep
00440b15  dcpav-interface-ep
00440b28  dcpdptx-port-ep
00440b38  dcpdptx-hdcp-ep
00440b48  cbservice-ep
00440b55  cb-ap-to-dcp-service-ep
00440b6d  aop-comms-dcp0-ep
00440b7f  aop-comms-dcp1-ep
00440bb0  RTKSTACK
00440c08  tTxEhTTR
00440d81  Qkkbal
0044103f  -0123456789abcdef0123456789ABCDEF
00441080  SPMIv02
004410a4  RTKit_armv8_cl4_Oz_flto_pac-3514.40.18.release
00441cb8  AAPL,phandle
00441cc5  afklib
00441cd8  service_id
00441cf0  afklib
00441cfd  afklib
00441d04  physical-layer-wl
00441e40  local_stop_state
00441e51  local_shtdn_state
00441e63  remote_stop_state
00441e75  user_stop_state
00441f73  DebugState
004420b8  md-allocator
004420c5  md-al-remote
00442138  register_local_power
0044214d  register_remote_power
00442163  power_state_msg_mask
00442178  remote_power_msg_mask
0044218e  workloops
00442198  dispatchqueues
004421a7  cache-size
004421f8  logEvent
00442201  clientId
0044220a  service-up
00442215  event-count
00442221  posted-event-count
00442234  cache-buffer
00442241  cache-cursor
00442298  SharedMemoryOffset
004422ab  gAFKConfigLogMask
004422bd  force-panic
004422cf  totalAllocCount
004422df  totalBytes
004422ea  usedBytes
004422f4  freeBytes
004422fe  <unknown>
00442308  stackSize
00442312  stackUsed
004423a0  system-service
004423af  reg-size-inc
004423bc  reg-stream-block-size
004423d2  handler-workloop
004423e3  handler-dispatch-queue
004423fa  service-matching
00442430  transport-wl
0044243d  server-wl
00442447  async-activation
00442458  assert-service
00442467  panic-on-assert-failure
0044247f  uhbr-rates
0044248a  max-lane-count
00442499  min-lane-count
004424a8  supports-auxless-alpm
004424be  max_lane_count
004424cd  min_lane_count
004424f5  HDCPProtocolType
00442506  no-virtual-display
00442519  hpdUnplugTime
00442527  deglitch
00442530  ignore-rodco-roleakcomp-fuse
0044254d  max_pixel_clock
0044255d  PixelClockLimit
0044256d  Suspended
00442577  alpm-data
00442581  wakeupLines
0044258d  wakeupCRSymbols
004425cc  auxPowerUpLines
004425dc  auxPowerUpWaitTime
004425ef  wakeupTPS1Length
00442600  wakeupTPS2Length
00442611  dptxWrap-seq2-pwrdn3-count
0044262c  enable-trusted-aon-hpd
00442643  dcp-lpdptx-port-epic
00442658  supports-ssc
00442665  pclkdrv-select
00442674  phy-ldo-bypass
00442683  driveSettings-rbr
00442695  driveSettings-hbr
004426a7  driveSettings-hbr2
004426ba  driveSettings-hbr3
004426d0  frequency
004426da  noiseWidth
004426e5  sacDivisor
004426f0  dcpdptx-port-epic
0044271b  MaxActivePixelRate
0044272e  MaxTotalPixelRate
00442740  MaxPixelWidth
0044274e  supports-phy-ps
0044275e  no-dptx-src-sel
00442785  max_link_rate_2_lanes
0044279b  max_link_rate_4_lanes
004427b1  alpm-shutdown-errata
004427c6  aux_ch_ctl_2
004427d3  fixed-m-vid
004427df  force-video-bist-master-mode
004427fc  dp-crc-support
0044280b  adaptive-sync
00442819  no-psr
00442820  no-fec
00442827  foce-dptx-pll-lock
0044283f  aux-log-size
0044289d  alpm_ctl_1
004428a8  alpm_ctl_2
004428b3  hdcp_requested
004428c2  lane-map
004428cb  pn-inv
004428d2  target-require-talisman-wa
004428ed  target-require-abdc-wa
00442904  target-require-color-desat-wa
00442922  target-capture-tcon-state-on-unplug
00442946  target-require-x3442-vghl-wa
00442963  min_link_rate
00442971  max_link_rate
0044297f  max_training_pattern
00442994  external_link_symbol_clock
004429af  default-power-state
004429c3  hot_plug_delay_ms
004429d5  hot_unplug_delay_ms
004429e9  flexible-v-timing
004429fb  max-generic-sdp-count
00442a11  virtual-dpcd
00442a1e  require-trusted-aux-trigger
00442a3a  require-trusted-link-debug-ctl
00442a59  require-trusted-video-ctl1
00442a74  VideoStreamEnabled
00442a87  AUXTimeoutCount
00442a97  AUXLog
00442a9e  send-dmsg
00442aa8  dcpdptx-hdcp-interface
00442abf  vid-fifo-threshold
00442bdc  dp-phy-fifo-threshold
00442bf2  dcpdptx-hdcp-auth-session
00442c0c  supports-dsc
00442c19  supports-alternative-target
00442c35  boot-args-prefix
00442c46  max_dsc_bpp
00442c52  aod-data
00442c74  lcd-off-on-ms
00442c82  support-headless-state
00442c99  support-tcon-power-mitigation
00442cb7  control-rails
00442cc5  pp1v24-power
00442cd2  pp1vx-power
00442cde  vccmain-power
00442cec  qbuck-power
00442cf8  refclk-gpio
00442d04  reset-gpio
00442d0f  xsync-on-to-pp1vx-delay
00442d27  pp1v24-on-to-pp1vx-delay
00442d40  ref-clk-on-to-rst-delay
00442d58  vccmain-on-to-qbuck-delay
00442d72  qbuck-on-to-refclk-delay
00442d8b  rst-off-to-ref-clk-delay
00442da4  pp1vx-off-to-pp1v24-delay
00442dbe  pp1vx-sleep-min
00442dce  pp1vx-power-on-override
00442de6  lcd-enable
00442df1  lcd-spi-clk
00442dfd  lcd-spi-mosi
00442e0a  lcd-spi-cs
00442e15  backlight-enable
00442e26  backlight-pmic-enable
00442e3c  tddi-ngpio
00442e47  lcd-on-to-spi-clk-delay
00442e5f  lcd-on-to-bl-pmic-delay
00442e77  lcd-on-to-bl-delay
00442e8a  bl-pmic-off-to-bl-delay
00442ea2  bl-pmic-off-to-lcd-delay
00442ebb  lcd-on-to-tddi-delay
00442ed0  tddi-to-lcd-off-delay
00442ee6  lcd-enable-no-power-off
00442efe  backlight-enable-no-power-off
00442f1c  backlight-pmic-enable-no-power-off
00442f3f  dptx-secure-monitor
00442f53  secure-aux-support
00442f66  dptx-register-capture-done
00442f81  coverglass-serial-number-size
00442f9f  pmgr-id-wa
00442faa  tcon-model
00442fb5  display-pmic-debug-panic
00442fce  InitializeTCON
00442fe3  panel-serial-number
00442ff7  DisplayPower
00443004  tcon-firmware-version
0044301a  tcon-ECID
00443024  tcon-BNCH
0044302e  tcon-life
00443038  tcon-SDOM-fused
00443048  tcon-PROD-fused
00443058  tcon-SDOM-value
00443068  tcon-PROD-value
00443078  tcon-cfg-hash
00443086  tcon-cfg-hash-result
0044309b  tcon-cfg-auth
004430a9  tcon-cfg-version
004430ba  tcon-module-info
004430cb  tcon-boot-status
004430dc  tcon-failsafe-data
004430ef  client-handle
004430fd  useDirectNits2iDAC
00443110  LmaxProduct
0044311c  lMaxProduct
00443128  LmidProduct
00443134  lMidProduct
00443140  LminProduct
0044314c  lMinProduct
00443231  iDAC2MilliAmpsTable
00443245  mA2Nits2ndOrderCoef
00443259  mA2Nits1stOrderCoef
0044326d  mA2Nits0thOrderCoef
00443281  lMinReachable
0044328f  miniDAC
00443297  midiDAC
0044329f  maxiDAC
004432a7  nitsAtMaxCode
004432bb  current-for-max-backlight
004432d5  current-for-mid-backlight
00443309  pmu-controller
00443318  smc-enable-key
00443327  bl-initial-state
00443338  smcKey
0044333f  dispatch-queue-label
00443354  lediMax
0044335c  dimmingRatio
00443369  LmaxReachable
00443377  LminPWMaximization
0044338a  LminReachable
00443398  DBVMin
0044339f  DBVMax
004433a6  panel-gamma
004433b2  formula-max-nits
004433c3  tap-linear-nits
004433d3  lMidPanel
004433e8  Display (Event Forward)
00443400  BrightnessUtil
0044340f  UNSERIALIZABLE
00443423  CBServiceiOSs
00443449  CBAOPEndpoint
00443457  genx-request-id
00443467  genx-sample
00443473  requestID
0044347d  timestamp
00443487  channelCount
00443494  measurementCount
004434a5  luxResidency
004434b2  countsBE
004434bb  LExpAvg
00443551  >GB7ZJB
00443571  $VBzvWB1
0044357e  ZBkk[B
004435e2  jB"NjBV}jB
004435f6  kB*:kB_ikB
0044360a  kB2&lBgUlB
00443665  4pB&dpB[
00443679   qB.PqBc
0044368e  rBP<rB
004436a2  rBX(sB
004436a9  WsBdisplayState
004436b9  av_min_sample_rate_lpcm
004436d1  av_max_sample_rate_lpcm
004436e9  av_min_sample_size_lpcm
00443701  av_max_sample_size_lpcm
00443719  av_min_channel_count_lpcm
00443733  av_max_channel_count_lpcm
0044374d  CPCapabilities
0044375c  DisplayAsleep
0044376a  Time To Light Measurements
00443785  dcpav-controller-epic
0044379b  WakeDisplay
004437a7  SleepDisplay
004437cc  dcpav-device-epic
004437de  av-no-virtual-audio
004437f2  EventLog
004437fb  RegisterSets
00443808  ProtectionType
00443817  ProtectionOptions
00443829  Protection
00443834  SourceSupport
0044385a  AudioProperties
0044386a  VideoProperties
0044387a  HDRStaticMetadata
0044388c  InfoFrames
00443897  CPFailureCount
004438a6  DSCCapabilities
0044390c  FRLCapabilities
00443963  LinkQuality
004439a0  AllElements
004439ac  TiledDisplayInfo
004439bd  DisplayAllocation
004439cf  dcpav-service-epic
004439e2  Charactor error rate exceeded
00443a00  CP failure rate exceeded
00443a19  Capabilities changed
00443a2e  FRL error rate exceeded
00443a46  FRL capabilities changed
00443a5f  RotationMin
00443a6b  RotationMax
00443a77  RotationIncrement
00443a89  BoundsSupport
00443ac7  Rotation
00443ad0  ColorDitherRemoval
00443ae3  VSDBElements
00443b05  hdmi-frl-enable
00443b2e  FRLSinkRateMax
00443b3d  FRLSinkRateDSCMax
00443b4f  FRLDFPRateMax
00443b5d  Identifier
00443b68  SingleEnclosure
00443b78  BezelInfoPresent
00443b9f  ForceSingleTile
00443bb9  Bottom
00443bcb  BezelInfo
00443bd5  TileSize
00443bde  TileTopology
00443beb  MainUFP
00443bf3  PeerUFP
00443bfb  ExtraPipes
00443c06  UseSingleTile
00443c85  LG HDR 4K
00443dab  ]^_bcd?@/
00444279  MaxTMDSClock
0044429b  MaxTMDSClockDivisor
004442c4  HasHDMILegacyEDID
004442d6  MaxPixelClock
004442e4  SupportsBT2020YCC
004442f6  SupportsBT2020cYCC
00444328  MaxFrameAverage
00444338  Luminance
004444ec  SupportsStandby
004444fc  SupportsSuspend
0044450c  SupportsActiveOff
00444550  WhitePoints
00444575  MinimumRefreshRate
00444588  MaximumRefreshRate
004445f4  Waiting
004445fc  Measuring
00444606  Monitoring
00444611  Recovery
00444633  HDCPReauthRequests
00444660  Physical Address
00444671  StartInfoFrame
00444680  StopInfoFrame
004446bd  dcpav-video-interface-epic
004446d8  PrepareLink
004446e4  StartLink
004446ee  DidStartLink
004446fb  UpdateLink
00444706  WillStopLink
00444713  StopLink
0044471c  CompleteLink
00444729  dcpav-interface
00444739  AudioElements
00444747  dcpav-audio-interface-epic
00444762  IOAVCECInterface
00444773  dcpav-cec-interface-epic
0044478c  reg-nodebug-0
0044479a  reg-nodebug-1
004447a8  reg-redact-0
004447b5  reg-redact-1
004447c6  HDCP Capable
004447d3  Downstream Established
004447ea  Repeater
004447f3  StatusVersion
00444801  HDCPTXVersion
0044480f  HDCPTopology
00444820  Success
00444828  Unknown Failure
00444950  ProductName
004449f5  ContrastFactorMin
00444a07  ContrastFactorMax
00444a4e  SupportsPQEOTF
00444a5d  SupportsHLGEOTF
00444a6d  SupportsBT2020RGB
00444b04  device-reset-id
00444b14  power-ltr
00444b58  Reserved
00444b61  telemetry-mapping
00444b73  telemetry-indices
00444b8b  IsVirtual
0044504c  ColorModes
004450a2  IsOverscanned
004450b0  IsPreferred
004450bc  IsPromoted
004450c7  ScanInformation
004450d7  ValidPixelEncodings
004450eb  TimingType
004450f6  AspectRatio
00445102  PreciseAspectRatio
00445115  UpstreamFormat
00445124  TimingStandard
00445169  HorizontalPipeCount
0044517d  VerticalPipeCount
0044518f  StandardType
0044519c  DownstreamFormat
004451ad  WhitePoint
004451b8  DisplayLuminance
00445214  MaxChannelCount
00445224  StreamSampleRate
00445250  ElementData
0044525c  ActiveChannelCount
0044526f  ChannelLayout
0044527d  ChannelAllocation
0044528f  dcpav-sac-epic
0044529e  dcpav-power-epic
004452af  with-panic-handler
004452c2  panicb-gpio
004452ce  ignore-remote-power-disp-pmic
004452ec  dcpav-power-interface
0044f2f0  ProtectLink
0044f2fc  ReprotectLink
0044f30a  UnprotectLink
0044f318  RestartInterfaces
0044f32a  Link Command
0044f337  Protection Command
0044f34a  Link Command (with source)
0044f365  Protection Command (with source and AUP data)
0044f393  Set Power
0044f39d  Hot Plug
0044f3a6  Add Child
0044f3b0  Remove Child
0044f3bd  LinearPCM
0044f3e9  OneBitAudio
0044f3ff  WMAPro
0044f40b  Dolby Atmos (EAC3)
0044f41e  Dolby Atmos (EAC3 7.1)
0044f435  Dolby TrueHD (MAT1.0)
0044f44b  Dolby TrueHD (MAT2.0)
0044f461  Dolby Atmos (MAT2.0)
0044f476  Dolby TrueHD (MAT2.1)
0044f48c  Dolby Atmos (MAT2.1)
0044f4a1  Front Left
0044f4ac  Front Center
0044f4b9  Front Right
0044f4c5  Front Left Center
0044f4d7  Front Right Center
0044f4ea  Rear Left
0044f4f4  Rear Center
0044f500  Rear Right
0044f50b  Rear Left Center
0044f51c  Rear Right Center
0044f52e  Low Frequency Effects
0044f544  Front Left Wide
0044f554  Front Right Wide
0044f565  Front Left High
0044f575  Front Center High
0044f587  Front Right High
0044f598  Top Center
0044f5a3  Master
0044f5aa  Capture
0044f5b8  Horizontal
0044f5c3  Vertical
0044f5cc  RGB 4:4:4
0044f5d6  YCbCr 4:2:0
0044f5e2  YCbCr 4:2:2
0044f5ee  YCbCr 4:4:4
0044f5fa  DolbyVision (native)
0044f60f  DolbyVision (HDMI tunneling)
0044f62c  YCbCr 4:2:2 (DP tunneling)
0044f647  YCbCr 4:2:2 (HDMI tunneling)
0044f664  DolbyVision LL YCbCr 4:2:2
0044f67f  DolbyVision LL YCbCr 4:2:2 (DP tunneling)
0044f6a9  DolbyVision LL YCbCr 4:2:2 (HDMI tunneling)
0044f6d5  DolbyVision LL YCbCr 4:4:4
0044f6f0  DolbyVision LL RGB 4:4:4
0044f709  GRGB Tunneled as YCbCr422 (Even line blue)
0044f734  GRGB Tunneled as YCbCr422 (Even line red)
0044f763  Limited
0044f76b  Traditional gamma (SDR)
0044f783  Traditional gamma (HDR)
0044f79b  SMPTE ST 2084 (PQ)
0044f7ae  BT.2100 HLG
0044f7ba  Default RGB
0044f7c6  SMPTE 170M/BT.601
0044f7df  xvYCC601
0044f7e8  xvYCC709
0044f7f1  sYCC601
0044f7f9  DolbyVision VSVDB
0044f810  AdobeYCC601
0044f81c  AdobeRGB
0044f825  BT.2020 (YcCbcCrc)
0044f838  BT.2020 (YCbCr)
0044f848  BT.2020 (RGB)
0044f856  DCI-P3 (D65)
0044f863  DCI-P3 (Theater)
0044f87a  scRGBfixed
0044f885  External
0044f88e  Embedded
0044f8a3  Upstream
0044f8ac  Intermediate
0044f8c2  Vendor Specific
0044f8d6  Product Description
0044f8f4  Dynamic Range & Mastering
0044f912  CVTv1X
0044f919  CVTv2X
0044f920  Overscan
0044f929  Underscan
0044f933  Selectable
0044f943  CEAShortID
0044f964  Unprotected
0044f970  Negotiating
0044f97c  Protected
0044f9aa  48 Gbps (12Gbps/lane * 4 lanes)
0044f9ca  40 Gbps (10Gbps/lane * 4 lanes)
0044f9ea  32 Gbps (8Gbps/lane * 4 lanes)
0044fa09  24 Gbps (6Gbps/lane * 4 lanes)
0044fa28  18 Gbps (6Gbps/lane * 3 lanes)
0044fa47  9 Gbps (3Gbps/lane * 3 lanes)
0044fa65  0 Gbps (FRL disabled)
0044fa7b  ? Gbps (Unknown FRL rate)
0044fa95  FRLCurrentRate
0044faa4  FRLTargetRate
0044fab2  LinkType
0044fabb  LinkTime
0044fac4  LinkData
0044fad3  PixelEncoding
0044fae1  DynamicRange
0044faf3  Colorimetry
0044fb14  VerticalAttributes
0044fb27  IsInterlaced
0044fb34  IsSplit
0044fb3c  LinkID
0044fb48  IsMirroring
0044fb5a  Timing
0044fb61  VRREnabled
0044fb6c  LLMEnabled
0044fb77  MergeEnabled
0044fb84  DSCBitsPerPixel
0044fb94  DSCPassthrough
0044fba3  DSCParameters
0044fbb7  FrontPorch
0044fbc2  SyncWidth
0044fbcc  BackPorch
0044fbd6  Active
0044fbdd  SyncRate
0044fbe6  PreciseSyncRate
0044fbf6  SyncPolarity
0044fc03  PixelRepetition
0044fc13  Version
0044fc1b  SupportsVBR
0044fc3f  SupportsRGB
0044fc4b  SupportsYCbCr444
0044fc5c  SupportsYCbCr422
0044fc6d  SupportsYCbCr420
0044fc95  Supports8bpc
0044fca2  Supports10bpc
0044fcb0  Supports12bpc
0044fcbe  LineBufferBitDepth
0044fcd1  MinBppIncrement
0044fce1  MaxSliceWidth
0044fcef  SliceCapabilityMask
0044fd03  RateBufferBitCount
0044fd16  PeakThroughputMode0
0044fd2a  PeakThroughputMode1
0044fd3e  MaxBpp444
0044fd48  MaxBpp420
0044fd52  Format
0044fd59  ChannelCount
0044fd66  SampleSize
0044fd71  LinkSampleRate
0044fd80  IOAVInterface
0044fd8e  IOAVVideoInterface
0044fda1  IOAVAudioInterface
0044fdb4  IOAVAudioDriver
0044fdc4  IOAVCECService
0044fddf  commandMask
0044fdeb  eventMask
0044fdf5  eventCapacity
0044fe03  Device Enumeration
0044fe16  Interface Enumeration
0044fe2c  Modes Validation
0044fe3d  Interface Enumeration -> Mode Set
00450045  testMode
0045004e  cpTypesMask
0045005a  hdcp.protocolMask
0045006c  CPProtocol
00450077  RegisterSetName
00450087  RegisterSetData
00450097  RegisterSetType
004500c0  RegisterSetOffset
004500d2  RegisterCount
004500e0  RegisterSize
004500f2  Return
004500f9  EventRaw
00450102  EventClass
0045010d  EventTime
00450117  EventPayload
00450124  Command
0045012c  CommandStatus
0045013a  ProtectionStatus
0045014b  EncryptionStatus
0045015c  AUPPacket
00450166  Reason
0045016d  PortID
00450174  HPDState
0045017d  HPDSuppressed
00450190  Status
00450197  CommandReason
004501a5  ElementType
004501b1  VendorID
004501be  Payload
004501c6  EPICName
004501cf  EPICUnit
004501d8  EPICLocation
004501e5  EPICProviderClass
004501f7  power-on-sequence
00450209  power-off-sequence
0045021c  power-rails
00450228  offset
00450235  vsgpio-scratch-v1px-cmd-valid
00450253  vsgpio-scratch-resetb-cmd-valid
00450273  vsgpio-scratch-common-string
00450290  vsgpio-scratch-pmu-status
004502aa  vsgpio-v1px-on-value
004502bf  vsgpio-v1px-off-value
004502d5  vsgpio-resetb-low-value
004502ed  vsgpio-resetb-high-value
00450306  vsgpio-resetb-gpce-trigger
00450321  vsgpio-v1px-gpce-trigger
0045033a  resetb-config
00450348  pp1vx-config
00450355  gpce-trigger-config
00450369  pp1vx-on-to-rst-delay
0045037f  rst-off-to-pp1vx-delay
00450396  pp1vx-off-to-xsync-delay
004503af  panel-min-sleep-delay
004503c5  prior-rst-off-delay
004503d9  PanelPowerStatus
004503f0  edp-sac-allow-tap-change
00450409  cdi-sac-noisewidth
00450420  cdi-sac-enable
0045042f  edp-sac-exclude-ranges
00450446  cdi-sac-exclude-ranges
0045045d  AgileBaseTap
0045046a  AgileTap
00450477  sac-enable
00450482  edp-sac-enable
004504ab  Supported
004504b5  CurrentIndex
004504c2  PendingIndex
004504cf  AggressorTable
004504f3  alpm-enable
004504ff  supports-detailed-panel-id
0045051a  panic-training-failure-retries
00450539  TCONErrorCount
00450548  dpcd-brightness-base-address
00450565  dpcd-brightness-minimum-value
00450583  dpcd-brightness-maximum-value
004505a1  dpcd-brightness-big-endian
004505c4  alpdpLinkRate
004505d2  virtual-temp-fmt
004505e3  supports-raw-panel-id
004505f9  dbv-sdp-line-trigger
0045060e  edpASSRMode
0045061a  enhancedMode
00450627  downspread
0045063d  fecMode
00450645  laneCount
0045064f  linkRate
00450658  maxPattern
00450663  laneScrambleSeed
00450695  encoding
004506a4  colorimetry
004506b5  interlaced
004506c0  axis-0
004506cd  active
004506d4  syncWidth
004506de  backPorch
004506e8  frontPorch
004506f3  syncPolarity
00450700  pixelRepetition
00450710  pixelRate
0045071a  ratioType
00450724  scanInformation
00450734  ecid_uuid
0045073e  tps1-ml-to-aux-delay-us
00450766  TrainLink
00450770  Link Training Command
004507a5  Symbol Error Rate Measurement Pattern
004507d1  80-bit custom pattern
004507e7  CP2520 Pattern 1
004507f8  CP2520 Pattern 2
00450809  CP2520 Pattern 3
0045081f  Source
00450826  VoltageSwing
00450833  PreEmphasis
00450844  EnhancedMode
00450851  Downspread
0045085c  LaneCount
00450866  LinkRate
0045086f  DriveSettings
0045089c  IODPController
004508ab  LaneMapping
004508b7  MinLaneCount
004508c4  MinLinkRate
004508d0  MinLinkRateScalar
004508e2  MaxLinkRateScalar
004508f4  ScramblingInhibited
00450908  dcpdp-controller-epic
0045092d  pHDMIg
00450938  $SYNAa
004509c4  dcpdp-device-epic
00450a0e  Revision
00450a17  SupportsALPM
00450a24  SupportsASSR
00450a31  SupportsDSC
00450a3d  SupportsFEC
00450a49  SupportsPSR
00450a79  MaxLinkRate
00450ab1  SupportsDownspread
00450ae3  DownstreamPortCount
00450af7  DownstreamPortTypes
00450b0b  Updated
00450b13  IOAVDevice
00450b1e  IODPDevice
00450b29  ALPMEnabled
00450b73  SupportsPanelReplay
00450b9f  FECEnabled
00450baa  DSCEnabled
00450bd8  ASSREnabled
00450be4  UpdateMode
00450bf4  Training
00450bfd  DFPPortCount
00450cc9  DFPMaxClockRate
00450cd9  DFPMaxColorDepth
00450d11  IOAVService
00450d1d  IODPService
00450d29  dcpdp-service-epic
00450d3c  SinkIEEEOUI
00450d48  BranchIEEEOUI
00450d56  BranchDeviceID
00450d65  ChipRevision
00450d72  FirmwareRevision
00450d83  SinkCount
00450d8d  SymbolErrorCounts
00450d9f  CRIterations
00450dac  EQIterations
00450dd1  FECErrorCounts
00450de0  SupportsSDPSplit
00450e27  BitErrorCounts
00450e84  hdmi_cec_enabled
00450f7c  TunnelBWA
00450f8c  Granularity
00450f98  AllocatedBandwidth
00450fd7  MaxR8b10bLinkRate
00450fe9  MaxLaneCount
00450ffa  LinkCountTotal
00451009  LinkCountRemaining
00451025  MsgEnabled
0045103b  IsMSTBranch
00451047  IsActiveSink
00451054  FecCap
0045105b  FullPBN
00451063  AvailablePBN
00451070  NoConnect
0045107e  Branch
00451089  LegacyConverter
00451099  WirelessConverter
004510ab  WirelessUFP
004510bf  Ranges
004510c6  Aggressor
004510d0  NoiseWidth
004510e6  LinkRateScalar
004510f5  MSTPorts
004510fe  Attribute
00451108  Resource
00451111  Address
0045113f  RetrainLink
0045114b  SetPower
00451154  coverglass-serial-number-key
00451171  color-accuracy-index-key
0045119f  IOAVController
0045121f  VirtualDevice
0045154a  Encrypted
00451554  sinkScramblingState
00451581  PLLBandwidth
0045158e  DataSlewRate
0045159b  ClockSlewRate
004515a9  DataSwing
004515b3  ClockSwing
004515be  Data0Preemph
004515cb  Data1Preemph
004515d8  Data2Preemph
004515e5  ClockPreemph
004515f2  DisableAllTerm
00451601  DisableClkTerm
00451610  DataHighImp
0045161c  ClockHighImp
00451629  FilterThresh
00451636  FilterFraction
0045165a  Unknown
0045169c  dcpav-audio-arc-epic
004516b1  dcpav-arc-ep
004516be  FFECtrlLane
004516ca  SelectTerm
004516d5  DPRXEQ
004516df  cHDMIb
0045402c  vid-clk-freq
00454039  vid-ref-source
00454048  vid-clk-div
00454054  vid-flags
0045405e  vid-clk-pll-freq
0045406f  vid-clk-pll-fbdiv
00454081  vid-clk-pll-prediv
00454094  vid-clk-pll-opdiv
004540a6  vid-clk-pll-sparediv
004540bb  vid-clk-pll-cpiset
004540ce  vid-clk-pll-lfrset
004540e1  vid-clk-pll-fcw_num
004540f5  vid-clk-pll-fcw_denom
0045410b  vid-clk-pll-fb_divn_half
00454124  vid-clk-pll-divisor
00454138  vid-clk-config
00454147  pipe-idx
00454157  personalities
004541f0  trusted-compartment
00454204  secure-mipi
00454210  property-overrides
00454223  panel-overrides
00454233  target-require-secure-dcp-comms
00454253  total-pgtable-count
00454267  frameish-count
00454276  cap-slot-count
00454285  page-table-stats
00454296  DispTarget
004542a1  BoardID
004542a9  BoardRev
004542b2  ChipID
004542b9  ChipRev
004542c1  DisplayModuleID
004542d1  Location
004542df  DCPPlatform
004542eb  SkipLoadStages
004542fa  driver-personalities
0045430f  property-personalities
00454326  axis-1
0045432d  syncRate
00454336  derivedSyncRate
00454346  vid-link-data
00454354  timing
0045435b  panel-vendor-id
0045436b  panel-build-id
0045437a  panel-program-id
0045438b  panel-device-id
0045439b  panel-variant-id
004543ac  panel-touch-id
004543bb  agile-clocking-data
004543cf  display-eeprom-compensation
004543eb  SinkDeviceID
004543f8  detailed-panel-id
0045440a  DCPRole
00454412  DCPPort
0045441a  DCPLocation
00454426  DisplayTargets
00454435  DispTargetNone
0045445a  support-audio-earc
0045446d  support-retention-default
00454487  require-sleep-mode-retention
004544a4  nap-threshold
004544b2  support-power-manage
004544c7  s2r-threshold
004544d5  pg-threshold
004544e2  prevent-dcpext-nap
004544f5  dcp-state-change-cnt
0045450a  nap-prevent-cnt
0045451a  diagnostics
00454526  support-pagetable-stats
00454542  TMDS_LOW
0045454b  TMDS_HIGH
00454555  TMDS_MID
0045455e  tcon-device-id
0045456d  dp-link-data
0045457a  driveSettings-dev
0045458c  driveSettings
0045459a  margin
004545a9  retry-code
004545b4  retry-count
004545c0  retry-interval-ms
004545e8  endpoint-name
004545f6  test-ep
004545fe  mcw-clientid
0045460b  psdSrvcIds
00454616  psdAliasNums
00454623  psdDbIrqs
0045464f  ?create-workloop
00454660  use-workloop-thread
00454674  SessionStart
004546a8  matched
004546b6  category
004546bf  endpoint
004546c8  ep-if-properties
004546d9  ep-if-class-props
004546eb  interface-id
004546f8  interface-remote
00454709  interface-name
00454718  interface-entitlements
0045472f  interface-reregister
00454744  ep-has-desc-mgr
00454754  epi-is-desc-mgr
00454764  cmd-oob-threshold
00454776  rsp-oob-threshold
00454788  ensure-delivery
00454798  default
004547a0  ep-connected
004547ad  remote-open
004547b9  endpoint-wl
004547c5  epif-wl
004547cd  max-command-count
004547df  interface-match
004547ef  <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0">
00454893  </plist>
004548a0  shallow
00454a68  regPowerEnable
00454a77  properties
00454a91  retain
00454a98  children
00454aa1  clients
00454aa9  config
00454ab0  @(#)PROGRAM:AppleFirmwareKit  PROJECT:AppleFirmwareKit-743.40.4
00454b1e  priority
00454b27  stacksize
00454b31  stackguard
00454b60  pmgr-dev-id
00454bc0  It took me all my life to learn how to salt a tomato. --Eric Ripert
00455354  enable
00455e51  CEA-861:Type1
00455ef0  Global
00455ef7  average-refresh-rate
00455f0c  layer0
00455f13  layer1
00455f1a  layer2
00455f21  layer3
00455f28  Current Display
00455f38  Pending Swap
00455f45  Swap Queue
00455f50  Temp Queue
00455f5b  Last Swap Layers Array
00455f72  Last Swaps Array
00455f83  Last Swaps Dictionary
00455f99  IOMFB power info
00455fb0  DCPIndex
004563be  u=raw-panel-serial-number
004563d8  luminance-ratio
004563e8  first-frame-response
004563fd  first-frame-response-high
00456417  llc-red
0045641f  llc-green
00456429  llc-blue
00456432  ptuc-red
0045643b  ptuc-green
00456446  ptuc-blue
00456450  ptuc-rsvd
0045645a  lMinPanel
00456464  lMaxPanel
0045646e  lMaxReachable
00456621  PILFDOA
00456629  YALDDOA
00456631  NACSDOA
0045663a  BMADOA
00456642  CRPDOA
0045664a  CDPDOA
00456652  MLLDOA
00456659  SLPADOA
00456661  CLPADOA
00456669  TCTFDOA
00456671  MSTFDOA
00456679  NMTFDOA
00456681  XMTFDOA
00456689  EBTFDOA
00456691  HENODOA
00456699  SSIMDOA
004566a1  ACIBDOA
004566aa  CABDOA
004566b2  CCBDOA
004566b9  CAPBDOA
004566c1  CCPBDOA
004566c9  BCMSDOA
004566d1  UFMSDOA
0045778c  TimingElements
0045779b  ColorElements
004577d2  ProductID
004577dc  ManufacturerID
004577eb  SerialNumber
004577f8  WeekOfManufacture
0045780a  YearOfManufacture
0045781c  ModelYear
00457826  IOMFB backlight info
0045783b  Downstream
00457846  export_uuid
004578a4  DisplayAttributes
004578b6  ProductAttributes
004578c8  Transport
004578d2  EDID UUID
004578dc  DisplayContainerID
0045791d  Chromaticity
0045792a  DefaultWhitePoint
00457eeb  HMF1F"F
00458e33  hJhaHDh
0045958b  hhP!}`
0045959d  QhPa} x
004595af  QhP1|pz
00459643  ! nhPC
0045964b  !`nhPC
00459663  A ohPC
0045966b  A`ohPC
0045a566  iHiIM"
0045a5d6  MHNIF"
0045a608  #)/5;AGMS
0045a837  u\jDQE
0045af7f  T(XjXB
0045b02f  T(XjXB
0045bc3c  ,L%hNo
0045bdff  aEh,CD`
0045bec6  3H0MAh!
0045bf00  !`.`ahA
0045bf15  Q)`ahA
0045c06f   hc.HAh!
0045c0eb  hCh@iB
0045c1f0  XIYJYLZKZN
0045c8cb  hShRi@
0045d28c  pGpGpGpG
0045d2a4  0XhLhI
0045d7ce  5a#n1hbnph
0045db2f  hLhIiC
0045e146  lXX{X~XXXXXuXXXXr
0045e74d  ppGkXU
0045e8fc  command_mode_mcpu.c
0045e910  command_mode_all_piodma_done
0045e92d  isr_nclk
0045e936  Internal state error
0045e94c  isr_pcc_stable
0045e95c  process_vbi
0045e968  command_mode_adisp.c
0045e97d  tsq_control
0045e989  command_mode_replay_request_is_not_allowed
0045e9b4  single_pipe_start_frm_state_machines
0045e9d9  command_mode_apt.c
0045e9ec  apt_control
0045e9f8  isr_writeback_handler: BIS WB FAIL
0045ea1c    BIS WB fail and exceed retry
0045ea3c  bics_v2.c
0045ea46  ferr_BicsFErr_RdDecompressError
0045ea66  bis_setup_stripe
0045ea77  cdi_v3.c
0045ea80  isr_cdidone
0045ea8c  cdi_prepare_cmd
0045ea9c  cdi_control
0045eaa8  cdi_irq_FifoOverflow
0045eabd  cdi_irq_RunAtVbi
0045eace  cdi_irq_AxiErr
0045eadd  cdi_irq_SfWrErr
0045eaed  cdi_irq_Type0RunAtType1BarrierT
0045eb0d  cdi_irq_Type1RunAtEndT
0045eb24  get_cmd_table_with_tag
0045eb3b  cdi_table_mark_done
0045eb4f  set_cmd_completed_state
0045eb67  cdi_configure_table
0045eb7b  debug_helper.c
0045eb8a  debug_helper_stop_clock
0045eba2  ferror_handlers.c
0045ebb4  isr_SecurityStat
0045ebc5  ferr_AxiWrErr
0045ebd3  ferr_AxiRdErr
0045ebe1  ferr_SfOverflow
0045ebf1  ferr_GP_DecompressFail
0045ec08  ferr_Underrun
0045ec16  M3 adisp SPDS version expecting %x, found %x
0045ec44  dmem SPDS version expecting %x, found %x
0045ec6e  command_mode_main_init.c
0045ec87  main_init
0045ec91  command_mode_mode_change.c
0045ecac  isr_mode_change_req
0045ecc0  M3 New Mode: Normal
0045ecd5  ../common/mxwrap_msgbox_mprintf.c
0045ecf7  m3_message
0045ed02  ../common/mprintf_shared.h
0045ed1d  m3_log_text
0045ed29  m3_vsnprintf
0045ed36  isr_inbox0_not_empty
0045ed4b  pdc_v22.c
0045ed55  pdc_cdi_configure_area
0045ed6c  pdc_rw_dma_early_stop
0045ed82  pdc_ext_wb_buffer_overflow
0045ed9d  pdc_int_wb_buffer_overflow
0045edb8  pdc_wr_dma_fail
0045edc8  pdc_rd_dma_fail
0045edd8  pdc_rd_decompress_error
0045edf0  state_machine_cmd
0045ee02  piodma_tagging.c
0045ee13  isr_apiodma
0045ee1f  piodma_check_idle
0045ee31  apiodma_irq_ParseErr
0045ee46  apiodma_irq_SeqPushErr
0045ee5d  apiodma_irq_AxiErr
0045ee70  apiodma_irq_AddrBoundsErr
0045ee8a  piodma_irq_command_tag_completed_mismatch
0045eeb4  piodma_transaction_not_completed_tsq
0045eed9  piodma_transaction_not_completed_prc0
0045eeff  piodma_transaction_not_completed_prc1
0045ef25  piodma_transaction_not_completed_pdclut
0045ef4d  piodma_transaction_not_completed_hgod
0045ef73  piodma_transaction_not_completed_pcc2dluslut
0045efa0  piodma_transaction_not_completed_proxlut
0045efc9  piodma_transaction_not_completed_spuc_map
0045eff3  piodma_transaction_not_completed_alsslut
0045f01c  piodma_transaction_not_completed_acsslut
0045f045  piodma_transaction_not_completed_ptuclut
0045f06e  debug_logging_update_piodma_done
0045f08f  piodma_control_tagging.c
0045f0a8  piodma_control
0045f0b7  pixel_capture_info2.c
0045f0cd  pixel_capture_frame_info
0045f0e6  profiler.c
0045f0f1  fw_budget_check
0045f101  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
0045f13d  disp_perf_state.c
0045f14f  error_rt_bwr_exceed_max_perf_state
0045f172  Control M3: update_disp_perf_state_hw %d -> %d
0045f1a2  rtplc.c
0045f1aa  interp1_rescalehist
0045f1be  rtplc_write_globalenable
0045f1d7  rtplc_setup
0045f1e3  rtplc_update_tsq_info
0045f1f9  rtplc_process_stats
0045f20d  isr_rtplc_global_failsafe_trig
0045f22c  rtplc_read_fd_histogram
0045f244  rtplc_current_limit_global_scaling
0045f267  rtplc_calc_rt_luts
0045f27a  swmpr_v1.c
0045f285  swmpr_mode_change
0045f297  isr_swmpr
0045f2a1  swmpr_refresh_rate.c
0045f2b6  swmpr_refresh_rate_update
0045f2d0  timebase.c
0045f2db  read_timebase
0045f2f9  Unsupported: '%c'
0045f30b  0123456789ABCDEF
0045f31c  0123456789abcdef
0045fc9e  Jhg(g0D
004605b0  `iJShC
00460da8  hpP!}`
00460e4a  QpP)|hz
00460e80  QhnpPO
004613d9  aHDi@F
00461ff2  iDiDj"
00462cc4  #)/5;AGM
00462e5a  u\jDQE
00463b01  le4YuY
00464314  T0XrXB
004643bc  T0XrXB
00465dcc  aEh,CD`
00465e70  hUhRiKN
00465ef2  A)`ahA
00465f0e  Q)`ahA
00466113  tP]FTF
00466190  hCh@iB
00466912  hShRi@
00466b2b  @DBDDD
00467936  eqf`m!o
004680c5  pGpGpGpGpGpG
004683fa  atDUhO
0046853b  lXX{X~XXXXXuXXXXr
00468c0e  A)PpG)X!
00468c18  A)PpGPC@
00468c2f  5Y4YpGAh!
00468c4d  pGmcpu.c
00468c56  read_dmem_m3control
00468c6a  configure_frame0_0_irq
00468c81  configure_subframe0_0_irq
00468c9b  configure_subframe0_3_irq
00468cb5  isr_vftg_subframe0_0
00468cca  isr_pcc_stable
00468cda  adisp.c
00468ce2  tsq_control
00468cee  single_pipe_start_frm_state_machines
00468d19  calc_vbi_position_lines
00468d31  apt_init
00468d3a  apt_vbi
00468d42  apt_control
00468d4e  apt_activate
00468d5b  adaptive_sync.c
00468d6b  adaptive_sync_control
00468d81  adaptive_sync_determine_min_max_duration
00468daa  qms_tsq
00468db2  adaptive_sync_activate
00468dc9  qms_vftg_update
00468dd9  bics_stub.c
00468de5  isr_bis_handler
00468df5  isr_BicsFErr_RdDecompressError
00468e19  ca_discharge
00468e26  ca_active
00468e30  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00468e81  cdi_v3.c
00468e8a  isr_cdidone
00468e96  cdi_check_idle
00468ea5  cdi_prepare_cmd
00468eb5  cdi_control
00468ec1  cdi_irq_FifoOverflow
00468ed6  cdi_irq_RunAtVbi
00468ee7  cdi_irq_AxiErr
00468ef6  cdi_irq_SfWrErr
00468f06  cdi_irq_Type0RunAtType1BarrierT
00468f26  cdi_irq_Type1RunAtEndT
00468f3d  get_cmd_table_with_tag
00468f54  cdi_table_mark_done
00468f68  set_cmd_completed_state
00468f80  cdi_configure_table
00468f94  debug_helper.c
00468fa3  debug_helper_stop_clock
00468fbb  fast_update_legacy.c
00468fd0  fast_layer_update_regs
00468fe7  ferror_handlers.c
00468ff9  isr_SecurityStat
0046900a  ferr_AxiWrErr
00469018  ferr_AxiRdErr
00469026  ferr_SfOverflow
00469036  ferr_Replay_DecompressFail
00469051  ferr_GP_DecompressFail
00469068  ferr_ReplayReadback_Underrun
00469085  ferr_Underrun
00469093  follower_mode_v3.c
004690a6  follower_mode_trigger
004690bc  LFC: dmem w 0x%x
004690ce  LFC: A->R 
004690da  LFC: 8.3 ms repeat. Rem %u 
004690fd  lfc_control
00469109  LFC: R->R 
00469115  LFC: Clear Pending from swid %u 
00469137  LFC: rem_sfm %u nr %u
0046914e  LFC: status %d 
0046915f  LFC: Reset states 
00469173  M3 adisp SPDS version expecting %x, found %x
004691a1  dmem SPDS version expecting %x, found %x
004691cb  video_mode_main_init.c
004691e2  main_init
004691ec  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00469238  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00469286  M3 vbi_pulse %u, vbi_offset %d (initial %d)
004692b2  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
004692f6  Control M3 error: Must have one subframe for external panels
00469334  mode_change_v2.c
00469345  isr_mode_change_req
00469359  M3 New Mode: %s
0046936f  Normal
00469376  WARNING; TSQ entry at normal to auto mode change. Replay=%d
004693b2  sideband_can_mode_switch
004693cb  ../common/mxwrap_msgbox_mprintf.c
004693ed  m3_message
004693f8  ../common/mprintf_shared.h
00469413  m3_log_text
0046941f  m3_vsnprintf
0046942c  isr_inbox0_not_empty
00469441  pdc_v22.c
0046944b  pdc_cdi_configure_area
00469462  pdc_rw_dma_early_stop
00469478  pdc_ext_wb_buffer_overflow
00469493  pdc_int_wb_buffer_overflow
004694ae  pdc_wr_dma_fail
004694be  pdc_rd_dma_fail
004694ce  pdc_rd_decompress_error
004694e6  pdc_control_vid
004694f6  piodma_tagging.c
00469507  isr_apiodma
00469513  piodma_check_idle
00469525  apiodma_irq_ParseErr
0046953a  apiodma_irq_SeqPushErr
00469551  apiodma_irq_AxiErr
00469564  apiodma_irq_AddrBoundsErr
0046957e  piodma_irq_command_tag_completed_mismatch
004695a8  piodma_transaction_not_completed_tsq
004695cd  piodma_transaction_not_completed_prc0
004695f3  piodma_transaction_not_completed_prc1
00469619  piodma_transaction_not_completed_pdclut
00469641  piodma_transaction_not_completed_hgod
00469667  piodma_transaction_not_completed_pcc2dluslut
00469694  piodma_transaction_not_completed_proxlut
004696bd  piodma_transaction_not_completed_spuc_map
004696e7  piodma_transaction_not_completed_alsslut
00469710  piodma_transaction_not_completed_acsslut
00469739  piodma_transaction_not_completed_ptuclut
00469762  debug_logging_update_piodma_done
00469783  piodma_control_tagging.c
0046979c  piodma_control
004697ab  pixel_capture_info2.c
004697c1  pixel_capture_frame_info
004697da  prc_v4.c
004697e3  prc_active
004697f4  rca_trigger_check
00469806  rca_vbi_check
00469814  isr_rca_main
00469821  isr_rca_error_handler
00469837  configure_rca_dpg_subframe0_1_irq
00469859  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00469895  disp_perf_state.c
004698a7  error_rt_bwr_exceed_max_perf_state
004698ca  Control M3: update_disp_perf_state_hw %d -> %d
004698fa  dptx_multi_sdp.c
0046990b  dptx_sdp_init
00469919  timebase.c
00469924  read_timebase
00469942  Unsupported: '%c'
00469954  0123456789ABCDEF
00469965  0123456789abcdef
0046a170  8p4ctc
0046a2f0  PtPaPdE
0046a4bf  QQXRF!
0046b806  "Q(XiX
0046b975  `(IjPS
0046ba88  # NFXb
0046c759  QpP)|hz
0046c797  QhnpPO
0046e758  dBc@b@
0046eb49  h%mfmA
0046ee31  #)/5;AGP
0046efe3  u\jDQE
0046f517  hBh@iE
00470fd9  T(XjXB
00471089  T(XjXB
00471945  aEh,CD`
004719e9  hKhIiRN
00471c90  tP]FTF
00471d83  hCh@iB
0047274f  hShRi@
00472968  @DBDDD
00473bbb  p`DHDJ
00473cd4  dqPPpG
0047419a  0XWMWL
00474848  EFpf0~
00474c41  hLhIiC
00474f48  vBs@r@
004753a1  X D"D@hRh
00475532  @hHAX`
00475c08  lXX{X~XXXXXuXXXXr
00476205  A!PpG(XiX
00476285  0pGkXU
004762eb  ApGPC@
0047638c  pGmcpu.c
00476395  read_dmem_m3control
004763a9  configure_frame0_0_irq
004763c0  configure_subframe0_0_irq
004763da  configure_subframe0_3_irq
004763f4  isr_vftg_subframe0_0
00476409  isr_pcc_stable
00476419  adisp.c
00476421  tsq_control
0047642d  start_frm_active
0047643e  single_pipe_start_frm_state_machines
00476469  calc_vbi_position_lines
00476481  apt_init
0047648a  apt_vbi
00476492  apt_control
0047649e  apt_activate
004764ab  isr_writeback_handler: BIS WB FAIL
004764cf    BIS WB fail and exceed retry
004764ef  bics_v2.c
004764f9  ferr_BicsFErr_RdDecompressError
00476519  bis_setup_stripe
0047652f  ca_discharge
0047653c  ca_active
00476546  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00476597  cdi_v3.c
004765a0  isr_cdidone
004765ac  cdi_check_idle
004765bb  cdi_prepare_cmd
004765cb  cdi_control
004765d7  cdi_irq_FifoOverflow
004765ec  cdi_irq_RunAtVbi
004765fd  cdi_irq_AxiErr
0047660c  cdi_irq_SfWrErr
0047661c  cdi_irq_Type0RunAtType1BarrierT
0047663c  cdi_irq_Type1RunAtEndT
00476653  get_cmd_table_with_tag
0047666a  cdi_table_mark_done
0047667e  set_cmd_completed_state
00476696  cdi_configure_table
004766aa  debug_helper.c
004766b9  debug_helper_stop_clock
004766d1  ferror_handlers.c
004766e3  isr_SecurityStat
004766f4  ferr_AxiWrErr
00476702  ferr_AxiRdErr
00476710  ferr_SfOverflow
00476720  ferr_Replay_DecompressFail
0047673b  ferr_GP_DecompressFail
00476752  ferr_ReplayReadback_Underrun
0047676f  ferr_Underrun
0047677d  M3 adisp SPDS version expecting %x, found %x
004767ab  dmem SPDS version expecting %x, found %x
004767d5  video_mode_main_init.c
004767ec  main_init
004767f6  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00476842  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00476890  M3 vbi_pulse %u, vbi_offset %d (initial %d)
004768bc  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00476900  Control M3 error: Must have one subframe for external panels
0047693e  mode_change_v2.c
0047694f  isr_mode_change_req
00476963  M3 New Mode: %s
00476979  Normal
00476980  WARNING; TSQ entry at normal to auto mode change. Replay=%d
004769bc  sideband_can_mode_switch
004769d5  ../common/mxwrap_msgbox_mprintf.c
004769f7  m3_message
00476a02  ../common/mprintf_shared.h
00476a1d  m3_log_text
00476a29  m3_vsnprintf
00476a36  isr_inbox0_not_empty
00476a4b  pdc_v22.c
00476a55  pdc_cdi_configure_area
00476a6c  pdc_rw_dma_early_stop
00476a82  pdc_ext_wb_buffer_overflow
00476a9d  pdc_int_wb_buffer_overflow
00476ab8  pdc_wr_dma_fail
00476ac8  pdc_rd_dma_fail
00476ad8  pdc_rd_decompress_error
00476af0  pdc_control_vid
00476b00  piodma_tagging.c
00476b11  isr_apiodma
00476b1d  piodma_check_idle
00476b2f  apiodma_irq_ParseErr
00476b44  apiodma_irq_SeqPushErr
00476b5b  apiodma_irq_AxiErr
00476b6e  apiodma_irq_AddrBoundsErr
00476b88  piodma_irq_command_tag_completed_mismatch
00476bb2  piodma_transaction_not_completed_tsq
00476bd7  piodma_transaction_not_completed_prc0
00476bfd  piodma_transaction_not_completed_prc1
00476c23  piodma_transaction_not_completed_pdclut
00476c4b  piodma_transaction_not_completed_hgod
00476c71  piodma_transaction_not_completed_pcc2dluslut
00476c9e  piodma_transaction_not_completed_proxlut
00476cc7  piodma_transaction_not_completed_spuc_map
00476cf1  piodma_transaction_not_completed_alsslut
00476d1a  piodma_transaction_not_completed_acsslut
00476d43  piodma_transaction_not_completed_ptuclut
00476d6c  debug_logging_update_piodma_done
00476d8d  piodma_control_tagging.c
00476da6  piodma_control
00476db5  pixel_capture_info2.c
00476dcb  pixel_capture_frame_info
00476de4  prc_v4.c
00476ded  prc_active
00476df8  profiler.c
00476e03  fw_budget_check
00476e13  prox.c
00476e1a  prox_active
00476e26  proxlut_piodma_context
00476e3d  prox_aod_shutdown
00476e4f  prox_aod_startup
00476e60  prox_sws_init
00476e6e  prox_sws_stats_ready
00476e83  div_fx
00476e8a  find_coex_curve_zeros
00476ea0  prox_process
00476ead  find_prox_fire_time_rr
00476ec4  ProxB: bailed trigger 0x%x > %d * 0x%x + 0x%x - 0x%x [%d-%d %d]
00476f05  prox_config_trigger
00476f1f  rca_trigger_check
00476f31  rca_vbi_check
00476f3f  isr_rca_main
00476f4c  isr_rca_error_handler
00476f62  configure_rca_dpg_subframe0_1_irq
00476f84  rt_bandwidth_perf_state.c
00476f9e  rt_bw_check_aod_bw_limit
00476fb7  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00476ff3  disp_perf_state.c
00477005  error_rt_bwr_exceed_max_perf_state
00477028  Control M3: update_disp_perf_state_hw %d -> %d
00477058  rtplc_v3.c
00477063  interp1_rescalehist
00477077  rtplc_write_globalenable
00477090  rtplc_setup
0047709c  rtplc_update_tsq_info
004770b2  rtplc_process_stats
004770c6  isr_rtplc_global_failsafe_trig
004770e5  rtplc_read_fd_histogram
004770fd  rtplc_rescale_histogram
00477115  rtplc_calc_rt_luts
00477128  dptx_multi_sdp.c
00477139  dptx_sdp_init
00477147  vmaod_replay.c
00477156  vmaod_replay_init
00477168  replay_vmaod_wb_completed
00477182  timebase.c
0047718d  read_timebase
004771ab  Unsupported: '%c'
004771bd  0123456789ABCDEF
004771ce  0123456789abcdef
00477fae  aPaXdE
00478176  QQXBF!
004792d9  "Q(XiX
00479442  `5IZPo
0047bd4d  dBc@b@
0047c13a  h%mfmA
0047c426  #)/5;AGR
0047c5d8  u\jDQE
0047e0fa  B+F(XiX
0047e238  B+F(XiX
0047e582  T(XjXB
0047e632  T(XjXB
0047eeee  aEh,CD`
0047ef92  hKhIiRN
0047f237  tP]FTF
0047f2fe  hCh@iB
0047fcc8  hShRi@
0047fee1  @DBDDD
00480c3f  0XWMWL
004812ed  EFpf0~
004816e6  hLhIiC
004819ed  vBs@r@
00481e46  X D"D@hRh
00481fdf  @hHAX`
004826b5  lXX{X~XXXXXuXXXXr
00482d2f  pG(XiX
00482e46  A)PpGAh!
00482e73  pGmcpu.c
00482e7c  read_dmem_m3control
00482e90  configure_frame0_0_irq
00482ea7  configure_subframe0_0_irq
00482ec1  configure_subframe0_3_irq
00482edb  isr_vftg_subframe0_0
00482ef0  isr_pcc_stable
00482f00  adisp.c
00482f08  tsq_control
00482f14  start_frm_active
00482f25  single_pipe_start_frm_state_machines
00482f50  calc_vbi_position_lines
00482f68  apt_init
00482f71  apt_vbi
00482f79  apt_control
00482f85  apt_activate
00482f92  isr_writeback_handler: BIS WB FAIL
00482fb6    BIS WB fail and exceed retry
00482fd6  bics_v2.c
00482fe0  ferr_BicsFErr_RdDecompressError
00483000  bis_setup_stripe
00483016  ca_discharge
00483023  ca_active
0048302d  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
0048307e  cdi_v3.c
00483087  isr_cdidone
00483093  cdi_check_idle
004830a2  cdi_prepare_cmd
004830b2  cdi_control
004830be  cdi_irq_FifoOverflow
004830d3  cdi_irq_RunAtVbi
004830e4  cdi_irq_AxiErr
004830f3  cdi_irq_SfWrErr
00483103  cdi_irq_Type0RunAtType1BarrierT
00483123  cdi_irq_Type1RunAtEndT
0048313a  get_cmd_table_with_tag
00483151  cdi_table_mark_done
00483165  set_cmd_completed_state
0048317d  cdi_configure_table
00483191  debug_helper.c
004831a0  debug_helper_stop_clock
004831b8  ferror_handlers.c
004831ca  isr_SecurityStat
004831db  ferr_AxiWrErr
004831e9  ferr_AxiRdErr
004831f7  ferr_SfOverflow
00483207  ferr_Replay_DecompressFail
00483222  ferr_GP_DecompressFail
00483239  ferr_ReplayReadback_Underrun
00483256  ferr_Underrun
00483264  M3 adisp SPDS version expecting %x, found %x
00483292  dmem SPDS version expecting %x, found %x
004832bc  video_mode_main_init.c
004832d3  main_init
004832dd  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00483329  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00483377  M3 vbi_pulse %u, vbi_offset %d (initial %d)
004833a3  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
004833e7  Control M3 error: Must have one subframe for external panels
00483425  mode_change_v2.c
00483436  isr_mode_change_req
0048344a  M3 New Mode: %s
00483460  Normal
00483467  WARNING; TSQ entry at normal to auto mode change. Replay=%d
004834a3  sideband_can_mode_switch
004834bc  ../common/mxwrap_msgbox_mprintf.c
004834de  m3_message
004834e9  ../common/mprintf_shared.h
00483504  m3_log_text
00483510  m3_vsnprintf
0048351d  isr_inbox0_not_empty
00483532  pdc_v22.c
0048353c  pdc_cdi_configure_area
00483553  pdc_rw_dma_early_stop
00483569  pdc_ext_wb_buffer_overflow
00483584  pdc_int_wb_buffer_overflow
0048359f  pdc_wr_dma_fail
004835af  pdc_rd_dma_fail
004835bf  pdc_rd_decompress_error
004835d7  pdc_control_vid
004835e7  piodma_tagging.c
004835f8  isr_apiodma
00483604  piodma_check_idle
00483616  apiodma_irq_ParseErr
0048362b  apiodma_irq_SeqPushErr
00483642  apiodma_irq_AxiErr
00483655  apiodma_irq_AddrBoundsErr
0048366f  piodma_irq_command_tag_completed_mismatch
00483699  piodma_transaction_not_completed_tsq
004836be  piodma_transaction_not_completed_prc0
004836e4  piodma_transaction_not_completed_prc1
0048370a  piodma_transaction_not_completed_pdclut
00483732  piodma_transaction_not_completed_hgod
00483758  piodma_transaction_not_completed_pcc2dluslut
00483785  piodma_transaction_not_completed_proxlut
004837ae  piodma_transaction_not_completed_spuc_map
004837d8  piodma_transaction_not_completed_alsslut
00483801  piodma_transaction_not_completed_acsslut
0048382a  piodma_transaction_not_completed_ptuclut
00483853  debug_logging_update_piodma_done
00483874  piodma_control_tagging.c
0048388d  piodma_control
0048389c  pixel_capture_info2.c
004838b2  pixel_capture_frame_info
004838cb  prc_v4.c
004838d4  prc_active
004838df  profiler.c
004838ea  fw_budget_check
00483900  rca_trigger_check
00483912  rca_vbi_check
00483920  isr_rca_main
0048392d  isr_rca_error_handler
00483943  configure_rca_dpg_subframe0_1_irq
00483965  rt_bandwidth_perf_state.c
0048397f  rt_bw_check_aod_bw_limit
00483998  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
004839d4  disp_perf_state.c
004839e6  error_rt_bwr_exceed_max_perf_state
00483a09  Control M3: update_disp_perf_state_hw %d -> %d
00483a39  rtplc_v3.c
00483a44  interp1_rescalehist
00483a58  rtplc_write_globalenable
00483a71  rtplc_setup
00483a7d  rtplc_update_tsq_info
00483a93  rtplc_process_stats
00483aa7  isr_rtplc_global_failsafe_trig
00483ac6  rtplc_read_fd_histogram
00483ade  rtplc_rescale_histogram
00483af6  rtplc_calc_rt_luts
00483b09  dptx_multi_sdp.c
00483b1a  dptx_sdp_init
00483b28  vmaod_replay.c
00483b37  vmaod_replay_init
00483b49  replay_vmaod_wb_completed
00483b63  timebase.c
00483b6e  read_timebase
00483b8c  Unsupported: '%c'
00483b9e  0123456789ABCDEF
00483baf  0123456789abcdef
00484b25  Jhg(g0D
00485437  `iJShC
00485702  t"pjSx
00485c2b  hpP!}`
00485ccd  QpP)|hz
00485d03  QhnpPO
00486242  aHDi@F
00486e59  iDiDj"
00487b2b  #)/5;AGM
00487cc1  u\jDQE
00488964  le4YuY
00489177  T0XrXB
0048921f  T0XrXB
00489864  qPRlKb
0048ac2f  aEh,CD`
0048acd3  hUhRiKN
0048ad55  A)`ahA
0048ad71  Q)`ahA
0048af76  tP]FTF
0048aff3  hCh@iB
0048b775  hShRi@
0048b98e  @DBDDD
0048c799  eqf`m!o
0048cf28  pGpGpGpGpGpG
0048d25d  atDUhO
0048d39e  lXX{X~XXXXXuXXXXr
0048da71  A)PpG)X!
0048da7b  A)PpGPC@
0048da92  5Y4YpGAh!
0048dab0  pGmcpu.c
0048dab9  read_dmem_m3control
0048dacd  configure_frame0_0_irq
0048dae4  configure_subframe0_0_irq
0048dafe  configure_subframe0_3_irq
0048db18  isr_vftg_subframe0_0
0048db2d  isr_pcc_stable
0048db3d  adisp.c
0048db45  tsq_control
0048db51  single_pipe_start_frm_state_machines
0048db7c  calc_vbi_position_lines
0048db94  apt_init
0048db9d  apt_vbi
0048dba5  apt_control
0048dbb1  apt_activate
0048dbbe  adaptive_sync.c
0048dbce  adaptive_sync_control
0048dbe4  adaptive_sync_determine_min_max_duration
0048dc0d  qms_tsq
0048dc15  adaptive_sync_activate
0048dc2c  qms_vftg_update
0048dc3c  bics_stub.c
0048dc48  isr_bis_handler
0048dc58  isr_BicsFErr_RdDecompressError
0048dc7c  ca_discharge
0048dc89  ca_active
0048dc93  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
0048dce4  cdi_v3.c
0048dced  isr_cdidone
0048dcf9  cdi_check_idle
0048dd08  cdi_prepare_cmd
0048dd18  cdi_control
0048dd24  cdi_irq_FifoOverflow
0048dd39  cdi_irq_RunAtVbi
0048dd4a  cdi_irq_AxiErr
0048dd59  cdi_irq_SfWrErr
0048dd69  cdi_irq_Type0RunAtType1BarrierT
0048dd89  cdi_irq_Type1RunAtEndT
0048dda0  get_cmd_table_with_tag
0048ddb7  cdi_table_mark_done
0048ddcb  set_cmd_completed_state
0048dde3  cdi_configure_table
0048ddf7  debug_helper.c
0048de06  debug_helper_stop_clock
0048de1e  fast_update_legacy.c
0048de33  fast_layer_update_regs
0048de4a  ferror_handlers.c
0048de5c  isr_SecurityStat
0048de6d  ferr_AxiWrErr
0048de7b  ferr_AxiRdErr
0048de89  ferr_SfOverflow
0048de99  ferr_Replay_DecompressFail
0048deb4  ferr_GP_DecompressFail
0048decb  ferr_ReplayReadback_Underrun
0048dee8  ferr_Underrun
0048def6  follower_mode_v3.c
0048df09  follower_mode_trigger
0048df1f  LFC: dmem w 0x%x
0048df31  LFC: A->R 
0048df3d  LFC: 8.3 ms repeat. Rem %u 
0048df60  lfc_control
0048df6c  LFC: R->R 
0048df78  LFC: Clear Pending from swid %u 
0048df9a  LFC: rem_sfm %u nr %u
0048dfb1  LFC: status %d 
0048dfc2  LFC: Reset states 
0048dfd6  M3 adisp SPDS version expecting %x, found %x
0048e004  dmem SPDS version expecting %x, found %x
0048e02e  video_mode_main_init.c
0048e045  main_init
0048e04f  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
0048e09b  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
0048e0e9  M3 vbi_pulse %u, vbi_offset %d (initial %d)
0048e115  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
0048e159  Control M3 error: Must have one subframe for external panels
0048e197  mode_change_v2.c
0048e1a8  isr_mode_change_req
0048e1bc  M3 New Mode: %s
0048e1d2  Normal
0048e1d9  WARNING; TSQ entry at normal to auto mode change. Replay=%d
0048e215  sideband_can_mode_switch
0048e22e  ../common/mxwrap_msgbox_mprintf.c
0048e250  m3_message
0048e25b  ../common/mprintf_shared.h
0048e276  m3_log_text
0048e282  m3_vsnprintf
0048e28f  isr_inbox0_not_empty
0048e2a4  pdc_v22.c
0048e2ae  pdc_cdi_configure_area
0048e2c5  pdc_rw_dma_early_stop
0048e2db  pdc_ext_wb_buffer_overflow
0048e2f6  pdc_int_wb_buffer_overflow
0048e311  pdc_wr_dma_fail
0048e321  pdc_rd_dma_fail
0048e331  pdc_rd_decompress_error
0048e349  pdc_control_vid
0048e359  piodma_tagging.c
0048e36a  isr_apiodma
0048e376  piodma_check_idle
0048e388  apiodma_irq_ParseErr
0048e39d  apiodma_irq_SeqPushErr
0048e3b4  apiodma_irq_AxiErr
0048e3c7  apiodma_irq_AddrBoundsErr
0048e3e1  piodma_irq_command_tag_completed_mismatch
0048e40b  piodma_transaction_not_completed_tsq
0048e430  piodma_transaction_not_completed_prc0
0048e456  piodma_transaction_not_completed_prc1
0048e47c  piodma_transaction_not_completed_pdclut
0048e4a4  piodma_transaction_not_completed_hgod
0048e4ca  piodma_transaction_not_completed_pcc2dluslut
0048e4f7  piodma_transaction_not_completed_proxlut
0048e520  piodma_transaction_not_completed_spuc_map
0048e54a  piodma_transaction_not_completed_alsslut
0048e573  piodma_transaction_not_completed_acsslut
0048e59c  piodma_transaction_not_completed_ptuclut
0048e5c5  debug_logging_update_piodma_done
0048e5e6  piodma_control_tagging.c
0048e5ff  piodma_control
0048e60e  pixel_capture_info2.c
0048e624  pixel_capture_frame_info
0048e63d  prc_v4.c
0048e646  prc_active
0048e657  rca_trigger_check
0048e669  rca_vbi_check
0048e677  isr_rca_main
0048e684  isr_rca_error_handler
0048e69a  configure_rca_dpg_subframe0_1_irq
0048e6bc  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
0048e6f8  disp_perf_state.c
0048e70a  error_rt_bwr_exceed_max_perf_state
0048e72d  Control M3: update_disp_perf_state_hw %d -> %d
0048e75d  dptx_multi_sdp.c
0048e76e  dptx_sdp_init
0048e77c  timebase.c
0048e787  read_timebase
0048e7a5  Unsupported: '%c'
0048e7b7  0123456789ABCDEF
0048e7c8  0123456789abcdef
0048f0bd  pt0upu
0048f2a8  f0D`fiX@
0048f474  pNLKKO
0048fb36  `iJShC
00490246  QhP1|pz
00490284  QpnhPO
004905b6  &*XiX#o
0049072f  RHDi0F
004909d5  @DXP0F
00491a96  u\jDQE
00492a62  T(XjXB
00492b10  T(XjXB
00494000  hQhQiB
0049409c  n\FXo@
00494248  `IhBn1
00494370  aEh,CD`
00494414  hUhRiHN
00494492  A)`ahA
004944ae  Q)`ahA
004946f6  hCh@iB
00495b01  pGpGpGpGpGpG
00495e36  atDUhO
00495f77  lXX{X~XXXXXuXXXXr
004965d8  ApGPC@
00496606  A!PpGZ
0049662a  PpGAh!
00496633  A`pGmcpu.c
0049663e  read_dmem_m3control
00496652  configure_frame0_0_irq
00496669  configure_subframe0_0_irq
00496683  configure_subframe0_3_irq
0049669d  isr_vftg_subframe0_0
004966b2  isr_pcc_stable
004966c2  adisp.c
004966ca  tsq_control
004966d6  single_pipe_start_frm_state_machines
00496701  calc_vbi_position_lines
00496719  apt_init
00496722  apt_vbi
0049672a  apt_control
00496736  apt_activate
00496743  adaptive_sync.c
00496753  adaptive_sync_control
00496769  adaptive_sync_determine_min_max_duration
00496792  qms_tsq
0049679a  adaptive_sync_activate
004967b1  qms_vftg_update
004967c1  bics_stub.c
004967cd  isr_bis_handler
004967dd  isr_BicsFErr_RdDecompressError
00496801  ca_discharge
0049680e  ca_active
00496818  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00496869  cdi_v3.c
00496872  isr_cdidone
0049687e  cdi_check_idle
0049688d  cdi_prepare_cmd
0049689d  cdi_control
004968a9  cdi_irq_FifoOverflow
004968be  cdi_irq_RunAtVbi
004968cf  cdi_irq_AxiErr
004968de  cdi_irq_SfWrErr
004968ee  cdi_irq_Type0RunAtType1BarrierT
0049690e  cdi_irq_Type1RunAtEndT
00496925  get_cmd_table_with_tag
0049693c  cdi_table_mark_done
00496950  set_cmd_completed_state
00496968  cdi_configure_table
0049697c  debug_helper.c
0049698b  debug_helper_stop_clock
004969a3  ferror_handlers.c
004969b5  isr_SecurityStat
004969c6  ferr_AxiWrErr
004969d4  ferr_AxiRdErr
004969e2  ferr_SfOverflow
004969f2  ferr_Replay_DecompressFail
00496a0d  ferr_GP_DecompressFail
00496a24  ferr_ReplayReadback_Underrun
00496a41  ferr_Underrun
00496a4f  follower_mode_v3.c
00496a62  follower_mode_trigger
00496a78  LFC: dmem w 0x%x
00496a8a  LFC: A->R 
00496a96  LFC: 8.3 ms repeat. Rem %u 
00496ab9  lfc_control
00496ac5  LFC: R->R 
00496ad1  LFC: Clear Pending from swid %u 
00496af3  LFC: rem_sfm %u nr %u
00496b0a  LFC: status %d 
00496b1b  LFC: Reset states 
00496b2f  M3 adisp SPDS version expecting %x, found %x
00496b5d  dmem SPDS version expecting %x, found %x
00496b87  video_mode_main_init.c
00496b9e  main_init
00496ba8  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00496bf4  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00496c42  M3 vbi_pulse %u, vbi_offset %d (initial %d)
00496c6e  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00496cb2  Control M3 error: Must have one subframe for external panels
00496cf0  mode_change_v2.c
00496d01  isr_mode_change_req
00496d15  M3 New Mode: %s
00496d2b  Normal
00496d32  WARNING; TSQ entry at normal to auto mode change. Replay=%d
00496d6e  ../common/mxwrap_msgbox_mprintf.c
00496d90  m3_message
00496d9b  ../common/mprintf_shared.h
00496db6  m3_log_text
00496dc2  m3_vsnprintf
00496dcf  isr_inbox0_not_empty
00496de4  piodma_tagging_ext.c
00496df9  isr_apiodma
00496e05  piodma_check_idle
00496e17  apiodma_irq_ParseErr
00496e2c  apiodma_irq_SeqPushErr
00496e43  apiodma_irq_AxiErr
00496e56  apiodma_irq_AddrBoundsErr
00496e70  piodma_irq_command_tag_completed_mismatch
00496e9a  piodma_transaction_not_completed_tsq
00496ebf  debug_logging_update_piodma
00496edb  debug_logging_update_piodma_done
00496efc  piodma_control_tagging.c
00496f15  piodma_control
00496f24  pixel_capture_info2.c
00496f3a  pixel_capture_frame_info
00496f53  prc_v4.c
00496f5c  prc_active
00496f67  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00496fa3  disp_perf_state.c
00496fb5  error_rt_bwr_exceed_max_perf_state
00496fd8  Control M3: update_disp_perf_state_hw %d -> %d
00497008  dptx_multi_sdp.c
00497019  dptx_sdp_init
00497027  timebase.c
00497032  read_timebase
00497050  Unsupported: '%c'
00497062  0123456789ABCDEF
00497073  0123456789abcdef
0049730a  )=hqu?=,
00497c3c  Invalid
0049933a  XFQFBF
004993f4  BFdFqFG
0049958c   `XFAF2FSF
004995e8  1FXFRF
004998c9  `0FAF*F#F
00499e1b  @0F)FJF
0049a8f3  B*dJl"
0049b2c7  `0F)F"FCF
0049b9dc  tA XaX
0049bc64  tA0XqX
0049cf16  +FbFDFNF_
0049d4fe  0FAFJF #
0049d50c  0FAF"F #
0049d519  F0FAFA
0049d527  F0FAFZF #
0049dc43  U*DJaF
0049dc72  hAAXQ`F
0049dc8a  tAAXQaF
0049dd07  0pETDA
004a331e  mcpu_pcc2d_ltm.c
004a332f  ltm_config_fw
004a333d  pcc2d_ltm_isr_first_pixel_impl
004a335c  ltm_process_local_hist_0dbl
004a3378  pcc2d_ltm_isr_mce_task_complete
004a3398  mprintf_msgbox_pcc2d_ltm.c
004a33b3  m3_message
004a33be  m3_log_text
004a33ca  isr_inbox0_not_empty
004a4a4a  |a8ete0i
004a4a6a  |i8mtm0q
004a4a8c  |q8utu0y
004a4bca  <cxc4gpg
004a4be6  <kxk4opo
004a4c04  <sxs4wpw
004a4ce6  <cxc4gpg
004a4d02  <kxk4opo
004a4d1e  <sxs4wpw
004a4dfc  <cxc4gpg
004a4e1a  <kxk4opo
004a4e38  <sxs4wpw
004a550a  XfTbSu
004a575d  bXbPfLj
004a59f9  bXb7&#>
004a5de5    !zdea~
004a6fdc  GQCw'y'
004a6ff4  GQCw'y'
004a700c  GQCw'y'
004a7024  GQCw'y'
004a703a  GQCw'y
004a704e  GQCw'y
004a705e  GQCw'y
004a72c2  Csg0Ss
004aa47e  RTKit_release-3504.0.0.0.1.release
004aa75d  stk_fail
004aa766  !Mthd:%p
004ac23c  not set
004ac5a8  coverglass-serial-number
004ae015  _HNIq$
004aea7c  aw`wnw
004aedb2  qpzewww
004af077  qdwww9
004c1e68  display-timing-info
004c1f03  >subframe-duration-nclks
004c1f1c  display-lead-time-nclks
004c1f34  subframe-interrupt-time-lines
004c1f52  frame-duration-nclks
004c1f90  mbox-register-len
004c1fa2  mbox-register
004c201c  DispTargetEXT
006e35f4  piodma-t-nclks
006e3603  swmpr-t-nclks
006e3611  frame-duration-lpm-nclks
006e36a0  oracle-tc-red
006e36ae  oracle-tc-green
006e36be  oracle-tc-blue
006e36cd  oracle-sf-red
006e36db  oracle-sf-green
006e36eb  oracle-sf-blue
006e3724  DispTargetP62
006e3732  DispTargetP63
006e3740  DispTargetP64
006e374e  DispTargetP68
006e375c  DispTarget595
006e376a  DispTargetS510
006e3779  DispTargetS837
006e3788  DispTargetS807
006e3797  DispTargetS68
006e37a5  DispTargetS68_DOE1
006e37b8  DispTarget67
006e37c5  DispTargetX3200
006e3ba0  proxboled-config
006e47f4  backlight-calibration-parameters
006e4815  color-accuracy-index
006e482a  vbatt-current
006e4838  raw-panel-id
006e4845  dcvrr-a
006e484d  dcvrr-b
006e4855  dcvrr-c
006e485d  dcvrr-d
006e4865  apt-version-control
006e4879  tcon-2dira-enable
006e48a8  adisp-register-len
006e48bb  adisp-register
006e48ca  service-node-match
006e48dd  power-gates
006e48e9  power-gates-len
006e48f9  power-gates-stg2
006e490a  power-gate-dsg
006e4919  power-gate-dbe
006e4928  power-node-split
006e4939  clock-ids
006e4943  dptx-generic-sdp-base
006e4959  perf-addr
006e4963  bw-addr
006e4bc8  fc~kbf
006e5d41  bX=XVC
006ecbf9  Ifg>Ibf
006f531f  bBX"iT
006f5dd3  /OcMw:
006fd1f1  Ifg>C37
007016ac  #wcw"C
007055c1  (HBpLbBX
00709591  V=[ded
007096bc  `DVK+g
0070c858  tvx{ppqrrqpp{xvt
0070c884  jnty[^bfRTVXPPPQTRQP^[XVnjfb
0070c8b8  fls{OTY_>BFJ468;00122100;864JFB>_YTO{slf
0070c8f4  [ckt@FMT*/4:
0070c934  ^hq{<DMU '.5
0070c94c  5.' UMD<{qh^
0070cc8d  4OjjO4
0070ccad  .JffJ.
0070cccd  *GccG*
0070cd09  )FccF)
0070cdd9  %DccD%
0070d01d  %DccD%
0070d0ed  )FccF)
0070d129  *GccG*
0070d149  .JffJ.
0070d169  4OjjO4
0070d4a4  ^hq{<DMU '.5
0070d4bc  5.' UMD<{qh^
0070d4fc  :4/*TMF@tkc[
0070d51c  fls{OTY_>BFJ468;00122100;864JFB>_YTO{slf
0070d55c  bfjnVX[^PQRTQPPPXVTRfb^[ytnj
0070d594  tvx{ppqrrqpp{xvt
00714b8e  NOi=_o
00718c0e  &(HbA8
0072e8a4  fc>Iff
00733b36  9@Oeww
00735e60  {|}}zzz{{{zz
00735eb0  tuwxppqrnnnonnnnqppowutr~|zx
00735f5c  psvzfikn_`bdYZ[]VWWXUUUVWWVV[ZYXb`_]kifdvspn
00735fbc  hknq]_beTVXZNOQRJKLMIIIJJJIINMLKTRQO]ZXVheb_uqnk
0073601c  impt\_beQSVYHJLNBCEF>?@A===>>>==BA@?HFECQNLJ\YVSieb_xtpm
00736080  imquZ]aeMPSVBEGJ:<>@56791234111132117654><:9GEB@SPMJa]ZVqmie
007360e8  fjosUY]aGKNR;>AD2469+-.0''(*%%%&%%%%(''&.-+*6420A>;9NKGD]YURojfa
00736150  mrw|Z_chJNRV<?BF0258&(*-
00736180  *(&$520-B?<8RNJFc_ZVwrmh
007361c0  ]bglKOTX:>BF-037!$&)
007361f4  -)&$:730KFB>]XTOqlgb
00736230  \aflHMRW7;?D(+/3
00736268  +($!;73/MHD?a\WRwqlf
007362a0  aglrLQV[8=BG'+/4
007362c8  4/+'GB=8[VQLrlga
007362fc  bhntKQV\7;AF$(-2
00736320  2-($FA;7\VQKtnhb
00736354  ]cipFKQW05;@
00736374  50+&KF@;c]WQ}vpi
007363a4  elryLRY_5;AF %*0
007363c4  ;50*RLFAle_Y
007363f4  T[ah<BHN%*06
00736410  B<60[TNHvoha
0073643c  ^elsDJQW+17=
00736458  =71+WQJDsle^
00736484  [bip@FMT&-39
0073649c  93-&TMF@pib[
007364c8  X_fn<CJQ"(/5
007364e0  C<5/_XQJ}unf
00736508  dls{GNU]+29@
00736520  @92+]UNG{sld
00736548  bjrzDLS[(/6=
00736560  =6/([SLDzrjb
00736588  ahpxBIQY%,3;
007365a0  IB;3haYQ
00736640  EMU]%-5=
007367bc  NWaj*3<E
007367cc  E<3*jaWN
007367f0  FOYb!*4=
00736800  OF=4ulbY
00736820  [dnw5>HQ
00736864  SI@6zpf]
007368b4  Xblv1;DN
00736954  C9/%laWM
007369e0  D9/%ncYN
00736a2c  LWbl"-7B
00736a94  A6+ laVK
00736ae0  KVal *5@
00736aec  @5* laVK
00736b44  LA5*xmbW
00736b8c  Xcoz+7BM
00736c1c  K?4(xmaV
00736c70  NB7+|peY
00736c8c  Uamx'3>J
00736ce0  Zeq}+7BN
00736d18  K?3(znbV
00736d94  MA5)|peY
00736db0  Vbnz&2>J
00736e7c  Vbnz&2>J
0073729c  J>2&znbV
00737368  J>2&znbV
00737384  Yep|)5AM
00737400  Vbnz(3?K
00737438  NB7+}qeZ
0073748c  J>3'xmaU
007374a8  Yep|+7BN
007374fc  Vamx(4?K
0073758c  MB7+zocX
007375d4  Wbmx*5AL
0073762c  KVal *5@
00737638  @5* laVK
00737684  KVal +6A
007376ec  B7-"lbWL
00737738  NYcn%/9D
007377c4  MWal%/9C
00737864  ND;1vlbX
007378b4  ]fpz6@IS
007378f8  QH>5wnd[
00737918  Yblu4=FO
00737928  =4*!bYOF
0073794c  NWaj*3<E
0073795c  E<3*jaWN
00737ad8  =5-%]UME
00737b78  QYah3;BI
00737b8c  ;3,%YQIBxpha
00737bb4  bjrzDLS[(/6=
00737bcc  =6/([SLDzrjb
00737bf4  dls{GNU]+29@
00737c0c  @92+]UNG{sld
00737c34  fnu}JQX_/5<C
00737c4c  5/("QJC<nf_X
00737c78  [bip@FMT&-39
00737c90  93-&TMF@pib[
00737cbc  ^elsDJQW+17=
00737cd8  =71+WQJDsle^
00737d04  ahovHNT[06<B
00737d20  60*%NHB<ha[T
00737d50  Y_elAFLR*05;
00737d6c  0*% FA;5_YRLyrle
00737d9c  ipv}QW]c;@FK&+05
00737dc0  @;50WQKFpic]
00737df0  bhntKQV\7;AF$(-2
00737e14  2-($FA;7\VQKtnhb
00737e48  aglrLQV[8=BG'+/4
00737e70  4/+'GB=8[VQLrlga
00737ea4  flqwRW\a?DHM/37;!$(+
00737ee0  3/+(D?;7WRMHlfa\
00737f18  bglqOTX]>BFK037:$&)-
00737f4c  )&$!730-FB>:XTOKlgb]
00737f88  hmrwVZ_cFJNR8<?B-025$&(*
00737fb8  -*(&8520FB?<VRNJhc_Z|wrm
00737ff8  afjoRUY]DGKN9;>A0246*+-.&''(%%%%&%%%*(''0.-+9642DA>;RNKGa]YUsojf
00738064  eimqVZ]aJMPS@BEG9:<>45671123111143219765@><:JGEBVSPMea]Zuqmi
007380cc  mptx_beiSVY\JLNQCEFH?@AB==>>>===A@?>FECBNLJHYVSQeb_\tpmi
00738134  knqu_behVXZ]OQRTKLMNIIJJJIIIMLKJRQONZXVTeb_]qnkh
00738198  npsvdfik]_`bXYZ[VVWWVUUUXWWV][ZYdb`_nkifzvsp
00738254  xz|~rtuwoppqnnnnonnnrqppxwut
007382b4  zz{{{zzz}}|{
0074c991  |:fik[
00750c61  #J,RXI
00751bbc  Hvww`w
00753c6c  ilosbceg```aecbaolig
00753c9c  jpv|W[`eILOSBCEG@@@AECBAOLIG`[WSvpje
00753cd8  V]dk@EKP/37;%'), !"#"!  )'%#73/,KE@;d]VP
00753d3c  71+&TLE>vmd\
00753d5c  ENWa&-5=
00753d70  =5-&aWNE
00753d8c  LVal&/9B
00753d9c  B9/&laVL
00753db4  Yeq~.8CN
00753dc4  NC8.~qeY
007540b9  3NiiN3
007540d9  ,HccH,
00754189  6TqqT6
007541b9  0NllN0
007541e5  .LkkL.
00754221  &EddE&
00754515  %CaaC%
00754591  1NkkN1
007545b1  1NjjN1
007546b5  0IbbI0
007546d8  )AYrA)
00754924  NYeq$.8C
0075495c  LB9/wlaV
0075498c  E=5-kaWN
007549ec  dks{KPV]7;@E),/3"#%'   !%#"!/,)'@;73VPKEskd]
00754a30  `ejpOSW[EGIL@ABCBA@@IGECWSOLje`[
00754a6c  osv{egil`abcba``igecvsol
00769fe3  DG8ANe
00773c18  stk_fail
00773c21  rtk_background
00773c30  %s-afk-log
00773c3b  dcp_force_syslog
00773c4c  power_work
00773c57  power_remote_work
00773c69  ASSERT!%s:%d power_conductor not inited
00773c91  platform_config_common.cpp
00773cac  dcp_background_thread_priority
00773ccb  dcp_ktrace_thread_priority
00773ce6  ktrace_work
00773cf2  dcp_kdebug_capacity
00773d06  ASSERT!%s:%d status=0x%x
00773d1f  dcp_kdebug_threshold
00773d34  dcp_kdebug_mask
00773d44  main.cpp
00773d4d  ASSERT!%s:%d Invalid IO Base 0x%llx or IO Size %u
00773d80  DCPTunables.h
00773d8e  ASSERT!%s:%d Received config size (%zu) is not as expected (%zu)
00773dcf  DCPTunablesT8160.h
00773de2  DispTargetP510
00773df1  DispTarget348
00773dff  DispTarget301_D90
00773e11  DispTarget109
00773e1f  Failed to map registers
00773e37  dcp_tracekit_buffer_kb
00773e4e  tracekit_work
00773e5c  dcp_tracekit_control
00773e71  log_tx
00773e78  dcp_log_coalescer_flush_priority
00773e99  ASSERT!%s:%d MBI_ENDPOINT_BUILT_IN_OSLOG not enabled!
00773ecf  platform_logging_common.cpp
00773eeb  dcp-2-smc
00773ef5  dcpsec-2-smc
00773f02  targetTBClient.cpp
00773f78  BrightnessUtilControllerPMUTBServer::Handler
00773fc0  TCONiBootInterfaceTBServer::Handler
00773fe4  invalid tag in `[UInt8]` metadata: 0x%x
0077400c  I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8
0077404f  invalid result returned from setEnabled
00774077  invalid result returned from setRawBrightness
007740ab  invalid result returned from displayPower
007740d5  invalid result returned from set2diraEnable
00774101  invalid result returned from getSerialNumber
0077412e  invalid result returned from displayPmicDebugPanic
00774161  invalid result returned from getConfigInfo
0077418c  !MIDR: 0x%x
00774198  ~CsPTR
0077419f  !ROf %#lx %#x
007741ad  pagetracker-impl.inc.h
007741c4  PGT_ERROR_ALREADY_MAPPED
007741dd  PGT_ERROR_VA_OUT_OF_RANGE
007741f7  PGT_ERROR_MAPPING_TOO_BIG
00774211  PGT_ERROR_NO_SPLITTING
00774228  PGT_ERROR_MAP_MODES_NOT_COMPATIBLE
0077424b  PGT_ERROR_NOT_MAPPED
00774260  PGT_ERROR_ALLOCATION_FORBIDDEN
0077427f  PGT_ERROR_UNTYPED_CREATE_FAILED
0077429f  PGT_ERROR_OUT_OF_CAP_SLOTS
007742ba  PGT_ERROR_OUT_OF_FRAMEISH_SLOTS
007742da  PGT_ERROR_OUT_OF_TABLE_SLOTS
007742f7  PGT_ERROR_CANT_REMAP_PARTIAL
00774314  unknown pgt_error_t value
0077433d  pgt_map_pa_range(va=%lx, pa=%llx, size=%lx, offset=%lx): not page-aligned
00774387  err1: %s at offset: %#lx, err2: %s
007743aa  range [pa=%llx, size=%lx] not in untypeds (try adjusting .mmio)
007743ea  range [pa=%llx, size=%lx] stretches past end of untyped (try adjusting .mmio)
00774438  untyped (%s) !size
0077444b  untyped (%s) !cap_slot
00774462  !untyped
0077446b  !pgt_assert (%s:%d)
0077447f  !mode %#x
00774489  pagetracker-bits.h
0077449c  !aligned
007744a5  invalid page state
007744b8  err: %s offset: %#lx, then when unmapping partial result, pgt_unmap err: %s
00774504  err: %s offset: %#lx, then when re-mapping large, pgt_map_pa_range err: %s
0077454f  this thread's stack
00774563  pagetracker state
00774575  va_overlap %s
00774583  PageFrame_Protect err: %s
0077459d  pgt_actually_unmap_frame
007745b6   (untyped cap was RO but tried to map as RW?)
007745e4  %s: map attr err: %s%s
007745fb  pgt_actually_map_frame
00774612  L4_Cap_Delete err: %s
00774628  overflow
00774631  pgt_map_internal
00774642  bad page table level
00774657  pa=0x%llx size=0x%llx cap_slot_idx=0x%x
0077467f  !tree depth
0077468b  !space +future_untyped_count
007746a8  !tree index
007746b4  untyped (%s) overlaps with (%s)
007746d4  !mmu lock:%x
007746e1  !2xinit
007746e9  !ctors %zu %zu
007746f8  !osckit-headers:%u,%u/%u,%u
00774715  Platform timer does not support setting frequency (for now)
00774751  L4_ErrorSuccess
00774761  L4_ErrorPreempted
00774773  L4_ErrorCanceled
00774784  L4_ErrorTruncated
00774796  L4_ErrorCapInvalid
007747a9  L4_ErrorSlotInvalid
007747bd  L4_ErrorMethodInvalid
007747d3  L4_ErrorArgumentInvalid
007747eb  L4_ErrorOperationInvalid
00774804  L4_ErrorPermissionInvalid
0077481e  !endpoint
00774828  !early-boot
00774835  chan msg type %#x != DATA
0077484f  !data body size
0077485f  chan msg type %#x != PHYS_ACCESS
00774880  !PAB size
0077488a  !PAB: m=%#x a=%#llx s:%zu
007748a4  !phys-access
007748b1  !cap_slot: %d
007748bf  !find_channel: %#x %#x %#x
007748da  !sem_wait %#x
007748e8  !copy_message: s %#zx ms %#zx
00774906  !copy_message 2
00774916  rptr 0x%zx wptr 0x%zx size 0x%zx
00774938  sem !empty
00774943  hosted_ipc: PHYS_ACCESS %#x != %#zx
00774967  bad msg %#x
00774973  RTK_hashtable_init
00774986  malloc
0077498d  RTK_hashtable_set
0077499f  !badge:%u
007749a9  !notify:%s(%lu)
007749b9  !prio:%s(%lu)
007749c7  !pac,%#llx:%#llx:%#llx:%#llx:%#llx
007749ea  !pac,irq
00774a08  Duty cycle
00774a13  Sleep count
00774a1f  Wake count
00774a2a  Power state
00774a36  Free heap
00774a40  Total heap
00774a4b  Peak heap alloc
00774a5b  Used stack
00774a66  Total stack
00774a72  CPU count
00774a7c  Thread time
00774a88  Performance
00774a94  Terminator
00774aa3  ASSERTION FAILED: %s:%d
00774ac3  ThIntr:%u,%u,%u,%u
00774ad6  ThLock:%p
00774ae0  MBI queue overflow:%s
00774af6  !Mthd:%p
00774aff  unimplemented
00774b0d  [CED] CLLT escalation detected
00774b2d  mme:0x%x
00774b36  SPMI:%d (%d,%#X,%u)
00774b4a  SPMI Fatal Error: %s Blocked
00774b67  Transfer
00774b70  HW Q Reset
00774b7b  Filter Modification
00774b8f  VmOv %d %d
00774b9a  !vm nodes
00774ba4  Unbalanced transients
00774bba  RTKit: %s - Client: %s
00774bd1  __cxa_guard_acquire
00774be5  __cxa_guard_release
00774bfd  MGMT msg=0x%llx st=%x
00774c13  MGMT st=%x
00774c1e  !reg clscr %u ps: 0x%x, 0x%x
00774c3b  !kb reg:%x
00774c46  rtk_ep_work
00774c5d  Corrupt log channel
00774c71  LOG: entries sz >= coalescer sz (%zu >= %zu)
00774c9e  log_flush
00774ca8  !flush: %x r=%zu w=%zu (%zu/%zu)
00774cc9  <null>
00774cd0  pmc.cpp
00774cd8  %s PMC Not IDLE, dcp_pipe=%d perf_state=%d
00774d03  RTKPMGR_pmc_boost_disp_perf_state
00774d25  %s dcp_pipe=%d perf_state=%d
00774d42  PMCLib Init
00774d4f  pmgr_t8160.cpp
00774d5e  Welcome to RTKitPMGR!: %s : t8160
00774d80  RTKPMGR_platform_init
00774d96  Disp perf state table is not set properly
00774dc0  %s: RTKitPMGR cannot config LAPLL for device %d
00774df0  RTKPMGR_config_pll
00774e03  RTKPMGR_platform_get_disp_clock
00774e23  pmgr.cpp
00774e2c  RTKPMGR_config_video_clock
00774e47  %s: disp_index= %d,  configPll= %d, srcSel= %d, divider= %d
00774e83  %s lvl=%d
00774e8d  RTKPMGR_set_log_lvl
00774ea1  %s Enabling PMC APIs
00774eb6  RTKPMGR_enable_pmc
00774ec9  RTKPMGR_enable_profile
00774ee4  rtkpmgr-profile
00774ef4  rtkpsd_platform_default.cpp
00774f10  %s: Invalid client
00774f23  initClientConfig
00774f34  Invalid numServiceSlots: 0x%x
00774f52  %s:client not init
00774f65  getServiceName
00774f74  %s: invalid param
00774f86  %s: Invalid slot pio index for client: %#x service: %#x
00774fbe  %s: invalid id: %u
00774fd1  getResetSendPayload
00774fe5  %s: invalid payload ptr
00774ffd  Client not initialized!!
00775016  Latency to P State Translation Failed
0077503c  Invalid slot pio index for client: %#x service: %#x
00775070  %s: client not init
00775084  initServiceConfig
00775096  %s: Invalid initConfig
007750ad  %s: serviceId 0x%x already initialized
007750d4  getNumServiceSlots
007750e7  getServiceConfig
007750f8  %s: Error Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
0077513f  %s: Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
0077516a  rtkpmgr-loglvl
00775179  rtkpsd_common.cpp
0077518b  %s: getServiceConfig(0x%x) err: 0x%x
007751b0  _initServiceDashboard
007751c6  %s: Unsupported service id: 0x%x
007751e7  %s:RTK dev init(0x%x) fail: 0x%x
00775208  %s:RTK dev config(0x%x) fail: 0x%x
0077522b  %s:RTK dev wake(0x%x) fail: 0x%x
0077524c  %s: Not support PSD ACK mode: %d
0077526d  _stateChange
0077527a  %s: Prev req pending service=0x%x wrVal=0x%x: 0x%x
007752ad  %s: Prev reqs caused sem signal service=0x%x wrVal=0x%x: 0x%x
007752eb  PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x) prevRdVal: (%#x) timeout after %llu usec
0077535d  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) sem wait err: (%#x)
007753ab  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) != rdVal: (%#x) err
007753f9  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x)
00775440  _getPowerStateVote
00775453  %s: client=0x%x service=0x%x err: 0x%x
0077547a  %s: clientId=0x%x serviceId=0x%x pstate=%d
007754a5  %s: initClientConfig err: 0x%x
007754c4  initPSDService
007754d3  %s: initServiceConfig err: 0x%x
007754f3  %s: initServiceDashboard err: 0x%x
00775516  %s: done clientId=0x%x serviceId=0x%x
0077553c  %s: clientId=0x%x serviceId=0x%x active=%u ltr_usec=%u
00775573  enablePSDService
00775584  %s: getNumServiceSlots err: 0x%x
007755a5  %s: invalid params
007755b8  %s: stateChange(serviceId 0x%x) err: 0x%x
007755e2  %s: clientId=0x%x serviceId=0x%x
00775603  getPSDServiceVote
00775615  %s: _getPowerStateVote(serviceId 0x%x) err: 0x%x
00775646  %s: Reset already initialized
00775664  initPSDReset
00775671  %s: routingEpId=0x%x
00775686  %s: Reset not initialized
007756a0  sendPSDReset
007756ad  %s: getResetSendPayload err: 0x%x
007756cf  %s: Start - routingEpId=0x%x id=0x%x payload=0x%llx
00775703  %s: MBI send msg timeout (routingEpId=0x%x id=0x%x)
00775737  %s: MBI send msg err (routingEpId=0x%x id=0x%x): 0x%x
0077576d  %s: MBI recv msg timeout (routingEpId=0x%x id=0x%x)
007757a1  %s: MBI recv msg err (routingEpId=0x%x id=0x%x): 0x%x
007757d7  %s: checkResetRcvdPayload err: 0x%x
007757fb  %s: Done - routingEpId=0x%x id=0x%x payload=0x%llx
00775835  setPSDLogLevel
00775844  mcw_v1.cpp
0077584f  Requested buf size(%d) is greater than max allowed size(%d)
0077588c  Requested address alignment value(%d) is not supported.
007758c5  Invalid parameters. bufid:%d buf_size:0x%x max_size:0x%x
007758ff  Request to allocate bufid %d while it is already mapped
00775938  Bufid 0x%x offset 0x%x size 0x%x crosses max size 0x%x
00775970  Failed to map for bufid %d size 0x%x. status:0x%x
007759a3  SRAM buffer allocation failure- bufid:%d  buf_offset:0x%x buf_size:0x%x status:0x%x
007759f8  Invalid buf_st_addr parameter
00775a17  Invalid parameters. bufid:%d
00775a35  Request to deallocate bufid %d when it is not allocated
00775a6e  Failed to unmap for bufid %d. status:0x%x
00775a99  SRAM buffer deallocation failure- bufid:%d status:0x%x
00775ad1  INVALID
00775ad9  PRIM_DCP
00775aea  SEC_DCP
00775af2  ACPU_AUDIO
00775afd  UNKNOWN
00775b05  Unknown mcw clientid %s (%d)
00775b23  MCW client %s (id=%d) is not supported on this platform
00775b5c  RTK_dev_control failed with error 0x%x
00775b84  !power: %#x
00775ba3  !hst:%#x
00775bb4  !Heapblk:%p
00775bc0  !mbs:%zu
00775bce  !TBVI: rt=0x%x, st=0x%x
00775bf2  /allowlists
00775bfe  routing
00775c0f  TB BdSt %#x
00775c1b  !ASPA%#x
```
