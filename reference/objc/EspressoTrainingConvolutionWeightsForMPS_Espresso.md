# `EspressoTrainingConvolutionWeightsForMPS`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EspressoConvolutionWeightsForMPS`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B is_training;
@"<MTLBuffer>" _weightsBuffer;
@"<MTLBuffer>" _biasesBuffer;
```

## Properties

```
@property (T@"<MTLBuffer>",&,V_weightsBuffer) weightsBuffer;
@property (T@"<MTLBuffer>",&,V_biasesBuffer) biasesBuffer;
```

## Instance methods

```
-[EspressoTrainingConvolutionWeightsForMPS ready];
-[EspressoTrainingConvolutionWeightsForMPS weightsBuffer];
-[EspressoTrainingConvolutionWeightsForMPS weights];
-[EspressoTrainingConvolutionWeightsForMPS biasTerms];
-[EspressoTrainingConvolutionWeightsForMPS biasesBuffer];
-[EspressoTrainingConvolutionWeightsForMPS initWithParams:forMode:];
-[EspressoTrainingConvolutionWeightsForMPS setBiasesBuffer:];
-[EspressoTrainingConvolutionWeightsForMPS setWeightsBuffer:];
-[EspressoTrainingConvolutionWeightsForMPS weightsLayout];
```
