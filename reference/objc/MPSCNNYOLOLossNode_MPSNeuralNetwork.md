# `MPSCNNYOLOLossNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 2 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"MPSNNLabelsNode" _labels;
@"MPSCNNYOLOLossDescriptor" _descriptor;
```

## Properties

```
@property (T@"MPSNNLabelsNode",R,&,N,V_labels) inputLabels;
```

## Class methods

```
+[MPSCNNYOLOLossNode nodeWithSource:lossDescriptor:];
```

## Instance methods

```
-[MPSCNNYOLOLossNode dealloc];
-[MPSCNNYOLOLossNode gradientFilterWithSources:];
-[MPSCNNYOLOLossNode initWithSource:lossDescriptor:];
-[MPSCNNYOLOLossNode inputLabels];
-[MPSCNNYOLOLossNode newFilterNode];
-[MPSCNNYOLOLossNode trainingGraphWithSourceGradient:nodeHandler:];
```
