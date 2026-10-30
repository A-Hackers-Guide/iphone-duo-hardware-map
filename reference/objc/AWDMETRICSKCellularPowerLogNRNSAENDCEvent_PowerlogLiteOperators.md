# `AWDMETRICSKCellularPowerLogNRNSAENDCEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 40 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _event;
i _fr;
I _numSubs;
@"NSData" _plmn;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"event"b1"fr"b1"numSubs"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasEvent;
@property (Ti,N,V_event) event;
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,R,N) hasPlmn;
@property (T@"NSData",&,N,V_plmn) plmn;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setEvent:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent writeTo:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent timestamp];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent event];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setPlmn:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hash];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent copyTo:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent description];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent readFrom:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent isEqual:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent plmn];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasEvent];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent StringAsEvent:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent eventAsString:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasEvent:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent StringAsFr:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasPlmn];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent numSubs];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent fr];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent frAsString:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasFr];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasNumSubs];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent hasSubsId];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setFr:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasFr:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setNumSubs:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent setSubsId:];
-[AWDMETRICSKCellularPowerLogNRNSAENDCEvent subsId];
```
