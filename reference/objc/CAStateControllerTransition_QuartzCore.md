# `CAStateControllerTransition`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 8 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CAStateController" _controller;
@"CALayer" _layer;
@"CAStateTransition" _transition;
d _beginTime;
d _duration;
f _speed;
@"NSString" _masterKey;
@"NSMutableArray" _animations;
```

## Properties

```
@property (T@"CALayer",R,N,V_layer) layer;
@property (T@"CAStateTransition",R,N,V_transition) transition;
@property (Td,R,N,V_beginTime) beginTime;
@property (Td,R,N,V_duration) duration;
@property (Tf,R,N,V_speed) speed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAStateControllerTransition transition];
-[CAStateControllerTransition animationDidStop:finished:];
-[CAStateControllerTransition layer];
-[CAStateControllerTransition speed];
-[CAStateControllerTransition init];
-[CAStateControllerTransition dealloc];
-[CAStateControllerTransition duration];
-[CAStateControllerTransition invalidate];
-[CAStateControllerTransition removeAnimationFromLayer:forKey:];
-[CAStateControllerTransition addAnimation:];
-[CAStateControllerTransition beginTime];
```
