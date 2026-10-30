# `MPSGraphTransposeOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q _dimensionIndex;
Q _dimensionIndex2;
```

## Instance methods

```
-[MPSGraphTransposeOp initWithGraph:inputTensors:controlDependencies:dimension:withDimension:name:];
-[MPSGraphTransposeOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphTransposeOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
