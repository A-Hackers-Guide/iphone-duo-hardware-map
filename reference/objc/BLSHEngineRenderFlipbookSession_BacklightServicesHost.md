# `BLSHEngineRenderFlipbookSession`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 20 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<BLSHFlipbook>" _flipbook;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHPresentationDateSpecifier" _lock_preparingSpecifier;
@"NSMutableSet" _lock_pendingEnvironments;
@"NSMutableArray" _lock_renderedFrames;
@"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>" _lock_timeoutTimer;
@"<BLSHEngineRenderFlipbookSessionDelegate>" _lock_delegate;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHOSDisplayInterfaceProviding>" _display;
Q _stateHandler;
d _sessionStartTime;
d _lock_layoutStartTime;
d _lock_accumulatedLayoutDuration;
d _lock_accumulatedRenderDuration;
i _lock_retryRenderCount;
B _lock_didFailToRender;
B _lock_timedOut;
B _lock_invalidated;
B _lock_didDisableFlipbookPowerSavings;
@"BLSHBacklightEnvironmentPresentation" _presentation;
```

## Properties

```
@property (TQ,R,N) count;
@property (TQ,R,N) memoryUsage;
@property (T@"NSArray",R,N) renderedFrames;
@property (T@"BLSHBacklightEnvironmentPresentation",R,N,V_presentation) presentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHEngineRenderFlipbookSession presentation];
-[BLSHEngineRenderFlipbookSession debugDescription];
-[BLSHEngineRenderFlipbookSession dealloc];
-[BLSHEngineRenderFlipbookSession count];
-[BLSHEngineRenderFlipbookSession invalidate];
-[BLSHEngineRenderFlipbookSession description];
-[BLSHEngineRenderFlipbookSession memoryUsage];
-[BLSHEngineRenderFlipbookSession prepareAndRenderFrameSpecifier:];
-[BLSHEngineRenderFlipbookSession initWithDelegate:flipbook:presentation:osInterfaceProvider:display:];
-[BLSHEngineRenderFlipbookSession renderedFrames];
-[BLSHEngineRenderFlipbookSession telemetryDataWithEndTime:reasonEnded:preventedSleepDuration:];
```
