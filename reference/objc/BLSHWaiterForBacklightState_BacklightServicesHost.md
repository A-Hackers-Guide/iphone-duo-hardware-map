# `BLSHWaiterForBacklightState`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHWaiterForBacklight`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@? _predicate;
q _backlightState;
```

## Instance methods

```
-[BLSHWaiterForBacklightState backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHWaiterForBacklightState initWithPredicate:];
-[BLSHWaiterForBacklightState isDesiredState:];
-[BLSHWaiterForBacklightState initWithBacklightState:];
-[BLSHWaiterForBacklightState isAlreadyAtDesiredState];
```
