# `MPSGraphSplitOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
q _dimensionIndex;
Q _numSplits;
```

## Instance methods

```
-[MPSGraphSplitOp initWithGraph:inputTensors:controlDependencies:dimension:name:];
-[MPSGraphSplitOp initWithGraph:inputTensors:controlDependencies:dimension:numSplits:name:];
-[MPSGraphSplitOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphSplitOp partialDerivativesForInputTensors:incomingGradients:name:];
```
