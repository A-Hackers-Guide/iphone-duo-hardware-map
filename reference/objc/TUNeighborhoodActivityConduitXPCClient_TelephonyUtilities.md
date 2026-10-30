# `TUNeighborhoodActivityConduitXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUNeighborhoodActivityConduitXPCClient`
- 4 instance variables, 8 properties, 34 instance methods, 3 class methods

## Instance variables

```
i _token;
@"<TUNeighborhoodActivityConduitXPCClientDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (Ti,N,V_token) token;
@property (T@"<TUNeighborhoodActivityConduitXPCClientDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUNeighborhoodActivityConduitXPCClient allowedXPCClasses];
+[TUNeighborhoodActivityConduitXPCClient neighborhoodActivityClientXPCInterface];
+[TUNeighborhoodActivityConduitXPCClient neighborhoodActivityServerXPCInterface];
```

## Instance methods

```
-[TUNeighborhoodActivityConduitXPCClient handoffConversation:toTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCClient pullConversation:fromTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCClient suggestionWithCompletion:];
-[TUNeighborhoodActivityConduitXPCClient server];
-[TUNeighborhoodActivityConduitXPCClient inviteTVDevice:toConversationWithUUID:completion:];
-[TUNeighborhoodActivityConduitXPCClient registerApprovalClientEnabled:];
-[TUNeighborhoodActivityConduitXPCClient tvDeviceDisappeared:];
-[TUNeighborhoodActivityConduitXPCClient init];
-[TUNeighborhoodActivityConduitXPCClient setXpcConnection:];
-[TUNeighborhoodActivityConduitXPCClient dealloc];
-[TUNeighborhoodActivityConduitXPCClient nearbyTVDevicesWithCompletion:];
-[TUNeighborhoodActivityConduitXPCClient ensureConnection];
-[TUNeighborhoodActivityConduitXPCClient activeSplitSessionTVDeviceWithCompletion:];
-[TUNeighborhoodActivityConduitXPCClient queue];
-[TUNeighborhoodActivityConduitXPCClient ensureConduitInitialized:];
-[TUNeighborhoodActivityConduitXPCClient xpcConnection];
-[TUNeighborhoodActivityConduitXPCClient setDelegate:];
-[TUNeighborhoodActivityConduitXPCClient _tearDownXPCConnection];
-[TUNeighborhoodActivityConduitXPCClient delegate];
-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:];
-[TUNeighborhoodActivityConduitXPCClient validateGuestSessionInvitationFromIDSIdentifier:requireActiveConnection:completion:];
-[TUNeighborhoodActivityConduitXPCClient disconnectTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCClient tvDeviceAppeared:];
-[TUNeighborhoodActivityConduitXPCClient approveSplitSessionForConversation:requestedFromDevice:pullContext:completion:];
-[TUNeighborhoodActivityConduitXPCClient cancelSplitSessionApproval];
-[TUNeighborhoodActivityConduitXPCClient token];
-[TUNeighborhoodActivityConduitXPCClient setToken:];
-[TUNeighborhoodActivityConduitXPCClient serverWithErrorHandler:];
-[TUNeighborhoodActivityConduitXPCClient startConversationWith:on:completion:];
-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceChanged:];
-[TUNeighborhoodActivityConduitXPCClient respondToSuggestionWithResult:completion:];
-[TUNeighborhoodActivityConduitXPCClient setSuggestedTVDeviceName:completion:];
-[TUNeighborhoodActivityConduitXPCClient splitSessionUpdated];
-[TUNeighborhoodActivityConduitXPCClient suggestionUpdated:];
```
