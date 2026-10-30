# `CBAODTransitionController`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- 42 instance variables, 14 properties, 101 instance methods, 0 class methods

## Instance variables

```
@"<CBBrightnessProxy>" _brtCtl;
@"CBAPEndpoint" _endpoint;
@ _currentState;
@ _pendingState;
Q _displayID;
@"CBRampManager" _rampManager;
f _edrRampDurationPerStop;
f _currentSDRBrightness;
f _targetSDRBrightness;
f _minNits;
f _maxNits;
f _currentEDRHeadroom;
f _targetEDRHeadroom;
f _currentIndicatorBrightness;
f _currentIndicatorBrightnessLimit;
f _currentAAPFactor;
f _targetAAPFactor;
f _currentBrightnessLimit;
f _targetBrightnessLimit;
f _currentLumaBoostFactor;
f _targetLumaBoostFactor;
i _currentFrequency;
f _currentTrustedLux;
@? _rampDoneCallback;
@? _rampCanceledCallback;
{?="ID"I"brightness_set"B"whitepoint_set"B"pccfactor_set"B"brightnessLimit_set"B"brightness"f"whitepoint"[3[3f]]"pccfactor"f"brightnessLimit"f"lowAmbientAdaptationStrength_set"B"lowAmbientAdaptationStrength"f"lowAmbientAdaptationLux"f"ammoliteStrength_set"B"ammoliteStrength"f"ammoliteLux"f"reserved"[5C]} _currentFlipBookEntry;
@"CBAODFlipBookWrapper" _flipbookCache;
@"CBAODThresholdModule" _thresholdModule;
@"NSObject<OS_dispatch_source>" _lastUpdateSwappedTimer;
^{ColorEffects=} cfx;
{?="matrix"[3[3f]]"xy"{?="x"f"y"f}"Y"f} _currentWhitepoint;
{?="matrix"[3[3f]]"xy"{?="x"f"y"f}"Y"f} _targetWhitepoint;
B _liveUpdatesOverride;
B _displayON;
f _nitsOverride;
f _currentDisplayNits;
f _brightnessFactor;
f _remainingTransitionLength;
@"CBDisplayContext" _displayContext;
@"CBTwilight" _twilight;
@"CBAmmolite" _ammolite;
@"CBIndicatorBrightnessModule" _indicator;
```

## Properties

```
@property (TB,V_liveUpdatesOverride) liveUpdatesOverride;
@property (Tf,V_nitsOverride) nitsOverride;
@property (Tf,N,V_currentDisplayNits) currentDisplayNits;
@property (Tf,N,V_currentAAPFactor) currentAAPFactor;
@property (Tf,N,V_brightnessFactor) brightnessFactor;
@property (TB,N,V_displayON) displayON;
@property (Tf,V_remainingTransitionLength) remainingTransitionLength;
@property (TB) liveUpdates;
@property (T@"CBDisplayContext",R,V_displayContext) displayContext;
@property (T@"CBAODState",R) AODState;
@property (T@"CBTwilight",&,V_twilight) twilight;
@property (T@"CBAmmolite",&,V_ammolite) ammolite;
@property (T@"CBGammaContrastPreservation",R) gcp;
@property (T@"CBIndicatorBrightnessModule",&,V_indicator) indicator;
```

## Instance methods

```
-[CBAODTransitionController displayContext];
-[CBAODTransitionController initWithContext:];
-[CBAODTransitionController sendNotificationForKey:andValue:];
-[CBAODTransitionController getFloatValueFrom:key:];
-[CBAODTransitionController AODState];
-[CBAODTransitionController dealloc];
-[CBAODTransitionController indicator];
-[CBAODTransitionController checkBootArgsConfiguration];
-[CBAODTransitionController cancelTransition];
-[CBAODTransitionController copyContext];
-[CBAODTransitionController colorRampRoutine:];
-[CBAODTransitionController setInitialState:];
-[CBAODTransitionController getFloatValueFrom:key:subkey:];
-[CBAODTransitionController setIndicator:];
-[CBAODTransitionController gcp];
-[CBAODTransitionController setCurrentWhitepointFromMatrix:];
-[CBAODTransitionController setLiveUpdates:];
-[CBAODTransitionController activateLastUpdateSwappedTimerWithTimeout:];
-[CBAODTransitionController addFlipBookEntry:];
-[CBAODTransitionController ammolite];
-[CBAODTransitionController applyPendingUpdates];
-[CBAODTransitionController brightnessFactor];
-[CBAODTransitionController brightnessLimitProgressCallback:rampContext:profile:];
-[CBAODTransitionController calculateSigmoidProgressForLinearProgress:];
-[CBAODTransitionController calculateSpringProgressForLinearProgress:];
-[CBAODTransitionController cancelDCPTransition];
-[CBAODTransitionController chromaticity:andIlluminance:fromMatrix:];
-[CBAODTransitionController clockUpdateHandler:];
-[CBAODTransitionController colorMatrix:fromState:];
-[CBAODTransitionController commitBrightness:force:];
-[CBAODTransitionController copyColourRampStatsWithLength:frequency:origin:target:];
-[CBAODTransitionController copyCurrentDisplayState];
-[CBAODTransitionController copyRampStatsWithLength:frequency:origin:target:];
-[CBAODTransitionController currentAAPFactor];
-[CBAODTransitionController currentAmmoliteLux];
-[CBAODTransitionController currentDisplayNits];
-[CBAODTransitionController currentFlipBookEntry:];
-[CBAODTransitionController currentTransitionUpdateID];
-[CBAODTransitionController currentTwilightLux];
-[CBAODTransitionController displayON];
-[CBAODTransitionController enableDCPFlipBookUpdates:];
-[CBAODTransitionController flipBookEntryForID:entry:];
-[CBAODTransitionController initAPEndpoint];
-[CBAODTransitionController initColorEffects];
-[CBAODTransitionController initWithContext:andThresholdModule:];
-[CBAODTransitionController initialiseFlipBookWithLength:frequency:lux:];
-[CBAODTransitionController liveUpdates];
-[CBAODTransitionController liveUpdatesOverride];
-[CBAODTransitionController logTransitionParameters:];
-[CBAODTransitionController nitsOverride];
-[CBAODTransitionController processInitialColorMatrixFromState:];
-[CBAODTransitionController rampsDoneCallback:];
-[CBAODTransitionController releaseCallbacks];
-[CBAODTransitionController releaseLastUpdateSwappedTimer];
-[CBAODTransitionController remainingTransitionLength];
-[CBAODTransitionController requestColorRampTransitionStop];
-[CBAODTransitionController requestTransitionStopForIdentifier:];
-[CBAODTransitionController sdrBrightnessProgressCallback:rampContext:];
-[CBAODTransitionController sdrBrightnessProgressCallback:rampContext:profile:];
-[CBAODTransitionController sendCurrentFlipBook];
-[CBAODTransitionController setAmmolite:];
-[CBAODTransitionController setBrightnessFactor:];
-[CBAODTransitionController setCurrentAAPFactor:];
-[CBAODTransitionController setCurrentDisplayNits:];
-[CBAODTransitionController setDisplayON:];
-[CBAODTransitionController setDurationOfEDRRamp:];
-[CBAODTransitionController setLiveUpdatesOverride:];
-[CBAODTransitionController setNitsOverride:];
-[CBAODTransitionController setRemainingTransitionLength:];
-[CBAODTransitionController setTargetWhitepointFromMatrix:];
-[CBAODTransitionController setTwilight:];
-[CBAODTransitionController setWhitepoint:fromMatrix:];
-[CBAODTransitionController shallUpdateWhitepointFrom:target:];
-[CBAODTransitionController sigmoidFunction:];
-[CBAODTransitionController startEternalIndicatorRamp];
-[CBAODTransitionController startTransition:length:forceUpdate:rampDoneCallback:rampCanceledCallback:];
-[CBAODTransitionController startTransition:transitionParameters:rampDoneCallback:rampCanceledCallback:];
-[CBAODTransitionController startTransitionOnDCP:transitionLength:];
-[CBAODTransitionController stopEternalIndicatorRamp];
-[CBAODTransitionController syncLiveStateWithDCP:];
-[CBAODTransitionController transitionDurationFromCurrent:toTarget:];
-[CBAODTransitionController twilight];
-[CBAODTransitionController updateAAPFactor:];
-[CBAODTransitionController updateAllBrightnessFeaturesForced:];
-[CBAODTransitionController updateAmbient:];
-[CBAODTransitionController updateAmmoliteStrength:];
-[CBAODTransitionController updateBrightnessLimit:];
-[CBAODTransitionController updateColorRamp:];
-[CBAODTransitionController updateEDRHeadroom:];
-[CBAODTransitionController updateFlipBookEntryWithAAPFactor:];
-[CBAODTransitionController updateFlipBookEntryWithAmmoliteLux:];
-[CBAODTransitionController updateFlipBookEntryWithAmmoliteStrength:];
-[CBAODTransitionController updateFlipBookEntryWithBrightness:];
-[CBAODTransitionController updateFlipBookEntryWithBrightnessLimit:];
-[CBAODTransitionController updateFlipBookEntryWithTwilightLux:];
-[CBAODTransitionController updateFlipBookEntryWithTwilightStrength:];
-[CBAODTransitionController updateIndicatorBrightness:andLimit:];
-[CBAODTransitionController updateLumaBoostFactor:];
-[CBAODTransitionController updateSDRBrightness:];
-[CBAODTransitionController updateTwilightStrength:];
-[CBAODTransitionController updateWhitePoint:];
```
