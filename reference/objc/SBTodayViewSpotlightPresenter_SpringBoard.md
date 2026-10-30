# `SBTodayViewSpotlightPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SPUISearchBarDelegate`, `SBSearchPresenterDelegate`, `SBSpotlightPresentableViewControllerDelegate`, `SBLegacyTodayViewSpotlightPresentableViewControllerDelegate`, `SBHLegibility`
- 12 instance variables, 14 properties, 52 instance methods, 1 class methods

## Instance variables

```
@"SBHHomePullToSearchSettings" _pullToSearchSettings;
B _containerViewIsVisible;
@"<SBHLegibilitySettings>" _legibilitySettings;
@"SPUISearchBarController" _searchBarViewController;
@"UIViewController" _spotlightViewController;
@"SBSearchPresenter" _presenter;
@"_SBTodaySpotlightViewController" _spotlightMultiplexingViewController;
@"UIView" _containerView;
@"UIScrollView" _scrollView;
@"<SBTodayViewSpotlightPresenterDelegate>" _delegate;
@"SBFFeatherBlurView" _featherBlurView;
@"NSArray" _searchBarGradientMaskLayers;
```

## Properties

```
@property (T@"SBSearchPresenter",&,N,V_presenter) presenter;
@property (T@"_SBTodaySpotlightViewController",&,N,V_spotlightMultiplexingViewController) spotlightMultiplexingViewController;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIScrollView",&,N,V_scrollView) scrollView;
@property (T@"<SBTodayViewSpotlightPresenterDelegate>",W,N,V_delegate) delegate;
@property (T@"SBFFeatherBlurView",&,N,V_featherBlurView) featherBlurView;
@property (T@"NSArray",&,N,V_searchBarGradientMaskLayers) searchBarGradientMaskLayers;
@property (T@"SPUISearchBarController",R,N,V_searchBarViewController) searchBarViewController;
@property (T@"UIViewController",R,N,V_spotlightViewController) spotlightViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHLegibilitySettings>",&,N,V_legibilitySettings) legibilitySettings;
```

## Class methods

```
+[SBTodayViewSpotlightPresenter supportsFeatherBlurForWindowScene:];
```

## Instance methods

```
-[SBTodayViewSpotlightPresenter setContainerView:];
-[SBTodayViewSpotlightPresenter searchPresenterWillDismissSearch:animated:];
-[SBTodayViewSpotlightPresenter searchPresenterDidPresentSearch:];
-[SBTodayViewSpotlightPresenter spotlightPresentableViewControllerShouldDismiss:];
-[SBTodayViewSpotlightPresenter backgroundViewForSpotlightPresentableViewController:];
-[SBTodayViewSpotlightPresenter displayConfigurationForPresenter:];
-[SBTodayViewSpotlightPresenter presenter];
-[SBTodayViewSpotlightPresenter searchPresentablesForPresenter:];
-[SBTodayViewSpotlightPresenter searchPresenterWillPresentSearch:animated:];
-[SBTodayViewSpotlightPresenter setPresenter:];
-[SBTodayViewSpotlightPresenter presentSpotlightAnimated:];
-[SBTodayViewSpotlightPresenter scrollView];
-[SBTodayViewSpotlightPresenter setScrollView:];
-[SBTodayViewSpotlightPresenter searchPresenterCanPresent:];
-[SBTodayViewSpotlightPresenter dismissSpotlightAnimated:];
-[SBTodayViewSpotlightPresenter containerView];
-[SBTodayViewSpotlightPresenter setDelegate:];
-[SBTodayViewSpotlightPresenter noteFeatherBlurPinningDidChange];
-[SBTodayViewSpotlightPresenter wantsHomeAffordanceForSpotlightPresentableViewController:];
-[SBTodayViewSpotlightPresenter scrollViewWillBeginDragging:];
-[SBTodayViewSpotlightPresenter searchTopOffsetForSearchPresenter:];
-[SBTodayViewSpotlightPresenter delegate];
-[SBTodayViewSpotlightPresenter legibilitySettings];
-[SBTodayViewSpotlightPresenter searchBarDidFocus];
-[SBTodayViewSpotlightPresenter layout];
-[SBTodayViewSpotlightPresenter searchPresenterDidDismissSearch:];
-[SBTodayViewSpotlightPresenter _shouldPinFeatherBlurToScreenPosition];
-[SBTodayViewSpotlightPresenter setLegibilitySettings:];
-[SBTodayViewSpotlightPresenter scrollViewWillEndDragging:withVelocity:];
-[SBTodayViewSpotlightPresenter scrollViewDidScroll:];
-[SBTodayViewSpotlightPresenter isPresenting];
-[SBTodayViewSpotlightPresenter spotlightViewController];
-[SBTodayViewSpotlightPresenter _topOffset];
-[SBTodayViewSpotlightPresenter searchBarViewController];
-[SBTodayViewSpotlightPresenter setSearchBarGradientMaskLayers:];
-[SBTodayViewSpotlightPresenter searchBarGradientMaskLayers];
-[SBTodayViewSpotlightPresenter featherBlurView];
-[SBTodayViewSpotlightPresenter legacyTodayViewSpotlightPresentableViewControllerShouldDismiss:];
-[SBTodayViewSpotlightPresenter _configureFeatherBlurMatchMoveAnimations];
-[SBTodayViewSpotlightPresenter _newSearchBackdropView];
-[SBTodayViewSpotlightPresenter _setUpFeatherBlurForWindow:];
-[SBTodayViewSpotlightPresenter _setUpStartingScrollOffset];
-[SBTodayViewSpotlightPresenter _updateFeatherBlurMaskLayers];
-[SBTodayViewSpotlightPresenter backdropViewForLegacyTodayViewSpotlightPresentableViewController:];
-[SBTodayViewSpotlightPresenter containerViewDidDisappear];
-[SBTodayViewSpotlightPresenter containerViewDidMoveToWindow:];
-[SBTodayViewSpotlightPresenter containerViewWillAppear];
-[SBTodayViewSpotlightPresenter initWithSearchBarViewController:containerView:scrollView:delegate:];
-[SBTodayViewSpotlightPresenter legacyTodayViewSpotlightPresentableViewControllerShouldPinFeatherBlurToScreenPosition:];
-[SBTodayViewSpotlightPresenter setFeatherBlurView:];
-[SBTodayViewSpotlightPresenter setSpotlightMultiplexingViewController:];
-[SBTodayViewSpotlightPresenter spotlightMultiplexingViewController];
```
