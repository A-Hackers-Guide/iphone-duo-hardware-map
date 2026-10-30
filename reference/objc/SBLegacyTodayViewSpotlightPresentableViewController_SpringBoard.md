# `SBLegacyTodayViewSpotlightPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SPUIRemoteSearchViewDelegate`, `SBSearchPresentable`
- 13 instance variables, 19 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"<SBLegacyTodayViewSpotlightPresentableViewControllerDelegate>" _delegate;
@"SBSpotlightMultiplexingViewController" _spotlightMultiplexingViewController;
@"SPUISearchBarController" _searchBarViewController;
@"UIScrollView" _scrollView;
d _topOffset;
d _maxPresentationOffset;
@"SBFFeatherBlurView" _featherBlurView;
@"NSLayoutConstraint" _featherBlurHeightConstraint;
@"NSArray" _searchBarGradientMaskLayers;
@"MTMaterialView" _searchBackdropView;
@"_UIPortalView" _searchBarPortalView;
@"NSLayoutConstraint" _searchBarViewTopConstraint;
@"NSMutableSet" _searchBarPortalRequirementReasons;
```

## Properties

```
@property (T@"SBFFeatherBlurView",&,N,V_featherBlurView) featherBlurView;
@property (T@"NSLayoutConstraint",&,N,V_featherBlurHeightConstraint) featherBlurHeightConstraint;
@property (T@"NSArray",&,N,V_searchBarGradientMaskLayers) searchBarGradientMaskLayers;
@property (T@"MTMaterialView",&,N,V_searchBackdropView) searchBackdropView;
@property (T@"_UIPortalView",&,N,V_searchBarPortalView) searchBarPortalView;
@property (T@"NSLayoutConstraint",&,N,V_searchBarViewTopConstraint) searchBarViewTopConstraint;
@property (T@"NSMutableSet",&,N,V_searchBarPortalRequirementReasons) searchBarPortalRequirementReasons;
@property (T@"<SBLegacyTodayViewSpotlightPresentableViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBSpotlightMultiplexingViewController",R,N,V_spotlightMultiplexingViewController) spotlightMultiplexingViewController;
@property (T@"SPUISearchBarController",R,N,V_searchBarViewController) searchBarViewController;
@property (T@"UIScrollView",R,N,V_scrollView) scrollView;
@property (Td,N,V_topOffset) topOffset;
@property (Td,N,V_maxPresentationOffset) maxPresentationOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHHomePullToSearchSettings",?,&,N) searchTransitionSettings;
@property (T@"FBSDisplayConfiguration",?,&,N) targetDisplayConfiguration;
```

## Instance methods

```
-[SBLegacyTodayViewSpotlightPresentableViewController willBeginModifyingPresentationProgressForState:animated:needsInitialLayout:];
-[SBLegacyTodayViewSpotlightPresentableViewController setMaxPresentationOffset:];
-[SBLegacyTodayViewSpotlightPresentableViewController dismissSearchView];
-[SBLegacyTodayViewSpotlightPresentableViewController topOffset];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBackdropView];
-[SBLegacyTodayViewSpotlightPresentableViewController scrollView];
-[SBLegacyTodayViewSpotlightPresentableViewController maxPresentationOffset];
-[SBLegacyTodayViewSpotlightPresentableViewController viewDidLoad];
-[SBLegacyTodayViewSpotlightPresentableViewController viewDidLayoutSubviews];
-[SBLegacyTodayViewSpotlightPresentableViewController setTargetDisplayConfiguration:];
-[SBLegacyTodayViewSpotlightPresentableViewController _canShowWhileLocked];
-[SBLegacyTodayViewSpotlightPresentableViewController setDelegate:];
-[SBLegacyTodayViewSpotlightPresentableViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBLegacyTodayViewSpotlightPresentableViewController updatePresentationProgress:withOffset:velocity:presentationState:];
-[SBLegacyTodayViewSpotlightPresentableViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBLegacyTodayViewSpotlightPresentableViewController noteFeatherBlurPinningDidChange];
-[SBLegacyTodayViewSpotlightPresentableViewController setTopOffset:];
-[SBLegacyTodayViewSpotlightPresentableViewController delegate];
-[SBLegacyTodayViewSpotlightPresentableViewController _shouldPinFeatherBlurToScreenPosition];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBarViewController];
-[SBLegacyTodayViewSpotlightPresentableViewController setSearchBarGradientMaskLayers:];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBarGradientMaskLayers];
-[SBLegacyTodayViewSpotlightPresentableViewController _setUpSearchBar];
-[SBLegacyTodayViewSpotlightPresentableViewController featherBlurView];
-[SBLegacyTodayViewSpotlightPresentableViewController setFeatherBlurHeightConstraint:];
-[SBLegacyTodayViewSpotlightPresentableViewController _beginRequiringSearchBarPortalViewForReason:];
-[SBLegacyTodayViewSpotlightPresentableViewController _endRequiringSearchBarPortalViewForReason:];
-[SBLegacyTodayViewSpotlightPresentableViewController _setUpFeatherBackgroundMatchMoveAnimations];
-[SBLegacyTodayViewSpotlightPresentableViewController _setUpFeatherBlurForWindow:];
-[SBLegacyTodayViewSpotlightPresentableViewController _setUpSearchBackdrop];
-[SBLegacyTodayViewSpotlightPresentableViewController _setUpSearchBackdropMatchMoveAnimation];
-[SBLegacyTodayViewSpotlightPresentableViewController _sharedRemoteSearchViewController];
-[SBLegacyTodayViewSpotlightPresentableViewController _updateMaskLayers];
-[SBLegacyTodayViewSpotlightPresentableViewController featherBlurHeightConstraint];
-[SBLegacyTodayViewSpotlightPresentableViewController initWithSpotlightMultiplexingViewController:searchBarViewController:scrollView:];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBarPortalRequirementReasons];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBarPortalView];
-[SBLegacyTodayViewSpotlightPresentableViewController searchBarViewTopConstraint];
-[SBLegacyTodayViewSpotlightPresentableViewController setFeatherBlurView:];
-[SBLegacyTodayViewSpotlightPresentableViewController setSearchBackdropView:];
-[SBLegacyTodayViewSpotlightPresentableViewController setSearchBarPortalRequirementReasons:];
-[SBLegacyTodayViewSpotlightPresentableViewController setSearchBarPortalView:];
-[SBLegacyTodayViewSpotlightPresentableViewController setSearchBarViewTopConstraint:];
-[SBLegacyTodayViewSpotlightPresentableViewController spotlightMultiplexingViewController];
```
