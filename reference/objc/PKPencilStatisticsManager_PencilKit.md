# `PKPencilStatisticsManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 0 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<PKRunningStat, std::default_delete<PKRunningStat>>=""{?="__ptr_"^{PKRunningStat}}} _intentionalHoverStats;
B _hasStarted;
d _accumulatedHoverDuration;
d _accumulatedOnScreenDuration;
@"NSString" _toolName;
d _startOfSessionTimestamp;
Q _numberOfHoverEventsInEdge;
Q _numberOfHoverEventsInExterior;
Q _totalNumberOfHoverEvents;
Q _doubleTapsInRange;
Q _doubleTapsOutsideRange;
d _intentionalToolPreviewDuration;
d _intentionalHoverDuration;
@"NSString" _allowedBundleID;
Q _activePencilMinutes;
```

## Class methods

```
+[PKPencilStatisticsManager allowedBundleIDFromBundleID:];
+[PKPencilStatisticsManager isAllowedBundleID:];
```
