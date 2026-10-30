# `IOSurfaceRemotePerSurfaceGlobalState`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
I _csid;
^v _mapped_address;
Q _mapped_size;
@"NSObject<OS_xpc_object>" _extraData;
```

## Class methods

```
+[IOSurfaceRemotePerSurfaceGlobalState globalStateForSurface:mappedAddress:mappedSize:extraData:];
```

## Instance methods

```
-[IOSurfaceRemotePerSurfaceGlobalState dealloc];
-[IOSurfaceRemotePerSurfaceGlobalState mergeExtraData:];
-[IOSurfaceRemotePerSurfaceGlobalState initWithSurfaceID:mappedAddress:mappedSize:extraData:];
```
