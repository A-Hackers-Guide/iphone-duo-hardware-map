# `SBTodayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHTodayViewController`
- Protocols: `SBTodayViewSpotlightPresenterDelegate`, `CSExternalBehaviorProviding`, `UIGestureRecognizerDelegate`, `SBUISpotlightInitiating`, `SBFIdleTimerBehaviorProviding`, `SBFOverlayObserving`
- 6 instance variables, 21 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"SBViewControllerTransitionContext" _transitionContext;
@"<SBHSearchPresenting>" _externalSearchPresenter;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarSettingsAssertion;
@"SBTodayViewSpotlightPresenter" _spotlightPresenter;
@"SBFTouchPassThroughView" _spotlightContainerView;
@"UITapGestureRecognizer" _dismissTapGestureRecognizer;
```

## Properties

```
@property (T@"SBWindowSceneStatusBarSettingsAssertion",&,N,V_statusBarSettingsAssertion) statusBarSettingsAssertion;
@property (T@"SBTodayViewSpotlightPresenter",&,N,V_spotlightPresenter) spotlightPresenter;
@property (T@"SBFTouchPassThroughView",&,N,V_spotlightContainerView) spotlightContainerView;
@property (T@"UITapGestureRecognizer",&,N,V_dismissTapGestureRecognizer) dismissTapGestureRecognizer;
@property (T@"<SBHSearchPresenting>",W,N,V_externalSearchPresenter) externalSearchPresenter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (T@"SBViewControllerTransitionContext",&,N,V_transitionContext) transitionContext;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
```

## Instance methods

```
-[SBTodayViewController overlayController:visibilityDidChange:];
-[SBTodayViewController _setStatusBarSettingsAssertionActive:];
-[SBTodayViewController setDisplayLayoutElementActive:];
-[SBTodayViewController conformsToCSBehaviorProviding];
-[SBTodayViewController spotlightPresenter];
-[SBTodayViewController gestureRecognizer:shouldReceiveTouch:];
-[SBTodayViewController overlayControllerDidBeginChangingPresentationProgress:];
-[SBTodayViewController _beginAppearanceTransitionForChildViewControllersToVisible:animated:];
-[SBTodayViewController transitionContext];
-[SBTodayViewController viewWillDisappear:];
-[SBTodayViewController presentSpotlightAnimated:];
-[SBTodayViewController resetForSpotlightDismissalAnimated:];
-[SBTodayViewController setDismissTapGestureRecognizer:];
-[SBTodayViewController setSpotlightContainerView:];
-[SBTodayViewController spotlightPresenterSearchBarDidFocus:];
-[SBTodayViewController todayViewControllerLocationForSpotlightPresenter:];
-[SBTodayViewController setTransitionContext:];
-[SBTodayViewController idleTimerDuration];
-[SBTodayViewController proximityDetectionMode];
-[SBTodayViewController statusBarSettingsAssertion];
-[SBTodayViewController cleanupViews];
-[SBTodayViewController dismissSpotlightAnimated:];
-[SBTodayViewController overlayController:didChangePresentationProgress:newPresentationProgress:fromLeading:];
-[SBTodayViewController spotlightContainerView];
-[SBTodayViewController _endAppearanceTransitionForChildViewControllersToVisible:];
-[SBTodayViewController viewWillAppear:];
-[SBTodayViewController spotlightHeaderAcquiringViewController];
-[SBTodayViewController setExternalSearchPresenter:];
-[SBTodayViewController searchBarTopOffsetForSpotlightPresenter:];
-[SBTodayViewController scrollViewWillEndDragging:withVelocity:targetContentOffset:];
-[SBTodayViewController spotlightPresenterDidPresentSpotlight:];
-[SBTodayViewController _canShowWhileLocked];
-[SBTodayViewController spotlightPresenterWillPresentSpotlight:];
-[SBTodayViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBTodayViewController viewDidAppear:];
-[SBTodayViewController setSpotlightPresenter:];
-[SBTodayViewController scrollingStrategy];
-[SBTodayViewController notificationBehavior];
-[SBTodayViewController loadView];
-[SBTodayViewController noteFeatherBlurPinningDidChange];
-[SBTodayViewController scrollViewWillBeginDragging:];
-[SBTodayViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBTodayViewController dismissTapGestureRecognizer];
-[SBTodayViewController parentViewControllerForSpotlightPresenter:];
-[SBTodayViewController viewWillLayoutSubviews];
-[SBTodayViewController spotlightPresenterDidDismissSpotlight:];
-[SBTodayViewController viewDidDisappear:];
-[SBTodayViewController spotlightPresenterShouldPinFeatherBlurToScreenPosition:];
-[SBTodayViewController conformsToCSExternalBehaviorProviding];
-[SBTodayViewController updateViewsWithLegibilitySettings];
-[SBTodayViewController idleTimerMode];
-[SBTodayViewController setStatusBarSettingsAssertion:];
-[SBTodayViewController coverSheetIdentifier];
-[SBTodayViewController _allowsPullToSearch];
-[SBTodayViewController _setUpGestureRecognizers];
-[SBTodayViewController _shouldIconViewForbidJiggling:];
-[SBTodayViewController cleanupAfterSpotlightDismissal];
-[SBTodayViewController idleWarnMode];
-[SBTodayViewController externalSearchPresenter];
-[SBTodayViewController participantState];
-[SBTodayViewController _updateScrollViewContentInset];
-[SBTodayViewController _dismissTodayViewOverlay:];
-[SBTodayViewController isSpotlightVisible];
-[SBTodayViewController spotlightPresenterAllowsPullToSearch:];
-[SBTodayViewController scrollViewDidScroll:];
-[SBTodayViewController restrictedCapabilities];
-[SBTodayViewController _setUpSearchPresenter];
```
