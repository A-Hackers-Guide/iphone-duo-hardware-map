# `_UIPlatterMenuDynamicsController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPlatterMenuPanningTransformerDelegate`
- 28 instance variables, 34 properties, 99 instance methods, 0 class methods

## Instance variables

```
B _leadingSwipeActionViewSelected;
B _trailingSwipeActionViewSelected;
B _isCurrentlyUnderDirectManipulation;
@"<_UIPlatterMenuDynamicsControllerDelegate>" _delegate;
@"UIView" _containerView;
@"UIView" _platterView;
@"UIView" _menuView;
@"<UIDynamicItem>" _platterItem;
@"_UIPlatterMenuPanningTransformer" _panningLockTransformer;
q _state;
d _leadingSwipeEdgeMultiplier;
d _trailingSwipeEdgeMultiplier;
@"UIDynamicAnimator" _animator;
@"UIDynamicItemBehavior" _menuItemBehavior;
@"UIDynamicItemBehavior" _platterItemBehavior;
@"UIAttachmentBehavior" _platterMenuSlidingAttachmentBehavior;
@"UIAttachmentBehavior" _platterMenuAttachmentBehavior;
@"UIAttachmentBehavior" _gestureAttachmentBehavior;
@"_UIPlatterMenuSnapBehavior" _platterSnapBehavior;
@"_UIPlatterMenuSnapBehavior" _menuPresentedSnapBehavior;
@"_UIPlatterMenuSnapBehavior" _menuDismissedSnapBehavior;
@"UIDynamicItemBehavior" _noRotationBehavior;
@"UIAttachmentBehavior" _menuVerticalLockAttachment;
@"UICollisionBehavior" _platterMenuCollisionBounds;
@"_UIDynamicItemObservingBehavior" _observingBehavior;
q _didPresentCount;
@"_UIStatesFeedbackGenerator" _swipeFeedbackGenerator;
{CGPoint="x"d"y"d} _initialTouchPoint;
```

## Properties

```
@property (T@"<_UIPlatterMenuDynamicsControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_containerView) containerView;
@property (T@"UIView",W,N,V_platterView) platterView;
@property (T@"UIView",W,N,V_menuView) menuView;
@property (T@"<UIDynamicItem>",W,N,V_platterItem) platterItem;
@property (T@"_UIPlatterMenuPanningTransformer",&,N,V_panningLockTransformer) panningLockTransformer;
@property (Tq,N,V_state) state;
@property (T{CGPoint=dd},N,V_initialTouchPoint) initialTouchPoint;
@property (Td,N,V_leadingSwipeEdgeMultiplier) leadingSwipeEdgeMultiplier;
@property (Td,N,V_trailingSwipeEdgeMultiplier) trailingSwipeEdgeMultiplier;
@property (TB,N,V_isCurrentlyUnderDirectManipulation) isCurrentlyUnderDirectManipulation;
@property (T@"UIDynamicAnimator",&,N,V_animator) animator;
@property (T@"UIDynamicItemBehavior",&,N,V_menuItemBehavior) menuItemBehavior;
@property (T@"UIDynamicItemBehavior",&,N,V_platterItemBehavior) platterItemBehavior;
@property (T@"UIAttachmentBehavior",&,N,V_platterMenuSlidingAttachmentBehavior) platterMenuSlidingAttachmentBehavior;
@property (T@"UIAttachmentBehavior",&,N,V_platterMenuAttachmentBehavior) platterMenuAttachmentBehavior;
@property (T@"UIAttachmentBehavior",&,N,V_gestureAttachmentBehavior) gestureAttachmentBehavior;
@property (T@"_UIPlatterMenuSnapBehavior",&,N,V_platterSnapBehavior) platterSnapBehavior;
@property (T@"_UIPlatterMenuSnapBehavior",&,N,V_menuPresentedSnapBehavior) menuPresentedSnapBehavior;
@property (T@"_UIPlatterMenuSnapBehavior",&,N,V_menuDismissedSnapBehavior) menuDismissedSnapBehavior;
@property (T@"UIDynamicItemBehavior",&,N,V_noRotationBehavior) noRotationBehavior;
@property (T@"UIAttachmentBehavior",&,N,V_menuVerticalLockAttachment) menuVerticalLockAttachment;
@property (T@"UICollisionBehavior",&,N,V_platterMenuCollisionBounds) platterMenuCollisionBounds;
@property (T@"_UIDynamicItemObservingBehavior",&,N,V_observingBehavior) observingBehavior;
@property (Tq,N,V_didPresentCount) didPresentCount;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_swipeFeedbackGenerator) swipeFeedbackGenerator;
@property (T{CGVector=dd},R,N) currentTranslation;
@property (T{CGVector=dd},R,N) currentVelocity;
@property (TB,N,V_leadingSwipeActionViewSelected) leadingSwipeActionViewSelected;
@property (TB,N,V_trailingSwipeActionViewSelected) trailingSwipeActionViewSelected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPlatterMenuDynamicsController platterView];
-[_UIPlatterMenuDynamicsController setContainerView:];
-[_UIPlatterMenuDynamicsController setState:];
-[_UIPlatterMenuDynamicsController setPlatterView:];
-[_UIPlatterMenuDynamicsController swipeFeedbackGenerator];
-[_UIPlatterMenuDynamicsController setSwipeFeedbackGenerator:];
-[_UIPlatterMenuDynamicsController setMenuView:];
-[_UIPlatterMenuDynamicsController dealloc];
-[_UIPlatterMenuDynamicsController setAnimator:];
-[_UIPlatterMenuDynamicsController animator];
-[_UIPlatterMenuDynamicsController containerView];
-[_UIPlatterMenuDynamicsController setDelegate:];
-[_UIPlatterMenuDynamicsController currentVelocity];
-[_UIPlatterMenuDynamicsController delegate];
-[_UIPlatterMenuDynamicsController menuView];
-[_UIPlatterMenuDynamicsController state];
-[_UIPlatterMenuDynamicsController centerForCurrentPlatterPosition];
-[_UIPlatterMenuDynamicsController didPresentCount];
-[_UIPlatterMenuDynamicsController isMenuPresented];
-[_UIPlatterMenuDynamicsController resetAnimatorToDefaultBehaviors];
-[_UIPlatterMenuDynamicsController setPlatterItem:];
-[_UIPlatterMenuDynamicsController setTrailingSwipeEdgeMultiplier:];
-[_UIPlatterMenuDynamicsController trailingSwipeActionViewSelected];
-[_UIPlatterMenuDynamicsController _activateFeedbackIfNeeded];
-[_UIPlatterMenuDynamicsController _animateToPlatterDismissedWithDuration:completion:];
-[_UIPlatterMenuDynamicsController _animateToPlatterPresentedWithVelocity:];
-[_UIPlatterMenuDynamicsController _beginInYLockedStatePresented];
-[_UIPlatterMenuDynamicsController _configureAnimator];
-[_UIPlatterMenuDynamicsController _configureFeedbackGenerator];
-[_UIPlatterMenuDynamicsController _deactivateFeedbackIfNeeded];
-[_UIPlatterMenuDynamicsController _fireConfirmFeedbackIfNeededForInitialSelectionState:finalSelectionState:];
-[_UIPlatterMenuDynamicsController _isPlatterInYLockedPosition];
-[_UIPlatterMenuDynamicsController _positionSwipeActionViewsForCurrentPlatterViewPosition];
-[_UIPlatterMenuDynamicsController _stateForPosition:offset:velocity:];
-[_UIPlatterMenuDynamicsController _updateSwipeEdgeMultipliersIfNeededForTouchPosition:];
-[_UIPlatterMenuDynamicsController addBehaviorIfNotPresent:];
-[_UIPlatterMenuDynamicsController beginTransitionWithAnimatorUsingBehaviors:observedItems:stateIfCompleted:];
-[_UIPlatterMenuDynamicsController centerForMenuPresentedRelativeToCurrentPlatter];
-[_UIPlatterMenuDynamicsController currentTranslation];
-[_UIPlatterMenuDynamicsController didBeginPanningWithPoint:];
-[_UIPlatterMenuDynamicsController didEndPanningWithPoint:];
-[_UIPlatterMenuDynamicsController didPanWithPoint:];
-[_UIPlatterMenuDynamicsController gestureAttachmentBehavior];
-[_UIPlatterMenuDynamicsController hasBeenPresented];
-[_UIPlatterMenuDynamicsController initWithContainerView:platterView:menuView:delegate:];
-[_UIPlatterMenuDynamicsController initialTouchPoint];
-[_UIPlatterMenuDynamicsController isCurrentlyUnderDirectManipulation];
-[_UIPlatterMenuDynamicsController isDefaultAnimatorBehavior:];
-[_UIPlatterMenuDynamicsController isMenuPresenting];
-[_UIPlatterMenuDynamicsController isSelectingSwipeAction];
-[_UIPlatterMenuDynamicsController leadingSwipeActionViewSelected];
-[_UIPlatterMenuDynamicsController leadingSwipeEdgeMultiplier];
-[_UIPlatterMenuDynamicsController lockIntoYAxis];
-[_UIPlatterMenuDynamicsController menuCenter];
-[_UIPlatterMenuDynamicsController menuDismissedSnapBehavior];
-[_UIPlatterMenuDynamicsController menuItemBehavior];
-[_UIPlatterMenuDynamicsController menuPresentedSnapBehavior];
-[_UIPlatterMenuDynamicsController menuVerticalLockAttachment];
-[_UIPlatterMenuDynamicsController modifiedOffsetForPosition:offset:touchPosition:axisLock:];
-[_UIPlatterMenuDynamicsController noRotationBehavior];
-[_UIPlatterMenuDynamicsController observingBehavior];
-[_UIPlatterMenuDynamicsController panningLockTransformer];
-[_UIPlatterMenuDynamicsController panningTransformer:didBeginPanToTransformedPosition:];
-[_UIPlatterMenuDynamicsController panningTransformer:didEndPanToTransformedPosition:offsetFromPrevious:velocity:];
-[_UIPlatterMenuDynamicsController panningTransformer:didEnterTransitionNotchForTransformedPosition:];
-[_UIPlatterMenuDynamicsController panningTransformer:didPanToTransformedPosition:offsetFromPrevious:touchPosition:velocity:didChangeAxis:axisLock:];
-[_UIPlatterMenuDynamicsController performActionsAndEnterState:];
-[_UIPlatterMenuDynamicsController performActionsAndEnterState:velocity:underDirectManipulation:];
-[_UIPlatterMenuDynamicsController platterCenter];
-[_UIPlatterMenuDynamicsController platterItem];
-[_UIPlatterMenuDynamicsController platterItemBehavior];
-[_UIPlatterMenuDynamicsController platterMenuAttachmentBehavior];
-[_UIPlatterMenuDynamicsController platterMenuCollisionBounds];
-[_UIPlatterMenuDynamicsController platterMenuSlidingAttachmentBehavior];
-[_UIPlatterMenuDynamicsController platterPanned];
-[_UIPlatterMenuDynamicsController platterSnapBehavior];
-[_UIPlatterMenuDynamicsController resetAnimator];
-[_UIPlatterMenuDynamicsController setDidPresentCount:];
-[_UIPlatterMenuDynamicsController setGestureAttachmentBehavior:];
-[_UIPlatterMenuDynamicsController setInitialTouchPoint:];
-[_UIPlatterMenuDynamicsController setIsCurrentlyUnderDirectManipulation:];
-[_UIPlatterMenuDynamicsController setLeadingSwipeActionViewSelected:];
-[_UIPlatterMenuDynamicsController setLeadingSwipeEdgeMultiplier:];
-[_UIPlatterMenuDynamicsController setMenuDismissedSnapBehavior:];
-[_UIPlatterMenuDynamicsController setMenuItemBehavior:];
-[_UIPlatterMenuDynamicsController setMenuPresentedSnapBehavior:];
-[_UIPlatterMenuDynamicsController setMenuVerticalLockAttachment:];
-[_UIPlatterMenuDynamicsController setNoRotationBehavior:];
-[_UIPlatterMenuDynamicsController setObservingBehavior:];
-[_UIPlatterMenuDynamicsController setPanningLockTransformer:];
-[_UIPlatterMenuDynamicsController setPlatterItemBehavior:];
-[_UIPlatterMenuDynamicsController setPlatterMenuAttachmentBehavior:];
-[_UIPlatterMenuDynamicsController setPlatterMenuCollisionBounds:];
-[_UIPlatterMenuDynamicsController setPlatterMenuSlidingAttachmentBehavior:];
-[_UIPlatterMenuDynamicsController setPlatterSnapBehavior:];
-[_UIPlatterMenuDynamicsController setTrailingSwipeActionViewSelected:];
-[_UIPlatterMenuDynamicsController stopObservingBehavior];
-[_UIPlatterMenuDynamicsController toggleAnimatorDebugState];
-[_UIPlatterMenuDynamicsController trailingSwipeEdgeMultiplier];
```
