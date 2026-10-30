# `BWCompressedShotBuffer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 11 instance methods, 0 class methods

## Properties

```
@property (Ti,N) uncompressedEquivalentCapacity;
@property (Ti,R,N) minimumUncompressedEquivalentCapacity;
@property (TB,R,N) compressionResourcesAllocated;
@property (T@?,C,N) freeBufferCountIncreasedHandler;
@property (TB,R,N) passthroughEnabled;
```

## Instance methods

```
-[BWCompressedShotBuffer flushAndWaitForUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBuffer setFreeBufferCountIncreasedHandler:];
-[BWCompressedShotBuffer freeBufferCountIncreasedHandler];
-[BWCompressedShotBuffer flushAndWaitUntilThreshold:];
-[BWCompressedShotBuffer passthroughEnabled];
-[BWCompressedShotBuffer uncompressedEquivalentCapacity];
-[BWCompressedShotBuffer hasUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBuffer compressionResourcesAllocated];
-[BWCompressedShotBuffer minimumUncompressedEquivalentCapacity];
-[BWCompressedShotBuffer getInUseCompressedBufferCount:inUseCompressedBytes:maxInUseCompressedBytes:forUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBuffer setUncompressedEquivalentCapacity:];
```
