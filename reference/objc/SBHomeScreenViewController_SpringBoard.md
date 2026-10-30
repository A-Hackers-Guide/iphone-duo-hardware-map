# `SBHomeScreenViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBAssistantSceneControllingObserver`, `SBFloatingDockControllerObserver`, `SBFHomeAffordanceInteractionDelegate`, `SBFZStackParticipantDelegate`, `SBHModalLibraryPresentationContainerViewProviding`
- 31 instance variables, 18 properties, 90 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _iconRotationPreventionReasons;
B _disableAnimationForNextIconRotation;
@"SBWindowSceneStatusBarSettingsAssertion" _childOrPresentedStatusBarAssertion;
@"NSMapTable" _contextMenuOrientationUpdateDeferralAssertions;
@"NSMapTable" _contextMenuWindowLevelAssertions;
@"SBDeviceOrientationUpdateDeferralManager" _deviceOrientationUpdateDeferralManager;
B _iconContentHidden;
B _homeScreenAutorotatesEvenWhenIconIsDragging;
B _homeAffordanceInteractionAllowed;
B _wallpaperEditorPresented;
B _configurationInteractionPresented;
B _appLibrarySearchPresented;
B _rotating;
B _performedInitialLayout;
@"UIView" _iconContentView;
@"UIView<SBHVisibleContentPresenter>" _iconEffectView;
q _orientation;
q _effectiveOrientation;
Q _allowedInterfaceOrientations;
Q _possibleInterfaceOrientations;
@"SBWindowScene" _windowScene;
@"<SBHomeScreenAppearanceControlling>" _appearanceController;
@"<SBHomeScreenViewControllerContextProviding>" _contextProvider;
@"SBHIconManager" _iconManager;
@"SBFloatingDockBehaviorAssertion" _homeScreenFloatingDockAssertion;
@"SBFloatingDockWindowLevelAssertion" _styleEditorWindowLevelAssertion;
@"SBFZStackParticipant" _zStackParticipant;
@"NSSet" _lastLoggedAutorotationPreventionReasons;
@"SBHomeScreenReturnToSpotlightPolicy" _returnToSpotlightPolicy;
@"<SBFHomeAffordanceInteraction>" _homeAffordanceInteraction;
@"SBFHomeAffordanceView" _homeAffordanceView;
```

## Properties

```
@property (T@"UIView",R,W,N,V_iconContentView) iconContentView;
@property (TB,N,GisIconContentHidden,V_iconContentHidden) iconContentHidden;
@property (T@"UIView<SBHVisibleContentPresenter>",R,N,V_iconEffectView) iconEffectView;
@property (T@"_UILegibilitySettings",&,D,N) legibilitySettings;
@property (TB,N,V_homeScreenAutorotatesEvenWhenIconIsDragging) homeScreenAutorotatesEvenWhenIconIsDragging;
@property (TB,N,GisHomeAffordanceInteractionAllowed,V_homeAffordanceInteractionAllowed) homeAffordanceInteractionAllowed;
@property (TB,N) usesGlassGroup;
@property (TB,N,GisWallpaperEditorPresented,V_wallpaperEditorPresented) wallpaperEditorPresented;
@property (TB,N,GisConfigurationInteractionPresented,V_configurationInteractionPresented) configurationInteractionPresented;
@property (TB,N,GisAppLibrarySearchPresented,V_appLibrarySearchPresented) appLibrarySearchPresented;
@property (Tq,N,V_orientation) orientation;
@property (Tq,N,V_effectiveOrientation) effectiveOrientation;
@property (TQ,N,V_allowedInterfaceOrientations) allowedInterfaceOrientations;
@property (TQ,N,V_possibleInterfaceOrientations) possibleInterfaceOrientations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeScreenViewController setOrientation:];
-[SBHomeScreenViewController _updateHomeAffordanceInteraction];
-[SBHomeScreenViewController possibleInterfaceOrientations];
-[SBHomeScreenViewController _relinquishContextMenuOrientationUpdateDeferralAssertionForView:];
-[SBHomeScreenViewController containerInsetsForPresentingContextMenuForIconView:];
-[SBHomeScreenViewController isAppLibrarySearchPresented];
-[SBHomeScreenViewController _dismissAllIconForceTouchControllersDidFire:];
-[SBHomeScreenViewController allowedInterfaceOrientations];
-[SBHomeScreenViewController _styleEditorWillPresent:];
-[SBHomeScreenViewController _createFloatingDockWindowLevelAssertionForView:priority:];
-[SBHomeScreenViewController homeAffordanceInteractionDidRecognizeSingleTap:];
-[SBHomeScreenViewController nudgeIconInterfaceOrientation:duration:];
-[SBHomeScreenViewController setAllowIconRotation:forReason:];
-[SBHomeScreenViewController _appendAutorotationStateCaptureInputsToFormatter:];
-[SBHomeScreenViewController _isCoplanarHomeScreenEnabled];
-[SBHomeScreenViewController isConfigurationInteractionPresented];
-[SBHomeScreenViewController setHomeScreenAutorotatesEvenWhenIconIsDragging:];
-[SBHomeScreenViewController homeAffordanceFrameForHomeAffordanceInteraction:];
-[SBHomeScreenViewController assistantDidChangeHomeAffordanceDoubleTapGestureEnablement:];
-[SBHomeScreenViewController setConfigurationInteractionPresented:];
-[SBHomeScreenViewController zStackParticipant:updatePreferences:];
-[SBHomeScreenViewController _beginAppearanceTransitionForChildViewControllersToVisible:animated:];
-[SBHomeScreenViewController _logAutorotationPreventionReasonsChangeFromTrigger:];
-[SBHomeScreenViewController viewWillDisappear:];
-[SBHomeScreenViewController _cleanupAfterTransitionToSize:fromInterfaceOrientation:withTransitionContext:];
-[SBHomeScreenViewController _contextMenuDidDismissNotification:];
-[SBHomeScreenViewController supportedInterfaceOrientations];
-[SBHomeScreenViewController initWithWindowScene:contextProvider:iconManager:appearanceController:deviceOrientationUpdateDeferralManager:];
-[SBHomeScreenViewController isWallpaperEditorPresented];
-[SBHomeScreenViewController orientation];
-[SBHomeScreenViewController _contextMenuWillPresentNotification:];
-[SBHomeScreenViewController _updateHomeAffordanceView];
-[SBHomeScreenViewController iconContentView];
-[SBHomeScreenViewController dealloc];
-[SBHomeScreenViewController setPossibleInterfaceOrientations:];
-[SBHomeScreenViewController setWallpaperEditorPresented:];
-[SBHomeScreenViewController _performInitialLayoutWithOrientation:];
-[SBHomeScreenViewController _autorotationPreventionReasons];
-[SBHomeScreenViewController _iconEditingDidChange:];
-[SBHomeScreenViewController _updateIconContentViewOrientationAndLayoutIfNeeded];
-[SBHomeScreenViewController containerViewForPresentingContextMenuForIconView:];
-[SBHomeScreenViewController containerViewForModalLibraryPresenter:];
-[SBHomeScreenViewController zStackParticipantDidChange:];
-[SBHomeScreenViewController viewDidLayoutSubviews];
-[SBHomeScreenViewController previewTargetContainerViewForPresentingFromTodayViewControllerAllowingCoverSheet:];
-[SBHomeScreenViewController usesGlassGroup];
-[SBHomeScreenViewController shouldAutorotate];
-[SBHomeScreenViewController setNeedsStatusBarAppearanceUpdate];
-[SBHomeScreenViewController zStackParticipant:updateZOrderPreferences:];
-[SBHomeScreenViewController setIconContentHidden:];
-[SBHomeScreenViewController _homeScreenRotationStyleWantsUIKitRotation];
-[SBHomeScreenViewController _endAppearanceTransitionForChildViewControllersToVisible:];
-[SBHomeScreenViewController viewWillAppear:];
-[SBHomeScreenViewController isIconContentHidden];
-[SBHomeScreenViewController setUsesGlassGroup:];
-[SBHomeScreenViewController viewDidAppear:];
-[SBHomeScreenViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBHomeScreenViewController loadView];
-[SBHomeScreenViewController floatingDockControllerDidRegister:];
-[SBHomeScreenViewController _acquireFloatingDockBehaviorAssertionIfNecessaryForFloatingDockController:];
-[SBHomeScreenViewController disableAnimationForNextIconRotation];
-[SBHomeScreenViewController _homeAffordanceFrameForHomeAffordanceInteraction];
-[SBHomeScreenViewController _acquireContextMenuWindowLevelAssertionForView:];
-[SBHomeScreenViewController viewWillLayoutSubviews];
-[SBHomeScreenViewController homeScreenAutorotatesEvenWhenIconIsDragging];
-[SBHomeScreenViewController legibilitySettings];
-[SBHomeScreenViewController viewDidDisappear:];
-[SBHomeScreenViewController standardHomeAffordanceHitTestRectOutsetsForHomeAffordanceInteraction:];
-[SBHomeScreenViewController previewTargetContainerViewForContextMenuForIconView:];
-[SBHomeScreenViewController _suggestedEdgeSpacingForHomeAffordance];
-[SBHomeScreenViewController _animateTransitionToSize:andInterfaceOrientation:withTransitionContext:];
-[SBHomeScreenViewController setAppLibrarySearchPresented:];
-[SBHomeScreenViewController setEffectiveOrientation:];
-[SBHomeScreenViewController _homeScreenView];
-[SBHomeScreenViewController _styleEditorDidDismiss:];
-[SBHomeScreenViewController _prepareForTransitionToSize:andInterfaceOrientation:withTransitionCoordinator:];
-[SBHomeScreenViewController _relinquishContextMenuWindowLevelAssertionForView:];
-[SBHomeScreenViewController containerViewControllerForPresentingFromTodayViewControllerAllowingCoverSheet:];
-[SBHomeScreenViewController _createFloatingDockWindowLevelAssertionForView:];
-[SBHomeScreenViewController setLegibilitySettings:];
-[SBHomeScreenViewController setHomeAffordanceInteractionAllowed:];
-[SBHomeScreenViewController setAllowedInterfaceOrientations:];
-[SBHomeScreenViewController iconEffectView];
-[SBHomeScreenViewController _floatingDockFrameDidChange:];
-[SBHomeScreenViewController canBecomeFirstResponder];
-[SBHomeScreenViewController _acquireContextMenuOrientationUpdateDeferralAssertionForView:];
-[SBHomeScreenViewController isHomeAffordanceInteractionAllowed];
-[SBHomeScreenViewController _iconContentView];
-[SBHomeScreenViewController effectiveOrientation];
-[SBHomeScreenViewController shouldAutomaticallyForwardAppearanceMethods];
```
