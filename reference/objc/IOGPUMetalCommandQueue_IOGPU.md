# `IOGPUMetalCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLCommandQueue`
- 7 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
^{__IOGPUCommandQueue=} _commandQueue;
@"IOGPUMetalDevice<MTLDevice>" _device;
B _disableAsyncCompletionDispatch;
Q _priority;
Q _backgroundPriority;
[2@"NSCountedSet"] _resourceGroups;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceGroupsLock;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
```

## Instance methods

```
-[IOGPUMetalCommandQueue removeInternalResidencySets:count:];
-[IOGPUMetalCommandQueue dispatchAvailableCompletionNotifications];
-[IOGPUMetalCommandQueue removeResidencySet:];
-[IOGPUMetalCommandQueue setGPUPriority:];
-[IOGPUMetalCommandQueue initWithDevice:descriptor:];
-[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:];
-[IOGPUMetalCommandQueue removeInternalResidencySet:];
-[IOGPUMetalCommandQueue addInternalResidencySet:];
-[IOGPUMetalCommandQueue addInternalResidencySets:count:];
-[IOGPUMetalCommandQueue addResidencySets:count:];
-[IOGPUMetalCommandQueue removeResidencySets:count:];
-[IOGPUMetalCommandQueue device];
-[IOGPUMetalCommandQueue setLabel:];
-[IOGPUMetalCommandQueue addResidencySet:];
-[IOGPUMetalCommandQueue setBackgroundGPUPriority:offset:];
-[IOGPUMetalCommandQueue dealloc];
-[IOGPUMetalCommandQueue submitCommandBuffers:count:];
-[IOGPUMetalCommandQueue _setGPUPriority:backgroundPriority:];
-[IOGPUMetalCommandQueue getBackgroundGPUPriority];
-[IOGPUMetalCommandQueue supportsBackgroundAppRole];
-[IOGPUMetalCommandQueue setGPUPriority:offset:];
-[IOGPUMetalCommandQueue _submitCommandBuffers:count:];
-[IOGPUMetalCommandQueue getGPUPriority];
-[IOGPUMetalCommandQueue setCompletionQueue:];
-[IOGPUMetalCommandQueue setBackgroundGPUPriority:];
```
