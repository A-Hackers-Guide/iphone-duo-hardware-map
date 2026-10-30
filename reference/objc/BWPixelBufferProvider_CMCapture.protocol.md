# `BWPixelBufferProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) name;
@property (TI,R,N) pixelFormat;
@property (TQ,R,N) width;
@property (TQ,R,N) height;
@property (T{?=ii},R,N) dimensions;
@property (TQ,R,N) sliceCount;
@property (TB,R,N) usesMemoryPool;
```

## Instance methods

```
-[BWPixelBufferProvider dimensions];
-[BWPixelBufferProvider sliceCount];
-[BWPixelBufferProvider flushToMinimumCapacity:];
-[BWPixelBufferProvider usesMemoryPool];
-[BWPixelBufferProvider newPixelBuffer];
-[BWPixelBufferProvider pixelFormat];
-[BWPixelBufferProvider width];
-[BWPixelBufferProvider name];
-[BWPixelBufferProvider height];
```
