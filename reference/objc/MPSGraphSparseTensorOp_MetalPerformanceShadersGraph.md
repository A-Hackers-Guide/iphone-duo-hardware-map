# `MPSGraphSparseTensorOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
I _dataType;
@"NSArray" _shape;
Q _sparseStorageType;
```

## Properties

```
@property (T@"NSArray",R,N,V_shape) shape;
@property (TI,R,N,V_dataType) dataType;
@property (TQ,R,N,V_sparseStorageType) sparseStorageType;
```

## Instance methods

```
-[MPSGraphSparseTensorOp shape];
-[MPSGraphSparseTensorOp dataType];
-[MPSGraphSparseTensorOp initWithGraph:sparseStorageType:inputTensors:shape:dataType:name:];
-[MPSGraphSparseTensorOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphSparseTensorOp sparseStorageType];
```
