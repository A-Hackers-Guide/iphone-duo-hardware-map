# `SBBarSwipeAffordanceView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `SBHomeGrabberDelegate`, `SBSystemGestureRecognizerDelegate`, `SBHomeGestureInteractionDelegate`, `SBHomeGesturePanGestureRecognizerContextDelegate`, `SBFBarSwipeBehaviorDelegate`, `CSBarSwipeAffordanceViewProtocol`
- 10 instance variables, 14 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"SBFBarSwipeBehavior" _barSwipeBehavior;
@"SBHomeGestureInteraction" _homeGestureInteraction;
@"SBSystemGestureManager" _gestureManager;
B _active;
B _homeAffordanceHidden;
B _allowsTouchesToPassThrough;
@"<SBBarSwipeAffordanceDelegate>" _delegate;
@"SBKeyboardHomeAffordanceAssertion" _keyboardHomeAffordanceAssertion;
@"SBHomeGrabberView" _grabberView;
```

## Properties

```
@property (T@"SBHomeGrabberView",R,N,V_grabberView) grabberView;
@property (Tq,N) feedbackType;
@property (T@"<SBBarSwipeAffordanceDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N) pointerClickDelegate;
@property (TB,N,GisActive,V_active) active;
@property (Tq,D,N) colorBias;
@property (TB,N) ignoresLuminance;
@property (TB,N,GisHomeAffordanceHidden,V_homeAffordanceHidden) homeAffordanceHidden;
@property (TB,N,V_allowsTouchesToPassThrough) allowsTouchesToPassThrough;
@property (T@"SBKeyboardHomeAffordanceAssertion",&,N,V_keyboardHomeAffordanceAssertion) keyboardHomeAffordanceAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBarSwipeAffordanceView didAddSubview:];
-[SBBarSwipeAffordanceView _activate];
-[SBBarSwipeAffordanceView feedbackType];
-[SBBarSwipeAffordanceView barSwipeBehaviorActionPerformed:];
-[SBBarSwipeAffordanceView isTrackingHomeGestureOfType:];
-[SBBarSwipeAffordanceView setPointerClickDelegate:];
-[SBBarSwipeAffordanceView colorBias];
-[SBBarSwipeAffordanceView _deactivate];
-[SBBarSwipeAffordanceView allowsTouchesToPassThrough];
-[SBBarSwipeAffordanceView setColorBias:];
-[SBBarSwipeAffordanceView setIgnoresLuminance:];
-[SBBarSwipeAffordanceView removeObserver:];
-[SBBarSwipeAffordanceView setAllowsTouchesToPassThrough:];
-[SBBarSwipeAffordanceView setFeedbackType:];
-[SBBarSwipeAffordanceView pointerClickDelegate];
-[SBBarSwipeAffordanceView layoutSubviews];
-[SBBarSwipeAffordanceView hitTest:withEvent:];
-[SBBarSwipeAffordanceView setActive:];
-[SBBarSwipeAffordanceView _unhideHomeAffordanceAnimationSettings];
-[SBBarSwipeAffordanceView homeGestureInteractionBegan:];
-[SBBarSwipeAffordanceView ignoresLuminance];
-[SBBarSwipeAffordanceView viewForSystemGestureRecognizer:];
-[SBBarSwipeAffordanceView barSwipeBehavior:didUpdateAdditionalEdgeSpacing:];
-[SBBarSwipeAffordanceView grabberView];
-[SBBarSwipeAffordanceView addObserver:];
-[SBBarSwipeAffordanceView sizeThatFits:];
-[SBBarSwipeAffordanceView homeGestureInteractionChanged:];
-[SBBarSwipeAffordanceView setDelegate:];
-[SBBarSwipeAffordanceView isHomeAffordanceHidden];
-[SBBarSwipeAffordanceView setKeyboardHomeAffordanceAssertion:];
-[SBBarSwipeAffordanceView shouldAllowThinStyleForHomeGrabberView:];
-[SBBarSwipeAffordanceView additionalEdgeSpacingForHomeGrabberView:];
-[SBBarSwipeAffordanceView _updateHomeAffordanceVisibility];
-[SBBarSwipeAffordanceView delegate];
-[SBBarSwipeAffordanceView homeGestureInteractionEnded:];
-[SBBarSwipeAffordanceView keyboardHomeAffordanceAssertion];
-[SBBarSwipeAffordanceView homeGestureInteraction:systemGestureTypeForType:];
-[SBBarSwipeAffordanceView touchInterfaceOrientationForHomeGesturePanGestureRecognizer:];
-[SBBarSwipeAffordanceView initWithFrame:systemGestureManager:enableGestures:];
-[SBBarSwipeAffordanceView shouldAllowAutoHideForHomeGrabberView:];
-[SBBarSwipeAffordanceView customScreenEdgePanGestureRecognizerForHomeGestureInteraction:];
-[SBBarSwipeAffordanceView homeGestureInteractionCancelled:];
-[SBBarSwipeAffordanceView isActive];
-[SBBarSwipeAffordanceView _effectiveOrientationAccountingForTransforms];
-[SBBarSwipeAffordanceView setHomeAffordanceHidden:];
-[SBBarSwipeAffordanceView _runBlockOnObservers:];
-[SBBarSwipeAffordanceView _hideHomeAffordanceAnimationSettings];
```
