# `BKTouchDeliveryObservationManagerServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSTouchDeliveryObservationService_IPC`, `BKHIDDomainServiceDelegate`, `BKHIDDomainIncomingServiceConnectionHandler`, `_BKHIDIncomingServiceConnectionHandler`
- 3 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
@"<BKTouchDeliveryObservationManagerIncomingConnectionHandler>" _incomingServiceConnectionHandler;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@"<BKTouchDeliveryObservationManagerIncomingConnectionHandler>",R,N) incomingConnectionHandler;
@property (T@"BKHIDDomainServiceServer",R,N) server;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchDeliveryObservationManagerServer server];
-[BKTouchDeliveryObservationManagerServer connectionDidTerminate:];
-[BKTouchDeliveryObservationManagerServer activate];
-[BKTouchDeliveryObservationManagerServer setObservesGeneralOccurrenceKinds:];
-[BKTouchDeliveryObservationManagerServer setObservesOccurrenceKinds:withIdentifier:];
-[BKTouchDeliveryObservationManagerServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKTouchDeliveryObservationManagerServer handleIncomingServiceConnection:];
-[BKTouchDeliveryObservationManagerServer incomingConnectionHandler];
-[BKTouchDeliveryObservationManagerServer rejectIncomingServiceConnection:];
-[BKTouchDeliveryObservationManagerServer addBackgroundObserver:];
-[BKTouchDeliveryObservationManagerServer initWithIncomingConnectionHandler:];
-[BKTouchDeliveryObservationManagerServer removeBackgroundObserver:];
```
