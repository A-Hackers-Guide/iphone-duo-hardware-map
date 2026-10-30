# `TUMomentsControllerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUMomentsControllerXPCClient`, `TUMomentsControllerDataSource`
- 4 instance variables, 10 properties, 37 instance methods, 6 class methods

## Instance variables

```
i _token;
@"<TUMomentsControllerDataSourceDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (Ti,R,N,V_token) token;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TUMomentsControllerDataSourceDelegate>",W,N,V_delegate) delegate;
@property (Ti,R,N) processIdentifier;
@property (T@"NSString",R,C,N) processName;
```

## Class methods

```
+[TUMomentsControllerXPCClient setAsynchronousServer:];
+[TUMomentsControllerXPCClient asynchronousServer];
+[TUMomentsControllerXPCClient setSynchronousServer:];
+[TUMomentsControllerXPCClient synchronousServer];
+[TUMomentsControllerXPCClient momentsControllerClientXPCInterface];
+[TUMomentsControllerXPCClient momentsControllerServerXPCInterface];
```

## Instance methods

```
-[TUMomentsControllerXPCClient synchronousServerWithErrorHandler:];
-[TUMomentsControllerXPCClient init];
-[TUMomentsControllerXPCClient setXpcConnection:];
-[TUMomentsControllerXPCClient dealloc];
-[TUMomentsControllerXPCClient queue];
-[TUMomentsControllerXPCClient xpcConnection];
-[TUMomentsControllerXPCClient invalidate];
-[TUMomentsControllerXPCClient setDelegate:];
-[TUMomentsControllerXPCClient processName];
-[TUMomentsControllerXPCClient delegate];
-[TUMomentsControllerXPCClient token];
-[TUMomentsControllerXPCClient processIdentifier];
-[TUMomentsControllerXPCClient serverWithErrorHandler:];
-[TUMomentsControllerXPCClient prewarmMediaRequest:completion:];
-[TUMomentsControllerXPCClient _registerConnection];
-[TUMomentsControllerXPCClient didFinishProcessingRawVideoMessage:];
-[TUMomentsControllerXPCClient didFinishRecordingMedia:];
-[TUMomentsControllerXPCClient didReceiveLocallyRequestedMomentDescriptor:];
-[TUMomentsControllerXPCClient didReceiveMediaRecordingError:];
-[TUMomentsControllerXPCClient didReceiveMessageRecordingError:];
-[TUMomentsControllerXPCClient didUpdateCapabilities:forVideoStreamToken:];
-[TUMomentsControllerXPCClient discardVideoMessageWithUUID:completion:];
-[TUMomentsControllerXPCClient endMediaRequestWithUUID:completion:];
-[TUMomentsControllerXPCClient endRecordingMessageWithUUID:completion:];
-[TUMomentsControllerXPCClient endRequestWithTransactionID:completion:];
-[TUMomentsControllerXPCClient prewarmAudioClientWithCompletion:];
-[TUMomentsControllerXPCClient processBundleIdentifier];
-[TUMomentsControllerXPCClient registerStreamToken:requesterID:remoteIDSDestinations:remoteMomentsAvailable:completion:];
-[TUMomentsControllerXPCClient requestSandboxExtensionForURL:reply:];
-[TUMomentsControllerXPCClient resetVideoMessagingWithSessionUUID:completion:];
-[TUMomentsControllerXPCClient saveVideoMessageWithUUID:completion:];
-[TUMomentsControllerXPCClient sendVideoMessageWithRequest:completion:];
-[TUMomentsControllerXPCClient startMediaRequest:completion:];
-[TUMomentsControllerXPCClient startRecordingMessageWithMediaType:completion:];
-[TUMomentsControllerXPCClient startRequestWithMediaType:forStreamToken:requesteeID:destinationID:completion:];
-[TUMomentsControllerXPCClient unregisterStreamToken:completion:];
-[TUMomentsControllerXPCClient willCaptureRemoteRequestFromRequesterID:];
```
