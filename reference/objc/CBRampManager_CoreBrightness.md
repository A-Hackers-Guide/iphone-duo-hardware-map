# `CBRampManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBRampManagerI`
- 13 instance variables, 8 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_source>" _clockTimer;
@"NSMutableDictionary" _ramps;
I _ephemeralRampCount;
B _activated;
f _requiredFrequency;
d _sMachTimebaseFactor;
@"<CBClockSource>" _frameLink;
B _enableFrameSynchronisation;
B _liveUpdates;
@? _clockHandler;
@? _rampDoneCallback;
```

## Properties

```
@property (T@?,C,V_clockHandler) clockHandler;
@property (T@?,C,V_rampDoneCallback) rampDoneCallback;
@property (TB,R,N,V_enableFrameSynchronisation) enableFrameSynchronisation;
@property (TB,V_liveUpdates) liveUpdates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBRampManager copyStatusInfo];
-[CBRampManager init];
-[CBRampManager dealloc];
-[CBRampManager stopTimer];
-[CBRampManager activate];
-[CBRampManager cancel];
-[CBRampManager setTimer];
-[CBRampManager disableClocking];
-[CBRampManager insertNewRampOrigin:target:length:frequency:identifier:profile:];
-[CBRampManager setLiveUpdates:];
-[CBRampManager remainingLength];
-[CBRampManager clockHandler];
-[CBRampManager enableClocking];
-[CBRampManager enableFrameSynchronisation];
-[CBRampManager generateRamp];
-[CBRampManager hasActiveEphemeralRamp];
-[CBRampManager hasAnyActiveRamp];
-[CBRampManager hasRampRunningForIdentifier:];
-[CBRampManager initWithClockSource:];
-[CBRampManager initWithClockSource:andDisplayId:];
-[CBRampManager initWithClockSource:andLogSubsystem:];
-[CBRampManager insertNewEternalRampFrequency:startRamp:identifier:progressCallback:];
-[CBRampManager insertNewLinearRampOrigin:target:length:frequency:identifier:];
-[CBRampManager insertNewLinearRampOrigin:target:length:frequency:startRamp:identifier:];
-[CBRampManager insertNewRampOrigin:target:length:frequency:identifier:progressCallback:];
-[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:profile:];
-[CBRampManager insertNewRampOrigin:target:length:frequency:startRamp:identifier:progressCallback:];
-[CBRampManager insertRamp:];
-[CBRampManager insertRamp:identifier:];
-[CBRampManager insertRamp:identifier:reevaluate:];
-[CBRampManager liveUpdates];
-[CBRampManager rampDoneCallback];
-[CBRampManager rampForIdentifier:];
-[CBRampManager reevaluateClocking];
-[CBRampManager removeAllRamps];
-[CBRampManager removeRampWithIdentifier:];
-[CBRampManager scheduleWithDispatchQueue:];
-[CBRampManager setClockHandler:];
-[CBRampManager setRampDoneCallback:];
-[CBRampManager startRamps];
-[CBRampManager timerClockHandler];
-[CBRampManager updateRampsForTimestamp:];
```
