# `SBUISwitcherAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIWorkspaceAnimationController`
- Protocols: `SBUIAnimationControllerObserver`
- 4 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _interruptible;
@"<SBSwitcherContentViewControlling>" _contentViewController;
@? _animationBlock;
@"<NSObject>" _activityToken;
```

## Properties

```
@property (T@"<SBSwitcherContentViewControlling>",W,N,V_contentViewController) contentViewController;
@property (T@?,C,N,V_animationBlock) animationBlock;
@property (T@"<NSObject>",&,N,V_activityToken) activityToken;
@property (TB,N,G_isInterruptible,S_setInterruptible:,V_interruptible) _interruptible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUISwitcherAnimationController _windowScene];
-[SBUISwitcherAnimationController animationSettings];
-[SBUISwitcherAnimationController _didComplete];
-[SBUISwitcherAnimationController setContentViewController:];
-[SBUISwitcherAnimationController _setInterruptible:];
-[SBUISwitcherAnimationController setAnimationBlock:];
-[SBUISwitcherAnimationController animationBlock];
-[SBUISwitcherAnimationController contentViewController];
-[SBUISwitcherAnimationController isReasonableMomentToInterrupt];
-[SBUISwitcherAnimationController shouldResignActiveForAnimation];
-[SBUISwitcherAnimationController _updatePPTsForAnimationStart];
-[SBUISwitcherAnimationController setActivityToken:];
-[SBUISwitcherAnimationController _addSignpostsAndEndAnimationTrackingForAnimationEnd];
-[SBUISwitcherAnimationController isInterruptible];
-[SBUISwitcherAnimationController _startAnimation];
-[SBUISwitcherAnimationController _updatePPTsForAnimationEnd];
-[SBUISwitcherAnimationController _addSignpostsAndBeginAnimationTrackingForAnimationStart];
-[SBUISwitcherAnimationController initWithWorkspaceTransitionRequest:contentViewController:childAnimationControllers:animationBlock:];
-[SBUISwitcherAnimationController animationControllerDidFinishAnimation:];
-[SBUISwitcherAnimationController _isInterruptible];
-[SBUISwitcherAnimationController _previousLayoutState];
-[SBUISwitcherAnimationController activityToken];
-[SBUISwitcherAnimationController _layoutState];
```
