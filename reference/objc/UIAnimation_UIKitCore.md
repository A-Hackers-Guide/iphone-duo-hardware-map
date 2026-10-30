# `UIAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
@ _target;
: _action;
@ _delegate;
@? _completion;
{?="curve"b4} _animationFlags;
d _startTime;
d _duration;
i _state;
@"UIScreen" _screen;
@"NSString" _screenIdentifier;
B _startTimePending;
```

## Instance methods

```
-[UIAnimation setCompletion:];
-[UIAnimation completion];
-[UIAnimation _screen];
-[UIAnimation setProgress:];
-[UIAnimation setAction:];
-[UIAnimation action];
-[UIAnimation initWithTarget:];
-[UIAnimation progressForFraction:];
-[UIAnimation setDelegate:];
-[UIAnimation setAnimationCurve:];
-[UIAnimation delegate];
-[UIAnimation setDuration:];
-[UIAnimation target];
-[UIAnimation state];
-[UIAnimation _screenIdentifier];
-[UIAnimation fractionForTime:];
-[UIAnimation markStart:];
-[UIAnimation markStartPending];
-[UIAnimation markStop];
-[UIAnimation resolvePendingStartTime:];
-[UIAnimation stopAnimation];
```
