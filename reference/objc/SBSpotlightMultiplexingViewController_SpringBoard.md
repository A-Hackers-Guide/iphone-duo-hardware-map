# `SBSpotlightMultiplexingViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBMultiplexedSpotlightDelegate`, `FBSceneManagerObserver`, `FBSceneObserver`, `SBScrollToTopSceneProxyViewDelegate`, `SBDeviceApplicationSceneStatusBarStateObserver`, `SBSceneManagerObserver`, `SBMedusaHostedKeyboardWindowControllerObserver`, `SBScenePresenting`
- 22 instance variables, 23 properties, 99 instance methods, 6 class methods

## Instance variables

```
@"SBScrollToTopSceneProxyView" _scrollToTopView;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"SBWindowSceneStatusBarSettingsAssertion" _hideStatusBarAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarStyleAssertion;
@"<SBScenePresentingDelegate>" _inputUIPresentingDelegate;
@"<BSInvalidatable>" _inputUIPresenterAssertion;
@"<BSInvalidatable>" _deferringRuleAssertion;
B _wantsExternalKeyboardView;
B _searchContentAvailable;
B _invalidated;
B _activeDelegate;
@"_UILegibilitySettings" _legibilitySettings;
@"<SBSpotlightMultiplexingViewControllerDelegate>" _delegate;
@"<SPUIRemoteSearchViewDelegate>" _spotlightDelegate;
@"UIView" _externalKeyboardView;
q _screenRegion;
@"FBSDisplayConfiguration" _targetDisplayConfiguration;
@"<BSInvalidatable>" _keyboardWindowLevelAssertion;
@"UIView" _keyboardHostView;
@"UIView" _inputUIView;
@"UIView" _hostedInputUIView;
@"<UIScenePresenter>" _keyboardPresenter;
```

## Properties

```
@property (TB,N,GisActiveDelegate,V_activeDelegate) activeDelegate;
@property (T@"<BSInvalidatable>",&,N,V_keyboardWindowLevelAssertion) keyboardWindowLevelAssertion;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"UIView",&,N,V_externalKeyboardView) externalKeyboardView;
@property (T@"UIView",&,N,V_keyboardHostView) keyboardHostView;
@property (T@"UIView",&,N,V_inputUIView) inputUIView;
@property (T@"UIView",&,N,V_hostedInputUIView) hostedInputUIView;
@property (T@"<UIScenePresenter>",&,N,V_keyboardPresenter) keyboardPresenter;
@property (TB,N,GisSearchContentAvailable,V_searchContentAvailable) searchContentAvailable;
@property (TQ,R,N) spotlightSupportedInterfaceOrientations;
@property (T{SBSpotlightHostedContentMetrics=dd{CGSize=dd}{CGSize=dd}d},R,N) spotlightHostedContentMetrics;
@property (T@"_UILegibilitySettings",C,N,V_legibilitySettings) legibilitySettings;
@property (TQ,R,N) level;
@property (T@"<SBSpotlightMultiplexingViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<SPUIRemoteSearchViewDelegate>",W,N,V_spotlightDelegate) spotlightDelegate;
@property (TB,N,V_wantsExternalKeyboardView) wantsExternalKeyboardView;
@property (TB,R,N) externalKeyboardViewContainsKeyboard;
@property (Tq,N,V_screenRegion) screenRegion;
@property (T@"FBSDisplayConfiguration",W,N,V_targetDisplayConfiguration) targetDisplayConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSpotlightMultiplexingViewController _class_spotlightHostedContentMetrics];
+[SBSpotlightMultiplexingViewController effectiveSpotlightSearchFieldAvoidanceHeight];
+[SBSpotlightMultiplexingViewController isShownWithinWindow:];
+[SBSpotlightMultiplexingViewController isShownWithinWindowScene:];
+[SBSpotlightMultiplexingViewController keyboardFocusTargetIfActiveForeground];
+[SBSpotlightMultiplexingViewController spotlightSceneIdentityTokenIfActiveForeground];
```

## Instance methods

```
-[SBSpotlightMultiplexingViewController setPresentingDelegate:];
-[SBSpotlightMultiplexingViewController sceneWithIdentifier:didChangeStatusBarAlphaTo:];
-[SBSpotlightMultiplexingViewController dismissSearchView];
-[SBSpotlightMultiplexingViewController noteFrameInKeyboardReferenceSpaceMayHaveChanged];
-[SBSpotlightMultiplexingViewController dismissScene:];
-[SBSpotlightMultiplexingViewController sceneWithIdentifier:didChangeStatusBarStyleTo:];
-[SBSpotlightMultiplexingViewController sceneDidInvalidate:withContext:];
-[SBSpotlightMultiplexingViewController sceneHandle];
-[SBSpotlightMultiplexingViewController viewWillDisappear:];
-[SBSpotlightMultiplexingViewController dealloc];
-[SBSpotlightMultiplexingViewController sceneContentStateDidChange:];
-[SBSpotlightMultiplexingViewController level];
-[SBSpotlightMultiplexingViewController viewDidLayoutSubviews];
-[SBSpotlightMultiplexingViewController setTargetDisplayConfiguration:];
-[SBSpotlightMultiplexingViewController presentScene:viewControllerBuilderBlock:];
-[SBSpotlightMultiplexingViewController initWithNibName:bundle:];
-[SBSpotlightMultiplexingViewController isInvalidated];
-[SBSpotlightMultiplexingViewController setInvalidated:];
-[SBSpotlightMultiplexingViewController viewWillAppear:];
-[SBSpotlightMultiplexingViewController invalidate];
-[SBSpotlightMultiplexingViewController setDelegate:];
-[SBSpotlightMultiplexingViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBSpotlightMultiplexingViewController viewDidAppear:];
-[SBSpotlightMultiplexingViewController delegate];
-[SBSpotlightMultiplexingViewController legibilitySettings];
-[SBSpotlightMultiplexingViewController viewDidDisappear:];
-[SBSpotlightMultiplexingViewController setLegibilitySettings:];
-[SBSpotlightMultiplexingViewController sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBSpotlightMultiplexingViewController targetDisplayConfiguration];
-[SBSpotlightMultiplexingViewController sceneManager:didAddScene:];
-[SBSpotlightMultiplexingViewController shouldAutomaticallyForwardAppearanceMethods];
-[SBSpotlightMultiplexingViewController isEligible];
-[SBSpotlightMultiplexingViewController setSpotlightDelegate:];
-[SBSpotlightMultiplexingViewController spotlightDelegate];
-[SBSpotlightMultiplexingViewController _invalidateDeferringRule];
-[SBSpotlightMultiplexingViewController _effectiveSceneForDeferringRule];
-[SBSpotlightMultiplexingViewController _configureExternalKeyboardView:];
-[SBSpotlightMultiplexingViewController _updateStatusBarHiddenAssertion];
-[SBSpotlightMultiplexingViewController setInputUIView:];
-[SBSpotlightMultiplexingViewController _acquireInputUIPresentingAssertionIfNecessary];
-[SBSpotlightMultiplexingViewController _analyticsLogSpotlightInvocationWhereAndHowWithSource:];
-[SBSpotlightMultiplexingViewController _appStatusBarSettingsLevelForSpotlightMultiplexingLevel:];
-[SBSpotlightMultiplexingViewController _clearStatusBarHiddenAssertion];
-[SBSpotlightMultiplexingViewController _clearStatusBarStyleAssertionAnimated:];
-[SBSpotlightMultiplexingViewController _configureExternalKeyboardView];
-[SBSpotlightMultiplexingViewController _configureSceneObservation:forScene:];
-[SBSpotlightMultiplexingViewController _configureStatusBarScrollToTopView];
-[SBSpotlightMultiplexingViewController _displayConfigurationForExternalClients];
-[SBSpotlightMultiplexingViewController _effectiveKeyboardContentView];
-[SBSpotlightMultiplexingViewController _evaluateDeferringRule];
-[SBSpotlightMultiplexingViewController _evaluateSearchContentAvailabilityForScene:];
-[SBSpotlightMultiplexingViewController _getSceneHandleFromSceneManager:];
-[SBSpotlightMultiplexingViewController _invalidateInputUIPresentingAssertion];
-[SBSpotlightMultiplexingViewController _isStatusBarEffectivelyHidden];
-[SBSpotlightMultiplexingViewController _notifyExternalKeyboardViewContainsKeyboard:];
-[SBSpotlightMultiplexingViewController _registerStatusBarScrollToTopView];
-[SBSpotlightMultiplexingViewController _registerStatusBarScrollToTopViewWithWindow:];
-[SBSpotlightMultiplexingViewController _remoteSearchViewControllerHasKeyboardPresented];
-[SBSpotlightMultiplexingViewController _returnKeyboardToSpotlightIfNecessary];
-[SBSpotlightMultiplexingViewController _spotlightSceneIdentifier];
-[SBSpotlightMultiplexingViewController _unregisterStatusBarScrollToTopView];
-[SBSpotlightMultiplexingViewController _unregisterStatusBarScrollToTopViewWithWindow:];
-[SBSpotlightMultiplexingViewController _updateStatusBarStyleAssertion];
-[SBSpotlightMultiplexingViewController _updateStatusBarStyleAssertionToStyle:animated:];
-[SBSpotlightMultiplexingViewController currentDisplayIdentity];
-[SBSpotlightMultiplexingViewController didBecomeActiveDelegate];
-[SBSpotlightMultiplexingViewController didResignActiveDelegate:];
-[SBSpotlightMultiplexingViewController externalKeyboardView];
-[SBSpotlightMultiplexingViewController externalKeyboardViewContainsKeyboard];
-[SBSpotlightMultiplexingViewController hostedInputUIView];
-[SBSpotlightMultiplexingViewController inputUIView];
-[SBSpotlightMultiplexingViewController isActiveDelegate];
-[SBSpotlightMultiplexingViewController isSearchContentAvailable];
-[SBSpotlightMultiplexingViewController isVisibleOnScreen];
-[SBSpotlightMultiplexingViewController keyboardHostView];
-[SBSpotlightMultiplexingViewController keyboardLayersDidChange:];
-[SBSpotlightMultiplexingViewController keyboardPresenter];
-[SBSpotlightMultiplexingViewController keyboardWindowLevelAssertion];
-[SBSpotlightMultiplexingViewController parentSceneIdentityToken];
-[SBSpotlightMultiplexingViewController remoteSearchViewPresentationSource];
-[SBSpotlightMultiplexingViewController screenRegion];
-[SBSpotlightMultiplexingViewController scrollToTopSceneProxyViewDidEnterViewHierarchy:rootedAtWindow:];
-[SBSpotlightMultiplexingViewController scrollToTopSceneProxyViewWillExitViewHierarchy:rootedAtWindow:];
-[SBSpotlightMultiplexingViewController searchViewContentAvailabilityDidChange];
-[SBSpotlightMultiplexingViewController searchViewKeyboardPresentationStateDidChange];
-[SBSpotlightMultiplexingViewController setActiveDelegate:];
-[SBSpotlightMultiplexingViewController setExternalKeyboardView:];
-[SBSpotlightMultiplexingViewController setHostedInputUIView:];
-[SBSpotlightMultiplexingViewController setKeyboardHostView:];
-[SBSpotlightMultiplexingViewController setKeyboardPresenter:];
-[SBSpotlightMultiplexingViewController setKeyboardWindowLevelAssertion:];
-[SBSpotlightMultiplexingViewController setScreenRegion:];
-[SBSpotlightMultiplexingViewController setSearchContentAvailable:];
-[SBSpotlightMultiplexingViewController setWantsExternalKeyboardView:];
-[SBSpotlightMultiplexingViewController shouldInhibitDeferringRule];
-[SBSpotlightMultiplexingViewController spotlightHostedContentMetrics];
-[SBSpotlightMultiplexingViewController spotlightRemoteViewController:didCreateScene:];
-[SBSpotlightMultiplexingViewController spotlightSupportedInterfaceOrientations];
-[SBSpotlightMultiplexingViewController wantsExternalKeyboardView];
```
