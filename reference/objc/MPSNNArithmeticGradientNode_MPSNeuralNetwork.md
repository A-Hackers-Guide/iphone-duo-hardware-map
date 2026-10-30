# `MPSNNArithmeticGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 9 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
f _primaryScale;
f _secondaryScale;
f _bias;
Q _secondaryStrideInPixelsX;
Q _secondaryStrideInPixelsY;
Q _secondaryStrideInFeatureChannels;
f _minimumValue;
f _maximumValue;
B _isSecondarySourceFilter;
```

## Properties

```
@property (Tf,N,V_primaryScale) primaryScale;
@property (Tf,N,V_secondaryScale) secondaryScale;
@property (Tf,N,V_bias) bias;
@property (TQ,N,V_secondaryStrideInPixelsX) secondaryStrideInPixelsX;
@property (TQ,N,V_secondaryStrideInPixelsY) secondaryStrideInPixelsY;
@property (TQ,N,V_secondaryStrideInFeatureChannels) secondaryStrideInFeatureChannels;
@property (Tf,N,V_minimumValue) minimumValue;
@property (Tf,N,V_maximumValue) maximumValue;
@property (TB,R,N,V_isSecondarySourceFilter) isSecondarySourceFilter;
```

## Class methods

```
+[MPSNNArithmeticGradientNode nodeWithSourceGradient:sourceImage:gradientState:isSecondarySourceFilter:];
```

## Instance methods

```
-[MPSNNArithmeticGradientNode bias];
-[MPSNNArithmeticGradientNode setMaximumValue:];
-[MPSNNArithmeticGradientNode setMinimumValue:];
-[MPSNNArithmeticGradientNode minimumValue];
-[MPSNNArithmeticGradientNode maximumValue];
-[MPSNNArithmeticGradientNode setBias:];
-[MPSNNArithmeticGradientNode setSecondaryStrideInPixelsX:];
-[MPSNNArithmeticGradientNode setSecondaryStrideInPixelsY:];
-[MPSNNArithmeticGradientNode secondaryScale];
-[MPSNNArithmeticGradientNode setPrimaryScale:];
-[MPSNNArithmeticGradientNode setSecondaryScale:];
-[MPSNNArithmeticGradientNode primaryScale];
-[MPSNNArithmeticGradientNode initWithGradientImages:forwardFilter:isSecondarySourceFilter:];
-[MPSNNArithmeticGradientNode initWithSourceGradient:sourceImage:gradientState:isSecondarySourceFilter:];
-[MPSNNArithmeticGradientNode isSecondarySourceFilter];
-[MPSNNArithmeticGradientNode secondaryStrideInFeatureChannels];
-[MPSNNArithmeticGradientNode secondaryStrideInPixelsX];
-[MPSNNArithmeticGradientNode secondaryStrideInPixelsY];
-[MPSNNArithmeticGradientNode setSecondaryStrideInFeatureChannels:];
```
