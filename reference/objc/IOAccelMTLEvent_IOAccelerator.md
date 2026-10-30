# `IOAccelMTLEvent`

- Image: [`/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator`](../userland/System__Library__PrivateFrameworks__IOAccelerator.framework__IOAccelerator.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{__IOAccelShared={__CFRuntimeBase=QAQ}^{__IOAccelDevice}I@?Q{os_unfair_lock_s=I}^{IOAcceldirtyRingRO}^{IOAcceldirtyRingRW}^{IOAccelDirtyResourceCommand}I{os_unfair_lock_s=I}{shmemlog_list=^{_s_shmemlog_}}^Q} _sharedRef;
I _eventName;
Q _globalTraceObjectID;
Q _eventOptions;
```

## Properties

```
@property (TB,R) supportsRollback;
```

## Instance methods

```
-[IOAccelMTLEvent dealloc];
-[IOAccelMTLEvent supportsRollback];
-[IOAccelMTLEvent encodeKernelSignalEventCommandArgs:value:];
-[IOAccelMTLEvent encodeKernelWaitEventCommandArgs:value:];
-[IOAccelMTLEvent encodeKernelWaitEventCommandArgs:value:timeout:];
-[IOAccelMTLEvent initWithShared:options:];
-[IOAccelMTLEvent initWithShared:];
-[IOAccelMTLEvent encodeKernelWaitEventCommandArgs:];
```
