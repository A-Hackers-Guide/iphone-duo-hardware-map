# `MTL4MachineLearningPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4PipelineDescriptor`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MTL4FunctionDescriptor" _machineLearningFunctionDescriptor;
^v _extents;
q _deviceSelection;
```

## Properties

```
@property (Tq) deviceSelection;
@property (T@"NSString",C,D,N) label;
@property (T@"MTL4FunctionDescriptor",C,N,V_machineLearningFunctionDescriptor) machineLearningFunctionDescriptor;
```

## Instance methods

```
-[MTL4MachineLearningPipelineDescriptor init];
-[MTL4MachineLearningPipelineDescriptor dealloc];
-[MTL4MachineLearningPipelineDescriptor reset];
-[MTL4MachineLearningPipelineDescriptor hash];
-[MTL4MachineLearningPipelineDescriptor copyWithZone:];
-[MTL4MachineLearningPipelineDescriptor isEqual:];
-[MTL4MachineLearningPipelineDescriptor deviceSelection];
-[MTL4MachineLearningPipelineDescriptor inputDimensionsAtBufferIndex:];
-[MTL4MachineLearningPipelineDescriptor machineLearningFunctionDescriptor];
-[MTL4MachineLearningPipelineDescriptor setDeviceSelection:];
-[MTL4MachineLearningPipelineDescriptor setInputDimensions:atBufferIndex:];
-[MTL4MachineLearningPipelineDescriptor setInputDimensions:withRange:];
-[MTL4MachineLearningPipelineDescriptor setMachineLearningFunctionDescriptor:];
```
