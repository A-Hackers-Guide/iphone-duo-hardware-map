# `AWDMETRICSKCellularPowerLogNRCarrierComponentInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 33 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _carrierInfos;
i _freqRange;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"freqRange"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (T@"NSMutableArray",&,N,V_carrierInfos) carrierInfos;
@property (TB,N) hasFreqRange;
@property (Ti,N,V_freqRange) freqRange;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo carrierInfoType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo writeTo:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo timestamp];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo hash];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo copyTo:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo description];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo readFrom:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo isEqual:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo addCarrierInfo:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo isDataPreferred];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo StringAsFreqRange:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo carrierInfoAtIndex:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo carrierInfos];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo carrierInfosCount];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo clearCarrierInfos];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo freqRange];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo freqRangeAsString:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo hasFreqRange];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo hasSubsId];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setCarrierInfos:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setFreqRange:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setHasFreqRange:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo setSubsId:];
-[AWDMETRICSKCellularPowerLogNRCarrierComponentInfo subsId];
```
