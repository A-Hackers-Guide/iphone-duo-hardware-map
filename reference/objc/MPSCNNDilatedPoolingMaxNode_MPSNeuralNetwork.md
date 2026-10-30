# `MPSCNNDilatedPoolingMaxNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 6 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
Q _strideInPixelsX;
Q _strideInPixelsY;
Q _dilationRateX;
Q _dilationRateY;
```

## Properties

```
@property (TQ,R,N,V_dilationRateX) dilationRateX;
@property (TQ,R,N,V_dilationRateY) dilationRateY;
```

## Class methods

```
+[MPSCNNDilatedPoolingMaxNode nodeWithSource:filterSize:];
+[MPSCNNDilatedPoolingMaxNode nodeWithSource:filterSize:stride:dilationRate:];
```

## Instance methods

```
-[MPSCNNDilatedPoolingMaxNode dilationRateX];
-[MPSCNNDilatedPoolingMaxNode dilationRateY];
-[MPSCNNDilatedPoolingMaxNode gradientClass];
-[MPSCNNDilatedPoolingMaxNode initWithSource:filterSize:];
-[MPSCNNDilatedPoolingMaxNode initWithSource:filterSize:stride:dilationRate:];
-[MPSCNNDilatedPoolingMaxNode initWithSource:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:dilationRateX:dilationRateY:];
-[MPSCNNDilatedPoolingMaxNode newFilterNode];
```
