# `SSRRemoteControlClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"OS_xpc_remote_connection" _connection;
@"CSDispatchGroup" _deviceWaitingGroup;
@"OS_remote_device" _device;
```

## Instance methods

```
-[SSRRemoteControlClient isConnected];
-[SSRRemoteControlClient dealloc];
-[SSRRemoteControlClient _handleServerError:];
-[SSRRemoteControlClient _handleServerEvent:];
-[SSRRemoteControlClient didDeviceConnect:];
-[SSRRemoteControlClient didDeviceDisconnect:];
-[SSRRemoteControlClient waitingForConnection:error:];
-[SSRRemoteControlClient _isImplicitTrainingRequiredForVoiceProfileId:locale:error:];
-[SSRRemoteControlClient addImplicitTrainingUtteranceToRemoteFilePath:forVoiceProfileId:withVoiceTriggerCtxt:locale:withOtherCtxt:completion:];
-[SSRRemoteControlClient initWithRemoteDeviceUUID:];
```
