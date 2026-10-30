# `MPSCNNConvolutionTransposeGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 5 instance variables, 5 properties, 21 instance methods, 1 class methods

## Instance variables

```
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _groups;
Q _gradientOption;
@"MPSCNNConvolutionGradient" _convolutionGradient;
```

## Properties

```
@property (TQ,R,N,V_inputFeatureChannels) sourceGradientFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) sourceImageFeatureChannels;
@property (TQ,R,N,V_groups) groups;
@property (T@"<MPSCNNConvolutionDataSource>",R,&,N) dataSource;
@property (TQ,N,V_gradientOption) gradientOption;
```

## Class methods

```
+[MPSCNNConvolutionTransposeGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNConvolutionTransposeGradient initWithDevice:];
-[MPSCNNConvolutionTransposeGradient maxBatchSize];
-[MPSCNNConvolutionTransposeGradient dealloc];
-[MPSCNNConvolutionTransposeGradient groups];
-[MPSCNNConvolutionTransposeGradient dataSource];
-[MPSCNNConvolutionTransposeGradient copyWithZone:device:];
-[MPSCNNConvolutionTransposeGradient initWithCoder:device:];
-[MPSCNNConvolutionTransposeGradient encodeWithCoder:];
-[MPSCNNConvolutionTransposeGradient isResultStateReusedAcrossBatch];
-[MPSCNNConvolutionTransposeGradient weights];
-[MPSCNNConvolutionTransposeGradient initWithDevice:weights:];
-[MPSCNNConvolutionTransposeGradient reloadWeightsAndBiasesWithCommandBuffer:state:];
-[MPSCNNConvolutionTransposeGradient setGradientOption:];
-[MPSCNNConvolutionTransposeGradient biases];
-[MPSCNNConvolutionTransposeGradient reloadWeightsAndBiasesFromDataSource];
-[MPSCNNConvolutionTransposeGradient PeakAtWeights:];
-[MPSCNNConvolutionTransposeGradient destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSCNNConvolutionTransposeGradient filterHandlesPlugin];
-[MPSCNNConvolutionTransposeGradient gradientOption];
-[MPSCNNConvolutionTransposeGradient sourceGradientFeatureChannels];
-[MPSCNNConvolutionTransposeGradient sourceImageFeatureChannels];
```
