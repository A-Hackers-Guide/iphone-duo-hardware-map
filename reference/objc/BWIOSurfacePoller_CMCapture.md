# `BWIOSurfacePoller`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _pollingTimer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _trackedSurfacesLock;
@"NSMutableArray" _trackedSurfaces;
```

## Class methods

```
+[BWIOSurfacePoller trackSurface:useCountIsZeroHandler:];
```

## Instance methods

```
-[BWIOSurfacePoller init];
-[BWIOSurfacePoller dealloc];
```
