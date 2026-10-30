# `BWStillImageCoreImageBlurMapRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 6 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"CIContext" _ciContext;
@"CIFilter" _blurMapFilter;
B _hairnetEnabled;
@"BWPixelBufferPool" _blurMapPixelBufferPool;
^{opaqueCMFormatDescription=} _blurredGainMapFormatDescription;
@"BWPixelBufferPool" _blurredGainMapPixelBufferPool;
```

## Properties

```
@property (T@"NSString",R,C,N) displayName;
@property (Ts,R,N) type;
@property (TB,R,N) supportsAnimation;
@property (TB,R,N) adjustsMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStillImageCoreImageBlurMapRenderer initialize];
```

## Instance methods

```
-[BWStillImageCoreImageBlurMapRenderer displayName];
-[BWStillImageCoreImageBlurMapRenderer dealloc];
-[BWStillImageCoreImageBlurMapRenderer type];
-[BWStillImageCoreImageBlurMapRenderer adjustsMetadata];
-[BWStillImageCoreImageBlurMapRenderer _allocateBlurredGainMapPixleBufferPoolForBuffersOfWidth:height:];
-[BWStillImageCoreImageBlurMapRenderer _allocateBlurMapPixelBufferPoolWithDimensions:];
-[BWStillImageCoreImageBlurMapRenderer adjustMetadataOfSampleBuffer:];
-[BWStillImageCoreImageBlurMapRenderer initForRenderingWithContext:hairnetEnabled:];
-[BWStillImageCoreImageBlurMapRenderer isPassThroughRenderer];
-[BWStillImageCoreImageBlurMapRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWStillImageCoreImageBlurMapRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWStillImageCoreImageBlurMapRenderer supportsAnimation];
```
