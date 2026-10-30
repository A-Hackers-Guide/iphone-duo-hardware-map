# `MPSGraphGatherOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
q _axis;
Q _batchDims;
B _allowNegativeIndices;
```

## Instance methods

```
-[MPSGraphGatherOp initWithGraph:inputTensors:controlDependencies:axis:batchDimensions:name:];
-[MPSGraphGatherOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphGatherOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
