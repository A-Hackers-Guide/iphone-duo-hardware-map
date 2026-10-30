# `SBDeviceMotionDetector`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CMMotionManager" _motionManager;
B _started;
@"SBDeviceMotionVector" _gravity;
@"SBDeviceMotionVector" _rotationRate;
@"NSTimer" _stopTimer;
```

## Properties

```
@property (T@"SBDeviceMotionVector",R,N) gravity;
@property (T@"SBDeviceMotionVector",R,N) rotationRate;
```

## Instance methods

```
-[SBDeviceMotionDetector init];
-[SBDeviceMotionDetector stop];
-[SBDeviceMotionDetector gravity];
-[SBDeviceMotionDetector rotationRate];
-[SBDeviceMotionDetector startWithTimeout:];
-[SBDeviceMotionDetector _initWithGravity:rotationRate:];
```
