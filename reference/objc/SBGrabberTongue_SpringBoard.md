# `SBGrabberTongue`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemGestureRecognizerDelegate`
- 21 instance variables, 8 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"UIPanGestureRecognizer" _edgePullGestureRecognizer;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"SBIndirectPanGestureRecognizer" _indirectEdgePullGestureRecognizer;
@"UIView" _tongueContainer;
@"_UIBackdropView" _tongueBackdropView;
@"UIImageView" _tongueChevron;
B _tongueVisible;
B _inPullGesture;
B _inShowTongueGesture;
B _inDismissTongueGesture;
B _inAmbiguousGesture;
B _beganAmbiguousPullGesture;
Q _screenEdge;
Q _systemGestureType;
@"UIView" _containingView;
d _gestureStartTime;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
@"SBWindowScene" _windowScene;
@"<SBGrabberTongueDelegate>" _delegate;
@"NSString" _name;
```

## Properties

```
@property (T@"<SBGrabberTongueDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N,GisVisible) visible;
@property (T@"NSString",C,N,V_name) name;
@property (TQ,R,N,V_screenEdge) screenEdge;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBGrabberTongue _tongueOrPullEnabledForGestureRecognizer:];
-[SBGrabberTongue edgePullGestureRecognizer];
-[SBGrabberTongue dismissWithStyle:animated:];
-[SBGrabberTongue uninstall];
-[SBGrabberTongue _centerOnScreenEdge];
-[SBGrabberTongue initWithDelegate:edge:type:windowScene:];
-[SBGrabberTongue gestureRecognizer:shouldReceiveTouch:];
-[SBGrabberTongue _dismissTongue:];
-[SBGrabberTongue isEdgeLocationInGrabberRegion:];
-[SBGrabberTongue init];
-[SBGrabberTongue _transformForTongueContainer];
-[SBGrabberTongue _frameForVisibleTongueIgnoringBoundingPath];
-[SBGrabberTongue _ambiguousActivationMarginIfHonored];
-[SBGrabberTongue installInView:withColorStyle:];
-[SBGrabberTongue _cancelPendingTongueDismissRequests];
-[SBGrabberTongue dealloc];
-[SBGrabberTongue _frameForTongueWhenVisible:];
-[SBGrabberTongue _pullGestureCanceled:];
-[SBGrabberTongue _handleTapped:];
-[SBGrabberTongue _frameForVisibleTongueConsideringBoundingPath];
-[SBGrabberTongue isVisible];
-[SBGrabberTongue _shouldSecondSwipeDismissTongueWithRecognizer:];
-[SBGrabberTongue _newChevronView];
-[SBGrabberTongue screenEdge];
-[SBGrabberTongue _newBackdropViewWithColorStyle:];
-[SBGrabberTongue indirectEdgePullGestureRecognizer];
-[SBGrabberTongue viewForSystemGestureRecognizer:];
-[SBGrabberTongue _pullGestureEnded:];
-[SBGrabberTongue _dismissTongueWithStyle:animated:];
-[SBGrabberTongue _shouldReceiveTouch:];
-[SBGrabberTongue edgeLocationForTouch:];
-[SBGrabberTongue invalidate];
-[SBGrabberTongue _willDismiss];
-[SBGrabberTongue _didDismiss];
-[SBGrabberTongue _createTongueAndGestureRecognizersIfNecessaryWithColorStyle:];
-[SBGrabberTongue gestureRecognizerShouldBegin:];
-[SBGrabberTongue _pullGestureBegan:];
-[SBGrabberTongue _ambiguousActivationMargin];
-[SBGrabberTongue _willPresentInteractively:];
-[SBGrabberTongue _pullGestureUpdated:];
-[SBGrabberTongue _edgeOrientedVelocityForRecognizer:];
-[SBGrabberTongue presentAnimated:];
-[SBGrabberTongue delegate];
-[SBGrabberTongue _didPresentInteractively:];
-[SBGrabberTongue _distanceFromEdgeForRecognizer:];
-[SBGrabberTongue _createTapGestureRecognizerWithAction:];
-[SBGrabberTongue setName:];
-[SBGrabberTongue _willPresent];
-[SBGrabberTongue _updateCancelsTouchesWithRecognizerIfNeeded:];
-[SBGrabberTongue _handlePullGesture:];
-[SBGrabberTongue presentAnimated:autoDismiss:];
-[SBGrabberTongue _frameForHiddenTongue];
-[SBGrabberTongue _presentTongueAnimated:autoDismiss:];
-[SBGrabberTongue name];
-[SBGrabberTongue distanceFromEdge];
-[SBGrabberTongue _chevronFrameForTongueBounds:];
-[SBGrabberTongue _shouldShowTongueOnFirstSwipeWithRecognizer:];
-[SBGrabberTongue edgeOrientedVelocity];
-[SBGrabberTongue _shouldAllowSecondSwipeWithRecognizer:];
-[SBGrabberTongue _createEdgePullGestureRecognizerWithAction:];
```
