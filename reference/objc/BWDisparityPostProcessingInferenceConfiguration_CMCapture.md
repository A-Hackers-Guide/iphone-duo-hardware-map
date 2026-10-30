# `BWDisparityPostProcessingInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 7 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _resetTemporalStateOnAspectRatioChange;
B _appliesValidBufferRectPadding;
I _disparityFormat;
{?="width"i"height"i} _inputDimensions;
{?="width"i"height"i} _outputDimensions;
@"NSString" _portType;
Q _concurrencyWidth;
```

## Properties

```
@property (T{?=ii},R,N,V_inputDimensions) inputDimensions;
@property (T{?=ii},R,N,V_outputDimensions) outputDimensions;
@property (TI,R,N,V_disparityFormat) disparityFormat;
@property (T@"NSString",R,N,V_portType) portType;
@property (TQ,R,N,V_concurrencyWidth) concurrencyWidth;
@property (TB,R,N,V_resetTemporalStateOnAspectRatioChange) resetTemporalStateOnAspectRatioChange;
@property (TB,R,N,V_appliesValidBufferRectPadding) appliesValidBufferRectPadding;
```

## Instance methods

```
-[BWDisparityPostProcessingInferenceConfiguration portType];
-[BWDisparityPostProcessingInferenceConfiguration concurrencyWidth];
-[BWDisparityPostProcessingInferenceConfiguration outputDimensions];
-[BWDisparityPostProcessingInferenceConfiguration inputDimensions];
-[BWDisparityPostProcessingInferenceConfiguration appliesValidBufferRectPadding];
-[BWDisparityPostProcessingInferenceConfiguration resetTemporalStateOnAspectRatioChange];
-[BWDisparityPostProcessingInferenceConfiguration disparityFormat];
-[BWDisparityPostProcessingInferenceConfiguration initWithConcurrencyWidth:inputDimensions:outputDimensions:disparityFormat:portType:resetTemporalStateOnAspectRatioChange:appliesValidBufferRectPadding:];
```
