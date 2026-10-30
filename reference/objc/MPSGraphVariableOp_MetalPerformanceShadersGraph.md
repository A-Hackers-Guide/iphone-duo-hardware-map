# `MPSGraphVariableOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"MPSGraphVariable" _variable;
I _dataType;
@"NSArray" _shape;
```

## Properties

```
@property (T@"MPSGraphVariable",R,N,V_variable) variable;
@property (T@"NSArray",R,N,V_shape) shape;
@property (TI,R,N,V_dataType) dataType;
```

## Instance methods

```
-[MPSGraphVariableOp shape];
-[MPSGraphVariableOp variable];
-[MPSGraphVariableOp dataType];
-[MPSGraphVariableOp initWithGraph:shape:dataType:name:];
-[MPSGraphVariableOp initWithGraph:variableMPSNDArray:name:];
-[MPSGraphVariableOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphVariableOp mpsNDArrayWithDevice:];
-[MPSGraphVariableOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
