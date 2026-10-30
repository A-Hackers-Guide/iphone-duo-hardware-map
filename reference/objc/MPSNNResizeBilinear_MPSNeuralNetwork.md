# `MPSNNResizeBilinear`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
Q _resizeWidth;
Q _resizeHeight;
B _alignCorners;
```

## Properties

```
@property (TQ,R,N,V_resizeWidth) resizeWidth;
@property (TQ,R,N,V_resizeHeight) resizeHeight;
@property (TB,R,N,V_alignCorners) alignCorners;
```

## Class methods

```
+[MPSNNResizeBilinear libraryInfo:];
```

## Instance methods

```
-[MPSNNResizeBilinear debugDescription];
-[MPSNNResizeBilinear copyWithZone:device:];
-[MPSNNResizeBilinear initWithCoder:device:];
-[MPSNNResizeBilinear encodeWithCoder:];
-[MPSNNResizeBilinear alignCorners];
-[MPSNNResizeBilinear resizeHeight];
-[MPSNNResizeBilinear resizeWidth];
-[MPSNNResizeBilinear destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNResizeBilinear initWithDevice:resizeWidth:resizeHeight:alignCorners:];
```
