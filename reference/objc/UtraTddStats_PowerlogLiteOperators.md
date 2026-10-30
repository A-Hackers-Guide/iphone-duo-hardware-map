# `UtraTddStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 18 instance variables, 34 properties, 77 instance methods, 0 class methods

## Instance variables

```
Q _startTime;
I _activeDuration;
I _deepSleepCycleCount;
I _deepSleepDuration;
I _duration;
I _normalSleepDuration;
I _thClkOpt0Duration;
I _thClkOpt1Duration;
I _voltHighDuration;
I _voltLowDuration;
I _voltMedDuration;
I _zspClkOpt0Duration;
I _zspClkOpt1Duration;
I _zspClkOpt2Duration;
I _zspClkOpt3Duration;
I _zspClkOpt4Duration;
I _zspClkOpt5Duration;
{?="startTime"b1"activeDuration"b1"deepSleepCycleCount"b1"deepSleepDuration"b1"duration"b1"normalSleepDuration"b1"thClkOpt0Duration"b1"thClkOpt1Duration"b1"voltHighDuration"b1"voltLowDuration"b1"voltMedDuration"b1"zspClkOpt0Duration"b1"zspClkOpt1Duration"b1"zspClkOpt2Duration"b1"zspClkOpt3Duration"b1"zspClkOpt4Duration"b1"zspClkOpt5Duration"b1} _has;
```

## Properties

```
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasActiveDuration;
@property (TI,N,V_activeDuration) activeDuration;
@property (TB,N) hasNormalSleepDuration;
@property (TI,N,V_normalSleepDuration) normalSleepDuration;
@property (TB,N) hasDeepSleepDuration;
@property (TI,N,V_deepSleepDuration) deepSleepDuration;
@property (TB,N) hasDeepSleepCycleCount;
@property (TI,N,V_deepSleepCycleCount) deepSleepCycleCount;
@property (TB,N) hasVoltLowDuration;
@property (TI,N,V_voltLowDuration) voltLowDuration;
@property (TB,N) hasVoltMedDuration;
@property (TI,N,V_voltMedDuration) voltMedDuration;
@property (TB,N) hasVoltHighDuration;
@property (TI,N,V_voltHighDuration) voltHighDuration;
@property (TB,N) hasZspClkOpt0Duration;
@property (TI,N,V_zspClkOpt0Duration) zspClkOpt0Duration;
@property (TB,N) hasZspClkOpt1Duration;
@property (TI,N,V_zspClkOpt1Duration) zspClkOpt1Duration;
@property (TB,N) hasZspClkOpt2Duration;
@property (TI,N,V_zspClkOpt2Duration) zspClkOpt2Duration;
@property (TB,N) hasZspClkOpt3Duration;
@property (TI,N,V_zspClkOpt3Duration) zspClkOpt3Duration;
@property (TB,N) hasZspClkOpt4Duration;
@property (TI,N,V_zspClkOpt4Duration) zspClkOpt4Duration;
@property (TB,N) hasZspClkOpt5Duration;
@property (TI,N,V_zspClkOpt5Duration) zspClkOpt5Duration;
@property (TB,N) hasThClkOpt0Duration;
@property (TI,N,V_thClkOpt0Duration) thClkOpt0Duration;
@property (TB,N) hasThClkOpt1Duration;
@property (TI,N,V_thClkOpt1Duration) thClkOpt1Duration;
@property (TB,N) hasStartTime;
@property (TQ,N,V_startTime) startTime;
```

## Instance methods

```
-[UtraTddStats setHasStartTime:];
-[UtraTddStats writeTo:];
-[UtraTddStats hasStartTime];
-[UtraTddStats startTime];
-[UtraTddStats mergeFrom:];
-[UtraTddStats hasDuration];
-[UtraTddStats activeDuration];
-[UtraTddStats duration];
-[UtraTddStats setHasDuration:];
-[UtraTddStats setStartTime:];
-[UtraTddStats hash];
-[UtraTddStats copyTo:];
-[UtraTddStats description];
-[UtraTddStats setDuration:];
-[UtraTddStats readFrom:];
-[UtraTddStats copyWithZone:];
-[UtraTddStats isEqual:];
-[UtraTddStats dictionaryRepresentation];
-[UtraTddStats deepSleepDuration];
-[UtraTddStats hasDeepSleepDuration];
-[UtraTddStats setHasDeepSleepDuration:];
-[UtraTddStats setActiveDuration:];
-[UtraTddStats hasActiveDuration];
-[UtraTddStats setHasActiveDuration:];
-[UtraTddStats voltLowDuration];
-[UtraTddStats voltMedDuration];
-[UtraTddStats deepSleepCycleCount];
-[UtraTddStats hasDeepSleepCycleCount];
-[UtraTddStats hasNormalSleepDuration];
-[UtraTddStats hasThClkOpt0Duration];
-[UtraTddStats hasThClkOpt1Duration];
-[UtraTddStats hasVoltHighDuration];
-[UtraTddStats hasVoltLowDuration];
-[UtraTddStats hasVoltMedDuration];
-[UtraTddStats hasZspClkOpt0Duration];
-[UtraTddStats hasZspClkOpt1Duration];
-[UtraTddStats hasZspClkOpt2Duration];
-[UtraTddStats hasZspClkOpt3Duration];
-[UtraTddStats hasZspClkOpt4Duration];
-[UtraTddStats hasZspClkOpt5Duration];
-[UtraTddStats normalSleepDuration];
-[UtraTddStats setDeepSleepCycleCount:];
-[UtraTddStats setDeepSleepDuration:];
-[UtraTddStats setHasDeepSleepCycleCount:];
-[UtraTddStats setHasNormalSleepDuration:];
-[UtraTddStats setHasThClkOpt0Duration:];
-[UtraTddStats setHasThClkOpt1Duration:];
-[UtraTddStats setHasVoltHighDuration:];
-[UtraTddStats setHasVoltLowDuration:];
-[UtraTddStats setHasVoltMedDuration:];
-[UtraTddStats setHasZspClkOpt0Duration:];
-[UtraTddStats setHasZspClkOpt1Duration:];
-[UtraTddStats setHasZspClkOpt2Duration:];
-[UtraTddStats setHasZspClkOpt3Duration:];
-[UtraTddStats setHasZspClkOpt4Duration:];
-[UtraTddStats setHasZspClkOpt5Duration:];
-[UtraTddStats setNormalSleepDuration:];
-[UtraTddStats setThClkOpt0Duration:];
-[UtraTddStats setThClkOpt1Duration:];
-[UtraTddStats setVoltHighDuration:];
-[UtraTddStats setVoltLowDuration:];
-[UtraTddStats setVoltMedDuration:];
-[UtraTddStats setZspClkOpt0Duration:];
-[UtraTddStats setZspClkOpt1Duration:];
-[UtraTddStats setZspClkOpt2Duration:];
-[UtraTddStats setZspClkOpt3Duration:];
-[UtraTddStats setZspClkOpt4Duration:];
-[UtraTddStats setZspClkOpt5Duration:];
-[UtraTddStats thClkOpt0Duration];
-[UtraTddStats thClkOpt1Duration];
-[UtraTddStats voltHighDuration];
-[UtraTddStats zspClkOpt0Duration];
-[UtraTddStats zspClkOpt1Duration];
-[UtraTddStats zspClkOpt2Duration];
-[UtraTddStats zspClkOpt3Duration];
-[UtraTddStats zspClkOpt4Duration];
-[UtraTddStats zspClkOpt5Duration];
```
