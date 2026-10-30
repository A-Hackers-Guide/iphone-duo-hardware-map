# `FBInterfaceOrientationServiceServer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSOrientationServiceServerInterface`, `BSInvalidatable`
- 8 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceDispatchQueue" _queue;
@"BSServiceConnectionListener" _listener;
@"NSMutableSet" _lock_pendingConnections;
@"NSMutableSet" _lock_interestedConnections;
@"NSMutableSet" _lock_connections;
B _lock_serviceSuspended;
@"FBSActiveInterfaceOrientationStateUpdate" _lock_latestUpdate;
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
-[FBInterfaceOrientationServiceServer _currentConnection];
-[FBInterfaceOrientationServiceServer initialize];
-[FBInterfaceOrientationServiceServer unregisterInterest];
-[FBInterfaceOrientationServiceServer init];
-[FBInterfaceOrientationServiceServer _connectionInvalidated:];
-[FBInterfaceOrientationServiceServer invalidate];
-[FBInterfaceOrientationServiceServer _connections];
-[FBInterfaceOrientationServiceServer activeInterfaceOrientationStateUpdateWithCompletion:];
-[FBInterfaceOrientationServiceServer _endpoint];
-[FBInterfaceOrientationServiceServer startService];
-[FBInterfaceOrientationServiceServer registerInterestWithCompletion:];
-[FBInterfaceOrientationServiceServer activeInterfaceOrientationStateUpdate];
-[FBInterfaceOrientationServiceServer _didReceiveConnection:];
-[FBInterfaceOrientationServiceServer _initWithDomain:service:];
-[FBInterfaceOrientationServiceServer _interestedConnections];
-[FBInterfaceOrientationServiceServer _latestUpdate];
-[FBInterfaceOrientationServiceServer _lock_noteActiveInterfaceOrientationStateDidChange:animationSettings:rotationDirection:];
-[FBInterfaceOrientationServiceServer _lock_registerInterestForConnection:];
-[FBInterfaceOrientationServiceServer _lock_sendMessageToInterestedClients:];
-[FBInterfaceOrientationServiceServer _lock_unregisterInterestForConnection:];
-[FBInterfaceOrientationServiceServer _pendingConnections];
-[FBInterfaceOrientationServiceServer noteActiveInterfaceOrientationStateDidChange:animationSettings:rotationDirection:];
```
