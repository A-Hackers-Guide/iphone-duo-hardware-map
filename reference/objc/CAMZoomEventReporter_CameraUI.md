# `CAMZoomEventReporter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
eventRateLimitingInterval;
shouldReportAllChangeEvents;
unfairLock;
latestEvent;
```

## Instance methods

```
-[CAMZoomEventReporter init];
-[CAMZoomEventReporter initWithRateLimit:reportingAllEvents:];
-[CAMZoomEventReporter zoomBeganWithFactor:device:interactionType:];
-[CAMZoomEventReporter zoomChangedToFactor:device:interactionType:];
-[CAMZoomEventReporter zoomChangedToFactor:interactionType:];
-[CAMZoomEventReporter zoomEndedFromSource:];
```
