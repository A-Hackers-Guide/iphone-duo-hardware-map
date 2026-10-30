# `SBMultitaskingApplicationShortcutService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSMultitaskingApplicationShortcutServiceClientToServerInterface`, `BSServiceConnectionListenerDelegate`
- 6 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _connectionListener;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"FBServiceClientAuthenticator" _serviceClientAuthenticator;
@"BSServiceConnection<BSServiceConnectionHost>" _spotlightConnection;
@"NSMutableSet" _spotlightInterestedBundleIDs;
@"SBWindowSceneManager" _windowSceneManager;
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
-[SBMultitaskingApplicationShortcutService listener:didReceiveConnection:withContext:];
-[SBMultitaskingApplicationShortcutService fetchSupportedShortcutActionsForBundleIdentifier:withCompletionHandler:];
-[SBMultitaskingApplicationShortcutService performShortcutAction:forBundleIdentifier:];
-[SBMultitaskingApplicationShortcutService stopObservingUpdatesForBundleIdentifier:];
-[SBMultitaskingApplicationShortcutService _handleDisconnectForServiceConnection:];
-[SBMultitaskingApplicationShortcutService _switcherShortcutActionForRequestedAction:];
-[SBMultitaskingApplicationShortcutService initWithWindowSceneManager:];
-[SBMultitaskingApplicationShortcutService updateSupportedShortcutsForInterestedClients];
```
