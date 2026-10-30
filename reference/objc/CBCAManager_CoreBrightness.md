# `CBCAManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _displays;
[9f] _currentlySetMatrix;
f _currentlySetScaler;
f _digitalDimmingBrightnessScaler;
```

## Instance methods

```
-[CBCAManager sendNotificationForKey:andValue:];
-[CBCAManager dealloc];
-[CBCAManager handleNotificationForKey:withProperty:];
-[CBCAManager colorRampPropertyHandler:];
-[CBCAManager displayBrightnessPropertyHandler:];
-[CBCAManager initWithCADisplay:andQueue:];
-[CBCAManager nitsThresholdPLCPropertyHandler:];
-[CBCAManager updateDigitalDimmingBrightnessScaler:];
```
