# `KCellularPmuAverageCurrent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _regulatorCurrents;
I _version;
{?="timestamp"b1"version"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_regulatorCurrents) regulatorCurrents;
@property (TB,N) hasVersion;
@property (TI,N,V_version) version;
```

## Class methods

```
+[KCellularPmuAverageCurrent regulatorCurrentType];
```

## Instance methods

```
-[KCellularPmuAverageCurrent hasVersion];
-[KCellularPmuAverageCurrent hasTimestamp];
-[KCellularPmuAverageCurrent setHasTimestamp:];
-[KCellularPmuAverageCurrent setTimestamp:];
-[KCellularPmuAverageCurrent writeTo:];
-[KCellularPmuAverageCurrent mergeFrom:];
-[KCellularPmuAverageCurrent timestamp];
-[KCellularPmuAverageCurrent setHasVersion:];
-[KCellularPmuAverageCurrent version];
-[KCellularPmuAverageCurrent hash];
-[KCellularPmuAverageCurrent copyTo:];
-[KCellularPmuAverageCurrent description];
-[KCellularPmuAverageCurrent setVersion:];
-[KCellularPmuAverageCurrent readFrom:];
-[KCellularPmuAverageCurrent copyWithZone:];
-[KCellularPmuAverageCurrent isEqual:];
-[KCellularPmuAverageCurrent dictionaryRepresentation];
-[KCellularPmuAverageCurrent addRegulatorCurrent:];
-[KCellularPmuAverageCurrent clearRegulatorCurrents];
-[KCellularPmuAverageCurrent regulatorCurrentAtIndex:];
-[KCellularPmuAverageCurrent regulatorCurrents];
-[KCellularPmuAverageCurrent regulatorCurrentsCount];
-[KCellularPmuAverageCurrent setRegulatorCurrents:];
```
