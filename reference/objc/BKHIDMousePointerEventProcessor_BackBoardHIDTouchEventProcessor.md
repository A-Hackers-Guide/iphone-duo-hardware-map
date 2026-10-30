# `BKHIDMousePointerEventProcessor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventProcessor`
- 4 instance variables, 5 properties, 3 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BKMousePointerController" _mousePointerController;
@"BKMousePointerServiceServer" _mousePointerServiceServer;
i _assistiveTouchNotificationToken;
```

## Properties

```
@property (T@"BKMousePointerController",R,N) mousePointerController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDMousePointerEventProcessor initWithContext:];
-[BKHIDMousePointerEventProcessor processEvent:sender:dispatcher:];
-[BKHIDMousePointerEventProcessor mousePointerController];
```
