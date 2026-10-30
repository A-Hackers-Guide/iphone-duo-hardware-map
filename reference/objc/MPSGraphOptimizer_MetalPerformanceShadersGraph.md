# `MPSGraphOptimizer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 6 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"MPSGraph" _graph;
@"MPSGraphTensor" _learningRateTensor;
@"NSArray" _trainableVariables;
@"NSDictionary" _variablesToGradientTensorMap;
@"NSDictionary" _variablesToUpdateOpMap;
@"NSString" _name;
```

## Properties

```
@property (T@"NSArray",R,N) updateOperations;
@property (T@"NSDictionary",R,N,V_variablesToGradientTensorMap) variablesToGradientTensorMap;
@property (T@"NSDictionary",R,N,V_variablesToUpdateOpMap) variablesToUpdateOpMap;
@property (T@"MPSGraphTensor",R,N,V_learningRateTensor) learningRateTensor;
```

## Instance methods

```
-[MPSGraphOptimizer initWithGraph:learningRateTensor:trainableVariables:variablesToGradientTensorMap:name:];
-[MPSGraphOptimizer initWithGraph:lossTensor:learningRateTensor:trainableVariables:name:];
-[MPSGraphOptimizer learningRateTensor];
-[MPSGraphOptimizer updateOperations];
-[MPSGraphOptimizer variablesToGradientTensorMap];
-[MPSGraphOptimizer variablesToUpdateOpMap];
```
