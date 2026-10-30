# `FigCoreMotionDelegate`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 0 properties, 29 instance methods, 0 class methods

## Instance variables

```
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} ringMutex;
@"CMMotionManager" motionManager;
B manageFusedMotion;
B manageAccel;
B manageGravity;
i accelRingIndex;
[256f] accelRingX;
[256f] accelRingY;
[256f] accelRingZ;
[256d] accelRingTime;
i fusedRingIndex;
[256d] fusedRingTime;
[256B] fusedRingDoingBiasEstimation;
[256{?="x"f"y"f"z"f}] fusedRingAccel;
[256{?="w"d"x"d"y"d"z"d}] fusedRingQuaternion;
[256{?="x"f"y"f"z"f}] fusedRingPosition;
^{OpaqueFigSemaphore=} dataSemaphore;
d latestMotionDataTime;
d latestGravityDataTime;
B copyingAllData;
d dLatestFusedMotionCopied;
d dLatestTimestamp;
d dGyroUpdateInterval;
d dStartOfLogging;
{?="w"d"x"d"y"d"z"d} previousQuaternion;
{?="w"d"x"d"y"d"z"d} currentQuaternion;
B computingPosition;
{?="timestamp"d"x"f"y"f"z"f} position;
{?="timestamp"d"x"f"y"f"z"f} velocity;
```

## Instance methods

```
-[FigCoreMotionDelegate init];
-[FigCoreMotionDelegate dealloc];
-[FigCoreMotionDelegate didUpdatePositionWithTimeStamp:];
-[FigCoreMotionDelegate managingGravity];
-[FigCoreMotionDelegate copyAllFusedMotionData];
-[FigCoreMotionDelegate copyFusedMotionData:endTime:timeoutValue:errOut:];
-[FigCoreMotionDelegate copyNewFusedMotionData];
-[FigCoreMotionDelegate didUpdateAcceleration:time:];
-[FigCoreMotionDelegate didUpdateFusedMotionWithDeviceMotion:time:ifsync:];
-[FigCoreMotionDelegate didUpdateGravity:time:];
-[FigCoreMotionDelegate didUpdatePositionWithAcceleration:forTimeStamp:];
-[FigCoreMotionDelegate didUpdateVelocityWithAcceleration:forTimeStamp:];
-[FigCoreMotionDelegate getCurrentAttitudeRoll:pitch:yaw:];
-[FigCoreMotionDelegate getCurrentDeltaAttitudeRoll:pitch:yaw:];
-[FigCoreMotionDelegate getCurrentDeltaQuaternion:];
-[FigCoreMotionDelegate getCurrentQuaternion:];
-[FigCoreMotionDelegate getFusedVectorX:y:z:forTimeStamp:];
-[FigCoreMotionDelegate getGravityX:y:z:forTimeStamp:];
-[FigCoreMotionDelegate getLatestMotionDataTime:];
-[FigCoreMotionDelegate getPositionX:y:z:forTimeStamp:];
-[FigCoreMotionDelegate getVectorX:y:z:forTimeStamp:];
-[FigCoreMotionDelegate initWithAccelerometer:gravityZ:fusedMotion:accelUpdateInterval:fusedMotionUpdateInterval:motionCallbackThreadPriority:];
-[FigCoreMotionDelegate isCopyingAllData];
-[FigCoreMotionDelegate managingAccel];
-[FigCoreMotionDelegate managingFusedMotion];
-[FigCoreMotionDelegate updateCurrentQuaternionForTimeStamp:];
-[FigCoreMotionDelegate updateCurrentQuaternionForTimeStamps:withEnd:];
-[FigCoreMotionDelegate updateDeviceCallback:fusedMotionUpdateInterval:];
-[FigCoreMotionDelegate updateGyroInterval:];
```
