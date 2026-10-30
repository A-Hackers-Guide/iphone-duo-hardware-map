# `BWPearlPortraitSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 32 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _numberOfFramesToWaitForAEAndLTMToStabilize;
f _sdofDepthQualitySmoothingFactor;
f _luxLevelSmoothingFactor;
i _numberOfDisabledFramesInARow;
i _numberOfFramesToStayEnabledThreshold;
S _sdofTooBrightLuxLevelThreshold;
S _sdofTooBrightMaxLuxLevelThreshold;
f _sdofTooBrightDepthQualityMinThreshold;
f _sdofDepthQualityKCount;
f _sdofTooCloseDepthDistanceThreshold;
f _sdofTooFarDepthDistanceThreshold;
f _sdofTooBrightTooFarDepthDistanceThreshold;
i _sdofNumberOfFramesSinceLastFaceThreshold;
f _stageTooBrightDepthQualityThreshold;
f _stageTooCloseDepthDistanceThreshold;
f _stageTooFarDepthDistanceThreshold;
f _stageBackgroundTooFarDepthQualityThreshold;
S _stageBackgroundTooFarLuxLevelThreshold;
i _stageFaceNumberOfFramesSinceLastFaceThreshold;
f _closeDepthDistanceAverage;
f _sdofDepthQuality;
f _sdofDepthQualityFiltered;
f _stageDepthQuality;
f _luxLevelFiltered;
B _aeStableAfterStartStreaming;
i _sdofNumFramesSinceAEBecameStable;
B _portraitSceneMonitoringRequiresStageThresholds;
B _depthSensorOccluded;
B _stageFaceDetected;
i _numberOfFramesSinceLastFace;
B _stageFaceHasBeenSeen;
i _stageMostRecentFacesCount;
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
+[BWPearlPortraitSceneMonitor initialize];
```

## Instance methods

```
-[BWPearlPortraitSceneMonitor dealloc];
-[BWPearlPortraitSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWPearlPortraitSceneMonitor focusScanDidComplete];
-[BWPearlPortraitSceneMonitor initWithTuningParameters:attachDebugFrameStatistics:];
-[BWPearlPortraitSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWPearlPortraitSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWPearlPortraitSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWPearlPortraitSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWPearlPortraitSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
