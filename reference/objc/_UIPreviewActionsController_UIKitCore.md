# `_UIPreviewActionsController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPlatterMenuDynamicsControllerDelegate`
- 17 instance variables, 22 properties, 87 instance methods, 1 class methods

## Instance variables

```
B _hasBegun;
@"UIView" _containerView;
@"UIView" _platterView;
@"UIView" _affordanceView;
@"UIImageView" _affordanceImageView;
@"UIViewController" _presentedViewController;
@"<_UIPreviewActionsControllerDelegate>" _delegate;
@"_UIPlatterMenuDynamicsController" _platterDynamicsController;
@"_UIPreviewActionSheetView" _previewActionsView;
@"NSArray" _currentPreviewActionItems;
@"UIPreviewAction" _leadingPreviewAction;
@"UIPreviewAction" _trailingPreviewAction;
@"_UIPreviewQuickActionView" _leadingPreviewActionView;
@"_UIPreviewQuickActionView" _trailingPreviewActionView;
@"_UIStatesFeedbackGenerator" _swipeFeedbackGenerator;
{CGSize="width"d"height"d} _totalPanningTranslation;
{CGPoint="x"d"y"d} _lastPanningLocation;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_platterView) platterView;
@property (T@"UIView",&,N,V_affordanceView) affordanceView;
@property (T@"UIImageView",&,N,V_affordanceImageView) affordanceImageView;
@property (T@"UIViewController",&,N,V_presentedViewController) presentedViewController;
@property (T@"<_UIPreviewActionsControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_hasBegun) hasBegun;
@property (T@"_UIPlatterMenuDynamicsController",&,N,V_platterDynamicsController) platterDynamicsController;
@property (T@"_UIPreviewActionSheetView",&,N,V_previewActionsView) previewActionsView;
@property (T@"NSArray",C,N,V_currentPreviewActionItems) currentPreviewActionItems;
@property (T@"UIPreviewAction",&,N,V_leadingPreviewAction) leadingPreviewAction;
@property (T@"UIPreviewAction",&,N,V_trailingPreviewAction) trailingPreviewAction;
@property (T@"_UIPreviewQuickActionView",&,N,V_leadingPreviewActionView) leadingPreviewActionView;
@property (T@"_UIPreviewQuickActionView",&,N,V_trailingPreviewActionView) trailingPreviewActionView;
@property (T{CGPoint=dd},N,V_lastPanningLocation) lastPanningLocation;
@property (T{CGSize=dd},N,V_totalPanningTranslation) totalPanningTranslation;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_swipeFeedbackGenerator) swipeFeedbackGenerator;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frameForActionView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPreviewActionsController actionsControllerWithContainerView:platterView:presentedViewController:delegate:];
```

## Instance methods

```
-[_UIPreviewActionsController platterView];
-[_UIPreviewActionsController setContainerView:];
-[_UIPreviewActionsController setPlatterView:];
-[_UIPreviewActionsController swipeFeedbackGenerator];
-[_UIPreviewActionsController setSwipeFeedbackGenerator:];
-[_UIPreviewActionsController dealloc];
-[_UIPreviewActionsController containerView];
-[_UIPreviewActionsController setDelegate:];
-[_UIPreviewActionsController delegate];
-[_UIPreviewActionsController _actionsControllerCommonInit];
-[_UIPreviewActionsController _activateFeedbackIfNeeded];
-[_UIPreviewActionsController _applyLayoutAdjustmentsForManagedViewWithPosition:];
-[_UIPreviewActionsController _centerForMenuDismissedForActionSheet:];
-[_UIPreviewActionsController _centerForMenuPresentedForActionSheet:];
-[_UIPreviewActionsController _centerForPlatterWithMenuViewPresentedForActionSheet:];
-[_UIPreviewActionsController _configureFeedbackGenerator];
-[_UIPreviewActionsController _configurePlatterDynamicsController];
-[_UIPreviewActionsController _deactivateFeedbackIfNeeded];
-[_UIPreviewActionsController _disablePlatterController];
-[_UIPreviewActionsController _dismissForSelectedSwipeAction];
-[_UIPreviewActionsController _dismissWithAction:];
-[_UIPreviewActionsController _fireConfirmFeedbackIfNeededForInitialSelectionState:finalSelectionState:];
-[_UIPreviewActionsController _hasPreviewSwipeActions];
-[_UIPreviewActionsController _hasSelectedSwipeAction];
-[_UIPreviewActionsController _hideChromeAndSetAffordanceHidden:];
-[_UIPreviewActionsController _initialPlatterFrame];
-[_UIPreviewActionsController _isSwipeActionVisible];
-[_UIPreviewActionsController _makeAndAddToViewHierarchyPreviewActionSheetForMenuItems:];
-[_UIPreviewActionsController _memoizePreviewActionViews];
-[_UIPreviewActionsController _platterIsInInitialPositionMostly];
-[_UIPreviewActionsController _platterOffsetDistance];
-[_UIPreviewActionsController _presentSubactionsForActionGroup:];
-[_UIPreviewActionsController _previewActionsSheetIsVisible];
-[_UIPreviewActionsController _quickActionSelectionOffset];
-[_UIPreviewActionsController _quickActionsSelectionThresholdForPreviewMenuItemStyle:];
-[_UIPreviewActionsController _setAffordanceAlpha:withDuration:hideOnCompletion:];
-[_UIPreviewActionsController _shouldDismiss];
-[_UIPreviewActionsController _updateAffordanceIfNecessary];
-[_UIPreviewActionsController _updateSwipeActionsState];
-[_UIPreviewActionsController affordanceImageView];
-[_UIPreviewActionsController affordanceView];
-[_UIPreviewActionsController beginPanningAtLocation:];
-[_UIPreviewActionsController centerForMenuDismissed];
-[_UIPreviewActionsController centerForMenuPresented];
-[_UIPreviewActionsController centerForPlatterWithMenuViewDismissed];
-[_UIPreviewActionsController centerForPlatterWithMenuViewPresented];
-[_UIPreviewActionsController currentPreviewActionItems];
-[_UIPreviewActionsController dismissPreviewActionsWithCompletion:];
-[_UIPreviewActionsController endPanningAtLocation:];
-[_UIPreviewActionsController flashScrollAffordance];
-[_UIPreviewActionsController frameForActionView];
-[_UIPreviewActionsController hasBegun];
-[_UIPreviewActionsController initWithContainerView:platterView:presentedViewController:delegate:];
-[_UIPreviewActionsController initialCenterForLeadingSwipeActionView];
-[_UIPreviewActionsController initialCenterForTrailingSwipeActionView];
-[_UIPreviewActionsController lastPanningLocation];
-[_UIPreviewActionsController leadingPreviewAction];
-[_UIPreviewActionsController leadingPreviewActionView];
-[_UIPreviewActionsController leadingSwipeActionView];
-[_UIPreviewActionsController minimumSpacingBetweenPlatterAndMenu];
-[_UIPreviewActionsController platterDynamicsController];
-[_UIPreviewActionsController platterMenuDynamicsController:didMoveSwipeView:toPosition:];
-[_UIPreviewActionsController platterMenuDynamicsControllerDidDismissWithController:];
-[_UIPreviewActionsController platterPanned];
-[_UIPreviewActionsController presentedViewController];
-[_UIPreviewActionsController previewActionsView];
-[_UIPreviewActionsController setAffordanceImageView:];
-[_UIPreviewActionsController setAffordanceView:];
-[_UIPreviewActionsController setCurrentPreviewActionItems:];
-[_UIPreviewActionsController setHasBegun:];
-[_UIPreviewActionsController setLastPanningLocation:];
-[_UIPreviewActionsController setLeadingPreviewAction:];
-[_UIPreviewActionsController setLeadingPreviewActionView:];
-[_UIPreviewActionsController setLeadingSwipeActionViewSelected:];
-[_UIPreviewActionsController setPlatterDynamicsController:];
-[_UIPreviewActionsController setPresentedViewController:];
-[_UIPreviewActionsController setPreviewActionsView:];
-[_UIPreviewActionsController setTotalPanningTranslation:];
-[_UIPreviewActionsController setTrailingPreviewAction:];
-[_UIPreviewActionsController setTrailingPreviewActionView:];
-[_UIPreviewActionsController setTrailingSwipeActionViewSelected:];
-[_UIPreviewActionsController totalPanningTranslation];
-[_UIPreviewActionsController trailingPreviewAction];
-[_UIPreviewActionsController trailingPreviewActionView];
-[_UIPreviewActionsController trailingSwipeActionView];
-[_UIPreviewActionsController translationDidUpdateForPlatterMenuDynamicsController:];
-[_UIPreviewActionsController updatePanningLocation:];
```
