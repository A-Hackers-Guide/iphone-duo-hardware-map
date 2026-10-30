# `CAMAnalyticsSessionEvent`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAnalyticsEvent`
- 38 instance variables, 39 properties, 98 instance methods, 2 class methods

## Instance variables

```
B __inCameraRoll;
B __mrcDetectionEnabled;
B __textDetectionEnabled;
B __hadActiveCall;
B __reducedResourceUsageActive;
@"CAMCaptureCapabilities" __capabilities;
@"NSString" __hostProcess;
d __startTime;
@"NSString" __firstCaptureMode;
@"NSString" __firstCaptureDevicePosition;
d __cameraRollStartTime;
d __cameraRollTotalTime;
q __cameraRollInteraction;
d __previewStartTime;
d __firstCaptureStartTime;
@"NSMutableDictionary" __captureCountsByMode;
@"NSMutableDictionary" __captureCountsByMediaType;
Q __totalZoomInteractions;
Q __totalFocusInteractions;
Q __totalFocusLockInteractions;
Q __totalPortraitLightingChanges;
@"NSString" __currentPose;
@"NSString" __firstPose;
Q __totalPoseTransitions;
Q __totalVisualIntelligenceActions;
Q __totalCaptures;
Q __totalTextInteractions;
Q __totalMRCInteractions;
@"NSSet" __availableCaptureModes;
@"CAMCallStatusMonitor" __callStatusMonitor;
@"NSString" __prewarmLaunchReason;
q __firstConfiguredMode;
q __firstConfiguredDevice;
q __smudgeDetectionStatus;
q __smudgeDetectionUserNotificationStatus;
Q __reducedResourceRequestCount;
d __reducedResourceStartTime;
d __reducedResourceTotalDuration;
```

## Properties

```
@property (T@"CAMCaptureCapabilities",R,N,V__capabilities) _capabilities;
@property (T@"NSString",R,N,V__hostProcess) _hostProcess;
@property (Td,R,N,V__startTime) _startTime;
@property (T@"NSString",&,N,V__firstCaptureMode) _firstCaptureMode;
@property (T@"NSString",&,N,V__firstCaptureDevicePosition) _firstCaptureDevicePosition;
@property (Td,N,V__cameraRollStartTime) _cameraRollStartTime;
@property (Td,N,V__cameraRollTotalTime) _cameraRollTotalTime;
@property (TB,N,G_isInCameraRoll,S_setInCameraRoll:,V__inCameraRoll) _inCameraRoll;
@property (Tq,N,V__cameraRollInteraction) _cameraRollInteraction;
@property (Td,N,V__previewStartTime) _previewStartTime;
@property (Td,N,V__firstCaptureStartTime) _firstCaptureStartTime;
@property (T@"NSMutableDictionary",R,N,V__captureCountsByMode) _captureCountsByMode;
@property (T@"NSMutableDictionary",R,N,V__captureCountsByMediaType) _captureCountsByMediaType;
@property (TQ,N,V__totalZoomInteractions) _totalZoomInteractions;
@property (TQ,N,V__totalFocusInteractions) _totalFocusInteractions;
@property (TQ,N,V__totalFocusLockInteractions) _totalFocusLockInteractions;
@property (TQ,N,V__totalPortraitLightingChanges) _totalPortraitLightingChanges;
@property (T@"NSString",C,N,V__currentPose) _currentPose;
@property (T@"NSString",C,N,V__firstPose) _firstPose;
@property (TQ,N,V__totalPoseTransitions) _totalPoseTransitions;
@property (TQ,N,V__totalVisualIntelligenceActions) _totalVisualIntelligenceActions;
@property (TQ,N,V__totalCaptures) _totalCaptures;
@property (TQ,N,V__totalTextInteractions) _totalTextInteractions;
@property (TQ,N,V__totalMRCInteractions) _totalMRCInteractions;
@property (TB,R,N,V__mrcDetectionEnabled) _mrcDetectionEnabled;
@property (TB,R,N,V__textDetectionEnabled) _textDetectionEnabled;
@property (T@"NSSet",C,N,V__availableCaptureModes) _availableCaptureModes;
@property (TB,N,V__hadActiveCall) _hadActiveCall;
@property (T@"CAMCallStatusMonitor",R,N,V__callStatusMonitor) _callStatusMonitor;
@property (T@"NSString",&,N,V__prewarmLaunchReason) _prewarmLaunchReason;
@property (Tq,N,V__firstConfiguredMode) _firstConfiguredMode;
@property (Tq,N,V__firstConfiguredDevice) _firstConfiguredDevice;
@property (Tq,N,V__smudgeDetectionStatus) _smudgeDetectionStatus;
@property (Tq,N,V__smudgeDetectionUserNotificationStatus) _smudgeDetectionUserNotificationStatus;
@property (TB,N,V__reducedResourceUsageActive) _reducedResourceUsageActive;
@property (TQ,N,V__reducedResourceRequestCount) _reducedResourceRequestCount;
@property (Td,N,V__reducedResourceStartTime) _reducedResourceStartTime;
@property (Td,N,V__reducedResourceTotalDuration) _reducedResourceTotalDuration;
@property (TB,R,N) didCapture;
```

## Class methods

```
+[CAMAnalyticsSessionEvent _bucketCaptureCount:];
+[CAMAnalyticsSessionEvent _incrementDictionaryCount:forKey:];
```

## Instance methods

```
-[CAMAnalyticsSessionEvent _startTime];
-[CAMAnalyticsSessionEvent publish];
-[CAMAnalyticsSessionEvent set_firstCaptureStartTime:];
-[CAMAnalyticsSessionEvent didStartPreview];
-[CAMAnalyticsSessionEvent didPrewarmWithReason:];
-[CAMAnalyticsSessionEvent didPresentCameraRoll];
-[CAMAnalyticsSessionEvent didDetectSmudgedLensForDevicePosition:didNotifyUser:];
-[CAMAnalyticsSessionEvent _firstPose];
-[CAMAnalyticsSessionEvent _totalPoseTransitions];
-[CAMAnalyticsSessionEvent didCaptureWithRequest:currentConfiguration:];
-[CAMAnalyticsSessionEvent _accumulateReducedResourceDuration];
-[CAMAnalyticsSessionEvent _reducedResourceTotalDuration];
-[CAMAnalyticsSessionEvent set_totalFocusLockInteractions:];
-[CAMAnalyticsSessionEvent set_reducedResourceUsageActive:];
-[CAMAnalyticsSessionEvent set_firstCaptureMode:];
-[CAMAnalyticsSessionEvent _firstConfiguredMode];
-[CAMAnalyticsSessionEvent set_totalPortraitLightingChanges:];
-[CAMAnalyticsSessionEvent set_previewStartTime:];
-[CAMAnalyticsSessionEvent _callStatusMonitor];
-[CAMAnalyticsSessionEvent initWithCapabilities:availableCaptureModes:currentCaptureMode:currentCaptureDevice:callStatusMonitor:mrcDetectionEnabled:textDetectionEnabled:];
-[CAMAnalyticsSessionEvent set_firstPose:];
-[CAMAnalyticsSessionEvent _totalZoomInteractions];
-[CAMAnalyticsSessionEvent _smudgeDetectionUserNotificationStatus];
-[CAMAnalyticsSessionEvent _totalPortraitLightingChanges];
-[CAMAnalyticsSessionEvent _mrcDetectionEnabled];
-[CAMAnalyticsSessionEvent _textDetectionEnabled];
-[CAMAnalyticsSessionEvent _handleCallStatusMonitorDidChangeCallActive:];
-[CAMAnalyticsSessionEvent didDismissCameraRoll];
-[CAMAnalyticsSessionEvent _hadActiveCall];
-[CAMAnalyticsSessionEvent didUpdateSystemPrefersReducedResourceUsage:];
-[CAMAnalyticsSessionEvent set_firstCaptureDevicePosition:];
-[CAMAnalyticsSessionEvent didFocusLockInteraction];
-[CAMAnalyticsSessionEvent _cameraRollTotalTime];
-[CAMAnalyticsSessionEvent set_smudgeDetectionStatus:];
-[CAMAnalyticsSessionEvent set_cameraRollTotalTime:];
-[CAMAnalyticsSessionEvent set_firstConfiguredMode:];
-[CAMAnalyticsSessionEvent set_totalCaptures:];
-[CAMAnalyticsSessionEvent didCapture];
-[CAMAnalyticsSessionEvent didCaptureTimelapseWithConfiguration:];
-[CAMAnalyticsSessionEvent _firstCaptureMode];
-[CAMAnalyticsSessionEvent set_totalFocusInteractions:];
-[CAMAnalyticsSessionEvent _bucketCaptureCountForMediaType:];
-[CAMAnalyticsSessionEvent _resolveSmudgeDetectionDevicePosition:forDevicePosition:];
-[CAMAnalyticsSessionEvent _smudgeDetectionStatus];
-[CAMAnalyticsSessionEvent _cameraRollInteraction];
-[CAMAnalyticsSessionEvent _totalCaptures];
-[CAMAnalyticsSessionEvent set_cameraRollInteraction:];
-[CAMAnalyticsSessionEvent set_totalPoseTransitions:];
-[CAMAnalyticsSessionEvent _incrementCaptureForGraphConfiguration:analyticsMediaType:];
-[CAMAnalyticsSessionEvent _stringForSmudgeDetectionDevicePosition:];
-[CAMAnalyticsSessionEvent _previewStartTime];
-[CAMAnalyticsSessionEvent set_reducedResourceRequestCount:];
-[CAMAnalyticsSessionEvent eventName];
-[CAMAnalyticsSessionEvent _currentPose];
-[CAMAnalyticsSessionEvent _totalTextInteractions];
-[CAMAnalyticsSessionEvent set_totalMRCInteractions:];
-[CAMAnalyticsSessionEvent _totalFocusLockInteractions];
-[CAMAnalyticsSessionEvent _captureCountsByMediaType];
-[CAMAnalyticsSessionEvent setFirstConfiguredCaptureMode:captureDevice:];
-[CAMAnalyticsSessionEvent _totalMRCInteractions];
-[CAMAnalyticsSessionEvent _firstCaptureDevicePosition];
-[CAMAnalyticsSessionEvent didChangePortraitLighting];
-[CAMAnalyticsSessionEvent _cameraRollStartTime];
-[CAMAnalyticsSessionEvent didPerformVisualIntelligenceAction];
-[CAMAnalyticsSessionEvent _totalVisualIntelligenceActions];
-[CAMAnalyticsSessionEvent set_availableCaptureModes:];
-[CAMAnalyticsSessionEvent set_totalTextInteractions:];
-[CAMAnalyticsSessionEvent _isInCameraRoll];
-[CAMAnalyticsSessionEvent _captureCountsByMode];
-[CAMAnalyticsSessionEvent didFocusInteraction];
-[CAMAnalyticsSessionEvent _availableCaptureModes];
-[CAMAnalyticsSessionEvent set_firstConfiguredDevice:];
-[CAMAnalyticsSessionEvent _totalFocusInteractions];
-[CAMAnalyticsSessionEvent set_prewarmLaunchReason:];
-[CAMAnalyticsSessionEvent _bucketCaptureCountForMode:];
-[CAMAnalyticsSessionEvent set_totalZoomInteractions:];
-[CAMAnalyticsSessionEvent updateForLocationController:];
-[CAMAnalyticsSessionEvent _reducedResourceUsageActive];
-[CAMAnalyticsSessionEvent set_reducedResourceTotalDuration:];
-[CAMAnalyticsSessionEvent _setInCameraRoll:];
-[CAMAnalyticsSessionEvent set_smudgeDetectionUserNotificationStatus:];
-[CAMAnalyticsSessionEvent _endSession];
-[CAMAnalyticsSessionEvent set_cameraRollStartTime:];
-[CAMAnalyticsSessionEvent didZoomInteraction:];
-[CAMAnalyticsSessionEvent set_hadActiveCall:];
-[CAMAnalyticsSessionEvent set_totalVisualIntelligenceActions:];
-[CAMAnalyticsSessionEvent didChangePose:isYoinked:isSplitScreen:];
-[CAMAnalyticsSessionEvent _prewarmLaunchReason];
-[CAMAnalyticsSessionEvent _hostProcess];
-[CAMAnalyticsSessionEvent _reducedResourceStartTime];
-[CAMAnalyticsSessionEvent _firstCaptureStartTime];
-[CAMAnalyticsSessionEvent set_reducedResourceStartTime:];
-[CAMAnalyticsSessionEvent countEventsFromAnalyticsVisionSession:];
-[CAMAnalyticsSessionEvent _reducedResourceRequestCount];
-[CAMAnalyticsSessionEvent _firstConfiguredDevice];
-[CAMAnalyticsSessionEvent _capabilities];
-[CAMAnalyticsSessionEvent _launchEventWithinReasonableTimeInterval];
-[CAMAnalyticsSessionEvent set_currentPose:];
```
