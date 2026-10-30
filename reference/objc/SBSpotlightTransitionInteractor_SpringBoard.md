# `SBSpotlightTransitionInteractor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBViewControllerInteractiveTransitioning`
- 4 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<SBViewControllerContextTransitioning>" _transitionContext;
@"<UIViewControllerAnimatedTransitioning>" _animator;
d _completionSpeed;
q _completionCurve;
```

## Properties

```
@property (Td,N,V_completionSpeed) completionSpeed;
@property (Tq,N,V_completionCurve) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSpotlightTransitionInteractor init];
-[SBSpotlightTransitionInteractor startInteractiveTransition:];
-[SBSpotlightTransitionInteractor finishInteractiveTransition];
-[SBSpotlightTransitionInteractor cancelTransition];
-[SBSpotlightTransitionInteractor completionCurve];
-[SBSpotlightTransitionInteractor completionSpeed];
-[SBSpotlightTransitionInteractor initWithAnimator:];
-[SBSpotlightTransitionInteractor setCompletionCurve:];
-[SBSpotlightTransitionInteractor setCompletionSpeed:];
-[SBSpotlightTransitionInteractor updateTransition:];
```
