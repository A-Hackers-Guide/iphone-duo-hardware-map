# `MPSCNNCrossChannelNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _kernelSize;
f _alpha;
f _beta;
f _delta;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
@property (TQ,R,N,V_kernelSize) kernelSize;
```

## Class methods

```
+[MPSCNNCrossChannelNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNCrossChannelNormalization initWithDevice:];
-[MPSCNNCrossChannelNormalization debugDescription];
-[MPSCNNCrossChannelNormalization setAlpha:];
-[MPSCNNCrossChannelNormalization copyWithZone:device:];
-[MPSCNNCrossChannelNormalization initWithCoder:device:];
-[MPSCNNCrossChannelNormalization encodeWithCoder:];
-[MPSCNNCrossChannelNormalization alpha];
-[MPSCNNCrossChannelNormalization delta];
-[MPSCNNCrossChannelNormalization setDelta:];
-[MPSCNNCrossChannelNormalization encodeBatchToCommandBuffer:sourceImages:destinationImages:];
-[MPSCNNCrossChannelNormalization encodeToCommandBuffer:sourceImage:destinationImage:];
-[MPSCNNCrossChannelNormalization initWithDevice:kernelSize:];
-[MPSCNNCrossChannelNormalization setBeta:];
-[MPSCNNCrossChannelNormalization beta];
-[MPSCNNCrossChannelNormalization encodeBatchToCommandBuffer:sourceImages:];
-[MPSCNNCrossChannelNormalization encodeToCommandBuffer:sourceImage:];
-[MPSCNNCrossChannelNormalization kernelSize];
```
