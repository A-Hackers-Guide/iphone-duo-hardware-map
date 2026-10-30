# `MPSCNNBinaryConvolutionNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNConvolutionNode`
- 7 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
f _scaleValue;
Q _type;
Q _flags;
^f _outputBiasTerms;
^f _outputScaleTerms;
^f _inputBiasTerms;
^f _inputScaleTerms;
```

## Properties

```
@property (T@"MPSCNNConvolutionGradientStateNode",R,N) convolutionGradientState;
```

## Class methods

```
+[MPSCNNBinaryConvolutionNode nodeWithSource:weights:outputBiasTerms:outputScaleTerms:inputBiasTerms:inputScaleTerms:type:flags:];
+[MPSCNNBinaryConvolutionNode nodeWithSource:weights:scaleValue:type:flags:];
```

## Instance methods

```
-[MPSCNNBinaryConvolutionNode dealloc];
-[MPSCNNBinaryConvolutionNode convolutionGradientState];
-[MPSCNNBinaryConvolutionNode convolutionState];
-[MPSCNNBinaryConvolutionNode initWithSource:weights:outputBiasTerms:outputScaleTerms:inputBiasTerms:inputScaleTerms:type:flags:];
-[MPSCNNBinaryConvolutionNode initWithSource:weights:scaleValue:type:flags:];
-[MPSCNNBinaryConvolutionNode newFilterNode];
```
