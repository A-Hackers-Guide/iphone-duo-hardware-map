# `BKSAlternateSystemApp`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSAlternateSystemAppClientProtocol`
- 7 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _stateChangeWaiter;
@"<BKSAlternateSystemAppDelegate>" _delegate;
@"NSString" _bundleId;
@"NSXPCConnection" _connection;
@"NSObject<OS_dispatch_queue>" _queue;
q _state;
@"NSObject<OS_dispatch_semaphore>" _stateChangeSemaphore;
```

## Properties

```
@property (T@"NSString",C,N,V_bundleId) bundleId;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (Tq,N,V_state) state;
@property (TB,N,V_stateChangeWaiter) stateChangeWaiter;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_stateChangeSemaphore) stateChangeSemaphore;
@property (T@"<BKSAlternateSystemAppDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSAlternateSystemApp terminate];
-[BKSAlternateSystemApp setState:];
-[BKSAlternateSystemApp dealloc];
-[BKSAlternateSystemApp setBundleId:];
-[BKSAlternateSystemApp queue];
-[BKSAlternateSystemApp _queue_ensureConnection];
-[BKSAlternateSystemApp setDelegate:];
-[BKSAlternateSystemApp bundleId];
-[BKSAlternateSystemApp initWithBundleId:];
-[BKSAlternateSystemApp activate];
-[BKSAlternateSystemApp connection];
-[BKSAlternateSystemApp delegate];
-[BKSAlternateSystemApp setConnection:];
-[BKSAlternateSystemApp _queue_invalidate];
-[BKSAlternateSystemApp state];
-[BKSAlternateSystemApp setQueue:];
-[BKSAlternateSystemApp _handleInterruptedConnection];
-[BKSAlternateSystemApp _handleInvalidatedConnection];
-[BKSAlternateSystemApp _queue_changeState:];
-[BKSAlternateSystemApp _waitForState:];
-[BKSAlternateSystemApp alternateSystemAppWithBundleID:didExitWithContext:];
-[BKSAlternateSystemApp alternateSystemAppWithBundleID:failedToOpenWithResult:];
-[BKSAlternateSystemApp alternateSystemAppWithBundleIDDidOpen:];
-[BKSAlternateSystemApp alternateSystemAppWithBundleIDDidTerminate:];
-[BKSAlternateSystemApp didBlockSystemAppForAlternateSystemApp];
-[BKSAlternateSystemApp didUnblockSystemAppForAlternateSystemApp];
-[BKSAlternateSystemApp setStateChangeSemaphore:];
-[BKSAlternateSystemApp setStateChangeWaiter:];
-[BKSAlternateSystemApp stateChangeSemaphore];
-[BKSAlternateSystemApp stateChangeWaiter];
```
