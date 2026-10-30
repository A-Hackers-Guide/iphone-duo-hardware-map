# `MPSGraphSampleGridOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 7 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
B _normalizeCoordinates;
B _relativeCoordinates;
B _alignCorners;
q _paddingMode;
Q _samplingMode;
Q _nearestRoundingMode;
Q _layout;
```

## Instance methods

```
-[MPSGraphSampleGridOp initWithGraph:inputTensors:controlDependencies:layout:normalizeCoordinates:relativeCoordinates:alignCorners:paddingMode:samplingMode:nearestRoundingMode:name:];
-[MPSGraphSampleGridOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphSampleGridOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
