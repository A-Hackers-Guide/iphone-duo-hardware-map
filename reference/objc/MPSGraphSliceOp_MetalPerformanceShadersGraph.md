# `MPSGraphSliceOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
q _dimensionIndex;
q _start;
q _length;
```

## Instance methods

```
-[MPSGraphSliceOp initWithGraph:inputTensors:controlDependencies:dimension:start:length:name:];
-[MPSGraphSliceOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphSliceOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
