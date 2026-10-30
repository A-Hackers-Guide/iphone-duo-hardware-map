# `CBColorModuleShared`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`, `NightShiftSupportProtocol`, `CBStatusInfoProtocol`, `CBAODProtocol`
- 52 instance variables, 4 properties, 123 instance methods, 0 class methods

## Instance variables

```
@"<CBBrightnessProxy>" _brightnessControlProxy;
@"<CBPrimitiveConfigurationProvider><CBBacklightConfigurationProvider>" _backlightConfig;
@"NSMutableArray" _relevantServices;
@"NSMutableDictionary" _alsNodes;
@"NSMutableDictionary" _currentChromaticitySensitivity;
{?="firstTimerFire"C"logTimer"@"NSObject<OS_dispatch_source>""periodS"i} _reportContext;
B _displayOn;
B _forceInitialFactorUpdate;
^{__IOHIDServiceClient=} _dfr;
B _clamshell;
@"NSObject<OS_dispatch_source>" _rampTimer;
@"NSString" _userName;
@"NSMutableDictionary" _properties;
{ColorType="cfx"^{ColorEffects}"blueReductionEnabled"B"blueReductionFactor"f"nightModeSupported"B"fadeInProgress"B"enforceSlowRamps"B"harmonyHWSupported"B"harmonyNativeSupported"B"harmonySystemSupported"B"harmonyEnabled"B"harmonyActive"B"harmonyAvailable"B"harmonyStrength"f"harmonyFixedStrength"f"presetDisableHarmony"B"moduleType"Q} _colorStruct;
B _aggregatedConfigApplied;
@"NSMutableDictionary" _aggregatedConfig;
q _analyticsPeriodicSender;
Q _colorFilterModeOverride;
@"CBColorFilter" _colorFilter;
@"NSMutableArray" _overrideFilters;
@"NSMutableArray" _filters;
@"NSMutableDictionary" _pendingALSSamples;
@"NSMutableSet" _nodesWithALSEvent;
@"StockholmALSCoexHandler" _nfcCoex;
i _NSamples;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
B _firstALSEventArrived;
f _firstSampleTimeoutValue;
B _allALSEventsArrived;
B _forceColorUpdate;
B _potentiallyBustedALS;
B _continueWithFewerALSs;
B _continueWithSelectedALSs;
B _useCopyEventOnDisplayWake;
f _preStrobeDimPeriod;
B _anyMitigationEnabled;
@"NSMutableArray" _modules;
@"NSMutableDictionary" _alsMitigationState;
B _colorEffectsEnabled;
B _ammoliteEnabledStatus;
B _supportsAmmoliteWithoutColor;
B _ammoliteSystemSupported;
f _trustedLux;
B _mirror;
I _panelPlacement;
@"CBDisplayContext" _displayContext;
@"CBCoexTracker" _coexTracker;
@"CBDisplayCoex" _displayCoex;
@"CBColorFloorCoex" _colorFloorCoex;
@"<CBEventServiceProtocol>" _angleService;
f _currentAngleDegrees;
@"<CBALSSelectionPolicyProtocol>" _firstALSSelectionPolicy;
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
-[CBColorModuleShared setNightShiftFactorDictionary:];
-[CBColorModuleShared copyPreferenceForKey:user:];
-[CBColorModuleShared copyPropertyForKey:];
-[CBColorModuleShared sendNotificationForKey:andValue:];
-[CBColorModuleShared setProperty:forKey:];
-[CBColorModuleShared handleEvent:];
-[CBColorModuleShared CoreBrightnessFeaturesDisabledPropertyHandler:];
-[CBColorModuleShared addHIDServiceClient:];
-[CBColorModuleShared setPreference:forKey:user:];
-[CBColorModuleShared copyIdentifiers];
-[CBColorModuleShared removeHIDServiceClient:];
-[CBColorModuleShared copyPropertyInternalForKey:];
-[CBColorModuleShared setWhitePointType];
-[CBColorModuleShared CAStrengthUpdate:withPeriod:];
-[CBColorModuleShared clamshellStatePropertyHandler:];
-[CBColorModuleShared displayBrightnessFactorUpdate:];
-[CBColorModuleShared BLRFactorUpdate:];
-[CBColorModuleShared displayPresetHarmonyHandler:];
-[CBColorModuleShared serializedAggregatedConfigPropertyHandler:];
-[CBColorModuleShared applyPendingSamples];
-[CBColorModuleShared uvThresholdPropertyHandler:forKey:];
-[CBColorModuleShared enableCarryLog];
-[CBColorModuleShared applySamples:withinTimeout:];
-[CBColorModuleShared reportInitialize];
-[CBColorModuleShared BLRFactorUpdate:withPeriod:shouldForceUpdate:];
-[CBColorModuleShared timerRoutine:];
-[CBColorModuleShared inputAmbientColorSample:force:trust:];
-[CBColorModuleShared displayBrightnessFactorPropertyHandler:];
-[CBColorModuleShared reportToCoreAnalytics:];
-[CBColorModuleShared copyPreferenceInternalForKey:];
-[CBColorModuleShared stop];
-[CBColorModuleShared reportCommitWithStop:];
-[CBColorModuleShared armFirstALSSampleTimer];
-[CBColorModuleShared CEModulePropertyHandler:key:];
-[CBColorModuleShared dealloc];
-[CBColorModuleShared setFirstSampleNoColor];
-[CBColorModuleShared newSerializedConfigFromAggregatedConfig:];
-[CBColorModuleShared start];
-[CBColorModuleShared CAStrengthRampPeriodTweakPropertyHandler:];
-[CBColorModuleShared BLRCCTTargetPropertyHandler:];
-[CBColorModuleShared CAWeakestColorAdaptationModePropertyHandler:];
-[CBColorModuleShared ttRestrictionHandler:];
-[CBColorModuleShared colorRampPeriodOverrideHandler:];
-[CBColorModuleShared CEEnablePropertyHandler:key:];
-[CBColorModuleShared setPropertyInternal:forKey:];
-[CBColorModuleShared initWithBrightnessControl:queue:backlightConfig:moduleType:];
-[CBColorModuleShared autoBrightnessPropertyHandler:];
-[CBColorModuleShared newAdaptationModeMappingArray:strengthNum:];
-[CBColorModuleShared CAFixedStrengthPropertyHandler:];
-[CBColorModuleShared newAggregatedConfigFromSerializedConfig:];
-[CBColorModuleShared ignoreALSEventsInAOD];
-[CBColorModuleShared handleNotificationForKey:withProperty:];
-[CBColorModuleShared CAWeakestColorAdaptationModeAnimatedPropertyHandler:];
-[CBColorModuleShared updateActivity];
-[CBColorModuleShared ammoliteSupported];
-[CBColorModuleShared enableMitigationsForALSNode:];
-[CBColorModuleShared carryLogCommitHandler:];
-[CBColorModuleShared replaceEvent:withFilteredEvent:];
-[CBColorModuleShared isRearALS:];
-[CBColorModuleShared activateColorAdaptation];
-[CBColorModuleShared CAFadesEnabledHandler:];
-[CBColorModuleShared initDFRHarmonyWithSKL:queue:];
-[CBColorModuleShared handleALSEvent:];
-[CBColorModuleShared updateHarmonySupport];
-[CBColorModuleShared updateAvailability];
-[CBColorModuleShared reportResetTimerWithStop:];
-[CBColorModuleShared initALSSelectionPolicy];
-[CBColorModuleShared CAAABSensorOverridePropertyHandler:];
-[CBColorModuleShared applyAggregatedConfig:];
-[CBColorModuleShared handleDisplayBrightnessFactorZero:];
-[CBColorModuleShared carryLogEnabledHandler:];
-[CBColorModuleShared ttRestrictionReload];
-[CBColorModuleShared CALabShiftPropertyHandler:];
-[CBColorModuleShared isDFR];
-[CBColorModuleShared activateBLR];
-[CBColorModuleShared colorRampRoutine:];
-[CBColorModuleShared newAdaptationModeMappingDictionary:strengthNum:];
-[CBColorModuleShared CAModeMappingHandler:];
-[CBColorModuleShared initWithBrightnessControl:moduleType:backlightConfig:queue:];
-[CBColorModuleShared BLRCCTRangePropertyHandler:];
-[CBColorModuleShared absoluteDifferenceForCurrentColor:andDeltaError:];
-[CBColorModuleShared loadBacklightProperties];
-[CBColorModuleShared firstALSSampleTimeout];
-[CBColorModuleShared supportsColorRepairability];
-[CBColorModuleShared applyAggregatedConfigPropertyHandler:];
-[CBColorModuleShared handleCoexUpdates:];
-[CBColorModuleShared copyALSSamples];
-[CBColorModuleShared startNewTimerWithFreq:];
-[CBColorModuleShared cancelFirstSampleTimeout];
-[CBColorModuleShared preStrobeDimPeriodPropertyHandler:];
-[CBColorModuleShared initWithContext:andModuleType:];
-[CBColorModuleShared setColorSensitivity:forALS:];
-[CBColorModuleShared hasRearALS];
-[CBColorModuleShared handleAODStateUpdate:transitionTime:context:];
-[CBColorModuleShared initAmmolite];
-[CBColorModuleShared copyLocalAggregatedConfig];
-[CBColorModuleShared externalDisplayModeHandler:];
-[CBColorModuleShared updateAggregatedConfigWithObject:forKey:];
-[CBColorModuleShared updateSensorPolicy];
-[CBColorModuleShared preStrobePropertyHandler:];
-[CBColorModuleShared BLRFactorPropertyHandler:];
-[CBColorModuleShared setNativeWhitePoint];
-[CBColorModuleShared hasCoexForALS:];
-[CBColorModuleShared copyPropertyForKey:withParameter:];
-[CBColorModuleShared parseAdaptationModeMappingDictionary:strengths:strengthNum:];
-[CBColorModuleShared CAEnabledPropertyHandler:];
-[CBColorModuleShared hasExternalALS];
-[CBColorModuleShared filterInitialize];
-[CBColorModuleShared parseAdaptationModeMappingArray:strengths:strengthNum:];
-[CBColorModuleShared colorFilterModeHandler:];
-[CBColorModuleShared ammolitePropertyHandler:];
-[CBColorModuleShared setPreferenceInternal:forKey:];
-[CBColorModuleShared carryLogCommentHandler:];
-[CBColorModuleShared updateClamshellState:];
-[CBColorModuleShared handleEventInternal:];
-[CBColorModuleShared CAStrengthPropertyHandler:];
-[CBColorModuleShared updateSensorSensitivity:forValue:];
-[CBColorModuleShared setLabShift];
-[CBColorModuleShared updateColorFilterMode];
-[CBColorModuleShared initCoexTracker];
-[CBColorModuleShared getRegistryIDForHIDServiceClient:];
-[CBColorModuleShared initColorStruct];
-[CBColorModuleShared commitPowerLogReport:];
```
