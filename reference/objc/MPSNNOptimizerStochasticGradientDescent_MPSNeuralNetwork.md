# `MPSNNOptimizerStochasticGradientDescent`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNOptimizer`
- 2 instance variables, 3 properties, 16 instance methods, 1 class methods

## Instance variables

```
f _momentumScale;
B _useNesterovMomentum;
```

## Properties

```
@property (Tf,R,N,V_momentumScale) momentumScale;
@property (TB,R,N,V_useNesterovMomentum) useNesterovMomentum;
@property (TB,R,N) useNestrovMomentum;
```

## Class methods

```
+[MPSNNOptimizerStochasticGradientDescent libraryInfo:];
```

## Instance methods

```
-[MPSNNOptimizerStochasticGradientDescent debugDescription];
-[MPSNNOptimizerStochasticGradientDescent copyWithZone:device:];
-[MPSNNOptimizerStochasticGradientDescent initWithCoder:device:];
-[MPSNNOptimizerStochasticGradientDescent encodeWithCoder:];
-[MPSNNOptimizerStochasticGradientDescent encodeToCommandBuffer:inputGradientVector:inputValuesVector:inputMomentumVector:resultValuesVector:];
-[MPSNNOptimizerStochasticGradientDescent initWithDevice:learningRate:];
-[MPSNNOptimizerStochasticGradientDescent initWithDevice:momentumScale:useNestrovMomentum:optimizerDescriptor:];
-[MPSNNOptimizerStochasticGradientDescent momentumScale];
-[MPSNNOptimizerStochasticGradientDescent encodeToCommandBuffer:batchNormalizationGradientState:batchNormalizationSourceState:inputMomentumVectors:resultState:];
-[MPSNNOptimizerStochasticGradientDescent encodeToCommandBuffer:batchNormalizationState:inputMomentumVectors:resultState:];
-[MPSNNOptimizerStochasticGradientDescent encodeToCommandBuffer:convolutionGradientState:convolutionSourceState:inputMomentumVectors:resultState:];
-[MPSNNOptimizerStochasticGradientDescent encodeToCommandBuffer:inputGradientMatrix:inputValuesMatrix:inputMomentumMatrix:resultValuesMatrix:];
-[MPSNNOptimizerStochasticGradientDescent initWithDevice:momentumScale:useNesterovMomentum:optimizerDescriptor:];
-[MPSNNOptimizerStochasticGradientDescent initWithDevice:optimizerDescriptor:];
-[MPSNNOptimizerStochasticGradientDescent useNesterovMomentum];
-[MPSNNOptimizerStochasticGradientDescent useNestrovMomentum];
```
