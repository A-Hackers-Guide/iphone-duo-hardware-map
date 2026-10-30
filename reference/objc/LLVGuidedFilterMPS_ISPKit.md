# `LLVGuidedFilterMPS`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LLVGuidedFilter`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MPSImageGuidedFilter" _filter;
@"MPSNNResizeBilinear" _scaler;
@"MPSImage" _subSampledImage;
@"MPSImage" _coefficientsImageA;
@"MPSImage" _coefficientsImageB;
```

## Properties

```
@property (T@"MPSImageGuidedFilter",&,N,V_filter) filter;
@property (T@"MPSNNResizeBilinear",&,N,V_scaler) scaler;
@property (T@"MPSImage",&,N,V_subSampledImage) subSampledImage;
@property (T@"MPSImage",&,N,V_coefficientsImageA) coefficientsImageA;
@property (T@"MPSImage",&,N,V_coefficientsImageB) coefficientsImageB;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LLVGuidedFilterMPS filter];
-[LLVGuidedFilterMPS setFilter:];
-[LLVGuidedFilterMPS scaler];
-[LLVGuidedFilterMPS setScaler:];
-[LLVGuidedFilterMPS subSampledImage];
-[LLVGuidedFilterMPS coefficientsImageA];
-[LLVGuidedFilterMPS coefficientsImageB];
-[LLVGuidedFilterMPS guidedFilterWithCommandBuffer:current:output:epsilon:];
-[LLVGuidedFilterMPS initWithDevice:inputSize:];
-[LLVGuidedFilterMPS initWithDevice:inputSize:epsilon:kernelDiameter:subSampleFactor:];
-[LLVGuidedFilterMPS setCoefficientsImageA:];
-[LLVGuidedFilterMPS setCoefficientsImageB:];
-[LLVGuidedFilterMPS setSubSampledImage:];
```
