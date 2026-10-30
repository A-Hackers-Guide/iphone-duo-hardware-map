# `MPSGraphBatchToSpaceOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
B _pixelShuffleOrder;
```

## Instance methods

```
-[MPSGraphBatchToSpaceOp initWithGraph:inputTensors:controlDependencies:usePixelShuffleOrder:name:];
-[MPSGraphBatchToSpaceOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphBatchToSpaceOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
