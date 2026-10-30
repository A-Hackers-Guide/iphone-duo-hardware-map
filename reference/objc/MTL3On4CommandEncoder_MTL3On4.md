# `MTL3On4CommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLCommandEncoderSPI`
- 6 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MTL3On4CommandBuffer" _commandBuffer;
@"<MTLResidencySet>" _residencySet;
@"<MTL4CommandEncoder>" _commandEncoder;
@"<MTLDevice>" _device;
{unordered_map<id<MTLResource>, unsigned long, std::hash<id<MTLResource>>, std::equal_to<id<MTLResource>>, std::allocator<std::pair<const id<MTLResource>, unsigned long>>>="__table_"{__hash_table<std::__hash_value_type<id<MTLResource>, unsigned long>, std::__unordered_map_hasher<id<MTLResource>, std::pair<const id<MTLResource>, unsigned long>, std::hash<id<MTLResource>>, std::equal_to<id<MTLResource>>>, std::__unordered_map_equal<id<MTLResource>, std::pair<const id<MTLResource>, unsigned long>, std::equal_to<id<MTLResource>>, std::hash<id<MTLResource>>>, std::allocator<std::pair<const id<MTLResource>, unsigned long>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLResource>, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLResource>, unsigned long>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLResource>, unsigned long>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLResource>, unsigned long>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _usedHazardTrackedResources;
{vector<MTL3On4CachedHazard, std::allocator<MTL3On4CachedHazard>>="__begin_"^{MTL3On4CachedHazard}"__end_"^{MTL3On4CachedHazard}""{?="__cap_"^{MTL3On4CachedHazard}}} _cachedHazards;
```

## Properties

```
@property (T@"MTL3On4CommandBuffer",R,N,V_commandBuffer) commandBuffer;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL3On4CommandEncoder insertDebugSignpost:];
-[MTL3On4CommandEncoder pushDebugGroup:];
-[MTL3On4CommandEncoder popDebugGroup];
-[MTL3On4CommandEncoder device];
-[MTL3On4CommandEncoder endEncoding];
-[MTL3On4CommandEncoder globalTraceObjectID];
-[MTL3On4CommandEncoder dealloc];
-[MTL3On4CommandEncoder commandBuffer];
-[MTL3On4CommandEncoder barrierAfterQueueStages:beforeStages:];
-[MTL3On4CommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTL3On4CommandEncoder insertSplit];
-[MTL3On4CommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:residencySet:];
-[MTL3On4CommandEncoder updateHazardsAfterEncoderStages:];
-[MTL3On4CommandEncoder useResourceImpl:usage:];
-[MTL3On4CommandEncoder useResourcesImpl:count:usage:];
-[MTL3On4CommandEncoder waitForHazardsBeforeEncoderStages:];
```
