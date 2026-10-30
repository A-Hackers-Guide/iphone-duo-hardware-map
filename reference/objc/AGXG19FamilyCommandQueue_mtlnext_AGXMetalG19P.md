# `AGXG19FamilyCommandQueue_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4CommandQueue`
- Protocols: `MTL4CommandQueueSPI`
- 5 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
{vector<id<MTL4CommandBuffer>, std::allocator<id<MTL4CommandBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} post_merge_command_buffers;
{vector<StoreActionGroup, std::allocator<StoreActionGroup>>="__begin_"^{StoreActionGroup}"__end_"^{StoreActionGroup}""{?="__cap_"^{StoreActionGroup}}} store_action_groups;
B needs_sstt_cfi;
@"AGXG19FamilyDevice" _device_objc;
B _isDriverInternal;
```

## Properties

```
@property (T@"<MTL4CommandBuffer>",R,N) lastCommittedCommandBuffer;
@property (TQ,R,N) lastCommittedCommandBufferGeneration;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyCommandQueue_mtlnext setGPUPriority:];
-[AGXG19FamilyCommandQueue_mtlnext initWithDevice:];
-[AGXG19FamilyCommandQueue_mtlnext initWithDevice:descriptor:];
-[AGXG19FamilyCommandQueue_mtlnext commit:count:];
-[AGXG19FamilyCommandQueue_mtlnext commit:count:options:];
-[AGXG19FamilyCommandQueue_mtlnext copyTextureMappingsFromTexture:toTexture:operations:count:];
-[AGXG19FamilyCommandQueue_mtlnext updateTextureMappings:heap:operations:count:];
-[AGXG19FamilyCommandQueue_mtlnext endTier1MappingCommands];
-[AGXG19FamilyCommandQueue_mtlnext initWithDevice:descriptor:isDriverInternal:];
-[AGXG19FamilyCommandQueue_mtlnext noMergeCommit:count:options:commitFeedback:error:];
-[AGXG19FamilyCommandQueue_mtlnext resolveAndUpdateQueuePriority:];
```
