# `AWDMETRICSCellularPowerLogNRCarrierComponentInfo`

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
+[AWDMETRICSCellularPowerLogNRCarrierComponentInfo carrierInfoType];
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo hasTimestamp];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo setHasTimestamp:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo setTimestamp:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo writeTo:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo mergeFrom:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo timestamp];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo hash];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo copyTo:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo description];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo readFrom:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo copyWithZone:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo isEqual:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo addCarrierInfo:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo carrierInfoAtIndex:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo carrierInfos];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo carrierInfosCount];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo clearCarrierInfos];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo hasSubsId];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo setCarrierInfos:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo setHasSubsId:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo setSubsId:];
-[AWDMETRICSCellularPowerLogNRCarrierComponentInfo subsId];
```
