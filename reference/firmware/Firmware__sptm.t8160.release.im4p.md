# `Firmware/sptm.t8160.release.im4p`

- File size: 216,966 bytes
- IM4P: Tag: IM4P  Type: sptm  Version: 1
- BuildManifest components that use it: `Ap,RestoreSecurePageTableMonitor`, `Ap,SecurePageTableMonitor`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         sptm
  Version:      1
  Data:         217 kB (216624 bytes)
  Compression:  LZFSE
  Uncompressed: 1.3 MB (1327136 bytes)
  Properties:
    kcep: 18446744005645157256
    kcev: 1130496
    kclf: 1327104
    kclz: 109544
    kcmf: 131072
    kcmz: 589824
    kcwz: 163840
    kclo: 18446744005644402688
    kcrf: 0
    kcrz: 720896
    kcuu: 1840
    kcwf: 1163264
    kcxf: 720896
    kcxz: 442368
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 1,327,136 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- `RTBuddySeg`
- `SPTM_T8110_DART_SK_POWER_RELEASE`

## Strings (2,628) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000028  __TEXT
00000068  __cstring
00000078  __TEXT
000000b8  __const
000000c8  __TEXT
00000108  __binname
00000118  __TEXT
00000158  __chain_starts
00000168  __TEXT
000001b0  __DATA_CONST
000001f0  __const
00000200  __DATA_CONST
00000248  __LATE_CONST
00000288  __late_const
00000298  __LATE_CONST
000002e0  __TEXT_EXEC
00000320  __text
00000330  __TEXT_EXEC
00000380  __TEXT_EXEC
000003c8  __LAST
00000408  __pinst
00000418  __LAST
00000460  __DATA
000004a0  __data
000004b0  __DATA
000004f0  __auth_ptr
00000500  __DATA
00000550  __DATA
00000590  __common
000005a0  __DATA
000005e8  __BOOTDATA
00000628  __data
00000638  __BOOTDATA
00000680  __LINKEDIT
000008b0  [SK] Unhandled synchronous exception taken from GL1
000008e4  [SK] Unhandled synchronous exception taken from GL0
00000918  [TXM] Unhandled synchronous exception taken from GL0
0000094d  [SPTM] Synchronous exception taken while SP0 selected
00000983  [SPTM Dispatch] Synchronous exception taken while SP1 selected
000009c2  [PANIC DURING BOOTSTRAP] 
000009dc  [SK BOOTSTRAP PANIC] 
000009f2  [SK HIB PANIC] SK panic during SPTM hibernation hook
00000a27  [SPTM] Synchronous exception taken from guest before XNU bootstrap
00000a6a  [SPTM] Synchronous External Abort
00000a8c  Assertion failed: %s, function %s, file %s, line %d.
00000ac2  (null)
00000ac9  fmt->flags & FLAG_HAS_PRECISION
00000ae9  src/libc/stdio/format.c
00000b01  write_integer
00000b0f  0123456789abcdef
00000b20  0123456789ABCDEF
00000b31  Security assertion failed: %s, function %s, file %s, line %d.
00000b70  (len) <= (dstlen)
00000b82  __vsnprintf_chk
00000b92  src/libc/stdio/vsnprintf.c
00000bad  __memcpy_chk
00000bba  src/libc/string/memcpy.c
00000bd3  (smax) <= (obj_size)
00000be8  __memset_s_chk
00000bf7  src/libc/string/memset_s.c
00000c12  __strlcpy_chk
00000c20  src/libc/string/strlcpy.c
00000c3a  (!cpylen && !cpylen) || (cpylen == ~((size_t)0)) || !((uintptr_t)src < (uintptr_t)dst + cpylen && (uintptr_t)dst < (uintptr_t)src + cpylen)
00000cc6  (len) <= (obj_size)
00000cda  __bzero_chk
00000ce6  src/libc/strings/bzero.c
00000cff  stack check fail
00000d28  SPTM_UAT_ENDPOINT_INIT_STATE
00000d45  SPTM_UAT_ENDPOINT_DESTROY_STATE
00000d65  SPTM_UAT_ENDPOINT_MAP_TABLE
00000d81  SPTM_UAT_ENDPOINT_UNMAP_TABLE
00000d9f  SPTM_UAT_ENDPOINT_MAP_BEGIN
00000dbb  SPTM_UAT_ENDPOINT_MAP_CONTINUE
00000dda  SPTM_UAT_ENDPOINT_PREPARE_FW_UNMAP_BEGIN
00000e03  SPTM_UAT_ENDPOINT_PREPARE_FW_UNMAP_CONTINUE
00000e2f  SPTM_UAT_ENDPOINT_UNMAP_BEGIN
00000e4d  SPTM_UAT_ENDPOINT_UNMAP_CONTINUE
00000e6e  SPTM_UAT_ENDPOINT_SET_CTX_ID
00000e8b  SPTM_UAT_ENDPOINT_REMOVE_CTX_ID
00000eab  SPTM_UAT_ENDPOINT_GET_INFO
00000ec6  SPTM_UAT_ENDPOINT_REVOKE_SAPT_MULTIPAGE
00000ef2  VIOLATION_UAT_INVALID_SUBTYPE
00000f10  VIOLATION_UAT_INVALID_TYPE
00000f2b  VIOLATION_UAT_ILLEGAL_STATE_OBJECT_TYPE
00000f53  VIOLATION_UAT_INVALID_ROOT_TABLE
00000f74  VIOLATION_UAT_ILLEGAL_OBJECT_STATE
00000f97  VIOLATION_UAT_INVALID_OBJECT_OFFSET
00000fbb  VIOLATION_UAT_INVALID_CONTEXT_ID
00000fdc  VIOLATION_UAT_INVALID_REFCNT
00000ff9  VIOLATION_UAT_INVALID_VADDR
00001015  VIOLATION_UAT_INVALID_PADDR
00001031  VIOLATION_UAT_INVALID_PT_LEVEL
00001050  VIOLATION_UAT_ILLEGAL_FW_TABLE
0000106f  VIOLATION_UAT_ILLEGAL_TTE
00001089  VIOLATION_UAT_ILLEGAL_MAP_FOUND_OCCUPIED_PTE
000010b6  VIOLATION_UAT_ILLEGAL_UNMAP_FOUND_FREE_PTE
000010e1  VIOLATION_UAT_ILLEGAL_PAGE_TABLE
00001102  VIOLATION_UAT_INVALID_NUM_SEGS
00001121  VIOLATION_UAT_INVALID_SEGMENT
0000113f  VIOLATION_UAT_ILLEGAL_TTBAT_MAPPING
00001163  VIOLATION_UAT_INVALID_NUM_MAPPINGS
00001186  VIOLATION_UAT_ILLEGAL_PREPARE_FW_UNMAP
000011ad  VIOLATION_UAT_ILLEGAL_CACHED_MAPPING
000011d2  VIOLATION_UAT_ILLEGAL_CACHE_FLUSH
000011f4  VIOLATION_UAT_INVALID_CTX_ID
00001211  VIOLATION_UAT_ILLEGAL_SET_CTX_ID
00001232  VIOLATION_UAT_ILLEGAL_REMOVE_CTX_ID
00001256  VIOLATION_UAT_ILLEGAL_TTBAT_LOCK
00001277  VIOLATION_UAT_INVALID_INFO_TYPE
00001297  VIOLATION_UAT_ILLEGAL_CONTINUE_FW_UNMAP
000012bf  VIOLATION_UAT_ILLEGAL_ACTIVE_CTX_ID
000012e3  VIOLATION_UAT_ILLEGAL_MAP_OPTION
00001304  VIOLATION_UAT_ILLEGAL_HW_FW_PERMS
00001326  VIOLATION_UAT_INVALID_MICROPPL_MAGIC_VALUE
00001351  VIOLATION_UAT_SAPT_REVOKE_PAGE_WAS_PERM_NA
0000137c  VIOLATION_UAT_SAPT_REVOKE_FRAME_HELD_SHARED
000013a8  VIOLATION_UAT_SAPT_INVALID_REFCNT
000013ca  %s: FTE %p should be held exclusive by sptm_retype()
000013ff  perform_gmmu_tlbi_if_needed
0000141b  %s: Only CPU pages may need a GMMU TLBI on retype
0000144d  %s: Failed to verify TLBI
00001467  uat_sync_outer_tlb_sapt_flush
00001485  %s: error %d looking up %s
000014a0  uat_get_dt_prop
000014b0  %s: %s is not %zu bytes wide (%d)
000014d2  iommu-mapper,gfx
000014e3  sptm_uat_init_state
000014fd  sanitize_integer(ttbr1_root_table_paddr_U.UNSAFE_VALUE)
00001535  %s: Non-zero root table paddr in state object %p %#llx
0000156c  sptm_uat_destroy_state
00001583  state_object
00001590  ttbr0_root_table_paddr
000015a7  ttbr0_refcnt
000015b4  ttbr1_root_table_paddr
000015cb  ttbr1_refcnt
000015d8  state_object->context_id
000015f1  sptm_uat_map_table
0000160f  prev_refcnt
0000161b  sptm_uat_unmap_table
00001630  %s: Parent page table has a zero refcnt
00001658  child_pt_paddr
00001667  %s: Corrupted map_data, current segment greater than number of segments %p %zu %zu
000016ba  sptm_uat_map_continue
000016d0  %s: Invalid cur_seg_offset %zu %zu
000016f3  sptm_uat_prepare_fw_unmap_begin
00001729  uat_instance->handoff_region->micro_magic
00001753  total_size
0000175e  sptm_uat_prepare_fw_unmap_continue
00001781  sanitize_integer(state_object_handle_U.UNSAFE_VALUE)
000017b6  %s: Corrupted prepare_fw_unmap_data, cur_mapping greater than num_mappings %p %zu %zu
00001812  flush->flush_state
00001825  sptm_uat_unmap_begin
0000183a  %s: Context ID not set despite cache flush maybe being needed
00001878  sptm_uat_unmap_continue
00001890  uat_instance->handoff_region->powered_off
000018ba  sptm_uat_set_ctx_id
000018ce  (&uat_instance->ttbat_lock)
000018ea  ttba0_entry
000018f6  ttba1_entry
00001902  sptm_uat_remove_ctx_id
00001919  flush_state
00001925  %s: Valid context ID but the TTBAT already contains invalid entries %p %d
0000196f  %s(%s:%d) - paddr(%#llx), fte(%p), fte->type(%s)
000019a1  sptm_uat_revoke_sapt_multipage
000019c0  %s(%s:%d) - paddr(%#llx), fte->type(%s)
000019e9  old_perm
000019f2  sptm_uat_get_info
00001a04  uat_instance->mode
00001a17  %s: Could not get devicetree
00001a34  uat_is_enabled
00001a43  /arm-io/sgx
00001a4f  %s: The /chosen devicetree node should always exist
00001a83  gpu-iouat
00001a8d  %s: The `gpu-iouat` property should be %lu bytes not %d
00001ac5  %s: new type not XNU_IOMMU
00001ae0  uat_retype_in
00001aee  retype_params.type
00001b01  %s: retyping from XNU_IOMMU but not to XNU_DEFAULT %s
00001b37  uat_retype_out
00001b4b  %s: UAT Dekker lock acquisition timed out after %llu ns (spun for %llu cycles)
00001b9a  uat_dekkerlock_lock
00001bae  %s: UAT Dekker gate acquisition timed out after %llu ns (spun for %llu cycles)
00001bfd  uat_dekker_gate_lock
00001c12  UAT Global
00001c1d  %s: uat_instance is NULL
00001c36  uat_bootstrap_parse_dt
00001c4d  %s: error %d looking up /arm-io/sgx
00001c71  agx-address-space-mgmt-mode
00001c8d  issue-gmmu-tlbis-at-retype
00001ca8  verify-gmmu-tlbis-at-sync
00001cc2  gmmu-tlbi-verification-reg
00001cdd  %s: verify-gmmu-tlbis-at-sync is enabled but gmmu-tlbi-verification-reg is not set
00001d30  %s: The GMMU TLBI verification register should be 8B-aligned
00001d6d  gmmu-tlbi-verification-bit
00001d88  %s: gmmu-tlbi-verification-bit (%llu) is unset or out of range [0, 63]
00001dcf  gfx-shared-region-base
00001de6  gfx-shared-region-size
00001dfd  %s: The ASC carveout region is smaller than a page in size or not a multiple of the SPTM_PAGE_SIZE %llu
00001e65  gfx-shared-l2-region-base
00001e7f  gfx-shared-l2-region-size
00001e99  %s: The TTBR1 shared L2 region size (0x%llx) is not equal to the SPTM_PAGE_SIZE
00001ee9  gpu-region-base
00001ef9  gpu-region-size
00001f09  %s: The TTBAT is smaller than a page in size or not a multiple of the SPTM_PAGE_SIZE %llu
00001f63  gfx-handoff-base
00001f74  gfx-handoff-size
00001f85  %s: The Handoff region is smaller than a page in size or not a multiple of the SPTM_PAGE_SIZE %llu
00001fe8  %s: error %d looking up /defaults
0000200a  uat-enforce-gpu-carveout
00002023  %s: uat-enforce-gpu-carveout is not %zu bytes wide (%d)
0000205b  uat-vaddr-size
0000206a  %s: uat-vaddr-size is %zu bytes wide (%d)
00002094  %s: Invalid vaddr size specified in device tree (%d). Valid values are %d to %d inclusive
000020ee  uat-segment-limit
00002100  uat-mapping-limit
0000211b  -shared-ro
00002126  -shared-rw
00002131  %s-data%s-base
00002140  %s: The %s data%s segment base(%#llx) is not page-aligned
0000217a  uat_register_gfx_data_segment
00002198  %s-data%s-size
000021a7  %s: The %s data%s segment size(%#llx) is not a multiple of the page size
000021f0  uat_atomically_change_subtype
0000220e  uat_page_paddr
0000221d  old_subtype
00002229  new_subtype
00002235  uat_state_get_root_table_paddr
00002254  %s: %d is not a valid UAT state object type when getting TTBR%d
00002294  uat_state_set_root_table_paddr
000022b3  uat_walk_tables
000022c3  root_table_paddr
000022d4  %s: Invalid UAT mode found %llu
000022f4  uat_get_table_ttep
00002307  %s: Invalid page table level specified %#llx %u.
00002338  uat_vaddr_tt_index
0000234b  %s: Attempted a TLB flush on a TTBR%d address but UAT state object type %d has no TTBR%d
000023a4  issue_tlbi_by_addr
000023b7  %s: Copying segments into %p will overflow the state object page %zu
000023fc  uat_copy_segments_locally
00002416  uat_validate_map_segment
0000242f  segment
00002437  segment->start_paddr
0000244c  segment->num_mappings
00002462  seg_size
0000246b  last_paddr
00002476  uat_map_segment
00002486  cur_vaddr
0000249b  cur_paddr
000024a5  uat_instance->ttbat_region.paddr
000024c6  hw_fw_perms_to_dprr_index
000024e0  fw_write
000024e9  fw_read
000024f1  hw_write
000024fa  hw_read
00002502  lut_index
0000250c  %s: Corrupted unmap_data, current segment greater than number of segments %p %zu %zu
00002561  uuc_segment_walker
00002574  uat_validate_unmap_segment
0000258f  segment->start_vaddr
000025a4  uuc_unmap_pte_update
000025b9  %s: Provided CTXID %d does not fit in the ASID field
000025ee  tlbi_info_for_tlbi_asid
00002606  %s: Attempted a TLB Invalidate by ASID on a UAT state object with type %d
00002650  issue_tlbi_by_asid
00002663  %s: invalid context ID %p %u
00002680  %s: Execution Modes cannot be supported by more than one domain
000026c0  populate_execution_modes
000026d9  %s: Invalid Execution Mode permissions for type %s
0000270c  populate_overlay_indices
00002725  %s: Invalid permissions found for the PAPT mapping (type_id = %d)
00002767  AAPL,phandle
00002774  configure_late_apple_regs
0000278e  die-id
00002795  %s: unsupported entry, bind: %d
000027b5  sptm_fixup
000027c0  %s: unsupported auth_rebase key %d
000027e4  %s: fixup ptr format is unsupported %d
0000280b  SPTMDebug
00002815  %s: AMCC [%p-%p] and ACC [%p-%p] CTRR-C regions don't match
00002851  init_pre_late_io_reservation
0000286e  %s: AMCC [%p-%p] and ACC [%p-%p] CTRR-D regions don't match
000028aa  BootKC-rs
000028b4  AuxKC-ro
000028bd  AuxKC-rx
000028c6  sptm_register_cpu
000028d8  sptm_init.c
000028e4  physical_id
000028f0  sptm_n_cpus
000028fe  %s: CPU not found in the device tree %p
00002926  %s: Error looking up image region
00002948  sptm_slide_region
0000295a  target_papt_start
0000296c  %s: Number of supported PAPT ranges has been exhausted
000029a3  sptm_cpu_id
000029af  sptm_output_area
000029c0  %s: Logical ID for cpu %p (%d) does not match array index %d
00002a01  %s: Scratch page not configured for cpu %p (ID %d)
00002a34  random-seed
00002a40  cl4-entropy
00002a4c  %s: Not enough SK entropy
00002a66  sptm_init
00002a70  SPTM-rw
00002a78  TXM-bx
00002a7f  TXM-rw
00002a86  TXM-le
00002a8d  BootKC-bx
00002a97  BootKC-rw
00002aa1  BootKC-le
00002aab  AuxKC-rw
00002ab4  AuxKC-le
00002abd  TrustCache
00002ae4  CL4-dummypage
00002af2  RAMDisk
00002afa  RTBuddySeg
00002b0b  SEPPatches
00002b16  uStuff
00002b1d  preoslog
00002b40  ExclaveOSTrustCache
00002b54  PHYS_SLIDE
00002b5f  MTE_TAG_STORAGE
00002b75  CL4-entry
00002b7f  CL4-virt
00002b88  TXM-entry
00002b92  TXM-virt
00002b9b  BootKC-entry
00002ba8  BootKC-virt
00002bb4  exclaves-enabled
00002bc5  POE2 is disabled.
00002bd8  Starting SK...
00002be7  Starting TXM...
00002bf7  SK bootstrap complete.
00002c0f  %s: TXM not yet fixed up
00002c28  sptm_init_txm_bootstrap_complete
00002c49  TXM bootstrap complete.
00002c62  Bootstrapping XNU...
00002c78  %s: Too many handoff pages!
00002c94  sptm_resume_cpu
00002ca4  %s: DT memory-map is NULL
00002cbe  init_get_image_region
00002cd4  %s: error %d looking up image region '%s'
00002cfe  %s: error %d looking up chosen/memory-map
00002d28  init_dt
00002d30  validate_papt_address_range
00002d4c  base_addr
00002d56  copy_and_clear_random_seed
00002d71  %s: Error looking up /chosen/%s
00002d91  %s: random-seed (%p) size mismatch (%d) or NULL
00002dc1  kernel-ctrr-to-be-enabled
00002ddb  %s: unexpected size %xu for bool property 'kernel-ctrr-to-be-enabled'
00002e21  sptm_determine_kernel_ctrr
00002e3c  %s: BootKC rs region does not fit xnu_ro_data (needed: %zu, have: %zu)
00002e83  init_xnu_ro_data
00002e94  %s: xnu ro pagetables don't begin on page boundary
00002ec7  %s: xnu ro pagetables don't end on page boundary
00002ef8  %s: %s not fully within BootKC ro region
00002f21  xnu_el2_exception_vector
00002f3a  xnu_exc_return_handler
00002f51  xnu_ctrr_dispatch_table
00002f69  xnu_ro_pagetables_begin
00002f81  xnu_ro_pagetables_end - 1
00002f9b  internal-isa-vm-allowed
00002fb3  /chosen/asmb
00002fc0  lp-sip0
00002fc8  %s: unexpected size %u for property '%s'
00002ff1  sptm_allow_vm_isa_internal_guests
00003013  internal-use-only-unit
0000302a  sptm_is_iuou_or_iuos_device
00003046  /chosen/manifest-properties
00003067  %s: init_get_image_region returned NULL for a non-optional region
000030a9  validate_region_order
000030bf  %s: region '%s' beginning [%p] or end [%p] is invalid
000030f5  %s: region '%s' [%p-%p] not immediately after region '%s' [ending at %p]
0000313e  sptm_init_mte_boundaries
00003157  %s: TagOffset_EL2 mismatch, expected: %p, actual: %p
0000318c  %s: TagOffset_EL2 (%p) not locked
000031ae  SPTM_CPUTRACE_ENDPOINTID_IS_MODE
000031cf  SPTM_CPUTRACE_ENDPOINTID_PA_CRV_ADDR
000031f4  SPTM_CPUTRACE_ENDPOINTID_PA_CRV_SIZE
00003219  SPTM_CPUTRACE_ENDPOINTID_PA_SET_BASE
0000323e  SPTM_CPUTRACE_ENDPOINTID_PA_START
00003260  SPTM_CPUTRACE_ENDPOINTID_PA_STOP
00003281  SPTM_CPUTRACE_ENDPOINTID_VA_FRM_LOCK
000032a6  SPTM_CPUTRACE_ENDPOINTID_VA_FRM_UNLOCK
000032cd  SPTM_CPUTRACE_ENDPOINTID_VA_INIT
000032ee  SPTM_CPUTRACE_ENDPOINTID_VA_DEINIT
00003311  SPTM_CPUTRACE_ENDPOINTID_VA_SET_BASE
00003336  SPTM_CPUTRACE_ENDPOINTID_VA_START
00003358  SPTM_CPUTRACE_ENDPOINTID_VA_STOP
00003379  CPUTRACE
00003382  VIOLATION_CPUTRACE_MODE_MISMATCH
000033a3  VIOLATION_CPUTRACE_STRM_BASE
000033c0  VIOLATION_CPUTRACE_PA_BUFFER
000033dd  VIOLATION_CPUTRACE_VA_REGION
000033fa  VIOLATION_CPUTRACE_VA_FRAME
00003416  VIOLATION_CPUTRACE_VA_BUFFER
00003433  VIOLATION_CPUTRACE_VA_TYPE
0000344e  VIOLATION_CPUTRACE_VA_UNMAPPED
0000346d  VIOLATION_CPUTRACE_VA_RACE
00003488  VIOLATION_CPUTRACE_VA_INITIALIZED
000034aa  VIOLATION_CPUTRACE_VA_DEINITIALIZED
000034ce  %s: clusters not deinitialized before hibernating.
00003501  sptm_cputrace_hib_wake
00003518  %s: cluster not deinitialized before hibernating.
0000354a  sptm_cputrace_set_base
00003561  cputrace.c
0000356c  cputrace_mode_bits()
00003581  sptm_cputrace_start
00003595  sptm_cputrace_stop
000035a8  sptm_cputrace_va_frame_lock
000035c4  (&cputrace_instance->va_guard)
000035e3  cputrace_instance->initialized_count
00003608  sptm_cputrace_va_frame_unlock
00003626  va_region_id
00003633  frame_vaddr
0000363f  sptm_cputrace_va_init
00003655  cputrace_get_cluster_id()
0000366f  %s: assert '!__builtin_add_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed.
000036ec  sptm_cputrace_va_deinit
00003704  %s: assert '!__builtin_sub_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed.
00003781  sptm_cputrace_va_set_base
0000379b  sptm_cputrace_va_start
000037b2  sptm_cputrace_va_stop
000037c8  %s: carveout_nb_frames %#llx %#llx does not fit in an unsigned int.
0000380c  cputrace_bootstrap
0000381f  cputrace_get_carveout_size_mib
0000383e  apt-carveout-size-mb
00003853  cputrace_va_locked_frame_lock
00003871  frame_paddr
0000387d  new_frame_paddr
0000388d  cputrace_va_locked_region_add
000038ab  %s: assert '(!region_start) == (!region_size)' failed.
000038e2  %s: assert '!(region_start & SPTM_PAGE_MASK)' failed.
00003918  %s: assert '!(region_size & SPTM_PAGE_MASK)' failed.
0000394d  %s: assert '!__builtin_add_overflow(region_start, region_size, &region_end)' failed.
000039a2  region_start
000039af  region_size
000039bb  %s: assert '!__builtin_add_overflow(region_size, SPTM_PAGE_SIZE, &region_size)' failed.
00003a13  cputrace_va_locked_region_remove
00003a34  %s: assert 'region_size >= SPTM_PAGE_SIZE' failed.
00003a67  cputrace_va_locked_frame_unlock
00003a87  %s: assert 'cluster_id < CPUTRACE_NB_CLUSTERS' failed.
00003abe  cputrace_get_cluster_id
00003ad6  %s: CPUTrace : condition (cputrace_tlbi_is_done()) timed out after ONE_MS_TIMEOUT nanoseconds.
00003b35  cputrace_va_locked_trace_init
00003b53  cputrace_va_locked_trace_deinit
00003b73  %s: CPUTrace : condition (cputrace_prefetch_is_done()) timed out after ONE_MS_TIMEOUT nanoseconds.
00003bd6  %s: Error getting SecureDT
00003bf1  hib_bootstrap_determine_support
00003c11  /hibernate
00003c1c  %s: Number of hibernation segments passed by iBoot is larger than NUM_HIBSEGINFO_SEGMENTS %zu
00003c7a  %s: address (%#llx) or size (%zu) of iBoot loaded range is not page aligned
00003cc6  hib_bootstrap_register_iboot_loaded_range
00003cf0  %s: Reached the maximum number of iBoot loaded ranges %d (%#llx %zu)
00003d35  chosen/hibernation
00003d48  /Library/Caches/com.apple.xbs/E6EECBFA-A35F-4C31-99B3-BA4E76C73F65/TemporaryDirectory.TftW7z/Sources/SPTM/sptm/core/sptm_hibentry.c
00003dcc  chosen/hibernation node not found in DT for key
00003dfc  key has unexpected size
00003e14  key property found but key is NULL
00003e37  key not found in DT
00003e4b  key is all-zero
00003e5b  %s: %s:%u: %s (%#llx/%s)
00003e74  hib_sptm_panic_func
00003e88  SPTM-ro
00003e90  SPTM-rm
00003e98  SPTM-le
00003ea0  BootKC-ro
00003eaa  TXM-ro
00003eb1  %s: Error looking up /hibernate
00003ed1  hib_bootstrap_cold
00003ee4  %s: Error looking up /hibernate/hmac-reg-base
00003f12  %s: hmac-reg-base (%p) size mismatch (%d) or NULL
00003f44  /chosen/hibernation
00003f58  key-exclave-entropy
00003f6c  %s: dt /chosen/hibernation/key-exclave-entropy length mismatch (%zu != %zu)
00003fb8  %s: SK_HIB_patchup() returned error (%llu)
00003fe3  hib_bootstrap_patchup
00003ff9  %s: SPTM HIB: Seed and Keys for key0 haven't been programmed yet
0000403a  compute_hardware_hmac
00004050  %s: SPTM HIB: Error occurred while hashing data, IRQ: %#x
0000408a  sptm_hib_begin
00004099  sptm_hibentry.c
000040a9  is_hib_supported()
000040bc  interrupts_enabled()
000040d1  %s(%s:%d) - scratch_io_buffer_pages[%d](%#llx), fte(%p), fte->type(%s)
00004119  %s: Hibernation is supported, but there's no hibernation segments. That shouldn't be possible.
00004178  %s: SK_HIB_start() returned error (%llu)
000041a1  %s: Invalid current hibseg %zu
000041c0  sptm_hib_hash_hibseg_page
000041da  %s: The current hibseg page is out of the bounds of the hibernation segment %d %d %d
0000422f  %s: Found non-DRAM hibernation segment page %#llx
00004261  %s: attempting to hibernate immutable page %p
0000428f  sptm_hib_hash_page
000042a2  %s: SK_HIB_finish() returned error (%llu)
000042cc  sptm_hib_finalize_sk
000042e1  %s: Finalizing the image but the SHA context is not set correctly %d.
00004327  sptm_hib_finalize_image
0000433f  sptm_hib_verify_hash_non_wired_page
00004363  %s: Somehow we're in the verify non-wired mem state, but the SHA context isn't correct %d
000043bd  sptm_hib_verify_finalize_non_wired_hash
000043e5  %s: region marked as both needing hibernation and forbidden for write during hib restore: addr %p, size %zu, wimg %#x
0000445b  parse_hibernate_io_ranges
00004475  %s: Attempted to register more than %d pmap-io-ranges as needing hibernating. The MAX_HIB_IO_RANGES limit probably needs increasing.
000044fa  %s: Attempted to register a managed memory region as an IO range that needs to be hibernated %p %p
0000455d  %s: Attempted to register an unaligned IO range that needs to be hibernated %p %p
000045af  %s: %p length is greater than the maximum allowed for a 32-bit integer (%llu)
000045fd  hib_init_sha_context
00004612  %s: Unexpected current SHA context type %d %d
00004640  hib_acquire_state
00004652  &hib_state.current_state
0000466b  HIB_STATE_LOCKED
0000467c  hib_release_state
0000468e  %s: MTE tag page containing SK tags is mapped %#lx
000046c1  hib_copy_and_hash_page
000046d8  %s: Found SK-owned memory in non-wired memory
00004706  %s: SK_HIB_encrypt(0x%llu) returned error (%llu)
00004737  hib_mark_page_as_hibernated
00004753  old_flags
0000475d  validate_page
0000476b  hib_enforce_required_mem_was_hibernated
00004793  was_hibernated
000047a2  iboot_loaded_range
000047bd  range->first_page
000047cf  range->page_count
000047e1  last_page
000047eb  range->next_page_to_hash
00004804  CTXR-A
0000480b  CTXR-B
00004812  CTXR-C
00004819  CTXR-D
00004820  ACC-CTRR-C
0000482b  ACC-CTRR-D
00004836  ACC-CTXR-A
00004841  ACC-CTXR-B
0000484c  ACC-CTXR-C
00004857  ACC-CTXR-D
00004862  %s: CTRR-A per-core register not locked by iBoot (expected: %llx, got: %llx)
000048af  ctXr_check_all_regions
000048c6  %s: CTRR-B per-core register not locked by iBoot (expected: %llx, got: %llx)
00004913  %s: CTRR-A per-cluster register not locked by iBoot (expected: %llx, got: %llx)
00004963  %s: CTRR-B per-cluster register not locked by iBoot (expected: %llx, got: %llx)
000049b3  %s: CTRR-C already locked! %#llx
000049d4  ctrr_lock_sptm
000049e3  %s: CTRR-D already locked! %#llx
00004a04  %s: %s begin invalid: %#llx
00004a20  validate_ctXr_region_bounds
00004a3c  %s: %s end invalid: %#llx
00004a56  %s: CTRR-%s begin > end: %#llx > %#llx
00004a7d  %s: %s configuration not as expected: actual %#llx != expected %#llx
00004ac2  ctrr_ctxr_check_region
00004ad9  %s: %s core region bounds [%p %p] mismatch stashed regions [%p %p]
00004b1c  SPTM_NVME_ENDPOINTID_ENABLE_CG
00004b3b  SPTM_NVME_ENDPOINTID_MAP_PAGES
00004b5a  SPTM_NVME_ENDPOINTID_UNMAP_PAGES
00004b7b  SPTM_NVME_ENDPOINTID_INIT
00004b95  SPTM_NVME_ENDPOINTID_ADMIN_QUEUE_REGS
00004bbb  SPTM_NVME_ENDPOINTID_IOQA_REG
00004bd9  SPTM_NVME_ENDPOINTID_IOSQ_REG
00004bf7  SPTM_NVME_ENDPOINTID_IOCQ_REG
00004c15  SPTM_NVME_ENDPOINTID_SHA_REG
00004c32  SPTM_NVME_ENDPOINTID_SET_SQ_ENTRY
00004c59  VIOLATION_NVME_INVALID_QID
00004c74  VIOLATION_NVME_INVALID_CID
00004c8f  VIOLATION_NVME_INVALID_QTAIL
00004cac  VIOLATION_NVME_INVALID_PAGE_COUNT
00004cce  VIOLATION_NVME_INVALID_NVME_PAGE
00004cef  VIOLATION_NVME_INVALID_NLB
00004d0a  VIOLATION_NVME_ILLEGAL_CALL
00004d26  VIOLATION_NVME_ILLEGAL_CID_STATE_TRANSITION
00004d52  VIOLATION_NVME_ILLEGAL_QTAIL_STATE_TRANSITION
00004d80  VIOLATION_NVME_ILLEGAL_FUNC_CALL_STATE
00004da7  VIOLATION_NVME_ILLEGAL_QUEUE_ADDRESS
00004dcc  VIOLATION_NVME_ILLEGAL_QUEUE_LENGTH
00004df0  VIOLATION_NVME_ILLEGAL_NVMe_QUEUEING_PROTOCOL_VERSION
00004e26  VIOLATION_NVME_ILLEGAL_NVMe_QUEUE_ENTRIES_MISMATCH
00004e59  VIOLATION_NVME_ILLEGAL_ANS_SHA_ADDRESS
00004e80  VIOLATION_NVME_ILLEGAL_ANS_SHA_PACKED_WRITES_CONFIG
00004eb4  VIOLATION_NVME_ILLEGAL_ANS_SHA_BUFFER_SIZE
00004edf  VIOLATION_NVME_ILLEGAL_SEG_COUNT
00004f00  VIOLATION_NVME_ILLEGAL_HIBERNATION_QUEUE_LATCH
00004f2f  %s: Zero TCB entries per queue is not supported
00004f5f  nvme_bootstrap
00004f6e  %s: Too many TCB entries per queue:%u
00004f94  %s: iommu_bootstrap_alloc_frames() returns 0
00004fc1  sptm_nvme_map_pages
00004fd5  nvme.c
00004fdc  &nvme_instance->cid_mode[c_id]
00004ffb  CID_EMPTY
00005005  CID_BUSY
0000500e  %s: TCB entry %d is not invalidated in DRAM for qid %d cid %d
0000504c  %s: TCB entry: %d NLB is not zero
0000506e  %s: Both WR bits are set !
00005089  seg_cnt
00005091  template->NLB
0000509f  sptm_nvme_unmap_pages
000050b5  (nvme_cid_mode_t)(((uint8_t)(q_id) << 4) | CID_FILLED_q)
000050ee  (nvme_cid_mode_t)(((uint8_t)(q_id) << 4) | CID_FILLED_RETRY_q)
0000512d  %s: SET_SQ_ENTRY called in linear queueing mode
0000515d  sptm_nvme_set_sq_entry
00005174  (nvme_cid_mode_t)(((uint8_t)(q_id) << 4) | CID_SHADOW_q)
000051ad  &nvme_instance->qtail_state[q_id][q_tail]
000051d7  QTAIL_LIVE
000051e2  QTAIL_BUSY
000051ed  %s: CID %u already mapped to slotID %u
00005214  sptm_nvme_bar_admin_queue_regs
00005233  &nvme_instance->func_state[4]
00005251  FUNC_CALLABLE
0000525f  FUNC_BUSY
00005269  %s: AQA doesnt match the previously cached value !
0000529c  sptm_nvme_bar_ioqa_reg
000052b3  &nvme_instance->func_state[5]
000052d1  %s: IOQA doesnt match the previously cached value !
00005305  sptm_nvme_bar_iosq_reg
0000531c  &nvme_instance->func_state[6]
0000533a  sptm_nvme_bar_iocq_reg
00005351  &nvme_instance->func_state[7]
0000536f  %s: ANS SHA flag was not set
0000538c  sptm_nvme_ans_sha_reg
000053a2  &nvme_instance->func_state[8]
000053c0  validate_nvme_call_allowed
000053e0  nvme_instance->allowed_functions
00005401  %s: Could not find /defaults
0000541e  read_edt_properties
00005432  nvme-iboot-sptm-security
0000544f  %s: Could not find /arm-io/ans
0000546e  nvme-secure-bar
0000547e  nvme-secure-reg-layout
00005495  nvme-linear-sq
000054a4  nvme-prp-flush-wa
000054b6  nvme-queue-entries
000054c9  %s: Couldn't find nvme-queue-entries
000054ee  nvme-tl-wa
000054f9  nvme-vdma-wa
00005506  %s: Could not find /arm-io/ans.reg
00005529  %s: /arm-io/ans.reg bad size
00005546  %s: Unexpected ANS register size
00005567  nvme-num-sl
00005573  %s: Could not find nvme-num-sl
00005592  nvme-ans-sha-present
000055a7  chosen/carveout-memory-map
000055c2  region-id-%d
000055cf  %s: Unexpected size of region id %d
000055f3  validate_qid
00005600  nvme_validation.h
00005616  validate_cid
00005627  validate_nvme_page
0000563a  %s: f2h and h2f bits are set !
00005659  invalidate_tcb_entry
0000566e  %s: ANS invalidation failed with state: %u
00005699  validate_qtail
000056ae  validate_nvme_queue_entries
000056ca  queue_entries
000056d8  validate_nvme_protocol_version
000056f7  protocol_version
00005708  validate_nvme_queue_len
00005720  nvme_queue_len
0000572f  validate_nvme_queue_addr
00005748  nvme_queue_addr
00005758  validate_nvme_sha_buffer_size
00005776  nvme_ans_sha_buffer_size
0000578f  validate_nvme_sha_base_addr
000057ab  nvme_ans_sha_addr
000057bd  validated_nvme_ans_sha_addr
000057d9  enforce_no_hib_latch
000057ee  validate_nvme_sha_packed_write_config
00005814  packed_writes_config
00005829  /chosen/lock-regs
0000583b  %s: /chosen/lock-regs not found
0000585b  ctrr_amcc_find_lock_group_data
0000587f  amcc-ctrr-a
0000588b  amcc-ctrr-b
00005897  amcc-ctrr-c
000058a3  amcc-ctrr-d
000058af  assert_ctrr_group_region_unlocked
000058d1  %s: lock group %u %s region has been locked unexpectedly (write_disabled=%d locked=%d)
00005928  assert_amcc_cache_disabled
00005943  %s: AMCC cache enabled unexpectedly: lock_group=%u aperture=%u plane=%u addr=%#llx read=%#x masked=%#x expected=%#x
000059b7  %s: Malformed %s memory region %p %p
000059dc  ctrr_map_lock_group
000059f0  ctrr_stash_group_regions
00005a09  %s: region %s page size does not agree, shift count: %u
00005a41  %s: /chosen/lock-regs/%s not found
00005a64  ctrr_dt_get_lock_group
00005a7b  aperture-count
00005a8a  %s: %s %s %u exceeds maximum %u
00005aaa  aperture-size
00005ab8  %s: %s have %u apertures, but 0 size
00005add  plane-count
00005ae9  plane-stride
00005af6  %s: %s plane-count (%u) > 1, but stride is 0/missing
00005b2b  %s: %s aperture-size (%#x) is insufficent to cover plane-count (%#x) of plane-stride (%#x) bytes
00005b8c  aperture-phys-addr
00005b9f  %s: %s missing required %s
00005bba  %s: %s aperture-phys-addr size (%#x) != (aperture-count (%#x) * PA size (%#zx) = %#lx)
00005c11  cache-status
00005c1e  %s: Could not find required property '%s'
00005c48  ctrr_dt_get_uint32
00005c5b  %s: Found unexpected size for property %s %u
00005c88  %s-reg-offset
00005c96  %s-reg-mask
00005ca2  %s-reg-value
00005caf  %s: /chosen/lock-regs/%s/%s not found
00005cd5  ctrr_dt_get_lock_type
00005ceb  page-size-shift
00005cfb  lower-limit
00005d07  upper-limit
00005d18  enable
00005d1f  write-disable
00005d2d  CTRR-A
00005d34  CTRR-B
00005d3b  CTRR-C
00005d42  CTRR-D
00005d49  %s: /chosen/lock-regs not found (your iBoot or EDT may be too old)
00005d8c  ctrr_dt_get_memcache_enable_status
00005daf  early-memcache-enable
00005dc5  ctrr_dt_get_force_flush_offset
00005de4  force-flush-offset
00005df7  ctrr_set_mc_hint_in_cpm
00005e0f  mc-hint-cpm-impl-offset
00005e27  mc-hint-cpm-impl-mask
00005e3d  mc-hint-cpm-impl-val
00005e52  ctrr_dt_get_uint64
00005e65  acquire_uat_state_object
00005e7e  uat_validation.c
00005e8f  state_object_handle
00005ea3  offset
00005eaa  uat_instance->state_object_size
00005eca  *iommu_frame_tsd(state_object_handle)
00005ef0  state_object->type
00005f03  allowed_types
00005f11  &state_object->current_state
00005f2e  expected_state
00005f3d  UAT_STATE_LOCKED
00005f4e  release_uat_state_object
00005f67  acquire_uat_translation_table
00005f85  *iommu_frame_tsd(pt_paddr)
00005fa0  expected_subtype
00005fb1  validate_uat_table_descriptor_level
00005fd5  validate_uat_vaddr_range
00005fee  ttbr_index
00005ff9  _range_start
00006006  _range_size
00006012  validate_uat_context_id
0000602a  context_id
00006035  validate_uat_get_info_type
00006050  info_type
0000605a  acquire_uat_segments_page
00006074  segments_page
00006082  validate_uat_segment_number
0000609e  num_segments
000060ab  validate_uat_map_options
000060c4  map_options
000060d0  %s: Accessing Shared Mode global data outside Shared Mode
0000610a  uat_shared_mode_global_data
00006126  %s: Accessing Private Mode global data outside Private Mode
00006162  uat_private_mode_global_data
0000617f  uat_validate_paddr
00006192  uat_utils.h
000061cb  SPTM PANIC:
000061d7  PANIC_BUF_SIZE(%u) and CONSISTENT_DEBUG_PANIC_LEN(%zu) is less than panic_string_buf size(%d)
0000623a  TRUNCATED ORIGINAL PANIC:
00006256  SPTM PANIC:
00006263  [SPTM]: somehow a violation was triggered in early boot. That shouldn't be possible, %s: %s
000062bf  [SPTM] %s: %s
000062cd  dart_check_restrictions
000062e5  dart_common.c
000062f3  metadata->iommu_id
0000630c  metadata->dva_base
0000631f  range_base_paddr
00006330  device_type
0000633c  dart-mapper
00006348  %s: SID missing or invalid size for dart-mapper
00006378  dart_register_iommu_restriction
00006398  %s: SID %x out of range
000063b0  %s: dart-id missing or invalid size for dart-mapper
000063e4  %s: DART id %x out of range
00006400  %s: dart is missing the "compatible" property for dart-mapper
0000643e  dart,gen3
00006448  dart,t8020
00006453  dart,t6000
0000645e  %s: Unable to set up DART restriction for unsupported DART type "%s"
000064a3  dart_compatible_to_iommu_id
000064bf  SPTM_SART_SET_STATE
000064d3  SPTM_SART_MAP_REGION
000064e8  SPTM_SART_UNMAP_REGION
00006504  VIOLATION_SART_INVALID_PT
0000651e  VIOLATION_SART_INVALID_PADDR
0000653b  VIOLATION_SART_INVALID_N_OPS
00006558  VIOLATION_SART_INVALID_SIZE
00006574  VIOLATION_SART_INVALID_PERM
00006590  VIOLATION_SART_INVALID_OPTIONS
000065af  VIOLATION_SART_ILLEGAL_STATE
000065cc  VIOLATION_SART_NO_SPACE
000065e4  VIOLATION_SART_ILLEGAL_MAP
000065ff  VIOLATION_SART_ILLEGAL_UNMAP
0000661c  VIOLATION_SART_CPU_RACE
00006634  VIOLATION_SART_INVALID_CONFIG
00006652  VIOLATION_SART_POWER
00006667  VIOLATION_SART_INVALID_STATE
00006684  sptm_sart_unmap_region
0000669b  sart.c
000066a2  %s: Invalid SART version %d from EDT
000066c7  sart_bootstrap
000066d6  %s: error %d looking up '%s'
000066f3  sart_bootstrap_parse_edt
0000670c  arm-io/sart-ans
0000671c  %s: error %d looking up '%s' - SPTM/EDT misconfiguration
00006755  sart-version
00006762  sart-ans/sart-version
00006778  %s: DT property '%s' has illegal size %zu
000067a2  sart-throttle-version
000067b8  sart-ans/sart-throttle-version
000067d7  sart-throttle-offset
000067ec  sart-ans/sart-throttle-offset
0000680a  sart-throttle-disable
00006820  power-canary-offset
00006834  sart-ans/regs
00006842  %s: Illegal SART Register Size %d
00006864  sart-ans/power-canary-offset
00006881  exclusive-bounds
00006892  validate_sart_address_range
000068ae  sart_validation.h
000068c0  validate_size
000068ce  maximum
000068d6  enforce_paddr_managed
000068ec  sptm_internal.h
000068fc  validate_sart_mapping_perms
00006918  sart_instance->iommu_instance.iommu_id
00006945  validate_sart_mapping_options
00006963  sart_instance_acquire
00006979  (&sart_instance->mtx_guard)
00006995  %s: overflow
000069a2  sart_assert_power_canary
000069bb  sart_add_region
000069cb  region_id
000069d5  %s: n_region overflow
000069eb  sart_instance_release
00006a01  %s: Invalid SART size region %d
00006a21  sart_get_registers
00006a34  %s: Invalid SART offset %x
00006a4f  sart_read_reg
00006a5d  %s: n_region underflow
00006a74  sart_remove_region_cache
00006a8d  %s: Invalid Region ID %d
00006aa6  sart_remove_region_hw
00006abc  %s: could not zero sart region
00006adb  sart_write_reg
00006aea  %s: power canary underflow
00006b05  sart_deassert_power_canary
00006b20  sart_instance->powerCanaryRefCnt
00006b41  validate_sart_state
00006b55  %s: Invalid bootloader mapping covers managed memory %llx
00006b8f  sart_bootstrap_register_bootloader_mappings
00006bbb  %s: Sart invalid throttle regs.
00006bdb  sart_sanity_check_throttles
00006bf7  %s: Sart invalid throttle cfg [%d] = 0x%x
00006c21  sart_set_registers
00006c39  SPTM-exception
00006c4c  BootKC-exception
00006c61  TXM-exception
00006c6f  EXEC_MODE_SPTM_DEFAULT
00006c86  EXEC_MODE_SK_DEFAULT
00006c9b  EXEC_MODE_TXM_DEFAULT
00006cb1  EXEC_MODE_XNU_DEFAULT
00006cc7  EXEC_MODE_XNU_ROZONE_RW
00006cdf  EXEC_MODE_XNU_USER_DEFAULT
00006cfa  EXEC_MODE_XNU_USER_JIT_RW
00006d14  EXEC_MODE_XNU_USER_TPRO_RW
00006d2f  SPTM_T8110_DART_MAP_TABLE
00006d49  SPTM_T8110_DART_UNMAP_TABLE
00006d65  SPTM_T8110_DART_MAP
00006d79  SPTM_T8110_DART_UNMAP
00006d8f  SPTM_T8110_DART_POWERDOWN
00006da9  SPTM_T8110_DART_POWERUP
00006dc1  SPTM_T8110_DART_INIT
00006dd6  SPTM_T8110_DART_DISABLE_TRANSLATION
00006dfa  SPTM_T8110_DART_ENABLE_TRANSLATION
00006e1d  SPTM_T8110_DART_CLEAR_ERR
00006e37  SPTM_T8110_DART_CLEAR_PERF_INTERRUPTS
00006e5d  SPTM_T8110_DART_CLEAR_ALL_INTERRUPTS
00006e82  SPTM_T8110_DART_QUERY_TLB
00006e9c  SPTM_T8110_DART_SET_SMMU_WINDOW
00006ebc  SPTM_T8110_DART_READ_SMMU_STT_INDEX
00006ee0  SPTM_T8110_DART_CLAMP_TLIMITS
00006efe  SPTM_T8110_DART_CLEAR_EXCEPTION
00006f1e  SPTM_T8110_DART_DISABLE_ALL_INTERRUPTS
00006f45  SPTM_T8110_DART_SK_TLBI_REQUEST
00006f65  SPTM_T8110_DART_SK_TLBI_BARRIER
00006f85  SPTM_T8110_DART_SK_POWER_ASSERT
00006fa5  SPTM_T8110_DART_SK_POWER_RELEASE
00006fc6  t8110dart
00006fd0  VIOLATION_T8110_DART_RACE
00006fea  VIOLATION_T8110_DART_SID_RACE
00007008  VIOLATION_T8110_DART_INVALID_RETYPE_NEW_TYPE
00007035  VIOLATION_T8110_DART_INVALID_LEVEL
00007058  VIOLATION_T8110_DART_INVALID_RETYPE_LEVEL
00007082  VIOLATION_T8110_DART_INVALID_TSD_LEVEL
000070a9  VIOLATION_T8110_DART_INVALID_DART_ID
000070ce  VIOLATION_T8110_DART_INVALID_RETYPE_DART_ID
000070fa  VIOLATION_T8110_DART_INVALID_TSD_DART_ID
00007123  VIOLATION_T8110_DART_INVALID_SID
00007144  VIOLATION_T8110_DART_INVALID_RETYPE_SID
0000716c  VIOLATION_T8110_DART_INVALID_TSD_SID
00007191  VIOLATION_T8110_DART_INVALID_NBYTES
000071b5  VIOLATION_T8110_DART_INVALID_MAP_OPTION
000071dd  VIOLATION_T8110_DART_INVALID_DVA
000071fe  VIOLATION_T8110_DART_INVALID_DVA_END
00007223  VIOLATION_T8110_DART_INVALID_FTE_TYPE
00007249  VIOLATION_T8110_DART_INVALID_TARGET_LEVEL_TTE
00007277  VIOLATION_T8110_DART_INVALID_INTERMEDIATE_LEVEL_TTE
000072ab  VIOLATION_T8110_DART_INVALID_PTE_REMAP
000072d2  VIOLATION_T8110_DART_PROT_MISMATCH
000072f5  VIOLATION_T8110_DART_INVALID_DART_INSTANCE
00007320  VIOLATION_T8110_DART_INVALID_POWER_STATE
00007349  VIOLATION_T8110_DART_INVALID_ERR_MASK
0000736f  VIOLATION_T8110_DART_INVALID_HARDWARE_VERSION
0000739d  VIOLATION_T8110_DART_INVALID_SMMU_WINDOW
000073c6  VIOLATION_T8110_DART_INVALID_STT_DEPTH
000073ed  VIOLATION_T8110_DART_INVALID_STT_INDEX
00007414  VIOLATION_T8110_DART_FREE_TABLE_IN_USE
0000743b  VIOLATION_T8110_DART_UNPERMITTED_TLIMIT_CLAMP
00007469  VIOLATION_T8110_DART_MULTIPLE_MAP_TABLE
00007491  VIOLATION_T8110_DART_SID_ACCESS_DENIED
000074b8  VIOLATION_T8110_DART_INVALID_SK_POLLER
000074df  VIOLATION_T8110_DART_INVALID_ADDRESS
00007504  VIOLATION_T8110_DART_INVALID_PTE
00007525  VIOLATION_T8110_DART_INVALID_MAPPING
0000754a  VIOLATION_T8110_DART_INVALID_UNMAP
0000756d  VIOLATION_T8110_DART_INVALID_TLB_OP_INDEX
00007597  VIOLATION_T8110_DART_PS_WR_DIS_RACE
000075bb  VIOLATION_T8110_DART_SID_TRANSLATION_DISABLED
000075e9  VIOLATION_T8110_DART_UNGANG_GAPF_RACE
0000760f  /Library/Caches/com.apple.xbs/E6EECBFA-A35F-4C31-99B3-BA4E76C73F65/TemporaryDirectory.TftW7z/Sources/SPTM/sptm/iommu/dart/t8110dart.c
00007695  %s(%s:%d) - new_type(%s)
000076af  t8110dart_retype_in
000076c3  t8110dart.c
000076cf  dart_id
000076db  %s: dart %s:%s:%d: %s == NULL
000076f9  outargsp
00007702  %s: dart %s:%s:%d: alloc size must be greater than 0
00007737  t8110dart_bootstrap_allocate
00007754  %s: dart %s:%s:%d: allocation requests must not have a size greater than one page (%#llx)
000077ae  t8110dart_bootstrap_tz
000077d4  inclusive-tz-range
000077e7  %s: dart %p (%s:%u): TZ select greater than max
00007817  %s: dart %p (%s:%u): TZ config greater than max
00007847  %s: dart %p (%s:%u): Disabled TZT region %u invalid %#x %#x %#x
00007887  %s: dart %p (%s:%u): Enabled TZT region %u invalid %#x %#x %#x
000078c6  t8110dart_bootstrap_sid
000078de  %s: dart %p (%s:%u): SID %u is greater than the maximum
00007916  %s: dart %p (%s:%u): SID 0 is invalid with Dynamic SID Assignment
00007958  apf-bypass
00007963  %s: dart %p (%s:%u): APF bypass and Dynamic SIDs are mutually exclusive
000079ab  %s: dart %p (%s:%u): overflow
000079c9  vm-base
000079d1  %s: dart %p (%s:%u): vm-base-%u must be of size %zu
00007a05  vm-size
00007a0d  %s: dart %p (%s:%u): vm-size-%u must be of size %zu
00007a41  %s: dart %p (%s:%u): %hu: Per-SID vm-base/vm-size override not supported for this class of DART
00007aa1  %s: dart %p (%s:%u): SID %u: per-sid vm-base/vm-size override unsupported for Dynamic SID Assignment
00007b06  %s: dart %p (%s:%u): Per-SID (%u) vm-base/vm-size override may increase VM limits
00007b58  %s: dart %p (%s:%u): Per-SID (%u) vm-size must be within global range
00007b9e  %s: dart %p (%s:%u): SID %u end page %llu is greater than maximum
00007be0  bypass
00007be7  %s: dart %p (%s:%u): Invalid SID (%u) configured as bypass
00007c22  %s: dart %p (%s:%u): SID %u: remap and bypass are mutually exclusive 
00007c68  %s: dart %p (%s:%u): SID %u: remap and translation are mutually exclusive 
00007cb3  pt-region
00007cbd  %s: dart %p (%s:%u): pt-region-%d incorrectly sized
00007cf1  %s: dart %p (%s:%u): SID %u: page table carveout not page-aligned
00007d33  %s: dart %p (%s:%u): SID %u: page table carveout size not page-aligned
00007d7a  %s: dart %p (%s:%u): carveout pages %zu must be < %u
00007daf  %s: dart %p (%s:%u): %s: invalid papt returned by iommu_bootstrap_register_io_range
00007e03  real-time
00007e0d  %s: dart %p (%s:%u): Cannot specify Per-SID (%u) realtime with global realtime
00007e5c  t8110dart_bootstrap_sids
00007e75  sid-count
00007e7f  %s: dart %p (%s:%u): sid-count %u is greater than max permitted sids %u
00007ec7  sid-trace
00007ed1  sid-mcw
00007ed9  sid-ocla
00007ee2  sid-lft
00007eea  ignore-sid-count-mismatch
00007f04  max-sids-in-mismatch
00007f1f  %s: dart %p (%s:%u): SID Remap incompatible with Dynamic SID Assignment
00007f67  %s: dart %p (%s:%u): Malformed 'remap' property
00007f97  %s: dart %p (%s:%u): remap %u -> %u is greater than max SID %u
00007fd6  %s: dart %p (%s:%u): Remap src SID %u already remapped to %u
00008013  %s: dart %p (%s:%u): Remap dst SID %u already remapped to %u
00008050  %s: dart %p (%s:%u): SID %u: SID remapped to itself: %#x
00008089  exclave-sids-only
0000809b  %s: dart %p (%s:%u): missing %s property
000080c4  %s: dart %p (%s:%u): sid count %u greater than maximum
000080fb  %s: dart %p (%s:%u): SID count (%u) must be greater than 0
00008136  %s: dart %p (%s:%u): malformed %s property
00008161  %s: dart %p (%s:%u): mismatch between 'sid-count' (%u) and 'sid' (%u) property length
000081b7  exclave-sid
000081c3  %s: dart %p (%s:%u): exclave sid count %u greater than maximum
00008202  %s: dart %p (%s:%u): SID %u: Not initialized
0000822f  %s: dart %p (%s:%u): SID remap %u->%u invalid target
00008264  %s: dart %s:%s:%d: error getting SecureDT
0000828e  t8110dart_bootstrap
000082a2  %s: dart %s:%s:%d: error %d looking up %s
000082cc  debug-enabled
000082da  %s: dart %s:%s:%d: unexpected size for 'debug-enabled'
00008311  dart-clock-protection
00008327  dart-ps-wr-dis-entries
0000833e  %s: dart %s:%s:%d: unexpected size for 'dart-ps-wr-dis-entries'
0000837e  dart-clock-gapf-ungang-count
0000839b  %s: dart %s:%s:%d: unexpected size for 'dart-clock-gapf-ungang-count'
000083e1  dart-gapf-sr-region
000083f5  %s: dart %s:%s:%d: unexpected size for 'dart-gapf-sr-region'
00008432  dart-clock-gapf-ungang-entries
00008451  %s: dart %s:%s:%d: unexpected size for 'dart-clock-gapf-ungang-entries'
00008499  compatible
000084a4  dart,t8110
000084af  sptm_t8110dart_map_table
000084c8  state->power_state
000084db  (&state->sids[sid]->lock)
000084f7  _mga_lock
00008505  pt_paddr
0000850e  tte->raw
00008517  %s: state_guard_release - %#llx, %#llx
0000853e  sptm_t8110dart_unmap_table
00008559  ttes[level]->raw
0000856a  nested_level
00008577  refcnt
0000857e  sptm_t8110dart_map
00008591  nbytes
00008598  %s: dart %p (%s:%u): The scratch size requested must be <= T8110_DART_PAGE_SIZE
000085e8  cur_dva
000085f0  physaddr
000085f9  pte->raw
00008602  new_pte.raw
0000860e  pte->wrprot
0000861a  unregister_wrprot
0000862c  sptm_t8110dart_unmap
00008641  phys_addr
0000864b  sptm_t8110dart_init
0000865f  (&state->lock)
0000866e  sptm_t8110dart_powerup
00008685  sptm_t8110dart_powerdown
0000869e  %s: dart %p (%s:%u): power down not permitted as SK still using the DART
000086e7  sptm_t8110dart_query_tlb
00008700  sptm_t8110dart_set_smmu_window
0000871f  sptm_t8110dart_read_smmu_stt_index
00008742  sptm_t8110dart_clamp_tlimits
0000875f  sptm_t8110dart_clear_err
00008778  instance
00008781  %s: dart %p (%s:%u): DART instance %u: Unrecoverable secondary error 0x%08x
000087cd  sptm_t8110dart_clear_exception
000087ec  sptm_t8110dart_disable_translation
0000880f  sptm_t8110dart_enable_translation
00008831  t8110dart_read_dart_reg
00008849  %s: dart %p (%s:%u): Invalid DART instance %u
00008877  t8110dart_read_smmu_reg
0000888f  %s: dart %p (%s:%u): Invalid SMMU instance %u
000088bd  t8110dart_read_dapf_reg
000088d5  %s: dart %p (%s:%u): Invalid DAPF instance %u
00008903  t8110dart_read_gapf_reg
0000891b  %s: dart %p (%s:%u): Invalid GAPF instance %u
00008949  state->gapfs[instance].register_base
0000896e  t8110dart_write_dart_reg
00008987  t8110dart_write_smmu_reg
000089a0  t8110dart_write_dapf_reg
000089b9  t8110dart_write_gapf_reg
000089d2  gen3_write_dart_tlbi_cmd_payload
000089f3  gen3_dart_tlbi_aperture_base
00008a10  %s: dart %p (%s:%u): DART instance %u: Attempt to modify locked reg at offset %x 0x%08x->0x%08x
00008a70  t8110dart_verify_dapf_reg
00008a8a  t8110dart_verify_dart_reg
00008aa4  t8110dart_sid_is_valid
00008abb  t8110dart_sid_is_valid_apf_remap
00008adc  t8110dart_addr_to_te_phy
00008afa  t8110dart_addr_to_page
00008b11  sptm_t8110dart_sk_tlbi_request
00008b30  dart_assert_prop_size
00008b4b  %s: dart %s:%s:%d: state %p (%s:%u): expected size %u for '%s', but it is %u
00008b98  t8110dart_new_sid
00008baa  %s: dart %p (%s:%u): invalid SID %u
00008bce  %s: dart %p (%s:%u): SID %u already allocated
00008bfc  t8110dart_get_sid_property
00008c1d  %s: dart %s:%s:%d: invalid %s size %u
00008c43  t8110dart_validate_carveout_table
00008c65  %s: dart %p (%s:%u): SID %u level %hhu table PA %#llx falls outside carveout region
00008cb9  %s: dart %p (%s:%u): SID %u TZ Dead Page only permitted in 3 level translation STEs
00008d0d  %s: dart %p (%s:%u): SID %u dead page must be zero
00008d40  %s: dart %p (%s:%u): SID %u TZ Dead Page not in TZ REGION at STE %zu
00008d85  %s: dart %p (%s:%u): SID %u leaf page table flags present in level %hhu page table entry %#zx: 0x%016llx
00008dee  t8110dart_carveout_phys_to_papt
00008e0e  %s: dart %p (%s:%u): Unable to convert secure carveout physical address %llx to a PAPT
00008e65  %s: dart %p (%s:%u): Number of %s props (%u) is greater than max permitted sids (%u)
00008eba  t8110dart_bootstrap_preconfig_exception_sid
00008ee6  %s: dart %p (%s:%u): %s (%u) must be less than sid-count (%u)
00008f24  gen3_map_tlbi_aperture
00008f3b  %s: dart %s:%s:%d: Expected gen3_dart_tlbi_aperture_base == NULL
00008f7c  arm-io/dart-tlbi-aperture
00008f96  %s: dart %s:%s:%d: incorrect size for 'reg'
00008fc2  %s: dart %s:%s:%d: mis-aligned TLBI Aperture base %#llx
00008ffa  %s: dart %s:%s:%d: mis-aligned TLBI Aperture size %#llx
00009032  %s: dart %s:%s:%d: invalid papt returned by iommu_bootstrap_register_io_range
00009080  t8110dart_bootstrap_instance
0000909d  dart-id
000090a5  %s: dart %s:%s:%d: error %d getting dart-id
000090d1  %s: dart %s:%s:%d: expected size %zu for '%s', but it is %u
0000910d  %s: dart %s:%s:%d: error %d invalid DART ID: %u
0000913d  %s: dart %s:%s:%d: DART ID %u used twice
00009166  %s: dart %s:%s:%d: error %d getting name
0000918f  dart-sep
00009198  txm-secure-channel-base
000091b0  txm-secure-channel-size
000091c8  allow-vm-reserve-mapping
000091e1  vm-reserve
000091ec  %s: dart %p (%s:%u): Start of the VM reserve space must be less than the end.
0000923a  dart-options
00009247  retention
00009251  no-sleep
0000925a  %s: dart %p (%s:%u): %s and %s are mutually exclusive
00009290  enable-perf-counters
000092a5  ioa-parent
000092b0  allow-mixed-bypass-mode
000092c8  flush-by-dva
000092d5  avoid-tlbi-in-map
000092e7  noncompliant-dead-mappings
00009302  clamp-tlimits
00009310  %s: dart %p (%s:%u): vm-size must be non-zero, but it is %#llx
0000934f  %s: dart %p (%s:%u): invalid vm-size %#llx
0000937a  %s: dart %p (%s:%u): vm-base %#llx is greater than the maximum DVA %#llx
000093c3  %s: dart %p (%s:%u): vm-size %#llx is less than the maximum size %#llx
0000940a  %s: dart %p (%s:%u): end of vm range %#llx is greater than the maximum DVA %#llx
0000945b  vm-alignment
00009468  %s: dart %p (%s:%u): invalid size %u for vm-alignment
0000949e  %s: dart %p (%s:%u): invalid vm_alignment
000094c8  ignore-secondary
000094d9  allow-apf-sid-remap
000094ed  relaxed-rw-protections
00009504  t8110dart_bootstrap_dart_instances
00009527  %s: dart %p (%s:%u): malformed 'instances' property
0000955b  %s: dart %p (%s:%u): invalid 'instance' size %u
0000958b  %s: dart %p (%s:%u): max %s instances exceeded
000095d4  PSWRDIS
000095dc  %s: dart %p (%s:%u): invalid instance type: 0x%08x
0000960f  %s: dart %p (%s:%u): missing '%s' property
0000963a  %s: dart %p (%s:%u): incorrect size for 'reg'
00009668  %s: dart %p (%s:%u): 'instance'/'reg' property count mismatch
000096a6  %s: dart %p (%s:%u): mis-aligned DART register size %#llx
000096e0  t8110dart_bootstrap_dart_instance_properties
0000970d  %s: dart %p (%s:%u): mis-aligned DART register base %#llx
00009747  dart-tunables-instance-%d
00009761  %s: dart %p (%s:%u): Malformed dart-tunables-instance-%u
0000979a  tlbi-aperture-offset
000097af  %s: dart %p (%s:%u): incorrect size for 'tlbi-aperture-offset'
000097ee  t8110dart_validate_tunable
00009809  tunable
00009811  %s: dart %p (%s:%u): DART instance %u: invalid tunable offset %#x
00009853  %s: dart %p (%s:%u): Invalid DART instance (%u) for SMMU instance (%u)
0000989a  t8110dart_bootstrap_smmu_instance_properties
000098c7  %s: dart %p (%s:%u): smmu instance %u 'reg' not page sized
00009902  %s: dart %p (%s:%u): mis-aligned SMMU register base %#llx
0000993c  allow-pte-remap
0000994c  %s: dart %p (%s:%u): PTE remap not permitted
00009979  pte-remap-carveout-only
00009991  %s: dart %p (%s:%u): PTE remap from carveout is present but remap itself isn't allowed
000099e8  %s: dart %p (%s:%u): relaxed_rw_protections and allow_pte_remap are not supported together
00009a43  %s: dart %p (%s:%u): unexpected dram base
00009a6d  t8110dart_bootstrap_dapf_instance_properties
00009a9a  %s: dart %p (%s:%u): APF is incompatible with Dynamic SID Assignment
00009adf  dual-vc-llt-workaround-%d
00009af9  %s: dart %p (%s:%u): Multiple instances using dual vc limits
00009b36  %s: dart %p (%s:%u): invalid dual-vc-llt-workaround size
00009b6f  %s: dart %p (%s:%u): num_dual_vc_limits %u exceed maximum %u
00009bac  %s: dart %p (%s:%u): dual VC LLT limit %d is invalid: [%#llx,%#llx]
00009bf0  dapf-instance-%d
00009c01  %s: dart %p (%s:%u): malformed dapf-instance-%u
00009c31  %s: dart %p (%s:%u): dapf-instance-%d must have at least one slice
00009c74  %s: dart %p (%s:%u): number of apf slices %u greater than max %u
00009cb5  %s: dart %p (%s:%u): Invalid DART instance (%u) for APF instance (%u)
00009cfb  %s: dart %p (%s:%u): apf instance %u 'reg' not page sized
00009d35  %s: dart %p (%s:%u): mis-aligned APF register base %#llx
00009d6e  allow-dram-apf-slices-%d
00009d87  %s: dart %p (%s:%u): malformed allow-dram-apf-slices-%d
00009dbf  %s: dart %p (%s:%u): allow-dram-apf-slices-%d must have at least one slice
00009e0a  %s: dart %p (%s:%u): allow-dram-apf-slices-%d[%zu] = %u can not index dapf-instance-%d length %u
00009e6b  %s: dart %p (%s:%u): end(%#llx) < start(%#llx) for slice %d instance %u
00009eb3  %s: dart %p (%s:%u): APF slice %u instance %u is in managed DRAM: [%#llx, %#llx]
00009f04  %s: dart %p (%s:%u): APF slice %u instance %u can not have both dual-vc-llt-workaround and alllow-dram-apf-slices properties
00009f81  %s: dart %p (%s:%u): Invalid limits for APF slice %u instance %u: [%#llx,%#llx]
00009fd1  %s: dart %p (%s:%u): APF slice %d instance %u has DRAM permissions and is not in DRAM: [%#llx,%#llx]
0000a036  %s: dart %p (%s:%u): PS write disable: %s GAPF configuration
0000a073  t8110dart_bootstrap_gapf_instance_properties
0000a0a0  Inconsistent
0000a0ad  %s: dart %p (%s:%u): %s clock protection configuration
0000a0e4  dart-ungang-shared-ps
0000a0fa  clock-protection-slice-index
0000a117  %s: dart %p (%s:%u): GAPF instance %u 'reg' not page sized
0000a152  %s: dart %p (%s:%u): mis-aligned GAPF register base %#llx
0000a18c  %s: dart %p (%s:%u): Invalid GAPF_CFG: %#x
0000a1b7  %s: dart %p (%s:%u): Invalid GAPF_LOCK: %#x
0000a1e3  %s: dart %p (%s:%u): Invalid '%s': %#x
0000a20a  %s: dart %p (%s:%u): Invalid '%s': %#x max %x
0000a238  GAPF slice ctrl
0000a248  %s: dart %p (%s:%u): Invalid slice address range: %#x..%x
0000a282  Missing
0000a28a  %s: dart %p (%s:%u): '%s' property not permitted
0000a2bb  piogw-ps-protection
0000a2cf  %s: dart %p (%s:%u): Invalid 'piogw_ps_protection' size (%d)
0000a30c  t8110dart_bootstrap_piogw_instance_properties
0000a33a  %s: dart %p (%s:%u): Invalid PIOGW slice (%d) or address (%#llx)
0000a37b  clock-protection-wr-dis-id
0000a396  t8110dart_bootstrap_ps_wr_dis_instance_properties
0000a3c8  clock-protection-dart-state
0000a3e4  validate_t8110dart_dart_id
0000a3ff  t8110dart_validation.h
0000a416  validate_t8110dart_sid
0000a42d  state->dart_id
0000a43c  validate_t8110dart_dva
0000a453  validate_t8110dart_target_level
0000a473  t8110dart_update_ttbr
0000a489  %s: dart %p (%s:%u): (DART instance %u): Locked register update: 0x%08x -> 0x%08x
0000a4db  %s: dart %p (%s:%u): (DART instance %u): Failed to write TTBR for SID %d
0000a524  %s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x
0000a57e  t8110dart_verify_sid_config
0000a59a  %s: dart %p (%s:%u): (DART instance %u): Inconsistent write disable set and lock 0x%08x
0000a5f2  t8110dart_dart_regs_are_locked
0000a611  t8110dart_invalidate_tlb
0000a62a  t8110dart_invalidate_tlb_by_dva
0000a64a  %s: dart %p (%s:%u): Invalid flush-by-DVA range [%#llx,%#llx]
0000a688  t8110dart_invalidate_tlb_by_sid
0000a6a8  validate_t8110dart_map_options
0000a6c7  validate_t8110dart_map_nbytes
0000a6e5  t8110dart_walk_tables
0000a6fb  %s: dart %p (%s:%u): table_pa==0
0000a71c  %s: dart %p (%s:%u): table==0
0000a73a  validate_t8110dart_unmap_options
0000a75b  t8110dart_init_instance
0000a773  %s: dart %p (%s:%u): DART instance %u: Unsupported hardware version %u.%u
0000a7bd  %s: dart %p (%s:%u): DART instance %u: hardware version mismatch %u.%u
0000a804  %s: dart %p (%s:%u): DART instance %u: max_pa %#llx doesn't match with the rest %#llx
0000a85a  %s: dart %p (%s:%u): DART instance %u: Incorrect max_pa %#llx
0000a898  %s: dart %p (%s:%u): flush-by-dva not supported
0000a8c8  %s: dart %p (%s:%u): Non-compliant dead page mapping not supported
0000a90b  %s: dart %p (%s:%u): DART instance %u: Inconsistent hardware definition: min_page %#llx hw %#x
0000a96a  %s: dart %p (%s:%u): DART instance %u: HW reported num_sids %u exceeds T8110_DART_MAX_SIDS %u
0000a9c8  %s: dart %p (%s:%u): DART instance %u: Max SID is %u
0000a9fd  %s: dart %p (%s:%u): DART instance %u: max_sid %#x doesn't match with the rest %#x
0000aa50  %s: dart %p (%s:%u): DART instance %u: Invalid VM page limits [%#x,%#x)
0000aa98  %s: dart %p (%s:%u): DART instance %u: invalid SID %u
0000aace  %s: dart %p (%s:%u): DART instance %u: invalid SID %u full bypass addr %#llx
0000ab1b  %s: dart %p (%s:%u): DART instance %d: invalid SID %u legacy bypass addr 0x%llx
0000ab6b  %s: dart %p (%s:%u): DART instance %u: SID %u translation disabled
0000abae  %s: dart %p (%s:%u): DART instance %u: SID %u page limits not set [%#llx..%#llx)
0000abff  %s: dart %p (%s:%u): DART instance %u: SID %u page limits [%#llx..%#llx) outside required limits [%#llx..%#llx)
0000ac6f  %s: dart %p (%s:%u): DART instance %u: 4-level translation not supported for SID %u
0000acc3  %s: dart %p (%s:%u): DART instance %u: SID %u: 3-level translation with noncompliant dead mappings and flush-by-DVA is unsupported on pre-Gen3 DARTs
0000ad58  %s: dart %p (%s:%u): DART instance %u uses dual-vc-llt-workaround, but has no APF
0000adaa  %s: dart %p (%s:%u): DART instance %u: Too many APF slices, max %u configured %u
0000adfb  %s: dart %p (%s:%u): DART instance %u: Invalid APF slice %u range [%#llx,%#llx]
0000ae4b  %s: dart %p (%s:%u): DART instance %u: APF slice %u uses invalid SID %u
0000ae93  %s: dart %p (%s:%u): DART instance %u: DART not locked
0000aeca  t8110dart_verify_sid_preconfiguration
0000aef0  %s: dart %p (%s:%u): DART instance %u: Unconfigured SID %u differs from reset value: 0x%08x
0000af4c  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent remap_enable configuration: actual %#x expected %#x
0000afbb  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent remap configuration: actual %#x expected %#x
0000b023  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent remap ttbr configuration: actual %#llx expected %#x
0000b092  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent translation_enable configuration: actual %#x expected %#x
0000b107  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent ttbr configuration: actual %#llx expected %#llx
0000b172  %s: dart %p (%s:%u): DART instance %u: SID %u unexpected ttbr valid with bypass: actual ttbr %#llx expected %#llx
0000b1e4  %s: dart %p (%s:%u): DART instance %u: SID %u unexpected non-zero TTBR for full bypass %#llx
0000b241  %s: dart %p (%s:%u): DART instance %u: SID %u unexpected zero TTBR for legacy bypass %#llx
0000b29c  %s: dart %p (%s:%u): DART instance %u: SID %u inconsistent APF bypass configuration: actual %#x expected %#x
0000b309  t8110dart_verify_bypass
0000b321  %s: dart %p (%s:%u): DART instance %u SID %u invalid translation setting
0000b36a  %s: dart %p (%s:%u): DART instance %u: APF not locked
0000b3a0  t8110dart_verify_dapf_preconfiguration
0000b3c7  t8110dart_read_piogw_reg
0000b3e0  %s: dart %p (%s:%u): Invalid PIOGW instance %u
0000b40f  state->piogws[instance].register_base
0000b435  t8110dart_write_piogw_reg
0000b44f  %s: dart %p (%s:%u): Client partitions not supported
0000b484  t8110dart_powerup_instance
0000b49f  %s: dart %p (%s:%u): DART instance %u: Locked register update SID_CONFIG[%u] 0x%08x->0x%08x
0000b4fb  %s: dart %p (%s:%u): DART instance %u: TTBR must be invalid for remapped SID(%u)
0000b54c  %s: dart %p (%s:%u): DART instance %u: Locked register update TTBR[%u] 0x%08x->0x%08x
0000b5a2  %s: dart %p (%s:%u): Inconsistent clock protection configuration
0000b5e3  sptm_t8110dart_enable_clock_protection
0000b60a  (&dart_gapf_ungang_map[state->gapf_ungang_map_index].lock)
0000b645  slice_index
0000b651  %s: dart %p (%s:%u): Inconsistent %s GAPF filter slice control: %#x
0000b695  power up
0000b69e  %s: dart %p (%s:%u): Inconsistent power %s GAPF slice_ctrl: %#x
0000b6e1  t8110dart_ps_wr_dis_increment_refcount
0000b708  (&ps_wr_dis_lock)
0000b71a  dart_ps_wr_dis_map
0000b72d  %s: dart %s:%s:%d: Invalid ps wr_dis id
0000b755  %s: dart %s:%s:%d: ps refcount overflow
0000b77d  t8110dart_set_ps_wr_dis
0000b795  %s: dart %s:%s:%d: Failed to set WR_DIS bit
0000b7c1  %s: dart %s:%s:%d: Failed to clear WR_DIS bit
0000b7ef  %s: dart %p (%s:%u): Inconsistent unganged clock protection configuration
0000b839  sptm_t8110dart_skip_enable_clock_protection_write
0000b86b  %s: dart %p (%s:%u): Inconsistent unganged clock protection counter
0000b8af  %s: dart %p (%s:%u): instance %u WRITE_DISABLE_LOCK unlocked expected 0x%08x actual 0x%08x
0000b90a  t8110dart_verify_tz_tagger
0000b925  %s: dart %p (%s:%u): instance %u WRITE_DISABLE enabled expected 0x%08x actual 0x%08x
0000b97a  %s: dart %p (%s:%u): instance %u %s changed expected 0x%08x actual 0x%08x
0000b9c4  (TZ_SELECT)
0000b9d0  (TZ_CONFIG)
0000b9dc  (TZ_REGION0_START)
0000b9ef  (TZ_REGION0_END)
0000ba00  (TZ_REGION0_OFFSET)
0000ba14  (TZ_REGION1_START)
0000ba27  (TZ_REGION1_END)
0000ba38  (TZ_REGION1_OFFSET)
0000ba4c  (TZ_REGION2_START)
0000ba5f  (TZ_REGION2_END)
0000ba70  (TZ_REGION2_OFFSET)
0000ba84  %s: dart %p (%s:%u): TZ Dead Page is not supported for hw version: %#hx
0000bacc  %s: dart %p (%s:%u): TZ Dead Page must be zero with build_params2.trustzone_tagger_supported
0000bb29  sptm_t8110dart_disable_clock_protection
0000bb56  t8110dart_ps_wr_dis_decrement_refcount
0000bb7d  %s: dart %s:%s:%d: ps refcount underflow
0000bba6  sptm_t8110dart_skip_disable_clock_protection_write
0000bbd9  validate_t8110dart_dart_instance
0000bbfa  validate_t8110dart_tlb_op_index
0000bc25  validate_t8110dart_smmu_instance
0000bc46  validate_t8110dart_smmu_window
0000bc65  window
0000bc6c  validate_t8110dart_smmu_stt_index
0000bc94  t8110dart_poll
0000bcaf  %s: dart %p (%s:%u): Invalid poller type %d
0000bcdb  %s: dart %p (%s:%u): Invalid poller type: %u
0000bd08  %s: dart %p (%s:%u): DART instance %u: %s still busy after %zu polls, OP=%#x
0000bd55  validate_t8110dart_err_mask
0000bd71  err_mask
0000bd7a  %s: dart %p (%s:%u): Flush Unlock not supported
0000bdaa  t8110dart_tlb_flush_unlock
0000bdc5  t8110dart_clear_all_interrupts_instance
0000bded  t8110dart_enable_translation
0000be0a  %s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x
0000be5e  t8110dart_verify_sid_shadow_config
0000be81  %s: Deferred SError detected: vaddr: %p, value: 0x%016llx_%016llx, disr: 0x%016llx
0000bed4  pio_write_synchronize_serror
0000bef1  validate_t8110dart_tlb_op
0000bf0b  start_page
0000bf16  end_page
0000bf1f  validate_t8110dart_poller
0000bf39  poller
0000bf40  %s: dart %p (%s:%u): DART CMAINT TLBI support is not enabled
0000bf7d  gen3_dart_cmaint_tlbi
0000bf93  %s: dart %p (%s:%u): Unsupported TLB operation %#x
0000bfc7  %s: dart %s:%s:%d: error, value (0x%016llx_%016llx) exceeds field width %d
0000c012  gen3_tlbi_cmd_payload_insert_field
0000c035  %s: dart %p (%s:%u): Not serialized request from %s
0000c06a  t8110dart_tlbi_request
0000c088  t8110dart_tlbi_start
0000c09d  SPTM_UNTYPED
0000c0aa  SPTM_UNUSED
0000c0b6  SPTM_DEFAULT
0000c0c3  SPTM_RO
0000c0cb  SPTM_CODE
0000c0d5  SPTM_TXM_CODE
0000c0e3  SPTM_XNU_CODE
0000c0f1  SPTM_XNU_CODE_DBG_RW
0000c106  SPTM_KERNEL_ROOT_TABLE
0000c11d  SPTM_PAGE_TABLE
0000c12d  SPTM_IOMMU_BOOTSTRAP
0000c142  XNU_DEFAULT
0000c14e  XNU_RO
0000c155  XNU_RO_DBG_RW
0000c163  XNU_USER_EXEC
0000c171  XNU_USER_DEBUG
0000c180  XNU_USER_JIT
0000c18d  XNU_USER_TPRO
0000c19b  XNU_USER_ROOT_TABLE
0000c1af  XNU_SHARED_ROOT_TABLE
0000c1c5  XNU_PAGE_TABLE
0000c1d4  XNU_PAGE_TABLE_SHARED
0000c1ea  XNU_PAGE_TABLE_ROZONE
0000c200  XNU_PAGE_TABLE_COMMPAGE
0000c218  XNU_IOMMU
0000c222  XNU_ROZONE
0000c22d  XNU_IO
0000c234  XNU_PROTECTED_IO
0000c245  XNU_COPROCESSOR_RO_IO
0000c25b  XNU_COMMPAGE_RW
0000c26b  XNU_COMMPAGE_RO
0000c27b  XNU_COMMPAGE_RX
0000c28b  XNU_TAG_STORAGE
0000c29b  XNU_STAGE2_ROOT_TABLE
0000c2b1  XNU_STAGE2_PAGE_TABLE
0000c2c7  XNU_KERNEL_RESTRICTED
0000c2dd  XNU_CPUTRACE_PA_BUFFER
0000c2f4  XNU_CPUTRACE_VA_BUFFER
0000c30b  XNU_RESTRICTED_IO
0000c31d  XNU_RESTRICTED_IO_RO
0000c332  XNU_RESTRICTED_IO_TELEMETRY
0000c34e  XNU_SUBPAGE_USER_ROOT_TABLES
0000c36b  TXM_DEFAULT
0000c377  TXM_RO
0000c37e  TXM_RW
0000c385  TXM_CPU_STACK
0000c393  TXM_THREAD_STACK
0000c3a4  TXM_ADDRESS_SPACE_TABLE
0000c3bc  TXM_MALLOC_PAGE
0000c3cc  TXM_FREE_LIST
0000c3da  TXM_SLAB_TRUST_CACHE
0000c3ef  TXM_SLAB_PROFILE
0000c400  TXM_SLAB_CODE_SIGNATURE
0000c418  TXM_SLAB_CODE_REGION
0000c42d  TXM_SLAB_ADDRESS_SPACE
0000c444  TXM_BUCKET_1024
0000c454  TXM_BUCKET_2048
0000c464  TXM_BUCKET_4096
0000c474  TXM_BUCKET_8192
0000c484  TXM_BULK_DATA
0000c492  TXM_BULK_DATA_READ_ONLY
0000c4aa  TXM_LOG
0000c4b2  TXM_SEP_SECURE_CHANNEL
0000c4c9  SK_DEFAULT
0000c4d4  SK_SHARED_RO
0000c4e1  SK_SHARED_RW
0000c4f4  SK_XNU_CONTENT
0000c503  INVALID_FRAME_TYPE
0000c516  %s: Invalid element_size/num_elements %zd %lld
0000c545  copy_array_to_scratch
0000c55b  %s(%s:%d) - array_fte(%p), array_pa(%#llx), array_fte->type(%s), in_flight_ops(%u)
0000c5af  sptm_misc.c
0000c5bb  %s(%s:%d) - array_fte->type(%s), array_pa(%#llx)
0000c5ed  array_pa
0000c5f6  element_size
0000c603  num_elements
0000c610  %s: Offset into scratch page crosses page boundary %zu %zu
0000c64b  %s: core file region name too long: %zu > %zu
0000c679  register_core_file_region
0000c693  %s: core file regions list full (max capacity %llu)
0000c6c7  %s: core file region not found: %s
0000c6ea  slide_core_file_region
0000c701  %s: core file region size overflow: %s
0000c728  adjust_core_file_region
0000c740  %s: core file region size underflow: %s
0000c768  VIOLATION_INVALID_PT
0000c77d  VIOLATION_INVALID_LEVEL
0000c795  VIOLATION_INVALID_GEOMETRY_ID
0000c7b3  VIOLATION_INVALID_IOMMU_ID
0000c7ce  VIOLATION_INVALID_ASID
0000c7e5  VIOLATION_INVALID_VMID
0000c7fc  VIOLATION_INVALID_PADDR
0000c814  VIOLATION_INVALID_VADDR
0000c82c  VIOLATION_INVALID_VADDR_RANGE
0000c84a  VIOLATION_INVALID_TYPE
0000c861  VIOLATION_INVALID_N_OPS
0000c879  VIOLATION_INVALID_ARRAY
0000c891  VIOLATION_INVALID_SHARED_RT
0000c8ad  VIOLATION_INVALID_USER_RT
0000c8c7  VIOLATION_INVALID_OPTIONS
0000c8e1  VIOLATION_INVALID_INSTANCE_ID
0000c8ff  VIOLATION_INVALID_FLAG
0000c916  VIOLATION_INVALID_CPU_PHYSICAL_ID
0000c938  VIOLATION_INVALID_CPU_LOGICAL_ID
0000c959  VIOLATION_CPU_NOT_INITIALIZED
0000c977  VIOLATION_INVALID_SIZE
0000c98e  VIOLATION_INVALID_TAG_STORAGE_FRAME
0000c9b2  VIOLATION_INVALID_PAPT_RANGE
0000c9cf  VIOLATION_INVALID_IO_FILTER_ENTRY
0000c9f1  VIOLATION_ILLEGAL_CPU_REGISTRATION
0000ca14  VIOLATION_ILLEGAL_RETYPE
0000ca2d  VIOLATION_ILLEGAL_RETYPE_PINNED
0000ca4d  VIOLATION_ILLEGAL_MAP
0000ca63  VIOLATION_ILLEGAL_NEST
0000ca7a  VIOLATION_ILLEGAL_UNNEST
0000ca93  VIOLATION_ILLEGAL_UPDATE
0000caac  VIOLATION_ILLEGAL_UNMAP
0000cac4  VIOLATION_ILLEGAL_UNMAP_PINNED
0000cae3  VIOLATION_ILLEGAL_UPGRADE
0000cafd  VIOLATION_ILLEGAL_DOWNGRADE
0000cb19  VIOLATION_ILLEGAL_UNCONDEMN
0000cb35  VIOLATION_ILLEGAL_PTE
0000cb4b  VIOLATION_ILLEGAL_TTE
0000cb61  VIOLATION_ILLEGAL_PERMS
0000cb79  VIOLATION_ILLEGAL_NG_FIELD
0000cb94  VIOLATION_ILLEGAL_PTE_WRITABLE
0000cbb3  VIOLATION_ILLEGAL_SPANS_TABLES
0000cbd2  VIOLATION_ILLEGAL_MAPPING_TYPE
0000cbf1  VIOLATION_ILLEGAL_DISPATCH_CMD
0000cc10  VIOLATION_ILLEGAL_DISPATCH_DOMAIN
0000cc32  VIOLATION_ILLEGAL_DISPATCH_TABLE
0000cc53  VIOLATION_ILLEGAL_DISPATCH_PERMISSION
0000cc79  VIOLATION_ILLEGAL_DISPATCH_ENTRY_POINT
0000cca0  VIOLATION_ILLEGAL_DISPATCH_TXM_STACK
0000ccc5  VIOLATION_ILLEGAL_SPTM_ENDPOINT
0000cce5  VIOLATION_ILLEGAL_SPTM_DISPATCH_TABLE
0000cd0b  VIOLATION_ILLEGAL_SPTM_EXC_RETURN
0000cd2d  VIOLATION_SIGN_ILLEGAL_KEY
0000cd48  VIOLATION_AUTH_ILLEGAL_KEY
0000cd63  VIOLATION_ILLEGAL_SLIDE
0000cd7b  VIOLATION_ILLEGAL_TAG_FRAME
0000cd97  VIOLATION_ILLEGAL_UNTAG_FRAME
0000cdb5  VIOLATION_ILLEGAL_TAGGED_MAPPING
0000cdd6  VIOLATION_DANGLING_PAPT_TAG
0000cdf2  VIOLATION_ILLEGAL_IOMMU_UNREGISTER
0000ce15  VIOLATION_IOMMU_RESTRICTED_IO_RANGE
0000ce39  VIOLATION_ILLEGAL_IO_RANGE_SIZE
0000ce59  VIOLATION_DOUBLE_NEST
0000ce6f  VIOLATION_MISMATCHED_PT_GEOMETRIES
0000ce92  VIOLATION_FRAME_HELD_EXCLUSIVE
0000ceb1  VIOLATION_FRAME_HELD_SHARED
0000cecd  VIOLATION_FRAME_HELD_SHARED_MULTIPLE
0000cef2  VIOLATION_FRAME_OWNER
0000cf08  VIOLATION_FRAME_PROTECTED
0000cf22  VIOLATION_FRAME_TYPE
0000cf37  VIOLATION_OVERFLOW_RO_REFCNT
0000cf54  VIOLATION_OVERFLOW_WX_REFCNT
0000cf71  VIOLATION_OVERFLOW_NESTED_REFCNT
0000cf92  VIOLATION_OVERFLOW_USER_REFCNT
0000cfb1  VIOLATION_SHARED_REGIONS_EXHAUSTED
0000cfd4  VIOLATION_SHARED_REGIONS_ALREADY_CONFIGURED
0000d000  VIOLATION_SHARED_REGIONS_MISMATCH
0000d022  VIOLATION_SHARED_REGIONS_NOT_CONFIGURED
0000d04a  VIOLATION_ASID_IN_USE
0000d060  VIOLATION_VMID_IN_USE
0000d076  VIOLATION_POSSIBLE_PENDING_TLBI
0000d096  VIOLATION_TABLE_NOT_EMPTY
0000d0b0  VIOLATION_ILLEGAL_COMMPAGE_VADDR
0000d0d1  VIOLATION_REG_ID_INVALID
0000d0ea  VIOLATION_REG_DENIED_BITS
0000d104  VIOLATION_POSSIBLE_PENDING_CACHE_FLUSH
0000d12b  VIOLATION_INCONSISTENT_PAGING_HIERARCHY
0000d153  VIOLATION_GUEST_ENTER_INTERRUPTS_ENABLED
0000d17c  VIOLATION_GUEST_INVALID_S1_TLB_OP
0000d19e  VIOLATION_GUEST_ILLEGAL_NV2_BADDR
0000d1c0  VIOLATION_ILLEGAL_HIBERNATION_CALL
0000d1e3  VIOLATION_ILLEGAL_HIBERNATION_STATE
0000d207  VIOLATION_ILLEGAL_HIBERNATION_IO_BUFFER
0000d22f  VIOLATION_ILLEGAL_HIBERNATION_PAGE
0000d252  VIOLATION_HIB_MISSING_REQUIRED_MANAGED_PAGE
0000d27e  VIOLATION_HIB_MISSING_REQUIRED_UNMANAGED_PAGE
0000d2ac  VIOLATION_ILLEGAL_VIRTUALIZATION_CALL
0000d2d2  VIOLATION_ILLEGAL_SPTM_REENTRY_CALL
0000d2f6  VIOLATION_INVALID_IOFILTER_WRITE_SIZE
0000d31c  VIOLATION_UNALIGNED_IOFILTER_WRITE_PADDR_AND_SIZE
0000d34e  VIOLATION_OUT_OF_BOUNDS_IOFILTER
0000d36f  VIOLATION_OOB_MULTIPAGE_OPS
0000d38b  VIOLATION_ILLEGAL_SPTM_SYSCTL_SELECTOR
0000d3b2  VIOLATION_ILLEGAL_SPTM_SYSCTL_OP
0000d3d3  VIOLATION_INVALID_PINNING_POLICY
0000d3f4  VIOLATION_ILLEGAL_PINNING_OPERATION
0000d418  VIOLATION_ILLEGAL_SUBPAGE_USER_ROOT_TABLE_INDEX
0000d448  VIOLATION_INVALID_SUBPAGE_USER_ROOT_TABLE_FRAME
0000d478  VIOLATION_ILLEGAL_SUBPAGE_USER_ROOT_TABLE_ALLOC
0000d4a8  VIOLATION_ILLEGAL_SUBPAGE_USER_ROOT_TABLE_FREE
0000d4d7  VIOLATION_OPERATING_ON_FREE_SUBPAGE_USER_ROOT_TABLE
0000d50b  VIOLATION_ILLEGAL_SPTM_CALL_IN_PANIC
0000d530  VIOLATION_INVALID_IO_PADDR
0000d54b  VIOLATION_INVALID_DT_RANGE
0000d566  VIOLATION_INVALID_RESTRICTED_IO_PADDR
0000d58c  %s: failed to get DT
0000d5a1  sptm_parse_io_ranges
0000d5b6  sptm_parse_io_filters
0000d5cc  sptm_iofilter_protected_write
0000d5ea  sptm_io.c
0000d5fa  pa_offset
0000d604  pa_length
0000d60e  io_filter_entry->offset
0000d626  io_filter_entry->length
0000d63e  sptm_init_parse_io_space
0000d657  DeviceTree
0000d662  %s: DeviceTree PAPT range not found.
0000d687  %s: Error while reading property %s
0000d6ab  prop_name
0000d6b5  prop_offset
0000d6c1  propSize
0000d6cd  num_pages
0000d6d7  %s: /defaults node doesn't exist in DT
0000d6fe  sptm_compute_io_ranges
0000d715  %s: Total size of pmap-io-ranges (%u) is not a multiple of pmap_io_range_t size (%zu)
0000d76b  dynamic iboot
0000d779  static edt
0000d784  %s: pmap-io-range %u (%s) has an address (0x%llx) that is not page-aligned. sig: %c%c%c%c, len: 0x%llx, wimg: 0x%x
0000d7f7  %s: pmap-io-range %u (%s) has a length (0x%llx) that is not page-aligned. sig: %c%c%c%c, addr: 0x%llx, wimg: 0x%x
0000d869  %s: pmap-io-range %u (%s) wraps around. sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx, wimg: 0x%x
0000d8c6  %s: pmap-io-range %u (%s) overlaps with managed physical memory. sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx, wimg: 0x%x
0000d93c  %s: Failed to get defaults node from EDT
0000d965  sptm_load_io_ranges
0000d979  %s: Failed to get pmap-io-ranges property from the defaults node
0000d9ba  %s: pmap-io-range (%s) sig: %c%c%c%c, addr: 0x%llx, length 0x%llx is greater than %u pages
0000da15  sptm_register_io_frame
0000da2c  %s: Number of IO ranges exhausted registering (%s) sig: %c%c%c%c, addr: 0x%llx
0000da7b  %s: Attempted to register managed page as an IO range (%s) sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx
0000dadf  %s: Attempted to register an empty IO range (%s) sig: %c%c%c%c, addr: 0x%llx
0000db2c  %s: Attempted to register unaligned IO range (%s) sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx
0000db87  %s: Attempted to register IO range (%s) sig: %c%c%c%c, addr: 0x%llx with invalid type %s
0000dbe0  %s: Number of IO pages exhausted registering (%s) sig: %c%c%c%c, addr: 0x%llx
0000dc2e  %s: sptm_pmap_io_ranges %u (%s, sig: %c%c%c%c, addr: %#llx len: %#llx) and %u (%s, sig: %c%c%c%c, addr: %#llx len: %#llx) overlap.
0000dcb1  sptm_validate_io_ranges
0000dcc9  sptm_compute_io_filters
0000dce1  pmap-io-filters
0000dcf1  %s: io filter entry %u offset 0x%hx length 0x%hx crosses page boundary
0000dd38  %s: failed to get the /defaults node from EDT
0000dd66  sptm_load_io_filters
0000dd7b  %s: failed to get the pmap-io-filters property
0000ddaa  %s: io filter entry %u and %u overlap.
0000ddd1  sptm_validate_io_filters
0000ddea  validate_sptm_io_filter_protected_write_size
0000de17  sptm_io_filter_protected_write_size
0000de3b  validate_sptm_io_filter_protected_paddr
0000de63  sptm_io_filter_protected_paddr
0000de82  sptm_find_io_filter_entry
0000de9c  io_range
0000dea5  io_range->len
0000debd  -internal-reg
0000decb  sptm_init_register_allow_io_range
0000deed  %s: Number of IO ranges exhausted
0000df0f  get_ptep
0000df18  sptm_page_tables.c
0000df2b  table_paddr
0000df37  %s: paddr isn't managed %#llx
0000df55  papt_update_mapping
0000df69  %s: invalid flag found while updating PAPT mapping %u
0000df9f  %s: Attempted to update PAPT permissions outside of a retype() operation, this is unsafe.
0000dff9  %s: invalid cache attribute index found while updating PAPT mapping %p %hhuu %hhu
0000e04b  %s: expected %#llx <= npages <= %#llx but got npages=%#llx
0000e086  generate_rtlbi_param
0000e09b  %s: invalid root table type %s for PA 0x%llx
0000e0c8  sptm_broadcast_tlbi
0000e0dc  %s: VA 0x%llx not aligned to root table page size
0000e10e  %s: unsupported full TLBI flavor 0x%x
0000e134  %s: unsupported RTLBI flavor 0x%x
0000e156  %s: unsupported TLBI flavor 0x%x
0000e177  sptm_bootstrap_tlbi
0000e18b  %s: Attempted to announce bootstrap stage that has already been reached %p %p
0000e1d9  bootstrap_stage_announce
0000e1f2  %s: Expected bootstrap stages not reached. Expected: %p, Actual: %p
0000e236  bootstrap_stage_enforce_after
0000e254  %s: Unexpected bootstrap stages reached. Expected: %p, Actual: %p
0000e296  bootstrap_stage_enforce_before
0000e2b5  SPTM Boot Pages
0000e2c5  %s: Exceeded available number of bootstrap SPTM CTRR-protected frames, dram_size=%#llx
0000e31c  bootstrap_alloc_frames
0000e333  %s: Exceeded available number of xnu CTRR-protected frames, dram_size=%#llx
0000e37f  %s: Called with [num_frames] of zero
0000e3a4  bootstrap_retype_frames
0000e3bc  %s: Attempted to retype a non-managed frame %p %u
0000e3ee  %s: Range overflow while attempting to retype frames %p %u
0000e429  %s: Invalid new type %u
0000e441  %s: wrong frame type for SPTM CTRR protected page tables: %s
0000e47e  bootstrap_expand_page_tables
0000e49b  %s: wrong frame type for page tables: %s
0000e4c4  %s: PAPT PTE could not be reached %p
0000e4e9  bootstrap_map_region
0000e4fe  %s: Valid PTE found while attempting to create mapping %p
0000e538  bootstrap_unmap_page
0000e54d  %s: Invalid PTE found while attempting to unmap page %p
0000e585  bootstrap_map_io_region
0000e59d  %s: request for %u mappings exceeds %u late I/O limit (current: %u), max needed %u, dram_size=%#llx
0000e601  %s: Attempted to unmap non-existent IO region %p %u
0000e635  bootstrap_unmap_io_region
0000e64f  %s: Name is NULL
0000e660  bootstrap_register_papt_range
0000e67e  %s: (range %s): Required PAPT range has no mappings.
0000e6b3  %s: (range %s): Invalid bootstrap type %u
0000e6dd  %s: (range %s): Attempted to go over the maximum number of PAPT ranges
0000e724  %s: (range %s): PAPT_RANGE_ALLOCATE_BACKWARD cannot coexist with other flags
0000e771  bootstrap_retype_papt_range
0000e78d  %s: attempt to bootstrap-retype via alias PAPT range %s
0000e7c5  %s: Unable to find requested range %s
0000e7eb  %s: %s PAPT range not found.
0000e808  papt_range_find
0000e818  %s: () No PAPT ranges have been registered
0000e843  papt_ranges_update
0000e856  certificate-production-status
0000e874  %s: failed to determine if device is prod-fused
0000e8a4  device_is_prod_fused_init
0000e8be  %s: () invalid virt_base: %llx
0000e8dd  sptm_bootstrap_early
0000e8f2  %s: () invalid phys_base: %llx
0000e911  %s: () invalid first_avail_phys: %llx
0000e937  %s: () invalid mem_size: %zx
0000e954  %s: () page count overflows 32 bits: %zx
0000e97d  %s: Error looking up /chosen
0000e99a  dram-base
0000e9a4  %s: Error looking up /chosen/dram-base
0000e9cb  %s: dram-base (%p) size mismatch (%d) or NULL
0000e9f9  dram-size
0000ea03  %s: Error looking up /chosen/dram-size
0000ea2a  %s: dram-size (%p) size mismatch (%d) or NULL
0000ea58  %s: sptm_first_dram is not page-aligned
0000ea80  %s: sptm_last_dram is not page-aligned
0000eaa7  %s: PAPT range is in multiple SPTM domains
0000ead2  %s: [current_contiguous] set on the first PAPT range
0000eb07  %s: Two or more PAPT ranges overlap in VA space %s
0000eb3a  %s: xnu ro pagetable page #%d is not SPTM owned, but %s
0000eb72  %s: Could not find /arm-io
0000eb8d  mapping-enforcement-mode
0000eba6  sptm_bootstrap_late
0000ebba  %s: IO Ranges %u and %u overlap
0000ebda  %s: NULL device tree
0000ebef  %s: Error looking up /defaults
0000ec0e  pmap-max-asids
0000ec1d  %s: pmap-max-asids DT property is not a 32-bit integer
0000ec54  %s: pmap-max-asids DT property is greater than 1 << 16
0000ec8b  %s: pmap-max-asids DT property is zero
0000ecb2  AVAILABLE
0000ecbc  %s: Frame has been left untyped during bootstrap %p
0000ecf0  sptm_bootstrap_finalize
0000ed08  %s: %p in alias papt range %u has mismatched physical mapping (%p != %p)
0000ed51  sptm_bootstrap_validate_alias_ranges
0000ed76  %s: %p in alias papt range %u has mismatched PTE (%#llx != %#llx)
0000edb8  %s: papt_to_phys(0) encountered.
0000edd9  papt_to_phys
0000ede6  %s: %s: No leaf table present for PAPT va %p
0000ee13  %s: No valid PAPT mapping found while traversing the page tables
0000ee54  %s: Trying to run on more CPUs than MAX_CPUS %d >= %d
0000ee8a  sptm_cpu_init
0000ee98  %s: Re-initializing already started CPU %d
0000eec3  %s: non-canonical or unaligned output address %#llx
0000eef7  cpu_temp_aperture_map
0000ef0d  cpu_temp_aperture_unmap
0000ef25  rc16_inc
0000ef34  %s: Error looking up /cpus
0000ef4f  sptm_parse_cpu_ranges
0000ef69  %s: Error obtaining CPU node
0000ef86  cpu-impl-reg
0000ef93  %s: Error looking up `cpu-impl-reg` region
0000efbe  %s: DT property has illegal size %zu
0000efe3  acc-impl-reg
0000eff0  %s: Error looking up `acc-impl-reg` region
0000f01b  cpm-impl-reg
0000f028  %s: Error looking up `cpm-impl-reg` region
0000f053  /product
0000f05c  %s: Error looking up /product
0000f07a  bootstrap_determine_virtualization_support
0000f0a5  has-virtualization
0000f0b8  %s: Type %s is not a CPU root table.
0000f0dd  cpu_root_table_fte_to_paddr
0000f0f9  %s: PA %p is not associated with a Subpage User Root Tables typed frame.
0000f142  %s: Frame %p not acquired, in_flight_ops: %hu
0000f170  %s: Type %s is not a CPU root table or XNU_SUBPAGE_USER_ROOT_TABLES.
0000f1b5  cpu_root_table_paddr_to_fte
0000f1d1  %s(%s:%d) - fte(%p), paddr(%#llx), fte->type(%s), fte->in_flight_ops(%u)
0000f21b  frame_acquire
0000f229  sptm_types.c
0000f236  frame_release
0000f244  tag_frame_acquire
0000f25a  tag_storage_fte
0000f26a  tag_storage_paddr
0000f27c  %s(%s:%d) - fte(%p), tag_storage_fte(%p), tag_storage_fte->type(%s)
0000f2c1  tag_frame_release
0000f2d3  %s: NULL ptep pointer
0000f2e9  table_acquire_if_present
0000f302  %s(%s:%d) - pt_fte(%p), pt_fte->type(%s), pt_fte->in_flight_ops(%u), vaddr(%#llx), level(%u)
0000f360  %s(%s:%d) - tte(%#llx), level(%u), pt_paddr(%#llx), vaddr(%#llx), pt_fte->type(%s), root_pt_fte->type(%s)
0000f3cb  %s: Non-PT frame found in page tables %p
0000f3f4  %s(%s:%d) - pt_fte(%p), pt_fte->type(%s), level(%u), root_pt_fte->type(%s), vaddr(%#llx)
0000f44e  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), pt_fte(%p), pt_fte->type(%s), vaddr(%#llx), level(%u)
0000f4b9  %s: XNU_PAGE_TABLE frame found while walking Shared Region page tables %p
0000f503  %s: Incorrect level set in page table FTE
0000f52d  table_release
0000f53b  %s: FTE type is not of a CPU page table
0000f563  refcounts_update_table_op
0000f57d  refcounts_update_page_op
0000f596  %s: NULL FTE with at least one valid PTE (%#llx or %#llx)
0000f5d0  %s: Attempted to update refcnts on a non-cpu-page: %s
0000f606  %s(%s:%d) - pt_fte(%p), fte(%p), fte->type(%s), prev_perms(%u), new_perms(%u)
0000f655  %s(%s:%d) - pt_fte(%p), fte(%p), fte->type(%s), old_wx_refcnt(%d)
0000f698  %s(%s:%d) - pt_fte(%p), fte(%p), fte->type(%s), old_wx_refcnt(%d), ro_refcnt(%u)
0000f6ea  %s(%s:%d) - pt_fte(%p), fte(%p), fte->type(%s), old_ro_refcnt(%d)
0000f72d  %s(%s:%d) - pt_fte(%p), fte(%p), fte->type(%s), old_ro_refcnt(%d), wx_refcnt(%u)
0000f77f  %s: Parent table FTE has not been acquired %p %s %u
0000f7b3  sptm_drop_table_refcnts
0000f7cb  %s: Child table FTE has not been acquired %p %s %u
0000f7fe  %s(%s:%d) - child_pt_fte(%p), child_pt_fte->type(%s), mapping_refcnt(%u), nested_refcnt(%u)
0000f85b  shared_region_alloc
0000f86f  %s: Shared region ID does not exist %d
0000f896  shared_region_free
0000f8a9  shared_region_configure
0000f8c1  expected_shared_region_state
0000f8de  %s: Unexpected failure while attempting to configure a shared region
0000f923  is_page_pinned
0000f932  %s: Frame expected to have been acquired shared has not been acquired shared %p %s %u
0000f988  set_page_pinned_state
0000f99e  %s(%s:%d) - fte(%p), fte->type(%s), policy(%u), action(%u)
0000f9da  %s(%s:%d) - fte(%p), fte->type(%s), fte->in_flight_ops(%u), action(%u)
0000fa22  %s(%s:%d) - fte(%p), fte->type(%s), flags(%u), action(%u)
0000fa5d  %s(%s:%d) - fte(%p), fte->type(%s), asid(%u)
0000fa8b  cpu_root_table_user_address_space_set_up
0000fab4  %s(%s:%d) - fte(%p), fte->type(%s), mapping_refcnt(%u)
0000faec  cpu_root_table_user_address_space_tear_down
0000fb18  %s: ASID 0x%hx was already clear in sptm_asid_bitmap
0000fb4d  cpt_mapcnt_dec
0000fb5c  rc16_dec
0000fb65  rc16_try_dec_from
0000fb77  expected
0000fb80  cpu_root_table_retype_in
0000fb9e  %s: Unexpected [new_type] while retyping page: %s
0000fbd0  validate_vmid
0000fbde  %s(%s:%d) - fte(%p), fte->type(%s), new_type(%s), mapping_refcnt(%u)
0000fc24  cpu_root_table_retype_out
0000fc3e  %s: VMID 0x%hx was already clear in sptm_vmid_bitmap
0000fc73  %s(%s:%d) - fte(%p), new_type(%s), user_refcnt(%u)
0000fca7  %s: Unexpected [fte->type] while retyping page: %s
0000fcda  %s(%s:%d) - fte(%p), new_type(%s), allocated(%u)
0000fd0c  xnu_subpage_user_root_tables_retype_out
0000fd34  validate_iommu_id
0000fd46  SPTM_IOMMUS_N_IDS
0000fd58  %s(%s:%d) - fte(%p), new_type(%s), fte_tsd->iommu_id(%u), iommu_refcnt(%u)
0000fda4  xnu_iommu_retype_out
0000fdb9  %s(%s:%d) - fte(%p), new_type(%s), sptm_first_tag_storage_paddr(%#llx), sptm_last_tag_storage_paddr(%#llx)
0000fe25  xnu_tag_storage_retype_in
0000fe3f  %s(%s:%d) - fte(%p), new_type(%s), xnu_refcnt(%d), sk_refcnt(%d)
0000fe81  xnu_tag_storage_retype_out
0000fe9c  validate_pt_level
0000feb4  %s(%s:%d) - fte(%p), fte->type(%s), new_type(%s), mapping_refcnt(%u), nested_refcnt(%u)
0000ff0d  cpu_page_table_retype_out
0000ff27  %s: %s: iommu_read_refcnt (0x%hhx) > read_refcnt(0x%x) for FTE %p
0000ff69  xnu_generic_retype_out
0000ff80  %s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d) iommu_read_refcnt(%u)
0000ffda  %s(%s:%d) - fte(%p), new_type(%s), write_exec_refcnt(%d)
00010014  %s: Unexpected write/exec refcount found while retyping an XNU_ROZONE frame (fte = %p)
0001006b  xnu_rozone_retype_out
00010081  %s(%s:%d) - fte(%p), new_type(%s), read_refcnt(%d)
000100b5  %s(%s:%d) - fte(%p), fte->type(%s), new_type(%s), write_exec_refcnt(%d)
000100fe  xnu_exec_retype_out
00010112  %s(%s:%d) - sk_flags(%u), new_type(%s)
0001013a  validate_sk_flags
0001014c  sk_types_retype_out
00010160  %s(%s:%d) - fte(%p), fte->type(%s), new_type(%s), read_refcnt(%d)
000101a3  %s: Invalid permission specified.
000101c5  sapt_set_permissions
000101da  %s: SAPT not bootstrapped.
000101f5  sapt_update_permissions_uat_map
00010215  sapt_update_permissions_uat_unmap
00010237  sapt_synchronize_permissions_update
0001025b  sapt_update_permissions_uat_unmap_sync
00010282  %s: Allowed IOMMU permissions are neither RO nor RW (%d)
000102bb  sapt_perm_for_retype_default_allow
000102de  %s: error getting SecureDT
000102f9  sapt_bootstrap_uat
0001030c  %s: Address 0x%llx not within DRAM
0001032f  sapt_paddr_to_pai
00010341  %s: UAT FW alias detected for physical page: %p.
00010372  sapt_uat_map_default_deny
0001038c  %s: Frame expected to have been acquired has not been acquired %p %s %u
000103d4  retype_paddr_will_be_uat_page_table
000103f8  /chosen
00010400  %s: error %d looking up /chosen
00010420  sapt_bootstrap_globals
00010437  /arm-io/sapt
00010444  %s: error %d looking up /arm-io/sapt
00010469  sapt_bootstrap_table
0001047e  n-entries
00010488  %s: Calculated SAPT table size doesn't match device tree.
000104c2  table-address
000104d0  %s: %s: invalid papt returned by iommu_bootstrap_register_io_range
00010513  sapt_bootstrap_policy
00010529  policy
00010530  %s: Invalid SAPT policy specified
00010552  %s: UAT global instance should not be null.
0001057e  sapt_bootstrap_validate_uat
0001059a  %s: TTBAT address should not be null.
000105c0  %s: UAT Handoff region should not be null.
000105eb  %s: Physical address %#llx is not page-aligned
0001061a  is_page_in_sapt_region
00010631  %s: IO PADDR could not be found %p
00010654  io_range_get_papt
00010666  %s: IO PADDR does not have an associated PAPT address %p %s
000106a2  %s: invalid bootstrap frames type %s, expected SPTM_IOMMU_BOOTSTRAP or XNU_CPUTRACE_PA_BUFFER.
00010701  iommu_bootstrap_alloc_frames_type
00010723  %s: IOMMU %s (%d): State objects exhausted
0001074e  iommu_bootstrap_alloc_instance
0001076d  %s: IOMMU %s (%d): Attempted to register managed page as an IO range %p %zu
000107b9  iommu_bootstrap_register_io_range
000107db  %s: IOMMU %s (%d): Attempted to register an empty IO range %p %zu
0001081d  %s: IOMMU %s (%d): Attempted to register unaligned IO range %p %zu
00010860  %s: IOMMU %s (%d): %#llx length is greater than 64K pages (%zu)
000108a0  %s: IOMMU %s (%d): IO frame does not have a valid type for IO range %p %u
000108ea  %s: IOMMU %s (%d): IO frame starting index %llu does not match IO range starting index %u
00010944  %s: IOMMU %s (%d): IO frame number of pages %llu does not match IO range number of pages %u
000109a0  %s: IOMMU %s (%d): pmap-io-ranges does not exist for IO range %p %u
000109e4  %s: IOMMU %s (%d): cache mode (%u) does not match with pmap-io-ranges (%u) for IO range %p %u
00010a42  %s: IOMMU %s (%d): Number of IO ranges exhausted
00010a73  %s: Number of IO pages exhausted
00010a94  %s(%s:%d) - fte->type(%s), type(%s)
00010ab9  iommu_frame_acquire_type
00010ad2  sptm_iommus.c
00010ae0  iommu_id
00010ae9  fte->iommu_page.iommu_id
00010b02  %s(%s:%d) - iommu_id(%u), fte(%p), fte->type(%s)
00010b34  %s: IOMMU %s (%d): attempted to release unexpected frame %p
00010b70  iommu_frame_release
00010b84  %s: Tried releasing a frame that should not have been acquired to begin with %d
00010bd4  %s: IOMMU %s (%d): attempted to increment refcnt of unexpected frame %p
00010c1c  iommu_page_refcnt_update
00010c35  %s(%s:%d) - paddr(%#llx), fte(%p), fte->type(%s), current_iommu(%u), allowed_permissions(%u), mapping_type(%u)
00010ca5  iommu_register_mapping
00010cbc  mapping_type
00010cc9  restriction->type
00010cdb  current_iommu()
00010ceb  %s: IOMMU %s (%d): attempted to unregister illegal mapping
00010d26  iommu_unregister_mapping
00010d3f  %s(%s:%d) - fte(%p), fte->type(%s), paddr(%#llx), current_iommu(%u), mapping_type(%u)
00010d96  %s: IOMMU %s (%d): attempted to request cache flush for non-generic frame %p %s
00010de6  iommu_mark_coprocessor_cache_flush_needed
00010e10  %s: Only CPUTrace is allowed to call %s() with type %u - %s/%s
00010e4f  iommu_set_page_pinned_state
00010e6d  %s: Unable to get root device tree node.
00010e96  sptm_iommu_reg_base
00010eaa  arm-io
00010eb1  %s: Could not find /arm-io device tree node!
00010ede  %s: Overflow while calculating register end address (0x%llx + 0x%llx)
00010f24  #address-cells
00010f33  %s: Unable to get expected value for #address-cells property from the root device tree node: prop_value = 0x%llx *prop_value = 0x%x.
00010fb8  #size-cells
00010fc4  %s: Unable to get expected value for #size-cells property from the root device tree node.
0001101e  ranges
00011025  %s: Invalid ranges property found.
00011048  %s: Overflow while calculating parent range  end address (0x%llx + 0x%llx)
00011093  %s: Overflow while calculating translated address (0x%llx + 0x%llx)
000110d7  %s: Unable to locate matching range for register range [0x%llx, 0x%llx]
0001111f  %s: Only IO ranges support restrictions
00011147  iommu_register_range_restriction
00011168  %s: Requested metadata storage but none passed
00011197  %s: Attempting to re-register restriction (existing index %d type %d)
000111dd  %s: Overflow when attempting to add a new IO range restriction
0001121c  %s: IO range restriction (%d) out of bounds
00011248  iommu_get_restriction
0001125e  /arm-io
00011266  %s: Error looking up /arm-io
00011283  sptm_register_iommu_restrictions
000112a4  %s: Error initializing DT iterator
000112c7  segment-ranges
000112d6  iommu-parent
000112e3  %s: Invalid iommu-parent size
00011301  %s: Could not look up IOMMU mapper by phandle 0x%x
00011334  %s: Attempted to register a pmap-io-range that is restricted, but could not identify mapper restrictions.
0001139e  %s: IOMMU with id %d not supported
000113c1  enforce_iommu_id_valid
000113d8  io_range_tsd
000113e5  io_range_tsd_const
000113f8  %s: Unexpected Dispatch ID %llu
00011418  current_iommu
00011426  iommu_page_tsd
00011435  iommu_validate_instance
0001144d  instance_id
00011459  next_instance_idx
0001146b  %s: Frame expected to have been acquired has not been acquired %p %s %u %u
000114b6  iommu_assert_frame_in_flight
000114d3  iommu_refcnt_add
000114e4  iommu_refcnt_sub
000114f5  hib_validate_io_buffer_page
00011511  %s: IOMMU %s (%d): Unexpected frame found while attempting to modify refcnt %p %s
00011563  iommu_update_page_refcount
0001157e  %s: IOMMU %s (%d): Non-refcounted frame found while attempting to modify refcnt %p %s
000115d4  %s(%s:%d) - fte(%p), fte->type(%s), current_iommu(%u)
0001160b  %s: IOMMU "%s" does not provide an XNU-facing dispatch table
00011648  iommu_init_driver
0001165a  %s: IOMMU "%s" bootstrap failure
0001167b  %s(%s:%d) - caller_domain(%s), table_permissions(%#llx), domain(%s), table(%s), endpoint_id(%s)
000116dc  dispatch_table_lookup
000116f2  dispatch.c
000116fd  %s: [SPTM Dispatch] Found illegal dispatch entry point. caller_domain: %s, entry_point: %#llx, domain: %s, table: %s, endpoint_id: %s
00011783  %s: invalid state: %s
00011799  dispatch_state_machine
000117b0  %s: invalid event type: %s
000117cb  %s: invalid next state: %s
000117e6  %s: invalid state transition - no action set for the transition. current_state: %s, event_type: %s, event_metadata: %#llx
00011860  %s(%s:%d) - cpu_id(%u), event_type(%s), event_metadata(%#llx), current_state(%s), next_state(%s)
000118c2  %s: Invalid hop detected when transitioning XNU->TXM %llu
000118fc  %s(%s:%d) - txm_stack(%#llx), phys_type(%u), domain(%s), table(%s), endpoint_id(%s)
00011951  %s(%s:%d) - caller_domain(%s), table(%s), dispatch_entry_addr(%#llx), permissions(%#llx)
000119ab  sptm_register_dispatch_table
000119c8  %s(%s:%d) - caller_domain(%s), table(%s), existing_entry_point(%#llx)
00011a0f  sptm_register_xnu_exc_return
00011a2c  return_addr
00011a38  *xnu_exc_return_handler
00011a50  register_sptm_iommu_dispatch_table
00011a73  %s: tried registering the same dispatch table twice %d
00011aaa  %s(%s:%d) - caller_domain(%s), domain(%s), table(%s), endpoint_id(%s)
00011af1  dispatch_cmd_call_from_xnu_handler
00011b14  %s(%s:%d) - caller_domain(%s), domain_id(%u), table(%s), endpoint_id(%s)
00011b5e  sptm_dispatch
00011b6c  %s: vector_type not valid
00011b86  handle_exception_action
00011b9e  %s: xnu_exc_return_handler not registered
00011bc8  %s: [%s] %s at pc 0x%016llx, lr 0x%016llx
00011bf3    x0:  0x%016llx x1:  0x%016llx  x2:  0x%016llx  x3:  0x%016llx
00011c34    x4:  0x%016llx x5:  0x%016llx  x6:  0x%016llx  x7:  0x%016llx
00011c75    x8:  0x%016llx x9:  0x%016llx  x10: 0x%016llx  x11: 0x%016llx
00011cb6    x12: 0x%016llx x13: 0x%016llx  x14: 0x%016llx  x15: 0x%016llx
00011cf7    x16: 0x%016llx x17: 0x%016llx  x18: 0x%016llx  x19: 0x%016llx
00011d38    x20: 0x%016llx x21: 0x%016llx  x22: 0x%016llx  x23: 0x%016llx
00011d79    x24: 0x%016llx x25: 0x%016llx  x26: 0x%016llx  x27: 0x%016llx
00011dba    x28: 0x%016llx fp:  0x%016llx  lr:  0x%016llx  sp:  0x%016llx
00011dfb    pc:  0x%016llx cpsr: 0x%08x         esr: 0x%016llx          far: 0x%016llx
00011e49    LLC_ERR_STS: 0x%016llx  LLC_ERR_ADR: 0x%016llx  LLC_ERR_INF: 0x%016llx
00011e93  panic_with_register_state
00011ead  %s: [SPTM Dispatch] Invalid Dispatch Command value %u in dispatch_cmd_handler (current CPU: %u, panicking CPU: %u).
00011f21  nested_panic_bad_dispatch_cmd
00011f3f  %s: [SPTM Dispatch] Invalid hop count in get_callee_state. hop_count: %lld
00011f8b  get_callee_state
00011f9c  %s: Invalid calling_exec_mode %u
00011fbd  dispatch_cmd_handler
00011fd2  %s: [SPTM Dispatch] Invalid calling domain in dispatch_cmd_handler. calling_domain: %s, calling_exec_mode: %d, domain: %s, table: %s, endpoint_id: %s
00012068  %s(%s:%d) - calling_domain(%s), calling_exec_mode(%u), dispatch_cmd_id(%u), domain(%s), table(%s), endpoint_id(%s)
000120dc  validate_dispatch_target
000120f5  caller_domain
00012103  domain_id
0001210d  table_id
00012116  endpoint_id
00012128  INVALID_DOMAIN_ID
0001213a  SPTM_DOMAIN
00012146  XNU_DOMAIN
00012151  TXM_DOMAIN
0001215c  SK_DOMAIN
00012166  XNU_HIB_DOMAIN
00012175  INVALID_DISPATCH_TABLE_ID
0001218f  SPTM_DISPATCH_TABLE_XNU_BOOTSTRAP
000121b1  SPTM_DISPATCH_TABLE_TXM_BOOTSTRAP
000121d3  SPTM_DISPATCH_TABLE_SK_BOOTSTRAP
000121f4  SPTM_DISPATCH_TABLE_T8110_DART_XNU
00012217  SPTM_DISPATCH_TABLE_T8110_DART_SK
00012239  SPTM_DISPATCH_TABLE_SART
00012252  SPTM_DISPATCH_TABLE_NVME
0001226b  SPTM_DISPATCH_TABLE_UAT
00012283  SPTM_DISPATCH_TABLE_SHART
0001229d  SPTM_DISPATCH_TABLE_CPUTRACE
000122ba  SPTM_DISPATCH_TABLE_HIB
000122d2  SPTM_DISPATCH_TABLE_GEN3_DART_XNU
000122f4  SPTM_DISPATCH_TABLE_GEN3_DART_SK
00012315  SPTM_DISPATCH_TABLE_T6000_DART_XNU
00012338  SPTM_DISPATCH_TABLE_T8020_DART_XNU
0001235b  SPTM_DISPATCH_TABLE_RESERVED2
00012379  INVALID_DISPATCH_STATE
00012390  STATE_SPTM_BOOTSTRAP
000123a5  STATE_SK_BOOTSTRAP
000123b8  STATE_TXM_BOOTSTRAP
000123cc  STATE_SPTM_CALLED_BY_TXM_BOOTSTRAP
000123ef  STATE_SPTM_CALLED_BY_SK_BOOTSTRAP
00012411  STATE_XNU
0001241b  STATE_XNU_GUEST
0001242b  STATE_XNU_HIB
00012439  STATE_TXM_CALLED_BY_XNU
00012451  STATE_TXM_SAVE_CONTEXT
00012468  STATE_TXM_CALLED_BY_SPTM
00012481  STATE_SPTM_CALLED_BY_XNU
0001249a  STATE_SPTM_CALLED_BY_XNU_HIB
000124b7  STATE_XNU_HANDLE_SPTM_EXCEPTION
000124d7  STATE_SPTM_CALLED_BY_TXM
000124f0  STATE_SPTM_CALLED_BY_SK
00012508  STATE_SK_CALLED_BY_XNU
0001251f  STATE_SK_CALLED_BY_SPTM_HIB
0001253b  STATE_SK_EXCEPTION
0001254e  STATE_XNU_PANIC
0001255e  STATE_PANIC_SPTM_CALLED_BY_XNU
0001257d  STATE_DISPATCH_PANIC_SPIN
00012597  STATE_SPTM_REENTERED_BY_XNU
000125b3  INVALID_EVENT_TYPE
000125c6  EVENT_BOOTSTRAP_TXM
000125da  EVENT_BOOTSTRAP_SK
000125ed  EVENT_CALL_SPTM
000125fd  EVENT_CALL_TXM
0001260c  EVENT_CALL_SK
0001261a  EVENT_RETURN
00012627  EVENT_EXCEPTION
00012637  EVENT_CONTEXT_SAVED
0001264b  EVENT_RESUME_SPTM
0001265d  EVENT_PANIC
00012669  EVENT_RESUME_TO_PANIC_CALL
00012684  EVENT_PANIC_SPIN
00012695  EVENT_ENTER_GUEST
000126a7  EVENT_EXIT_GUEST
000126b8  EVENT_CALL_SPTM_HIB
000126cc  validate_sptm_dispatch_table_id
000126ec  SPTM-rx
000126f4  BootKC-rx
000126fe  TXM-rx
00012706  %s: Caller domain exceeds array dimensions %d
00012734  validate_dispatch_entry_addr
00012751  entry_addr
0001275c  SPTM_FUNCTIONID_LOCKDOWN
00012775  SPTM_FUNCTIONID_RETYPE
0001278c  SPTM_FUNCTIONID_MAP_PAGE
000127a5  SPTM_FUNCTIONID_MAP_TABLE
000127bf  SPTM_FUNCTIONID_UNMAP_TABLE
000127db  SPTM_FUNCTIONID_UPDATE_REGION
000127f9  SPTM_FUNCTIONID_UPDATE_DISJOINT
00012819  SPTM_FUNCTIONID_UNMAP_REGION
00012836  SPTM_FUNCTIONID_UNMAP_DISJOINT
00012855  SPTM_FUNCTIONID_CONFIGURE_SHAREDREGION
0001287c  SPTM_FUNCTIONID_NEST_REGION
00012898  SPTM_FUNCTIONID_UNNEST_REGION
000128b6  SPTM_FUNCTIONID_CONFIGURE_ROOT
000128d5  SPTM_FUNCTIONID_SWITCH_ROOT
000128f1  SPTM_FUNCTIONID_REGISTER_CPU
0001290e  SPTM_FUNCTIONID_FIXUPS_COMPLETE
0001292e  SPTM_FUNCTIONID_SIGN_USER_POINTER
00012950  SPTM_FUNCTIONID_AUTH_USER_POINTER
00012972  SPTM_FUNCTIONID_REGISTER_EXC_RETURN
00012996  SPTM_FUNCTIONID_CPU_ID
000129ad  SPTM_FUNCTIONID_SLIDE_REGION
000129ca  SPTM_FUNCTIONID_UPDATE_DISJOINT_MULTIPAGE
000129f4  SPTM_FUNCTIONID_GUEST_VA_TO_IPA
00012a14  SPTM_FUNCTIONID_GUEST_STAGE1_TLBOP
00012a37  SPTM_FUNCTIONID_GUEST_STAGE2_TLBOP
00012a5a  SPTM_FUNCTIONID_GUEST_DISPATCH
00012a79  SPTM_FUNCTIONID_GUEST_EXIT
00012a94  SPTM_FUNCTIONID_HIB_BEGIN
00012aae  SPTM_FUNCTIONID_HIB_VERIFY_HASH_NON_WIRED
00012ad8  SPTM_FUNCTIONID_HIB_FINALIZE_NON_WIRED
00012aff  SPTM_FUNCTIONID_IOFILTER_PROTECTED_WRITE
00012b28  SPTM_FUNCTIONID_SPTM_TAG_PAPT_MULTIPAGE
00012b50  SPTM_FUNCTIONID_SPTM_UNTAG_PAPT_MULTIPAGE
00012b7a  SPTM_FUNCTIONID_DISABLE_KERNEL_MODE_CPA2
00012ba3  SPTM_FUNCTIONID_SET_SHARED_REGION
00012bc5  SPTM_FUNCTIONID_BATCH_SIGN_USER_POINTER
00012bed  SPTM_FUNCTIONID_SURT_ALLOC
00012c08  SPTM_FUNCTIONID_SURT_FREE
00012c22  SPTM_FUNCTIONID_CONDEMN_LEAF_TABLE
00012c45  SPTM_FUNCTIONID_UNCONDEMN_LEAF_TABLE
00012c6a  SPTM_FUNCTIONID_SPTM_SERIAL_PUTC
00012c8b  SPTM_FUNCTIONID_SPTM_SERIAL_DISABLE
00012caf  SPTM_FUNCTIONID_PROGRAM_IRGKEY
00012cce  SPTM_FUNCTIONID_OUTPUT_AREA
00012cea  TXM_TO_SPTM_ENDPOINTID_FIXUPS_COMPLETE
00012d11  TXM_TO_SPTM_ENDPOINTID_REGISTER_DISPATCH_TABLE
00012d40  TXM_TO_SPTM_ENDPOINTID_RETYPE
00012d5e  TXM_TO_SPTM_ENDPOINTID_USER_ASID
00012d7f  SK_TO_SPTM_ENDPOINTID_REGISTER_DISPATCH_TABLE
00012dad  SK_TO_SPTM_ENDPOINTID_RETYPE
00012dca  SK_TO_SPTM_ENDPOINTID_PHYS_TO_TYPE
00012ded  SK_TO_SPTM_ENDPOINTID_IS_SK_DEFAULT_TAGGABLE
00012e1a  SPTM_HIB_ENDPOINTID_HASH_HIBSEG_PAGE
00012e3f  SPTM_HIB_ENDPOINTID_HASH_PAGE
00012e5d  SPTM_HIB_ENDPOINTID_FINALIZE_HASH
00012e7f  SPTM_HIB_ENDPOINTID_FINALIZE_SK
00012e9f  SPTM_HIB_ENDPOINTID_FINALIZE_IMAGE
00012ec2  SPTM_HIB_ENDPOINTID_IOFILTER_PROTECTED_WRITE
00012eef  INVALID_ENDPOINT_ID
00012f03  validate_dispatch_endpoint_id
00012f24  DISPATCH_ID_SPTM_CORE
00012f3a  INVALID_DISPATCH_ID
00012f4e  IOMMU_ID_SHART
00012f5d  IOMMU_ID_SART
00012f6b  IOMMU_ID_NVME
00012f79  IOMMU_ID_UAT
00012f86  IOMMU_ID_DART_T8020
00012f9a  IOMMU_ID_DART_T8110
00012fae  IOMMU_ID_DART_T6000
00012fc2  IOMMU_ID_CPUTRACE
00012fd4  IOMMU_ID_DART_GEN3
00012fe7  %s: Invalid exception vector type: %s (%u) (current_hop=%llu, dispatch_state=%s)
00013038  dispatch_cmd_exception_saved_from_sk
0001305d  %s: Unexpected current_hop %llu (vector_type=%s (%u), dispatch_state=%s)
000130a6  INVALID_VECTOR_TYPE
000130ba  SPTM_VECTOR_IRQ
000130ca  SPTM_VECTOR_FIQ
000130da  SPTM_VECTOR_SERROR
000130ed  SPTM_VECTOR_SYNC
000130fe  /Library/Caches/com.apple.xbs/E6EECBFA-A35F-4C31-99B3-BA4E76C73F65/TemporaryDirectory.TftW7z/Sources/SPTM/sptm/boot/hib/hibernate_restore.c
0001318a  header->image1Size > (uintptr_t)page_list_end_paddr - (uintptr_t)header_paddr
000131d8  Invalid image1 size
000131ec  bitmap_page_is_valid(first_free_paddr, header, &temp_dt)
00013225  managed_phys_start != 0
0001323d  managed_phys_end != 0
00013253  IS_BIT_SET(header->kernelSlide, 63)
00013277  header->handoffPageCount < HIB_HANDOFF_PAGECOUNT_LIMIT
000132ae  arg.limit_upper > arg.limit_lower
000132d0  memcmp(hib_header_copy->imageHeaderHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
0001331d  memcmp(hib_header_copy->handoffHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
00013366  memcmp(hib_header_copy->image1PagesHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
000133b3  memcmp(hib_header_copy->image2PagesHMAC, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
00013400  memcmp(hib_header_copy->protected_metadata_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
00013455  memcmp(hib_header_copy->sptm_rorgn_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
000134a2  memcmp(hib_header_copy->hib_segs_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
000134ed  memcmp(hib_header_copy->xnu_rorgn_hmac, zeroHMAC, HIBERNATE_HMAC_SIZE) != 0
00013539  hib_header_copy->handoffPageCount < HIB_HANDOFF_PAGECOUNT_LIMIT
00013579  !sptm_add_overflow(src_paddr, (0), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr
000135da  preview_list_paddr != 0
000135f2  !sptm_add_overflow(src_paddr, (2 * sizeof(uint32_t)), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr
00013666  __probable((dst_raddr >= hib_ctx->restore_slide) && (dst_raddr < hib_ctx->hibtext_slide))
000136c0  attempting to restore immutable page
000136e5  !sptm_add_overflow(src_paddr, (sizeof(uint32_t)), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr
00013755  (tag & kIOHibernateTagSigMask) == kIOHibernateTagSignature
00013790  compressed_size <= SPTM_PAGE_SIZE
000137b2  __probable(hib_page_bitmap(hib_ctx->page_list, dst_ppnum) == NULL || !hib_page_bitget(hib_ctx->page_list, dst_ppnum))
00013828  !sptm_add_overflow(src_paddr, (compressed_size), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr
00013897  hib_header_copy->protected_metadata.exclave_key_phys != 0
000138d1  io_range == NULL || !(io_range->flags & HIB_PHYS_RANGE_FLAG_PROHIBITED)
00013919  ccgcm_finalize(gcm, ctx, sizeof(hib_header_copy->exclave_iv.tag), hib_header_copy->exclave_iv.tag) == 0
00013981  hib_ctx->restore_slide != 0
0001399d  hib_ctx->hibtext_slide != 0
000139b9  hib_ctx->hibtext_fixup_slide != 0
000139db   Hibernation Exit Panic: 
000139f5   Assertion failed: 
00013a09  hdr_page_list_length >= sizeof(hibernate_page_list_t)
00013a3f  list->list_size <= hdr_page_list_length
00013a67  (end - ptr) >= (sizeof(hibernate_page_list_t))
00013a96  (end - ptr) >= (sizeof(hibernate_bitmap_t))
00013ac2  bank->last_page >= bank->first_page
00013ae6  bank->first_page > last_page_seen
00013b08  bank_page_count > 0
00013b1c  !sptm_add_overflow(bank_page_count, bitmapword_bits - 1, &roundup)
00013b5f  bank->bitmapwords == (roundup / bitmapword_bits)
00013b90  !sptm_add_overflow(pages_seen, bank_page_count, &pages_seen)
00013bcd  pages_seen <= list->page_count
00013bec  (end - ptr) >= (bank->bitmapwords * sizeof(bank->bitmap[0]))
00013c29  pages_seen == list->page_count
00013c48  Could not find device tree in handoff region
00013c75  (header != NULL) && (list != NULL)
00013c98  list != NULL
00013ca5  (list != NULL) && (next_free_page != NULL)
00013cd0  !sptm_add_overflow(next_free_in_bank, bitmap_count, &total_count)
00013d12  bitmap != NULL
00013d21  !sptm_add_overflow(count, zero_count, &total_count)
00013d55  !sptm_add_overflow(count, offset, &total_count)
00013d85  !sptm_add_overflow(page, count, &total_count)
00013db3  !sptm_add_overflow(bitmap->last_page, 1, &total_count)
00013dea  dt != NULL
00013df5  !((uint64_t)sptm_hib_unaligned_read_uint32(&range->flags) & (uint64_t)(HIB_PHYS_RANGE_FLAG_PROHIBITED | HIB_PHYS_RANGE_FLAG_DEV_MEM))
00013e7b  src != NULL
00013e87  size > 0
00013e90  /defaults
00013e9a  err == kSuccess
00013eaa  pmap-io-ranges
00013eb9  upper != NULL
00013ec7  (addr & SPTM_PAGE_MASK) == 0
00013ee4  (len >> SPTM_PAGE_SHIFT) <= UINT32_MAX
00013f0b  !(wimg & (PMAP_IO_RANGE_NOT_IO | PMAP_IO_RANGE_PROHIBIT_HIB_WRITE))
00013f4f  hib_ctx->num_hib_io_ranges < MAX_HIB_IO_RANGES
00013f7e  (hib_ctx->page_list != NULL) && (hib_ctx->next_free_page != 0)
00013fbd  Invalid bitmap page attempted to be allocated
00013feb  end_paddr >= start_paddr
00014004  IS_BIT_SET(start_vaddr, 63)
00014020  bank_start <= bank_end
00014037  (bank_start >= data->limit_lower) && (bank_start <= data->limit_upper) && (bank_end <= data->limit_upper)
000140a1  io_range != NULL
000140b2  io_range->flags & HIB_PHYS_RANGE_FLAG_NEEDS_HIB
000140e2  !(io_range->flags & HIB_PHYS_RANGE_FLAG_PROHIBITED)
00014116  hib_ctx != NULL
00014126  (size & SPTM_PAGE_MASK) == 0
00014143  hib_ctx->restore_slide == 0
0001415f  root_table_paddr != 0
00014175  IS_PTE_INVALID(table_base[index + i])
0001419b  level < LEAF_TABLE_LEVEL
000141b4  (entry & (ARM_TTE_VALID | ARM_TTE_TYPE_MASK)) != (ARM_TTE_VALID | ARM_TTE_TYPE_BLOCK)
0001420a  (child_pt_paddr & SPTM_PAGE_MASK) == 0
00014231  chosen/memory-map
00014243  Failed to locate chosen/memory-map node in device tree
0001427a  BootArgs
00014283  Failed to read /chosen/memory-map/BootArgs property.
000142b8  Wrong property length on /chosen/memory-map/BootArgs.
000142ee  hibernate
000142f8  Failed to locate hibernate node in device tree
00014327  hmac-reg-base
00014335  Failed to read hmac-reg-base property.
0001435c  hmac-reg-base property size is incorrect.
00014386  pmgr-reg-base
00014394  Failed to read pmgr-reg-base property.
000143bb  pmgr-reg-base property size is incorrect.
000143e5  pmgr-reg-base is 0.
000143f9  pmgr-aes-offset
00014409  Failed to read pmgr-aes-offset property.
00014432  pmgr-aes-offset property size is incorrect.
0001445e  arm-io/aop/iop-aop-nub/aop-gapf-filters
00014486  sptm-gapf-enable-reg
0001449b  Failed to read sptm-gapf-enable-reg property.
000144c9  sptm-gapf-enable-reg property size is incorrect.
000144fa  sptm-gapf-lock-reg
0001450d  Failed to read sptm-gapf-lock-reg property.
00014539  sptm-gapf-lock-reg property size is incorrect.
00014568  ((uintptr_t)hib_ctx->aop_gapf_lock_reg & ~SPTM_PAGE_MASK) == reg_page
000145ae  memcmp(hib_ctx->hmac_buf, hib_header->handoffHMAC, sizeof(hib_ctx->hmac_buf)) == 0
00014601  key-sptm-ctrr
0001460f  key-xnu-ctrr
0001461c  key-exclave-original
00014631  key-exclave
0001463d  (serialize != NULL) && (buffer != NULL)
00014665  size != 0
0001466f  (serialize->bytes_accessed + size) <= serialize->total_length
000146ad  cur_page_pos <= max_page_size
000146cb  *next_page_ptr != NULL
000146e2  (src != NULL) && (wkdm_scratch != NULL)
0001470a  compressed_size > 0
0001471e  !is_immutable(dst_paddr)
00014737  dst_paddr != hib_ctx->hibtext_stack_paddr
00014761  io_range != NULL && (io_range->flags & HIB_PHYS_RANGE_FLAG_NEEDS_HIB)
000147a7  (src != NULL) && (dst != NULL) && (scratch != NULL)
000147db  (((uintptr_t)wkdm_src) & 63) == 0
000147fd  (((uintptr_t)dst) & SPTM_PAGE_MASK) == 0
00014826  result.status == 0
00014839  memcmp(hib_ctx->hmac_buf, hib_header->image1PagesHMAC, sizeof(hib_ctx->hmac_buf)) == 0
00014890  memory region HMAC mismatch!
000148ad  %s(%s:%d) - fte(%p), fte->type(%s), new_type(%s), retype_params(%#llx)
000148f5  sptm_retype
00014901  sptm.c
00014908  %s(%s:%d) - fte(%p), fte->type(%s), current_type(%s), calling_domain(%u), owner_domain(%u)
00014964  %s(%s:%d) - paddr(%#llx), fte->type(%s), current_type(%s), new_type(%s)
000149ad  %s(%s:%d) - paddr(%#llx), fte->type(%s), new_type(%s)
000149e4  %s(%s:%d) - paddr(%#llx), fte(%p), fte->type(%s), new_type(%s)
00014a24  %s(%s:%d) - fte(%p), new_type(%s), flags(%u)
00014a52  %s: Unsupported cacheattr_index %u from retype_in for incoming type %s
00014a99  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), attr_idx(%u), vaddr(%#llx), pagezero_size(%#llx)
00014aff  sptm_map_page
00014b0d  %s(%s:%d) - %s(%#llx)
00014b24  page_paddr
00014b2f  %s(%s:%d) - %s(%#llx), %s(%#llx), %s(%#llx)
00014b5c  new_pte
00014b6a  %s(%s:%d) - %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx)
00014ba2  root_pt_fte
00014bae  page_fte
00014bb7  %s(%s:%d) - page_paddr(%#llx), page_fte(%p), page_fte->type(%s), root_pt_fte->type(%s), vaddr(%#llx)
00014c1d  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), leaf_pt_fte->type(%s), page_fte->type(%s), vaddr(%#llx), new_pte(%#llx)
00014c9a  %s(%s:%d) - page_fte(%p), page_fte->type(%s), new_perms(%u), new_pte(%#llx), vaddr(%#llx)
00014cf5  %s(%s:%d) - root_pt_fte->type(%s), leaf_pt_fte->type(%s), page_fte->type(%s), new_pte(%#llx)
00014d53  %s(%s:%d) - is_user_mapping(%u), new_perms(%u), page_fte->type(%s)
00014d97  %s(%s:%d) - prev_perms(%u), new_perms(%u), prev_pte(%#llx), new_pte(%#llx), page_fte->type(%s)
00014df7  sptm_map_table
00014e06  child_pt_fte
00014e13  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), vaddr(%#llx), commpage_region_start(%#llx), commpage_region_size(%#llx), root_table_flags(%#x)
00014ea7  %s(%s:%d) - root_pt_fte(%p), child_pt_paddr(%#llx), root_pt_fte->type(%s), child_pt_fte->type(%s)
00014f0a  %s(%s:%d) - root_pt_fte(%p), child_pt_paddr(%#llx), parent_pt_fte->type(%s), child_pt_fte->type(%s)
00014f6f  child_pt_tsd->level
00014f83  target_level
00014f90  %s(%s:%d) - child_pt_fte(%p), child_pt_fte->type(%s), mapping_refcnt(%d), nested_refcnt(%d)
00014fed  expected_tte
00014ffa  %s: rw_guard_release_shared: %p
0001501a  %s(%s:%d) - root_pt_fte(%p), sptm_root_table_paddr(%#llx), root_pt_fte->type(%s), vaddr(%#llx), target_level(%u)
0001508c  sptm_unmap_table
0001509d  %s(%s:%d) - %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx)
000150e0  parent_ttep
000150ec  parent_tte
000150f7  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), child_pt_fte(%p), child_pt_fte->type(%s)
00015155  %s: incompatible page table type %s found in page table %p
00015190  %s(%s:%d) - %s(%#llx), %s(%#llx)
000151b2  sptm_surt_alloc
000151c2  sanitize_integer(surt_frame_U.UNSAFE_VALUE)
000151ee  surt_index
000151f9  metadata->fte.in_flight_ops
00015215  attr_idx
0001521e  sptm_surt_free
0001522d  %s: preflight or finalize mapping operation function pointers are NULL
00015274  sptm_region_op
00015283  start_vaddr
0001528f  cur_mapping
0001529b  *prev_pte
000152a5  mapping_data->page_fte->type
000152c2  %s: Page FTE does not match the validity of the previous PTE %#llx %p
00015308  %s(%s:%d) - leaf_pt_fte(%p), leaf_pt_fte->type(%s), prev_pte(%#llx), pte_template(%#llx)
00015362  unmap_preflight_op
00015375  %s(%s:%d) - page_fte(%p), page_fte->type(%s), prev_pte(%#llx), pte_template(%#llx)
000153c9  cur_mapping_data
000153da  prev_pte
000153e3  pte_template
000153f0  options
000153f8  %s: Dangling tag storage reference from previous mapping attempt
00015439  %s: PTEP is somehow NULL
00015452  unmap_finalize_op
00015464  %s: prev_pte is somehow empty
00015482  %s: Leaf page table FTE is somehow NULL
000154aa  update_preflight_op
000154be  %s(%s:%d) - cur_mapping_data(%p), page_fte->type(%s), prev_pte(%#llx), pte_template(%#llx), new_perms(%u), current_perms(%u)
0001553c  %s(%s:%d) - cur_mapping_data(%p), page_fte->type(%s), prev_pte(%#llx), pte_template(%#llx), options(%#x)
000155a6  %s: prev_pte is somehow empty in the final pass
000155d6  update_finalize_op
000155e9  sptm_update_region
000155fc  sanitize_integer(root_pt_U.UNSAFE_VALUE)
00015625  sanitize_integer(start_vaddr_U.UNSAFE_VALUE)
00015652  sptm_disjoint_op
00015663  %s(%s:%d) - paddr(%#llx), page_fte(%p), page_fte->type(%s)
0001569f  %s: Leaf page table FTE is somehow NULL even though prev_pte is valid
000156e5  sptm_update_disjoint
000156fa  sanitize_integer(paddr_U.UNSAFE_VALUE)
00015721  sanitize_integer(disjoint_ops_U.UNSAFE_VALUE)
0001574f  %s(%s:%d) - %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx), %s(%#llx)
0001579d  sptm_update_disjoint_multipage
000157bc  cur_entry_idx
000157ca  num_mappings
000157d7  num_entries
000157e3  multipage_ops_pa
000157f4  cur_entry
000157fe  sptm_configure_shared_region
0001581b  shared_root_fte
0001582b  %s: Unexpected shared region state
0001584e  sptm_set_shared_region
00015865  user_root_fte
00015873  user_root_fte->cpu_root_table.attr_idx
0001589a  shared_root_fte->cpu_root_table.attr_idx
000158c3  shared_region_id
000158d6  expected_shared_region
000158ed  sptm_nest_region
000158fe  user_root_fte->cpu_root_table.shared_region_id
00015932  shared_region_start_vaddr
0001594c  shared_region_end_vaddr
00015964  user_ttep
0001596e  new_user_tte
0001597b  sanitize_integer(user_root_pt_U.UNSAFE_VALUE)
000159a9  sanitize_integer(shared_root_pt_U.UNSAFE_VALUE)
000159d9  shared_tte
000159e4  leaf_pt_fte->type
000159f6  user_tt_fte->type
00015a08  sptm_unnest_region
00015a1b  prev_shared_region_id
00015a31  shared_region_size
00015a44  user_tt_fte
00015a50  user_tte
00015a59  sptm_switch_root
00015a6a  override_flags
00015a79  override_mask
00015a87  sptm_guest_stage1_tlb_op
00015aa3  %s(%s:%d) - stage2_root_pt_fte(%p), stage2_root_pt_fte->type(%s), vmid(%u), current_vmid(%u)
00015b01  sptm_guest_exit
00015b11  stashed_vncr_paddr
00015b24  vncr_paddr
00015b2f  stashed_avncr_paddr
00015b43  avncr_paddr
00015b4f  sptm_batch_sign_user_pointer
00015b6c  user_pointer_ops_pa
00015b80  ops_count
00015b8a  jop_key
00015b92  sptm_tag_op
00015ba4  read_refcnt
00015bb0  write_exec_refcnt
00015bc2  %s: Unexpected return value from papt_update_mapping(), paddr = %p
00015c05  %s: SPTM_UPDATE_DEFER_TLBI passed for untag operation?!
00015c3d  sptm_tag_papt_multipage
00015c55  %s: non-success return code %d
00015c74  sptm_untag_papt_multipage
00015c8e  sptm_guest_dispatch
00015ca2  sanitize_integer(guest_state_paddr_U.UNSAFE_VALUE)
00015cd5  %s(%s:%d) - vncr_paddr(%#llx), avncr_paddr(%#llx), vncr_fte(%p), vncr_fte->type(%s), avncr_fte(%p), avncr_fte->type(%s)
00015d4e  %s: per-cpu last_vncr_paddr already set (%llx)
00015d7d  %s: per-cpu last_avncr_paddr already set (%llx)
00015dad  %s: interrupts must be disabled by caller
00015dd7  sptm_guest_va_to_ipa
00015dec  validate_managed_page
00015e02  sptm_validation.h
00015e14  sptm_first_phys
00015e24  sptm_last_phys
00015e33  validate_frame_type
00015e47  frame_type
00015e52  N_FRAME_TYPES
00015e60  %s: Type %s is not xnu-taggable
00015e80  mark_fte_xnu_tagged
00015e94  acquire_root_pt
00015ea4  root_pt
00015eac  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), in_flight_ops(%u)
00015ef3  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s)
00015f27  validate_aligned_vaddr
00015f3e  aligned_vaddr
00015f4c  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), aligned_vaddr(%#llx), target_level(%u), va_size(%#llx)
00015fb8  cpu_root_table_tsd
00015fcb  validate_pte
00015fdc  helper_enforce_paddr_mappable
00016000  %s: FNXS is expected to be set.
00016020  pte_is_xs
0001602a  %s: refcnt overflow: rc %p old_value %lld value %lld
0001605f  rc32_inc
00016068  tag_storage_page_tsd
0001607d  release_root_pt
0001608d  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), level(%u), attr_idx(%u), root_level(%u), max_level(%u)
000160f9  validate_pt_level_intermediate
00016118  validate_tte
00016129  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), ptep(%p), *ptep(%#llx), vaddr(%#llx)
00016183  table_acquire
00016191  sptm_types.h
0001619e  cpu_page_table_tsd
000161b1  rc16_try_inc_from
000161c3  sptm_concurrency.h
000161dc  crt_mapcnt_inc
000161eb  cpt_mapcnt_inc
000161fa  sptm_leaf_table_condemn_op
00016215  new_tte
0001621d  acquire_surt_frame
00016230  surt_frame
0001623b  %s(%s:%d) - surt_frame_fte(%p), surt_frame_fte->type(%s), in_flight_ops(%u)
00016288  %s(%s:%d) - surt_frame(%#llx), surt_frame_fte->type(%s)
000162c1  validate_surt_index
000162d5  subpage_user_root_tables_tsd
000162f2  validate_attribute_index
00016311  supported_geometries[stage]
0001632d  validate_root_flags
00016341  root_flags
0001634c  validate_asid
0001635f  sptm_num_asids
0001636e  release_surt_frame
00016381  validate_vaddr_range_leaf
0001639b  end_vaddr
000163a5  helper_validate_aligned_vaddr_range
000163c9  page_count
000163d4  page_size
000163de  %s(%s:%d) - root_pt_fte(%p), root_pt_fte->type(%s), attr_idx(%u), va_size(%#llx), start_vaddr(%#llx), end_vaddr(%#llx)
00016456  %s: refcnt underflow: rc %p old_value %lld value %lld
0001648c  rc32_dec
00016495  cpu_page_tsd
000164a2  validate_managed_addr
000164b8  validate_page_count
000164cc  max_page_count
000164db  validate_multipage_ops_entries
000164fa  max_entry_count
0001650a  entry_size
00016515  sptm_update_papt
00016526  acquire_shared_root_pt
0001653d  shared_root_pt
0001654c  %s(%s:%d) - shared_root_pt_fte(%p), shared_root_pt_fte->type(%s), in_flight_ops(%u)
000165a1  %s(%s:%d) - shared_root_pt_fte(%p), shared_root_pt_fte->type(%s)
000165e3  %s: Unexpected shared region ID
00016603  shared_region_get_state
0001661b  acquire_user_root_pt
00016630  user_root_pt
0001663d  %s(%s:%d) - page_fte(%p), page_fte->type(%s), in_flight_ops(%u)
0001667e  %s(%s:%d) - metadata->fte(%p), metadata->fte.type(%s), in_flight_ops(%u)
000166cd  %s(%s:%d) - page_fte(%p), page_fte->type(%s)
000166fb  user_root_pt_fte
0001670c  user_root_pt_fte->cpu_root_table.flags
00016733  shared_region_get_start_vaddr
00016751  rc16_try_inc
0001675e  old_value
00016768  rc->_value
00016773  release_shared_root_pt
0001678a  release_user_root_pt
0001679f  validate_vaddr_range_twig
000167b9  validate_root_config
000167ce  root_config
000167da  crt_mapcnt_dec
000167e9  acquire_stage2_root_pt
00016800  stage2_root_pt
0001680f  %s(%s:%d) - stage2_root_pt_fte(%p), stage2_root_pt_fte->type(%s), in_flight_ops(%u)
00016864  %s(%s:%d) - stage2_root_pt_fte(%p), stage2_root_pt_fte->type(%s)
000168a6  sptm_guest_enter
000168b7  sanitize_integer(stage2_root_pt_U.UNSAFE_VALUE)
000168e7  validate_sptm_ptrauth_user_key
00016910  discriminator
0001691e  validate_user_pointer_ops_count
0001693e  max_ops_count
0001694c  mark_fte_xnu_untagged
00016962  SPTM-820.40.24|2026-10-03:15:39:53.723193|
00016997  validate_sptm_cputrace_mode
000169b3  cputrace_validation.c
000169c9  validate_cputrace_strm_base_id
000169e8  %s: assert 'carveout_start_paddr' failed.
00016a12  validate_cputrace_pa_buffer
00016a2e  %s: assert 'carveout_size' failed.
00016a51  %s: assert '!__builtin_add_overflow(carveout_start_paddr, carveout_size, &carveout_end_paddr)' failed.
00016ab8  validate_cputrace_va_buffer
00016ad4  validate_cputrace_va_region_id
00016af3  validate_cputrace_va_frame_vaddr
00016b14  %s: assert 'nb_units' failed.
00016b32  cputrace_pa_get_stream_base
00016b4e  %s: assert '!(size_limit >> PROD_TRC_STRM_BASE_VALID_BASE)' failed.
00016b92  %s: assert '!(paddr >> PROD_TRC_STRM_BASE_ADDR_SIZE)' failed.
00016bd0  cputrace_va_get_stream_base
00016bec  %s: Type (%s) class of FTE (%p) does not match the type class of the type-specific-data trying to be retrieved: actual (%d) != requested (%d).
00016c7b  cpu_root_table_tsd_const
00017040  randseed
00017744  sptm.t8160.release
000bec5d  J(NZk(N
000beca1  J(NZk(N
000bece5  J(NZk(N
000bed29  J(NZk(N
000bed6d  J(NZk(N
000bedb1  J(NZk(N
000bedf5  J(NZk(N
000bee39  J(NZk(N
000bee7d  J(NZk(N
000beecd  J(NZk(N
000bef11  J(NZk(N
000bef61  J(NZk(N
000befa5  J(NZk(N
000bf145  J(NZk(ND
000bf1c1  J(NZk(ND
000bf23d  J(NZk(ND
000bf2b9  J(NZk(ND
000bf335  J(NZk(ND
000bf3b1  J(NZk(ND
000bf42d  J(NZk(ND
000bf4a1  J(NZk(N
000bf4fd  J(NZk(N
000bf551  J(NZk(N
000bf595  J(NZk(N
000bf5e5  J(NZk(N
000bf629  J(NZk(N
000bfc31  J(NZk(N
000bfcb1  J(NZk(N
000bfd31  J(NZk(N
000bfdb1  J(NZk(N
000bfe31  J(NZk(N
000bfeb1  J(NZk(N
000bff35  J(NZk(N
000bffa5  J(NZk(N
000c0001  J(NZk(N
000c0055  J(NZk(N
000c0099  J(NZk(N
000c00e9  J(NZk(N
000c012d  J(NZk(N
000c08b0  RRRRRRRRRRRRRRRR
000c08eb  oCh@LB
000c08fb  nAH(N!
000c095f  oCh@L 
000c0977  nAH(N!
000c09ef  oCh@L 
000c0a03  nAH(N!
000c2666  AoBTAO
000c301c  _h(8Hhi
000c31a1  H(NBh(N
000c31a9  H(Nch(N
000c3d34  JAB9j%
000c47e3  TNE@9.
000c4ef8  @)CzA'
000c5bbc  JAB9j%
000c6f0c  JAB9j%
000d6671  y6xhA%
000db777  Tv*Xyh
000dbfc7  Thfp9)
000dbfd3  Khf09hfp9)
000de06f  Thbp9H
000deee3  Rhb09h*2
000df6e4  iZp9jVp9kRp9
000e0cce   6irp9)
000e1df3  4vrp9hnp9
000e1e07  Rhnp9h
000e7a53  Thnp9Hl
000e8b07  Thzp9(
000eae63  5hzp9hC
000eb10f  Tjzp9J*
000ed9b1  0@9Kyk
000f1f75  "@9Ilu
001025df  TLQ@9MU@9NY@9J]@9
0010ab24  s0@9Kys
0011c002  AGKCTS
00144014  __start
```
