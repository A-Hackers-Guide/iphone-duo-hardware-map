# `MPSCNNLocalContrastNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNNormalizationNode`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
f _pm;
f _ps;
f _p0;
Q _kernelWidth;
Q _kernelHeight;
```

## Properties

```
@property (Tf,N,V_pm) pm;
@property (Tf,N,V_ps) ps;
@property (Tf,N,V_p0) p0;
@property (TQ,N,V_kernelWidth) kernelWidth;
@property (TQ,N,V_kernelHeight) kernelHeight;
```

## Class methods

```
+[MPSCNNLocalContrastNormalizationNode nodeWithSource:kernelSize:];
```

## Instance methods

```
-[MPSCNNLocalContrastNormalizationNode initWithSource:];
-[MPSCNNLocalContrastNormalizationNode pm];
-[MPSCNNLocalContrastNormalizationNode setPm:];
-[MPSCNNLocalContrastNormalizationNode kernelHeight];
-[MPSCNNLocalContrastNormalizationNode kernelWidth];
-[MPSCNNLocalContrastNormalizationNode setKernelWidth:];
-[MPSCNNLocalContrastNormalizationNode setKernelHeight:];
-[MPSCNNLocalContrastNormalizationNode gradientClass];
-[MPSCNNLocalContrastNormalizationNode initWithSource:kernelSize:];
-[MPSCNNLocalContrastNormalizationNode newFilterNode];
-[MPSCNNLocalContrastNormalizationNode p0];
-[MPSCNNLocalContrastNormalizationNode ps];
-[MPSCNNLocalContrastNormalizationNode setP0:];
-[MPSCNNLocalContrastNormalizationNode setPs:];
```
