# `BWVisionInferenceStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceProviderStorage`
- 1 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _requestsByRequirement;
```

## Class methods

```
+[BWVisionInferenceStorage initialize];
```

## Instance methods

```
-[BWVisionInferenceStorage removeRequest:];
-[BWVisionInferenceStorage requestForRequirement:];
-[BWVisionInferenceStorage dealloc];
-[BWVisionInferenceStorage newSampleBufferSatisfyingRequirement:withPropagationSampleBuffer:];
-[BWVisionInferenceStorage newMetadataDictionarySatisfyingRequirement:];
-[BWVisionInferenceStorage initWithRequirementsNeedingPixelBuffers:requirementsNeedingPixelBufferPools:];
-[BWVisionInferenceStorage setRequest:forRequirement:];
```
