# `MPSGraphPlaceholderOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
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
-[MPSGraphPlaceholderOp shape];
-[MPSGraphPlaceholderOp dataType];
-[MPSGraphPlaceholderOp initWithGraph:shape:dataType:name:];
-[MPSGraphPlaceholderOp initWithGraph:shape:dataType:value:name:];
-[MPSGraphPlaceholderOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
```
