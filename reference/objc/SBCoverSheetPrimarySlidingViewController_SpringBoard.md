# `SBCoverSheetPrimarySlidingViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBCoverSheetSlidingViewController`
- Protocols: `SBGrabberTongueDelegate`, `SBReachabilityObserver`, `PTSettingsKeyObserver`
- 18 instance variables, 21 properties, 89 instance methods, 0 class methods

## Instance variables

```
@"SBControlCenterController" _controlCenterController;
@"SBSystemGesturesSettings" _systemGesturesSettings;
B _hasCommittedCurrentTransition;
@"<SBCoverSheetGrabberDelegate>" _grabberDelegate;
@"SBFTouchPassThroughView" _unlockedContentOverlayView;
@"SBCoverSheetPanelBackgroundContainerView" _panelBackgroundContainerView;
@"SBFTouchPassThroughView" _parallaxClippingView;
@"SBCoverSheetParallaxContainerView" _parallaxContainerView;
@"SBCoverSheetDimmingView" _maskedDimmingView;
@"SBGrabberTongue" _grabberTongue;
@"SBCoverSheetBlurView" _behindCoverSheetBlurView;
@"SBCoverSheetBlurView" _panelCoverSheetBlurView;
@"SBWallpaperEffectView" _panelWallpaperEffectView;
@"SBWallpaperEffectView" _panelFadeOutWallpaperEffectView;
@"<PBUIWallpaperAnimatedInvalidating>" _homescreenWallpaperScaleAssertion;
@"<PBUIWallpaperAnimatedInvalidating>" _lockscreenWallpaperScaleAssertion;
d _defaultPresentGestureEdgeRegionSize;
d _presentationProgressAtCommit;
```

## Properties

```
@property (T@"SBFTouchPassThroughView",&,N,V_unlockedContentOverlayView) unlockedContentOverlayView;
@property (T@"SBCoverSheetPanelBackgroundContainerView",&,N,V_panelBackgroundContainerView) panelBackgroundContainerView;
@property (T@"SBFTouchPassThroughView",&,N,V_parallaxClippingView) parallaxClippingView;
@property (T@"SBCoverSheetParallaxContainerView",&,N,V_parallaxContainerView) parallaxContainerView;
@property (T@"SBCoverSheetDimmingView",&,N,V_maskedDimmingView) maskedDimmingView;
@property (T@"SBGrabberTongue",&,N,V_grabberTongue) grabberTongue;
@property (T@"SBCoverSheetBlurView",&,N,V_behindCoverSheetBlurView) behindCoverSheetBlurView;
@property (T@"SBCoverSheetBlurView",&,N,V_panelCoverSheetBlurView) panelCoverSheetBlurView;
@property (T@"SBWallpaperEffectView",&,N,V_panelWallpaperEffectView) panelWallpaperEffectView;
@property (T@"SBWallpaperEffectView",&,N,V_panelFadeOutWallpaperEffectView) panelFadeOutWallpaperEffectView;
@property (T@"<PBUIWallpaperAnimatedInvalidating>",&,N,V_homescreenWallpaperScaleAssertion) homescreenWallpaperScaleAssertion;
@property (T@"<PBUIWallpaperAnimatedInvalidating>",&,N,V_lockscreenWallpaperScaleAssertion) lockscreenWallpaperScaleAssertion;
@property (Td,N,V_defaultPresentGestureEdgeRegionSize) defaultPresentGestureEdgeRegionSize;
@property (Td,N,V_presentationProgressAtCommit) presentationProgressAtCommit;
@property (TB,N,V_hasCommittedCurrentTransition) hasCommittedCurrentTransition;
@property (T@"<SBCoverSheetGrabberDelegate>",W,N,V_grabberDelegate) grabberDelegate;
@property (T@"UIGestureRecognizer",R,N) edgePullGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCoverSheetPrimarySlidingViewController handleReachabilityModeActivated];
-[SBCoverSheetPrimarySlidingViewController grabberTongueDidDismiss:];
-[SBCoverSheetPrimarySlidingViewController grabberTongueEndedPulling:withDistance:andVelocity:andGesture:];
-[SBCoverSheetPrimarySlidingViewController _updateWindowVisibility];
-[SBCoverSheetPrimarySlidingViewController edgePullGestureRecognizer];
-[SBCoverSheetPrimarySlidingViewController _updatePresentGestureEdgeRegionSize];
-[SBCoverSheetPrimarySlidingViewController customGestureRecognizerForGrabberTongue:];
-[SBCoverSheetPrimarySlidingViewController setGrabberTongue:];
-[SBCoverSheetPrimarySlidingViewController grabberTongueCanceledPulling:withDistance:andVelocity:andGesture:];
-[SBCoverSheetPrimarySlidingViewController behindCoverSheetBlurView];
-[SBCoverSheetPrimarySlidingViewController _updateTransitionProgress:velocity:forPresentationValue:];
-[SBCoverSheetPrimarySlidingViewController handleReachabilityModeDeactivated];
-[SBCoverSheetPrimarySlidingViewController hasCommittedCurrentTransition];
-[SBCoverSheetPrimarySlidingViewController handleDidEndReachabilityAnimation];
-[SBCoverSheetPrimarySlidingViewController panelBackgroundContainerView];
-[SBCoverSheetPrimarySlidingViewController setDefaultPresentGestureEdgeRegionSize:];
-[SBCoverSheetPrimarySlidingViewController _edgeOccludingCaseStatusDidChange:];
-[SBCoverSheetPrimarySlidingViewController setGrabberDelegate:];
-[SBCoverSheetPrimarySlidingViewController _transitionToViewControllerAppearState:ifNeeded:forUserGesture:];
-[SBCoverSheetPrimarySlidingViewController grabberTongueWillPresent:];
-[SBCoverSheetPrimarySlidingViewController _visibilityDescriptionForView:];
-[SBCoverSheetPrimarySlidingViewController setHomescreenWallpaperScaleAssertion:];
-[SBCoverSheetPrimarySlidingViewController grabberTongue];
-[SBCoverSheetPrimarySlidingViewController _applyDismissalCornerRadii:forPresentationValue:];
-[SBCoverSheetPrimarySlidingViewController _updateWallpaperScaled:animated:];
-[SBCoverSheetPrimarySlidingViewController setUnlockedContentOverlayView:];
-[SBCoverSheetPrimarySlidingViewController getRotationContentSettings:forWindow:];
-[SBCoverSheetPrimarySlidingViewController _updateFadeOutWallpaperEffectView];
-[SBCoverSheetPrimarySlidingViewController dealloc];
-[SBCoverSheetPrimarySlidingViewController _controlCenterWindowSceneDidConnect:];
-[SBCoverSheetPrimarySlidingViewController _panelOptions];
-[SBCoverSheetPrimarySlidingViewController panelCoverSheetBlurView];
-[SBCoverSheetPrimarySlidingViewController setPanelFadeOutWallpaperEffectView:];
-[SBCoverSheetPrimarySlidingViewController defaultPresentGestureEdgeRegionSize];
-[SBCoverSheetPrimarySlidingViewController viewDidLayoutSubviews];
-[SBCoverSheetPrimarySlidingViewController lockscreenWallpaperScaleAssertion];
-[SBCoverSheetPrimarySlidingViewController shouldAutorotate];
-[SBCoverSheetPrimarySlidingViewController _willTranslateToPresented:];
-[SBCoverSheetPrimarySlidingViewController grabberTongueUpdatedPulling:withDistance:andVelocity:andGesture:];
-[SBCoverSheetPrimarySlidingViewController setPanelCoverSheetBlurView:];
-[SBCoverSheetPrimarySlidingViewController _updatePanelWallpaperEffectView];
-[SBCoverSheetPrimarySlidingViewController setParallaxClippingView:];
-[SBCoverSheetPrimarySlidingViewController settings:changedValueForKey:];
-[SBCoverSheetPrimarySlidingViewController grabberTongue:shouldShowTongueOnFirstSwipeWithEdgeLocation:];
-[SBCoverSheetPrimarySlidingViewController _updatePanelBackgroundAppearance];
-[SBCoverSheetPrimarySlidingViewController positionViewDidUpdateContentViewPosition:];
-[SBCoverSheetPrimarySlidingViewController _positionSubviewsForContentFrame:forPresentationValue:];
-[SBCoverSheetPrimarySlidingViewController setPanelWallpaperEffectView:];
-[SBCoverSheetPrimarySlidingViewController _shouldShowGrabberOnFirstSwipeAtEdgeLocation:onScreenEdge:];
-[SBCoverSheetPrimarySlidingViewController _panelBackgroundShouldUseRoundedCornerAppearance];
-[SBCoverSheetPrimarySlidingViewController handleWillBeginReachabilityAnimation];
-[SBCoverSheetPrimarySlidingViewController _endTransitionToAppeared:];
-[SBCoverSheetPrimarySlidingViewController _createPanelWallpaperEffectViewIfNeeded];
-[SBCoverSheetPrimarySlidingViewController _canShowWhileLocked];
-[SBCoverSheetPrimarySlidingViewController panelWallpaperEffectView];
-[SBCoverSheetPrimarySlidingViewController _sbWindowScene];
-[SBCoverSheetPrimarySlidingViewController grabberDelegate];
-[SBCoverSheetPrimarySlidingViewController setBehindCoverSheetBlurView:];
-[SBCoverSheetPrimarySlidingViewController _beginTransitionFromAppeared:];
-[SBCoverSheetPrimarySlidingViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBCoverSheetPrimarySlidingViewController loadView];
-[SBCoverSheetPrimarySlidingViewController setPanelBackgroundContainerView:];
-[SBCoverSheetPrimarySlidingViewController setHasCommittedCurrentTransition:];
-[SBCoverSheetPrimarySlidingViewController _setupPanelPartsIfNecessary];
-[SBCoverSheetPrimarySlidingViewController setParallaxContainerView:];
-[SBCoverSheetPrimarySlidingViewController setPresentationProgressAtCommit:];
-[SBCoverSheetPrimarySlidingViewController _handleDismissGestureBegan];
-[SBCoverSheetPrimarySlidingViewController panelFadeOutWallpaperEffectView];
-[SBCoverSheetPrimarySlidingViewController grabberTongueOrPullEnabled:forGestureRecognizer:];
-[SBCoverSheetPrimarySlidingViewController homescreenWallpaperScaleAssertion];
-[SBCoverSheetPrimarySlidingViewController setLockscreenWallpaperScaleAssertion:];
-[SBCoverSheetPrimarySlidingViewController _childViewControllerForAlwaysOnTimelines];
-[SBCoverSheetPrimarySlidingViewController setMaskedDimmingView:];
-[SBCoverSheetPrimarySlidingViewController _updateBackgroundIfNecessary];
-[SBCoverSheetPrimarySlidingViewController _didFinishOffscreenTransition];
-[SBCoverSheetPrimarySlidingViewController _configureControlCenterController:];
-[SBCoverSheetPrimarySlidingViewController setTransitionSettings:];
-[SBCoverSheetPrimarySlidingViewController unlockedContentOverlayView];
-[SBCoverSheetPrimarySlidingViewController parallaxClippingView];
-[SBCoverSheetPrimarySlidingViewController presentationProgressAtCommit];
-[SBCoverSheetPrimarySlidingViewController _usesPadLayoutBehavior];
-[SBCoverSheetPrimarySlidingViewController _createFadeOutWallpaperEffectViewIfNeeded];
-[SBCoverSheetPrimarySlidingViewController grabberTongueBeganPulling:withDistance:andVelocity:andGesture:];
-[SBCoverSheetPrimarySlidingViewController parallaxContainerView];
-[SBCoverSheetPrimarySlidingViewController _animationTickedWithProgress:velocity:forPresentationValue:];
-[SBCoverSheetPrimarySlidingViewController _updateDimmingViewMaskPositionForOffScreenWithBounds:];
-[SBCoverSheetPrimarySlidingViewController _commitTransitionToAppeared:animated:];
-[SBCoverSheetPrimarySlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:animated:];
-[SBCoverSheetPrimarySlidingViewController maskedDimmingView];
```
