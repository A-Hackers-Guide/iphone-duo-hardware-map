# `BWActionCameraSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPortraitSceneMonitor`
- 5 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _oneShotFocusScanInProgress;
B _sceneTooDarkMonitoringEnabled;
@"NSDictionary" _luxThresholdsByPortType;
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
+[BWActionCameraSceneMonitor initialize];
```

## Instance methods

```
-[BWActionCameraSceneMonitor dealloc];
-[BWActionCameraSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWActionCameraSceneMonitor focusScanDidComplete];
-[BWActionCameraSceneMonitor initWithTuningParametersByPortType:videoStabilizationStrength:bravoTelephotoEnabled:attachDebugFrameStatistics:];
-[BWActionCameraSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWActionCameraSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWActionCameraSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWActionCameraSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWActionCameraSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
