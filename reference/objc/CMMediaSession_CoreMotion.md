# `CMMediaSession`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMDistributedSensingDelegate`
- 106 instance variables, 11 properties, 68 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<CMHeadTrackingService, std::default_delete<CMHeadTrackingService>>=""{?="__ptr_"^{CMHeadTrackingService}}} _headTrackingService;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _deviceMotionDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionConfigDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionInEarStatusDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryMonitorDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryActivityDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryActivityStatusDispatcher;
@"NSObject<OS_dispatch_queue>" _clientQueue;
@? _clientHandler;
B _started;
i _clientMode;
i _scheme;
{CMOQuaternion="elements"} _q_bf;
B _useHeadToHeadsetTransformationEstimator;
B _disable2IMU;
d _lidAngle;
i _displayCount;
i _maxDisplayCount;
i _schemePrev;
B _simulateCameraOnOffRequest;
B _simulatePeriodicCameraBurst;
B _hasUserDefaultTrackingScheme;
B _bypassCameraController;
B _bypassWalkingAwayDistractedViewing;
{UnTimesyncedAuxSampleHelper="totalUnsyncedSamples"I"totalUnsyncedOutlierSamples"I"auxAndSrcSensorTimeOffset"d"auxAndSrcSensorTimeOffsetBuffer"{CMFixedSizeQueue<double, 10UL>="fHeadAndSize"{?="fHead"S"fSize"S}"fCapacity"I"fBuffer"[8c]"fStorage"{CMQueueStorage<double, 10UL>="buffer"[72c]}}} _unsyncedAuxHelper;
{unique_ptr<CMMediaSessionAnalyticsTracker, std::default_delete<CMMediaSessionAnalyticsTracker>>=""{?="__ptr_"^{CMMediaSessionAnalyticsTracker}}} _analyticsTracker;
i _previousBTZState;
d _lastInBTZTime;
i _previousMotionActivityType;
i _previousHeadphoneMotionActivityType;
d _lastAccessoryDMTime;
i _previousTracking1IMU;
B _previousCTState;
B _previousCTBodyTurnState;
B _previousHeadTurnState;
d _lastExitCTTime;
f _lastAngleBetweenCurrentBoresightToDefault;
B _previousTrackingEnabled;
d _lastDistractedViewingStartTime;
d _lastDistractedViewingEndTime;
B _previousSrcMoving;
B _previousAuxMoving;
B _previousSteadyStatePedestrian;
B _previousKeepBoresightCentered;
i _lastTrackingDisableRoute;
{CAFwdPredictorError="timestamp"Q"errorRad"f} _lastCAFwdPredictorError;
i _analyticsClientMode;
{AudioAccessorySample="auxDM"{?="quaternion"{CMOQuaternion="elements"}"rotationRate"{CMVector<float, 3UL>="elements"}"biasCovariance"{CMVector<float, 3UL>="elements"}"userAcceleration"{CMVector<float, 3UL>="elements"}"status"{Status="bits"S}}"sensorTime"Q"timestamp"d"arrivalTimestamp"d"filteredAcceleration"{CMVector<float, 3UL>="elements"}"quiescentNoise"f"quiescentMode"i"sequenceNumber"I"sensorLocation"i"timeSyncStatus"i"btcTimestamp"Q"sampleLatency"d"gyroBias"[3f]"isGyroBiasValid"B"activity"C"isActivityValid"B"isInEar"B"sourceTimestampToMachContinuous"d"sourceTimestampToCFAbsoluteTime"d"isIEDEnabled"B"isVirtual"B"virtualProductID"I} _lastAudioAccessorySample;
Q _lastAccessoryTimestamp;
Q _lastSourceTimestampMicroSeconds;
Q _lastStateTimestamp;
Q _lastPresentationTimestamp;
d _lastListenerOrientationGenerationTimestampSeconds;
B _trackingEstimatesStagnated;
B _logForReplay;
d _printPoseTimer;
B _enableJBLThreshold;
B _verboseLogging;
d _accessorySampleTimer;
i _accessorySamplesPerSecond;
@"CMMotionActivityManager" _activityManager;
@"NSOperationQueue" _activityQueue;
{unique_ptr<CLSettings, std::default_delete<CLSettings>>=""{?="__ptr_"^{CLSettings}}} _motionSettings;
@"NSUserDefaults" _motionDefaults;
d _minQuiescentPeriodForBTZ;
i _notify50HzPoseDecimator;
Q _lastFacePoseTimestampUs;
Q _anchorUpdateIntervalUs;
f _cameraControllerPeriodicBurstPulseWidthSeconds;
f _cameraControllerPeriodicBurstTotalWidthSeconds;
f _correspondenceThresholdDegrees;
d _sessionStartTime;
d _firstAccessoryDMTime;
d _firstValidPoseTime;
d _lastTimesyncLostTime;
{unique_ptr<CMSpatialLogger, std::default_delete<CMSpatialLogger>>=""{?="__ptr_"^{CMSpatialLogger}}} _logger;
i _inEarStatus;
B _inEarStatusGatingEnabled;
i _jitterBufferLevelNotificationToken;
@"NSObject<OS_dispatch_source>" _jitterBufferLevelInitialUpdateTimer;
S _jitterBufferLevel;
S _jitterBufferLevelThreshold;
B _sitStandDetectorEnabled;
B _userSettingFwdPredictorEnabled;
f _renderingOverheadSeconds;
B _motionContextSessonEnabled;
B _humanMotionLearningModelEnabled;
@"CMMotionContextSession" _mcSession;
B _userSettingBypassAmbienceBedForE2ELatencyTesting;
{CMOQuaternion="elements"} _cameraToSourceAlignment;
{CMVector<float, 3UL>="elements"} _offsetFromDisplayCenterToFrontCameraInSourceFrameMeters;
Q _lastRequestingCameraTimestampUs;
Q _lastResetCamControllerTimersTimestampUs;
Q _firstFacePoseInCameraRequestTimestampUs;
@"CMDeviceOrientationManager" _deviceOrientationManager;
i _orientationCounter;
f _defaultLidAngleDeg;
B _forceDefaultLidAngle;
B _requestingCameraOn;
B _returnDefaultPose;
B _returnRandomPose;
B _alwaysNotify50HzPose;
I _accessoryIMUSampleRate;
f _prevAmbienceBedRoll;
@"NSString" _mcLogPath;
```

## Properties

```
@property (TI,V_accessoryIMUSampleRate) accessoryIMUSampleRate;
@property (Tf,V_prevAmbienceBedRoll) prevAmbienceBedRoll;
@property (TB,V_returnDefaultPose) returnDefaultPose;
@property (TB,V_returnRandomPose) returnRandomPose;
@property (TB,V_alwaysNotify50HzPose) alwaysNotify50HzPose;
@property (T@"NSString",C,V_mcLogPath) mcLogPath;
@property (TB,R,N,GisRequestingCameraOn,V_requestingCameraOn) requestingCameraOn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CMMediaSession _isAvailable];
+[CMMediaSession defaultFaceToDevicePitchAngle];
```

## Instance methods

```
-[CMMediaSession _initWithOptions:];
-[CMMediaSession _stop];
-[CMMediaSession _reset];
-[CMMediaSession observeValueForKeyPath:ofObject:change:context:];
-[CMMediaSession _start];
-[CMMediaSession init];
-[CMMediaSession dealloc];
-[CMMediaSession _logEvent:];
-[CMMediaSession _updateMinQuiescentPeriodForBTZ];
-[CMMediaSession shouldHeadTrackWithInEarStatus:];
-[CMMediaSession _startDefaultsPreferenceUpdater];
-[CMMediaSession _createPoseFromListenerOrientation:Pose:];
-[CMMediaSession _disableLoggingForReplay];
-[CMMediaSession _disallowOpportunisticAnchorTrackingForFTClients:clientMode:];
-[CMMediaSession _enableLoggingForReplayWithFilenamePrefix:filePath:];
-[CMMediaSession _feedAccessoryActivity:];
-[CMMediaSession _feedAccessoryActivityStatus:];
-[CMMediaSession _feedAccessoryConfig:];
-[CMMediaSession _feedAccessoryDeviceMotion:];
-[CMMediaSession _feedAccessoryInEarStatus:];
-[CMMediaSession _feedActiveAudioRouteChangedEvent];
-[CMMediaSession _feedAdaptiveLatencyJitterBufferLevel];
-[CMMediaSession _feedDisplayCount:];
-[CMMediaSession _feedFaceKitData:timestamp:];
-[CMMediaSession _feedLidAngle:];
-[CMMediaSession _feedPoseAnchor:facePoseError:lidAngleDeg:];
-[CMMediaSession _feedPredictorEstimates];
-[CMMediaSession _feedScreenUnlockedEvent:];
-[CMMediaSession _feedSourceDeviceIMU:];
-[CMMediaSession _getAuxSampleTimestamp:currentTime:];
-[CMMediaSession _getLastAudioAccessorySample];
-[CMMediaSession _mapCMMediaSessionClientModeToRelDMClientMode:];
-[CMMediaSession _notifyClientHandler];
-[CMMediaSession _readFrontCameraToDisplayCenterOffset];
-[CMMediaSession _resolvedLidAngleDeg:];
-[CMMediaSession _setFixedTransforms:];
-[CMMediaSession _setTrackingSchemeInternal:];
-[CMMediaSession _startHeadTracking];
-[CMMediaSession _startJitterBufferLevelMonitor];
-[CMMediaSession _startJitterBufferLevelRetryTimer];
-[CMMediaSession _startPoseUpdatesToQueue:andHandler:];
-[CMMediaSession _stopDefaultsPreferenceUpdater];
-[CMMediaSession _stopHeadTracking];
-[CMMediaSession _stopJitterBufferLevelMonitor];
-[CMMediaSession _stopJitterBufferLevelRetryTimer];
-[CMMediaSession _triggerUserInteractedWithDeviceEvent];
-[CMMediaSession _updateAnchorIntervalSettings];
-[CMMediaSession _updateCameraControllerParameters];
-[CMMediaSession _updateClientMode:];
-[CMMediaSession _updateTrackingScheme:];
-[CMMediaSession _updateTrackingSchemeSettings];
-[CMMediaSession _updateUseFwdPredictionUserSettings];
-[CMMediaSession _updateUseHeadToHeadsetTransformationEstimator];
-[CMMediaSession _updateUserSettings];
-[CMMediaSession accessoryIMUSampleRate];
-[CMMediaSession alwaysNotify50HzPose];
-[CMMediaSession feedPoseAnchorWithAttitude:position:lidAngleDeg:numberOfDetectedFaces:timestampUs:];
-[CMMediaSession isRequestingCameraOn];
-[CMMediaSession mcLogPath];
-[CMMediaSession prevAmbienceBedRoll];
-[CMMediaSession returnDefaultPose];
-[CMMediaSession returnRandomPose];
-[CMMediaSession setAccessoryIMUSampleRate:];
-[CMMediaSession setAlwaysNotify50HzPose:];
-[CMMediaSession setMcLogPath:];
-[CMMediaSession setPrevAmbienceBedRoll:];
-[CMMediaSession setReturnDefaultPose:];
-[CMMediaSession setReturnRandomPose:];
```
