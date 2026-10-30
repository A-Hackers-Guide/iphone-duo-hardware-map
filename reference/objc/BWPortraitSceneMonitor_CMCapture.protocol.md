# `BWPortraitSceneMonitor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB,N) portraitSceneMonitoringRequiresStageThresholds;
@property (Tf,R,N) focusDistanceToMaxAllowedFocusDistanceRatio;
```

## Instance methods

```
-[BWPortraitSceneMonitor focusDistanceToMaxAllowedFocusDistanceRatio];
-[BWPortraitSceneMonitor focusScanDidComplete];
-[BWPortraitSceneMonitor portraitSceneMonitoringRequiresStageThresholds];
-[BWPortraitSceneMonitor resolveSDOFStatusWithSampleBuffer:frameStatisticsByPortType:sceneFlags:flashOrTorchWillBeActive:digitalFlashWillFire:thermalPressureLevel:peakPowerPressureLevel:effectStatus:stagePreviewStatus:];
-[BWPortraitSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
-[BWPortraitSceneMonitor setPortraitSceneMonitoringRequiresStageThresholds:];
-[BWPortraitSceneMonitor setSDOFBackgroundShiftSum:invalidShiftRatio:closeCanonicalDisparityAverage:faceCanonicalDisparityAverages:erodedForegroundRatio:foregroundRatio:occluded:faces:personSegmentationRatio:];
```
