# `BWInferenceVideoScalingProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceExecutable`, `BWInferencePreventable`, `BWInferencePropagatable`
- 20 instance variables, 23 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _inputRequirement;
@"BWInferenceVideoRequirement" _derivedFromRequirement;
@"NSArray" _outputRequirements;
@"NSDictionary" _colorSpaceProperties;
B _applyUprightExifOrientation;
i _offsetRotationDegrees;
B _applyValidBufferRect;
B _applyCustomCrop;
B _computeAndApplyAspectRatioCrop;
B _shouldApplyHorizontalFlip;
@"FigM2MController" _scalerController;
i _filterType;
I _scalerPriority;
f _customFiltersLastUsedHorizontalRatio;
f _customFiltersLastUsedVerticalRatio;
B _enableFencing;
f _outputAspectRatio;
@"NSMutableArray" _cloneVideoRequirements;
B _disableRotationInLandscapeAspectRatio;
```

## Properties

```
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N) outputVideoRequirements;
@property (T@"NSArray",R,N,V_cloneVideoRequirements) cloneVideoRequirements;
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
@property (TB,R,N) mustExecuteWhenAllowed;
@property (TB,R,N) allowsAsyncPropagation;
```

## Class methods

```
+[BWInferenceVideoScalingProvider initialize];
```

## Instance methods

```
-[BWInferenceVideoScalingProvider cacheable];
-[BWInferenceVideoScalingProvider prepareForExecution];
-[BWInferenceVideoScalingProvider extractable];
-[BWInferenceVideoScalingProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:];
-[BWInferenceVideoScalingProvider outputVideoRequirements];
-[BWInferenceVideoScalingProvider prewarmUsingLimitedMemory:];
-[BWInferenceVideoScalingProvider allowsAsyncPropagation];
-[BWInferenceVideoScalingProvider dealloc];
-[BWInferenceVideoScalingProvider reconcileWithPlaceholderProvider:];
-[BWInferenceVideoScalingProvider bindOutputByCloningInputRequirement:toAttachedMediaUsingKey:];
-[BWInferenceVideoScalingProvider setCustomInferenceIdentifier:];
-[BWInferenceVideoScalingProvider cloneVideoRequirements];
-[BWInferenceVideoScalingProvider initWithInputRequirement:derivedFromRequirement:outputRequirements:enableFencing:filterType:scalerPriority:];
-[BWInferenceVideoScalingProvider allowedPixelBufferCompressionDirection];
-[BWInferenceVideoScalingProvider executionTarget];
-[BWInferenceVideoScalingProvider preventionReasons];
-[BWInferenceVideoScalingProvider type];
-[BWInferenceVideoScalingProvider executable];
-[BWInferenceVideoScalingProvider outputMetadataRequirements];
-[BWInferenceVideoScalingProvider newStorage];
-[BWInferenceVideoScalingProvider description];
-[BWInferenceVideoScalingProvider mustExecuteWhenAllowed];
-[BWInferenceVideoScalingProvider propagatable];
-[BWInferenceVideoScalingProvider preventionReasonWithSampleBuffer:executionTime:];
-[BWInferenceVideoScalingProvider submittable];
-[BWInferenceVideoScalingProvider sharedResourcePreparator];
-[BWInferenceVideoScalingProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceVideoScalingProvider customInferenceIdentifier];
-[BWInferenceVideoScalingProvider inputMetadataRequirements];
-[BWInferenceVideoScalingProvider inputVideoRequirements];
-[BWInferenceVideoScalingProvider prewarmingSharedResourceType];
```
