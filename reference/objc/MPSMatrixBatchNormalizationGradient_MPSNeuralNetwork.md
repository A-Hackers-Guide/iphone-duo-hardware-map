# `MPSMatrixBatchNormalizationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixBinaryKernel`
- 7 instance variables, 7 properties, 23 instance methods, 1 class methods

## Instance variables

```
i _neuronType;
f _neuronA;
f _neuronB;
f _neuronC;
f _epsilon;
Q _sourceNumberOfFeatureVectors;
Q _sourceInputFeatureChannels;
```

## Properties

```
@property (Ti,N,V_neuronType) neuronType;
@property (Tf,N,V_neuronA) neuronA;
@property (Tf,N,V_neuronB) neuronB;
@property (Tf,N,V_neuronC) neuronC;
@property (TQ,N,V_sourceNumberOfFeatureVectors) sourceNumberOfFeatureVectors;
@property (TQ,N,V_sourceInputFeatureChannels) sourceInputFeatureChannels;
@property (Tf,N,V_epsilon) epsilon;
```

## Class methods

```
+[MPSMatrixBatchNormalizationGradient libraryInfo:];
```

## Instance methods

```
-[MPSMatrixBatchNormalizationGradient initWithDevice:];
-[MPSMatrixBatchNormalizationGradient copyWithZone:device:];
-[MPSMatrixBatchNormalizationGradient initWithCoder:device:];
-[MPSMatrixBatchNormalizationGradient encodeWithCoder:];
-[MPSMatrixBatchNormalizationGradient setEpsilon:];
-[MPSMatrixBatchNormalizationGradient epsilon];
-[MPSMatrixBatchNormalizationGradient setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixBatchNormalizationGradient setSourceInputFeatureChannels:];
-[MPSMatrixBatchNormalizationGradient neuronB];
-[MPSMatrixBatchNormalizationGradient neuronA];
-[MPSMatrixBatchNormalizationGradient neuronC];
-[MPSMatrixBatchNormalizationGradient neuronType];
-[MPSMatrixBatchNormalizationGradient setNeuronType:];
-[MPSMatrixBatchNormalizationGradient encodeToCommandBuffer:gradientMatrix:inputMatrix:meanVector:varianceVector:gammaVector:betaVector:resultGradientForDataMatrix:resultGradientForGammaVector:resultGradientForBetaVector:];
-[MPSMatrixBatchNormalizationGradient neuronParameterA];
-[MPSMatrixBatchNormalizationGradient neuronParameterB];
-[MPSMatrixBatchNormalizationGradient neuronParameterC];
-[MPSMatrixBatchNormalizationGradient setNeuronA:];
-[MPSMatrixBatchNormalizationGradient setNeuronB:];
-[MPSMatrixBatchNormalizationGradient setNeuronC:];
-[MPSMatrixBatchNormalizationGradient setSourceNumberOfFeatureVectors:];
-[MPSMatrixBatchNormalizationGradient sourceInputFeatureChannels];
-[MPSMatrixBatchNormalizationGradient sourceNumberOfFeatureVectors];
```
