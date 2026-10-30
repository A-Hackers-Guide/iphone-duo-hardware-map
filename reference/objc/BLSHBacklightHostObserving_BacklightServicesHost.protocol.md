# `BLSHBacklightHostObserving` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSBacklightStateObserving`
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[BLSHBacklightHostObserving backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHBacklightHostObserving backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHBacklightHostObserving backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:];
-[BLSHBacklightHostObserving observesDeactivation];
-[BLSHBacklightHostObserving observesPerformingAllEvents];
-[BLSHBacklightHostObserving backlight:rampingToBrightnessCurve:withDuration:forEvents:abortedEvents:];
-[BLSHBacklightHostObserving backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:];
-[BLSHBacklightHostObserving observesActivation];
-[BLSHBacklightHostObserving backlightHost:willTransitionToState:forEvent:];
-[BLSHBacklightHostObserving observesDidUpdateVisualContents];
-[BLSHBacklightHostObserving backlight:didBlankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHBacklightHostObserving backlight:didCompleteUpdateToFlipbookState:forEvent:];
-[BLSHBacklightHostObserving backlight:willUnblankToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHBacklightHostObserving observesBlankingChanges];
-[BLSHBacklightHostObserving observesRampingToBrightnessCurve];
-[BLSHBacklightHostObserving observesUpdateToDisplayMode];
```
