# `CMSkiTrackerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
B fStartedUpdates;
@"CMSkiData" fMostRecentRecord;
@? fHandler;
@? fLiveUpdateHandler;
d fRunDistanceOffset;
d fRunElevationDescendedOffset;
```

## Instance methods

```
-[CMSkiTrackerInternal init];
-[CMSkiTrackerInternal dealloc];
-[CMSkiTrackerInternal _teardown];
-[CMSkiTrackerInternal _handleUpdates:];
-[CMSkiTrackerInternal _queryUpdatesFromRecord:handler:];
-[CMSkiTrackerInternal _startLiveUpdatesWithHandler:];
-[CMSkiTrackerInternal _startUpdatesFromRecord:handler:];
-[CMSkiTrackerInternal _stopLiveUpdates];
-[CMSkiTrackerInternal _stopUpdates];
```
