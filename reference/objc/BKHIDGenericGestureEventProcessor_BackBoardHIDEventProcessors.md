# `BKHIDGenericGestureEventProcessor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventProcessors.framework__BackBoardHIDEventProcessors.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKIOHIDServiceDisappearanceObserver`, `BKHIDEventProcessor`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _pendingDestinationsPerSenderID;
@"NSMutableDictionary" _genericGestureTypePerSenderID;
@"<BKHIDEventDispatcher>" _eventDispatcher;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_pendingDestinationsPerSenderID) pendingDestinationsPerSenderID;
@property (T@"NSMutableDictionary",&,N,V_genericGestureTypePerSenderID) genericGestureTypePerSenderID;
@property (T@"<BKHIDEventDispatcher>",&,N,V_eventDispatcher) eventDispatcher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDGenericGestureEventProcessor eventDispatcher];
-[BKHIDGenericGestureEventProcessor processEvent:sender:dispatcher:];
-[BKHIDGenericGestureEventProcessor setEventDispatcher:];
-[BKHIDGenericGestureEventProcessor serviceDidDisappear:];
-[BKHIDGenericGestureEventProcessor _postEvent:toDestination:usingDispatcher:];
-[BKHIDGenericGestureEventProcessor genericGestureTypePerSenderID];
-[BKHIDGenericGestureEventProcessor pendingDestinationsPerSenderID];
-[BKHIDGenericGestureEventProcessor setGenericGestureTypePerSenderID:];
-[BKHIDGenericGestureEventProcessor setPendingDestinationsPerSenderID:];
```
