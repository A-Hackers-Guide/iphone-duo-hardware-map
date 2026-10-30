# `GeraStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _startTime;
I _duration;
I _sleepCycleCount;
I _sleepDuration;
{?="startTime"b1"duration"b1"sleepCycleCount"b1"sleepDuration"b1} _has;
```

## Properties

```
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasSleepDuration;
@property (TI,N,V_sleepDuration) sleepDuration;
@property (TB,N) hasSleepCycleCount;
@property (TI,N,V_sleepCycleCount) sleepCycleCount;
@property (TB,N) hasStartTime;
@property (TQ,N,V_startTime) startTime;
```

## Instance methods

```
-[GeraStats setHasStartTime:];
-[GeraStats writeTo:];
-[GeraStats hasStartTime];
-[GeraStats startTime];
-[GeraStats sleepDuration];
-[GeraStats mergeFrom:];
-[GeraStats hasDuration];
-[GeraStats duration];
-[GeraStats setHasDuration:];
-[GeraStats setStartTime:];
-[GeraStats hash];
-[GeraStats copyTo:];
-[GeraStats description];
-[GeraStats setDuration:];
-[GeraStats readFrom:];
-[GeraStats copyWithZone:];
-[GeraStats isEqual:];
-[GeraStats dictionaryRepresentation];
-[GeraStats hasSleepDuration];
-[GeraStats setHasSleepDuration:];
-[GeraStats sleepCycleCount];
-[GeraStats hasSleepCycleCount];
-[GeraStats setHasSleepCycleCount:];
-[GeraStats setSleepCycleCount:];
-[GeraStats setSleepDuration:];
```
