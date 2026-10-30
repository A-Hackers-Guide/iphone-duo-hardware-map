# `MPSGraphConvolution3DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 16 instance variables, 16 properties, 34 instance methods, 2 class methods

## Instance variables

```
Q _strideInX;
Q _strideInY;
Q _strideInZ;
Q _dilationRateInX;
Q _dilationRateInY;
Q _dilationRateInZ;
Q _paddingLeft;
Q _paddingRight;
Q _paddingTop;
Q _paddingBottom;
Q _paddingFront;
Q _paddingBack;
Q _paddingStyle;
Q _dataLayout;
Q _weightsLayout;
Q _groups;
```

## Properties

```
@property (TQ,N,V_strideInX) strideInX;
@property (TQ,N,V_strideInY) strideInY;
@property (TQ,N,V_strideInZ) strideInZ;
@property (TQ,N,V_dilationRateInX) dilationRateInX;
@property (TQ,N,V_dilationRateInY) dilationRateInY;
@property (TQ,N,V_dilationRateInZ) dilationRateInZ;
@property (TQ,N,V_paddingLeft) paddingLeft;
@property (TQ,N,V_paddingRight) paddingRight;
@property (TQ,N,V_paddingTop) paddingTop;
@property (TQ,N,V_paddingBottom) paddingBottom;
@property (TQ,N,V_paddingFront) paddingFront;
@property (TQ,N,V_paddingBack) paddingBack;
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (TQ,N,V_dataLayout) dataLayout;
@property (TQ,N,V_weightsLayout) weightsLayout;
@property (TQ,N,V_groups) groups;
```

## Class methods

```
+[MPSGraphConvolution3DOpDescriptor descriptorWithStrideInX:strideInY:strideInZ:dilationRateInX:dilationRateInY:dilationRateInZ:groups:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingFront:paddingBack:paddingStyle:dataLayout:weightsLayout:];
+[MPSGraphConvolution3DOpDescriptor descriptorWithStrideInX:strideInY:strideInZ:dilationRateInX:dilationRateInY:dilationRateInZ:groups:paddingStyle:dataLayout:weightsLayout:];
```

## Instance methods

```
-[MPSGraphConvolution3DOpDescriptor setGroups:];
-[MPSGraphConvolution3DOpDescriptor groups];
-[MPSGraphConvolution3DOpDescriptor copyWithZone:];
-[MPSGraphConvolution3DOpDescriptor setPaddingLeft:];
-[MPSGraphConvolution3DOpDescriptor paddingBottom];
-[MPSGraphConvolution3DOpDescriptor paddingLeft];
-[MPSGraphConvolution3DOpDescriptor paddingRight];
-[MPSGraphConvolution3DOpDescriptor paddingTop];
-[MPSGraphConvolution3DOpDescriptor setPaddingBottom:];
-[MPSGraphConvolution3DOpDescriptor setPaddingRight:];
-[MPSGraphConvolution3DOpDescriptor setPaddingTop:];
-[MPSGraphConvolution3DOpDescriptor weightsLayout];
-[MPSGraphConvolution3DOpDescriptor dataLayout];
-[MPSGraphConvolution3DOpDescriptor dilationRateInX];
-[MPSGraphConvolution3DOpDescriptor dilationRateInY];
-[MPSGraphConvolution3DOpDescriptor setDataLayout:];
-[MPSGraphConvolution3DOpDescriptor setDilationRateInX:];
-[MPSGraphConvolution3DOpDescriptor setDilationRateInY:];
-[MPSGraphConvolution3DOpDescriptor dilationRateInZ];
-[MPSGraphConvolution3DOpDescriptor setPaddingBack:];
-[MPSGraphConvolution3DOpDescriptor paddingBack];
-[MPSGraphConvolution3DOpDescriptor paddingFront];
-[MPSGraphConvolution3DOpDescriptor paddingStyle];
-[MPSGraphConvolution3DOpDescriptor setDilationRateInZ:];
-[MPSGraphConvolution3DOpDescriptor setExplicitPaddingWithPaddingLeft:paddingRight:paddingTop:paddingBottom:paddingFront:paddingBack:];
-[MPSGraphConvolution3DOpDescriptor setPaddingFront:];
-[MPSGraphConvolution3DOpDescriptor setPaddingStyle:];
-[MPSGraphConvolution3DOpDescriptor setStrideInX:];
-[MPSGraphConvolution3DOpDescriptor setStrideInY:];
-[MPSGraphConvolution3DOpDescriptor setStrideInZ:];
-[MPSGraphConvolution3DOpDescriptor setWeightsLayout:];
-[MPSGraphConvolution3DOpDescriptor strideInX];
-[MPSGraphConvolution3DOpDescriptor strideInY];
-[MPSGraphConvolution3DOpDescriptor strideInZ];
```
