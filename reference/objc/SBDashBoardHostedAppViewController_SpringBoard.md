# `SBDashBoardHostedAppViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDashBoardViewExternalControllerBase`
- Protocols: `SBAppViewControllerDelegate`, `SBApplicationSceneHandleUpdateContributing`, `SBSceneHandleObserver`, `SBMainDisplaySceneLayoutStatusBarViewDataSource`, `SBDeviceApplicationSceneStatusBarStateObserver`, `SBApplicationSceneViewControllingStatusBarDelegate`, `CSHostedEntityTransferCoordinationObserving`, `SBApplicationHosting`, `BSInvalidatable`
- 22 instance variables, 19 properties, 94 instance methods, 0 class methods

## Instance variables

```
@"<SBDashBoardHostedAppViewControllerDelegate>" _delegate;
@"SBAppViewController" _appViewController;
@"UIApplicationSceneDeactivationAssertion" _resignActiveAssertion;
@"UIApplicationSceneDeactivationAssertion" _transferDeactivationAssertion;
@"SBFAuthenticationAssertion" _authenticationAssertion;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
@"NSString" _cachedBasicPublicDescription;
B _invalidated;
B _wantsIdleTimerDisabled;
B _waitingToDeactivateAfterDisappearance;
B _hasPendingAppearance;
@"SBMainDisplaySceneLayoutStatusBarView" _statusBarView;
@"_SBDashBoardHostedAppStatusBarStateProxy" _statusBarObserverProxy;
@"UIApplicationSceneClientSettingsDiffInspector" _appClientSettingsDiffInspector;
@"<BSInvalidatable>" _suspensionUnderLockExemption;
B _preventSceneBackgrounding;
B _intentToTransitionFromSecureAppToFull;
B _interfaceOrientationLocked;
B _providesIdleTimerDuration;
q _overrideIdleWarnMode;
@"<CSAppHostContextProviding>" _hostContextProvider;
@? _invalidationHandler;
```

## Properties

```
@property (T@"<SBApplicationSceneStatusBarDescribing>",R,N,V_statusBarObserverProxy) statusBarDescriber;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (TB,N,V_preventSceneBackgrounding) preventSceneBackgrounding;
@property (T@"<SBDashBoardHostedAppViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBApplicationSceneHandle",R,N) applicationSceneHandle;
@property (T@"SBApplicationSceneView",R,N) appView;
@property (T@"<SBScenePlaceholderContentContext>",&,N) placeholderContentContext;
@property (T@"<CSAppHostContextProviding>",W,N,V_hostContextProvider) hostContextProvider;
@property (Tq,N) mode;
@property (T@"NSSet",&,N) actionsToDeliver;
@property (TB,N,V_intentToTransitionFromSecureAppToFull) intentToTransitionFromSecureAppToFull;
@property (TB,N) placeholderContentEnabled;
@property (TB,N,V_interfaceOrientationLocked) interfaceOrientationLocked;
@property (TB,N,V_providesIdleTimerDuration) providesIdleTimerDuration;
@property (Tq,N,V_overrideIdleWarnMode) overrideIdleWarnMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardHostedAppViewController sceneHandle:didCreateScene:];
-[SBDashBoardHostedAppViewController sceneHandle:didUpdateClientSettings:];
-[SBDashBoardHostedAppViewController presentationType];
-[SBDashBoardHostedAppViewController handleEvent:];
-[SBDashBoardHostedAppViewController _endShowingStatusBarView];
-[SBDashBoardHostedAppViewController initWithApplicationSceneEntity:];
-[SBDashBoardHostedAppViewController _isHostedEntityBeingPreserved];
-[SBDashBoardHostedAppViewController appViewControllerDidFailToActivateApplication:];
-[SBDashBoardHostedAppViewController _setResignActiveAssertionEnabled:];
-[SBDashBoardHostedAppViewController statusBarDescriberForStatusBarPart:];
-[SBDashBoardHostedAppViewController setProvidesIdleTimerDuration:];
-[SBDashBoardHostedAppViewController appViewControllerShouldBackgroundApplicationOnDeactivate:];
-[SBDashBoardHostedAppViewController _updateSuspensionUnderLockExemption];
-[SBDashBoardHostedAppViewController setTransferringBetweenWindowScenes:];
-[SBDashBoardHostedAppViewController appearanceIdentifier];
-[SBDashBoardHostedAppViewController _deactivateIfAppropriateForReason:];
-[SBDashBoardHostedAppViewController aggregateBehavior:];
-[SBDashBoardHostedAppViewController actionsToDeliver];
-[SBDashBoardHostedAppViewController setInvalidationHandler:];
-[SBDashBoardHostedAppViewController viewIsAppearing:];
-[SBDashBoardHostedAppViewController viewWillDisappear:];
-[SBDashBoardHostedAppViewController applicationSceneHandle];
-[SBDashBoardHostedAppViewController setOverrideIdleWarnMode:];
-[SBDashBoardHostedAppViewController appViewControllerShouldReactivateApplicationOnDestruction:];
-[SBDashBoardHostedAppViewController setPlaceholderContentContext:];
-[SBDashBoardHostedAppViewController dealloc];
-[SBDashBoardHostedAppViewController presentationPriority];
-[SBDashBoardHostedAppViewController _containerInterfaceOrientation];
-[SBDashBoardHostedAppViewController presentationStyle];
-[SBDashBoardHostedAppViewController _shouldInvalidateUponDeactivation];
-[SBDashBoardHostedAppViewController willMoveToParentViewController:];
-[SBDashBoardHostedAppViewController viewDidLoad];
-[SBDashBoardHostedAppViewController setPlaceholderContentEnabled:];
-[SBDashBoardHostedAppViewController handlesRotationIndependentOfCoverSheet];
-[SBDashBoardHostedAppViewController setSupplementalActivationSettings:];
-[SBDashBoardHostedAppViewController appView];
-[SBDashBoardHostedAppViewController _shouldDelayDeactivationUntilAfterDisappearance];
-[SBDashBoardHostedAppViewController setPreventSceneBackgrounding:];
-[SBDashBoardHostedAppViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBDashBoardHostedAppViewController sceneWithIdentifier:didChangeSceneInterfaceOrientationTo:];
-[SBDashBoardHostedAppViewController preventSceneBackgrounding];
-[SBDashBoardHostedAppViewController _newDisplayLayoutElement];
-[SBDashBoardHostedAppViewController hostedEntityTransferCoordinationDidEnd:];
-[SBDashBoardHostedAppViewController setMode:];
-[SBDashBoardHostedAppViewController interfaceOrientationLocked];
-[SBDashBoardHostedAppViewController viewWillAppear:];
-[SBDashBoardHostedAppViewController conformsToSBApplicationHosting];
-[SBDashBoardHostedAppViewController invalidate];
-[SBDashBoardHostedAppViewController appViewControllerWillActivateApplication:];
-[SBDashBoardHostedAppViewController aggregateAppearance:];
-[SBDashBoardHostedAppViewController appViewController:didTransitionFromMode:toMode:];
-[SBDashBoardHostedAppViewController setDelegate:];
-[SBDashBoardHostedAppViewController setActionsToDeliver:];
-[SBDashBoardHostedAppViewController _contentInterfaceOrientation];
-[SBDashBoardHostedAppViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBDashBoardHostedAppViewController viewDidAppear:];
-[SBDashBoardHostedAppViewController setHostedAppReferenceSize:withInterfaceOrientation:];
-[SBDashBoardHostedAppViewController hostedAppSceneHandle];
-[SBDashBoardHostedAppViewController overrideIdleWarnMode];
-[SBDashBoardHostedAppViewController applicationSceneViewController:didUpdateStatusBarSettings:];
-[SBDashBoardHostedAppViewController setIntentToTransitionFromSecureAppToFull:];
-[SBDashBoardHostedAppViewController _appViewController];
-[SBDashBoardHostedAppViewController canHostAnApp];
-[SBDashBoardHostedAppViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBDashBoardHostedAppViewController _updateDisplayIdentityForWindow:];
-[SBDashBoardHostedAppViewController appViewControllerDidDeactivateApplication:];
-[SBDashBoardHostedAppViewController appViewControllerIsInNonRotatingWindow:];
-[SBDashBoardHostedAppViewController mode];
-[SBDashBoardHostedAppViewController setInterfaceOrientationLocked:];
-[SBDashBoardHostedAppViewController hostedAppSceneHandles];
-[SBDashBoardHostedAppViewController delegate];
-[SBDashBoardHostedAppViewController allowsConfiguringIndividualStatusBarParts];
-[SBDashBoardHostedAppViewController providesIdleTimerDuration];
-[SBDashBoardHostedAppViewController statusBarDescribers];
-[SBDashBoardHostedAppViewController applicationSceneHandle:appendToSceneSettings:fromRequestContext:entity:];
-[SBDashBoardHostedAppViewController _updateDisplayLayoutElementForActivation:];
-[SBDashBoardHostedAppViewController viewDidDisappear:];
-[SBDashBoardHostedAppViewController isTransferringBetweenWindowScenes];
-[SBDashBoardHostedAppViewController appViewControllerShouldHideHomeGrabberView:];
-[SBDashBoardHostedAppViewController setHostContextProvider:];
-[SBDashBoardHostedAppViewController statusBarOrientation];
-[SBDashBoardHostedAppViewController invalidationHandler];
-[SBDashBoardHostedAppViewController _updateStatusBarContainerOrientation];
-[SBDashBoardHostedAppViewController _beginShowingStatusBarView];
-[SBDashBoardHostedAppViewController containerDidUpdateTraitsParticipant:];
-[SBDashBoardHostedAppViewController intentToTransitionFromSecureAppToFull];
-[SBDashBoardHostedAppViewController _setMode:fromClient:forReason:];
-[SBDashBoardHostedAppViewController _addStatusBarViewIfNeeded];
-[SBDashBoardHostedAppViewController _deviceApplicationSceneHandle];
-[SBDashBoardHostedAppViewController isHostingAnApp];
-[SBDashBoardHostedAppViewController placeholderContentEnabled];
-[SBDashBoardHostedAppViewController placeholderContentContext];
-[SBDashBoardHostedAppViewController statusBarDescriber];
-[SBDashBoardHostedAppViewController hostContextProvider];
```
