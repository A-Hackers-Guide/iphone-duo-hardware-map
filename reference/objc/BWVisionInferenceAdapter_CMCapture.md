# `BWVisionInferenceAdapter`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceAdapter`
- 4 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"VNProcessingDevice" _applicationProcessingDevice;
@"VNProcessingDevice" _graphicsProcessingDevice;
@"VNProcessingDevice" _neuralProcessingDevice;
@"NSMutableDictionary" _visionRequestByDescriptor;
```

## Properties

```
@property (T@"VNProcessingDevice",R,N,V_applicationProcessingDevice) applicationProcessingDevice;
@property (T@"VNProcessingDevice",R,N,V_graphicsProcessingDevice) graphicsProcessingDevice;
@property (T@"VNProcessingDevice",R,N,V_neuralProcessingDevice) neuralProcessingDevice;
@property (T@"VNProcessingDevice",R,N) espressoBasedRequestProcessingDevice;
@property (T@"NSMutableDictionary",&,N,V_visionRequestByDescriptor) visionRequestByDescriptor;
```

## Class methods

```
+[BWVisionInferenceAdapter initialize];
```

## Instance methods

```
-[BWVisionInferenceAdapter init];
-[BWVisionInferenceAdapter dealloc];
-[BWVisionInferenceAdapter applicationProcessingDevice];
-[BWVisionInferenceAdapter espressoBasedRequestProcessingDevice];
-[BWVisionInferenceAdapter graphicsProcessingDevice];
-[BWVisionInferenceAdapter inferenceProviderForType:version:configuration:resourceProvider:status:];
-[BWVisionInferenceAdapter neuralProcessingDevice];
-[BWVisionInferenceAdapter setVisionRequestByDescriptor:];
-[BWVisionInferenceAdapter visionRequestByDescriptor];
```
