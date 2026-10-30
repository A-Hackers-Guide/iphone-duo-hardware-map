# `_CLLocationSmootherProxy`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationSmootherClientInterface`
- 7 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@? _pendingCompletion;
@? _connectionInterruptionHandler;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
@"NSXPCConnection" _connection;
@"<CLLocationSmootherDelegate>" _delegate;
@"CLLocationSmoother" _locationManagerSmoother;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"<CLLocationSmootherDelegate>",W,N,V_delegate) delegate;
@property (T@"CLLocationSmoother",W,N,V_locationManagerSmoother) locationManagerSmoother;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_CLLocationSmootherProxy createConnection];
-[_CLLocationSmootherProxy invalidateConnection];
-[_CLLocationSmootherProxy dealloc];
-[_CLLocationSmootherProxy setDelegate:];
-[_CLLocationSmootherProxy connection];
-[_CLLocationSmootherProxy delegate];
-[_CLLocationSmootherProxy setConnection:];
-[_CLLocationSmootherProxy didSmoothLocations:ofType:];
-[_CLLocationSmootherProxy initWithCLLocationSmoother:];
-[_CLLocationSmootherProxy locationManagerSmoother];
-[_CLLocationSmootherProxy setLocationManagerSmoother:];
```
