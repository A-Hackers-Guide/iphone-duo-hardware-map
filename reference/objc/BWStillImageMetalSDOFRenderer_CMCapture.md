# `BWStillImageMetalSDOFRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 6 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _sdofRenderingTuningParameters;
@"FigSDOFEffectRendering" _sdofEffectRenderer;
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
+[BWStillImageMetalSDOFRenderer initialize];
```

## Instance methods

```
-[BWStillImageMetalSDOFRenderer displayName];
-[BWStillImageMetalSDOFRenderer dealloc];
-[BWStillImageMetalSDOFRenderer type];
-[BWStillImageMetalSDOFRenderer adjustsMetadata];
-[BWStillImageMetalSDOFRenderer adjustMetadataOfSampleBuffer:];
-[BWStillImageMetalSDOFRenderer initWithSDOFRenderingTuningParameters:imageDimensions:depthDataMapDimensions:portraitRenderQuality:metalCommandQueue:];
-[BWStillImageMetalSDOFRenderer isPassThroughRenderer];
-[BWStillImageMetalSDOFRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWStillImageMetalSDOFRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWStillImageMetalSDOFRenderer shouldEnableForegroundBlur];
-[BWStillImageMetalSDOFRenderer supportsAnimation];
```
