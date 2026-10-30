# `MPSGraphNonMaximumSuppressionOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
f _iouThreshold;
f _scoreThreshold;
B _perClassSuppression;
Q _coordinateMode;
```

## Instance methods

```
-[MPSGraphNonMaximumSuppressionOp initWithGraph:inputTensors:controlDependencies:iouThreshold:scoreThreshold:perClassSuppression:coordinateMode:name:];
-[MPSGraphNonMaximumSuppressionOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphNonMaximumSuppressionOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
