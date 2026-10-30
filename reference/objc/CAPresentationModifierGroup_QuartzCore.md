# `CAPresentationModifierGroup`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
^v _shmem;
Q _capacity;
Q _count;
Q _totalSize;
I _localId;
```

## Properties

```
@property (TQ,R) capacity;
@property (TQ,R) count;
@property (TB,N) updatesAsynchronously;
```

## Class methods

```
+[CAPresentationModifierGroup groupWithCapacity:];
```

## Instance methods

```
-[CAPresentationModifierGroup updatesAsynchronously];
-[CAPresentationModifierGroup capacity];
-[CAPresentationModifierGroup flushLocally];
-[CAPresentationModifierGroup shmem];
-[CAPresentationModifierGroup flush];
-[CAPresentationModifierGroup _setLocalContextId:];
-[CAPresentationModifierGroup dealloc];
-[CAPresentationModifierGroup markWritten:];
-[CAPresentationModifierGroup count];
-[CAPresentationModifierGroup _renderShmem];
-[CAPresentationModifierGroup flushWithTargetTime:];
-[CAPresentationModifierGroup setUpdatesAsynchronously:];
-[CAPresentationModifierGroup flushWithTransaction];
-[CAPresentationModifierGroup resetBitMask];
-[CAPresentationModifierGroup flushLocallyWithTargetTime:];
-[CAPresentationModifierGroup flushWithTransactionAndTargetTime:];
-[CAPresentationModifierGroup nextSlotWithPayloadSize:];
-[CAPresentationModifierGroup initWithCapacity:];
```
