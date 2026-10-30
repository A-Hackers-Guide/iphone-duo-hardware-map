# `BWVideoDepthNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWInferenceFormatProvider`, `BWInferencePixelBufferPoolProvider`
- 45 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceEngine" _inferenceEngine;
@"BWInferenceEngine" _postProcessingInferenceEngine;
@"BWInferenceScheduler" _inferenceScheduler;
B _skipProcessing;
B _releasesResourcesAtEndOfData;
B _nodePrepared;
@"BWInferenceVideoFormat" _primaryMediaInputFormat;
@"BWInferenceVideoFormat" _disparityInputFormat;
@"NSMutableDictionary" _inferenceVideoFormatsToPrepareByAttachedMediaKeys;
^{opaqueCMFormatDescription=} _depthFormatDescription;
@"BWFigVideoCaptureDevice" _captureDevice;
^{opaqueCMSampleBuffer=} _previousDisparityStateSampleBuffer;
^{opaqueCMSampleBuffer=} _previousFeatureStateSampleBuffer;
^{opaqueCMSampleBuffer=} _disparityPostprocessingInStateSampleBuffer;
^{opaqueCMSampleBuffer=} _disparityPostprocessingOutStateSampleBuffer;
^{__CVBuffer=} _initialDisparityStatePixelBuffer;
^{__CVBuffer=} _initialFeatureStatePixelBuffer;
^{__CVBuffer=} _blankDisparityPixelBuffer;
{?="width"i"height"i} _depthOutputDimensions;
B _videoDepthEnabled;
B _structuredLightIsOccluded;
B _sourceIsNuri;
@"BWVideoFormat" _featuresVideoFormat;
@"BWVideoFormat" _disparityStateVideoFormat;
@"BWVideoFormat" _internalDisparityVideoFormat;
@"BWVideoFormat" _disparityEspressoOutputVideoFormat;
@"BWPixelBufferPool" _internalDisparityPool;
@"BWPixelBufferPool" _disparityEspressoOutputPool;
@"BWPixelBufferPool" _featuresPool;
@"<MTLEvent>" _backpressureEvent;
@"BWVideoDepthInferenceConfiguration" _videoDepthConfiguration;
B _useMonocularInference;
B _networkInputIsRotated;
^{__CVBuffer=} _disparityMultiplierPixelBuffer;
@"BWVideoFormat" _disparityMultiplierFormat;
f _disparityScalingFactor;
@"BWDisparityAPSScaling" _disparityAPSScaling;
{?="value"q"timescale"i"flags"I"epoch"q} _lastTimeStampWhenAPSComputed;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastInferenceCropRect;
f _cropRectScaleFactor;
B _usePrimaryPreviewSourceAttachedMediaForInference;
B _previousAspectRatioIsLandscape;
B _highFrameRateModeEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _lastInferencePTS;
^{__CVBuffer=} _cachedDisparityPixelBuffer;
```

## Properties

```
@property (TB,V_skipProcessing) skipProcessing;
@property (TB,N,V_releasesResourcesAtEndOfData) releasesResourcesAtEndOfData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWVideoDepthNode initialize];
```

## Instance methods

```
-[BWVideoDepthNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoDepthNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWVideoDepthNode renderSampleBuffer:forInput:];
-[BWVideoDepthNode initWithInferenceScheduler:captureDevice:videoDepthConfiguration:extraDepthOutputRetainedBufferCount:highFrameRateModeEnabled:error:];
-[BWVideoDepthNode outputFormatForAttachedMediaKey:];
-[BWVideoDepthNode skipProcessing];
-[BWVideoDepthNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWVideoDepthNode inputVideoFormatForAttachedMediaKey:];
-[BWVideoDepthNode dealloc];
-[BWVideoDepthNode setReleasesResourcesAtEndOfData:];
-[BWVideoDepthNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWVideoDepthNode outputVideoFormatForAttachedMediaKey:];
-[BWVideoDepthNode inputFormatForAttachedMediaKey:];
-[BWVideoDepthNode setSkipProcessing:];
-[BWVideoDepthNode releasesResourcesAtEndOfData];
-[BWVideoDepthNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWVideoDepthNode didReachEndOfDataForConfigurationID:input:];
-[BWVideoDepthNode nodeSubType];
-[BWVideoDepthNode nodeType];
```
