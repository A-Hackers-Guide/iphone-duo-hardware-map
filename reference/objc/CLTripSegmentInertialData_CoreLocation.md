# `CLTripSegmentInertialData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _dataPeriod_s;
d _deltaCourse_rad;
d _deltaSpeed_mps;
d _deltaCourseVar_rad2;
d _deltaSpeedVar_mps2;
d _deltaCourseSpeedCovar_radmps;
```

## Properties

```
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (Td,N,V_dataPeriod_s) dataPeriod_s;
@property (Td,N,V_deltaCourse_rad) deltaCourse_rad;
@property (Td,N,V_deltaSpeed_mps) deltaSpeed_mps;
@property (Td,N,V_deltaCourseVar_rad2) deltaCourseVar_rad2;
@property (Td,N,V_deltaSpeedVar_mps2) deltaSpeedVar_mps2;
@property (Td,N,V_deltaCourseSpeedCovar_radmps) deltaCourseSpeedCovar_radmps;
```

## Class methods

```
+[CLTripSegmentInertialData supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentInertialData dealloc];
-[CLTripSegmentInertialData timestamp];
-[CLTripSegmentInertialData encodeWithCoder:];
-[CLTripSegmentInertialData isValid];
-[CLTripSegmentInertialData description];
-[CLTripSegmentInertialData initWithCoder:];
-[CLTripSegmentInertialData copyWithZone:];
-[CLTripSegmentInertialData deltaCourse_rad];
-[CLTripSegmentInertialData dataPeriod_s];
-[CLTripSegmentInertialData deltaCourseSpeedCovar_radmps];
-[CLTripSegmentInertialData deltaCourseVar_rad2];
-[CLTripSegmentInertialData deltaSpeedVar_mps2];
-[CLTripSegmentInertialData deltaSpeed_mps];
-[CLTripSegmentInertialData initWithTime:dataPeriodSec:deltaCourseRad:deltaSpeedMps:deltaCourseVarRad2:deltaSpeedVarMps2:deltaCourseSpeedCovarRadMps:];
-[CLTripSegmentInertialData setDataPeriod_s:];
-[CLTripSegmentInertialData setDeltaCourseSpeedCovar_radmps:];
-[CLTripSegmentInertialData setDeltaCourseVar_rad2:];
-[CLTripSegmentInertialData setDeltaCourse_rad:];
-[CLTripSegmentInertialData setDeltaSpeedVar_mps2:];
-[CLTripSegmentInertialData setDeltaSpeed_mps:];
```
