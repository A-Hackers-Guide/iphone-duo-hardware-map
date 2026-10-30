# `CSVTUIRemoteRecordClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"OS_xpc_remote_connection" _connection;
@"OS_remote_device_browser" _deviceBrowser;
@"CSDispatchGroup" _deviceWaitingGroup;
B _isRemoteRecording;
@"<CSVTUIRemoteRecordClientDelegate>" _delegate;
Q _audioStreamHandleId;
@"NSString" _deviceId;
@"OS_remote_device" _device;
```

## Properties

```
@property (T@"OS_remote_device",&,N,V_device) device;
@property (T@"<CSVTUIRemoteRecordClientDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_audioStreamHandleId) audioStreamHandleId;
@property (T@"NSString",R,N,V_deviceId) deviceId;
```

## Instance methods

```
-[CSVTUIRemoteRecordClient isConnected];
-[CSVTUIRemoteRecordClient isRecording];
-[CSVTUIRemoteRecordClient deviceId];
-[CSVTUIRemoteRecordClient setDevice:];
-[CSVTUIRemoteRecordClient device];
-[CSVTUIRemoteRecordClient init];
-[CSVTUIRemoteRecordClient dealloc];
-[CSVTUIRemoteRecordClient setDelegate:];
-[CSVTUIRemoteRecordClient delegate];
-[CSVTUIRemoteRecordClient voiceTriggerEventInfo];
-[CSVTUIRemoteRecordClient stopRecording:];
-[CSVTUIRemoteRecordClient _handleDidStartRecordingMessage:];
-[CSVTUIRemoteRecordClient _handleServerError:];
-[CSVTUIRemoteRecordClient _handleServerEvent:];
-[CSVTUIRemoteRecordClient _handleServerMessage:];
-[CSVTUIRemoteRecordClient _handleTwoShotDetectedMessage:];
-[CSVTUIRemoteRecordClient audioStreamHandleId];
-[CSVTUIRemoteRecordClient didDeviceConnect:];
-[CSVTUIRemoteRecordClient didDeviceDisconnect:];
-[CSVTUIRemoteRecordClient didPlayEndpointBeep];
-[CSVTUIRemoteRecordClient hasPendingTwoShotBeep];
-[CSVTUIRemoteRecordClient initWithDeviceId:audioStreamHandleId:];
-[CSVTUIRemoteRecordClient startRecordingWithOptions:error:];
-[CSVTUIRemoteRecordClient waitingForConnection:error:];
```
