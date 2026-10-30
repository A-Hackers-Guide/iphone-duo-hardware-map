# `MPSCNNConvolutionTransposeNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNConvolutionNode`
- 0 instance variables, 1 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"MPSCNNConvolutionGradientStateNode",R,N) convolutionGradientState;
```

## Class methods

```
+[MPSCNNConvolutionTransposeNode nodeWithSource:convolutionGradientState:weights:];
+[MPSCNNConvolutionTransposeNode nodeWithSource:convolutionState:weights:];
```

## Instance methods

```
-[MPSCNNConvolutionTransposeNode resultState];
-[MPSCNNConvolutionTransposeNode convolutionGradientState];
-[MPSCNNConvolutionTransposeNode convolutionState];
-[MPSCNNConvolutionTransposeNode gradientClass];
-[MPSCNNConvolutionTransposeNode initWithSource:convolutionGradientState:weights:];
-[MPSCNNConvolutionTransposeNode initWithSource:convolutionState:weights:];
-[MPSCNNConvolutionTransposeNode newFilterNode];
```
