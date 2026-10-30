# `SBUIAnimationControllerSteppedAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIAnimationControllerAnimator`
- Protocols: `SBViewControllerInteractiveAnimatedTransitioning`
- 1 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBAnimationStepper" _stepper;
```

## Properties

```
@property (T@"SBAnimationStepper",R,N,V_stepper) stepper;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIAnimationControllerSteppedAnimator percentComplete];
-[SBUIAnimationControllerSteppedAnimator stepper];
-[SBUIAnimationControllerSteppedAnimator cancelTransition:withCompletionSpeed:completionCurve:];
-[SBUIAnimationControllerSteppedAnimator finishInteractiveTransition:withCompletionSpeed:completionCurve:];
-[SBUIAnimationControllerSteppedAnimator updateTransition:withPercentComplete:];
-[SBUIAnimationControllerSteppedAnimator initWithAnimationController:];
-[SBUIAnimationControllerSteppedAnimator initWithAnimationController:stepper:];
```
