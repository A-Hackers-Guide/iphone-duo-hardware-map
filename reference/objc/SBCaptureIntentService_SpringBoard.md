# `SBCaptureIntentService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSCaptureIntentServiceServerInterface`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _listener;
@"NSMutableSet" _connections;
@"NSMutableSet" _observingConnections;
@"<SBFCaptureApplicationProviding>" _applicationProvider;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureIntentService listener:didReceiveConnection:withContext:];
-[SBCaptureIntentService init];
-[SBCaptureIntentService captureIntentContext];
-[SBCaptureIntentService queue];
-[SBCaptureIntentService setCaptureIntentContext:];
-[SBCaptureIntentService _captureApplication];
```
