# `CMAudioAccessoryManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 17 properties, 105 instance methods, 3 class methods

## Instance variables

```
@ _internal;
{unique_ptr<CMResampleAccessoryDeviceMotion, std::default_delete<CMResampleAccessoryDeviceMotion>>=""{?="__ptr_"^{CMResampleAccessoryDeviceMotion}}} _resampleAccessoryDeviceMotion;
```

## Properties

```
@property (Td,D,N,S_setAudioAccessoryAccelerometerUpdateInterval:) _audioAccessoryAccelerometerUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryAccelerometerAvailable) _audioAccessoryAccelerometerAvailable;
@property (Td,D,N,S_setAudioAccessoryGyroUpdateInterval:) _audioAccessoryGyroUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryGyroAvailable) _audioAccessoryGyroAvailable;
@property (Td,D,N,S_setAudioAccessoryMagnetometerUpdateInterval:) _audioAccessoryMagnetometerUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryMagnetometerAvailable) _audioAccessoryMagnetometerAvailable;
@property (TB,R,D,N,G_isAudioAccessoryDeviceMotionAvailable) _audioAccessoryDeviceMotionAvailable;
@property (Td,D,N,S_setAudioAccessoryDeviceMotionUpdateInterval:) _audioAccessoryDeviceMotionUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryActivityAvailable) _audioAccessoryActivityAvailable;
@property (Td,D,N,S_setAudioAccessoryActivityUpdateInterval:) _audioAccessoryActivityUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessorySitStandAvailable) _audioAccessorySitStandAvailable;
@property (Td,D,N,S_setAudioAccessorySitStandUpdateInterval:) _audioAccessorySitStandUpdateInterval;
@property (Td,D,N,S_setAudioAccessoryHeartRateUpdateInterval:) _audioAccessoryHeartRateUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryHeartRateAvailable) _audioAccessoryHeartRateAvailable;
@property (TB,R,D,N,G_isAudioAccessoryPPGAvailable) _audioAccessoryPPGAvailable;
@property (Td,D,N,S_setAudioAccessoryInertialOdometryUpdateInterval:) _audioAccessoryInertialOdometryUpdateInterval;
@property (TB,R,D,N,G_isAudioAccessoryInertialOdometryAvailable) _audioAccessoryInertialOdometryAvailable;
```

## Class methods

```
+[CMAudioAccessoryManager _isAvailable];
+[CMAudioAccessoryManager _selectActiveAudioRouteForDeviceMotionWithBTAddress:modelID:];
+[CMAudioAccessoryManager _selectDeviceWithBTAddress:];
```

## Instance methods

```
-[CMAudioAccessoryManager init];
-[CMAudioAccessoryManager initPrivate];
-[CMAudioAccessoryManager dealloc];
-[CMAudioAccessoryManager deallocPrivate];
-[CMAudioAccessoryManager _audioAccessoryMagnetometerData];
-[CMAudioAccessoryManager _startAudioAccessoryHeartRateUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager onAudioAccessoryActivityStatus:];
-[CMAudioAccessoryManager _startAudioAccessoryInertialOdometryUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _audioAccessoryAccelerometerData];
-[CMAudioAccessoryManager _audioAccessoryAccelerometerUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryActivityUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryDeviceMotionUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryGyroData];
-[CMAudioAccessoryManager _audioAccessoryGyroUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryHeartRateUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryInertialOdometryUpdateInterval];
-[CMAudioAccessoryManager _audioAccessoryMagnetometerUpdateInterval];
-[CMAudioAccessoryManager _audioAccessorySitStandUpdateInterval];
-[CMAudioAccessoryManager _isAudioAccessoryAccelerometerAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryAccelerometerAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryActivityAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryActivityAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryDeviceMotionAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryDeviceMotionAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryGyroAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryGyroAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryHeartRateAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryHeartRateAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryInertialOdometryAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryInertialOdometryAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryMagnetometerAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryMagnetometerAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessoryPPGAvailable];
-[CMAudioAccessoryManager _isAudioAccessoryPPGAvailablePrivate];
-[CMAudioAccessoryManager _isAudioAccessorySitStandAvailable];
-[CMAudioAccessoryManager _isAudioAccessorySitStandAvailablePrivate];
-[CMAudioAccessoryManager _setAudioAccessoryAccelerometerUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryAccelerometerUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryActivityUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryActivityUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryDeviceMotionUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryDeviceMotionUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryGyroUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryGyroUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryHeartRateUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryHeartRateUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryInertialOdometryUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryInertialOdometryUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessoryMagnetometerUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessoryMagnetometerUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _setAudioAccessorySitStandUpdateInterval:];
-[CMAudioAccessoryManager _setAudioAccessorySitStandUpdateIntervalPrivate:];
-[CMAudioAccessoryManager _startAudioAccessoryAccelerometerUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryAccelerometerUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryActivityStatusUpdatesPrivate:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryActivityStatusUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryActivityUpdatesPrivate:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryActivityUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryDeviceMotionStatusUpdatesPrivate:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryDeviceMotionStatusUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryDeviceMotionUpdatesPrivate:lowLatencyMode:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryDeviceMotionUpdatesToQueue:lowLatencyMode:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryGyroUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryGyroUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryHeartRateUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryInertialOdometryUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryMagnetometerUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryMagnetometerUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryPPGUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessoryPPGUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessorySitStandUpdatesPrivateToQueue:withHandler:];
-[CMAudioAccessoryManager _startAudioAccessorySitStandUpdatesToQueue:withHandler:];
-[CMAudioAccessoryManager _stopAudioAccessoryAccelerometerUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryAccelerometerUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryActivityStatusUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryActivityStatusUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryActivityUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryActivityUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryDeviceMotionStatusUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryDeviceMotionStatusUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryDeviceMotionUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryDeviceMotionUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryGyroUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryGyroUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryHeartRateUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryHeartRateUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryInertialOdometryUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryInertialOdometryUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryMagnetometerUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryMagnetometerUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessoryPPGUpdates];
-[CMAudioAccessoryManager _stopAudioAccessoryPPGUpdatesPrivate];
-[CMAudioAccessoryManager _stopAudioAccessorySitStandUpdates];
-[CMAudioAccessoryManager _stopAudioAccessorySitStandUpdatesPrivate];
-[CMAudioAccessoryManager onAudioAccessoryAccelerometer:];
-[CMAudioAccessoryManager onAudioAccessoryActivity:];
-[CMAudioAccessoryManager onAudioAccessoryDeviceMotion:];
-[CMAudioAccessoryManager onAudioAccessoryDeviceMotionConfig:];
-[CMAudioAccessoryManager onAudioAccessoryDeviceMotionStatus:];
-[CMAudioAccessoryManager onAudioAccessoryGyro:];
-[CMAudioAccessoryManager onAudioAccessoryHeartRate:];
-[CMAudioAccessoryManager onAudioAccessoryInertialOdometry:];
-[CMAudioAccessoryManager onAudioAccessoryMagnetometer:];
-[CMAudioAccessoryManager onAudioAccessoryPPG:];
-[CMAudioAccessoryManager onAudioAccessorySitStand:];
```
