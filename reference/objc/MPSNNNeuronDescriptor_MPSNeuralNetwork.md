# `MPSNNNeuronDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 5 properties, 20 instance methods, 6 class methods

## Instance variables

```
i _neuronType;
f _a;
f _b;
f _c;
@"NSData" _data;
B _noCopy;
Q _count;
```

## Properties

```
@property (Ti,N,V_neuronType) neuronType;
@property (Tf,N,V_a) a;
@property (Tf,N,V_b) b;
@property (Tf,N,V_c) c;
@property (T@"NSData",&,N,V_data) data;
```

## Class methods

```
+[MPSNNNeuronDescriptor supportsSecureCoding];
+[MPSNNNeuronDescriptor cnnNeuronDescriptorWithType:];
+[MPSNNNeuronDescriptor cnnNeuronDescriptorWithType:a:];
+[MPSNNNeuronDescriptor cnnNeuronDescriptorWithType:a:b:];
+[MPSNNNeuronDescriptor cnnNeuronDescriptorWithType:a:b:c:];
+[MPSNNNeuronDescriptor cnnNeuronPReLUDescriptorWithData:noCopy:];
```

## Instance methods

```
-[MPSNNNeuronDescriptor debugDescription];
-[MPSNNNeuronDescriptor data];
-[MPSNNNeuronDescriptor dealloc];
-[MPSNNNeuronDescriptor setData:];
-[MPSNNNeuronDescriptor encodeWithCoder:];
-[MPSNNNeuronDescriptor initWithCoder:];
-[MPSNNNeuronDescriptor copyWithZone:];
-[MPSNNNeuronDescriptor a];
-[MPSNNNeuronDescriptor b];
-[MPSNNNeuronDescriptor c];
-[MPSNNNeuronDescriptor setC:];
-[MPSNNNeuronDescriptor setA:];
-[MPSNNNeuronDescriptor setB:];
-[MPSNNNeuronDescriptor neuronType];
-[MPSNNNeuronDescriptor setNeuronType:];
-[MPSNNNeuronDescriptor initWithType:a:b:c:];
-[MPSNNNeuronDescriptor initWithPReLUWithData:noCopy:];
-[MPSNNNeuronDescriptor initializeWithPReLUWithData:noCopy:];
-[MPSNNNeuronDescriptor initializeWithType:a:b:c:];
-[MPSNNNeuronDescriptor neuronInfo];
```
