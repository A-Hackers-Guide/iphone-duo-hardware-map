# `BWDeferredProcessingContainer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWDeferredContainer`
- 10 instance variables, 6 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _sessionDictionary;
i _previousAttemptErrorCode;
I _processingCount;
@"NSObject<OS_dispatch_queue>" _metadataPrefetchQueue;
@"NSObject<OS_dispatch_queue>" _bufferPrefetchQueue;
Q _sizeBytes;
I _ageSeconds;
I _initSeconds;
B _isRemote;
@"BWPhotoManifest" _photoManifest;
```

## Properties

```
@property (TI,R,N) ageSeconds;
@property (TQ,R,N) sizeBytes;
@property (TB,R,N,V_isRemote) isRemote;
@property (TI,R,N,V_processingCount) processingCount;
@property (Ti,R,N,V_previousAttemptErrorCode) previousAttemptErrorCode;
@property (T@"BWPhotoManifest",R,N,V_photoManifest) photoManifest;
```

## Class methods

```
+[BWDeferredProcessingContainer maxProcessingCount];
```

## Instance methods

```
-[BWDeferredProcessingContainer isRemote];
-[BWDeferredProcessingContainer dealloc];
-[BWDeferredProcessingContainer photoManifest];
-[BWDeferredProcessingContainer sizeBytes];
-[BWDeferredProcessingContainer initWithApplicationID:resolvedSettings:unresolvedSettings:processingSettings:pipelineParameters:intermediates:photoDescriptors:];
-[BWDeferredProcessingContainer processingCount];
-[BWDeferredProcessingContainer abortingProcessingDueToError:];
-[BWDeferredProcessingContainer ageSeconds];
-[BWDeferredProcessingContainer copyArrayForTag:customClasses:err:];
-[BWDeferredProcessingContainer copyAttributesForBufferType:portType:err:];
-[BWDeferredProcessingContainer copyBufferForTag:err:];
-[BWDeferredProcessingContainer copyBufferForType:portType:metadata:err:];
-[BWDeferredProcessingContainer copyBuffersForType:portType:metadataArray:err:];
-[BWDeferredProcessingContainer copyDictionaryForTag:customClasses:err:];
-[BWDeferredProcessingContainer copyDictionaryForTag:err:];
-[BWDeferredProcessingContainer copyInferenceBufferForKey:portType:err:];
-[BWDeferredProcessingContainer copyInferenceForKey:customClasses:portType:err:];
-[BWDeferredProcessingContainer copyMetadataForBufferTag:err:];
-[BWDeferredProcessingContainer copyMetadataForTag:err:];
-[BWDeferredProcessingContainer hasBufferForType:portType:];
-[BWDeferredProcessingContainer hasInference:portType:];
-[BWDeferredProcessingContainer hasInferenceBuffer:portType:];
-[BWDeferredProcessingContainer initWithApplicationID:captureRequestIdentifier:baseFolderURL:openForPeeking:err:];
-[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:];
-[BWDeferredProcessingContainer previousAttemptErrorCode];
-[BWDeferredProcessingContainer releaseIntermediates];
```
