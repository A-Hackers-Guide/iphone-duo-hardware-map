# `BKTouchPadManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKIOHIDServiceMatchObserver`, `BKIOHIDServiceDisappearanceObserver`, `BKHIDEventProcessor`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _touchPadQueue;
@"NSMutableDictionary" _queue_currentTouchPads;
@"BKIOHIDServiceMatcher" _touchPadMatcher;
@"BKHIDEventSenderCache" _senderCache;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchPadManager dealloc];
-[BKTouchPadManager processEvent:sender:dispatcher:];
-[BKTouchPadManager matcher:servicesDidMatch:];
-[BKTouchPadManager serviceDidDisappear:];
-[BKTouchPadManager _queue_handleEvent:fromTouchPad:dispatcher:];
-[BKTouchPadManager _queue_sendCancelEventForTouchPad:];
-[BKTouchPadManager _queue_sendEvent:fromTouchPad:toDestination:dispatcher:];
-[BKTouchPadManager _queue_touchPadRemoved:];
-[BKTouchPadManager _queue_touchPadsDetected:];
-[BKTouchPadManager initWithMatcherDataProvider:senderCache:];
-[BKTouchPadManager processEvent:sender:display:dispatcher:];
-[BKTouchPadManager sendCancelEventForAllDisplays];
-[BKTouchPadManager sendCancelEventForDisplay:];
```
