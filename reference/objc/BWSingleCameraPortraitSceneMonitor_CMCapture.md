# `BWSingleCameraPortraitSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 36 instance variables, 6 properties, 9 instance methods, 1 class methods

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
f _numFacesDetectedFiltered;
B _subjectTooCloseMonitoringEnabled;
B _subjectIsTooClose;
f _subjectTooCloseFocusDistanceThreshold;
f _subjectTooCloseFocusDistanceHysteresisLag;
i _subjectTooCloseLastFocusPosition;
B _subjectTooFarMonitoringEnabled;
B _subjectTooFarDistanceThresholdReached;
f _subjectTooFarFocusDistanceThreshold;
f _subjectTooFarFocusDistanceHysteresisLag;
i _subjectTooFarLastFocusPosition;
B _useAPSFocusDistance;
B _sceneTooDarkMonitoringEnabled;
B _sceneIsTooDark;
i _lastSDOFEffectStatus;
f _lastFocusDistance;
@"BWTrackedFace" _currentlyTrackedFace;
B _enabled;
B _portraitSceneMonitoringRequiresStageThresholds;
i _stageFaceNumberOfFramesSinceLastFaceThreshold;
B _stageFaceDetected;
B _stageFaceHasBeenSeen;
i _numberOfFramesSinceLastFace;
i _stageMostRecentFacesCount;
@"NSDictionary" _cinematicVideoFocusRequest;
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
+[BWSingleCameraPortraitSceneMonitor initialize];
```

## Instance methods

```
-[BWSingleCameraPortraitSceneMonitor dealloc];
-[BWSingleCameraPortraitSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWSingleCameraPortraitSceneMonitor focusScanDidComplete];
-[BWSingleCameraPortraitSceneMonitor initWithTuningParameters:attachDebugFrameStatistics:];
-[BWSingleCameraPortraitSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWSingleCameraPortraitSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWSingleCameraPortraitSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWSingleCameraPortraitSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWSingleCameraPortraitSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
