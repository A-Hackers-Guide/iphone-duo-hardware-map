# `AWDMETRICSKCellularPowerLogLteCarrierComponentInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _carrierInfos;
I _subsId;
B _isDataPreferred;
{?="timestamp"b1"subsId"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (T@"NSMutableArray",&,N,V_carrierInfos) carrierInfos;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo carrierInfoType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo hasTimestamp];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setTimestamp:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo writeTo:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo timestamp];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo hash];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo copyTo:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo description];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo readFrom:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo isEqual:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo addCarrierInfo:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo isDataPreferred];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo carrierInfoAtIndex:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo carrierInfos];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo carrierInfosCount];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo clearCarrierInfos];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo hasSubsId];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setCarrierInfos:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setHasSubsId:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo setSubsId:];
-[AWDMETRICSKCellularPowerLogLteCarrierComponentInfo subsId];
```
