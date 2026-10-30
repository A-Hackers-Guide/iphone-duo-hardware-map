# `AVVoiceTriggerClient`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VoiceTriggerNotificationInterface`
- 13 instance variables, 14 properties, 64 instance methods, 4 class methods

## Instance variables

```
i _audioSeverUpNotificationToken;
@? _voiceTriggerBlock;
@? _speakerStateChangedBlock;
@? _speakerMuteStateChangedBlock;
@? _portStateChangedBlock;
@? _siriClientRecordStateChangedBlock;
@? _serverCrashedBlock;
@? _serverResetBlock;
@"NSXPCConnection" _voiceTriggerServerConnection;
@"NSObject<OS_dispatch_queue>" _workQueue;
@? _avvcServerCrashedBlock;
@? _avvcServerResetBlock;
q _clientType;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_voiceTriggerServerConnection) voiceTriggerServerConnection;
@property (Ti,N,V_audioSeverUpNotificationToken) audioSeverUpNotificationToken;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@?,C,N,V_avvcServerCrashedBlock) avvcServerCrashedBlock;
@property (T@?,C,N,V_avvcServerResetBlock) avvcServerResetBlock;
@property (Tq,N,V_clientType) clientType;
@property (T@?,C,N,V_voiceTriggerBlock) voiceTriggerBlock;
@property (T@?,C,N,V_speakerStateChangedBlock) speakerStateChangedBlock;
@property (T@?,C,N,V_speakerMuteStateChangedBlock) speakerMuteStateChangedBlock;
@property (T@?,C,N,V_portStateChangedBlock) portStateChangedBlock;
@property (T@?,C,N,V_siriClientRecordStateChangedBlock) siriClientRecordStateChangedBlock;
@property (T@?,C,N,V_serverCrashedBlock) serverCrashedBlock;
@property (T@?,C,N,V_serverResetBlock) serverResetBlock;
@property (TQ,R,N) voiceTriggerPastDataFramesAvailable;
```

## Class methods

```
+[AVVoiceTriggerClient sharedInstance];
+[AVVoiceTriggerClient isAPIAvailable];
+[AVVoiceTriggerClient sharedInstance:];
+[AVVoiceTriggerClient supportsDuckingOnSpeakerOutput];
```

## Instance methods

```
-[AVVoiceTriggerClient setWorkQueue:];
-[AVVoiceTriggerClient clientType];
-[AVVoiceTriggerClient init];
-[AVVoiceTriggerClient workQueue];
-[AVVoiceTriggerClient dealloc];
-[AVVoiceTriggerClient setClientType:];
-[AVVoiceTriggerClient init:];
-[AVVoiceTriggerClient closeServerConnection];
-[AVVoiceTriggerClient getInputChannelInfoCompletion:];
-[AVVoiceTriggerClient portStateChangedNotification:];
-[AVVoiceTriggerClient siriClientRecordStateChangedNotification:recordingCount:];
-[AVVoiceTriggerClient speakerMuteStateChangedNotification:];
-[AVVoiceTriggerClient speakerStateChangedNotification:];
-[AVVoiceTriggerClient voiceTriggerNotification:];
-[AVVoiceTriggerClient portStateActiveCompletionBlock:];
-[AVVoiceTriggerClient activateSecureSession:];
-[AVVoiceTriggerClient audioSeverUpNotificationToken];
-[AVVoiceTriggerClient avvcServerCrashedBlock];
-[AVVoiceTriggerClient avvcServerResetBlock];
-[AVVoiceTriggerClient callServerCrashedBlock];
-[AVVoiceTriggerClient callServerResetBlock];
-[AVVoiceTriggerClient enableBargeInMode:completionBlock:];
-[AVVoiceTriggerClient enableListeningOnPorts:completionBlock:];
-[AVVoiceTriggerClient enableSpeakerStateListening:];
-[AVVoiceTriggerClient enableSpeakerStateListening:completionBlock:];
-[AVVoiceTriggerClient enableVoiceTriggerListening:];
-[AVVoiceTriggerClient enableVoiceTriggerListening:completionBlock:];
-[AVVoiceTriggerClient isSiriClient];
-[AVVoiceTriggerClient listeningEnabledCompletionBlock:];
-[AVVoiceTriggerClient portStateChangedBlock];
-[AVVoiceTriggerClient recordingPIDList];
-[AVVoiceTriggerClient removeAudioServerUpNotificationHandler];
-[AVVoiceTriggerClient serverCrashedBlock];
-[AVVoiceTriggerClient serverResetBlock];
-[AVVoiceTriggerClient setAVVCServerCrashedBlock:];
-[AVVoiceTriggerClient setAVVCServerResetBlock:];
-[AVVoiceTriggerClient setAggressiveECMode:completionBlock:];
-[AVVoiceTriggerClient setAudioServerUpNotificationHandler];
-[AVVoiceTriggerClient setAudioSeverUpNotificationToken:];
-[AVVoiceTriggerClient setAvvcServerCrashedBlock:];
-[AVVoiceTriggerClient setAvvcServerResetBlock:];
-[AVVoiceTriggerClient setListeningProperty:completionBlock:];
-[AVVoiceTriggerClient setPortStateChangedBlock:];
-[AVVoiceTriggerClient setServerCrashedBlock:];
-[AVVoiceTriggerClient setServerResetBlock:];
-[AVVoiceTriggerClient setSiriClientRecordStateChangedBlock:];
-[AVVoiceTriggerClient setSpeakerMuteStateChangedBlock:];
-[AVVoiceTriggerClient setSpeakerStateChangedBlock:];
-[AVVoiceTriggerClient setVoiceTriggerBlock:];
-[AVVoiceTriggerClient setVoiceTriggerServerConnection:];
-[AVVoiceTriggerClient siriClientRecordStateChangedBlock];
-[AVVoiceTriggerClient siriClientsRecordingCompletionBlock:];
-[AVVoiceTriggerClient speakerMuteStateChangedBlock];
-[AVVoiceTriggerClient speakerStateActive];
-[AVVoiceTriggerClient speakerStateActiveCompletionBlock:];
-[AVVoiceTriggerClient speakerStateChangedBlock];
-[AVVoiceTriggerClient speakerStateMuted];
-[AVVoiceTriggerClient speakerStateMutedCompletionBlock:];
-[AVVoiceTriggerClient updateVoiceTriggerConfiguration:];
-[AVVoiceTriggerClient updateVoiceTriggerConfiguration:completionBlock:];
-[AVVoiceTriggerClient voiceTriggerBlock];
-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailable];
-[AVVoiceTriggerClient voiceTriggerPastDataFramesAvailableCompletion:];
-[AVVoiceTriggerClient voiceTriggerServerConnection];
```
