# `BWPhotonicEngineNodeResourceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorCoordinator`
- Protocols: `BWInferencePixelBufferPoolProvider`
- 45 instance variables, 16 properties, 47 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceCoordinatorLock;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWNodeInput" _input;
@"BWNodeOutput" _output;
@"BWPixelBufferPool" _noiseReductionAndFusionProcessorOutputIntermediatePool;
@"BWPixelBufferPool" _enhancedResolutionGainMapPool;
@"BWPixelBufferPool" _deepZoomTransferHighResolutionInputPool;
@"BWPixelBufferPool" _deepZoomTransferEnhancedResolutionOutputPool;
@"BWPixelBufferPool" _deepFusionEnhancedResolutionOutputPool;
@"BWPixelBufferPool" _deepFusionEnhancedResolutionSemanticStyleOutputPool;
@"BWPixelBufferPool" _learnedFusionEnhancedResolutionOutputPool;
@"BWPixelBufferPool" _smartStyleEnhancedResolutionOutputPool;
@"BWPixelBufferPool" _smartStyleUltraHighResolutionOutputPool;
@"BWPixelBufferPool" _distortionCorrectionEnhancedResolutionOutputPool;
@"NSDictionary" _softISPOutputPoolByPixelFormat;
{?="width"i"height"i} _softISPOutputPoolDimensions;
@"BWPixelBufferPool" _syntheticIntermediatesPool;
@"BWPixelBufferPool" _fusionMapPool;
@"NSDictionary" _inferenceOutputPixelBufferProvidersByAttachedMediaKey;
@"BWPixelBufferPool" _intermediateInferenceInputPool;
@"NSDictionary" _inferenceInputPixelBufferProviderByResolutionFlavor;
@"NSDictionary" _inferenceInputPixelBufferProviderByResolutionFlavorByPortType;
@"BWPixelBufferPool" _stereoPhotoOutputPool;
@"NSDictionary" _pixelBufferProviderByPixelFormatByResolutionFlavor;
@"NSDictionary" _adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderByPortType;
B _hasSuccessfullySetupProcessorControllersAndMemoryResources;
@"NSObject<OS_dispatch_queue>" _postponedResourceSetupQueue;
@"NSObject<OS_dispatch_group>" _postponedResourceSetupGroup;
@"NSObject<OS_dispatch_queue>" _inferenceControllerQueue;
@"NSObject<OS_dispatch_group>" _inferenceControllerGroup;
@"NSObject<OS_dispatch_queue>" _workerQueue;
@"NSObject<OS_dispatch_queue>" _emitQueue;
@"NSObject<OS_dispatch_queue>" _stereoDisparityProcessorControllerQueue;
@"NSObject<OS_dispatch_queue>" _deferredProcessorControllerQueue;
B _useSharedExternalMemoryResourceForProcessorControllers;
@"NSArray" _sharedExternalMemoryResourceSetUpForResolutionFlavors;
@"CMIExternalMemoryResource" _sharedExternalMemoryResource;
@"NSMutableArray" _postponedProcessorTypes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _enhancedResolutionPortraitSemaphoreLock;
@"NSObject<OS_dispatch_semaphore>" _enhancedResolutionPortraitSemaphore;
@"BWStillImageInferences" _inferences;
@"BWStillImageInferences" _quadraForEnhancedResolutionInferences;
@"BWStillImageInferences" _stereoPhotoSecondaryInferences;
@"NSMutableDictionary" _inferenceAttachedMediaFormatDescriptionByAttachedMediaKey;
@"BWNode" _preparingNode;
```

## Properties

```
@property (TB,R) hasSuccessfullySetupProcessorControllersAndMemoryResources;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_emitQueue) emitQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_workerQueue) workerQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_inferenceControllerQueue) inferenceControllerQueue;
@property (T@"NSObject<OS_dispatch_group>",R,N,V_inferenceControllerGroup) inferenceControllerGroup;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_stereoDisparityProcessorControllerQueue) stereoDisparityProcessorControllerQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_deferredProcessorControllerQueue) deferredProcessorControllerQueue;
@property (T@"BWNode",N,V_preparingNode) preparingNode;
@property (TB,R,N,V_useSharedExternalMemoryResourceForProcessorControllers) useSharedExternalMemoryResourceForProcessorControllers;
@property (T@"CMIExternalMemoryResource",R,N,V_sharedExternalMemoryResource) sharedExternalMemoryResource;
@property (T@"NSArray",R,N,V_postponedProcessorTypes) postponedProcessorTypes;
@property (T@"BWStillImageInferences",R,N) syncInferences;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPhotonicEngineNodeResourceCoordinator initialize];
```

## Instance methods

```
-[BWPhotonicEngineNodeResourceCoordinator releaseResources];
-[BWPhotonicEngineNodeResourceCoordinator preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWPhotonicEngineNodeResourceCoordinator prepareEnhancedResolutionPortraitSemaphoreIfNeededWithSettings:];
-[BWPhotonicEngineNodeResourceCoordinator flushDeepZoomTransferHighResolutionInputPool];
-[BWPhotonicEngineNodeResourceCoordinator inferenceControllerQueue];
-[BWPhotonicEngineNodeResourceCoordinator pixelBufferProviderForInferencesWithResolutionFlavor:];
-[BWPhotonicEngineNodeResourceCoordinator asyncSetInference:inferenceAttachmentKey:];
-[BWPhotonicEngineNodeResourceCoordinator flushUltraHighResolutionBufferPools];
-[BWPhotonicEngineNodeResourceCoordinator syncMergeInferencesWithSampleBuffer:stillImageSettings:];
-[BWPhotonicEngineNodeResourceCoordinator attachedMediaFromInferencesOrSampleBuffer:attachedMediaKeys:];
-[BWPhotonicEngineNodeResourceCoordinator processorControllersForSharedExternalMemoryResource];
-[BWPhotonicEngineNodeResourceCoordinator prepareSharedExternalMemoryResourceForProcessorControllersIfNeededWithSettings:];
-[BWPhotonicEngineNodeResourceCoordinator stereoDisparityProcessorControllerQueue];
-[BWPhotonicEngineNodeResourceCoordinator asyncSetInferenceAttachedMediaMetadata:];
-[BWPhotonicEngineNodeResourceCoordinator dealloc];
-[BWPhotonicEngineNodeResourceCoordinator postponedProcessorForType:safelyExecuteBlockWhenReady:];
-[BWPhotonicEngineNodeResourceCoordinator syncGetInferencesForInferenceInputBufferType:];
-[BWPhotonicEngineNodeResourceCoordinator flushDeepFusionEnhancedResolutionOutputPool];
-[BWPhotonicEngineNodeResourceCoordinator inferenceControllerGroup];
-[BWPhotonicEngineNodeResourceCoordinator unsafeAddInferences:forInferenceInputBufferType:];
-[BWPhotonicEngineNodeResourceCoordinator useSharedExternalMemoryResourceForProcessorControllers];
-[BWPhotonicEngineNodeResourceCoordinator pixelBufferProviderForProcessorController:processorInput:type:dimensions:pixelFormat:attachedMediaKey:];
-[BWPhotonicEngineNodeResourceCoordinator purgeProcessorAndSharedExternalMemoryResourceBackendMemoryIfNeededWithSettings:];
-[BWPhotonicEngineNodeResourceCoordinator initWithNodeConfiguration:nodeInput:nodeOutput:];
-[BWPhotonicEngineNodeResourceCoordinator pixelBufferProviderForInferencesWithResolutionFlavor:portType:photoFormat:];
-[BWPhotonicEngineNodeResourceCoordinator emitQueue];
-[BWPhotonicEngineNodeResourceCoordinator postponedProcessorTypes];
-[BWPhotonicEngineNodeResourceCoordinator waitOnEnhancedResolutionPortraitSemaphoreIfNeeded];
-[BWPhotonicEngineNodeResourceCoordinator preparingNode];
-[BWPhotonicEngineNodeResourceCoordinator workerQueue];
-[BWPhotonicEngineNodeResourceCoordinator description];
-[BWPhotonicEngineNodeResourceCoordinator kickoffAnyPostonedResourceAllocations];
-[BWPhotonicEngineNodeResourceCoordinator cancelAllProcessing];
-[BWPhotonicEngineNodeResourceCoordinator asyncSetInferenceBuffer:metadata:inferenceAttachedMediaKey:];
-[BWPhotonicEngineNodeResourceCoordinator deferredProcessorControllerQueue];
-[BWPhotonicEngineNodeResourceCoordinator clearEnhancedResolutionPortraitSemaphoreWithError:];
-[BWPhotonicEngineNodeResourceCoordinator setupProcessorControllersAndMemoryResources];
-[BWPhotonicEngineNodeResourceCoordinator syncReleaseInferencesForInferenceInputBufferType:];
-[BWPhotonicEngineNodeResourceCoordinator adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:];
-[BWPhotonicEngineNodeResourceCoordinator liveReconfigureIfNeeded];
-[BWPhotonicEngineNodeResourceCoordinator waitAndSafelyGetProcessorControllerForType:];
-[BWPhotonicEngineNodeResourceCoordinator hasSuccessfullySetupProcessorControllersAndMemoryResources];
-[BWPhotonicEngineNodeResourceCoordinator syncInferences];
-[BWPhotonicEngineNodeResourceCoordinator releaseResourcesWithSettings:];
-[BWPhotonicEngineNodeResourceCoordinator sharedExternalMemoryResource];
-[BWPhotonicEngineNodeResourceCoordinator setPreparingNode:];
-[BWPhotonicEngineNodeResourceCoordinator flushSoftISPOutputBufferPools];
```
