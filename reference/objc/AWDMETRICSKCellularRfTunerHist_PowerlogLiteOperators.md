# `AWDMETRICSKCellularRfTunerHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 30 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSData" _plmn;
I _subsId;
@"NSMutableArray" _tunerStateDurations;
B _isDataPreferred;
{?="timestamp"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_tunerStateDurations) tunerStateDurations;
@property (TB,R,N) hasPlmn;
@property (T@"NSData",&,N,V_plmn) plmn;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Class methods

```
+[AWDMETRICSKCellularRfTunerHist tunerStateDurationType];
```

## Instance methods

```
-[AWDMETRICSKCellularRfTunerHist hasTimestamp];
-[AWDMETRICSKCellularRfTunerHist setHasTimestamp:];
-[AWDMETRICSKCellularRfTunerHist setTimestamp:];
-[AWDMETRICSKCellularRfTunerHist writeTo:];
-[AWDMETRICSKCellularRfTunerHist mergeFrom:];
-[AWDMETRICSKCellularRfTunerHist timestamp];
-[AWDMETRICSKCellularRfTunerHist setPlmn:];
-[AWDMETRICSKCellularRfTunerHist hash];
-[AWDMETRICSKCellularRfTunerHist copyTo:];
-[AWDMETRICSKCellularRfTunerHist description];
-[AWDMETRICSKCellularRfTunerHist readFrom:];
-[AWDMETRICSKCellularRfTunerHist copyWithZone:];
-[AWDMETRICSKCellularRfTunerHist isEqual:];
-[AWDMETRICSKCellularRfTunerHist plmn];
-[AWDMETRICSKCellularRfTunerHist dictionaryRepresentation];
-[AWDMETRICSKCellularRfTunerHist hasPlmn];
-[AWDMETRICSKCellularRfTunerHist isDataPreferred];
-[AWDMETRICSKCellularRfTunerHist addTunerStateDuration:];
-[AWDMETRICSKCellularRfTunerHist clearTunerStateDurations];
-[AWDMETRICSKCellularRfTunerHist hasIsDataPreferred];
-[AWDMETRICSKCellularRfTunerHist hasSubsId];
-[AWDMETRICSKCellularRfTunerHist setHasIsDataPreferred:];
-[AWDMETRICSKCellularRfTunerHist setHasSubsId:];
-[AWDMETRICSKCellularRfTunerHist setIsDataPreferred:];
-[AWDMETRICSKCellularRfTunerHist setSubsId:];
-[AWDMETRICSKCellularRfTunerHist setTunerStateDurations:];
-[AWDMETRICSKCellularRfTunerHist subsId];
-[AWDMETRICSKCellularRfTunerHist tunerStateDurationAtIndex:];
-[AWDMETRICSKCellularRfTunerHist tunerStateDurations];
-[AWDMETRICSKCellularRfTunerHist tunerStateDurationsCount];
```
