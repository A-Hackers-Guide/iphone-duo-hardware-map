# `MPSCNNConvolutionNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- Protocols: `MPSNNTrainableNode`
- 3 instance variables, 9 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNConvolutionDataSource>" _weights;
Q _accumulatorPrecision;
Q _trainingStyle;
```

## Properties

```
@property (T@"MPSCNNConvolutionStateNode",R,N) convolutionState;
@property (T@"<MPSCNNConvolutionDataSource>",R,N,V_weights) weights;
@property (TQ,N,V_trainingStyle) trainingStyle;
@property (TQ,N,V_accumulatorPrecision) accumulatorPrecision;
@property (T@"MPSCNNConvolutionGradientStateNode",R,N) convolutionGradientState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSCNNConvolutionNode nodeWithSource:weights:];
```

## Instance methods

```
-[MPSCNNConvolutionNode dealloc];
-[MPSCNNConvolutionNode weights];
-[MPSCNNConvolutionNode resultState];
-[MPSCNNConvolutionNode accumulatorPrecision];
-[MPSCNNConvolutionNode convolutionGradientState];
-[MPSCNNConvolutionNode convolutionState];
-[MPSCNNConvolutionNode gradientClass];
-[MPSCNNConvolutionNode initWithSource:weights:];
-[MPSCNNConvolutionNode initWithSource:weights:state:];
-[MPSCNNConvolutionNode newFilterNode];
-[MPSCNNConvolutionNode setAccumulatorPrecision:];
-[MPSCNNConvolutionNode setTrainingStyle:];
-[MPSCNNConvolutionNode trainingStyle];
```
