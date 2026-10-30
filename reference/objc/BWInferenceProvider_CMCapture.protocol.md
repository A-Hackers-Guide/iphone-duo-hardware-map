# `BWInferenceProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BWInferenceJobProvider`
- 0 instance variables, 9 properties, 11 instance methods, 0 class methods

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
```

## Instance methods

```
-[BWInferenceProvider outputVideoRequirements];
-[BWInferenceProvider prewarmUsingLimitedMemory:];
-[BWInferenceProvider cloneVideoRequirements];
-[BWInferenceProvider allowedPixelBufferCompressionDirection];
-[BWInferenceProvider executionTarget];
-[BWInferenceProvider preventionReasons];
-[BWInferenceProvider outputMetadataRequirements];
-[BWInferenceProvider newStorage];
-[BWInferenceProvider inputMetadataRequirements];
-[BWInferenceProvider inputVideoRequirements];
-[BWInferenceProvider prewarmingSharedResourceType];
```
