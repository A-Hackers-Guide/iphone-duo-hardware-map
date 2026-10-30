# `AWDMETRICSKCellularPowerLogBasebandSleepVeto`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
@"NSMutableArray" _sleepVetos;
{?="timestamp"b1"durationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_sleepVetos) sleepVetos;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
```

## Class methods

```
+[AWDMETRICSKCellularPowerLogBasebandSleepVeto sleepVetoType];
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto hasTimestamp];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto setTimestamp:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto writeTo:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto mergeFrom:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto timestamp];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto hash];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto copyTo:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto description];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto readFrom:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto copyWithZone:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto isEqual:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto durationMs];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto hasDurationMs];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto setDurationMs:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto setHasDurationMs:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto clearSleepVetos];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto sleepVetosCount];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto addSleepVeto:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto setSleepVetos:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto sleepVetoAtIndex:];
-[AWDMETRICSKCellularPowerLogBasebandSleepVeto sleepVetos];
```
