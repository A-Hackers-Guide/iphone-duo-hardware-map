# `BWStreamingCVAFilterRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 35 instance variables, 12 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _sharedContextQueue;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
{?="depthFilterEnabled"B"mostRecentPostprocessedDisparityBuffer"^{__CVBuffer}"mostRecentFocusDisparity"f"mostRecentDeltaDisparity"f"mostRecentPortraitStability"f"numberOfFramesSinceLastStableFocus"i"clientSuppliedSimulatedAperture"f"clientSuppliedPortraitLightingEffectStrength"f"mostRecentStructuredLightOcclusion"B"previousPortraitRequestFellbackToNonDepthRendering"B"mostRecentDetectedFaces"@"NSArray""previousPortraitRequest"@"<CVAPortraitGenericRequest>""previousStagePreviewStatus"i} _sharedContext;
@"<CVAPortraitVideoPipeline>" _portraitVideoPipeline;
@"BWPixelBufferPool" _postprocessedDisparityBufferPool;
^{__CVBuffer=} _mattingBuffer;
I _requiredDisparityFormat;
^{__CVBuffer=} _previousForegroundSegmentationPixelBuffer;
^{__CVBuffer=} _previousSkinSegmentationPixelBuffer;
^{__CVBuffer=} _previousDisparityPixelBuffer;
Q _configuredColorBufferWidth;
Q _configuredColorBufferHeight;
i _depthDataSource;
@"BWFigVideoCaptureDevice" _captureDevice;
@"<MTLCommandQueue>" _commandQueue;
B _studioAndContourRenderingEnabled;
B _stageRenderingEnabled;
@"BWSpringSimulation" _stageProxyLiveRenderingSpringSimulation;
@"BWStreamingCVAFilterRendererAnimator" _animator;
@"NSMutableDictionary" _objectVisibilityByID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _objectVisibilityByIDLock;
@"NSMutableArray" _postprocessedFaces;
B _foregroundBlurEnabled;
B _hasSeenDepth;
i _maxFramesWithoutDepth;
i _unexpectedFramesWithoutDepth;
B _hasSeenSegmentation;
i _maxFramesWithoutSegmentation;
i _unexpectedFramesWithoutSegmentation;
B _mirroredForMetadataAdjustment;
i _rotationDegreesForMetadataAdjustment;
B _secondaryStreamingPersonSegmentationEnabled;
B _depthFilterRenderingIsAfterPreviewStitcher;
B _cropDepthToPrimaryCaptureAspectRatio;
B _disableDepthAndSegmentationRotationInLandscape;
```

## Properties

```
@property (TB,R,N,V_studioAndContourRenderingEnabled) studioAndContourRenderingEnabled;
@property (TB,R,N,V_stageRenderingEnabled) stageRenderingEnabled;
@property (Tf) simulatedAperture;
@property (Tf) portraitLightingEffectStrength;
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
+[BWStreamingCVAFilterRenderer initialize];
```

## Instance methods

```
-[BWStreamingCVAFilterRenderer stageRenderingEnabled];
-[BWStreamingCVAFilterRenderer portraitLightingEffectStrength];
-[BWStreamingCVAFilterRenderer displayName];
-[BWStreamingCVAFilterRenderer dealloc];
-[BWStreamingCVAFilterRenderer setSimulatedAperture:];
-[BWStreamingCVAFilterRenderer type];
-[BWStreamingCVAFilterRenderer setPortraitLightingEffectStrength:];
-[BWStreamingCVAFilterRenderer simulatedAperture];
-[BWStreamingCVAFilterRenderer studioAndContourRenderingEnabled];
-[BWStreamingCVAFilterRenderer adjustsMetadata];
-[BWStreamingCVAFilterRenderer adjustMetadataOfSampleBuffer:];
-[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:];
-[BWStreamingCVAFilterRenderer isPassThroughRenderer];
-[BWStreamingCVAFilterRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWStreamingCVAFilterRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWStreamingCVAFilterRenderer supportsAnimation];
```
