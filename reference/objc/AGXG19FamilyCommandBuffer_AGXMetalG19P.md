# `AGXG19FamilyCommandBuffer`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalCommandBuffer`
- Protocols: `MTLCommandBufferSPI`
- 15 instance variables, 29 properties, 59 instance methods, 0 class methods

## Instance variables

```
@"AGXG19FamilyBlitContext" _previousBlitCommandEncoder;
@"AGXG19FamilyComputeContext" _previousComputeCommandEncoder;
@"AGXG19FamilyRenderContext" _previousRenderCommandEncoder;
{AGXATelemetryUsage="usage"[2Q]} _telemetryUsage;
^v _impl;
B _disableDeferredEndEncoding;
{vector<AGXG19FamilyTexture *, std::allocator<AGXG19FamilyTexture *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} texturesToEvaluate;
B _captureProgramAddressTable;
B _cloneIntersectionFunctionTablesPerDispatch;
B hasEncoded;
B enableContentProtection;
B needsProtectedContentBarrier;
Q oldProtectionOptions;
I deadline_namespace_id;
Q deadline;
```

## Properties

```
@property (TQ,R,GgetSupportedAndEnabledErrorOptions) supportedAndEnabledErrorOptions;
@property (TB,V_disableDeferredEndEncoding) disableDeferredEndEncoding;
@property (TI,Vdeadline_namespace_id) deadline_namespace_id;
@property (TQ,Vdeadline) deadline;
@property (TQ,?,R,N,GgetListIndex) listIndex;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (T@"NSDictionary",R) profilingResults;
@property (T@"NSMutableDictionary",R,N) userDictionary;
@property (TQ,?,R) globalTraceObjectID;
@property (T@"<MTLBuffer>",?,&,N) privateData;
@property (TQ,?,N) privateDataOffset;
@property (T@"<MTLBuffer>",?,N) privateLoggingBuffer;
@property (T@"<MTLDeadlineProfile>",R,&) deadlineProfile;
@property (T@"<MTLDevice>",R) device;
@property (T@"<MTLCommandQueue>",R) commandQueue;
@property (TB,R) retainedReferences;
@property (TQ,R) errorOptions;
@property (T@"NSString",C) label;
@property (Td,R) kernelStartTime;
@property (Td,R) kernelEndTime;
@property (T@"<MTLLogContainer>",R) logs;
@property (Td,R) GPUStartTime;
@property (Td,R) GPUEndTime;
@property (TQ,R) status;
@property (T@"NSError",R) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyCommandBuffer validate];
-[AGXG19FamilyCommandBuffer commitWithDeadline:];
-[AGXG19FamilyCommandBuffer encodeSignalEvent:value:agentMask:];
-[AGXG19FamilyCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[AGXG19FamilyCommandBuffer encodeDashboardTagForResourceGroup:];
-[AGXG19FamilyCommandBuffer setProtectionOptions:];
-[AGXG19FamilyCommandBuffer setCurrentCommandEncoder:];
-[AGXG19FamilyCommandBuffer initWithQueue:retainedReferences:];
-[AGXG19FamilyCommandBuffer blitCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer getDriverEncoderInfoData:];
-[AGXG19FamilyCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[AGXG19FamilyCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer fillCommandBufferArgs:commandQueue:];
-[AGXG19FamilyCommandBuffer computeCommandEncoderWithDispatchType:];
-[AGXG19FamilyCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer commit];
-[AGXG19FamilyCommandBuffer computeCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer accelerationStructureCommandEncoder];
-[AGXG19FamilyCommandBuffer encodeSignalEvent:value:];
-[AGXG19FamilyCommandBuffer computeCommandEncoder];
-[AGXG19FamilyCommandBuffer dealloc];
-[AGXG19FamilyCommandBuffer commitEncoder];
-[AGXG19FamilyCommandBuffer encodeWaitForEvent:value:];
-[AGXG19FamilyCommandBuffer encodeWaitForEvent:value:timeout:];
-[AGXG19FamilyCommandBuffer blitCommandEncoder];
-[AGXG19FamilyCommandBuffer encodeCacheHintFinalize:resourceGroups:count:];
-[AGXG19FamilyCommandBuffer encodeCacheHintTag:resourceGroups:count:];
-[AGXG19FamilyCommandBuffer renderCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer resourceStateCommandEncoder];
-[AGXG19FamilyCommandBuffer reserveKernelCommandBufferSpace:];
-[AGXG19FamilyCommandBuffer deadline];
-[AGXG19FamilyCommandBuffer computeCommandEncoderWithDispatchType:substreamCount:];
-[AGXG19FamilyCommandBuffer dropResourceGroups:count:];
-[AGXG19FamilyCommandBuffer setResourceGroups:count:];
-[AGXG19FamilyCommandBuffer isBlitEncoderCoalescingDisabled];
-[AGXG19FamilyCommandBuffer _accelerationStructureCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer blitCommandEncoderCommon:];
-[AGXG19FamilyCommandBuffer computeCommandEncoderWithConfig:];
-[AGXG19FamilyCommandBuffer deadline_namespace_id];
-[AGXG19FamilyCommandBuffer disableDeferredEndEncoding];
-[AGXG19FamilyCommandBuffer getSupportedAndEnabledErrorOptions];
-[AGXG19FamilyCommandBuffer gtpContinuePreParse];
-[AGXG19FamilyCommandBuffer isComputeEncoderCoalescingDisabled];
-[AGXG19FamilyCommandBuffer isEncoderCoalescingDisabled];
-[AGXG19FamilyCommandBuffer sampledComputeCommandEncoderWithConfig:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer sampledSubRenderCommandEncoderWithDescriptor:subEncoderIndex:framebuffer:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer setDeadline:];
-[AGXG19FamilyCommandBuffer setDeadline_namespace_id:];
-[AGXG19FamilyCommandBuffer setDisableDeferredEndEncoding:];
-[AGXG19FamilyCommandBuffer setPreviousBlitCommandEncoder:];
-[AGXG19FamilyCommandBuffer setPreviousComputeCommandEncoder:];
-[AGXG19FamilyCommandBuffer setPreviousRenderCommandEncoder:];
-[AGXG19FamilyCommandBuffer subRenderCommandEncoderWithDescriptor:subEncoderIndex:framebuffer:];
-[AGXG19FamilyCommandBuffer tryCoalescingPreviousComputeCommandEncoderWithConfig:nextEncoderClass:];
```
