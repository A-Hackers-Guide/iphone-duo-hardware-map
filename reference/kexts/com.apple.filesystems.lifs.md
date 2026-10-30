# `com.apple.filesystems.lifs`

- Name: lifs
- Version: `1`
- UUID: `87D05774-1009-3F79-AE66-D7D98BE2D66F`
- Source version: `974.40.12.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 14.1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 14.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### com.apple.filesystems.lifs
- `CFBundleIdentifier`: `com.apple.filesystems.lifs`
- `IOClass`: `com_apple_filesystems_lifs`
- `IOMatchCategory`: `com_apple_filesystems_lifs`
- `IOPersonalityPublisher`: `com.apple.filesystems.lifs`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `IOUserClientClass`: `AppleLIFSUserClient`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleLIFSUserClient` | 0x140 | IOUserClient → IOService → IORegistryEntry |
| `IOCancelationWrapper` | 0x28 |  |
| `IOWrappedMemoryDescriptor` | 0x38 | IOCancelationWrapper |
| `com_apple_filesystems_lifs` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000054c8 off=0x00e17440-0x00e1c908 addr=0xfffffe0007e1b440-0xfffffe0007e20908 r--/r--   __TEXT            
	sz=0x00001ffc off=0x00e17ba8-0x00e19ba4 addr=0xfffffe0007e1bba8-0xfffffe0007e1dba4               __TEXT.__os_log           
	sz=0x00002a13 off=0x00e19ba4-0x00e1c5b7 addr=0xfffffe0007e1dba4-0xfffffe0007e205b7               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000348 off=0x00e1c5c0-0x00e1c908 addr=0xfffffe0007e205c0-0xfffffe0007e20908               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000219b4 off=0x03b957a0-0x03bb7154 addr=0xfffffe000ab997a0-0xfffffe000abbb154 r-x/r-x   __TEXT_EXEC       
	sz=0x00020a04 off=0x03b957a0-0x03bb61a4 addr=0xfffffe000ab997a0-0xfffffe000abba1a4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000fb0 off=0x03bb61a4-0x03bb7154 addr=0xfffffe000abba1a4-0xfffffe000abbb154          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000740 off=0x04a3ccb8-0x04a3d3f8 addr=0xfffffe000ba40cb8-0xfffffe000ba413f8 rw-/rw-   __DATA            
	sz=0x00000578 off=0x04a3ccb8-0x04a3d230 addr=0xfffffe000ba40cb8-0xfffffe000ba41230               __DATA.__data             
	sz=0x00000138 off=0x00000000-0x00000138 addr=0xfffffe000ba41230-0xfffffe000ba41368               __DATA.__common           (Zerofill)
	sz=0x00000090 off=0x00000000-0x00000090 addr=0xfffffe000ba41368-0xfffffe000ba413f8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002f30 off=0x014bf088-0x014c1fb8 addr=0xfffffe00084c3088-0xfffffe00084c5fb8 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x014bf088-0x014bf0a0 addr=0xfffffe00084c3088-0xfffffe00084c30a0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x014bf0a0-0x014bf0b8 addr=0xfffffe00084c30a0-0xfffffe00084c30b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001768 off=0x014bf0b8-0x014c0820 addr=0xfffffe00084c30b8-0xfffffe00084c4820         __DATA_CONST.__const            
	sz=0x00000e40 off=0x014c0820-0x014c1660 addr=0xfffffe00084c4820-0xfffffe00084c5660         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x014c1660-0x014c1750 addr=0xfffffe00084c5660-0xfffffe00084c5750         __DATA_CONST.__kalloc_var       
	sz=0x000007d8 off=0x014c1750-0x014c1f28 addr=0xfffffe00084c5750-0xfffffe00084c5f28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x014c1f28-0x014c1fb0 addr=0xfffffe00084c5f28-0xfffffe00084c5fb0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x014c1fb0-0x014c1fb8 addr=0xfffffe00084c5fb0-0xfffffe00084c5fb8         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 519 at 0x04b0017c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     87D05774-1009-3F79-AE66-D7D98BE2D66F
008: LC_SOURCE_VERSION           974.40.12.0.0
009: LC_FUNCTION_STARTS          offset=0x004acef00 size=0x2f0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `lifs`
- `CFBundleIdentifier`: `com.apple.filesystems.lifs`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `lifs`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/lifs.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891023296`
- `_PrelinkExecutableRelativePath`: `lifs`
- `_PrelinkExecutableSize`: `173292`
- `_PrelinkExecutableSourceAddr`: `-2198891023296`
- `_PrelinkKmodInfo`: `-2198827955016`

## Strings (524) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `readdir:vp:%p:error on retry:%d`
- `Skipping %s`
- `NULL lifs mount`
- `%s: lifs_listxattr_send() failed, err: %d\n`
- `lifs_unmount (lmp %p) started`
- `get FS_FSATTR_MODULE_BUNDLE_ID got %d, string %s`
- `%s: lifs_readdir_send() failed, err: %d\n`
- `%s: thread %p starting for mount %p\n`
- `%s:inline_data: No buffer pool found for release`
- `%s:inline_data: buffer pool initialized: %u buffers, %lu MB total (async copy thread started)`
- `%s:inline_data: timed out waiting for %u buffers to be released - forcing cleanup`
- `Request ID %llx expected response via op %u but received it via %u`
- `%s:inline_data: Cached mapping is NULL!`
- `%s:inline_data: destroying buffer[%u] in state %d (expected FREE)`
- `%s:inline_data: Destroying buffer pool for mount %p`
- `%s:inline_data: Inline data proprties initialized for mount %p`
- `%s: suppressing error on dead port`
- `readdir:vp:%p:lifs_readdir_request:error:%d:bytesRead:%d\n`
- `%s: OSDynamicCast failed, client_object is not AppleLIFSUserClient`
- `lmp %p max_filesize 0x%llx`
- `Failed to mirror mount - error %d`
- `%s: lifs_mkdir_send() failed, err: %d\n`
- `%s: lifs_symlink_send() failed, err: %d\n`
- `%s:inline_data: copy failed for buffer[%u]: error %d`
- `%s: lmp %p freespace 0x%llx sync write enabled`
- `%s:inline_data: wrapped_desc->init failed for buffer %u`
- `%s:inline_data: iokit_make_ident_port failed for buffer %u`
- `Unexpected attribute type changed from %d to %d`
- `%s: lifs_lookupmed_send() failed, err: %d\n`
- `%s: lifs_getxattr_send() failed, err: %d\n`
- `Failed to allocate fsids buffer.`
- `%s: lmp %p freespace 0x%llx`
- `lifs_u2_req no port\n`
- `%s: lifs_getfsattr_send() failed, err: %d\n`
- `Invalid mmap flags`
- `Missing target node`
- `%s: extent range [%llu:%llu] doesn't overlap with range [%llu:%u]`
- `%s:inline_data: all buffers successfully released`
- `%s:inline_data: buffer pool init failed %d, disabling inline data`
- `%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found`
- `%s: lifs_clonefile_send() failed, err: %d\n`
- `readdir:start:vp:%p:lnode:%p:cookie:0x%llx:verifier:0x%llx\n`
- `%s:inline_data: failed to create buffer %u, error %d`
- `%s:inline_data: prepare failed %d for buffer %u`
- `%s: lifs_unmount_send() failed, err: %d\n`
- `%s: lifs_get_volume_port_send() failed, err: %d\n`
- `%s: lifs_removexattr_send() failed, err: %d\n`
- `%s: preallocate returned invalid extents count %d`
- `%s: returning user task %p from client %p`
- `%s:inline_data: creating buffer pool: %u buffers x %lu bytes`
- `Failed to create trigger vnode`
- `%s: got %d from msleep, giving up with EIO`
- `%s:inline_data: buffer[%u] still in active list during pool destroy (state=%d)`
- `lifs_unmount_request returned err %d`
- `%s: lifs_setfsattr_send() failed, err: %d\n`
- `%s: lifs_remove_send() failed, err: %d\n`
- `%s: lifs_reclaim_send() failed, err: %d\n`
- `%s: lifs_endio_send() failed, err: %d\n`
- `LIFS: PID %d listxattr on requested size %zd`
- `Invalid file handle size`
- `Directory Entry name not within entry bounds`
- `%s:inline_data: async copy thread stopped and work queue drained`
- `%s: caught a signal, giving up with %d`
- `%s: lifs_getattrlistbulk_send() failed, err: %d\n`
- `%s: lifs_access_send() failed, err: %d\n`
- `%s: lifs_create_namedstream_send()                         failed, err: %d\n`
- `%s:inline_data: all buffers destroyed`
- `%s:inline_data: releasing buffer[%u] in unexpected state %d (expected READY)`
- `Failed to copy mount arguments`
- `%s: lifs_close_send() failed, err: %d\n`
- `%s:inline_data: buffer-to-UPL copy failed: %d`
- `Got error during mount request: %d`
- `Missing lifs mount`
- `%s: lifs_create_send() failed, err: %d\n`
- `%s: lifs_setattr_send() failed, err: %d\n`
- `%s: request %llu was claimed by a reply while giving up with error %d, awaiting that reply's completion`
- `%s: fail to create stream node [%d]`
- `%s: attributes update returned error %d`
- `%s:inline_data: pool exhausted: free=%u allocated=%u`
- `%s: isssd %u devblksize %u devreadsize %d devwritesize %d maxreadcnt %u segreadcnt %u maxwritecnt %u segwritecnt %u mnt_flags 0x%llx\n`
- `Failed to remove lifs`
- `%s: lifs_statfs_send() failed, err: %d\n`
- `%s: lifs_link_send() failed, err: %d\n`
- `%s: lifs_lookup_namedstream_send()                         failed, err: %d\n`
- `%s: xattr size %zu (%s) too large`
- `%s:inline_data: UPL copy failed %d, using default submit IO`
- `lifs_u_req no port\n`
- `%s: lifs_rename_send() failed, err: %d\n`
- `%s: thread %p exiting for mount %p\n`
- `%s: fail to create node [%d]`
- `%s: incorrect extent (type %d range [%llu:%u]) returned for write operation`
- `%s: lnode %p flags 0x%x offset %llu length %llu status %u ope_id %llu error %d\n`
- `Failed to open block device %s, err: %d`
- `readdir:bytesRead:%d`
- `%s (lmp %p) vflush returned err %d`
- `lifs_unmount (lmp %p) done`
- `Skipping directory entry contains '/': %.*s`
- `%s: lifs_unmount2_send() failed, err: %d\n`
- `%s: lifs_lookup_send() failed, err: %d\n`
- `%s: lifs_open_send() failed, err: %d\n`
- `%s:inline_data: vm_allocate failed %d for buffer %u`
- `%s:inline_data: createMappingInTask failed %d for buffer %u`
- `Failed to query mountpoint`
- `%s: lifs_remove_namedstream_send()                         failed, err: %d\n`
- `Request ID %llx returned %u bytes for buffer sized %u`
- `LIFS: PID %d getxattr on '%s'`
- `%s:inline_data:   forcefully releasing buffer[%u] in state %d`
- `%s: lifs_attach_mount_to_iouc_volume returned err %d\n`
- `readdir:finish:offset:%llx:numdirentries:%d:eof:%d:error:%d\n`
- `Missing lifs node to remove`
- `%s:inline_data: failed to start copy thread, error %d`
- `Found %d dangling mount(s).`
- `%s: lifs_seek_send() failed, err: %d\n`
- `Missing lifs node`
- `%s:inline_data: buffer[%u] created: kern_addr=%p user_addr=%llx port=%p size=%lu`
- `%s:uid:%u:gid:%u`
- `Failed to start unmount dangling thread, kern_return %d`
- `%s: lifs_rmdir_send() failed, err: %d\n`
- `%s() failed, err: %d\n`
- `readdir:vp:%p:invalid:entry:length:%d`
- `%s: lifs_readlink_send() failed, err: %d\n`
- `%s: lifs_write_send() failed, err: %d\n`
- `%s: lmp %p req %p reqid %llu\n`
- `%s: pageout called with UPL created`
- `LIFS: PID %d getxattr on '%s' requested size %zd`
- `%s:inline_data: No pooled buffer found, continue`
- `%s:inline_data: new IOWrappedMemoryDescriptor failed for buffer %u`
- `%s (lmp %p) is busy (usecount: %d)`
- `%s: lnode %p file_size(0x%llx) != valid_data_size(0x%llx) in non-VDL mode`
- `Failed to create root vnode`
- `%s:inline_data: Clearing user_task reference for mount %p`
- `%s: lmp %p freespace 0x%llx sync write disabled`
- `%s: Unsupported extent clone policy [%d]`
- `%s:inline_data: destroying %u buffers from free list`
- `%s:inline_data: withAddressRange failed for buffer %u`
- `%s:inline_data: getCachedMapping returned NULL for buffer %u`
- `%s: Got block_size = 0. Using the device's block size instead.`
- `%s: failed to find request for op %u with id %llu`
- `Failed to start lifs endio thread for mount %p kern_return %d`
- `%s: lifs_get_volume_port_request returned err %d\n`
- `%s: msleep says it got wakeup, but request not done, going back to sleep`
- `%s: lifs_mount_send() failed, err: %d\n`
- `%s: lifs_getattr_send() failed, err: %d\n`
- `readdir:vp:%p:retrying with new verifier:%llx\n`
- `Unable to retrieve updated attrs from created directory`
- `Failed to start lifs IO thread for mount %p kern_return %d`
- `throttle_info_create() failed`
- `%s:inline_data: destroying buffer pool`
- `%s: lifs_lookupsmall_send() failed, err: %d\n`
- `%s: lifs_pathconf_send() failed, err: %d\n`
- `%s: lifs_read_send() failed, err: %d\n`
- `%s: we got no buffer to copyin, but requested to copyin, returning EIO`
- `%s: timed out, giving up with %d`
- `Failed to set mnt_devvp on the mount point: %d`
- `%s: lifs_setxattr_%s_send() failed, err: %d\n`
- `readdir:verifier changed without error:cookie:0x%llx:cookie_verifier:0x%llx:lnode->dir_verifier:0x%llx:reply_data.verifier:0x%llx\n`
- `Invalid lifs host port or port dying`
- `Failed to create vnode`
- `%s: lifs_blockmap_file_send() failed, err: %d\n`
- `readdir:bytes_left:%d:de_nextrec:%d:error:%d`
- `%s: no extent found for lnode %p offset %lld size %u`
- `%s:inline_data: waiting for %u buffers to be released`
- `Failed to add lifs`
- `Failed to start lifs request thread for mount %p kern_return %d`
- `%s: pagein called with UPL created`

**[__TEXT.__cstring]**

- `lifs_read_request_async`
- `lifs_read_wrapped_request_async`
- `lifs_get_volume_port_request`
- `._%s`
- `lifs_io_thread_start`
- `lifs_copy_from_pooled_buffer_to_upl`
- `lifs_dispatch_async_endio`
- `%s: mount %p volume %p client %p device: %s\n`
- `_N_SYNC`
- `lifs_req_callback_thread`
- `lifs_vnop_clonefile`
- `lifs_get_user_task_from_client`
- `_O_vol_attributes_attr`
- `lifs:/`
- `lifs_reclaim_request`
- `\"%s: totalentries overflowed\" @%s:%d`
- `%s: client %p pid: %d pidversion: %d supportBlockResource: %d\n`
- `11212111`
- `lifs_mirror_mount_trigger_rearm`
- `IOWrappedMemoryDescriptor`
- `lifs_vnop_pageout`
- `lifs_vnop_getattrlistbulk`
- `lifs_submit_io`
- `11111222222222`
- `lifs_getattrlistbulk_request`
- `lifs_close_request`
- `1121121223222222222222`
- `%s: vfs_unmountbyfsid for mount_ref %llu returned error %d\n`
- `lifs_wait_req_completion_with_params`
- `122`
- `%s: Not privileged (no fsmodule entitlement)\n`
- `%s: write_meta_delayed failed with err %d (device: %s buffer: %p offset: 0x%llx length: 0x%lx)\n`
- `%s: read_meta failed with err %d (device: %s buffer %p offset: 0x%llx length: 0x%lx)\n`
- `lifs_vnop_write`
- `lifs_vnop_mkdir`
- `site.lifs_pooled_buffer_t`
- `/dev/`
- `Largest IO size to submit inline in lifs_vnop_strategy (4KB-2MB)`
- `_O_f_uuid`
- `lifs_mount_request`
- `disk`
- `lifs_request_done`
- `lifs_endio_thread_start`
- `%s: purge_meta_blocks failed with err %d (device: %s)\n`
- `111212222`
- `lifs_release_buffer`
- `_N_f_subtype`
- `lifs_readdir_cached`
- `site.struct dirent`
- `ALUC:clientDied(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_block_resource %d\n`
- `methodPurgeMetaBlocks`
- `write_meta_cache_hit`
- `lifs_update_freespace`
- `\"%s: numentries overflowed\" @%s:%d`
- `lifs_update_attrs_if_needed`
- `lifs_iokit.cpp`
- `AppleLIFSUserClient`
- `com.apple.developer.fskit.fsmodule`
- `%s: unknown or unauthorized mount_reference %u\n`
- `lifs_destroy_pooled_buffer`
- `lifs_get_supported_xattrs`
- `site.lifsnode`
- `lifs_flush_async_endio`
- `methodCloseKernelFD`
- `\"%s: blocks_purged overflowed\" @%s:%d`
- `\"could not stop lifs kext!\" @%s:%d`
- `%s: failed to get device vnode for fd %d, err: %d\n`
- `methodReadMeta`
- `112`
- `max_write_blockmap_size`
- `small`
- `lifs_vnop_create`
- `%s: write_meta_subblock failed with err %d (device: %s blockOffset: 0x%llx blockLength: 0x%lx buffer: %p offset: 0x%llx length: 0x%lx)\n`
- `lifs_add_extent`
- `Untitled`
- `N`
- `lifs_flush_meta`
- `lifs_endio_thread_stop`
- `methodSetClientDomain entered\n`
- `%s: no container found (pid %d pidversion %d)\n`
- `site.IOWrappedMemoryDescriptor`
- `lifs_cache_upgrade_send`
- `lifs_req_thread_start`
- `lifs_setxattr_request`
- `methodCreateVolumePort`
- `%s: no lifsnode found for fh\n`
- `methodFlushMeta`
- `site.lifs_extent_tree_t`
- `site.lifs_copy_work_t`
- `_N_INACTIVE`
- `lifs_remove_request`
- `lifs_write_request_async`
- `lifs_removexattr_request`
- `lifs_vnop_makenamedstream`
- `rdisk`
- `lifs_unmount`
- `_N_f_bsize`
- `lifs_cache_open_send`
- `%s: clear_meta_blocks failed with err %d (device: %s wait: %d)\n`
- `%s: client_object %p is not an AppleLIFSUserClient\n`
- `Largest run size that can be returned in lifs_vnop_blockmap for read (128KB-1MB)`
- `Dead volume`
- `IOCancelationWrapper`
- `lifs_req_thread_stop`
- `site.lifs_iouc_volume_t`
- `%s: failed to get block size for device %s, err: %d\n`
- `%s: flush_meta_blocks failed with err %d (device: %s wait: %d)\n`
- `11112222`
- `max_read_blockmap_size`
- `max_ssd_read_blockmap_size`
- `lifs_unmount_dangling`
- `lifs_setfsattr_request_async`
- `lifs_link_request`
- `lifs_getxattr_request`
- `\"%s: lnode->rdcount overflowed\" @%s:%d`
- `lifs_flush_async_io`
- `com.apple.private.fskit.moduleBundleID`
- `lifs_endio`
- `LIFS file system`
- `com.apple.FinderInfo`
- `%s: copyPortNameForObjectInTask for task %p object %p port %d error %d\n`
- `\"%s: extent_tree->count overflowed\" @%s:%d`
- `Max IO threads to perform IO submission asynchronously (1-8)`
- `_N_caps_interfaces`
- `lifs_wait_req_completion`
- `%s: node has declared limited xattr support, but we got an empty list\n`
- `\"%s: blocks_cleared overflowed\" @%s:%d`
- `lifs_purge_meta_blocks`
- `_N_f_vdl`
- `1211111212221212111111111111122222222211`
- `%s: no container found for pid %d pidversion %d\n`
- `1112`
- `lifs_remove_overlapping_extents`
- `site.struct lifs_mntargs`
- `max_read_size`
- `max_ssd_read_size`
- `lifs_vnop_strategy_done_pooled`
- `lifs_request_abort_all`
- `lifs_io_strategy_thread`
- `ALUC:externalMethod: no entitlement for selector %d\n`
- `%s: no volume found for client %p in container %p with fd %d\n`
- `LU`
- `force_vfs_xattr_emulation`
- `lifs_mirror_mount_trigger_resolve`
- `com.apple.ResourceFork`
- `11112222222222222222`
- `site.lifs_koio_context_t`
- `%s: lifs_apply_cache_action failed with error %d\n`
- `methodClearMetaBlocks`
- `lifs_destroy_iouc_volume`
- `unknown`
- `lifs_lookup_named_stream_request`
- `ALUC:externalMethod: no provider or not active\n`
- `%s: copyObjectForPortNameInTask for port %d returned %d\n`
- `%s: write_meta failed with err %d (device: %s buffer: %p offset: 0x%llx length: 0x%lx)\n`
- `methodWriteMetaAsync`
- `site.struct lifs_uc_mount_entry`
- `%s: node has declared limited xattr support, but we got an error: %d\n`
- `lifs_flush_meta_blocks`
- `lifs_lookupmed_request`
- `lifs_open_request`
- `111122121111`
- `registerNotificationPort entered\n`
- `max_io_threads`
- `hw.ncpu`
- `site.lifs_mntargs`
- `methodGetMapping`
- `site.lifs_buffer_pool_t`
- `\"%s: io_lock_override is already set for lnode %p by thread %p\" @%s:%d`
- `lifs_create_request`
- `lifs_blockmap_file_request`
- `lifs_io_strategy`
- `lifs_wait_for_device_idle`
- `_N_caps_format`
- `lifs_set_io_lock_override`
- `lifs_endio_request`
- `\"%s: page %d is NOT dirty!\" @%s:%d`
- `methodSetCacheState`
- `%s: all %u volume(s) unmounted successfully\n`
- `221111122112222`
- `lifs_node`
- `_N_f_bavail`
- `site.lifs_sillyrename_entry`
- `\"%s: endio_flushed overflowed\" @%s:%d`
- `12121`
- `void IOCancelationWrapper::stopUsingObjectAndRelease(OSObject *)`
- `lifs_access_request`
- `ALUC:externalMethod: selector %d >= count %d\n`
- `none`
- `%s: caller lacks fsmodule entitlement\n`
- `%s: invalid volume count %u\n`
- `lifs_attach_mount_to_iouc_volume`
- `lifs`
- `read_meta_cache_hit`
- `lifs_rw`
- `lifs_getattr`
- `%s%s`
- `/..namedfork/rsrc`
- `%s: supported xattrs list size is not reasonable: %llu\n`
- `%s called when use count was zero`
- `lifs_endio_done`
- `site.AppleLIFSUserClient`
- `%s: invalid vnode type %d name %s for fd %d, err: %d\n`
- `lifs_destroy_iouc_container`
- `_S_f_location`
- `lifs_readlink_request`
- `methodReadMetaWithRA`
- `%s: flush_meta failed with err %d (device: %s wait: %d)\n`
- `%s: container %p removed (pid %d pidversion %d)\n`
- `_N_supported_xattr_namessize`
- `lifs_io_thread_stop`
- `%s: write_meta_async failed with err %d (device: %s buffer: %p offset: 0x%llx length: 0x%lx)\n`
- `lifs_get_volume_by_fd`
- `lifs_get_buffer_from_pool`
- `lifs_getattr_request`
- `lifs_vnops.c`
- `222222222222222222222222222222222222222222222222222222222222222222211112221112222112222222222222222222222222222222121212211222222`
- `lifs_enable_lowspace_sync_write`
- `%s: kernel unmount successful for mount_ref %llu\n`
- `_S_f_vol_name`
- `IU`
- `max_ssd_write_blockmap_size`
- `Largest run size that can be returned in lifs_vnop_blockmap for SSD write (128KB-1MB)`
- `lifs_query_mountpoint`
- `lifsbusywant`
- `://`
- `\"%s: io_lock_override is not set for lnode %p\" @%s:%d`
- `lifs_clear_io_lock_override`
- `lifs_setfsattr_request`
- `lifs_symlink_request`
- `12`
- `max_write_size`
- `lifs_mkdir_request`
- `lifs_write_wrapped_request_async`
- `\"%s: lnode->wrcount overflowed\" @%s:%d`
- `lifs_koio_blockmap`
- `lifs_lookup_request`
- `_O_f_preallocate`
- `lifs_seek_request`
- `site.lifs_endio_context_t`
- `lifs_get_extent_layout`
- `\"%s: lnode %p async_endio_inflights (%d) < 0\" @%s:%d`
- `12111112122212121`
- `%s: vnode %p isn't a regular file or a directory\n`
- `lifs_remove_named_stream_request`
- `\"%s: lnode %p vp %p async_io_inflights (%d) < 0\" @%s:%d`
- `com_apple_filesystems_lifs`
- `%s: read_meta_with_ra failed with err %d (device: %s buffer %p offset: 0x%llx length: 0x%lx ra_list: %p ra_count: %d)\n`
- `Max size for non-SSD read (1MB-8MB)`
- `_N_mntflags`
- `_S_module_bundle_id`
- `\"%s: lnode->trigseq overflowed\" @%s:%d`
- `lifs_req_callback`
- `%s: got error (%d) trying to increment iocount\n`
- `Largest run size that can be returned in lifs_vnop_blockmap for write (128KB-1MB)`
- `lifs_rename_request`
- `lifs_vnop_open`
- `%s: No mount reference in file handle\n`
- `lifs_init_buffer_pool`
- `%s: supported xattr names list not NUL terminated\n`
- `lifs_lookupsmall_request`
- `lifs_vnop_allocate`
- `site.lifs_reclaim_context_t`
- `%s: set cache state for vnode %p (ref:%u -> idx:%u mode:%d coherency:%d action:%d)\n`
- `site.lifsmount`
- `_B_has_perm_enforcement`
- `lifs_pathconf_request`
- `lifs_listxattr_request`
- `\"%s: lnode->rwcount overflowed\" @%s:%d`
- `\"%s: lmp %p async_endio_inflights (%d) < 0\" @%s:%d`
- `methodKernelUnmount`
- `%s: triggering vfs_unmountbyfsid for mount_ref %llu (mount %p)\n`
- `lifs_abandon_sync_req`
- `lifs_vnop_strategy_done`
- `com.apple.filesystems.kernelOffloadedIOClient`
- `methodOpenKernelFD`
- `site.lifs_request_t`
- `site.com_apple_filesystems_lifs`
- `com.apple.private.LiveFS.setmachport`
- `%s: new container %p added (pid %d pidversion %d)\n`
- `site.IOCancelationWrapper`
- `lifs_statfs_request`
- `lifs_clonefile_request`
- `lifs_readdir_request`
- `lifs_cache_close_send`
- `lifs_vnop_readdir`
- `_N_PC_XATTR_SIZE_BITS`
- `site.lifs_extent_t`
- `_O_supported_xattr_names`
- `1111`
- `lifs_endio_thread`
- `site.lifs_iouc_container_t`
- `lifs_destroy_buffer_pool`
- `112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `lifs_getfsattr_request`
- `%s: triggering kernel unmount for %u volume(s) with flags 0x%x\n`
- `lifs_uc_add_mount`
- `%s: mismatched pid/pidversion, userClient (pid: %d pidversion: %d) configUC (pid: %d pidversion: %d)\n`
- `lifs_subr.c`
- `%s: failed to get supported xattr names: %d\n`
- `lnode_larval`
- `methodFlushMetaBlocks`
- `lifs_extent.c`
- `111222222222222222122222222222222212111111111222222222222222211212222222112221`
- `_S_f_type`
- `/`
- `lifs_vnop_symlink`
- `ALUC:init(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_block_resource %d\n`
- `lifs_close_device`
- `Largest run size that can be returned in lifs_vnop_blockmap for SSD read (128KB-1MB)`
- `NO-NAME`
- `%s: duplicate volume found (client %p fd %d) in container %p\n`
- `lifs_wait_for_copy_completion`
- `lifs_buffer_pool_copy_thread`
- `lifs_kext`
- `max_inline_io_size`
- `Max size for SSD read (1MB-16MB)`
- `I`
- `lifs_mirror_mount_trigger_unresolve`
- `lifs_unmount_request`
- `site.struct direntry`
- `%s: add volume %p client %p container %p (fd: %d device: %s fmode: 0x%x blocksize: 0x%x)\n`
- `lifs_create_pooled_buffer`
- `Max size for SSD write (1MB-8MB)`
- `lifs_setup_mount_for_devvp`
- `lifs_clear_meta_blocks`
- `lifs_create_named_stream_request`
- `%s: invalid mount_reference 0 at index %u\n`
- `%s: no mount found for mount_ref %llu (idx %u)\n`
- `lifs_mount`
- `Max size for non-SSD write (1MB-4MB)`
- `lifs_unmount2_request`
- `lifs_rmdir_request`
- `.nfs.%08x.%04x`
- `site.lifs_setfsattr_context_t`
- `%s: No LiveFS file handle provided\n`
- `%s: registered mount_reference %u -> mount_index %u for IOUC %p\n`
- `lifs_create_iouc_container`
- `lifs_buffer_pool_copy`
- `lifs_vnop_pagein`
- `methodGetVolumePortReply`
- `addMountEntry`
- `%s passed object other than object shared`
- `%s: failed to unmount all volumes, unmounted %u of %u volume(s)\n`
- `methodWriteMeta`
- `methodWriteMetaSubBlock`
- `/dev/%s`
- `_B_has_access_check`
- `methodConfigureUserClient`
- `%s: remove volume %p client %p container %p (fd: %d device: %s fmode: 0x%x)\n`
- `1212111`
- `large`
- `site.lifs_strategy_desc_t`
- `lifs_vnop_close`
- `site.fsid_t`
- `lifs_setattr_request`
- `methodWriteMetaDelayed`
- `max_ssd_write_size`
- `\"%s: blocks_flushed overflowed\" @%s:%d`
