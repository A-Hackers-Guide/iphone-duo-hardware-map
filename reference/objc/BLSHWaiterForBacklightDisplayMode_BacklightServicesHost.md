# `BLSHWaiterForBacklightDisplayMode`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHWaiterForBacklight`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@? _predicate;
q _displayMode;
```

## Instance methods

```
-[BLSHWaiterForBacklightDisplayMode backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHWaiterForBacklightDisplayMode backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHWaiterForBacklightDisplayMode initWithPredicate:];
-[BLSHWaiterForBacklightDisplayMode observesUpdateToDisplayMode];
-[BLSHWaiterForBacklightDisplayMode initWithDisplayMode:];
-[BLSHWaiterForBacklightDisplayMode isAlreadyAtDesiredState];
-[BLSHWaiterForBacklightDisplayMode isDesiredDisplayMode:];
```
