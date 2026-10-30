# `CLPCMAbsoluteAltitude`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
d _accuracy;
d _altitude;
d _filteredPressure;
d _precision;
d _timestamp;
i _statusInfo;
{?="accuracy"b1"filteredPressure"b1"precision"b1"statusInfo"b1} _has;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_altitude) altitude;
@property (TB,N) hasAccuracy;
@property (Td,N,V_accuracy) accuracy;
@property (TB,N) hasPrecision;
@property (Td,N,V_precision) precision;
@property (TB,N) hasFilteredPressure;
@property (Td,N,V_filteredPressure) filteredPressure;
@property (TB,N) hasStatusInfo;
@property (Ti,N,V_statusInfo) statusInfo;
```

## Instance methods

```
-[CLPCMAbsoluteAltitude precision];
-[CLPCMAbsoluteAltitude setTimestamp:];
-[CLPCMAbsoluteAltitude writeTo:];
-[CLPCMAbsoluteAltitude mergeFrom:];
-[CLPCMAbsoluteAltitude altitude];
-[CLPCMAbsoluteAltitude timestamp];
-[CLPCMAbsoluteAltitude accuracy];
-[CLPCMAbsoluteAltitude setAltitude:];
-[CLPCMAbsoluteAltitude hash];
-[CLPCMAbsoluteAltitude copyTo:];
-[CLPCMAbsoluteAltitude description];
-[CLPCMAbsoluteAltitude readFrom:];
-[CLPCMAbsoluteAltitude copyWithZone:];
-[CLPCMAbsoluteAltitude isEqual:];
-[CLPCMAbsoluteAltitude filteredPressure];
-[CLPCMAbsoluteAltitude dictionaryRepresentation];
-[CLPCMAbsoluteAltitude setPrecision:];
-[CLPCMAbsoluteAltitude setAccuracy:];
-[CLPCMAbsoluteAltitude statusInfo];
-[CLPCMAbsoluteAltitude setHasAccuracy:];
-[CLPCMAbsoluteAltitude hasAccuracy];
-[CLPCMAbsoluteAltitude StringAsStatusInfo:];
-[CLPCMAbsoluteAltitude hasFilteredPressure];
-[CLPCMAbsoluteAltitude hasPrecision];
-[CLPCMAbsoluteAltitude hasStatusInfo];
-[CLPCMAbsoluteAltitude setFilteredPressure:];
-[CLPCMAbsoluteAltitude setHasFilteredPressure:];
-[CLPCMAbsoluteAltitude setHasPrecision:];
-[CLPCMAbsoluteAltitude setHasStatusInfo:];
-[CLPCMAbsoluteAltitude setStatusInfo:];
-[CLPCMAbsoluteAltitude statusInfoAsString:];
```
