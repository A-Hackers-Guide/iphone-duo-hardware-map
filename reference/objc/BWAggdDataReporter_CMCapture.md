# `BWAggdDataReporter`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 47 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _aggdDispatchQueue;
i _lastShutterLag;
```

## Class methods

```
+[BWAggdDataReporter sharedInstance];
+[BWAggdDataReporter initialize];
```

## Instance methods

```
-[BWAggdDataReporter reportShutterLag:primaryCaptureType:secondaryCaptureType:captureFlags:sceneFlags:stillDuringVideo:frontCamera:];
-[BWAggdDataReporter reportAutoFocusPositionSensorMode:portType:];
-[BWAggdDataReporter reportISPCreateDuration:];
-[BWAggdDataReporter reportFaceCount:frontCamera:];
-[BWAggdDataReporter reportLockScreenCameraLaunchCancelledWithPrewarming:ispStreamingStarted:];
-[BWAggdDataReporter reportCameraLaunchWithoutPrewarm:];
-[BWAggdDataReporter reportStereoFusionProcessingTypeForCaptureType:isStereoFusionCapture:wideSubCaptureType:teleSubCaptureType:isOriginalImage:];
-[BWAggdDataReporter reportZeroShutterLagSuccess];
-[BWAggdDataReporter reportZoomFactor:primaryCaptureType:secondaryCaptureType:captureFlags:sceneFlags:stillDuringVideo:frontCamera:];
-[BWAggdDataReporter init];
-[BWAggdDataReporter reportStillImageAPSStatisticsForPortType:logicalFocusPosition:apsMotion:sphereMotion:accelMotion:gyroMotion:subjectDistance:luxLevel:];
-[BWAggdDataReporter reportCameraLaunchWithPrewarm:reason:];
-[BWAggdDataReporter reportSphereCalibrationForPosition:freqX:deltaFreqX:qX:deltaQX:gainX:freqY:deltaFreqY:qY:deltaQY:gainY:calibrationStatus:isValid:];
-[BWAggdDataReporter dealloc];
-[BWAggdDataReporter reportZeroShutterLagReferenceFrameSelectionFailureForCaptureType:];
-[BWAggdDataReporter reportZeroShutterLagPreviewTimeMachineInitFailure];
-[BWAggdDataReporter _aggdStereoFusionProcessingTypeStringForCaptureType:isStereoFusionCapture:wideSubCaptureType:teleSubCaptureType:isOriginalImage:];
-[BWAggdDataReporter reportNonCameraAppCaptureWithPrimaryCaptureType:secondaryCaptureType:captureFlags:sceneFlags:stillDuringVideo:frontCamera:];
-[BWAggdDataReporter reportSphereEndStopCalibrationForPosition:oisPositiveX:oisNegativeX:oisPositiveY:oisNegativeY:maxPositiveXDriftFromNVM:maxNegativeXDriftFromNVM:maxPositiveYDriftFromNVM:maxNegativeYDriftFromNVM:sphereStrokeX:sphereStrokeY:calibrationStatus:isValid:];
-[BWAggdDataReporter lastShutterLag];
-[BWAggdDataReporter reportZeroShutterLagInitSuccess];
-[BWAggdDataReporter reportAutoFocusCalibrationForPosition:freqZ:deltaFreqZ:qZ:deltaQZ:gainZ:calibrationStatus:gelModelCoefficientD1:gelModelCoefficientD2:gelModelCoefficientP1:gelModelCoefficientP2:isValid:];
-[BWAggdDataReporter reportCameraAppCaptureForNonCameraAppLoggingWithFrontCamera:];
-[BWAggdDataReporter reportPearlInfraredProjectorUptime:current:pattern:applicationID:];
-[BWAggdDataReporter reportAPSSphereInteractionCalibrationForPosition:residualErrorNeutral:calibrationZHeightNeutral:residualErrorMacro:calibrationZHeightMacro:calibrationStatus:isValid:];
-[BWAggdDataReporter reportAutoFocusPositionSensorCalibrationForPosition:iStopZEstimate:eSensorOutput:wSensorOutput:gravityZ:calibrationStatus:sensorTemp:successfulInfinityEndStopDelta:currentInfinityEndStopDelta:previousInfinityEndStopDelta:currentAngleDelta:previousAngleDelta:factoryCalibrationOffset:estimatedNeutralZ:deltaNeutralZFromNVM:estimatedSagZ:combinedSensorOutput:deltaSagFromNVM:isValid:dataWasRejectedByHistory:];
-[BWAggdDataReporter reportLockScreenCameraLaunchCompletedWithPrewarming:restartedSessionDueToError:];
-[BWAggdDataReporter _aggdGNRProcessingStatusStringFromProcessingStatus:];
-[BWAggdDataReporter reportZeroShutterLagFirmwareTimeMachineInitFailure];
-[BWAggdDataReporter reportLuxLevel:primaryCaptureType:secondaryCaptureType:captureFlags:sceneFlags:stillDuringVideo:frontCamera:];
-[BWAggdDataReporter reportGNRSampleBufferProcessorProcessingStatus:];
-[BWAggdDataReporter reportSDOFSampleBufferProcessorProcessingStatus:];
-[BWAggdDataReporter reportVideoRecordingAPSStatistics:stdDataFromAPSForTele:stdDataFromSphereForWide:stdDataFromSphereForTele:stdDataFromAccel:stdDataFromGyro:maxDataFromAPSForWide:maxDataFromAPSForTele:minDataFromAPSForWide:minDataFromAPSForTele:maxDataFromSphereForWide:maxDataFromSphereForTele:minDataFromSphereForWide:minDataFromSphereForTele:maxDataFromAccel:minDataFromAccel:maxDataFromGyro:minDataFromGyro:];
-[BWAggdDataReporter _aggdStringForPrefix:primaryCaptureType:secondaryCaptureType:captureFlags:sceneFlags:stillDuringVideo:frontCamera:];
-[BWAggdDataReporter reportSensorTemperature:frontCamera:];
-[BWAggdDataReporter _aggdSDOFProcessingStatusStringFromProcessingStatus:];
-[BWAggdDataReporter _aggdCameraStreamingTimeStringFromDeviceType:devicePosition:];
-[BWAggdDataReporter reportCriticalFocusErrorOccurredForPortType:];
-[BWAggdDataReporter reportCalibrationStatisticsWithTime:timeValue:attemptsField:attemptsValue:successField:successValue:magneticFieldMagnitudeField:magneticFieldMagnitudeValue:];
-[BWAggdDataReporter reportCameraStreamingTimeInMilliseconds:deviceType:devicePosition:];
-[BWAggdDataReporter _aggdPearlInfraredProjectorUptimeStringFromCurrent:pattern:applicationID:];
-[BWAggdDataReporter reportZeroShutterLagSphereInitFailure];
-[BWAggdDataReporter _aggdStereoFusionProcessingStatusStringFromProcessingStatus:];
-[BWAggdDataReporter reportSphereJitterDetectionsForPortType:detectionAttemps:successfulDetections:];
-[BWAggdDataReporter reportZeroShutterLagMetadataInitFailureWithReasons:];
-[BWAggdDataReporter reportStereoFusionSampleBufferProcessorProcessingStatus:];
-[BWAggdDataReporter reportAPSOffsetEstimatorForPortType:accelMotion:gyroMotion:inSessionOffset:deltaOffsetFC:deltaOffsetMI:deltaOffsetFATP:deltaOffsetLastSession:errorHeadroomViolated:errorConvergenceFailed:errorMotionTooLarge:errorConfidenceTooLow:errorOffsetTooLarge:errorDeltaTooLarge:errorSaturated:errorCouldNotRun:successRun:startAPSVoltage:modeGCOL:modeOL:];
```
