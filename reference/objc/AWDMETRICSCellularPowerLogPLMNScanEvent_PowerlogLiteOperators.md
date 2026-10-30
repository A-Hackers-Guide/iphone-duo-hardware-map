# `AWDMETRICSCellularPowerLogPLMNScanEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 39 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _duration;
i _reasonForScan;
i _scanResult;
i _scanType;
I _subsId;
{?="timestamp"b1"duration"b1"reasonForScan"b1"scanResult"b1"scanType"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasScanResult;
@property (Ti,N,V_scanResult) scanResult;
@property (TB,N) hasScanType;
@property (Ti,N,V_scanType) scanType;
@property (TB,N) hasReasonForScan;
@property (Ti,N,V_reasonForScan) reasonForScan;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasTimestamp];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasTimestamp:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setTimestamp:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent writeTo:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent mergeFrom:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasDuration];
-[AWDMETRICSCellularPowerLogPLMNScanEvent timestamp];
-[AWDMETRICSCellularPowerLogPLMNScanEvent duration];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasDuration:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent scanType];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hash];
-[AWDMETRICSCellularPowerLogPLMNScanEvent copyTo:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent description];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setScanType:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setDuration:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent readFrom:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent copyWithZone:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent isEqual:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogPLMNScanEvent scanResult];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setScanResult:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent StringAsScanType:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasScanType:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasScanType];
-[AWDMETRICSCellularPowerLogPLMNScanEvent scanTypeAsString:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent StringAsReasonForScan:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent StringAsScanResult:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasReasonForScan];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasScanResult];
-[AWDMETRICSCellularPowerLogPLMNScanEvent hasSubsId];
-[AWDMETRICSCellularPowerLogPLMNScanEvent reasonForScan];
-[AWDMETRICSCellularPowerLogPLMNScanEvent reasonForScanAsString:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent scanResultAsString:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasReasonForScan:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasScanResult:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setHasSubsId:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setReasonForScan:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent setSubsId:];
-[AWDMETRICSCellularPowerLogPLMNScanEvent subsId];
```
