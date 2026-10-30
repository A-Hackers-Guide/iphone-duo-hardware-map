# `SBWebClipService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSWebClipServiceClientToServerInterface`
- 14 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"SBMainWorkspace" _workspace;
@"SBApplicationPlaceholderController" _placeholderController;
@"SBApplicationController" _applicationController;
@"SBContinuitySessionManager" _continuitySessionManager;
@"FBServiceClientAuthenticator" _legacyClientAuthenticator;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"NSMutableArray" _connections;
Q _pendingLaunchGenerationCount;
@"NSString" _pendingBundleIdentifier;
@"NSString" _pendingWebClipIdentifier;
@"NSNumber" _pendingLaunchOrigin;
d _pendingLaunchTimeout;
```

## Properties

```
@property (Td,N,V_pendingLaunchTimeout) pendingLaunchTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWebClipService bestWebClipForTargetContentIdentifier:fromWebClips:];
```

## Instance methods

```
-[SBWebClipService listener:didReceiveConnection:withContext:];
-[SBWebClipService _applicationsDidChange:];
-[SBWebClipService launchWebClipWithIdentifier:origin:];
-[SBWebClipService updateWebClipPropertiesWithIdentifier:];
-[SBWebClipService _queue_addConnection:];
-[SBWebClipService _queue_removeConnection:];
-[SBWebClipService _addActivationActionToSceneEntity:forWebClip:];
-[SBWebClipService _beginWaitingForBundleIdentifier:webClipIdentifier:launchOrigin:];
-[SBWebClipService _clearPendingLaunch];
-[SBWebClipService _generateUserActivityDataFromUserActivity:completion:];
-[SBWebClipService _performActionIfContinuitySessionActive:];
-[SBWebClipService _placeholdersDidChange:];
-[SBWebClipService buildLaunchActionsForAppClipWithWebClipIdentifier:completion:];
-[SBWebClipService initForTestingWithPlaceholderController:applicationController:];
-[SBWebClipService initWithWorkspace:placeholderController:applicationController:continuitySessionManager:];
-[SBWebClipService pendingLaunchTimeout];
-[SBWebClipService prepareToLaunchWebClipWithIdentifier:handler:];
-[SBWebClipService setPendingLaunchTimeout:];
-[SBWebClipService targetApplicationBundleIdentifierForWebClip:];
```
