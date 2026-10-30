# `AWDMETRICSKCellularPowerLogServiceStatusEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _rat;
i _status;
I _subsId;
{?="timestamp"b1"rat"b1"status"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasStatus;
@property (Ti,N,V_status) status;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogServiceStatusEvent hasTimestamp];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setTimestamp:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent statusAsString:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent writeTo:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent StringAsStatus:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent mergeFrom:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent timestamp];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent status];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setHasStatus:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent rat];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent hasStatus];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent hash];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent copyTo:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent description];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent readFrom:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setStatus:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent copyWithZone:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent isEqual:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setRat:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent hasRat];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setHasRat:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent StringAsRat:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent hasSubsId];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent ratAsString:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setHasSubsId:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent setSubsId:];
-[AWDMETRICSKCellularPowerLogServiceStatusEvent subsId];
```
