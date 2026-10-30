# `MPSNNReshapeNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 3 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
Q _resultWidth;
Q _resultHeight;
Q _resultFeatureChannels;
```

## Class methods

```
+[MPSNNReshapeNode nodeWithSource:resultWidth:resultHeight:resultFeatureChannels:];
```

## Instance methods

```
-[MPSNNReshapeNode gradientClass];
-[MPSNNReshapeNode initWithSource:resultWidth:resultHeight:resultFeatureChannels:];
-[MPSNNReshapeNode newFilterNode];
```
