# `MPSNNGramMatrixCalculationGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 1 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
f _alpha;
```

## Properties

```
@property (Tf,R,N,V_alpha) alpha;
```

## Class methods

```
+[MPSNNGramMatrixCalculationGradientNode nodeWithSourceGradient:sourceImage:gradientState:];
+[MPSNNGramMatrixCalculationGradientNode nodeWithSourceGradient:sourceImage:gradientState:alpha:];
```

## Instance methods

```
-[MPSNNGramMatrixCalculationGradientNode alpha];
-[MPSNNGramMatrixCalculationGradientNode initWithGradientImages:forwardFilter:];
-[MPSNNGramMatrixCalculationGradientNode initWithSourceGradient:sourceImage:gradientState:];
-[MPSNNGramMatrixCalculationGradientNode initWithSourceGradient:sourceImage:gradientState:alpha:];
-[MPSNNGramMatrixCalculationGradientNode newFilterNode];
```
