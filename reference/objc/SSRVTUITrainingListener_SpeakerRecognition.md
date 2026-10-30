# `SSRVTUITrainingListener`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 4 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSXPCListener" _listener;
@"NSXPCConnection" _activeConnection;
@"NSObject<OS_dispatch_queue>" _queue;
@"SSRVTUITrainingMessageHandler" _messageHandler;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (T@"NSXPCConnection",&,N,V_activeConnection) activeConnection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"SSRVTUITrainingMessageHandler",&,N,V_messageHandler) messageHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVTUITrainingListener messageHandler];
-[SSRVTUITrainingListener setMessageHandler:];
-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:];
-[SSRVTUITrainingListener setListener:];
-[SSRVTUITrainingListener queue];
-[SSRVTUITrainingListener listener];
-[SSRVTUITrainingListener activeConnection];
-[SSRVTUITrainingListener setQueue:];
-[SSRVTUITrainingListener setActiveConnection:];
-[SSRVTUITrainingListener listen];
-[SSRVTUITrainingListener initWithMessageHandler:];
```
