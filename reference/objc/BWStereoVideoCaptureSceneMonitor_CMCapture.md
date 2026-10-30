# `BWStereoVideoCaptureSceneMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _oneShotFocusScanInProgress;
B _sceneTooDarkMonitoringEnabled;
B _subjectTooCloseMonitoringEnabled;
B _sceneIsTooDark;
B _subjectIsTooClose;
f _normalizedSNRThreshold;
i _luxLevelThreshold;
d _focusDistanceThreshold;
d _lastWideFocusDistance;
d _lastSuperWideFocusDistance;
```

## Class methods

```
+[BWStereoVideoCaptureSceneMonitor initialize];
```

## Instance methods

```
-[BWStereoVideoCaptureSceneMonitor dealloc];
-[BWStereoVideoCaptureSceneMonitor focusScanDidComplete];
-[BWStereoVideoCaptureSceneMonitor initWithTuningParametersByPortType:attachDebugFrameStatistics:];
-[BWStereoVideoCaptureSceneMonitor resolveStereoVideoCaptureStatusWithFrameStatistics:sceneFlags:stereoVideoCaptureStatusOut:];
-[BWStereoVideoCaptureSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:];
```
