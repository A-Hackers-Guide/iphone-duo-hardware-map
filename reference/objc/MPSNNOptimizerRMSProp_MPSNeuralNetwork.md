# `MPSNNOptimizerRMSProp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNOptimizer`
- 4 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
d _decay;
d _momentumScale;
f _epsilon;
B _centered;
```

## Properties

```
@property (Td,R,N,V_momentumScale) momentumScale;
@property (TB,R,N,V_centered) centered;
@property (Td,R,N,V_decay) decay;
@property (Tf,R,N,V_epsilon) epsilon;
```

## Class methods

```
+[MPSNNOptimizerRMSProp libraryInfo:];
```

## Instance methods

```
-[MPSNNOptimizerRMSProp debugDescription];
-[MPSNNOptimizerRMSProp decay];
-[MPSNNOptimizerRMSProp copyWithZone:device:];
-[MPSNNOptimizerRMSProp initWithCoder:device:];
-[MPSNNOptimizerRMSProp encodeWithCoder:];
-[MPSNNOptimizerRMSProp epsilon];
-[MPSNNOptimizerRMSProp initWithDevice:learningRate:];
-[MPSNNOptimizerRMSProp centered];
-[MPSNNOptimizerRMSProp momentumScale];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:batchNormalizationGradientState:batchNormalizationSourceState:inputSumOfSquaresVectors:resultState:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:batchNormalizationState:inputSumOfSquaresVectors:resultState:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:convolutionGradientState:convolutionSourceState:inputSumOfSquaresVectors:resultState:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:inputGradientMatrix:inputValuesMatrix:inputSumOfSquaresMatrix:inputWeightedSumMatrix:inputMomentumMatrix:resultValuesMatrix:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:inputGradientMatrix:inputValuesMatrix:inputSumOfSquaresMatrix:resultValuesMatrix:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:inputGradientVector:inputValuesVector:inputSumOfSquaresVector:inputWeightedSumVector:inputMomentumVector:resultValuesVector:];
-[MPSNNOptimizerRMSProp encodeToCommandBuffer:inputGradientVector:inputValuesVector:inputSumOfSquaresVector:resultValuesVector:];
-[MPSNNOptimizerRMSProp initWithDevice:decay:epsilon:momentumScale:centered:optimizerDescriptor:];
-[MPSNNOptimizerRMSProp initWithDevice:decay:epsilon:optimizerDescriptor:];
-[MPSNNOptimizerRMSProp initWithDevice:optimizerDescriptor:];
```
