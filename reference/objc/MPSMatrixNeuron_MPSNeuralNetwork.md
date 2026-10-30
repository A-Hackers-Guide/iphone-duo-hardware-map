# `MPSMatrixNeuron`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixUnaryKernel`
- 8 instance variables, 7 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"<MTLBuffer>" neuronAParamBuf;
i _neuronType;
f _neuronA;
f _neuronB;
f _neuronC;
Q _sourceNumberOfFeatureVectors;
Q _sourceInputFeatureChannels;
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
@property (Td,N,V_alpha) alpha;
```

## Class methods

```
+[MPSMatrixNeuron libraryInfo:];
```

## Instance methods

```
-[MPSMatrixNeuron initWithDevice:];
-[MPSMatrixNeuron debugDescription];
-[MPSMatrixNeuron dealloc];
-[MPSMatrixNeuron setAlpha:];
-[MPSMatrixNeuron copyWithZone:device:];
-[MPSMatrixNeuron initWithCoder:device:];
-[MPSMatrixNeuron encodeWithCoder:];
-[MPSMatrixNeuron alpha];
-[MPSMatrixNeuron encodeToCommandBuffer:inputMatrix:biasVector:resultMatrix:];
-[MPSMatrixNeuron setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixNeuron setSourceInputFeatureChannels:];
-[MPSMatrixNeuron neuronB];
-[MPSMatrixNeuron neuronA];
-[MPSMatrixNeuron neuronC];
-[MPSMatrixNeuron neuronType];
-[MPSMatrixNeuron setNeuronType:];
-[MPSMatrixNeuron neuronParameterA];
-[MPSMatrixNeuron neuronParameterB];
-[MPSMatrixNeuron neuronParameterC];
-[MPSMatrixNeuron setNeuronA:];
-[MPSMatrixNeuron setNeuronB:];
-[MPSMatrixNeuron setNeuronC:];
-[MPSMatrixNeuron setNeuronToPReLUWithParametersA:];
-[MPSMatrixNeuron setSourceNumberOfFeatureVectors:];
-[MPSMatrixNeuron sourceInputFeatureChannels];
-[MPSMatrixNeuron sourceNumberOfFeatureVectors];
```
