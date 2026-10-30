# `/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`

iOS 27.2 dyld shared cache image. Version `27.0.0.0.0`. **[DSC]**

## Linked libraries (14)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 5 classes, 0 protocols, 31 methods, 10 properties

### Class pages

Every class and protocol, with its methods: [`SensorAccessDeviceState`](../objc/SensorAccessDeviceState_SensorAccess.md), [`SensorAccessDuration`](../objc/SensorAccessDuration_SensorAccess.md), [`SensorAccessIndicator`](../objc/SensorAccessIndicator_SensorAccess.md), [`SensorAccessIndicatorHealth`](../objc/SensorAccessIndicatorHealth_SensorAccess.md), [`_TtC12SensorAccess17SensorAccessUtils`](../objc/_TtC12SensorAccess17SensorAccessUtils_SensorAccess.md)

### Classes

`SensorAccessDeviceState`, `SensorAccessDuration`, `SensorAccessIndicator`, `SensorAccessIndicatorHealth`, `_TtC12SensorAccess17SensorAccessUtils`

### Properties

```
@property (TI,N,Vstate) state;
@property (T@"NSString",N,R) description;
@property (TQ,N,VremainingMicrophoneDurationNanoSeconds) remainingMicrophoneDurationNanoSeconds;
@property (TQ,N,VremainingCameraDurationNanoSeconds) remainingCameraDurationNanoSeconds;
@property (TQ,N,VremainingFaceIDDurationNanoSeconds) remainingFaceIDDurationNanoSeconds;
@property (T@"NSString",N,R) description;
@property (Ti,N,VindicatorType) indicatorType;
@property (Ti,N,VhealthCheckType) healthCheckType;
@property (TB,N,VindicatorHealthy) indicatorHealthy;
@property (T@"NSString",N,R) description;
```

## Swift types (4)

`SensorAccess.SensorAccessError`, `SensorAccess.SensorAccessUtils`, `__C.exclaves_device_state_t`, `conformance`

## Strings (46)

```
EXDisplayPipeFailure
Health check type: 
Indicator healthy: 
IODeviceTree:/arm-io/eic
Unsupported Platform
Secure Indicator Policy not enforced on this platform
Sensor Access object initialized
isIndicatorHealthy
Microphone Alternate indicator
performHealthCheck Unable to open EXDisplayPipe connection
Mic indicator duration: 
FaceID indicator duration: 
RemainingTimeCalculationOverflow
Sensor Access object destroyed
SensorAccessIndicator
isIndicatorHealthyThrows SecureIndicatorPolicyNotSupported
SensorAccess.SensorAccessIndicatorHealth
SecureIndicatorPolicyNotSupported
GetMinimumOnTimeFailed
GetMinimumOnTimeNotSupported
getGlobalTimebase failed
init()
Face ID delayed indicator
SensorAccess.SensorAccessError
GetDeviceStateFailed
Indicator type: 
Face ID indicator
Microphone indicator
Cam indicator duration: 
HealthCheckNotSupported
com.apple.SensorAccess
isIndicatorHealthyThrows invalidArgument for healthCheckType
Unknown health check type
performHealthCheck EXDisplayPipeGetSCASessionHealth failed
Policy enforced
Unknown indicator type
Camera indicator
Policy not enforced
exclaves_device_state failed with code: %d
exclaves_device_state returned unrecognized value: %u
Device state: %u
Kernel call failed with code: %d
Remaining duration %@ from SensorAccess
Evaluating remaining time with curr_time %llu cil %llu mil %llu fid %llu
performHealthCheck result - %@
performHealthCheck EXDP status 0b%s
```
