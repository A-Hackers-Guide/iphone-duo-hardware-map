# `SBSwitcherDemoCommandsServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSSwitcherDemoCommandsClientToServerInterface`
- 7 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBAppSwitcherSettings" _switcherSettings;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"SBSwitcherDemoFilteringController" _demoFilteringController;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _connections;
@"SBRecentAppLayouts" _recents;
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
-[SBSwitcherDemoCommandsServer listener:didReceiveConnection:withContext:];
-[SBSwitcherDemoCommandsServer loadStashedSwitcherModelFromPath:];
-[SBSwitcherDemoCommandsServer stashSwitcherModelToPath:];
-[SBSwitcherDemoCommandsServer setShouldDisableSwitcherModelUpdates:];
-[SBSwitcherDemoCommandsServer updateHiddenApplicationBundleIDs:];
-[SBSwitcherDemoCommandsServer _queue_addConnection:];
-[SBSwitcherDemoCommandsServer _queue_removeConnection:];
-[SBSwitcherDemoCommandsServer initWithRecentAppLayouts:demoFilteringController:];
```
