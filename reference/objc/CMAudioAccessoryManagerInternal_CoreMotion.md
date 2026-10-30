# `CMAudioAccessoryManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 59 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} fSampleLock;
^{Dispatcher=^^?@} fAudioAccessoryAccelerometerDispatcher;
d fAudioAccessoryAccelerometerUpdateInterval;
@? fAudioAccessoryAccelerometerHandler;
@"NSOperationQueue" fAudioAccessoryAccelerometerQueue;
{Sample="timestamp"d"acceleration"{?="x"f"y"f"z"f}"sensorTime"Q"sequenceNumber"S"temperature"f} fLatestAudioAccessoryAccelerometerSample;
^{Dispatcher=^^?@} fAudioAccessoryGyroDispatcher;
d fAudioAccessoryGyroUpdateInterval;
@? fAudioAccessoryGyroHandler;
@"NSOperationQueue" fAudioAccessoryGyroQueue;
{Sample="timestamp"d"gyro"{?="x"f"y"f"z"f}"sensorTime"Q"sequenceNumber"S"temperature"f} fLatestAudioAccessoryGyroSample;
^{Dispatcher=^^?@} fAudioAccessoryMagnetometerDispatcher;
d fAudioAccessoryMagnetometerUpdateInterval;
@? fAudioAccessoryMagnetometerHandler;
@"NSOperationQueue" fAudioAccessoryMagnetometerQueue;
{Sample="timestamp"d"magneticField"{?="x"f"y"f"z"f}"sensorTime"Q"sequenceNumber"S"temperature"f} fLatestAudioAccessoryMagnetometerSample;
^{Dispatcher=^^?@} fAudioAccessoryDeviceMotionDispatcher;
^{Dispatcher=^^?@} fAudioAccessoryDeviceMotionConfigDispatcher;
d fAudioAccessoryDeviceMotionUpdateInterval;
@? fAudioAccessoryDeviceMotionHandler;
@"NSOperationQueue" fAudioAccessoryDeviceMotionQueue;
{?="w"d"x"d"y"d"z"d} fBodyFrameRotationFromSensorToDefault;
^{Dispatcher=^^?@} fAudioAccessoryDeviceMotionStatusDispatcher;
@? fAudioAccessoryDeviceMotionStatusHandler;
@"NSOperationQueue" fAudioAccessoryDeviceMotionStatusQueue;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fAudioAccessoryActivityDispatcher;
d fAudioAccessoryActivityUpdateInterval;
@? fAudioAccessoryActivityHandler;
@"NSOperationQueue" fAudioAccessoryActivityQueue;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fAudioAccessoryActivityStatusDispatcher;
@? fAudioAccessoryActivityStatusHandler;
@"NSOperationQueue" fAudioAccessoryActivityStatusQueue;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fAudioAccessorySitStandDispatcher;
d fAudioAccessorySitStandUpdateInterval;
@? fAudioAccessorySitStandHandler;
@"NSOperationQueue" fAudioAccessorySitStandQueue;
^{Dispatcher=^^?@} fAudioAccessoryHeartRateDispatcher;
d fAudioAccessoryHeartRateUpdateInterval;
@? fAudioAccessoryHeartRateHandler;
@"NSOperationQueue" fAudioAccessoryHeartRateQueue;
{Sample="timestamp"d"heartRate"I"confidence"f"sensorTime"Q"sequenceNumber"I} fLatestAudioAccessoryHeartRateSample;
^{Dispatcher=^^?@} fAudioAccessoryInertialOdometryDispatcher;
d fAudioAccessoryInertialOdometryUpdateInterval;
@? fAudioAccessoryInertialOdometryHandler;
@"NSOperationQueue" fAudioAccessoryInertialOdometryQueue;
{InertialOdometryReport="timestamp"Q"position"[3f]"deltaVelocityCumSum"[3f]"timestampPositionRollOver"Q"timestampVelocityRollOver"Q"timestampDeltaPositionUnavailable"[3Q]"timestampUninitialized"Q"attitude"[4f]"rotationArbitraryToMagneticNorth"f"displacingState"C"displacementUncertainty"[3f]"side"i"timestampSecs"d"continuousTimestampSecs"d"buffered"B} fLatestAudioAccessoryInertialOdometrySample;
^{Dispatcher=^^?@} fAudioAccessoryPPGDispatcher;
@? fAudioAccessoryPPGHandler;
@"NSOperationQueue" fAudioAccessoryPPGQueue;
{Sample="timestamp"d"sensorTime"Q"frameNum"C"error"C"dark0"[3C]"light0"[3C]"dark1"[3C]"dark2"[3C]"light1"[3C]"dark3"[3C]"rxGain"[2C]"ledCurrent"[2C]} fLatestAudioAccessoryPPGSample;
B fAudioAccessoryAccelerometerAvailable;
B fAudioAccessoryGyroAvailable;
B fAudioAccessoryMagnetometerAvailable;
B fAudioAccessoryDeviceMotionAvailable;
B fAudioAccessoryActivityAvailable;
B fAudioAccessorySitStandAvailable;
B fAudioAccessoryHeartRateAvailable;
B fAudioAccessoryInertialOdometryAvailable;
B fAudioAccessoryPPGAvailable;
```

## Instance methods

```
-[CMAudioAccessoryManagerInternal init];
-[CMAudioAccessoryManagerInternal dealloc];
```
