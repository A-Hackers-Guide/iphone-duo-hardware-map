# `BWStillImageFilterNodeResourceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWRendererResourceProvider`
- 43 instance variables, 13 properties, 42 instance methods, 2 class methods

## Instance variables

```
@"BWStillImageFilterNodeConfiguration" _nodeConfiguration;
@"BWNodeInput" _nodeInput;
@"BWNodeOutput" _nodeOutput;
@"<BWRendererResourceProvider>" _rendererProvider;
@"CIContext" _cachedCIContext;
@"<MTLCommandQueue>" _mtlCommandQueue;
@"FigMetalAllocatorBackend" _sharedMetalAllocatorBackend;
@"BWStillImageMetalSDOFRenderer" _metalSDOFRenderer;
@"BWStillImageMetalBlurMapRenderer" _metalBlurMapRenderer;
@"BWMetalColorCubeRenderer" _metalFilterRenderer;
@"BWStillImageCoreImageBlurMapRenderer" _coreImageBlurMapRenderer;
@"BWApplySmartStyleRenderer" _applySmartStyleRenderer;
@"BWLearnSmartStyleRenderer" _learnSmartStyleRenderer;
@"BWSmartStyleReversibilityRenderer" _smartStyleReversibilityRenderer;
@"BWSmartStyleTargetRenderer" _smartStyleTargetRenderer;
@"BWSkinTextureStyleRenderer" _skinTextureStyleRenderer;
@"BWGlobalTextureStyleRenderer" _globalTextureStyleRenderer;
@"BWBaselineTextureStyleRenderer" _baselineTextureStyleRenderer;
@"BWGlowTextureStyleRenderer" _glowTextureStyleRenderer;
@"BWColorLookupCache" _colorLookupCache;
@"NSMutableDictionary" _renderListsByKey;
@"BWRenderListProcessor" _renderListProcessor;
B _renderersPrewarmed;
@"BWPixelBufferPool" _portraitProcessingBufferPool;
@"BWPixelBufferPool" _styleProcessingPixelBufferPool;
@"BWVideoFormat" _blurMapOutputFormat;
{?="width"i"height"i} _maskDimensions;
@"BWVideoFormat" _outputFormat;
@"BWVideoFormat" _outputFormatUsedForStyleConfiguration;
@"BWVideoFormat" _outputFormatUsedForTextureStyleConfiguration;
B _ccPortraitLoaded;
@"NSString" _currentPortType;
f _currentZoomFactorForSDOFRenderingParameters;
@"NSDictionary" _currentSDOFRenderingParameters;
{?="width"i"height"i} _outputDimensions;
{?="width"i"height"i} _depthDataMapDimensions;
B _usesCoreImageDepthFilters;
@"NSObject<OS_dispatch_queue>" _emitQueue;
^{OpaqueVTPixelTransferSession=} _portraitDownsamplingTransferSession;
@"BWSmartStyleRendererConfiguration" _smartStyleRendererConfiguration;
@"BWPhotoEncoderController" _photoEncoderController;
@"CMIExternalMemoryResource" _smartStyleSharedExternalMemoryResource;
B _waitForLastMetalRendererToComplete;
```

## Properties

```
@property (T{?=ii},N,V_depthDataMapDimensions) depthDataMapDimensions;
@property (T@"FigMetalAllocatorBackend",&,N,V_sharedMetalAllocatorBackend) sharedMetalAllocatorBackend;
@property (T@"BWRenderListProcessor",R,N,V_renderListProcessor) renderListProcessor;
@property (T{?=ii},R,N,V_outputDimensions) outputDimensions;
@property (T{?=ii},R,N,V_maskDimensions) maskDimensions;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_emitQueue) emitQueue;
@property (T@"BWPixelBufferPool",R,N,V_portraitProcessingBufferPool) portraitProcessingBufferPool;
@property (T@"BWPixelBufferPool",R,N,V_styleProcessingPixelBufferPool) styleProcessingPixelBufferPool;
@property (T@"BWPhotoEncoderController",&,N,V_photoEncoderController) photoEncoderController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStillImageFilterNodeResourceCoordinator initialize];
+[BWStillImageFilterNodeResourceCoordinator attachedMediaToDownscaleForDownsampledProxy];
```

## Instance methods

```
-[BWStillImageFilterNodeResourceCoordinator releaseResources];
-[BWStillImageFilterNodeResourceCoordinator injectRendererProvider:];
-[BWStillImageFilterNodeResourceCoordinator styleProcessingPixelBufferPool];
-[BWStillImageFilterNodeResourceCoordinator provideSmartStyleReversibilityRenderer];
-[BWStillImageFilterNodeResourceCoordinator photoEncoderController];
-[BWStillImageFilterNodeResourceCoordinator provideSmartStyleTargetRenderer];
-[BWStillImageFilterNodeResourceCoordinator releaseResourcesForLiveReconfiguration];
-[BWStillImageFilterNodeResourceCoordinator provideStillImageCoreImageBlurMapRenderer];
-[BWStillImageFilterNodeResourceCoordinator prepareStylesSharedExternalMemoryResourceForRenderersIfNeeded];
-[BWStillImageFilterNodeResourceCoordinator processRenderListForKey:inputPixelBuffer:inputSampleBuffer:pixelBufferProvider:resultHandler:];
-[BWStillImageFilterNodeResourceCoordinator dealloc];
-[BWStillImageFilterNodeResourceCoordinator provideColorLookupCache];
-[BWStillImageFilterNodeResourceCoordinator outputDimensions];
-[BWStillImageFilterNodeResourceCoordinator provideSkinTextureStyleRenderer];
-[BWStillImageFilterNodeResourceCoordinator ensureTextureStyleIsSetup];
-[BWStillImageFilterNodeResourceCoordinator downsampleImageForSampleBuffer:outputSampleBuffer:dimensions:];
-[BWStillImageFilterNodeResourceCoordinator ensureResourcesWithSharedMetalAllocatorBackend:];
-[BWStillImageFilterNodeResourceCoordinator provideLearnSmartStyleRenderer];
-[BWStillImageFilterNodeResourceCoordinator initWithNodeConfiguration:nodeInput:nodeOutput:];
-[BWStillImageFilterNodeResourceCoordinator depthDataMapDimensions];
-[BWStillImageFilterNodeResourceCoordinator setSharedMetalAllocatorBackend:];
-[BWStillImageFilterNodeResourceCoordinator provideBaselineTextureStyleRenderer];
-[BWStillImageFilterNodeResourceCoordinator prewarmWithSharedMetalAllocatorBackend:];
-[BWStillImageFilterNodeResourceCoordinator emitQueue];
-[BWStillImageFilterNodeResourceCoordinator provideStreamingSDOFFilterRenderer];
-[BWStillImageFilterNodeResourceCoordinator provideStillImageMetalSDOFRenderer];
-[BWStillImageFilterNodeResourceCoordinator portraitProcessingBufferPool];
-[BWStillImageFilterNodeResourceCoordinator setDepthDataMapDimensions:];
-[BWStillImageFilterNodeResourceCoordinator provideGlowTextureStyleRenderer];
-[BWStillImageFilterNodeResourceCoordinator renderListProcessor];
-[BWStillImageFilterNodeResourceCoordinator sharedMetalAllocatorBackend];
-[BWStillImageFilterNodeResourceCoordinator provideCoreImageFilterRenderer];
-[BWStillImageFilterNodeResourceCoordinator prepareRenderListForKey:processedFilters:metadata:settings:inputDimensions:];
-[BWStillImageFilterNodeResourceCoordinator provideApplySmartStyleRenderer];
-[BWStillImageFilterNodeResourceCoordinator ensureSmartStyleIsSetup];
-[BWStillImageFilterNodeResourceCoordinator maskDimensions];
-[BWStillImageFilterNodeResourceCoordinator updateStyleBufferPoolWithDimensions:pixelFormat:constituentPhotoDeviceCount:];
-[BWStillImageFilterNodeResourceCoordinator downsampleAttachedMediaForSampleBuffer:];
-[BWStillImageFilterNodeResourceCoordinator provideMetalFilterRenderer];
-[BWStillImageFilterNodeResourceCoordinator setPhotoEncoderController:];
-[BWStillImageFilterNodeResourceCoordinator provideStillImageMetalBlurMapRenderer];
-[BWStillImageFilterNodeResourceCoordinator provideGlobalTextureStyleRenderer];
```
