# `BWStreamingRaytracingSDOFRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 21 instance variables, 8 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"PTRenderPipeline" _ptRenderPipeline;
@"PTRenderRequest" _ptRenderRequest;
@"<PTRenderState>" _ptRenderState;
B _ptRenderStateIsConfigured;
^{__CVMetalTextureCache=} _textureCache;
@"MTLTextureDescriptor" _textureDescriptorDisparity;
@"<MTLTexture>" _disparityTextureWhileWaitingForCamera;
{?="width"i"height"i} _alignment;
f _networkBias;
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSString" _portTypeProvidingTuningParameters;
@"<MTLCommandQueue>" _commandQueue;
@"PTCinematographyFocusDisparitySampler" _focusDisparitySampler;
B _smartStyleRenderingEnabled;
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
# _smartStyleProcessorInputOutputClass;
# _smartStyleProcessorClass;
Q _smartStyleCoefficientsFilterType;
@"BWPixelBufferPool" _smartStyleCoefficientsPixelBufferPool;
I _smartStyleFilteredCoefficientsPixelBufferPoolSize;
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
+[BWStreamingRaytracingSDOFRenderer initialize];
```

## Instance methods

```
-[BWStreamingRaytracingSDOFRenderer displayName];
-[BWStreamingRaytracingSDOFRenderer dealloc];
-[BWStreamingRaytracingSDOFRenderer type];
-[BWStreamingRaytracingSDOFRenderer adjustsMetadata];
-[BWStreamingRaytracingSDOFRenderer adjustMetadataOfSampleBuffer:];
-[BWStreamingRaytracingSDOFRenderer initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:squareAspectRatioConfigEnabled:computeFocusDisparity:];
-[BWStreamingRaytracingSDOFRenderer isPassThroughRenderer];
-[BWStreamingRaytracingSDOFRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWStreamingRaytracingSDOFRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWStreamingRaytracingSDOFRenderer supportsAnimation];
```
