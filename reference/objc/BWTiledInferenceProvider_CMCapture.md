# `BWTiledInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceSubmittable`, `BWInferencePropagatable`, `BWInferenceCacheable`
- 16 instance variables, 22 properties, 34 instance methods, 9 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"NSArray" _inputVideoRequirements;
@"NSArray" _outputVideoRequirements;
@"NSArray" _tileInputVideoRequirements;
@"NSArray" _tileInputBindingNames;
@"NSArray" _tileOutputVideoRequirements;
@"NSArray" _tileOutputBindingNames;
@"NSArray" _additionalVideoRequirements;
_maxTileCount;
@"BWEspressoInferenceProvider" _espressoProvider;
@"NSObject<OS_dispatch_queue>" _espressoWorkQueue;
@"BWTiledEspressoInferenceConfiguration" _configuration;
@"<BWInferenceResourceProvider>" _resourceProvider;
@"FigMetalContext" _metalContext;
^{__CVMetalTextureCache=} _textureCache;
i type;
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
@property (Ti,R,N,Vtype) type;
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
+[BWTiledInferenceProvider initialize];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:appliesFinalCropRect:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:includesInvalidContent:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:includesInvalidContent:appliesFinalCropRect:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:sliceCount:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:sliceCount:appliesFinalCropRect:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:sliceCount:includesInvalidContent:];
+[BWTiledInferenceProvider videoFormatWithPixelFormat:size:sliceCount:includesInvalidContent:appliesFinalCropRect:];
```

## Instance methods

```
-[BWTiledInferenceProvider cacheable];
-[BWTiledInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWTiledInferenceProvider extractable];
-[BWTiledInferenceProvider outputVideoRequirements];
-[BWTiledInferenceProvider prewarmUsingLimitedMemory:];
-[BWTiledInferenceProvider allowsAsyncPropagation];
-[BWTiledInferenceProvider dealloc];
-[BWTiledInferenceProvider reconcileWithPlaceholderProvider:];
-[BWTiledInferenceProvider setCustomInferenceIdentifier:];
-[BWTiledInferenceProvider cloneVideoRequirements];
-[BWTiledInferenceProvider allowedPixelBufferCompressionDirection];
-[BWTiledInferenceProvider executionTarget];
-[BWTiledInferenceProvider preventionReasons];
-[BWTiledInferenceProvider type];
-[BWTiledInferenceProvider executable];
-[BWTiledInferenceProvider purgeIntermediateResources];
-[BWTiledInferenceProvider outputMetadataRequirements];
-[BWTiledInferenceProvider newStorage];
-[BWTiledInferenceProvider propagatable];
-[BWTiledInferenceProvider submittable];
-[BWTiledInferenceProvider sharedResourcePreparator];
-[BWTiledInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWTiledInferenceProvider propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWTiledInferenceProvider customInferenceIdentifier];
-[BWTiledInferenceProvider inputMetadataRequirements];
-[BWTiledInferenceProvider inputVideoRequirements];
-[BWTiledInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWTiledInferenceProvider prewarmingSharedResourceType];
-[BWTiledInferenceProvider createInputTileFor:to:withInputs:atPosition:encodeToCmdBuffer:];
-[BWTiledInferenceProvider initWithConfiguration:inputVideoRequirements:outputVideoRequirements:resourceProvider:];
-[BWTiledInferenceProvider loadNetworkWithURL:configName:inferenceType:maxTileCount:inputFormatsByBindingName:outputFormatsByBindingName:additionalVideoRequirements:];
-[BWTiledInferenceProvider preProcessOutputTexture:forMediaKey:encodeToCmdBuffer:];
-[BWTiledInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:currentTileCount:];
-[BWTiledInferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalTextures:withInputTileTextures:withInputFullTextures:atPosition:encodeToCmdBuffer:];
```
