# `MPSMatrixNeuronGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSMatrixBinaryKernel`
- 8 instance variables, 7 properties, 25 instance methods, 1 class methods

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
+[MPSMatrixNeuronGradient libraryInfo:];
```

## Instance methods

```
-[MPSMatrixNeuronGradient initWithDevice:];
-[MPSMatrixNeuronGradient dealloc];
-[MPSMatrixNeuronGradient setAlpha:];
-[MPSMatrixNeuronGradient copyWithZone:device:];
-[MPSMatrixNeuronGradient initWithCoder:device:];
-[MPSMatrixNeuronGradient encodeWithCoder:];
-[MPSMatrixNeuronGradient alpha];
-[MPSMatrixNeuronGradient setNeuronType:parameterA:parameterB:parameterC:];
-[MPSMatrixNeuronGradient setSourceInputFeatureChannels:];
-[MPSMatrixNeuronGradient neuronB];
-[MPSMatrixNeuronGradient neuronA];
-[MPSMatrixNeuronGradient neuronC];
-[MPSMatrixNeuronGradient encodeToCommandBuffer:gradientMatrix:inputMatrix:biasVector:resultGradientForDataMatrix:resultGradientForBiasVector:];
-[MPSMatrixNeuronGradient neuronType];
-[MPSMatrixNeuronGradient setNeuronType:];
-[MPSMatrixNeuronGradient neuronParameterA];
-[MPSMatrixNeuronGradient neuronParameterB];
-[MPSMatrixNeuronGradient neuronParameterC];
-[MPSMatrixNeuronGradient setNeuronA:];
-[MPSMatrixNeuronGradient setNeuronB:];
-[MPSMatrixNeuronGradient setNeuronC:];
-[MPSMatrixNeuronGradient setNeuronToPReLUWithParametersA:];
-[MPSMatrixNeuronGradient setSourceNumberOfFeatureVectors:];
-[MPSMatrixNeuronGradient sourceInputFeatureChannels];
-[MPSMatrixNeuronGradient sourceNumberOfFeatureVectors];
```
