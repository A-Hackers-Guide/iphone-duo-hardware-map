# `BLSHFlipbookHistoryFrame`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSDiagnosticFlipbookFrame`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<BLSHRenderedFlipbookFrame>" _lock_retainedHostFrame;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHRenderedFlipbookFrame>" _hostFrame;
```

## Properties

```
@property (TB,R,N,GisRetainingSurface) retainingSurface;
@property (TQ,R,N) retainedMemoryUsage;
@property (T@"<BLSHRenderedFlipbookFrame>",R,W,N,V_hostFrame) hostFrame;
```

## Instance methods

```
-[BLSHFlipbookHistoryFrame surface];
-[BLSHFlipbookHistoryFrame description];
-[BLSHFlipbookHistoryFrame initWithFrame:];
-[BLSHFlipbookHistoryFrame rawSurface];
-[BLSHFlipbookHistoryFrame hostFrame];
-[BLSHFlipbookHistoryFrame isRetainingSurface];
-[BLSHFlipbookHistoryFrame retainedMemoryUsage];
-[BLSHFlipbookHistoryFrame stopRetainingSurface];
```
