# `MPSGraphDepthwiseConvolution3DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _strides;
@"NSArray" _dilationRates;
@"NSArray" _paddingValues;
Q _paddingStyle;
q _channelDimensionIndex;
```

## Properties

```
@property (T@"NSArray",C,N,V_strides) strides;
@property (T@"NSArray",C,N,V_dilationRates) dilationRates;
@property (T@"NSArray",C,N,V_paddingValues) paddingValues;
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (Tq,N,V_channelDimensionIndex) channelDimensionIndex;
```

## Class methods

```
+[MPSGraphDepthwiseConvolution3DOpDescriptor descriptorWithStrides:dilationRates:paddingValues:paddingStyle:];
+[MPSGraphDepthwiseConvolution3DOpDescriptor descriptorWithPaddingStyle:];
```

## Instance methods

```
-[MPSGraphDepthwiseConvolution3DOpDescriptor strides];
-[MPSGraphDepthwiseConvolution3DOpDescriptor copyWithZone:];
-[MPSGraphDepthwiseConvolution3DOpDescriptor setStrides:];
-[MPSGraphDepthwiseConvolution3DOpDescriptor setChannelDimensionIndex:];
-[MPSGraphDepthwiseConvolution3DOpDescriptor dilationRates];
-[MPSGraphDepthwiseConvolution3DOpDescriptor setDilationRates:];
-[MPSGraphDepthwiseConvolution3DOpDescriptor channelDimensionIndex];
-[MPSGraphDepthwiseConvolution3DOpDescriptor paddingStyle];
-[MPSGraphDepthwiseConvolution3DOpDescriptor paddingValues];
-[MPSGraphDepthwiseConvolution3DOpDescriptor setPaddingStyle:];
-[MPSGraphDepthwiseConvolution3DOpDescriptor setPaddingValues:];
```
