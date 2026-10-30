# `SBRemoteAlertHandleLocalClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRemoteTransientOverlaySessionObserver`, `SBSRemoteAlertHandleClient`
- 3 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _accessSerialQueue;
@"SBRemoteTransientOverlaySessionManager" _sessionManager;
@"NSMutableDictionary" _sessionIDToRemoteAlertHandle;
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
-[SBRemoteAlertHandleLocalClient remoteTransientOverlaySession:didInvalidateWithReason:error:];
-[SBRemoteAlertHandleLocalClient remoteTransientOverlaySessionDidDeactivate:];
-[SBRemoteAlertHandleLocalClient activateRemoteAlertHandle:withContext:];
-[SBRemoteAlertHandleLocalClient createRemoteAlertHandleWithDefinition:configurationContext:];
-[SBRemoteAlertHandleLocalClient invalidateRemoteAlertHandle:];
-[SBRemoteAlertHandleLocalClient remoteAlertHandlesForDefinition:allowsCreation:configurationContext:];
-[SBRemoteAlertHandleLocalClient initWithSessionManager:];
-[SBRemoteAlertHandleLocalClient _registerHandle:forSession:];
-[SBRemoteAlertHandleLocalClient _unregisterHandle:];
-[SBRemoteAlertHandleLocalClient remoteTransientOverlaySessionDidActivate:];
```
