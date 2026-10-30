# `MPSGraphConstantOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 4 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSData" _data;
B _isSplat;
I _dataType;
@"NSArray" _shape;
```

## Properties

```
@property (T@"NSArray",R,N,V_shape) shape;
@property (TI,R,N,V_dataType) dataType;
```

## Instance methods

```
-[MPSGraphConstantOp shape];
-[MPSGraphConstantOp dataType];
-[MPSGraphConstantOp initWithGraph:data:shape:dataType:isSplat:name:];
-[MPSGraphConstantOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
```
