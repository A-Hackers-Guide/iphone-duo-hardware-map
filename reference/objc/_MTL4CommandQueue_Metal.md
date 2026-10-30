# `_MTL4CommandQueue`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CommandQueueGGDSPI`
- 9 instance variables, 11 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _globalTraceObjectID;
Q _labelTraceID;
i _backgroundTrackingPID;
@"NSObject<OS_dispatch_queue>" _submissionQueue;
@"<MTL4CommandBuffer>" _lastCommittedCommandBuffer;
Q _lastCommittedCommandBufferGeneration;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _mlCommandQueueLock;
@"<MTLCommandQueue>" _mlCommandQueue;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (Ti,R,V_backgroundTrackingPID) backgroundTrackingPID;
@property (T@"<MTL4CommandBuffer>",R,N,V_lastCommittedCommandBuffer) lastCommittedCommandBuffer;
@property (TQ,R,N,V_lastCommittedCommandBufferGeneration) lastCommittedCommandBufferGeneration;
@property (T@"<MTLCommandQueue>",R) mlCommandQueue;
@property (T@"NSString",R) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4CommandQueue removeInternalResidencySets:count:];
-[_MTL4CommandQueue removeResidencySet:];
-[_MTL4CommandQueue setGPUPriority:];
-[_MTL4CommandQueue initWithDevice:];
-[_MTL4CommandQueue removeInternalResidencySet:];
-[_MTL4CommandQueue addInternalResidencySet:];
-[_MTL4CommandQueue addInternalResidencySets:count:];
-[_MTL4CommandQueue addResidencySets:count:];
-[_MTL4CommandQueue removeResidencySets:count:];
-[_MTL4CommandQueue device];
-[_MTL4CommandQueue backgroundTrackingPID];
-[_MTL4CommandQueue addResidencySet:];
-[_MTL4CommandQueue globalTraceObjectID];
-[_MTL4CommandQueue dealloc];
-[_MTL4CommandQueue getBackgroundGPUPriority];
-[_MTL4CommandQueue getGPUPriority];
-[_MTL4CommandQueue setBackgroundGPUPriority:];
-[_MTL4CommandQueue commitBlock:];
-[_MTL4CommandQueue signalEvent:value:];
-[_MTL4CommandQueue waitForEvent:value:];
-[_MTL4CommandQueue signalDrawable:];
-[_MTL4CommandQueue commit:count:];
-[_MTL4CommandQueue commit:count:options:];
-[_MTL4CommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[_MTL4CommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:];
-[_MTL4CommandQueue updateBufferMappings:heap:operations:count:];
-[_MTL4CommandQueue updateTextureMappings:heap:operations:count:];
-[_MTL4CommandQueue waitForDrawable:];
-[_MTL4CommandQueue initWithDescriptor:device:];
-[_MTL4CommandQueue lastCommittedCommandBuffer];
-[_MTL4CommandQueue lastCommittedCommandBufferGeneration];
-[_MTL4CommandQueue mlCommandQueue];
-[_MTL4CommandQueue preCommit:count:error:];
-[_MTL4CommandQueue preCommit:count:options:];
-[_MTL4CommandQueue waitForEvent:value:timeout:];
```
