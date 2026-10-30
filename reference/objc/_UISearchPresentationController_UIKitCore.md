# `_UISearchPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- Protocols: `_UIPassthroughScrollInteractionDelegate`, `_UISearchControllerPresenting`
- 8 instance variables, 18 properties, 63 instance methods, 1 class methods

## Instance variables

```
@"UISearchController" _searchController;
@"_UISearchPresentationAssistant" _assistant;
@"UIView" _placeholderView;
@"NSMapTable" _excisedSearchBarConstraitMap;
@"NSMapTable" _placeholderConstraitMap;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _finalFrameForContainerView;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
{?="searchBarWasTableHeaderView"b1"excisedSearchBarDuringPresentation"b1"searchBarWantedAutolayoutBeforeExcision"b1"searchHostedInNavigationBar"b1} _controllerFlags;
```

## Properties

```
@property (T@"UIView",R,N) backgroundObscuringView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,&,N) searchBarContainerView;
@property (TB,R,N) shouldAccountForStatusBar;
@property (Td,R,N) statusBarAdjustment;
@property (TB,R,N) searchBarToBecomeTopAttached;
@property (TB,R,N) resultsUnderlapsSearchBar;
@property (TB,R,N) searchBarCanContainScopeBar;
@property (TB,R,N) searchBarShouldClipToBounds;
@property (Td,R,N) resultsControllerContentOffset;
@property (T@"UIPresentationController<_UISearchControllerPresenting>",R,N) adaptivePresentationController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_finalFrameForContainerView) finalFrameForContainerView;
@property (TB,R,N) animatorShouldLayoutPresentationViews;
@property (TB,R,N) forceObeyNavigationBarInsets;
@property (TQ,R,N) edgeForHidingNavigationBar;
```

## Class methods

```
+[_UISearchPresentationController shouldExciseSearchBar:duringPresentationWithPresenter:];
```

## Instance methods

```
-[_UISearchPresentationController _shouldRespectDefinesPresentationContext];
-[_UISearchPresentationController presentationTransitionDidEnd:];
-[_UISearchPresentationController _presentationControllerForTraitCollection:];
-[_UISearchPresentationController setContentVisible:];
-[_UISearchPresentationController dealloc];
-[_UISearchPresentationController adaptivePresentationController];
-[_UISearchPresentationController _shouldKeepCurrentFirstResponder];
-[_UISearchPresentationController searchBarContainerView];
-[_UISearchPresentationController statusBarAdjustment];
-[_UISearchPresentationController passthroughScrollInteractionDidRecognize:atLocation:];
-[_UISearchPresentationController passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UISearchPresentationController initWithPresentedViewController:presentingViewController:];
-[_UISearchPresentationController viewWillTransitionToSize:withTransitionCoordinator:];
-[_UISearchPresentationController frameOfPresentedViewInContainerView];
-[_UISearchPresentationController resultsControllerContentOffset];
-[_UISearchPresentationController shouldAccountForStatusBar];
-[_UISearchPresentationController shouldPresentInFullscreen];
-[_UISearchPresentationController _createVisualStyleForProvider:];
-[_UISearchPresentationController _shouldDisableInteractionDuringTransitions];
-[_UISearchPresentationController searchBarToBecomeTopAttached];
-[_UISearchPresentationController _isEffectivelyFullScreen];
-[_UISearchPresentationController dismissalTransitionWillBegin];
-[_UISearchPresentationController dismissalTransitionDidEnd:];
-[_UISearchPresentationController presentationTransitionWillBegin];
-[_UISearchPresentationController containerViewWillLayoutSubviews];
-[_UISearchPresentationController _constraintCopyOfConstraint:replaceItem:withItem:];
-[_UISearchPresentationController _dismissalTransitionWithSearchBarHostedByNavBarDidEnd:];
-[_UISearchPresentationController _dismissalTransitionWithSearchBarHostedByNavBarWillBegin];
-[_UISearchPresentationController _dismissalTransitionWithSearchBarNotHostedByNavBarDidEnd:];
-[_UISearchPresentationController _dismissalTransitionWithSearchBarNotHostedByNavBarWillBegin];
-[_UISearchPresentationController _exciseSearchBarFromCurrentContext];
-[_UISearchPresentationController _keyboardDidRequestDismissal];
-[_UISearchPresentationController _layoutPresentationWithSize:transitionCoordinator:];
-[_UISearchPresentationController _occludedFrameOfPresentedViewInContainerView];
-[_UISearchPresentationController _placeSearchBarBackIntoOriginalContext];
-[_UISearchPresentationController _presentationTransitionWithSearchBarHostedByNavBarDidEnd:];
-[_UISearchPresentationController _presentationTransitionWithSearchBarHostedByNavBarWillBegin];
-[_UISearchPresentationController _presentationTransitionWithSearchBarNotHostedByNavBarDidEnd:];
-[_UISearchPresentationController _presentationTransitionWithSearchBarNotHostedByNavBarWillBegin];
-[_UISearchPresentationController _presentedViewControllerForPresentationController:traitCollection:];
-[_UISearchPresentationController _requiresDeferralToCoordinateWithNavigationTransitionAnimated:];
-[_UISearchPresentationController _shouldAnchorSearchTextFieldToKeyboard];
-[_UISearchPresentationController _shouldUsePassthroughInteractionForDismissal];
-[_UISearchPresentationController _transitionFromDidEnd];
-[_UISearchPresentationController _transitionFromWillBegin];
-[_UISearchPresentationController _transitionToDidEnd];
-[_UISearchPresentationController _transitionToPresentationController:withTransitionCoordinator:];
-[_UISearchPresentationController _transitionToWillBegin];
-[_UISearchPresentationController _updateContainerFinalFrameForNonExcisedSearchBar];
-[_UISearchPresentationController _updatePresentingViewControllerContentScrollViewWithOffsets:transitionCoordinator:];
-[_UISearchPresentationController _visibleRefreshControlHeightForTableView:];
-[_UISearchPresentationController adaptivePresentationStyle];
-[_UISearchPresentationController animatorShouldLayoutPresentationViews];
-[_UISearchPresentationController backgroundObscuringView];
-[_UISearchPresentationController contentSizeCategoryOrLegibilityWeightChanged];
-[_UISearchPresentationController edgeForHidingNavigationBar];
-[_UISearchPresentationController finalFrameForContainerView];
-[_UISearchPresentationController forceObeyNavigationBarInsets];
-[_UISearchPresentationController hideBackgroundObscuringView];
-[_UISearchPresentationController resultsUnderlapsSearchBar];
-[_UISearchPresentationController searchBarCanContainScopeBar];
-[_UISearchPresentationController searchBarShouldClipToBounds];
-[_UISearchPresentationController showBackgroundObscuringView];
```
