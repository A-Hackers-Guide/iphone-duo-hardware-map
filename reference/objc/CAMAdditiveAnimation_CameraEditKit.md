# `CAMAdditiveAnimation`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 15 instance methods, 2 class methods

## Instance variables

```
d __toValue;
d __fromValue;
d __duration;
@"CAMediaTimingFunction" __curve;
@"CAMAdditiveAnimation" __fromAnimation;
d __startTime;
d __lastTime;
```

## Properties

```
@property (Td,R,N,V__toValue) _toValue;
@property (Td,N,V__fromValue) _fromValue;
@property (Td,R,N,V__duration) _duration;
@property (T@"CAMediaTimingFunction",R,N,V__curve) _curve;
@property (T@"CAMAdditiveAnimation",&,N,V__fromAnimation) _fromAnimation;
@property (Td,N,S_setStartTime:,V__startTime) _startTime;
@property (Td,N,S_setLastTime:,V__lastTime) _lastTime;
@property (Td,R,N) value;
@property (TB,R,N,GisFinished) finished;
```

## Class methods

```
+[CAMAdditiveAnimation animationToValue:fromAnimation:duration:curve:];
+[CAMAdditiveAnimation animationToValue:fromValue:duration:curve:];
```

## Instance methods

```
-[CAMAdditiveAnimation _startTime];
-[CAMAdditiveAnimation _duration];
-[CAMAdditiveAnimation isFinished];
-[CAMAdditiveAnimation value];
-[CAMAdditiveAnimation _curve];
-[CAMAdditiveAnimation _setStartTime:];
-[CAMAdditiveAnimation description];
-[CAMAdditiveAnimation _lastTime];
-[CAMAdditiveAnimation _setLastTime:];
-[CAMAdditiveAnimation updateWithTimestamp:];
-[CAMAdditiveAnimation _fromAnimation];
-[CAMAdditiveAnimation _fromValue];
-[CAMAdditiveAnimation _toValue];
-[CAMAdditiveAnimation set_fromAnimation:];
-[CAMAdditiveAnimation set_fromValue:];
```
