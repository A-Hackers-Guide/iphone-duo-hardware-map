# `BWE5InferenceStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceProviderStorage`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _bindingNameByRequirement;
@"NSMapTable" _tensorPortByRequirement;
```

## Class methods

```
+[BWE5InferenceStorage initialize];
```

## Instance methods

```
-[BWE5InferenceStorage clear];
-[BWE5InferenceStorage dealloc];
-[BWE5InferenceStorage bindingNameForRequirement:];
-[BWE5InferenceStorage setTensorPort:forRequirement:];
-[BWE5InferenceStorage newMetadataDictionarySatisfyingRequirement:];
-[BWE5InferenceStorage initWithBindingNameByRequirement:requirementsNeedingPixelBuffers:requirementsNeedingPixelBufferPools:requirementsNeedingTensors:];
-[BWE5InferenceStorage tensorPortForRequirement:];
```
