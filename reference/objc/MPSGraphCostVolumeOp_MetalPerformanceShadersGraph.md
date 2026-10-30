# `MPSGraphCostVolumeOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 11 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
B _normalizeCoordinates;
B _relativeCoordinates;
B _alignCorners;
B _coordinateIs1DInWidth;
q _paddingMode;
Q _samplingMode;
Q _nearestRoundingMode;
Q _layout;
Q _similarity;
Q _windowWidth;
Q _windowHeight;
```

## Instance methods

```
-[MPSGraphCostVolumeOp initWithGraph:inputTensors:controlDependencies:layout:normalizeCoordinates:relativeCoordinates:alignCorners:coordinateIs1DInWidth:paddingMode:samplingMode:nearestRoundingMode:similarityType:windowWidth:windowHeight:name:];
-[MPSGraphCostVolumeOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphCostVolumeOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
