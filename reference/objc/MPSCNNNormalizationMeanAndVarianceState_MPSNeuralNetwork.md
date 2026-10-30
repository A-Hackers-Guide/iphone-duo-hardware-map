# `MPSCNNNormalizationMeanAndVarianceState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 1 instance variables, 2 properties, 4 instance methods, 2 class methods

## Instance variables

```
B _initialized;
```

## Properties

```
@property (T@"<MTLBuffer>",R,N) mean;
@property (T@"<MTLBuffer>",R,N) variance;
```

## Class methods

```
+[MPSCNNNormalizationMeanAndVarianceState temporaryStateWithCommandBuffer:bufferSize:];
+[MPSCNNNormalizationMeanAndVarianceState temporaryStateWithCommandBuffer:numberOfFeatureChannels:];
```

## Instance methods

```
-[MPSCNNNormalizationMeanAndVarianceState mean];
-[MPSCNNNormalizationMeanAndVarianceState variance];
-[MPSCNNNormalizationMeanAndVarianceState initWithMean:variance:];
-[MPSCNNNormalizationMeanAndVarianceState initWithDevice:bufferSize:];
```
