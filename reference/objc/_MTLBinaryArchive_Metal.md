# `_MTLBinaryArchive`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLBinaryArchiveSPI`
- 49 instance variables, 10 properties, 103 instance methods, 6 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _options;
@"MTLLoadedFile" _fileMapping;
@"MTLLoadedFileContentsWrapper" _fileData;
I _internalArchiverId;
B _isLegacy;
B _alwaysReturnDriverReflection;
B _bitcodeStripped;
* _archiveIDInt;
B _reloadingAfterSerialization;
B _hasBuiltins;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _serializeQueue;
{map<MTLUINT256_t, std::pair<unsigned int, unsigned long long>, CompareHash, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__tree_"{__tree<std::__value_type<MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, std::__map_value_compare<MTLUINT256_t, std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, CompareHash>, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _legacyPipelineFileIndex;
@"NSMutableDictionary" _entries;
@"NSMutableDictionary" _asynEntries;
@"NSString" _absoluteOpenPath;
{unordered_map<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>, CompareFunctionIdHash, CompareFunctionIdHash, std::allocator<std::pair<const MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>>>="__table_"{__hash_table<std::__hash_value_type<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, std::__unordered_map_hasher<MTLHashKey, std::pair<const MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, CompareFunctionIdHash, CompareFunctionIdHash>, std::__unordered_map_equal<MTLHashKey, std::pair<const MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, CompareFunctionIdHash, CompareFunctionIdHash>, std::allocator<std::pair<const MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _executableFileIndex;
{unordered_map<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, std::tuple<unsigned long long, unsigned long long, unsigned long long, unsigned long long>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _reflectionsIndex;
{unordered_map<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::vector<std::pair<MTLHashKey, unsigned int>>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _airntBinaryList;
{vector<MTLAirNTObject *, std::allocator<MTLAirNTObject *>>="__begin_"^^{MTLAirNTObject}"__end_"^^{MTLAirNTObject}""{?="__cap_"^^{MTLAirNTObject}}} _airntObjectList;
{vector<MTLAirNTObject *, std::allocator<MTLAirNTObject *>>="__begin_"^^{MTLAirNTObject}"__end_"^^{MTLAirNTObject}""{?="__cap_"^^{MTLAirNTObject}}} _airntFromDescriptorFunctionList;
{vector<MTLPipelineNTObject *, std::allocator<MTLPipelineNTObject *>>="__begin_"^^{MTLPipelineNTObject}"__end_"^^{MTLPipelineNTObject}""{?="__cap_"^^{MTLPipelineNTObject}}} _airntPipelineList;
{vector<functionIdExtended, std::allocator<functionIdExtended>>="__begin_"^{functionIdExtended}"__end_"^{functionIdExtended}""{?="__cap_"^{functionIdExtended}}} _airntExtraBinaryEntries;
{unordered_map<unsigned long long, unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, unsigned long long>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, unsigned long long>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, unsigned long long>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, unsigned long long>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, unsigned long long>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned long long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned long long>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned long long>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned long long>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _airntOffsetToIndexMap;
{unordered_map<unsigned long long, id<MTLLibrarySPI>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, id<MTLLibrarySPI>>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, id<MTLLibrarySPI>>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, id<MTLLibrarySPI>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, id<MTLLibrarySPI>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, id<MTLLibrarySPI>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id<MTLLibrarySPI>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id<MTLLibrarySPI>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id<MTLLibrarySPI>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id<MTLLibrarySPI>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _libCache;
{unordered_map<MTLUINT256_t, MTLResourcePosInArchive, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, MTLResourcePosInArchive>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLResourcePosInArchive>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLResourcePosInArchive>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, MTLResourcePosInArchive>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _specializedLibraryCache;
{unordered_map<MTLUINT256_t, MTLResourcePosInArchive, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, MTLResourcePosInArchive>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLResourcePosInArchive>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLResourcePosInArchive>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, MTLResourcePosInArchive>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLResourcePosInArchive>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _stitchedLibraryCache;
{unordered_map<std::string_view, id<MTLLibrarySPI>, std::hash<basic_string_view<char, char_traits<char>>>, std::equal_to<std::string_view>, std::allocator<std::pair<const std::string_view, id<MTLLibrarySPI>>>>="__table_"{__hash_table<std::__hash_value_type<std::string_view, id<MTLLibrarySPI>>, std::__unordered_map_hasher<std::string_view, std::pair<const std::string_view, id<MTLLibrarySPI>>, std::hash<basic_string_view<char, char_traits<char>>>, std::equal_to<std::string_view>>, std::__unordered_map_equal<std::string_view, std::pair<const std::string_view, id<MTLLibrarySPI>>, std::equal_to<std::string_view>, std::hash<basic_string_view<char, char_traits<char>>>>, std::allocator<std::pair<const std::string_view, id<MTLLibrarySPI>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, id<MTLLibrarySPI>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, id<MTLLibrarySPI>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, id<MTLLibrarySPI>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, id<MTLLibrarySPI>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _extLibCache;
{unordered_map<MTLUINT256_t, MTLAirEntry *, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, MTLAirEntry *>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLAirEntry *>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLAirEntry *>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, MTLAirEntry *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _specializedFunctionByHash;
{unordered_map<MTLUINT256_t, MTLAirEntry *, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, MTLAirEntry *>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLAirEntry *>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLAirEntry *>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, MTLAirEntry *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLAirEntry *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _stitchedFunctionByHash;
{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__table_"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _librarySeen;
@"NSObject<OS_dispatch_data>" _metalScript;
{unordered_map<MTLHashKey, MTLOpaqueGPUArchiverUnitId *, CompareFunctionIdHash, CompareFunctionIdHash, std::allocator<std::pair<const MTLHashKey, MTLOpaqueGPUArchiverUnitId *>>>="__table_"{__hash_table<std::__hash_value_type<MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, std::__unordered_map_hasher<MTLHashKey, std::pair<const MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, CompareFunctionIdHash, CompareFunctionIdHash>, std::__unordered_map_equal<MTLHashKey, std::pair<const MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, CompareFunctionIdHash, CompareFunctionIdHash>, std::allocator<std::pair<const MTLHashKey, MTLOpaqueGPUArchiverUnitId *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLHashKey, MTLOpaqueGPUArchiverUnitId *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _gpuArchiverIDMap;
{unique_ptr<MTLPipelineCollection, std::default_delete<MTLPipelineCollection>>=""{?="__ptr_"^{MTLPipelineCollection}}} _pipelineCollection;
{unique_ptr<MTLMetalScriptBuilder, std::default_delete<MTLMetalScriptBuilder>>=""{?="__ptr_"^{MTLMetalScriptBuilder}}} _mtlScriptBuilder;
{shared_ptr<std::unordered_map<MTLUINT256_t, NSObject<OS_dispatch_data> *, UnorderedContainerHash, UnorderedContainerHash>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _uniqueBitcodeList;
B _collectArchives;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _serializing;
{unique_ptr<MTLArchiveLinkResolver, std::default_delete<MTLArchiveLinkResolver>>=""{?="__ptr_"^{MTLArchiveLinkResolver}}} _linkResolver;
{unordered_map<MTLUINT256_t, NSObject<OS_dispatch_data> *, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, NSObject<OS_dispatch_data> *>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, NSObject<OS_dispatch_data> *>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, NSObject<OS_dispatch_data> *>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, NSObject<OS_dispatch_data> *>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, NSObject<OS_dispatch_data> *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, NSObject<OS_dispatch_data> *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, NSObject<OS_dispatch_data> *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, NSObject<OS_dispatch_data> *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, NSObject<OS_dispatch_data> *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _legacySpecializedFunctions;
{map<MTLUINT256_t, std::pair<unsigned int, unsigned long long>, CompareHash, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__tree_"{__tree<std::__value_type<MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, std::__map_value_compare<MTLUINT256_t, std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, CompareHash>, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _legacySpecializedFunctionArchiveFileIndex;
Q _specializedFunctionArchiveOffset;
Q _specializedFunctionArchiveBytes;
{map<MTLUINT256_t, std::pair<unsigned int, unsigned long long>, CompareHash, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__tree_"{__tree<std::__value_type<MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, std::__map_value_compare<MTLUINT256_t, std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>, CompareHash>, std::allocator<std::pair<const MTLUINT256_t, std::pair<unsigned int, unsigned long long>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _recompilationArchiveFileIndex;
Q _recompilationArchiveOffset;
Q _recompilationArchiveBytes;
{unordered_map<MTLUINT256_t, MTLProgramObject *, UnorderedContainerHash, UnorderedContainerHash, std::allocator<std::pair<const MTLUINT256_t, MTLProgramObject *>>>="__table_"{__hash_table<std::__hash_value_type<MTLUINT256_t, MTLProgramObject *>, std::__unordered_map_hasher<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLProgramObject *>, UnorderedContainerHash, UnorderedContainerHash>, std::__unordered_map_equal<MTLUINT256_t, std::pair<const MTLUINT256_t, MTLProgramObject *>, UnorderedContainerHash, UnorderedContainerHash>, std::allocator<std::pair<const MTLUINT256_t, MTLProgramObject *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLProgramObject *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLProgramObject *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLProgramObject *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLUINT256_t, MTLProgramObject *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _variantMap;
Q _newBinary;
```

## Properties

```
@property (TB) recompilationTarget;
@property (TB,R) stripped;
@property (TQ,R,V_options) options;
@property (T@"NSArray",R) keys;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_MTLBinaryArchive deserializeBinaryArchiveHeader:fileData:linkResolver:device:];
+[_MTLBinaryArchive deserializeBinaryArchiveDescriptorMachO:fileData:];
+[_MTLBinaryArchive archiveTypeAtURL:device:error:];
+[_MTLBinaryArchive archiveVersionCompatible:isMatchingSlice:device:];
+[_MTLBinaryArchive sliceIDForSpecializedFunctionsForLLVMVersion:];
+[_MTLBinaryArchive descriptorDataForArchive:];
```

## Instance methods

```
-[_MTLBinaryArchive materializeFromHash:fileIndex:];
-[_MTLBinaryArchive loadFromURL:error:];
-[_MTLBinaryArchive getScriptsWithAIRNTObject:];
-[_MTLBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:error:];
-[_MTLBinaryArchive storeTileRenderPipelineDescriptor:];
-[_MTLBinaryArchive clearLibCache];
-[_MTLBinaryArchive recompileToArchiveWithURL:error:];
-[_MTLBinaryArchive requiresLegacyReflection];
-[_MTLBinaryArchive legacySerializeToURL:options:error:];
-[_MTLBinaryArchive newLibraryInArchiveWithPosition:libraryPath:];
-[_MTLBinaryArchive addStitchedLibraryWithKey:descriptors:inputFunctions:library:];
-[_MTLBinaryArchive recompileToArchive:error:];
-[_MTLBinaryArchive formattedDescription:];
-[_MTLBinaryArchive storeRenderPipelineDescriptor:];
-[_MTLBinaryArchive loadAirSliceAtOffset:sliceLength:];
-[_MTLBinaryArchive device];
-[_MTLBinaryArchive materializeEntryForKey:fileIndex:containsEntry:addEntry:];
-[_MTLBinaryArchive addFunctionWithDescriptor:library:error:];
-[_MTLBinaryArchive initMetalScriptWithArchive:];
-[_MTLBinaryArchive checkDescriptorsWithObject:error:];
-[_MTLBinaryArchive addBinaryEntryInternal:forKey:];
-[_MTLBinaryArchive dealloc];
-[_MTLBinaryArchive getArchiveIDWithError:];
-[_MTLBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:options:error:];
-[_MTLBinaryArchive reflectionHashWithFunctionId:binaryPos:];
-[_MTLBinaryArchive findProgramObjectForFunction:];
-[_MTLBinaryArchive getSpecializedFunctionArchivesToSerialize:];
-[_MTLBinaryArchive setMTLLinkedFunctions:LFS:obj:destinationArchive:error:];
-[_MTLBinaryArchive materializeAirNTSpecializedFunctions:];
-[_MTLBinaryArchive addComputePipelineFunctionsWithDescriptor:options:error:];
-[_MTLBinaryArchive preloadLibrariesInAirntObject:error:];
-[_MTLBinaryArchive newSpecializedFunctionWithHash:libraryPath:];
-[_MTLBinaryArchive materializeBitCode:atIndex:];
-[_MTLBinaryArchive newRecompiledFunctionWithAIRNTObject:index:destinationArchive:error:];
-[_MTLBinaryArchive newComputePipelineDescriptorWithScript:obj:destinationArchive:error:];
-[_MTLBinaryArchive pipelineCollection];
-[_MTLBinaryArchive deallocContainers];
-[_MTLBinaryArchive materializeAll];
-[_MTLBinaryArchive newArchiverIdWithBinaryKey:entry:srcArchiverId:functionType:];
-[_MTLBinaryArchive materializeLinkedBitcodes:hashList:];
-[_MTLBinaryArchive stripped];
-[_MTLBinaryArchive remoteInsertionBegin];
-[_MTLBinaryArchive newMeshRenderPipelineDescriptorWithScript:obj:destinationArchive:error:];
-[_MTLBinaryArchive enumerateArchivesFromBackingFile:];
-[_MTLBinaryArchive keys];
-[_MTLBinaryArchive addBinaryEntryImpl:forKey:];
-[_MTLBinaryArchive getMetalScript];
-[_MTLBinaryArchive materializeAirNTFromOnlineForSlice:entryList:];
-[_MTLBinaryArchive archiveSkipsAIRValidation];
-[_MTLBinaryArchive addStitchingInputsFunction:toEntry:];
-[_MTLBinaryArchive localStitchedFunctionLookupWithDescriptor:];
-[_MTLBinaryArchive enumerateArchivesFromBackingFileFromSlice:version:verifyKey:offset:bytes:enumerator:];
-[_MTLBinaryArchive initWithOptions:device:url:error:];
-[_MTLBinaryArchive newArchiveDataForKeyInternal:];
-[_MTLBinaryArchive recompilePipelinesToArchive:error:];
-[_MTLBinaryArchive getBinaryDataForKey:reflectionType:];
-[_MTLBinaryArchive addArchiveEntryInternal:forKey:];
-[_MTLBinaryArchive programObjectForFunction:];
-[_MTLBinaryArchive materializeAIRNTBlockForKey:reflectionType:];
-[_MTLBinaryArchive storeMeshRenderPipelineDescriptor:];
-[_MTLBinaryArchive recompilationTarget];
-[_MTLBinaryArchive setRecompilationTarget:];
-[_MTLBinaryArchive newStitchedLibraryWithKey:descriptors:];
-[_MTLBinaryArchive addRenderPipelineFunctionsWithDescriptor:error:];
-[_MTLBinaryArchive updateReflectionForEntry:binaryKey:requiredReflection:];
-[_MTLBinaryArchive loadAirntBlocksForSlice:sliceOffset:skipAIRValidation:];
-[_MTLBinaryArchive storeComputePipelineDescriptor:];
-[_MTLBinaryArchive removeComputePipelineFunctionsWithDescriptor:error:];
-[_MTLBinaryArchive getLibraryDescriptorWithAirScrpt:];
-[_MTLBinaryArchive description];
-[_MTLBinaryArchive serializeToURL:error:];
-[_MTLBinaryArchive enumerateSpecializedFunctionArchivesFromBackingFile:];
-[_MTLBinaryArchive newLibraryInArchiveAtPos:atIndex:error:];
-[_MTLBinaryArchive materializeReflectionBlock:];
-[_MTLBinaryArchive airntSerializeToURL:options:error:];
-[_MTLBinaryArchive materializeFromFileOffset:hash:];
-[_MTLBinaryArchive newLibraryInArchiveWithPosition:];
-[_MTLBinaryArchive options];
-[_MTLBinaryArchive recompileFunction:inLibrary:toArchive:toBinary:error:];
-[_MTLBinaryArchive initWithDevice:descriptor:error:];
-[_MTLBinaryArchive getFunctionNameFromAirDescriptor:];
-[_MTLBinaryArchive loadFileIndex:expectedSliceId:expectedVersion:sliceOffset:];
-[_MTLBinaryArchive updatePipelineWithPipelineArchiverId:key:functionType:];
-[_MTLBinaryArchive newTileRenderPipelineDescriptorWithScript:obj:destinationArchive:error:];
-[_MTLBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:error:];
-[_MTLBinaryArchive materializeAirNTStitchedFunctions:];
-[_MTLBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:options:error:];
-[_MTLBinaryArchive getArchiveIDWithErrorInternal:];
-[_MTLBinaryArchive addLibraryWithDescriptor:error:];
-[_MTLBinaryArchive recompileStatelessToArchive:error:];
-[_MTLBinaryArchive materializeAllAIRNTLegacy];
-[_MTLBinaryArchive archiveFunctionIds];
-[_MTLBinaryArchive serializeToURL:options:error:];
-[_MTLBinaryArchive newRecompiledFunctionWithAIRNTObject:destinationArchive:error:];
-[_MTLBinaryArchive addComputePipelineFunctionsWithDescriptor:error:];
-[_MTLBinaryArchive enumerateArchivesFromPipelineCollection:];
-[_MTLBinaryArchive remoteInsertionEnd];
-[_MTLBinaryArchive materializeAirScript:];
-[_MTLBinaryArchive materializeAirNTAllForSlice:entryList:];
-[_MTLBinaryArchive addRenderPipelineFunctionsWithDescriptor:options:error:];
-[_MTLBinaryArchive supportsAIRNT];
-[_MTLBinaryArchive newRenderPipelineDescriptorWithScript:obj:destinationArchive:error:];
-[_MTLBinaryArchive newFunctionDescriptorWithAirScript:];
```
