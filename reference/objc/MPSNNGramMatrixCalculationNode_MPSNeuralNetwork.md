# `MPSNNGramMatrixCalculationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
f _alpha;
@"<MPSNNGramMatrixCallback>" _propertyCallBack;
```

## Properties

```
@property (Tf,R,N,V_alpha) alpha;
@property (T@"<MPSNNGramMatrixCallback>",&,N,V_propertyCallBack) propertyCallBack;
```

## Class methods

```
+[MPSNNGramMatrixCalculationNode nodeWithSource:];
+[MPSNNGramMatrixCalculationNode nodeWithSource:alpha:];
```

## Instance methods

```
-[MPSNNGramMatrixCalculationNode initWithSource:];
-[MPSNNGramMatrixCalculationNode dealloc];
-[MPSNNGramMatrixCalculationNode alpha];
-[MPSNNGramMatrixCalculationNode gradientClass];
-[MPSNNGramMatrixCalculationNode initWithSource:alpha:];
-[MPSNNGramMatrixCalculationNode newFilterNode];
-[MPSNNGramMatrixCalculationNode propertyCallBack];
-[MPSNNGramMatrixCalculationNode setPropertyCallBack:];
```
