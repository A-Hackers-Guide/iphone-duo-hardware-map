# `TUCallHistoryControllerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallHistoryControllerXPCClient`, `TUCallHistoryControllerDataSource`
- 7 instance variables, 11 properties, 23 instance methods, 7 class methods

## Instance variables

```
B _hasRequestedInitialState;
B _hasInitialState;
B _shouldConnectToHost;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
i _shouldConnectToken;
@"NSXPCConnection" _xpcConnection;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_accessorLock) accessorLock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TB,N,V_hasRequestedInitialState) hasRequestedInitialState;
@property (TB,N,V_hasInitialState) hasInitialState;
@property (Ti,N,V_shouldConnectToken) shouldConnectToken;
@property (TB,N,V_shouldConnectToHost) shouldConnectToHost;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallHistoryControllerXPCClient setAsynchronousServer:];
+[TUCallHistoryControllerXPCClient asynchronousServer];
+[TUCallHistoryControllerXPCClient setSynchronousServer:];
+[TUCallHistoryControllerXPCClient synchronousServer];
+[TUCallHistoryControllerXPCClient callHistoryControllerAllowedClasses];
+[TUCallHistoryControllerXPCClient callHistoryControllerClientXPCInterface];
+[TUCallHistoryControllerXPCClient callHistoryControllerServerXPCInterface];
```

## Instance methods

```
-[TUCallHistoryControllerXPCClient accessorLock];
-[TUCallHistoryControllerXPCClient synchronousServerWithErrorHandler:];
-[TUCallHistoryControllerXPCClient hasInitialState];
-[TUCallHistoryControllerXPCClient init];
-[TUCallHistoryControllerXPCClient setXpcConnection:];
-[TUCallHistoryControllerXPCClient setHasInitialState:];
-[TUCallHistoryControllerXPCClient _requestInitialStateWithCompletionHandler:];
-[TUCallHistoryControllerXPCClient shouldConnectToken];
-[TUCallHistoryControllerXPCClient dealloc];
-[TUCallHistoryControllerXPCClient registerWithCompletionHandler:];
-[TUCallHistoryControllerXPCClient setShouldConnectToken:];
-[TUCallHistoryControllerXPCClient hasRequestedInitialState];
-[TUCallHistoryControllerXPCClient queue];
-[TUCallHistoryControllerXPCClient xpcConnection];
-[TUCallHistoryControllerXPCClient invalidate];
-[TUCallHistoryControllerXPCClient _invokeCompletionHandler:];
-[TUCallHistoryControllerXPCClient setShouldConnectToHost:];
-[TUCallHistoryControllerXPCClient shouldConnectToHost];
-[TUCallHistoryControllerXPCClient setHasRequestedInitialState:];
-[TUCallHistoryControllerXPCClient _requestInitialStateIfNecessary];
-[TUCallHistoryControllerXPCClient asynchronousServerWithErrorHandler:];
-[TUCallHistoryControllerXPCClient allCallHistoryDeleted];
-[TUCallHistoryControllerXPCClient recentCallsDeleted:];
```
