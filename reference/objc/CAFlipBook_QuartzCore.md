# `CAFlipBook`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 10 properties, 38 instance methods, 0 class methods

## Instance variables

```
I _serverPort;
Q _maximumSize;
I _contextId;
I _displayId;
Q _lastFrameId;
I _generation;
B _inverted;
B _powerSavingEnabled;
B _oneHzFlipBook;
B _cachesFramesOnExit;
Q _maximumPoolMemory;
f _overAllocationFactor;
Q _maximumMemoryUsageForDiagnostics;
{SpinLock="_l"{?="x"i}} _framesLock;
@"NSMutableArray" _frames;
Q _cancelTimestamp;
Q _renderTimestamp;
{SpinLock="_l"{?="x"i}} _onRenderCBLock;
@ _onRenderInfo;
@? _onRenderBegunCB;
@? _onRenderCompletedCB;
{ClientIPC="_port"I"_queue"@"NSObject<OS_dispatch_queue>""_source"@"NSObject<OS_dispatch_source>"} _onRenderBeginClientIpc;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _renderInProgress;
B _wantsTransform;
B _lowPowerRendering;
```

## Properties

```
@property (TI,N,V_contextId) contextId;
@property (TB,N,V_wantsTransform) wantsTransform;
@property (TB,N,GisInverted,V_inverted) inverted;
@property (TQ,N,V_maximumMemoryUsageForDiagnostics) maximumMemoryUsageForDiagnostics;
@property (TB,N,V_powerSavingEnabled) powerSavingEnabled;
@property (TB,N,GisOneHzFlipBook,V_oneHzFlipBook) oneHzFlipBook;
@property (TB,N,V_cachesFramesOnExit) cachesFramesOnExit;
@property (TQ,N,V_maximumPoolMemory) maximumPoolMemory;
@property (Tf,N,V_overAllocationFactor) overAllocationFactor;
@property (TB,N,GisLowPowerRendering,V_lowPowerRendering) lowPowerRendering;
```

## Instance methods

```
-[CAFlipBook isInverted];
-[CAFlipBook contextId];
-[CAFlipBook setContextId:];
-[CAFlipBook dealloc];
-[CAFlipBook isLowPowerRendering];
-[CAFlipBook purge];
-[CAFlipBook description];
-[CAFlipBook cancelWithError:];
-[CAFlipBook cancel];
-[CAFlipBook setInverted:];
-[CAFlipBook collect];
-[CAFlipBook isOneHzFlipBook];
-[CAFlipBook _collectFlipBookFrames];
-[CAFlipBook _frameById:];
-[CAFlipBook _initWithDisplayId:options:];
-[CAFlipBook _notifyRenderBegin];
-[CAFlipBook _notifyRenderCompletedForTime:status:frameId:oldestFrameId:apl:aplDimming:memoryUsage:rawSurfacePort:rawSurfaceDestRect:];
-[CAFlipBook activeFrames];
-[CAFlipBook cachesFramesOnExit];
-[CAFlipBook copyCurrentFrame];
-[CAFlipBook frameAtTime:];
-[CAFlipBook maximumMemoryUsageForDiagnostics];
-[CAFlipBook maximumPoolMemory];
-[CAFlipBook memoryUsage];
-[CAFlipBook overAllocationFactor];
-[CAFlipBook powerSavingEnabled];
-[CAFlipBook purgePool];
-[CAFlipBook renderForTime:options:userInfo:error:];
-[CAFlipBook renderForTime:options:userInfo:onRenderBegin:onRenderComplete:];
-[CAFlipBook setCachesFramesOnExit:];
-[CAFlipBook setLowPowerRendering:];
-[CAFlipBook setMaximumMemoryUsageForDiagnostics:];
-[CAFlipBook setMaximumPoolMemory:];
-[CAFlipBook setOneHzFlipBook:];
-[CAFlipBook setOverAllocationFactor:];
-[CAFlipBook setPowerSavingEnabled:];
-[CAFlipBook setWantsTransform:];
-[CAFlipBook wantsTransform];
```
