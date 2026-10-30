# `BWPhotoDecompressor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
i _poolSize;
I _outputPixelFormat;
@"BWPixelBufferPool" _outputPixelBufferPool;
i _outputLargestDimension;
B _decompressionSetupIsComplete;
^{__CVBuffer=} _decompressionPixelBufferPool;
^{CMPhotoSurfacePool=} _decompressionSurfacePool;
^{CMPhotoDecompressionSession=} _decompressionSession;
@"NSMutableDictionary" _decompressionOptions;
^{opaqueCMFormatDescription=} _uncompressedFormatDescription;
B _forceAllocationsFromFigSurfacePool;
B _preserveBorderRows;
```

## Properties

```
@property (TB,N,V_preserveBorderRows) preserveBorderRows;
@property (T@"BWPixelBufferPool",R) outputPixelBufferPool;
```

## Instance methods

```
-[BWPhotoDecompressor flush];
-[BWPhotoDecompressor outputPixelBufferPool];
-[BWPhotoDecompressor dealloc];
-[BWPhotoDecompressor initWithOutputPixelBufferPool:];
-[BWPhotoDecompressor initWithPoolSize:outputPixelFormat:outputLargestDimension:];
-[BWPhotoDecompressor newUncompressedPixelBufferFromSampleBuffer:];
-[BWPhotoDecompressor newUncompressedSampleBufferFromSampleBuffer:];
-[BWPhotoDecompressor preserveBorderRows];
-[BWPhotoDecompressor setPreserveBorderRows:];
```
