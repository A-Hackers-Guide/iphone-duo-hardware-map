# `MPSGraphQuantizedGatherOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 6 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
B _hasZeroPoint;
B _hasMin;
q _axis;
Q _batchDims;
B _allowNegativeIndices;
I _dequantDataType;
```

## Instance methods

```
-[MPSGraphQuantizedGatherOp initWithGraph:inputTensors:controlDependencies:hasZeroPoint:hasMin:dequantDataType:axis:batchDimensions:name:];
-[MPSGraphQuantizedGatherOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
```
