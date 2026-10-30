# `SBCaptureApplicationService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSCaptureApplicationServiceServerInterface`, `SBCaptureApplicationServiceMonitoring`
- 6 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnectionListener" _listener;
@"NSMutableSet" _connections;
@"NSMutableSet" _observingConnections;
@"<SBFCaptureApplicationProviding>" _applicationProvider;
@"NSHashTable" _observers;
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

## Class methods

```
+[SBCaptureApplicationService sharedInstance];
```

## Instance methods

```
-[SBCaptureApplicationService listener:didReceiveConnection:withContext:];
-[SBCaptureApplicationService removeObserver:];
-[SBCaptureApplicationService queue];
-[SBCaptureApplicationService addObserver:];
-[SBCaptureApplicationService applicationDidCompleteTransition];
-[SBCaptureApplicationService beginDelayingAppearance];
-[SBCaptureApplicationService endDelayingAppearance];
-[SBCaptureApplicationService _captureApplication];
-[SBCaptureApplicationService initWithCaptureApplicationProvider:];
```
