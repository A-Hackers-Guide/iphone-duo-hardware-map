# `CBLuxRamp`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 18 instance methods, 1 class methods

## Instance variables

```
i _state;
f _targetLux;
@"<CBLuxRampPolicy>" _policy;
@"<CBCurveShape>" _shape;
f _duration;
f _startLux;
f _startTime;
f _targetTime;
f _lux;
```

## Properties

```
@property (Tf,R,V_duration) duration;
@property (Tf,R) targetLux;
@property (Tf,R,V_startLux) startLux;
@property (Tf,R,V_startTime) startTime;
@property (Tf,R,V_targetTime) targetTime;
@property (Tf,R,V_lux) lux;
```

## Class methods

```
+[CBLuxRamp luxRampStateToString:];
```

## Instance methods

```
-[CBLuxRamp startTime];
-[CBLuxRamp dealloc];
-[CBLuxRamp duration];
-[CBLuxRamp targetTime];
-[CBLuxRamp lux];
-[CBLuxRamp cancelRamp];
-[CBLuxRamp forceLux:];
-[CBLuxRamp initWithPolicy:andLuxShape:];
-[CBLuxRamp rampFromLux:toLux:];
-[CBLuxRamp rampFromLux:toLux:forceRamp:];
-[CBLuxRamp rampIsRunning];
-[CBLuxRamp rampTimedFromLux:toLux:atTime:];
-[CBLuxRamp rampTimedFromLux:toLux:atTime:forceRamp:];
-[CBLuxRamp shouldRampFromStartLux:toTargetLux:];
-[CBLuxRamp startLux];
-[CBLuxRamp targetLux];
-[CBLuxRamp updateRampWithProgress:];
-[CBLuxRamp updateTimedRamp:];
```
