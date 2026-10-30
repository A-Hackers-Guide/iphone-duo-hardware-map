# `MPSCNNNeuronNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 4 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _type;
f _a;
f _b;
f _c;
```

## Properties

```
@property (Tf,R,N,V_a) a;
@property (Tf,R,N,V_b) b;
@property (Tf,R,N,V_c) c;
```

## Class methods

```
+[MPSCNNNeuronNode nodeWithSource:descriptor:];
```

## Instance methods

```
-[MPSCNNNeuronNode descriptor];
-[MPSCNNNeuronNode debugDescription];
-[MPSCNNNeuronNode isEqual:];
-[MPSCNNNeuronNode a];
-[MPSCNNNeuronNode b];
-[MPSCNNNeuronNode c];
-[MPSCNNNeuronNode gradientClass];
-[MPSCNNNeuronNode initWithSource:type:a:b:c:];
-[MPSCNNNeuronNode newFilterNode];
```
