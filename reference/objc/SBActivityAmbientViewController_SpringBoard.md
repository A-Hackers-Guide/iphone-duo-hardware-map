# `SBActivityAmbientViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBActivityViewControllerDelegate`, `SBActivityAmbientCompactOverlayViewControllerDelegate`, `UIGestureRecognizerDelegate`, `CAAnimationDelegate`, `SBFBacklightSceneHostEnvironmentProviding`, `BSInvalidatable`
- 23 instance variables, 14 properties, 122 instance methods, 0 class methods

## Instance variables

```
@"MTMaterialView" _fullOverlayTransitionBlurView;
@"MTMaterialView" _backgroundBlurMaterialView;
@"UIView" _compactOverlayTransitionView;
@"UIView" _switchingTransitionView;
@"UIScreenEdgePanGestureRecognizer" _dismissEdgePanGesture;
@"UIPanGestureRecognizer" _dismissPanGesture;
B _isAnimatingTransition;
d _currentFullOverlayDragTranslationY;
d _currentFullOverlayDragOriginY;
d _currentFullOverlayDragScale;
B _isInFullOverlayDrag;
Q _transitionAnimationCount;
@"NSMutableSet" _itemsWithSwappedScenes;
B _isCreatingFullScreenOverlay;
B _compactOverlayHidden;
B _compactOverlaySuppressed;
@"SBActivityItem" _primaryActivityItem;
@"SBActivityItem" _secondaryActivityItem;
q _overlayMode;
@"NSSet" _audioCategoriesDisablingVolumeHUD;
@"<SBActivityAmbientViewControllerDelegate>" _delegate;
@"SBActivityAmbientFullOverlayViewController" _fullOverlayViewController;
@"SBActivityAmbientCompactOverlayViewController" _compactOverlayViewController;
```

## Properties

```
@property (T@"SBActivityItem",&,N,S_setPrimaryActivityItem:,V_primaryActivityItem) primaryActivityItem;
@property (T@"SBActivityItem",&,N,S_setSecondaryActivityItem:,V_secondaryActivityItem) secondaryActivityItem;
@property (T@"SBActivityAmbientFullOverlayViewController",&,N,V_fullOverlayViewController) fullOverlayViewController;
@property (T@"SBActivityAmbientCompactOverlayViewController",&,N,V_compactOverlayViewController) compactOverlayViewController;
@property (TB,N,GisCompactOverlaySuppressed,V_compactOverlaySuppressed) compactOverlaySuppressed;
@property (Tq,R,N,V_overlayMode) overlayMode;
@property (TB,R,N) wantsIdleTimerDisabled;
@property (T@"NSSet",R,N,V_audioCategoriesDisablingVolumeHUD) audioCategoriesDisablingVolumeHUD;
@property (T@"<SBActivityAmbientViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisTransitioning) transitioning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityAmbientViewController sceneHostEnvironmentEntriesForBacklightSession];
-[SBActivityAmbientViewController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBActivityAmbientViewController animationDidStop:finished:];
-[SBActivityAmbientViewController activityViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:];
-[SBActivityAmbientViewController viewWillDisappear:];
-[SBActivityAmbientViewController supportedInterfaceOrientations];
-[SBActivityAmbientViewController isTransitioning];
-[SBActivityAmbientViewController dealloc];
-[SBActivityAmbientViewController audioCategoriesDisablingVolumeHUD];
-[SBActivityAmbientViewController _updateAudioCategoriesDisablingVolumeHUD];
-[SBActivityAmbientViewController viewDidLoad];
-[SBActivityAmbientViewController invalidate];
-[SBActivityAmbientViewController _canShowWhileLocked];
-[SBActivityAmbientViewController _activityHasDifferentAlertSceneTarget:];
-[SBActivityAmbientViewController setDelegate:];
-[SBActivityAmbientViewController viewDidAppear:];
-[SBActivityAmbientViewController gestureRecognizerShouldBegin:];
-[SBActivityAmbientViewController _supportsPortraitOrientation];
-[SBActivityAmbientViewController loadView];
-[SBActivityAmbientViewController delegate];
-[SBActivityAmbientViewController viewWillLayoutSubviews];
-[SBActivityAmbientViewController _isInnerSurface];
-[SBActivityAmbientViewController _supportsInnerSurfaceGutter];
-[SBActivityAmbientViewController wantsIdleTimerDisabled];
-[SBActivityAmbientViewController overlayMode];
-[SBActivityAmbientViewController _cleanupSwitchingTransitionView];
-[SBActivityAmbientViewController _gutterAwareCornerRadiiForView:];
-[SBActivityAmbientViewController _setAnchorPointForDrag:forView:];
-[SBActivityAmbientViewController _transitionTypeIsToFullOverlay:];
-[SBActivityAmbientViewController _animatePresentationOfFullOverlayWithViewController:completion:];
-[SBActivityAmbientViewController _addDismissGesture];
-[SBActivityAmbientViewController _addGaussianBlurToLayer:inputRadius:];
-[SBActivityAmbientViewController _addNewBackgroundBlurMaterialViewWithInitialWeighting:hidden:];
-[SBActivityAmbientViewController _addNewCompactOverlayTransitionViewWithParentView:alpha:];
-[SBActivityAmbientViewController _addNewFullOverlayTransitionBlurMaterialViewWithFullOverlayViewController:initialWeighting:hidden:];
-[SBActivityAmbientViewController _addNewSwitchingTransitionViewBelowSubview:];
-[SBActivityAmbientViewController _addOverlayForPrimaryActivity];
-[SBActivityAmbientViewController _addSecondaryActivityItemIfAvailable];
-[SBActivityAmbientViewController _adjustedFrameForBounds:];
-[SBActivityAmbientViewController _ambientActivitySettings];
-[SBActivityAmbientViewController _animatePresentationOfCompactOverlayWithCompactViewController:completion:];
-[SBActivityAmbientViewController _animateTransitionToBecomeNewPrimaryAcivityWithItem:transitionType:fullOverlayViewController:compactOverlayViewControllerForTransition:oldFullViewController:oldCompactViewController:completion:];
-[SBActivityAmbientViewController _animateTransitionToCompactOverlayForItem:transitionType:compactOverlayViewController:completion:];
-[SBActivityAmbientViewController _animateTransitionToFullOverlayForPrimaryActivityItem:transitionType:fullOverlayViewControllerForTransition:oldCompactOverlayViewController:completion:];
-[SBActivityAmbientViewController _animationSettingsForBackgroundBlurWindDown];
-[SBActivityAmbientViewController _animationSettingsForFullOverlayDrag];
-[SBActivityAmbientViewController _animationSettingsForFullOverlayDragCancel];
-[SBActivityAmbientViewController _animationSettingsForFullOverlayTransitionYCurve];
-[SBActivityAmbientViewController _animationSettingsForTransitionType:];
-[SBActivityAmbientViewController _beginFullOverlayDragWithTranslation:dismissesDownward:];
-[SBActivityAmbientViewController _beginTransitionForActivityItem:transitionType:configuringForAlerting:withCompletion:];
-[SBActivityAmbientViewController _blurWeightingForFullOverlayDismissalWithTranslation:];
-[SBActivityAmbientViewController _canTransitionActivityItem:forTransitionType:];
-[SBActivityAmbientViewController _cancelFullOverlayDrag];
-[SBActivityAmbientViewController _cleanupBackgroundBlurViewIfNecessary];
-[SBActivityAmbientViewController _cleanupCompactViewController:];
-[SBActivityAmbientViewController _cleanupCurrentCompactOverlayViewController];
-[SBActivityAmbientViewController _cleanupCurrentFullOverlayViewController];
-[SBActivityAmbientViewController _cleanupFullViewController:];
-[SBActivityAmbientViewController _cleanupTransitionBlurViewIfNecessary];
-[SBActivityAmbientViewController _compactOverlayFrameForContentSize:];
-[SBActivityAmbientViewController _compactOverlayViewControllerForItem:completion:];
-[SBActivityAmbientViewController _cornerRadiusForFullOverlayDismissalWithTranslation:];
-[SBActivityAmbientViewController _didUpdateVisibleActivityItems];
-[SBActivityAmbientViewController _dismissCompactOverlayForActivityEnding:completion:];
-[SBActivityAmbientViewController _dismissCompactOverlayWithView:forActivityEnding:completion:];
-[SBActivityAmbientViewController _dismissFullOverlayWithCompletion:];
-[SBActivityAmbientViewController _dismissalDirectionMultiplierForDownwardDismissal:];
-[SBActivityAmbientViewController _dismissesDownwardForGesture:];
-[SBActivityAmbientViewController _displayCornerConfigurationForFullOverlayViewController:];
-[SBActivityAmbientViewController _displayCornerRadiiForFullOverlayViewController:];
-[SBActivityAmbientViewController _endAndCleanupTransitionForActivityItem:forTransitionType:compactOverlayViewController:fullOverlayViewController:completion:];
-[SBActivityAmbientViewController _fullOverlayViewControllerForItem:configuringForAlert:completion:];
-[SBActivityAmbientViewController _gutterAwareCornerConfigurationForView:];
-[SBActivityAmbientViewController _handleDismissGesture:];
-[SBActivityAmbientViewController _handleDismissGestureBegan:];
-[SBActivityAmbientViewController _handleDismissGestureChanged:];
-[SBActivityAmbientViewController _handleDismissGestureEnded:];
-[SBActivityAmbientViewController _invalidateBacklightSceneHostEnvironments];
-[SBActivityAmbientViewController _isActiveActivityItem:];
-[SBActivityAmbientViewController _itemIsFirstPartyActivity:];
-[SBActivityAmbientViewController _layerHasGaussianBlurFilter:];
-[SBActivityAmbientViewController _layoutCompactOverlayIfNecessaryWithView:frame:];
-[SBActivityAmbientViewController _layoutFullOverlayWithActivityView:];
-[SBActivityAmbientViewController _nextSecondaryActivityItemForTransitionType:];
-[SBActivityAmbientViewController _prepareFullOverlayViewForDragWithLocation:];
-[SBActivityAmbientViewController _prepareSuppressedCompactOverlayWithCompactViewController:];
-[SBActivityAmbientViewController _removeBackgroundBlurMaterialView];
-[SBActivityAmbientViewController _removeDismissGesture];
-[SBActivityAmbientViewController _removeGaussianBlurFromLayer:];
-[SBActivityAmbientViewController _resetPrimaryActivityItemWithCompletion:];
-[SBActivityAmbientViewController _restingFullOverlayCornerConfigurationForViewController:];
-[SBActivityAmbientViewController _scaleForFullOverlayDismissalWithTranslation:];
-[SBActivityAmbientViewController _sceneTargetBundleIdentifierForItem:configuringForAlert:];
-[SBActivityAmbientViewController _setPrimaryActivityItem:];
-[SBActivityAmbientViewController _setSecondaryActivityItem:];
-[SBActivityAmbientViewController _switchToAlertSceneForActivityItem:];
-[SBActivityAmbientViewController _transitionOverlayForActivityItem:withTransitionType:configuringForAlerting:withCompletion:];
-[SBActivityAmbientViewController _updateCompactActivityOverlayWithItem:withCompletion:];
-[SBActivityAmbientViewController _updateCompactOverlayVisibilityForHandoff:];
-[SBActivityAmbientViewController _updateFullActivityOverlayWithItem:configuringForAlert:];
-[SBActivityAmbientViewController _updateHostReferenceAngleForFullOverlay];
-[SBActivityAmbientViewController _updateResolvedPreferences];
-[SBActivityAmbientViewController activityViewController:didSetIdleTimerDisabled:];
-[SBActivityAmbientViewController activityViewControllerContentRequestsCancellingGesture:];
-[SBActivityAmbientViewController addOverlayForPrimaryActivityItem:withOverlayMode:];
-[SBActivityAmbientViewController addOverlayForSecondaryActivityItem:];
-[SBActivityAmbientViewController alertActivityItem:withAlertBlock:];
-[SBActivityAmbientViewController alertDidDismissForActivityItem:completion:];
-[SBActivityAmbientViewController compactOverlayViewController];
-[SBActivityAmbientViewController fullOverlayViewController];
-[SBActivityAmbientViewController handleTapForCompactOverlayViewController:withActivityItem:];
-[SBActivityAmbientViewController initWithPrimaryActivityItem:overlayMode:];
-[SBActivityAmbientViewController isCompactOverlaySuppressed];
-[SBActivityAmbientViewController primaryActivityItem];
-[SBActivityAmbientViewController removeOverlayForActivityItem:withCompletion:];
-[SBActivityAmbientViewController secondaryActivityItem];
-[SBActivityAmbientViewController setCompactOverlayHidden:];
-[SBActivityAmbientViewController setCompactOverlaySuppressed:];
-[SBActivityAmbientViewController setCompactOverlayViewController:];
-[SBActivityAmbientViewController setFullOverlayViewController:];
-[SBActivityAmbientViewController transitionToCompactOverlayModeWithCompletion:];
```
