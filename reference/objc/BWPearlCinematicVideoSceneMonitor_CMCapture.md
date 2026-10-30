# `BWPearlCinematicVideoSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 8 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _numberOfFramesToWaitForAEAndLTMToStabilize;
B _aeStableAfterStartStreaming;
i _sdofNumFramesSinceAEBecameStable;
B _sceneTooDarkMonitoringEnabled;
i _sceneTooDarkLuxThreshold;
B _sceneIsTooDark;
B _occluded;
B portraitSceneMonitoringRequiresStageThresholds;
```

## Properties

```
@property (TB,N,VportraitSceneMonitoringRequiresStageThresholds) portraitSceneMonitoringRequiresStageThresholds;
@property (Tf,R,N) focusDistanceToMaxAllowedFocusDistanceRatio;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPearlCinematicVideoSceneMonitor initialize];
```

## Instance methods

```
-[BWPearlCinematicVideoSceneMonitor dealloc];
-[BWPearlCinematicVideoSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWPearlCinematicVideoSceneMonitor focusScanDidComplete];
-[BWPearlCinematicVideoSceneMonitor initWithTuningParameters:attachDebugFrameStatistics:];
-[BWPearlCinematicVideoSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWPearlCinematicVideoSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWPearlCinematicVideoSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWPearlCinematicVideoSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWPearlCinematicVideoSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
