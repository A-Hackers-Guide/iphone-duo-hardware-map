# `BKHIDEventRecognizerEngine`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventProcessor`
- 3 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _recognizers;
@"NSMutableArray" _blocks;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_recognizers) recognizers;
@property (T@"NSMutableArray",&,N,V_blocks) blocks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventRecognizerEngine init];
-[BKHIDEventRecognizerEngine processEvent:sender:dispatcher:];
-[BKHIDEventRecognizerEngine blocks];
-[BKHIDEventRecognizerEngine recognizers];
-[BKHIDEventRecognizerEngine setBlocks:];
-[BKHIDEventRecognizerEngine addRecognizer:recognitionBlock:];
-[BKHIDEventRecognizerEngine setRecognizers:];
-[BKHIDEventRecognizerEngine removeRecognizer:];
```
