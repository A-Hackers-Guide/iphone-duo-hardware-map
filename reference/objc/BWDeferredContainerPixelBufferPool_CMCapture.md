# `BWDeferredContainerPixelBufferPool`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWPixelBufferPool`
- 1 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"BWVideoFormat" _videoFormat;
```

## Properties

```
@property (T@"BWVideoFormat",R,N,V_videoFormat) videoFormat;
@property (T^{__CVPixelBufferPool=},R,N) cvPixelBufferPool;
@property (T^{__CFDictionary=},R,N) cvPixelBufferPoolAuxAttributes;
```

## Class methods

```
+[BWDeferredContainerPixelBufferPool initialize];
```

## Instance methods

```
-[BWDeferredContainerPixelBufferPool videoFormat];
-[BWDeferredContainerPixelBufferPool setCapacity:];
-[BWDeferredContainerPixelBufferPool initWithAttributes:capacity:name:];
-[BWDeferredContainerPixelBufferPool setCVPixelBufferPool:attributes:];
-[BWDeferredContainerPixelBufferPool cvPixelBufferPool];
-[BWDeferredContainerPixelBufferPool flush];
-[BWDeferredContainerPixelBufferPool flushToMinimumCapacity:];
-[BWDeferredContainerPixelBufferPool dealloc];
-[BWDeferredContainerPixelBufferPool enumerateSurfacesUsingBlock:];
-[BWDeferredContainerPixelBufferPool preallocateWithCompletionHandler:];
-[BWDeferredContainerPixelBufferPool newPixelBuffer];
-[BWDeferredContainerPixelBufferPool prefetchWithCompletionHandler:];
-[BWDeferredContainerPixelBufferPool initWithVideoFormat:capacity:name:clientProvidesPool:memoryPool:providesBackPressure:reportSlowBackPressureAllocations:];
-[BWDeferredContainerPixelBufferPool initWithVideoFormat:capacity:name:memoryPool:];
-[BWDeferredContainerPixelBufferPool cvPixelBufferPoolAuxAttributes];
-[BWDeferredContainerPixelBufferPool initWithVideoFormat:capacity:name:memoryPool:additionalPixelBufferAttributes:providesBackPressure:reportSlowBackPressureAllocations:];
-[BWDeferredContainerPixelBufferPool preallocate];
-[BWDeferredContainerPixelBufferPool initWithVideoFormat:capacity:name:];
-[BWDeferredContainerPixelBufferPool flushWithCompletionHandler:];
```
