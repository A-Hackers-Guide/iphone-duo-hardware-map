# `EutraStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 11 instance variables, 20 properties, 49 instance methods, 0 class methods

## Instance variables

```
Q _startTime;
I _activeDuration;
I _deepSleepCycleCount;
I _deepSleepDuration;
I _duration;
I _lightSleepCycleCount;
I _lightSleepDuration;
I _voltHighDuration;
I _voltLowDuration;
I _voltMedDuration;
{?="startTime"b1"activeDuration"b1"deepSleepCycleCount"b1"deepSleepDuration"b1"duration"b1"lightSleepCycleCount"b1"lightSleepDuration"b1"voltHighDuration"b1"voltLowDuration"b1"voltMedDuration"b1} _has;
```

## Properties

```
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasActiveDuration;
@property (TI,N,V_activeDuration) activeDuration;
@property (TB,N) hasLightSleepDuration;
@property (TI,N,V_lightSleepDuration) lightSleepDuration;
@property (TB,N) hasDeepSleepDuration;
@property (TI,N,V_deepSleepDuration) deepSleepDuration;
@property (TB,N) hasLightSleepCycleCount;
@property (TI,N,V_lightSleepCycleCount) lightSleepCycleCount;
@property (TB,N) hasDeepSleepCycleCount;
@property (TI,N,V_deepSleepCycleCount) deepSleepCycleCount;
@property (TB,N) hasVoltLowDuration;
@property (TI,N,V_voltLowDuration) voltLowDuration;
@property (TB,N) hasVoltMedDuration;
@property (TI,N,V_voltMedDuration) voltMedDuration;
@property (TB,N) hasVoltHighDuration;
@property (TI,N,V_voltHighDuration) voltHighDuration;
@property (TB,N) hasStartTime;
@property (TQ,N,V_startTime) startTime;
```

## Instance methods

```
-[EutraStats setHasStartTime:];
-[EutraStats writeTo:];
-[EutraStats hasStartTime];
-[EutraStats startTime];
-[EutraStats mergeFrom:];
-[EutraStats hasDuration];
-[EutraStats activeDuration];
-[EutraStats duration];
-[EutraStats setHasDuration:];
-[EutraStats setStartTime:];
-[EutraStats hash];
-[EutraStats copyTo:];
-[EutraStats description];
-[EutraStats setDuration:];
-[EutraStats readFrom:];
-[EutraStats copyWithZone:];
-[EutraStats isEqual:];
-[EutraStats dictionaryRepresentation];
-[EutraStats deepSleepDuration];
-[EutraStats hasDeepSleepDuration];
-[EutraStats setHasDeepSleepDuration:];
-[EutraStats setActiveDuration:];
-[EutraStats hasActiveDuration];
-[EutraStats setHasActiveDuration:];
-[EutraStats voltLowDuration];
-[EutraStats voltMedDuration];
-[EutraStats deepSleepCycleCount];
-[EutraStats hasDeepSleepCycleCount];
-[EutraStats hasLightSleepCycleCount];
-[EutraStats hasLightSleepDuration];
-[EutraStats hasVoltHighDuration];
-[EutraStats hasVoltLowDuration];
-[EutraStats hasVoltMedDuration];
-[EutraStats lightSleepCycleCount];
-[EutraStats lightSleepDuration];
-[EutraStats setDeepSleepCycleCount:];
-[EutraStats setDeepSleepDuration:];
-[EutraStats setHasDeepSleepCycleCount:];
-[EutraStats setHasLightSleepCycleCount:];
-[EutraStats setHasLightSleepDuration:];
-[EutraStats setHasVoltHighDuration:];
-[EutraStats setHasVoltLowDuration:];
-[EutraStats setHasVoltMedDuration:];
-[EutraStats setLightSleepCycleCount:];
-[EutraStats setLightSleepDuration:];
-[EutraStats setVoltHighDuration:];
-[EutraStats setVoltLowDuration:];
-[EutraStats setVoltMedDuration:];
-[EutraStats voltHighDuration];
```
