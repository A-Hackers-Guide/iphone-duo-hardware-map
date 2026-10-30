# `BWDerectificationInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`, `BWInferencePropagatable`
- 18 instance variables, 22 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"BWInferenceVideoRequirement" _opticalFlowInputRequirement;
@"BWInferenceVideoRequirement" _outputRequirement;
@"NSString" _portType;
@"BWMetalInferenceContext" _metalInferenceContext;
@"MTLTextureDescriptor" _inputDescriptor;
@"MTLTextureDescriptor" _opticalFlowInputDescriptor;
@"MTLTextureDescriptor" _outputDescriptor;
@"PTDisparityPostProcessing" _disparityPostProcessor;
@"<MTLTexture>" _disparityIntermediate;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"<MTLComputePipelineState>" _depthPaddingPipelineState;
Q _concurrencyWidth;
B _applyRollingShutterCorrection;
f _canonicalDisparityScaleFactorOverride;
@"GDCTransform" _gdcTransform;
B _lastIsQsubFrame;
```

## Properties

```
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
@property (Ti,R,N) type;
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
+[BWDerectificationInferenceProvider initialize];
```

## Instance methods

```
-[BWDerectificationInferenceProvider cacheable];
-[BWDerectificationInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWDerectificationInferenceProvider extractable];
-[BWDerectificationInferenceProvider outputVideoRequirements];
-[BWDerectificationInferenceProvider prewarmUsingLimitedMemory:];
-[BWDerectificationInferenceProvider allowsAsyncPropagation];
-[BWDerectificationInferenceProvider dealloc];
-[BWDerectificationInferenceProvider reconcileWithPlaceholderProvider:];
-[BWDerectificationInferenceProvider setCustomInferenceIdentifier:];
-[BWDerectificationInferenceProvider cloneVideoRequirements];
-[BWDerectificationInferenceProvider allowedPixelBufferCompressionDirection];
-[BWDerectificationInferenceProvider executionTarget];
-[BWDerectificationInferenceProvider preventionReasons];
-[BWDerectificationInferenceProvider type];
-[BWDerectificationInferenceProvider executable];
-[BWDerectificationInferenceProvider outputMetadataRequirements];
-[BWDerectificationInferenceProvider newStorage];
-[BWDerectificationInferenceProvider propagatable];
-[BWDerectificationInferenceProvider submittable];
-[BWDerectificationInferenceProvider sharedResourcePreparator];
-[BWDerectificationInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWDerectificationInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWDerectificationInferenceProvider customInferenceIdentifier];
-[BWDerectificationInferenceProvider inputMetadataRequirements];
-[BWDerectificationInferenceProvider inputVideoRequirements];
-[BWDerectificationInferenceProvider prewarmingSharedResourceType];
-[BWDerectificationInferenceProvider initWithInputRequirement:opticalFlowInputRequirement:outputRequirement:resourceProvider:configuration:];
```
