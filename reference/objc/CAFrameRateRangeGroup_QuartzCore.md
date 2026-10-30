# `CAFrameRateRangeGroup`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 12 instance methods, 0 class methods

## Instance variables

```
^v _impl;
I _current_reason_count;
[8I] _reasons;
```

## Properties

```
@property (T{CAFrameRateRange=fff},R,N) arbitratedRange;
```

## Instance methods

```
-[CAFrameRateRangeGroup initWithDisplay:];
-[CAFrameRateRangeGroup dealloc];
-[CAFrameRateRangeGroup arbitratedRange];
-[CAFrameRateRangeGroup addCompatQuantaIntent];
-[CAFrameRateRangeGroup addFrameRateRange:];
-[CAFrameRateRangeGroup addReason:];
-[CAFrameRateRangeGroup arbitratedIntervalRange];
-[CAFrameRateRangeGroup hasCompatQuantaIntent];
-[CAFrameRateRangeGroup initWithDisplayId:heartbeatRate:minimumFrameDuration:supportsVRR:compatQuantaMode:serverCompatQuantaMode:];
-[CAFrameRateRangeGroup reasonsWithCount:];
-[CAFrameRateRangeGroup removeFrameRateRange:];
-[CAFrameRateRangeGroup updateFrameRateRange:toRange:];
```
