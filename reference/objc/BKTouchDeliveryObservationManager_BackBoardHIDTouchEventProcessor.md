# `BKTouchDeliveryObservationManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDDomainServiceDelegate`, `BKTouchLifecycleObserver`
- 10 instance variables, 6 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
@"BSMutableIntegerMap" _touchIdentifierToPidKinds;
@"BSMutableIntegerMap" _pidToGeneralKinds;
@"BSMutableIntegerMap" _touchIdentifierToUpdate;
@"BSMutableIntegerMap" _touchIdentifierToDownUpdate;
@"BSMutableIntegerMap" _touchIdentifierToTransducerType;
@"BSMutableIntegerMap" _pidsToBackgroundObservers;
@"BSMutableIntegerMap" _touchIdentifierToBackgroundUpdate;
@"BSServiceDispatchQueue" _bsServiceDispatchQueue;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N) queue;
@property (T@"BKHIDDomainServiceServer",R,N) domainServiceServer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchDeliveryObservationManager touch:pathIndex:downAtPoint:eventMask:transducerType:];
-[BKTouchDeliveryObservationManager touch:didAlwaysRouteToTargetID:clientTaskName:];
-[BKTouchDeliveryObservationManager _queue_pendDownUpdate:];
-[BKTouchDeliveryObservationManager touchDidFinishProcessingTouchCollection];
-[BKTouchDeliveryObservationManager _queue_isAnyPIDObservingIdentifier:];
-[BKTouchDeliveryObservationManager touch:didMoveToPoint:eventMask:z:maxZ:];
-[BKTouchDeliveryObservationManager touch:didHitTestToDestination:hostingChainIndex:];
-[BKTouchDeliveryObservationManager hitTestRegionsDidChange:];
-[BKTouchDeliveryObservationManager _queue_pendUpdate:];
-[BKTouchDeliveryObservationManager _queue_postPendingBackgroundUpdates];
-[BKTouchDeliveryObservationManager _queue_pendBackgroundUpdate:];
-[BKTouchDeliveryObservationManager setProcessPID:observesGeneralOccurrenceKinds:];
-[BKTouchDeliveryObservationManager touchWillStartProcessingTouchCollection];
-[BKTouchDeliveryObservationManager _queue_addBackgroundUpdate:toNotify:];
-[BKTouchDeliveryObservationManager touchDidHIDCancel:];
-[BKTouchDeliveryObservationManager touchDidSoftCancel:];
-[BKTouchDeliveryObservationManager touch:pathIndex:rangeInAtPoint:eventMask:z:maxZ:transducerType:];
-[BKTouchDeliveryObservationManager queue];
-[BKTouchDeliveryObservationManager addBackgroundObserver:inPID:];
-[BKTouchDeliveryObservationManager touch:pathIndex:upAtPoint:detached:];
-[BKTouchDeliveryObservationManager touch:pathIndex:rangeOutAtPoint:];
-[BKTouchDeliveryObservationManager _queue_postPendingUpdates];
-[BKTouchDeliveryObservationManager touchDidDetach:destinations:];
-[BKTouchDeliveryObservationManager noteTouchDownOccurred:destination:event:];
-[BKTouchDeliveryObservationManager _queue_postUpdate:toProcessPID:];
-[BKTouchDeliveryObservationManager touchDidTransfer:destination:];
-[BKTouchDeliveryObservationManager connectionDidTerminate:];
-[BKTouchDeliveryObservationManager _queue_postUpdate:forTouchIdentifier:];
-[BKTouchDeliveryObservationManager _queue_setProcessPID:observesOccurrenceKinds:withTouchIdentifier:];
-[BKTouchDeliveryObservationManager domainServiceServer];
-[BKTouchDeliveryObservationManager initWithServer:];
-[BKTouchDeliveryObservationManager removeBackgroundObserver:inPID:];
-[BKTouchDeliveryObservationManager noteTouchUpOccurred:destination:event:];
-[BKTouchDeliveryObservationManager _pidForClientTaskName:];
-[BKTouchDeliveryObservationManager _queue_postBackgroundUpdateToProcessPID:observers:];
-[BKTouchDeliveryObservationManager _queue_setProcessPID:observesGeneralOccurrenceKinds:];
-[BKTouchDeliveryObservationManager _queue_connectionDidTerminate:];
-[BKTouchDeliveryObservationManager setProcessPID:observesOccurrenceKinds:withTouchIdentifier:];
```
