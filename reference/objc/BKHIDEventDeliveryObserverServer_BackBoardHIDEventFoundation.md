# `BKHIDEventDeliveryObserverServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventObserverServerInterface`, `BKHIDDomainServiceDelegate`, `BKHIDDomainIncomingServiceConnectionHandler`, `_BKHIDIncomingServiceConnectionHandler`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>" _incomingServiceConnectionHandler;
```

## Properties

```
@property (T@"BKHIDDomainServiceServer",R,N) domainServiceServer;
@property (T@"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>",R,N) incomingConnectionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventDeliveryObserverServer connectionDidTerminate:];
-[BKHIDEventDeliveryObserverServer activate];
-[BKHIDEventDeliveryObserverServer domainServiceServer];
-[BKHIDEventDeliveryObserverServer setObservesDeferringChanges:];
-[BKHIDEventDeliveryObserverServer setReachabilityObservationTargets:];
-[BKHIDEventDeliveryObserverServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKHIDEventDeliveryObserverServer handleIncomingServiceConnection:];
-[BKHIDEventDeliveryObserverServer incomingConnectionHandler];
-[BKHIDEventDeliveryObserverServer initWithDeliveryObserverServiceProvider:];
-[BKHIDEventDeliveryObserverServer initWithIncomingServiceConnectionHandler:];
-[BKHIDEventDeliveryObserverServer rejectIncomingServiceConnection:];
```
