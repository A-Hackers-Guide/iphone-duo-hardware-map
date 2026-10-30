# `CMMotionManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 110 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} fSampleLock;
^{Dispatcher=^^?@} fAccelerometerDispatcher;
d fAccelerometerUpdateInterval;
@? fAccelerometerHandler;
@"NSOperationQueue" fAccelerometerQueue;
d fLastAccelerometerNotificationTimestamp;
{Sample="timestamp"d"acceleration"{?="x"f"y"f"z"f}} fLatestAccelerometerSample;
^{Dispatcher=^^?@} fAmbientPressureDispatcher;
d fAmbientPressureUpdateInterval;
@? fAmbientPressureHandler;
@"NSOperationQueue" fAmbientPressureQueue;
d fLastAmbientPressureNotificationTimestamp;
{Sample="timestamp"d"pressureData"{?="pressure"f"temperature"f}} fLatestAmbientPressureSample;
^{Dispatcher=^^?@} fCompensatedAmbientPressureDispatcher;
d fCompensatedAmbientPressureUpdateInterval;
@? fCompensatedAmbientPressureHandler;
@"NSOperationQueue" fCompensatedAmbientPressureQueue;
d fLastCompensatedAmbientPressureNotificationTimestamp;
{Sample="timestamp"d"pressureData"{?="pressure"f"temperature"f}} fLatestCompensatedAmbientPressureSample;
^{Dispatcher=^^?@} fGyroDispatcher;
d fGyroUpdateInterval;
@? fGyroHandler;
@"NSOperationQueue" fGyroQueue;
d fLastGyroNotificationTimestamp;
{Sample="timestamp"d"rotationRate"{?="x"f"y"f"z"f}"sampleNum"S"fsync"B} fLatestGyroSample;
^{Dispatcher=^^?@} fDeviceMotionDispatcher;
@"<CMBodyIdentifiable>" fDeviceMotionBody;
@"CMBodyToken" fDeviceMotionBodyToken;
{CMBodyTransform="fTransform"{optional<CMBodyTransform::Transform>=""(?="__null_state_"c"__val_"{Transform="qFixedRotation"{CMOQuaternion="elements"}"angleScaleAxis"{CMVector<float, 3UL>="elements"}})"__engaged_"B}"fUUID"@"NSUUID""fInterfaceAngle"f} fBodyTransform;
d fDeviceMotionUpdateInterval;
@? fDeviceMotionHandler;
@"NSOperationQueue" fDeviceMotionQueue;
d fLastDeviceMotionNotificationTimestamp;
i fDeviceMotionMode;
Q fAttitudeReferenceFrame;
B fCompassCalibrationHud;
B fIsCompassCalibrated;
B fIsUsingCalibratedCompass;
B fHaveSentDeviceRequiresMovementError;
B fHaveSentTrueNorthUnavailableError;
d fDeviceMotionStartTimestamp;
{?="w"d"x"d"y"d"z"d} fInitialReferenceRotation;
B fIsInitialReferenceAvailable;
^{Dispatcher=^^?@} fMagnetometerDispatcher;
d fMagnetometerUpdateInterval;
@? fMagnetometerHandler;
@"NSOperationQueue" fMagnetometerQueue;
d fLastMagnetometerNotificationTimestamp;
{Sample="timestamp"d"magneticField"{?="x"f"y"f"z"f}"temperature"f} fLatestMagnetometerSample;
B fShowsDeviceMovementDisplay;
^{Dispatcher=^^?@} fPrivateAccelerometerDataDispatcher;
^? fPrivateAccelerometerDataCallback;
^v fPrivateAccelerometerDataCallbackInfo;
^{Dispatcher=^^?@} fPrivateGyroDataDispatcher;
^? fPrivateGyroDataCallback;
^v fPrivateGyroDataCallbackInfo;
^{Dispatcher=^^?@} fPrivateMagnetometerDataDispatcher;
^? fPrivateMagnetometerDataCallback;
^v fPrivateMagnetometerDataCallbackInfo;
^{Dispatcher=^^?@} fPrivateDeviceMotionDispatcher;
^? fPrivateDeviceMotionCallback;
^v fPrivateDeviceMotionCallbackInfo;
B fPrivateDeviceMotionUse9Axis;
B fPrivateUseAccelerometer;
B fPrivateDeviceMotionNoSimClient;
^v fConnection;
@"NSObject<OS_dispatch_queue>" fConnectionQueue;
B fSidebandSensorFusionEnabled;
B fSidebandSensorFusionLatency;
B fSidebandSensorFusionSnoop;
{unique_ptr<CLIspDataVisitor, std::default_delete<CLIspDataVisitor>>=""{?="__ptr_"^{CLIspDataVisitor}}} fSidebandVisitor;
{unique_ptr<CLDisplayGravityService, std::default_delete<CLDisplayGravityService>>=""{?="__ptr_"^{CLDisplayGravityService}}} fDisplayGravityService;
{unique_ptr<CMDisplayAngleService, std::default_delete<CMDisplayAngleService>>=""{?="__ptr_"^{CMDisplayAngleService}}} fDisplayAngleService;
B fShouldResetStartingReference;
B fShouldDeliverUninitializedDeviceMotion;
i fPrivatePowerConservationMode;
^? fPrivateNotificationCallback;
^v fPrivateNotificationCallbackInfo;
^{Dispatcher=^^?@} fPrivateDeviceMotionSensorStatusDispatcher;
@? fDeviceMotionErrorHandler;
@"NSOperationQueue" fDeviceMotionErrorQueue;
B fIsApplicationActive;
{unique_ptr<CLDeviceMotionLiteService, std::default_delete<CLDeviceMotionLiteService>>=""{?="__ptr_"^{CLDeviceMotionLiteService}}} fDeviceMotionLiteService;
{unique_ptr<CMMotionManagerStatsCollector, std::default_delete<CMMotionManagerStatsCollector>>=""{?="__ptr_"^{CMMotionManagerStatsCollector}}} fMotionManagerStatsCollector;
^{Dispatcher=^^?@} fFactoryGyroDispatcher;
d fFactoryGyroUpdateInterval;
^{Dispatcher=^^?@} fFactoryGyroTemperatureDispatcher;
d fFactoryGyroTemperatureUpdateInterval;
I fFactoryGyroLocationID;
{unique_ptr<CLFactoryGYTTCalibration, std::default_delete<CLFactoryGYTTCalibration>>=""{?="__ptr_"^{CLFactoryGYTTCalibration}}} fFactoryGYTTCalibrator;
@? fFactoryGyroHandler;
@"NSOperationQueue" fFactoryGyroQueue;
d fLastFactoryGyroNotificationTimestamp;
f fLastFactoryGyroTemperature;
B fFactoryGyroFitComputed;
{NonlinearGyroBiasFit="fType"C"fImuIndex"C"fPadding"[2C]"fFits"[8{LinearFit="fSlope"[3f]"fIntercept"[3f]}]"fTemperatures"[7f]"fOverlap"f"fError"[3[18C]]} fFactoryGyroNonlinearGyroBiasFit;
{LinearFit="fSlope"[3f]"fIntercept"[3f]} fFactoryGyroLinearGyroBiasFit;
@? fKeyboardMotionHandler;
@"NSOperationQueue" fKeyboardMotionQueue;
^{Dispatcher=^^?@} fKeyboardMotionDMDispatcher;
d fKeyboardMotionTimestampGravityHidReportPrev;
{CMVector<float, 3UL>="elements"} fKeyboardMotionGravityHIDReportPrev;
f fKeyboardMotionGravityDeltaThreshold;
f fKeyboardMotionGravityNotificationFrequency;
^{Dispatcher=^^?@} fKeyboardMotionDispatcher;
@"NSObject<OS_dispatch_semaphore>" fLocalTimeSyncSemaphore;
@"NSOperationQueue" _fDeviceMotionLiteClientQueue;
@? _fDeviceMotionLiteFusedHandler;
@"NSString" _fDeviceMotionLitePhysicalDeviceID;
@? _fDisplayGravityHandler;
```

## Properties

```
@property (T@"NSOperationQueue",&,N,V_fDeviceMotionLiteClientQueue) fDeviceMotionLiteClientQueue;
@property (T@?,C,N,V_fDeviceMotionLiteFusedHandler) fDeviceMotionLiteFusedHandler;
@property (T@"NSString",&,N,V_fDeviceMotionLitePhysicalDeviceID) fDeviceMotionLitePhysicalDeviceID;
@property (T@?,C,N,V_fDisplayGravityHandler) fDisplayGravityHandler;
```

## Instance methods

```
-[CMMotionManagerInternal init];
-[CMMotionManagerInternal dealloc];
-[CMMotionManagerInternal fDisplayGravityHandler];
-[CMMotionManagerInternal fDeviceMotionLiteClientQueue];
-[CMMotionManagerInternal setFDeviceMotionLiteFusedHandler:];
-[CMMotionManagerInternal setFDeviceMotionLiteClientQueue:];
-[CMMotionManagerInternal teardownPrivate];
-[CMMotionManagerInternal setFDeviceMotionLitePhysicalDeviceID:];
-[CMMotionManagerInternal setFDisplayGravityHandler:];
-[CMMotionManagerInternal fDeviceMotionLitePhysicalDeviceID];
-[CMMotionManagerInternal fDeviceMotionLiteFusedHandler];
```
