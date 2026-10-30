# `GPUDebugRetainedReportingData`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
{vector<MetalBuffer, std::allocator<MetalBuffer>>="__begin_"^{MetalBuffer}"__end_"^{MetalBuffer}""{?="__cap_"^{MetalBuffer}}} _usedBuffers;
@"<MTLBuffer>" _privateData;
@"NSMutableArray" _cbAllocations;
@"NSMutableArray" _usedPipelineStates;
@"NSMutableArray" _preCommitLogs;
{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, NSString *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _encoderLabels;
```

## Properties

```
@property (T{vector<MetalBuffer, std::allocator<MetalBuffer>>=^{MetalBuffer}^{MetalBuffer}{?=^{MetalBuffer}}},V_usedBuffers) usedBuffers;
@property (T@"NSMutableArray",V_cbAllocations) cbAllocations;
@property (T@"<MTLBuffer>",V_privateData) privateData;
@property (T{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>={__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, NSString *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=^v}}{?=Q}{?=f}}},V_encoderLabels) encoderLabels;
@property (T@"NSMutableArray",V_usedPipelineStates) usedPipelineStates;
@property (T@"NSMutableArray",V_preCommitLogs) preCommitLogs;
```

## Instance methods

```
-[GPUDebugRetainedReportingData initWithDevice:];
-[GPUDebugRetainedReportingData setPrivateData:];
-[GPUDebugRetainedReportingData privateData];
-[GPUDebugRetainedReportingData dealloc];
-[GPUDebugRetainedReportingData setUsedBuffers:];
-[GPUDebugRetainedReportingData addUsedBuffer:];
-[GPUDebugRetainedReportingData cbAllocations];
-[GPUDebugRetainedReportingData encoderLabels];
-[GPUDebugRetainedReportingData preCommitLogs];
-[GPUDebugRetainedReportingData setCbAllocations:];
-[GPUDebugRetainedReportingData setEncoderLabelForIndex:encoderIndex:];
-[GPUDebugRetainedReportingData setEncoderLabels:];
-[GPUDebugRetainedReportingData setPreCommitLogs:];
-[GPUDebugRetainedReportingData setUsedPipelineStates:];
-[GPUDebugRetainedReportingData usedBuffers];
-[GPUDebugRetainedReportingData usedPipelineStates];
```
