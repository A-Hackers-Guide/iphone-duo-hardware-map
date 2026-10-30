# `BWBravoPortraitSceneMonitorV2`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 59 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _numberOfFramesWithStableFocusThreshold;
B _oneShotFocusScanInProgress;
B _focusLocked;
i _numFramesSinceFocusLocked;
i _numFramesSinceFocusBecameStable;
B _focusHasBeenAttainedAfterStart;
i _numFramesSinceFocusFirstAttainedStability;
B _focusIsStationaryBeyondThreshold;
B _subjectTooCloseMonitoringEnabled;
B _subjectTooCloseMonitoringForcingWideLens;
f _subjectTooCloseFocusDistanceThreshold;
f _subjectTooCloseHysteresis;
B _subjectIsTooClose;
B _subjectTooClosePreviousFrame;
B _subjectTooFarMonitoringEnabled;
f _subjectTooFarFocusDistanceThreshold;
f _subjectTooFarBackgroundShiftSumTooLowThreshold;
B _subjectTooFarDistanceThresholdReached;
f _subjectTooFarDistanceThresholdHysteresis;
B _backgroundShiftSumTooLowThresholdReached;
f _subjectTooFarBackGroundShiftSumIsTooLowHysteresis;
f _jasperDistanceAtFocus;
B _subjectIsTooFarDigitalFlash;
B _subjectIsTooFarForStageDigitalFlash;
f _subjectTooFarDigitalFlashThreshold;
f _stageTooFarDigitalFlashThreshold;
f _sceneTooDarkGainThresholdHard;
f _jasperDistanceAtFocusSmoothingFactor;
B _subjectIsTooFar;
B _subjectIsTooFarForStage;
B _subjectIsTooFarForStageNoFaces;
B _deliveryOfShiftsHasStarted;
f _backgroundShiftSumSmoothed;
f _backgroundShiftSumSmoothingTrend;
f _backgroundShiftSumSmoothingFactor;
f _backgroundShiftSumSmoothingTrendUpdateFactor;
f _invalidShiftRatioSmoothed;
f _invalidShiftRatioSmoothingFactor;
B _sceneTooDarkMonitoringEnabled;
f _sceneTooDarkGainThreshold;
f _sceneTooDarkAEAverageAETargetFractionThreshold;
f _sceneTooDarkAEAverageAETargetFractionThresholdHysteresisLag;
B _sceneIsTooDark;
B _stageFaceMonitoringEnabled;
i _stageFaceNumberOfFramesSinceLastFace;
B _stageFaceHasBeenSeen;
i _stageFaceNumberOfFramesSinceLastFaceThreshold;
@"NSArray" _stageMostRecentFaces;
B _portraitSceneMonitoringRequiresStageThresholds;
B _stageTooFarMonitoringEnabled;
f _stageTooFarFocusDistanceThreshold;
B _stageTooFarDistanceThresholdReached;
f _stageTooFarDistanceThresholdHysteresis;
B _stageBackgroundShiftSumTooLowThresholdReached;
f _stageTooFarBackgroundShiftSumTooLowThreshold;
f _stageTooFarBackGroundShiftSumIsTooLowHysteresis;
B _stageTooFarBackgroundShiftSumNoFacesIsTooLow;
f _stageTooFarBackgroundShiftSumNoFacesThreshold;
i _lastSDOFEffectStatus;
```

## Properties

```
@property (TB,N,V_portraitSceneMonitoringRequiresStageThresholds) portraitSceneMonitoringRequiresStageThresholds;
@property (Tf,R,N) focusDistanceToMaxAllowedFocusDistanceRatio;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWBravoPortraitSceneMonitorV2 initialize];
```

## Instance methods

```
-[BWBravoPortraitSceneMonitorV2 dealloc];
-[BWBravoPortraitSceneMonitorV2 focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWBravoPortraitSceneMonitorV2 focusScanDidComplete];
-[BWBravoPortraitSceneMonitorV2 initWithTuningParameters:attachDebugFrameStatistics:];
-[BWBravoPortraitSceneMonitorV2 portraitSceneMonitoringRequiresStageThresholds];
-[BWBravoPortraitSceneMonitorV2 resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWBravoPortraitSceneMonitorV2 setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWBravoPortraitSceneMonitorV2 setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWBravoPortraitSceneMonitorV2 setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
