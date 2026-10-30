# `MPSNNCropAndResizeBilinear`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 5 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _resizeWidth;
Q _resizeHeight;
Q _numberOfRegions;
^{MPSRegion={MPSOrigin=ddd}{MPSSize=ddd}} _regions;
^{Region_params=} _gpuRegions;
```

## Properties

```
@property (TQ,R,N,V_resizeWidth) resizeWidth;
@property (TQ,R,N,V_resizeHeight) resizeHeight;
@property (TQ,R,N,V_numberOfRegions) numberOfRegions;
@property (Tr^{MPSRegion={MPSOrigin=ddd}{MPSSize=ddd}},R,N,V_regions) regions;
```

## Class methods

```
+[MPSNNCropAndResizeBilinear libraryInfo:];
```

## Instance methods

```
-[MPSNNCropAndResizeBilinear regions];
-[MPSNNCropAndResizeBilinear debugDescription];
-[MPSNNCropAndResizeBilinear dealloc];
-[MPSNNCropAndResizeBilinear copyWithZone:device:];
-[MPSNNCropAndResizeBilinear initWithCoder:device:];
-[MPSNNCropAndResizeBilinear encodeWithCoder:];
-[MPSNNCropAndResizeBilinear numberOfRegions];
-[MPSNNCropAndResizeBilinear resizeHeight];
-[MPSNNCropAndResizeBilinear resizeWidth];
-[MPSNNCropAndResizeBilinear destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNCropAndResizeBilinear initWithDevice:resizeWidth:resizeHeight:numberOfRegions:regions:];
```
