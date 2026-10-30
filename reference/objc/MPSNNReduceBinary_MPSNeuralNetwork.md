# `MPSNNReduceBinary`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNBinaryKernel`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRectPrimarySource;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _secondarySourceClipRect;
i _reduceOp;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _primarySourceClipRect;
```

## Properties

```
@property (T{?={?=QQQ}{?=QQQ}},N,V_primarySourceClipRect) primarySourceClipRect;
@property (T{?={?=QQQ}{?=QQQ}},N,V_secondarySourceClipRect) secondarySourceClipRect;
@property (T{?=qqq},N) primaryOffset;
@property (T{?=qqq},N) secondaryOffset;
```

## Class methods

```
+[MPSNNReduceBinary libraryInfo:];
```

## Instance methods

```
-[MPSNNReduceBinary initWithDevice:];
-[MPSNNReduceBinary debugDescription];
-[MPSNNReduceBinary copyWithZone:device:];
-[MPSNNReduceBinary initWithCoder:device:];
-[MPSNNReduceBinary encodeWithCoder:];
-[MPSNNReduceBinary initWithDevice:reduceOperation:];
-[MPSNNReduceBinary primarySourceClipRect];
-[MPSNNReduceBinary reduceOp];
-[MPSNNReduceBinary secondarySourceClipRect];
-[MPSNNReduceBinary setPrimarySourceClipRect:];
-[MPSNNReduceBinary setSecondarySourceClipRect:];
```
