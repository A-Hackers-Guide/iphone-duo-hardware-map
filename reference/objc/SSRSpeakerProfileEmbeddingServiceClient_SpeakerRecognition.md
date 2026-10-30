# `SSRSpeakerProfileEmbeddingServiceClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerProfileEmbeddingService`
- 5 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _notifyToken;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
@ _remoteObjectProxy;
@"<SSRSpeakerProfileEmbeddingServiceDelegate>" _delegate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T@,&,N,V_remoteObjectProxy) remoteObjectProxy;
@property (T@"<SSRSpeakerProfileEmbeddingServiceDelegate>",W,N,V_delegate) delegate;
@property (Ti,N,V_notifyToken) notifyToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerProfileEmbeddingServiceClient initWithDelegate:];
-[SSRSpeakerProfileEmbeddingServiceClient setXpcConnection:];
-[SSRSpeakerProfileEmbeddingServiceClient dealloc];
-[SSRSpeakerProfileEmbeddingServiceClient queue];
-[SSRSpeakerProfileEmbeddingServiceClient setRemoteObjectProxy:];
-[SSRSpeakerProfileEmbeddingServiceClient xpcConnection];
-[SSRSpeakerProfileEmbeddingServiceClient invalidate];
-[SSRSpeakerProfileEmbeddingServiceClient setDelegate:];
-[SSRSpeakerProfileEmbeddingServiceClient delegate];
-[SSRSpeakerProfileEmbeddingServiceClient setNotifyToken:];
-[SSRSpeakerProfileEmbeddingServiceClient notifyToken];
-[SSRSpeakerProfileEmbeddingServiceClient remoteObjectProxy];
-[SSRSpeakerProfileEmbeddingServiceClient setQueue:];
-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection];
-[SSRSpeakerProfileEmbeddingServiceClient _remoteServiceProxyObjectWithErrorHandler:];
-[SSRSpeakerProfileEmbeddingServiceClient connectToServiceIfNeeded];
-[SSRSpeakerProfileEmbeddingServiceClient didFinishProcessingEmbeddingsForLanguageCode:withSuccess:];
-[SSRSpeakerProfileEmbeddingServiceClient refreshEmbeddingsforLanguageCode:withCompletion:];
-[SSRSpeakerProfileEmbeddingServiceClient speakerProfileEmbeddingsUpdated:];
```
