# `FudInternalConnection`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FudConnection`
- 5 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" clientIdentifier;
@"NSObject<OS_dispatch_queue>" handlerQueue;
@? messageHandler;
@"NSMutableDictionary" pendingRequests;
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
-[FudInternalConnection stop];
-[FudInternalConnection dealloc];
-[FudInternalConnection getNextMessageID];
-[FudInternalConnection handleInternalMessage:];
-[FudInternalConnection initWithClientIdentifier:handlerQueue:messageHandler:];
-[FudInternalConnection sendMessageToFud:];
-[FudInternalConnection sendMessageToFud:reply:];
```
