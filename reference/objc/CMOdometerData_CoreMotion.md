# `CMOdometerData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 21 instance variables, 32 properties, 57 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _slope;
@"NSNumber" _maxAbsSlope;
@"NSDate" _startDate;
@"NSDate" _endDate;
q _originDevice;
@"NSNumber" _distance;
@"NSNumber" _currentSpeed;
@"NSNumber" _averageSpeed;
@"NSNumber" _accuracy;
@"NSNumber" _gpsAltitude;
@"NSNumber" _rawSpeed;
@"NSNumber" _odometer;
@"NSNumber" _gpsSpeedAccuracy;
@"NSNumber" _timestampGps;
@"NSNumber" _groundAltitude;
@"NSNumber" _groundAltitudeUncertainty;
@"NSNumber" _smoothedGPSAltitude;
@"NSNumber" _smoothedGPSAltitudeUncertainty;
@"NSNumber" _gpsCourseRadians;
@"NSNumber" _gpsCourseAccuracy;
@"NSNumber" _deltaGroundAltitude;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSNumber",&,N,V_distance) distance;
@property (T@"NSNumber",&,N,V_currentSpeed) currentSpeed;
@property (T@"NSNumber",&,N,V_averageSpeed) averageSpeed;
@property (T@"NSNumber",&,N,V_accuracy) accuracy;
@property (T@"NSNumber",&,N,V_gpsAltitude) gpsAltitude;
@property (T@"NSNumber",&,N,V_rawSpeed) rawSpeed;
@property (T@"NSNumber",&,N,V_odometer) odometer;
@property (T@"NSNumber",&,N,V_gpsSpeedAccuracy) gpsSpeedAccuracy;
@property (T@"NSNumber",&,N,V_timestampGps) timestampGps;
@property (T@"NSNumber",&,N,V_groundAltitude) groundAltitude;
@property (T@"NSNumber",&,N,V_groundAltitudeUncertainty) groundAltitudeUncertainty;
@property (T@"NSNumber",&,N,V_smoothedGPSAltitude) smoothedGPSAltitude;
@property (T@"NSNumber",&,N,V_smoothedGPSAltitudeUncertainty) smoothedGPSAltitudeUncertainty;
@property (T@"NSNumber",&,N,V_gpsCourseRadians) gpsCourseRadians;
@property (T@"NSNumber",&,N,V_gpsCourseAccuracy) gpsCourseAccuracy;
@property (T@"NSNumber",&,N,V_deltaGroundAltitude) deltaGroundAltitude;
@property (T@"NSNumber",&,N,V_slope) slope;
@property (T@"NSNumber",&,N,V_maxAbsSlope) maxAbsSlope;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
@property (Td,R,N) deltaDistance;
@property (Td,R,N) deltaDistanceAccuracy;
@property (Td,R,N) speed;
@property (Td,R,N) speedAccuracy;
@property (T@"NSDate",R,N) gpsDate;
@property (Td,R,N) deltaAltitude;
@property (Td,R,N) verticalAccuracy;
@property (Tq,R,N,V_originDevice) originDevice;
```

## Class methods

```
+[CMOdometerData supportsSecureCoding];
```

## Instance methods

```
-[CMOdometerData startDate];
-[CMOdometerData distance];
-[CMOdometerData setDistance:];
-[CMOdometerData groundAltitudeUncertainty];
-[CMOdometerData speed];
-[CMOdometerData dealloc];
-[CMOdometerData endDate];
-[CMOdometerData deltaDistanceAccuracy];
-[CMOdometerData groundAltitude];
-[CMOdometerData accuracy];
-[CMOdometerData odometer];
-[CMOdometerData verticalAccuracy];
-[CMOdometerData encodeWithCoder:];
-[CMOdometerData speedAccuracy];
-[CMOdometerData description];
-[CMOdometerData initWithCoder:];
-[CMOdometerData deltaDistance];
-[CMOdometerData copyWithZone:];
-[CMOdometerData originDevice];
-[CMOdometerData slope];
-[CMOdometerData gpsDate];
-[CMOdometerData setGpsAltitude:];
-[CMOdometerData setMaxAbsSlope:];
-[CMOdometerData averageSpeed];
-[CMOdometerData binarySampleRepresentation];
-[CMOdometerData currentSpeed];
-[CMOdometerData deltaAltitude];
-[CMOdometerData deltaGroundAltitude];
-[CMOdometerData gpsAltitude];
-[CMOdometerData gpsCourseAccuracy];
-[CMOdometerData gpsCourseRadians];
-[CMOdometerData gpsSpeedAccuracy];
-[CMOdometerData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMOdometerData initWithDeltaDistance:startDate:endDate:accuracy:rawSpeed:gpsSpeedAccuracy:timestampGps:deltaGroundAltitude:groundAltitudeUncertainty:originDevice:slope:maxAbsSlope:];
-[CMOdometerData initWithDistance:startDate:endDate:currentSpeed:averageSpeed:];
-[CMOdometerData maxAbsSlope];
-[CMOdometerData rawSpeed];
-[CMOdometerData relativeTimestampGps];
-[CMOdometerData setAccuracy:];
-[CMOdometerData setAverageSpeed:];
-[CMOdometerData setCurrentSpeed:];
-[CMOdometerData setDeltaGroundAltitude:];
-[CMOdometerData setGpsCourseAccuracy:];
-[CMOdometerData setGpsCourseRadians:];
-[CMOdometerData setGpsSpeedAccuracy:];
-[CMOdometerData setGroundAltitude:];
-[CMOdometerData setGroundAltitudeUncertainty:];
-[CMOdometerData setOdometer:];
-[CMOdometerData setRawSpeed:];
-[CMOdometerData setSlope:];
-[CMOdometerData setSmoothedGPSAltitude:];
-[CMOdometerData setSmoothedGPSAltitudeUncertainty:];
-[CMOdometerData setTimestampGps:];
-[CMOdometerData smoothedGPSAltitude];
-[CMOdometerData smoothedGPSAltitudeUncertainty];
-[CMOdometerData timestampGps];
-[CMOdometerData updateStartDate:];
```
