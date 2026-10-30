# `MTLIOAccelDeviceShmem`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
{_MTLIOAccelDeviceShmemPrivate="pool"@"MTLIOAccelDeviceShmemPool""entry"{?="tqe_next"@"MTLIOAccelDeviceShmem""tqe_prev"^@}"time_added"Q} _priv;
@"MTLIOAccelDevice" _device;
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
-[MTLIOAccelDeviceShmem shmemSize];
-[MTLIOAccelDeviceShmem dealloc];
-[MTLIOAccelDeviceShmem shmemID];
-[MTLIOAccelDeviceShmem virtualAddress];
-[MTLIOAccelDeviceShmem initWithDevice:shmemSize:];
```
