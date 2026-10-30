# `CLPIndoorPressure`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
f _pressure;
f _temperature;
{?="timestamp"b1"pressure"b1"temperature"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasPressure;
@property (Tf,N,V_pressure) pressure;
@property (TB,N) hasTemperature;
@property (Tf,N,V_temperature) temperature;
```

## Instance methods

```
-[CLPIndoorPressure hasTimestamp];
-[CLPIndoorPressure setHasTimestamp:];
-[CLPIndoorPressure setTimestamp:];
-[CLPIndoorPressure writeTo:];
-[CLPIndoorPressure mergeFrom:];
-[CLPIndoorPressure setTemperature:];
-[CLPIndoorPressure timestamp];
-[CLPIndoorPressure pressure];
-[CLPIndoorPressure hash];
-[CLPIndoorPressure copyTo:];
-[CLPIndoorPressure description];
-[CLPIndoorPressure readFrom:];
-[CLPIndoorPressure copyWithZone:];
-[CLPIndoorPressure isEqual:];
-[CLPIndoorPressure temperature];
-[CLPIndoorPressure dictionaryRepresentation];
-[CLPIndoorPressure setPressure:];
-[CLPIndoorPressure hasTemperature];
-[CLPIndoorPressure setHasTemperature:];
-[CLPIndoorPressure hasPressure];
-[CLPIndoorPressure setHasPressure:];
```
