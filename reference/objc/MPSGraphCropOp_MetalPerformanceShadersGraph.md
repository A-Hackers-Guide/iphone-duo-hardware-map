# `MPSGraphCropOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q _amount_before;
Q _amount_after;
q _dimensionIndex;
```

## Instance methods

```
-[MPSGraphCropOp initWithGraph:inputTensors:controlDependencies:dimension_index:amount_before:amount_after:name:];
-[MPSGraphCropOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphCropOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
