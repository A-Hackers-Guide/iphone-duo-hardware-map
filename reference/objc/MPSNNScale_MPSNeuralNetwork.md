# `MPSNNScale`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 4 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<MPSImageTransformProvider>" _transformProvider;
{?="width"Q"height"Q"depth"Q} _destSize;
@"MPSImageScale" _filter;
@"<MPSHandle>" _handle;
```

## Class methods

```
+[MPSNNScale libraryInfo:];
```

## Instance methods

```
-[MPSNNScale initWithDevice:];
-[MPSNNScale setOptions:];
-[MPSNNScale debugDescription];
-[MPSNNScale setLabel:];
-[MPSNNScale dealloc];
-[MPSNNScale copyWithZone:device:];
-[MPSNNScale initWithCoder:device:];
-[MPSNNScale encodeWithCoder:];
-[MPSNNScale setEdgeMode:];
-[MPSNNScale destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNScale initWithDevice:transformProvider:handle:outputSize:scaleClass:];
```
