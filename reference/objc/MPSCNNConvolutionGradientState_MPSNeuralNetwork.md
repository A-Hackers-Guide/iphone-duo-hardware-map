# `MPSCNNConvolutionGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- Protocols: `MPSImageSizeEncodingState`
- 9 instance variables, 12 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _initialized;
@"MPSCNNConvolution" _convolution;
@"<MTLBuffer>" _intermediateWeightsBuffer;
@"<MTLBuffer>" _intermeidateBiasesBuffer;
Q _numReductionBlocks;
B _needReductionInN;
B _needReductionInXY;
I _weightsLayout;
Q _dimSizeN;
```

## Properties

```
@property (TQ,R,N) numberOfWeightGradients;
@property (TQ,R,N) numberOfBiasGradients;
@property (T@"<MTLBuffer>",R,N) gradientForWeights;
@property (T@"<MTLBuffer>",R,N) gradientForBiases;
@property (T@"MPSCNNConvolution",R,&,N,V_convolution) convolution;
@property (TI,R,N) gradientForWeightsLayout;
@property (TQ,R,N) sourceWidth;
@property (TQ,R,N) sourceHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSCNNConvolutionGradientState temporaryStateWithCommandBuffer:resourceList:convolution:];
+[MPSCNNConvolutionGradientState temporaryStateWithCommandBuffer:resourceList:convolution:weightsLayout:];
```

## Instance methods

```
-[MPSCNNConvolutionGradientState debugDescription];
-[MPSCNNConvolutionGradientState dealloc];
-[MPSCNNConvolutionGradientState initWithResource:];
-[MPSCNNConvolutionGradientState gradientForBiases];
-[MPSCNNConvolutionGradientState gradientForWeights];
-[MPSCNNConvolutionGradientState sourceHeight];
-[MPSCNNConvolutionGradientState sourceWidth];
-[MPSCNNConvolutionGradientState destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
-[MPSCNNConvolutionGradientState initWithResource:weightsLayout:];
-[MPSCNNConvolutionGradientState convolution];
-[MPSCNNConvolutionGradientState gradientForWeightsLayout];
-[MPSCNNConvolutionGradientState initWithDevice:resourceList:convolution:];
-[MPSCNNConvolutionGradientState initWithDevice:resourceList:convolution:weightsLayout:];
-[MPSCNNConvolutionGradientState numberOfBiasGradients];
-[MPSCNNConvolutionGradientState numberOfWeightGradients];
```
