# `MPSGraphRandomTruncatedNormalOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 6 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
I _dataType;
Q _samplingMethod;
f _mean;
f _standardDeviation;
f _maximum;
f _minimum;
```

## Instance methods

```
-[MPSGraphRandomTruncatedNormalOp initWithGraph:inputTensors:controlDependencies:descriptor:name:];
-[MPSGraphRandomTruncatedNormalOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphRandomTruncatedNormalOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
