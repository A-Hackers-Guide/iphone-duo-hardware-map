# `AWDMETRICSCellularRfTunerHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _ftQualInd;
I _subsId;
@"NSMutableArray" _tunerStateDurations;
{?="timestamp"b1"ftQualInd"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_tunerStateDurations) tunerStateDurations;
@property (TB,N) hasFtQualInd;
@property (TI,N,V_ftQualInd) ftQualInd;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Class methods

```
+[AWDMETRICSCellularRfTunerHist tunerStateDurationType];
```

## Instance methods

```
-[AWDMETRICSCellularRfTunerHist hasTimestamp];
-[AWDMETRICSCellularRfTunerHist setHasTimestamp:];
-[AWDMETRICSCellularRfTunerHist setTimestamp:];
-[AWDMETRICSCellularRfTunerHist writeTo:];
-[AWDMETRICSCellularRfTunerHist mergeFrom:];
-[AWDMETRICSCellularRfTunerHist timestamp];
-[AWDMETRICSCellularRfTunerHist hash];
-[AWDMETRICSCellularRfTunerHist copyTo:];
-[AWDMETRICSCellularRfTunerHist description];
-[AWDMETRICSCellularRfTunerHist readFrom:];
-[AWDMETRICSCellularRfTunerHist copyWithZone:];
-[AWDMETRICSCellularRfTunerHist isEqual:];
-[AWDMETRICSCellularRfTunerHist dictionaryRepresentation];
-[AWDMETRICSCellularRfTunerHist addTunerStateDuration:];
-[AWDMETRICSCellularRfTunerHist clearTunerStateDurations];
-[AWDMETRICSCellularRfTunerHist ftQualInd];
-[AWDMETRICSCellularRfTunerHist hasFtQualInd];
-[AWDMETRICSCellularRfTunerHist hasSubsId];
-[AWDMETRICSCellularRfTunerHist setFtQualInd:];
-[AWDMETRICSCellularRfTunerHist setHasFtQualInd:];
-[AWDMETRICSCellularRfTunerHist setHasSubsId:];
-[AWDMETRICSCellularRfTunerHist setSubsId:];
-[AWDMETRICSCellularRfTunerHist setTunerStateDurations:];
-[AWDMETRICSCellularRfTunerHist subsId];
-[AWDMETRICSCellularRfTunerHist tunerStateDurationAtIndex:];
-[AWDMETRICSCellularRfTunerHist tunerStateDurations];
-[AWDMETRICSCellularRfTunerHist tunerStateDurationsCount];
```
