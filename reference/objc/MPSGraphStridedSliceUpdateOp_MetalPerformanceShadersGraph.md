# `MPSGraphStridedSliceUpdateOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
I _begin_mask;
I _end_mask;
I _shrink_axis_mask;
```

## Instance methods

```
-[MPSGraphStridedSliceUpdateOp initWithGraph:inputTensors:controlDependencies:startMask:endMask:shrinkAxisMask:name:];
-[MPSGraphStridedSliceUpdateOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphStridedSliceUpdateOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
