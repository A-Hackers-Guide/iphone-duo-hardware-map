# `CMSwimTrackerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
B fStartedUpdates;
@? fHandler;
Q fStrokeCountOffset;
d fDistanceOffset;
Q fLapCountOffset;
d fActiveTime;
Q fSegmentCountOffset;
```

## Instance methods

```
-[CMSwimTrackerInternal init];
-[CMSwimTrackerInternal dealloc];
-[CMSwimTrackerInternal _teardown];
-[CMSwimTrackerInternal _handleUpdates:];
-[CMSwimTrackerInternal _querySWOLFSummaryWithSessionID:handler:];
-[CMSwimTrackerInternal _querySwimUpdatesFromRecord:handler:];
-[CMSwimTrackerInternal _resetOffsets];
-[CMSwimTrackerInternal _startUpdatesFromRecord:handler:];
-[CMSwimTrackerInternal _stopUpdates];
```
