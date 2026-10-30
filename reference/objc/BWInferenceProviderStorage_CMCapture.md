# `BWInferenceProviderStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceStorage`
- 7 instance variables, 11 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _requirementsNeedingPixelBuffers;
@"NSMutableDictionary" _pixelBufferByRequirement;
@"NSArray" _requirementsNeedingPixelBufferPools;
@"NSMutableDictionary" _pixelBufferPoolByRequirement;
@"NSDictionary" _inputSampleBufferAttachments;
@"NSMutableDictionary" _mutableInferenceMetadata;
@"NSDictionary" _inferenceResults;
```

## Properties

```
@property (T@"BWInferenceProviderStorage",R,N) inferenceStorage;
@property (T@"<BWInferenceTextureStorage>",R,N) textureStorage;
@property (T@"NSArray",R,C,N,V_requirementsNeedingPixelBufferPools) requirementsNeedingPixelBufferPools;
@property (T@"NSArray",R,C,N,V_requirementsNeedingPixelBuffers) requirementsNeedingPixelBuffers;
@property (T@"NSDictionary",&,N,V_inferenceResults) inferenceResults;
@property (T@"NSDictionary",C,N,V_inputSampleBufferAttachments) inputSampleBufferAttachments;
@property (T@"NSMutableDictionary",&,N,V_mutableInferenceMetadata) mutableInferenceMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceProviderStorage initialize];
```

## Instance methods

```
-[BWInferenceProviderStorage clear];
-[BWInferenceProviderStorage inputSampleBufferAttachments];
-[BWInferenceProviderStorage setMutableInferenceMetadata:];
-[BWInferenceProviderStorage pixelBufferForRequirement:];
-[BWInferenceProviderStorage textureStorage];
-[BWInferenceProviderStorage inferenceResults];
-[BWInferenceProviderStorage dealloc];
-[BWInferenceProviderStorage setInferenceResults:];
-[BWInferenceProviderStorage newSampleBufferSatisfyingRequirement:withPropagationSampleBuffer:];
-[BWInferenceProviderStorage newSampleBufferSatisfyingCloneRequirement:];
-[BWInferenceProviderStorage inferenceStorage];
-[BWInferenceProviderStorage pixelBufferPoolForRequirement:];
-[BWInferenceProviderStorage setPixelBufferPool:forRequirement:];
-[BWInferenceProviderStorage newMetadataDictionarySatisfyingRequirement:];
-[BWInferenceProviderStorage setPixelBuffer:forRequirement:];
-[BWInferenceProviderStorage requirementsNeedingPixelBufferPools];
-[BWInferenceProviderStorage description];
-[BWInferenceProviderStorage initWithRequirementsNeedingPixelBuffers:requirementsNeedingPixelBufferPools:];
-[BWInferenceProviderStorage setInputSampleBufferAttachments:];
-[BWInferenceProviderStorage mutableInferenceMetadata];
-[BWInferenceProviderStorage requirementsNeedingPixelBuffers];
```
