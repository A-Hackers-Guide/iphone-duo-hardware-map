# `CLPLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 33 instance variables, 59 properties, 125 instance methods, 1 class methods

## Instance variables

```
d _latitude;
d _longitude;
d _timestamp;
f _altitude;
@"NSMutableArray" _appBundleIdIndices;
@"CLPBaroCalibrationIndication" _baroCalibrationIndication;
i _context;
f _course;
f _courseAccuracy;
@"CLPMotionActivity" _dominantMotionActivity;
i _floor;
f _horizontalAccuracy;
f _horzUncSemiMaj;
f _horzUncSemiMajAz;
f _horzUncSemiMin;
i _modeIndicator;
@"CLPMotionActivity" _motionActivity;
i _motionActivityConfidence;
i _motionActivityType;
@"CLPPipelineDiagnosticReport" _pipelineDiagnosticReport;
@"CLPLocationProcessingMetadata" _processingMetadata;
i _provider;
@"CLPMotionActivity" _rawMotionActivity;
@"CLPSatelliteReport" _satReport;
f _speed;
f _speedAccuracy;
@"CLPVehicleType" _vehicleType;
f _verticalAccuracy;
B _isFromLocationController;
B _isProactiveLocation;
B _motionVehicleConnected;
B _motionVehicleConnectedStateChanged;
{?="altitude"b1"context"b1"course"b1"courseAccuracy"b1"floor"b1"horzUncSemiMaj"b1"horzUncSemiMajAz"b1"horzUncSemiMin"b1"modeIndicator"b1"motionActivityConfidence"b1"motionActivityType"b1"provider"b1"speed"b1"speedAccuracy"b1"verticalAccuracy"b1"isFromLocationController"b1"isProactiveLocation"b1"motionVehicleConnected"b1"motionVehicleConnectedStateChanged"b1} _has;
```

## Properties

```
@property (Td,N,V_latitude) latitude;
@property (Td,N,V_longitude) longitude;
@property (Tf,N,V_horizontalAccuracy) horizontalAccuracy;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasAltitude;
@property (Tf,N,V_altitude) altitude;
@property (TB,N) hasVerticalAccuracy;
@property (Tf,N,V_verticalAccuracy) verticalAccuracy;
@property (TB,N) hasSpeed;
@property (Tf,N,V_speed) speed;
@property (TB,N) hasCourse;
@property (Tf,N,V_course) course;
@property (TB,N) hasContext;
@property (Ti,N,V_context) context;
@property (TB,N) hasMotionActivityType;
@property (Ti,N,V_motionActivityType) motionActivityType;
@property (TB,N) hasMotionActivityConfidence;
@property (Ti,N,V_motionActivityConfidence) motionActivityConfidence;
@property (TB,N) hasProvider;
@property (Ti,N,V_provider) provider;
@property (TB,N) hasFloor;
@property (Ti,N,V_floor) floor;
@property (T@"NSMutableArray",&,N,V_appBundleIdIndices) appBundleIdIndices;
@property (TB,N) hasMotionVehicleConnectedStateChanged;
@property (TB,N,V_motionVehicleConnectedStateChanged) motionVehicleConnectedStateChanged;
@property (TB,N) hasMotionVehicleConnected;
@property (TB,N,V_motionVehicleConnected) motionVehicleConnected;
@property (TB,R,N) hasRawMotionActivity;
@property (T@"CLPMotionActivity",&,N,V_rawMotionActivity) rawMotionActivity;
@property (TB,R,N) hasMotionActivity;
@property (T@"CLPMotionActivity",&,N,V_motionActivity) motionActivity;
@property (TB,R,N) hasDominantMotionActivity;
@property (T@"CLPMotionActivity",&,N,V_dominantMotionActivity) dominantMotionActivity;
@property (TB,N) hasCourseAccuracy;
@property (Tf,N,V_courseAccuracy) courseAccuracy;
@property (TB,N) hasSpeedAccuracy;
@property (Tf,N,V_speedAccuracy) speedAccuracy;
@property (TB,N) hasModeIndicator;
@property (Ti,N,V_modeIndicator) modeIndicator;
@property (TB,N) hasHorzUncSemiMaj;
@property (Tf,N,V_horzUncSemiMaj) horzUncSemiMaj;
@property (TB,N) hasHorzUncSemiMin;
@property (Tf,N,V_horzUncSemiMin) horzUncSemiMin;
@property (TB,N) hasHorzUncSemiMajAz;
@property (Tf,N,V_horzUncSemiMajAz) horzUncSemiMajAz;
@property (TB,R,N) hasSatReport;
@property (T@"CLPSatelliteReport",&,N,V_satReport) satReport;
@property (TB,N) hasIsFromLocationController;
@property (TB,N,V_isFromLocationController) isFromLocationController;
@property (TB,R,N) hasPipelineDiagnosticReport;
@property (T@"CLPPipelineDiagnosticReport",&,N,V_pipelineDiagnosticReport) pipelineDiagnosticReport;
@property (TB,R,N) hasBaroCalibrationIndication;
@property (T@"CLPBaroCalibrationIndication",&,N,V_baroCalibrationIndication) baroCalibrationIndication;
@property (TB,R,N) hasProcessingMetadata;
@property (T@"CLPLocationProcessingMetadata",&,N,V_processingMetadata) processingMetadata;
@property (TB,N) hasIsProactiveLocation;
@property (TB,N,V_isProactiveLocation) isProactiveLocation;
@property (TB,R,N) hasVehicleType;
@property (T@"CLPVehicleType",&,N,V_vehicleType) vehicleType;
```

## Class methods

```
+[CLPLocation appBundleIdIndicesType];
```

## Instance methods

```
-[CLPLocation setTimestamp:];
-[CLPLocation setSpeed:];
-[CLPLocation writeTo:];
-[CLPLocation speed];
-[CLPLocation setLatitude:];
-[CLPLocation latitude];
-[CLPLocation mergeFrom:];
-[CLPLocation hasContext];
-[CLPLocation longitude];
-[CLPLocation altitude];
-[CLPLocation setLongitude:];
-[CLPLocation timestamp];
-[CLPLocation vehicleType];
-[CLPLocation provider];
-[CLPLocation horizontalAccuracy];
-[CLPLocation setHorizontalAccuracy:];
-[CLPLocation setContext:];
-[CLPLocation setAltitude:];
-[CLPLocation setVerticalAccuracy:];
-[CLPLocation verticalAccuracy];
-[CLPLocation dominantMotionActivity];
-[CLPLocation hash];
-[CLPLocation speedAccuracy];
-[CLPLocation copyTo:];
-[CLPLocation description];
-[CLPLocation readFrom:];
-[CLPLocation setDominantMotionActivity:];
-[CLPLocation courseAccuracy];
-[CLPLocation copyWithZone:];
-[CLPLocation context];
-[CLPLocation isEqual:];
-[CLPLocation setProvider:];
-[CLPLocation course];
-[CLPLocation motionActivity];
-[CLPLocation dictionaryRepresentation];
-[CLPLocation hasProvider];
-[CLPLocation setCourse:];
-[CLPLocation setHasAltitude:];
-[CLPLocation floor];
-[CLPLocation hasAltitude];
-[CLPLocation hasFloor];
-[CLPLocation setHasFloor:];
-[CLPLocation hasCourse];
-[CLPLocation hasCourseAccuracy];
-[CLPLocation hasSpeed];
-[CLPLocation hasSpeedAccuracy];
-[CLPLocation hasVerticalAccuracy];
-[CLPLocation setCourseAccuracy:];
-[CLPLocation setHasCourse:];
-[CLPLocation setHasCourseAccuracy:];
-[CLPLocation setHasSpeed:];
-[CLPLocation setHasSpeedAccuracy:];
-[CLPLocation setHasVerticalAccuracy:];
-[CLPLocation setSpeedAccuracy:];
-[CLPLocation setHasProvider:];
-[CLPLocation clearAppBundleIdIndices];
-[CLPLocation setHasHorzUncSemiMaj:];
-[CLPLocation setHasHorzUncSemiMajAz:];
-[CLPLocation setHasHorzUncSemiMin:];
-[CLPLocation setHasModeIndicator:];
-[CLPLocation setHasMotionVehicleConnected:];
-[CLPLocation setHasMotionVehicleConnectedStateChanged:];
-[CLPLocation setMotionActivity:];
-[CLPLocation setRawMotionActivity:];
-[CLPLocation hasMotionActivity];
-[CLPLocation setHasContext:];
-[CLPLocation setVehicleType:];
-[CLPLocation setFloor:];
-[CLPLocation setHasMotionActivityConfidence:];
-[CLPLocation hasMotionActivityConfidence];
-[CLPLocation hasMotionActivityType];
-[CLPLocation motionActivityConfidence];
-[CLPLocation motionActivityType];
-[CLPLocation setHasMotionActivityType:];
-[CLPLocation setMotionActivityConfidence:];
-[CLPLocation setMotionActivityType:];
-[CLPLocation StringAsModeIndicator:];
-[CLPLocation setHasIsFromLocationController:];
-[CLPLocation addAppBundleIdIndices:];
-[CLPLocation appBundleIdIndices];
-[CLPLocation appBundleIdIndicesAtIndex:];
-[CLPLocation appBundleIdIndicesCount];
-[CLPLocation baroCalibrationIndication];
-[CLPLocation hasBaroCalibrationIndication];
-[CLPLocation hasDominantMotionActivity];
-[CLPLocation hasHorzUncSemiMaj];
-[CLPLocation hasHorzUncSemiMajAz];
-[CLPLocation hasHorzUncSemiMin];
-[CLPLocation hasIsFromLocationController];
-[CLPLocation hasIsProactiveLocation];
-[CLPLocation hasModeIndicator];
-[CLPLocation hasMotionVehicleConnected];
-[CLPLocation hasMotionVehicleConnectedStateChanged];
-[CLPLocation hasPipelineDiagnosticReport];
-[CLPLocation hasProcessingMetadata];
-[CLPLocation hasRawMotionActivity];
-[CLPLocation hasSatReport];
-[CLPLocation hasVehicleType];
-[CLPLocation horzUncSemiMaj];
-[CLPLocation horzUncSemiMajAz];
-[CLPLocation horzUncSemiMin];
-[CLPLocation isFromLocationController];
-[CLPLocation isProactiveLocation];
-[CLPLocation modeIndicator];
-[CLPLocation modeIndicatorAsString:];
-[CLPLocation motionVehicleConnected];
-[CLPLocation motionVehicleConnectedStateChanged];
-[CLPLocation pipelineDiagnosticReport];
-[CLPLocation processingMetadata];
-[CLPLocation rawMotionActivity];
-[CLPLocation satReport];
-[CLPLocation setAppBundleIdIndices:];
-[CLPLocation setBaroCalibrationIndication:];
-[CLPLocation setHasIsProactiveLocation:];
-[CLPLocation setHorzUncSemiMaj:];
-[CLPLocation setHorzUncSemiMajAz:];
-[CLPLocation setHorzUncSemiMin:];
-[CLPLocation setIsFromLocationController:];
-[CLPLocation setIsProactiveLocation:];
-[CLPLocation setModeIndicator:];
-[CLPLocation setMotionVehicleConnected:];
-[CLPLocation setMotionVehicleConnectedStateChanged:];
-[CLPLocation setPipelineDiagnosticReport:];
-[CLPLocation setProcessingMetadata:];
-[CLPLocation setSatReport:];
```
