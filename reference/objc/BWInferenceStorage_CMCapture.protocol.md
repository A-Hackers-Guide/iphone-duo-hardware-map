# `BWInferenceStorage` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"BWInferenceProviderStorage",R,N) inferenceStorage;
@property (T@"<BWInferenceTextureStorage>",R,N) textureStorage;
@property (T@"NSArray",R,C,N) requirementsNeedingPixelBufferPools;
@property (T@"NSArray",R,C,N) requirementsNeedingPixelBuffers;
@property (T@"NSDictionary",&,N) inferenceResults;
@property (T@"NSDictionary",C,N) inputSampleBufferAttachments;
@property (T@"NSMutableDictionary",&,N) mutableInferenceMetadata;
```

## Instance methods

```
-[BWInferenceStorage clear];
-[BWInferenceStorage inputSampleBufferAttachments];
-[BWInferenceStorage setMutableInferenceMetadata:];
-[BWInferenceStorage pixelBufferForRequirement:];
-[BWInferenceStorage textureStorage];
-[BWInferenceStorage inferenceResults];
-[BWInferenceStorage setInferenceResults:];
-[BWInferenceStorage inferenceStorage];
-[BWInferenceStorage pixelBufferPoolForRequirement:];
-[BWInferenceStorage setPixelBufferPool:forRequirement:];
-[BWInferenceStorage setPixelBuffer:forRequirement:];
-[BWInferenceStorage requirementsNeedingPixelBufferPools];
-[BWInferenceStorage setInputSampleBufferAttachments:];
-[BWInferenceStorage mutableInferenceMetadata];
-[BWInferenceStorage requirementsNeedingPixelBuffers];
```
