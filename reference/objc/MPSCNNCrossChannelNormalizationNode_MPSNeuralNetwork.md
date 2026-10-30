# `MPSCNNCrossChannelNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNNormalizationNode`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
Q _kernelSizeInFeatureChannels;
```

## Properties

```
@property (TQ,N,V_kernelSizeInFeatureChannels) kernelSizeInFeatureChannels;
```

## Class methods

```
+[MPSCNNCrossChannelNormalizationNode nodeWithSource:kernelSize:];
```

## Instance methods

```
-[MPSCNNCrossChannelNormalizationNode initWithSource:];
-[MPSCNNCrossChannelNormalizationNode setKernelSizeInFeatureChannels:];
-[MPSCNNCrossChannelNormalizationNode gradientClass];
-[MPSCNNCrossChannelNormalizationNode initWithSource:kernelSize:];
-[MPSCNNCrossChannelNormalizationNode kernelSizeInFeatureChannels];
-[MPSCNNCrossChannelNormalizationNode newFilterNode];
```
