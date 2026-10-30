# `IOGPUMetal4CommandQueue`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandQueue`
- 16 instance variables, 0 properties, 34 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _mappingLock;
@"IOGPUMetal4CommandBuffer" _mappingCommandBuffer;
@"<MTLSharedEventSPI>" _postMappingEvent;
Q _postMappingValue;
B _disableAsyncMapping;
B _tier1ResourceMapping;
^{__IOGPUCommandQueue=} _commandQueue;
i _qosLevel;
@"NSObject<OS_dispatch_queue>" _completionQueue;
[2@"NSCountedSet"] _resourceGroups;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceGroupsLock;
@"IOGPUMetal4CommandAllocator" _commandAllocator;
Q _lastSubmissionID;
Q _priority;
Q _backgroundPriority;
@? _scheduledHandler;
```

## Instance methods

```
-[IOGPUMetal4CommandQueue removeInternalResidencySets:count:];
-[IOGPUMetal4CommandQueue removeResidencySet:];
-[IOGPUMetal4CommandQueue setGPUPriority:];
-[IOGPUMetal4CommandQueue initWithDevice:];
-[IOGPUMetal4CommandQueue initWithDevice:descriptor:];
-[IOGPUMetal4CommandQueue initWithDevice:descriptor:args:argsSize:];
-[IOGPUMetal4CommandQueue removeInternalResidencySet:];
-[IOGPUMetal4CommandQueue addInternalResidencySet:];
-[IOGPUMetal4CommandQueue addInternalResidencySets:count:];
-[IOGPUMetal4CommandQueue addResidencySets:count:];
-[IOGPUMetal4CommandQueue removeResidencySets:count:];
-[IOGPUMetal4CommandQueue addResidencySet:];
-[IOGPUMetal4CommandQueue dealloc];
-[IOGPUMetal4CommandQueue _setGPUPriority:backgroundPriority:];
-[IOGPUMetal4CommandQueue getBackgroundGPUPriority];
-[IOGPUMetal4CommandQueue supportsBackgroundAppRole];
-[IOGPUMetal4CommandQueue getGPUPriority];
-[IOGPUMetal4CommandQueue setBackgroundGPUPriority:];
-[IOGPUMetal4CommandQueue commitBlock:];
-[IOGPUMetal4CommandQueue signalEvent:value:];
-[IOGPUMetal4CommandQueue waitForEvent:value:];
-[IOGPUMetal4CommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[IOGPUMetal4CommandQueue updateBufferMappings:heap:operations:count:];
-[IOGPUMetal4CommandQueue setScheduledHandler:];
-[IOGPUMetal4CommandQueue commandAllocator];
-[IOGPUMetal4CommandQueue preCommit:count:options:];
-[IOGPUMetal4CommandQueue waitForEvent:value:timeout:];
-[IOGPUMetal4CommandQueue _commit:count:commitFeedback:];
-[IOGPUMetal4CommandQueue allocateMappingCommandBuffer];
-[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:commandBufferGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:];
-[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:];
-[IOGPUMetal4CommandQueue commitMappingCommandBuffer];
-[IOGPUMetal4CommandQueue endTier1MappingCommands];
-[IOGPUMetal4CommandQueue initIOGPUMTL4CommandQueue:descriptor:args:argsSize:];
```
