# `KCellularTdsL1State`

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
-[KCellularTdsL1State hasTimestamp];
-[KCellularTdsL1State setHasTimestamp:];
-[KCellularTdsL1State setTimestamp:];
-[KCellularTdsL1State writeTo:];
-[KCellularTdsL1State mergeFrom:];
-[KCellularTdsL1State timestamp];
-[KCellularTdsL1State hash];
-[KCellularTdsL1State copyTo:];
-[KCellularTdsL1State description];
-[KCellularTdsL1State readFrom:];
-[KCellularTdsL1State copyWithZone:];
-[KCellularTdsL1State isEqual:];
-[KCellularTdsL1State dictionaryRepresentation];
-[KCellularTdsL1State hasSubsId];
-[KCellularTdsL1State setHasSubsId:];
-[KCellularTdsL1State setSubsId:];
-[KCellularTdsL1State subsId];
-[KCellularTdsL1State StringAsL1State:];
-[KCellularTdsL1State l1State];
-[KCellularTdsL1State hasL1State];
-[KCellularTdsL1State l1StateAsString:];
-[KCellularTdsL1State setHasL1State:];
-[KCellularTdsL1State setL1State:];
```
