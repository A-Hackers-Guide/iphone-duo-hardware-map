# `CAMAnalyticsLaunchAggregator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _waitingForNewLaunch;
q _mode;
q _devicePosition;
i _modeOrDevicePositionChangeCount;
B _hasConfiguredMode;
B _warmLaunch;
B _sessionRunning;
B _sessionInterrupted;
B _applicationBackgrounded;
i _runtimeErrorCount;
q _willEnterForegroundHostTimeMicroseconds;
q _prewarmHostTimeMicroseconds;
@"NSString" _prewarmReason;
B _prewarmedLaunch;
q _firstGraphBuildHostTimeMicroseconds;
q _lastGraphBuildHostTimeMicroseconds;
i _graphBuildCount;
B _graphBuildingForPrewarming;
@"NSNumber" _memoryStatusLevel;
@"NSNumber" _thermalLevel;
q _previewStartedHostTimeMicroseconds;
B _viewfinderClosedDueToSession;
q _endedViewfinderClosedDueToSessionHostTimeMicroseconds;
B _didDisplayFirstPreviewFrame;
q _didDisplayFirstPreviewFrameHostTimeMicroseconds;
```

## Class methods

```
+[CAMAnalyticsLaunchAggregator sharedInstance];
```

## Instance methods

```
-[CAMAnalyticsLaunchAggregator _reset];
-[CAMAnalyticsLaunchAggregator applicationDidEnterBackground];
-[CAMAnalyticsLaunchAggregator applicationWillEnterForeground];
-[CAMAnalyticsLaunchAggregator didStartRunning];
-[CAMAnalyticsLaunchAggregator _checkLaunchCompletionAndReportIfNeeded];
-[CAMAnalyticsLaunchAggregator _clearSessionStats];
-[CAMAnalyticsLaunchAggregator _reportLaunchEvent];
-[CAMAnalyticsLaunchAggregator cancelLaunchTelemetry];
-[CAMAnalyticsLaunchAggregator didBeginGraphBuild:];
-[CAMAnalyticsLaunchAggregator didConfigureMode:devicePosition:];
-[CAMAnalyticsLaunchAggregator didDisplayFirstPreviewFrame:];
-[CAMAnalyticsLaunchAggregator didPrewarmWithNotificationPayload:];
-[CAMAnalyticsLaunchAggregator didStartPreviewing:];
-[CAMAnalyticsLaunchAggregator didStopRunningWithNotificationPayload:];
-[CAMAnalyticsLaunchAggregator interruptedForReason:];
-[CAMAnalyticsLaunchAggregator interruptionEnded];
-[CAMAnalyticsLaunchAggregator receivedSessionRuntimeError];
-[CAMAnalyticsLaunchAggregator viewfinderClosedDueToSession:];
```
