# `MPSNNGramMatrixCalculation`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 3 instance variables, 1 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"<MPSNNGramMatrixCallback>" _propertyCallback;
{MPSCNNGramFilters_s="i2mCopy"@"MPSImageCopyToMatrix""m2iCopy"@"MPSMatrixCopyToImage""gemm_TN"@"MPSMatrixMultiplication"} _filters;
f _alpha;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
```

## Class methods

```
+[MPSNNGramMatrixCalculation libraryInfo:];
```

## Instance methods

```
-[MPSNNGramMatrixCalculation initWithDevice:];
-[MPSNNGramMatrixCalculation debugDescription];
-[MPSNNGramMatrixCalculation dealloc];
-[MPSNNGramMatrixCalculation resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSNNGramMatrixCalculation setAlpha:];
-[MPSNNGramMatrixCalculation copyWithZone:device:];
-[MPSNNGramMatrixCalculation initWithCoder:device:];
-[MPSNNGramMatrixCalculation temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNGramMatrixCalculation encodeWithCoder:];
-[MPSNNGramMatrixCalculation alpha];
-[MPSNNGramMatrixCalculation isResultStateReusedAcrossBatch];
-[MPSNNGramMatrixCalculation destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSNNGramMatrixCalculation initWithDevice:alpha:];
```
