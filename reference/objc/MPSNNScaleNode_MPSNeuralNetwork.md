# `MPSNNScaleNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 2 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"<MPSImageTransformProvider>" _transformProvider;
{?="width"Q"height"Q"depth"Q} _size;
```

## Class methods

```
+[MPSNNScaleNode nodeWithSource:outputSize:];
+[MPSNNScaleNode nodeWithSource:transformProvider:outputSize:];
```

## Instance methods

```
-[MPSNNScaleNode debugDescription];
-[MPSNNScaleNode dealloc];
-[MPSNNScaleNode initWithSource:outputSize:];
-[MPSNNScaleNode initWithSource:transformProvider:outputSize:];
-[MPSNNScaleNode privateInitWithSource:transformProvider:outputSize:];
```
