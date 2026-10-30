# `MPSGraphPooling2DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 16 instance variables, 16 properties, 35 instance methods, 2 class methods

## Instance variables

```
B _ceilMode;
B _includeZeroPadToAverage;
I _returnIndicesDataType;
Q _returnIndicesMode;
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
Q _paddingStyle;
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
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (TQ,N,V_dataLayout) dataLayout;
@property (TQ,N,V_returnIndicesMode) returnIndicesMode;
@property (TI,N,V_returnIndicesDataType) returnIndicesDataType;
@property (TB,N,V_ceilMode) ceilMode;
@property (TB,N,V_includeZeroPadToAverage) includeZeroPadToAverage;
```

## Class methods

```
+[MPSGraphPooling2DOpDescriptor descriptorWithKernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingStyle:dataLayout:];
+[MPSGraphPooling2DOpDescriptor descriptorWithKernelWidth:kernelHeight:strideInX:strideInY:paddingStyle:dataLayout:];
```

## Instance methods

```
-[MPSGraphPooling2DOpDescriptor init];
-[MPSGraphPooling2DOpDescriptor copyWithZone:];
-[MPSGraphPooling2DOpDescriptor setPaddingLeft:];
-[MPSGraphPooling2DOpDescriptor paddingBottom];
-[MPSGraphPooling2DOpDescriptor paddingLeft];
-[MPSGraphPooling2DOpDescriptor paddingRight];
-[MPSGraphPooling2DOpDescriptor paddingTop];
-[MPSGraphPooling2DOpDescriptor setPaddingBottom:];
-[MPSGraphPooling2DOpDescriptor setPaddingRight:];
-[MPSGraphPooling2DOpDescriptor setPaddingTop:];
-[MPSGraphPooling2DOpDescriptor kernelHeight];
-[MPSGraphPooling2DOpDescriptor kernelWidth];
-[MPSGraphPooling2DOpDescriptor setKernelWidth:];
-[MPSGraphPooling2DOpDescriptor dataLayout];
-[MPSGraphPooling2DOpDescriptor setKernelHeight:];
-[MPSGraphPooling2DOpDescriptor setIncludeZeroPadToAverage:];
-[MPSGraphPooling2DOpDescriptor setReturnIndicesMode:];
-[MPSGraphPooling2DOpDescriptor dilationRateInX];
-[MPSGraphPooling2DOpDescriptor dilationRateInY];
-[MPSGraphPooling2DOpDescriptor setDataLayout:];
-[MPSGraphPooling2DOpDescriptor setDilationRateInX:];
-[MPSGraphPooling2DOpDescriptor setDilationRateInY:];
-[MPSGraphPooling2DOpDescriptor ceilMode];
-[MPSGraphPooling2DOpDescriptor includeZeroPadToAverage];
-[MPSGraphPooling2DOpDescriptor paddingStyle];
-[MPSGraphPooling2DOpDescriptor returnIndicesDataType];
-[MPSGraphPooling2DOpDescriptor returnIndicesMode];
-[MPSGraphPooling2DOpDescriptor setCeilMode:];
-[MPSGraphPooling2DOpDescriptor setExplicitPaddingWithPaddingLeft:paddingRight:paddingTop:paddingBottom:];
-[MPSGraphPooling2DOpDescriptor setPaddingStyle:];
-[MPSGraphPooling2DOpDescriptor setReturnIndicesDataType:];
-[MPSGraphPooling2DOpDescriptor setStrideInX:];
-[MPSGraphPooling2DOpDescriptor setStrideInY:];
-[MPSGraphPooling2DOpDescriptor strideInX];
-[MPSGraphPooling2DOpDescriptor strideInY];
```
