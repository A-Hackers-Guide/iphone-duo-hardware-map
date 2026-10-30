# `BWObjectRingBuffer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 25 instance methods, 1 class methods

## Instance variables

```
^@ _objects;
^{?=qiIq} _times;
i _capacity;
i _count;
i _oldest;
B _ascending;
B _expectAscending;
B _enforceAscending;
```

## Properties

```
@property (Ti,R,N,V_count) count;
@property (Ti,N,V_capacity) capacity;
@property (TB,R,N,V_ascending) ascending;
@property (TB,N,V_expectAscending) expectAscending;
@property (TB,N) enforceAscending;
```

## Class methods

```
+[BWObjectRingBuffer initialize];
```

## Instance methods

```
-[BWObjectRingBuffer setCapacity:];
-[BWObjectRingBuffer lastObject];
-[BWObjectRingBuffer clear];
-[BWObjectRingBuffer firstObject];
-[BWObjectRingBuffer capacity];
-[BWObjectRingBuffer dealloc];
-[BWObjectRingBuffer count];
-[BWObjectRingBuffer initWithCapacity:];
-[BWObjectRingBuffer description];
-[BWObjectRingBuffer ascending];
-[BWObjectRingBuffer lastTime];
-[BWObjectRingBuffer expectAscending];
-[BWObjectRingBuffer _enumerateObjectsStartingAtOffset:usingBlock:];
-[BWObjectRingBuffer _findClosestOffsetToTimestamp:];
-[BWObjectRingBuffer _forceAscendingTo:];
-[BWObjectRingBuffer _reverseEnumerateObjectsStartingAtOffset:usingBlock:];
-[BWObjectRingBuffer appendObject:forTime:];
-[BWObjectRingBuffer enforceAscending];
-[BWObjectRingBuffer enumerateObjectsStartingAt:usingBlock:];
-[BWObjectRingBuffer extractTimeRangeFrom:until:into:times:];
-[BWObjectRingBuffer firstTime];
-[BWObjectRingBuffer flushEntriesEarlierThan:];
-[BWObjectRingBuffer reverseEnumerateObjectsStartingAt:usingBlock:];
-[BWObjectRingBuffer setEnforceAscending:];
-[BWObjectRingBuffer setExpectAscending:];
```
