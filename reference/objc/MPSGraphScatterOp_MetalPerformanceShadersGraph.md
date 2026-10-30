# `MPSGraphScatterOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
q _axis;
q _mode;
```

## Instance methods

```
-[MPSGraphScatterOp initWithGraph:inputTensors:controlDependencies:axis:mode:name:];
-[MPSGraphScatterOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphScatterOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
