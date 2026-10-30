# `FigCapturePixelConverter`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{OpaqueVTPixelTransferSession=} _transferSession;
@"BWPixelBufferPool" _pool;
@"BWVideoFormat" _outputFormat;
^{opaqueCMFormatDescription=} _outputFormatDescription;
i _poolCapacity;
B _prefetchPool;
```

## Properties

```
@property (T@"BWVideoFormat",R,N,V_outputFormat) outputFormat;
```

## Class methods

```
+[FigCapturePixelConverter initialize];
```

## Instance methods

```
-[FigCapturePixelConverter init];
-[FigCapturePixelConverter dealloc];
-[FigCapturePixelConverter outputFormat];
-[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:];
-[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:];
-[FigCapturePixelConverter initWithPrefetchPool:];
-[FigCapturePixelConverter updateOutputPixelFormat:dimensions:poolCapacity:colorSpaceProperties:];
```
