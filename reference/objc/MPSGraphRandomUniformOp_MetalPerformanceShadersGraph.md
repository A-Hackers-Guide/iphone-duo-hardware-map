# `MPSGraphRandomUniformOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
I _dataType;
f _maximum;
f _minimum;
Q _minInteger;
Q _maxInteger;
```

## Instance methods

```
-[MPSGraphRandomUniformOp initWithGraph:inputTensors:controlDependencies:descriptor:name:];
-[MPSGraphRandomUniformOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphRandomUniformOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
