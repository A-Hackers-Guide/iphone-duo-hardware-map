# `BWBravoStreamSelector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 82 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureStream" _wideStream;
@"BWFigVideoCaptureStream" _teleStream;
@"BWFigVideoCaptureStream" _superWideStream;
f _teleMaxAEGain;
f _teleAEGainHysteresisLag;
B _teleAEHysteresisUseEIT;
f _teleMaxEIT;
f _teleMinTeleToWideEITThresholdPercentage;
f _teleMaxTeleToWideEITThresholdPercentage;
f _teleToWideFocusDistance;
f _wideToTeleFocusDistance;
i _teleMaxSubsequentFramesAtMaxGain;
i _teleMaxSubsequentFramesAtMaxEIT;
B _teleSwitchBasedOnExposureAndFocusTargetOffsetEnabled;
B _teleSwitchBasedOnFocusTargetOffsetInRestrictedModeEnabled;
B _teleExposureLimitsEnabled;
f _wideToSuperWideFocusDistance;
f _superWideToWideFocusDistance;
f _superWideMaximumAETargetOffset;
f _superWideMaximumAETargetOffsetHysteresisLag;
i _superWideToWideNumberOfConsecutiveFramesWithMaximumAETargetOffset;
i _superWideToWideNumberOfConsecutiveFramesWithMaximumAETargetOffsetThreshold;
B _superWideAllowedInAutoFlashScenes;
d _digitalFlashMinTeleToWideEITThreshold;
d _digitalFlashMaxTeleToWideEITThreshold;
d _digitalFlashMinTeleToWideEITThresholdWithHumansPresent;
d _digitalFlashMaxTeleToWideEITThresholdWithHumansPresent;
i _digitalFlashTeleToWideNumberOfConsecutiveFramesWithHumanPresentThreshold;
B _digitalFlashAdjustEITForTargetOffsetAndBias;
B _digitalFlashEITTargetOffsetThresholdsEnabled;
d _digitalFlashMinTeleToWideEITTargetOffsetThreshold;
d _digitalFlashMaxTeleToWideEITTargetOffsetThreshold;
d _digitalFlashTripodMinTeleToWideEITTargetOffsetThreshold;
d _digitalFlashTripodMaxTeleToWideEITTargetOffsetThreshold;
d _digitalFlashTeleToWideEITTargetOffsetHysteresisLag;
B _afRecommendedPrimaryPortTypeForWideTeleAutoSwitchEnabled;
B _afRecommendedPrimaryPortTypeForWideSuperWideAutoSwitchEnabled;
I _afMaxFocusPositionStepForStableStatus;
B _afHigherFPSDuringConvergenceEnabled;
@"BWFigVideoCaptureStream" _currentMasterStream;
@"BWFigVideoCaptureStream" _recommendedMasterStream;
{?="selectionBehavior"q"restrictedSelectionConditions"Q"lockedPortType"^{__CFString}} _selectionConfiguration;
{?="selectionBehavior"q"restrictedSelectionConditions"Q"lockedPortType"^{__CFString}} _pendingSelectionConfiguration;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pendingSelectionConfigurationLock;
@"BWFigVideoCaptureStream" _slaveStreamBlockingFocusAndExposureStability;
i _lastSelectionReason;
@"NSArray" _lastPotentialMasterStreams;
@"NSArray" _lastEligibleFallbackPortTypes;
@"BWFigVideoCaptureStream" _preferredMasterStreamIgnoringEligibleFallbackPortTypes;
B _allowSwitchesWithFineMovement;
f _previousZoomFactor;
q _timeOfLastZoomFactorChange;
q _timeOfLastPortTypeMadeEligibleByZoom;
@"NSString" _lastPortTypeMadeEligibleByZoom;
q _timeOfLastFocusModeChange;
q _timeOfLastExposureModeChange;
B _waitingForSlaveFocusAfterZoomChange;
i _teleMaxGainReachedCounter;
i _teleMaxEITReachedCounter;
i _numberOfConsecutiveFramesWithHumans;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _eligibleFallbackPortTypesLock;
@"NSArray" _eligibleFallbackPortTypes;
@"NSArray" _supportedFallbackPortTypes;
f _minLuxLevelChangeForSceneChange;
f _maxLuxLevelForSceneChangeMonitoring;
d _digitalFlashMinEITPercentageChangeForSceneChange;
f _minFocusDistanceChangeForSceneChange;
B _resetSceneChangeMonitoring;
B _sceneChangeDetected;
i _initialLuxLevel;
d _initialEIT;
f _initialFocusDistance;
i _lastDigitalFlashMode;
B _superWideWaitForStableFocusOnce;
{?="value"q"timescale"i"flags"I"epoch"q} _superWideFirstFrameReceivedTime;
i _lastSuperWideLogicalLensFocusPosition;
B _superWideLogicalLensFocusPositionChangedOnce;
I _superWideLogicalLensFocusPositionChangedTimeoutInMilliSeconds;
B _superWideFocusIsStableOnce;
f _exposureRangeLowForRecommendedMasterSwitch;
f _exposureRangeHighForRecommendedMasterSwitch;
Q _switchDelayReasons;
```

## Properties

```
@property (TB,R,N) superWideAutoSwitchingSupported;
@property (Tf,R,N,V_wideToSuperWideFocusDistance) wideToSuperWideFocusDistance;
@property (Tf,R,N,V_superWideToWideFocusDistance) superWideToWideFocusDistance;
@property (Tf,N) teleMaxAEGain;
@property (Tf,N) teleMaxEIT;
@property (T{?=qQ^{__CFString}},N) selectionConfiguration;
@property (T@"NSArray",C,N) eligibleFallbackPortTypes;
@property (T@"BWFigVideoCaptureStream",R,N,V_slaveStreamBlockingFocusAndExposureStability) slaveStreamBlockingFocusAndExposureStability;
@property (T@"BWFigVideoCaptureStream",R,N,V_preferredMasterStreamIgnoringEligibleFallbackPortTypes) preferredMasterStreamIgnoringEligibleFallbackPortTypes;
@property (T@"BWFigVideoCaptureStream",R,N,V_recommendedMasterStream) recommendedMasterStream;
@property (Ti,R,N,V_lastSelectionReason) lastSelectionReason;
@property (TQ,N,V_switchDelayReasons) switchDelayReasons;
```

## Class methods

```
+[BWBravoStreamSelector initialize];
```

## Instance methods

```
-[BWBravoStreamSelector teleMaxAEGain];
-[BWBravoStreamSelector superWideToWideFocusDistance];
-[BWBravoStreamSelector resetWithZoomFactor:currentMasterStream:];
-[BWBravoStreamSelector telephotoLimitsReachedForFrameStatisticsByPortType:];
-[BWBravoStreamSelector dealloc];
-[BWBravoStreamSelector teleMaxEIT];
-[BWBravoStreamSelector lastSelectionReason];
-[BWBravoStreamSelector recommendMasterStreamUsingCurrentMasterStream:frameStatisticsByPortType:zoomFactor:isAutoFlashScene:digitalFlashMode:isStationary:detectedObjects:cameraControlsStatisticsMasterStream:];
-[BWBravoStreamSelector setEligibleFallbackPortTypes:];
-[BWBravoStreamSelector eligibleFallbackPortTypes];
-[BWBravoStreamSelector setTeleMaxAEGain:];
-[BWBravoStreamSelector setTeleMaxEIT:];
-[BWBravoStreamSelector preferredMasterStreamIgnoringEligibleFallbackPortTypes];
-[BWBravoStreamSelector selectionConfiguration];
-[BWBravoStreamSelector setSelectionConfiguration:];
-[BWBravoStreamSelector slaveStreamBlockingFocusAndExposureStability];
-[BWBravoStreamSelector setSwitchDelayReasons:];
-[BWBravoStreamSelector focusModeDidChange];
-[BWBravoStreamSelector recommendedMasterStream];
-[BWBravoStreamSelector exposureModeDidChange];
-[BWBravoStreamSelector wideToSuperWideFocusDistance];
-[BWBravoStreamSelector superWideAutoSwitchingSupported];
-[BWBravoStreamSelector initWithStreamSelectionAttributes:wideStream:teleStream:superWideStream:cameraCalibrationValid:];
-[BWBravoStreamSelector preferredMasterPortTypeForFrameStatisticsByPortType:zoomFactor:];
-[BWBravoStreamSelector switchDelayReasons];
```
