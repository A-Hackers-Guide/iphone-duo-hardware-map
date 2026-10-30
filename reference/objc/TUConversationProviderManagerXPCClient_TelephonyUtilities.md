# `TUConversationProviderManagerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationProviderManagerXPCClient`, `TUConversationProviderManagerDataSource`
- 6 instance variables, 10 properties, 28 instance methods, 7 class methods

## Instance variables

```
B _hasRequestedInitialState;
B _hasInitialState;
B _shouldConnectToHost;
i _shouldConnectToken;
@"NSXPCConnection" _xpcConnection;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
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
+[TUConversationProviderManagerXPCClient setAsynchronousServer:];
+[TUConversationProviderManagerXPCClient asynchronousServer];
+[TUConversationProviderManagerXPCClient setSynchronousServer:];
+[TUConversationProviderManagerXPCClient synchronousServer];
+[TUConversationProviderManagerXPCClient conversationProviderManagerAllowedClasses];
+[TUConversationProviderManagerXPCClient conversationProviderManagerClientXPCInterface];
+[TUConversationProviderManagerXPCClient conversationProviderManagerServerXPCInterface];
```

## Instance methods

```
-[TUConversationProviderManagerXPCClient synchronousServerWithErrorHandler:];
-[TUConversationProviderManagerXPCClient hasInitialState];
-[TUConversationProviderManagerXPCClient init];
-[TUConversationProviderManagerXPCClient setXpcConnection:];
-[TUConversationProviderManagerXPCClient setHasInitialState:];
-[TUConversationProviderManagerXPCClient _requestInitialStateWithCompletionHandler:];
-[TUConversationProviderManagerXPCClient shouldConnectToken];
-[TUConversationProviderManagerXPCClient dealloc];
-[TUConversationProviderManagerXPCClient registerWithCompletionHandler:];
-[TUConversationProviderManagerXPCClient setShouldConnectToken:];
-[TUConversationProviderManagerXPCClient hasRequestedInitialState];
-[TUConversationProviderManagerXPCClient queue];
-[TUConversationProviderManagerXPCClient xpcConnection];
-[TUConversationProviderManagerXPCClient invalidate];
-[TUConversationProviderManagerXPCClient _invokeCompletionHandler:];
-[TUConversationProviderManagerXPCClient setShouldConnectToHost:];
-[TUConversationProviderManagerXPCClient shouldConnectToHost];
-[TUConversationProviderManagerXPCClient setHasRequestedInitialState:];
-[TUConversationProviderManagerXPCClient _requestInitialStateIfNecessary];
-[TUConversationProviderManagerXPCClient asynchronousServerWithErrorHandler:];
-[TUConversationProviderManagerXPCClient conversationProviderForIdentifier:completionHandler:];
-[TUConversationProviderManagerXPCClient doesHandle:correspondToConversationProvider:completionHandler:];
-[TUConversationProviderManagerXPCClient generatePseudonymHandleForConversationProvider:expiryDuration:URI:completionHandler:];
-[TUConversationProviderManagerXPCClient registerConversationProvider:completionHandler:];
-[TUConversationProviderManagerXPCClient registerForCallbacksForProvider:completionHandler:];
-[TUConversationProviderManagerXPCClient renewPseudonymHandle:forConversationProvider:expirationDate:completionHandler:];
-[TUConversationProviderManagerXPCClient revokePseudonymHandle:forConversationProvider:completionHandler:];
-[TUConversationProviderManagerXPCClient updateConversationProviders:];
```
