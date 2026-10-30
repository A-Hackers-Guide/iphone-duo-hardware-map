# `MPSMatrixFullyConnected`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixBinaryKernel`
- 11 instance variables, 8 properties, 28 instance methods, 1 class methods

## Instance variables

```
^? _encode;
@"<MTLBuffer>" neuronAParamBuf;
@"<MPSExternalMatrixFullyConnected>" _plugin;
i _neuronType;
f _neuronA;
f _neuronB;
f _neuronC;
Q _sourceNumberOfFeatureVectors;
Q _sourceInputFeatureChannels;
Q _sourceOutputFeatureChannels;
d _alpha;
```

## Properties

```
@property (Ti,N,V_neuronType) neuronType;
@property (Tf,N,V_neuronA) neuronA;
@property (Tf,N,V_neuronB) neuronB;
@property (Tf,N,V_neuronC) neuronC;
@property (TQ,N,V_sourceNumberOfFeatureVectors) sourceNumberOfFeatureVectors;
@property (TQ,N,V_sourceInputFeatureChannels) sourceInputFeatureChannels;
@property (TQ,N,V_sourceOutputFeatureChannels) sourceOutputFeatureChannels;
@property (Td,N,V_alpha) alpha;
```

## Class methods

```
+[MPSMatrixFullyConnected libraryInfo:];
```

## Instance methods

```
-[MPSMatrixFullyConnected initWithDevice:];
-[MPSMatrixFullyConnected debugDescription];
-[MPSMatrixFullyConnected dealloc];
-[MPSMatrixFullyConnected setAlpha:];
-[MPSMatrixFullyConnected copyWithZone:device:];
-[MPSMatrixFullyConnected initWithCoder:device:];
-[MPSMatrixFullyConnected encodeWithCoder:];
-[MPSMatrixFullyConnected alpha];
-[MPSMatrixFullyConnected setSourceOutputFeatureChannels:];
-[MPSMatrixFullyConnected encodeToCommandBuffer:inputMatrix:weightMatrix:biasVector:resultMatrix:];
-[MPSMatrixFullyConnected setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixFullyConnected setSourceInputFeatureChannels:];
-[MPSMatrixFullyConnected neuronB];
-[MPSMatrixFullyConnected neuronA];
-[MPSMatrixFullyConnected neuronC];
-[MPSMatrixFullyConnected neuronType];
-[MPSMatrixFullyConnected setNeuronType:];
-[MPSMatrixFullyConnected neuronParameterA];
-[MPSMatrixFullyConnected neuronParameterB];
-[MPSMatrixFullyConnected neuronParameterC];
-[MPSMatrixFullyConnected setNeuronA:];
-[MPSMatrixFullyConnected setNeuronB:];
-[MPSMatrixFullyConnected setNeuronC:];
-[MPSMatrixFullyConnected setNeuronToPReLUWithParametersA:];
-[MPSMatrixFullyConnected setSourceNumberOfFeatureVectors:];
-[MPSMatrixFullyConnected sourceInputFeatureChannels];
-[MPSMatrixFullyConnected sourceNumberOfFeatureVectors];
-[MPSMatrixFullyConnected sourceOutputFeatureChannels];
```
