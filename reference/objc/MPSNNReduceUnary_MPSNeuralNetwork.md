# `MPSNNReduceUnary`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 3 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRectSource;
i _reduceOp;
f _weightValue;
```

## Properties

```
@property (T{?={?=QQQ}{?=QQQ}},N,V_clipRectSource) clipRectSource;
@property (T{?=qqq},N) offset;
```

## Class methods

```
+[MPSNNReduceUnary libraryInfo:];
```

## Instance methods

```
-[MPSNNReduceUnary initWithDevice:];
-[MPSNNReduceUnary debugDescription];
-[MPSNNReduceUnary copyWithZone:device:];
-[MPSNNReduceUnary initWithCoder:device:];
-[MPSNNReduceUnary encodeWithCoder:];
-[MPSNNReduceUnary setClipRectSource:];
-[MPSNNReduceUnary initWithDevice:reduceOperation:];
-[MPSNNReduceUnary clipRectSource];
-[MPSNNReduceUnary setWeightValue:];
```
