# `AWDMETRICSKCellularPowerLogNRAntennaElement`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _antennaElements;
I _subsId;
I _totalDurationMs;
{?="timestamp"b1"subsId"b1"totalDurationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasTotalDurationMs;
@property (TI,N,V_totalDurationMs) totalDurationMs;
@property (T@"NSMutableArray",&,N,V_antennaElements) antennaElements;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRAntennaElement hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement writeTo:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement timestamp];
-[AWDMETRICSKCellularPowerLogNRAntennaElement totalDurationMs];
-[AWDMETRICSKCellularPowerLogNRAntennaElement hash];
-[AWDMETRICSKCellularPowerLogNRAntennaElement copyTo:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement description];
-[AWDMETRICSKCellularPowerLogNRAntennaElement readFrom:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement isEqual:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElements];
-[AWDMETRICSKCellularPowerLogNRAntennaElement addAntennaElements:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsAtIndex:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsCount];
-[AWDMETRICSKCellularPowerLogNRAntennaElement clearAntennaElements];
-[AWDMETRICSKCellularPowerLogNRAntennaElement hasSubsId];
-[AWDMETRICSKCellularPowerLogNRAntennaElement hasTotalDurationMs];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setAntennaElements:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setHasTotalDurationMs:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setSubsId:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement setTotalDurationMs:];
-[AWDMETRICSKCellularPowerLogNRAntennaElement subsId];
```
