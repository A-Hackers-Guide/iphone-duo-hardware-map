# `MTLIOAccelDeviceShmemPool`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{_MTLIOAccelDeviceShmemPoolPrivate="queue"{shmemPoolQueue="tqh_first"@"MTLIOAccelDeviceShmem""tqh_last"^@}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"count"i"shmemClass"#"device"@"MTLIOAccelDevice""shmemSize"I} _priv;
```

## Instance methods

```
-[MTLIOAccelDeviceShmemPool shmemSize];
-[MTLIOAccelDeviceShmemPool availableCount];
-[MTLIOAccelDeviceShmemPool prune];
-[MTLIOAccelDeviceShmemPool dealloc];
-[MTLIOAccelDeviceShmemPool setShmemSize:];
-[MTLIOAccelDeviceShmemPool purge];
-[MTLIOAccelDeviceShmemPool initWithDevice:resourceClass:shmemSize:options:];
```
