# `SBDashBoardCameraPageViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSPageViewController`
- Protocols: `SBDashBoardHostedAppViewControllerDelegate`, `SBSceneHandleObserver`, `FBSceneObserver`, `SBSystemGestureRecognizerDelegate`, `SBHomeGesturePanGestureRecognizerContextDelegate`, `SBFZStackParticipantDelegate`, `SBHomeGrabberDelegate`, `SBHomeGrabberPointerClickDelegate`, `SBHomeGestureInteractionDelegate`, `CSHostableEntityPresenterDelegate`, `SBAccidentalActivationMitigationSessionCoordinatorObserver`, `CSHostedEntityTransferCoordinationObserving`, `SBSystemApertureZStackPolicyAssistantWindowSceneProviding`, `SBApplicationHosting`, `CSEntityHosting`
- 38 instance variables, 22 properties, 142 instance methods, 2 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"UIView" _maskView;
@"UIView" _tintView;
@"SBDashBoardHostedAppViewController" _appViewController;
@"SBTraitsSceneParticipantDelegate" _traitsParticipantDelegate;
@"SBDashBoardTraitsOrientedContentViewController" _orientedContentViewController;
@"UIViewController" _appViewControllerContainerVC;
B _interactiveDismissalInProgress;
B _hasWarmedCameraForThisPresentation;
B _cameraPrewarmSucceeded;
B _hasPendingHostedEntityGoLiveRequest;
q _cameraPresentLargestPercent;
d _presentationProgress;
@"NSTimer" _prewarmDebounceTimer;
@"NSTimer" _prewarmCancelTimer;
@"CSLockScreenSettings" _prototypeSettings;
@"SBLockScreenDefaults" _lockScreenDefaults;
B _didConfigureSceneEntity;
@"NSString" _cachedBasicPublicDescription;
B _needsDeferredEntityReset;
@"SBSceneHandle" _observedSceneHandle;
@"FBScene" _observedScene;
B _wantsHomeGestureOwnership;
B _enforcesViewWindowRequirements;
B _canWarmRealCamera;
@"<BSInvalidatable>" _entityPreservationToken;
@"<SBDashBoardCameraPageViewControllerDelegate>" _cameraPageDelegate;
@"SBHomeGestureInteraction" _homeGestureInteraction;
@"UIViewFloatAnimatableProperty" _scaleProperty;
@"UIViewFloatAnimatableProperty" _alphaProperty;
@"SBFFluidBehaviorSettings" _scaleSettings;
@"SBFFluidBehaviorSettings" _alphaSettings;
@"SBFZStackParticipant" _zStackParticipant;
@"TRAParticipant" _traitsParticipant;
@"SBAudioCategoryZStackPolicyAssistant" _audioCategoryZStackPolicyAssistant;
@"SBSystemApertureZStackPolicyAssistant" _systemApertureZStackPolicyAssistant;
@"SBPhysicalButtonZStackPolicyAssistant" _physicalButtonZStackPolicyAssistant;
@"CSHostedEntityViewController" _hostedEntityViewController;
```

## Properties

```
@property (TB,N,V_wantsHomeGestureOwnership) wantsHomeGestureOwnership;
@property (T@"SBHomeGestureInteraction",&,N,V_homeGestureInteraction) homeGestureInteraction;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_scaleProperty) scaleProperty;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_alphaProperty) alphaProperty;
@property (T@"SBFFluidBehaviorSettings",&,N,V_scaleSettings) scaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_alphaSettings) alphaSettings;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (T@"TRAParticipant",&,N,V_traitsParticipant) traitsParticipant;
@property (T@"SBAudioCategoryZStackPolicyAssistant",&,N,V_audioCategoryZStackPolicyAssistant) audioCategoryZStackPolicyAssistant;
@property (T@"SBSystemApertureZStackPolicyAssistant",&,N,V_systemApertureZStackPolicyAssistant) systemApertureZStackPolicyAssistant;
@property (T@"SBPhysicalButtonZStackPolicyAssistant",&,N,V_physicalButtonZStackPolicyAssistant) physicalButtonZStackPolicyAssistant;
@property (T@"CSHostedEntityViewController",&,N,V_hostedEntityViewController) hostedEntityViewController;
@property (TB,N,V_enforcesViewWindowRequirements) enforcesViewWindowRequirements;
@property (TB,N,V_canWarmRealCamera) canWarmRealCamera;
@property (T@"<CSHostableEntity>",&,D,N) hostedEntity;
@property (T@"<SBDashBoardCameraPageViewControllerDelegate>",W,N,V_cameraPageDelegate) cameraPageDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BSInvalidatable>",?,&,N,V_entityPreservationToken) entityPreservationToken;
@property (T@"NSSet",?,&,N) actionsToDeliver;
```

## Class methods

```
+[SBDashBoardCameraPageViewController requiredCapabilities];
+[SBDashBoardCameraPageViewController isAvailableForConfiguration];
```

## Instance methods

```
-[SBDashBoardCameraPageViewController sceneHandle:didDestroyScene:];
-[SBDashBoardCameraPageViewController sceneHandle:didCreateScene:];
-[SBDashBoardCameraPageViewController sceneHandle:clientConnectedForScene:];
-[SBDashBoardCameraPageViewController sceneHandle:didUpdateClientSettings:];
-[SBDashBoardCameraPageViewController zStackParticipant];
-[SBDashBoardCameraPageViewController _prepareForInteractiveGestureToCameraVisible:];
-[SBDashBoardCameraPageViewController hostableEntityPresenter:didBeginHosting:];
-[SBDashBoardCameraPageViewController _takeHiddenAssertionForHomeGrabber:];
-[SBDashBoardCameraPageViewController hostableEntityPresenter:didEndHosting:];
-[SBDashBoardCameraPageViewController hostedEntity];
-[SBDashBoardCameraPageViewController acquireLiveContentAssertionForReason:];
-[SBDashBoardCameraPageViewController setSystemApertureZStackPolicyAssistant:];
-[SBDashBoardCameraPageViewController conformsToCSApplicationHosting];
-[SBDashBoardCameraPageViewController handleEvent:];
-[SBDashBoardCameraPageViewController setZStackParticipant:];
-[SBDashBoardCameraPageViewController wouldHandleButtonEvent:];
-[SBDashBoardCameraPageViewController _prewarmCameraInteractively:];
-[SBDashBoardCameraPageViewController sceneObserverWantsUpdatesFromInactiveScenes];
-[SBDashBoardCameraPageViewController sceneDidInvalidate:withContext:];
-[SBDashBoardCameraPageViewController _shouldCancelInteractiveDismissGesture];
-[SBDashBoardCameraPageViewController presentationAltitude];
-[SBDashBoardCameraPageViewController homeGrabberViewDidReceiveClick:];
-[SBDashBoardCameraPageViewController updateTransitionToVisible:progress:mode:];
-[SBDashBoardCameraPageViewController dashBoardHostedAppViewControllerDidFailToActivateApplication:];
-[SBDashBoardCameraPageViewController _createPropertiesWithView:];
-[SBDashBoardCameraPageViewController zStackParticipant:updatePreferences:];
-[SBDashBoardCameraPageViewController _convertTranslationFromContainerOrientationToContentOrientation:];
-[SBDashBoardCameraPageViewController aggregateBehavior:];
-[SBDashBoardCameraPageViewController actionsToDeliver];
-[SBDashBoardCameraPageViewController physicalButtonZStackPolicyAssistant];
-[SBDashBoardCameraPageViewController _updateSceneHandleObservation];
-[SBDashBoardCameraPageViewController setHostedEntityViewController:];
-[SBDashBoardCameraPageViewController scene:didUpdateSettings:];
-[SBDashBoardCameraPageViewController viewWillDisappear:];
-[SBDashBoardCameraPageViewController _sbAnimationUpdateModeForCoverSheetTransitionMode:];
-[SBDashBoardCameraPageViewController _removeSceneHandleObservation];
-[SBDashBoardCameraPageViewController sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBDashBoardCameraPageViewController _hostedContentModeDescription];
-[SBDashBoardCameraPageViewController accidentalActivationMitigationSessionCoordinator:didMitigateMitigationSession:];
-[SBDashBoardCameraPageViewController initWithApplicationController:];
-[SBDashBoardCameraPageViewController _updateDimmingAlpha:transitionMode:];
-[SBDashBoardCameraPageViewController alphaSettings];
-[SBDashBoardCameraPageViewController _invalidateZStackParticipantIfNeeded];
-[SBDashBoardCameraPageViewController _updateCameraScale:transitionMode:];
-[SBDashBoardCameraPageViewController canWarmRealCamera];
-[SBDashBoardCameraPageViewController homeGestureInteraction:shouldReceiveTouch:];
-[SBDashBoardCameraPageViewController _endPrewarmBackoffPeriod];
-[SBDashBoardCameraPageViewController _updateCameraScale:dimmingAlpha:];
-[SBDashBoardCameraPageViewController handlesRotationIndependentOfCoverSheet];
-[SBDashBoardCameraPageViewController scaleProperty];
-[SBDashBoardCameraPageViewController setCameraPageDelegate:];
-[SBDashBoardCameraPageViewController _prewarmingCameraBundleIdentifier];
-[SBDashBoardCameraPageViewController willTransitionToVisible:];
-[SBDashBoardCameraPageViewController zStackParticipantDidChange:];
-[SBDashBoardCameraPageViewController _resetHostedEntityToDefault];
-[SBDashBoardCameraPageViewController homeGestureInteraction];
-[SBDashBoardCameraPageViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBDashBoardCameraPageViewController setCanWarmRealCamera:];
-[SBDashBoardCameraPageViewController setHomeGestureInteraction:];
-[SBDashBoardCameraPageViewController systemApertureZStackPolicyAssistant];
-[SBDashBoardCameraPageViewController _passesHasVisibleWindowTest];
-[SBDashBoardCameraPageViewController zStackParticipant:updateZOrderPreferences:];
-[SBDashBoardCameraPageViewController homeGestureInteractionBegan:];
-[SBDashBoardCameraPageViewController hostedEntityTransferCoordinationDidEnd:];
-[SBDashBoardCameraPageViewController _requestHomeGestureOwnership];
-[SBDashBoardCameraPageViewController setPhysicalButtonZStackPolicyAssistant:];
-[SBDashBoardCameraPageViewController setWantsHomeGestureOwnership:];
-[SBDashBoardCameraPageViewController _traitsArbiter];
-[SBDashBoardCameraPageViewController handleAction:fromSender:];
-[SBDashBoardCameraPageViewController viewForSystemGestureRecognizer:];
-[SBDashBoardCameraPageViewController _updateForPropertyChangedForPresentation:];
-[SBDashBoardCameraPageViewController viewWillAppear:];
-[SBDashBoardCameraPageViewController conformsToSBApplicationHosting];
-[SBDashBoardCameraPageViewController homeGestureInteraction:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBDashBoardCameraPageViewController homeGestureInteractionChanged:];
-[SBDashBoardCameraPageViewController aggregateAppearance:];
-[SBDashBoardCameraPageViewController setActionsToDeliver:];
-[SBDashBoardCameraPageViewController setHostedEntity:];
-[SBDashBoardCameraPageViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBDashBoardCameraPageViewController viewDidAppear:];
-[SBDashBoardCameraPageViewController scaleSettings];
-[SBDashBoardCameraPageViewController setAlphaSettings:];
-[SBDashBoardCameraPageViewController hostedAppSceneHandle];
-[SBDashBoardCameraPageViewController setScaleSettings:];
-[SBDashBoardCameraPageViewController canHostAnApp];
-[SBDashBoardCameraPageViewController alphaProperty];
-[SBDashBoardCameraPageViewController _addOrRemoveGestureForCurrentSettings];
-[SBDashBoardCameraPageViewController _ensureZStackParticipantForced:];
-[SBDashBoardCameraPageViewController additionalEdgeSpacingForHomeGrabberView:];
-[SBDashBoardCameraPageViewController loadView];
-[SBDashBoardCameraPageViewController entityPreservationToken];
-[SBDashBoardCameraPageViewController accidentalActivationMitigationSessionCoordinator:didStartMitigationSession:];
-[SBDashBoardCameraPageViewController setScaleProperty:];
-[SBDashBoardCameraPageViewController audioCategoryZStackPolicyAssistant];
-[SBDashBoardCameraPageViewController hostableEntityPresenter:didFailToActivate:];
-[SBDashBoardCameraPageViewController _setupHostingViewControllerHierarchyIfNeeded];
-[SBDashBoardCameraPageViewController _updateCameraScale:dimmingAlpha:transitionMode:];
-[SBDashBoardCameraPageViewController _setSceneGrabberHidden:];
-[SBDashBoardCameraPageViewController hostedAppSceneHandles];
-[SBDashBoardCameraPageViewController dashBoardHostedAppViewController:shouldTransitionToMode:];
-[SBDashBoardCameraPageViewController _coolCameraIfNecessary];
-[SBDashBoardCameraPageViewController wantsHomeGestureOwnership];
-[SBDashBoardCameraPageViewController homeGestureInteractionEnded:];
-[SBDashBoardCameraPageViewController setAudioCategoryZStackPolicyAssistant:];
-[SBDashBoardCameraPageViewController homeGestureInteraction:systemGestureTypeForType:];
-[SBDashBoardCameraPageViewController setEntityPreservationToken:];
-[SBDashBoardCameraPageViewController requestedDismissalType];
-[SBDashBoardCameraPageViewController touchInterfaceOrientationForHomeGesturePanGestureRecognizer:];
-[SBDashBoardCameraPageViewController viewDidDisappear:];
-[SBDashBoardCameraPageViewController _acquireTraitsParticipant];
-[SBDashBoardCameraPageViewController _resetAfterInteractiveGestureToCameraVisible:];
-[SBDashBoardCameraPageViewController _invalidateCameraTraitsParticipant];
-[SBDashBoardCameraPageViewController customScreenEdgePanGestureRecognizerForHomeGestureInteraction:];
-[SBDashBoardCameraPageViewController _transitionAppViewWithProgress:transitionMode:];
-[SBDashBoardCameraPageViewController homeGestureInteractionCancelled:];
-[SBDashBoardCameraPageViewController accidentalActivationMitigationSessionCoordinator:didCancelMitigationSession:];
-[SBDashBoardCameraPageViewController requestedDismissalSettings];
-[SBDashBoardCameraPageViewController _prelaunchThreshold];
-[SBDashBoardCameraPageViewController _handlePrelaunchForTransitionToVisible:mode:];
-[SBDashBoardCameraPageViewController cameraPageDelegate];
-[SBDashBoardCameraPageViewController homeGestureInteraction:shouldBeginGestureRecognizerOfType:];
-[SBDashBoardCameraPageViewController noteDefaultHostableEntityMayHaveChanged];
-[SBDashBoardCameraPageViewController traitsParticipant];
-[SBDashBoardCameraPageViewController enforcesViewWindowRequirements];
-[SBDashBoardCameraPageViewController _makeApplicationStatic];
-[SBDashBoardCameraPageViewController _addObservationForSceneIfNeeded:];
-[SBDashBoardCameraPageViewController _shouldPrelaunchOnSwipe];
-[SBDashBoardCameraPageViewController pageRole];
-[SBDashBoardCameraPageViewController setAlphaProperty:];
-[SBDashBoardCameraPageViewController _prewarmThreshold];
-[SBDashBoardCameraPageViewController _relinquishHiddenAssertionForHomeGrabber:];
-[SBDashBoardCameraPageViewController _updateZStackPolicyAssistants];
-[SBDashBoardCameraPageViewController isHostingAnApp];
-[SBDashBoardCameraPageViewController setEnforcesViewWindowRequirements:];
-[SBDashBoardCameraPageViewController _handlePrewarmForTransitionToVisible:mode:];
-[SBDashBoardCameraPageViewController _bailIfFaceTimeCallComesIn];
-[SBDashBoardCameraPageViewController setTraitsParticipant:];
-[SBDashBoardCameraPageViewController didTransitionToVisible:];
-[SBDashBoardCameraPageViewController _shouldPrewarmOnSwipe];
-[SBDashBoardCameraPageViewController hostedEntityViewController];
-[SBDashBoardCameraPageViewController _noteUserLaunchEventTime];
-[SBDashBoardCameraPageViewController windowSceneForSystemApertureZStackPolicyAssistant:];
```
