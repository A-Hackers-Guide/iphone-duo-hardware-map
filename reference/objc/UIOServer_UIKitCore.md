# `UIOServer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`
- 6 instance variables, 4 properties, 11 instance methods, 3 class methods

## Instance variables

```
B _activated;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"BSServiceConnectionListener" _connectionListener;
@"NSMutableSet" _connections;
@"NSMapTable" _displayDelegateTable;
@"NSMutableDictionary" _awaitingDisplayDelegateRequests;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIOServer sharedInstance];
+[UIOServer _identifierForSceneType:spaceIdentifier:];
+[UIOServer displayDelegateIdentifierForScene:];
```

## Instance methods

```
-[UIOServer listener:didReceiveConnection:withContext:];
-[UIOServer init];
-[UIOServer invalidate];
-[UIOServer activate];
-[UIOServer _fulfillAwaitingDisplayDelegate:forIdentifier:];
-[UIOServer awaitDisplayDelegateForAction:sceneType:timeout:completion:];
-[UIOServer displayDelegateForAction:];
-[UIOServer displayDelegateForAction:sceneType:];
-[UIOServer displayDelegateForIdentifier:];
-[UIOServer registerDisplayDelegate:forIdentifier:];
-[UIOServer unregisterDisplayDelegateForIdentifier:];
```
