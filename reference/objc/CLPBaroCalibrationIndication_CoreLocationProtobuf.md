# `CLPBaroCalibrationIndication`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
d _outdoorConfidence;
i _mapMatchRoadType;
B _isCalibratedBarometricAlt;
B _isMapMatched;
B _isOutdoorContext;
{?="outdoorConfidence"b1"mapMatchRoadType"b1"isCalibratedBarometricAlt"b1"isMapMatched"b1"isOutdoorContext"b1} _has;
```

## Properties

```
@property (TB,N) hasIsCalibratedBarometricAlt;
@property (TB,N,V_isCalibratedBarometricAlt) isCalibratedBarometricAlt;
@property (TB,N) hasIsMapMatched;
@property (TB,N,V_isMapMatched) isMapMatched;
@property (TB,N) hasIsOutdoorContext;
@property (TB,N,V_isOutdoorContext) isOutdoorContext;
@property (TB,N) hasOutdoorConfidence;
@property (Td,N,V_outdoorConfidence) outdoorConfidence;
@property (TB,N) hasMapMatchRoadType;
@property (Ti,N,V_mapMatchRoadType) mapMatchRoadType;
```

## Instance methods

```
-[CLPBaroCalibrationIndication writeTo:];
-[CLPBaroCalibrationIndication mergeFrom:];
-[CLPBaroCalibrationIndication hash];
-[CLPBaroCalibrationIndication copyTo:];
-[CLPBaroCalibrationIndication description];
-[CLPBaroCalibrationIndication readFrom:];
-[CLPBaroCalibrationIndication copyWithZone:];
-[CLPBaroCalibrationIndication isEqual:];
-[CLPBaroCalibrationIndication dictionaryRepresentation];
-[CLPBaroCalibrationIndication isMapMatched];
-[CLPBaroCalibrationIndication StringAsMapMatchRoadType:];
-[CLPBaroCalibrationIndication hasIsMapMatched];
-[CLPBaroCalibrationIndication hasIsCalibratedBarometricAlt];
-[CLPBaroCalibrationIndication hasIsOutdoorContext];
-[CLPBaroCalibrationIndication hasMapMatchRoadType];
-[CLPBaroCalibrationIndication hasOutdoorConfidence];
-[CLPBaroCalibrationIndication isCalibratedBarometricAlt];
-[CLPBaroCalibrationIndication isOutdoorContext];
-[CLPBaroCalibrationIndication mapMatchRoadType];
-[CLPBaroCalibrationIndication mapMatchRoadTypeAsString:];
-[CLPBaroCalibrationIndication outdoorConfidence];
-[CLPBaroCalibrationIndication setHasIsCalibratedBarometricAlt:];
-[CLPBaroCalibrationIndication setHasIsMapMatched:];
-[CLPBaroCalibrationIndication setHasIsOutdoorContext:];
-[CLPBaroCalibrationIndication setHasMapMatchRoadType:];
-[CLPBaroCalibrationIndication setHasOutdoorConfidence:];
-[CLPBaroCalibrationIndication setIsCalibratedBarometricAlt:];
-[CLPBaroCalibrationIndication setIsMapMatched:];
-[CLPBaroCalibrationIndication setIsOutdoorContext:];
-[CLPBaroCalibrationIndication setMapMatchRoadType:];
-[CLPBaroCalibrationIndication setOutdoorConfidence:];
```
