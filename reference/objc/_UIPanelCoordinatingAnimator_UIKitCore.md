# `_UIPanelCoordinatingAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewPropertyAnimator`
- Protocols: `UIViewControllerTransitionCoordinator`, `UIViewControllerTransitionCoordinatorContext`
- 5 instance variables, 16 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _wasCancelled;
B _isInStartAnimation;
@"NSMutableArray" _clientCompletions;
@"NSMutableArray" _lateAnimations;
@"UIView" _containerView;
```

## Properties

```
@property (T@"UIView",W,N,V_containerView) containerView;
@property (TB,R,N,GisAnimated) animated;
@property (Tq,R,N) presentationStyle;
@property (TB,R,N) initiallyInteractive;
@property (TB,R,N) isInterruptible;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N,GisCancelled) cancelled;
@property (Td,R,N) transitionDuration;
@property (Td,R,N) percentComplete;
@property (Td,R,N) completionVelocity;
@property (Tq,R,N) completionCurve;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPanelCoordinatingAnimator _runCompletions:finished:];
-[_UIPanelCoordinatingAnimator startAnimation];
-[_UIPanelCoordinatingAnimator stopAnimation:];
-[_UIPanelCoordinatingAnimator setContainerView:];
-[_UIPanelCoordinatingAnimator completionVelocity];
-[_UIPanelCoordinatingAnimator _sendPanelCoordinationCompletions];
-[_UIPanelCoordinatingAnimator percentComplete];
-[_UIPanelCoordinatingAnimator animateAlongsideTransitionInView:animation:completion:];
-[_UIPanelCoordinatingAnimator viewControllerForKey:];
-[_UIPanelCoordinatingAnimator animateAlongsideTransition:completion:];
-[_UIPanelCoordinatingAnimator viewForKey:];
-[_UIPanelCoordinatingAnimator isAnimated];
-[_UIPanelCoordinatingAnimator notifyWhenInteractionEndsUsingBlock:];
-[_UIPanelCoordinatingAnimator initiallyInteractive];
-[_UIPanelCoordinatingAnimator notifyWhenInteractionChangesUsingBlock:];
-[_UIPanelCoordinatingAnimator isInteractive];
-[_UIPanelCoordinatingAnimator presentationStyle];
-[_UIPanelCoordinatingAnimator isCancelled];
-[_UIPanelCoordinatingAnimator transitionDuration];
-[_UIPanelCoordinatingAnimator containerView];
-[_UIPanelCoordinatingAnimator targetTransform];
-[_UIPanelCoordinatingAnimator completionCurve];
```
