# `AWDMETRICSCellularPowerLogShutdown`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _duration;
Q _timestamp;
I _count;
I _durationMs;
{?="duration"b1"timestamp"b1"count"b1"durationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasCount;
@property (TI,N,V_count) count;
@property (TB,N) hasDuration;
@property (TQ,N,V_duration) duration;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogShutdown hasTimestamp];
-[AWDMETRICSCellularPowerLogShutdown setHasTimestamp:];
-[AWDMETRICSCellularPowerLogShutdown setTimestamp:];
-[AWDMETRICSCellularPowerLogShutdown writeTo:];
-[AWDMETRICSCellularPowerLogShutdown setCount:];
-[AWDMETRICSCellularPowerLogShutdown mergeFrom:];
-[AWDMETRICSCellularPowerLogShutdown hasDuration];
-[AWDMETRICSCellularPowerLogShutdown timestamp];
-[AWDMETRICSCellularPowerLogShutdown count];
-[AWDMETRICSCellularPowerLogShutdown duration];
-[AWDMETRICSCellularPowerLogShutdown setHasDuration:];
-[AWDMETRICSCellularPowerLogShutdown hash];
-[AWDMETRICSCellularPowerLogShutdown copyTo:];
-[AWDMETRICSCellularPowerLogShutdown description];
-[AWDMETRICSCellularPowerLogShutdown setDuration:];
-[AWDMETRICSCellularPowerLogShutdown readFrom:];
-[AWDMETRICSCellularPowerLogShutdown copyWithZone:];
-[AWDMETRICSCellularPowerLogShutdown isEqual:];
-[AWDMETRICSCellularPowerLogShutdown dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogShutdown hasCount];
-[AWDMETRICSCellularPowerLogShutdown setHasCount:];
-[AWDMETRICSCellularPowerLogShutdown durationMs];
-[AWDMETRICSCellularPowerLogShutdown hasDurationMs];
-[AWDMETRICSCellularPowerLogShutdown setDurationMs:];
-[AWDMETRICSCellularPowerLogShutdown setHasDurationMs:];
```
