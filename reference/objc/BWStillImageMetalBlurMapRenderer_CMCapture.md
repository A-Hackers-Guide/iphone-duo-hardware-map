# `BWStillImageMetalBlurMapRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 8 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _sdofRenderingTuningParameters;
@"FigSDOFBlurMapRendering" _sdofBlurMapRenderer;
@"BWPixelBufferPool" _blurMapPixelBufferPool;
B _backPressureDrivenPipelining;
i _portraitRenderQuality;
{?="width"i"height"i} _imageDimensions;
{?="width"i"height"i} _depthDataMapDimensions;
@"<MTLCommandQueue>" _mtlCommandQueue;
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
+[BWStillImageMetalBlurMapRenderer initialize];
```

## Instance methods

```
-[BWStillImageMetalBlurMapRenderer displayName];
-[BWStillImageMetalBlurMapRenderer dealloc];
-[BWStillImageMetalBlurMapRenderer type];
-[BWStillImageMetalBlurMapRenderer adjustsMetadata];
-[BWStillImageMetalBlurMapRenderer adjustMetadataOfSampleBuffer:];
-[BWStillImageMetalBlurMapRenderer initWithSDOFRenderingTuningParameters:imageDimensions:depthDataMapDimensions:portraitRenderQuality:metalCommandQueue:backPressureDrivenPipelining:];
-[BWStillImageMetalBlurMapRenderer isPassThroughRenderer];
-[BWStillImageMetalBlurMapRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWStillImageMetalBlurMapRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWStillImageMetalBlurMapRenderer shouldEnableForegroundBlur];
-[BWStillImageMetalBlurMapRenderer supportsAnimation];
```
