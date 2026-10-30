# `CMMotionContextSession`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 0 properties, 22 instance methods, 1 class methods

## Instance variables

```
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _deviceMotionDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionConfigDispatcher;
{CMPdr="fPdrInputs"{CMPdrInputs="fInertialAccelTNB"{AccelTNBFrame="lastValidTNBTimestamp"d"lastSample"{CMVector<float, 3UL>="elements"}"T"{CMVector<float, 3UL>="elements"}"N"{CMVector<float, 3UL>="elements"}"B"{CMVector<float, 3UL>="elements"}"jerkNorm"f"curvature"f"torsion"f"isValid"B}"fLastTimestamp"d"fSampleDT"d"kSosFilterParams"{Parameters="B"[12d]"A"[12d]"inputScaleValues"[4d]"outputScaleValues"[4d]}"fInertialUserAccelFilter"{array<CMSosFilter<4>, 3UL>="__elems_"[3{CMSosFilter<4UL>="kParams"^{Parameters}"fOutput"f"fRegister"[12f]}]}"fInertialRotationRateFilter"{array<CMSosFilter<4>, 3UL>="__elems_"[3{CMSosFilter<4UL>="kParams"^{Parameters}"fOutput"f"fRegister"[12f]}]}}"fAlgType"i"fDirectionalityDetector"{CMPdrDirectionality="_lastStartImpulseTimestamp"d"_lastEndImpulseTimestamp"d"_lastStepDirectionRadians"d"_lastPosition"{CMVector<double, 2UL>="elements"}"_inertialBuffer"{CMFixedSizeQueue<CMPdrDirectionality::AggAccelSample, 245UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[32c]"fStorage"{CMQueueStorage<CMPdrDirectionality::AggAccelSample, 245UL>="buffer"[7808c]}}}"fPdrEstimatorOnHead"{unique_ptr<CMPdrEstimatorOnHead, std::default_delete<CMPdrEstimatorOnHead>>=""{?="__ptr_"^{CMPdrEstimatorOnHead}}}"fPdrEstimatorOnBody"{unique_ptr<CMPdrEstimatorOnBody, std::default_delete<CMPdrEstimatorOnBody>>=""{?="__ptr_"^{CMPdrEstimatorOnBody}}}"fPdrEstimatorHandSwing"{unique_ptr<CMDoTEstimatorHandSwing, std::default_delete<CMDoTEstimatorHandSwing>>=""{?="__ptr_"^{CMDoTEstimatorHandSwing}}}"fPdrEstimatorTexting"{unique_ptr<CMDoTEstimatorInHandTexting, std::default_delete<CMDoTEstimatorInHandTexting>>=""{?="__ptr_"^{CMDoTEstimatorInHandTexting}}}} _pdr;
{CMAccessoryActivity="fActivityPacket"{ActivityPacket="state"i"stateTransitionTimestamp"d"stepImpulse"{Impulse="start"d"end"d}}"fSitStandEnabled"B"fSitStandDetector"{unique_ptr<CMSitStandDetector, std::default_delete<CMSitStandDetector>>=""{?="__ptr_"^{CMSitStandDetector}}}"fAccessoryStepDetector"{CMAccessoryStepDetector="fDetectedSteps"B"fCandidateDetected"B"fNotifiedDetectedSteps"B"fLookingForFirstStep"B"fInertialAggAccelBuffer"{CMFixedSizeQueue<CMAccessoryStepDetector::AggAccelSample, 50UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[32c]"fStorage"{CMQueueStorage<CMAccessoryStepDetector::AggAccelSample, 50UL>="buffer"[1568c]}}"fInertialAccelBuffer"{CMFixedSizeQueue<CMAccessoryStepDetector::VectorSample, 50UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[32c]"fStorage"{CMQueueStorage<CMAccessoryStepDetector::VectorSample, 50UL>="buffer"[1568c]}}"fFaceRotationRateBuffer"{CMFixedSizeQueue<CMAccessoryStepDetector::FaceRotationRateSample, 50UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[32c]"fStorage"{CMQueueStorage<CMAccessoryStepDetector::FaceRotationRateSample, 50UL>="buffer"[1568c]}}"fAuxRotationRateNormBuffer"{CMFixedSizeQueue<float, 150UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[4c]"fStorage"{CMQueueStorage<float, 150UL>="buffer"[596c]}}"fInertialAggForwardAccelBufferFaceFrame"{CMFixedSizeQueue<float, 50UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[4c]"fStorage"{CMQueueStorage<float, 50UL>="buffer"[196c]}}"fYawRotationRateBuffer"{CMFixedSizeQueue<float, 50UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[4c]"fStorage"{CMQueueStorage<float, 50UL>="buffer"[196c]}}"fSpatialSampleTimestampBuffer"{CMFixedSizeQueue<double, 7UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[8c]"fStorage"{CMQueueStorage<double, 7UL>="buffer"[48c]}}"fSpatialSampleAggAccelBuffer"{CMFixedSizeQueue<CMVector<float, 3>, 7UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[16c]"fStorage"{CMQueueStorage<CMVector<float, 3>, 7UL>="buffer"[96c]}}"fCurrentPointTimestamp"d"fCurrentPointAggAccel"{CMVector<float, 3UL>="elements"}"fState"i"fPreviousState"i"fLastStateTransitionedFrom"i"fCurrentUpSample"{AggAccelSample="timestamp"d"aggAccel"{CMVector<float, 3UL>="elements"}}"fCurrentDownSample"{AggAccelSample="timestamp"d"aggAccel"{CMVector<float, 3UL>="elements"}}"fLastEndImpulseTimestamp"d"fEndImpulseTimestampHistory"{CMFixedSizeQueue<double, 3UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[8c]"fStorage"{CMQueueStorage<double, 3UL>="buffer"[16c]}}"fStartImpulseTimestampHistory"{CMFixedSizeQueue<double, 3UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[8c]"fStorage"{CMQueueStorage<double, 3UL>="buffer"[16c]}}"fHeadsetOrientation"{CMOQuaternion="elements"}"fStepModel"{StepModel="timeSinceLastStepSecRatio"[7d]"impulseDurationSecRatio"[7d]"deltaInertialZVelRatio"[7d]"thetaRollFaceDegreesRatio"[9d]"thetaPitchFaceDegreesRatio"[9d]"horizontalDisplacementRatio"[8d]"peakinessRatio"[2d]"bobbinessRatio"[2d]"timeSinceLastStepSecEdge"[7d]"impulseDurationSecEdge"[7d]"deltaInertialZVelEdge"[7d]"thetaRollFaceDegreesEdge"[9d]"thetaPitchFaceDegreesEdge"[9d]"horizontalDisplacementEdge"[8d]"peakinessEdge"[2d]"bobbinessEdge"[2d]"ratios"[8^d]"rightBinEdges"[8^d]}"fCallback"^?"fCallbackInfo"^v"fLastNotifiedTimeSec"d"fLogger"^{CMSpatialLogger}}"fCurrStepImpulse"{Impulse="start"d"end"d}"fHeadsetOrientationIsSet"B} _accessoryActivity;
i _motionContextState;
B _drawPositionOnStart;
{PdrResults="step"B"startImpulse"d"endImpulse"d"position"{CMVector<double, 2UL>="elements"}"stepsCount"i"directionOfTravelDegrees"f"speedMps"d"attitude"{CMOQuaternion="elements"}} _result;
f _totalSessionTime;
i _auxSampleCounter;
d _currentTime;
@"NSObject<OS_dispatch_queue>" _stepCountClientQueue;
@? _stepCountClientHandler;
@"NSObject<OS_dispatch_queue>" _pdrClientQueue;
@? _pdrClientHandler;
{CMVector<double, 2UL>="elements"} _prevPDRPosition;
@"NSObject<OS_dispatch_queue>" _motionContextClientQueue;
@? _motionContextClientHandler;
{unique_ptr<CMPdrMLModel, std::default_delete<CMPdrMLModel>>=""{?="__ptr_"^{CMPdrMLModel}}} hmlModel;
B _enableMLModel;
{unique_ptr<CMMotionContextSessionAnalyticsTracker, std::default_delete<CMMotionContextSessionAnalyticsTracker>>=""{?="__ptr_"^{CMMotionContextSessionAnalyticsTracker}}} _analyticsTracker;
f _distanceTravelledPerDVEvent;
i _stepCountPerDVEvent;
d _distractedViewingEnterTime;
{CMVector<double, 2UL>="elements"} _initialPosition;
f _initialHeadingDegrees;
B _inDVEvent;
i _lastTrackingDisableRoute;
```

## Class methods

```
+[CMMotionContextSession isAvailable];
```

## Instance methods

```
-[CMMotionContextSession init];
-[CMMotionContextSession stop];
-[CMMotionContextSession start];
-[CMMotionContextSession initWithOptions:];
-[CMMotionContextSession enableMLModel:];
-[CMMotionContextSession enterDistractedViewingSession:];
-[CMMotionContextSession exitDistractedViewingSession:];
-[CMMotionContextSession feedARKitWorldPoseWithTimestamp:pose:status:];
-[CMMotionContextSession feedAccessoryConfig:];
-[CMMotionContextSession feedAudioAccessoryIMU:];
-[CMMotionContextSession feedGPSLocationWithTimestamp:course:speed:latitude:longitude:horizontalAccuracy:];
-[CMMotionContextSession feedSourceDeviceIMU:];
-[CMMotionContextSession initLoggerWithPrefix:filePath:];
-[CMMotionContextSession notifyMotionContextClient:];
-[CMMotionContextSession notifyPdrClient:];
-[CMMotionContextSession notifyStepCountClient:];
-[CMMotionContextSession setAlgType:];
-[CMMotionContextSession setSpeedEstType:];
-[CMMotionContextSession setTrackingClientMode:];
-[CMMotionContextSession startMotionContextUpdatesToQueue:andHandler:];
-[CMMotionContextSession startPdrUpdatesToQueue:andHandler:];
-[CMMotionContextSession startStepCountUpdatesToQueue:andHandler:];
```
