# `CBAurora`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 56 instance variables, 26 properties, 82 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _log;
@"CBDisplayModule" _displayModule;
Q _displayID;
@"NSObject<OS_dispatch_queue>" _queue;
@"CBFrameStats" _frameStats;
@"NSObject<OS_dispatch_source>" _apceTimer;
B _isMonitoring;
f _lastFrameInfoReceivedTimestamp;
f _lastRampTargetScaler;
f _minimumReactionNitsDelta;
i _curveLevel;
{array<float, 3UL>="__elems_"[3f]} _luxActivationThreshold;
{array<float, 3UL>="__elems_"[3f]} _luxExitThreshold;
{array<float, 3UL>="__elems_"[3f]} _luxSaturationThreshold;
f _nitsMinimum;
f _nitsMaximum;
f _minimumScaler;
f _maximumScaler;
f _averageAPCESamplingRate;
B _ignorePeakAPCE;
f _rampUpTimeSecondsPerStop;
f _rampDownTimeSecondsPerStop;
f _rampUpTapPointAPCEMinimum;
f _rampUpTapPointAPCEMaximum;
f _rampDownTapPointAPCEMinimum;
f _rampDownTapPointAPCEMaximum;
f _maximumEnergyConsumption;
f _currentEnergyConsumption;
f _edrDurationPerStop;
B _ignoreSessionLimit;
B _ignoreAPCE;
B _allowEDR;
B _edrHeadroomRestorePending;
{?="active"B"start"f"length"f} _gracePeriod;
{?="targetMargin"f"rampInProgress"B"targetScaler"f"tripMaxBrightness"f} _rtplc;
{?="firstEvaluation"B"auroraStateSatisfied"B"displayStateSatisfied"B"luxSatisfied"B"autoBrightnessSatisfied"B"lowPowerModeSatisfied"B"dominoModeSatisfied"B"autoDimSatisfied"B"gracePeriodSatisfied"B"aodStateSatisfied"B"cltmSatisfied"B"upoSatisfied"B} _entryConditions;
{?="cltmCap"f"upoCap"f"cltmActivationThreshold"f"cltmEntryDelta"f"upoActivationThreshold"f"upoEntryDelta"f} _cpms;
B _supportCLTMAwareAurora;
{?="sdrLUT"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"rampUpMinAPCELUT"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"rampUpMaxAPCELUT"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"rampDownMinAPCELUT"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"rampDownMaxAPCELUT"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"maxGain"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}"energyConsumptionTarget"{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}} _powerAwareAurora;
B _isEnabled;
B _displayIsOn;
B _aodIsOn;
B _autoBrightnessIsEnabled;
B _lowPowerModeIsEnabled;
B _dominoModeIsEnabled;
B _autoDimIsEnabled;
B _autoBrightnessIsAvailable;
B _rampInProgress;
f _currentNits;
f _currentScaler;
f _currentEDRHeadroom;
f _currentEDRHeadroomRequest;
f _cltmCap;
f _upoCap;
f _lux;
f _autoDimRampLength;
```

## Properties

```
@property (TB,R) isActive;
@property (TB,R) isBoostingBrightness;
@property (TB,R) allowsEDR;
@property (TB,N,V_isEnabled) isEnabled;
@property (TB,N,V_displayIsOn) displayIsOn;
@property (TB,N,SsetAODIsOn:,V_aodIsOn) aodIsOn;
@property (TB,N,V_autoBrightnessIsEnabled) autoBrightnessIsEnabled;
@property (Ti,N,V_curveLevel) curveLevel;
@property (TB,N,V_lowPowerModeIsEnabled) lowPowerModeIsEnabled;
@property (TB,N,V_dominoModeIsEnabled) dominoModeIsEnabled;
@property (TB,N,V_autoDimIsEnabled) autoDimIsEnabled;
@property (TB,N,V_autoBrightnessIsAvailable) autoBrightnessIsAvailable;
@property (TB,V_rampInProgress) rampInProgress;
@property (Tf,V_currentNits) currentNits;
@property (Tf,R) currentPreAuroraNits;
@property (Tf,N,V_currentScaler) currentScaler;
@property (Tf,V_currentEDRHeadroom) currentEDRHeadroom;
@property (Tf,N,V_currentEDRHeadroomRequest) currentEDRHeadroomRequest;
@property (Tf,N,SsetCLTMCap:,V_cltmCap) cltmCap;
@property (Tf,N,SsetUPOCap:,V_upoCap) upoCap;
@property (Tf,N,V_lux) lux;
@property (Tf,N,V_autoDimRampLength) autoDimRampLength;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBAurora enter];
-[CBAurora startMonitoring];
-[CBAurora copyPropertyForKey:];
-[CBAurora lowPowerModeIsEnabled];
-[CBAurora rampTo:];
-[CBAurora setProperty:forKey:];
-[CBAurora calculateRampUpTargetForNits:andAPCE:];
-[CBAurora calculateLuxTargetScaler:];
-[CBAurora currentEDRHeadroom];
-[CBAurora convertScalerToNits:];
-[CBAurora setAutoBrightnessIsAvailable:];
-[CBAurora autoDimRampLength];
-[CBAurora calculateNumberOfStopsForCurrentScaler:andRequestedScaler:];
-[CBAurora calculateCurrentRampDownTargetForAPCE:];
-[CBAurora currentNits];
-[CBAurora setIsEnabled:];
-[CBAurora initWithQueue:andDisplayModule:andBrtCapabilities:andFrameStats:andDisplayID:];
-[CBAurora clampScaler:];
-[CBAurora stop];
-[CBAurora autoDimIsEnabled];
-[CBAurora upoCap];
-[CBAurora setDominoModeIsEnabled:];
-[CBAurora dealloc];
-[CBAurora calculateRampTimeForCurrentScaler:andRequestedScaler:];
-[CBAurora exit];
-[CBAurora start];
-[CBAurora luxActivationThreshold];
-[CBAurora calculateCurrentRampUpTargetForAPCE:];
-[CBAurora autoBrightnessIsEnabled];
-[CBAurora setDisplayIsOn:];
-[CBAurora autoBrightnessIsAvailable];
-[CBAurora setCurrentEDRHeadroomRequest:];
-[CBAurora setRampInProgress:];
-[CBAurora setUPOCap:];
-[CBAurora setPropertyInternal:forKey:];
-[CBAurora setLux:];
-[CBAurora setAutoBrightnessIsEnabled:];
-[CBAurora stopMonitoring];
-[CBAurora setAutoDimRampLength:];
-[CBAurora updateAPCENitsLUT];
-[CBAurora handleNotificationForKey:withProperty:];
-[CBAurora energyConsumptionExceeded];
-[CBAurora setCurrentNits:];
-[CBAurora setCurrentScaler:];
-[CBAurora allowsEDR];
-[CBAurora isEnabled];
-[CBAurora setRampDownTimeSecondsPerStop:];
-[CBAurora luxExitThreshold];
-[CBAurora evaluateEntryConditions];
-[CBAurora processAPCESample];
-[CBAurora calculateCurrentLuxTargetScaler];
-[CBAurora currentScaler];
-[CBAurora calculateRampTargetForNits:andAPCE:withTapPointAPCEMinimum:andTapPointAPCEMaximum:];
-[CBAurora displayIsOn];
-[CBAurora calculateRampTargetScalerForNits:];
-[CBAurora cltmCap];
-[CBAurora restoreEDRHeadroom];
-[CBAurora setLowPowerModeIsEnabled:];
-[CBAurora isBoostingBrightness];
-[CBAurora initializeMembers:];
-[CBAurora setAuroraFactor:withFadePeriod:];
-[CBAurora luxSaturationThreshold];
-[CBAurora setCLTMCap:];
-[CBAurora entryConditionsSatisfied];
-[CBAurora calculateEnergyConsumptionCap];
-[CBAurora setCurrentEDRHeadroom:];
-[CBAurora lux];
-[CBAurora dominoModeIsEnabled];
-[CBAurora setCLTMActivationThreshold:];
-[CBAurora isActive];
-[CBAurora rampInProgress];
-[CBAurora setCurveLevel:];
-[CBAurora setAutoDimIsEnabled:];
-[CBAurora currentEDRHeadroomRequest];
-[CBAurora copyPropertyForKey:withParameter:];
-[CBAurora aodIsOn];
-[CBAurora sendEDRHeadroomRequest:];
-[CBAurora curveLevel];
-[CBAurora currentPreAuroraNits];
-[CBAurora setRampUpTimeSecondsPerStop:];
-[CBAurora setAODIsOn:];
-[CBAurora calculateRampDownTargetForNits:andAPCE:];
```
