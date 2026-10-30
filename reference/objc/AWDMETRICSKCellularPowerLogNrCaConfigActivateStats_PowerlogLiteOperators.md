# `AWDMETRICSKCellularPowerLogNrCaConfigActivateStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 11 properties, 37 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _durationMs;
i _lastSdmState;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_bins) bins;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hasTimestamp];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setTimestamp:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats writeTo:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats mergeFrom:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats timestamp];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hash];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats copyTo:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats description];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats readFrom:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats copyWithZone:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats isEqual:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats durationMs];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hasDurationMs];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setDurationMs:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats bins];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setBins:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats isDataPreferred];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats addBin:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hasLastSdmState];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats binAtIndex:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats binsCount];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats clearBins];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats hasSubsId];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats lastSdmState];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setLastSdmState:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats setSubsId:];
-[AWDMETRICSKCellularPowerLogNrCaConfigActivateStats subsId];
```
