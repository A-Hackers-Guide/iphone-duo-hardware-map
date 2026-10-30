# `AWDMETRICSCellularNrSdmEndcRelease`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _fr;
I _subsId;
i _triggerCause;
{?="timestamp"b1"fr"b1"subsId"b1"triggerCause"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasTriggerCause;
@property (Ti,N,V_triggerCause) triggerCause;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasFr;
@property (Ti,N,V_fr) fr;
```

## Instance methods

```
-[AWDMETRICSCellularNrSdmEndcRelease hasTimestamp];
-[AWDMETRICSCellularNrSdmEndcRelease setHasTimestamp:];
-[AWDMETRICSCellularNrSdmEndcRelease setTimestamp:];
-[AWDMETRICSCellularNrSdmEndcRelease writeTo:];
-[AWDMETRICSCellularNrSdmEndcRelease mergeFrom:];
-[AWDMETRICSCellularNrSdmEndcRelease timestamp];
-[AWDMETRICSCellularNrSdmEndcRelease hash];
-[AWDMETRICSCellularNrSdmEndcRelease copyTo:];
-[AWDMETRICSCellularNrSdmEndcRelease description];
-[AWDMETRICSCellularNrSdmEndcRelease readFrom:];
-[AWDMETRICSCellularNrSdmEndcRelease copyWithZone:];
-[AWDMETRICSCellularNrSdmEndcRelease isEqual:];
-[AWDMETRICSCellularNrSdmEndcRelease dictionaryRepresentation];
-[AWDMETRICSCellularNrSdmEndcRelease StringAsFr:];
-[AWDMETRICSCellularNrSdmEndcRelease hasTriggerCause];
-[AWDMETRICSCellularNrSdmEndcRelease StringAsTriggerCause:];
-[AWDMETRICSCellularNrSdmEndcRelease fr];
-[AWDMETRICSCellularNrSdmEndcRelease frAsString:];
-[AWDMETRICSCellularNrSdmEndcRelease hasFr];
-[AWDMETRICSCellularNrSdmEndcRelease hasSubsId];
-[AWDMETRICSCellularNrSdmEndcRelease setFr:];
-[AWDMETRICSCellularNrSdmEndcRelease setHasFr:];
-[AWDMETRICSCellularNrSdmEndcRelease setHasSubsId:];
-[AWDMETRICSCellularNrSdmEndcRelease setHasTriggerCause:];
-[AWDMETRICSCellularNrSdmEndcRelease setSubsId:];
-[AWDMETRICSCellularNrSdmEndcRelease setTriggerCause:];
-[AWDMETRICSCellularNrSdmEndcRelease subsId];
-[AWDMETRICSCellularNrSdmEndcRelease triggerCause];
-[AWDMETRICSCellularNrSdmEndcRelease triggerCauseAsString:];
```
