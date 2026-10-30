# `MPSMatrixFullyConnectedGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixBinaryKernel`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
Q _sourceNumberOfFeatureVectors;
Q _sourceInputFeatureChannels;
Q _sourceOutputFeatureChannels;
d _alpha;
```

## Properties

```
@property (TQ,N,V_sourceNumberOfFeatureVectors) sourceNumberOfFeatureVectors;
@property (TQ,N,V_sourceOutputFeatureChannels) sourceOutputFeatureChannels;
@property (TQ,N,V_sourceInputFeatureChannels) sourceInputFeatureChannels;
@property (Td,N,V_alpha) alpha;
```

## Class methods

```
+[MPSMatrixFullyConnectedGradient libraryInfo:];
```

## Instance methods

```
-[MPSMatrixFullyConnectedGradient initWithDevice:];
-[MPSMatrixFullyConnectedGradient setAlpha:];
-[MPSMatrixFullyConnectedGradient copyWithZone:device:];
-[MPSMatrixFullyConnectedGradient initWithCoder:device:];
-[MPSMatrixFullyConnectedGradient encodeWithCoder:];
-[MPSMatrixFullyConnectedGradient alpha];
-[MPSMatrixFullyConnectedGradient setSourceOutputFeatureChannels:];
-[MPSMatrixFullyConnectedGradient setSourceInputFeatureChannels:];
-[MPSMatrixFullyConnectedGradient encodeGradientForDataToCommandBuffer:gradientMatrix:weightMatrix:resultGradientForDataMatrix:];
-[MPSMatrixFullyConnectedGradient encodeGradientForWeightsAndBiasToCommandBuffer:gradientMatrix:inputMatrix:resultGradientForWeightMatrix:resultGradientForBiasVector:];
-[MPSMatrixFullyConnectedGradient setSourceNumberOfFeatureVectors:];
-[MPSMatrixFullyConnectedGradient sourceInputFeatureChannels];
-[MPSMatrixFullyConnectedGradient sourceNumberOfFeatureVectors];
-[MPSMatrixFullyConnectedGradient sourceOutputFeatureChannels];
```
