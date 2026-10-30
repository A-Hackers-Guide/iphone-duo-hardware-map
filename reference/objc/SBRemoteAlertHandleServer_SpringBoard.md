# `SBRemoteAlertHandleServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSRemoteAlertHandleServiceServerInterface`, `SBRemoteTransientOverlaySessionObserver`
- 7 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _activeConnections;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"FBServiceClientAuthenticator" _legacyClientAuthenticator;
@"NSObject<OS_dispatch_queue>" _queue;
@"SBRemoteTransientOverlaySessionManager" _sessionManager;
@"NSMapTable" _sessionToConnections;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRemoteAlertHandleServer listener:didReceiveConnection:withContext:];
-[SBRemoteAlertHandleServer remoteTransientOverlaySession:didInvalidateWithReason:error:];
-[SBRemoteAlertHandleServer dealloc];
-[SBRemoteAlertHandleServer activate];
-[SBRemoteAlertHandleServer remoteTransientOverlaySessionDidDeactivate:];
-[SBRemoteAlertHandleServer activateRemoteAlertHandleWithID:activationContext:];
-[SBRemoteAlertHandleServer createRemoteAlertHandleContextWithDefinition:configurationContext:];
-[SBRemoteAlertHandleServer invalidateRemoteAlertHandleWithID:];
-[SBRemoteAlertHandleServer remoteAlertHandleContextsForDefinition:allowsCreationValue:configurationContext:];
-[SBRemoteAlertHandleServer initWithSessionManager:];
-[SBRemoteAlertHandleServer _addConnection:forSession:];
-[SBRemoteAlertHandleServer _handleDisconnectForServiceConnection:];
-[SBRemoteAlertHandleServer _removeConnection:forSession:];
-[SBRemoteAlertHandleServer _shouldAllowAuditToken:forDefinition:];
-[SBRemoteAlertHandleServer remoteTransientOverlaySessionDidActivate:];
```
