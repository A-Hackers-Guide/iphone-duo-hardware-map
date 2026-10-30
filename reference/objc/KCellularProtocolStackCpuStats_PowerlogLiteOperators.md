# `KCellularProtocolStackCpuStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _cores;
I _durationMs;
I _voltageVm;
{?="timestamp"b1"durationMs"b1"voltageVm"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasVoltageVm;
@property (TI,N,V_voltageVm) voltageVm;
@property (T@"NSMutableArray",&,N,V_cores) cores;
```

## Class methods

```
+[KCellularProtocolStackCpuStats coresType];
```

## Instance methods

```
-[KCellularProtocolStackCpuStats hasTimestamp];
-[KCellularProtocolStackCpuStats setHasTimestamp:];
-[KCellularProtocolStackCpuStats setTimestamp:];
-[KCellularProtocolStackCpuStats writeTo:];
-[KCellularProtocolStackCpuStats mergeFrom:];
-[KCellularProtocolStackCpuStats timestamp];
-[KCellularProtocolStackCpuStats hash];
-[KCellularProtocolStackCpuStats copyTo:];
-[KCellularProtocolStackCpuStats description];
-[KCellularProtocolStackCpuStats readFrom:];
-[KCellularProtocolStackCpuStats copyWithZone:];
-[KCellularProtocolStackCpuStats isEqual:];
-[KCellularProtocolStackCpuStats dictionaryRepresentation];
-[KCellularProtocolStackCpuStats durationMs];
-[KCellularProtocolStackCpuStats hasDurationMs];
-[KCellularProtocolStackCpuStats setDurationMs:];
-[KCellularProtocolStackCpuStats setHasDurationMs:];
-[KCellularProtocolStackCpuStats addCores:];
-[KCellularProtocolStackCpuStats clearCores];
-[KCellularProtocolStackCpuStats cores];
-[KCellularProtocolStackCpuStats coresAtIndex:];
-[KCellularProtocolStackCpuStats coresCount];
-[KCellularProtocolStackCpuStats hasVoltageVm];
-[KCellularProtocolStackCpuStats setCores:];
-[KCellularProtocolStackCpuStats setHasVoltageVm:];
-[KCellularProtocolStackCpuStats setVoltageVm:];
-[KCellularProtocolStackCpuStats voltageVm];
```
