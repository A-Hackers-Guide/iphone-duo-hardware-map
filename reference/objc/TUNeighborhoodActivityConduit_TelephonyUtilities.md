# `TUNeighborhoodActivityConduit`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUNeighborhoodActivityConduitXPCClientDelegate`, `TUConduitLifecycleControllerDelegate`
- 10 instance variables, 16 properties, 52 instance methods, 1 class methods

## Instance variables

```
B _isRingingFaceTimeCallsOnConnectedTVDevice;
@"<TUNeighborhoodActivityConduitApprovalDelegate>" _approvalDelegate;
@"TUNearbyDeviceHandle" _activeSplitSessionTV;
@"TUNearbySuggestion" _suggestion;
@"NSMapTable" _delegates;
@"NSMutableSet" _nearbyTVs;
@"TUNeighborhoodActivityConduitXPCClient" _xpcClient;
@"TUConversationManager" _conversationManager;
Q _stateHandle;
@"<TUConduitLifecycleController>" _conduitLifecycleController;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_delegates) delegates;
@property (T@"NSMutableSet",R,N,V_nearbyTVs) nearbyTVs;
@property (T@"TUNearbyDeviceHandle",&,N,V_activeSplitSessionTV) activeSplitSessionTV;
@property (TB,N,V_isRingingFaceTimeCallsOnConnectedTVDevice) isRingingFaceTimeCallsOnConnectedTVDevice;
@property (T@"TUNeighborhoodActivityConduitXPCClient",R,N,V_xpcClient) xpcClient;
@property (T@"TUConversationManager",R,N,V_conversationManager) conversationManager;
@property (TQ,N,V_stateHandle) stateHandle;
@property (T@"<TUConduitLifecycleController>",&,N,V_conduitLifecycleController) conduitLifecycleController;
@property (T@"<TUNeighborhoodActivityConduitApprovalDelegate>",W,N,V_approvalDelegate) approvalDelegate;
@property (T@"NSDictionary",R,N) nearbyTVDevices;
@property (T@"NSSet",R,N) nearbyTVDeviceHandles;
@property (T@"TUNearbySuggestion",R,N,V_suggestion) suggestion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUNeighborhoodActivityConduit isConduitAvailable];
```

## Instance methods

```
-[TUNeighborhoodActivityConduit xpcClient];
-[TUNeighborhoodActivityConduit stateHandle];
-[TUNeighborhoodActivityConduit callStatusChanged:];
-[TUNeighborhoodActivityConduit removeDelegate:];
-[TUNeighborhoodActivityConduit handoffConversation:toTVDevice:completion:];
-[TUNeighborhoodActivityConduit setConduitLifecycleController:];
-[TUNeighborhoodActivityConduit setDelegates:];
-[TUNeighborhoodActivityConduit addDelegate:queue:];
-[TUNeighborhoodActivityConduit pullConversation:fromTVDevice:completion:];
-[TUNeighborhoodActivityConduit delegates];
-[TUNeighborhoodActivityConduit nearbyTVs];
-[TUNeighborhoodActivityConduit suggestion];
-[TUNeighborhoodActivityConduit connectionLostForClient:];
-[TUNeighborhoodActivityConduit addDelegate:];
-[TUNeighborhoodActivityConduit tvDeviceDisappeared:];
-[TUNeighborhoodActivityConduit setActiveSplitSessionTV:];
-[TUNeighborhoodActivityConduit continuityCameraDidConnect];
-[TUNeighborhoodActivityConduit _findConversationForUUID:];
-[TUNeighborhoodActivityConduit dealloc];
-[TUNeighborhoodActivityConduit splitSessionUpdated:];
-[TUNeighborhoodActivityConduit nearbyTVDeviceHandles];
-[TUNeighborhoodActivityConduit setSuggestion:];
-[TUNeighborhoodActivityConduit ensureConduitInitialized:];
-[TUNeighborhoodActivityConduit activeSplitSessionTV];
-[TUNeighborhoodActivityConduit inviteTVDevice:toConversation:completion:];
-[TUNeighborhoodActivityConduit approvalDelegate];
-[TUNeighborhoodActivityConduit initWithConversationManager:xpcClient:];
-[TUNeighborhoodActivityConduit setStateHandle:];
-[TUNeighborhoodActivityConduit _osStateDictionary];
-[TUNeighborhoodActivityConduit initWithConversationManager:];
-[TUNeighborhoodActivityConduit validateGuestSessionInvitationFromIDSIdentifier:requireActiveConnection:completion:];
-[TUNeighborhoodActivityConduit conduitLifecycleController];
-[TUNeighborhoodActivityConduit disconnectTVDevice:completion:];
-[TUNeighborhoodActivityConduit conversationManager];
-[TUNeighborhoodActivityConduit tvDeviceAppeared:];
-[TUNeighborhoodActivityConduit approveSplitSessionForConversation:device:pullContext:completion:];
-[TUNeighborhoodActivityConduit cancelSplitSessionApproval];
-[TUNeighborhoodActivityConduit _forEachDelegate:];
-[TUNeighborhoodActivityConduit _shouldReconnect];
-[TUNeighborhoodActivityConduit isRingingFaceTimeCallsOnConnectedTVDevice];
-[TUNeighborhoodActivityConduit startConversationWith:on:completion:];
-[TUNeighborhoodActivityConduit setApprovalDelegate:];
-[TUNeighborhoodActivityConduit _requestInitialState];
-[TUNeighborhoodActivityConduit isRingingFaceTimeCallsOnConnectedTVDeviceChanged:];
-[TUNeighborhoodActivityConduit respondToSuggestionWithResult:completion:];
-[TUNeighborhoodActivityConduit canPullBackConversation:];
-[TUNeighborhoodActivityConduit setSuggestedTVDeviceName:completion:];
-[TUNeighborhoodActivityConduit splitSessionUpdated];
-[TUNeighborhoodActivityConduit suggestionUpdated:];
-[TUNeighborhoodActivityConduit nearbyTVDevices];
-[TUNeighborhoodActivityConduit setIsRingingFaceTimeCallsOnConnectedTVDevice:];
-[TUNeighborhoodActivityConduit connectionEstablishedForClient:];
```
