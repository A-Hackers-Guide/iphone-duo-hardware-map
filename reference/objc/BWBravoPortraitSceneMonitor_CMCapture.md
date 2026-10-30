# `BWBravoPortraitSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 49 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
f _backgroundShiftSumFiltered;
f _invalidShiftRatioFiltered;
B _oneShotFocusScanInProgress;
B _focusLocked;
i _numFramesSinceFocusLocked;
B _focusStableAfterStartStreaming;
B _focusAdjusting;
i _lastFocusingMethod;
i _numFramesSinceFocusBecameStable;
B _aeStableAfterStartStreaming;
i _numFramesSinceAEBecameStable;
B _subjectTooCloseMonitoringEnabled;
B _subjectIsTooClose;
f _subjectTooCloseWideFocusDistanceThreshold;
f _subjectTooCloseWideFocusDistanceHysteresisLag;
i _subjectTooCloseLastWideFocusPosition;
B _subjectTooFarMonitoringEnabled;
B _subjectTooFarDistanceThresholdReached;
f _subjectTooFarFocusDistanceThreshold;
f _subjectTooFarFocusDistanceHysteresisLag;
f _subjectTooFarFocusDistanceInfinityThreshold;
B _subjectTooFarUseTeleForFocusDistance;
B _subjectTooFarBackgroundShiftSumIsTooLow;
i _subjectTooFarBackgroundShiftTooLowNumFrames;
f _subjectTooFarBackgroundShiftSumTooLowThreshold;
f _subjectTooFarBackgroundShiftSumTooLowHysteresisLag;
f _subjectTooFarBackgroundShiftRollOffInvalidShiftRatioStart;
f _subjectTooFarBackgroundShiftRollOffInvalidShiftRatioEnd;
i _subjectTooFarLastTeleFocusPosition;
B _sceneTooDarkMonitoringEnabled;
B _sceneIsTooDark;
B _sceneTooDarkExposureThresholdReached;
f _sceneTooDarkGainThreshold;
f _sceneTooDarkGainHysteresisLag;
f _sceneTooDarkInvalidShiftRatioThreshold;
f _sceneTooDarkInvalidShiftRatioHysteresisLag;
B _stageFaceMonitoringEnabled;
B _stageFaceDetected;
i _stageFaceNumberOfFramesSinceLastFace;
B _stageFaceHasBeenSeen;
i _stageFaceNumberOfFramesSinceLastFaceThreshold;
@"NSArray" _stageMostRecentFaces;
B _portraitSceneMonitoringRequiresStageThresholds;
f _stageTooFarFocusDistanceThreshold;
B _stageSubjectTooFarDistanceThresholdReached;
i _stageTooFarBackgroundShiftTooLowNumFrames;
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
+[BWBravoPortraitSceneMonitor initialize];
```

## Instance methods

```
-[BWBravoPortraitSceneMonitor dealloc];
-[BWBravoPortraitSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWBravoPortraitSceneMonitor focusScanDidComplete];
-[BWBravoPortraitSceneMonitor initWithTuningParameters:attachDebugFrameStatistics:];
-[BWBravoPortraitSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWBravoPortraitSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWBravoPortraitSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWBravoPortraitSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWBravoPortraitSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
