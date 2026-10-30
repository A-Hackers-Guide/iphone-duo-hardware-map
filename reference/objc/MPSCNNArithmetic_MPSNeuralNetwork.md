# `MPSCNNArithmetic`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNBinaryKernel`
- 8 instance variables, 7 properties, 31 instance methods, 1 class methods

## Instance variables

```
f _primaryScale;
f _secondaryScale;
f _bias;
f _minimumValue;
f _maximumValue;
Q _primaryStrideInFeatureChannels;
Q _secondaryStrideInFeatureChannels;
i _arithmeticType;
```

## Properties

```
@property (Tf,N,V_primaryScale) primaryScale;
@property (Tf,N,V_secondaryScale) secondaryScale;
@property (Tf,N,V_bias) bias;
@property (TQ,N,V_primaryStrideInFeatureChannels) primaryStrideInFeatureChannels;
@property (TQ,N,V_secondaryStrideInFeatureChannels) secondaryStrideInFeatureChannels;
@property (Tf,N,V_minimumValue) minimumValue;
@property (Tf,N,V_maximumValue) maximumValue;
```

## Class methods

```
+[MPSCNNArithmetic libraryInfo:];
```

## Instance methods

```
-[MPSCNNArithmetic bias];
-[MPSCNNArithmetic initWithDevice:];
-[MPSCNNArithmetic setMaximumValue:];
-[MPSCNNArithmetic debugDescription];
-[MPSCNNArithmetic maxBatchSize];
-[MPSCNNArithmetic setMinimumValue:];
-[MPSCNNArithmetic copyWithZone:device:];
-[MPSCNNArithmetic initWithCoder:device:];
-[MPSCNNArithmetic encodeWithCoder:];
-[MPSCNNArithmetic minimumValue];
-[MPSCNNArithmetic maximumValue];
-[MPSCNNArithmetic setBias:];
-[MPSCNNArithmetic setSecondaryStrideInPixelsX:];
-[MPSCNNArithmetic setSecondaryStrideInPixelsY:];
-[MPSCNNArithmetic secondaryScale];
-[MPSCNNArithmetic setPrimaryScale:];
-[MPSCNNArithmetic setSecondaryScale:];
-[MPSCNNArithmetic initWithDevice:arithmeticType:];
-[MPSCNNArithmetic primaryScale];
-[MPSCNNArithmetic destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSCNNArithmetic encodeBatchToCommandBuffer:primaryImages:secondaryImages:destinationStates:destinationImages:];
-[MPSCNNArithmetic encodeToCommandBuffer:primaryImage:secondaryImage:destinationState:destinationImage:];
-[MPSCNNArithmetic primaryStrideInFeatureChannels];
-[MPSCNNArithmetic privateResultStateForPrimaryImage:secondaryImage:sourceStates:destinationImage:commandBuffer:isTemporary:];
-[MPSCNNArithmetic resultStateForPrimaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNArithmetic secondaryStrideInFeatureChannels];
-[MPSCNNArithmetic setPrimaryStrideInFeatureChannels:];
-[MPSCNNArithmetic setPrimaryStrideInPixelsX:];
-[MPSCNNArithmetic setPrimaryStrideInPixelsY:];
-[MPSCNNArithmetic setSecondaryStrideInFeatureChannels:];
-[MPSCNNArithmetic temporaryResultStateForCommandBuffer:primaryImage:secondaryImage:sourceStates:destinationImage:];
```
