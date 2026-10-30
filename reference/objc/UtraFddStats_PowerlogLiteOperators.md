# `UtraFddStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 14 instance variables, 26 properties, 61 instance methods, 0 class methods

## Instance variables

```
Q _startTime;
I _activeDuration;
I _clkHighDuration;
I _clkLowDuration;
I _clkMedDuration;
I _deepSleepCycleCount;
I _deepSleepDuration;
I _duration;
I _lightSleepCycleCount;
I _lightSleepDuration;
I _voltHighDuration;
I _voltLowDuration;
I _voltMedDuration;
{?="startTime"b1"activeDuration"b1"clkHighDuration"b1"clkLowDuration"b1"clkMedDuration"b1"deepSleepCycleCount"b1"deepSleepDuration"b1"duration"b1"lightSleepCycleCount"b1"lightSleepDuration"b1"voltHighDuration"b1"voltLowDuration"b1"voltMedDuration"b1} _has;
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
@property (TB,N) hasClkLowDuration;
@property (TI,N,V_clkLowDuration) clkLowDuration;
@property (TB,N) hasClkMedDuration;
@property (TI,N,V_clkMedDuration) clkMedDuration;
@property (TB,N) hasClkHighDuration;
@property (TI,N,V_clkHighDuration) clkHighDuration;
@property (TB,N) hasStartTime;
@property (TQ,N,V_startTime) startTime;
```

## Instance methods

```
-[UtraFddStats setHasStartTime:];
-[UtraFddStats writeTo:];
-[UtraFddStats hasStartTime];
-[UtraFddStats startTime];
-[UtraFddStats mergeFrom:];
-[UtraFddStats hasDuration];
-[UtraFddStats activeDuration];
-[UtraFddStats duration];
-[UtraFddStats setHasDuration:];
-[UtraFddStats setStartTime:];
-[UtraFddStats hash];
-[UtraFddStats copyTo:];
-[UtraFddStats description];
-[UtraFddStats setDuration:];
-[UtraFddStats readFrom:];
-[UtraFddStats copyWithZone:];
-[UtraFddStats isEqual:];
-[UtraFddStats dictionaryRepresentation];
-[UtraFddStats deepSleepDuration];
-[UtraFddStats hasDeepSleepDuration];
-[UtraFddStats setHasDeepSleepDuration:];
-[UtraFddStats setActiveDuration:];
-[UtraFddStats hasActiveDuration];
-[UtraFddStats setHasActiveDuration:];
-[UtraFddStats voltLowDuration];
-[UtraFddStats clkHighDuration];
-[UtraFddStats voltMedDuration];
-[UtraFddStats clkLowDuration];
-[UtraFddStats clkMedDuration];
-[UtraFddStats deepSleepCycleCount];
-[UtraFddStats hasClkHighDuration];
-[UtraFddStats hasClkLowDuration];
-[UtraFddStats hasClkMedDuration];
-[UtraFddStats hasDeepSleepCycleCount];
-[UtraFddStats hasLightSleepCycleCount];
-[UtraFddStats hasLightSleepDuration];
-[UtraFddStats hasVoltHighDuration];
-[UtraFddStats hasVoltLowDuration];
-[UtraFddStats hasVoltMedDuration];
-[UtraFddStats lightSleepCycleCount];
-[UtraFddStats lightSleepDuration];
-[UtraFddStats setClkHighDuration:];
-[UtraFddStats setClkLowDuration:];
-[UtraFddStats setClkMedDuration:];
-[UtraFddStats setDeepSleepCycleCount:];
-[UtraFddStats setDeepSleepDuration:];
-[UtraFddStats setHasClkHighDuration:];
-[UtraFddStats setHasClkLowDuration:];
-[UtraFddStats setHasClkMedDuration:];
-[UtraFddStats setHasDeepSleepCycleCount:];
-[UtraFddStats setHasLightSleepCycleCount:];
-[UtraFddStats setHasLightSleepDuration:];
-[UtraFddStats setHasVoltHighDuration:];
-[UtraFddStats setHasVoltLowDuration:];
-[UtraFddStats setHasVoltMedDuration:];
-[UtraFddStats setLightSleepCycleCount:];
-[UtraFddStats setLightSleepDuration:];
-[UtraFddStats setVoltHighDuration:];
-[UtraFddStats setVoltLowDuration:];
-[UtraFddStats setVoltMedDuration:];
-[UtraFddStats voltHighDuration];
```
