# `BWInferenceSimpleStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceStorage`
- 5 instance variables, 11 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _pixelBufferByRequirement;
@"NSArray" _requirementsNeedingPixelBufferPools;
@"NSMutableDictionary" _pixelBufferPoolByRequirement;
@"NSDictionary" _inputSampleBufferAttachments;
@"NSMutableDictionary" _mutableInferenceMetadata;
```

## Properties

```
@property (T@"BWInferenceProviderStorage",R,N) inferenceStorage;
@property (T@"<BWInferenceTextureStorage>",R,N) textureStorage;
@property (T@"NSArray",R,C,N,V_requirementsNeedingPixelBufferPools) requirementsNeedingPixelBufferPools;
@property (T@"NSArray",R,C,N) requirementsNeedingPixelBuffers;
@property (T@"NSDictionary",&,N) inferenceResults;
@property (T@"NSDictionary",C,N,V_inputSampleBufferAttachments) inputSampleBufferAttachments;
@property (T@"NSMutableDictionary",&,N,V_mutableInferenceMetadata) mutableInferenceMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWInferenceSimpleStorage clear];
-[BWInferenceSimpleStorage inputSampleBufferAttachments];
-[BWInferenceSimpleStorage setMutableInferenceMetadata:];
-[BWInferenceSimpleStorage pixelBufferForRequirement:];
-[BWInferenceSimpleStorage textureStorage];
-[BWInferenceSimpleStorage inferenceResults];
-[BWInferenceSimpleStorage dealloc];
-[BWInferenceSimpleStorage setInferenceResults:];
-[BWInferenceSimpleStorage inferenceStorage];
-[BWInferenceSimpleStorage pixelBufferPoolForRequirement:];
-[BWInferenceSimpleStorage setPixelBufferPool:forRequirement:];
-[BWInferenceSimpleStorage setPixelBuffer:forRequirement:];
-[BWInferenceSimpleStorage requirementsNeedingPixelBufferPools];
-[BWInferenceSimpleStorage setInputSampleBufferAttachments:];
-[BWInferenceSimpleStorage mutableInferenceMetadata];
-[BWInferenceSimpleStorage initWithRequirementsNeedingPools:];
-[BWInferenceSimpleStorage requirementsNeedingPixelBuffers];
```
