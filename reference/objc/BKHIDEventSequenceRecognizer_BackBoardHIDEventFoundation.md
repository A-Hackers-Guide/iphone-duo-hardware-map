# `BKHIDEventSequenceRecognizer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventRecognizer`
- 3 instance variables, 6 properties, 4 instance methods, 2 class methods

## Instance variables

```
q _descriptorIndex;
B _shouldConsumeEvents;
@"NSArray" _descriptors;
```

## Properties

```
@property (TB,N,V_shouldConsumeEvents) shouldConsumeEvents;
@property (T@"NSArray",R,N,V_descriptors) descriptors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDEventSequenceRecognizer recognizerForEventDescriptor:];
+[BKHIDEventSequenceRecognizer recognizerForEventDescriptors:];
```

## Instance methods

```
-[BKHIDEventSequenceRecognizer descriptors];
-[BKHIDEventSequenceRecognizer processEvent:shouldConsume:];
-[BKHIDEventSequenceRecognizer setShouldConsumeEvents:];
-[BKHIDEventSequenceRecognizer shouldConsumeEvents];
```
