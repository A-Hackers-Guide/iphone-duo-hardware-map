# `BLSHFlipbook`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHFlipbook`
- 11 instance variables, 15 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"BLSHOSDisplayInterface" _display;
@"BSAbsoluteMachTimer" _hangDetectorTimer;
@"NSObject<OS_dispatch_workloop>" _hangDetectorWorkloop;
@"NSObject<OS_dispatch_queue>" _hangDetectorQueue;
Q _hangDetectorStartTimestamp;
B _hangResolved;
@"CAFlipBook" _flipbook;
B _wantsTransform;
B _inverted;
@"NSMutableDictionary" _dateToMachTimeCache;
B _hangDetected;
```

## Properties

```
@property (TB,V_hangDetected) hangDetected;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) frameOnGlass;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) captureFrameOnGlass;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) lastRenderedFrame;
@property (T@"NSArray",R,N) activeFrames;
@property (TQ,R,N) memoryUsage;
@property (TB,N,GisPowerSavingEnabled) powerSavingEnabled;
@property (TB,N,Gis1HzFlipbook,Sset1HzFlipbook:) oneHzFlipbook;
@property (TB,N,GisCompositingWithLowPowerRenderer,SsetCompositingWithLowPowerRenderer:) compositingWithLowPowerRenderer;
@property (TB,N) cachesFramesOnExit;
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHFlipbook createForDisplay:platformProvider:];
```

## Instance methods

```
-[BLSHFlipbook display];
-[BLSHFlipbook is1HzFlipbook];
-[BLSHFlipbook dealloc];
-[BLSHFlipbook invalidate];
-[BLSHFlipbook purge];
-[BLSHFlipbook collect];
-[BLSHFlipbook activeFrames];
-[BLSHFlipbook cachesFramesOnExit];
-[BLSHFlipbook memoryUsage];
-[BLSHFlipbook setCachesFramesOnExit:];
-[BLSHFlipbook setPowerSavingEnabled:];
-[BLSHFlipbook set1HzFlipbook:];
-[BLSHFlipbook cancelAllFramesWithError:];
-[BLSHFlipbook captureFrameOnGlass];
-[BLSHFlipbook frameOnGlass];
-[BLSHFlipbook hangDetected];
-[BLSHFlipbook initForDisplay:platformProvider:];
-[BLSHFlipbook isCompositingWithLowPowerRenderer];
-[BLSHFlipbook isPowerSavingEnabled];
-[BLSHFlipbook lastRenderedFrame];
-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:];
-[BLSHFlipbook setCompositingWithLowPowerRenderer:];
-[BLSHFlipbook setHangDetected:];
```
