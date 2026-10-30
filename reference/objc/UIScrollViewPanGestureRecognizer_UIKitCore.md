# `UIScrollViewPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- Protocols: `_UIScrollEventAsyncDeliverable`
- 17 instance variables, 11 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
: _scrollViewAction;
{CGPoint="x"d"y"d} _reconsideredLockingLocation;
b2 _lastLockingAxis;
b2 _lockingAxis;
b1 _hasParentScrollView;
b1 _caughtDeceleratingScrollView;
b1 _directionalLockEnabled;
b1 _transfersTrackingFromParentScrollView;
b1 _movedAfterCaughtDeceleratingScrollViewButBeganNotYetDelivered;
q _modifierFlags;
q _indirectScrollingState;
B _scrollViewCanScrubWithTouch;
B _activeEventIsDiscrete;
d _translationScaleFactor;
@"UIScrollViewDirectionalPressGestureRecognizer" _directionalPressGestureRecognizer;
d _discreteFastScrollMultiplier;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (TB,N,GisDirectionalLockEnabled) directionalLockEnabled;
@property (TB,R,N,G_caughtDeceleratingScrollView) caughtDeceleratingScrollView;
@property (TB,R,N,G_beganCaughtDeceleratingScrollViewAndMoved) beganCaughtDeceleratingScrollViewAndMoved;
@property (Td,N,V_translationScaleFactor) translationScaleFactor;
@property (T@"UIScrollViewDirectionalPressGestureRecognizer",W,N,V_directionalPressGestureRecognizer) directionalPressGestureRecognizer;
@property (Td,N,G_discreteFastScrollMultiplier,S_setDiscreteFastScrollMultiplier:,V_discreteFastScrollMultiplier) discreteFastScrollMultiplier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScrollViewPanGestureRecognizer translationInView:];
-[UIScrollViewPanGestureRecognizer _hysteresis];
-[UIScrollViewPanGestureRecognizer _caughtDeceleratingScrollView];
-[UIScrollViewPanGestureRecognizer velocityInView:];
-[UIScrollViewPanGestureRecognizer shouldReceiveEvent:];
-[UIScrollViewPanGestureRecognizer _scrollingChangedWithEvent:];
-[UIScrollViewPanGestureRecognizer setAllowedTouchTypes:];
-[UIScrollViewPanGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIScrollViewPanGestureRecognizer _resetGestureRecognizer];
-[UIScrollViewPanGestureRecognizer _shouldReceiveTouch:withEvent:];
-[UIScrollViewPanGestureRecognizer touchesCancelled:withEvent:];
-[UIScrollViewPanGestureRecognizer _convertPoint:toSceneReferenceCoordinatesFromView:];
-[UIScrollViewPanGestureRecognizer scrollView];
-[UIScrollViewPanGestureRecognizer _isGestureType:];
-[UIScrollViewPanGestureRecognizer _scrollViewDidEndZooming];
-[UIScrollViewPanGestureRecognizer setScrollView:];
-[UIScrollViewPanGestureRecognizer _modifierFlags];
-[UIScrollViewPanGestureRecognizer setView:];
-[UIScrollViewPanGestureRecognizer _convertPoint:fromSceneReferenceCoordinatesToView:];
-[UIScrollViewPanGestureRecognizer touchesBegan:withEvent:];
-[UIScrollViewPanGestureRecognizer touchesMoved:withEvent:];
-[UIScrollViewPanGestureRecognizer directionalPressGestureRecognizer];
-[UIScrollViewPanGestureRecognizer initWithTarget:action:];
-[UIScrollViewPanGestureRecognizer setDirectionalPressGestureRecognizer:];
-[UIScrollViewPanGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[UIScrollViewPanGestureRecognizer translationScaleFactor];
-[UIScrollViewPanGestureRecognizer _asyncDeliveryTargetForScrollEvent:];
-[UIScrollViewPanGestureRecognizer _isParentScrollView:consideringEvent:];
-[UIScrollViewPanGestureRecognizer setDelegate:];
-[UIScrollViewPanGestureRecognizer _shouldTryToBeginWithEvent:];
-[UIScrollViewPanGestureRecognizer _beganCaughtDeceleratingScrollViewAndMoved];
-[UIScrollViewPanGestureRecognizer _handleCaughtDeceleratingScrollViewWithEvent:];
-[UIScrollViewPanGestureRecognizer delaysTouchesBegan];
-[UIScrollViewPanGestureRecognizer _canTransferTrackingFromParentPagingScrollView];
-[UIScrollViewPanGestureRecognizer _adjustSceneReferenceLocation:];
-[UIScrollViewPanGestureRecognizer _shouldTransferTrackingFromParentScrollViewForCurrentOffset];
-[UIScrollViewPanGestureRecognizer _discreteFastScrollMultiplier];
-[UIScrollViewPanGestureRecognizer setTranslationScaleFactor:];
-[UIScrollViewPanGestureRecognizer removeTarget:action:];
-[UIScrollViewPanGestureRecognizer _centroidMovedTo:atTime:affectingTranslation:];
-[UIScrollViewPanGestureRecognizer setDirectionalLockEnabled:];
-[UIScrollViewPanGestureRecognizer _allowsBounce];
-[UIScrollViewPanGestureRecognizer _velocityIncludingDiscreteScrollInView:];
-[UIScrollViewPanGestureRecognizer isDirectionalLockEnabled];
-[UIScrollViewPanGestureRecognizer _shouldContinueToWaitToTransferTrackingFromParentScrollView];
-[UIScrollViewPanGestureRecognizer _beginScrollWithEvent:];
-[UIScrollViewPanGestureRecognizer _setDiscreteFastScrollMultiplier:];
```
