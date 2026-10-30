# `BKHIDIncomingServiceConnection`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BKHIDDomainIncomingServiceConnectionDelegate`
- 7 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSString" _debugMappedObjectName;
@"NSObject<OS_os_log>" _log;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_wasHandled;
@"<BKHIDIncomingServiceConnectionDelegate>" _lock_delegate;
@"<_BKHIDIncomingServiceConnectionHandler>" _lock_handler;
@"BKHIDDomainIncomingServiceConnection" _domainIncomingServiceConnection;
```

## Properties

```
@property (T@"BKHIDDomainIncomingServiceConnection",R,N,V_domainIncomingServiceConnection) domainIncomingServiceConnection;
@property (T@"<_BKHIDIncomingServiceConnectionHandler>",N) handler;
@property (T@"BSAuditToken",R,N) auditToken;
@property (T@"<BKHIDIncomingServiceConnectionDelegate>",N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDIncomingServiceConnection rejectConnection];
-[BKHIDIncomingServiceConnection dealloc];
-[BKHIDIncomingServiceConnection setHandler:];
-[BKHIDIncomingServiceConnection setDelegate:];
-[BKHIDIncomingServiceConnection handler];
-[BKHIDIncomingServiceConnection delegate];
-[BKHIDIncomingServiceConnection description];
-[BKHIDIncomingServiceConnection appendDescriptionToStream:];
-[BKHIDIncomingServiceConnection auditToken];
-[BKHIDIncomingServiceConnection domainIncomingServiceConnection];
-[BKHIDIncomingServiceConnection acceptConnectionWithMappedObject:];
-[BKHIDIncomingServiceConnection acceptConnectionWithServiceQueue:clientCalloutContextualizer:];
-[BKHIDIncomingServiceConnection incomingServiceConnectionDidRevoke:];
-[BKHIDIncomingServiceConnection initWithIncomingServiceConnection:debugMappedObjectName:];
```
