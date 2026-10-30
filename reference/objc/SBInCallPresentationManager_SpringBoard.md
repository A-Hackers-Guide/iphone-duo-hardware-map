# `SBInCallPresentationManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBInCallPresentationSessionDelegate`, `SBInCallPresentationRequestServerDelegate`, `FBSceneManagerObserver`, `SBSceneManagerObserver`, `SBFBacklightEnvironmentSceneProviding`, `SBApplicationHosting`
- 12 instance variables, 12 properties, 62 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBInCallPresentationRequestServer" _presentationRequestServer;
@"SBInCallBannerAuthority" _inCallBannerAuthority;
@"SBExpanseBannerAuthority" _expanseBannerAuthority;
@"NSMutableDictionary" _clientIdentifierToPresentationSession;
@"NSMutableArray" _pendingInvalidationSessions;
@"NSMutableSet" _bundleIdentifiersOfObservedApplications;
@"BSCompoundAssertion" _nonModalSuppressionAssertions;
B _supportsHandlingUILockForWindowedAccessoryAttach;
@"SBHideSharePlayContentFromSharedScreenController" _lazy_hideSharePlayContentFromSharedScreenController;
@"<SBInCallPresentationManagerDelegate>" _delegate;
@"SBWindowSceneManager" _windowSceneManager;
```

## Properties

```
@property (T@"SBInCallPresentationSession",R,N) _lastPresentationSession;
@property (T@"<SBInCallPresentationManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBWindowSceneManager",R,N,V_windowSceneManager) windowSceneManager;
@property (T@"SBHideSharePlayContentFromSharedScreenController",R,N,V_lazy_hideSharePlayContentFromSharedScreenController) hideSharePlayContentFromSharedScreenController;
@property (TB,R,N) supportsHandlingDeviceLock;
@property (TB,R,N) disallowsLockHardwareButtonDoublePress;
@property (TB,R,N) hasFullscreenActiveCallInSwitcher;
@property (TB,R,N,V_supportsHandlingUILockForWindowedAccessoryAttach) supportsHandlingUILockForWindowedAccessoryAttach;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInCallPresentationManager scenesForBacklightSession];
-[SBInCallPresentationManager _applicationDidExit:];
-[SBInCallPresentationManager acquireNonModalSuppressionAssertionForReason:];
-[SBInCallPresentationManager supportsBecomingVisibleWhenUnlockingFromSource:wakingDisplay:];
-[SBInCallPresentationManager sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBInCallPresentationManager _dismissClientWithIdentifier:animated:analyticsSource:reason:completion:];
-[SBInCallPresentationManager sessionForSceneIdentifier:];
-[SBInCallPresentationManager disablesSystemVolumeHUDForCategory:];
-[SBInCallPresentationManager supportsHandlingDeviceLock];
-[SBInCallPresentationManager handleDeviceLockFromSource:];
-[SBInCallPresentationManager inCallClientPresentationSessionInterfaceOrientationForBannerPresentation:];
-[SBInCallPresentationManager initWithWindowSceneManager:applicationController:bannerManager:];
-[SBInCallPresentationManager supportsHandlingUILockForWindowedAccessoryAttach];
-[SBInCallPresentationManager _sessionForSceneWithIdentifier:];
-[SBInCallPresentationManager _actionButtonPressed:];
-[SBInCallPresentationManager overrideAppSceneEntityForLaunchingApplication:];
-[SBInCallPresentationManager inCallPresentationRequestServer:clientWithIdentifier:requestsPresentationWithConfiguration:completion:];
-[SBInCallPresentationManager handlePresentationForActivityContinuationIdentifier:];
-[SBInCallPresentationManager _runZombieChecksForSceneHandle:];
-[SBInCallPresentationManager handleHeadsetButtonPress:];
-[SBInCallPresentationManager _hasPendingDismissalOfSceneHandleWithPersistenceIdentifier:];
-[SBInCallPresentationManager handlesRotationIndependentOfCoverSheet];
-[SBInCallPresentationManager hostedAppWillRotateToInterfaceOrientation:];
-[SBInCallPresentationManager canHandleOpenApplicationRequestForApplication:];
-[SBInCallPresentationManager inCallClientPresentationSessionInterfaceOrientationForTransientOverlayPresentation:];
-[SBInCallPresentationManager reactivateInCallForReason:];
-[SBInCallPresentationManager ensureSwitcherInclusionForRestoringFromPIPForSceneWithPersistenceIdentifier:completion:];
-[SBInCallPresentationManager _shouldSuppressNonModalCalls];
-[SBInCallPresentationManager conformsToSBApplicationHosting];
-[SBInCallPresentationManager windowSceneManager];
-[SBInCallPresentationManager inCallClientPresentationSession:handleDestroySceneActionWithReason:analyticsSource:completion:];
-[SBInCallPresentationManager setDelegate:];
-[SBInCallPresentationManager hostedAppSceneHandle];
-[SBInCallPresentationManager canHostAnApp];
-[SBInCallPresentationManager hasFullscreenActiveCallInSwitcher];
-[SBInCallPresentationManager disallowsLockHardwareButtonDoublePress];
-[SBInCallPresentationManager _evaluateNonModalSuppressionAssertions];
-[SBInCallPresentationManager _lastPresentationSession];
-[SBInCallPresentationManager hostedAppSceneHandles];
-[SBInCallPresentationManager delegate];
-[SBInCallPresentationManager handleAccessoryAttachWithCompletion:];
-[SBInCallPresentationManager hideSharePlayContentFromSharedScreenController];
-[SBInCallPresentationManager _newClientPresentationSessionWithSceneHandle:];
-[SBInCallPresentationManager inCallClientPresentationSessionResolvedPIPDodgingInsets:];
-[SBInCallPresentationManager inCallClientPresentationSessionAmbientPresentationActive:];
-[SBInCallPresentationManager inCallPresentationRequestServer:clientWithIdentifierDidInvalidate:];
-[SBInCallPresentationManager inCallClientPresentationSessionSceneWasDestroyed:];
-[SBInCallPresentationManager _runZombieChecksForScene:];
-[SBInCallPresentationManager _isManagingSceneOrSceneHandleWithPersistenceIdentifier:];
-[SBInCallPresentationManager inCallClientPresentationSession:canRestoreToPreviousEntity:];
-[SBInCallPresentationManager activeCallAppSceneEntity];
-[SBInCallPresentationManager _dismissAllPresentations];
-[SBInCallPresentationManager inCallClientPresentationSession:acquireHideSharePlayContentFromClonedDisplaysAssertionForReason:];
-[SBInCallPresentationManager _hostedPresentationSessions];
-[SBInCallPresentationManager inCallClientPresentationSession:callConnectedStatusChangedForPresentableViewController:];
-[SBInCallPresentationManager isSceneHandleCloseableInSwitcher:];
-[SBInCallPresentationManager hasOverrideAppSceneEntityForLaunchingApplication:];
-[SBInCallPresentationManager isHostingAnApp];
-[SBInCallPresentationManager handleOpenApplicationRequest:clientWorkspace:actions:origin:options:withResult:];
-[SBInCallPresentationManager inCallClientPresentationSessionInvalidateBacklightEnvironment:];
-[SBInCallPresentationManager sceneManager:didAddScene:];
-[SBInCallPresentationManager _dismissAllPresentationsForApplication:];
```
