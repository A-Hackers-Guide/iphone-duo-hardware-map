# `BWIrisDiscontinuity`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _discontinuityTime;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
@"NSArray" _timeSkews;
@"NSArray" _recipe;
q _recipeMinDisplacement;
q _recipeMaxDisplacement;
i _recipeIdentifier;
{?="value"q"timescale"i"flags"I"epoch"q} _targetFrameDuration;
B _onlyRetime;
B _haveSeenNonPositiveDisplacement;
B _generateIFrames;
B _minDisplacementIFrameRequested;
```

## Properties

```
@property (T{?=qiIq},R) time;
@property (T{?=qiIq},R) targetFrameDuration;
```

## Instance methods

```
-[BWIrisDiscontinuity dealloc];
-[BWIrisDiscontinuity targetFrameDuration];
-[BWIrisDiscontinuity time];
-[BWIrisDiscontinuity containsVideoBufferTime:];
-[BWIrisDiscontinuity initWithTime:duration:targetFrameDuration:onlyRetime:generateIFrames:timeSkews:];
-[BWIrisDiscontinuity resetWithNewTimeSkews:];
-[BWIrisDiscontinuity shouldKeepBufferWithTime:forceKeepingBuffer:nextAdjustedTimeInOut:discontinuityFrameAttributesOut:];
```
