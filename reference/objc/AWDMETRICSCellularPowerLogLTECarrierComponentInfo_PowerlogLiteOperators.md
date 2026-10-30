# `AWDMETRICSCellularPowerLogLTECarrierComponentInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _carrierInfos;
I _subsId;
{?="timestamp"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (T@"NSMutableArray",&,N,V_carrierInfos) carrierInfos;
```

## Class methods

```
+[AWDMETRICSCellularPowerLogLTECarrierComponentInfo carrierInfoType];
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo hasTimestamp];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo setHasTimestamp:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo setTimestamp:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo writeTo:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo mergeFrom:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo timestamp];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo hash];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo copyTo:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo description];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo readFrom:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo copyWithZone:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo isEqual:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo addCarrierInfo:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo carrierInfoAtIndex:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo carrierInfos];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo carrierInfosCount];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo clearCarrierInfos];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo hasSubsId];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo setCarrierInfos:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo setHasSubsId:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo setSubsId:];
-[AWDMETRICSCellularPowerLogLTECarrierComponentInfo subsId];
```
