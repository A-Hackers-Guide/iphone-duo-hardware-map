# `MPSGraphConvolution2DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 12 instance variables, 12 properties, 26 instance methods, 2 class methods

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
Q _groups;
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
@property (TQ,N,V_groups) groups;
```

## Class methods

```
+[MPSGraphConvolution2DOpDescriptor descriptorWithStrideInX:strideInY:dilationRateInX:dilationRateInY:groups:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingStyle:dataLayout:weightsLayout:];
+[MPSGraphConvolution2DOpDescriptor descriptorWithStrideInX:strideInY:dilationRateInX:dilationRateInY:groups:paddingStyle:dataLayout:weightsLayout:];
```

## Instance methods

```
-[MPSGraphConvolution2DOpDescriptor setGroups:];
-[MPSGraphConvolution2DOpDescriptor groups];
-[MPSGraphConvolution2DOpDescriptor copyWithZone:];
-[MPSGraphConvolution2DOpDescriptor setPaddingLeft:];
-[MPSGraphConvolution2DOpDescriptor paddingBottom];
-[MPSGraphConvolution2DOpDescriptor paddingLeft];
-[MPSGraphConvolution2DOpDescriptor paddingRight];
-[MPSGraphConvolution2DOpDescriptor paddingTop];
-[MPSGraphConvolution2DOpDescriptor setPaddingBottom:];
-[MPSGraphConvolution2DOpDescriptor setPaddingRight:];
-[MPSGraphConvolution2DOpDescriptor setPaddingTop:];
-[MPSGraphConvolution2DOpDescriptor weightsLayout];
-[MPSGraphConvolution2DOpDescriptor dataLayout];
-[MPSGraphConvolution2DOpDescriptor dilationRateInX];
-[MPSGraphConvolution2DOpDescriptor dilationRateInY];
-[MPSGraphConvolution2DOpDescriptor setDataLayout:];
-[MPSGraphConvolution2DOpDescriptor setDilationRateInX:];
-[MPSGraphConvolution2DOpDescriptor setDilationRateInY:];
-[MPSGraphConvolution2DOpDescriptor paddingStyle];
-[MPSGraphConvolution2DOpDescriptor setExplicitPaddingWithPaddingLeft:paddingRight:paddingTop:paddingBottom:];
-[MPSGraphConvolution2DOpDescriptor setPaddingStyle:];
-[MPSGraphConvolution2DOpDescriptor setStrideInX:];
-[MPSGraphConvolution2DOpDescriptor setStrideInY:];
-[MPSGraphConvolution2DOpDescriptor setWeightsLayout:];
-[MPSGraphConvolution2DOpDescriptor strideInX];
-[MPSGraphConvolution2DOpDescriptor strideInY];
```
