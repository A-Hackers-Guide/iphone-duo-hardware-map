# `BKBufferedEventEntry`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@ _rawEvent;
@"<BKHIDEventSenderInfo>" _sender;
@"BKHIDEventDeliverySequence" _sequence;
@ _additionalContext;
```

## Properties

```
@property (T@"<BKHIDEventSenderInfo>",&,N,V_sender) sender;
@property (T@"BKHIDEventDeliverySequence",&,N,V_sequence) sequence;
@property (T@,&,N,V_additionalContext) additionalContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKBufferedEventEntry setEvent:];
-[BKBufferedEventEntry sequence];
-[BKBufferedEventEntry event];
-[BKBufferedEventEntry invalidate];
-[BKBufferedEventEntry sender];
-[BKBufferedEventEntry setSequence:];
-[BKBufferedEventEntry setSender:];
-[BKBufferedEventEntry additionalContext];
-[BKBufferedEventEntry setAdditionalContext:];
```
