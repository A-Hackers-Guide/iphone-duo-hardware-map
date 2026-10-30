# `BLSHPseudoFlipbook`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHFlipbook`
- 7 instance variables, 14 properties, 20 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _lock_activeFrames;
Q _lock_nextframeID;
B _lock_powerSavingEnabled;
B _lock_1HzFlipbook;
B _lock_compositingWithLowPowerRenderer;
B _lock_cachesFramesOnExit;
```

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
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHPseudoFlipbook display];
-[BLSHPseudoFlipbook init];
-[BLSHPseudoFlipbook is1HzFlipbook];
-[BLSHPseudoFlipbook invalidate];
-[BLSHPseudoFlipbook purge];
-[BLSHPseudoFlipbook collect];
-[BLSHPseudoFlipbook activeFrames];
-[BLSHPseudoFlipbook cachesFramesOnExit];
-[BLSHPseudoFlipbook memoryUsage];
-[BLSHPseudoFlipbook setCachesFramesOnExit:];
-[BLSHPseudoFlipbook setPowerSavingEnabled:];
-[BLSHPseudoFlipbook set1HzFlipbook:];
-[BLSHPseudoFlipbook cancelAllFramesWithError:];
-[BLSHPseudoFlipbook captureFrameOnGlass];
-[BLSHPseudoFlipbook frameOnGlass];
-[BLSHPseudoFlipbook isCompositingWithLowPowerRenderer];
-[BLSHPseudoFlipbook isPowerSavingEnabled];
-[BLSHPseudoFlipbook lastRenderedFrame];
-[BLSHPseudoFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:];
-[BLSHPseudoFlipbook setCompositingWithLowPowerRenderer:];
```
