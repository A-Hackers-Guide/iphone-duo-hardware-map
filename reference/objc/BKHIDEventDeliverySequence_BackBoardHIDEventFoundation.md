# `BKHIDEventDeliverySequence`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSCopying`
- 13 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<BKHIDEventSenderInfo>" _senderInfo;
@"<BKHIDBufferedEventProcessor>" _processor;
@"<BKHIDEventDispatcher>" _dispatcher;
@"BKHIDEventDeliveryManager" _deliveryManager;
@ _additionalContext;
@"BKSHIDEventKeyCommand" _keyCommand;
@"NSMutableSet" _currentBuffers;
@"NSMutableSet" _buffersWithIncompleteSequences;
@"NSMutableSet" _currentResolutions;
@"NSMutableSet" _resolutionsWithIncompleteSequences;
@"NSMutableSet" _repostedToBuffers;
^{__IOHIDEvent=} _firstEvent;
@ _firstAdditionalContext;
```

## Properties

```
@property (T@,R,V_firstAdditionalContext) firstAdditionalContext;
@property (T@"BKSHIDEventKeyCommand",R,V_keyCommand) keyCommand;
@property (T@"<BKHIDEventDispatcher>",R,V_dispatcher) dispatcher;
@property (T@"<BKHIDBufferedEventProcessor>",R,V_processor) processor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventDeliverySequence dispatcher];
-[BKHIDEventDeliverySequence buffers];
-[BKHIDEventDeliverySequence appendDescriptionToFormatter:];
-[BKHIDEventDeliverySequence dealloc];
-[BKHIDEventDeliverySequence description];
-[BKHIDEventDeliverySequence processor];
-[BKHIDEventDeliverySequence keyCommand];
-[BKHIDEventDeliverySequence copyWithZone:];
-[BKHIDEventDeliverySequence resolutions];
-[BKHIDEventDeliverySequence bufferDidDrain:];
-[BKHIDEventDeliverySequence firstAdditionalContext];
-[BKHIDEventDeliverySequence initWithProcessor:dispatcher:senderInfo:additionalContext:keyCommand:deliveryManager:resolutions:buffers:];
-[BKHIDEventDeliverySequence postEvent:position:additionalContext:];
-[BKHIDEventDeliverySequence postEvent:position:additionalContext:fromBuffer:toResolution:];
-[BKHIDEventDeliverySequence repostFirstEventToBufferedTargets:];
```
