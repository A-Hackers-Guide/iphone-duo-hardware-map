# `IOGPUMetalDeviceShmem`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
{_IOGPUMetalDeviceShmemPrivate="pool"@"IOGPUMetalDeviceShmemPool""entry"{?="tqe_next"@"IOGPUMetalDeviceShmem""tqe_prev"^@}"time_added"Q"trim_level"q"used_history"[8q]"used_history_index"i} _priv;
@"IOGPUMetalDevice" _device;
I _shmemID;
I _shmemSize;
^v _virtualAddress;
B purgeable;
```

## Properties

```
@property (T^v,R,V_virtualAddress) virtualAddress;
@property (TI,R,V_shmemID) shmemID;
@property (TI,R,V_shmemSize) shmemSize;
```

## Instance methods

```
-[IOGPUMetalDeviceShmem shmemSize];
-[IOGPUMetalDeviceShmem dealloc];
-[IOGPUMetalDeviceShmem shmemID];
-[IOGPUMetalDeviceShmem initWithDevice:shmemSize:shmemType:];
-[IOGPUMetalDeviceShmem virtualAddress];
```
