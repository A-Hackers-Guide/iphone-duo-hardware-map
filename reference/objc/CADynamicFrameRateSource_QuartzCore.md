# `CADynamicFrameRateSource`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
^{DynamicFrameRateSource=I^v{CAFrameRateRange=fff}{CAFrameIntervalRange=III}QiQQ[4I]b1b1^{DynamicFrameRateSource}b1} _impl;
```

## Properties

```
@property (T{CAFrameRateRange=fff},N) preferredFrameRateRange;
@property (TB,N,GisPaused) paused;
```

## Instance methods

```
-[CADynamicFrameRateSource initWithDisplay:];
-[CADynamicFrameRateSource isPaused];
-[CADynamicFrameRateSource setPreferredFrameRateRange:];
-[CADynamicFrameRateSource dealloc];
-[CADynamicFrameRateSource preferredFrameRateRange];
-[CADynamicFrameRateSource setPaused:];
-[CADynamicFrameRateSource setHighFrameRateReasons:count:];
-[CADynamicFrameRateSource commitDeadline];
-[CADynamicFrameRateSource commitDeadlineAfterTimestamp:];
-[CADynamicFrameRateSource shiftFramePhaseBy:];
```
