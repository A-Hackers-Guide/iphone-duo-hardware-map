# `CBFrameStats`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"CBFrameInfoProvider" _frameInfoProvider;
@"NSArray" _rtplcFrameDelayedNitsTable;
@"NSArray" _rtplcFrameDelayedAPCETable;
@"NSArray" _rtplcNitsTable;
@"NSArray" _rtplcAPCETable;
@"NSArray" _rtplcNitsTableRef;
@"NSArray" _rtplcAPCETableRef;
{PeakAPCE="current"f"windowStart"f"recoveryTimer"@"NSObject<OS_dispatch_source>"} _peakAPCE;
{RTPLCCap="previouslyApplied"B"count"f"triggerCount"f} _rtplcCap;
^v _frameSamples;
f _previousFramePresentationTime;
B _frameInfoLoggingEnabled;
B _isMonitoring;
B _referenceModeState;
f _scaleFactor;
f _movingAverageDuration;
{RTPLCTrip="length"Q"startTime"f"maxAPCE"f} _currentTrip;
```

## Properties

```
@property (Tf,R,V_scaleFactor) scaleFactor;
@property (Tf,R,V_movingAverageDuration) movingAverageDuration;
@property (T{RTPLCTrip=Qff},R,V_currentTrip) currentTrip;
@property (TB,N,V_referenceModeState) referenceModeState;
```

## Instance methods

```
-[CBFrameStats dealloc];
-[CBFrameStats stopMonitoring];
-[CBFrameStats scaleFactor];
-[CBFrameStats startMonitoring:];
-[CBFrameStats addFrameInfo:];
-[CBFrameStats currentTrip];
-[CBFrameStats enableFrameInfoLogging:];
-[CBFrameStats getMovingAverage];
-[CBFrameStats getMovingAverageForWindowStart:andWindowEnd:];
-[CBFrameStats getNitsCapForAPCE:tableDelta:];
-[CBFrameStats getPeakAPCE];
-[CBFrameStats getReferenceModeState];
-[CBFrameStats initWithQueue:frameInfoProvider:rtplcCapabilities:movingAverageDuration:];
-[CBFrameStats movingAverageDuration];
-[CBFrameStats processFrameInfo:];
-[CBFrameStats referenceModeState];
-[CBFrameStats setPreviousFramePresentationTime:];
-[CBFrameStats setReferenceModeState:];
-[CBFrameStats updatePeakAPCEForFrameInfo:];
-[CBFrameStats updatePeakAPCEForFrameInfo:atCurrentTime:];
-[CBFrameStats updateRTPLCCapForFrameInfo:previousPresentationTime:];
-[CBFrameStats updateRTPLCTripForFrameInfo:];
```
