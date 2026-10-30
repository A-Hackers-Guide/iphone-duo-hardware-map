# `MPSMatrixSum`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 9 instance variables, 12 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _transpose;
i _neuronType;
f _neuronA;
f _neuronB;
f _neuronC;
Q _rows;
Q _columns;
Q _count;
{?="x"Q"y"Q"z"Q} _resultMatrixOrigin;
```

## Properties

```
@property (Ti,N,V_neuronType) neuronType;
@property (Tf,N,V_neuronA) neuronA;
@property (Tf,N,V_neuronB) neuronB;
@property (Tf,N,V_neuronC) neuronC;
@property (TQ,R,N,V_rows) rows;
@property (TQ,R,N,V_columns) columns;
@property (TQ,R,N,V_count) count;
@property (TB,R,N,V_transpose) transpose;
@property (T{?=QQQ},N,V_resultMatrixOrigin) resultMatrixOrigin;
@property (Tf,R,N) neuronParameterA;
@property (Tf,R,N) neuronParameterB;
@property (Tf,R,N) neuronParameterC;
```

## Class methods

```
+[MPSMatrixSum libraryInfo:];
```

## Instance methods

```
-[MPSMatrixSum columns];
-[MPSMatrixSum initWithDevice:];
-[MPSMatrixSum rows];
-[MPSMatrixSum count];
-[MPSMatrixSum initWithCoder:device:];
-[MPSMatrixSum setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixSum neuronB];
-[MPSMatrixSum neuronA];
-[MPSMatrixSum neuronC];
-[MPSMatrixSum encodeToCommandBuffer:sourceMatrices:resultMatrix:scaleVector:offsetVector:biasVector:startIndex:];
-[MPSMatrixSum initWithDevice:count:rows:columns:transpose:];
-[MPSMatrixSum neuronType];
-[MPSMatrixSum setResultMatrixOrigin:];
-[MPSMatrixSum setNeuronType:];
-[MPSMatrixSum resultMatrixOrigin];
-[MPSMatrixSum transpose];
-[MPSMatrixSum encodeToCommandBuffer:encoder:sourceMatrices:resultMatrix:scaleVector:offsetVector:biasVector:startIndex:];
-[MPSMatrixSum neuronParameterA];
-[MPSMatrixSum neuronParameterB];
-[MPSMatrixSum neuronParameterC];
-[MPSMatrixSum setNeuronA:];
-[MPSMatrixSum setNeuronB:];
-[MPSMatrixSum setNeuronC:];
```
