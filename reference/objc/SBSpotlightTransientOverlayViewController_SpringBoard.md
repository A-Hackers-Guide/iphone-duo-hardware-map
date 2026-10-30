# `SBSpotlightTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `SPUIRemoteSearchViewDelegate`
- 15 instance variables, 14 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"UIVisualEffectView" _blurEffectView;
@"SBSpotlightTransientOverlaySpotlightViewController" _spotlightViewController;
B _presentingInteractively;
B _performedAlongsideAnimations;
@"<SBTransientOverlayTransitionContextProviding>" _interactivePresentationContextProvider;
@"<SBSpotlightTransientOverlayViewControllerDelegate>" _delegate;
@"FBSDisplayConfiguration" _targetDisplayConfiguration;
Q _presentationSource;
Q _dismissalSource;
@"SBSpotlightSettings" _settings;
@"UIView" _scalingView;
Q _animationCount;
@"SBModalUIFluidDismissGestureManager" _modalUIDismissGestureManager;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UITapGestureRecognizer" _tapToDismissGestureRecognizer;
```

## Properties

```
@property (T@"SBSpotlightSettings",&,N,V_settings) settings;
@property (T@"UIView",&,N,V_scalingView) scalingView;
@property (TQ,N,V_animationCount) animationCount;
@property (T@"SBModalUIFluidDismissGestureManager",&,N,V_modalUIDismissGestureManager) modalUIDismissGestureManager;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_tapToDismissGestureRecognizer) tapToDismissGestureRecognizer;
@property (T@"<SBSpotlightTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"FBSDisplayConfiguration",W,N,V_targetDisplayConfiguration) targetDisplayConfiguration;
@property (TQ,N,V_presentationSource) presentationSource;
@property (TQ,N,V_dismissalSource) dismissalSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSpotlightTransientOverlayViewController panGestureRecognizer];
-[SBSpotlightTransientOverlayViewController animationCount];
-[SBSpotlightTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBSpotlightTransientOverlayViewController dismissSearchView];
-[SBSpotlightTransientOverlayViewController setPanGestureRecognizer:];
-[SBSpotlightTransientOverlayViewController handleGestureDismissal];
-[SBSpotlightTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBSpotlightTransientOverlayViewController presentationSource];
-[SBSpotlightTransientOverlayViewController preferredDisplayLayoutElementIdentifier];
-[SBSpotlightTransientOverlayViewController setSettings:];
-[SBSpotlightTransientOverlayViewController init];
-[SBSpotlightTransientOverlayViewController viewWillDisappear:];
-[SBSpotlightTransientOverlayViewController setPresentationSource:];
-[SBSpotlightTransientOverlayViewController supportedInterfaceOrientations];
-[SBSpotlightTransientOverlayViewController settings];
-[SBSpotlightTransientOverlayViewController dealloc];
-[SBSpotlightTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBSpotlightTransientOverlayViewController viewDidLoad];
-[SBSpotlightTransientOverlayViewController shouldDisableOrientationUpdates];
-[SBSpotlightTransientOverlayViewController hostedSceneIdentityTokens];
-[SBSpotlightTransientOverlayViewController viewDidLayoutSubviews];
-[SBSpotlightTransientOverlayViewController shouldAutorotate];
-[SBSpotlightTransientOverlayViewController _preferredStatusBarVisibility];
-[SBSpotlightTransientOverlayViewController keyboardFocusTarget];
-[SBSpotlightTransientOverlayViewController setTargetDisplayConfiguration:];
-[SBSpotlightTransientOverlayViewController _handlePanGestureRecognizer:];
-[SBSpotlightTransientOverlayViewController shouldUseSceneBasedKeyboardFocus];
-[SBSpotlightTransientOverlayViewController isPresentedFromSceneWithIdentityTokenString:];
-[SBSpotlightTransientOverlayViewController setAnimationCount:];
-[SBSpotlightTransientOverlayViewController _canShowWhileLocked];
-[SBSpotlightTransientOverlayViewController setDelegate:];
-[SBSpotlightTransientOverlayViewController viewDidAppear:];
-[SBSpotlightTransientOverlayViewController isContentOpaque];
-[SBSpotlightTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBSpotlightTransientOverlayViewController delegate];
-[SBSpotlightTransientOverlayViewController allowsStackingOverlayContentAbove];
-[SBSpotlightTransientOverlayViewController preferredStatusBarStyle];
-[SBSpotlightTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBSpotlightTransientOverlayViewController targetDisplayConfiguration];
-[SBSpotlightTransientOverlayViewController handleHomeButtonPress];
-[SBSpotlightTransientOverlayViewController setTapToDismissGestureRecognizer:];
-[SBSpotlightTransientOverlayViewController tapToDismissGestureRecognizer];
-[SBSpotlightTransientOverlayViewController dismissalSource];
-[SBSpotlightTransientOverlayViewController setScalingView:];
-[SBSpotlightTransientOverlayViewController scalingView];
-[SBSpotlightTransientOverlayViewController prefersWindowHitTestingDisabled];
-[SBSpotlightTransientOverlayViewController _configureBlurFilterOnView:];
-[SBSpotlightTransientOverlayViewController _handleTapToDismissGestureRecognizer:];
-[SBSpotlightTransientOverlayViewController _isReduceMotionOrTransparency];
-[SBSpotlightTransientOverlayViewController _isSpotlightVisible];
-[SBSpotlightTransientOverlayViewController _setSpotlightAlpha:scale:blurProgress:translation:withAnimationMode:alongsideAnimationBlock:completion:];
-[SBSpotlightTransientOverlayViewController _setSpotlightPresented:withAnimationMode:alongsideAnimationBlock:completion:];
-[SBSpotlightTransientOverlayViewController beginInteractivePresentation];
-[SBSpotlightTransientOverlayViewController dismissesForCoverSheetPresentation];
-[SBSpotlightTransientOverlayViewController dismissesSiriForPresentation];
-[SBSpotlightTransientOverlayViewController endInteractivePresentation:];
-[SBSpotlightTransientOverlayViewController homeAffordanceSuppression];
-[SBSpotlightTransientOverlayViewController modalUIDismissGestureManager];
-[SBSpotlightTransientOverlayViewController presentationDimmingViewColor];
-[SBSpotlightTransientOverlayViewController preservesAppSwitcherDuringPresentationAndDismissal];
-[SBSpotlightTransientOverlayViewController preventsClippingToBounds];
-[SBSpotlightTransientOverlayViewController sceneDeactivationPredicate];
-[SBSpotlightTransientOverlayViewController setDismissalSource:];
-[SBSpotlightTransientOverlayViewController setModalUIDismissGestureManager:];
-[SBSpotlightTransientOverlayViewController shouldPreventDragAndDrop];
-[SBSpotlightTransientOverlayViewController updateInteractivePresentationWithProgress:translation:];
-[SBSpotlightTransientOverlayViewController wantsInitialKeyboardFocus];
```
