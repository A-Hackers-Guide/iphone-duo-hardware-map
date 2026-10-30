# `MPSNNGramMatrixCalculationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 2 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
{MPSCNNGramGradientFilters_s="fwdFilters"{MPSCNNGramFilters_s="i2mCopy"@"MPSImageCopyToMatrix""m2iCopy"@"MPSMatrixCopyToImage""gemm_TN"@"MPSMatrixMultiplication"}"gemm_NN"@"MPSMatrixMultiplication"} _filters;
f _alpha;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
```

## Class methods

```
+[MPSNNGramMatrixCalculationGradient libraryInfo:];
```

## Instance methods

```
-[MPSNNGramMatrixCalculationGradient initWithDevice:];
-[MPSNNGramMatrixCalculationGradient debugDescription];
-[MPSNNGramMatrixCalculationGradient dealloc];
-[MPSNNGramMatrixCalculationGradient setAlpha:];
-[MPSNNGramMatrixCalculationGradient copyWithZone:device:];
-[MPSNNGramMatrixCalculationGradient initWithCoder:device:];
-[MPSNNGramMatrixCalculationGradient encodeWithCoder:];
-[MPSNNGramMatrixCalculationGradient alpha];
-[MPSNNGramMatrixCalculationGradient initWithDevice:alpha:];
```
