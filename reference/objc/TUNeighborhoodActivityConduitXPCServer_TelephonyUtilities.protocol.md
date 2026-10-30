# `TUNeighborhoodActivityConduitXPCServer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[TUNeighborhoodActivityConduitXPCServer handoffConversation:toTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCServer pullConversation:fromTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCServer suggestionWithCompletion:];
-[TUNeighborhoodActivityConduitXPCServer nearbyTVDevicesWithCompletion:];
-[TUNeighborhoodActivityConduitXPCServer activeSplitSessionTVDeviceWithCompletion:];
-[TUNeighborhoodActivityConduitXPCServer ensureConduitInitialized:];
-[TUNeighborhoodActivityConduitXPCServer inviteTVDevice:toConversation:completion:];
-[TUNeighborhoodActivityConduitXPCServer unregisterClient:];
-[TUNeighborhoodActivityConduitXPCServer isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:];
-[TUNeighborhoodActivityConduitXPCServer validateGuestSessionInvitationFromIDSIdentifier:requireActiveConnection:completion:];
-[TUNeighborhoodActivityConduitXPCServer disconnectTVDevice:completion:];
-[TUNeighborhoodActivityConduitXPCServer startConversationWith:on:completion:];
-[TUNeighborhoodActivityConduitXPCServer respondToSuggestionWithResult:completion:];
-[TUNeighborhoodActivityConduitXPCServer setSuggestedTVDeviceName:completion:];
-[TUNeighborhoodActivityConduitXPCServer registerClient:];
-[TUNeighborhoodActivityConduitXPCServer registerSplitSessionApprovalEnabled:];
```
