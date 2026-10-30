# `MPSCNNConvolutionTransposeGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNConvolutionGradientState`
- 4 instance variables, 2 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"MPSCNNConvolutionTranspose" _convolutionTranspose;
@"MPSCNNConvolutionGradientState" _convolutionGradientState;
q _kernelOffsetX;
q _kernelOffsetY;
```

## Properties

```
@property (T@"MPSCNNConvolutionGradientState",R,N,V_convolutionGradientState) convolutionGradientState;
@property (T@"MPSCNNConvolutionTranspose",R,&,N,V_convolutionTranspose) convolutionTranspose;
```

## Class methods

```
+[MPSCNNConvolutionTransposeGradientState temporaryStateWithCommandBuffer:resourceList:convolutionTranspose:convolutionGradientState:];
+[MPSCNNConvolutionTransposeGradientState temporaryStateWithCommandBuffer:resourceList:convolutionTranspose:convolutionGradientState:weightsLayout:];
```

## Instance methods

```
-[MPSCNNConvolutionTransposeGradientState debugDescription];
-[MPSCNNConvolutionTransposeGradientState dealloc];
-[MPSCNNConvolutionTransposeGradientState initWithResource:];
-[MPSCNNConvolutionTransposeGradientState sourceHeight];
-[MPSCNNConvolutionTransposeGradientState sourceWidth];
-[MPSCNNConvolutionTransposeGradientState convolutionTranspose];
-[MPSCNNConvolutionTransposeGradientState destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
-[MPSCNNConvolutionTransposeGradientState initWithResource:weightsLayout:];
-[MPSCNNConvolutionTransposeGradientState convolution];
-[MPSCNNConvolutionTransposeGradientState convolutionGradientState];
-[MPSCNNConvolutionTransposeGradientState initWithDevice:resourceList:convolution:];
-[MPSCNNConvolutionTransposeGradientState initWithDevice:resourceList:convolution:weightsLayout:];
-[MPSCNNConvolutionTransposeGradientState initWithDevice:resourceList:convolutionTranspose:convolutionGradientState:];
-[MPSCNNConvolutionTransposeGradientState initWithDevice:resourceList:convolutionTranspose:convolutionGradientState:weightsLayout:];
```
