# `MPSGraphImToColOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 24 instance methods, 2 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
Q _strideInX;
Q _strideInY;
Q _dilationRateInX;
Q _dilationRateInY;
Q _paddingLeft;
Q _paddingRight;
Q _paddingTop;
Q _paddingBottom;
Q _dataLayout;
```

## Properties

```
@property (TQ,N,V_kernelWidth) kernelWidth;
@property (TQ,N,V_kernelHeight) kernelHeight;
@property (TQ,N,V_strideInX) strideInX;
@property (TQ,N,V_strideInY) strideInY;
@property (TQ,N,V_dilationRateInX) dilationRateInX;
@property (TQ,N,V_dilationRateInY) dilationRateInY;
@property (TQ,N,V_paddingLeft) paddingLeft;
@property (TQ,N,V_paddingRight) paddingRight;
@property (TQ,N,V_paddingTop) paddingTop;
@property (TQ,N,V_paddingBottom) paddingBottom;
@property (TQ,N,V_dataLayout) dataLayout;
```

## Class methods

```
+[MPSGraphImToColOpDescriptor descriptorWithKernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:dataLayout:];
+[MPSGraphImToColOpDescriptor descriptorWithKernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:dataLayout:];
```

## Instance methods

```
-[MPSGraphImToColOpDescriptor copyWithZone:];
-[MPSGraphImToColOpDescriptor setPaddingLeft:];
-[MPSGraphImToColOpDescriptor paddingBottom];
-[MPSGraphImToColOpDescriptor paddingLeft];
-[MPSGraphImToColOpDescriptor paddingRight];
-[MPSGraphImToColOpDescriptor paddingTop];
-[MPSGraphImToColOpDescriptor setPaddingBottom:];
-[MPSGraphImToColOpDescriptor setPaddingRight:];
-[MPSGraphImToColOpDescriptor setPaddingTop:];
-[MPSGraphImToColOpDescriptor kernelHeight];
-[MPSGraphImToColOpDescriptor kernelWidth];
-[MPSGraphImToColOpDescriptor setKernelWidth:];
-[MPSGraphImToColOpDescriptor dataLayout];
-[MPSGraphImToColOpDescriptor setKernelHeight:];
-[MPSGraphImToColOpDescriptor dilationRateInX];
-[MPSGraphImToColOpDescriptor dilationRateInY];
-[MPSGraphImToColOpDescriptor setDataLayout:];
-[MPSGraphImToColOpDescriptor setDilationRateInX:];
-[MPSGraphImToColOpDescriptor setDilationRateInY:];
-[MPSGraphImToColOpDescriptor setExplicitPaddingWithPaddingLeft:paddingRight:paddingTop:paddingBottom:];
-[MPSGraphImToColOpDescriptor setStrideInX:];
-[MPSGraphImToColOpDescriptor setStrideInY:];
-[MPSGraphImToColOpDescriptor strideInX];
-[MPSGraphImToColOpDescriptor strideInY];
```
