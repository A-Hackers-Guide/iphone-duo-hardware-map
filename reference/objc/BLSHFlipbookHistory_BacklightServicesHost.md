# `BLSHFlipbookHistory`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _frameLimit;
Q _memoryLimit;
@"NSMutableArray" _lock_frames;
@"NSMutableDictionary" _lock_framesDict;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R,N) memoryUsage;
@property (T@"NSArray",R,N) allFrames;
```

## Instance methods

```
-[BLSHFlipbookHistory frameWithUUID:];
-[BLSHFlipbookHistory memoryUsage];
-[BLSHFlipbookHistory initWithFrameLimit:memoryLimit:];
-[BLSHFlipbookHistory addRenderedFrameToHistory:];
-[BLSHFlipbookHistory allFrames];
```
