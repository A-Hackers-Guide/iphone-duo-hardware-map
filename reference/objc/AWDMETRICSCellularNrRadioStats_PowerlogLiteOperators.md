# `AWDMETRICSCellularNrRadioStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bwpInfos;
I _durationMs;
I _subsId;
{?="timestamp"b1"durationMs"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_bwpInfos) bwpInfos;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
```

## Class methods

```
+[AWDMETRICSCellularNrRadioStats bwpInfoType];
```

## Instance methods

```
-[AWDMETRICSCellularNrRadioStats hasTimestamp];
-[AWDMETRICSCellularNrRadioStats setHasTimestamp:];
-[AWDMETRICSCellularNrRadioStats setTimestamp:];
-[AWDMETRICSCellularNrRadioStats writeTo:];
-[AWDMETRICSCellularNrRadioStats mergeFrom:];
-[AWDMETRICSCellularNrRadioStats timestamp];
-[AWDMETRICSCellularNrRadioStats hash];
-[AWDMETRICSCellularNrRadioStats copyTo:];
-[AWDMETRICSCellularNrRadioStats description];
-[AWDMETRICSCellularNrRadioStats readFrom:];
-[AWDMETRICSCellularNrRadioStats copyWithZone:];
-[AWDMETRICSCellularNrRadioStats isEqual:];
-[AWDMETRICSCellularNrRadioStats dictionaryRepresentation];
-[AWDMETRICSCellularNrRadioStats durationMs];
-[AWDMETRICSCellularNrRadioStats hasDurationMs];
-[AWDMETRICSCellularNrRadioStats setDurationMs:];
-[AWDMETRICSCellularNrRadioStats setHasDurationMs:];
-[AWDMETRICSCellularNrRadioStats bwpInfoAtIndex:];
-[AWDMETRICSCellularNrRadioStats addBwpInfo:];
-[AWDMETRICSCellularNrRadioStats bwpInfos];
-[AWDMETRICSCellularNrRadioStats bwpInfosCount];
-[AWDMETRICSCellularNrRadioStats clearBwpInfos];
-[AWDMETRICSCellularNrRadioStats hasSubsId];
-[AWDMETRICSCellularNrRadioStats setBwpInfos:];
-[AWDMETRICSCellularNrRadioStats setHasSubsId:];
-[AWDMETRICSCellularNrRadioStats setSubsId:];
-[AWDMETRICSCellularNrRadioStats subsId];
```
