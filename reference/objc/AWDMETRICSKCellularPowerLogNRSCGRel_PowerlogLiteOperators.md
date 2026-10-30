# `AWDMETRICSKCellularPowerLogNRSCGRel`

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
-[AWDMETRICSKCellularPowerLogNRSCGRel setEvent:];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRSCGRel writeTo:];
-[AWDMETRICSKCellularPowerLogNRSCGRel mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRSCGRel timestamp];
-[AWDMETRICSKCellularPowerLogNRSCGRel event];
-[AWDMETRICSKCellularPowerLogNRSCGRel setPlmn:];
-[AWDMETRICSKCellularPowerLogNRSCGRel hash];
-[AWDMETRICSKCellularPowerLogNRSCGRel copyTo:];
-[AWDMETRICSKCellularPowerLogNRSCGRel description];
-[AWDMETRICSKCellularPowerLogNRSCGRel readFrom:];
-[AWDMETRICSKCellularPowerLogNRSCGRel copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRSCGRel isEqual:];
-[AWDMETRICSKCellularPowerLogNRSCGRel plmn];
-[AWDMETRICSKCellularPowerLogNRSCGRel dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasEvent];
-[AWDMETRICSKCellularPowerLogNRSCGRel StringAsEvent:];
-[AWDMETRICSKCellularPowerLogNRSCGRel eventAsString:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasEvent:];
-[AWDMETRICSKCellularPowerLogNRSCGRel StringAsFr:];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasPlmn];
-[AWDMETRICSKCellularPowerLogNRSCGRel isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSCGRel numSubs];
-[AWDMETRICSKCellularPowerLogNRSCGRel fr];
-[AWDMETRICSKCellularPowerLogNRSCGRel frAsString:];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasFr];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasNumSubs];
-[AWDMETRICSKCellularPowerLogNRSCGRel hasSubsId];
-[AWDMETRICSKCellularPowerLogNRSCGRel setFr:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasFr:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setNumSubs:];
-[AWDMETRICSKCellularPowerLogNRSCGRel setSubsId:];
-[AWDMETRICSKCellularPowerLogNRSCGRel subsId];
```
