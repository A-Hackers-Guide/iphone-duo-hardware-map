# `BWInferenceEngine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceResourceProvider`
- 25 instance variables, 12 properties, 33 instance methods, 3 class methods

## Instance variables

```
@"NSString" _name;
@"NSMutableArray" _inferences;
@"NSMutableArray" _inferencesDeferredUntilFormatResolution;
@"NSMutableArray" _inferencePostProcessors;
@"BWInferenceScheduler" _scheduler;
I _priority;
@"BWInferenceEngineConfiguration" _engineConfiguration;
@"BWInferenceEngineConfiguration" _engineConfigurationForReconfiguration;
@"BWInferenceProcessingConfiguration" _processingConfiguration;
@"BWEspressoInferenceAdapter" _espressoAdapter;
@"BWTiledEspressoInferenceAdapter" _tiledEspressoAdapter;
@"BWTiledInferenceAdapter" _tiledInferenceAdapter;
@"BWEspressoInferenceContext" _cpuContext;
@"BWEspressoInferenceContext" _gpuContext;
@"BWEspressoInferenceContext" _aneContext;
@"BWMetalInferenceContext" _defaultDeviceMetalContext;
@"BWVisionInferenceAdapter" _visionAdapter;
@"BWVisionInferenceContext" _visionContext;
@"BWVideoDepthInferenceAdapter" _videoDepthAdapter;
@"BWFusionTrackerInferenceAdapter" _fusionTrackerAdapter;
@"BWVideoProcessingInferenceAdapter" _videoProcessingAdapter;
@"BWMattingInferenceAdapter" _mattingAdapter;
B _backPressureDrivenPipelining;
B _requiresDeviceOrientationMetadata;
@"NSString" _preparedWorkloadDescription;
```

## Properties

```
@property (T@"NSArray",R,N) inferenceTypes;
@property (T@"NSString",R,N,V_preparedWorkloadDescription) preparedWorkloadDescription;
@property (T@"NSString",C,N,V_name) name;
@property (TB,N,V_backPressureDrivenPipelining) backPressureDrivenPipelining;
@property (T@"NSDictionary",R,C,N) providedVideoRequirementsByAttachedMediaKey;
@property (TB,R,N,V_requiresDeviceOrientationMetadata) requiresDeviceOrientationMetadata;
@property (TB,R,N,GisConfiguredForInference) configuredForInference;
@property (T@"NSArray",R,C,N) postProcessors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceEngine initialize];
+[BWInferenceEngine isNeuralEngineSupported];
+[BWInferenceEngine allowedBufferCompressionDirectionForExecutionTarget:];
```

## Instance methods

```
-[BWInferenceEngine backPressureDrivenPipelining];
-[BWInferenceEngine initWithScheduler:priority:shareIntermediateBuffer:processingConfiguration:name:];
-[BWInferenceEngine initWithScheduler:priority:];
-[BWInferenceEngine setBackPressureDrivenPipelining:];
-[BWInferenceEngine performInferencesOnSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:];
-[BWInferenceEngine prewarmInferencesUsingLimitedMemory:];
-[BWInferenceEngine postProcessors];
-[BWInferenceEngine dealloc];
-[BWInferenceEngine providedVideoRequirementsByAttachedMediaKey];
-[BWInferenceEngine visionContextForExecutionTarget:];
-[BWInferenceEngine addPostProcessor:];
-[BWInferenceEngine addInferenceOfType:version:configuration:];
-[BWInferenceEngine performInferencesOnSampleBuffer:attachingResultsToSampleBuffer:];
-[BWInferenceEngine inferenceTypes];
-[BWInferenceEngine prepareForInferenceWithFormatProvider:];
-[BWInferenceEngine prepareForReconfigurationWithInputFormat:];
-[BWInferenceEngine reconfigure];
-[BWInferenceEngine prepareForInputInferenceVideoFormat:attachedMediaKey:];
-[BWInferenceEngine initWithScheduler:priority:processingConfiguration:name:];
-[BWInferenceEngine preparedWorkloadDescription];
-[BWInferenceEngine espressoContextForExecutionTarget:];
-[BWInferenceEngine prepareForInferenceWithFormatProvider:pixelBufferPoolProvider:];
-[BWInferenceEngine prepareForInputVideoFormat:attachedMediaKey:];
-[BWInferenceEngine enableIntermediateBufferSharingWithNetworksLoadedFromPath:];
-[BWInferenceEngine isConfiguredForInference];
-[BWInferenceEngine requiresDeviceOrientationMetadata];
-[BWInferenceEngine description];
-[BWInferenceEngine initWithScheduler:priority:shareIntermediateBuffer:];
-[BWInferenceEngine setName:];
-[BWInferenceEngine newMetalEvent];
-[BWInferenceEngine name];
-[BWInferenceEngine metalCommandBuffer];
-[BWInferenceEngine defaultDeviceMetalContext];
```
