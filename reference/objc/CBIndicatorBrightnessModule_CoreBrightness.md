# `CBIndicatorBrightnessModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`, `CBAODProtocol`
- 39 instance variables, 4 properties, 69 instance methods, 0 class methods

## Instance variables

```
@? _notificationBlock;
@"NSObject<OS_os_log>" _logHandle;
f _minBrightness;
f _maxBrightness;
f _sdrBrightness;
f _lux;
f _contentHeadroom;
B _hdrContent;
{?="maxContrastBoostedBrightness"f"sdrBrightness"f"appliedHeadroom"f"minimumIndicatorBrightness"f"lux"f"contentHeadroom"f"rtplc"{?="cap"f"applied"B}"silEnabled"B"dirty"B} _nextUpdate;
f _currentIndicatorBrightness;
f _mib;
f _mibCompensationFactor;
f _targetIndicatorBrightness;
B _jumpOnRestart;
B _firstMIBReceived;
f _lastAppliedDimmingFactor;
f _rampSpeed;
@"CBStopsBasedBrightnessRamp" _ramp;
^? _currentTimeFunction;
B _forcedBrightnessUpdate;
f _lastReportedUIBrightness;
Q _lastSILOnTimestampUs;
Q _lastSILOffTimestampUs;
@"NSMutableArray" _mibServices;
@"CBFrameInfoProvider" _frameInfoProvider;
f _rtplcCap;
B _rtplcApplied;
B _rtplcMonitoring;
B _enforceMIB;
B _indicatorBrightnessFollowsMIB;
B _aodOn;
@"NSObject<CBContrastIndicatorPolicy>" _contrastIndicatorPolicy;
@"CBDisplayContext" _context;
C _dcpRoleID;
@"CBIndicatorAnalyticsModule" _mibAnalytics;
i _thermalPressureNotificationToken;
Q _thermalPressure;
@"NSObject" _swapStallObserverToken;
AI _consecutiveSwapStalledCount;
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
-[CBIndicatorBrightnessModule setThermalPressure:];
-[CBIndicatorBrightnessModule sendRampIsRunningNotificationActive];
-[CBIndicatorBrightnessModule copyPropertyForKey:];
-[CBIndicatorBrightnessModule jumpTo:forReason:withForce:];
-[CBIndicatorBrightnessModule rampTo:];
-[CBIndicatorBrightnessModule setSDRBrightness:];
-[CBIndicatorBrightnessModule setProperty:forKey:];
-[CBIndicatorBrightnessModule handleEvent:];
-[CBIndicatorBrightnessModule addHIDServiceClient:];
-[CBIndicatorBrightnessModule className];
-[CBIndicatorBrightnessModule removeHIDServiceClient:];
-[CBIndicatorBrightnessModule recordSwapStall:];
-[CBIndicatorBrightnessModule dcpRoleID];
-[CBIndicatorBrightnessModule updateMaxContrastBoostedBrightnessGated:];
-[CBIndicatorBrightnessModule forceSILOff];
-[CBIndicatorBrightnessModule indicatorBrightnessFollowsMIB];
-[CBIndicatorBrightnessModule sendRampIsRunningNotificationAOD];
-[CBIndicatorBrightnessModule forceBrightnessTransaction];
-[CBIndicatorBrightnessModule setSilState:];
-[CBIndicatorBrightnessModule isPipelineStalled];
-[CBIndicatorBrightnessModule stop];
-[CBIndicatorBrightnessModule currentIndicatorBrightness];
-[CBIndicatorBrightnessModule determineJumpTarget];
-[CBIndicatorBrightnessModule registerForThermalPressureNotifications];
-[CBIndicatorBrightnessModule shouldJumpToMIB];
-[CBIndicatorBrightnessModule shouldHintSILOnForEventTimestampUs:];
-[CBIndicatorBrightnessModule dealloc];
-[CBIndicatorBrightnessModule isThermalPressureCritical];
-[CBIndicatorBrightnessModule SILState];
-[CBIndicatorBrightnessModule start];
-[CBIndicatorBrightnessModule setRampSpeed:];
-[CBIndicatorBrightnessModule updateRamp];
-[CBIndicatorBrightnessModule canJumpToTargetIndicatorBrightness];
-[CBIndicatorBrightnessModule initWithContext:min:max:maxBoost:andFrameInfoProvider:];
-[CBIndicatorBrightnessModule setLux:];
-[CBIndicatorBrightnessModule sendRampIsRunningNotification];
-[CBIndicatorBrightnessModule handleNotificationForKey:withProperty:];
-[CBIndicatorBrightnessModule startMonitoringForRTPLC];
-[CBIndicatorBrightnessModule initWithContext:min:max:contrastIndicatorPolicy:andFrameInfoProvider:];
-[CBIndicatorBrightnessModule endRamp];
-[CBIndicatorBrightnessModule currentDigitalDimmingFactor];
-[CBIndicatorBrightnessModule isEXBrightDispatching];
-[CBIndicatorBrightnessModule sendRampFinishedNotificationActive];
-[CBIndicatorBrightnessModule processTransaction];
-[CBIndicatorBrightnessModule isRampRunning];
-[CBIndicatorBrightnessModule updateMaxContrastBoostedBrightness:];
-[CBIndicatorBrightnessModule thermalPressureNotificationHandler:];
-[CBIndicatorBrightnessModule sendRampFinishedNotification];
-[CBIndicatorBrightnessModule setAppliedHeadroom:];
-[CBIndicatorBrightnessModule sendRampFinishedNotificationAOD];
-[CBIndicatorBrightnessModule findContrastIndicatorNodeForContext:];
-[CBIndicatorBrightnessModule stopMonitoringForSwapStalls];
-[CBIndicatorBrightnessModule initWithContext:min:max:andContrastIndicatorPolicy:];
-[CBIndicatorBrightnessModule startMonitoringForSwapStalls];
-[CBIndicatorBrightnessModule setMinimumIndicatorBrightness:];
-[CBIndicatorBrightnessModule currentTimeUs];
-[CBIndicatorBrightnessModule setSilEnabled:];
-[CBIndicatorBrightnessModule rampTo:indicatorUpdatedOutsideOfRamp:];
-[CBIndicatorBrightnessModule handleAODStateUpdate:transitionTime:context:];
-[CBIndicatorBrightnessModule calculate20JNDContrastIndicatorForSDRBrightness:andLux:];
-[CBIndicatorBrightnessModule getDCPRoleIDFromContext:];
-[CBIndicatorBrightnessModule copyPropertyForKey:withParameter:];
-[CBIndicatorBrightnessModule initWithContext:min:max:contrastIndicatorPolicy:frameInfoProvider:andCurrentTimeFunction:];
-[CBIndicatorBrightnessModule calculateJumpTargetForFastStart];
-[CBIndicatorBrightnessModule currentUIBrightness];
-[CBIndicatorBrightnessModule handleRampDecisionForTargetIB:indicatorUpdatedOutsideOfRamp:];
-[CBIndicatorBrightnessModule stopMonitoringForRTPLC];
-[CBIndicatorBrightnessModule calculate60JNDContrastIndicatorForSDRBrightness:andLux:];
-[CBIndicatorBrightnessModule calculate22JNDContrastIndicatorForSDRBrightness:andLux:];
```
