# `AAControllerSharedXPCManager`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _sharedXPCConnection;
B _connectionEstablished;
@"NSMutableArray" _pendingActivations;
B _invalidateCalled;
B _connectionActive;
@"NSMutableSet" _registeredControllers;
@"NSMutableArray" _pendingMessages;
@"NSObject<OS_dispatch_queue>" _managerQueue;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_registeredControllers) registeredControllers;
@property (T@"NSMutableArray",&,N,V_pendingMessages) pendingMessages;
@property (TB,N,V_invalidateCalled) invalidateCalled;
@property (TB,N,V_connectionActive) connectionActive;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_managerQueue) managerQueue;
```

## Class methods

```
+[AAControllerSharedXPCManager sharedManager];
```

## Instance methods

```
-[AAControllerSharedXPCManager _handleXPCEvent:];
-[AAControllerSharedXPCManager _handleConnectionInterruption];
-[AAControllerSharedXPCManager init];
-[AAControllerSharedXPCManager _invalidateConnection];
-[AAControllerSharedXPCManager dealloc];
-[AAControllerSharedXPCManager pendingMessages];
-[AAControllerSharedXPCManager connectionActive];
-[AAControllerSharedXPCManager invalidate];
-[AAControllerSharedXPCManager _handleConnectionInvalidation];
-[AAControllerSharedXPCManager setConnectionActive:];
-[AAControllerSharedXPCManager unregisterController:];
-[AAControllerSharedXPCManager managerQueue];
-[AAControllerSharedXPCManager setManagerQueue:];
-[AAControllerSharedXPCManager invalidateCalled];
-[AAControllerSharedXPCManager setInvalidateCalled:];
-[AAControllerSharedXPCManager setPendingMessages:];
-[AAControllerSharedXPCManager _activateSharedConnection];
-[AAControllerSharedXPCManager _distributeXPCMessage:];
-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:];
-[AAControllerSharedXPCManager _handleActivationReply:];
-[AAControllerSharedXPCManager _processPendingMessages];
-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:];
-[AAControllerSharedXPCManager registerController:completion:];
-[AAControllerSharedXPCManager registeredControllers];
-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:];
-[AAControllerSharedXPCManager setRegisteredControllers:];
```
