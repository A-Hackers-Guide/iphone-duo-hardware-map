# `BWPearlPortraitSceneMonitorV2`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 37 instance variables, 7 properties, 11 instance methods, 1 class methods

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
B _autoSuggestEnabled;
@"BWPortraitAutoSuggest" _autoSuggestMonitor;
B _shallowDepthOfFieldRenderingEnabled;
i _autoSuggestMaxThermalPressureLevel;
i _autoSuggestMaxPeakPowerPressureLevel;
```

## Properties

```
@property (TB,N,V_shallowDepthOfFieldRenderingEnabled) shallowDepthOfFieldRenderingEnabled;
@property (TB,N,V_portraitSceneMonitoringRequiresStageThresholds) portraitSceneMonitoringRequiresStageThresholds;
@property (Tf,R,N) focusDistanceToMaxAllowedFocusDistanceRatio;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPearlPortraitSceneMonitorV2 initialize];
```

## Instance methods

```
-[BWPearlPortraitSceneMonitorV2 dealloc];
-[BWPearlPortraitSceneMonitorV2 focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWPearlPortraitSceneMonitorV2 focusScanDidComplete];
-[BWPearlPortraitSceneMonitorV2 initWithTuningParameters:attachDebugFrameStatistics:portraitAutoSuggestEnabled:shallowDepthOfFieldEnabled:];
-[BWPearlPortraitSceneMonitorV2 portraitSceneMonitoringRequiresStageThresholds];
-[BWPearlPortraitSceneMonitorV2 resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWPearlPortraitSceneMonitorV2 setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWPearlPortraitSceneMonitorV2 setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWPearlPortraitSceneMonitorV2 setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
-[BWPearlPortraitSceneMonitorV2 setShallowDepthOfFieldRenderingEnabled:];
-[BWPearlPortraitSceneMonitorV2 shallowDepthOfFieldRenderingEnabled];
```
