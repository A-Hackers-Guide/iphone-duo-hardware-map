# `SBAlwaysOnTelemetryMetrics`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _stopWatches;
@"NSMutableDictionary" _stateChangeCounts;
@"_SBMachContinuousStopwatch" _activeStopWatch;
@"NSMutableSet" _presentationSources;
Q _invalidatedFramesUpTo2mStale;
Q _invalidatedFramesUpTo3mStale;
Q _invalidatedFramesUpTo4mStale;
Q _invalidatedFramesUpTo5mStale;
Q _invalidatedFramesUpTo6mStale;
Q _discardedFramesUpTo2mStale;
Q _discardedFramesUpTo3mStale;
Q _discardedFramesUpTo4mStale;
Q _discardedFramesUpTo5mStale;
Q _discardedFramesUpTo6mStale;
Q _renderedFramesLessThan1Min;
Q _renderedFrames1to2Min;
Q _renderedFrames2to3Min;
Q _renderedFrames3to4Min;
Q _renderedFrames4to5Min;
Q _renderedFrames5to6Min;
Q _renderedFramesMoreThan6Min;
Q _renderedFrameCount;
Q _renderedPartialMinuteCount;
@"NSNumber" _minimumAPL;
@"NSNumber" _maximumAPL;
@"NSNumber" _averageAPL;
@"NSNumber" _minimumAPLDimming;
@"NSNumber" _maximumAPLDimming;
@"NSNumber" _averageAPLDimming;
```

## Instance methods

```
-[SBAlwaysOnTelemetryMetrics setBacklightState:];
-[SBAlwaysOnTelemetryMetrics init];
-[SBAlwaysOnTelemetryMetrics accumulateDiscardHistogram:];
-[SBAlwaysOnTelemetryMetrics accumulateInvalidationHistogram:];
-[SBAlwaysOnTelemetryMetrics accumulatePresentationSources:];
-[SBAlwaysOnTelemetryMetrics accumulateRenderHistogram:];
-[SBAlwaysOnTelemetryMetrics iOSSpecificFields];
```
