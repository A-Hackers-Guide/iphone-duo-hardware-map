# `MPSGraphPooling4DOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 19 instance methods, 2 class methods

## Instance variables

```
B _ceilMode;
B _includeZeroPadToAverage;
I _returnIndicesDataType;
@"NSArray" _kernelSizes;
@"NSArray" _strides;
@"NSArray" _dilationRates;
@"NSArray" _paddingValues;
Q _paddingStyle;
Q _returnIndicesMode;
```

## Properties

```
@property (T@"NSArray",C,N,V_kernelSizes) kernelSizes;
@property (T@"NSArray",C,N,V_strides) strides;
@property (T@"NSArray",C,N,V_dilationRates) dilationRates;
@property (T@"NSArray",C,N,V_paddingValues) paddingValues;
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (TB,N,V_ceilMode) ceilMode;
@property (TB,N,V_includeZeroPadToAverage) includeZeroPadToAverage;
@property (TQ,N,V_returnIndicesMode) returnIndicesMode;
@property (TI,N,V_returnIndicesDataType) returnIndicesDataType;
```

## Class methods

```
+[MPSGraphPooling4DOpDescriptor descriptorWithKernelSizes:paddingStyle:];
+[MPSGraphPooling4DOpDescriptor descriptorWithKernelSizes:strides:dilationRates:paddingValues:paddingStyle:];
```

## Instance methods

```
-[MPSGraphPooling4DOpDescriptor strides];
-[MPSGraphPooling4DOpDescriptor copyWithZone:];
-[MPSGraphPooling4DOpDescriptor setStrides:];
-[MPSGraphPooling4DOpDescriptor setIncludeZeroPadToAverage:];
-[MPSGraphPooling4DOpDescriptor setReturnIndicesMode:];
-[MPSGraphPooling4DOpDescriptor setKernelSizes:];
-[MPSGraphPooling4DOpDescriptor dilationRates];
-[MPSGraphPooling4DOpDescriptor kernelSizes];
-[MPSGraphPooling4DOpDescriptor setDilationRates:];
-[MPSGraphPooling4DOpDescriptor ceilMode];
-[MPSGraphPooling4DOpDescriptor includeZeroPadToAverage];
-[MPSGraphPooling4DOpDescriptor paddingStyle];
-[MPSGraphPooling4DOpDescriptor paddingValues];
-[MPSGraphPooling4DOpDescriptor returnIndicesDataType];
-[MPSGraphPooling4DOpDescriptor returnIndicesMode];
-[MPSGraphPooling4DOpDescriptor setCeilMode:];
-[MPSGraphPooling4DOpDescriptor setPaddingStyle:];
-[MPSGraphPooling4DOpDescriptor setPaddingValues:];
-[MPSGraphPooling4DOpDescriptor setReturnIndicesDataType:];
```
