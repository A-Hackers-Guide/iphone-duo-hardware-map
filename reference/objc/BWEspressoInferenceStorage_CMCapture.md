# `BWEspressoInferenceStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceProviderStorage`
- 4 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _bindingNameByRequirement;
@"NSMapTable" _tensorByRequirement;
@"NSMutableSet" _requirementsUsingTensors;
@"NSMutableSet" _requirementsUsingPixelBuffers;
```

## Class methods

```
+[BWEspressoInferenceStorage initialize];
```

## Instance methods

```
-[BWEspressoInferenceStorage clear];
-[BWEspressoInferenceStorage addTensorInUseRequirement:];
-[BWEspressoInferenceStorage dealloc];
-[BWEspressoInferenceStorage newSampleBufferSatisfyingRequirement:withPropagationSampleBuffer:];
-[BWEspressoInferenceStorage bindingNameForRequirement:];
-[BWEspressoInferenceStorage addPixelBufferInUseRequirement:];
-[BWEspressoInferenceStorage newMetadataDictionarySatisfyingRequirement:];
-[BWEspressoInferenceStorage initWithBindingNameByRequirement:requirementsNeedingPixelBuffers:requirementsNeedingPixelBufferPools:requirementsNeedingTensors:];
-[BWEspressoInferenceStorage tensorForRequirement:];
```
