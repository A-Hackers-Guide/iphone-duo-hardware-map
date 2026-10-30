# `/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator`

iOS 27.2 dyld shared cache image. Version `491.0.0.0.0`. **[DSC]**

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 1 classes, 0 protocols, 8 methods, 1 properties

### Class pages

Every class and protocol, with its methods: [`IOAccelMTLEvent`](../objc/IOAccelMTLEvent_IOAccelerator.md)

### Classes

`IOAccelMTLEvent`

### Properties

```
@property (TB,R) supportsRollback;
```

## Strings (47)

```
<IOAccelDevice %p connect=%08x refcnt=%d>
IOAccelShared
IOAccelContextRef.c
IOAccelCommandQueue.c
IOAccelResource
/Library/Caches/com.apple.xbs/0BAD7529-220A-416A-B515-C6FC1778BEAA/TemporaryDirectory.Nj5kYg/Sources/IOAcceleratorFamily/Framework/IOAccelResourceRef.c
IOAccelResourceList.c
ioAccelResourceGroupMergeNewResource
v8@?0
com.apple.IOAccelerator.CommandQueueCompletion
ioAccelResourceListMergeNewResource
v12@?0i8
v16@?0^v8
Payload
IOAccelDevice
IOAccelDeviceRef.c
com.apple.IOAccelerator.BlockFences
context->context_connect
Resource freed while busy
<IOAccelResource %p id=%08x refcnt=%d>
ioAccelResourceGroupAddNewResource
CheckIn
getNextGIDGroup
0 != gid_group_data.gid_group_min
!context->fenceNotificationPort
result == kIOReturnSuccess
<IOAccelCommandQueue %p connect=%08x refcnt=%d>
ioAccelResourceListAddNewGroupAndResource
context
wakePort
IOAccelContext
refcon != NULL
l->remainingBytes <= l->threshold
l->numResourceGroups < l->capacity
IOAccelContextEnableBlockFences
<IOAccelContext %p connect=%08x refcnt=%d>
ioAccelContextBlockFenceCallback
IOAccelCommandQueueCreateWithQoS
<IOAccelShared %p connect=%08x refcnt=%d>
queue
IOAccelCommandQueue
com.apple.gpumemd.check_in_request
block
ioAccelCommandQueueBlockFenceCallback
Resource at %d(%d,%d) is %08x\n
com.apple.gpumemd.source
Failed to create an IOAccelDevice... IOServiceOpen returned kIOReturn(0x%X)
```
