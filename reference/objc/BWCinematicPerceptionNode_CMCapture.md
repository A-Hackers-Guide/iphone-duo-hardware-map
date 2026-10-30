# `BWCinematicPerceptionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceNode`
- Protocols: `BWInferencePixelBufferPoolProvider`
- 22 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _framesSinceLastDDR;
@"FTCinematicTracker" _cinematicTracker;
@"BWVideoDepthInferenceConfiguration" _videoDepthConfiguration;
@"NSObject<OS_dispatch_semaphore>" _backpressureSemaphore;
@"<MTLEvent>" _backpressureEvent;
Q _backpressureEventNumber;
@"NSSet" _humanPosePreventionSet;
^{opaqueCMFormatDescription=} _depthFormatDescription;
@"BWVideoFormat" _disparityFeaturesVideoFormat;
@"BWVideoFormat" _colorFeaturesVideoFormat;
@"BWPixelBufferPool" _disparityFeaturesPool;
@"BWPixelBufferPool" _colorFeaturesPool;
^{opaqueCMSampleBuffer=} _previousDisparityFeaturesSampleBuffer;
^{opaqueCMSampleBuffer=} _previousColorFeaturesSampleBuffer;
^{__CVBuffer=} _initialDisparityFeaturesPixelBuffer;
^{__CVBuffer=} _initialColorFeaturesPixelBuffer;
^{__CVBuffer=} _currentFeaturesMinPixelBuffer;
^{__CVBuffer=} _previousFeaturesMinPixelBuffer;
^{opaqueCMSampleBuffer=} _currentFeaturesMinSampleBuffer;
^{opaqueCMSampleBuffer=} _previousFeaturesMinSampleBuffer;
B _depthInferenceEnabled;
B _opticalFlowInferenceEnabled;
```

## Properties

```
@property (T@"BWVideoDepthInferenceConfiguration",R,N,V_videoDepthConfiguration) videoDepthConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCinematicPerceptionNode initialize];
```

## Instance methods

```
-[BWCinematicPerceptionNode prepareForCurrentConfigurationToBecomeLive];
-[BWCinematicPerceptionNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWCinematicPerceptionNode willEmitSampleBufferAlways:];
-[BWCinematicPerceptionNode renderSampleBuffer:forInput:];
-[BWCinematicPerceptionNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWCinematicPerceptionNode inputVideoFormatForAttachedMediaKey:];
-[BWCinematicPerceptionNode dealloc];
-[BWCinematicPerceptionNode videoDepthConfiguration];
-[BWCinematicPerceptionNode initWithConvEngineSupportWithCaptureDevice:scheduler:priority:depthInferenceEnabled:aspectRatio:opticalFlowInferenceEnabled:];
-[BWCinematicPerceptionNode handleDroppedSample:forInput:];
-[BWCinematicPerceptionNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWCinematicPerceptionNode nodeSubType];
-[BWCinematicPerceptionNode nodeType];
```
