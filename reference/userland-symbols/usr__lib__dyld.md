# Symbols: `/usr/lib/dyld`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/usr__lib__dyld.md). **[DSC]**

3 public symbols, 3,893 private symbols, 0 undefined (imported).

## Public (external)

```
0x1804829a0  __TEXT,__text  __dyld_start
0x1edfb2600  __DATA_DIRTY,__all_image_info  _dyld_all_image_infos
0x180499560  __TEXT,__text  _lldb_image_notifier
```

## Private

```
0x18047e000  __TEXT,__text  dyld4::APIs::_dyld_objc_class_count()
0x18047e07c  __TEXT,__text  dyld4::APIs::dyld_program_sdk_at_least(dyld_build_version_t)
0x18047e154  __TEXT,__text  mach_o::Platform::empty() const
0x18047e174  __TEXT,__text  dyld4::APIs::dyld_get_active_platform()
0x18047e1d4  __TEXT,__text  mach_o::Platform::Platform(unsigned int)
0x18047e230  __TEXT,__text  mach_o::Platform::value() const
0x18047e248  __TEXT,__text  dyld4::APIs::findImageMappedAt(void const*, mach_o::UnsafeHeader const**, bool*, char const**, void const**, unsigned long long*, unsigned char*, dyld4::Loader const**)
0x18047e648  __TEXT,__text  DyldSharedCache::forEachRange(void  block_pointer(char const*, unsigned long long, unsigned long long, unsigned int, unsigned long long, unsigned int, unsigned int, bool&), void  block_pointer(DyldSharedCache const*, unsigned int)) const
0x18047e784  __TEXT,__text  invocation function for block in DyldSharedCache::forEachRange(void  block_pointer(char const*, unsigned long long, unsigned long long, unsigned int, unsigned long long, unsigned int, unsigned int, bool&), void  block_pointer(DyldSharedCache const*, unsigned int)) const
0x18047e85c  __TEXT,__text  dyld4::APIs::dyld_image_header_containing_address(void const*)
0x18047e8dc  __TEXT,__text  DyldSharedCache::forEachCache(void  block_pointer(DyldSharedCache const*, bool&)) const
0x18047e9b4  __TEXT,__text  DyldSharedCache::mappedSize() const
0x18047ea98  __TEXT,__text  DyldSharedCache::forEachRegion(void  block_pointer(void const*, unsigned long long, unsigned long long, unsigned int, unsigned int, unsigned long long, unsigned long long, bool&)) const
0x18047ebc0  __TEXT,__text  DyldSharedCache::unslidLoadAddress() const
0x18047ebf0  __TEXT,__text  __platform_strncmp
0x18047ebf0  __TEXT,__text  __platform_strncmp
0x18047ed10  __TEXT,__text  __platform_strcmp
0x18047ed10  __TEXT,__text  __platform_strcmp
0x18047ed24  __TEXT,__text  __platform_strcmp_noMTE
0x18047edf8  __TEXT,__text  __Block_object_dispose
0x18047ee40  __TEXT,__text  __platform_strnlen
0x18047ee40  __TEXT,__text  __platform_strnlen
0x18047eee0  __TEXT,__text  __platform_strlen
0x18047eee0  __TEXT,__text  __platform_strlen
0x18047ef40  __TEXT,__text  objc::lookup8(unsigned char const*, unsigned long, unsigned long long)
0x18047f260  __TEXT,__text  dyld4::APIs::_dyld_for_each_objc_class(char const*, dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>)
0x18047f3bc  __TEXT,__text  void dyld3::MultiMapBase<prebuilt_objc::ObjCStringKeyOnDisk, prebuilt_objc::ObjCObjectOnDiskLocation, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk>::forEachEntry<char const*>(dyld3::Array<unsigned long long> const&, dyld3::Array<dyld3::MultiMapBase<prebuilt_objc::O
0x18047f65c  __TEXT,__text  dyld4::APIs::_dyld_get_objc_selector(char const*)
0x18047f71c  __TEXT,__text  invocation function for block in DyldSharedCache::forEachRange(void  block_pointer(char const*, unsigned long long, unsigned long long, unsigned int, unsigned long long, unsigned int, unsigned int, bool&), void  block_pointer(DyldSharedCache const*, unsigned int)) const
0x18047f874  __TEXT,__text  DyldSharedCache::mappingName(unsigned int, unsigned long long)
0x18047f94c  __TEXT,__text  invocation function for block in dyld4::APIs::findImageMappedAt(void const*, mach_o::UnsafeHeader const**, bool*, char const**, void const**, unsigned long long*, unsigned char*, dyld4::Loader const**)
0x18047f980  __TEXT,__text  invocation function for block in dyld4::APIs::findImageMappedAt(void const*, mach_o::UnsafeHeader const**, bool*, char const**, void const**, unsigned long long*, unsigned char*, dyld4::Loader const**)
0x18047fa34  __TEXT,__text  dyld4::APIs::_dyld_is_memory_immutable(void const*, unsigned long)
0x18047fb94  __TEXT,__text  dyld4::RuntimeState::inPermanentRange(unsigned long, unsigned long, unsigned char*, dyld4::Loader const**)
0x18047fc08  __TEXT,__text  prebuilt_objc::forEachClass(dyld4::RuntimeState*, dyld3::MultiMapView<prebuilt_objc::ObjCStringKeyOnDisk, prebuilt_objc::ObjCObjectOnDiskLocation, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk> const&, char const*, void  block_pointer(dyld3::Array<dyld4::PrebuiltLoa
0x18047fc8c  __TEXT,__text  objc::ObjectHashTable::forEachObject(char const*, void  block_pointer(unsigned long long, unsigned short, bool&)) const
0x18047fdd8  __TEXT,__text  DyldSharedCache::forEachImageTextSegment(void  block_pointer(unsigned long long, unsigned long long, unsigned char const*, char const*, bool&)) const
0x18047fe74  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_is_memory_immutable(void const*, unsigned long)
0x18047fef4  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_is_memory_immutable(void const*, unsigned long)
0x18047ff44  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_for_each_objc_class(char const*, dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>)
0x18047ffdc  __TEXT,__text  void dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>::operator()<unsigned char*, bool, bool*>(unsigned char*&&, bool&&, bool*&&) const
0x180480244  __TEXT,__text  lsl::MemoryManager::memoryManager()
0x18048026c  __TEXT,__text  lsl::ProtectedStack::onStackInCurrentFrame() const
0x1804802b4  __TEXT,__text  dyld4::APIs::_dyld_find_protocol_conformance_on_disk(void const*, void const*, void const*, unsigned int)
0x180480524  __TEXT,__text  dyld4::PrebuiltLoaderSet::hasOptimizedSwift() const
0x18048054c  __TEXT,__text  mach_o::Header::fromDyldMapped(mach_header const*)
0x180480574  __TEXT,__text  objc::objc_headeropt_rw_t::isLoaded(unsigned int) const
0x1804805a8  __TEXT,__text  mach_o::Image::makeFromDyldMapped(mach_header const*)
0x180480708  __TEXT,__text  mach_o::Header::forEachSegment(void  block_pointer(mach_o::Header::SegmentInfo const&, bool&)) const
0x180480864  __TEXT,__text  invocation function for block in mach_o::Header::forEachSegment(void  block_pointer(mach_o::Header::SegmentInfo const&, bool&)) const
0x1804809e4  __TEXT,__text  mach_o::Header::forEachLoadCommand(void  block_pointer(mach_o::Header::LoadCommandInfo const&, bool&), mach_o::Error*) const
0x180480b78  __TEXT,__text  start
0x1804829b4  __TEXT,__text  dyld4::restartWithDyldInCache(dyld4::KernelArgs const*, mach_o::UnsafeHeader const*, DyldSharedCache const*, unsigned long long, void*)
0x1804829bc  __TEXT,__text  _mach_continuous_time
0x180482a64  __TEXT,__text  dyld3::kdebug_trace_dyld_marker(unsigned int, dyld3::kt_arg, dyld3::kt_arg, dyld3::kt_arg, dyld3::kt_arg)
0x180482be0  __TEXT,__text  ___kdebug_typefilter
0x180482c0c  __TEXT,__text  _kdebug_trace
0x180482c80  __TEXT,__text  ___kdebug_trace64
0x180482cac  __TEXT,__text  _kdebug_is_enabled
0x180482d70  __TEXT,__text  mach_o::UnsafeHeader::inDyldCache() const
0x180482d7c  __TEXT,__text  invocation function for block in mach_o::Image::makeFromDyldMapped(mach_header const*)
0x180482e30  __TEXT,__text  mach_o::Header::SegmentInfo mach_o::Header::parse_segment_command<true>(mach_o::Header::LoadCommandInfo const&, unsigned short, void  block_pointer(mach_o::Header::SegmentInfo const&, mach_o::Header::SectionInfo const&), mach_o::Error*) const
0x180483094  __TEXT,__text  mach_o::Header::is64() const
0x1804830c0  __TEXT,__text  mach_o::Header::chainedFixups() const
0x1804830e4  __TEXT,__text  mach_o::Image::chainedFixups() const
0x180483160  __TEXT,__text  mach_o::Header::linkeditRangeFor(unsigned int) const
0x180483300  __TEXT,__text  invocation function for block in mach_o::Header::linkeditRangeFor(unsigned int) const
0x180483428  __TEXT,__text  mach_o::Image::linkeditBytes(mach_o::Header::LinkEditRange) const
0x1804834c8  __TEXT,__text  mach_o::Header::parse_linkedit_data_command(mach_o::Header::LoadCommandInfo const&, mach_o::Error*) const
0x1804835e0  __TEXT,__text  mach_o::Header::isPreload() const
0x180483604  __TEXT,__text  mach_o::Header::getSlide() const
0x1804837c8  __TEXT,__text  invocation function for block in mach_o::Header::getSlide() const
0x18048381c  __TEXT,__text  mach_o::ChainedFixups::ChainedFixups(std::__1::span<unsigned char const, 18446744073709551615ul>)
0x180483828  __TEXT,__text  mach_o::Header::isObjectFile() const
0x18048384c  __TEXT,__text  hactivateRegion(bool, bool, unsigned long long, unsigned long long, unsigned long long)
0x180483950  __TEXT,__text  mach_o::Header::segmentVmAddr(unsigned int) const
0x180483b34  __TEXT,__text  mach_o::PointerMetaData::PointerMetaData(void const*, unsigned short)
0x180483c28  __TEXT,__text  mach_o::PointerMetaData::signPointer(unsigned long long, void*) const
0x180483c88  __TEXT,__text  __pthread_set_self_dyld
0x180483ce8  __TEXT,__text  ___thread_selfid
0x180483d14  __TEXT,__text  __thread_set_tsd_base
0x180483d24  __TEXT,__text  dyld4::KernelArgs::findApple() const
0x180483d64  __TEXT,__text  __simple_getenv
0x180483e0c  __TEXT,__text  dyld4::KernelArgs::findEnvp() const
0x180483e3c  __TEXT,__text  lsl::MemoryManager::init(char const**, char const**, void*)
0x180484020  __TEXT,__text  lsl::MemoryManager::MemoryManager(char const**, char const**, void*)
0x1804840ec  __TEXT,__text  _vm_allocate
0x1804842c8  __TEXT,__text  ___chkstk_darwin
0x1804842e0  __TEXT,__text  ____chkstk_darwin
0x1804842f0  __TEXT,__text  _memmove
0x1804842f0  __TEXT,__text  _memmove
0x1804842f0  __TEXT,__text  _memmove
0x1804845b8  __TEXT,__text  lsl::Allocator::Pool::Pool(lsl::Allocator*, lsl::Allocator::Pool*, lsl::MemoryManager::Buffer, lsl::MemoryManager::Buffer, bool, bool)
0x18048464c  __TEXT,__text  dyld4::PrebuiltLoader::BindTargetRef::value(dyld4::RuntimeState&) const
0x180484754  __TEXT,__text  dyld4::Loader::LoaderRef::loader(dyld4::RuntimeState const&) const
0x1804847b0  __TEXT,__text  dyld4::PrebuiltLoader::mf(dyld4::RuntimeState const&) const
0x1804847b0  __TEXT,__text  dyld4::PrebuiltLoader::mf(dyld4::RuntimeState const&) const
0x1804847d4  __TEXT,__text  dyld4::RuntimeState::appLoadAddress(unsigned short) const
0x18048480c  __TEXT,__text  dyld4::Loader::loadAddress(dyld4::RuntimeState const&) const
0x180484840  __TEXT,__text  murmurHash(void const*, int, unsigned long long)
0x180484920  __TEXT,__text  dyld4::APIs::_dyld_find_protocol_conformance(void const*, void const*, void const*) const
0x180484bec  __TEXT,__text  unsigned int SwiftHashTable::hash<SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484bec  __TEXT,__text  unsigned int SwiftHashTable::hash<SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484c68  __TEXT,__text  unsigned char SwiftHashTable::checkbyte<SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484c68  __TEXT,__text  unsigned char SwiftHashTable::checkbyte<SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484c7c  __TEXT,__text  bool SwiftHashTable::equal<SwiftTypeProtocolConformanceLocationKey, SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484c7c  __TEXT,__text  bool SwiftHashTable::equal<SwiftTypeProtocolConformanceLocationKey, SwiftTypeProtocolConformanceLocationKey>(SwiftTypeProtocolConformanceLocationKey const&, SwiftTypeProtocolConformanceLocationKey const&, unsigned char const*) const
0x180484c94  __TEXT,__text  lsl::ProtectedStack::getRange(void const*&, void const*&) const
0x180484cc8  __TEXT,__text  dyld4::APIs::_dyld_find_unwind_sections(void*, dyld_unwind_sections*)
0x180484ee0  __TEXT,__text  dyld4::APIs::mapFromVersionSet(dyld_build_version_t, mach_o::Platform)
0x180485080  __TEXT,__text  DyldSharedCache::inDyldCache(DyldSharedCache const*, mach_o::UnsafeHeader const*)
0x1804851a0  __TEXT,__text  mach_o::Header::header() const
0x1804851b8  __TEXT,__text  dyld4::APIs::dyld_sdk_at_least(mach_header const*, dyld_build_version_t)
0x1804852c8  __TEXT,__text  dyld4::APIs::getImagePlatformAndVersions(mach_o::UnsafeHeader const*)
0x180485384  __TEXT,__text  dyld4::APIs::_dyld_stack_range(void const**, void const**)
0x18048538c  __TEXT,__text  mach_o::Image::operator=(mach_o::Image const&)
0x1804853c0  __TEXT,__text  mach_o::Image::Image(mach_o::Image const&&)
0x1804853c0  __TEXT,__text  mach_o::Image::Image(mach_o::Image const&&)
0x18048540c  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_find_unwind_sections(void*, dyld_unwind_sections*)
0x180485500  __TEXT,__text  dyld4::APIs::_dyld_shared_cache_real_path(char const*)
0x180485568  __TEXT,__text  dyld4::ProcessConfig::canonicalDylibPathInCache(char const*) const
0x180485570  __TEXT,__text  dyld4::ProcessConfig::DyldCache::getCanonicalPath(char const*) const
0x1804855c4  __TEXT,__text  mach_o::GenericTrie::find(CString, bool) const
0x18048581c  __TEXT,__text  DyldSharedCache::hasImagePath(char const*, unsigned int&) const
0x180485928  __TEXT,__text  mach_o::PathToIntTrie::hasPath(CString, unsigned int&) const
0x1804859c0  __TEXT,__text  mach_o::GenericTrie::recursiveVisit(unsigned long, unsigned long, unsigned long, bool&, void  block_pointer(std::__1::span<unsigned char const, 18446744073709551615ul>, bool&), bool  block_pointer(CString, unsigned long long, unsigned long, unsigned long, bool&), mach_o::Error*) const
0x180485cb0  __TEXT,__text  __platform_memcmp
0x180485cb0  __TEXT,__text  __platform_memcmp
0x180485cb0  __TEXT,__text  __platform_memcmp
0x180485dd0  __TEXT,__text  lsl::Lock::unlock()
0x180485e38  __TEXT,__text  dyld4::ExternallyViewableState::ExternallyViewableState(lsl::Allocator&)
0x180485f18  __TEXT,__text  mach_o::Platform::basePlatform() const
0x180485f44  __TEXT,__text  invocation function for block in mach_o::Header::forEachSection(void  block_pointer(mach_o::Header::SectionInfo const&, bool&)) const
0x180486078  __TEXT,__text  mach_o::Header::forEachSection(void  block_pointer(mach_o::Header::SectionInfo const&, bool&)) const
0x1804861d4  __TEXT,__text  dyld4::ExternallyViewableState::ExternallyViewableState(lsl::Allocator&)
0x1804861d8  __TEXT,__text  CString::substr(unsigned long) const
0x180486220  __TEXT,__text  _bzero
0x180486220  __TEXT,__text  _bzero
0x180486220  __TEXT,__text  _bzero
0x180486280  __TEXT,__text  __platform_memset
0x180486280  __TEXT,__text  __platform_memset
0x180486354  __TEXT,__text  lsl::Allocator::AllocationMetadata::reserve(unsigned long long, bool)
0x180486438  __TEXT,__text  __subsystem_init
0x180486464  __TEXT,__text  lsl::MemoryManager::defaultAllocator()
0x18048648c  __TEXT,__text  hexStringPairToUInt64Pair(CString, unsigned long long&, unsigned long long&)
0x180486638  __TEXT,__text  FileIdTuple::getPath(char*) const
0x180486668  __TEXT,__text  lsl::Allocator::malloc(unsigned long long)
0x180486674  __TEXT,__text  lsl::Allocator::aligned_alloc(unsigned long long, unsigned long long)
0x180486828  __TEXT,__text  lsl::Lock::lock()
0x180486894  __TEXT,__text  DyldSharedCache::dynamicRegion() const
0x1804868dc  __TEXT,__text  _fsgetpath
0x180486908  __TEXT,__text  dyld4::SyscallDelegate::hasExistingDyldCache(unsigned long long&, FileIdTuple&) const
0x18048695c  __TEXT,__text  FileIdTuple::FileIdTuple(unsigned long long, unsigned long long)
0x18048695c  __TEXT,__text  FileIdTuple::FileIdTuple(unsigned long long, unsigned long long)
0x18048695c  __TEXT,__text  FileIdTuple::FileIdTuple(unsigned long long, unsigned long long)
0x180486964  __TEXT,__text  ___shared_region_check_np
0x180486990  __TEXT,__text  DyldSharedCache::DynamicRegion::getDyldCacheFileID(FileIdTuple&) const
0x1804869bc  __TEXT,__text  lsl::Allocator::AllocationMetadata::pool(bool) const
0x180486a50  __TEXT,__text  lsl::Allocator::AllocationMetadata::setPoolHint(lsl::Allocator::Pool*)
0x180486b2c  __TEXT,__text  lsl::Allocator::AllocationMetadata::firstAddress() const
0x180486b7c  __TEXT,__text  lsl::Allocator::AllocationMetadata::AllocationMetadata(lsl::Allocator::AllocationMetadata*, unsigned long long, unsigned long long, unsigned long long)
0x180486d34  __TEXT,__text  ___chkstk_darwin_probe
0x180486d60  __TEXT,__text  lsl::Allocator::Pool::aligned_alloc(unsigned long long, unsigned long long)
0x180486f64  __TEXT,__text  lsl::MemoryManager::init(char const**, char const**, void*)::$_0::operator()() const
0x1804871c4  __TEXT,__text  __kernelrpc_mach_vm_allocate_trap
0x1804871d0  __TEXT,__text  __kernelrpc_mach_vm_purgable_control_trap
0x1804871dc  __TEXT,__text  __kernelrpc_mach_vm_deallocate_trap
0x1804871e8  __TEXT,__text  _task_dyld_process_info_notify_get
0x1804871f4  __TEXT,__text  __kernelrpc_mach_vm_protect_trap
0x180487200  __TEXT,__text  __kernelrpc_mach_vm_map_trap
0x18048720c  __TEXT,__text  __kernelrpc_mach_port_allocate_trap
0x180487218  __TEXT,__text  __kernelrpc_mach_port_deallocate_trap
0x180487224  __TEXT,__text  __kernelrpc_mach_port_mod_refs_trap
0x180487230  __TEXT,__text  __kernelrpc_mach_port_move_member_trap
0x18048723c  __TEXT,__text  __kernelrpc_mach_port_insert_right_trap
0x180487248  __TEXT,__text  __kernelrpc_mach_port_insert_member_trap
0x180487254  __TEXT,__text  __kernelrpc_mach_port_extract_member_trap
0x180487260  __TEXT,__text  __kernelrpc_mach_port_construct_trap
0x18048726c  __TEXT,__text  __kernelrpc_mach_port_destruct_trap
0x180487278  __TEXT,__text  _mach_reply_port
0x180487284  __TEXT,__text  _thread_self_trap
0x180487290  __TEXT,__text  _task_self_trap
0x18048729c  __TEXT,__text  _host_self_trap
0x1804872a8  __TEXT,__text  _mach_msg_trap
0x1804872b4  __TEXT,__text  _mach_msg_overwrite_trap
0x1804872c0  __TEXT,__text  _semaphore_signal_trap
0x1804872cc  __TEXT,__text  _semaphore_signal_all_trap
0x1804872d8  __TEXT,__text  _semaphore_signal_thread_trap
0x1804872e4  __TEXT,__text  _semaphore_wait_trap
0x1804872f0  __TEXT,__text  _semaphore_wait_signal_trap
0x1804872fc  __TEXT,__text  _semaphore_timedwait_trap
0x180487308  __TEXT,__text  _semaphore_timedwait_signal_trap
0x180487314  __TEXT,__text  __kernelrpc_mach_port_get_attributes_trap
0x180487320  __TEXT,__text  __kernelrpc_mach_port_guard_trap
0x18048732c  __TEXT,__text  __kernelrpc_mach_port_unguard_trap
0x180487338  __TEXT,__text  _mach_generate_activity_id
0x180487344  __TEXT,__text  _task_name_for_pid
0x180487350  __TEXT,__text  _task_for_pid
0x18048735c  __TEXT,__text  _pid_for_task
0x180487368  __TEXT,__text  _mach_msg2_trap
0x180487374  __TEXT,__text  _macx_swapon
0x180487380  __TEXT,__text  _macx_swapoff
0x18048738c  __TEXT,__text  _thread_get_special_reply_port
0x180487398  __TEXT,__text  _macx_triggers
0x1804873a4  __TEXT,__text  _macx_backing_store_suspend
0x1804873b0  __TEXT,__text  _macx_backing_store_recovery
0x1804873bc  __TEXT,__text  _swtch_pri
0x1804873c8  __TEXT,__text  _swtch
0x1804873d4  __TEXT,__text  _syscall_thread_switch
0x1804873e0  __TEXT,__text  _clock_sleep_trap
0x1804873ec  __TEXT,__text  _mach_vm_reclaim_update_kernel_accounting_trap
0x1804873f8  __TEXT,__text  _host_create_mach_voucher_trap
0x180487404  __TEXT,__text  _mach_voucher_extract_attr_recipe_trap
0x180487410  __TEXT,__text  __kernelrpc_mach_port_type_trap
0x18048741c  __TEXT,__text  __kernelrpc_mach_port_request_notification_trap
0x180487428  __TEXT,__text  __exclaves_ctl_trap
0x180487434  __TEXT,__text  _mach_timebase_info_trap
0x180487440  __TEXT,__text  _mach_wait_until
0x18048744c  __TEXT,__text  _mk_timer_create
0x180487458  __TEXT,__text  _mk_timer_destroy
0x180487464  __TEXT,__text  _mk_timer_arm
0x180487470  __TEXT,__text  _mk_timer_cancel
0x18048747c  __TEXT,__text  _mk_timer_arm_leeway
0x180487488  __TEXT,__text  _debug_control_port_for_pid
0x180487494  __TEXT,__text  _thread_set_x86_64_compat
0x1804874a0  __TEXT,__text  ___guard_setup
0x180487560  __TEXT,__text  mach_o::Image::segmentCount() const
0x180487564  __TEXT,__text  mach_o::Header::segmentCount() const
0x18048760c  __TEXT,__text  invocation function for block in mach_o::Header::segmentCount() const
0x180487638  __TEXT,__text  mach_o::ChainedFixups::startsForSegment(unsigned int) const
0x180487670  __TEXT,__text  invocation function for block in mach_o::Header::segmentVmAddr(unsigned int) const
0x1804876bc  __TEXT,__text  _mach_init
0x180487768  __TEXT,__text  __pthread_set_self
0x1804877d4  __TEXT,__text  _rosetta_dyld_is_translated
0x180487808  __TEXT,__text  __crossarch_trap
0x180487814  __TEXT,__text  CString::leafName() const
0x18048785c  __TEXT,__text  mach_o::Image::sectionContent(mach_o::Header::SectionInfo const&) const
0x1804878f8  __TEXT,__text  invocation function for block in mach_o::Header::forEachSection(void  block_pointer(mach_o::Header::SectionInfo const&, bool&)) const
0x180487920  __TEXT,__text  PropertyList::Data::Data(PropertyList&, std::__1::span<std::byte, 18446744073709551615ul>)
0x1804879f0  __TEXT,__text  dyld4::ExternallyViewableState::activateAtlas(lsl::Allocator&, ByteStream&)
0x180487c10  __TEXT,__text  lsl::Allocator::owned(void const*, unsigned long long) const
0x180487c54  __TEXT,__text  dyld4::objc_headeropt_rw_t::isLoaded(unsigned int) const
0x180487c88  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::getDylibInstallName(char const**, mach_o::Version32*, mach_o::Version32*) const
0x180487cd8  __TEXT,__text  mach_o::UnsafeHeader::getSlide() const
0x180487d7c  __TEXT,__text  _open_with_subsystem
0x180487e80  __TEXT,__text  _open
0x180487eb4  __TEXT,__text  ___open
0x180487ee0  __TEXT,__text  _close
0x180487f0c  __TEXT,__text  mach_o::Architecture::Architecture(mach_header const*)
0x180487f3c  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::getSlide() const
0x180487f8c  __TEXT,__text  lsl::Allocator::Pool::aligned_alloc_best_fit(unsigned long long, unsigned long long)
0x1804880e4  __TEXT,__text  dyld3::kdebug_trace_dyld_duration_start(unsigned int, dyld3::kt_arg, dyld3::kt_arg, dyld3::kt_arg)
0x18048823c  __TEXT,__text  dyld3::ScopedTimer::endTimer()
0x180488258  __TEXT,__text  dyld4::open(char const*, int, int)
0x1804882e4  __TEXT,__text  _fcntl
0x180488494  __TEXT,__text  ___fcntl
0x1804884c0  __TEXT,__text  _munmap
0x180488520  __TEXT,__text  ___munmap
0x18048854c  __TEXT,__text  dyld3::ScopedTimer::startTimer()
0x180488584  __TEXT,__text  dyld4::SyscallDelegate::sandboxBlockedPageInLinking() const
0x1804885d8  __TEXT,__text  ___sandbox_ms
0x1804885d8  __TEXT,__text  ___sandbox_ms
0x180488604  __TEXT,__text  dyld3::kdebug_trace_dyld_duration_end(unsigned long long, unsigned int, dyld3::kt_arg, dyld3::kt_arg, dyld3::kt_arg)
0x18048874c  __TEXT,__text  _kdebug_trace_string
0x1804887e8  __TEXT,__text  ___kdebug_trace_string
0x180488814  __TEXT,__text  DyldSharedCache::DynamicRegion::cachePath() const
0x180488868  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::preferredLoadAddress() const
0x1804888b4  __TEXT,__text  mach_o::UnsafeHeader::forEachSegment(void  block_pointer(mach_o::UnsafeHeader::SegmentInfo const&, bool&)) const
0x180488958  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::forEachSegment(void  block_pointer(mach_o::UnsafeHeader::SegmentInfo const&, bool&)) const
0x180488a40  __TEXT,__text  mach_o::UnsafeHeader::preferredLoadAddress() const
0x180488ae4  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::platformAndVersions() const
0x180488b3c  __TEXT,__text  PropertyList::Dictionary& PropertyList::Array::addObject<PropertyList::Dictionary>()
0x180488bbc  __TEXT,__text  PropertyList::Dictionary::Dictionary(PropertyList&)
0x180488bc0  __TEXT,__text  PropertyList::String& PropertyList::Dictionary::addObjectForKey<PropertyList::String, char const*&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, char const*&)
0x180488bc0  __TEXT,__text  PropertyList::String& PropertyList::Dictionary::addObjectForKey<PropertyList::String, char const*&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, char const*&)
0x180488cdc  __TEXT,__text  dyld4::ExternallyViewableState::atlasAddImage(PropertyList::Dictionary&, unsigned long long, char const*)
0x180488e94  __TEXT,__text  mach_o::UnsafeHeader::getDylibInstallName(char const**, mach_o::Version32*, mach_o::Version32*) const
0x180488f48  __TEXT,__text  mach_o::UnsafeHeader::installName() const
0x180488f8c  __TEXT,__text  mach_o::UnsafeHeader::platformAndVersions() const
0x180489074  __TEXT,__text  mach_o::UnsafeHeader::forEachPlatformLoadCommand(void  block_pointer(mach_o::Platform, mach_o::Version32, mach_o::Version32)) const
0x180489154  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::forEachPlatformLoadCommand(void  block_pointer(mach_o::Platform, mach_o::Version32, mach_o::Version32)) const
0x180489300  __TEXT,__text  mach_o::PlatformAndVersions::zip(mach_o::PlatformAndVersions const&)
0x180489554  __TEXT,__text  PropertyList::String::String(PropertyList&, std::__1::basic_string_view<char, std::__1::char_traits<char> >)
0x180489614  __TEXT,__text  PropertyList::Array::Array(PropertyList&)
0x1804896c0  __TEXT,__text  PropertyList::Dictionary::Dictionary(PropertyList&)
0x180489784  __TEXT,__text  PropertyList::PropertyList(lsl::Allocator&)
0x180489838  __TEXT,__text  AAREncoder::addFile(std::__1::basic_string_view<char, std::__1::char_traits<char> >, std::__1::span<std::byte, 18446744073709551615ul>)
0x1804898e0  __TEXT,__text  PropertyList::PropertyList(lsl::Allocator&)
0x1804898e4  __TEXT,__text  PropertyList::Array& PropertyList::Dictionary::addObjectForKey<PropertyList::Array>(std::__1::basic_string_view<char, std::__1::char_traits<char> >)
0x1804899e0  __TEXT,__text  PropertyList::rootDictionary()
0x1804899e8  __TEXT,__text  _getpid
0x1804899e8  __TEXT,__text  _getpid
0x180489a38  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, int>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, int&&)
0x180489b3c  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned char const&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned char const&)
0x180489b3c  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned char const&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned char const&)
0x180489c40  __TEXT,__text  PropertyList::Array::Array(PropertyList&)
0x180489c44  __TEXT,__text  PropertyList::Flags<long long>& PropertyList::Dictionary::addObjectForKey<PropertyList::Flags<long long> >(std::__1::basic_string_view<char, std::__1::char_traits<char> >)
0x180489d60  __TEXT,__text  dyld4::ExternallyViewableState::gatherAtlasProcessInfo(unsigned long long, DyldSharedCache const*, PropertyList::Dictionary&)
0x18048a008  __TEXT,__text  PropertyList::Integer::Integer(PropertyList&, long long)
0x18048a008  __TEXT,__text  PropertyList::Integer::Integer(PropertyList&, long long)
0x18048a094  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned long long&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long long&)
0x18048a094  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned long long&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long long&)
0x18048a094  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned long long&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long long&)
0x18048a094  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned long long&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long long&)
0x18048a094  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned long long&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long long&)
0x18048a198  __TEXT,__text  mach_o::UnsafeHeader::forEachLoadCommand(void  block_pointer(load_command const*, bool&)) const
0x18048a374  __TEXT,__text  mach_o::Error::~Error()
0x18048a378  __TEXT,__text  CStringBuilder::CStringBuilder(std::__1::span<char, 18446744073709551615ul>, bool)
0x18048a394  __TEXT,__text  CStringBuilder::~CStringBuilder()
0x18048a3d8  __TEXT,__text  mach_o::UnsafeHeader::hasMachOMagic() const
0x18048a3f0  __TEXT,__text  mach_o::UnsafeHeader::isMachO(std::__1::span<unsigned char const, 18446744073709551615ul>)
0x18048a41c  __TEXT,__text  mach_o::UnsafeHeader::getUuid(unsigned char*) const
0x18048a4f4  __TEXT,__text  lsl::MemoryManager::Buffer::align(unsigned long long, unsigned long long)
0x18048a538  __TEXT,__text  lsl::MemoryManager::Buffer::consumeSpace(unsigned long long)
0x18048a574  __TEXT,__text  lsl::Allocator::Pool::Pool(lsl::Allocator*, lsl::Allocator::Pool*, lsl::MemoryManager::Buffer, lsl::MemoryManager::Buffer, bool, bool)
0x18048a580  __TEXT,__text  lsl::Allocator::Allocator(lsl::MemoryManager&)
0x18048a590  __TEXT,__text  lsl::Allocator::setInitialPool(lsl::Allocator::Pool&)
0x18048a5c0  __TEXT,__text  lsl::Vector<dyld4::InterposeTupleSpecific>::reserve(unsigned long long)
0x18048a618  __TEXT,__text  lsl::Allocator::realloc(void*, unsigned long long)
0x18048a66c  __TEXT,__text  _strlcpy
0x18048a670  __TEXT,__text  __platform_strlcpy
0x18048aab4  __TEXT,__text  lsl::Vector<std::byte>::reserve(unsigned long long)
0x18048aaf8  __TEXT,__text  lsl::Allocator::free(void*)
0x18048abb4  __TEXT,__text  __stackAllocatorInternal(void*, unsigned long long)
0x18048ac8c  __TEXT,__text  __stackAllocatorInternal(void*, unsigned long long)
0x18048ad68  __TEXT,__text  _mach_absolute_time
0x18048adec  __TEXT,__text  _mach_absolute_time_kernel
0x18048adf8  __TEXT,__text  _mach_continuous_time_kernel
0x18048ae04  __TEXT,__text  AAREncoder::AAREncoder(lsl::Allocator&)
0x18048ae44  __TEXT,__text  lsl::Vector<dyld4::RuntimeState::MissingFlatSymbol>::reserveExact(unsigned long long)
0x18048afcc  __TEXT,__text  _mach_vm_map
0x18048b214  __TEXT,__text  lsl::Allocator::Pool::Pool(lsl::Allocator*, lsl::Allocator::Pool*, unsigned long long, bool)
0x18048b2c4  __TEXT,__text  lsl::MemoryManager::vm_allocate_bytes(unsigned long long, bool)
0x18048b3b0  __TEXT,__text  metadata_visitor::ResolvedValue::value() const
0x18048b3b0  __TEXT,__text  metadata_visitor::ResolvedValue::value() const
0x18048b3b8  __TEXT,__text  lsl::Allocator::strdup(char const*)
0x18048b414  __TEXT,__text  lsl::Vector<dyld4::Loader const*>::reserveExact(unsigned long long)
0x18048b578  __TEXT,__text  lsl::Vector<dyld4::Loader const*>::reserve(unsigned long long)
0x18048b5bc  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::getUuid(unsigned char*) const
0x18048b5f0  __TEXT,__text  lsl::Vector<std::byte>::reserveExact(unsigned long long)
0x18048b758  __TEXT,__text  dyld4::ExternallyViewableState::createMinimalInfo(lsl::Allocator&, unsigned long long, char const*, unsigned long long, char const*, DyldSharedCache const*)
0x18048bcd8  __TEXT,__text  lsl::Vector<char const*>::resize(unsigned long long)
0x18048bd90  __TEXT,__text  lsl::Vector<std::byte>::resize(unsigned long long)
0x18048be48  __TEXT,__text  dyld4::PrebuiltLoader::dependent(dyld4::RuntimeState const&, unsigned int, mach_o::LinkedDylibAttributes*) const
0x18048bf20  __TEXT,__text  dyld4::PrebuiltLoader::loadDependents(Diagnostics&, dyld4::RuntimeState&, dyld4::Loader::LoadOptions const&)
0x18048c19c  __TEXT,__text  dyld4::RuntimeState::add(dyld4::Loader const*)
0x18048c2f4  __TEXT,__text  dyld4::PrebuiltLoader::map(Diagnostics&, dyld4::RuntimeState&, dyld4::Loader::LoadOptions const&, bool) const
0x18048c708  __TEXT,__text  dyld4::prepare(dyld4::APIs&, mach_o::UnsafeHeader const*)
0x18048db58  __TEXT,__text  dyld4::RuntimeState::addPermanentRanges(dyld3::Array<dyld4::Loader const*> const&)
0x18048dba8  __TEXT,__text  dyld4::RuntimeState::PermanentRanges::make(dyld4::RuntimeState&, dyld3::Array<dyld4::Loader const*> const&)
0x18048de40  __TEXT,__text  invocation function for block in dyld4::RuntimeState::PermanentRanges::make(dyld4::RuntimeState&, dyld3::Array<dyld4::Loader const*> const&)
0x18048df18  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::RuntimeState::PermanentRanges::Range, 4294967295ull>::push_back(dyld4::RuntimeState::PermanentRanges::Range const&)
0x18048df18  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::RuntimeState::PermanentRanges::Range, 4294967295ull>::push_back(dyld4::RuntimeState::PermanentRanges::Range const&)
0x18048df18  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::RuntimeState::PermanentRanges::Range, 4294967295ull>::push_back(dyld4::RuntimeState::PermanentRanges::Range const&)
0x18048df18  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::RuntimeState::PermanentRanges::Range, 4294967295ull>::push_back(dyld4::RuntimeState::PermanentRanges::Range const&)
0x18048df70  __TEXT,__text  dyld4::PrebuiltLoader::BindTargetRef::absValueOrOffset() const
0x18048dfac  __TEXT,__text  dyld4::PrebuiltLoader::BindTargetRef::makeAbsolute(unsigned long long)
0x18048dfdc  __TEXT,__text  dyld4::PrebuiltLoaderSet::swiftTypeProtocolTable() const
0x18048dff0  __TEXT,__text  dyld3::MultiMap<SwiftTypeProtocolConformanceDiskLocationKey, SwiftTypeProtocolConformanceDiskLocation, dyld4::HashTypeConformanceKey, dyld4::EqualTypeConformanceKey>::find(SwiftTypeProtocolConformanceDiskLocationKey const&)
0x18048e178  __TEXT,__text  dyld4::PrebuiltLoaderSet::swiftMetadataProtocolTable() const
0x18048e18c  __TEXT,__text  dyld3::OverflowSafeArray<unsigned long long, 4294967295ull>::operator[](unsigned long long)
0x18048e1f8  __TEXT,__text  dyld3::OverflowSafeArray<dyld3::MultiMapBase<SwiftTypeProtocolConformanceDiskLocationKey, SwiftTypeProtocolConformanceDiskLocation, dyld4::HashTypeConformanceKey, dyld4::EqualTypeConformanceKey>::NodeEntryT, 4294967295ull>::operator[](unsigned long long)
0x18048e1f8  __TEXT,__text  dyld3::OverflowSafeArray<dyld3::MultiMapBase<SwiftTypeProtocolConformanceDiskLocationKey, SwiftTypeProtocolConformanceDiskLocation, dyld4::HashTypeConformanceKey, dyld4::EqualTypeConformanceKey>::NodeEntryT, 4294967295ull>::operator[](unsigned long long)
0x18048e1f8  __TEXT,__text  dyld3::OverflowSafeArray<dyld3::MultiMapBase<SwiftTypeProtocolConformanceDiskLocationKey, SwiftTypeProtocolConformanceDiskLocation, dyld4::HashTypeConformanceKey, dyld4::EqualTypeConformanceKey>::NodeEntryT, 4294967295ull>::operator[](unsigned long long)
0x18048e264  __TEXT,__text  prebuilt_objc::forEachProtocol(dyld4::RuntimeState*, dyld3::MultiMapView<prebuilt_objc::ObjCStringKeyOnDisk, prebuilt_objc::ObjCObjectOnDiskLocation, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk> const&, char const*, void  block_pointer(dyld3::Array<dyld4::Prebuilt
0x18048e2e8  __TEXT,__text  dyld4::APIs::_dyld_for_each_objc_protocol(char const*, dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>)
0x18048e440  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_for_each_objc_protocol(char const*, dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>)
0x18048e4d8  __TEXT,__text  invocation function for block in prebuilt_objc::forEachProtocol(dyld4::RuntimeState*, dyld3::MultiMapView<prebuilt_objc::ObjCStringKeyOnDisk, prebuilt_objc::ObjCObjectOnDiskLocation, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk> const&, char const*, void  block_poi
0x18048e5c0  __TEXT,__text  void dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>::operator()<void*, bool, bool*>(void*&&, bool&&, bool*&&) const
0x18048e6cc  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_for_each_objc_protocol(char const*, dyld4::ReadOnlyCallback<void  block_pointer(void*, bool, bool*)>)
0x18048e76c  __TEXT,__text  dyld4::PrebuiltLoader::path(dyld4::RuntimeState const&) const
0x18048e7b4  __TEXT,__text  dyld4::RuntimeState::cachedDylibLoadAddress(unsigned short) const
0x18048e7f8  __TEXT,__text  DyldSharedCache::getIndexedImageEntry(unsigned int, unsigned long long&, unsigned long long&) const
0x18048e848  __TEXT,__text  dyld4::DyldCacheDataConstLazyScopedWriter::DyldCacheDataConstLazyScopedWriter(dyld4::RuntimeState&)
0x18048e84c  __TEXT,__text  dyld4::Loader::overridesDylibInCache(dyld4::Loader::DylibPatch const*&, unsigned short&) const
0x18048e880  __TEXT,__text  dyld4::Loader::path(dyld4::RuntimeState const&) const
0x18048e8b4  __TEXT,__text  dyld4::Loader::applyFixups(Diagnostics&, dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&, bool, lsl::Vector<std::__1::pair<dyld4::Loader const*, char const*> >*) const
0x18048e8e8  __TEXT,__text  dyld4::Loader::applyFixupsCheckCachePatching(dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&) const
0x18048ebb4  __TEXT,__text  dyld4::RuntimeState::buildInterposingTables()
0x18048ee64  __TEXT,__text  dyld4::JustInTimeLoader::handleStrongWeakDefOverrides(dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&)
0x18048ef50  __TEXT,__text  dyld4::PrebuiltLoader::applyFixups(Diagnostics&, dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&, bool, lsl::Vector<std::__1::pair<dyld4::Loader const*, char const*> >*) const
0x18048f464  __TEXT,__text  dyld4::PrebuiltLoader::overridesDylibInCache(dyld4::Loader::DylibPatch const*&, unsigned short&) const
0x18048f490  __TEXT,__text  dyld4::SyscallDelegate::withReadOnlyMappedFile(Diagnostics&, char const*, void  block_pointer(void const*, unsigned long, dyld4::FileID const&, char const*, int)) const
0x18048f564  __TEXT,__text  mach_o::UnsafeHeader::isDylib() const
0x18048f574  __TEXT,__text  Diagnostics::Diagnostics()
0x18048f57c  __TEXT,__text  dyld4::Loader::fileID(dyld4::RuntimeState const&) const
0x18048f5b0  __TEXT,__text  dyld4::PrebuiltLoader::fileID(dyld4::RuntimeState const&) const
0x18048f5f4  __TEXT,__text  mach_o::UnsafeHeader::arch() const
0x18048f600  __TEXT,__text  dyld4::RuntimeLocks::takeDlopenLockBeforeFork()
0x18048f634  __TEXT,__text  dyld4::RuntimeLocks::withLoadersWriteLockAndProtectedStack<dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const::{lambda()#1}>(dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const::{lambda()#1})::{lambda()#1}::operator()() const
0x18048f74c  __TEXT,__text  dyld4::ProcessConfig::PathOverrides::forEachPathVariant(CString, mach_o::Platform, bool, bool, bool&, void  block_pointer(char const*, dyld4::ProcessConfig::PathOverrides::Type, bool&)) const
0x18048fe48  __TEXT,__text  dyld4::Loader::makeDiskLoader(Diagnostics&, dyld4::RuntimeState&, char const*, dyld4::Loader::LoadOptions const&, bool, unsigned int)
0x18048ff28  __TEXT,__text  Diagnostics::hasError() const
0x18048ff4c  __TEXT,__text  dyld4::Loader::mf(dyld4::RuntimeState const&) const
0x18048ff4c  __TEXT,__text  dyld4::Loader::mf(dyld4::RuntimeState const&) const
0x18048ff80  __TEXT,__text  dyld4::RuntimeLocks::withLoadersReadLock(void  block_pointer())
0x180490020  __TEXT,__text  dyld4::Loader::contains(dyld4::RuntimeState&, void const*, void const**, unsigned long long*, unsigned char*) const
0x180490054  __TEXT,__text  invocation function for block in dyld4::APIs::findImageMappedAt(void const*, mach_o::UnsafeHeader const**, bool*, char const**, void const**, unsigned long long*, unsigned char*, dyld4::Loader const**)
0x1804901cc  __TEXT,__text  dyld4::JustInTimeLoader::contains(dyld4::RuntimeState&, void const*, void const**, unsigned long long*, unsigned char*) const
0x1804902f0  __TEXT,__text  invocation function for block in dyld4::JustInTimeLoader::contains(dyld4::RuntimeState&, void const*, void const**, unsigned long long*, unsigned char*) const
0x180490348  __TEXT,__text  dyld4::JustInTimeLoader::mf(dyld4::RuntimeState const&) const
0x180490348  __TEXT,__text  dyld4::JustInTimeLoader::mf(dyld4::RuntimeState const&) const
0x180490350  __TEXT,__text  mach_o::UnsafeHeader::validStructureLoadCommands(unsigned long long) const
0x1804904e0  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::validStructureLoadCommands(unsigned long long) const
0x1804908d4  __TEXT,__text  mach_o::stringOverflow(load_command const*, unsigned int, unsigned int)
0x18049094c  __TEXT,__text  mach_o::Error::operator=(mach_o::Error&&)
0x180490994  __TEXT,__text  CStringBuilder::moveStringFrom(CStringBuilder&)
0x180490a24  __TEXT,__text  dyld4::APIs::getPlatformAndVersions(mach_o::UnsafeHeader const*)
0x180490a98  __TEXT,__text  dyld4::SyscallDelegate::mapFileReadOnly(Diagnostics&, char const*, int*, unsigned long*, dyld4::FileID*, char*) const
0x180490c04  __TEXT,__text  dyld4::stat(char const*, stat*)
0x180490c64  __TEXT,__text  _mmap
0x180490d0c  __TEXT,__text  ___mmap
0x180490d38  __TEXT,__text  mach_o::Universal::isUniversal(std::__1::span<unsigned char const, 18446744073709551615ul>)
0x180490d64  __TEXT,__text  Diagnostics::~Diagnostics()
0x180490dbc  __TEXT,__text  Diagnostics::clearError()
0x180490e10  __TEXT,__text  dyld4::Loader::applyFixupsGeneric(Diagnostics&, dyld4::RuntimeState&, unsigned long long, dyld3::Array<void const*> const&, dyld3::Array<void const*> const&, bool, dyld3::Array<dyld4::Loader::MissingFlatLazySymbol> const&) const
0x180491258  __TEXT,__text  dyld4::Loader::setUpPageInLinking(Diagnostics&, dyld4::RuntimeState&, unsigned long, unsigned long long, dyld3::Array<void const*> const&) const
0x180491648  __TEXT,__text  dyld4::SyscallDelegate::open(char const*, int, int) const
0x180491658  __TEXT,__text  invocation function for block in dyld4::Loader::setUpPageInLinking(Diagnostics&, dyld4::RuntimeState&, unsigned long, unsigned long long, dyld3::Array<void const*> const&) const
0x1804917dc  __TEXT,__text  dyld4::Loader::getOnDiskBinarySliceOffset(dyld4::RuntimeState&, mach_o::UnsafeHeader const*, char const*)
0x1804918b0  __TEXT,__text  _stat_with_subsystem
0x18049199c  __TEXT,__text  _stat64
0x18049199c  __TEXT,__text  _stat64
0x1804919c8  __TEXT,__text  invocation function for block in dyld4::Loader::getOnDiskBinarySliceOffset(dyld4::RuntimeState&, mach_o::UnsafeHeader const*, char const*)
0x180491a5c  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::PageInLinkingRange, 4294967295ull>::push_back(dyld4::PageInLinkingRange const&)
0x180491a5c  __TEXT,__text  dyld3::OverflowSafeArray<dyld4::PageInLinkingRange, 4294967295ull>::push_back(dyld4::PageInLinkingRange const&)
0x180491acc  __TEXT,__text  dyld4::setUpPageInLinkingRegions(dyld4::RuntimeState&, dyld4::Loader const*, unsigned long, unsigned short, unsigned short, bool, dyld3::Array<dyld4::PageInLinkingRange> const&, dyld3::Array<void const*> const&)
0x180491ea4  __TEXT,__text  ___map_with_linking_np
0x180491ed0  __TEXT,__text  dyld4::dyld_map_with_linking_np(mwl_region const*, unsigned int, mwl_info_hdr const*, unsigned int)
0x1804920c8  __TEXT,__text  dyld4::fixupPageAuth64(void*, mwl_info_hdr const*, dyld_chained_starts_in_segment const*, unsigned int, bool)
0x18049224c  __TEXT,__text  signPointer(unsigned long long, void*, bool, unsigned short, ptrauth_key)
0x1804922cc  __TEXT,__text  prebuilt_objc::findSelector(dyld4::RuntimeState*, dyld3::MapView<prebuilt_objc::ObjCStringKeyOnDisk, void, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk> const&, char const*)
0x180492334  __TEXT,__text  dyld3::MapBase<prebuilt_objc::ObjCStringKeyOnDisk, void, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk>::NodeImplT<true> const* dyld3::MapBase<prebuilt_objc::ObjCStringKeyOnDisk, void, prebuilt_objc::HashObjCStringKeyOnDisk, prebuilt_objc::EqualObjCStringKeyOnDisk>:
0x180492468  __TEXT,__text  dyld4::APIs::_dyld_shared_cache_contains_path(char const*)
0x1804924dc  __TEXT,__text  dyld4::RuntimeState::findPrebuiltLoader(char const*) const
0x1804925a0  __TEXT,__text  mach_o::Header::isValidMachOStructure(std::__1::span<unsigned char const, 18446744073709551615ul>, mach_o::Header&)
0x18049262c  __TEXT,__text  mach_o::Image::makeFromRawSlice(std::__1::span<unsigned char const, 18446744073709551615ul>, mach_o::Image&)
0x1804928a4  __TEXT,__text  mach_o::Header::validStructureLoadCommands(unsigned long long) const
0x180492da4  __TEXT,__text  invocation function for block in mach_o::Header::validStructureLoadCommands(unsigned long long) const
0x180493290  __TEXT,__text  mach_o::Header::parse_dylib_command(mach_o::Header::LoadCommandInfo const&, mach_o::Error*) const
0x1804933d0  __TEXT,__text  mach_o::Header::isDylibLoadCommand(mach_o::Header::LoadCommandInfo const&, mach_o::LinkedDylibAttributes&) const
0x180493484  __TEXT,__text  mach_o::Header::parse_dysymtab_command(mach_o::Header::LoadCommandInfo const&, mach_o::Error*) const
0x180493584  __TEXT,__text  mach_o::Header::validMachOHeader(std::__1::span<unsigned char const, 18446744073709551615ul>, unsigned long&)
0x180493668  __TEXT,__text  mach_o::Header::stringFromOffsetInLoadCommand(mach_o::Header::LoadCommandInfo const&, unsigned int, mach_o::Error*) const
0x1804937b0  __TEXT,__text  mach_o::Header::parse_symtab_command(mach_o::Header::LoadCommandInfo const&, mach_o::Error*) const
0x180493860  __TEXT,__text  mach_o::Header::parse_uuid_command(mach_o::Header::LoadCommandInfo const&, mach_o::Error*) const
0x1804938c8  __TEXT,__text  mach_o::Header::validSemanticsPlatform(mach_o::PlatformAndVersions&) const
0x180493a74  __TEXT,__text  invocation function for block in mach_o::Header::validSemanticsPlatform(mach_o::PlatformAndVersions&) const
0x180493b2c  __TEXT,__text  mach_o::Platform::valid() const
0x180493b8c  __TEXT,__text  mach_o::Header::isStaticExecutable() const
0x180493bdc  __TEXT,__text  mach_o::Header::loadCommandCount(unsigned int) const
0x180493d4c  __TEXT,__text  mach_o::Header::validSemanticsUUID(mach_o::Policy const&) const
0x180493e30  __TEXT,__text  mach_o::Header::validSemanticsInstallName(mach_o::Policy const&) const
0x180493e90  __TEXT,__text  invocation function for block in mach_o::Header::validSemanticsLinkedDylibs(mach_o::Policy const&) const
0x180493eac  __TEXT,__text  mach_o::GradedArchitectures::bestSlice(std::__1::span<unsigned char const, 18446744073709551615ul>, std::__1::span<unsigned char const, 18446744073709551615ul>&) const
0x1804940c8  __TEXT,__text  mach_o::UnsafeHeader::noDynamicAccess() const
0x1804940d4  __TEXT,__text  invocation function for block in mach_o::Header::loadCommandCount(unsigned int) const
0x180494100  __TEXT,__text  mach_o::Header::forEachLinkedDylib(void  block_pointer(mach_o::Header::DylibInfo const&, bool, bool&)) const
0x18049440c  __TEXT,__text  dyld4::PrebuiltLoaderSet::findIndex(dyld4::RuntimeState const&, char const*, unsigned short&) const
0x1804944d8  __TEXT,__text  dyld4::PrebuiltLoaderSet::findLoader(dyld4::RuntimeState const&, char const*) const
0x18049453c  __TEXT,__text  dyld4::JustInTimeLoader::makeJustInTimeLoaderDisk(Diagnostics&, dyld4::RuntimeState&, char const*, dyld4::Loader::LoadOptions const&, bool, unsigned int)
0x180494b60  __TEXT,__text  mach_o::Header::isValidMachO(std::__1::span<unsigned char const, 18446744073709551615ul>, mach_o::Header&)
0x180494d78  __TEXT,__text  mach_o::Header::validSemanticsLinkedDylibs(mach_o::Policy const&) const
0x18049511c  __TEXT,__text  invocation function for block in mach_o::Header::forEachLinkedDylib(void  block_pointer(mach_o::Header::DylibInfo const&, bool, bool&)) const
0x1804951d4  __TEXT,__text  mach_o::hasWarningHandler()
0x1804951e8  __TEXT,__text  DyldSharedCache::imagesCount() const
0x180495204  __TEXT,__text  DyldSharedCache::swiftOpt() const
0x18049522c  __TEXT,__text  DyldSharedCache::patchTable() const
0x180495248  __TEXT,__text  lsl::MemoryManager::setDyldCacheAddr(void*)
0x180495260  __TEXT,__text  mach_o::Header::inDyldCache() const
0x180495280  __TEXT,__text  FileIdTuple::operator bool() const
0x1804952a0  __TEXT,__text  mach_o::Header::forEachPlatformLoadCommand(void  block_pointer(mach_o::Platform, mach_o::Version32, mach_o::Version32)) const
0x180495458  __TEXT,__text  invocation function for block in mach_o::Header::forEachPlatformLoadCommand(void  block_pointer(mach_o::Platform, mach_o::Version32, mach_o::Version32)) const
0x180495624  __TEXT,__text  mach_o::Policy::Policy(mach_o::Architecture, mach_o::PlatformAndVersions, unsigned int, bool, bool, bool)
0x180495628  __TEXT,__text  mach_o::Policy::Policy(mach_o::Architecture, mach_o::PlatformAndVersions, unsigned int, bool, bool, bool)
0x1804956cc  __TEXT,__text  mach_o::Platform::epoch(mach_o::Version32) const
0x180495748  __TEXT,__text  mach_o::PlatformInfo::yearForMajorVersion(mach_o::Version32, unsigned short&, bool&) const
0x180495800  __TEXT,__text  mach_o::PlatformInfo::yearForVersion(mach_o::Version32, unsigned short&, bool&) const
0x180495808  __TEXT,__text  mach_o::PlatformInfo::minorVersionForSpring(unsigned short) const
0x180495810  __TEXT,__text  mach_o::Policy::useProtectedStack() const
0x180495810  __TEXT,__text  mach_o::Policy::useProtectedStack() const
0x180495810  __TEXT,__text  mach_o::Policy::useProtectedStack() const
0x180495810  __TEXT,__text  mach_o::Policy::useProtectedStack() const
0x180495810  __TEXT,__text  mach_o::Policy::useProtectedStack() const
0x180495828  __TEXT,__text  invocation function for block in mach_o::Header::platformAndVersions() const
0x18049588c  __TEXT,__text  ___error
0x1804958a8  __TEXT,__text  __graft_select_fire
0x180495b1c  __TEXT,__text  _boot_get_dylib_root
0x180495b24  __TEXT,__text  _sandbox_operation_fixup
0x180495b90  __TEXT,__text  _sandbox_check
0x180495c04  __TEXT,__text  _stage_fire
0x180495d44  __TEXT,__text  __hello_fire
0x180495dac  __TEXT,__text  __graft_fetch_fire
0x180495f14  __TEXT,__text  _openat
0x180495f48  __TEXT,__text  ___openat
0x180495f74  __TEXT,__text  _dupfd
0x180495ff4  __TEXT,__text  _dup
0x180496020  __TEXT,__text  _ignition_get_shared_cache_directory
0x180496074  __TEXT,__text  _fstatat64
0x180496074  __TEXT,__text  _fstatat64
0x1804960a0  __TEXT,__text  __dylib_cache_fire
0x1804962c8  __TEXT,__text  _realpathfd
0x18049635c  __TEXT,__text  __dylib_cache_payload_check
0x18049639c  __TEXT,__text  __goodbye_fire
0x1804963a4  __TEXT,__text  _boot_set_payload
0x180496440  __TEXT,__text  _dupfd_optional
0x180496450  __TEXT,__text  _boot_destroy
0x1804964e0  __TEXT,__text  _log_destroy
0x1804964f4  __TEXT,__text  dyld3::reuseExistingCache(dyld3::SharedCacheOptions const&, dyld3::SharedCacheLoadInfo*)
0x18049665c  __TEXT,__text  dyld4::SyscallDelegate::getDyldCache(dyld3::SharedCacheOptions const&, dyld3::SharedCacheLoadInfo&) const
0x180496724  __TEXT,__text  FileIdTuple::fsID() const
0x18049672c  __TEXT,__text  dyld3::loadDyldCache(dyld3::SharedCacheOptions const&, dyld3::SharedCacheLoadInfo*)
0x1804967b0  __TEXT,__text  dyld3::validMagic(dyld3::SharedCacheOptions const&, DyldSharedCache const*)
0x180496834  __TEXT,__text  FileIdTuple::inode() const
0x18049683c  __TEXT,__text  dyld4::ProcessConfig::DyldCache::setPlatformOSVersion(dyld4::ProcessConfig::Process const&)
0x180496998  __TEXT,__text  DyldSharedCache::objcHeaderInfoRW() const
0x1804969f0  __TEXT,__text  DyldSharedCache::objcHeaderInfoRO() const
0x180496a48  __TEXT,__text  DyldSharedCache::objcProtocolHashTable() const
0x180496aa0  __TEXT,__text  DyldSharedCache::objcSelectorHashTable() const
0x180496af8  __TEXT,__text  DyldSharedCache::objcClassHashTable() const
0x180496b50  __TEXT,__text  PropertyList::UUID& PropertyList::Dictionary::addObjectForKey<PropertyList::UUID, unsigned char (&) [16]>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned char (&) [16])
0x180496c54  __TEXT,__text  PropertyList::UUID::UUID(PropertyList&, unsigned char*)
0x180496c8c  __TEXT,__text  invocation function for block in dyld4::ExternallyViewableState::atlasAddImage(PropertyList::Dictionary&, unsigned long long, char const*)
0x180496dc8  __TEXT,__text  PropertyList::String& PropertyList::Dictionary::addObjectForKey<PropertyList::String, std::__1::basic_string_view<char, std::__1::char_traits<char> > const&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, std::__1::basic_string_view<char, std::__1::char_traits<char> > const&)
0x180496ecc  __TEXT,__text  PropertyList::encode(ByteStream&)
0x1804975d4  __TEXT,__text  void ByteStream::push_back<char const*>(char const*)
0x180497648  __TEXT,__text  void (anonymous namespace)::quickSort<lsl::Vector<PropertyList::String*>::CheckedIterator<PropertyList::String*> >(lsl::Vector<PropertyList::String*>::CheckedIterator<PropertyList::String*>, lsl::Vector<PropertyList::String*>::CheckedIterator<PropertyList::String*>)
0x1804978f4  __TEXT,__text  lsl::Vector<unsigned long long>::reserve(unsigned long long)
0x180497938  __TEXT,__text  lsl::Vector<unsigned long long>::reserveExact(unsigned long long)
0x180497aa0  __TEXT,__text  PropertyList::String::emit(unsigned char, ByteStream&)
0x180497bb0  __TEXT,__text  PropertyList::String::emitUnicode(unsigned char, unsigned long long, ByteStream&) const
0x180497e8c  __TEXT,__text  (anonymous namespace)::emitPlistEncodedInteger(long long, ByteStream&)
0x180497f7c  __TEXT,__text  ByteStream::push_back(unsigned char, unsigned long long)
0x1804980a8  __TEXT,__text  void (anonymous namespace)::quickSort<lsl::Vector<PropertyList::Integer*>::CheckedIterator<PropertyList::Integer*> >(lsl::Vector<PropertyList::Integer*>::CheckedIterator<PropertyList::Integer*>, lsl::Vector<PropertyList::Integer*>::CheckedIterator<PropertyList::Integer*>)
0x180498338  __TEXT,__text  PropertyList::Integer::emit(unsigned char, ByteStream&)
0x180498428  __TEXT,__text  void ByteStream::push_back<unsigned short>(unsigned short)
0x180498470  __TEXT,__text  void ByteStream::push_back<unsigned int>(unsigned int)
0x1804984b8  __TEXT,__text  void ByteStream::push_back<unsigned long long>(unsigned long long)
0x180498500  __TEXT,__text  PropertyList::Data::operator<=>(PropertyList::Data const&) const
0x180498584  __TEXT,__text  void (anonymous namespace)::quickSort<lsl::Vector<PropertyList::Data*>::CheckedIterator<PropertyList::Data*> >(lsl::Vector<PropertyList::Data*>::CheckedIterator<PropertyList::Data*>, lsl::Vector<PropertyList::Data*>::CheckedIterator<PropertyList::Data*>)
0x180498808  __TEXT,__text  (anonymous namespace)::emitUnsignedPlistEncodedInteger(unsigned long long, ByteStream&)
0x18049887c  __TEXT,__text  PropertyList::Data::emit(unsigned char, ByteStream&)
0x18049893c  __TEXT,__text  PropertyList::Dictionary::emit(unsigned char, ByteStream&)
0x180498ac0  __TEXT,__text  PropertyList::Array::emit(unsigned char, ByteStream&)
0x180498b84  __TEXT,__text  lsl::Vector<unsigned long long>::resize(unsigned long long)
0x180498c3c  __TEXT,__text  AAREncoder::encodeFile(AAREncoder::File const&, ByteStream&) const
0x180498edc  __TEXT,__text  AAREncoder::encode(ByteStream&) const
0x1804990b4  __TEXT,__text  AAREncoder::headerSize(AAREncoder::File const&) const
0x18049911c  __TEXT,__text  lsl::Vector<std::byte>::CheckedIterator<std::byte> lsl::Vector<std::byte>::insert<lsl::Vector<std::byte>::CheckedIterator<std::byte> >(lsl::Vector<std::byte>::CheckedIterator<std::byte const>, lsl::Vector<std::byte>::CheckedIterator<std::byte>, lsl::Vector<std::byte>::CheckedIterator<std::byte>)
0x1804992a0  __TEXT,__text  lsl::Allocator::size(void const*)
0x1804992bc  __TEXT,__text  dyld4::ExternallyViewableState::triggerNotifications(dyld_image_mode, unsigned int, dyld_image_info const*)
0x18049955c  __TEXT,__text  dyld4::RemoteNotificationResponder::RemoteNotificationResponder(unsigned int)
0x180499564  __TEXT,__text  dyld4::RemoteNotificationResponder::RemoteNotificationResponder(unsigned int)
0x18049964c  __TEXT,__text  dyld4::RemoteNotificationResponder::~RemoteNotificationResponder()
0x180499650  __TEXT,__text  dyld4::RemoteNotificationResponder::active() const
0x180499690  __TEXT,__text  lsl::Allocator::freeObject(void*)
0x1804997f4  __TEXT,__text  dyld4::RemoteNotificationResponder::~RemoteNotificationResponder()
0x180499868  __TEXT,__text  PropertyList::~PropertyList()
0x180499bac  __TEXT,__text  PropertyList::Object::deallocate()
0x180499c54  __TEXT,__text  PropertyList::~PropertyList()
0x180499c58  __TEXT,__text  PropertyList::Dictionary::~Dictionary()
0x180499d08  __TEXT,__text  PropertyList::Array::~Array()
0x180499d80  __TEXT,__text  AAREncoder::~AAREncoder()
0x180499ed0  __TEXT,__text  AAREncoder::~AAREncoder()
0x180499ed4  __TEXT,__text  lsl::Vector<dyld_image_info>::resize(unsigned long long)
0x180499f8c  __TEXT,__text  invocation function for block in lsl::Allocator::~Allocator()
0x180499fbc  __TEXT,__text  PropertyList::Dictionary& PropertyList::Dictionary::addObjectForKey<PropertyList::Dictionary>(std::__1::basic_string_view<char, std::__1::char_traits<char> >)
0x18049a0b8  __TEXT,__text  PropertyList::Bitmap& PropertyList::Dictionary::addObjectForKey<PropertyList::Bitmap, unsigned long>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned long&&)
0x18049a1bc  __TEXT,__text  PropertyList::Bitmap::Bitmap(PropertyList&, unsigned long long)
0x18049a1f8  __TEXT,__text  DyldSharedCache::getUUID(unsigned char*) const
0x18049a204  __TEXT,__text  PropertyList::Bitmap::setBit(unsigned long long)
0x18049a254  __TEXT,__text  _sandbox_check_common
0x18049a4e8  __TEXT,__text  PropertyList::Data::Data(PropertyList&, unsigned long long)
0x18049a5b8  __TEXT,__text  lsl::Vector<std::byte>::CheckedIterator<std::byte> lsl::Vector<std::byte>::insert<std::byte*>(lsl::Vector<std::byte>::CheckedIterator<std::byte const>, std::byte*, std::byte*)
0x18049a5b8  __TEXT,__text  lsl::Vector<std::byte>::CheckedIterator<std::byte> lsl::Vector<std::byte>::insert<std::byte*>(lsl::Vector<std::byte>::CheckedIterator<std::byte const>, std::byte*, std::byte*)
0x18049a6fc  __TEXT,__text  lsl::Vector<std::byte>::insert(lsl::Vector<std::byte>::CheckedIterator<std::byte const>, unsigned long long, std::byte const&)
0x18049a85c  __TEXT,__text  PropertyList::Integer& PropertyList::Dictionary::addObjectForKey<PropertyList::Integer, unsigned int const&>(std::__1::basic_string_view<char, std::__1::char_traits<char> >, unsigned int const&)
0x18049a960  __TEXT,__text  _mach_vm_deallocate
0x18049aad8  __TEXT,__text  _vm_deallocate
0x18049aadc  __TEXT,__text  lsl::Allocator::~Allocator()
0x18049ab18  __TEXT,__text  mach_o::Architecture::usesArm64AuthPointers() const
0x18049ab4c  __TEXT,__text  mach_o::Image::dataSectionContent(CString) const
0x18049ac2c  __TEXT,__text  invocation function for block in mach_o::Image::dataSectionContent(CString) const
0x18049acc4  __TEXT,__text  _proc_set_dyld_all_image_info
0x18049ad08  __TEXT,__text  invocation function for block in dyld4::handleDyldInCache(lsl::Allocator&, mach_o::UnsafeHeader const*, dyld4::KernelArgs const*, mach_o::UnsafeHeader const*, unsigned long long)
0x18049ad94  __TEXT,__text  DyldSharedCache::slide() const
0x18049ada8  __TEXT,__text  dyld4::SyscallDelegate::internalInstall() const
0x18049adbc  __TEXT,__text  dyld4::ExternallyViewableState::prepareInCacheDyldAllImageInfos(mach_header const*)
0x18049af50  __TEXT,__text  ___proc_info
0x18049af7c  __TEXT,__text  dyld3::kdebug_trace_dyld_cache(unsigned long long, unsigned long long, unsigned long long, unsigned char const*)
0x18049b0b0  __TEXT,__text  _mig_get_reply_port
0x18049b144  __TEXT,__text  _mach_port_construct
0x18049b2d4  __TEXT,__text  _mach_msg2_internal
0x18049b3d4  __TEXT,__text  _mach_msg_destroy
0x18049b61c  __TEXT,__text  _mach_msg_destroy_port
0x18049b8e0  __TEXT,__text  dyld4::RuntimeLocks::RuntimeLocks()
0x18049b8f0  __TEXT,__text  dyld4::start(dyld4::KernelArgs*, void*, void*, unsigned long long)::$_1::operator()() const
0x18049ba4c  __TEXT,__text  lsl::Allocator::setBestFit(bool)
0x18049ba54  __TEXT,__text  dyld4::ProcessConfig::Process::Process(dyld4::KernelArgs const*, dyld4::SyscallDelegate&, lsl::Allocator&)
0x18049bfa8  __TEXT,__text  dyld4::ProcessConfig::ProcessConfig(dyld4::KernelArgs const*, dyld4::SyscallDelegate&, lsl::Allocator&)
0x18049bfac  __TEXT,__text  dyld4::ProcessConfig::ProcessConfig(dyld4::KernelArgs const*, dyld4::SyscallDelegate&, lsl::Allocator&)
0x18049c198  __TEXT,__text  dyld4::SyscallDelegate::DyldCommPage::DyldCommPage()
0x18049c1c4  __TEXT,__text  dyld4::SyscallDelegate::getpid() const
0x18049c1c8  __TEXT,__text  dyld4::SyscallDelegate::isTranslated() const
0x18049c200  __TEXT,__text  dyld4::SyscallDelegate::dyldCommPageFlags() const
0x18049c210  __TEXT,__text  dyld4::ProcessConfig::Process::getMainUnrealPath(dyld4::SyscallDelegate&, lsl::Allocator&)
0x18049c3a4  __TEXT,__text  dyld4::ProcessConfig::Process::getMainPath(dyld4::SyscallDelegate&, lsl::Allocator&)
0x18049c484  __TEXT,__text  dyld4::ProcessConfig::Process::pathFromAppleParamFileID(dyld4::SyscallDelegate&, lsl::Allocator&, CString) const
0x18049c560  __TEXT,__text  dyld4::SyscallDelegate::fsgetpath(unsigned long long, unsigned long long, CStringBuilder&) const
0x18049c628  __TEXT,__text  mach_o::Architecture::operator==(mach_o::Architecture const&) const
0x18049c66c  __TEXT,__text  mach_o::Header::platformAndVersions() const
0x18049c754  __TEXT,__text  dyld4::SyscallDelegate::realpath(char const*, char*) const
0x18049c8a8  __TEXT,__text  dyld4::ProcessConfig::Process::getMainArchs(dyld4::SyscallDelegate&)
0x18049c968  __TEXT,__text  mach_o::Architecture::name() const
0x18049c96c  __TEXT,__text  _strrchr
0x18049c9c0  __TEXT,__text  __platform_strchr
0x18049c9c0  __TEXT,__text  __platform_strchr
0x18049ca38  __TEXT,__text  mach_o::Header::archName() const
0x18049caa0  __TEXT,__text  mach_o::Architecture::nameSV() const
0x18049cb20  __TEXT,__text  dyld4::SyscallDelegate::getGradedArchs(char const*, bool) const
0x18049cb64  __TEXT,__text  _sysctlbyname
0x18049cc34  __TEXT,__text  invocation function for block in mach_o::Header::hasSection(CString, CString, bool) const
0x18049ccec  __TEXT,__text  mach_o::Header::isFairPlayEncrypted(unsigned int&, unsigned int&) const
0x18049cd28  __TEXT,__text  lsl::Allocator::cstrdup(CString)
0x18049cd78  __TEXT,__text  dyld4::ProcessConfig::Process::getMainPlatform()
0x18049cf24  __TEXT,__text  dyld4::ProcessConfig::Process::defaultTproStack() const
0x18049cfb0  __TEXT,__text  dyld4::ProcessConfig::Security::Security(dyld4::ProcessConfig::Process&, dyld4::SyscallDelegate&)
0x18049d16c  __TEXT,__text  dyld4::SyscallDelegate::inLockdownMode() const
0x18049d1c0  __TEXT,__text  ___sysctl
0x18049d1ec  __TEXT,__text  mach_o::Header::hasSection(CString, CString, bool) const
0x18049d3bc  __TEXT,__text  invocation function for block in mach_o::Header::hasEncryptionInfo(unsigned int&, unsigned int&, unsigned int&) const
0x18049d428  __TEXT,__text  invocation function for block in mach_o::Header::forEachDyldEnvVar(void  block_pointer(std::__1::basic_string_view<char, std::__1::char_traits<char> >, CString, bool&)) const
0x18049d4e8  __TEXT,__text  dyld4::ProcessConfig::Logging::Logging(dyld4::ProcessConfig::Process const&, dyld4::ProcessConfig::Security const&, dyld4::SyscallDelegate&)
0x18049d828  __TEXT,__text  dyld4::ProcessConfig::DyldCache::DyldCache(dyld4::ProcessConfig::Process&, dyld4::ProcessConfig::Security const&, dyld4::ProcessConfig::Logging const&, dyld4::SyscallDelegate&, lsl::Allocator&, dyld4::ProcessConfig const&)
0x18049dd8c  __TEXT,__text  dyld4::CacheFinder::CacheFinder(dyld4::ProcessConfig::Process const&, dyld4::ProcessConfig::Logging const&, dyld4::SyscallDelegate&)
0x18049e098  __TEXT,__text  _ignite
0x18049e520  __TEXT,__text  __open_console
0x18049e574  __TEXT,__text  _log_init
0x18049e5b8  __TEXT,__text  _arguments_dump
0x18049e694  __TEXT,__text  _arguments
0x18049e6bc  __TEXT,__text  _configuration_dump
0x18049ea50  __TEXT,__text  _configuration
0x18049ea78  __TEXT,__text  _boot_dump_spec
0x18049eb2c  __TEXT,__text  _boot_boot
0x18049ec24  __TEXT,__text  dyld4::ProcessConfig::Process::findVersionSetEquivalent(mach_o::Platform, unsigned int) const
0x18049edd0  __TEXT,__text  mach_o::Header::isRestricted() const
0x18049edf0  __TEXT,__text  mach_o::Header::hasEncryptionInfo(unsigned int&, unsigned int&, unsigned int&) const
0x18049eea8  __TEXT,__text  dyld4::SyscallDelegate::amfiFlags(bool, bool) const
0x18049eef4  __TEXT,__text  _amfi_check_dyld_policy_self
0x18049ef68  __TEXT,__text  mach_o::Header::forEachDyldEnvVar(void  block_pointer(std::__1::basic_string_view<char, std::__1::char_traits<char> >, CString, bool&)) const
0x18049efd8  __TEXT,__text  _vdlog
0x18049f064  __TEXT,__text  _dlog
0x18049f090  __TEXT,__text  _dyld_parse_boot_arg_cstr
0x18049f1d4  __TEXT,__text  _arguments_init
0x18049f398  __TEXT,__text  _dyld_parse_boot_arg_int
0x18049f550  __TEXT,__text  _configuration_init
0x18049fcd8  __TEXT,__text  _ignition_test_BRA
0x18049fcd8  __TEXT,__text  _ignition_test_BRA
0x18049fcdc  __TEXT,__text  __derive_proc_name
0x18049fd64  __TEXT,__text  _boot_select_spec
0x18049fe54  __TEXT,__text  _boot_init
0x18049fec0  __TEXT,__text  dyld4::ProcessConfig::Security::getAMFI(dyld4::ProcessConfig::Process const&, dyld4::SyscallDelegate&)
0x18049ff7c  __TEXT,__text  _boot_set_root
0x18049ffdc  __TEXT,__text  _closefd_optional
0x1804a0070  __TEXT,__text  _xferfd
0x1804a0084  __TEXT,__text  _stage_next
0x1804a00b0  __TEXT,__text  dyld4::Loader::makeSegmentsReadOnly(dyld4::RuntimeState&) const
0x1804a0148  __TEXT,__text  dyld4::PrebuiltLoader::applyObjCFixups(dyld4::RuntimeState&) const
0x1804a05c4  __TEXT,__text  invocation function for block in dyld4::Loader::makeSegmentsReadOnly(dyld4::RuntimeState&) const
0x1804a0660  __TEXT,__text  dyld4::SyscallDelegate::mprotect(void*, unsigned long, int) const
0x1804a0670  __TEXT,__text  _mprotect
0x1804a0670  __TEXT,__text  _mprotect
0x1804a069c  __TEXT,__text  dyld4::RuntimeState::doSingletonPatching(dyld4::DyldCacheDataConstLazyScopedWriter&)
0x1804a06e0  __TEXT,__text  dyld4::Loader::adjustFunctionVariantsInDyldCache(dyld4::RuntimeState&)
0x1804a07cc  __TEXT,__text  DyldSharedCache::forEachFunctionVariantPatchLocation(void  block_pointer(void const*, mach_o::PointerMetaData, mach_o::FunctionVariants const&, mach_o::UnsafeHeader const*, int, bool&)) const
0x1804a08d8  __TEXT,__text  dyld4::ProcessConfig::Process::selectFromFunctionVariants(mach_o::FunctionVariants const&, unsigned int) const
0x1804a09e0  __TEXT,__text  invocation function for block in dyld4::Loader::adjustFunctionVariantsInDyldCache(dyld4::RuntimeState&)
0x1804a0b74  __TEXT,__text  mach_o::FunctionVariantsRuntimeTable::forEachVariant(void  block_pointer(mach_o::FunctionVariantsRuntimeTable::Kind, unsigned int, bool, std::__1::span<unsigned char const, 18446744073709551615ul>, bool&)) const
0x1804a0c68  __TEXT,__text  mach_o::FunctionVariants::entry(unsigned int) const
0x1804a0ca8  __TEXT,__text  invocation function for block in dyld4::ProcessConfig::Process::selectFromFunctionVariants(mach_o::FunctionVariants const&, unsigned int) const
0x1804a0d64  __TEXT,__text  dyld4::DyldCacheDataConstLazyScopedWriter::makeWriteable() const
0x1804a0dac  __TEXT,__text  dyld4::PrebuiltLoaderSet::forEachCachePatch(void  block_pointer(dyld4::PrebuiltLoaderSet::CachePatch const&)) const
0x1804a0e20  __TEXT,__text  mach_o::UnsafeHeader::findSectionContent(CString, CString, bool) const
0x1804a0efc  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::findSectionContent(CString, CString, bool) const
0x1804a0fb8  __TEXT,__text  dyld4::PrebuiltLoader::setDelayInit(dyld4::RuntimeState&, bool) const
0x1804a1004  __TEXT,__text  lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::erase(lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::CheckedIterator<AuthenticatedValue<dyld4::PseudoDylib*> >, lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::CheckedIterator<AuthenticatedValue<dyld4::PseudoDylib*> >)
0x1804a1004  __TEXT,__text  lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::erase(lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::CheckedIterator<AuthenticatedValue<dyld4::PseudoDylib*> >, lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::CheckedIterator<AuthenticatedValue<dyld4::PseudoDylib*> >)
0x1804a1108  __TEXT,__text  dyld3::kdebug_trace_dyld_image(unsigned int, char const*, unsigned char const (*) [16], fsobj_id, fsid, void const*, unsigned int)
0x1804a11d4  __TEXT,__text  lsl::Vector<dyld4::ExternallyViewableState::ImageInfo>::reserveExact(unsigned long long)
0x1804a1340  __TEXT,__text  lsl::Vector<dyld4::ExternallyViewableState::ImageInfo>::reserve(unsigned long long)
0x1804a1384  __TEXT,__text  dyld4::Loader::setDelayInit(dyld4::RuntimeState&, bool) const
0x1804a13b8  __TEXT,__text  dyld4::RuntimeState::recursiveMarkNonDelayed(dyld4::Loader const*, dyld4::Loader::LinksWithChain*, dyld4::Loader::LinksWithChain*)
0x1804a1644  __TEXT,__text  dyld4::RuntimeState::partitionDelayLoads(std::__1::span<dyld4::Loader const*, 18446744073709551615ul>, std::__1::span<dyld4::Loader const*, 18446744073709551615ul>, lsl::Vector<dyld4::Loader const*>*)
0x1804a1bfc  __TEXT,__text  lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info> lsl::Vector<dyld_image_info>::insert<lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info> >(lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info const>, lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info>, l
0x1804a1bfc  __TEXT,__text  lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info> lsl::Vector<dyld_image_info>::insert<lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info> >(lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info const>, lsl::Vector<dyld_image_info>::CheckedIterator<dyld_image_info>, l
0x1804a1d50  __TEXT,__text  dyld4::Loader::applyFunctionVariantFixups(Diagnostics&, dyld4::RuntimeState const&) const
0x1804a1e38  __TEXT,__text  dyld4::Loader::hasConstantSegmentsToProtect() const
0x1804a1e50  __TEXT,__text  _cerror_nocancel
0x1804a1e74  __TEXT,__text  dyld4::Loader::applyCachePatches(dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&) const
0x1804a2024  __TEXT,__text  dyld4::RuntimeState::notifyDebuggerLoad(std::__1::span<dyld4::Loader const*, 18446744073709551615ul> const&)
0x1804a22e4  __TEXT,__text  dyld4::ExternallyViewableState::addImages(lsl::Allocator&, lsl::Allocator&, std::__1::span<dyld4::ExternallyViewableState::ImageInfo, 18446744073709551615ul> const&)
0x1804a277c  __TEXT,__text  dyld4::PrebuiltLoader::isDelayInit(dyld4::RuntimeState&) const
0x1804a27ac  __TEXT,__text  dyld4::Loader::isDelayInit(dyld4::RuntimeState&) const
0x1804a27e0  __TEXT,__text  dyld4::Loader::dependentCount() const
0x1804a2814  __TEXT,__text  dyld4::Loader::dependent(dyld4::RuntimeState const&, unsigned int, mach_o::LinkedDylibAttributes*) const
0x1804a2848  __TEXT,__text  dyld4::ExternallyViewableState::generateAtlas(lsl::Allocator&)
0x1804a2cfc  __TEXT,__text  dyld4::DyldCacheDataConstLazyScopedWriter::~DyldCacheDataConstLazyScopedWriter()
0x1804a2cfc  __TEXT,__text  dyld4::DyldCacheDataConstLazyScopedWriter::~DyldCacheDataConstLazyScopedWriter()
0x1804a2d30  __TEXT,__text  dyld4::PrebuiltLoader::dependentCount() const
0x1804a2d38  __TEXT,__text  dyld4::SyscallDelegate::close(int) const
0x1804a2d40  __TEXT,__text  mach_o::Header::preferredLoadAddress() const
0x1804a2f04  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::forEachSection(void  block_pointer(mach_o::UnsafeHeader::SectionInfo const&, bool&)) const
0x1804a314c  __TEXT,__text  mach_o::UnsafeHeader::forEachSection(void  block_pointer(mach_o::UnsafeHeader::SectionInfo const&, bool&)) const
0x1804a31f0  __TEXT,__text  CStringBuilder::append(std::__1::basic_string_view<char, std::__1::char_traits<char> >)
0x1804a3264  __TEXT,__text  invocation function for block in mach_o::GenericTrie::validate(mach_o::Error  block_pointer(CString, std::__1::span<unsigned char const, 18446744073709551615ul>)) const
0x1804a3368  __TEXT,__text  CStringBuilder::ifGrowableEnsureSpaceForAppending(unsigned long)
0x1804a3428  __TEXT,__text  invocation function for block in mach_o::ExportsTrie::valid(unsigned long long, unsigned long long) const
0x1804a3518  __TEXT,__text  mach_o::Symbol::isAbsolute(unsigned long long&) const
0x1804a3538  __TEXT,__text  mach_o::Image::dyldNeverUnloads() const
0x1804a3610  __TEXT,__text  mach_o::Image::objCInfo() const
0x1804a36e8  __TEXT,__text  mach_o::Header::installName() const
0x1804a3728  __TEXT,__text  mach_o::Header::dylibInfo() const
0x1804a391c  __TEXT,__text  mach_o::Header::hasWeakDefs() const
0x1804a393c  __TEXT,__text  mach_o::Header::isDylib() const
0x1804a3960  __TEXT,__text  mach_o::Header::functionVariantFixups() const
0x1804a3980  __TEXT,__text  dyld4::JustInTimeLoader::loadDependents(Diagnostics&, dyld4::RuntimeState&, dyld4::Loader::LoadOptions const&)
0x1804a3be4  __TEXT,__text  invocation function for block in dyld4::JustInTimeLoader::loadDependents(Diagnostics&, dyld4::RuntimeState&, dyld4::Loader::LoadOptions const&)
0x1804a3f9c  __TEXT,__text  dyld4::Loader::forEachBindTarget(Diagnostics&, dyld4::RuntimeState&, void  block_pointer(unsigned int, unsigned int, dyld4::Loader::ResolvedSymbol const&), bool, void  block_pointer(dyld4::Loader::ResolvedSymbol const&, bool&), void  block_pointer(dyld4::Loader::ResolvedSymbol const&, bool&)) const
0x1804a40e8  __TEXT,__text  mach_o::Image::forEachBindTarget(void  block_pointer(mach_o::Fixup::BindTarget const&, bool&), void  block_pointer(mach_o::Fixup::BindTarget const&, bool&)) const
0x1804a41b8  __TEXT,__text  dyld4::RuntimeState::incDlRefCount(dyld4::Loader const*)
0x1804a42b8  __TEXT,__text  dyld4::JustInTimeLoader::setDelayInit(dyld4::RuntimeState&, bool) const
0x1804a42d8  __TEXT,__text  dyld4::JustInTimeLoader::dependentCount() const
0x1804a42e4  __TEXT,__text  _getfsstat64
0x1804a42e4  __TEXT,__text  _getfsstat64
0x1804a4310  __TEXT,__text  _getattrlist
0x1804a4310  __TEXT,__text  _getattrlist
0x1804a433c  __TEXT,__text  void dyld4::ReadOnlyCallback<void (*)(mach_header const*, long)>::operator()<mach_header const*&, long>(mach_header const*&, long&&) const
0x1804a43fc  __TEXT,__text  dyld4::JustInTimeLoader::beginInitializers(dyld4::RuntimeState&)
0x1804a4414  __TEXT,__text  dyld4::JustInTimeLoader::runInitializers(dyld4::RuntimeState&) const
0x1804a44b8  __TEXT,__text  dyld4::RuntimeLocks::withLoadersWriteLockAndProtectedStack<dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const::{lambda()#2}>(dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const::{lambda()#2})::{lambda()#1}::operator()() const
0x1804a45d0  __TEXT,__text  dyld4::RuntimeLocks::releaseDlopenLockInForkParent()
0x1804a4600  __TEXT,__text  dyld4::APIs::validLoader(dyld4::Loader const*)
0x1804a4664  __TEXT,__text  dyld4::Loader::resolvedAddress(dyld4::RuntimeState&, dyld4::Loader::ResolvedSymbol const&)
0x1804a46b4  __TEXT,__text  dyld4::APIs::dlsym(void*, char const*)
0x1804a4ed0  __TEXT,__text  dyld4::APIs::NSVersionOfLinkTimeLibrary(char const*)
0x1804a4fc0  __TEXT,__text  dyld4::nameMatch(char const*, char const*)
0x1804a50a0  __TEXT,__text  invocation function for block in dyld4::APIs::NSVersionOfLinkTimeLibrary(char const*)
0x1804a50e8  __TEXT,__text  invocation function for block in mach_o::Header::validSemanticsLinkedDylibs(mach_o::Policy const&) const
0x1804a5234  __TEXT,__text  mach_o::Header::validSemanticsRPath(mach_o::Policy const&) const
0x1804a5458  __TEXT,__text  mach_o::Error::Error(mach_o::Error&&)
0x1804a54b4  __TEXT,__text  invocation function for block in mach_o::Header::forEachRPath(void  block_pointer(CString, bool&)) const
0x1804a5520  __TEXT,__text  mach_o::Error::Error(mach_o::Error&&)
0x1804a5524  __TEXT,__text  mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const
0x1804a5bbc  __TEXT,__text  invocation function for block in mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const
0x1804a5ea8  __TEXT,__text  mach_o::Error mach_o::Header::validSemanticsSingleSegment<true>(mach_o::Policy const&, unsigned long long, std::__1::span<unsigned char const, 18446744073709551615ul>) const
0x1804a6610  __TEXT,__text  mach_o::Policy::enforceTextSegmentPermissions() const
0x1804a6610  __TEXT,__text  mach_o::Policy::enforceTextSegmentPermissions() const
0x1804a6610  __TEXT,__text  mach_o::Policy::enforceTextSegmentPermissions() const
0x1804a6628  __TEXT,__text  mach_o::Policy::enforceReadOnlyLinkedit() const
0x1804a6658  __TEXT,__text  mach_o::Policy::enforceSectionsInSegment() const
0x1804a6670  __TEXT,__text  dyld3::OverflowSafeArray<mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange, 4294967295ull>::push_back(mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange&&)
0x1804a6670  __TEXT,__text  dyld3::OverflowSafeArray<mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange, 4294967295ull>::push_back(mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange&&)
0x1804a66d4  __TEXT,__text  dyld3::OverflowSafeArray<mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange, 4294967295ull>::operator[](unsigned long long)
0x1804a66d4  __TEXT,__text  dyld3::OverflowSafeArray<mach_o::Header::validSemanticsSegments(mach_o::Policy const&, unsigned long long) const::SegRange, 4294967295ull>::operator[](unsigned long long)
0x1804a6744  __TEXT,__text  mach_o::Header::validStructureLinkedit(mach_o::Policy const&, unsigned long long) const
0x1804a6d70  __TEXT,__text  mach_o::Policy::enforceSegmentOrderMatchesLoadCmds() const
0x1804a6da0  __TEXT,__text  mach_o::Header::getAllLinkEditRanges(std::__1::span<mach_o::Header::LinkEditRange, 18446744073709551615ul>&, mach_o::Error*) const
0x1804a6f14  __TEXT,__text  invocation function for block in mach_o::Header::getAllLinkEditRanges(std::__1::span<mach_o::Header::LinkEditRange, 18446744073709551615ul>&, mach_o::Error*) const
0x1804a7118  __TEXT,__text  mach_o::Header::hasSegment(CString) const
0x1804a72e0  __TEXT,__text  invocation function for block in mach_o::Header::hasSegment(CString) const
0x1804a733c  __TEXT,__text  invocation function for block in mach_o::Header::validStructureLinkedit(mach_o::Policy const&, unsigned long long) const
0x1804a7398  __TEXT,__text  invocation function for block in mach_o::Image::makeFromRawSlice(std::__1::span<unsigned char const, 18446744073709551615ul>, mach_o::Image&)
0x1804a73f8  __TEXT,__text  mach_o::Header::arch() const
0x1804a7414  __TEXT,__text  mach_o::Image::validLinkedit(mach_o::Policy const&) const
0x1804a75d8  __TEXT,__text  mach_o::Header::fileType() const
0x1804a75f4  __TEXT,__text  mach_o::Image::withSegments(void  block_pointer(std::__1::span<mach_o::MappedSegment const, 18446744073709551615ul>)) const
0x1804a7788  __TEXT,__text  mach_o::Image::segmentMapInfo(mach_o::Header::SegmentInfo const&, unsigned long long) const
0x1804a7858  __TEXT,__text  invocation function for block in mach_o::Image::withSegments(void  block_pointer(std::__1::span<mach_o::MappedSegment const, 18446744073709551615ul>)) const
0x1804a78c4  __TEXT,__text  invocation function for block in mach_o::Image::validLinkedit(mach_o::Policy const&) const
0x1804a7bb8  __TEXT,__text  mach_o::ChainedFixups::PointerFormat::make(unsigned short)
0x1804a7be4  __TEXT,__text  mach_o::PointerFormat_Generic_arm64e::maxBindOrdinal(bool) const
0x1804a7c20  __TEXT,__text  mach_o::PointerFormat_DYLD_CHAINED_PTR_ARM64E::bindBitCount() const
0x1804a7c28  __TEXT,__text  mach_o::ChainedFixups::forEachBindTarget(void  block_pointer(mach_o::Fixup::BindTarget const&, bool&), mach_o::Error*) const
0x1804a7d28  __TEXT,__text  mach_o::GenericTrie::validate(mach_o::Error  block_pointer(CString, std::__1::span<unsigned char const, 18446744073709551615ul>)) const
0x1804a7f70  __TEXT,__text  mach_o::ExportsTrie::valid(unsigned long long, unsigned long long) const
0x1804a7fe0  __TEXT,__text  CStringBuilder::trunc(unsigned long)
0x1804a8010  __TEXT,__text  invocation function for block in mach_o::GenericTrie::validate(mach_o::Error  block_pointer(CString, std::__1::span<unsigned char const, 18446744073709551615ul>)) const
0x1804a80b8  __TEXT,__text  mach_o::ExportsTrie::terminalPayloadToSymbol(CString, std::__1::span<unsigned char const, 18446744073709551615ul>, mach_o::Symbol&) const
0x1804a8434  __TEXT,__text  mach_o::Symbol::implOffset() const
0x1804a845c  __TEXT,__text  mach_o::Symbol::isReExport(int&, char const*&) const
0x1804a8490  __TEXT,__text  mach_o::Header::builtForPlatform(mach_o::Platform, bool) const
0x1804a858c  __TEXT,__text  mach_o::Header::loadableIntoProcess(mach_o::Platform, CString, bool) const
0x1804a884c  __TEXT,__text  mach_o::Header::mappedSize() const
0x1804a8a38  __TEXT,__text  invocation function for block in mach_o::Header::mappedSize() const
0x1804a8abc  __TEXT,__text  mach_o::Header::hasThreadLocalVariables() const
0x1804a8adc  __TEXT,__text  invocation function for block in mach_o::Image::dyldNeverUnloads() const
0x1804a8b00  __TEXT,__text  mach_o::UnsafeHeader::hasCodeSignature(unsigned int&, unsigned int&) const
0x1804a8bfc  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::hasCodeSignature(unsigned int&, unsigned int&) const
0x1804a8c38  __TEXT,__text  dyld4::SyscallDelegate::registerSignature(Diagnostics&, char const*, char const*, int, unsigned long long, unsigned int, unsigned int) const
0x1804a8dac  __TEXT,__text  dyld4::Loader::uuidToStr(unsigned char const*, char*)
0x1804a9148  __TEXT,__text  dyld4::SyscallDelegate::unmapFile(void const*, unsigned long) const
0x1804a9148  __TEXT,__text  dyld4::SyscallDelegate::unmapFile(void const*, unsigned long) const
0x1804a9154  __TEXT,__text  dyld4::SyscallDelegate::mmap(void*, unsigned long, int, int, int, unsigned long) const
0x1804a9170  __TEXT,__text  dyld4::JustInTimeLoader::withRegions(mach_o::UnsafeHeader const*, void  block_pointer(std::__1::span<dyld4::Loader::Region const, 18446744073709551615ul>))
0x1804a92dc  __TEXT,__text  mach_o::UnsafeHeader::segmentCount() const
0x1804a9350  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::segmentCount() const
0x1804a937c  __TEXT,__text  invocation function for block in dyld4::JustInTimeLoader::withRegions(mach_o::UnsafeHeader const*, void  block_pointer(std::__1::span<dyld4::Loader::Region const, 18446744073709551615ul>))
0x1804a9498  __TEXT,__text  dyld3::Array<dyld4::Loader::Region>::push_back(dyld4::Loader::Region const&)
0x1804a94cc  __TEXT,__text  dyld4::Loader::mapSegments(Diagnostics&, dyld4::RuntimeState&, char const*, int, unsigned long long, dyld4::Loader::CodeSignatureInFile const&, bool, std::__1::span<dyld4::Loader::Region const, 18446744073709551615ul>, bool, bool, dyld4::Loader::FileValidationInfo const&)
0x1804a9aa4  __TEXT,__text  invocation function for block in dyld4::JustInTimeLoader::makeJustInTimeLoaderDisk(Diagnostics&, dyld4::RuntimeState&, char const*, dyld4::Loader::LoadOptions const&, bool, unsigned int)
0x1804a9b90  __TEXT,__text  dyld4::SyscallDelegate::fstat(int, stat*) const
0x1804a9b9c  __TEXT,__text  dyld4::Loader::validateFile(Diagnostics&, dyld4::RuntimeState const&, int, char const*, dyld4::Loader::CodeSignatureInFile const&, dyld4::Loader::FileValidationInfo const&)
0x1804a9e8c  __TEXT,__text  _fstat64
0x1804a9e8c  __TEXT,__text  _fstat64
0x1804a9eb8  __TEXT,__text  dyld4::getUuidFromFd(dyld4::RuntimeState&, int, unsigned long long, char*)
0x1804a9ff0  __TEXT,__text  dyld4::SyscallDelegate::pread(int, void*, unsigned long, unsigned long) const
0x1804aa004  __TEXT,__text  _pread
0x1804aa030  __TEXT,__text  dyld4::SyscallDelegate::fcntl(int, int, void*) const
0x1804aa05c  __TEXT,__text  mach_o::UnsafeHeader::findFairPlayEncryptionLoadCommand() const
0x1804aa0c8  __TEXT,__text  mach_o::UnsafeHeader::isFairPlayEncrypted(unsigned int&, unsigned int&) const
0x1804aa118  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::findFairPlayEncryptionLoadCommand() const
0x1804aa144  __TEXT,__text  dyld4::JustInTimeLoader::make(dyld4::RuntimeState&, mach_o::UnsafeHeader const*, char const*, dyld4::FileID const&, unsigned long long, bool, bool, bool, unsigned short)
0x1804aa674  __TEXT,__text  mach_o::UnsafeHeader::linkedDylibCount(bool*) const
0x1804aa724  __TEXT,__text  mach_o::UnsafeHeader::forEachLinkedDylib(void  block_pointer(char const*, mach_o::LinkedDylibAttributes, mach_o::Version32, mach_o::Version32, bool, bool&)) const
0x1804aa934  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::forEachLinkedDylib(void  block_pointer(char const*, mach_o::LinkedDylibAttributes, mach_o::Version32, mach_o::Version32, bool, bool&)) const
0x1804aaa04  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::linkedDylibCount(bool*) const
0x1804aaa38  __TEXT,__text  mach_o::Header::isMainExecutable() const
0x1804aaa5c  __TEXT,__text  mach_o::Policy::Policy(mach_o::Header const&, bool, bool, bool)
0x1804aaae4  __TEXT,__text  mach_o::Header::hasObjC() const
0x1804aab88  __TEXT,__text  dyld4::Loader::InitialOptions::InitialOptions()
0x1804aab94  __TEXT,__text  invocation function for block in mach_o::Header::hasObjC() const
0x1804aac2c  __TEXT,__text  mach_o::UnsafeHeader::hasPlusLoadMethod() const
0x1804aacd0  __TEXT,__text  invocation function for block in mach_o::UnsafeHeader::hasPlusLoadMethod() const
0x1804aad80  __TEXT,__text  invocation function for block in dyld4::hasDataConst(mach_o::UnsafeHeader const*)
0x1804aada0  __TEXT,__text  mach_o::Policy::enforceNoFallbackDylibSearchPaths() const
0x1804aadb8  __TEXT,__text  dyld4::ExternallyViewableState::recordMetrics(PropertyList::Dictionary&)
0x1804aaf68  __TEXT,__text  _os_unfair_lock_assert_not_owner
0x1804aaf94  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804aafa4  __TEXT,__text  _OUTLINED_FUNCTION_3
0x1804aafa4  __TEXT,__text  _OUTLINED_FUNCTION_3
0x1804aafc4  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804aafc4  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804aafc4  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804aafe4  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804aaff0  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab010  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab020  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab040  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab04c  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab06c  __TEXT,__text  _OUTLINED_FUNCTION_4
0x1804ab080  __TEXT,__text  dyld4::APIs::runAllInitializersForMain()
0x1804ab270  __TEXT,__text  _os_unfair_lock_assert_owner
0x1804ab29c  __TEXT,__text  dyld4::APIs::_dyld_lookup_section_info(mach_header const*, _dyld_section_location_info_s*, _dyld_section_location_kind)
0x1804ab3e4  __TEXT,__text  dyld4::PrebuiltLoader::runInitializers(dyld4::RuntimeState&) const
0x1804ab448  __TEXT,__text  dyld4::PrebuiltLoader::beginInitializers(dyld4::RuntimeState&)
0x1804ab4a8  __TEXT,__text  dyld4::RuntimeState::notifyObjCInit(dyld4::Loader const*)
0x1804ab68c  __TEXT,__text  dyld4::ExternallyViewableState::setDyldState(unsigned char)
0x1804ab794  __TEXT,__text  dyld4::Loader::getSectionLocations() const
0x1804ab7c8  __TEXT,__text  void dyld4::ReadOnlyCallback<void (*)(_dyld_objc_notify_mapped_info const*)>::operator()<_dyld_objc_notify_mapped_info*>(_dyld_objc_notify_mapped_info*&&) const
0x1804ab87c  __TEXT,__text  dyld4::Loader::dyldDoesObjCFixups() const
0x1804ab8b0  __TEXT,__text  dyld4::PrebuiltLoader::dyldDoesObjCFixups() const
0x1804ab8d8  __TEXT,__text  invocation function for block in dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const::$_0::operator()() const
0x1804aba54  __TEXT,__text  dyld4::PrebuiltLoader::getSectionLocations() const
0x1804aba5c  __TEXT,__text  dyld4::Loader::runInitializersBottomUpPlusUpwardLinks(dyld4::RuntimeState&) const
0x1804abc10  __TEXT,__text  dyld4::Loader::runInitializersBottomUpPlusUpwardLinks(dyld4::RuntimeState&) const::$_0::operator()() const
0x1804abe44  __TEXT,__text  lsl::Vector<AuthenticatedValue<dyld4::PseudoDylib*> >::reserveExact(unsigned long long)
0x1804abfd0  __TEXT,__text  lsl::Allocator::AllocationMetadata::returnToNext(unsigned long long)
0x1804ac0bc  __TEXT,__text  dyld4::APIs::_dyld_get_shared_cache_range(unsigned long*)
0x1804ac160  __TEXT,__text  dyld4::SyscallDelegate::dtraceUserProbesEnabled() const
0x1804ac174  __TEXT,__text  dyld4::SyscallDelegate::disablePageInLinking() const
0x1804ac17c  __TEXT,__text  _OUTLINED_FUNCTION_12
0x1804ac188  __TEXT,__text  _OUTLINED_FUNCTION_12
0x1804ac198  __TEXT,__text  _OUTLINED_FUNCTION_12
0x1804ac1ac  __TEXT,__text  _OUTLINED_FUNCTION_12
0x1804ac1b8  __TEXT,__text  _OUTLINED_FUNCTION_2
0x1804ac1b8  __TEXT,__text  _OUTLINED_FUNCTION_2
0x1804ac1b8  __TEXT,__text  _OUTLINED_FUNCTION_2
0x1804ac1c8  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac1c8  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac1c8  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac1e8  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac1f4  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac214  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac220  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac240  __TEXT,__text  _OUTLINED_FUNCTION_5
0x1804ac254  __TEXT,__text  dyld4::APIs::_dyld_get_image_slide(mach_header const*)
0x1804ac30c  __TEXT,__text  dyld4::APIs::_libdyld_initialize()
0x1804ac4b4  __TEXT,__text  dyld4::LibSystemHelpersWrapper::pthread_key_create_free(unsigned long*) const
0x1804ac608  __TEXT,__text  dyld4::RuntimeState::initialize()
0x1804ac75c  __TEXT,__text  lsl::MemoryManager::adoptLock(lsl::Lock&&)
0x1804ac768  __TEXT,__text  DyldSharedCache::objcLibMsgSendLibOffsets() const
0x1804ac7bc  __TEXT,__text  dyld4::APIs::_dyld_objc_register_callbacks(dyld4::ObjCCallbacks const*)
0x1804ac874  __TEXT,__text  dyld4::APIs::_dyld_for_objc_header_opt_ro()
0x1804ac8f8  __TEXT,__text  dyld4::APIs::_dyld_for_objc_header_opt_rw()
0x1804ac97c  __TEXT,__text  dyld4::APIs::dyld_get_base_platform(unsigned int)
0x1804ac9f8  __TEXT,__text  dyld4::ExternallyViewableState::setLibSystemInitialized()
0x1804aca2c  __TEXT,__text  lsl::Vector<AuthenticatedValue<dyld4::Loader const*> >::resize(unsigned long long)
0x1804acae4  __TEXT,__text  dyld3::MachOFile::isMainExecutable() const
0x1804acaf4  __TEXT,__text  dyld4::Loader::runInitializersBottomUp(dyld4::RuntimeState&, lsl::Vector<AuthenticatedValue<dyld4::Loader const*> >&, lsl::Vector<AuthenticatedValue<dyld4::Loader const*> >&) const
0x1804acdb0  __TEXT,__text  dyld4::Loader::beginInitializers(dyld4::RuntimeState&)
0x1804acdf4  __TEXT,__text  dyld4::Loader::findAndRunAllInitializers(dyld4::RuntimeState&) const
0x1804ad080  __TEXT,__text  dyld4::Loader::runInitializers(dyld4::RuntimeState&) const
0x1804ad0b4  __TEXT,__text  mach_o::Image::forEachInitializer(void  block_pointer(unsigned int)) const
0x1804ad1c0  __TEXT,__text  mach_o::Header::initAddress() const
0x1804ad298  __TEXT,__text  invocation function for block in mach_o::Header::initAddress() const
0x1804ad2f8  __TEXT,__text  invocation function for block in mach_o::Image::forEachInitializer(void  block_pointer(unsigned int)) const
0x1804ad350  __TEXT,__text  invocation function for block in mach_o::Image::forEachInitializer(void  block_pointer(unsigned int)) const
0x1804ad3c4  __TEXT,__text  dyld4::APIs::dyld_shared_cache_some_image_overridden()
0x1804ad41c  __TEXT,__text  invocation function for block in mach_o::Header::preferredLoadAddress() const
0x1804ad468  __TEXT,__text  lsl::ProtectedStack::onStackInAnyFrameInThisThread() const
0x1804ad4d4  __TEXT,__text  dyld4::APIs::_NSGetExecutablePath(char*, unsigned int*)
0x1804ad58c  __TEXT,__text  dyld4::APIs::dyld_has_inserted_or_interposing_libraries()
0x1804ad5f0  __TEXT,__text  dyld4::APIs::_dyld_get_swift_prespecialized_data()
0x1804ad6a0  __TEXT,__text  dyld4::APIs::dlopen(char const*, int)
0x1804ad6cc  __TEXT,__text  dyld4::LibSystemHelpersWrapper::pthread_getspecific(unsigned long) const
0x1804ad92c  __TEXT,__text  dyld4::APIs::clearErrorString()
0x1804ad9a8  __TEXT,__text  dyld4::APIs::_dyld_find_pointer_hash_table_entry(void const*, void const*, unsigned long, void const**)
0x1804adcb4  __TEXT,__text  dyld4::APIs::dlopen_from(char const*, int, void*)
0x1804ae020  __TEXT,__text  dyld4::ProcessConfig::DyldCache::indexOfPath(char const*, unsigned int&) const
0x1804ae030  __TEXT,__text  unsigned int SwiftHashTable::hash<PointerHashTableBuilderKey>(PointerHashTableBuilderKey const&, unsigned char const*) const
0x1804ae0b0  __TEXT,__text  unsigned char SwiftHashTable::checkbyte<PointerHashTableBuilderKey>(PointerHashTableBuilderKey const&, unsigned char const*) const
0x1804ae0c8  __TEXT,__text  dyld4::handleFromLoader(dyld4::Loader const*, bool)
0x1804ae10c  __TEXT,__text  dyld4::PrebuiltLoader::isInitialized(dyld4::RuntimeState const&) const
0x1804ae13c  __TEXT,__text  dyld4::APIs::_dyld_lazy_load(unsigned int*, mach_header const*)
0x1804ae208  __TEXT,__text  bool SwiftHashTable::equal<PointerHashTableBuilderKey, PointerHashTableOnDiskKey>(PointerHashTableOnDiskKey const&, PointerHashTableBuilderKey const&, unsigned char const*) const
0x1804ae254  __TEXT,__text  mach_o::Header::forEachLazyLoadDylib(void  block_pointer(mach_o::Header::LinkEditRange)) const
0x1804ae2c4  __TEXT,__text  mach_o::Image::forEachLazyLoadDylib(void  block_pointer(unsigned int*, CString, bool, bool)) const
0x1804ae330  __TEXT,__text  invocation function for block in mach_o::Header::forEachLazyLoadDylib(void  block_pointer(mach_o::Header::LinkEditRange)) const
0x1804ae364  __TEXT,__text  invocation function for block in mach_o::Image::forEachLazyLoadDylib(void  block_pointer(unsigned int*, CString, bool, bool)) const
0x1804ae428  __TEXT,__text  mach_o::LazyLoadDylib::imageLoadedFlag(mach_header const*) const
0x1804ae448  __TEXT,__text  mach_o::LazyLoadDylib::dylibMayBeMissing() const
0x1804ae468  __TEXT,__text  invocation function for block in dyld4::APIs::_dyld_lazy_load(unsigned int*, mach_header const*)
0x1804ae60c  __TEXT,__text  mach_o::LazyLoadDylib::dylibLoadPath() const
0x1804ae684  __TEXT,__text  mach_o::LazyLoadDylib::dylibSymbolsAlreadyBound() const
0x1804ae6a4  __TEXT,__text  dyld4::RuntimeLocks::withNotifiersReadLock(void  block_pointer())
0x1804ae744  __TEXT,__text  void dyld4::ReadOnlyCallback<void (*)(unsigned int, mach_header const**, char const**)>::operator()<unsigned int const&, mach_header const**, char const**>(unsigned int const&, mach_header const**&&, char const**&&) const
0x1804ae848  __TEXT,__text  dyld4::Loader::hasExportedSymbol(Diagnostics&, dyld4::RuntimeState&, char const*, dyld4::Loader::ExportedSymbolMode, dyld4::Loader::ResolverMode, dyld4::Loader::ResolvedSymbol*, bool, dyld3::Array<dyld4::Loader const*>*) const
0x1804af278  __TEXT,__text  invocation function for block in mach_o::Header::addressInCodeSection(unsigned long long) const
0x1804af2c8  __TEXT,__text  dyld4::Loader::image(dyld4::RuntimeState const&) const
0x1804af31c  __TEXT,__text  invocation function for block in mach_o::Image::objCInfo() const
0x1804af3fc  __TEXT,__text  mach_o::Header::fit32(unsigned long)
0x1804af418  __TEXT,__text  dyld4::APIs::addressLookupsDisabled(char const*) const
0x1804af558  __TEXT,__text  dyld4::Loader::hasMagic() const
0x1804af570  __TEXT,__text  dyld3::Array<dyld4::Loader const*>::push_back(dyld4::Loader const* const&)
0x1804af5c0  __TEXT,__text  mach_o::Header::exportsTrie() const
0x1804af6c0  __TEXT,__text  mach_o::Image::exportsTrie() const
0x1804af780  __TEXT,__text  mach_o::ExportsTrie::hasExportedSymbol(CString, mach_o::Symbol&, bool) const
0x1804af804  __TEXT,__text  mach_o::Symbol::makeRegularExport(CString, unsigned long long, unsigned char, bool, bool, bool, bool)
0x1804af858  __TEXT,__text  mach_o::Symbol::isFunctionVariant(unsigned int&) const
0x1804af878  __TEXT,__text  mach_o::Symbol::isDynamicResolver(unsigned long long&) const
0x1804af89c  __TEXT,__text  mach_o::Header::addressInCodeSection(unsigned long long) const
0x1804afa60  __TEXT,__text  dyld4::Loader::interpose(dyld4::RuntimeState&, unsigned long, dyld4::Loader const*)
0x1804afce8  __TEXT,__text  lsl::ProtectedStack::withProtectedStack(void  block_pointer())
0x1804afea0  __TEXT,__text  _callWithProtectedStack
0x1804aff60  __TEXT,__text  _callWithRegularStack
0x1804b0028  __TEXT,__text  invocation function for block in void lsl::MemoryManager::withProtectedStack<dyld4::RuntimeLocks::withLoadersWriteLockAndProtectedStack<dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const::{lambda()#1}>(dyld4::APIs::dlopen_from(char const*, int, void*)::$_0::operator()() const
0x1804b0030  __TEXT,__text  dyld4::Loader::forEachResolvedAtPathVar(dyld4::RuntimeState&, char const*, dyld4::Loader::LoadOptions const&, dyld4::ProcessConfig::PathOverrides::Type, bool&, void  block_pointer(char const*, dyld4::ProcessConfig::PathOverrides::Type, bool&))
0x1804b027c  __TEXT,__text  Diagnostics::appendError(char const*, ...)
0x1804b0450  __TEXT,__text  dyld4::ProcessConfig::PathOverrides::forEachFrameworkFallback(mach_o::Platform, bool, bool&, void  block_pointer(std::__1::basic_string_view<char, std::__1::char_traits<char> >, dyld4::ProcessConfig::PathOverrides::Type, bool&)) const
0x1804b0634  __TEXT,__text  _cerror
0x1804b0668  __TEXT,__text  __pthread_exit_if_canceled
0x1804b06dc  __TEXT,__text  ___simple_bprintf
0x1804b0718  __TEXT,__text  _hex
0x1804b084c  __TEXT,__text  __simple_string
0x1804b085c  __TEXT,__text  lsl::ProtectedStack::withNestedRegularStack(lsl::ProtectedStackReturnType  block_pointer())
0x1804b08e8  __TEXT,__text  invocation function for block in callback_impl::return_type<decltype (&dyld4::LibSystemHelpersWrapper::pthread_getspecific(unsigned long) const::{lambda()#1}::operator())>::type lsl::MemoryManager::withReadOnlyTPROMemory<dyld4::LibSystemHelpersWrapper::pthread_getspecific(unsigned long) const::{lamb
0x1804b0a38  __TEXT,__text  _OUTLINED_FUNCTION_6
0x1804b0a38  __TEXT,__text  _OUTLINED_FUNCTION_6
0x1804b0a48  __TEXT,__text  _OUTLINED_FUNCTION_11
0x1804b0a68  __TEXT,__text  _OUTLINED_FUNCTION_11
0x1804b0a7c  __TEXT,__text  _OUTLINED_FUNCTION_11
0x1804b0a8c  __TEXT,__text  dyld4::LibSystemHelpersWrapper::malloc(unsigned long) const
0x1804b0be0  __TEXT,__text  dyld4::LibSystemHelpersWrapper::pthread_setspecific(unsigned long, void const*) const
0x1804b0d48  __TEXT,__text  __simple_sfree
0x1804b0dd0  __TEXT,__text  dyld4::APIs::_dyld_find_foreign_type_protocol_conformance(void const*, char const*, unsigned long) const
0x1804b0ef4  __TEXT,__text  unsigned int SwiftHashTable::hash<SwiftForeignTypeProtocolConformanceLookupKey>(SwiftForeignTypeProtocolConformanceLookupKey const&, unsigned char const*) const
0x1804b0f6c  __TEXT,__text  unsigned int SwiftHashTable::getIndex<SwiftForeignTypeProtocolConformanceLookupKey, SwiftForeignTypeProtocolConformanceLocationKey>(SwiftForeignTypeProtocolConformanceLookupKey const&, unsigned char const*) const
0x1804b1030  __TEXT,__text  bool SwiftHashTable::equal<SwiftForeignTypeProtocolConformanceLookupKey, SwiftForeignTypeProtocolConformanceLocationKey>(SwiftForeignTypeProtocolConformanceLocationKey const&, SwiftForeignTypeProtocolConformanceLookupKey const&, unsigned char const*) const
0x1804b1084  __TEXT,__text  dyld4::RuntimeState::inPrebuiltLoader(void const*, unsigned long) const
0x1804b10f0  __TEXT,__text  dyld4::PrebuiltLoaderSet::contains(void const*, unsigned long) const
0x1804b1118  __TEXT,__text  invocation function for block in dyld4::JustInTimeLoader::parseSectionLocations(mach_o::UnsafeHeader const*, dyld4::SectionLocations&)
0x1804b1398  __TEXT,__text  dyld4::Loader::loadDependents(Diagnostics&, dyld4::RuntimeState&, dyld4::Loader::LoadOptions const&)
0x1804b13cc  __TEXT,__text  dyld4::JustInTimeLoader::applyFixups(Diagnostics&, dyld4::RuntimeState&, dyld4::DyldCacheDataConstLazyScopedWriter&, bool, lsl::Vector<std::__1::pair<dyld4::Loader const*, char const*> >*) const
0x1804b1768  __TEXT,__text  lsl::Vector<std::__1::pair<dyld4::Loader const*, char const*> >::reserve(unsigned long long)
0x1804b17ac  __TEXT,__text  dyld4::RuntimeState::notifyLoad(std::__1::span<dyld4::Loader const*, 18446744073709551615ul> const&)
0x1804b1d1c  __TEXT,__text  dyld4::RuntimeState::notifyLoad(std::__1::span<dyld4::Loader const*, 18446744073709551615ul> const&)::'block-literal'::$_8::operator()() const
0x1804b21a8  __TEXT,__text  dyld4::APIs::dyld_image_path_containing_address(void const*)
0x1804b2230  __TEXT,__text  dyld4::APIs::_dyld_has_preoptimized_swift_protocol_conformances(mach_header const*)
0x1804b22f8  __TEXT,__text  mach_o::UnsafeHeader::loadCommandToDylibKind(dylib_command const*)
0x1804b2398  __TEXT,__text  dyld4::APIs::setErrorString(char const*, ...)
0x1804b24ac  __TEXT,__text  __simple_salloc
0x1804b252c  __TEXT,__text  Diagnostics::errorMessage() const
0x1804b2550  __TEXT,__text  __simple_vsprintf
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
0x1804b2578  __TEXT,__text  dyld4::APIs::_libdyld_initialize() [clone .cold.1]
```
First 1,000 of 3,893.

