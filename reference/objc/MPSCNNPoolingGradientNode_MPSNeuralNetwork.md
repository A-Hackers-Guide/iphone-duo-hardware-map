# `MPSCNNPoolingGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 4 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
Q _strideInPixelsX;
Q _strideInPixelsY;
```

## Properties

```
@property (TQ,R,N,V_kernelWidth) kernelWidth;
@property (TQ,R,N,V_kernelHeight) kernelHeight;
@property (TQ,R,N,V_strideInPixelsX) strideInPixelsX;
@property (TQ,R,N,V_strideInPixelsY) strideInPixelsY;
```

## Class methods

```
+[MPSCNNPoolingGradientNode nodeWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:paddingPolicy:];
```

## Instance methods

```
-[MPSCNNPoolingGradientNode kernelHeight];
-[MPSCNNPoolingGradientNode kernelWidth];
-[MPSCNNPoolingGradientNode strideInPixelsX];
-[MPSCNNPoolingGradientNode strideInPixelsY];
-[MPSCNNPoolingGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNPoolingGradientNode initWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:paddingPolicy:];
```
