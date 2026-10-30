# `SBAssistantIslandStageCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `SBAssistantIslandStageControllerDelegate`, `SBAssistantIslandStageGestureManagerDelegate`, `FBSceneObserver`, `SBRemoteTransientOverlaySessionManagerObserver`, `SBRemoteTransientOverlaySessionObserver`, `SBFIdleTimerBehaviorProviding`, `SBAmbientPresentationObserver`, `SBFMobileKeyBagObserver`, `FBProcessManagerObserver`, `FBProcessObserver`, `SBIdleTimerProviding`
- 22 instance variables, 23 properties, 125 instance methods, 1 class methods

## Instance variables

```
B _didRegisterAsManagerObserver;
B _lastPushedHasIdleTimerBehaviors;
@"NSMapTable" _ambientOrientationPolicyTokensByWindowScene;
@"NSMapTable" _zOrderStageResolverTokensByWindowScene;
@"NSMapTable" _windowSceneByAmbientPresentationController;
Q _rapidClientCrashCount;
Q _clientCrashCount;
B _prewarmDisabledUntilUnlock;
B _lastKeybagEffectivelyLocked;
@"<SBIdleTimerCoordinating>" _idleTimerCoordinator;
@"SBAssistantIslandWorkspace" _workspace;
@"SBAssistantIslandSettings" _settings;
@"NSMapTable" _controllersByWindowScene;
@"NSMapTable" _gestureManagersByWindowScene;
@"NSMapTable" _placeholderWindowsByWindowScene;
@"NSMapTable" _resignActiveManagersByWindowScene;
@"NSMapTable" _remoteOverlaySessionResignActiveAssertions;
@"PTTestRecipe" _toggleSearchAndVoiceTestRecipe;
@"PTTestRecipe" _toggleActivityResignActiveTestRecipe;
@"NSMutableSet" _testRecipeResignActiveAssertions;
@"SBBackgroundAngelKeepAliveHandler" _siriBackgroundHandler;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastTransientCanvasFrame;
```

## Properties

```
@property (T@"SBAssistantIslandSettings",R,N,V_settings) settings;
@property (T@"NSMapTable",R,N,V_controllersByWindowScene) controllersByWindowScene;
@property (T@"NSMapTable",R,N,V_gestureManagersByWindowScene) gestureManagersByWindowScene;
@property (T@"NSMapTable",R,N,V_placeholderWindowsByWindowScene) placeholderWindowsByWindowScene;
@property (T@"NSMapTable",R,N,V_resignActiveManagersByWindowScene) resignActiveManagersByWindowScene;
@property (T@"NSMapTable",R,N,V_remoteOverlaySessionResignActiveAssertions) remoteOverlaySessionResignActiveAssertions;
@property (T@"PTTestRecipe",R,N,V_toggleSearchAndVoiceTestRecipe) toggleSearchAndVoiceTestRecipe;
@property (T@"PTTestRecipe",R,N,V_toggleActivityResignActiveTestRecipe) toggleActivityResignActiveTestRecipe;
@property (T@"NSMutableSet",&,N,V_testRecipeResignActiveAssertions) testRecipeResignActiveAssertions;
@property (T@"SBBackgroundAngelKeepAliveHandler",&,N,V_siriBackgroundHandler) siriBackgroundHandler;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_lastTransientCanvasFrame) lastTransientCanvasFrame;
@property (T@"SBAssistantIslandWorkspace",W,N,V_workspace) workspace;
@property (T@"<SBIdleTimerCoordinating>",W,N,G_idleTimerCoordinator,S_setIdleTimerCoordinator:,V_idleTimerCoordinator) idleTimerCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Class methods

```
+[SBAssistantIslandStageCoordinator _setupInfo];
```

## Instance methods

```
-[SBAssistantIslandStageCoordinator _assistantIslandEnablementDidChange:];
-[SBAssistantIslandStageCoordinator _stageControllerForScene:];
-[SBAssistantIslandStageCoordinator lastTransientCanvasFrame];
-[SBAssistantIslandStageCoordinator sceneWillDeactivate:withError:];
-[SBAssistantIslandStageCoordinator stageController:didUpdateLastTransientCanvasFrameTo:];
-[SBAssistantIslandStageCoordinator workspace];
-[SBAssistantIslandStageCoordinator _isAssistantIslandVisiblyPresentedOnWindowScene:];
-[SBAssistantIslandStageCoordinator _windowSceneWithActivelyDrivingStageController];
-[SBAssistantIslandStageCoordinator draggableActivityFrameForWindowScene:];
-[SBAssistantIslandStageCoordinator sceneWillDeactivate:withContext:];
-[SBAssistantIslandStageCoordinator _idleTimerCoordinator];
-[SBAssistantIslandStageCoordinator sceneDidInvalidate:withContext:];
-[SBAssistantIslandStageCoordinator initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBAssistantIslandStageCoordinator _clientSettingsForScene:];
-[SBAssistantIslandStageCoordinator _updateBackgroundAngelKeepAlive];
-[SBAssistantIslandStageCoordinator _registerZOrderStageResolverForWindowSceneIfNeeded:];
-[SBAssistantIslandStageCoordinator _reduceMotionStatusDidChange:];
-[SBAssistantIslandStageCoordinator remoteTransientOverlaySession:didInvalidateWithReason:error:];
-[SBAssistantIslandStageCoordinator stageController:moveSceneController:toWindowScene:];
-[SBAssistantIslandStageCoordinator _stageControllerForGesture:];
-[SBAssistantIslandStageCoordinator _setupTestRecipes];
-[SBAssistantIslandStageCoordinator windowSceneDidDisconnect:];
-[SBAssistantIslandStageCoordinator processManager:didAddProcess:];
-[SBAssistantIslandStageCoordinator toggleSearchAndVoiceTestRecipe];
-[SBAssistantIslandStageCoordinator _windowSceneForStageController:];
-[SBAssistantIslandStageCoordinator _tearDownAllStageControllers];
-[SBAssistantIslandStageCoordinator _recheckIdleTimerBehaviorForReason:];
-[SBAssistantIslandStageCoordinator settings];
-[SBAssistantIslandStageCoordinator _relocatableStageControllerForWindowScene:];
-[SBAssistantIslandStageCoordinator dismissAssistantIslandOnAllWindowScenesIfNeeded];
-[SBAssistantIslandStageCoordinator ambientPresentationController:willUpdatePresented:];
-[SBAssistantIslandStageCoordinator dealloc];
-[SBAssistantIslandStageCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBAssistantIslandStageCoordinator idleTimerDuration];
-[SBAssistantIslandStageCoordinator remoteOverlaySessionResignActiveAssertions];
-[SBAssistantIslandStageCoordinator gestureManagerShouldActivityDragRequireClientGestureGate:];
-[SBAssistantIslandStageCoordinator stageController:acquireHomeGestureAssertionWithReason:];
-[SBAssistantIslandStageCoordinator _handleActivateSearchTestRecipe];
-[SBAssistantIslandStageCoordinator isActivityResignedActiveForStageController:];
-[SBAssistantIslandStageCoordinator _updateResidentInactiveStages];
-[SBAssistantIslandStageCoordinator gestureManager:beginGestureWithType:delegate:];
-[SBAssistantIslandStageCoordinator gestureManagerShouldSuppressSystemAperture:];
-[SBAssistantIslandStageCoordinator gestureManagersByWindowScene];
-[SBAssistantIslandStageCoordinator gestureManagerShouldFailActivityDragPastMaximumPressDurationWithoutHysteresis:];
-[SBAssistantIslandStageCoordinator _isGestureTypeEnabled:forWindowScene:];
-[SBAssistantIslandStageCoordinator gestureManagerActivityDragContentAvoidanceInsets:];
-[SBAssistantIslandStageCoordinator _releaseResignActiveAssertionForRemoteOverlaySession:];
-[SBAssistantIslandStageCoordinator activityPresentationPreferredTopRegionForWindowScene:];
-[SBAssistantIslandStageCoordinator _idleTimerBehavior];
-[SBAssistantIslandStageCoordinator isPoint:containedWithinStageContentForWindowScene:];
-[SBAssistantIslandStageCoordinator _invalidateSceneControllersForWindowScene:];
-[SBAssistantIslandStageCoordinator gestureManager:didBeginGesture:];
-[SBAssistantIslandStageCoordinator _settingsForScene:];
-[SBAssistantIslandStageCoordinator canBeginInteractiveSearchPresentationForWindowScene:];
-[SBAssistantIslandStageCoordinator siriBackgroundHandler];
-[SBAssistantIslandStageCoordinator _canShowWhileLocked];
-[SBAssistantIslandStageCoordinator _prepareCampoWorkspaceRequestAndUpdateWithBlock:];
-[SBAssistantIslandStageCoordinator _windowScenesToResignActiveForRemoteOverlaySession:reason:rearmWhileSessionIsActive:];
-[SBAssistantIslandStageCoordinator processDidExit:];
-[SBAssistantIslandStageCoordinator gestureManagerActivityDragHittestOutsets:];
-[SBAssistantIslandStageCoordinator gestureManager:didEndGesture:];
-[SBAssistantIslandStageCoordinator toggleActivityResignActiveTestRecipe];
-[SBAssistantIslandStageCoordinator controllersByWindowScene];
-[SBAssistantIslandStageCoordinator _anyOtherWindowSceneHasStageControllerThanWindowScene:];
-[SBAssistantIslandStageCoordinator _noteClientDidCrash];
-[SBAssistantIslandStageCoordinator gestureManagerIsActivityResignedActive:];
-[SBAssistantIslandStageCoordinator setSiriBackgroundHandler:];
-[SBAssistantIslandStageCoordinator processManager:didRemoveProcess:];
-[SBAssistantIslandStageCoordinator keybag:extendedStateDidChange:];
-[SBAssistantIslandStageCoordinator setTestRecipeResignActiveAssertions:];
-[SBAssistantIslandStageCoordinator placeholderWindowsByWindowScene];
-[SBAssistantIslandStageCoordinator resignActiveManagersByWindowScene];
-[SBAssistantIslandStageCoordinator _shouldHideForInvalidClientProcess];
-[SBAssistantIslandStageCoordinator remoteTransientOverlaySessionManager:didActivateSession:];
-[SBAssistantIslandStageCoordinator _remoteOverlayResignActiveSafetyReleaseTimeout];
-[SBAssistantIslandStageCoordinator stageControllerSystemChromeSuppressionDidChange:];
-[SBAssistantIslandStageCoordinator toggleSearchForWindowScene:spotlightInvocationSource:];
-[SBAssistantIslandStageCoordinator resignActiveAssertionManagerForStageController:];
-[SBAssistantIslandStageCoordinator windowDragGestureRecognizerForWindowScene:];
-[SBAssistantIslandStageCoordinator _scheduleSafetyReleaseForRemoteOverlaySession:assertion:rearmWhileSessionIsActive:];
-[SBAssistantIslandStageCoordinator configureSceneController:forWindowScene:];
-[SBAssistantIslandStageCoordinator _deactivateScene:];
-[SBAssistantIslandStageCoordinator dragGestureRecognizerForWindowScene:];
-[SBAssistantIslandStageCoordinator testRecipeResignActiveAssertions];
-[SBAssistantIslandStageCoordinator remoteTransientOverlaySessionDidDeactivate:];
-[SBAssistantIslandStageCoordinator _isDefaultPresenterDelegate];
-[SBAssistantIslandStageCoordinator _updateResidentInactiveStageForWindowScene:];
-[SBAssistantIslandStageCoordinator dismissAssistantIslandForWindowSceneIfNeeded:];
-[SBAssistantIslandStageCoordinator hasIdleTimerBehaviors];
-[SBAssistantIslandStageCoordinator gestureManager:didUpdateGesture:];
-[SBAssistantIslandStageCoordinator gestureManager:isGestureTypeEnabled:];
-[SBAssistantIslandStageCoordinator _fetchStageControllerForWindowScene:states:];
-[SBAssistantIslandStageCoordinator setWorkspace:];
-[SBAssistantIslandStageCoordinator transientCanvasFrameForWindowScene:];
-[SBAssistantIslandStageCoordinator _invalidateAllSceneControllers];
-[SBAssistantIslandStageCoordinator _handleActivateVoiceTestRecipe];
-[SBAssistantIslandStageCoordinator idleTimerMode];
-[SBAssistantIslandStageCoordinator _relocateStageController:fromWindowScene:toWindowScene:completion:];
-[SBAssistantIslandStageCoordinator gestureManagerActivityPresentationTopHittestRegion:];
-[SBAssistantIslandStageCoordinator _ambientPresentationControllerDidConnect:];
-[SBAssistantIslandStageCoordinator _handleResignActiveTestRecipe];
-[SBAssistantIslandStageCoordinator placeholderControllerForStageController:];
-[SBAssistantIslandStageCoordinator defaultScenePresenterForStageController:];
-[SBAssistantIslandStageCoordinator gestureManagerActivityDragRequiresEditingAvoidance:];
-[SBAssistantIslandStageCoordinator _allowsResidentInactiveStages];
-[SBAssistantIslandStageCoordinator _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBAssistantIslandStageCoordinator windowSceneDidConnect:];
-[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:dismissesControlCenterIfVisible:actions:completion:];
-[SBAssistantIslandStageCoordinator _isReduceMotionEnabled];
-[SBAssistantIslandStageCoordinator stageContentViewForWindowScene:];
-[SBAssistantIslandStageCoordinator isActiveOnWindowScene:];
-[SBAssistantIslandStageCoordinator idleWarnMode];
-[SBAssistantIslandStageCoordinator _setupBackgroundKeepAlive];
-[SBAssistantIslandStageCoordinator presentGestureRecognizerForWindowScene:];
-[SBAssistantIslandStageCoordinator _setIdleTimerCoordinator:];
-[SBAssistantIslandStageCoordinator stageControllerActiveStateDidChange:];
-[SBAssistantIslandStageCoordinator dismissAssistantIslandForWindowSceneIfNeeded:completion:];
-[SBAssistantIslandStageCoordinator _fetchStageControllerForWindowScene:state:];
-[SBAssistantIslandStageCoordinator _deviceSupportsAppleIntelligence];
-[SBAssistantIslandStageCoordinator gestureRecognizersForWindowScene:];
-[SBAssistantIslandStageCoordinator _isPrewarmDisabledForClientCrashLoop];
-[SBAssistantIslandStageCoordinator _stageControllerForDraggableActivityForWindowScene:];
-[SBAssistantIslandStageCoordinator coordinatorRequestedIdleTimerBehavior:];
-[SBAssistantIslandStageCoordinator _newAppSceneRequestOptionsForWindowScene:withBlueprintOptions:];
-[SBAssistantIslandStageCoordinator lastTransientCanvasFrameForWindowScene:];
```
