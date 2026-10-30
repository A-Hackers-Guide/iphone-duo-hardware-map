# `BLSHFlipbook` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSDisplaySpecifying`, `BSInvalidatable`
- 0 instance variables, 9 properties, 17 instance methods, 0 class methods

## Properties

```
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) frameOnGlass;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) captureFrameOnGlass;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) lastRenderedFrame;
@property (T@"NSArray",R,N) activeFrames;
@property (TQ,R,N) memoryUsage;
@property (TB,N,GisPowerSavingEnabled) powerSavingEnabled;
@property (TB,N,Gis1HzFlipbook,Sset1HzFlipbook:) oneHzFlipbook;
@property (TB,N,GisCompositingWithLowPowerRenderer,SsetCompositingWithLowPowerRenderer:) compositingWithLowPowerRenderer;
@property (TB,N) cachesFramesOnExit;
```

## Instance methods

```
-[BLSHFlipbook is1HzFlipbook];
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
-[BLSHFlipbook isCompositingWithLowPowerRenderer];
-[BLSHFlipbook isPowerSavingEnabled];
-[BLSHFlipbook lastRenderedFrame];
-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:];
-[BLSHFlipbook setCompositingWithLowPowerRenderer:];
```
