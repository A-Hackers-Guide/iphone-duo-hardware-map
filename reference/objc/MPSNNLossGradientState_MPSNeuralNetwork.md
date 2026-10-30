# `MPSNNLossGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 5 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
f _weight;
f _labelSmoothing;
f _epsilon;
f _delta;
@"MPSCNNLossLabels" _lossLabels;
```

## Class methods

```
+[MPSNNLossGradientState temporaryStateWithCommandBuffer:];
```

## Instance methods

```
-[MPSNNLossGradientState debugDescription];
-[MPSNNLossGradientState dealloc];
-[MPSNNLossGradientState initWithResource:];
```
