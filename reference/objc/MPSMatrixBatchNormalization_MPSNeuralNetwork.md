# `MPSMatrixBatchNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixUnaryKernel`
- 8 instance variables, 8 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _computeStatistics;
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
@property (TB,N,V_computeStatistics) computeStatistics;
```

## Class methods

```
+[MPSMatrixBatchNormalization libraryInfo:];
```

## Instance methods

```
-[MPSMatrixBatchNormalization initWithDevice:];
-[MPSMatrixBatchNormalization debugDescription];
-[MPSMatrixBatchNormalization copyWithZone:device:];
-[MPSMatrixBatchNormalization initWithCoder:device:];
-[MPSMatrixBatchNormalization encodeWithCoder:];
-[MPSMatrixBatchNormalization setEpsilon:];
-[MPSMatrixBatchNormalization epsilon];
-[MPSMatrixBatchNormalization setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixBatchNormalization setSourceInputFeatureChannels:];
-[MPSMatrixBatchNormalization neuronB];
-[MPSMatrixBatchNormalization neuronA];
-[MPSMatrixBatchNormalization neuronC];
-[MPSMatrixBatchNormalization neuronType];
-[MPSMatrixBatchNormalization setNeuronType:];
-[MPSMatrixBatchNormalization computeStatistics];
-[MPSMatrixBatchNormalization encodeToCommandBuffer:inputMatrix:meanVector:varianceVector:gammaVector:betaVector:resultMatrix:];
-[MPSMatrixBatchNormalization neuronParameterA];
-[MPSMatrixBatchNormalization neuronParameterB];
-[MPSMatrixBatchNormalization neuronParameterC];
-[MPSMatrixBatchNormalization setComputeStatistics:];
-[MPSMatrixBatchNormalization setNeuronA:];
-[MPSMatrixBatchNormalization setNeuronB:];
-[MPSMatrixBatchNormalization setNeuronC:];
-[MPSMatrixBatchNormalization setSourceNumberOfFeatureVectors:];
-[MPSMatrixBatchNormalization sourceInputFeatureChannels];
-[MPSMatrixBatchNormalization sourceNumberOfFeatureVectors];
```
