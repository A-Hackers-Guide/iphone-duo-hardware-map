# `BWOnDemandPixelBufferAllocator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPixelBufferProvider`
- 4 instance variables, 11 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"BWVideoFormat" _videoFormat;
@"NSString" _name;
@"NSDictionary" _pixelBufferAttributes;
@"BWMemoryPool" _memoryPool;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
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
+[BWOnDemandPixelBufferAllocator initialize];
+[BWOnDemandPixelBufferAllocator onDemandAllocatorWithDimensions:dimensionAlignment:pixelFormat:name:memoryPool:];
+[BWOnDemandPixelBufferAllocator onDemandAllocatorWithDimensions:pixelFormat:name:memoryPool:];
+[BWOnDemandPixelBufferAllocator onDemandAllocatorWithoutMemoryPoolWithDimensions:dimensionAlignment:pixelFormat:name:];
```

## Instance methods

```
-[BWOnDemandPixelBufferAllocator dimensions];
-[BWOnDemandPixelBufferAllocator sliceCount];
-[BWOnDemandPixelBufferAllocator flushToMinimumCapacity:];
-[BWOnDemandPixelBufferAllocator dealloc];
-[BWOnDemandPixelBufferAllocator usesMemoryPool];
-[BWOnDemandPixelBufferAllocator newPixelBuffer];
-[BWOnDemandPixelBufferAllocator description];
-[BWOnDemandPixelBufferAllocator pixelFormat];
-[BWOnDemandPixelBufferAllocator width];
-[BWOnDemandPixelBufferAllocator name];
-[BWOnDemandPixelBufferAllocator height];
-[BWOnDemandPixelBufferAllocator initWithVideoFormat:name:memoryPool:additionalPixelBufferAttributes:];
-[BWOnDemandPixelBufferAllocator initWithoutMemoryPoolWithVideoFormat:name:additionalPixelBufferAttributes:];
```
