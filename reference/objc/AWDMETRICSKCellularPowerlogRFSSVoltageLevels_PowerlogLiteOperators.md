# `AWDMETRICSKCellularPowerlogRFSSVoltageLevels`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
@"NSMutableArray" _rfssStates;
{?="timestamp"b1"durationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_rfssStates) rfssStates;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
```

## Class methods

```
+[AWDMETRICSKCellularPowerlogRFSSVoltageLevels rfssStateType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels hasTimestamp];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels setHasTimestamp:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels setTimestamp:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels writeTo:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels mergeFrom:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels timestamp];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels hash];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels copyTo:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels description];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels readFrom:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels copyWithZone:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels isEqual:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels dictionaryRepresentation];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels durationMs];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels hasDurationMs];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels setDurationMs:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels setHasDurationMs:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels clearRfssStates];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels rfssStatesCount];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels addRfssState:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels rfssStateAtIndex:];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels rfssStates];
-[AWDMETRICSKCellularPowerlogRFSSVoltageLevels setRfssStates:];
```
