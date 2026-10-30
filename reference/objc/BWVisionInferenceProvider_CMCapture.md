# `BWVisionInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferencePropagatable`
- 28 instance variables, 23 properties, 37 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
i _type;
i _executionTarget;
@"NSSet" _preventionReasons;
@"BWVisionInferenceConfiguration" _configuration;
@"BWFaceSegmentsWithLandmarksInferenceConfiguration" _faceSegmentsWithLandmarksInferenceConfiguration;
@"NSArray" _prototypeRequests;
@"BWVisionInferenceContext" _context;
Q _indexOfRequestForMaximumNumberOfFaces;
Q _maximumNumberOfFaces;
B _clampToLargestMaximumNumberOfFaces;
B _prioritizeISPMatchedFacesWhenClamping;
B _alwaysExecuteForRedEyeReduction;
Q _indexOfRequestForMergedFaceDetection;
@"NSIndexSet" _indicesOfRequestsMergedWithFaceDetection;
@"NSMapTable" _requestIndexByRequest;
@"NSMutableDictionary" _requestIndexByRequirement;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputVideoRequirements;
@"NSMutableArray" _cloneVideoRequirements;
@"NSMutableArray" _inputMetadataRequirements;
@"NSMutableArray" _outputMetadataRequirements;
@"BWInferenceVideoRequirement" _primaryInputVideoRequirement;
B _executesRequestsIndividually;
B _considerISPRectsIfVisionFails;
B _didLoadResourcesForAllRequests;
^{OpaqueVTPixelRotationSession=} _rotationSession;
@"NSString" _contextName;
```

## Properties

```
@property (T@"BWInferenceVideoRequirement",&,N,V_primaryInputVideoRequirement) primaryInputVideoRequirement;
@property (Ti,R,N,V_executionTarget) executionTarget;
@property (T@"NSSet",R,C,N,V_preventionReasons) preventionReasons;
@property (T@"NSArray",R,N,V_inputVideoRequirements) inputVideoRequirements;
@property (T@"NSArray",R,N,V_outputVideoRequirements) outputVideoRequirements;
@property (T@"NSArray",R,N,V_cloneVideoRequirements) cloneVideoRequirements;
@property (T@"NSArray",R,N,V_inputMetadataRequirements) inputMetadataRequirements;
@property (T@"NSArray",R,N,V_outputMetadataRequirements) outputMetadataRequirements;
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
+[BWVisionInferenceProvider initialize];
```

## Instance methods

```
-[BWVisionInferenceProvider cacheable];
-[BWVisionInferenceProvider prepareForExecution];
-[BWVisionInferenceProvider bindOutputForRequest:asAttachedMediaUsingKey:withVideoFormat:];
-[BWVisionInferenceProvider extractable];
-[BWVisionInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWVisionInferenceProvider outputVideoRequirements];
-[BWVisionInferenceProvider prewarmUsingLimitedMemory:];
-[BWVisionInferenceProvider allowsAsyncPropagation];
-[BWVisionInferenceProvider bindOutputForRequest:asMetadataUsingKey:];
-[BWVisionInferenceProvider primaryInputVideoRequirement];
-[BWVisionInferenceProvider dealloc];
-[BWVisionInferenceProvider setPrimaryInputVideoRequirement:];
-[BWVisionInferenceProvider reconcileWithPlaceholderProvider:];
-[BWVisionInferenceProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWVisionInferenceProvider setCustomInferenceIdentifier:];
-[BWVisionInferenceProvider cloneVideoRequirements];
-[BWVisionInferenceProvider bindOutputForRequest:asConsolidatedMetadataUsingKeys:];
-[BWVisionInferenceProvider allowedPixelBufferCompressionDirection];
-[BWVisionInferenceProvider executionTarget];
-[BWVisionInferenceProvider preventionReasons];
-[BWVisionInferenceProvider type];
-[BWVisionInferenceProvider executable];
-[BWVisionInferenceProvider initWithConfiguration:requests:executesRequestsIndividually:executionTarget:preventionReasons:resourceProvider:];
-[BWVisionInferenceProvider outputMetadataRequirements];
-[BWVisionInferenceProvider bindInputForRequest:fromMetadataUsingKeys:];
-[BWVisionInferenceProvider newStorage];
-[BWVisionInferenceProvider propagatable];
-[BWVisionInferenceProvider bindOutputForRequest:asMetadataUsingKeys:];
-[BWVisionInferenceProvider submittable];
-[BWVisionInferenceProvider sharedResourcePreparator];
-[BWVisionInferenceProvider bindIdealInputForRequest:fromAttachedMediaUsingKey:];
-[BWVisionInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWVisionInferenceProvider bindInputForRequest:fromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWVisionInferenceProvider customInferenceIdentifier];
-[BWVisionInferenceProvider inputMetadataRequirements];
-[BWVisionInferenceProvider inputVideoRequirements];
-[BWVisionInferenceProvider prewarmingSharedResourceType];
```
