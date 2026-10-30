# `AWDMETRICSKCellularPowerLogRatChangeEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _event;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"event"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEvent;
@property (Ti,N,V_event) event;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogRatChangeEvent setEvent:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent hasTimestamp];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setTimestamp:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent writeTo:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent mergeFrom:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent timestamp];
-[AWDMETRICSKCellularPowerLogRatChangeEvent event];
-[AWDMETRICSKCellularPowerLogRatChangeEvent hash];
-[AWDMETRICSKCellularPowerLogRatChangeEvent copyTo:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent description];
-[AWDMETRICSKCellularPowerLogRatChangeEvent readFrom:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent copyWithZone:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent isEqual:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogRatChangeEvent hasEvent];
-[AWDMETRICSKCellularPowerLogRatChangeEvent StringAsEvent:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent eventAsString:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setHasEvent:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent isDataPreferred];
-[AWDMETRICSKCellularPowerLogRatChangeEvent hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogRatChangeEvent hasSubsId];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setHasSubsId:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent setSubsId:];
-[AWDMETRICSKCellularPowerLogRatChangeEvent subsId];
```
