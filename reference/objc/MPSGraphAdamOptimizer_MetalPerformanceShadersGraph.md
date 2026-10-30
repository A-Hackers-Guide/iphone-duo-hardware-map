# `MPSGraphAdamOptimizer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOptimizer`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"MPSGraphTensor" _beta1Tensor;
@"MPSGraphTensor" _beta2Tensor;
@"MPSGraphTensor" _epsilonTensor;
@"MPSGraphVariableOp" _iterationsVariable;
```

## Instance methods

```
-[MPSGraphAdamOptimizer initWithGraph:learningRateTensor:momentumTensors:velocityTensors:maximumVelocityTensors:beta1:beta2:epsilon:iterations:trainableVariables:variablesToGradientTensorMap:name:];
-[MPSGraphAdamOptimizer initWithGraph:learningRateTensor:trainableVariables:variablesToGradientTensorMap:name:];
-[MPSGraphAdamOptimizer initWithGraph:lossTensor:learningRateTensor:beta1:beta2:epsilon:iterations:trainableVariables:name:];
-[MPSGraphAdamOptimizer initWithGraph:lossTensor:learningRateTensor:momentumTensors:velocityTensors:maximumVelocityTensors:beta1:beta2:epsilon:iterations:trainableVariables:name:];
-[MPSGraphAdamOptimizer initWithGraph:lossTensor:learningRateTensor:trainableVariables:name:];
```
