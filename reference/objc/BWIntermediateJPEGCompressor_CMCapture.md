# `BWIntermediateJPEGCompressor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSObject<OS_dispatch_semaphore>" _backPressureSemaphore;
Q _compressedBufferSize;
Q _compressedBufferPoolAllocationTimeoutMS;
f _compressionQuality;
f _compressionRate;
i _numberOfTimesWaitedOnBackPressureSemaphore;
i _jpegSurfacePoolLowWaterBufferCount;
i _jpegSurfacePoolHighWaterBufferCount;
B _setupIsComplete;
^{CMPhotoSurfacePool=} _surfacePool;
^{CMPhotoCompressionSession=} _compressionSession;
^{__CFDictionary=} _containerOptions;
@"NSMutableDictionary" _qualityControllerParameters;
^{__CFDictionary=} _compressionOptions;
^{opaqueCMFormatDescription=} _jpegFormatDescription;
@"BWStats" _overallWaitStats;
@"BWMovingWindowStats" _recentWaitStats;
```

## Class methods

```
+[BWIntermediateJPEGCompressor initialize];
```

## Instance methods

```
-[BWIntermediateJPEGCompressor flush];
-[BWIntermediateJPEGCompressor dealloc];
-[BWIntermediateJPEGCompressor initWithCompressionQuality:compressionRate:jpegSurfacePoolLowWaterBufferCount:jpegSurfacePoolHighWaterBufferCount:compressedBufferPoolAllocationTimeoutMS:name:];
-[BWIntermediateJPEGCompressor newJPEGSampleBufferFromUncompressedSampleBuffer:];
-[BWIntermediateJPEGCompressor prepareForVideoFormat:];
```
