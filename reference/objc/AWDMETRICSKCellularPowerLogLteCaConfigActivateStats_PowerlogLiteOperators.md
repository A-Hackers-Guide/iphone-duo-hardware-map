# `AWDMETRICSKCellularPowerLogLteCaConfigActivateStats`

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
+[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats binType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats writeTo:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats timestamp];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hash];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats copyTo:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats description];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats readFrom:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats isEqual:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats durationMs];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hasDurationMs];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setDurationMs:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats bins];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setBins:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats isDataPreferred];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats addBin:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hasLastSdmState];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats binAtIndex:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats binsCount];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats clearBins];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats hasSubsId];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats lastSdmState];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats setSubsId:];
-[AWDMETRICSKCellularPowerLogLteCaConfigActivateStats subsId];
```
