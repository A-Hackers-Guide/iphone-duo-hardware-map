# `BKSTouchDeliveryObservationService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 6 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _calloutQueue;
@"NSObject<OS_dispatch_queue>" _touchClientQueue;
@"BSServiceDispatchQueue" _bsServiceDispatchQueue;
@"<BKSTouchDeliveryObservationService_IPC>" _remoteTarget;
@"BSServiceInitiatingConnection" _connection;
@"NSMapTable" _generalObserverToKinds;
@"BSMutableIntegerMap" _touchIdentifierToObserverKinds;
@"NSMapTable" _observersToTouchIdentifiers;
@"NSSet" _lastGeneralKindsSent;
@"BSMutableIntegerMap" _lastKindsSentForTouchIdentifier;
```

## Properties

```
@property (T@"BSServiceInitiatingConnection",&,N,V_connection) connection;
@property (T@"NSMapTable",&,N,V_generalObserverToKinds) generalObserverToKinds;
@property (T@"BSMutableIntegerMap",&,N,V_touchIdentifierToObserverKinds) touchIdentifierToObserverKinds;
@property (T@"NSMapTable",&,N,V_observersToTouchIdentifiers) observersToTouchIdentifiers;
@property (T@"NSSet",&,N,V_lastGeneralKindsSent) lastGeneralKindsSent;
@property (T@"BSMutableIntegerMap",&,N,V_lastKindsSentForTouchIdentifier) lastKindsSentForTouchIdentifier;
```

## Class methods

```
+[BKSTouchDeliveryObservationService sharedInstance];
```

## Instance methods

```
-[BKSTouchDeliveryObservationService removeObserver:];
-[BKSTouchDeliveryObservationService init];
-[BKSTouchDeliveryObservationService dealloc];
-[BKSTouchDeliveryObservationService initWithConnection:];
-[BKSTouchDeliveryObservationService addObserver:];
-[BKSTouchDeliveryObservationService connection];
-[BKSTouchDeliveryObservationService setConnection:];
-[BKSTouchDeliveryObservationService addObserver:forTouchIdentifier:];
-[BKSTouchDeliveryObservationService lastKindsSentForTouchIdentifier];
-[BKSTouchDeliveryObservationService _queue_syncGeneralKindsToRemote];
-[BKSTouchDeliveryObservationService addObserver:forOccurrenceKinds:];
-[BKSTouchDeliveryObservationService setObserversToTouchIdentifiers:];
-[BKSTouchDeliveryObservationService _configureConnection];
-[BKSTouchDeliveryObservationService _connectionForTouchDeliveryService];
-[BKSTouchDeliveryObservationService _deliverOccurrence:toObserver:];
-[BKSTouchDeliveryObservationService _processTouchEventDeliveryUpdate:];
-[BKSTouchDeliveryObservationService _queue_addObserver:forTouchIdentifier:kinds:];
-[BKSTouchDeliveryObservationService _queue_aggregateGeneralKinds];
-[BKSTouchDeliveryObservationService _queue_aggregateKindsForTouchIdentifier:];
-[BKSTouchDeliveryObservationService _queue_aggregateKindsFromMapTable:];
-[BKSTouchDeliveryObservationService _queue_handlePendingObservers:];
-[BKSTouchDeliveryObservationService _queue_observerKindsForTouchIdentifier:];
-[BKSTouchDeliveryObservationService _queue_removeObserver:forTouchIdentifier:];
-[BKSTouchDeliveryObservationService _queue_syncKindsForTouchIdentifier:];
-[BKSTouchDeliveryObservationService addObserver:forTouchIdentifier:occurrenceKinds:];
-[BKSTouchDeliveryObservationService generalObserverToKinds];
-[BKSTouchDeliveryObservationService lastGeneralKindsSent];
-[BKSTouchDeliveryObservationService observeTouchEventDeliveryDidOccur:response:];
-[BKSTouchDeliveryObservationService observersToTouchIdentifiers];
-[BKSTouchDeliveryObservationService setGeneralObserverToKinds:];
-[BKSTouchDeliveryObservationService setLastGeneralKindsSent:];
-[BKSTouchDeliveryObservationService setLastKindsSentForTouchIdentifier:];
-[BKSTouchDeliveryObservationService setTouchIdentifierToObserverKinds:];
-[BKSTouchDeliveryObservationService touchIdentifierToObserverKinds];
```
