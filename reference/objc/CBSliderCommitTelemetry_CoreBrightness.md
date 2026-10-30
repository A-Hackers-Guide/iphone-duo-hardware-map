# `CBSliderCommitTelemetry`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBAODProtocol`
- 18 instance variables, 4 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"CBDisplayContaineriOS" _displayContainer;
{TrackedState="darkThemeApplied"B"landscapeOrientation"B"autobrightnessEnabled"B"ecoModeEnabled"B} _state;
@"NSObject<OS_dispatch_queue>" _loggingQueue;
{array<CBSliderCommitInfo, 100UL>="__elems_"[100{CBSliderCommitInfo="timestamp"q"localTimestamp"q"trustedLux"i"frontLux"f"rearLux"f"rearLuxInUse"B"nits"f"slider"f"apce"f"delayedAPCE"f"delayedAPCEStatus"i"autobrightnessEnabled"B"ecoModeEnabled"B"ecoModeFactor"f"aabParams"{CBAABParams="e0a"f"e0b"f"e1"f"e2"f"l0a"f"l0b"f"l1"f"l2"f"thirdSlope"f"curveType"i}"aabAlternativeParams"{CBAABParams="e0a"f"e0b"f"e1"f"e2"f"l0a"f"l0b"f"l1"f"l2"f"thirdSlope"f"curveType"i}"aabParamsUpdateOnly"B"aabParamsUpdateReason"i"nitsDelta"f"nitsDeltaAlternative"f"restoreTimeTarget"q"inactiveLength"f"inactiveStart"q"cpmsMitigationLimitingBrightness"B"touchMitigationTriggered"B"proxMitigationTriggered"B"auroraFactor"f"edrHeadroom"f"colorAdaptationStrength"f"colorAdaptationMode"i"darkThemeApplied"B"landscapeOrientation"B"trialExperimentId"@"NSString""trialDeploymentId"i"trialTreatmentId"@"NSString""aabMultiModeEnabled"B"aabMode"i"edrHeadroomRequest"f"displayID"@"NSString""colorTargetX"f"colorTargetY"f"colorTargetZ"f}]} _entryBuffer;
Q _bufferIndex;
Q _bufferEntriesFilled;
q _delayedAPCEDelay;
{CBAABParams="e0a"f"e0b"f"e1"f"e2"f"l0a"f"l0b"f"l1"f"l2"f"thirdSlope"f"curveType"i} _lastAABParams;
{CBAABParams="e0a"f"e0b"f"e1"f"e2"f"l0a"f"l0b"f"l1"f"l2"f"thirdSlope"f"curveType"i} _lastAABAlternativeParams;
@"NSObject<OS_os_log>" _bufferLogHandle;
^{__IOMobileFramebuffer=} _iomfb;
@"NSObject<OS_dispatch_source>" _delayedAPCETimer;
d _displayOffTimestamp;
d _longestInactivityLength;
d _inactivityStartTimestamp;
B _initialFactorUpdateArrived;
q _telemetryVariant;
@"NSString" _displayID;
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
-[CBSliderCommitTelemetry copyPropertyForKey:];
-[CBSliderCommitTelemetry setProperty:forKey:];
-[CBSliderCommitTelemetry stop];
-[CBSliderCommitTelemetry dealloc];
-[CBSliderCommitTelemetry start];
-[CBSliderCommitTelemetry sendNotificationForKey:withValue:];
-[CBSliderCommitTelemetry handleNotificationForKey:withProperty:];
-[CBSliderCommitTelemetry handleAODStateUpdate:transitionTime:context:];
-[CBSliderCommitTelemetry copyPropertyForKey:withParameter:];
-[CBSliderCommitTelemetry getAPCE];
-[CBSliderCommitTelemetry addOrUpdateEntryWithTimestamp:slider:apce:andTrackedState:];
-[CBSliderCommitTelemetry cancelDelayedAPCETimer];
-[CBSliderCommitTelemetry delayedAPCETimerHandler:];
-[CBSliderCommitTelemetry fillEntry:withTimestamp:andAABParams:andAlternativeAABParams:];
-[CBSliderCommitTelemetry fillEntry:withTimestamp:andRestoreTimeTarget:andAABParams:andAlternativeAABParams:];
-[CBSliderCommitTelemetry fillEntry:withTimestamp:slider:apce:andTrackedState:];
-[CBSliderCommitTelemetry getLastFilledEntry];
-[CBSliderCommitTelemetry getNextEntryAndAdvanceBufferIndex];
-[CBSliderCommitTelemetry getUserAABParams:];
-[CBSliderCommitTelemetry getUserAABParams:alternativeAABParams:];
-[CBSliderCommitTelemetry getUserAABParams:key:];
-[CBSliderCommitTelemetry initWithQueue:andDisplayContainer:andVariant:andContext:];
-[CBSliderCommitTelemetry logAfterUserBrightnessCommitWithTimestamp:slider:apce:andTrackedState:];
-[CBSliderCommitTelemetry logAllFilledEntries];
-[CBSliderCommitTelemetry reportCommit:];
-[CBSliderCommitTelemetry sliderInfoToNSDictionary:];
-[CBSliderCommitTelemetry timestampFromCurveDistionary:];
```
