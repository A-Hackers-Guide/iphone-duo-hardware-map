# `KCellularWcdmaRrcConfiguration`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _drxCycleLengthMs;
I _subsId;
B _isDcConfigured;
B _isMimoConfigured;
{?="timestamp"b1"drxCycleLengthMs"b1"subsId"b1"isDcConfigured"b1"isMimoConfigured"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDrxCycleLengthMs;
@property (TI,N,V_drxCycleLengthMs) drxCycleLengthMs;
@property (TB,N) hasIsMimoConfigured;
@property (TB,N,V_isMimoConfigured) isMimoConfigured;
@property (TB,N) hasIsDcConfigured;
@property (TB,N,V_isDcConfigured) isDcConfigured;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularWcdmaRrcConfiguration hasTimestamp];
-[KCellularWcdmaRrcConfiguration setHasTimestamp:];
-[KCellularWcdmaRrcConfiguration setTimestamp:];
-[KCellularWcdmaRrcConfiguration writeTo:];
-[KCellularWcdmaRrcConfiguration mergeFrom:];
-[KCellularWcdmaRrcConfiguration timestamp];
-[KCellularWcdmaRrcConfiguration hash];
-[KCellularWcdmaRrcConfiguration copyTo:];
-[KCellularWcdmaRrcConfiguration description];
-[KCellularWcdmaRrcConfiguration readFrom:];
-[KCellularWcdmaRrcConfiguration copyWithZone:];
-[KCellularWcdmaRrcConfiguration isEqual:];
-[KCellularWcdmaRrcConfiguration dictionaryRepresentation];
-[KCellularWcdmaRrcConfiguration hasSubsId];
-[KCellularWcdmaRrcConfiguration setHasSubsId:];
-[KCellularWcdmaRrcConfiguration setSubsId:];
-[KCellularWcdmaRrcConfiguration subsId];
-[KCellularWcdmaRrcConfiguration drxCycleLengthMs];
-[KCellularWcdmaRrcConfiguration hasDrxCycleLengthMs];
-[KCellularWcdmaRrcConfiguration hasIsDcConfigured];
-[KCellularWcdmaRrcConfiguration hasIsMimoConfigured];
-[KCellularWcdmaRrcConfiguration isDcConfigured];
-[KCellularWcdmaRrcConfiguration isMimoConfigured];
-[KCellularWcdmaRrcConfiguration setDrxCycleLengthMs:];
-[KCellularWcdmaRrcConfiguration setHasDrxCycleLengthMs:];
-[KCellularWcdmaRrcConfiguration setHasIsDcConfigured:];
-[KCellularWcdmaRrcConfiguration setHasIsMimoConfigured:];
-[KCellularWcdmaRrcConfiguration setIsDcConfigured:];
-[KCellularWcdmaRrcConfiguration setIsMimoConfigured:];
```
