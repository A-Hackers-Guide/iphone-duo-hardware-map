# `MPSGraphArithmeticOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 1 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _mathOpType;
```

## Instance methods

```
-[MPSGraphArithmeticOp initWithGraph:inputTensors:controlDependencies:mathOpType:name:];
-[MPSGraphArithmeticOp broadcastGradTernaryWithOutputGradient:inputIndex:name:];
-[MPSGraphArithmeticOp broadcastGradWithOutputGradient:inputIndex:name:];
-[MPSGraphArithmeticOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphArithmeticOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
