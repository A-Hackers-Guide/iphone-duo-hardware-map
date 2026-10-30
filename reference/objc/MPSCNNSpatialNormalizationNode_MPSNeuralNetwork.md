# `MPSCNNSpatialNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNNormalizationNode`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
```

## Properties

```
@property (TQ,N,V_kernelWidth) kernelWidth;
@property (TQ,N,V_kernelHeight) kernelHeight;
```

## Class methods

```
+[MPSCNNSpatialNormalizationNode nodeWithSource:kernelSize:];
```

## Instance methods

```
-[MPSCNNSpatialNormalizationNode initWithSource:];
-[MPSCNNSpatialNormalizationNode kernelHeight];
-[MPSCNNSpatialNormalizationNode kernelWidth];
-[MPSCNNSpatialNormalizationNode setKernelWidth:];
-[MPSCNNSpatialNormalizationNode setKernelHeight:];
-[MPSCNNSpatialNormalizationNode gradientClass];
-[MPSCNNSpatialNormalizationNode initWithSource:kernelSize:];
-[MPSCNNSpatialNormalizationNode newFilterNode];
```
