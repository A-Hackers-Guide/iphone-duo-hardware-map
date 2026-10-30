# `CMSpringTrackerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
B fTrackingStarted;
@? fHandler;
```

## Instance methods

```
-[CMSpringTrackerInternal init];
-[CMSpringTrackerInternal dealloc];
-[CMSpringTrackerInternal _teardown];
-[CMSpringTrackerInternal _isTracking];
-[CMSpringTrackerInternal _handleStartStopResponse:handler:];
-[CMSpringTrackerInternal _querySpringDataFromRecord:handler:];
-[CMSpringTrackerInternal _startWithHandler:];
-[CMSpringTrackerInternal _stopWithHandler:];
```
