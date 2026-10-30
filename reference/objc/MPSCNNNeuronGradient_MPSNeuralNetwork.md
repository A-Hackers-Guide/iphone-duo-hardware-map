# `MPSCNNNeuronGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 8 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
i _neuronType;
f _a;
f _b;
f _c;
@"NSData" _data;
B _noCopy;
Q _count;
@"<MTLBuffer>" _aBuf;
```

## Properties

```
@property (Ti,R,N,V_neuronType) neuronType;
@property (Tf,R,N,V_a) a;
@property (Tf,R,N,V_b) b;
@property (Tf,R,N,V_c) c;
@property (T@"NSData",R,&,N,V_data) data;
```

## Class methods

```
+[MPSCNNNeuronGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNNeuronGradient initWithDevice:];
-[MPSCNNNeuronGradient debugDescription];
-[MPSCNNNeuronGradient data];
-[MPSCNNNeuronGradient dealloc];
-[MPSCNNNeuronGradient copyWithZone:device:];
-[MPSCNNNeuronGradient initWithCoder:device:];
-[MPSCNNNeuronGradient encodeWithCoder:];
-[MPSCNNNeuronGradient a];
-[MPSCNNNeuronGradient b];
-[MPSCNNNeuronGradient initWithDevice:neuronDescriptor:];
-[MPSCNNNeuronGradient c];
-[MPSCNNNeuronGradient neuronType];
-[MPSCNNNeuronGradient initializeWithNeuronType:neuronParameterA:count:];
-[MPSCNNNeuronGradient initializeWithNeuronType:neuronParameterA:neuronParameterB:neuronParameterC:];
-[MPSCNNNeuronGradient privateInitWithDevice:a:b:c:type:];
-[MPSCNNNeuronGradient privateInitWithDevice:a:count:type:];
```
