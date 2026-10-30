# `KCellularPeripheralStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _durationMs;
@"NSMutableArray" _peripherals;
{?="timestamp"b1"durationMs"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_peripherals) peripherals;
```

## Class methods

```
+[KCellularPeripheralStats peripheralsType];
```

## Instance methods

```
-[KCellularPeripheralStats hasTimestamp];
-[KCellularPeripheralStats setHasTimestamp:];
-[KCellularPeripheralStats setTimestamp:];
-[KCellularPeripheralStats writeTo:];
-[KCellularPeripheralStats mergeFrom:];
-[KCellularPeripheralStats timestamp];
-[KCellularPeripheralStats hash];
-[KCellularPeripheralStats copyTo:];
-[KCellularPeripheralStats description];
-[KCellularPeripheralStats readFrom:];
-[KCellularPeripheralStats copyWithZone:];
-[KCellularPeripheralStats isEqual:];
-[KCellularPeripheralStats peripherals];
-[KCellularPeripheralStats dictionaryRepresentation];
-[KCellularPeripheralStats durationMs];
-[KCellularPeripheralStats hasDurationMs];
-[KCellularPeripheralStats setDurationMs:];
-[KCellularPeripheralStats setHasDurationMs:];
-[KCellularPeripheralStats setPeripherals:];
-[KCellularPeripheralStats addPeripherals:];
-[KCellularPeripheralStats clearPeripherals];
-[KCellularPeripheralStats peripheralsAtIndex:];
-[KCellularPeripheralStats peripheralsCount];
```
