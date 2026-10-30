# `BKHIDPrimaryEventProcessor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventProcessor`, `BKHIDBufferedEventProcessor`
- 5 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
[45@"NSArray"] _subProcessors;
@"<BKHIDEventProcessor>" _defaultProcessor;
[45@"NSArray"] _bufferedSubProcessors;
@"NSSet" _allBufferedEventProcessors;
@"<BKHIDBufferedEventProcessor>" _defaultBufferedEventProcessor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDPrimaryEventProcessor primaryProcessorWithCreationContext:configuration:];
```

## Instance methods

```
-[BKHIDPrimaryEventProcessor processEvent:sender:dispatcher:];
-[BKHIDPrimaryEventProcessor _eventProcessorsForEventType:];
-[BKHIDPrimaryEventProcessor bufferDidEndDraining:];
-[BKHIDPrimaryEventProcessor bufferWillBeginDraining:];
-[BKHIDPrimaryEventProcessor bufferingDidAddNewBuffers:];
-[BKHIDPrimaryEventProcessor conformsToBKHIDBufferedEventProcessor];
-[BKHIDPrimaryEventProcessor postEvent:withContext:toResolution:fromSequence:];
-[BKHIDPrimaryEventProcessor processEvent:withContext:buffer:sequence:sender:dispatcher:resolution:];
```
