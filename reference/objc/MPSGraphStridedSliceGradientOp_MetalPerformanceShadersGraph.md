# `MPSGraphStridedSliceGradientOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
I _begin_mask;
I _end_mask;
I _shrink_axis_mask;
B _end_is_size;
```

## Instance methods

```
-[MPSGraphStridedSliceGradientOp initWithGraph:inputTensors:controlDependencies:startMask:endMask:shrinkAxisMask:endIsSize:name:];
-[MPSGraphStridedSliceGradientOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphStridedSliceGradientOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
