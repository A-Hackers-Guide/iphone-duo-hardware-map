# `CBAODModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`, `CBDisplayModeProtocol`
- 20 instance variables, 7 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _modules;
@"<CBBrightnessProxy>" _brtCtl;
@"CBAODTransitionController" _transitionController;
@"CBAODThresholdModule" _thresholdModule;
@"CBALSEvent" _currentALSEvent;
@"NSMutableSet" _alsNodes;
B _ABStateBackup;
f _displayBrightnessBackup;
q _ABLuxFilterBackup;
@"NSDictionary" _backupState;
@"NSObject<OS_dispatch_source>" _displayModeCompletionTimer;
@"CBSensorOverrideFilter" _aabSensorOverrideFilter;
B _flipBookEnabled;
q _currentDisplayMode;
B _suspendFeatureUpdates;
B _dominoModeEnabled;
@"CBDisplayContext" _context;
@"CBDisplayALSSamplingPolicy" _alsPolicy;
B _aodEnabled;
q _displayMode;
```

## Properties

```
@property (TB,V_aodEnabled) aodEnabled;
@property (T@"CBAODState",R) AODState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,V_displayMode) displayMode;
```

## Instance methods

```
-[CBAODModule initWithContext:];
-[CBAODModule copyPropertyForKey:];
-[CBAODModule handleDisplayModeUpdate:withDuration:callback:];
-[CBAODModule releaseDisplayModeCompletionTimer];
-[CBAODModule sendNotificationForKey:andValue:];
-[CBAODModule setProperty:forKey:];
-[CBAODModule getFloatValueFrom:key:];
-[CBAODModule copyModulesInfo:];
-[CBAODModule handleEvent:];
-[CBAODModule addHIDServiceClient:];
-[CBAODModule AODState];
-[CBAODModule addModule:];
-[CBAODModule removeHIDServiceClient:];
-[CBAODModule performUpdate:];
-[CBAODModule offAODRoutineForDisplayMode:transitionParameters:];
-[CBAODModule setDisplayMode:];
-[CBAODModule copyAndHandleEventWithTransitionLength:];
-[CBAODModule stop];
-[CBAODModule copyAndHandleEvent];
-[CBAODModule prepareForEnterToAODRoutine];
-[CBAODModule dealloc];
-[CBAODModule copyArrayFromPrefsForKey:];
-[CBAODModule handleALSEvent:transitionParameters:];
-[CBAODModule displayMode];
-[CBAODModule setALSServiceProperty:forKey:];
-[CBAODModule start];
-[CBAODModule setAodEnabled:];
-[CBAODModule copyModulesIdentifiers];
-[CBAODModule performUpdateWithTransitionParameters:];
-[CBAODModule exitingAODRoutineForDisplayMode:transitionParameters:];
-[CBAODModule handleFlipBookStatePropertyHandler:];
-[CBAODModule copyAndHandleEventWithTransitionLength:forceUpdate:];
-[CBAODModule updateModulesAODState:transitionParameters:context:];
-[CBAODModule handleSystemDidWakeFromSleepPropertyHandler:];
-[CBAODModule handleEvent:transitionParameters:];
-[CBAODModule handleNotificationForKey:withProperty:];
-[CBAODModule updateModulesAODState:transitionParameters:];
-[CBAODModule aodEnabled];
-[CBAODModule setModulesProperty:forKey:];
-[CBAODModule checkBootArgsConfiguration];
-[CBAODModule loadAODCurveFromDefaults];
-[CBAODModule performUpdate:forceUpdate:];
-[CBAODModule handleDisplayModeUpdate:transitionLength:];
-[CBAODModule fadeInBrightnessBoost];
-[CBAODModule performUpdateWithTransitionParameters:rampDoneCallback:rampCanceledCallback:];
-[CBAODModule updateAODState:transitionParameters:brightnessFactor:forDisplayMode:];
-[CBAODModule updateModulesAODState:];
-[CBAODModule fadeOutBrightnessBoost];
-[CBAODModule updateModulesAODState:context:];
-[CBAODModule copyModulesExtendedIdentifiers];
-[CBAODModule handleEvent:transitionLength:forceUpdate:];
-[CBAODModule handleAABSensorOverridePropertyHandler:];
-[CBAODModule updateModulesAODConfigWithContext:];
-[CBAODModule didCompleteTransitionToDisplayMode:];
-[CBAODModule reevaluatePThresholdsForLux:];
-[CBAODModule enteringAODRoutineForDisplayMode:transitionParameters:];
-[CBAODModule enteringSuppressedAODRoutineWithTransitionParameters:];
-[CBAODModule handleDisplayNitsOverridePropertyHandler:];
-[CBAODModule onSuppresedAODRoutine];
-[CBAODModule copyAndHandleEventWithTransitionParameters:];
-[CBAODModule setDisplayFactor:transitionLength:];
-[CBAODModule getFloatValueFrom:key:subkey:];
-[CBAODModule getIntegerValueFrom:key:];
-[CBAODModule copyPropertyForKey:withParameter:];
-[CBAODModule copyModulesPropertyForKey:];
-[CBAODModule performUpdate:forceUpdate:rampDoneCallback:rampCanceledCallback:];
-[CBAODModule isDesignatedAODSensor:];
-[CBAODModule onAODRoutineForDisplayMode:transitionParameters:];
-[CBAODModule scheduleDisplayModeCompletionTimerIn:forDisplayMode:];
-[CBAODModule performUpdate];
```
