# `BWPixelBufferPool`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPixelBufferProvider`
- 15 instance variables, 16 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"BWVideoFormat" _videoFormat;
Q _capacity;
@"NSString" _name;
B _clientProvidesPool;
@"NSDictionary" _additionalPixelBufferAttributes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pixelBufferPoolConfigurationLock;
^{__CVPixelBufferPool=} _pixelBufferPool;
@"NSDictionary" _pixelBufferPoolAuxAttributes;
@"NSMutableSet" _prefetchedSurfaceIDs;
i _pixelBufferPoolCreateError;
@"BWMemoryPool" _memoryPool;
B _providesBackPressure;
B _reportSlowBackPressureAllocations;
@"NSObject<OS_dispatch_semaphore>" _backPressureSemaphore;
AQ _backpressureSemaphoreWaitID;
```

## Properties

```
@property (TB,R,N,GisPixelBufferAvailable) pixelBufferAvailable;
@property (TQ,R,N) capacity;
@property (T^{__CVPixelBufferPool=},R,N) cvPixelBufferPool;
@property (T^{__CFDictionary=},R,N) cvPixelBufferPoolAuxAttributes;
@property (T@"BWVideoFormat",R,N) videoFormat;
@property (T@"NSString",R,N) name;
@property (TI,R,N) pixelFormat;
@property (TQ,R,N) width;
@property (TQ,R,N) height;
@property (T{?=ii},R,N) dimensions;
@property (TQ,R,N) sliceCount;
@property (TB,R,N) usesMemoryPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPixelBufferPool initialize];
```

## Instance methods

```
-[BWPixelBufferPool videoFormat];
-[BWPixelBufferPool setCapacity:];
-[BWPixelBufferPool dimensions];
-[BWPixelBufferPool prefetch:lastEmittedSurfaceID:];
-[BWPixelBufferPool enumerateAllSurfacesUsingBlock:];
-[BWPixelBufferPool capacity];
-[BWPixelBufferPool setCVPixelBufferPool:attributes:];
-[BWPixelBufferPool sliceCount];
-[BWPixelBufferPool cvPixelBufferPool];
-[BWPixelBufferPool flushToMinimumCapacity:];
-[BWPixelBufferPool dealloc];
-[BWPixelBufferPool enumerateSurfacesUsingBlock:];
-[BWPixelBufferPool preallocateWithCompletionHandler:];
-[BWPixelBufferPool usesMemoryPool];
-[BWPixelBufferPool newPixelBuffer];
-[BWPixelBufferPool prefetchWithCompletionHandler:];
-[BWPixelBufferPool initWithVideoFormat:capacity:name:clientProvidesPool:memoryPool:providesBackPressure:reportSlowBackPressureAllocations:];
-[BWPixelBufferPool initWithVideoFormat:capacity:name:memoryPool:];
-[BWPixelBufferPool description];
-[BWPixelBufferPool cvPixelBufferPoolAuxAttributes];
-[BWPixelBufferPool initWithVideoFormat:capacity:name:memoryPool:additionalPixelBufferAttributes:providesBackPressure:reportSlowBackPressureAllocations:];
-[BWPixelBufferPool pixelFormat];
-[BWPixelBufferPool preallocate];
-[BWPixelBufferPool width];
-[BWPixelBufferPool initWithVideoFormat:capacity:name:];
-[BWPixelBufferPool name];
-[BWPixelBufferPool height];
-[BWPixelBufferPool isPixelBufferAvailable];
-[BWPixelBufferPool waitForAvailablePixelBuffer];
```
