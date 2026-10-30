# `FigIrisAutoTrimmerMotionSample`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 17 instance methods, 1 class methods

## Instance variables

```
i _vitalityObjectCount;
d _timestamp;
d _deltaPeriod;
@"NSDictionary" _inferences;
@"NSMutableDictionary" _intermediateCalculations;
{?="x"f"y"f"z"f} _gravity;
{?="value"q"timescale"i"flags"I"epoch"q} _originatingFrameTime;
{?="w"d"x"d"y"d"z"d} _attitude;
{?="w"d"x"d"y"d"z"d} _delta;
{?="w"d"x"d"y"d"z"d} _accel;
```

## Properties

```
@property (T{?=qiIq},R,N,V_originatingFrameTime) originatingFrameTime;
@property (Td,R,N,V_timestamp) timestamp;
@property (T{?=qiIq},R,N) cmTimestamp;
@property (Td,R,N,V_deltaPeriod) deltaPeriod;
@property (T{?=dddd},R,N,V_attitude) attitude;
@property (T{?=dddd},R,N,V_delta) delta;
@property (T{?=dddd},R,N,V_accel) accel;
@property (T{?=fff},R,N,V_gravity) gravity;
@property (T@"NSDictionary",&,N,V_inferences) inferences;
@property (Ti,N,V_vitalityObjectCount) vitalityObjectCount;
@property (T@"NSMutableDictionary",R,N,V_intermediateCalculations) intermediateCalculations;
```

## Class methods

```
+[FigIrisAutoTrimmerMotionSample initialize];
```

## Instance methods

```
-[FigIrisAutoTrimmerMotionSample dealloc];
-[FigIrisAutoTrimmerMotionSample timestamp];
-[FigIrisAutoTrimmerMotionSample gravity];
-[FigIrisAutoTrimmerMotionSample attitude];
-[FigIrisAutoTrimmerMotionSample delta];
-[FigIrisAutoTrimmerMotionSample accel];
-[FigIrisAutoTrimmerMotionSample attitudeRelativeTo:];
-[FigIrisAutoTrimmerMotionSample cmTimestamp];
-[FigIrisAutoTrimmerMotionSample deltaPeriod];
-[FigIrisAutoTrimmerMotionSample inferences];
-[FigIrisAutoTrimmerMotionSample initWithAttitude:gravity:motionTimestamp:frameTimestamp:previousSample:];
-[FigIrisAutoTrimmerMotionSample intermediateCalculations];
-[FigIrisAutoTrimmerMotionSample originatingFrameTime];
-[FigIrisAutoTrimmerMotionSample prepareIntermediates:];
-[FigIrisAutoTrimmerMotionSample setInferences:];
-[FigIrisAutoTrimmerMotionSample setVitalityObjectCount:];
-[FigIrisAutoTrimmerMotionSample vitalityObjectCount];
```
