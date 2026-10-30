# `BKHIDEventSenderCache`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKIOHIDServiceDisappearanceObserver`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _senderIDToSenderInfo;
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
-[BKHIDEventSenderCache initWithQueue:];
-[BKHIDEventSenderCache description];
-[BKHIDEventSenderCache serviceDidDisappear:];
-[BKHIDEventSenderCache sync];
-[BKHIDEventSenderCache addSenderInfo:];
-[BKHIDEventSenderCache addSenderInfo:forSenderID:];
-[BKHIDEventSenderCache removeSenderInfo:];
-[BKHIDEventSenderCache senderInfoForSenderID:];
```
