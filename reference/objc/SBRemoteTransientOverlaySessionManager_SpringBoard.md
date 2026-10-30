# `SBRemoteTransientOverlaySessionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRemoteTransientOverlaySessionHostDelegate`, `SBFSceneWorkspaceControllerDelegate`
- 5 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _accessSerialQueue;
@"NSMutableDictionary" _sessionIDToSession;
@"SBFSceneWorkspaceController" _sceneWorkspaceController;
@"NSHashTable" _observers;
@"<SBRemoteTransientOverlaySessionManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBRemoteTransientOverlaySessionManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:didInvalidateWithReason:error:];
-[SBRemoteTransientOverlaySessionManager removeObserver:];
-[SBRemoteTransientOverlaySessionManager init];
-[SBRemoteTransientOverlaySessionManager addObserver:];
-[SBRemoteTransientOverlaySessionManager setDelegate:];
-[SBRemoteTransientOverlaySessionManager setScene:shouldActivateUponClientConnection:withContextGenerator:];
-[SBRemoteTransientOverlaySessionManager setScene:shouldAlwaysBeKeptActive:withContextGenerator:];
-[SBRemoteTransientOverlaySessionManager delegate];
-[SBRemoteTransientOverlaySessionManager setScene:shouldBeKeptActiveWhileForeground:withContextGenerator:];
-[SBRemoteTransientOverlaySessionManager createSessionWithDefinition:];
-[SBRemoteTransientOverlaySessionManager hasActiveSessionMatchingPredicate:options:];
-[SBRemoteTransientOverlaySessionManager sessionsWithDefinition:options:];
-[SBRemoteTransientOverlaySessionManager _createSessionWithDefinition:];
-[SBRemoteTransientOverlaySessionManager _existingSessionsWithDefinition:options:];
-[SBRemoteTransientOverlaySessionManager activeWallpaperVariantForRemoteTransientOverlaySession:];
-[SBRemoteTransientOverlaySessionManager embeddedDisplayWindowSceneForRemoteTransientOverlaySession:];
-[SBRemoteTransientOverlaySessionManager existingSessionWithSessionID:options:];
-[SBRemoteTransientOverlaySessionManager existingSessionsWithDefinition:options:];
-[SBRemoteTransientOverlaySessionManager hasActiveSessionWithSceneIdentityTokenString:options:];
-[SBRemoteTransientOverlaySessionManager hasSessionWithPendingButtonEvents:options:];
-[SBRemoteTransientOverlaySessionManager hasSessionWithServiceProcessIdentifier:options:];
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:performDismissalRequest:];
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:performPresentationRequest:];
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:prefersStatusBarActivityItemVisibleForServiceBundleIdentifier:];
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:requestsHandlingForButtonEvents:viewController:];
-[SBRemoteTransientOverlaySessionManager remoteTransientOverlaySession:shouldActivateWithContext:];
-[SBRemoteTransientOverlaySessionManager sessionWithDefinition:options:];
```
