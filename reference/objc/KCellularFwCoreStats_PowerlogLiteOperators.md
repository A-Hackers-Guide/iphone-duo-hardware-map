# `KCellularFwCoreStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
@"EutraStats" _eutraStats;
@"GeraStats" _geraStats;
I _subsId;
@"UtraFddStats" _utraFddStats;
@"UtraTddStats" _utraTddStats;
{?="timestamp"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,R,N) hasGeraStats;
@property (T@"GeraStats",&,N,V_geraStats) geraStats;
@property (TB,R,N) hasUtraFddStats;
@property (T@"UtraFddStats",&,N,V_utraFddStats) utraFddStats;
@property (TB,R,N) hasUtraTddStats;
@property (T@"UtraTddStats",&,N,V_utraTddStats) utraTddStats;
@property (TB,R,N) hasEutraStats;
@property (T@"EutraStats",&,N,V_eutraStats) eutraStats;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularFwCoreStats hasTimestamp];
-[KCellularFwCoreStats setHasTimestamp:];
-[KCellularFwCoreStats setTimestamp:];
-[KCellularFwCoreStats writeTo:];
-[KCellularFwCoreStats mergeFrom:];
-[KCellularFwCoreStats timestamp];
-[KCellularFwCoreStats hash];
-[KCellularFwCoreStats copyTo:];
-[KCellularFwCoreStats description];
-[KCellularFwCoreStats readFrom:];
-[KCellularFwCoreStats copyWithZone:];
-[KCellularFwCoreStats isEqual:];
-[KCellularFwCoreStats dictionaryRepresentation];
-[KCellularFwCoreStats hasSubsId];
-[KCellularFwCoreStats setHasSubsId:];
-[KCellularFwCoreStats setSubsId:];
-[KCellularFwCoreStats subsId];
-[KCellularFwCoreStats hasUtraFddStats];
-[KCellularFwCoreStats hasUtraTddStats];
-[KCellularFwCoreStats eutraStats];
-[KCellularFwCoreStats geraStats];
-[KCellularFwCoreStats hasEutraStats];
-[KCellularFwCoreStats hasGeraStats];
-[KCellularFwCoreStats setEutraStats:];
-[KCellularFwCoreStats setGeraStats:];
-[KCellularFwCoreStats setUtraFddStats:];
-[KCellularFwCoreStats setUtraTddStats:];
-[KCellularFwCoreStats utraFddStats];
-[KCellularFwCoreStats utraTddStats];
```
