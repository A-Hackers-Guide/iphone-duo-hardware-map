# `SBSpotlightTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `SBViewControllerInteractiveAnimatedTransitioning`
- 14 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBSystemAnimationSettings" _settings;
@"<SBViewControllerContextTransitioning>" _transitionContext;
d _percentComplete;
d _transitionDuration;
Q _transitionToken;
Q _operation;
@"UIView" _touchSwallowingView;
@"UIView" _containerView;
@"UIView" _searchView;
@"SBSearchBackdropView" _backdropView;
B _ownsBackdropView;
{?="start"{?="value"d"inclusive"B}"end"{?="value"d"inclusive"B}} _pulldownInterval;
@"<SBUISpotlightInitiating>" _initiatingViewController;
@"SPUIRemoteSearchViewController" _spotlightViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSpotlightTransitionAnimator percentComplete];
-[SBSpotlightTransitionAnimator animateTransition:];
-[SBSpotlightTransitionAnimator transitionDuration:];
-[SBSpotlightTransitionAnimator init];
-[SBSpotlightTransitionAnimator settings:changedValueForKey:];
-[SBSpotlightTransitionAnimator supportsRestarting];
-[SBSpotlightTransitionAnimator cancelTransition:withCompletionSpeed:completionCurve:];
-[SBSpotlightTransitionAnimator finishInteractiveTransition:withCompletionSpeed:completionCurve:];
-[SBSpotlightTransitionAnimator updateTransition:withPercentComplete:];
-[SBSpotlightTransitionAnimator _animateInteractiveTransition:];
-[SBSpotlightTransitionAnimator _animateIntoSearch:];
-[SBSpotlightTransitionAnimator _cancelInteractiveTransition:withCompletionSpeed:completionCurve:];
-[SBSpotlightTransitionAnimator _cleanupAfterAnimating:];
-[SBSpotlightTransitionAnimator _finishInteractiveTransition:withCompletionSpeed:completionCurve:];
-[SBSpotlightTransitionAnimator _percentVisibleForPercentComplete:];
-[SBSpotlightTransitionAnimator _prepareToAnimate];
-[SBSpotlightTransitionAnimator _prototypeSettingsChanged];
-[SBSpotlightTransitionAnimator _restoreSpotlightHeaderToInitiatingViewController];
-[SBSpotlightTransitionAnimator _restoreSpotlightHeaderToInitiatingViewControllerForCancellation:];
-[SBSpotlightTransitionAnimator _updateTransitionIntoSearch:percentComplete:];
-[SBSpotlightTransitionAnimator shouldMoveIntoSearch];
-[SBSpotlightTransitionAnimator shouldMoveIntoSearchOnCancel];
```
