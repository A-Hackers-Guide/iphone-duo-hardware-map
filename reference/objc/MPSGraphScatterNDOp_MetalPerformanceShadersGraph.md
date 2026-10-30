# `MPSGraphScatterNDOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q _batchDims;
q _mode;
```

## Instance methods

```
-[MPSGraphScatterNDOp initWithGraph:inputTensors:controlDependencies:batchDimensions:mode:name:];
-[MPSGraphScatterNDOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphScatterNDOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
