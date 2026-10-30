# `MPSCNNConvolutionState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- Protocols: `MPSImageSizeEncodingState`
- 5 instance variables, 9 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _originalConvolutionSourceWidth;
Q _originalConvolutionSourceHeight;
Q _kernelWidth;
Q _kernelHeight;
{?="x"q"y"q"z"q} _srcOffset;
```

## Properties

```
@property (TQ,R,N,V_kernelWidth) kernelWidth;
@property (TQ,R,N,V_kernelHeight) kernelHeight;
@property (T{?=qqq},R,N,V_srcOffset) sourceOffset;
@property (TQ,R,N,V_originalConvolutionSourceWidth) sourceWidth;
@property (TQ,R,N,V_originalConvolutionSourceHeight) sourceHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MPSCNNConvolutionState kernelHeight];
-[MPSCNNConvolutionState kernelWidth];
-[MPSCNNConvolutionState sourceHeight];
-[MPSCNNConvolutionState sourceWidth];
-[MPSCNNConvolutionState sourceOffset];
-[MPSCNNConvolutionState destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
-[MPSCNNConvolutionState initWithSourceWidth:sourceHeight:kernelWidth:kernelHeight:sourceOffset:];
```
