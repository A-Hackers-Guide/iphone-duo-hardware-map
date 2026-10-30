# `CLPCalibratedPressureCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 21 instance variables, 40 properties, 89 instance methods, 0 class methods

## Instance variables

```
d _latitudeDeg;
d _longitudeDeg;
d _timeSinceLastSignificantLocationVisitExitS;
d _timestampOfCalibrationS;
@"CLPMotionActivity" _activity;
f _altitudeHAEM;
f _altitudeHAEUncM;
f _calibratedPressurePa;
f _calibratedPressureUncPa;
@"CLPBaroCalibrationIndication" _calibration;
f _devicePressurePa;
f _devicePressureUncPa;
f _horizontalUncM;
i _quantizedDistChangeSinceLastCalibrationM;
i _quantizedTimeChangeSinceLastCalibrationS;
f _referenceAltM;
f _referenceAltUncM;
i _reliability;
f _speedMps;
f _speedUncMps;
{?="latitudeDeg"b1"longitudeDeg"b1"timeSinceLastSignificantLocationVisitExitS"b1"timestampOfCalibrationS"b1"altitudeHAEM"b1"altitudeHAEUncM"b1"calibratedPressurePa"b1"calibratedPressureUncPa"b1"devicePressurePa"b1"devicePressureUncPa"b1"horizontalUncM"b1"quantizedDistChangeSinceLastCalibrationM"b1"quantizedTimeChangeSinceLastCalibrationS"b1"referenceAltM"b1"referenceAltUncM"b1"reliability"b1"speedMps"b1"speedUncMps"b1} _has;
```

## Properties

```
@property (TB,N) hasDevicePressurePa;
@property (Tf,N,V_devicePressurePa) devicePressurePa;
@property (TB,N) hasDevicePressureUncPa;
@property (Tf,N,V_devicePressureUncPa) devicePressureUncPa;
@property (TB,N) hasCalibratedPressurePa;
@property (Tf,N,V_calibratedPressurePa) calibratedPressurePa;
@property (TB,N) hasCalibratedPressureUncPa;
@property (Tf,N,V_calibratedPressureUncPa) calibratedPressureUncPa;
@property (TB,N) hasTimestampOfCalibrationS;
@property (Td,N,V_timestampOfCalibrationS) timestampOfCalibrationS;
@property (TB,N) hasLatitudeDeg;
@property (Td,N,V_latitudeDeg) latitudeDeg;
@property (TB,N) hasLongitudeDeg;
@property (Td,N,V_longitudeDeg) longitudeDeg;
@property (TB,N) hasHorizontalUncM;
@property (Tf,N,V_horizontalUncM) horizontalUncM;
@property (TB,N) hasAltitudeHAEM;
@property (Tf,N,V_altitudeHAEM) altitudeHAEM;
@property (TB,N) hasAltitudeHAEUncM;
@property (Tf,N,V_altitudeHAEUncM) altitudeHAEUncM;
@property (TB,N) hasSpeedMps;
@property (Tf,N,V_speedMps) speedMps;
@property (TB,N) hasSpeedUncMps;
@property (Tf,N,V_speedUncMps) speedUncMps;
@property (TB,N) hasReferenceAltM;
@property (Tf,N,V_referenceAltM) referenceAltM;
@property (TB,N) hasReferenceAltUncM;
@property (Tf,N,V_referenceAltUncM) referenceAltUncM;
@property (TB,N) hasTimeSinceLastSignificantLocationVisitExitS;
@property (Td,N,V_timeSinceLastSignificantLocationVisitExitS) timeSinceLastSignificantLocationVisitExitS;
@property (TB,R,N) hasActivity;
@property (T@"CLPMotionActivity",&,N,V_activity) activity;
@property (TB,N) hasReliability;
@property (Ti,N,V_reliability) reliability;
@property (TB,R,N) hasCalibration;
@property (T@"CLPBaroCalibrationIndication",&,N,V_calibration) calibration;
@property (TB,N) hasQuantizedDistChangeSinceLastCalibrationM;
@property (Ti,N,V_quantizedDistChangeSinceLastCalibrationM) quantizedDistChangeSinceLastCalibrationM;
@property (TB,N) hasQuantizedTimeChangeSinceLastCalibrationS;
@property (Ti,N,V_quantizedTimeChangeSinceLastCalibrationS) quantizedTimeChangeSinceLastCalibrationS;
```

## Instance methods

```
-[CLPCalibratedPressureCollectionRequest writeTo:];
-[CLPCalibratedPressureCollectionRequest setActivity:];
-[CLPCalibratedPressureCollectionRequest mergeFrom:];
-[CLPCalibratedPressureCollectionRequest activity];
-[CLPCalibratedPressureCollectionRequest reliability];
-[CLPCalibratedPressureCollectionRequest hash];
-[CLPCalibratedPressureCollectionRequest copyTo:];
-[CLPCalibratedPressureCollectionRequest description];
-[CLPCalibratedPressureCollectionRequest readFrom:];
-[CLPCalibratedPressureCollectionRequest copyWithZone:];
-[CLPCalibratedPressureCollectionRequest setReliability:];
-[CLPCalibratedPressureCollectionRequest isEqual:];
-[CLPCalibratedPressureCollectionRequest dictionaryRepresentation];
-[CLPCalibratedPressureCollectionRequest calibration];
-[CLPCalibratedPressureCollectionRequest setLatitudeDeg:];
-[CLPCalibratedPressureCollectionRequest latitudeDeg];
-[CLPCalibratedPressureCollectionRequest longitudeDeg];
-[CLPCalibratedPressureCollectionRequest setLongitudeDeg:];
-[CLPCalibratedPressureCollectionRequest hasActivity];
-[CLPCalibratedPressureCollectionRequest setCalibration:];
-[CLPCalibratedPressureCollectionRequest hasAltitudeHAEM];
-[CLPCalibratedPressureCollectionRequest setSpeedUncMps:];
-[CLPCalibratedPressureCollectionRequest StringAsReliability:];
-[CLPCalibratedPressureCollectionRequest altitudeHAEUncM];
-[CLPCalibratedPressureCollectionRequest hasLongitudeDeg];
-[CLPCalibratedPressureCollectionRequest setHasSpeedMps:];
-[CLPCalibratedPressureCollectionRequest altitudeHAEM];
-[CLPCalibratedPressureCollectionRequest calibratedPressurePa];
-[CLPCalibratedPressureCollectionRequest calibratedPressureUncPa];
-[CLPCalibratedPressureCollectionRequest devicePressurePa];
-[CLPCalibratedPressureCollectionRequest devicePressureUncPa];
-[CLPCalibratedPressureCollectionRequest hasAltitudeHAEUncM];
-[CLPCalibratedPressureCollectionRequest hasCalibratedPressurePa];
-[CLPCalibratedPressureCollectionRequest hasCalibratedPressureUncPa];
-[CLPCalibratedPressureCollectionRequest hasCalibration];
-[CLPCalibratedPressureCollectionRequest hasDevicePressurePa];
-[CLPCalibratedPressureCollectionRequest hasDevicePressureUncPa];
-[CLPCalibratedPressureCollectionRequest hasHorizontalUncM];
-[CLPCalibratedPressureCollectionRequest hasLatitudeDeg];
-[CLPCalibratedPressureCollectionRequest hasQuantizedDistChangeSinceLastCalibrationM];
-[CLPCalibratedPressureCollectionRequest hasQuantizedTimeChangeSinceLastCalibrationS];
-[CLPCalibratedPressureCollectionRequest hasReferenceAltM];
-[CLPCalibratedPressureCollectionRequest hasReferenceAltUncM];
-[CLPCalibratedPressureCollectionRequest hasReliability];
-[CLPCalibratedPressureCollectionRequest hasSpeedMps];
-[CLPCalibratedPressureCollectionRequest hasSpeedUncMps];
-[CLPCalibratedPressureCollectionRequest hasTimeSinceLastSignificantLocationVisitExitS];
-[CLPCalibratedPressureCollectionRequest hasTimestampOfCalibrationS];
-[CLPCalibratedPressureCollectionRequest horizontalUncM];
-[CLPCalibratedPressureCollectionRequest quantizedDistChangeSinceLastCalibrationM];
-[CLPCalibratedPressureCollectionRequest quantizedTimeChangeSinceLastCalibrationS];
-[CLPCalibratedPressureCollectionRequest referenceAltM];
-[CLPCalibratedPressureCollectionRequest referenceAltUncM];
-[CLPCalibratedPressureCollectionRequest reliabilityAsString:];
-[CLPCalibratedPressureCollectionRequest setAltitudeHAEM:];
-[CLPCalibratedPressureCollectionRequest setAltitudeHAEUncM:];
-[CLPCalibratedPressureCollectionRequest setCalibratedPressurePa:];
-[CLPCalibratedPressureCollectionRequest setCalibratedPressureUncPa:];
-[CLPCalibratedPressureCollectionRequest setDevicePressurePa:];
-[CLPCalibratedPressureCollectionRequest setDevicePressureUncPa:];
-[CLPCalibratedPressureCollectionRequest setHasAltitudeHAEM:];
-[CLPCalibratedPressureCollectionRequest setHasAltitudeHAEUncM:];
-[CLPCalibratedPressureCollectionRequest setHasCalibratedPressurePa:];
-[CLPCalibratedPressureCollectionRequest setHasCalibratedPressureUncPa:];
-[CLPCalibratedPressureCollectionRequest setHasDevicePressurePa:];
-[CLPCalibratedPressureCollectionRequest setHasDevicePressureUncPa:];
-[CLPCalibratedPressureCollectionRequest setHasHorizontalUncM:];
-[CLPCalibratedPressureCollectionRequest setHasLatitudeDeg:];
-[CLPCalibratedPressureCollectionRequest setHasLongitudeDeg:];
-[CLPCalibratedPressureCollectionRequest setHasQuantizedDistChangeSinceLastCalibrationM:];
-[CLPCalibratedPressureCollectionRequest setHasQuantizedTimeChangeSinceLastCalibrationS:];
-[CLPCalibratedPressureCollectionRequest setHasReferenceAltM:];
-[CLPCalibratedPressureCollectionRequest setHasReferenceAltUncM:];
-[CLPCalibratedPressureCollectionRequest setHasReliability:];
-[CLPCalibratedPressureCollectionRequest setHasSpeedUncMps:];
-[CLPCalibratedPressureCollectionRequest setHasTimeSinceLastSignificantLocationVisitExitS:];
-[CLPCalibratedPressureCollectionRequest setHasTimestampOfCalibrationS:];
-[CLPCalibratedPressureCollectionRequest setHorizontalUncM:];
-[CLPCalibratedPressureCollectionRequest setQuantizedDistChangeSinceLastCalibrationM:];
-[CLPCalibratedPressureCollectionRequest setQuantizedTimeChangeSinceLastCalibrationS:];
-[CLPCalibratedPressureCollectionRequest setReferenceAltM:];
-[CLPCalibratedPressureCollectionRequest setReferenceAltUncM:];
-[CLPCalibratedPressureCollectionRequest setSpeedMps:];
-[CLPCalibratedPressureCollectionRequest setTimeSinceLastSignificantLocationVisitExitS:];
-[CLPCalibratedPressureCollectionRequest setTimestampOfCalibrationS:];
-[CLPCalibratedPressureCollectionRequest speedMps];
-[CLPCalibratedPressureCollectionRequest speedUncMps];
-[CLPCalibratedPressureCollectionRequest timeSinceLastSignificantLocationVisitExitS];
-[CLPCalibratedPressureCollectionRequest timestampOfCalibrationS];
```
