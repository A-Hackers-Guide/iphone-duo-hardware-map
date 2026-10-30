# `MPSCNNArithmeticGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 11 instance variables, 7 properties, 24 instance methods, 1 class methods

## Instance variables

```
f _primaryScale;
f _secondaryScale;
f _bias;
f _minimumValue;
f _maximumValue;
Q _secondaryStrideInFeatureChannels;
i _arithmeticType;
B _isSecondarySourceFilter;
@"MPSNNReduceUnary" _reduceRows;
@"MPSNNReduceUnary" _reduceColumns;
@"MPSNNReduceUnary" _reduceFeatureChannels;
```

## Properties

```
@property (Tf,N,V_primaryScale) primaryScale;
@property (Tf,N,V_secondaryScale) secondaryScale;
@property (Tf,N,V_bias) bias;
@property (TQ,N,V_secondaryStrideInFeatureChannels) secondaryStrideInFeatureChannels;
@property (Tf,N,V_minimumValue) minimumValue;
@property (Tf,N,V_maximumValue) maximumValue;
@property (TB,R,N,V_isSecondarySourceFilter) isSecondarySourceFilter;
```

## Class methods

```
+[MPSCNNArithmeticGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNArithmeticGradient bias];
-[MPSCNNArithmeticGradient initWithDevice:];
-[MPSCNNArithmeticGradient setMaximumValue:];
-[MPSCNNArithmeticGradient debugDescription];
-[MPSCNNArithmeticGradient maxBatchSize];
-[MPSCNNArithmeticGradient dealloc];
-[MPSCNNArithmeticGradient setMinimumValue:];
-[MPSCNNArithmeticGradient copyWithZone:device:];
-[MPSCNNArithmeticGradient initWithCoder:device:];
-[MPSCNNArithmeticGradient encodeWithCoder:];
-[MPSCNNArithmeticGradient minimumValue];
-[MPSCNNArithmeticGradient maximumValue];
-[MPSCNNArithmeticGradient setBias:];
-[MPSCNNArithmeticGradient setSecondaryStrideInPixelsX:];
-[MPSCNNArithmeticGradient setSecondaryStrideInPixelsY:];
-[MPSCNNArithmeticGradient secondaryScale];
-[MPSCNNArithmeticGradient setPrimaryScale:];
-[MPSCNNArithmeticGradient setSecondaryScale:];
-[MPSCNNArithmeticGradient primaryScale];
-[MPSCNNArithmeticGradient destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSCNNArithmeticGradient initWithDevice:arithmeticType:isSecondarySourceFilter:];
-[MPSCNNArithmeticGradient isSecondarySourceFilter];
-[MPSCNNArithmeticGradient secondaryStrideInFeatureChannels];
-[MPSCNNArithmeticGradient setSecondaryStrideInFeatureChannels:];
```
