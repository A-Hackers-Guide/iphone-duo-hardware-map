# `TUMomentsController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUMomentsControllerDataSourceDelegate`
- 6 instance variables, 10 properties, 39 instance methods, 9 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUMomentsControllerDataSource>" _dataSource;
@"NSMutableDictionary" _capabilitiesByVideoStreamToken;
@"NSMutableDictionary" _providerByVideoStreamToken;
@"NSHashTable" _delegates;
@? _lockdownModeEnabled;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<TUMomentsControllerDataSource>",R,N,V_dataSource) dataSource;
@property (T@"NSMutableDictionary",R,N,V_capabilitiesByVideoStreamToken) capabilitiesByVideoStreamToken;
@property (T@"NSMutableDictionary",R,N,V_providerByVideoStreamToken) providerByVideoStreamToken;
@property (T@"NSHashTable",&,N,V_delegates) delegates;
@property (T@?,C,N,V_lockdownModeEnabled) lockdownModeEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUMomentsController sharedInstance];
+[TUMomentsController isInternalInstall];
+[TUMomentsController faceTimePhotosEnabledDeterminer];
+[TUMomentsController isFaceTimePhotosEnabled];
+[TUMomentsController isFaceTimePhotosEnabledByDefault];
+[TUMomentsController isFaceTimePhotosRestricted];
+[TUMomentsController isFaceTimePhotosXPCServiceEnabled];
+[TUMomentsController setFaceTimePhotosEnabled:];
+[TUMomentsController setFaceTimePhotosEnabledDeterminer:];
```

## Instance methods

```
-[TUMomentsController initWithDataSource:];
-[TUMomentsController removeDelegate:];
-[TUMomentsController setDelegates:];
-[TUMomentsController initWithQueue:];
-[TUMomentsController delegates];
-[TUMomentsController addDelegate:];
-[TUMomentsController init];
-[TUMomentsController dealloc];
-[TUMomentsController queue];
-[TUMomentsController lockdownModeEnabled];
-[TUMomentsController dataSource];
-[TUMomentsController setLockdownModeEnabled:];
-[TUMomentsController prewarmMediaRequest:completion:];
-[TUMomentsController capabilitiesByVideoStreamToken];
-[TUMomentsController capabilitiesForProvider:];
-[TUMomentsController dataSource:didFinishProcessingRawVideoMessage:];
-[TUMomentsController dataSource:didFinishRecordingMedia:];
-[TUMomentsController dataSource:didReceiveLocallyRequestedMomentDescriptor:];
-[TUMomentsController dataSource:didReceiveMediaRecordingError:];
-[TUMomentsController dataSource:didReceiveMessageRecordingError:];
-[TUMomentsController dataSource:didUpdateCapabilities:forVideoStreamToken:];
-[TUMomentsController dataSource:requestSandboxExtensionForURL:reply:];
-[TUMomentsController dataSource:willCaptureRemoteRequestFromRequesterID:];
-[TUMomentsController discardVideoMessageWithUUID:completion:];
-[TUMomentsController endMediaRequestWithUUID:completion:];
-[TUMomentsController endRecordingMessageWithUUID:completion:];
-[TUMomentsController endRequestWithTransactionID:completion:];
-[TUMomentsController initWithDataSource:queue:];
-[TUMomentsController prewarmAudioClientWithCompletion:];
-[TUMomentsController providerByVideoStreamToken];
-[TUMomentsController registerProvider:completion:];
-[TUMomentsController resetVideoMessagingWithSessionUUID:completion:];
-[TUMomentsController saveVideoMessageWithUUID:completion:];
-[TUMomentsController sendVideoMessageWithRequest:completion:];
-[TUMomentsController serverDiedForDataSource:];
-[TUMomentsController startMediaRequest:completion:];
-[TUMomentsController startRecordingMessageWithMediaType:completion:];
-[TUMomentsController startRequestWithMediaType:forProvider:requesteeID:completion:];
-[TUMomentsController unregisterProvider:completion:];
```
