# `MPSCNNDropout`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 4 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
f _keepProbability;
Q _seed;
{?="width"Q"height"Q"depth"Q} _maskStrideInPixels;
@"MPSParallelRandomMTGP32" _parallelGenerator;
```

## Properties

```
@property (Tf,R,N,V_keepProbability) keepProbability;
@property (TQ,R,N,V_seed) seed;
@property (T{?=QQQ},R,N,V_maskStrideInPixels) maskStrideInPixels;
```

## Class methods

```
+[MPSCNNDropout libraryInfo:];
```

## Instance methods

```
-[MPSCNNDropout seed];
-[MPSCNNDropout debugDescription];
-[MPSCNNDropout dealloc];
-[MPSCNNDropout resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNDropout copyWithZone:device:];
-[MPSCNNDropout initWithCoder:device:];
-[MPSCNNDropout temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNDropout encodeWithCoder:];
-[MPSCNNDropout resultStateBatchForSourceImage:sourceStates:destinationImage:];
-[MPSCNNDropout initWithDevice:keepProbability:seed:maskStrideInPixels:];
-[MPSCNNDropout resetSeedOnCommandBuffer:seed:];
-[MPSCNNDropout keepProbability];
-[MPSCNNDropout exportRandomState];
-[MPSCNNDropout initWithDevice:keepProbability:state:maskStrideInPixels:];
-[MPSCNNDropout maskStrideInPixels];
-[MPSCNNDropout privateResultStateForSourceImage:sourceStates:destinationImage:commandBuffer:isTemporary:];
-[MPSCNNDropout synchronizeRandomStateOnCommandBuffer:];
-[MPSCNNDropout temporaryResultStateBatchForCommandBuffer:sourceImage:sourceStates:destinationImage:];
```
