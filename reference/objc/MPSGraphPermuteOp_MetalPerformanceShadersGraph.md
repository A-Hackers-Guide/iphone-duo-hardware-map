# `MPSGraphPermuteOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _permute;
```

## Instance methods

```
-[MPSGraphPermuteOp initWithGraph:inputTensors:controlDependencies:permute:name:];
-[MPSGraphPermuteOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphPermuteOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
