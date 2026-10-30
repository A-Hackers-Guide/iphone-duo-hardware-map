# `SBUIAnimationPropertyAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBViewControllerAnimatedTransitioning`
- 6 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _completionBlocks;
B _wasStarted;
Q _reverseCount;
@"UIViewPropertyAnimator" _propertyAnimator;
d _duration;
@? _generator;
```

## Properties

```
@property (T@?,R,C,N,V_generator) generator;
@property (T@"UIViewPropertyAnimator",R,N,V_propertyAnimator) propertyAnimator;
@property (Td,R,N,V_duration) duration;
@property (TB,R,N) isReversed;
@property (TB,R,N) wasReversed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIAnimationPropertyAnimator generator];
-[SBUIAnimationPropertyAnimator isReversed];
-[SBUIAnimationPropertyAnimator addCompletion:];
-[SBUIAnimationPropertyAnimator animateTransition:];
-[SBUIAnimationPropertyAnimator transitionDuration:];
-[SBUIAnimationPropertyAnimator duration];
-[SBUIAnimationPropertyAnimator propertyAnimator];
-[SBUIAnimationPropertyAnimator cancelTransition:withCompletionSpeed:completionCurve:];
-[SBUIAnimationPropertyAnimator _executeGenerator:];
-[SBUIAnimationPropertyAnimator initWithPropertyAnimator:duration:];
-[SBUIAnimationPropertyAnimator initWithPropertyAnimatorGenerator:];
-[SBUIAnimationPropertyAnimator prepareToRunAnimation:];
-[SBUIAnimationPropertyAnimator reverseAnimation];
-[SBUIAnimationPropertyAnimator wasReversed];
```
