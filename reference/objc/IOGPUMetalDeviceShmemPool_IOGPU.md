# `IOGPUMetalDeviceShmemPool`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{_IOGPUMetalDeviceShmemPoolPrivate="queue"{shmemPoolQueue="tqh_first"@"IOGPUMetalDeviceShmem""tqh_last"^@}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"count"i"shmemClass"#"device"@"IOGPUMetalDevice""shmemSize"I"shmemType"i} _priv;
Q _allocatedSize;
```

## Instance methods

```
-[IOGPUMetalDeviceShmemPool shmemSize];
-[IOGPUMetalDeviceShmemPool availableCount];
-[IOGPUMetalDeviceShmemPool prune];
-[IOGPUMetalDeviceShmemPool allocatedSize];
-[IOGPUMetalDeviceShmemPool dealloc];
-[IOGPUMetalDeviceShmemPool initWithDevice:resourceClass:shmemSize:shmemType:options:];
-[IOGPUMetalDeviceShmemPool setShmemSize:];
-[IOGPUMetalDeviceShmemPool purge];
```
