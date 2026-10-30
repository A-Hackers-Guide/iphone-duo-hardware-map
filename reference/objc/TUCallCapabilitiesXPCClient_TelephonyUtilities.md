# `TUCallCapabilitiesXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallCapabilitiesXPCClient`, `TUCallCapabilitiesXPCServerActions`
- 5 instance variables, 10 properties, 35 instance methods, 6 class methods

## Instance variables

```
i _token;
@"TUCallCapabilitiesState" _state;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
@"NSMapTable" _delegateToQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T^v,R,N) queueContext;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (Ti,R,N,V_token) token;
@property (T@"NSMapTable",R,N,V_delegateToQueue) delegateToQueue;
@property (T@"TUCallCapabilitiesState",&,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallCapabilitiesXPCClient setAsynchronousServer:];
+[TUCallCapabilitiesXPCClient callCapabilitiesClientXPCInterface];
+[TUCallCapabilitiesXPCClient asynchronousServer];
+[TUCallCapabilitiesXPCClient setSynchronousServer:];
+[TUCallCapabilitiesXPCClient synchronousServer];
+[TUCallCapabilitiesXPCClient callCapabilitiesServerXPCInterface];
```

## Instance methods

```
-[TUCallCapabilitiesXPCClient performBlockOnQueue:];
-[TUCallCapabilitiesXPCClient setThumperCallingAllowed:onSecondaryDeviceWithID:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient queueContext];
-[TUCallCapabilitiesXPCClient handleServerDisconnect];
-[TUCallCapabilitiesXPCClient removeDelegate:];
-[TUCallCapabilitiesXPCClient cancelPinRequestFromPrimaryDevice];
-[TUCallCapabilitiesXPCClient endEmergencyCallbackMode];
-[TUCallCapabilitiesXPCClient requestPinFromPrimaryDevice];
-[TUCallCapabilitiesXPCClient setRelayCallingEnabled:forDeviceWithID:];
-[TUCallCapabilitiesXPCClient synchronousServerWithErrorHandler:];
-[TUCallCapabilitiesXPCClient setRelayCallingEnabled:];
-[TUCallCapabilitiesXPCClient addDelegate:queue:];
-[TUCallCapabilitiesXPCClient setState:];
-[TUCallCapabilitiesXPCClient invalidateAndRefreshThumperCallingProvisioningURLForSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient delegateToQueue];
-[TUCallCapabilitiesXPCClient setVoLTECallingEnabled:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient init];
-[TUCallCapabilitiesXPCClient _retrieveState];
-[TUCallCapabilitiesXPCClient setXpcConnection:];
-[TUCallCapabilitiesXPCClient dealloc];
-[TUCallCapabilitiesXPCClient queue];
-[TUCallCapabilitiesXPCClient xpcConnection];
-[TUCallCapabilitiesXPCClient setWiFiCallingRoamingEnabled:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient invalidate];
-[TUCallCapabilitiesXPCClient setThumperCallingAllowedOnDefaultPairedDevice:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient capabilityStateUpdated:];
-[TUCallCapabilitiesXPCClient invalidateAndRefreshWiFiCallingProvisioningURLForSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient asynchronousServer];
-[TUCallCapabilitiesXPCClient token];
-[TUCallCapabilitiesXPCClient performDelegateCallbackBlock:];
-[TUCallCapabilitiesXPCClient setThumperCallingEnabled:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient setWiFiCallingEnabled:forSenderIdentityWithUUID:];
-[TUCallCapabilitiesXPCClient asynchronousServerWithErrorHandler:];
-[TUCallCapabilitiesXPCClient state];
-[TUCallCapabilitiesXPCClient _updateState:];
```
