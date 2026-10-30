# `KCellularGsmL1State`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
i _l1State;
I _subsId;
{?="timestamp"b1"l1State"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasL1State;
@property (Ti,N,V_l1State) l1State;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularGsmL1State hasTimestamp];
-[KCellularGsmL1State setHasTimestamp:];
-[KCellularGsmL1State setTimestamp:];
-[KCellularGsmL1State writeTo:];
-[KCellularGsmL1State mergeFrom:];
-[KCellularGsmL1State timestamp];
-[KCellularGsmL1State hash];
-[KCellularGsmL1State copyTo:];
-[KCellularGsmL1State description];
-[KCellularGsmL1State readFrom:];
-[KCellularGsmL1State copyWithZone:];
-[KCellularGsmL1State isEqual:];
-[KCellularGsmL1State dictionaryRepresentation];
-[KCellularGsmL1State hasSubsId];
-[KCellularGsmL1State setHasSubsId:];
-[KCellularGsmL1State setSubsId:];
-[KCellularGsmL1State subsId];
-[KCellularGsmL1State StringAsL1State:];
-[KCellularGsmL1State l1State];
-[KCellularGsmL1State hasL1State];
-[KCellularGsmL1State l1StateAsString:];
-[KCellularGsmL1State setHasL1State:];
-[KCellularGsmL1State setL1State:];
```
