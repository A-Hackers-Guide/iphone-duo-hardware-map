# `MPSCNNConvolutionGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- Protocols: `MPSNNTrainableNode`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNConvolutionDataSource>" _weights;
Q _trainingStyle;
```

## Properties

```
@property (T@"<MPSCNNConvolutionDataSource>",R,N,V_weights) weights;
@property (TQ,N,V_trainingStyle) trainingStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSCNNConvolutionGradientNode nodeWithSourceGradient:sourceImage:convolutionGradientState:weights:];
```

## Instance methods

```
-[MPSCNNConvolutionGradientNode debugDescription];
-[MPSCNNConvolutionGradientNode dealloc];
-[MPSCNNConvolutionGradientNode weights];
-[MPSCNNConvolutionGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNConvolutionGradientNode initWithSourceGradient:sourceImage:convolutionGradientState:weights:];
-[MPSCNNConvolutionGradientNode initWithSourceGradient:sourceImage:gradientState:weights:];
-[MPSCNNConvolutionGradientNode newFilterNode];
-[MPSCNNConvolutionGradientNode setTrainingStyle:];
-[MPSCNNConvolutionGradientNode trainingStyle];
```
