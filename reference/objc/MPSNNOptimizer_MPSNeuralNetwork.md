# `MPSNNOptimizer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
f _learningRate;
f _gradientRescale;
B _applyGradientClipping;
f _gradientClipMax;
f _gradientClipMin;
Q _regularizationType;
f _regularizationScale;
```

## Properties

```
@property (Tf,R,N,V_learningRate) learningRate;
@property (Tf,R,N,V_gradientRescale) gradientRescale;
@property (TB,N,V_applyGradientClipping) applyGradientClipping;
@property (Tf,R,N,V_gradientClipMax) gradientClipMax;
@property (Tf,R,N,V_gradientClipMin) gradientClipMin;
@property (Tf,R,N,V_regularizationScale) regularizationScale;
@property (TQ,R,N,V_regularizationType) regularizationType;
```

## Instance methods

```
-[MPSNNOptimizer initWithDevice:];
-[MPSNNOptimizer debugDescription];
-[MPSNNOptimizer copyWithZone:device:];
-[MPSNNOptimizer initWithCoder:device:];
-[MPSNNOptimizer encodeWithCoder:];
-[MPSNNOptimizer setLearningRate:];
-[MPSNNOptimizer learningRate];
-[MPSNNOptimizer gradientClipMax];
-[MPSNNOptimizer gradientClipMin];
-[MPSNNOptimizer setApplyGradientClipping:];
-[MPSNNOptimizer gradientRescale];
-[MPSNNOptimizer regularizationScale];
-[MPSNNOptimizer regularizationType];
-[MPSNNOptimizer applyGradientClipping];
-[MPSNNOptimizer initWithDevice:optimizerDescriptor:];
```
