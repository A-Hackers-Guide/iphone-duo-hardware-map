# `BWObjectRingBufferThreadSafe`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWObjectRingBuffer`
- 1 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigReentrantMutex=} _lock;
```

## Instance methods

```
-[BWObjectRingBufferThreadSafe setCapacity:];
-[BWObjectRingBufferThreadSafe lastObject];
-[BWObjectRingBufferThreadSafe clear];
-[BWObjectRingBufferThreadSafe firstObject];
-[BWObjectRingBufferThreadSafe dealloc];
-[BWObjectRingBufferThreadSafe initWithCapacity:];
-[BWObjectRingBufferThreadSafe description];
-[BWObjectRingBufferThreadSafe lastTime];
-[BWObjectRingBufferThreadSafe appendObject:forTime:];
-[BWObjectRingBufferThreadSafe enumerateObjectsStartingAt:usingBlock:];
-[BWObjectRingBufferThreadSafe extractTimeRangeFrom:until:into:times:];
-[BWObjectRingBufferThreadSafe firstTime];
-[BWObjectRingBufferThreadSafe flushEntriesEarlierThan:];
-[BWObjectRingBufferThreadSafe reverseEnumerateObjectsStartingAt:usingBlock:];
```
