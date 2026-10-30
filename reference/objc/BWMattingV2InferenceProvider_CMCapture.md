# `BWMattingV2InferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferencePropagatable`, `BWMattingInferenceBinding`
- 29 instance variables, 34 properties, 56 instance methods, 2 class methods

## Instance variables

```
i _type;
@"NSString" _customInferenceIdentifier;
@"NSDictionary" _sensorConfigurationsByPortType;
@"FigMatting" _mattingProcessor;
i _mattingProcessorVersion;
i _mattingTuningConfiguration;
I _enabledMattes;
B _submitWithoutSynchronization;
B _appliesFinalCropRect;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputVideoRequirements;
@"NSMutableArray" _inputMetadataRequirements;
@"NSMutableArray" _outputMetadataRequirements;
@"BWInferenceVideoRequirement" _primaryFormatInputVideoRequirement;
@"BWInferenceVideoRequirement" _depthInputVideoRequirement;
@"BWInferenceVideoRequirement" _disparityInputVideoRequirement;
@"BWInferenceVideoRequirement" _segmentationInputVideoRequirement;
@"BWInferenceVideoRequirement" _segmentationOutputVideoRequirement;
@"BWInferenceCloneVideoRequirement" _lowResSegmentationCloneOutputVideoRequirement;
@"BWInferenceVideoRequirement" _refinedDepthOutputVideoRequirement;
@"NSArray" _enabledSemanticMattingOutputTypes;
@"NSMutableDictionary" _semanticMatteInputVideoRequirementsByMattingOutputType;
@"NSMutableDictionary" _semanticMatteOutputVideoRequirementsByMattingOutputType;
@"BWInferenceMetadataRequirement" _faceSegmentsWithLandmarksMetadataRequirement;
@"BWInferenceMetadataRequirement" _outputMasksContainsValidContentRequirement;
@"<MTLCommandQueue>" _metalCommandQueue;
^{OpaqueVTPixelTransferSession=} _lowResSegmentationCloneCopySession;
@"NSDictionary" _sdofRenderingTuningParameters;
f _mainImageDownscalingFactor;
```

## Properties

```
@property (T@"BWInferenceVideoRequirement",&,N,V_primaryFormatInputVideoRequirement) primaryFormatInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_segmentationInputVideoRequirement) segmentationInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_depthInputVideoRequirement) depthInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_disparityInputVideoRequirement) disparityInputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_segmentationOutputVideoRequirement) segmentationOutputVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_refinedDepthOutputVideoRequirement) refinedDepthOutputVideoRequirement;
@property (T@"BWInferenceCloneVideoRequirement",&,N,V_lowResSegmentationCloneOutputVideoRequirement) lowResSegmentationCloneOutputVideoRequirement;
@property (T@"NSArray",&,N,V_enabledSemanticMattingOutputTypes) enabledSemanticMattingOutputTypes;
@property (T@"NSMutableDictionary",&,N,V_semanticMatteInputVideoRequirementsByMattingOutputType) semanticMatteInputVideoRequirementsByMattingOutputType;
@property (T@"NSMutableDictionary",&,N,V_semanticMatteOutputVideoRequirementsByMattingOutputType) semanticMatteOutputVideoRequirementsByMattingOutputType;
@property (T@"BWInferenceMetadataRequirement",&,N,V_faceSegmentsWithLandmarksMetadataRequirement) faceSegmentsWithLandmarksMetadataRequirement;
@property (T@"BWInferenceMetadataRequirement",&,N,V_outputMasksContainsValidContentRequirement) outputMasksContainsValidContentRequirement;
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N) outputVideoRequirements;
@property (T@"NSArray",R,N) cloneVideoRequirements;
@property (T@"NSArray",R,N) inputMetadataRequirements;
@property (T@"NSArray",R,N) outputMetadataRequirements;
@property (TI,R,N) allowedPixelBufferCompressionDirection;
@property (Ti,R,N) prewarmingSharedResourceType;
@property (T@"NSString",&,N) customInferenceIdentifier;
@property (Ti,R,N,V_type) type;
@property (T@"<BWInferenceCacheable>",R,N) cacheable;
@property (T@"<BWInferenceExecutable>",R,N) executable;
@property (T@"<BWInferenceSubmittable>",R,N) submittable;
@property (T@"<BWInferenceSharedResourcePreparatory>",R,N) sharedResourcePreparator;
@property (T@"<BWInferenceExtractable>",R,N) extractable;
@property (T@"<BWInferencePropagatable>",R,N) propagatable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) allowsAsyncPropagation;
```

## Class methods

```
+[BWMattingV2InferenceProvider initialize];
+[BWMattingV2InferenceProvider inputAttachedMediaKeyForMattingOutputType:];
```

## Instance methods

```
-[BWMattingV2InferenceProvider cacheable];
-[BWMattingV2InferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWMattingV2InferenceProvider primaryFormatInputVideoRequirement];
-[BWMattingV2InferenceProvider extractable];
-[BWMattingV2InferenceProvider segmentationInputVideoRequirement];
-[BWMattingV2InferenceProvider bindMattingOutput:fromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWMattingV2InferenceProvider outputVideoRequirements];
-[BWMattingV2InferenceProvider prewarmUsingLimitedMemory:];
-[BWMattingV2InferenceProvider setSegmentationInputVideoRequirement:];
-[BWMattingV2InferenceProvider segmentationOutputVideoRequirement];
-[BWMattingV2InferenceProvider semanticMatteOutputVideoRequirementsByMattingOutputType];
-[BWMattingV2InferenceProvider allowsAsyncPropagation];
-[BWMattingV2InferenceProvider bindMattingOutput:asMetadataUsingKeys:];
-[BWMattingV2InferenceProvider bindMattingInput:fromMetadataUsingKeys:];
-[BWMattingV2InferenceProvider dealloc];
-[BWMattingV2InferenceProvider setDepthInputVideoRequirement:];
-[BWMattingV2InferenceProvider setLowResSegmentationCloneOutputVideoRequirement:];
-[BWMattingV2InferenceProvider lowResSegmentationCloneOutputVideoRequirement];
-[BWMattingV2InferenceProvider enabledSemanticMattingOutputTypes];
-[BWMattingV2InferenceProvider reconcileWithPlaceholderProvider:];
-[BWMattingV2InferenceProvider refinedDepthOutputVideoRequirement];
-[BWMattingV2InferenceProvider setSemanticMatteInputVideoRequirementsByMattingOutputType:];
-[BWMattingV2InferenceProvider initWithConfiguration:];
-[BWMattingV2InferenceProvider setCustomInferenceIdentifier:];
-[BWMattingV2InferenceProvider cloneVideoRequirements];
-[BWMattingV2InferenceProvider disparityInputVideoRequirement];
-[BWMattingV2InferenceProvider allowedPixelBufferCompressionDirection];
-[BWMattingV2InferenceProvider setEnabledSemanticMattingOutputTypes:];
-[BWMattingV2InferenceProvider setDisparityInputVideoRequirement:];
-[BWMattingV2InferenceProvider semanticMatteInputVideoRequirementsByMattingOutputType];
-[BWMattingV2InferenceProvider executionTarget];
-[BWMattingV2InferenceProvider preventionReasons];
-[BWMattingV2InferenceProvider faceSegmentsWithLandmarksMetadataRequirement];
-[BWMattingV2InferenceProvider type];
-[BWMattingV2InferenceProvider setRefinedDepthOutputVideoRequirement:];
-[BWMattingV2InferenceProvider setSegmentationOutputVideoRequirement:];
-[BWMattingV2InferenceProvider executable];
-[BWMattingV2InferenceProvider depthInputVideoRequirement];
-[BWMattingV2InferenceProvider setPrimaryFormatInputVideoRequirement:];
-[BWMattingV2InferenceProvider outputMetadataRequirements];
-[BWMattingV2InferenceProvider newStorage];
-[BWMattingV2InferenceProvider propagatable];
-[BWMattingV2InferenceProvider setFaceSegmentsWithLandmarksMetadataRequirement:];
-[BWMattingV2InferenceProvider submittable];
-[BWMattingV2InferenceProvider outputMasksContainsValidContentRequirement];
-[BWMattingV2InferenceProvider bindMattingInput:fromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWMattingV2InferenceProvider sharedResourcePreparator];
-[BWMattingV2InferenceProvider bindMattingInput:fromAttachedMediaUsingKey:withVideoFormat:];
-[BWMattingV2InferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWMattingV2InferenceProvider setOutputMasksContainsValidContentRequirement:];
-[BWMattingV2InferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWMattingV2InferenceProvider customInferenceIdentifier];
-[BWMattingV2InferenceProvider inputMetadataRequirements];
-[BWMattingV2InferenceProvider inputVideoRequirements];
-[BWMattingV2InferenceProvider prewarmingSharedResourceType];
-[BWMattingV2InferenceProvider setSemanticMatteOutputVideoRequirementsByMattingOutputType:];
```
