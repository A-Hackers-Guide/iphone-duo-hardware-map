# `MPSCNNPoolingNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 4 instance variables, 4 properties, 8 instance methods, 2 class methods

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
+[MPSCNNPoolingNode nodeWithSource:filterSize:];
+[MPSCNNPoolingNode nodeWithSource:filterSize:stride:];
```

## Instance methods

```
-[MPSCNNPoolingNode kernelHeight];
-[MPSCNNPoolingNode kernelWidth];
-[MPSCNNPoolingNode strideInPixelsX];
-[MPSCNNPoolingNode strideInPixelsY];
-[MPSCNNPoolingNode initWithSource:filterSize:];
-[MPSCNNPoolingNode initWithSource:filterSize:stride:];
-[MPSCNNPoolingNode initWithSource:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
-[MPSCNNPoolingNode newFilterNode];
```
