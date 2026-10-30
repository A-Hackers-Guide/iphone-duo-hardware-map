# `Firmware/dcp/t8160dcp.im4p`

- File size: 3,016,187 bytes
- IM4P: Tag: IM4P  Type: dcpf  Version: 1
- BuildManifest components that use it: `DCP`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         dcpf
  Version:      1
  Data:         3.0 MB (3016151 bytes)
  Compression:  LZFSE
  Uncompressed: 17 MB (17022976 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 17,022,976 bytes
- Format: raw binary

## Identity strings (versions, build tags) [FW]

- `%s: RTKitPMGR cannot config LAPLL for device %d`
- `@(#)PROGRAM:AppleFirmwareKit  PROJECT:AppleFirmwareKit-743.40.4`
- `Apple Inc.`
- `AppleDCP-1317.40.16~1190-t8160dcp.RELEASE`
- `BUILD-INFO[390]:{"DisplayName":"roottask.IOP_ASC8.RELEASE","DisplayVersion":"1223.40.8~1601","BuildTime":"2026-10-03T15:46:14-0700","ProjectName":"pitayaOS","ProductName":"roottask.IOP_ASC8.RELEASE","SourceVersion":"1223.40.8","BuildVersion":"1601","BuildConfiguration":"RELEASE","BuildType":"Officia`
- `RTKit: %s - Client: %s`
- `RTKit_armv8_cl4_Oz_flto_pac-3514.40.18.release`
- `RTKit_release-3504.0.0.0.1.release`
- `Welcome to RTKitPMGR!: %s : t8160`
- `[AFK]DCP Firmware (firmware version:%s RTKit version:%s Variant:RELEASE)`
- `requested IRQ not found (i: %u, RTKit %s: %#x, cL4 %s: %#x)`

## Strings (17,756) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.
First 4,000 of 17,756.

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
0005f57f  qH(EzK
0005fae3  7hVA9h
0005faeb  6hZA9(
00061020  _h(8Hhw
00061068  _h(8Hhw
000613a7  JTig8q
000702c6  @9|N@yaR@y`
000757d0  hFB9iBB9
00075bb3  TLa@9-
00075be7  T{FA9iBA90
00075d23  ThNA9H
00075e27  4hBA9uB
00079a6f  TaBA9b"D
0007b1cc  xBAyyFAyz^Ay{bAy
000842eb  7hFA9H
0009a347  ThnP9(
0009b09b  RhnP9h
0009b3a7  7hBHy)
000afc2f  TUX@)X
000c7193  6hrK9H
000c75b9  bG9hbK9
000c762a  \8hbK9
00120463  Rb2Hzi6
0012c513  4hBB9H
0013399b  4hBB9H
00139a5f  4hbF9H
00139d64  ibF9hv
0013a08b  4hbF9H
0013b2aa  G9JAB9
0013b3ea  C9JAB9,
001560a4  )Ih8HIh8
001561ab  Rmij8J
00156237  9mii8)
0015634b  9lii8)
0015689b  RLii8)
001776e3  2Lh(8Mih8
0017c99a  Y8hfI9(!
0018319a  ]8ibU9
001b1a1e  @9hBH8
001e7893  Thb@9h
001f091f  ylyix)
001f0dc1  sJyn.S)
001f1d5b  ThBA9h
001f3278  hJh8I{h
001f471c  ,klx,k-xL
001f51e1  zhxi*@
001f59c9  {uxi*@
001ff766  @9-Q@xjA
0020446e  @yoy-x
00204696  @yoy-x
00204c4b  TMy)x{vCy
00204f13  TMy)xu
002051b7  Tny*xn
00205297  *azCy|
0020545b  Tny*xnzCy
0020743b  T*QBx_
0020745b  T*QBx_
0020b739  yvxJyvx)
0020ca97  TpvYyoRly
0020caaa  YyoVly?
0020cab7  T`zYyoZly
0020caca  Yyobly?
0020cbc8  pvYy`zYyq
0020ce46  DygJVy
0020ce56  Eyg&Ey
0020ce66  EygRVy
0020ce76  EygZVy
0020d10e  Byg"By
0020d134  gnCyfJVy
0020d143  Tt~CyfNVy
0020d153  TurCyfRVy
0020d166  CyfZVy
0020d264  gnCyurCyt~Cyv
0020dccc  oylxninx
0020dceb  4iYixj
0020e0cb  4'RBxE
0020f2ce  PyuvCyjzCy8
0020f339  {nxQ{nx
0020f397  RNyhxoyhx
0020f459  {nxQ{nx
0020f4b7  RNyhxoyhx
002115f6  fyv~Yy|
00211653  R/{mxp{mx
002116b7  R.ylxOylx
00211e1b  TanBy",
0021219b  Qhzxx 
00212343  TMAry.Ary
002123a3  TMAry.Ary
00212409  AryNAry
0021248b  TnAryOAry
002124f1  AryNAry
00212535  AryoAry
002125b9  ArypAry
002126a5  ArypAry
00212733  T+AryLAry
00212753  T+AryLAry
00212773  TLArymAry
002127c7  T+AryLAry
002127df  T+AryLAry
002127ff  TKAry,Ary
00212817  TLArymAry
00212839  Ary+Ary_
00212857  TlAryMAry
00212891  ArynAry
002128ad  ArylAry_
00212b31  ArylAry?
00212b85  AryJAry
00212ba9  AryJAry
00212be5  AryJAry
00212c35  ArykAry
00212c91  ArymAry
00212fe1  Bry1Bry
00213099  AryQAry
002130d9  AryQAry
002130f1  Ary+Ary_
00213169  Ary+Ary_
0021325d  AryLAry
0021327d  Ary-Ary
002132d9  ArylAry_
002132f9  Ary+Ary_
00213319  AryKAry?
00213331  Ary+Ary_
002133c9  Ary-Ary
00213515  Ary+Ary_
0021352d  Ary+Ary_
00213563  T+AryLAry
00213585  Ary+Ary_
002137cb  TLAry.Ary
00213815  Ary+Ary_
0021382d  Ary+Ary_
0021384d  Ary-Ary
00213891  AryOAry
00213989  AryLAry
002139b9  ArylAry_
002139d9  Ary+Ary_
002139f5  AryOAry
00213a15  AryKAry?
00213a2d  Ary+Ary_
00213a75  Ary+Ary_
00213a91  Ary+Ary_
00213b45  AryNAry
00213be5  AryPAry
00214873  9KIE9?
0021506f  9KIE9?
0021705f  TMABy.ABy
002170b3  TMABy.ABy
0021710d  AByNABy
0021717f  TnAByOABy
002171d9  AByNABy
00217219  AByoABy
0021728d  ABypABy
0021735d  ABypABy
002173e7  T+AByLABy
00217407  T+AByLABy
00217427  TLABymABy
0021747b  T+AByLABy
00217493  T+AByLABy
002174b3  TKABy,ABy
002174cb  TLABymABy
002174ed  ABy+ABy_
0021750b  TlAByMABy
00217545  ABynABy
00217561  ABylABy_
002177c1  ABylABy?
0021780d  AByJABy
00217831  AByJABy
00217869  AByJABy
002178b5  ABykABy
0021790d  ABymABy
00217b8d  ABy0ABy
00217cbd  ABy0ABy
00217cf5  ABy+ABy_
00217d59  ABy+ABy_
00217e3d  AByLABy
00217e5d  ABy-ABy
00217ead  ABylABy_
00217ecd  ABy+ABy_
00217eed  AByKABy?
00217f05  ABy+ABy_
00217f89  ABy-ABy
00218095  ABy+ABy_
002180ad  ABy+ABy_
002180e3  T+AByLABy
00218105  ABy+ABy_
002182db  TLABy.ABy
0021831d  ABy+ABy_
00218335  ABy+ABy_
00218355  ABy-ABy
00218391  AByOABy
00218479  AByLABy
002184a9  ABylABy_
002184c9  ABy+ABy_
002184e5  AByOABy
00218505  AByKABy?
0021851d  ABy+ABy_
00218565  ABy+ABy_
00218581  ABy+ABy_
0021861d  AByNABy
002186ad  AByOABy
0022b38b  7hFa9H
00243804  ibB9jb
002524f4  Jiv8h&
0027228c  irJ9hf@
00276d13  7h{xx){xxJ{xx
00285885  kt8Zyt
002ab383  7hnG9(
002ad094  Qio8Bi`8Aip8?
002ad0f0  Bin8@io8
002b3cc1  yjxny*x
002b4a33  RNyhx.y(xnyh
002b4ad0  +yhxKy(xk
002b5a64  Lyixly)x)
002b701b  RoyixOy)x
002b70c7  R,yhxLy(x
002b7183  R+yhxkz(x
002d2d8c  kil8KA
002d55c4  kil8KA
002e0537  RadanBdan
002e05fc  lyhx,y(
002e58f0  hkv8)'@
002e6ac4  hR]yiV]yk
002ee9dc  Hq@yIy@yJ
002f3390  HGAyICAy*}
002f3603  *+{hxl[@
002f3c33  =0FAy BJ
002f4898  kyzxk}
002f4ae0  )ytxjZ@
002f519f  TiFD9h"@
002f53ab  TiFD9h"@
002f592f  TiFD9j"@
002f737b  *VXfx7
003017f4  4UA)WaA)
00301848  5]A)ZmA)
00306873  R-yhxNyhx
003068db  RNyixoyix)
003091b4  4UA)WaA)
0030b713  6h"Byi
00318df3  Rmyix.
00319093  RmyjxN
00319167  Rmyix.
0031b7e0  jBDyiFDy
0031dc2b  TirR9?
0031f3bf  Rcyj|c
0031f41b  Rcyj|c
0031fe87  Tcyd|c
00320037  TIyCy_
00321134  jBDyiFDy
003235f7  TirR9?
003245d7  Rcyj|c
00324633  Rcyj|c
00324ce7  Tcyd|c
00324e97  TIyCy_
00327a49  khx){v
003281b8  /ko8pyj
0032a138  jzByK}
0032a62f  *hrC9j
0032ab5c  h:Byv>ByiFBywIj
0032b23f  5jvByJ5
0032b297  TjrByJ5
0032b737  TirC9?
0032bb7b  TirC9?
0032e063  R.yhxNy(
0032e54b  ThrC9)
0032e5ac  hBE9iNA
0032ecbf  Tv~Byw
0032ff1c  jzByK}
0033024c  jJByK}
0033074b  *hrC9j
00330c73  TvjByynBywzBy
00330c8c  v:Byy>BywFBy
00330ca8  v:Byy>BywvBy`
00331393  5jvByJ5
003313eb  TjrByJ5
0033188b  TirC9?
00331e87  TirC9?
00333d2f  RkjkxjjjxJ}
00333e17  Rijixhjhx`B
00334073  R.yhxNy(
003341c7  Rkjkxj}
00334217  ROyixoy)
0033429b  Rijixhjhx`B
00334737  ThrC9)
00334798  hBE9iNA
00334ac7  Rjjjxijix)}
00334c5b  RkjkxjjjxJ}
00334dcf  RjjjxijixS
00334e23  Rjjjxijix)}
00334fab  RkjkxjjjxJ}
0033511b  Rjjjxijix+
0033516f  Rjjjxijix)}
003352eb  Tv~Byw
00345eb0  *yjxB@
00370adc  WaA)ZmB)Ji@9
00383a23  Rij989
00389ed4  jZGyk^Gy)
00397218  v]A)zmB)km@9
0039e758  k<Ayl 
0039e95b  yj<Ayi$
00423f3f  Thr@9I
0043aa1f  ?8bunz8
0043b17f  ?UUUUUU
0043b1e7  ?bXM`8q
0043bfb0  8bunz8
0043c720  UUUUUU
0043ea6d  G1@(knN
0043eab4  DispTarget150_D90
0043ee70  DispTargetP61
0043ee7e  DispTargetS61
0043ee8c  power_enable
0043ee99  tb-transport-wl
0043eea9  trusted-route-wl
0043eeba  hid-route-wl
0043eec7  hid-transport-wl
0043eed8  hid-device-wl
0043eee6  endpointWL
0043eef1  system-server-wl
0043ef02  hpd-server-wl
0043ef10  hpd-down-wl
0043ef1c  hpd-up-wl
0043ef26  dcpexpert-service
0043ef38  system
0043ef3f  AFKDiagnostics
0043ef4e  HeapUsage
0043ef58  ThreadInfo
0043ef63  compartment
0043ef6f  system-epic
0043ef7b  test-service
0043ef88  test-epic
0043ef92  display-clock-manager
0043efa8  pmgr-dcp0-service
0043efba  pmgr-dcp1-service
0043efcc  pmgr-dcpext0-service
0043efe1  mcw-service-sec
0043eff1  mcw-service
0043effd  dptx-generic-sdp-count
0043f014  disp0-service
0043f022  disp0-epic
0043f02d  disp1-service
0043f03b  dispext0-service
0043f04c  brightness-service-v6x
0043f063  cb-ap-to-dcp-service-v6x
0043f07c  cb-ap-to-dcp-service-epic
0043f096  brightness-service-v68p
0043f0ae  cb-ap-to-dcp-service-v68p
0043f0c8  brightness-service-v68s
0043f0e0  cb-ap-to-dcp-service-v68s
0043f0fa  brightness-service-v68s-doe1
0043f117  cb-ap-to-dcp-service-v68s-d1
0043f134  brightness-service-x3200
0043f14d  transportType
0043f15b  cb-ap-to-dcp-service-x3200
0043f176  transport-stub
0043f185  controller-pmu-frontend
0043f19d  brightness-service-v61p
0043f1b5  cb-ap-to-dcp-service-v61p
0043f1cf  brightness-service-v61s
0043f1e7  cb-ap-to-dcp-service-v61s
0043f201  cbroot-service
0043f210  cbxtalk-service
0043f220  cbgenx-service
0043f22f  cbrootservice-epic
0043f242  cb-x3200-telemetry-zEDC
0043f25a  cbtelemetry-X3200-service
0043f278  dcp-trusted-client
0043f28b  aon-hpd-down-tb-client
0043f2a2  gpio-service
0043f2af  dispsec-spi
0043f2c3  nesos-driver
0043f2d0  tcon-service
0043f2dd  tcon-epic
0043f2e7  bim-epic
0043f2f0  tcon-iboot
0043f2fb  disp-health-mon-tb-client
0043f315  tcon-iboot-tb-proxy
0043f329  dcpav-dptx0-root-nub
0043f33e  dcpav-dptx0-root-service
0043f357  dbv-sdp-channel-index
0043f36d  hdcp_fuse_mask
0043f37c  dcpav-dptx0-core0-nub
0043f392  dcpav-dptx0-port0-nub
0043f3a8  dcpav-sac-controller
0043f3bd  dcpav-dptx-sec-root-nub
0043f3d5  dcpav-dptx-sec-root-service
0043f3f1  dcpav-dptx-sec-core0-nub
0043f40a  dcpav-dptx-sec-port0-nub
0043f423  dcpav-dptx1-root-nub
0043f438  dcpav-dptx1-root-service
0043f451  dcpav-dptx1-core0-nub
0043f467  dcpav-dptx1-remote-port0-nub
0043f484  aon-hpd-up-tb-server
0043f499  dcpexpert-epic
0043f4a8  endpoints
0043f4b2  generate-route-config
0043f4c8  trusted-route
0043f4d6  dptx-monitor-tb-if-client
0043f4f0  disp-health-mon-tb-if-client
0043f50d  aon-hpd-down-tb-if-client
0043f527  aon-hpd-up-tb-if-server
0043f53f  dcptrustedclient-tb-interface
0043f55d  brightness-util-tb-client
0043f577  tcon-iboot-tb-interface
0043f58f  tcon-bim-tb-interface
0043f5a5  bim-epic-tb
0043f5b1  {&RTK_platform_mbi_config}
0043f5cc  ap-route
0043f5d5  afkdcp-smc-service-ep
0043f5eb  afksmc-service
0043f5fa  afkdcppsec-smc-service-ep
0043f614  powerlog-service
0043f625  powerlog-epic
0043f633  md-manager
0043f63e  aop-route-dcp0
0043f64d  aop-route-dcp1
0043f65c  aop-test
0043f665  aop-test-control-epic
0043f67b  pwr-cntr-untrusted-v6x
0043f692  pwr-cntr-untrusted-v68-pri
0043f6ad  pwr-cntr-untrusted-v68-sec
0043f6cd  display-manager
0043f6e3  alscolorxtalk
0043f6f1  als-dcp-frontend
0043f702  als-dcp-frontend-sec
0043f717  dcp-control
0043f723  dcp-sec-control
0043f733  dptx-monitor-tb-ep
0043f746  disp-health-mon-tb-ep
0043f75c  aon-hpd-tb-down-ep
0043f76f  aon-hpd-tb-up-ep
0043f780  dcptrustedclient-tb-ep
0043f797  brightness-util-tb-ep
0043f7ad  tcon-iboot-tb-ep
0043f7be  tcon-bim-tb-ep
0043f7cd  management-ep
0043f7db  syslog-ep
0043f7e5  kdebug-ep
0043f7ef  tracekit-ep
0043f7fb  oslog-ep
0043f804  report-ep
0043f80e  iomfb-link
0043f819  tcon-ep
0043f821  bim-ep
0043f828  system-ep
0043f838  dcpexpert-ep
0043f845  disp0-ep
0043f84e  dcpav-controller-ep
0043f862  dcpav-power-ep
0043f871  dcpav-sac-ep
0043f87e  dcpav-device-ep
0043f88e  dcpav-service-ep
0043f89f  dcpav-interface-ep
0043f8b2  dcpdptx-port-ep
0043f8c2  dcpdptx-hdcp-ep
0043f8d2  cbservice-ep
0043f8df  cb-ap-to-dcp-service-ep
0043f8f7  aop-comms-dcp0-ep
0043f909  aop-comms-dcp1-ep
0043f938  RTKSTACK
0043f990  tTxEhTTR
0043fb09  Qkkbal
0043fdc7  -0123456789abcdef0123456789ABCDEF
0043fe08  SPMIv02
0043fe2c  RTKit_armv8_cl4_Oz_flto_pac-3514.40.18.release
00440a38  AAPL,phandle
00440a45  afklib
00440a58  service_id
00440a70  afklib
00440a7d  afklib
00440a84  physical-layer-wl
00440bc0  local_stop_state
00440bd1  local_shtdn_state
00440be3  remote_stop_state
00440bf5  user_stop_state
00440cf3  DebugState
00440e38  md-allocator
00440e45  md-al-remote
00440eb8  register_local_power
00440ecd  register_remote_power
00440ee3  power_state_msg_mask
00440ef8  remote_power_msg_mask
00440f0e  workloops
00440f18  dispatchqueues
00440f27  cache-size
00440f78  logEvent
00440f81  clientId
00440f8a  service-up
00440f95  event-count
00440fa1  posted-event-count
00440fb4  cache-buffer
00440fc1  cache-cursor
00441018  SharedMemoryOffset
0044102b  gAFKConfigLogMask
0044103d  force-panic
0044104f  totalAllocCount
0044105f  totalBytes
0044106a  usedBytes
00441074  freeBytes
0044107e  <unknown>
00441088  stackSize
00441092  stackUsed
00441120  system-service
0044112f  reg-size-inc
0044113c  reg-stream-block-size
00441152  handler-workloop
00441163  handler-dispatch-queue
0044117a  service-matching
004411b0  transport-wl
004411bd  server-wl
004411c7  async-activation
004411d8  assert-service
004411e7  panic-on-assert-failure
004411ff  uhbr-rates
0044120a  max-lane-count
00441219  min-lane-count
00441228  supports-auxless-alpm
0044123e  max_lane_count
0044124d  min_lane_count
00441275  HDCPProtocolType
00441286  no-virtual-display
00441299  hpdUnplugTime
004412a7  deglitch
004412b0  ignore-rodco-roleakcomp-fuse
004412cd  max_pixel_clock
004412dd  PixelClockLimit
004412ed  Suspended
004412f7  alpm-data
00441301  wakeupLines
0044130d  wakeupCRSymbols
0044134c  auxPowerUpLines
0044135c  auxPowerUpWaitTime
0044136f  wakeupTPS1Length
00441380  wakeupTPS2Length
00441391  dptxWrap-seq2-pwrdn3-count
004413ac  enable-trusted-aon-hpd
004413c3  dcp-lpdptx-port-epic
004413d8  supports-ssc
004413e5  pclkdrv-select
004413f4  phy-ldo-bypass
00441403  driveSettings-rbr
00441415  driveSettings-hbr
00441427  driveSettings-hbr2
0044143a  driveSettings-hbr3
00441450  frequency
0044145a  noiseWidth
00441465  sacDivisor
00441470  dcpdptx-port-epic
0044149b  MaxActivePixelRate
004414ae  MaxTotalPixelRate
004414c0  MaxPixelWidth
004414ce  supports-phy-ps
004414de  no-dptx-src-sel
00441505  max_link_rate_2_lanes
0044151b  max_link_rate_4_lanes
00441531  alpm-shutdown-errata
00441546  aux_ch_ctl_2
00441553  fixed-m-vid
0044155f  force-video-bist-master-mode
0044157c  dp-crc-support
0044158b  adaptive-sync
00441599  no-psr
004415a0  no-fec
004415a7  foce-dptx-pll-lock
004415bf  aux-log-size
0044161d  alpm_ctl_1
00441628  alpm_ctl_2
00441633  hdcp_requested
00441642  lane-map
0044164b  pn-inv
00441652  target-require-talisman-wa
0044166d  target-require-abdc-wa
00441684  target-require-color-desat-wa
004416a2  target-capture-tcon-state-on-unplug
004416c6  target-require-x3442-vghl-wa
004416e3  min_link_rate
004416f1  max_link_rate
004416ff  max_training_pattern
00441714  external_link_symbol_clock
0044172f  default-power-state
00441743  hot_plug_delay_ms
00441755  hot_unplug_delay_ms
00441769  flexible-v-timing
0044177b  max-generic-sdp-count
00441791  virtual-dpcd
0044179e  require-trusted-aux-trigger
004417ba  require-trusted-link-debug-ctl
004417d9  require-trusted-video-ctl1
004417f4  VideoStreamEnabled
00441807  AUXTimeoutCount
00441817  AUXLog
0044181e  send-dmsg
00441828  dcpdptx-hdcp-interface
0044183f  vid-fifo-threshold
0044195c  dp-phy-fifo-threshold
00441972  dcpdptx-hdcp-auth-session
0044198c  supports-dsc
00441999  supports-alternative-target
004419b5  boot-args-prefix
004419c6  max_dsc_bpp
004419d2  aod-data
004419f4  lcd-off-on-ms
00441a02  support-headless-state
00441a19  support-tcon-power-mitigation
00441a37  control-rails
00441a45  pp1v24-power
00441a52  pp1vx-power
00441a5e  vccmain-power
00441a6c  qbuck-power
00441a78  refclk-gpio
00441a84  reset-gpio
00441a8f  xsync-on-to-pp1vx-delay
00441aa7  pp1v24-on-to-pp1vx-delay
00441ac0  ref-clk-on-to-rst-delay
00441ad8  vccmain-on-to-qbuck-delay
00441af2  qbuck-on-to-refclk-delay
00441b0b  rst-off-to-ref-clk-delay
00441b24  pp1vx-off-to-pp1v24-delay
00441b3e  pp1vx-sleep-min
00441b4e  pp1vx-power-on-override
00441b66  lcd-enable
00441b71  lcd-spi-clk
00441b7d  lcd-spi-mosi
00441b8a  lcd-spi-cs
00441b95  backlight-enable
00441ba6  backlight-pmic-enable
00441bbc  tddi-ngpio
00441bc7  lcd-on-to-spi-clk-delay
00441bdf  lcd-on-to-bl-pmic-delay
00441bf7  lcd-on-to-bl-delay
00441c0a  bl-pmic-off-to-bl-delay
00441c22  bl-pmic-off-to-lcd-delay
00441c3b  lcd-on-to-tddi-delay
00441c50  tddi-to-lcd-off-delay
00441c66  lcd-enable-no-power-off
00441c7e  backlight-enable-no-power-off
00441c9c  backlight-pmic-enable-no-power-off
00441cbf  dptx-secure-monitor
00441cd3  secure-aux-support
00441ce6  dptx-register-capture-done
00441d01  coverglass-serial-number-size
00441d1f  pmgr-id-wa
00441d2a  tcon-model
00441d35  display-pmic-debug-panic
00441d4e  InitializeTCON
00441d63  panel-serial-number
00441d77  DisplayPower
00441d84  tcon-firmware-version
00441d9a  tcon-ECID
00441da4  tcon-BNCH
00441dae  tcon-life
00441db8  tcon-SDOM-fused
00441dc8  tcon-PROD-fused
00441dd8  tcon-SDOM-value
00441de8  tcon-PROD-value
00441df8  tcon-cfg-hash
00441e06  tcon-cfg-hash-result
00441e1b  tcon-cfg-auth
00441e29  tcon-cfg-version
00441e3a  tcon-module-info
00441e4b  tcon-boot-status
00441e5c  tcon-failsafe-data
00441e6f  client-handle
00441e7d  useDirectNits2iDAC
00441e90  LmaxProduct
00441e9c  lMaxProduct
00441ea8  LmidProduct
00441eb4  lMidProduct
00441ec0  LminProduct
00441ecc  lMinProduct
00441fb1  iDAC2MilliAmpsTable
00441fc5  mA2Nits2ndOrderCoef
00441fd9  mA2Nits1stOrderCoef
00441fed  mA2Nits0thOrderCoef
00442001  lMinReachable
0044200f  miniDAC
00442017  midiDAC
0044201f  maxiDAC
00442027  nitsAtMaxCode
0044203b  current-for-max-backlight
00442055  current-for-mid-backlight
00442089  pmu-controller
00442098  smc-enable-key
004420a7  bl-initial-state
004420b8  smcKey
004420bf  dispatch-queue-label
004420d4  lediMax
004420dc  dimmingRatio
004420e9  LmaxReachable
004420f7  LminPWMaximization
0044210a  LminReachable
00442118  DBVMin
0044211f  DBVMax
00442126  panel-gamma
00442132  formula-max-nits
00442143  tap-linear-nits
00442153  lMidPanel
00442168  Display (Event Forward)
00442180  BrightnessUtil
0044218f  UNSERIALIZABLE
004421a3  CBServiceiOSs
004421c9  CBAOPEndpoint
004421d7  genx-request-id
004421e7  genx-sample
004421f3  requestID
004421fd  timestamp
00442207  channelCount
00442214  measurementCount
00442225  luxResidency
00442232  countsBE
0044223b  LExpAvg
004422d1  >GB7ZJB
004422f1  $VBzvWB1
004422fe  ZBkk[B
00442362  jB"NjBV}jB
00442376  kB*:kB_ikB
0044238a  kB2&lBgUlB
004423e5  4pB&dpB[
004423f9   qB.PqBc
0044240e  rBP<rB
00442422  rBX(sB
00442429  WsBdisplayState
00442439  av_min_sample_rate_lpcm
00442451  av_max_sample_rate_lpcm
00442469  av_min_sample_size_lpcm
00442481  av_max_sample_size_lpcm
00442499  av_min_channel_count_lpcm
004424b3  av_max_channel_count_lpcm
004424cd  CPCapabilities
004424dc  DisplayAsleep
004424ea  Time To Light Measurements
00442505  dcpav-controller-epic
0044251b  WakeDisplay
00442527  SleepDisplay
0044254c  dcpav-device-epic
0044255e  av-no-virtual-audio
00442572  EventLog
0044257b  RegisterSets
00442588  ProtectionType
00442597  ProtectionOptions
004425a9  Protection
004425b4  SourceSupport
004425da  AudioProperties
004425ea  VideoProperties
004425fa  HDRStaticMetadata
0044260c  InfoFrames
00442617  CPFailureCount
00442626  DSCCapabilities
0044268c  FRLCapabilities
004426e3  LinkQuality
00442720  AllElements
0044272c  TiledDisplayInfo
0044273d  DisplayAllocation
0044274f  dcpav-service-epic
00442762  Charactor error rate exceeded
00442780  CP failure rate exceeded
00442799  Capabilities changed
004427ae  FRL error rate exceeded
004427c6  FRL capabilities changed
004427df  RotationMin
004427eb  RotationMax
004427f7  RotationIncrement
00442809  BoundsSupport
00442847  Rotation
00442850  ColorDitherRemoval
00442863  VSDBElements
00442885  hdmi-frl-enable
004428ae  FRLSinkRateMax
004428bd  FRLSinkRateDSCMax
004428cf  FRLDFPRateMax
004428dd  Identifier
004428e8  SingleEnclosure
004428f8  BezelInfoPresent
0044291f  ForceSingleTile
00442939  Bottom
0044294b  BezelInfo
00442955  TileSize
0044295e  TileTopology
0044296b  MainUFP
00442973  PeerUFP
0044297b  ExtraPipes
00442986  UseSingleTile
00442a05  LG HDR 4K
00442b2b  ]^_bcd?@/
00442ff9  MaxTMDSClock
0044301b  MaxTMDSClockDivisor
00443044  HasHDMILegacyEDID
00443056  MaxPixelClock
00443064  SupportsBT2020YCC
00443076  SupportsBT2020cYCC
004430a8  MaxFrameAverage
004430b8  Luminance
0044326c  SupportsStandby
0044327c  SupportsSuspend
0044328c  SupportsActiveOff
004432d0  WhitePoints
004432f5  MinimumRefreshRate
00443308  MaximumRefreshRate
00443374  Waiting
0044337c  Measuring
00443386  Monitoring
00443391  Recovery
004433b3  HDCPReauthRequests
004433e0  Physical Address
004433f1  StartInfoFrame
00443400  StopInfoFrame
0044343d  dcpav-video-interface-epic
00443458  PrepareLink
00443464  StartLink
0044346e  DidStartLink
0044347b  UpdateLink
00443486  WillStopLink
00443493  StopLink
0044349c  CompleteLink
004434a9  dcpav-interface
004434b9  AudioElements
004434c7  dcpav-audio-interface-epic
004434e2  IOAVCECInterface
004434f3  dcpav-cec-interface-epic
0044350c  reg-nodebug-0
0044351a  reg-nodebug-1
00443528  reg-redact-0
00443535  reg-redact-1
00443546  HDCP Capable
00443553  Downstream Established
0044356a  Repeater
00443573  StatusVersion
00443581  HDCPTXVersion
0044358f  HDCPTopology
004435a0  Success
004435a8  Unknown Failure
004436d0  ProductName
00443775  ContrastFactorMin
00443787  ContrastFactorMax
004437ce  SupportsPQEOTF
004437dd  SupportsHLGEOTF
004437ed  SupportsBT2020RGB
00443884  device-reset-id
00443894  power-ltr
004438d8  Reserved
004438e1  telemetry-mapping
004438f3  telemetry-indices
0044390b  IsVirtual
00443dcc  ColorModes
00443e22  IsOverscanned
00443e30  IsPreferred
00443e3c  IsPromoted
00443e47  ScanInformation
00443e57  ValidPixelEncodings
00443e6b  TimingType
00443e76  AspectRatio
00443e82  PreciseAspectRatio
00443e95  UpstreamFormat
00443ea4  TimingStandard
00443ee9  HorizontalPipeCount
00443efd  VerticalPipeCount
00443f0f  StandardType
00443f1c  DownstreamFormat
00443f2d  WhitePoint
00443f38  DisplayLuminance
00443f94  MaxChannelCount
00443fa4  StreamSampleRate
00443fd0  ElementData
00443fdc  ActiveChannelCount
00443fef  ChannelLayout
00443ffd  ChannelAllocation
0044400f  dcpav-sac-epic
0044401e  dcpav-power-epic
0044402f  with-panic-handler
00444042  panicb-gpio
0044404e  ignore-remote-power-disp-pmic
0044406c  dcpav-power-interface
0044e070  ProtectLink
0044e07c  ReprotectLink
0044e08a  UnprotectLink
0044e098  RestartInterfaces
0044e0aa  Link Command
0044e0b7  Protection Command
0044e0ca  Link Command (with source)
0044e0e5  Protection Command (with source and AUP data)
0044e113  Set Power
0044e11d  Hot Plug
0044e126  Add Child
0044e130  Remove Child
0044e13d  LinearPCM
0044e169  OneBitAudio
0044e17f  WMAPro
0044e18b  Dolby Atmos (EAC3)
0044e19e  Dolby Atmos (EAC3 7.1)
0044e1b5  Dolby TrueHD (MAT1.0)
0044e1cb  Dolby TrueHD (MAT2.0)
0044e1e1  Dolby Atmos (MAT2.0)
0044e1f6  Dolby TrueHD (MAT2.1)
0044e20c  Dolby Atmos (MAT2.1)
0044e221  Front Left
0044e22c  Front Center
0044e239  Front Right
0044e245  Front Left Center
0044e257  Front Right Center
0044e26a  Rear Left
0044e274  Rear Center
0044e280  Rear Right
0044e28b  Rear Left Center
0044e29c  Rear Right Center
0044e2ae  Low Frequency Effects
0044e2c4  Front Left Wide
0044e2d4  Front Right Wide
0044e2e5  Front Left High
0044e2f5  Front Center High
0044e307  Front Right High
0044e318  Top Center
0044e323  Master
0044e32a  Capture
0044e338  Horizontal
0044e343  Vertical
0044e34c  RGB 4:4:4
0044e356  YCbCr 4:2:0
0044e362  YCbCr 4:2:2
0044e36e  YCbCr 4:4:4
0044e37a  DolbyVision (native)
0044e38f  DolbyVision (HDMI tunneling)
0044e3ac  YCbCr 4:2:2 (DP tunneling)
0044e3c7  YCbCr 4:2:2 (HDMI tunneling)
0044e3e4  DolbyVision LL YCbCr 4:2:2
0044e3ff  DolbyVision LL YCbCr 4:2:2 (DP tunneling)
0044e429  DolbyVision LL YCbCr 4:2:2 (HDMI tunneling)
0044e455  DolbyVision LL YCbCr 4:4:4
0044e470  DolbyVision LL RGB 4:4:4
0044e489  GRGB Tunneled as YCbCr422 (Even line blue)
0044e4b4  GRGB Tunneled as YCbCr422 (Even line red)
0044e4e3  Limited
0044e4eb  Traditional gamma (SDR)
0044e503  Traditional gamma (HDR)
0044e51b  SMPTE ST 2084 (PQ)
0044e52e  BT.2100 HLG
0044e53a  Default RGB
0044e546  SMPTE 170M/BT.601
0044e55f  xvYCC601
0044e568  xvYCC709
0044e571  sYCC601
0044e579  DolbyVision VSVDB
0044e590  AdobeYCC601
0044e59c  AdobeRGB
0044e5a5  BT.2020 (YcCbcCrc)
0044e5b8  BT.2020 (YCbCr)
0044e5c8  BT.2020 (RGB)
0044e5d6  DCI-P3 (D65)
0044e5e3  DCI-P3 (Theater)
0044e5fa  scRGBfixed
0044e605  External
0044e60e  Embedded
0044e623  Upstream
0044e62c  Intermediate
0044e642  Vendor Specific
0044e656  Product Description
0044e674  Dynamic Range & Mastering
0044e692  CVTv1X
0044e699  CVTv2X
0044e6a0  Overscan
0044e6a9  Underscan
0044e6b3  Selectable
0044e6c3  CEAShortID
0044e6e4  Unprotected
0044e6f0  Negotiating
0044e6fc  Protected
0044e72a  48 Gbps (12Gbps/lane * 4 lanes)
0044e74a  40 Gbps (10Gbps/lane * 4 lanes)
0044e76a  32 Gbps (8Gbps/lane * 4 lanes)
0044e789  24 Gbps (6Gbps/lane * 4 lanes)
0044e7a8  18 Gbps (6Gbps/lane * 3 lanes)
0044e7c7  9 Gbps (3Gbps/lane * 3 lanes)
0044e7e5  0 Gbps (FRL disabled)
0044e7fb  ? Gbps (Unknown FRL rate)
0044e815  FRLCurrentRate
0044e824  FRLTargetRate
0044e832  LinkType
0044e83b  LinkTime
0044e844  LinkData
0044e853  PixelEncoding
0044e861  DynamicRange
0044e873  Colorimetry
0044e894  VerticalAttributes
0044e8a7  IsInterlaced
0044e8b4  IsSplit
0044e8bc  LinkID
0044e8c8  IsMirroring
0044e8da  Timing
0044e8e1  VRREnabled
0044e8ec  LLMEnabled
0044e8f7  MergeEnabled
0044e904  DSCBitsPerPixel
0044e914  DSCPassthrough
0044e923  DSCParameters
0044e937  FrontPorch
0044e942  SyncWidth
0044e94c  BackPorch
0044e956  Active
0044e95d  SyncRate
0044e966  PreciseSyncRate
0044e976  SyncPolarity
0044e983  PixelRepetition
0044e993  Version
0044e99b  SupportsVBR
0044e9bf  SupportsRGB
0044e9cb  SupportsYCbCr444
0044e9dc  SupportsYCbCr422
0044e9ed  SupportsYCbCr420
0044ea15  Supports8bpc
0044ea22  Supports10bpc
0044ea30  Supports12bpc
0044ea3e  LineBufferBitDepth
0044ea51  MinBppIncrement
0044ea61  MaxSliceWidth
0044ea6f  SliceCapabilityMask
0044ea83  RateBufferBitCount
0044ea96  PeakThroughputMode0
0044eaaa  PeakThroughputMode1
0044eabe  MaxBpp444
0044eac8  MaxBpp420
0044ead2  Format
0044ead9  ChannelCount
0044eae6  SampleSize
0044eaf1  LinkSampleRate
0044eb00  IOAVInterface
0044eb0e  IOAVVideoInterface
0044eb21  IOAVAudioInterface
0044eb34  IOAVAudioDriver
0044eb44  IOAVCECService
0044eb5f  commandMask
0044eb6b  eventMask
0044eb75  eventCapacity
0044eb83  Device Enumeration
0044eb96  Interface Enumeration
0044ebac  Modes Validation
0044ebbd  Interface Enumeration -> Mode Set
0044edc5  testMode
0044edce  cpTypesMask
0044edda  hdcp.protocolMask
0044edec  CPProtocol
0044edf7  RegisterSetName
0044ee07  RegisterSetData
0044ee17  RegisterSetType
0044ee40  RegisterSetOffset
0044ee52  RegisterCount
0044ee60  RegisterSize
0044ee72  Return
0044ee79  EventRaw
0044ee82  EventClass
0044ee8d  EventTime
0044ee97  EventPayload
0044eea4  Command
0044eeac  CommandStatus
0044eeba  ProtectionStatus
0044eecb  EncryptionStatus
0044eedc  AUPPacket
0044eee6  Reason
0044eeed  PortID
0044eef4  HPDState
0044eefd  HPDSuppressed
0044ef10  Status
0044ef17  CommandReason
0044ef25  ElementType
0044ef31  VendorID
0044ef3e  Payload
0044ef46  EPICName
0044ef4f  EPICUnit
0044ef58  EPICLocation
0044ef65  EPICProviderClass
0044ef77  power-on-sequence
0044ef89  power-off-sequence
0044ef9c  power-rails
0044efa8  offset
0044efb5  vsgpio-scratch-v1px-cmd-valid
0044efd3  vsgpio-scratch-resetb-cmd-valid
0044eff3  vsgpio-scratch-common-string
0044f010  vsgpio-scratch-pmu-status
0044f02a  vsgpio-v1px-on-value
0044f03f  vsgpio-v1px-off-value
0044f055  vsgpio-resetb-low-value
0044f06d  vsgpio-resetb-high-value
0044f086  vsgpio-resetb-gpce-trigger
0044f0a1  vsgpio-v1px-gpce-trigger
0044f0ba  resetb-config
0044f0c8  pp1vx-config
0044f0d5  gpce-trigger-config
0044f0e9  pp1vx-on-to-rst-delay
0044f0ff  rst-off-to-pp1vx-delay
0044f116  pp1vx-off-to-xsync-delay
0044f12f  panel-min-sleep-delay
0044f145  prior-rst-off-delay
0044f159  PanelPowerStatus
0044f170  edp-sac-allow-tap-change
0044f189  cdi-sac-noisewidth
0044f1a0  cdi-sac-enable
0044f1af  edp-sac-exclude-ranges
0044f1c6  cdi-sac-exclude-ranges
0044f1dd  AgileBaseTap
0044f1ea  AgileTap
0044f1f7  sac-enable
0044f202  edp-sac-enable
0044f22b  Supported
0044f235  CurrentIndex
0044f242  PendingIndex
0044f24f  AggressorTable
0044f273  alpm-enable
0044f27f  supports-detailed-panel-id
0044f29a  panic-training-failure-retries
0044f2b9  TCONErrorCount
0044f2c8  dpcd-brightness-base-address
0044f2e5  dpcd-brightness-minimum-value
0044f303  dpcd-brightness-maximum-value
0044f321  dpcd-brightness-big-endian
0044f344  alpdpLinkRate
0044f352  virtual-temp-fmt
0044f363  supports-raw-panel-id
0044f379  dbv-sdp-line-trigger
0044f38e  edpASSRMode
0044f39a  enhancedMode
0044f3a7  downspread
0044f3bd  fecMode
0044f3c5  laneCount
0044f3cf  linkRate
0044f3d8  maxPattern
0044f3e3  laneScrambleSeed
0044f415  encoding
0044f424  colorimetry
0044f435  interlaced
0044f440  axis-0
0044f44d  active
0044f454  syncWidth
0044f45e  backPorch
0044f468  frontPorch
0044f473  syncPolarity
0044f480  pixelRepetition
0044f490  pixelRate
0044f49a  ratioType
0044f4a4  scanInformation
0044f4b4  ecid_uuid
0044f4be  tps1-ml-to-aux-delay-us
0044f4e6  TrainLink
0044f4f0  Link Training Command
0044f525  Symbol Error Rate Measurement Pattern
0044f551  80-bit custom pattern
0044f567  CP2520 Pattern 1
0044f578  CP2520 Pattern 2
0044f589  CP2520 Pattern 3
0044f59f  Source
0044f5a6  VoltageSwing
0044f5b3  PreEmphasis
0044f5c4  EnhancedMode
0044f5d1  Downspread
0044f5dc  LaneCount
0044f5e6  LinkRate
0044f5ef  DriveSettings
0044f61c  IODPController
0044f62b  LaneMapping
0044f637  MinLaneCount
0044f644  MinLinkRate
0044f650  MinLinkRateScalar
0044f662  MaxLinkRateScalar
0044f674  ScramblingInhibited
0044f688  dcpdp-controller-epic
0044f6ad  pHDMIg
0044f6b8  $SYNAa
0044f744  dcpdp-device-epic
0044f78e  Revision
0044f797  SupportsALPM
0044f7a4  SupportsASSR
0044f7b1  SupportsDSC
0044f7bd  SupportsFEC
0044f7c9  SupportsPSR
0044f7f9  MaxLinkRate
0044f831  SupportsDownspread
0044f863  DownstreamPortCount
0044f877  DownstreamPortTypes
0044f88b  Updated
0044f893  IOAVDevice
0044f89e  IODPDevice
0044f8a9  ALPMEnabled
0044f8f3  SupportsPanelReplay
0044f91f  FECEnabled
0044f92a  DSCEnabled
0044f958  ASSREnabled
0044f964  UpdateMode
0044f974  Training
0044f97d  DFPPortCount
0044fa49  DFPMaxClockRate
0044fa59  DFPMaxColorDepth
0044fa91  IOAVService
0044fa9d  IODPService
0044faa9  dcpdp-service-epic
0044fabc  SinkIEEEOUI
0044fac8  BranchIEEEOUI
0044fad6  BranchDeviceID
0044fae5  ChipRevision
0044faf2  FirmwareRevision
0044fb03  SinkCount
0044fb0d  SymbolErrorCounts
0044fb1f  CRIterations
0044fb2c  EQIterations
0044fb51  FECErrorCounts
0044fb60  SupportsSDPSplit
0044fba7  BitErrorCounts
0044fc04  hdmi_cec_enabled
0044fcfc  TunnelBWA
0044fd0c  Granularity
0044fd18  AllocatedBandwidth
0044fd57  MaxR8b10bLinkRate
0044fd69  MaxLaneCount
0044fd7a  LinkCountTotal
0044fd89  LinkCountRemaining
0044fda5  MsgEnabled
0044fdbb  IsMSTBranch
0044fdc7  IsActiveSink
0044fdd4  FecCap
0044fddb  FullPBN
0044fde3  AvailablePBN
0044fdf0  NoConnect
0044fdfe  Branch
0044fe09  LegacyConverter
0044fe19  WirelessConverter
0044fe2b  WirelessUFP
0044fe3f  Ranges
0044fe46  Aggressor
0044fe50  NoiseWidth
0044fe66  LinkRateScalar
0044fe75  MSTPorts
0044fe7e  Attribute
0044fe88  Resource
0044fe91  Address
0044febf  RetrainLink
0044fecb  SetPower
0044fed4  coverglass-serial-number-key
0044fef1  color-accuracy-index-key
0044ff1f  IOAVController
0044ff9f  VirtualDevice
004502ca  Encrypted
004502d4  sinkScramblingState
00450301  PLLBandwidth
0045030e  DataSlewRate
0045031b  ClockSlewRate
00450329  DataSwing
00450333  ClockSwing
0045033e  Data0Preemph
0045034b  Data1Preemph
00450358  Data2Preemph
00450365  ClockPreemph
00450372  DisableAllTerm
00450381  DisableClkTerm
00450390  DataHighImp
0045039c  ClockHighImp
004503a9  FilterThresh
004503b6  FilterFraction
004503da  Unknown
0045041c  dcpav-audio-arc-epic
00450431  dcpav-arc-ep
0045043e  FFECtrlLane
0045044a  SelectTerm
00450455  DPRXEQ
0045045f  cHDMIb
00452dac  vid-clk-freq
00452db9  vid-ref-source
00452dc8  vid-clk-div
00452dd4  vid-flags
00452dde  vid-clk-pll-freq
00452def  vid-clk-pll-fbdiv
00452e01  vid-clk-pll-prediv
00452e14  vid-clk-pll-opdiv
00452e26  vid-clk-pll-sparediv
00452e3b  vid-clk-pll-cpiset
00452e4e  vid-clk-pll-lfrset
00452e61  vid-clk-pll-fcw_num
00452e75  vid-clk-pll-fcw_denom
00452e8b  vid-clk-pll-fb_divn_half
00452ea4  vid-clk-pll-divisor
00452eb8  vid-clk-config
00452ec7  pipe-idx
00452ed7  personalities
00452f70  trusted-compartment
00452f84  secure-mipi
00452f90  property-overrides
00452fa3  panel-overrides
00452fb3  target-require-secure-dcp-comms
00452fd3  total-pgtable-count
00452fe7  frameish-count
00452ff6  cap-slot-count
00453005  page-table-stats
00453016  DispTarget
00453021  BoardID
00453029  BoardRev
00453032  ChipID
00453039  ChipRev
00453041  DisplayModuleID
00453051  Location
0045305f  DCPPlatform
0045306b  SkipLoadStages
0045307a  driver-personalities
0045308f  property-personalities
004530a6  axis-1
004530ad  syncRate
004530b6  derivedSyncRate
004530c6  vid-link-data
004530d4  timing
004530db  panel-vendor-id
004530eb  panel-build-id
004530fa  panel-program-id
0045310b  panel-device-id
0045311b  panel-variant-id
0045312c  panel-touch-id
0045313b  agile-clocking-data
0045314f  display-eeprom-compensation
0045316b  SinkDeviceID
00453178  detailed-panel-id
0045318a  DCPRole
00453192  DCPPort
0045319a  DCPLocation
004531a6  DisplayTargets
004531b5  DispTargetNone
004531da  support-audio-earc
004531ed  support-retention-default
00453207  require-sleep-mode-retention
00453224  nap-threshold
00453232  support-power-manage
00453247  s2r-threshold
00453255  pg-threshold
00453262  prevent-dcpext-nap
00453275  dcp-state-change-cnt
0045328a  nap-prevent-cnt
0045329a  diagnostics
004532a6  support-pagetable-stats
004532c2  TMDS_LOW
004532cb  TMDS_HIGH
004532d5  TMDS_MID
004532de  tcon-device-id
004532ed  dp-link-data
004532fa  driveSettings-dev
0045330c  driveSettings
0045331a  margin
00453329  retry-code
00453334  retry-count
00453340  retry-interval-ms
00453368  endpoint-name
00453376  test-ep
0045337e  mcw-clientid
0045338b  psdSrvcIds
00453396  psdAliasNums
004533a3  psdDbIrqs
004533cf  ?create-workloop
004533e0  use-workloop-thread
004533f4  SessionStart
00453428  matched
00453436  category
0045343f  endpoint
00453448  ep-if-properties
00453459  ep-if-class-props
0045346b  interface-id
00453478  interface-remote
00453489  interface-name
00453498  interface-entitlements
004534af  interface-reregister
004534c4  ep-has-desc-mgr
004534d4  epi-is-desc-mgr
004534e4  cmd-oob-threshold
004534f6  rsp-oob-threshold
00453508  ensure-delivery
00453518  default
00453520  ep-connected
0045352d  remote-open
00453539  endpoint-wl
00453545  epif-wl
0045354d  max-command-count
0045355f  interface-match
0045356f  <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0">
00453613  </plist>
00453620  shallow
004537e8  regPowerEnable
004537f7  properties
00453811  retain
00453818  children
00453821  clients
00453829  config
00453830  @(#)PROGRAM:AppleFirmwareKit  PROJECT:AppleFirmwareKit-743.40.4
0045389e  priority
004538a7  stacksize
004538b1  stackguard
004538e0  pmgr-dev-id
00453940  It took me all my life to learn how to salt a tomato. --Eric Ripert
004540d4  enable
00454bd1  CEA-861:Type1
00454c70  Global
00454c77  average-refresh-rate
00454c8c  layer0
00454c93  layer1
00454c9a  layer2
00454ca1  layer3
00454ca8  Current Display
00454cb8  Pending Swap
00454cc5  Swap Queue
00454cd0  Temp Queue
00454cdb  Last Swap Layers Array
00454cf2  Last Swaps Array
00454d03  Last Swaps Dictionary
00454d19  IOMFB power info
00454d30  DCPIndex
0045513e  u=raw-panel-serial-number
00455158  luminance-ratio
00455168  first-frame-response
0045517d  first-frame-response-high
00455197  llc-red
0045519f  llc-green
004551a9  llc-blue
004551b2  ptuc-red
004551bb  ptuc-green
004551c6  ptuc-blue
004551d0  ptuc-rsvd
004551da  lMinPanel
004551e4  lMaxPanel
004551ee  lMaxReachable
004553a1  PILFDOA
004553a9  YALDDOA
004553b1  NACSDOA
004553ba  BMADOA
004553c2  CRPDOA
004553ca  CDPDOA
004553d2  MLLDOA
004553d9  SLPADOA
004553e1  CLPADOA
004553e9  TCTFDOA
004553f1  MSTFDOA
004553f9  NMTFDOA
00455401  XMTFDOA
00455409  EBTFDOA
00455411  HENODOA
00455419  SSIMDOA
00455421  ACIBDOA
0045542a  CABDOA
00455432  CCBDOA
00455439  CAPBDOA
00455441  CCPBDOA
00455449  BCMSDOA
00455451  UFMSDOA
0045650c  TimingElements
0045651b  ColorElements
00456552  ProductID
0045655c  ManufacturerID
0045656b  SerialNumber
00456578  WeekOfManufacture
0045658a  YearOfManufacture
0045659c  ModelYear
004565a6  IOMFB backlight info
004565bb  Downstream
004565c6  export_uuid
00456624  DisplayAttributes
00456636  ProductAttributes
00456648  Transport
00456652  EDID UUID
0045665c  DisplayContainerID
0045669d  Chromaticity
004566aa  DefaultWhitePoint
00456c6b  HMF1F"F
00457bb3  hJhaHDh
0045830b  hhP!}`
0045831d  QhPa} x
0045832f  QhP1|pz
004583c3  ! nhPC
004583cb  !`nhPC
004583e3  A ohPC
004583eb  A`ohPC
004592e6  iHiIM"
00459356  MHNIF"
00459388  #)/5;AGMS
004595b7  u\jDQE
00459cff  T(XjXB
00459daf  T(XjXB
0045a9bc  ,L%hNo
0045ab7f  aEh,CD`
0045ac46  3H0MAh!
0045ac80  !`.`ahA
0045ac95  Q)`ahA
0045adef   hc.HAh!
0045ae6b  hCh@iB
0045af70  XIYJYLZKZN
0045b64b  hShRi@
0045c00c  pGpGpGpG
0045c024  0XhLhI
0045c54e  5a#n1hbnph
0045c8af  hLhIiC
0045cec6  lXX{X~XXXXXuXXXXr
0045d4cd  ppGkXU
0045d67c  command_mode_mcpu.c
0045d690  command_mode_all_piodma_done
0045d6ad  isr_nclk
0045d6b6  Internal state error
0045d6cc  isr_pcc_stable
0045d6dc  process_vbi
0045d6e8  command_mode_adisp.c
0045d6fd  tsq_control
0045d709  command_mode_replay_request_is_not_allowed
0045d734  single_pipe_start_frm_state_machines
0045d759  command_mode_apt.c
0045d76c  apt_control
0045d778  isr_writeback_handler: BIS WB FAIL
0045d79c    BIS WB fail and exceed retry
0045d7bc  bics_v2.c
0045d7c6  ferr_BicsFErr_RdDecompressError
0045d7e6  bis_setup_stripe
0045d7f7  cdi_v3.c
0045d800  isr_cdidone
0045d80c  cdi_prepare_cmd
0045d81c  cdi_control
0045d828  cdi_irq_FifoOverflow
0045d83d  cdi_irq_RunAtVbi
0045d84e  cdi_irq_AxiErr
0045d85d  cdi_irq_SfWrErr
0045d86d  cdi_irq_Type0RunAtType1BarrierT
0045d88d  cdi_irq_Type1RunAtEndT
0045d8a4  get_cmd_table_with_tag
0045d8bb  cdi_table_mark_done
0045d8cf  set_cmd_completed_state
0045d8e7  cdi_configure_table
0045d8fb  debug_helper.c
0045d90a  debug_helper_stop_clock
0045d922  ferror_handlers.c
0045d934  isr_SecurityStat
0045d945  ferr_AxiWrErr
0045d953  ferr_AxiRdErr
0045d961  ferr_SfOverflow
0045d971  ferr_GP_DecompressFail
0045d988  ferr_Underrun
0045d996  M3 adisp SPDS version expecting %x, found %x
0045d9c4  dmem SPDS version expecting %x, found %x
0045d9ee  command_mode_main_init.c
0045da07  main_init
0045da11  command_mode_mode_change.c
0045da2c  isr_mode_change_req
0045da40  M3 New Mode: Normal
0045da55  ../common/mxwrap_msgbox_mprintf.c
0045da77  m3_message
0045da82  ../common/mprintf_shared.h
0045da9d  m3_log_text
0045daa9  m3_vsnprintf
0045dab6  isr_inbox0_not_empty
0045dacb  pdc_v22.c
0045dad5  pdc_cdi_configure_area
0045daec  pdc_rw_dma_early_stop
0045db02  pdc_ext_wb_buffer_overflow
0045db1d  pdc_int_wb_buffer_overflow
0045db38  pdc_wr_dma_fail
0045db48  pdc_rd_dma_fail
0045db58  pdc_rd_decompress_error
0045db70  state_machine_cmd
0045db82  piodma_tagging.c
0045db93  isr_apiodma
0045db9f  piodma_check_idle
0045dbb1  apiodma_irq_ParseErr
0045dbc6  apiodma_irq_SeqPushErr
0045dbdd  apiodma_irq_AxiErr
0045dbf0  apiodma_irq_AddrBoundsErr
0045dc0a  piodma_irq_command_tag_completed_mismatch
0045dc34  piodma_transaction_not_completed_tsq
0045dc59  piodma_transaction_not_completed_prc0
0045dc7f  piodma_transaction_not_completed_prc1
0045dca5  piodma_transaction_not_completed_pdclut
0045dccd  piodma_transaction_not_completed_hgod
0045dcf3  piodma_transaction_not_completed_pcc2dluslut
0045dd20  piodma_transaction_not_completed_proxlut
0045dd49  piodma_transaction_not_completed_spuc_map
0045dd73  piodma_transaction_not_completed_alsslut
0045dd9c  piodma_transaction_not_completed_acsslut
0045ddc5  piodma_transaction_not_completed_ptuclut
0045ddee  debug_logging_update_piodma_done
0045de0f  piodma_control_tagging.c
0045de28  piodma_control
0045de37  pixel_capture_info2.c
0045de4d  pixel_capture_frame_info
0045de66  profiler.c
0045de71  fw_budget_check
0045de81  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
0045debd  disp_perf_state.c
0045decf  error_rt_bwr_exceed_max_perf_state
0045def2  Control M3: update_disp_perf_state_hw %d -> %d
0045df22  rtplc.c
0045df2a  interp1_rescalehist
0045df3e  rtplc_write_globalenable
0045df57  rtplc_setup
0045df63  rtplc_update_tsq_info
0045df79  rtplc_process_stats
0045df8d  isr_rtplc_global_failsafe_trig
0045dfac  rtplc_read_fd_histogram
0045dfc4  rtplc_current_limit_global_scaling
0045dfe7  rtplc_calc_rt_luts
0045dffa  swmpr_v1.c
0045e005  swmpr_mode_change
0045e017  isr_swmpr
0045e021  swmpr_refresh_rate.c
0045e036  swmpr_refresh_rate_update
0045e050  timebase.c
0045e05b  read_timebase
0045e079  Unsupported: '%c'
0045e08b  0123456789ABCDEF
0045e09c  0123456789abcdef
0045ea1e  Jhg(g0D
0045f330  `iJShC
0045fb28  hpP!}`
0045fbca  QpP)|hz
0045fc00  QhnpPO
00460159  aHDi@F
00460d72  iDiDj"
00461a44  #)/5;AGM
00461bda  u\jDQE
00462881  le4YuY
00463094  T0XrXB
0046313c  T0XrXB
00464b4c  aEh,CD`
00464bf0  hUhRiKN
00464c72  A)`ahA
00464c8e  Q)`ahA
00464e93  tP]FTF
00464f10  hCh@iB
00465692  hShRi@
004658ab  @DBDDD
004666b6  eqf`m!o
00466e45  pGpGpGpGpGpG
0046717a  atDUhO
004672bb  lXX{X~XXXXXuXXXXr
0046798e  A)PpG)X!
00467998  A)PpGPC@
004679af  5Y4YpGAh!
004679cd  pGmcpu.c
004679d6  read_dmem_m3control
004679ea  configure_frame0_0_irq
00467a01  configure_subframe0_0_irq
00467a1b  configure_subframe0_3_irq
00467a35  isr_vftg_subframe0_0
00467a4a  isr_pcc_stable
00467a5a  adisp.c
00467a62  tsq_control
00467a6e  single_pipe_start_frm_state_machines
00467a99  calc_vbi_position_lines
00467ab1  apt_init
00467aba  apt_vbi
00467ac2  apt_control
00467ace  apt_activate
00467adb  adaptive_sync.c
00467aeb  adaptive_sync_control
00467b01  adaptive_sync_determine_min_max_duration
00467b2a  qms_tsq
00467b32  adaptive_sync_activate
00467b49  qms_vftg_update
00467b59  bics_stub.c
00467b65  isr_bis_handler
00467b75  isr_BicsFErr_RdDecompressError
00467b99  ca_discharge
00467ba6  ca_active
00467bb0  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00467c01  cdi_v3.c
00467c0a  isr_cdidone
00467c16  cdi_check_idle
00467c25  cdi_prepare_cmd
00467c35  cdi_control
00467c41  cdi_irq_FifoOverflow
00467c56  cdi_irq_RunAtVbi
00467c67  cdi_irq_AxiErr
00467c76  cdi_irq_SfWrErr
00467c86  cdi_irq_Type0RunAtType1BarrierT
00467ca6  cdi_irq_Type1RunAtEndT
00467cbd  get_cmd_table_with_tag
00467cd4  cdi_table_mark_done
00467ce8  set_cmd_completed_state
00467d00  cdi_configure_table
00467d14  debug_helper.c
00467d23  debug_helper_stop_clock
00467d3b  fast_update_legacy.c
00467d50  fast_layer_update_regs
00467d67  ferror_handlers.c
00467d79  isr_SecurityStat
00467d8a  ferr_AxiWrErr
00467d98  ferr_AxiRdErr
00467da6  ferr_SfOverflow
00467db6  ferr_Replay_DecompressFail
00467dd1  ferr_GP_DecompressFail
00467de8  ferr_ReplayReadback_Underrun
00467e05  ferr_Underrun
00467e13  follower_mode_v3.c
00467e26  follower_mode_trigger
00467e3c  LFC: dmem w 0x%x
00467e4e  LFC: A->R 
00467e5a  LFC: 8.3 ms repeat. Rem %u 
00467e7d  lfc_control
00467e89  LFC: R->R 
00467e95  LFC: Clear Pending from swid %u 
00467eb7  LFC: rem_sfm %u nr %u
00467ece  LFC: status %d 
00467edf  LFC: Reset states 
00467ef3  M3 adisp SPDS version expecting %x, found %x
00467f21  dmem SPDS version expecting %x, found %x
00467f4b  video_mode_main_init.c
00467f62  main_init
00467f6c  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00467fb8  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00468006  M3 vbi_pulse %u, vbi_offset %d (initial %d)
00468032  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00468076  Control M3 error: Must have one subframe for external panels
004680b4  mode_change_v2.c
004680c5  isr_mode_change_req
004680d9  M3 New Mode: %s
004680ef  Normal
004680f6  WARNING; TSQ entry at normal to auto mode change. Replay=%d
00468132  sideband_can_mode_switch
0046814b  ../common/mxwrap_msgbox_mprintf.c
0046816d  m3_message
00468178  ../common/mprintf_shared.h
00468193  m3_log_text
0046819f  m3_vsnprintf
004681ac  isr_inbox0_not_empty
004681c1  pdc_v22.c
004681cb  pdc_cdi_configure_area
004681e2  pdc_rw_dma_early_stop
004681f8  pdc_ext_wb_buffer_overflow
00468213  pdc_int_wb_buffer_overflow
0046822e  pdc_wr_dma_fail
0046823e  pdc_rd_dma_fail
0046824e  pdc_rd_decompress_error
00468266  pdc_control_vid
00468276  piodma_tagging.c
00468287  isr_apiodma
00468293  piodma_check_idle
004682a5  apiodma_irq_ParseErr
004682ba  apiodma_irq_SeqPushErr
004682d1  apiodma_irq_AxiErr
004682e4  apiodma_irq_AddrBoundsErr
004682fe  piodma_irq_command_tag_completed_mismatch
00468328  piodma_transaction_not_completed_tsq
0046834d  piodma_transaction_not_completed_prc0
00468373  piodma_transaction_not_completed_prc1
00468399  piodma_transaction_not_completed_pdclut
004683c1  piodma_transaction_not_completed_hgod
004683e7  piodma_transaction_not_completed_pcc2dluslut
00468414  piodma_transaction_not_completed_proxlut
0046843d  piodma_transaction_not_completed_spuc_map
00468467  piodma_transaction_not_completed_alsslut
00468490  piodma_transaction_not_completed_acsslut
004684b9  piodma_transaction_not_completed_ptuclut
004684e2  debug_logging_update_piodma_done
00468503  piodma_control_tagging.c
0046851c  piodma_control
0046852b  pixel_capture_info2.c
00468541  pixel_capture_frame_info
0046855a  prc_v4.c
00468563  prc_active
00468574  rca_trigger_check
00468586  rca_vbi_check
00468594  isr_rca_main
004685a1  isr_rca_error_handler
004685b7  configure_rca_dpg_subframe0_1_irq
004685d9  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00468615  disp_perf_state.c
00468627  error_rt_bwr_exceed_max_perf_state
0046864a  Control M3: update_disp_perf_state_hw %d -> %d
0046867a  dptx_multi_sdp.c
0046868b  dptx_sdp_init
00468699  timebase.c
004686a4  read_timebase
004686c2  Unsupported: '%c'
004686d4  0123456789ABCDEF
004686e5  0123456789abcdef
00468ef0  8p4ctc
00469070  PtPaPdE
0046923f  QQXRF!
0046a586  "Q(XiX
0046a6f5  `(IjPS
0046a808  # NFXb
0046b4d9  QpP)|hz
0046b517  QhnpPO
0046d4d8  dBc@b@
0046d8c9  h%mfmA
0046dbb1  #)/5;AGP
0046dd63  u\jDQE
0046e297  hBh@iE
0046fd59  T(XjXB
0046fe09  T(XjXB
004706c5  aEh,CD`
00470769  hKhIiRN
00470a10  tP]FTF
00470b03  hCh@iB
004714cf  hShRi@
004716e8  @DBDDD
0047293b  p`DHDJ
00472a54  dqPPpG
00472f1a  0XWMWL
004735c8  EFpf0~
004739c1  hLhIiC
00473cc8  vBs@r@
00474121  X D"D@hRh
004742b2  @hHAX`
00474988  lXX{X~XXXXXuXXXXr
00474f85  A!PpG(XiX
00475005  0pGkXU
0047506b  ApGPC@
0047510c  pGmcpu.c
00475115  read_dmem_m3control
00475129  configure_frame0_0_irq
00475140  configure_subframe0_0_irq
0047515a  configure_subframe0_3_irq
00475174  isr_vftg_subframe0_0
00475189  isr_pcc_stable
00475199  adisp.c
004751a1  tsq_control
004751ad  start_frm_active
004751be  single_pipe_start_frm_state_machines
004751e9  calc_vbi_position_lines
00475201  apt_init
0047520a  apt_vbi
00475212  apt_control
0047521e  apt_activate
0047522b  isr_writeback_handler: BIS WB FAIL
0047524f    BIS WB fail and exceed retry
0047526f  bics_v2.c
00475279  ferr_BicsFErr_RdDecompressError
00475299  bis_setup_stripe
004752af  ca_discharge
004752bc  ca_active
004752c6  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00475317  cdi_v3.c
00475320  isr_cdidone
0047532c  cdi_check_idle
0047533b  cdi_prepare_cmd
0047534b  cdi_control
00475357  cdi_irq_FifoOverflow
0047536c  cdi_irq_RunAtVbi
0047537d  cdi_irq_AxiErr
0047538c  cdi_irq_SfWrErr
0047539c  cdi_irq_Type0RunAtType1BarrierT
004753bc  cdi_irq_Type1RunAtEndT
004753d3  get_cmd_table_with_tag
004753ea  cdi_table_mark_done
004753fe  set_cmd_completed_state
00475416  cdi_configure_table
0047542a  debug_helper.c
00475439  debug_helper_stop_clock
00475451  ferror_handlers.c
00475463  isr_SecurityStat
00475474  ferr_AxiWrErr
00475482  ferr_AxiRdErr
00475490  ferr_SfOverflow
004754a0  ferr_Replay_DecompressFail
004754bb  ferr_GP_DecompressFail
004754d2  ferr_ReplayReadback_Underrun
004754ef  ferr_Underrun
004754fd  M3 adisp SPDS version expecting %x, found %x
0047552b  dmem SPDS version expecting %x, found %x
00475555  video_mode_main_init.c
0047556c  main_init
00475576  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
004755c2  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
00475610  M3 vbi_pulse %u, vbi_offset %d (initial %d)
0047563c  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00475680  Control M3 error: Must have one subframe for external panels
004756be  mode_change_v2.c
004756cf  isr_mode_change_req
004756e3  M3 New Mode: %s
004756f9  Normal
00475700  WARNING; TSQ entry at normal to auto mode change. Replay=%d
0047573c  sideband_can_mode_switch
00475755  ../common/mxwrap_msgbox_mprintf.c
00475777  m3_message
00475782  ../common/mprintf_shared.h
0047579d  m3_log_text
004757a9  m3_vsnprintf
004757b6  isr_inbox0_not_empty
004757cb  pdc_v22.c
004757d5  pdc_cdi_configure_area
004757ec  pdc_rw_dma_early_stop
00475802  pdc_ext_wb_buffer_overflow
0047581d  pdc_int_wb_buffer_overflow
00475838  pdc_wr_dma_fail
00475848  pdc_rd_dma_fail
00475858  pdc_rd_decompress_error
00475870  pdc_control_vid
00475880  piodma_tagging.c
00475891  isr_apiodma
0047589d  piodma_check_idle
004758af  apiodma_irq_ParseErr
004758c4  apiodma_irq_SeqPushErr
004758db  apiodma_irq_AxiErr
004758ee  apiodma_irq_AddrBoundsErr
00475908  piodma_irq_command_tag_completed_mismatch
00475932  piodma_transaction_not_completed_tsq
00475957  piodma_transaction_not_completed_prc0
0047597d  piodma_transaction_not_completed_prc1
004759a3  piodma_transaction_not_completed_pdclut
004759cb  piodma_transaction_not_completed_hgod
004759f1  piodma_transaction_not_completed_pcc2dluslut
00475a1e  piodma_transaction_not_completed_proxlut
00475a47  piodma_transaction_not_completed_spuc_map
00475a71  piodma_transaction_not_completed_alsslut
00475a9a  piodma_transaction_not_completed_acsslut
00475ac3  piodma_transaction_not_completed_ptuclut
00475aec  debug_logging_update_piodma_done
00475b0d  piodma_control_tagging.c
00475b26  piodma_control
00475b35  pixel_capture_info2.c
00475b4b  pixel_capture_frame_info
00475b64  prc_v4.c
00475b6d  prc_active
00475b78  profiler.c
00475b83  fw_budget_check
00475b93  prox.c
00475b9a  prox_active
00475ba6  proxlut_piodma_context
00475bbd  prox_aod_shutdown
00475bcf  prox_aod_startup
00475be0  prox_sws_init
00475bee  prox_sws_stats_ready
00475c03  div_fx
00475c0a  find_coex_curve_zeros
00475c20  prox_process
00475c2d  find_prox_fire_time_rr
00475c44  ProxB: bailed trigger 0x%x > %d * 0x%x + 0x%x - 0x%x [%d-%d %d]
00475c85  prox_config_trigger
00475c9f  rca_trigger_check
00475cb1  rca_vbi_check
00475cbf  isr_rca_main
00475ccc  isr_rca_error_handler
00475ce2  configure_rca_dpg_subframe0_1_irq
00475d04  rt_bandwidth_perf_state.c
00475d1e  rt_bw_check_aod_bw_limit
00475d37  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00475d73  disp_perf_state.c
00475d85  error_rt_bwr_exceed_max_perf_state
00475da8  Control M3: update_disp_perf_state_hw %d -> %d
00475dd8  rtplc_v3.c
00475de3  interp1_rescalehist
00475df7  rtplc_write_globalenable
00475e10  rtplc_setup
00475e1c  rtplc_update_tsq_info
00475e32  rtplc_process_stats
00475e46  isr_rtplc_global_failsafe_trig
00475e65  rtplc_read_fd_histogram
00475e7d  rtplc_rescale_histogram
00475e95  rtplc_calc_rt_luts
00475ea8  dptx_multi_sdp.c
00475eb9  dptx_sdp_init
00475ec7  vmaod_replay.c
00475ed6  vmaod_replay_init
00475ee8  replay_vmaod_wb_completed
00475f02  timebase.c
00475f0d  read_timebase
00475f2b  Unsupported: '%c'
00475f3d  0123456789ABCDEF
00475f4e  0123456789abcdef
00476d2e  aPaXdE
00476ef6  QQXBF!
00478059  "Q(XiX
004781c2  `5IZPo
0047aacd  dBc@b@
0047aeba  h%mfmA
0047b1a6  #)/5;AGR
0047b358  u\jDQE
0047ce7a  B+F(XiX
0047cfb8  B+F(XiX
0047d302  T(XjXB
0047d3b2  T(XjXB
0047dc6e  aEh,CD`
0047dd12  hKhIiRN
0047dfb7  tP]FTF
0047e07e  hCh@iB
0047ea48  hShRi@
0047ec61  @DBDDD
0047f9bf  0XWMWL
0048006d  EFpf0~
00480466  hLhIiC
0048076d  vBs@r@
00480bc6  X D"D@hRh
00480d5f  @hHAX`
00481435  lXX{X~XXXXXuXXXXr
00481aaf  pG(XiX
00481bc6  A)PpGAh!
00481bf3  pGmcpu.c
00481bfc  read_dmem_m3control
00481c10  configure_frame0_0_irq
00481c27  configure_subframe0_0_irq
00481c41  configure_subframe0_3_irq
00481c5b  isr_vftg_subframe0_0
00481c70  isr_pcc_stable
00481c80  adisp.c
00481c88  tsq_control
00481c94  start_frm_active
00481ca5  single_pipe_start_frm_state_machines
00481cd0  calc_vbi_position_lines
00481ce8  apt_init
00481cf1  apt_vbi
00481cf9  apt_control
00481d05  apt_activate
00481d12  isr_writeback_handler: BIS WB FAIL
00481d36    BIS WB fail and exceed retry
00481d56  bics_v2.c
00481d60  ferr_BicsFErr_RdDecompressError
00481d80  bis_setup_stripe
00481d96  ca_discharge
00481da3  ca_active
00481dad  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
00481dfe  cdi_v3.c
00481e07  isr_cdidone
00481e13  cdi_check_idle
00481e22  cdi_prepare_cmd
00481e32  cdi_control
00481e3e  cdi_irq_FifoOverflow
00481e53  cdi_irq_RunAtVbi
00481e64  cdi_irq_AxiErr
00481e73  cdi_irq_SfWrErr
00481e83  cdi_irq_Type0RunAtType1BarrierT
00481ea3  cdi_irq_Type1RunAtEndT
00481eba  get_cmd_table_with_tag
00481ed1  cdi_table_mark_done
00481ee5  set_cmd_completed_state
00481efd  cdi_configure_table
00481f11  debug_helper.c
00481f20  debug_helper_stop_clock
00481f38  ferror_handlers.c
00481f4a  isr_SecurityStat
00481f5b  ferr_AxiWrErr
00481f69  ferr_AxiRdErr
00481f77  ferr_SfOverflow
00481f87  ferr_Replay_DecompressFail
00481fa2  ferr_GP_DecompressFail
00481fb9  ferr_ReplayReadback_Underrun
00481fd6  ferr_Underrun
00481fe4  M3 adisp SPDS version expecting %x, found %x
00482012  dmem SPDS version expecting %x, found %x
0048203c  video_mode_main_init.c
00482053  main_init
0048205d  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
004820a9  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
004820f7  M3 vbi_pulse %u, vbi_offset %d (initial %d)
00482123  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00482167  Control M3 error: Must have one subframe for external panels
004821a5  mode_change_v2.c
004821b6  isr_mode_change_req
004821ca  M3 New Mode: %s
004821e0  Normal
004821e7  WARNING; TSQ entry at normal to auto mode change. Replay=%d
00482223  sideband_can_mode_switch
0048223c  ../common/mxwrap_msgbox_mprintf.c
0048225e  m3_message
00482269  ../common/mprintf_shared.h
00482284  m3_log_text
00482290  m3_vsnprintf
0048229d  isr_inbox0_not_empty
004822b2  pdc_v22.c
004822bc  pdc_cdi_configure_area
004822d3  pdc_rw_dma_early_stop
004822e9  pdc_ext_wb_buffer_overflow
00482304  pdc_int_wb_buffer_overflow
0048231f  pdc_wr_dma_fail
0048232f  pdc_rd_dma_fail
0048233f  pdc_rd_decompress_error
00482357  pdc_control_vid
00482367  piodma_tagging.c
00482378  isr_apiodma
00482384  piodma_check_idle
00482396  apiodma_irq_ParseErr
004823ab  apiodma_irq_SeqPushErr
004823c2  apiodma_irq_AxiErr
004823d5  apiodma_irq_AddrBoundsErr
004823ef  piodma_irq_command_tag_completed_mismatch
00482419  piodma_transaction_not_completed_tsq
0048243e  piodma_transaction_not_completed_prc0
00482464  piodma_transaction_not_completed_prc1
0048248a  piodma_transaction_not_completed_pdclut
004824b2  piodma_transaction_not_completed_hgod
004824d8  piodma_transaction_not_completed_pcc2dluslut
00482505  piodma_transaction_not_completed_proxlut
0048252e  piodma_transaction_not_completed_spuc_map
00482558  piodma_transaction_not_completed_alsslut
00482581  piodma_transaction_not_completed_acsslut
004825aa  piodma_transaction_not_completed_ptuclut
004825d3  debug_logging_update_piodma_done
004825f4  piodma_control_tagging.c
0048260d  piodma_control
0048261c  pixel_capture_info2.c
00482632  pixel_capture_frame_info
0048264b  prc_v4.c
00482654  prc_active
0048265f  profiler.c
0048266a  fw_budget_check
00482680  rca_trigger_check
00482692  rca_vbi_check
004826a0  isr_rca_main
004826ad  isr_rca_error_handler
004826c3  configure_rca_dpg_subframe0_1_irq
004826e5  rt_bandwidth_perf_state.c
004826ff  rt_bw_check_aod_bw_limit
00482718  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00482754  disp_perf_state.c
00482766  error_rt_bwr_exceed_max_perf_state
00482789  Control M3: update_disp_perf_state_hw %d -> %d
004827b9  rtplc_v3.c
004827c4  interp1_rescalehist
004827d8  rtplc_write_globalenable
004827f1  rtplc_setup
004827fd  rtplc_update_tsq_info
00482813  rtplc_process_stats
00482827  isr_rtplc_global_failsafe_trig
00482846  rtplc_read_fd_histogram
0048285e  rtplc_rescale_histogram
00482876  rtplc_calc_rt_luts
00482889  dptx_multi_sdp.c
0048289a  dptx_sdp_init
004828a8  vmaod_replay.c
004828b7  vmaod_replay_init
004828c9  replay_vmaod_wb_completed
004828e3  timebase.c
004828ee  read_timebase
0048290c  Unsupported: '%c'
0048291e  0123456789ABCDEF
0048292f  0123456789abcdef
004838a5  Jhg(g0D
004841b7  `iJShC
00484482  t"pjSx
004849ab  hpP!}`
00484a4d  QpP)|hz
00484a83  QhnpPO
00484fc2  aHDi@F
00485bd9  iDiDj"
004868ab  #)/5;AGM
00486a41  u\jDQE
004876e4  le4YuY
00487ef7  T0XrXB
00487f9f  T0XrXB
004885e4  qPRlKb
004899af  aEh,CD`
00489a53  hUhRiKN
00489ad5  A)`ahA
00489af1  Q)`ahA
00489cf6  tP]FTF
00489d73  hCh@iB
0048a4f5  hShRi@
0048a70e  @DBDDD
0048b519  eqf`m!o
0048bca8  pGpGpGpGpGpG
0048bfdd  atDUhO
0048c11e  lXX{X~XXXXXuXXXXr
0048c7f1  A)PpG)X!
0048c7fb  A)PpGPC@
0048c812  5Y4YpGAh!
0048c830  pGmcpu.c
0048c839  read_dmem_m3control
0048c84d  configure_frame0_0_irq
0048c864  configure_subframe0_0_irq
0048c87e  configure_subframe0_3_irq
0048c898  isr_vftg_subframe0_0
0048c8ad  isr_pcc_stable
0048c8bd  adisp.c
0048c8c5  tsq_control
0048c8d1  single_pipe_start_frm_state_machines
0048c8fc  calc_vbi_position_lines
0048c914  apt_init
0048c91d  apt_vbi
0048c925  apt_control
0048c931  apt_activate
0048c93e  adaptive_sync.c
0048c94e  adaptive_sync_control
0048c964  adaptive_sync_determine_min_max_duration
0048c98d  qms_tsq
0048c995  adaptive_sync_activate
0048c9ac  qms_vftg_update
0048c9bc  bics_stub.c
0048c9c8  isr_bis_handler
0048c9d8  isr_BicsFErr_RdDecompressError
0048c9fc  ca_discharge
0048ca09  ca_active
0048ca13  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
0048ca64  cdi_v3.c
0048ca6d  isr_cdidone
0048ca79  cdi_check_idle
0048ca88  cdi_prepare_cmd
0048ca98  cdi_control
0048caa4  cdi_irq_FifoOverflow
0048cab9  cdi_irq_RunAtVbi
0048caca  cdi_irq_AxiErr
0048cad9  cdi_irq_SfWrErr
0048cae9  cdi_irq_Type0RunAtType1BarrierT
0048cb09  cdi_irq_Type1RunAtEndT
0048cb20  get_cmd_table_with_tag
0048cb37  cdi_table_mark_done
0048cb4b  set_cmd_completed_state
0048cb63  cdi_configure_table
0048cb77  debug_helper.c
0048cb86  debug_helper_stop_clock
0048cb9e  fast_update_legacy.c
0048cbb3  fast_layer_update_regs
0048cbca  ferror_handlers.c
0048cbdc  isr_SecurityStat
0048cbed  ferr_AxiWrErr
0048cbfb  ferr_AxiRdErr
0048cc09  ferr_SfOverflow
0048cc19  ferr_Replay_DecompressFail
0048cc34  ferr_GP_DecompressFail
0048cc4b  ferr_ReplayReadback_Underrun
0048cc68  ferr_Underrun
0048cc76  follower_mode_v3.c
0048cc89  follower_mode_trigger
0048cc9f  LFC: dmem w 0x%x
0048ccb1  LFC: A->R 
0048ccbd  LFC: 8.3 ms repeat. Rem %u 
0048cce0  lfc_control
0048ccec  LFC: R->R 
0048ccf8  LFC: Clear Pending from swid %u 
0048cd1a  LFC: rem_sfm %u nr %u
0048cd31  LFC: status %d 
0048cd42  LFC: Reset states 
0048cd56  M3 adisp SPDS version expecting %x, found %x
0048cd84  dmem SPDS version expecting %x, found %x
0048cdae  video_mode_main_init.c
0048cdc5  main_init
0048cdcf  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
0048ce1b  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
0048ce69  M3 vbi_pulse %u, vbi_offset %d (initial %d)
0048ce95  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
0048ced9  Control M3 error: Must have one subframe for external panels
0048cf17  mode_change_v2.c
0048cf28  isr_mode_change_req
0048cf3c  M3 New Mode: %s
0048cf52  Normal
0048cf59  WARNING; TSQ entry at normal to auto mode change. Replay=%d
0048cf95  sideband_can_mode_switch
0048cfae  ../common/mxwrap_msgbox_mprintf.c
0048cfd0  m3_message
0048cfdb  ../common/mprintf_shared.h
0048cff6  m3_log_text
0048d002  m3_vsnprintf
0048d00f  isr_inbox0_not_empty
0048d024  pdc_v22.c
0048d02e  pdc_cdi_configure_area
0048d045  pdc_rw_dma_early_stop
0048d05b  pdc_ext_wb_buffer_overflow
0048d076  pdc_int_wb_buffer_overflow
0048d091  pdc_wr_dma_fail
0048d0a1  pdc_rd_dma_fail
0048d0b1  pdc_rd_decompress_error
0048d0c9  pdc_control_vid
0048d0d9  piodma_tagging.c
0048d0ea  isr_apiodma
0048d0f6  piodma_check_idle
0048d108  apiodma_irq_ParseErr
0048d11d  apiodma_irq_SeqPushErr
0048d134  apiodma_irq_AxiErr
0048d147  apiodma_irq_AddrBoundsErr
0048d161  piodma_irq_command_tag_completed_mismatch
0048d18b  piodma_transaction_not_completed_tsq
0048d1b0  piodma_transaction_not_completed_prc0
0048d1d6  piodma_transaction_not_completed_prc1
0048d1fc  piodma_transaction_not_completed_pdclut
0048d224  piodma_transaction_not_completed_hgod
0048d24a  piodma_transaction_not_completed_pcc2dluslut
0048d277  piodma_transaction_not_completed_proxlut
0048d2a0  piodma_transaction_not_completed_spuc_map
0048d2ca  piodma_transaction_not_completed_alsslut
0048d2f3  piodma_transaction_not_completed_acsslut
0048d31c  piodma_transaction_not_completed_ptuclut
0048d345  debug_logging_update_piodma_done
0048d366  piodma_control_tagging.c
0048d37f  piodma_control
0048d38e  pixel_capture_info2.c
0048d3a4  pixel_capture_frame_info
0048d3bd  prc_v4.c
0048d3c6  prc_active
0048d3d7  rca_trigger_check
0048d3e9  rca_vbi_check
0048d3f7  isr_rca_main
0048d404  isr_rca_error_handler
0048d41a  configure_rca_dpg_subframe0_1_irq
0048d43c  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
0048d478  disp_perf_state.c
0048d48a  error_rt_bwr_exceed_max_perf_state
0048d4ad  Control M3: update_disp_perf_state_hw %d -> %d
0048d4dd  dptx_multi_sdp.c
0048d4ee  dptx_sdp_init
0048d4fc  timebase.c
0048d507  read_timebase
0048d525  Unsupported: '%c'
0048d537  0123456789ABCDEF
0048d548  0123456789abcdef
0048de3d  pt0upu
0048e028  f0D`fiX@
0048e1f4  pNLKKO
0048e8b6  `iJShC
0048efc6  QhP1|pz
0048f004  QpnhPO
0048f336  &*XiX#o
0048f4af  RHDi0F
0048f755  @DXP0F
00490816  u\jDQE
004917e2  T(XjXB
00491890  T(XjXB
00492d80  hQhQiB
00492e1c  n\FXo@
00492fc8  `IhBn1
004930f0  aEh,CD`
00493194  hUhRiHN
00493212  A)`ahA
0049322e  Q)`ahA
00493476  hCh@iB
00494881  pGpGpGpGpGpG
00494bb6  atDUhO
00494cf7  lXX{X~XXXXXuXXXXr
00495358  ApGPC@
00495386  A!PpGZ
004953aa  PpGAh!
004953b3  A`pGmcpu.c
004953be  read_dmem_m3control
004953d2  configure_frame0_0_irq
004953e9  configure_subframe0_0_irq
00495403  configure_subframe0_3_irq
0049541d  isr_vftg_subframe0_0
00495432  isr_pcc_stable
00495442  adisp.c
0049544a  tsq_control
00495456  single_pipe_start_frm_state_machines
00495481  calc_vbi_position_lines
00495499  apt_init
004954a2  apt_vbi
004954aa  apt_control
004954b6  apt_activate
004954c3  adaptive_sync.c
004954d3  adaptive_sync_control
004954e9  adaptive_sync_determine_min_max_duration
00495512  qms_tsq
0049551a  adaptive_sync_activate
00495531  qms_vftg_update
00495541  bics_stub.c
0049554d  isr_bis_handler
0049555d  isr_BicsFErr_RdDecompressError
00495581  ca_discharge
0049558e  ca_active
00495598  M3 CA parity error -- saved value 0x%08x does not match calculated value 0x%08x
004955e9  cdi_v3.c
004955f2  isr_cdidone
004955fe  cdi_check_idle
0049560d  cdi_prepare_cmd
0049561d  cdi_control
00495629  cdi_irq_FifoOverflow
0049563e  cdi_irq_RunAtVbi
0049564f  cdi_irq_AxiErr
0049565e  cdi_irq_SfWrErr
0049566e  cdi_irq_Type0RunAtType1BarrierT
0049568e  cdi_irq_Type1RunAtEndT
004956a5  get_cmd_table_with_tag
004956bc  cdi_table_mark_done
004956d0  set_cmd_completed_state
004956e8  cdi_configure_table
004956fc  debug_helper.c
0049570b  debug_helper_stop_clock
00495723  ferror_handlers.c
00495735  isr_SecurityStat
00495746  ferr_AxiWrErr
00495754  ferr_AxiRdErr
00495762  ferr_SfOverflow
00495772  ferr_Replay_DecompressFail
0049578d  ferr_GP_DecompressFail
004957a4  ferr_ReplayReadback_Underrun
004957c1  ferr_Underrun
004957cf  follower_mode_v3.c
004957e2  follower_mode_trigger
004957f8  LFC: dmem w 0x%x
0049580a  LFC: A->R 
00495816  LFC: 8.3 ms repeat. Rem %u 
00495839  lfc_control
00495845  LFC: R->R 
00495851  LFC: Clear Pending from swid %u 
00495873  LFC: rem_sfm %u nr %u
0049588a  LFC: status %d 
0049589b  LFC: Reset states 
004958af  M3 adisp SPDS version expecting %x, found %x
004958dd  dmem SPDS version expecting %x, found %x
00495907  video_mode_main_init.c
0049591e  main_init
00495928  M3 display_lead_nclks: %u, subframe_lines %u, tsq_position %u (initial %u)
00495974  M3 active_subframes_cnt %u, auto_duration_sfm %u, subframe_duration_nclks %u
004959c2  M3 vbi_pulse %u, vbi_offset %d (initial %d)
004959ee  M3 initial frame ID: %u, frame counter: %u, subframe: %u, line: %u
00495a32  Control M3 error: Must have one subframe for external panels
00495a70  mode_change_v2.c
00495a81  isr_mode_change_req
00495a95  M3 New Mode: %s
00495aab  Normal
00495ab2  WARNING; TSQ entry at normal to auto mode change. Replay=%d
00495aee  ../common/mxwrap_msgbox_mprintf.c
00495b10  m3_message
00495b1b  ../common/mprintf_shared.h
00495b36  m3_log_text
00495b42  m3_vsnprintf
00495b4f  isr_inbox0_not_empty
00495b64  piodma_tagging_ext.c
00495b79  isr_apiodma
00495b85  piodma_check_idle
00495b97  apiodma_irq_ParseErr
00495bac  apiodma_irq_SeqPushErr
00495bc3  apiodma_irq_AxiErr
00495bd6  apiodma_irq_AddrBoundsErr
00495bf0  piodma_irq_command_tag_completed_mismatch
00495c1a  piodma_transaction_not_completed_tsq
00495c3f  debug_logging_update_piodma
00495c5b  debug_logging_update_piodma_done
00495c7c  piodma_control_tagging.c
00495c95  piodma_control
00495ca4  pixel_capture_info2.c
00495cba  pixel_capture_frame_info
00495cd3  prc_v4.c
00495cdc  prc_active
00495ce7  rt_bw_error_bandwidth_increasing_at_procfrm on frame %04x!
00495d23  disp_perf_state.c
00495d35  error_rt_bwr_exceed_max_perf_state
00495d58  Control M3: update_disp_perf_state_hw %d -> %d
00495d88  dptx_multi_sdp.c
00495d99  dptx_sdp_init
00495da7  timebase.c
00495db2  read_timebase
00495dd0  Unsupported: '%c'
00495de2  0123456789ABCDEF
00495df3  0123456789abcdef
0049608a  )=hqu?=,
004969bc  Invalid
004980ba  XFQFBF
00498174  BFdFqFG
0049830c   `XFAF2FSF
00498368  1FXFRF
00498649  `0FAF*F#F
00498b9b  @0F)FJF
00499673  B*dJl"
0049a047  `0F)F"FCF
0049a75c  tA XaX
0049a9e4  tA0XqX
0049bc96  +FbFDFNF_
0049c27e  0FAFJF #
0049c28c  0FAF"F #
0049c299  F0FAFA
0049c2a7  F0FAFZF #
0049c9c3  U*DJaF
0049c9f2  hAAXQ`F
0049ca0a  tAAXQaF
0049ca87  0pETDA
004a209e  mcpu_pcc2d_ltm.c
004a20af  ltm_config_fw
004a20bd  pcc2d_ltm_isr_first_pixel_impl
004a20dc  ltm_process_local_hist_0dbl
004a20f8  pcc2d_ltm_isr_mce_task_complete
004a2118  mprintf_msgbox_pcc2d_ltm.c
004a2133  m3_message
004a213e  m3_log_text
004a214a  isr_inbox0_not_empty
004a37ca  |a8ete0i
004a37ea  |i8mtm0q
004a380c  |q8utu0y
004a394a  <cxc4gpg
004a3966  <kxk4opo
004a3984  <sxs4wpw
004a3a66  <cxc4gpg
004a3a82  <kxk4opo
004a3a9e  <sxs4wpw
004a3b7c  <cxc4gpg
004a3b9a  <kxk4opo
004a3bb8  <sxs4wpw
004a428a  XfTbSu
004a44dd  bXbPfLj
004a4779  bXb7&#>
004a4b65    !zdea~
004a5d5c  GQCw'y'
004a5d74  GQCw'y'
004a5d8c  GQCw'y'
004a5da4  GQCw'y'
004a5dba  GQCw'y
004a5dce  GQCw'y
004a5dde  GQCw'y
004a6042  Csg0Ss
004a91fe  RTKit_release-3504.0.0.0.1.release
004a94dd  stk_fail
004a94e6  !Mthd:%p
004aafbc  not set
004ab328  coverglass-serial-number
004acd95  _HNIq$
004ad7fc  aw`wnw
004adb32  qpzewww
004addf7  qdwww9
004c0be8  display-timing-info
004c0c83  >subframe-duration-nclks
004c0c9c  display-lead-time-nclks
004c0cb4  subframe-interrupt-time-lines
004c0cd2  frame-duration-nclks
004c0d10  mbox-register-len
004c0d22  mbox-register
004c0d9c  DispTargetEXT
006e2374  piodma-t-nclks
006e2383  swmpr-t-nclks
006e2391  frame-duration-lpm-nclks
006e2420  oracle-tc-red
006e242e  oracle-tc-green
006e243e  oracle-tc-blue
006e244d  oracle-sf-red
006e245b  oracle-sf-green
006e246b  oracle-sf-blue
006e24a4  DispTargetP62
006e24b2  DispTargetP63
006e24c0  DispTargetP64
006e24ce  DispTargetP68
006e24dc  DispTarget595
006e24ea  DispTargetS510
006e24f9  DispTargetS837
006e2508  DispTargetS807
006e2517  DispTargetS68
006e2525  DispTargetS68_DOE1
006e2538  DispTarget67
006e2545  DispTargetX3200
006e2920  proxboled-config
006e3574  backlight-calibration-parameters
006e3595  color-accuracy-index
006e35aa  vbatt-current
006e35b8  raw-panel-id
006e35c5  dcvrr-a
006e35cd  dcvrr-b
006e35d5  dcvrr-c
006e35dd  dcvrr-d
006e35e5  apt-version-control
006e35f9  tcon-2dira-enable
006e3628  adisp-register-len
006e363b  adisp-register
006e364a  service-node-match
006e365d  power-gates
006e3669  power-gates-len
006e3679  power-gates-stg2
006e368a  power-gate-dsg
006e3699  power-gate-dbe
006e36a8  power-node-split
006e36b9  clock-ids
006e36c3  dptx-generic-sdp-base
006e36d9  perf-addr
006e36e3  bw-addr
006e3948  fc~kbf
006e4ac1  bX=XVC
006eb979  Ifg>Ibf
006f409f  bBX"iT
006f4b53  /OcMw:
006fbf71  Ifg>C37
0070042c  #wcw"C
00704341  (HBpLbBX
00708311  V=[ded
0070843c  `DVK+g
0070b5d8  tvx{ppqrrqpp{xvt
0070b604  jnty[^bfRTVXPPPQTRQP^[XVnjfb
0070b638  fls{OTY_>BFJ468;00122100;864JFB>_YTO{slf
0070b674  [ckt@FMT*/4:
0070b6b4  ^hq{<DMU '.5
0070b6cc  5.' UMD<{qh^
0070ba0d  4OjjO4
0070ba2d  .JffJ.
0070ba4d  *GccG*
0070ba89  )FccF)
0070bb59  %DccD%
0070bd9d  %DccD%
0070be6d  )FccF)
0070bea9  *GccG*
0070bec9  .JffJ.
0070bee9  4OjjO4
0070c224  ^hq{<DMU '.5
0070c23c  5.' UMD<{qh^
0070c27c  :4/*TMF@tkc[
0070c29c  fls{OTY_>BFJ468;00122100;864JFB>_YTO{slf
0070c2dc  bfjnVX[^PQRTQPPPXVTRfb^[ytnj
0070c314  tvx{ppqrrqpp{xvt
0071390e  NOi=_o
0071798e  &(HbA8
0072d624  fc>Iff
007328b6  9@Oeww
00734be0  {|}}zzz{{{zz
00734c30  tuwxppqrnnnonnnnqppowutr~|zx
00734cdc  psvzfikn_`bdYZ[]VWWXUUUVWWVV[ZYXb`_]kifdvspn
00734d3c  hknq]_beTVXZNOQRJKLMIIIJJJIINMLKTRQO]ZXVheb_uqnk
00734d9c  impt\_beQSVYHJLNBCEF>?@A===>>>==BA@?HFECQNLJ\YVSieb_xtpm
00734e00  imquZ]aeMPSVBEGJ:<>@56791234111132117654><:9GEB@SPMJa]ZVqmie
00734e68  fjosUY]aGKNR;>AD2469+-.0''(*%%%&%%%%(''&.-+*6420A>;9NKGD]YURojfa
00734ed0  mrw|Z_chJNRV<?BF0258&(*-
00734f00  *(&$520-B?<8RNJFc_ZVwrmh
00734f40  ]bglKOTX:>BF-037!$&)
00734f74  -)&$:730KFB>]XTOqlgb
00734fb0  \aflHMRW7;?D(+/3
00734fe8  +($!;73/MHD?a\WRwqlf
00735020  aglrLQV[8=BG'+/4
00735048  4/+'GB=8[VQLrlga
0073507c  bhntKQV\7;AF$(-2
007350a0  2-($FA;7\VQKtnhb
007350d4  ]cipFKQW05;@
007350f4  50+&KF@;c]WQ}vpi
00735124  elryLRY_5;AF %*0
00735144  ;50*RLFAle_Y
00735174  T[ah<BHN%*06
00735190  B<60[TNHvoha
007351bc  ^elsDJQW+17=
007351d8  =71+WQJDsle^
00735204  [bip@FMT&-39
0073521c  93-&TMF@pib[
00735248  X_fn<CJQ"(/5
00735260  C<5/_XQJ}unf
00735288  dls{GNU]+29@
007352a0  @92+]UNG{sld
007352c8  bjrzDLS[(/6=
007352e0  =6/([SLDzrjb
00735308  ahpxBIQY%,3;
00735320  IB;3haYQ
007353c0  EMU]%-5=
0073553c  NWaj*3<E
0073554c  E<3*jaWN
00735570  FOYb!*4=
00735580  OF=4ulbY
007355a0  [dnw5>HQ
007355e4  SI@6zpf]
00735634  Xblv1;DN
007356d4  C9/%laWM
00735760  D9/%ncYN
007357ac  LWbl"-7B
00735814  A6+ laVK
00735860  KVal *5@
0073586c  @5* laVK
007358c4  LA5*xmbW
0073590c  Xcoz+7BM
0073599c  K?4(xmaV
007359f0  NB7+|peY
00735a0c  Uamx'3>J
00735a60  Zeq}+7BN
00735a98  K?3(znbV
00735b14  MA5)|peY
00735b30  Vbnz&2>J
00735bfc  Vbnz&2>J
0073601c  J>2&znbV
007360e8  J>2&znbV
00736104  Yep|)5AM
00736180  Vbnz(3?K
007361b8  NB7+}qeZ
0073620c  J>3'xmaU
00736228  Yep|+7BN
0073627c  Vamx(4?K
0073630c  MB7+zocX
00736354  Wbmx*5AL
007363ac  KVal *5@
007363b8  @5* laVK
00736404  KVal +6A
0073646c  B7-"lbWL
007364b8  NYcn%/9D
00736544  MWal%/9C
007365e4  ND;1vlbX
00736634  ]fpz6@IS
00736678  QH>5wnd[
00736698  Yblu4=FO
007366a8  =4*!bYOF
007366cc  NWaj*3<E
007366dc  E<3*jaWN
00736858  =5-%]UME
007368f8  QYah3;BI
0073690c  ;3,%YQIBxpha
00736934  bjrzDLS[(/6=
0073694c  =6/([SLDzrjb
00736974  dls{GNU]+29@
0073698c  @92+]UNG{sld
007369b4  fnu}JQX_/5<C
007369cc  5/("QJC<nf_X
007369f8  [bip@FMT&-39
00736a10  93-&TMF@pib[
00736a3c  ^elsDJQW+17=
00736a58  =71+WQJDsle^
00736a84  ahovHNT[06<B
00736aa0  60*%NHB<ha[T
00736ad0  Y_elAFLR*05;
00736aec  0*% FA;5_YRLyrle
00736b1c  ipv}QW]c;@FK&+05
00736b40  @;50WQKFpic]
00736b70  bhntKQV\7;AF$(-2
00736b94  2-($FA;7\VQKtnhb
00736bc8  aglrLQV[8=BG'+/4
00736bf0  4/+'GB=8[VQLrlga
00736c24  flqwRW\a?DHM/37;!$(+
00736c60  3/+(D?;7WRMHlfa\
00736c98  bglqOTX]>BFK037:$&)-
00736ccc  )&$!730-FB>:XTOKlgb]
00736d08  hmrwVZ_cFJNR8<?B-025$&(*
00736d38  -*(&8520FB?<VRNJhc_Z|wrm
00736d78  afjoRUY]DGKN9;>A0246*+-.&''(%%%%&%%%*(''0.-+9642DA>;RNKGa]YUsojf
00736de4  eimqVZ]aJMPS@BEG9:<>45671123111143219765@><:JGEBVSPMea]Zuqmi
00736e4c  mptx_beiSVY\JLNQCEFH?@AB==>>>===A@?>FECBNLJHYVSQeb_\tpmi
00736eb4  knqu_behVXZ]OQRTKLMNIIJJJIIIMLKJRQONZXVTeb_]qnkh
00736f18  npsvdfik]_`bXYZ[VVWWVUUUXWWV][ZYdb`_nkifzvsp
00736fd4  xz|~rtuwoppqnnnnonnnrqppxwut
00737034  zz{{{zzz}}|{
0074b711  |:fik[
0074f9e1  #J,RXI
0075093c  Hvww`w
007529ec  ilosbceg```aecbaolig
00752a1c  jpv|W[`eILOSBCEG@@@AECBAOLIG`[WSvpje
00752a58  V]dk@EKP/37;%'), !"#"!  )'%#73/,KE@;d]VP
00752abc  71+&TLE>vmd\
00752adc  ENWa&-5=
00752af0  =5-&aWNE
00752b0c  LVal&/9B
00752b1c  B9/&laVL
00752b34  Yeq~.8CN
00752b44  NC8.~qeY
00752e39  3NiiN3
00752e59  ,HccH,
00752f09  6TqqT6
00752f39  0NllN0
00752f65  .LkkL.
00752fa1  &EddE&
00753295  %CaaC%
00753311  1NkkN1
00753331  1NjjN1
00753435  0IbbI0
00753458  )AYrA)
007536a4  NYeq$.8C
007536dc  LB9/wlaV
0075370c  E=5-kaWN
0075376c  dks{KPV]7;@E),/3"#%'   !%#"!/,)'@;73VPKEskd]
007537b0  `ejpOSW[EGIL@ABCBA@@IGECWSOLje`[
007537ec  osv{egil`abcba``igecvsol
00768d63  DG8ANe
00772998  stk_fail
007729a1  rtk_background
007729b0  %s-afk-log
007729bb  dcp_force_syslog
007729cc  power_work
007729d7  power_remote_work
007729e9  ASSERT!%s:%d power_conductor not inited
00772a11  platform_config_common.cpp
00772a2c  dcp_background_thread_priority
00772a4b  dcp_ktrace_thread_priority
00772a66  ktrace_work
00772a72  dcp_kdebug_capacity
00772a86  ASSERT!%s:%d status=0x%x
00772a9f  dcp_kdebug_threshold
00772ab4  dcp_kdebug_mask
00772ac4  main.cpp
00772acd  ASSERT!%s:%d Invalid IO Base 0x%llx or IO Size %u
00772b00  DCPTunables.h
00772b0e  ASSERT!%s:%d Received config size (%zu) is not as expected (%zu)
00772b4f  DCPTunablesT8160.h
00772b62  DispTargetP510
00772b71  DispTarget348
00772b7f  DispTarget301_D90
00772b91  DispTarget109
00772b9f  Failed to map registers
00772bb7  dcp_tracekit_buffer_kb
00772bce  tracekit_work
00772bdc  dcp_tracekit_control
00772bf1  log_tx
00772bf8  dcp_log_coalescer_flush_priority
00772c19  ASSERT!%s:%d MBI_ENDPOINT_BUILT_IN_OSLOG not enabled!
00772c4f  platform_logging_common.cpp
00772c6b  dcp-2-smc
00772c75  dcpsec-2-smc
00772c82  targetTBClient.cpp
00772cf8  BrightnessUtilControllerPMUTBServer::Handler
00772d40  TCONiBootInterfaceTBServer::Handler
00772d64  invalid tag in `[UInt8]` metadata: 0x%x
00772d8c  I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8
00772dcf  invalid result returned from setEnabled
00772df7  invalid result returned from setRawBrightness
00772e2b  invalid result returned from displayPower
00772e55  invalid result returned from set2diraEnable
00772e81  invalid result returned from getSerialNumber
00772eae  invalid result returned from displayPmicDebugPanic
00772ee1  invalid result returned from getConfigInfo
00772f0c  !MIDR: 0x%x
00772f18  ~CsPTR
00772f1f  !ROf %#lx %#x
00772f2d  pagetracker-impl.inc.h
00772f44  PGT_ERROR_ALREADY_MAPPED
00772f5d  PGT_ERROR_VA_OUT_OF_RANGE
00772f77  PGT_ERROR_MAPPING_TOO_BIG
00772f91  PGT_ERROR_NO_SPLITTING
00772fa8  PGT_ERROR_MAP_MODES_NOT_COMPATIBLE
00772fcb  PGT_ERROR_NOT_MAPPED
00772fe0  PGT_ERROR_ALLOCATION_FORBIDDEN
00772fff  PGT_ERROR_UNTYPED_CREATE_FAILED
0077301f  PGT_ERROR_OUT_OF_CAP_SLOTS
0077303a  PGT_ERROR_OUT_OF_FRAMEISH_SLOTS
0077305a  PGT_ERROR_OUT_OF_TABLE_SLOTS
00773077  PGT_ERROR_CANT_REMAP_PARTIAL
00773094  unknown pgt_error_t value
007730bd  pgt_map_pa_range(va=%lx, pa=%llx, size=%lx, offset=%lx): not page-aligned
00773107  err1: %s at offset: %#lx, err2: %s
0077312a  range [pa=%llx, size=%lx] not in untypeds (try adjusting .mmio)
0077316a  range [pa=%llx, size=%lx] stretches past end of untyped (try adjusting .mmio)
007731b8  untyped (%s) !size
007731cb  untyped (%s) !cap_slot
007731e2  !untyped
007731eb  !pgt_assert (%s:%d)
007731ff  !mode %#x
00773209  pagetracker-bits.h
0077321c  !aligned
00773225  invalid page state
00773238  err: %s offset: %#lx, then when unmapping partial result, pgt_unmap err: %s
00773284  err: %s offset: %#lx, then when re-mapping large, pgt_map_pa_range err: %s
007732cf  this thread's stack
007732e3  pagetracker state
007732f5  va_overlap %s
00773303  PageFrame_Protect err: %s
0077331d  pgt_actually_unmap_frame
00773336   (untyped cap was RO but tried to map as RW?)
00773364  %s: map attr err: %s%s
0077337b  pgt_actually_map_frame
00773392  L4_Cap_Delete err: %s
007733a8  overflow
007733b1  pgt_map_internal
007733c2  bad page table level
007733d7  pa=0x%llx size=0x%llx cap_slot_idx=0x%x
007733ff  !tree depth
0077340b  !space +future_untyped_count
00773428  !tree index
00773434  untyped (%s) overlaps with (%s)
00773454  !mmu lock:%x
00773461  !2xinit
00773469  !ctors %zu %zu
00773478  !osckit-headers:%u,%u/%u,%u
00773495  Platform timer does not support setting frequency (for now)
007734d1  L4_ErrorSuccess
007734e1  L4_ErrorPreempted
007734f3  L4_ErrorCanceled
00773504  L4_ErrorTruncated
00773516  L4_ErrorCapInvalid
00773529  L4_ErrorSlotInvalid
0077353d  L4_ErrorMethodInvalid
00773553  L4_ErrorArgumentInvalid
0077356b  L4_ErrorOperationInvalid
00773584  L4_ErrorPermissionInvalid
0077359e  !endpoint
007735a8  !early-boot
007735b5  chan msg type %#x != DATA
007735cf  !data body size
007735df  chan msg type %#x != PHYS_ACCESS
00773600  !PAB size
0077360a  !PAB: m=%#x a=%#llx s:%zu
00773624  !phys-access
00773631  !cap_slot: %d
0077363f  !find_channel: %#x %#x %#x
0077365a  !sem_wait %#x
00773668  !copy_message: s %#zx ms %#zx
00773686  !copy_message 2
00773696  rptr 0x%zx wptr 0x%zx size 0x%zx
007736b8  sem !empty
007736c3  hosted_ipc: PHYS_ACCESS %#x != %#zx
007736e7  bad msg %#x
007736f3  RTK_hashtable_init
00773706  malloc
0077370d  RTK_hashtable_set
0077371f  !badge:%u
00773729  !notify:%s(%lu)
00773739  !prio:%s(%lu)
00773747  !pac,%#llx:%#llx:%#llx:%#llx:%#llx
0077376a  !pac,irq
00773788  Duty cycle
00773793  Sleep count
0077379f  Wake count
007737aa  Power state
007737b6  Free heap
007737c0  Total heap
007737cb  Peak heap alloc
007737db  Used stack
007737e6  Total stack
007737f2  CPU count
007737fc  Thread time
00773808  Performance
00773814  Terminator
00773823  ASSERTION FAILED: %s:%d
00773843  ThIntr:%u,%u,%u,%u
00773856  ThLock:%p
00773860  MBI queue overflow:%s
00773876  !Mthd:%p
0077387f  unimplemented
0077388d  [CED] CLLT escalation detected
007738ad  mme:0x%x
007738b6  SPMI:%d (%d,%#X,%u)
007738ca  SPMI Fatal Error: %s Blocked
007738e7  Transfer
007738f0  HW Q Reset
007738fb  Filter Modification
0077390f  VmOv %d %d
0077391a  !vm nodes
00773924  Unbalanced transients
0077393a  RTKit: %s - Client: %s
00773951  __cxa_guard_acquire
00773965  __cxa_guard_release
0077397d  MGMT msg=0x%llx st=%x
00773993  MGMT st=%x
0077399e  !reg clscr %u ps: 0x%x, 0x%x
007739bb  !kb reg:%x
007739c6  rtk_ep_work
007739dd  Corrupt log channel
007739f1  LOG: entries sz >= coalescer sz (%zu >= %zu)
00773a1e  log_flush
00773a28  !flush: %x r=%zu w=%zu (%zu/%zu)
00773a49  <null>
00773a50  pmc.cpp
00773a58  %s PMC Not IDLE, dcp_pipe=%d perf_state=%d
00773a83  RTKPMGR_pmc_boost_disp_perf_state
00773aa5  %s dcp_pipe=%d perf_state=%d
00773ac2  PMCLib Init
00773acf  pmgr_t8160.cpp
00773ade  Welcome to RTKitPMGR!: %s : t8160
00773b00  RTKPMGR_platform_init
00773b16  Disp perf state table is not set properly
00773b40  %s: RTKitPMGR cannot config LAPLL for device %d
00773b70  RTKPMGR_config_pll
00773b83  RTKPMGR_platform_get_disp_clock
00773ba3  pmgr.cpp
00773bac  RTKPMGR_config_video_clock
00773bc7  %s: disp_index= %d,  configPll= %d, srcSel= %d, divider= %d
00773c03  %s lvl=%d
00773c0d  RTKPMGR_set_log_lvl
00773c21  %s Enabling PMC APIs
00773c36  RTKPMGR_enable_pmc
00773c49  RTKPMGR_enable_profile
00773c64  rtkpmgr-profile
00773c74  rtkpsd_platform_default.cpp
00773c90  %s: Invalid client
00773ca3  initClientConfig
00773cb4  Invalid numServiceSlots: 0x%x
00773cd2  %s:client not init
00773ce5  getServiceName
00773cf4  %s: invalid param
00773d06  %s: Invalid slot pio index for client: %#x service: %#x
00773d3e  %s: invalid id: %u
00773d51  getResetSendPayload
00773d65  %s: invalid payload ptr
00773d7d  Client not initialized!!
00773d96  Latency to P State Translation Failed
00773dbc  Invalid slot pio index for client: %#x service: %#x
00773df0  %s: client not init
00773e04  initServiceConfig
00773e16  %s: Invalid initConfig
00773e2d  %s: serviceId 0x%x already initialized
00773e54  getNumServiceSlots
00773e67  getServiceConfig
00773e78  %s: Error Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
00773ebf  %s: Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
00773eea  rtkpmgr-loglvl
00773ef9  rtkpsd_common.cpp
00773f0b  %s: getServiceConfig(0x%x) err: 0x%x
00773f30  _initServiceDashboard
00773f46  %s: Unsupported service id: 0x%x
00773f67  %s:RTK dev init(0x%x) fail: 0x%x
00773f88  %s:RTK dev config(0x%x) fail: 0x%x
00773fab  %s:RTK dev wake(0x%x) fail: 0x%x
00773fcc  %s: Not support PSD ACK mode: %d
00773fed  _stateChange
00773ffa  %s: Prev req pending service=0x%x wrVal=0x%x: 0x%x
0077402d  %s: Prev reqs caused sem signal service=0x%x wrVal=0x%x: 0x%x
0077406b  PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x) prevRdVal: (%#x) timeout after %llu usec
007740dd  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) sem wait err: (%#x)
0077412b  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) != rdVal: (%#x) err
00774179  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x)
007741c0  _getPowerStateVote
007741d3  %s: client=0x%x service=0x%x err: 0x%x
007741fa  %s: clientId=0x%x serviceId=0x%x pstate=%d
00774225  %s: initClientConfig err: 0x%x
00774244  initPSDService
00774253  %s: initServiceConfig err: 0x%x
00774273  %s: initServiceDashboard err: 0x%x
00774296  %s: done clientId=0x%x serviceId=0x%x
007742bc  %s: clientId=0x%x serviceId=0x%x active=%u ltr_usec=%u
007742f3  enablePSDService
00774304  %s: getNumServiceSlots err: 0x%x
00774325  %s: invalid params
00774338  %s: stateChange(serviceId 0x%x) err: 0x%x
00774362  %s: clientId=0x%x serviceId=0x%x
00774383  getPSDServiceVote
00774395  %s: _getPowerStateVote(serviceId 0x%x) err: 0x%x
007743c6  %s: Reset already initialized
007743e4  initPSDReset
007743f1  %s: routingEpId=0x%x
00774406  %s: Reset not initialized
00774420  sendPSDReset
0077442d  %s: getResetSendPayload err: 0x%x
0077444f  %s: Start - routingEpId=0x%x id=0x%x payload=0x%llx
00774483  %s: MBI send msg timeout (routingEpId=0x%x id=0x%x)
007744b7  %s: MBI send msg err (routingEpId=0x%x id=0x%x): 0x%x
007744ed  %s: MBI recv msg timeout (routingEpId=0x%x id=0x%x)
00774521  %s: MBI recv msg err (routingEpId=0x%x id=0x%x): 0x%x
00774557  %s: checkResetRcvdPayload err: 0x%x
0077457b  %s: Done - routingEpId=0x%x id=0x%x payload=0x%llx
007745b5  setPSDLogLevel
007745c4  mcw_v1.cpp
007745cf  Requested buf size(%d) is greater than max allowed size(%d)
0077460c  Requested address alignment value(%d) is not supported.
00774645  Invalid parameters. bufid:%d buf_size:0x%x max_size:0x%x
0077467f  Request to allocate bufid %d while it is already mapped
007746b8  Bufid 0x%x offset 0x%x size 0x%x crosses max size 0x%x
007746f0  Failed to map for bufid %d size 0x%x. status:0x%x
00774723  SRAM buffer allocation failure- bufid:%d  buf_offset:0x%x buf_size:0x%x status:0x%x
00774778  Invalid buf_st_addr parameter
00774797  Invalid parameters. bufid:%d
007747b5  Request to deallocate bufid %d when it is not allocated
007747ee  Failed to unmap for bufid %d. status:0x%x
00774819  SRAM buffer deallocation failure- bufid:%d status:0x%x
00774851  INVALID
00774859  PRIM_DCP
0077486a  SEC_DCP
00774872  ACPU_AUDIO
0077487d  UNKNOWN
00774885  Unknown mcw clientid %s (%d)
007748a3  MCW client %s (id=%d) is not supported on this platform
007748dc  RTK_dev_control failed with error 0x%x
00774904  !power: %#x
00774923  !hst:%#x
00774934  !Heapblk:%p
00774940  !mbs:%zu
0077494e  !TBVI: rt=0x%x, st=0x%x
00774972  /allowlists
0077497e  routing
0077498f  TB BdSt %#x
0077499b  !ASPA%#x
007749a4  !AGPA:%#x
007749ae  !rtac:%#x
007749b8  tytbmxport
007749c3  tytbmxportsrvr
007749d2  TB msg=0x%llx st=%x
007749e6  TB err st=%x
007749f3  TB StRx %#X
007749ff  TB StTx %#X
00774a0b  TBpv r:0x%x e:0x%x
00774a1e  !rtanb
```
