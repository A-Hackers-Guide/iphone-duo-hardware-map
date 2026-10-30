# `CWFXPCListener`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `CWFXPCConnectionDelegate`
- 8 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSXPCListener" _XPCListener;
@"NSMutableArray" _mutableXPCConnections;
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSXPCInterface" _requestXPCInterface;
@"NSXPCInterface" _eventXPCInterface;
@"NSArray" _bootArgs;
@"<CWFXPCListenerDelegate>" _delegate;
q _serviceType;
```

## Properties

```
@property (T@"<CWFXPCListenerDelegate>",&,V_delegate) delegate;
@property (Tq,R,N,V_serviceType) serviceType;
@property (T@"NSXPCListener",R,&,N,V_XPCListener) XPCListener;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CWFXPCListener sendXPCEvent:reply:];
-[CWFXPCListener registeredEventIDs];
-[CWFXPCListener registeredActivities];
-[CWFXPCListener initWithServiceType:];
-[CWFXPCListener suspend];
-[CWFXPCListener listener:shouldAcceptNewConnection:];
-[CWFXPCListener init];
-[CWFXPCListener invalidate];
-[CWFXPCListener setDelegate:];
-[CWFXPCListener activate];
-[CWFXPCListener delegate];
-[CWFXPCListener resume];
-[CWFXPCListener serviceType];
-[CWFXPCListener XPCConnection:canceledXPCRequestsWithUUID:];
-[CWFXPCListener XPCConnection:completedXPCRequest:];
-[CWFXPCListener XPCConnection:receivedXPCRequest:];
-[CWFXPCListener XPCConnection:updatedProcessState:];
-[CWFXPCListener XPCConnection:updatedRegisteredEventIDs:];
-[CWFXPCListener XPCConnections];
-[CWFXPCListener XPCListener];
-[CWFXPCListener __allowXPCConnection:serviceType:];
-[CWFXPCListener localXPCClient];
```
