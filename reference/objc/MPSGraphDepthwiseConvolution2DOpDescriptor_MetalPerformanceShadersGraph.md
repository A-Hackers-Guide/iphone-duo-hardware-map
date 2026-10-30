# `MPSGraphDepthwiseConvolution2DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 24 instance methods, 2 class methods

## Instance variables

```
Q _strideInX;
Q _strideInY;
Q _dilationRateInX;
Q _dilationRateInY;
Q _paddingLeft;
Q _paddingRight;
Q _paddingTop;
Q _paddingBottom;
Q _paddingStyle;
Q _dataLayout;
Q _weightsLayout;
```

## Properties

```
@property (TQ,N,V_strideInX) strideInX;
@property (TQ,N,V_strideInY) strideInY;
@property (TQ,N,V_dilationRateInX) dilationRateInX;
@property (TQ,N,V_dilationRateInY) dilationRateInY;
@property (TQ,N,V_paddingLeft) paddingLeft;
@property (TQ,N,V_paddingRight) paddingRight;
@property (TQ,N,V_paddingTop) paddingTop;
@property (TQ,N,V_paddingBottom) paddingBottom;
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (TQ,N,V_dataLayout) dataLayout;
@property (TQ,N,V_weightsLayout) weightsLayout;
```

## Class methods

```
+[MPSGraphDepthwiseConvolution2DOpDescriptor descriptorWithDataLayout:weightsLayout:];
+[MPSGraphDepthwiseConvolution2DOpDescriptor descriptorWithStrideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingStyle:dataLayout:weightsLayout:];
```

## Instance methods

```
-[MPSGraphDepthwiseConvolution2DOpDescriptor copyWithZone:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setPaddingLeft:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor paddingBottom];
-[MPSGraphDepthwiseConvolution2DOpDescriptor paddingLeft];
-[MPSGraphDepthwiseConvolution2DOpDescriptor paddingRight];
-[MPSGraphDepthwiseConvolution2DOpDescriptor paddingTop];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setPaddingBottom:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setPaddingRight:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setPaddingTop:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor weightsLayout];
-[MPSGraphDepthwiseConvolution2DOpDescriptor dataLayout];
-[MPSGraphDepthwiseConvolution2DOpDescriptor dilationRateInX];
-[MPSGraphDepthwiseConvolution2DOpDescriptor dilationRateInY];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setDataLayout:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setDilationRateInX:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setDilationRateInY:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor paddingStyle];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setExplicitPaddingWithPaddingLeft:paddingRight:paddingTop:paddingBottom:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setPaddingStyle:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setStrideInX:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setStrideInY:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor setWeightsLayout:];
-[MPSGraphDepthwiseConvolution2DOpDescriptor strideInX];
-[MPSGraphDepthwiseConvolution2DOpDescriptor strideInY];
```
