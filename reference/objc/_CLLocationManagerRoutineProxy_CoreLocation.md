# `_CLLocationManagerRoutineProxy`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerRoutineClientInterface`
- 6 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _updating;
@"NSXPCConnection" _connection;
@ _delegate;
@ _inertialDelegate;
@"CLLocationManagerRoutine" _locationManagerRoutine;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@,N,V_delegate) delegate;
@property (T@,N,V_inertialDelegate) inertialDelegate;
@property (T@"CLLocationManagerRoutine",N,V_locationManagerRoutine) locationManagerRoutine;
@property (TB,N,V_updating) updating;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_CLLocationManagerRoutineProxy createConnection];
-[_CLLocationManagerRoutineProxy didUpdateLocations:];
-[_CLLocationManagerRoutineProxy dealloc];
-[_CLLocationManagerRoutineProxy locationManagerRoutine];
-[_CLLocationManagerRoutineProxy setDelegate:];
-[_CLLocationManagerRoutineProxy connection];
-[_CLLocationManagerRoutineProxy delegate];
-[_CLLocationManagerRoutineProxy setConnection:];
-[_CLLocationManagerRoutineProxy setUpdating:];
-[_CLLocationManagerRoutineProxy setLocationManagerRoutine:];
-[_CLLocationManagerRoutineProxy didUpdateInertialData:];
-[_CLLocationManagerRoutineProxy didUpdateLocations:withReply:];
-[_CLLocationManagerRoutineProxy getRemoteObjectProxyWithErrorHandler:];
-[_CLLocationManagerRoutineProxy inertialDelegate];
-[_CLLocationManagerRoutineProxy initWithQueue:locationManagerRoutine:];
-[_CLLocationManagerRoutineProxy setInertialDelegate:];
-[_CLLocationManagerRoutineProxy updating];
```
