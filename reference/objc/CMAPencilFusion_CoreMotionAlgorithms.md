# `CMAPencilFusion`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 43 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CMABarrelRoll::CMABarrelRollService, std::default_delete<CMABarrelRoll::CMABarrelRollService>>=""{?="__ptr_"^{CMABarrelRollService}}} _barrelRollService;
B _running;
B _verboseLoggingEnabled;
B _mslEnabled;
B _preciseTipPositionLoggingEnabled;
@"NSMutableArray" _estimations;
Q _currentEstimationUpdateIndex;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _handlerQueue;
@? _handler;
@"NSUserDefaults" _defaults;
```

## Properties

```
@property (TB,N,GisRunning,V_running) running;
@property (T@"NSMutableArray",&,N,V_estimations) estimations;
@property (TQ,N,V_currentEstimationUpdateIndex) currentEstimationUpdateIndex;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_handlerQueue) handlerQueue;
@property (T@?,C,N,V_handler) handler;
@property (T@"NSUserDefaults",&,N,V_defaults) defaults;
@property (TB,N,V_verboseLoggingEnabled) verboseLoggingEnabled;
@property (TB,N,V_mslEnabled) mslEnabled;
@property (TB,N,V_preciseTipPositionLoggingEnabled) preciseTipPositionLoggingEnabled;
@property (T@"CMAPencilFusionResult",R,N) currentEstimation;
```

## Instance methods

```
-[CMAPencilFusion setDefaults:];
-[CMAPencilFusion isRunning];
-[CMAPencilFusion defaults];
-[CMAPencilFusion observeValueForKeyPath:ofObject:change:context:];
-[CMAPencilFusion init];
-[CMAPencilFusion dealloc];
-[CMAPencilFusion setHandler:];
-[CMAPencilFusion queue];
-[CMAPencilFusion setRunning:];
-[CMAPencilFusion setHandlerQueue:];
-[CMAPencilFusion handler];
-[CMAPencilFusion verboseLoggingEnabled];
-[CMAPencilFusion handlerQueue];
-[CMAPencilFusion setQueue:];
-[CMAPencilFusion setVerboseLoggingEnabled:];
-[CMAPencilFusion setEstimations:];
-[CMAPencilFusion currentEstimation];
-[CMAPencilFusion currentEstimationUpdateIndex];
-[CMAPencilFusion estimations];
-[CMAPencilFusion flushMSL];
-[CMAPencilFusion logHostDeviceMotionQuaternion:rotationRate:acceleration:timestamp:];
-[CMAPencilFusion logPencilDeviceMotionQuaternion:rotationRate:acceleration:gyroBias:temperatureGyroBias:temperatureGyro:status:sensorTime:timestamp:];
-[CMAPencilFusion logPencilFusionResult:];
-[CMAPencilFusion logTouchAltitudeAngle:altitudeAngleConfidence:azimuthAngle:azimuthAngleConfidence:position:positionConfidence:timestamp:];
-[CMAPencilFusion mslEnabled];
-[CMAPencilFusion preciseTipPositionLoggingEnabled];
-[CMAPencilFusion readUserDefaults];
-[CMAPencilFusion sendPencilGyroBiasAxisStatistics:axis:];
-[CMAPencilFusion sendPencilSensorContactTypeStatistics:contactType:];
-[CMAPencilFusion sendPencilStatistics];
-[CMAPencilFusion sendPencilTimingStatistics:];
-[CMAPencilFusion setCurrentEstimationUpdateIndex:];
-[CMAPencilFusion setMslEnabled:];
-[CMAPencilFusion setPreciseTipPositionLoggingEnabled:];
-[CMAPencilFusion startPencilFusionUpdatesToQueue:withHandler:];
-[CMAPencilFusion startUserDefaults];
-[CMAPencilFusion stopPencilFusionUpdates];
-[CMAPencilFusion stopPencilFusionUpdatesPrivate];
-[CMAPencilFusion stopUserDefaults];
-[CMAPencilFusion updateEstimationsWithRealValuesWithQuaternion:timestamp:];
-[CMAPencilFusion updateHostDeviceMotionQuaternion:rotationRate:acceleration:timestamp:];
-[CMAPencilFusion updatePencilDeviceMotionPayload:];
-[CMAPencilFusion updateTouchAltitudeAngle:altitudeAngleConfidence:azimuthAngle:azimuthAngleConfidence:position:positionConfidence:timestamp:];
```
