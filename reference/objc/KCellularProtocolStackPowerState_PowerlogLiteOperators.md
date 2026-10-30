# `KCellularProtocolStackPowerState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _prevState;
I _prevStateDurMs;
I _state;
I _subsId;
{?="timestamp"b1"prevState"b1"prevStateDurMs"b1"state"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasState;
@property (TI,N,V_state) state;
@property (TB,N) hasPrevState;
@property (TI,N,V_prevState) prevState;
@property (TB,N) hasPrevStateDurMs;
@property (TI,N,V_prevStateDurMs) prevStateDurMs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularProtocolStackPowerState hasTimestamp];
-[KCellularProtocolStackPowerState setHasTimestamp:];
-[KCellularProtocolStackPowerState setTimestamp:];
-[KCellularProtocolStackPowerState writeTo:];
-[KCellularProtocolStackPowerState setState:];
-[KCellularProtocolStackPowerState mergeFrom:];
-[KCellularProtocolStackPowerState timestamp];
-[KCellularProtocolStackPowerState hasState];
-[KCellularProtocolStackPowerState hash];
-[KCellularProtocolStackPowerState copyTo:];
-[KCellularProtocolStackPowerState description];
-[KCellularProtocolStackPowerState readFrom:];
-[KCellularProtocolStackPowerState copyWithZone:];
-[KCellularProtocolStackPowerState setHasState:];
-[KCellularProtocolStackPowerState isEqual:];
-[KCellularProtocolStackPowerState state];
-[KCellularProtocolStackPowerState dictionaryRepresentation];
-[KCellularProtocolStackPowerState hasPrevState];
-[KCellularProtocolStackPowerState hasPrevStateDurMs];
-[KCellularProtocolStackPowerState hasSubsId];
-[KCellularProtocolStackPowerState prevState];
-[KCellularProtocolStackPowerState prevStateDurMs];
-[KCellularProtocolStackPowerState setHasPrevState:];
-[KCellularProtocolStackPowerState setHasPrevStateDurMs:];
-[KCellularProtocolStackPowerState setHasSubsId:];
-[KCellularProtocolStackPowerState setPrevState:];
-[KCellularProtocolStackPowerState setPrevStateDurMs:];
-[KCellularProtocolStackPowerState setSubsId:];
-[KCellularProtocolStackPowerState subsId];
```
