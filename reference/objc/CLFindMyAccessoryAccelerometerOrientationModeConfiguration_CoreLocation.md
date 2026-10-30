# `CLFindMyAccessoryAccelerometerOrientationModeConfiguration`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
S _sleepDuration_ms;
I _threshold;
```

## Properties

```
@property (TI,N,V_threshold) threshold;
@property (TS,N,V_sleepDuration_ms) sleepDuration_ms;
```

## Class methods

```
+[CLFindMyAccessoryAccelerometerOrientationModeConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration setThreshold:];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration threshold];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration encodeWithCoder:];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration initWithCoder:];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration initWithThreshold:sleepDuration:];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration setSleepDuration_ms:];
-[CLFindMyAccessoryAccelerometerOrientationModeConfiguration sleepDuration_ms];
```
