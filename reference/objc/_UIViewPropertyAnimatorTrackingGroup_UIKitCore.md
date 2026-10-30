# `_UIViewPropertyAnimatorTrackingGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewImplicitlyAnimating`
- 1 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _trackingAnimators;
```

## Properties

```
@property (T@"NSArray",R,N,V_trackingAnimators) trackingAnimators;
@property (Tq,R,N) state;
@property (TB,R,N,GisRunning) running;
@property (TB,N,GisReversed) reversed;
@property (Td,N) fractionComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIViewPropertyAnimatorTrackingGroup setReversed:];
-[_UIViewPropertyAnimatorTrackingGroup setFractionComplete:];
-[_UIViewPropertyAnimatorTrackingGroup isRunning];
-[_UIViewPropertyAnimatorTrackingGroup fractionComplete];
-[_UIViewPropertyAnimatorTrackingGroup pauseAnimation];
-[_UIViewPropertyAnimatorTrackingGroup addAnimations:];
-[_UIViewPropertyAnimatorTrackingGroup isReversed];
-[_UIViewPropertyAnimatorTrackingGroup startAnimation];
-[_UIViewPropertyAnimatorTrackingGroup addCompletion:];
-[_UIViewPropertyAnimatorTrackingGroup continueAnimationWithTimingParameters:durationFactor:];
-[_UIViewPropertyAnimatorTrackingGroup stopAnimation:];
-[_UIViewPropertyAnimatorTrackingGroup finishAnimationAtPosition:];
-[_UIViewPropertyAnimatorTrackingGroup startAnimationAfterDelay:];
-[_UIViewPropertyAnimatorTrackingGroup state];
-[_UIViewPropertyAnimatorTrackingGroup initWithAnimators:];
-[_UIViewPropertyAnimatorTrackingGroup trackingAnimators];
```
