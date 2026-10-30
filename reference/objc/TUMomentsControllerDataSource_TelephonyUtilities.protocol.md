# `TUMomentsControllerDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 19 instance methods, 0 class methods

## Properties

```
@property (T@"<TUMomentsControllerDataSourceDelegate>",W,N) delegate;
@property (Ti,R,N) processIdentifier;
@property (T@"NSString",R,C,N) processName;
```

## Instance methods

```
-[TUMomentsControllerDataSource invalidate];
-[TUMomentsControllerDataSource setDelegate:];
-[TUMomentsControllerDataSource processName];
-[TUMomentsControllerDataSource delegate];
-[TUMomentsControllerDataSource processIdentifier];
-[TUMomentsControllerDataSource prewarmMediaRequest:completion:];
-[TUMomentsControllerDataSource discardVideoMessageWithUUID:completion:];
-[TUMomentsControllerDataSource endMediaRequestWithUUID:completion:];
-[TUMomentsControllerDataSource endRecordingMessageWithUUID:completion:];
-[TUMomentsControllerDataSource endRequestWithTransactionID:completion:];
-[TUMomentsControllerDataSource prewarmAudioClientWithCompletion:];
-[TUMomentsControllerDataSource registerStreamToken:requesterID:remoteIDSDestinations:remoteMomentsAvailable:completion:];
-[TUMomentsControllerDataSource resetVideoMessagingWithSessionUUID:completion:];
-[TUMomentsControllerDataSource saveVideoMessageWithUUID:completion:];
-[TUMomentsControllerDataSource sendVideoMessageWithRequest:completion:];
-[TUMomentsControllerDataSource startMediaRequest:completion:];
-[TUMomentsControllerDataSource startRecordingMessageWithMediaType:completion:];
-[TUMomentsControllerDataSource startRequestWithMediaType:forStreamToken:requesteeID:destinationID:completion:];
-[TUMomentsControllerDataSource unregisterStreamToken:completion:];
```
