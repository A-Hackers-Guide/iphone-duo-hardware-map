# `BKHIDDomainIncomingServiceConnection`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceListenerConnectionEventObserver`, `BSDescriptionStreaming`
- 7 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"BSServiceListenerConnection" _connection;
@"NSObject<OS_os_log>" _log;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BSInvalidatable>" _lock_eventObserver;
B _lock_wasHandled;
@"<BKHIDDomainIncomingServiceConnectionDelegate>" _lock_delegate;
@"<_BKHIDDomainIncomingServiceConnectionHandler>" _lock_handler;
```

## Properties

```
@property (T@"<_BKHIDDomainIncomingServiceConnectionHandler>",N) handler;
@property (T@"BSServiceListenerConnection",R,N,V_connection) connection;
@property (T@"NSObject<OS_os_log>",R,N,V_log) log;
@property (T@"<BKHIDDomainIncomingServiceConnectionDelegate>",N) delegate;
@property (TB,R,N,GisRevoked) revoked;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDDomainIncomingServiceConnection rejectConnection];
-[BKHIDDomainIncomingServiceConnection dealloc];
-[BKHIDDomainIncomingServiceConnection setHandler:];
-[BKHIDDomainIncomingServiceConnection setDelegate:];
-[BKHIDDomainIncomingServiceConnection handler];
-[BKHIDDomainIncomingServiceConnection connection];
-[BKHIDDomainIncomingServiceConnection isRevoked];
-[BKHIDDomainIncomingServiceConnection delegate];
-[BKHIDDomainIncomingServiceConnection description];
-[BKHIDDomainIncomingServiceConnection appendDescriptionToStream:];
-[BKHIDDomainIncomingServiceConnection log];
-[BKHIDDomainIncomingServiceConnection connection:revokedWithEvent:];
-[BKHIDDomainIncomingServiceConnection acceptConnectionUsingServiceQueue:clientCalloutContextualizer:];
-[BKHIDDomainIncomingServiceConnection initWithConnection:log:];
```
