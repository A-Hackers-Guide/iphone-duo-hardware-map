# `CMMotionManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 28 properties, 167 instance methods, 17 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (TB,R,N,GisSidebandSensorFusionAvailable) sidebandSensorFusionAvailable;
@property (TB,R,N,GisDisplayAngleAvailable) displayAngleAvailable;
@property (TB,R,N,GisDisplayGravityAvailable) displayGravityAvailable;
@property (TB,N) shouldResetStartingReference;
@property (TB,N) shouldDeliverUninitializedDeviceMotion;
@property (TB,R,N,GisPredictedDeviceMotionAvailable) predictedDeviceMotionAvailable;
@property (T@"CMAmbientPressureData",R) ambientPressureData;
@property (T@"CMAmbientPressureData",R) compensatedAmbientPressureData;
@property (TB,R,N,GisDeviceMotionLiteAvailable) isDeviceMotionLiteAvailable;
@property (Td,D,N) accelerometerUpdateInterval;
@property (TB,R,D,N,GisAccelerometerAvailable) accelerometerAvailable;
@property (TB,R,D,N,GisAccelerometerActive) accelerometerActive;
@property (T@"CMAccelerometerData",R,D) accelerometerData;
@property (Td,D,N) gyroUpdateInterval;
@property (TB,R,D,N,GisGyroAvailable) gyroAvailable;
@property (TB,R,D,N,GisGyroActive) gyroActive;
@property (T@"CMGyroData",R,D) gyroData;
@property (Td,N) magnetometerUpdateInterval;
@property (TB,R,N,GisMagnetometerAvailable) magnetometerAvailable;
@property (TB,R,N,GisMagnetometerActive) magnetometerActive;
@property (T@"CMMagnetometerData",R) magnetometerData;
@property (Td,D,N) deviceMotionUpdateInterval;
@property (TQ,R,D,N) attitudeReferenceFrame;
@property (T@"<CMBodyIdentifiable>",&,D,N) deviceMotionBody;
@property (TB,R,D,N,GisDeviceMotionAvailable) deviceMotionAvailable;
@property (TB,R,D,N,GisDeviceMotionActive) deviceMotionActive;
@property (T@"CMDeviceMotion",R,D) deviceMotion;
@property (TB,N) showsDeviceMovementDisplay;
```

## Class methods

```
+[CMMotionManager authorizationStatus];
+[CMMotionManager initialize];
+[CMMotionManager availableAttitudeReferenceFrames];
+[CMMotionManager availableAttitudeReferenceFramesNoSim];
+[CMMotionManager configureM7Activity:stepCounting:activityForceCodeTransition:stepCountingForceCodeTransition:threshold:onBodyDetection:ispMode:predictionInterval:logLevel:proactiveRevisitTime:];
+[CMMotionManager deviceMotionInitialized:];
+[CMMotionManager dummySelector:];
+[CMMotionManager dumpDb:toURL:onCompletion:];
+[CMMotionManager gyroCalibrationDatabaseGetBiasFit];
+[CMMotionManager gyroCalibrationDatabaseGetBiasFitAndEstimate:atTemperature:];
+[CMMotionManager hasRunMiniCal];
+[CMMotionManager northAlignedReferenceFrame:];
+[CMMotionManager setAllowInBackground:];
+[CMMotionManager setVirtualAlmondDevice:];
+[CMMotionManager startGyroMiniCalibration];
+[CMMotionManager supportsGyroMiniCalibration];
+[CMMotionManager virtualAlmondDevice];
```

## Instance methods

```
-[CMMotionManager connect];
-[CMMotionManager isGyroActive];
-[CMMotionManager readRawAmbientPressureSamplesFromDB:toQueue:where:withHandler:];
-[CMMotionManager setDeviceMotionUpdateInterval:];
-[CMMotionManager stopFactoryGyroUpdates];
-[CMMotionManager setDisplayAngleHandler:interval:];
-[CMMotionManager magnetometerUpdateInterval];
-[CMMotionManager setMotionThreadPriority:];
-[CMMotionManager accelerometerUpdateInterval];
-[CMMotionManager applyNorthReference:];
-[CMMotionManager deviceMotionUpdateInterval];
-[CMMotionManager setMagnetometerDataCallback:info:interval:];
-[CMMotionManager applyInitialReference:];
-[CMMotionManager setNotificationCallback:info:];
-[CMMotionManager showDeviceMovementDisplay];
-[CMMotionManager stopAmbientPressureUpdates];
-[CMMotionManager setDeviceMotionUpdateIntervalNoSim:];
-[CMMotionManager isMagnetometerAvailable];
-[CMMotionManager attitudeReferenceFrameNoSim];
-[CMMotionManager startDeviceMotionLiteFusedUpdatesForDeviceID:toQueue:withHandler:];
-[CMMotionManager setCompensatedAmbientPressureUpdateIntervalPrivate:];
-[CMMotionManager setMagnetometerUpdateIntervalPrivate:];
-[CMMotionManager isAccelerometerActive];
-[CMMotionManager shouldDeliverUninitializedDeviceMotion];
-[CMMotionManager gyttDataForSensorLocation:databasePath:error:];
-[CMMotionManager startCompensatedAmbientPressureUpdates];
-[CMMotionManager stopMagnetometerUpdates];
-[CMMotionManager isAccelerometerAvailable];
-[CMMotionManager setSidebandSensorFusionEnable:withSnoopHandler:];
-[CMMotionManager init];
-[CMMotionManager stopGyroUpdates];
-[CMMotionManager setGyroDataCallback:info:interval:];
-[CMMotionManager stopDeviceMotionUpdates];
-[CMMotionManager _stopDeviceMotionErrorUpdates];
-[CMMotionManager onCompensatedAmbientPressure:];
-[CMMotionManager ambientPressureData];
-[CMMotionManager onDeviceMotionForKeyboardMotion:];
-[CMMotionManager startDeviceMotionLiteUpdatesForDeviceID:usingConfiguration:toQueue:withFusedHandler:];
-[CMMotionManager startMagnetometerUpdatesToQueue:withHandler:];
-[CMMotionManager gyttNumTemperatures];
-[CMMotionManager setGyroUpdateIntervalPrivate:];
-[CMMotionManager startFactoryGyroUpdatesPrivateToQueue:forSensorLocation:atUpdateInterval:withHandler:residualHandler:];
-[CMMotionManager initPrivate];
-[CMMotionManager didBecomeActive:];
-[CMMotionManager startAccelerometerUpdatesToQueue:withHandler:];
-[CMMotionManager dealloc];
-[CMMotionManager gyroUpdateInterval];
-[CMMotionManager onAmbientPressure:];
-[CMMotionManager setShouldDeliverUninitializedDeviceMotion:];
-[CMMotionManager onDeviceMotion:];
-[CMMotionManager startAccelerometerUpdatesPrivateToQueue:withHandler:];
-[CMMotionManager startDeviceMotionUpdatesNoSimToQueue:withHandler:];
-[CMMotionManager onGyro:];
-[CMMotionManager isDeviceMotionAvailable];
-[CMMotionManager deviceMotionNoSim];
-[CMMotionManager startAmbientPressureUpdatesPrivateToQueue:withHandler:];
-[CMMotionManager sendDeviceMotionError:];
-[CMMotionManager compensatedAmbientPressureData];
-[CMMotionManager isGyroAvailable];
-[CMMotionManager showsDeviceMovementDisplay];
-[CMMotionManager stopDeviceMotionUpdatesForKeyboardMotionPrivate];
-[CMMotionManager isCompensatedAmbientPressureActive];
-[CMMotionManager setAmbientPressureUpdateInterval:];
-[CMMotionManager stopFactoryGyroUpdatesPrivate];
-[CMMotionManager willResignActive:];
-[CMMotionManager stopAmbientPressureUpdatesPrivate];
-[CMMotionManager isAmbientPressureAvailable];
-[CMMotionManager didBecomeActivePrivate:];
-[CMMotionManager computeNonlinearPRTTFromDB:where:];
-[CMMotionManager stopCompensatedAmbientPressureUpdatesPrivate];
-[CMMotionManager gyroData];
-[CMMotionManager _startDeviceMotionErrorUpdatesToQueue:withHandler:];
-[CMMotionManager startMagnetometerUpdates];
-[CMMotionManager startFactoryGyroUpdatesToQueue:forSensorLocation:atUpdateInterval:withHandler:];
-[CMMotionManager onFactoryGyroTemperature:];
-[CMMotionManager isDeviceMotionLiteAvailable];
-[CMMotionManager setMagnetometerUpdateInterval:];
-[CMMotionManager setCompensatedAmbientPressureUpdateInterval:];
-[CMMotionManager stopGyroUpdatesPrivate];
-[CMMotionManager _didUpdateBody:];
-[CMMotionManager compensatedAmbientPressureUpdateInterval];
-[CMMotionManager startFactoryGyroUpdatesToQueue:atUpdateInterval:withHandler:residualHandler:];
-[CMMotionManager startAmbientPressureUpdates];
-[CMMotionManager setUseAccelerometer:];
-[CMMotionManager startDeviceMotionUpdatesNoSimUsingReferenceFrame:toQueue:withHandler:];
-[CMMotionManager resetGYTTDatabaseForSensorLocation:databasePath:error:];
-[CMMotionManager stopGYTTCalibrationForSensorLocation:error:];
-[CMMotionManager startCompensatedAmbientPressureUpdatesPrivateToQueue:withHandler:];
-[CMMotionManager sendDeviceMotionHostGravityToKeyboard:];
-[CMMotionManager setDisplayGravityHandler:interval:];
-[CMMotionManager startGYTTCalibrationForSensorLocation:databasePath:error:];
-[CMMotionManager startFactoryGyroUpdatesToQueue:withHandler:];
-[CMMotionManager stopAccelerometerUpdates];
-[CMMotionManager deviceMotion];
-[CMMotionManager startDeviceMotionUpdatesUsingReferenceFrame:toQueue:withHandler:];
-[CMMotionManager gyttDictForSensorLocation:databasePath:error:];
-[CMMotionManager isDeviceMotionAvailableNoSim];
-[CMMotionManager predictedDeviceMotionAtTimestamp:error:];
-[CMMotionManager startDeviceMotionUpdatesNoSimUsingReferenceFrame:];
-[CMMotionManager startFactoryGyroUpdatesToQueue:forSensorLocation:withHandler:];
-[CMMotionManager isMagnetometerActive];
-[CMMotionManager setShouldResetStartingReference:];
-[CMMotionManager initUsing6AxisSensorFusion];
-[CMMotionManager setAmbientPressureUpdateIntervalPrivate:];
-[CMMotionManager deallocPrivate];
-[CMMotionManager rebuildGytt];
-[CMMotionManager onFactoryGyro:];
-[CMMotionManager startDeviceMotionUpdatesNoSim];
-[CMMotionManager startDeviceMotionUpdates];
-[CMMotionManager setDeviceMotionUpdateIntervalPrivate:];
-[CMMotionManager isSidebandSensorFusionAvailable];
-[CMMotionManager updateDeviceMotionMode];
-[CMMotionManager isDisplayAngleAvailable];
-[CMMotionManager setAccelerometerUpdateInterval:];
-[CMMotionManager setDeviceMotionBody:];
-[CMMotionManager gyttStringForSensorLocation:databasePath:error:];
-[CMMotionManager setGyroUpdateInterval:];
-[CMMotionManager startDeviceMotionUpdatesToQueue:withHandler:];
-[CMMotionManager startDeviceMotionUpdatesUsingReferenceFrame:];
-[CMMotionManager setSidebandSensorFusionEnable:measureLatency:withSnoopHandler:];
-[CMMotionManager startAmbientPressureUpdatesToQueue:withHandler:];
-[CMMotionManager startFactoryGyroUpdatesToQueue:forSensorLocation:atUpdateInterval:withHandler:residualHandler:];
-[CMMotionManager startGyroUpdatesPrivateToQueue:withHandler:];
-[CMMotionManager startMagnetometerUpdatesPrivateToQueue:withHandler:];
-[CMMotionManager onAccelerometer:];
-[CMMotionManager applyBodyTransform:];
-[CMMotionManager setSidebandSensorFusionEnable:measureLatency:imuIndex:withSnoopHandler:];
-[CMMotionManager startFactoryGyroUpdatesToQueue:atUpdateInterval:withHandler:];
-[CMMotionManager startDeviceMotionUpdatesForKeyboardMotionPrivateToQueue:withGravityDeltaThreshold:notificationFrequency:andHandler:];
-[CMMotionManager ambientPressureUpdateInterval];
-[CMMotionManager stopMagnetometerUpdatesPrivate];
-[CMMotionManager accelerometerData];
-[CMMotionManager stopDeviceMotionUpdatesPrivate];
-[CMMotionManager onMagnetometer:];
-[CMMotionManager shouldResetStartingReference];
-[CMMotionManager attitudeReferenceFrame];
-[CMMotionManager deviceMotionBody];
-[CMMotionManager setSidebandTimeSyncHandler:];
-[CMMotionManager setPowerConservationMode:];
-[CMMotionManager willResignActivePrivate:];
-[CMMotionManager magnetometerData];
-[CMMotionManager startGyroUpdatesToQueue:withHandler:];
-[CMMotionManager setShowsDeviceMovementDisplay:];
-[CMMotionManager useAccelerometer];
-[CMMotionManager isDeviceMotionActive];
-[CMMotionManager setAccelerometerUpdateIntervalPrivate:];
-[CMMotionManager startAccelerometerUpdates];
-[CMMotionManager stopAccelerometerUpdatesPrivate];
-[CMMotionManager startDeviceMotionUpdatesForKeyboardMotionToQueue:withGravityDeltaThreshold:sendFrequency:andHandler:];
-[CMMotionManager isAmbientPressureActive];
-[CMMotionManager setDeviceMotionCallback:info:interval:fsync:];
-[CMMotionManager startDeviceMotionUpdatesPrivateUsingReferenceFrame:toQueue:withHandler:];
-[CMMotionManager setShowsDeviceMovementDisplayPrivate:];
-[CMMotionManager startCompensatedAmbientPressureUpdatesToQueue:withHandler:];
-[CMMotionManager initUsingGyroOnlySensorFusion];
-[CMMotionManager stopDeviceMotionUpdatesNoSim];
-[CMMotionManager stopDeviceMotionUpdatesForKeyboardMotion];
-[CMMotionManager setSidebandSensorFusionEnable:];
-[CMMotionManager setAccelerometerDataCallback:info:interval:];
-[CMMotionManager startGyroUpdates];
-[CMMotionManager dismissDeviceMovementDisplay];
-[CMMotionManager gyttDataStructForSensorLocation:databasePath:error:];
-[CMMotionManager stopCompensatedAmbientPressureUpdates];
-[CMMotionManager isDisplayGravityAvailable];
-[CMMotionManager stopDeviceMotionLiteUpdatesForDeviceID:];
-[CMMotionManager isPredictedDeviceMotionAvailable];
-[CMMotionManager isDeviceMotionActiveNoSim];
```
