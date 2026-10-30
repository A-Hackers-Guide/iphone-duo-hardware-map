# `SBAssistantIslandStageController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBBacklightControllerObserver`, `SBLayoutStateTransitionObserver`, `SBAmbientPresentationObserver`, `SBAssistantIslandStagePlaceholderControllerDelegate`, `SBSceneHandleObserver`, `SBDeviceApplicationSceneHandleObserver`, `SBTransientOverlayPresentationManagerObserver`, `PTSettingsKeyObserver`, `SBAssistantIslandStageKeyboardPresenterDelegate`, `BSInvalidatable`, `SBAssistantIslandActivityElementViewProviderDelegate`, `SBAssistantIslandResignActiveAssertionManagerObserver`
- 41 instance variables, 27 properties, 103 instance methods, 5 class methods

## Instance variables

```
q _stageState;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastTransientCanvasContentFrame;
@"SBAssistantIslandActivityElement" _activityElement;
@"<SAInvalidatable>" _activityElementAssertion;
B _isFloatingDockFullyPresented;
d _floatingDockHeight;
d _floatingDockViewTopMargin;
q _spotlightInvocationSource;
B _shouldCleanupHomeScreenAfterTransitioning;
B _presentedOverApp;
{?="nanostamp"Q"isPointerTouch"B"isCanceled"B"touchTimestamp"d"location"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}"velocity"{CGPoint="x"d"y"d}"hysteresis"d} _initialGestureState;
q _activeGestureSource;
@"<BSInvalidatable>" _resignActiveAssertionToken;
@"<BSInvalidatable>" _systemApertureSuppressionAssertion;
@"<BSInvalidatable>" _keyboardFocusSuppressionAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _punchOutStatusBarHiddenAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _v68CoverDisplayTransientCanvasStatusBarHiddenAssertion;
B _systemChromeSuppressed;
q _currentViewProviderLayoutMode;
@"NSMutableArray" _pendingDismissCompletions;
Q _residentInactiveSettleGenerationCount;
B _hasStatusBarWindowLevelOverride;
@"SBAssistantIslandStageKeyboardPresenter" _keyboardPresenter;
B _ambientModeEntered;
B _invalidated;
B _hasSystemApertureBehavior;
B _isPresentationGestureValidForHomeScreenTranslation;
@"UIViewController" _contentViewController;
@"NSString" _stageDebugName;
@"SBWindowScene" _windowScene;
q _stageQuiescentPresentationState;
@"<SBAssistantIslandStageControllerDelegate>" _delegate;
@"SBAssistantIslandSettings" _settings;
@"SBAppSwitcherSettings" _switcherSettings;
@"FBScene" _scene;
@"SBAssistantIslandHomeGestureAssertion" _homeGestureAssertion;
@"<BSInvalidatable>" _displayLayoutAssertion;
@"SBAssistantIslandStagePlaceholderController" _searchPlaceholderController;
@"SBSingleSceneController" _sceneController;
@"AIRemoteGesture" _activeGesture;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _statusBarAvoidanceFrame;
```

## Properties

```
@property (T@"<SBAssistantIslandStageControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N,V_invalidated) invalidated;
@property (T@"SBAssistantIslandSettings",R,N,V_settings) settings;
@property (T@"SBAppSwitcherSettings",R,N,V_switcherSettings) switcherSettings;
@property (T@"FBScene",R,N,V_scene) scene;
@property (T@"SBAssistantIslandHomeGestureAssertion",R,N,V_homeGestureAssertion) homeGestureAssertion;
@property (T@"<BSInvalidatable>",R,N,V_displayLayoutAssertion) displayLayoutAssertion;
@property (TB,N,V_hasSystemApertureBehavior) hasSystemApertureBehavior;
@property (T@"SBAssistantIslandStagePlaceholderController",R,N,V_searchPlaceholderController) searchPlaceholderController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_statusBarAvoidanceFrame) statusBarAvoidanceFrame;
@property (TB,N,V_isPresentationGestureValidForHomeScreenTranslation) isPresentationGestureValidForHomeScreenTranslation;
@property (T@"SBSingleSceneController",&,N,V_sceneController) sceneController;
@property (TB,R,N) isResidentInactive;
@property (T@"AIRemoteGesture",R,W,N,V_activeGesture) activeGesture;
@property (T@"NSString",R,C,N,V_stageDebugName) stageDebugName;
@property (T@"UIViewController",R,N,V_contentViewController) contentViewController;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) stageContentFrame;
@property (Td,R,N) stageContentCornerRadius;
@property (Tq,R,N) stageState;
@property (Tq,R,N,V_stageQuiescentPresentationState) stageQuiescentPresentationState;
@property (TB,N,V_ambientModeEntered) ambientModeEntered;
@property (TB,R,N) wantsSystemChromeSuppressed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAssistantIslandStageController topEdgeZonesApplyToWindowScene:];
+[SBAssistantIslandStageController _statusBarAvoidanceFrameSettings];
+[SBAssistantIslandStageController defaultSystemApertureFrameForWindowScene:];
+[SBAssistantIslandStageController hasSystemApertureBehaviorForWindowScene:];
+[SBAssistantIslandStageController supportsCustomStageKeyboardPresentationForWindowScene:];
```

## Instance methods

```
-[SBAssistantIslandStageController backlightController:didTransitionToBacklightState:source:];
-[SBAssistantIslandStageController _assistantIslandEnablementDidChange:];
-[SBAssistantIslandStageController _dismiss];
-[SBAssistantIslandStageController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBAssistantIslandStageController contentViewForStageKeyboardPresenter:];
-[SBAssistantIslandStageController _coverSheetWillPresent:];
-[SBAssistantIslandStageController statusBarAvoidanceFrame];
-[SBAssistantIslandStageController _settings];
-[SBAssistantIslandStageController _createAndRegisterElementIfNeeded];
-[SBAssistantIslandStageController sceneWillActivate:];
-[SBAssistantIslandStageController _updateKeyboardFocusSuppression];
-[SBAssistantIslandStageController sceneHandle:didUpdateContentState:];
-[SBAssistantIslandStageController switcherSettings];
-[SBAssistantIslandStageController backlightController:willTransitionToBacklightState:source:];
-[SBAssistantIslandStageController _homeScreenProgress];
-[SBAssistantIslandStageController _controlCenterWillPresent:];
-[SBAssistantIslandStageController displayLayoutAssertion];
-[SBAssistantIslandStageController _setDisplayLayoutElementActive:];
-[SBAssistantIslandStageController setStatusBarAvoidanceFrame:];
-[SBAssistantIslandStageController resignActiveAssertionManagerDidChange:];
-[SBAssistantIslandStageController _updateHomeScreenStyle];
-[SBAssistantIslandStageController _homeScreenTranslationProgressForPresentationProgress:];
-[SBAssistantIslandStageController isResidentInactive];
-[SBAssistantIslandStageController relocateToWindowScene:completion:];
-[SBAssistantIslandStageController dismiss];
-[SBAssistantIslandStageController invalidated];
-[SBAssistantIslandStageController didBeginGesture:source:];
-[SBAssistantIslandStageController orientedBounds];
-[SBAssistantIslandStageController stageDebugName];
-[SBAssistantIslandStageController stageQuiescentPresentationState];
-[SBAssistantIslandStageController ambientModeEntered];
-[SBAssistantIslandStageController settings];
-[SBAssistantIslandStageController contentViewController];
-[SBAssistantIslandStageController _setHostWindowAlpha:];
-[SBAssistantIslandStageController isPresentationGestureValidForHomeScreenTranslation];
-[SBAssistantIslandStageController ambientPresentationController:willUpdatePresented:];
-[SBAssistantIslandStageController _updateStatusBarWindowLevelOverride];
-[SBAssistantIslandStageController viewProviderDidSettleContainerTransition:];
-[SBAssistantIslandStageController initWithDelegate:windowScene:spotlightInvocationSource:];
-[SBAssistantIslandStageController ambientPresentationController:didUpdatePresented:];
-[SBAssistantIslandStageController _hostingWindow];
-[SBAssistantIslandStageController _tearDownElement];
-[SBAssistantIslandStageController _updateListeningThinkingWaveSettings];
-[SBAssistantIslandStageController sceneContentStateDidChange:];
-[SBAssistantIslandStageController _supportsCustomStageKeyboardPresentation];
-[SBAssistantIslandStageController stageContentCornerRadius];
-[SBAssistantIslandStageController _updateSystemChromeSuppression];
-[SBAssistantIslandStageController windowSceneForStageKeyboardPresenter:];
-[SBAssistantIslandStageController _updateStatusBarAvoidanceFrame];
-[SBAssistantIslandStageController _rubberband:fromMinV:maxV:range:factor:];
-[SBAssistantIslandStageController _homeScreenTranslationForProgress:];
-[SBAssistantIslandStageController hostingWindowForStageKeyboardPresenter:];
-[SBAssistantIslandStageController settings:changedValueForKey:];
-[SBAssistantIslandStageController setSceneController:];
-[SBAssistantIslandStageController _defaultSystemApertureFrame];
-[SBAssistantIslandStageController sceneController];
-[SBAssistantIslandStageController setIsPresentationGestureValidForHomeScreenTranslation:];
-[SBAssistantIslandStageController _activityElementViewProvider];
-[SBAssistantIslandStageController _hasSystemApertureBehavior];
-[SBAssistantIslandStageController wantsSystemChromeSuppressed];
-[SBAssistantIslandStageController _updateSystemApertureBehaviorSettings];
-[SBAssistantIslandStageController invalidate];
-[SBAssistantIslandStageController _presentationProgress];
-[SBAssistantIslandStageController _updateSystemApertureAnimationStyle];
-[SBAssistantIslandStageController _updateResidentInactive];
-[SBAssistantIslandStageController viewProvider:didUpdateLayoutMode:];
-[SBAssistantIslandStageController updateSpotlightInvocationSource:];
-[SBAssistantIslandStageController sceneForStageKeyboardPresenter:];
-[SBAssistantIslandStageController scene];
-[SBAssistantIslandStageController _sceneClientSettingsDidUpdate];
-[SBAssistantIslandStageController placeholderControllerDidInvalidate:];
-[SBAssistantIslandStageController searchPlaceholderController];
-[SBAssistantIslandStageController _homeScreenAnimator];
-[SBAssistantIslandStageController activeGesture];
-[SBAssistantIslandStageController dismissWithCompletion:];
-[SBAssistantIslandStageController homeGestureAssertion];
-[SBAssistantIslandStageController _dockHeightWillChange:];
-[SBAssistantIslandStageController delegate];
-[SBAssistantIslandStageController ensureActivityElementRegistered];
-[SBAssistantIslandStageController _clientSettings];
-[SBAssistantIslandStageController _postAssistantIslandLayoutUpdate];
-[SBAssistantIslandStageController viewProviderDidBeginCooperativeDismissal:];
-[SBAssistantIslandStageController _resignActiveStateDidChange];
-[SBAssistantIslandStageController resignActiveAssertionManagerDidSettle:];
-[SBAssistantIslandStageController _updateInitialSceneSettings];
-[SBAssistantIslandStageController _updateHostingDisplayBacklightStateActive];
-[SBAssistantIslandStageController stageState];
-[SBAssistantIslandStageController _updateHomeScreenStyleWithProgress:animationMode:enableHomeScreenTranslation:];
-[SBAssistantIslandStageController _applyListeningThinkingWaveSettings:];
-[SBAssistantIslandStageController _canMoveAcrossDisplays];
-[SBAssistantIslandStageController beginGestureWithType:delegate:];
-[SBAssistantIslandStageController hasSystemApertureBehavior];
-[SBAssistantIslandStageController didUpdateGesture:];
-[SBAssistantIslandStageController windowScene];
-[SBAssistantIslandStageController transientOverlayPresentationManager:willPresentViewController:];
-[SBAssistantIslandStageController didEndGesture:];
-[SBAssistantIslandStageController stageContentFrame];
-[SBAssistantIslandStageController _isActivityResignedActive];
-[SBAssistantIslandStageController viewProvider:didUpdateContainerFrame:];
-[SBAssistantIslandStageController scene:didUpdateClientSettings:];
-[SBAssistantIslandStageController _setSceneActivityMode:jetsamPriority:];
-[SBAssistantIslandStageController setAmbientModeEntered:];
-[SBAssistantIslandStageController setHasSystemApertureBehavior:];
```
