# `AWDMETRICSCellularPowerLogNRNSAENDCEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _event;
i _fr;
I _subsId;
{?="timestamp"b1"event"b1"fr"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEvent;
@property (Ti,N,V_event) event;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setEvent:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent hasTimestamp];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setHasTimestamp:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setTimestamp:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent writeTo:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent mergeFrom:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent timestamp];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent event];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent hash];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent copyTo:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent description];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent readFrom:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent copyWithZone:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent isEqual:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent hasEvent];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent StringAsEvent:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent eventAsString:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setHasEvent:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent StringAsFr:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent fr];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent frAsString:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent hasFr];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent hasSubsId];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setFr:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setHasFr:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setHasSubsId:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent setSubsId:];
-[AWDMETRICSCellularPowerLogNRNSAENDCEvent subsId];
```
