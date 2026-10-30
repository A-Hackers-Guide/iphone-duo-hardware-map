# `MPSNNOptimizerDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 2 class methods

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
@property (Tf,N,V_learningRate) learningRate;
@property (Tf,N,V_gradientRescale) gradientRescale;
@property (TB,N,V_applyGradientClipping) applyGradientClipping;
@property (Tf,N,V_gradientClipMax) gradientClipMax;
@property (Tf,N,V_gradientClipMin) gradientClipMin;
@property (Tf,N,V_regularizationScale) regularizationScale;
@property (TQ,N,V_regularizationType) regularizationType;
```

## Class methods

```
+[MPSNNOptimizerDescriptor optimizerDescriptorWithLearningRate:gradientRescale:regularizationType:regularizationScale:];
+[MPSNNOptimizerDescriptor optimizerDescriptorWithLearningRate:gradientRescale:applyGradientClipping:gradientClipMax:gradientClipMin:regularizationType:regularizationScale:];
```

## Instance methods

```
-[MPSNNOptimizerDescriptor initWithLearningRate:gradientRescale:regularizationType:regularizationScale:];
-[MPSNNOptimizerDescriptor setLearningRate:];
-[MPSNNOptimizerDescriptor learningRate];
-[MPSNNOptimizerDescriptor gradientClipMax];
-[MPSNNOptimizerDescriptor gradientClipMin];
-[MPSNNOptimizerDescriptor setApplyGradientClipping:];
-[MPSNNOptimizerDescriptor setGradientClipMax:];
-[MPSNNOptimizerDescriptor setGradientClipMin:];
-[MPSNNOptimizerDescriptor gradientRescale];
-[MPSNNOptimizerDescriptor initWithLearningRate:gradientRescale:applyGradientClipping:gradientClipMax:gradientClipMin:regularizationType:regularizationScale:];
-[MPSNNOptimizerDescriptor regularizationScale];
-[MPSNNOptimizerDescriptor regularizationType];
-[MPSNNOptimizerDescriptor applyGradientClipping];
-[MPSNNOptimizerDescriptor setGradientRescale:];
-[MPSNNOptimizerDescriptor setRegularizationScale:];
-[MPSNNOptimizerDescriptor setRegularizationType:];
```
