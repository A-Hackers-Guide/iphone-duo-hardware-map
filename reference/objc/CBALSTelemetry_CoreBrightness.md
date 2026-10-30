# `CBALSTelemetry`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 6 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDServiceClient=} _alsService;
@"NSObject<OS_dispatch_source>" _timer;
@"NSUserDefaults" _defaults;
d _timeFactor;
Q _lastTimestampInMicroseconds;
B _alsLiveOnTelemetryEnabled;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBALSTelemetry copyPropertyForKey:];
-[CBALSTelemetry sendNotificationForKey:andValue:];
-[CBALSTelemetry setProperty:forKey:];
-[CBALSTelemetry initWithQueue:];
-[CBALSTelemetry stop];
-[CBALSTelemetry dealloc];
-[CBALSTelemetry start];
-[CBALSTelemetry handleSystemDidWakeFromSleepPropertyHandler:];
-[CBALSTelemetry handleNotificationForKey:withProperty:];
-[CBALSTelemetry timerFired];
-[CBALSTelemetry copyPropertyForKey:withParameter:];
-[CBALSTelemetry copyALSSampleHistoryWithLength:frequency:lastTimestamp:];
-[CBALSTelemetry getBootTimeInMicroSeconds];
-[CBALSTelemetry handleSystemPrepareForSleepPropertyHandler:];
-[CBALSTelemetry setALSService:];
-[CBALSTelemetry updateLastTimestampInDefaults];
```
