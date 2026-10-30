# `FBSOrientationObserverClient`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSOrientationServiceClientInterface`, `BSInvalidatable`
- 8 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
@"BSServiceQueue" _calloutQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<FBSOrientationObserverClientDelegate>" _lock_delegate;
@"BSServiceInitiatingConnection" _lock_connection;
B _lock_isActive;
B _lock_isInterested;
B _lock_invalidated;
```

## Properties

```
@property (TB,R,N) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSOrientationObserverClient _setDelegate:];
-[FBSOrientationObserverClient _connection];
-[FBSOrientationObserverClient initWithDelegate:];
-[FBSOrientationObserverClient _isInterested];
-[FBSOrientationObserverClient _connectionInterrupted:];
-[FBSOrientationObserverClient unregisterInterest];
-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:];
-[FBSOrientationObserverClient _connectionInvalidated:];
-[FBSOrientationObserverClient registerInterest];
-[FBSOrientationObserverClient _server:registerInterest:];
-[FBSOrientationObserverClient dealloc];
-[FBSOrientationObserverClient activeInterfaceOrientationState];
-[FBSOrientationObserverClient invalidate];
-[FBSOrientationObserverClient activate];
-[FBSOrientationObserverClient _lock_activate];
-[FBSOrientationObserverClient _lock_remoteTarget];
-[FBSOrientationObserverClient activeInterfaceOrientationStateDidChange:];
-[FBSOrientationObserverClient isActive];
-[FBSOrientationObserverClient _connectionActivated:];
-[FBSOrientationObserverClient activeInterfaceOrientationStateUpdateWithCompletion:];
-[FBSOrientationObserverClient _lock_invalidate];
```
