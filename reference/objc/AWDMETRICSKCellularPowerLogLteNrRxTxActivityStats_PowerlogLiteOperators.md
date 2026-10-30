# `AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 13 properties, 40 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
i _lastSdmState;
@"NSData" _plmn;
@"NSMutableArray" _rxTxActs;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"lastSdmState"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_rxTxActs) rxTxActs;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,R,N) hasPlmn;
@property (T@"NSData",&,N,V_plmn) plmn;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
@property (TB,N) hasLastSdmState;
@property (Ti,N,V_lastSdmState) lastSdmState;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats rxTxActType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats writeTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats timestamp];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setPlmn:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hash];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats copyTo:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats description];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats readFrom:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats isEqual:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats plmn];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats durationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasDurationMs];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasPlmn];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats isDataPreferred];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats rxTxActAtIndex:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats StringAsLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasLastSdmState];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats addRxTxAct:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats clearRxTxActs];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats hasSubsId];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats lastSdmState];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats lastSdmStateAsString:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats rxTxActs];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats rxTxActsCount];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setHasLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setLastSdmState:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setRxTxActs:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats setSubsId:];
-[AWDMETRICSKCellularPowerLogLteNrRxTxActivityStats subsId];
```
