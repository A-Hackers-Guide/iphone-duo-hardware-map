# `CAMTorchPattern`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
f _torchLevel;
q __type;
@"CAAnimationGroup" __animationGroup;
d __lastUpdateTime;
d _startTime;
```

## Properties

```
@property (Tq,R,N,V__type) _type;
@property (T@"CAAnimationGroup",R,N,V__animationGroup) _animationGroup;
@property (Td,R,N,V__lastUpdateTime) _lastUpdateTime;
@property (Td,N,V_startTime) startTime;
@property (Tf,R,N,V_torchLevel) torchLevel;
```

## Instance methods

```
-[CAMTorchPattern _type];
-[CAMTorchPattern init];
-[CAMTorchPattern startTime];
-[CAMTorchPattern initWithType:];
-[CAMTorchPattern setStartTime:];
-[CAMTorchPattern torchLevel];
-[CAMTorchPattern updateAtTime:];
-[CAMTorchPattern _animationGroup];
-[CAMTorchPattern _lastUpdateTime];
-[CAMTorchPattern _blinkAnimationGroup];
-[CAMTorchPattern _blinkAnimationWithBeginTime:duration:repeatCount:];
-[CAMTorchPattern _doubleBlinkAnimationGroup];
-[CAMTorchPattern _longPatternAnimationGroup];
-[CAMTorchPattern _patternAnimationWithBeginTime:duration:repeatCount:];
-[CAMTorchPattern _shortPatternAnimationGroup];
-[CAMTorchPattern _updateAnimationGroup];
```
