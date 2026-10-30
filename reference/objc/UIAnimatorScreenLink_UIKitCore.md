# `UIAnimatorScreenLink`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
^{_UIUpdateSequenceItemInternal=} _updateSequenceItem;
@"CADisplayLink" _displayLink;
@? _updateAction;
S _animationCount;
```

## Properties

```
@property (TS,V_animationCount) animationCount;
```

## Class methods

```
+[UIAnimatorScreenLink startTimerWithScreen:action:];
```

## Instance methods

```
-[UIAnimatorScreenLink animationCount];
-[UIAnimatorScreenLink dealloc];
-[UIAnimatorScreenLink invalidate];
-[UIAnimatorScreenLink setAnimationCount:];
-[UIAnimatorScreenLink onDisplayLink:];
```
