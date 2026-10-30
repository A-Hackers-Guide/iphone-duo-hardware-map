# `SSRSpeakerProfileEmbeddingServiceListener`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 3 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSXPCListener" _listener;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _messageHandlers;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableArray",&,N,V_messageHandlers) messageHandlers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerProfileEmbeddingServiceListener listener:shouldAcceptNewConnection:];
-[SSRSpeakerProfileEmbeddingServiceListener init];
-[SSRSpeakerProfileEmbeddingServiceListener setListener:];
-[SSRSpeakerProfileEmbeddingServiceListener queue];
-[SSRSpeakerProfileEmbeddingServiceListener listener];
-[SSRSpeakerProfileEmbeddingServiceListener resumeConnection];
-[SSRSpeakerProfileEmbeddingServiceListener setQueue:];
-[SSRSpeakerProfileEmbeddingServiceListener messageHandlers];
-[SSRSpeakerProfileEmbeddingServiceListener setMessageHandlers:];
```
