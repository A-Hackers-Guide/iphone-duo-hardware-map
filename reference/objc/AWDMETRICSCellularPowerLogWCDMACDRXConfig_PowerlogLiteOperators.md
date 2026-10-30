# `AWDMETRICSCellularPowerLogWCDMACDRXConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _drxCycleLength;
I _subsId;
{?="timestamp"b1"drxCycleLength"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDrxCycleLength;
@property (TI,N,V_drxCycleLength) drxCycleLength;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig hasTimestamp];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setHasTimestamp:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setTimestamp:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig writeTo:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig mergeFrom:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig timestamp];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig hash];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig copyTo:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig description];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig readFrom:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig copyWithZone:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig isEqual:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig drxCycleLength];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig hasDrxCycleLength];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig hasSubsId];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setDrxCycleLength:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setHasDrxCycleLength:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setHasSubsId:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig setSubsId:];
-[AWDMETRICSCellularPowerLogWCDMACDRXConfig subsId];
```
