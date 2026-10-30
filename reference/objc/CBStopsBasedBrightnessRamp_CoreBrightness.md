# `CBStopsBasedBrightnessRamp`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
f _start;
f _target;
f _current;
f _rampSpeed;
f _rampTime;
f _startTime;
f _timeOfLastUpdate;
```

## Instance methods

```
-[CBStopsBasedBrightnessRamp target];
-[CBStopsBasedBrightnessRamp currentBrightness];
-[CBStopsBasedBrightnessRamp initWithStartingBrightness:targetBrightness:rampSpeed:andCurrentTime:];
-[CBStopsBasedBrightnessRamp timeOfLastUpdate];
-[CBStopsBasedBrightnessRamp updateRampWithProgress:];
-[CBStopsBasedBrightnessRamp updateRampWithTimestamp:];
```
