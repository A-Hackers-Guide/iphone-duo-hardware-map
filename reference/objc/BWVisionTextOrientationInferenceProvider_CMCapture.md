# `BWVisionTextOrientationInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferencePropagatable`
- 13 instance variables, 22 properties, 29 instance methods, 1 class methods

## Instance variables

```
i _type;
i _executionTarget;
@"NSSet" _preventionReasons;
@"ImageReader_CRLegacyCompatibility" _imageReader;
@"NSMutableArray" _inputVideoRequirements;
@"NSMutableArray" _outputMetadataRequirements;
@"NSString" _customInferenceIdentifier;
@"NSDictionary" _orientationResult;
@"NSArray" _outputVideoRequirements;
@"NSArray" _cloneVideoRequirements;
@"NSArray" _inputMetadataRequirements;
I _allowedPixelBufferCompressionDirection;
i _prewarmingSharedResourceType;
```

## Properties

```
@property (Ti,R,N,V_executionTarget) executionTarget;
@property (T@"NSSet",R,C,N,V_preventionReasons) preventionReasons;
@property (T@"NSArray",R,N,V_inputVideoRequirements) inputVideoRequirements;
@property (T@"NSArray",R,N,V_outputVideoRequirements) outputVideoRequirements;
@property (T@"NSArray",R,N,V_cloneVideoRequirements) cloneVideoRequirements;
@property (T@"NSArray",R,N,V_inputMetadataRequirements) inputMetadataRequirements;
@property (T@"NSArray",R,N,V_outputMetadataRequirements) outputMetadataRequirements;
@property (TI,R,N,V_allowedPixelBufferCompressionDirection) allowedPixelBufferCompressionDirection;
@property (Ti,R,N,V_prewarmingSharedResourceType) prewarmingSharedResourceType;
@property (T@"NSString",&,N,V_customInferenceIdentifier) customInferenceIdentifier;
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
+[BWVisionTextOrientationInferenceProvider initialize];
```

## Instance methods

```
-[BWVisionTextOrientationInferenceProvider cacheable];
-[BWVisionTextOrientationInferenceProvider prepareForExecution];
-[BWVisionTextOrientationInferenceProvider extractable];
-[BWVisionTextOrientationInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWVisionTextOrientationInferenceProvider outputVideoRequirements];
-[BWVisionTextOrientationInferenceProvider prewarmUsingLimitedMemory:];
-[BWVisionTextOrientationInferenceProvider allowsAsyncPropagation];
-[BWVisionTextOrientationInferenceProvider bindOutputAsMetadataUsingKey:];
-[BWVisionTextOrientationInferenceProvider dealloc];
-[BWVisionTextOrientationInferenceProvider reconcileWithPlaceholderProvider:];
-[BWVisionTextOrientationInferenceProvider bindInputFromAttachedMediaUsingKey:preparedByAttachedMediaKey:withVideoFormatProvider:];
-[BWVisionTextOrientationInferenceProvider setCustomInferenceIdentifier:];
-[BWVisionTextOrientationInferenceProvider cloneVideoRequirements];
-[BWVisionTextOrientationInferenceProvider allowedPixelBufferCompressionDirection];
-[BWVisionTextOrientationInferenceProvider executionTarget];
-[BWVisionTextOrientationInferenceProvider preventionReasons];
-[BWVisionTextOrientationInferenceProvider type];
-[BWVisionTextOrientationInferenceProvider executable];
-[BWVisionTextOrientationInferenceProvider outputMetadataRequirements];
-[BWVisionTextOrientationInferenceProvider newStorage];
-[BWVisionTextOrientationInferenceProvider propagatable];
-[BWVisionTextOrientationInferenceProvider submittable];
-[BWVisionTextOrientationInferenceProvider sharedResourcePreparator];
-[BWVisionTextOrientationInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWVisionTextOrientationInferenceProvider customInferenceIdentifier];
-[BWVisionTextOrientationInferenceProvider inputMetadataRequirements];
-[BWVisionTextOrientationInferenceProvider inputVideoRequirements];
-[BWVisionTextOrientationInferenceProvider initWithImageReader:executionTarget:preventionReasons:resourceProvider:];
-[BWVisionTextOrientationInferenceProvider prewarmingSharedResourceType];
```
