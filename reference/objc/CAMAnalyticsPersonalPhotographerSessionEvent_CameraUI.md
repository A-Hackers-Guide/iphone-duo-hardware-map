# `CAMAnalyticsPersonalPhotographerSessionEvent`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAnalyticsEvent`
- 7 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _startSource;
d _sessionStartTime;
q _autoCaptureCount;
q _manualCaptureCount;
d _sessionEndTime;
q _sessionEndReason;
B _populatedSessionEndReason;
```

## Instance methods

```
-[CAMAnalyticsPersonalPhotographerSessionEvent publish];
-[CAMAnalyticsPersonalPhotographerSessionEvent eventName];
-[CAMAnalyticsPersonalPhotographerSessionEvent incrementAutoCaptureCount];
-[CAMAnalyticsPersonalPhotographerSessionEvent incrementManualCaptureCount];
-[CAMAnalyticsPersonalPhotographerSessionEvent populateSessionEndReason:];
-[CAMAnalyticsPersonalPhotographerSessionEvent populateSessionEndTime];
-[CAMAnalyticsPersonalPhotographerSessionEvent populateSessionStartTimeWithSource:];
```
