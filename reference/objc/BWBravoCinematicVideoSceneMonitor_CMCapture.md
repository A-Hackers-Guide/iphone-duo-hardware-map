# `BWBravoCinematicVideoSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 5 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _oneShotFocusScanInProgress;
B _sceneTooDarkMonitoringEnabled;
i _sceneTooDarkLuxThreshold;
B _sceneIsTooDark;
B _portraitSceneMonitoringRequiresStageThresholds;
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
+[BWBravoCinematicVideoSceneMonitor initialize];
```

## Instance methods

```
-[BWBravoCinematicVideoSceneMonitor dealloc];
-[BWBravoCinematicVideoSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWBravoCinematicVideoSceneMonitor focusScanDidComplete];
-[BWBravoCinematicVideoSceneMonitor initWithTuningParameters:attachDebugFrameStatistics:];
-[BWBravoCinematicVideoSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWBravoCinematicVideoSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWBravoCinematicVideoSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWBravoCinematicVideoSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWBravoCinematicVideoSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
