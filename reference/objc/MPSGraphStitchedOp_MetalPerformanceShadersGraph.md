# `MPSGraphStitchedOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@? _stitchingBlock;
@"MPSGraphTensor" _finalOutputTensorForStitchedRegion;
@"NSArray" _opsAddedInStitchedRegion;
```

## Instance methods

```
-[MPSGraphStitchedOp initWithGraph:withBlock:inputTensors:controlDependencies:name:];
-[MPSGraphStitchedOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphStitchedOp recurseOperation:builder:symbolTable:tensorToValueMap:operationsRecursed:];
```
