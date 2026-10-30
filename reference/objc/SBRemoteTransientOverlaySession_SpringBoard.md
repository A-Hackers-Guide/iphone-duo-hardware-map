# `SBRemoteTransientOverlaySession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRemoteTransientOverlayViewControllerDelegate`
- 21 instance variables, 16 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"BSTransaction" _activeTransaction;
@"SBRemoteTransientOverlayViewController" _containerViewController;
@"SBRemoteTransientOverlayViewController" _secondaryViewController;
B _prefersEmbeddedDisplayPresentation;
B _hasInitiatedPresentation;
B _hasPresented;
B _hasPresentedSecondaryVC;
@"NSMutableDictionary" _identifierToHandlingButtonEvents;
@"NSHashTable" _observers;
@"NSMutableArray" _pendingTransactions;
@"SBFSceneWorkspaceController" _sceneWorkspaceController;
B _activated;
B _prepared;
B _valid;
B _pendingInvalidation;
B _shouldEmbedOverShieldedApps;
@"SBSRemoteAlertDefinition" _definition;
@"NSError" _error;
@"NSString" _sessionID;
@"SBWindowScene" _primaryPresentationWindowScene;
@"<SBRemoteTransientOverlaySessionHostDelegate>" _hostDelegate;
```

## Properties

```
@property (TB,N,V_shouldEmbedOverShieldedApps) shouldEmbedOverShieldedApps;
@property (T@"SBWindowScene",W,N,V_primaryPresentationWindowScene) primaryPresentationWindowScene;
@property (T@"<SBRemoteTransientOverlaySessionHostDelegate>",W,N,V_hostDelegate) hostDelegate;
@property (T@"SBSRemoteAlertDefinition",R,C,N,V_definition) definition;
@property (T@"NSError",R,C,N,V_error) error;
@property (T@"NSString",R,C,N,V_sessionID) sessionID;
@property (T@"NSString",R,C,N) serviceBundleIdentifier;
@property (TB,R,N,GisActivated,V_activated) activated;
@property (TB,R,N,GisPrepared,V_prepared) prepared;
@property (TB,R,N,GisSwitcherEligible) switcherEligible;
@property (TB,R,N,GisValid,V_valid) valid;
@property (TB,R,N,GisPendingInvalidation,V_pendingInvalidation) pendingInvalidation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRemoteTransientOverlaySession isPrepared];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewControllerDidInvalidate:];
-[SBRemoteTransientOverlaySession isActivated];
-[SBRemoteTransientOverlaySession definition];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewControllerRequestsDeactivation:];
-[SBRemoteTransientOverlaySession sessionID];
-[SBRemoteTransientOverlaySession deactivate];
-[SBRemoteTransientOverlaySession removeSessionObserver:];
-[SBRemoteTransientOverlaySession serviceBundleIdentifier];
-[SBRemoteTransientOverlaySession _actionForHandlingButtonEvents:];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:didDisappearAnimated:];
-[SBRemoteTransientOverlaySession _didDeactivate];
-[SBRemoteTransientOverlaySession hostDelegate];
-[SBRemoteTransientOverlaySession setHostDelegate:];
-[SBRemoteTransientOverlaySession isSwitcherEligible];
-[SBRemoteTransientOverlaySession hasServiceProcessIdentifier:];
-[SBRemoteTransientOverlaySession dealloc];
-[SBRemoteTransientOverlaySession getActionForHandlingButtonEvents:completion:];
-[SBRemoteTransientOverlaySession isPendingInvalidation];
-[SBRemoteTransientOverlaySession _registerObserversForTransaction:];
-[SBRemoteTransientOverlaySession isPresentedOnWindowScene:];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:requestsActionForHandlingButtonEvents:];
-[SBRemoteTransientOverlaySession shouldEmbedOverShieldedApps];
-[SBRemoteTransientOverlaySession error];
-[SBRemoteTransientOverlaySession activateWithContext:];
-[SBRemoteTransientOverlaySession hasPendingButtonEvents:];
-[SBRemoteTransientOverlaySession primaryPresentationWindowScene];
-[SBRemoteTransientOverlaySession _initWithSessionID:definition:sceneWorkspaceController:];
-[SBRemoteTransientOverlaySession isPresentedFromSceneWithIdentityTokenString:];
-[SBRemoteTransientOverlaySession setPrimaryPresentationWindowScene:];
-[SBRemoteTransientOverlaySession invalidate];
-[SBRemoteTransientOverlaySession _processPendingTransactions];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewControllerRequestsInvalidation:];
-[SBRemoteTransientOverlaySession setShouldEmbedOverShieldedApps:];
-[SBRemoteTransientOverlaySession isValid];
-[SBRemoteTransientOverlaySession prepareWithConfigurationContext:];
-[SBRemoteTransientOverlaySession addSessionObserver:];
-[SBRemoteTransientOverlaySession _invalidateWithReason:error:];
-[SBRemoteTransientOverlaySession _requestInvalidationWithReason:error:];
-[SBRemoteTransientOverlaySession _didActivate];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:willAppearAnimated:];
-[SBRemoteTransientOverlaySession _addTransaction:];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:prefersStatusBarActivityItemVisibleForServiceBundleIdentifier:];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:didTerminateWithError:];
-[SBRemoteTransientOverlaySession remoteTransientOverlayViewController:didAppearAnimated:];
```
