# `SSRSpeakerProfileEmbeddingMessageHandler`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVoiceProfileManagerDelegate`, `SSRSpeakerProfileEmbeddingService`
- 5 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _connection;
@? _errorHandler;
@"<SSRSpeakerProfileEmbeddingServiceDelegate>" _listenerDelegate;
@"SSRVoiceProfileManager" _voiceProfileManager;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@"<SSRSpeakerProfileEmbeddingServiceDelegate>",&,N,V_listenerDelegate) listenerDelegate;
@property (T@"SSRVoiceProfileManager",&,N,V_voiceProfileManager) voiceProfileManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerProfileEmbeddingMessageHandler setVoiceProfileManager:];
-[SSRSpeakerProfileEmbeddingMessageHandler voiceProfileManager];
-[SSRSpeakerProfileEmbeddingMessageHandler reset];
-[SSRSpeakerProfileEmbeddingMessageHandler queue];
-[SSRSpeakerProfileEmbeddingMessageHandler initWithConnection:];
-[SSRSpeakerProfileEmbeddingMessageHandler connection];
-[SSRSpeakerProfileEmbeddingMessageHandler setConnection:];
-[SSRSpeakerProfileEmbeddingMessageHandler setErrorHandler:];
-[SSRSpeakerProfileEmbeddingMessageHandler errorHandler];
-[SSRSpeakerProfileEmbeddingMessageHandler setQueue:];
-[SSRSpeakerProfileEmbeddingMessageHandler listenerDelegate];
-[SSRSpeakerProfileEmbeddingMessageHandler didFinishProcessingEmbeddingsForLanguageCode:withSuccess:];
-[SSRSpeakerProfileEmbeddingMessageHandler refreshEmbeddingsforLanguageCode:withCompletion:];
-[SSRSpeakerProfileEmbeddingMessageHandler setListenerDelegate:];
-[SSRSpeakerProfileEmbeddingMessageHandler setupListenerDelegate:];
-[SSRSpeakerProfileEmbeddingMessageHandler speakerProfileUpdated:];
```
