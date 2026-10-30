# `BKHIDPointerEventRecord`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventProcessors.framework__BackBoardHIDEventProcessors.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _didTrackPointerMovement;
B _didTrackButtonDown;
B _trackingPointerMovement;
B _trackingButtonDown;
@"<BKHIDEventSenderInfo>" _senderInfo;
@"NSSet" _destinations;
d _destinationCaptureTime;
```

## Properties

```
@property (T@"<BKHIDEventSenderInfo>",&,N,V_senderInfo) senderInfo;
@property (T@"NSSet",&,N,V_destinations) destinations;
@property (Td,N,V_destinationCaptureTime) destinationCaptureTime;
@property (TB,N,V_trackingPointerMovement) trackingPointerMovement;
@property (TB,N,V_trackingButtonDown) trackingButtonDown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDPointerEventRecord setDestinations:];
-[BKHIDPointerEventRecord succinctDescriptionBuilder];
-[BKHIDPointerEventRecord destinations];
-[BKHIDPointerEventRecord descriptionWithMultilinePrefix:];
-[BKHIDPointerEventRecord succinctDescription];
-[BKHIDPointerEventRecord descriptionBuilderWithMultilinePrefix:];
-[BKHIDPointerEventRecord senderInfo];
-[BKHIDPointerEventRecord setSenderInfo:];
-[BKHIDPointerEventRecord destinationCaptureTime];
-[BKHIDPointerEventRecord setDestinationCaptureTime:];
-[BKHIDPointerEventRecord setTrackingButtonDown:];
-[BKHIDPointerEventRecord setTrackingPointerMovement:];
-[BKHIDPointerEventRecord trackingButtonDown];
-[BKHIDPointerEventRecord trackingPointerMovement];
```
