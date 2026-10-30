# `BWIOSurfaceTracking`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 2 instance methods, 4 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _trackedSurfacesLock;
@"NSMutableArray" _trackedSurfaces;
```

## Class methods

```
+[BWIOSurfaceTracking initialize];
+[BWIOSurfaceTracking noteSurfaceIDInUse:byClient:];
+[BWIOSurfaceTracking noteSurfaceIDNoLongerInUse:byClient:];
+[BWIOSurfaceTracking trackPixelBuffer:surfaceUseCountIsZeroHandler:];
```

## Instance methods

```
-[BWIOSurfaceTracking init];
-[BWIOSurfaceTracking dealloc];
```
