# `/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`

iOS 27.2 dyld shared cache image. Version `877.2.2.600.0`. **[DSC]**

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog`
- `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`
- `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 7 classes, 4 protocols, 58 methods, 40 properties

### Class pages

Every class and protocol, with its methods: [`BKHIDBiometricEventProcessor`](../objc/BKHIDBiometricEventProcessor_BackBoardHIDEventProcessors.md), [`BKHIDEventProcessor`](../objc/BKHIDEventProcessor_BackBoardHIDEventProcessors.protocol.md), [`BKHIDGameControllerEventProcessor`](../objc/BKHIDGameControllerEventProcessor_BackBoardHIDEventProcessors.md), [`BKHIDGenericGestureEventProcessor`](../objc/BKHIDGenericGestureEventProcessor_BackBoardHIDEventProcessors.md), [`BKHIDPointerEventProcessor`](../objc/BKHIDPointerEventProcessor_BackBoardHIDEventProcessors.md), [`BKHIDPointerEventRecord`](../objc/BKHIDPointerEventRecord_BackBoardHIDEventProcessors.md), [`BKHIDScrollEventProcessor`](../objc/BKHIDScrollEventProcessor_BackBoardHIDEventProcessors.md), [`BKHIDVendorDefinedEventProcessor`](../objc/BKHIDVendorDefinedEventProcessor_BackBoardHIDEventProcessors.md), [`BKIOHIDServiceDisappearanceObserver`](../objc/BKIOHIDServiceDisappearanceObserver_BackBoardHIDEventProcessors.protocol.md), [`BSDescriptionProviding`](../objc/BSDescriptionProviding_BackBoardHIDEventProcessors.protocol.md), [`NSObject`](../objc/NSObject_BackBoardHIDEventProcessors.protocol.md)

### Classes

`BKHIDBiometricEventProcessor`, `BKHIDGameControllerEventProcessor`, `BKHIDGenericGestureEventProcessor`, `BKHIDPointerEventProcessor`, `BKHIDPointerEventRecord`, `BKHIDScrollEventProcessor`, `BKHIDVendorDefinedEventProcessor`

### Protocols

`BKHIDEventProcessor`, `BKIOHIDServiceDisappearanceObserver`, `BSDescriptionProviding`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",&,N,V_pendingDestinationsPerSenderID) pendingDestinationsPerSenderID;
@property (T@"NSMutableDictionary",&,N,V_genericGestureTypePerSenderID) genericGestureTypePerSenderID;
@property (T@"<BKHIDEventDispatcher>",&,N,V_eventDispatcher) eventDispatcher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BKHIDEventSenderInfo>",&,N,V_senderInfo) senderInfo;
@property (T@"NSSet",&,N,V_destinations) destinations;
@property (Td,N,V_destinationCaptureTime) destinationCaptureTime;
@property (TB,N,V_trackingPointerMovement) trackingPointerMovement;
@property (TB,N,V_trackingButtonDown) trackingButtonDown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (38)

```
generic %{public}@
filtering out generic event with zero phase (%{public}@)
  sender:%llX acquire destinations:%{public}@
  send to %{public}@
 %llX <displayID:%{public}@> pointer processing finished: %{public}@
 %llX <displayID:%{public}@> pointer processing began: %{public}@
Got an external interaction event meant for display: %{public}@, %{public}@
Motion event usagePage:0x%lX usage:%ld 
VendorDefinedEvent usagePage:0x%lX usage:%ld 
  sender:%llX remove all destinations
generic cancel %{public}@
Got an external interaction event of type %d, but there is no destination set for it
Dropping unknown biometric event type %d 
game controller event occurred; notifying user event timer
senderInfo
destinations
destinationCaptureTime
GenericGesture
RenderOverlay
IdleTimer
HapticFeedback
MotionEvents
@16@?0@\"BKSHIDEventDeferringResolution\"8
trackingButtonDown
trackingPointerMovement
didTrackPointerMovement
com.apple.BackBoard
DisplayMonitor
HID
KeyPresses
trackedTime
didTrackButtonDown
v8@?0
Button
Accelerometer
SendHIDEvent
BootUI
DisplayAnnotations
```
