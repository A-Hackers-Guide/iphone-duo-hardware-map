# `AWDMETRICSKCellularPlatformApBbSleepStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 33 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
i _lastSdmState;
@"NSMutableArray" _states;
B _isMsim;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"isMsim"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasIsMsim;
@property (TB,N,V_isMsim) isMsim;
@property (T@"NSMutableArray",&,N,V_states) states;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPlatformApBbSleepStats stateType];
```

## Instance methods

```
-[AWDMETRICSKCellularPlatformApBbSleepStats hasTimestamp];
-[AWDMETRICSKCellularPlatformApBbSleepStats setHasTimestamp:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setTimestamp:];
-[AWDMETRICSKCellularPlatformApBbSleepStats writeTo:];
-[AWDMETRICSKCellularPlatformApBbSleepStats addState:];
-[AWDMETRICSKCellularPlatformApBbSleepStats mergeFrom:];
-[AWDMETRICSKCellularPlatformApBbSleepStats timestamp];
-[AWDMETRICSKCellularPlatformApBbSleepStats hash];
-[AWDMETRICSKCellularPlatformApBbSleepStats copyTo:];
-[AWDMETRICSKCellularPlatformApBbSleepStats description];
-[AWDMETRICSKCellularPlatformApBbSleepStats readFrom:];
-[AWDMETRICSKCellularPlatformApBbSleepStats copyWithZone:];
-[AWDMETRICSKCellularPlatformApBbSleepStats isEqual:];
-[AWDMETRICSKCellularPlatformApBbSleepStats states];
-[AWDMETRICSKCellularPlatformApBbSleepStats dictionaryRepresentation];
-[AWDMETRICSKCellularPlatformApBbSleepStats setStates:];
-[AWDMETRICSKCellularPlatformApBbSleepStats durationMs];
-[AWDMETRICSKCellularPlatformApBbSleepStats hasDurationMs];
-[AWDMETRICSKCellularPlatformApBbSleepStats setDurationMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setHasDurationMs:];
-[AWDMETRICSKCellularPlatformApBbSleepStats stateAtIndex:];
-[AWDMETRICSKCellularPlatformApBbSleepStats statesCount];
-[AWDMETRICSKCellularPlatformApBbSleepStats StringAsLastSdmState:];
-[AWDMETRICSKCellularPlatformApBbSleepStats hasLastSdmState];
-[AWDMETRICSKCellularPlatformApBbSleepStats clearStates];
-[AWDMETRICSKCellularPlatformApBbSleepStats hasIsMsim];
-[AWDMETRICSKCellularPlatformApBbSleepStats isMsim];
-[AWDMETRICSKCellularPlatformApBbSleepStats lastSdmState];
-[AWDMETRICSKCellularPlatformApBbSleepStats lastSdmStateAsString:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setHasIsMsim:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setHasLastSdmState:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setIsMsim:];
-[AWDMETRICSKCellularPlatformApBbSleepStats setLastSdmState:];
```
