# `BWStreamingFilterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWCinematicVideoDisparityProvider`, `BWRendererResourceProvider`, `BWDetectedFacesFilterDelegate`, `BWSemanticStyleSceneObserver`, `BWFigVideoCaptureDeviceStreamingFilterDelegate`
- 84 instance variables, 30 properties, 75 instance methods, 1 class methods

## Instance variables

```
B _preparedToBecomeLive;
B _streamingSegmentationFromInferenceEngine;
B _depthDataDeliveryEnabled;
B _focusBlurMapDeliveryEnabled;
B _depthFromMonocularNetworkEnabled;
B _portraitAutoSuggestEnabled;
B _metadataProcessingEnabled;
B _attachesInputPixelBufferAfterRendering;
B _studioAndContourRenderingEnabled;
B _stageRenderingEnabled;
B _cinematicVideoEnabled;
B _computeFocusDisparity;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _latestCinematicDisparityLock;
^{__CVBuffer=} _latestCinematicDisparityBuffer;
B _applyStyleBackgroundToEntireFrame;
B _haveSeenFirstSampleBuffer;
B _primaryStreamingPersonSegmentationEnabled;
B _secondaryStreamingPersonSegmentationEnabled;
B _depthFilterRenderingIsAfterPreviewStitcher;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _renderListLock;
@"BWRenderList" _currentRenderList;
@"BWRenderListAnimator" _currentAnimator;
@"BWRenderList" _nextRenderList;
@"BWRenderList" _mostRecentRenderListRequested;
@"BWRenderListAnimator" _nextAnimator;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _filterChangeLock;
@"NSArray" _filters;
@"BWMetalColorCubeRenderer" _metalFilterRenderer;
B _semanticStyleRenderingEnabled;
@"FigCaptureSemanticStyle" _semanticStyle;
B _semanticStyleRenderingSuspended;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _semanticStyleSceneLock;
i _semanticStyleSceneType;
@"BWFencedAnimationQueue" _fencedAnimationQueue;
B _multipleSemanticStylesEnabled;
^{opaqueCMSampleBuffer=} _lastSampleBuffer;
{?="value"q"timescale"i"flags"I"epoch"q} _lastRenderedPTS;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lastSampleBufferLock;
B _renderingSemanticStyleSet;
@"NSArray" _semanticStyleFiltersAndRegionArray;
@"FigCaptureSemanticStyleSet" _currentSemanticStyleSet;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _primaryCaptureRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fullScreenRectangle;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _semanticStyleSetLock;
@"BWSemanticStyleColorCubeCache" _colorCubeCache;
f _pickerComparisonMaxCubeStrength;
B _maskVisualizationEnabled;
@"BWStreamingCVAFilterRenderer" _streamingCVAFilterRenderer;
f _simulatedAperture;
f _portraitLightingEffectStrength;
B _mirroredForMetadataAdjustment;
i _rotationDegreesForMetadataAdjustment;
@"BWStreamingRaytracingSDOFRenderer" _streamingRaytracingSDOFRenderer;
@"BWRenderListProcessor" _renderListProcessor;
@"<BWPixelBufferProvider>" _pixelBufferProvider;
@"BWColorLookupCache" _colorLookupCache;
@"NSObject<OS_dispatch_queue>" _processorPreparationQueue;
@"BWFigVideoCaptureDevice" _captureDevice;
B _receivedInitialFixedPointDisparityBuffer;
B _receivedOccludedFixedPointDisparityBuffer;
B _mixColorCubesInGammaDomain;
B _portraitPreviewForegroundBlurEnabled;
@"<MTLCommandQueue>" _metalCommandQueue;
I _priority;
I _receivedFrameCounter;
I _perFrameLoggingRatio;
B _shouldLogPerFrameLogging;
B _smartStyleRenderingEnabled;
B _squareAspectRatioConfigEnabled;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"BWNodeInput" _videoInput;
@"NSDictionary" _stillImageInputsByPortType;
@"NSDictionary" _stillImageOutputsByPortType;
B _stillImageCaptureEnabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stillCaptureLock;
[2{?="pixelBuffer"^{__CVBuffer}"pts"{?="value"q"timescale"i"flags"I"epoch"q}}] _stillCaptureQueue;
I _stillCaptureEnqueueIndex;
i _maxLossyCompressionLevel;
^{OpaqueVTPixelTransferSession=} _stillImagePixelTransferSession;
@"NSObject<OS_dispatch_queue>" _videoOutputEventMessagesEmitQueue;
B _cropDepthToPrimaryCaptureAspectRatio;
B _disableDepthAndSegmentationRotationInLandscape;
@"NSObject<OS_dispatch_semaphore>" _previewFilterBackpressureSemaphore;
{?="width"i"height"i} _outputDimensions;
```

## Properties

```
@property (TB,N,GisStreamingSegmentationFromInferenceEngine) streamingSegmentationFromInferenceEngine;
@property (TB,N,GisDepthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N,GisFocusBlurMapDeliveryEnabled) focusBlurMapDeliveryEnabled;
@property (TB,N,GisDepthFromMonocularNetworkEnabled) depthFromMonocularNetworkEnabled;
@property (TB,N,GisPortraitAutoSuggestEnabled) portraitAutoSuggestEnabled;
@property (TB,N,GisMetadataProcessingEnabled) metadataProcessingEnabled;
@property (TB,N) attachesInputPixelBufferAfterRendering;
@property (TB,N) studioAndContourRenderingEnabled;
@property (TB,N) stageRenderingEnabled;
@property (TB,N) primaryStreamingPersonSegmentationEnabled;
@property (TB,N) secondaryStreamingPersonSegmentationEnabled;
@property (T@"NSDictionary",R,N) stillImageInputsByPortType;
@property (T@"NSDictionary",R,N) stillImageOutputsByPortType;
@property (T@"NSObject<OS_dispatch_semaphore>",N) previewFilterBackpressureSemaphore;
@property (T{?=ii},N) outputDimensions;
@property (T@"NSArray",R,&,N) filters;
@property (TB,R,N,GisSemanticStyleRenderingEnabled) semanticStyleRenderingEnabled;
@property (TB,R,N,GisRenderingSemanticStyle) renderingSemanticStyle;
@property (T@"FigCaptureSemanticStyle",R,&,N) semanticStyle;
@property (TB,R,N,GisSemanticStyleRenderingSuspended) semanticStyleRenderingSuspended;
@property (Ti,R,N) semanticStyleSceneType;
@property (TB,R,N,GisRenderingSemanticStyleSet,V_renderingSemanticStyleSet) renderingSemanticStyleSet;
@property (Tf) simulatedAperture;
@property (Tf) portraitLightingEffectStrength;
@property (T@"BWColorLookupCache",R) colorLookupCache;
@property (TB,R,N) providesCinematicDisparity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStreamingFilterNode initialize];
```

## Instance methods

```
-[BWStreamingFilterNode prepareForCurrentConfigurationToBecomeLive];
-[BWStreamingFilterNode semanticStyleSceneTypeDidChange:];
-[BWStreamingFilterNode semanticStyleSceneType];
-[BWStreamingFilterNode isPortraitAutoSuggestEnabled];
-[BWStreamingFilterNode renderSampleBuffer:forInput:];
-[BWStreamingFilterNode setAttachesInputPixelBufferAfterRendering:];
-[BWStreamingFilterNode provideSmartStyleReversibilityRenderer];
-[BWStreamingFilterNode stageRenderingEnabled];
-[BWStreamingFilterNode portraitLightingEffectStrength];
-[BWStreamingFilterNode isMetadataProcessingEnabled];
-[BWStreamingFilterNode setOutputDimensions:];
-[BWStreamingFilterNode setDepthFromMonocularNetworkEnabled:];
-[BWStreamingFilterNode isFocusBlurMapDeliveryEnabled];
-[BWStreamingFilterNode provideSmartStyleTargetRenderer];
-[BWStreamingFilterNode provideStillImageCoreImageBlurMapRenderer];
-[BWStreamingFilterNode stillImageOutputsByPortType];
-[BWStreamingFilterNode setMetadataProcessingEnabled:];
-[BWStreamingFilterNode setStageRenderingEnabled:];
-[BWStreamingFilterNode dealloc];
-[BWStreamingFilterNode isDepthFromMonocularNetworkEnabled];
-[BWStreamingFilterNode prepareForRenderingWithPreparedPixelBufferPool];
-[BWStreamingFilterNode provideColorLookupCache];
-[BWStreamingFilterNode outputDimensions];
-[BWStreamingFilterNode provideSkinTextureStyleRenderer];
-[BWStreamingFilterNode filters];
-[BWStreamingFilterNode stillImageInputsByPortType];
-[BWStreamingFilterNode setSimulatedAperture:];
-[BWStreamingFilterNode setSemanticStyleSet:fencePortSendRight:];
-[BWStreamingFilterNode setStreamingSegmentationFromInferenceEngine:];
-[BWStreamingFilterNode setSecondaryStreamingPersonSegmentationEnabled:];
-[BWStreamingFilterNode setFocusBlurMapDeliveryEnabled:];
-[BWStreamingFilterNode provideLearnSmartStyleRenderer];
-[BWStreamingFilterNode isSemanticStyleRenderingEnabled];
-[BWStreamingFilterNode provideBaselineTextureStyleRenderer];
-[BWStreamingFilterNode isDepthDataDeliveryEnabled];
-[BWStreamingFilterNode initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:computeFocusDisparity:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:squareAspectRatioConfigEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:];
-[BWStreamingFilterNode setPreviewFilterBackpressureSemaphore:];
-[BWStreamingFilterNode changeToSemanticStyle:animated:];
-[BWStreamingFilterNode semanticStyle];
-[BWStreamingFilterNode attachesInputPixelBufferAfterRendering];
-[BWStreamingFilterNode provideStreamingSDOFFilterRenderer];
-[BWStreamingFilterNode isRenderingSemanticStyle];
-[BWStreamingFilterNode latestCinematicDisparityBuffer];
-[BWStreamingFilterNode handleDroppedSample:forInput:];
-[BWStreamingFilterNode provideStillImageMetalSDOFRenderer];
-[BWStreamingFilterNode previewFilterBackpressureSemaphore];
-[BWStreamingFilterNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStreamingFilterNode secondaryStreamingPersonSegmentationEnabled];
-[BWStreamingFilterNode primaryStreamingPersonSegmentationEnabled];
-[BWStreamingFilterNode didReachEndOfDataForConfigurationID:input:];
-[BWStreamingFilterNode provideGlowTextureStyleRenderer];
-[BWStreamingFilterNode changeToFilters:semanticStyle:animated:];
-[BWStreamingFilterNode setPrimaryStreamingPersonSegmentationEnabled:];
-[BWStreamingFilterNode filterDetectedFacesInSampleBuffer:];
-[BWStreamingFilterNode setPortraitLightingEffectStrength:];
-[BWStreamingFilterNode setDepthDataDeliveryEnabled:];
-[BWStreamingFilterNode provideCoreImageFilterRenderer];
-[BWStreamingFilterNode setStudioAndContourRenderingEnabled:];
-[BWStreamingFilterNode simulatedAperture];
-[BWStreamingFilterNode provideApplySmartStyleRenderer];
-[BWStreamingFilterNode isRenderingSemanticStyleSet];
-[BWStreamingFilterNode nodeSubType];
-[BWStreamingFilterNode setSemanticStyleRenderingSuspended:animated:];
-[BWStreamingFilterNode colorLookupCache];
-[BWStreamingFilterNode studioAndContourRenderingEnabled];
-[BWStreamingFilterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStreamingFilterNode provideMetalFilterRenderer];
-[BWStreamingFilterNode provideStillImageMetalBlurMapRenderer];
-[BWStreamingFilterNode setPortraitAutoSuggestEnabled:];
-[BWStreamingFilterNode providesCinematicDisparity];
-[BWStreamingFilterNode provideGlobalTextureStyleRenderer];
-[BWStreamingFilterNode nodeType];
-[BWStreamingFilterNode isStreamingSegmentationFromInferenceEngine];
-[BWStreamingFilterNode changeToFilters:animated:];
-[BWStreamingFilterNode isSemanticStyleRenderingSuspended];
```
