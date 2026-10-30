# `MPSNNBinaryArithmeticNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 11 instance variables, 11 properties, 27 instance methods, 2 class methods

## Instance variables

```
f _primaryScale;
f _secondaryScale;
f _bias;
Q _primaryStrideInPixelsX;
Q _primaryStrideInPixelsY;
Q _primaryStrideInFeatureChannels;
Q _secondaryStrideInPixelsX;
Q _secondaryStrideInPixelsY;
Q _secondaryStrideInFeatureChannels;
f _minimumValue;
f _maximumValue;
```

## Properties

```
@property (Tf,N,V_primaryScale) primaryScale;
@property (Tf,N,V_secondaryScale) secondaryScale;
@property (Tf,N,V_bias) bias;
@property (TQ,N,V_primaryStrideInPixelsX) primaryStrideInPixelsX;
@property (TQ,N,V_primaryStrideInPixelsY) primaryStrideInPixelsY;
@property (TQ,N,V_primaryStrideInFeatureChannels) primaryStrideInFeatureChannels;
@property (TQ,N,V_secondaryStrideInPixelsX) secondaryStrideInPixelsX;
@property (TQ,N,V_secondaryStrideInPixelsY) secondaryStrideInPixelsY;
@property (TQ,N,V_secondaryStrideInFeatureChannels) secondaryStrideInFeatureChannels;
@property (Tf,N,V_minimumValue) minimumValue;
@property (Tf,N,V_maximumValue) maximumValue;
```

## Class methods

```
+[MPSNNBinaryArithmeticNode nodeWithLeftSource:rightSource:];
+[MPSNNBinaryArithmeticNode nodeWithSources:];
```

## Instance methods

```
-[MPSNNBinaryArithmeticNode bias];
-[MPSNNBinaryArithmeticNode setMaximumValue:];
-[MPSNNBinaryArithmeticNode setMinimumValue:];
-[MPSNNBinaryArithmeticNode minimumValue];
-[MPSNNBinaryArithmeticNode maximumValue];
-[MPSNNBinaryArithmeticNode setBias:];
-[MPSNNBinaryArithmeticNode setSecondaryStrideInPixelsX:];
-[MPSNNBinaryArithmeticNode setSecondaryStrideInPixelsY:];
-[MPSNNBinaryArithmeticNode initWithSources:];
-[MPSNNBinaryArithmeticNode secondaryScale];
-[MPSNNBinaryArithmeticNode setPrimaryScale:];
-[MPSNNBinaryArithmeticNode setSecondaryScale:];
-[MPSNNBinaryArithmeticNode primaryScale];
-[MPSNNBinaryArithmeticNode initWithLeftSource:rightSource:];
-[MPSNNBinaryArithmeticNode gradientClass];
-[MPSNNBinaryArithmeticNode gradientFilterWithSources:];
-[MPSNNBinaryArithmeticNode gradientFiltersWithSources:];
-[MPSNNBinaryArithmeticNode primaryStrideInFeatureChannels];
-[MPSNNBinaryArithmeticNode primaryStrideInPixelsX];
-[MPSNNBinaryArithmeticNode primaryStrideInPixelsY];
-[MPSNNBinaryArithmeticNode secondaryStrideInFeatureChannels];
-[MPSNNBinaryArithmeticNode secondaryStrideInPixelsX];
-[MPSNNBinaryArithmeticNode secondaryStrideInPixelsY];
-[MPSNNBinaryArithmeticNode setPrimaryStrideInFeatureChannels:];
-[MPSNNBinaryArithmeticNode setPrimaryStrideInPixelsX:];
-[MPSNNBinaryArithmeticNode setPrimaryStrideInPixelsY:];
-[MPSNNBinaryArithmeticNode setSecondaryStrideInFeatureChannels:];
```
