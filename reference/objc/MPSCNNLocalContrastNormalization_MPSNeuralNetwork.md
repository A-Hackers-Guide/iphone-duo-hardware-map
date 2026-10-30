# `MPSCNNLocalContrastNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 6 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
f _alpha;
f _beta;
f _delta;
f _p0;
f _pm;
f _ps;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
@property (Tf,N,V_p0) p0;
@property (Tf,N,V_pm) pm;
@property (Tf,N,V_ps) ps;
```

## Class methods

```
+[MPSCNNLocalContrastNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNLocalContrastNormalization initWithDevice:];
-[MPSCNNLocalContrastNormalization pm];
-[MPSCNNLocalContrastNormalization debugDescription];
-[MPSCNNLocalContrastNormalization setAlpha:];
-[MPSCNNLocalContrastNormalization copyWithZone:device:];
-[MPSCNNLocalContrastNormalization setPm:];
-[MPSCNNLocalContrastNormalization initWithCoder:device:];
-[MPSCNNLocalContrastNormalization encodeWithCoder:];
-[MPSCNNLocalContrastNormalization alpha];
-[MPSCNNLocalContrastNormalization delta];
-[MPSCNNLocalContrastNormalization setDelta:];
-[MPSCNNLocalContrastNormalization encodeBatchToCommandBuffer:sourceImages:destinationImages:];
-[MPSCNNLocalContrastNormalization encodeToCommandBuffer:sourceImage:destinationImage:];
-[MPSCNNLocalContrastNormalization setBeta:];
-[MPSCNNLocalContrastNormalization beta];
-[MPSCNNLocalContrastNormalization initWithDevice:kernelWidth:kernelHeight:];
-[MPSCNNLocalContrastNormalization encodeBatchToCommandBuffer:sourceImages:];
-[MPSCNNLocalContrastNormalization encodeToCommandBuffer:sourceImage:];
-[MPSCNNLocalContrastNormalization p0];
-[MPSCNNLocalContrastNormalization ps];
-[MPSCNNLocalContrastNormalization setP0:];
-[MPSCNNLocalContrastNormalization setPs:];
```
