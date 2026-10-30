# `SBDashBoardPosterSwitcherViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `CSTraitAwareAppHostContextProviding`, `SBDeviceApplicationSceneHandleObserver`, `SBSceneHandleActionConsuming`, `CSPosterSwitcherViewControllerConfiguring`, `SBApplicationHosting`
- 28 instance variables, 33 properties, 108 instance methods, 0 class methods

## Instance variables

```
@? _toFullscreenBlock;
B _clientPosterEditorPresented;
B _coverSheetWallpaperFloatingLayerInlined;
B _coverSheetComplicationRowHidden;
B _handledInitialTransition;
B _hasTransferredInitialTouches;
B _hasCommittedInContentReadyState;
B _hasEverAppeared;
B _hasEverGoneBeyondAlongside;
@"NSArray" _activatingTouches;
@"<CSTraitAwareAppHostConfiguring>" _appHostConfiguring;
@"UIView" _coverSheetBackgroundView;
@"UIView" _coverSheetWallpaperView;
@"UIView" _coverSheetFloatingView;
d _lastAdaptiveTimeTextHeight;
@"UIWindow" _targetWindow;
@"BSUIVibrancyConfiguration" _vibrancyConfiguration;
@? _invalidationHandler;
@? _stateCoordinationHandler;
Q _fullscreenTransitionAnimationCount;
Q _clientSwitcherLayoutMode;
@"PRUISSwitcherSceneClientSettingsDiffInspector" _sceneClientSettingsDiffInspector;
@"UIView" _scaleView;
@"CSCoverSheetViewControllerBase<SBApplicationHosting>" _applicationHoster;
@"SBSceneHandleActiveAppearanceAssertion" _activeAppearanceAssertion;
@"UIViewController<CSTraitsAwareOrientedAppHosting>" _traitsAwareViewController;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leadingTopButtonFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trailingTopButtonFrame;
```

## Properties

```
@property (TB,N,V_handledInitialTransition) handledInitialTransition;
@property (TB,N,V_hasTransferredInitialTouches) hasTransferredInitialTouches;
@property (TB,N,V_hasCommittedInContentReadyState) hasCommittedInContentReadyState;
@property (TB,N,V_hasEverAppeared) hasEverAppeared;
@property (TB,N,V_hasEverGoneBeyondAlongside) hasEverGoneBeyondAlongside;
@property (TQ,N,V_fullscreenTransitionAnimationCount) fullscreenTransitionAnimationCount;
@property (TQ,N,V_clientSwitcherLayoutMode) clientSwitcherLayoutMode;
@property (T@"PRUISSwitcherSceneClientSettingsDiffInspector",R,N,V_sceneClientSettingsDiffInspector) sceneClientSettingsDiffInspector;
@property (T@"UIView",R,N,V_scaleView) scaleView;
@property (T@"CSCoverSheetViewControllerBase<SBApplicationHosting>",R,N,V_applicationHoster) applicationHoster;
@property (T@"SBSceneHandleActiveAppearanceAssertion",R,N,V_activeAppearanceAssertion) activeAppearanceAssertion;
@property (T@"UIViewController<CSTraitsAwareOrientedAppHosting>",&,N,V_traitsAwareViewController) traitsAwareViewController;
@property (T@"NSString",R,N) hostedAppBundleIdentifier;
@property (TB,R,N) hostedAppShouldHideHomeGrabberView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CSTraitAwareAppHostConfiguring>",&,N,V_appHostConfiguring) appHostConfiguring;
@property (T@"NSArray",&,N,V_activatingTouches) activatingTouches;
@property (T@"UIView",W,N,V_coverSheetBackgroundView) coverSheetBackgroundView;
@property (T@"UIView",W,N,V_coverSheetWallpaperView) coverSheetWallpaperView;
@property (T@"UIView",W,N,V_coverSheetFloatingView) coverSheetFloatingView;
@property (TB,N,GisCoverSheetWallpaperFloatingLayerInlined,V_coverSheetWallpaperFloatingLayerInlined) coverSheetWallpaperFloatingLayerInlined;
@property (TB,N,GisCoverSheetComplicationRowHidden,V_coverSheetComplicationRowHidden) coverSheetComplicationRowHidden;
@property (Td,N,V_lastAdaptiveTimeTextHeight) lastAdaptiveTimeTextHeight;
@property (T@"UIWindow",&,N,V_targetWindow) targetWindow;
@property (T@"BSUIVibrancyConfiguration",C,N,V_vibrancyConfiguration) vibrancyConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_leadingTopButtonFrame) leadingTopButtonFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_trailingTopButtonFrame) trailingTopButtonFrame;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N) toFullscreenBlock;
@property (T@?,?,C,N,V_stateCoordinationHandler) stateCoordinationHandler;
```

## Instance methods

```
-[SBDashBoardPosterSwitcherViewController setVibrancyConfiguration:];
-[SBDashBoardPosterSwitcherViewController scaleView];
-[SBDashBoardPosterSwitcherViewController _sceneIfExists];
-[SBDashBoardPosterSwitcherViewController sceneHandle:didDestroyScene:];
-[SBDashBoardPosterSwitcherViewController sceneHandle:clientConnectedForScene:];
-[SBDashBoardPosterSwitcherViewController addGrabberView:];
-[SBDashBoardPosterSwitcherViewController sceneHandle:didUpdateClientSettings:];
-[SBDashBoardPosterSwitcherViewController hostedAppBundleIdentifier];
-[SBDashBoardPosterSwitcherViewController setAppHostConfiguring:];
-[SBDashBoardPosterSwitcherViewController conformsToCSApplicationHosting];
-[SBDashBoardPosterSwitcherViewController applicationHoster];
-[SBDashBoardPosterSwitcherViewController handleEvent:];
-[SBDashBoardPosterSwitcherViewController setActivatingTouches:];
-[SBDashBoardPosterSwitcherViewController setStateCoordinationHandler:];
-[SBDashBoardPosterSwitcherViewController sceneHandle:didUpdateContentState:];
-[SBDashBoardPosterSwitcherViewController dismissForHomeButton];
-[SBDashBoardPosterSwitcherViewController hostedAppShouldHideHomeGrabberView];
-[SBDashBoardPosterSwitcherViewController clientSwitcherLayoutMode];
-[SBDashBoardPosterSwitcherViewController setHasEverGoneBeyondAlongside:];
-[SBDashBoardPosterSwitcherViewController _updateAdaptiveTimeTextHeightForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController handleBottomEdgeGestureEnded:];
-[SBDashBoardPosterSwitcherViewController setHasTransferredInitialTouches:];
-[SBDashBoardPosterSwitcherViewController vibrancyConfiguration];
-[SBDashBoardPosterSwitcherViewController targetWindow];
-[SBDashBoardPosterSwitcherViewController traitsAwareViewController];
-[SBDashBoardPosterSwitcherViewController zStackParticipant:updatePreferences:];
-[SBDashBoardPosterSwitcherViewController aggregateBehavior:];
-[SBDashBoardPosterSwitcherViewController _updatePreferredActiveAppearance:withReason:forSceneHandle:];
-[SBDashBoardPosterSwitcherViewController lastAdaptiveTimeTextHeight];
-[SBDashBoardPosterSwitcherViewController _applicationHosterDidInvalidate];
-[SBDashBoardPosterSwitcherViewController setInvalidationHandler:];
-[SBDashBoardPosterSwitcherViewController setFullscreenTransitionAnimationCount:];
-[SBDashBoardPosterSwitcherViewController setClientSwitcherLayoutMode:];
-[SBDashBoardPosterSwitcherViewController _updateLockVibrancyConfigurationForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController setHasCommittedInContentReadyState:];
-[SBDashBoardPosterSwitcherViewController sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBDashBoardPosterSwitcherViewController _evaluateInitialTouchTransferActuation];
-[SBDashBoardPosterSwitcherViewController _updateFloatingLayerInlinedForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController isCoverSheetComplicationRowHidden];
-[SBDashBoardPosterSwitcherViewController trailingTopButtonFrame];
-[SBDashBoardPosterSwitcherViewController hostedAppShouldInvalidateUponDeactivation];
-[SBDashBoardPosterSwitcherViewController appendToHostedAppSceneSettings:];
-[SBDashBoardPosterSwitcherViewController _updateLiveContentViewSpecificationForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController _effectiveSceneClientLayoutMode];
-[SBDashBoardPosterSwitcherViewController _dismissTier:];
-[SBDashBoardPosterSwitcherViewController appHostConfiguring];
-[SBDashBoardPosterSwitcherViewController handlesRotationIndependentOfCoverSheet];
-[SBDashBoardPosterSwitcherViewController hasCommittedInContentReadyState];
-[SBDashBoardPosterSwitcherViewController zStackParticipantDidChange:];
-[SBDashBoardPosterSwitcherViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBDashBoardPosterSwitcherViewController hasEverAppeared];
-[SBDashBoardPosterSwitcherViewController coverSheetFloatingView];
-[SBDashBoardPosterSwitcherViewController _dismissEntirely];
-[SBDashBoardPosterSwitcherViewController handleBottomEdgeGestureBegan:];
-[SBDashBoardPosterSwitcherViewController zStackParticipant:updateZOrderPreferences:];
-[SBDashBoardPosterSwitcherViewController sceneClientSettingsDiffInspector];
-[SBDashBoardPosterSwitcherViewController initWithNibName:bundle:];
-[SBDashBoardPosterSwitcherViewController stateCoordinationHandler];
-[SBDashBoardPosterSwitcherViewController handledInitialTransition];
-[SBDashBoardPosterSwitcherViewController _sendDismissEntirelyActionToScene];
-[SBDashBoardPosterSwitcherViewController _updateAppearanceWithClientLayoutMode:previousLayoutMode:transitionContext:];
-[SBDashBoardPosterSwitcherViewController viewWillAppear:];
-[SBDashBoardPosterSwitcherViewController activatingTouches];
-[SBDashBoardPosterSwitcherViewController conformsToSBApplicationHosting];
-[SBDashBoardPosterSwitcherViewController _updateTopButtonLayoutForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController _canShowWhileLocked];
-[SBDashBoardPosterSwitcherViewController aggregateAppearance:];
-[SBDashBoardPosterSwitcherViewController viewDidAppear:];
-[SBDashBoardPosterSwitcherViewController hostedAppShouldReactivateUponDestruction];
-[SBDashBoardPosterSwitcherViewController hostedAppSceneHandle];
-[SBDashBoardPosterSwitcherViewController _updateComplicationRowHiddenForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController canHostAnApp];
-[SBDashBoardPosterSwitcherViewController _updateOverlayViewSpecificationForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController setCoverSheetBackgroundView:];
-[SBDashBoardPosterSwitcherViewController loadView];
-[SBDashBoardPosterSwitcherViewController toFullscreenBlock];
-[SBDashBoardPosterSwitcherViewController setCoverSheetComplicationRowHidden:];
-[SBDashBoardPosterSwitcherViewController fullscreenTransitionAnimationCount];
-[SBDashBoardPosterSwitcherViewController setHandledInitialTransition:];
-[SBDashBoardPosterSwitcherViewController _evaluateInitialTransitionActivation];
-[SBDashBoardPosterSwitcherViewController hostedAppSceneHandles];
-[SBDashBoardPosterSwitcherViewController sceneHandle:didReceiveAction:];
-[SBDashBoardPosterSwitcherViewController hostedAppShouldDeactivateAfterDisappearance];
-[SBDashBoardPosterSwitcherViewController setLastAdaptiveTimeTextHeight:];
-[SBDashBoardPosterSwitcherViewController setHasEverAppeared:];
-[SBDashBoardPosterSwitcherViewController viewDidDisappear:];
-[SBDashBoardPosterSwitcherViewController _updateAppearanceWithoutAnimation];
-[SBDashBoardPosterSwitcherViewController setLeadingTopButtonFrame:trailingTopButtonFrame:];
-[SBDashBoardPosterSwitcherViewController invalidationHandler];
-[SBDashBoardPosterSwitcherViewController _initialAlongsideLayoutMode];
-[SBDashBoardPosterSwitcherViewController _updateLiveFloatingViewSpecificationForSceneSettings:];
-[SBDashBoardPosterSwitcherViewController setTargetWindow:];
-[SBDashBoardPosterSwitcherViewController setToFullscreenBlock:];
-[SBDashBoardPosterSwitcherViewController coverSheetBackgroundView];
-[SBDashBoardPosterSwitcherViewController handleBottomEdgeGestureChanged:];
-[SBDashBoardPosterSwitcherViewController setCoverSheetWallpaperView:];
-[SBDashBoardPosterSwitcherViewController _updateContentClippingPreference];
-[SBDashBoardPosterSwitcherViewController _transitionScene:toLayoutMode:animated:];
-[SBDashBoardPosterSwitcherViewController setCoverSheetFloatingView:];
-[SBDashBoardPosterSwitcherViewController isCoverSheetWallpaperFloatingLayerInlined];
-[SBDashBoardPosterSwitcherViewController coverSheetWallpaperView];
-[SBDashBoardPosterSwitcherViewController activeAppearanceAssertion];
-[SBDashBoardPosterSwitcherViewController hasEverGoneBeyondAlongside];
-[SBDashBoardPosterSwitcherViewController leadingTopButtonFrame];
-[SBDashBoardPosterSwitcherViewController hasTransferredInitialTouches];
-[SBDashBoardPosterSwitcherViewController isHostingAnApp];
-[SBDashBoardPosterSwitcherViewController setTraitsAwareViewController:];
-[SBDashBoardPosterSwitcherViewController setCoverSheetWallpaperFloatingLayerInlined:];
```
