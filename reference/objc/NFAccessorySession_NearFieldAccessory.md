# `NFAccessorySession`

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFAccessorySession`
- 8 instance variables, 7 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _isFirstInQueue;
B _isCallbackQueueSuspended;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"NSObject<NFSessionAccessoryInterface><NSXPCProxyCreating>" _proxy;
@? _didStartCallback;
@? _didEndCallback;
@"NFTimer" _sessionTimeout;
Q _state;
```

## Properties

```
@property (TQ,R,V_state) state;
@property (TB,R) didEnd;
@property (TB,R) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NFAccessorySession proxy];
-[NFAccessorySession setProxy:];
-[NFAccessorySession init];
-[NFAccessorySession dealloc];
-[NFAccessorySession didEndUnexpectedly];
-[NFAccessorySession synchronousRemoteObjectProxyWithErrorHandler:];
-[NFAccessorySession remoteObjectProxyWithErrorHandler:];
-[NFAccessorySession callbackQueue];
-[NFAccessorySession isActive];
-[NFAccessorySession didTimeout];
-[NFAccessorySession resume];
-[NFAccessorySession state];
-[NFAccessorySession didEnd];
-[NFAccessorySession endSessionWithCompletion:];
-[NFAccessorySession isFirstInQueue];
-[NFAccessorySession didStartSession:];
-[NFAccessorySession _endProxySession];
-[NFAccessorySession didStartSessionWithoutQueue:];
-[NFAccessorySession setDidEndCallback:];
-[NFAccessorySession setDidStartCallback:];
-[NFAccessorySession setIsFirstInQueue:];
-[NFAccessorySession _didEndSession];
-[NFAccessorySession _didStartSession:];
-[NFAccessorySession _setSessionTimeLimit:];
```
