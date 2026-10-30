# `AWDMETRICSCellularPowerLogRATChangeEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _event;
I _subsId;
{?="timestamp"b1"event"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEvent;
@property (Ti,N,V_event) event;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogRATChangeEvent setEvent:];
-[AWDMETRICSCellularPowerLogRATChangeEvent hasTimestamp];
-[AWDMETRICSCellularPowerLogRATChangeEvent setHasTimestamp:];
-[AWDMETRICSCellularPowerLogRATChangeEvent setTimestamp:];
-[AWDMETRICSCellularPowerLogRATChangeEvent writeTo:];
-[AWDMETRICSCellularPowerLogRATChangeEvent mergeFrom:];
-[AWDMETRICSCellularPowerLogRATChangeEvent timestamp];
-[AWDMETRICSCellularPowerLogRATChangeEvent event];
-[AWDMETRICSCellularPowerLogRATChangeEvent hash];
-[AWDMETRICSCellularPowerLogRATChangeEvent copyTo:];
-[AWDMETRICSCellularPowerLogRATChangeEvent description];
-[AWDMETRICSCellularPowerLogRATChangeEvent readFrom:];
-[AWDMETRICSCellularPowerLogRATChangeEvent copyWithZone:];
-[AWDMETRICSCellularPowerLogRATChangeEvent isEqual:];
-[AWDMETRICSCellularPowerLogRATChangeEvent dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogRATChangeEvent hasEvent];
-[AWDMETRICSCellularPowerLogRATChangeEvent StringAsEvent:];
-[AWDMETRICSCellularPowerLogRATChangeEvent eventAsString:];
-[AWDMETRICSCellularPowerLogRATChangeEvent setHasEvent:];
-[AWDMETRICSCellularPowerLogRATChangeEvent hasSubsId];
-[AWDMETRICSCellularPowerLogRATChangeEvent setHasSubsId:];
-[AWDMETRICSCellularPowerLogRATChangeEvent setSubsId:];
-[AWDMETRICSCellularPowerLogRATChangeEvent subsId];
```
