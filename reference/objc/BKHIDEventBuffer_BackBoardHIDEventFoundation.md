# `BKHIDEventBuffer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `BSInvalidatable`
- 5 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _buffer;
B _invalidated;
B _allBufferingClientsTerminated;
@"BKSHIDEventDispatchingTarget" _dispatchTarget;
@"NSSet" _bufferingPIDs;
```

## Properties

```
@property (T@"BKSHIDEventDispatchingTarget",R,C,N,V_dispatchTarget) dispatchTarget;
@property (TB,N,V_allBufferingClientsTerminated) allBufferingClientsTerminated;
@property (T@"NSSet",&,N,V_bufferingPIDs) bufferingPIDs;
@property (TB,R,N) hasEvents;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventBuffer appendDescriptionToFormatter:];
-[BKHIDEventBuffer dealloc];
-[BKHIDEventBuffer invalidate];
-[BKHIDEventBuffer description];
-[BKHIDEventBuffer hasEvents];
-[BKHIDEventBuffer _test_peekAllEvents];
-[BKHIDEventBuffer _test_peekAllIOHIDEvents];
-[BKHIDEventBuffer allBufferingClientsTerminated];
-[BKHIDEventBuffer appendEvent:sender:sequence:additionalContext:];
-[BKHIDEventBuffer bufferingPIDs];
-[BKHIDEventBuffer dispatchTarget];
-[BKHIDEventBuffer drainAllEvents];
-[BKHIDEventBuffer initWithDispatchTarget:];
-[BKHIDEventBuffer setAllBufferingClientsTerminated:];
-[BKHIDEventBuffer setBufferingPIDs:];
```
