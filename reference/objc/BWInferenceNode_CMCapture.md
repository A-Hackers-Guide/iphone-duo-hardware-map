# `BWInferenceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWInferencePixelBufferPoolProvider`, `BWInferenceFormatProvider`
- 19 instance variables, 15 properties, 47 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceScheduler" _inferenceScheduler;
I _priority;
@"BWInferenceEngine" _inferenceEngine;
B _inferenceEnginePrepared;
@"NSSet" _inferenceTypesToSkip;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _inferenceTypesToSkipLock;
AB _tearDown;
@"BWFigVideoCaptureDevice" _captureDevice;
B _awaitAsynchronousOutputs;
B _applyRecommendedMasterPortType;
@"NSString" _recommendedMasterPortType;
B _passthroughInputSampleBuffer;
B _ignoreInvalidContentInformationForPrimaryMedia;
i _additionalOutputPoolRetainedBufferCount;
B _backPressureDrivenPipelining;
i _endOfDataBehavior;
{?="width"i"height"i} _maxInputDimensions;
@? _inferenceTypesToSkipResolver;
@? _postprocessFilter;
```

## Properties

```
@property (T@"BWInferenceEngine",R,N,V_inferenceEngine) inferenceEngine;
@property (TB,N) awaitAsynchronousOutputs;
@property (TB,N) applyRecommendedMasterPortType;
@property (TB,N,V_passthroughInputSampleBuffer) passthroughInputSampleBuffer;
@property (TB,N,V_ignoreInvalidContentInformationForPrimaryMedia) ignoreInvalidContentInformationForPrimaryMedia;
@property (Ti,N,V_additionalOutputPoolRetainedBufferCount) additionalOutputPoolRetainedBufferCount;
@property (TB,N,V_backPressureDrivenPipelining) backPressureDrivenPipelining;
@property (Ti,N,V_endOfDataBehavior) endOfDataBehavior;
@property (T{?=ii},N,V_maxInputDimensions) maxInputDimensions;
@property (T@?,C,N,V_inferenceTypesToSkipResolver) inferenceTypesToSkipResolver;
@property (T@?,C,N,V_postprocessFilter) postprocessFilter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceNode initialize];
```

## Instance methods

```
-[BWInferenceNode prepareForCurrentConfigurationToBecomeLive];
-[BWInferenceNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWInferenceNode backPressureDrivenPipelining];
-[BWInferenceNode willEmitSampleBufferAlways:];
-[BWInferenceNode initWithScheduler:priority:];
-[BWInferenceNode renderSampleBuffer:forInput:];
-[BWInferenceNode setBackPressureDrivenPipelining:];
-[BWInferenceNode ignoreInvalidContentInformationForPrimaryMedia];
-[BWInferenceNode postprocessFilter];
-[BWInferenceNode outputFormatForAttachedMediaKey:];
-[BWInferenceNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWInferenceNode inferenceEngine];
-[BWInferenceNode applyRecommendedMasterPortType];
-[BWInferenceNode inputVideoFormatForAttachedMediaKey:];
-[BWInferenceNode additionalOutputPoolRetainedBufferCount];
-[BWInferenceNode dealloc];
-[BWInferenceNode endOfDataBehavior];
-[BWInferenceNode setIgnoreInvalidContentInformationForPrimaryMedia:];
-[BWInferenceNode setPostprocessFilter:];
-[BWInferenceNode setInferenceTypesToSkipResolver:];
-[BWInferenceNode setEndOfDataBehavior:];
-[BWInferenceNode addInferenceOfType:version:configuration:];
-[BWInferenceNode setAwaitAsynchronousOutputs:];
-[BWInferenceNode hasNonLiveConfigurationChanges];
-[BWInferenceNode setPassthroughInputSampleBuffer:];
-[BWInferenceNode setMaxInputDimensions:];
-[BWInferenceNode awaitAsynchronousOutputs];
-[BWInferenceNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWInferenceNode outputVideoFormatForAttachedMediaKey:];
-[BWInferenceNode setAdditionalOutputPoolRetainedBufferCount:];
-[BWInferenceNode initWithConvEngineSupportWithCaptureDevice:scheduler:priority:];
-[BWInferenceNode addInferenceOfType:version:];
-[BWInferenceNode inputFormatForAttachedMediaKey:];
-[BWInferenceNode maxInputDimensions];
-[BWInferenceNode initWithScheduler:priority:processingConfiguration:name:];
-[BWInferenceNode inferenceTypesToSkipResolver];
-[BWInferenceNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWInferenceNode didReachEndOfDataForConfigurationID:input:];
-[BWInferenceNode description];
-[BWInferenceNode setInferencesToSkip:];
-[BWInferenceNode passthroughInputSampleBuffer];
-[BWInferenceNode nodeSubType];
-[BWInferenceNode willEmitSampleBuffer:];
-[BWInferenceNode tearDownInferenceEngine];
-[BWInferenceNode initWithConvEngineSupportWithCaptureDevice:scheduler:priority:processingConfiguration:];
-[BWInferenceNode nodeType];
-[BWInferenceNode setApplyRecommendedMasterPortType:];
```
