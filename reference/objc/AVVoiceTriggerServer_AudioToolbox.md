# `AVVoiceTriggerServer`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `VoiceTriggerInterface`
- 9 instance variables, 12 properties, 42 instance methods, 0 class methods

## Instance variables

```
^{AVVoiceTriggerServerImpl=^^?I^{HALListener}^{HALListener}^{HALListener}i**BBBBB@@i^{unfair_recursive_lock}@BI@} serverImpl;
@"NSXPCListener" _serverListener;
@"NSMutableArray" _clientConnections;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
^v _mobileAssistantDylib;
^? _afSiriActivationBuiltInMicVoiceFuncPtr;
^v _voiceTriggerDylib;
# _clsVTStateManager;
@"VTStateManager" _vtStateManager;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_serverListener) serverListener;
@property (T@"NSMutableArray",&,N,V_clientConnections) clientConnections;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_notificationQueue) notificationQueue;
@property (T^v,N,V_mobileAssistantDylib) mobileAssistantDylib;
@property (T^?,N,V_afSiriActivationBuiltInMicVoiceFuncPtr) afSiriActivationBuiltInMicVoiceFuncPtr;
@property (T^v,N,V_voiceTriggerDylib) voiceTriggerDylib;
@property (T#,&,N,V_clsVTStateManager) clsVTStateManager;
@property (T@"VTStateManager",&,N,V_vtStateManager) vtStateManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVVoiceTriggerServer setNotificationQueue:];
-[AVVoiceTriggerServer notificationQueue];
-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:];
-[AVVoiceTriggerServer init];
-[AVVoiceTriggerServer dealloc];
-[AVVoiceTriggerServer initializeWithReply:];
-[AVVoiceTriggerServer clientConnections];
-[AVVoiceTriggerServer activateSecureSession:reply:];
-[AVVoiceTriggerServer afSiriActivationBuiltInMicVoiceFuncPtr];
-[AVVoiceTriggerServer clsVTStateManager];
-[AVVoiceTriggerServer enableBargeInMode:reply:];
-[AVVoiceTriggerServer enableListeningOnPorts:reply:];
-[AVVoiceTriggerServer enableSpeakerStateListening:reply:];
-[AVVoiceTriggerServer enableVoiceTriggerListening:reply:];
-[AVVoiceTriggerServer getInputChannelInfoCompletion:];
-[AVVoiceTriggerServer hardwareSupportsVoiceTrigger];
-[AVVoiceTriggerServer isAssistantVoiceTriggerEnabled];
-[AVVoiceTriggerServer listeningEnabledReply:];
-[AVVoiceTriggerServer mobileAssistantDylib];
-[AVVoiceTriggerServer portsActiveReply:];
-[AVVoiceTriggerServer sendActiveStateChangedNotificationForPort:isActive:];
-[AVVoiceTriggerServer sendSpeakerMuteStateChangedNotification:];
-[AVVoiceTriggerServer sendVoiceTriggerOccuredNotification:triggerTime:];
-[AVVoiceTriggerServer serverListener];
-[AVVoiceTriggerServer setAfSiriActivationBuiltInMicVoiceFuncPtr:];
-[AVVoiceTriggerServer setAggressiveECMode:reply:];
-[AVVoiceTriggerServer setClientConnections:];
-[AVVoiceTriggerServer setClsVTStateManager:];
-[AVVoiceTriggerServer setListeningProperty:reply:];
-[AVVoiceTriggerServer setMobileAssistantDylib:];
-[AVVoiceTriggerServer setServerListener:];
-[AVVoiceTriggerServer setVoiceTriggerDylib:];
-[AVVoiceTriggerServer setVtStateManager:];
-[AVVoiceTriggerServer siriClientRecordStateChanged:];
-[AVVoiceTriggerServer siriClientsRecordingReply:];
-[AVVoiceTriggerServer speakerStateActiveReply:];
-[AVVoiceTriggerServer speakerStateMutedReply:];
-[AVVoiceTriggerServer speechDetectionVADCreated];
-[AVVoiceTriggerServer updateVoiceTriggerConfiguration:reply:];
-[AVVoiceTriggerServer voiceTriggerDylib];
-[AVVoiceTriggerServer voiceTriggerPastDataFramesAvailable:];
-[AVVoiceTriggerServer vtStateManager];
```
