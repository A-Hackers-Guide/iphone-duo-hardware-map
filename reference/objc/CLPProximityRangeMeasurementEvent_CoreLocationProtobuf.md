# `CLPProximityRangeMeasurementEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
d _azimuthAngleRad;
d _elevationAngleRad;
d _multipathProbability;
d _rangeM;
d _sweepAngleDeg;
d _timestamp;
d _trackScore;
i _technology;
{?="azimuthAngleRad"b1"elevationAngleRad"b1"multipathProbability"b1"rangeM"b1"sweepAngleDeg"b1"timestamp"b1"trackScore"b1"technology"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasRangeM;
@property (Td,N,V_rangeM) rangeM;
@property (TB,N) hasAzimuthAngleRad;
@property (Td,N,V_azimuthAngleRad) azimuthAngleRad;
@property (TB,N) hasElevationAngleRad;
@property (Td,N,V_elevationAngleRad) elevationAngleRad;
@property (TB,N) hasTechnology;
@property (Ti,N,V_technology) technology;
@property (TB,N) hasMultipathProbability;
@property (Td,N,V_multipathProbability) multipathProbability;
@property (TB,N) hasTrackScore;
@property (Td,N,V_trackScore) trackScore;
@property (TB,N) hasSweepAngleDeg;
@property (Td,N,V_sweepAngleDeg) sweepAngleDeg;
```

## Instance methods

```
-[CLPProximityRangeMeasurementEvent hasTimestamp];
-[CLPProximityRangeMeasurementEvent setHasTimestamp:];
-[CLPProximityRangeMeasurementEvent setTimestamp:];
-[CLPProximityRangeMeasurementEvent writeTo:];
-[CLPProximityRangeMeasurementEvent mergeFrom:];
-[CLPProximityRangeMeasurementEvent timestamp];
-[CLPProximityRangeMeasurementEvent hash];
-[CLPProximityRangeMeasurementEvent copyTo:];
-[CLPProximityRangeMeasurementEvent description];
-[CLPProximityRangeMeasurementEvent readFrom:];
-[CLPProximityRangeMeasurementEvent copyWithZone:];
-[CLPProximityRangeMeasurementEvent isEqual:];
-[CLPProximityRangeMeasurementEvent dictionaryRepresentation];
-[CLPProximityRangeMeasurementEvent technology];
-[CLPProximityRangeMeasurementEvent setTechnology:];
-[CLPProximityRangeMeasurementEvent azimuthAngleRad];
-[CLPProximityRangeMeasurementEvent elevationAngleRad];
-[CLPProximityRangeMeasurementEvent hasAzimuthAngleRad];
-[CLPProximityRangeMeasurementEvent hasElevationAngleRad];
-[CLPProximityRangeMeasurementEvent hasMultipathProbability];
-[CLPProximityRangeMeasurementEvent hasRangeM];
-[CLPProximityRangeMeasurementEvent hasSweepAngleDeg];
-[CLPProximityRangeMeasurementEvent hasTechnology];
-[CLPProximityRangeMeasurementEvent hasTrackScore];
-[CLPProximityRangeMeasurementEvent multipathProbability];
-[CLPProximityRangeMeasurementEvent rangeM];
-[CLPProximityRangeMeasurementEvent setAzimuthAngleRad:];
-[CLPProximityRangeMeasurementEvent setElevationAngleRad:];
-[CLPProximityRangeMeasurementEvent setHasAzimuthAngleRad:];
-[CLPProximityRangeMeasurementEvent setHasElevationAngleRad:];
-[CLPProximityRangeMeasurementEvent setHasMultipathProbability:];
-[CLPProximityRangeMeasurementEvent setHasRangeM:];
-[CLPProximityRangeMeasurementEvent setHasSweepAngleDeg:];
-[CLPProximityRangeMeasurementEvent setHasTechnology:];
-[CLPProximityRangeMeasurementEvent setHasTrackScore:];
-[CLPProximityRangeMeasurementEvent setMultipathProbability:];
-[CLPProximityRangeMeasurementEvent setRangeM:];
-[CLPProximityRangeMeasurementEvent setSweepAngleDeg:];
-[CLPProximityRangeMeasurementEvent setTrackScore:];
-[CLPProximityRangeMeasurementEvent sweepAngleDeg];
-[CLPProximityRangeMeasurementEvent trackScore];
```
