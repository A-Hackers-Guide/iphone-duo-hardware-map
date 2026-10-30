# `MPSCNNNeuronGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"MPSNNNeuronDescriptor" _descriptor;
```

## Properties

```
@property (T@"MPSNNNeuronDescriptor",R,N,V_descriptor) descriptor;
```

## Class methods

```
+[MPSCNNNeuronGradientNode nodeWithSourceGradient:sourceImage:gradientState:descriptor:];
```

## Instance methods

```
-[MPSCNNNeuronGradientNode descriptor];
-[MPSCNNNeuronGradientNode dealloc];
-[MPSCNNNeuronGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNNeuronGradientNode initWithSourceGradient:sourceImage:gradientState:descriptor:];
-[MPSCNNNeuronGradientNode newFilterNode];
```
