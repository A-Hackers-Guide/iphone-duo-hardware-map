# `TUCallHistoryManagerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallHistoryManagerXPCClient`, `TUCallHistoryManagerDataSource`
- 2 instance variables, 6 properties, 12 instance methods, 7 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallHistoryManagerXPCClient setAsynchronousServer:];
+[TUCallHistoryManagerXPCClient asynchronousServer];
+[TUCallHistoryManagerXPCClient setSynchronousServer:];
+[TUCallHistoryManagerXPCClient synchronousServer];
+[TUCallHistoryManagerXPCClient callHistoryManagerAllowedClasses];
+[TUCallHistoryManagerXPCClient callHistoryManagerClientXPCInterface];
+[TUCallHistoryManagerXPCClient callHistoryManagerServerXPCInterface];
```

## Instance methods

```
-[TUCallHistoryManagerXPCClient handleServerDisconnect];
-[TUCallHistoryManagerXPCClient synchronousServerWithErrorHandler:];
-[TUCallHistoryManagerXPCClient init];
-[TUCallHistoryManagerXPCClient setXpcConnection:];
-[TUCallHistoryManagerXPCClient dealloc];
-[TUCallHistoryManagerXPCClient queue];
-[TUCallHistoryManagerXPCClient xpcConnection];
-[TUCallHistoryManagerXPCClient invalidate];
-[TUCallHistoryManagerXPCClient serverWithErrorHandler:];
-[TUCallHistoryManagerXPCClient setQueue:];
-[TUCallHistoryManagerXPCClient updateOutgoingLocalParticipantUUID:forCallsWithOutgoingLocalParticipantUUID:];
-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:avMode:];
```
