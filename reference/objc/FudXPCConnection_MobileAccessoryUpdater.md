# `FudXPCConnection`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FudConnection`
- 8 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" clientIdentifier;
@"NSObject<OS_xpc_object>" connection;
@"NSObject<OS_dispatch_queue>" connectionQueue;
@"NSObject<OS_dispatch_queue>" sessionQueue;
@"NSObject<OS_dispatch_queue>" replyQueue;
@? messageHandler;
i notifyToken;
B didStop;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FudXPCConnection createConnection];
-[FudXPCConnection stop];
-[FudXPCConnection dealloc];
-[FudXPCConnection createSession];
-[FudXPCConnection initWithClientName:replyHandlerQueue:messageHandler:];
-[FudXPCConnection registerForBSDNotifications];
-[FudXPCConnection sendMessageToFud:];
-[FudXPCConnection sendMessageToFud:reply:];
```
