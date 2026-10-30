# `TUMomentsControllerXPCServer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance methods

```
-[TUMomentsControllerXPCServer unregisterClient:];
-[TUMomentsControllerXPCServer prewarmMediaRequest:completion:];
-[TUMomentsControllerXPCServer registerClient:];
-[TUMomentsControllerXPCServer discardVideoMessageWithUUID:completion:];
-[TUMomentsControllerXPCServer endMediaRequestWithUUID:completion:];
-[TUMomentsControllerXPCServer endRecordingMessageWithUUID:completion:];
-[TUMomentsControllerXPCServer endRequestWithTransactionID:reply:];
-[TUMomentsControllerXPCServer prewarmAudioClientWithCompletion:];
-[TUMomentsControllerXPCServer registerStreamToken:requesterID:remoteIDSDestinations:remoteMomentsAvailable:reply:];
-[TUMomentsControllerXPCServer registerXPCClientWithReply:];
-[TUMomentsControllerXPCServer resetVideoMessagingWithSessionUUID:completionHandler:];
-[TUMomentsControllerXPCServer saveVideoMessageWithUUID:completion:];
-[TUMomentsControllerXPCServer sendVideoMessageWithRequest:completion:];
-[TUMomentsControllerXPCServer startMediaRequest:completion:];
-[TUMomentsControllerXPCServer startRecordingMessageWithMediaType:completion:];
-[TUMomentsControllerXPCServer startRequestWithMediaType:forStreamToken:requesteeID:destinationID:reply:];
-[TUMomentsControllerXPCServer unregisterStreamToken:reply:];
```
