# `CLTripSegmentLocation`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 23 instance variables, 23 properties, 84 instance methods, 1 class methods

## Instance variables

```
i _referenceFrame;
i _rawReferenceFrame;
i _mapsRoadClass;
i _mapsFormOfWay;
i _locType;
i _locTypeStart;
i _locTypeStop;
i _signalEnvironmentType;
@"NSDate" _timestamp;
d _latitude;
d _longitude;
d _rawLatitude;
d _rawLongitude;
d _horizontalAccuracy;
d _course;
d _courseAccuracy;
d _speed;
d _speedAccuracy;
d _altitude;
d _altitudeAccuracy;
Q _reconstructionType;
Q _clRoadID;
Q _locationDataMask;
```

## Properties

```
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (Td,N,V_rawLatitude) rawLatitude;
@property (Td,N,V_rawLongitude) rawLongitude;
@property (Ti,R,N,V_rawReferenceFrame) rawReferenceFrame;
@property (Td,N,V_latitude) latitude;
@property (Td,N,V_longitude) longitude;
@property (Ti,R,N,V_referenceFrame) referenceFrame;
@property (Td,N,V_horizontalAccuracy) horizontalAccuracy;
@property (Td,N,V_course) course;
@property (Td,N,V_courseAccuracy) courseAccuracy;
@property (Td,N,V_speed) speed;
@property (Td,N,V_speedAccuracy) speedAccuracy;
@property (Td,N,V_altitude) altitude;
@property (Td,N,V_altitudeAccuracy) altitudeAccuracy;
@property (Ti,N,V_mapsRoadClass) mapsRoadClass;
@property (Ti,N,V_mapsFormOfWay) mapsFormOfWay;
@property (Ti,N,V_locType) locType;
@property (Ti,N,V_locTypeStart) locTypeStart;
@property (Ti,N,V_locTypeStop) locTypeStop;
@property (TQ,N,V_reconstructionType) reconstructionType;
@property (Ti,N,V_signalEnvironmentType) signalEnvironmentType;
@property (TQ,N,V_clRoadID) clRoadID;
@property (TQ,N,V_locationDataMask) locationDataMask;
```

## Class methods

```
+[CLTripSegmentLocation supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentLocation setSpeed:];
-[CLTripSegmentLocation speed];
-[CLTripSegmentLocation setLatitude:];
-[CLTripSegmentLocation latitude];
-[CLTripSegmentLocation longitude];
-[CLTripSegmentLocation altitude];
-[CLTripSegmentLocation setLongitude:];
-[CLTripSegmentLocation dealloc];
-[CLTripSegmentLocation timestamp];
-[CLTripSegmentLocation referenceFrame];
-[CLTripSegmentLocation horizontalAccuracy];
-[CLTripSegmentLocation setHorizontalAccuracy:];
-[CLTripSegmentLocation distanceFromLocation:];
-[CLTripSegmentLocation setAltitude:];
-[CLTripSegmentLocation encodeWithCoder:];
-[CLTripSegmentLocation speedAccuracy];
-[CLTripSegmentLocation initWithCoder:];
-[CLTripSegmentLocation initWithCLLocation:];
-[CLTripSegmentLocation courseAccuracy];
-[CLTripSegmentLocation copyWithZone:];
-[CLTripSegmentLocation course];
-[CLTripSegmentLocation setCourse:];
-[CLTripSegmentLocation isMapMatched];
-[CLTripSegmentLocation setCourseAccuracy:];
-[CLTripSegmentLocation setSpeedAccuracy:];
-[CLTripSegmentLocation distanceFromLatitude:longitude:];
-[CLTripSegmentLocation iOSTime];
-[CLTripSegmentLocation initWithTime:latitude:longitude:horizontalAccuracy:course:courseAccuracy:speed:speedAccuracy:altitude:altitudeAccuracy:locType:];
-[CLTripSegmentLocation locType];
-[CLTripSegmentLocation setRawLatitude:];
-[CLTripSegmentLocation setTripSegmentLocationDataMask:];
-[CLTripSegmentLocation setLocTypeStop:];
-[CLTripSegmentLocation updateCourse:andCourseAccuracy:];
-[CLTripSegmentLocation altitudeAccuracy];
-[CLTripSegmentLocation clRoadID];
-[CLTripSegmentLocation initWithLatitude:longitude:altitude:];
-[CLTripSegmentLocation initWithTime:latitude:longitude:horizontalAccuracy:course:courseAccuracy:speed:speedAccuracy:altitude:altitudeAccuracy:locType:referenceFrame:];
-[CLTripSegmentLocation initWithTime:latitude:longitude:horizontalAccuracy:course:courseAccuracy:speed:speedAccuracy:altitude:altitudeAccuracy:locType:referenceFrame:signalEnvironmentType:];
-[CLTripSegmentLocation isCourseValid];
-[CLTripSegmentLocation isDenseUrbanSignalEnvironment];
-[CLTripSegmentLocation isFoliageSignalEnvironment];
-[CLTripSegmentLocation isGPSLocationType];
-[CLTripSegmentLocation isGoodGPSFix];
-[CLTripSegmentLocation isGoodGPSFixWithGoodCourse];
-[CLTripSegmentLocation isInertialIntegrated];
-[CLTripSegmentLocation isLinearInterpolated];
-[CLTripSegmentLocation isLoiLocationType];
-[CLTripSegmentLocation isMarineSignalEnvironment];
-[CLTripSegmentLocation isOriginalLocationType];
-[CLTripSegmentLocation isRuralSignalEnvironment];
-[CLTripSegmentLocation isSpeedValid];
-[CLTripSegmentLocation isTripSegmentLocationFollowedByUTurnMaskSet];
-[CLTripSegmentLocation isTripSegmentLocationMotionStationaryMaskSet];
-[CLTripSegmentLocation isUrbanSignalEnvironment];
-[CLTripSegmentLocation isWiFiLocationType];
-[CLTripSegmentLocation locTypeStart];
-[CLTripSegmentLocation locTypeStop];
-[CLTripSegmentLocation locationDataMask];
-[CLTripSegmentLocation mapsFormOfWay];
-[CLTripSegmentLocation mapsRoadClass];
-[CLTripSegmentLocation rawLatitude];
-[CLTripSegmentLocation rawLongitude];
-[CLTripSegmentLocation rawReferenceFrame];
-[CLTripSegmentLocation reconstructionType];
-[CLTripSegmentLocation setAltitudeAccuracy:];
-[CLTripSegmentLocation setCLRoadID:];
-[CLTripSegmentLocation setClRoadID:];
-[CLTripSegmentLocation setLocType:];
-[CLTripSegmentLocation setLocTypeStart:];
-[CLTripSegmentLocation setLocationDataMask:];
-[CLTripSegmentLocation setLocationReconstructionType:];
-[CLTripSegmentLocation setMapsFormOfWay:];
-[CLTripSegmentLocation setMapsRoadClass:];
-[CLTripSegmentLocation setRawLatitude:longitude:referenceFrame:];
-[CLTripSegmentLocation setRawLongitude:];
-[CLTripSegmentLocation setReconstructionType:];
-[CLTripSegmentLocation setSignalEnvironmentType:];
-[CLTripSegmentLocation setStartLocationType:];
-[CLTripSegmentLocation setStartLocationType:andStopLocationType:];
-[CLTripSegmentLocation setStopLocationType:];
-[CLTripSegmentLocation signalEnvironmentType];
-[CLTripSegmentLocation updateAltitude:andAltitudeAccuracy:];
-[CLTripSegmentLocation updateLatitude:longitude:horizontalAccuracy:referenceFrame:];
-[CLTripSegmentLocation updateSpeed:andSpeedAccuracy:];
```
