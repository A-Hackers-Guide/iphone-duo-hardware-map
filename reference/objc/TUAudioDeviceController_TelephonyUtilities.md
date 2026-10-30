# `TUAudioDeviceController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUAudioDeviceControllerActions`
- 5 instance variables, 18 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"AVAudioClient" _audioClient;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSHashTable" _delegates;
@"<TUAudioDeviceControllerActions>" _actionsDelegate;
@? _registerForMutedTalkerNotificationCallback;
```

## Properties

```
@property (T@"AVAudioClient",&,N,V_audioClient) audioClient;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serialQueue) serialQueue;
@property (T@"NSHashTable",&,N,V_delegates) delegates;
@property (T@"<TUAudioDeviceControllerActions>",W,N,V_actionsDelegate) actionsDelegate;
@property (T@?,C,N,V_registerForMutedTalkerNotificationCallback) registerForMutedTalkerNotificationCallback;
@property (T@"<TUAudioDeviceControllerActions>",W,N) actionsDelegate;
@property (T@?,C,N) registerForMutedTalkerNotificationCallback;
@property (T@"AVAudioDevice",&,N) currentInputDevice;
@property (T@"AVAudioDevice",&,N) currentOutputDevice;
@property (T@"NSArray",R,N) devices;
@property (T@"NSArray",R,N) inputDevices;
@property (T@"NSArray",R,N) outputDevices;
@property (TB,R,N) isFollowingSystemInputSetting;
@property (TB,R,N) isFollowingSystemOutputSetting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUAudioDeviceController prewarm];
```

## Instance methods

```
-[TUAudioDeviceController removeDelegate:];
-[TUAudioDeviceController actionsDelegate];
-[TUAudioDeviceController setCurrentInputDevice:];
-[TUAudioDeviceController setDelegates:];
-[TUAudioDeviceController delegates];
-[TUAudioDeviceController serialQueue];
-[TUAudioDeviceController addDelegate:];
-[TUAudioDeviceController debugDescription];
-[TUAudioDeviceController init];
-[TUAudioDeviceController setMixesVoiceWithMedia:];
-[TUAudioDeviceController dealloc];
-[TUAudioDeviceController setMediaPlaybackOnExternalDevice:];
-[TUAudioDeviceController setSerialQueue:];
-[TUAudioDeviceController outputDevices];
-[TUAudioDeviceController devices];
-[TUAudioDeviceController setCurrentAudioInputDeviceToDeviceWithUID:];
-[TUAudioDeviceController currentInputDevice];
-[TUAudioDeviceController setActionsDelegate:];
-[TUAudioDeviceController currentOutputDevice];
-[TUAudioDeviceController setCurrentOutputDevice:];
-[TUAudioDeviceController setCurrentAudioOutputDeviceToDeviceWithUID:];
-[TUAudioDeviceController inputDevices];
-[TUAudioDeviceController setAudioClient:];
-[TUAudioDeviceController _handleCallStatusChangedNotification:];
-[TUAudioDeviceController audioClient];
-[TUAudioDeviceController initWithActionsDelegate:serialQueue:];
-[TUAudioDeviceController isFollowingSystemInputSetting];
-[TUAudioDeviceController isFollowingSystemOutputSetting];
-[TUAudioDeviceController notifyDelegatesOfDeviceListChange];
-[TUAudioDeviceController registerForMutedTalkerNotificationCallback];
-[TUAudioDeviceController setFollowsSystemInputSetting:];
-[TUAudioDeviceController setFollowsSystemOutputSetting:];
-[TUAudioDeviceController setRegisterForMutedTalkerNotificationCallback:];
```
