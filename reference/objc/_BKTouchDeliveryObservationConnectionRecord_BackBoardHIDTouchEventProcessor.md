# `_BKTouchDeliveryObservationConnectionRecord`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
i _pid;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
d _lock_updateSentTimestamp;
@"NSMutableArray" _lock_pendingUpdates;
@"NSMutableIndexSet" _lock_pendingBackgroundUpdate;
B _lock_waitingOnClient;
@"BKHIDDomainServiceServer" _domainServiceServer;
```

## Instance methods

```
-[_BKTouchDeliveryObservationConnectionRecord _lock_sendQueuedUpdatesToClient];
-[_BKTouchDeliveryObservationConnectionRecord _didRespondToTouchDelivery];
-[_BKTouchDeliveryObservationConnectionRecord sendBackgroundTouchUpdate:];
-[_BKTouchDeliveryObservationConnectionRecord sendTouchUpdate:];
```
