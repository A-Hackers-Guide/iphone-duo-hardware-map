# `CMCameraWorkoutSession`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 27 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CMCameraWorkoutLogger, std::default_delete<CMCameraWorkoutLogger>>=""{?="__ptr_"^{CMCameraWorkoutLogger}}} _logger;
@"CMAudioAccessoryManager" _audioAccessoryManager;
^{Dispatcher=^^?@} _deviceMotionDispatcher;
^{Dispatcher=^^?@} _accelerometerDispatcher;
^{Dispatcher=^^?@} _gyroDispatcher;
^{Dispatcher=^^?@} _gyroTemperatureDispatcher;
B _logAirpodsDM;
B _logDM;
B _logAccel;
B _logGyro;
@"NSObject<OS_dispatch_source>" _logCountersTimer;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _accelCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _gyroCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _dmCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _airpodsDmCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _skeletonCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _facePoseCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _watchActiveCalorieCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _watchBasalCalorieCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _watchHeartRateCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _heartRateReferenceCount;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} _fitnessMachineSampleCount;
```

## Instance methods

```
-[CMCameraWorkoutSession init];
-[CMCameraWorkoutSession stop];
-[CMCameraWorkoutSession dealloc];
-[CMCameraWorkoutSession start];
-[CMCameraWorkoutSession stats];
-[CMCameraWorkoutSession initWithOptions:];
-[CMCameraWorkoutSession _feedHeadAccessoryDeviceMotion:];
-[CMCameraWorkoutSession _feed2DSkeleton:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession _feed3DLiftedSkeleton:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession _feed3DRetargetedSkeleton:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession _feedAccel:];
-[CMCameraWorkoutSession _feedAccessoryConfig:];
-[CMCameraWorkoutSession _feedAccessoryInEarStatus:];
-[CMCameraWorkoutSession _feedDeviceMotion:];
-[CMCameraWorkoutSession _feedGyro:];
-[CMCameraWorkoutSession _feedGyroTemperature:];
-[CMCameraWorkoutSession feedBodyMetrics:];
-[CMCameraWorkoutSession feedFacePose:];
-[CMCameraWorkoutSession feedFitnessMachineSample:];
-[CMCameraWorkoutSession feedHeartRateReference:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession feedSkeleton:];
-[CMCameraWorkoutSession feedWatchActiveCalories:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession feedWatchBasalCalories:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession feedWatchHeartRate:confidence:localMachtime:globalMachtime:];
-[CMCameraWorkoutSession feedWorkoutEvent:];
-[CMCameraWorkoutSession flushMsl];
-[CMCameraWorkoutSession logCounters];
```
