# `TUSimulatedConversationControllerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSimulatedConversationControllerXPCClient`, `TUSimulatedConversationControllerDataSource`
- 2 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSXPCConnection" _xpcConnection;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUSimulatedConversationControllerXPCClient simulatedConversationControllerAllowedClasses];
+[TUSimulatedConversationControllerXPCClient simulatedConversationControllerClientXPCInterface];
+[TUSimulatedConversationControllerXPCClient simulatedConversationControllerServerXPCInterface];
```

## Instance methods

```
-[TUSimulatedConversationControllerXPCClient synchronousServerWithErrorHandler:];
-[TUSimulatedConversationControllerXPCClient init];
-[TUSimulatedConversationControllerXPCClient setXpcConnection:];
-[TUSimulatedConversationControllerXPCClient dealloc];
-[TUSimulatedConversationControllerXPCClient queue];
-[TUSimulatedConversationControllerXPCClient xpcConnection];
-[TUSimulatedConversationControllerXPCClient invalidate];
-[TUSimulatedConversationControllerXPCClient asynchronousServerWithErrorHandler:];
-[TUSimulatedConversationControllerXPCClient addRemoteParticipantWithHandle:update:toConversation:];
-[TUSimulatedConversationControllerXPCClient createIncomingConversationWithHandles:];
-[TUSimulatedConversationControllerXPCClient removeRemoteParticipant:fromConversation:];
-[TUSimulatedConversationControllerXPCClient updateParticipant:withUpdate:onConversation:];
```
