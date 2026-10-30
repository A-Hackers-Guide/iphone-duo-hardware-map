# `UIAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _animations;
d _lastUpdateTime;
@"NSMutableDictionary" _animatorScreenLinks;
```

## Class methods

```
+[UIAnimator enableAnimation];
+[UIAnimator disableAnimation];
+[UIAnimator sharedAnimator];
```

## Instance methods

```
-[UIAnimator stopAnimation:];
-[UIAnimator init];
-[UIAnimator dealloc];
-[UIAnimator removeAnimationsForTarget:];
-[UIAnimator addAnimation:withDuration:start:];
-[UIAnimator _markStartOfAnimation:requestedStartTime:];
-[UIAnimator _advanceAnimationsOnScreenWithIdentifier:withTimestamp:];
-[UIAnimator addAnimations:withDuration:start:];
-[UIAnimator _startAnimation:withStartTime:];
-[UIAnimator removeAnimationsForTarget:ofKind:];
-[UIAnimator _isRunningAnimation:];
-[UIAnimator startAnimation:];
-[UIAnimator _addAnimation:withDuration:start:startTime:];
```
