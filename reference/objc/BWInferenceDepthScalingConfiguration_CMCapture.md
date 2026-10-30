# `BWInferenceDepthScalingConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 12 instance variables, 12 properties, 19 instance methods, 0 class methods

## Instance variables

```
{?="width"i"height"i} _inputDimensions;
{?="width"i"height"i} _outputDimensions;
I _outputFormat;
@"NSString" _inputAttachedMediaKey;
@"NSString" _outputAttachedMediaKey;
B _flipX;
i _rotationDegrees;
@"NSNumber" _clampMin;
@"NSNumber" _clampMax;
@"NSNumber" _NANValue;
B _allowUpsampling;
Q _concurrencyWidth;
```

## Properties

```
@property (T{?=ii},N,V_inputDimensions) inputDimensions;
@property (T{?=ii},N,V_outputDimensions) outputDimensions;
@property (TI,N,V_outputFormat) outputFormat;
@property (T@"NSString",&,N,V_inputAttachedMediaKey) inputAttachedMediaKey;
@property (T@"NSString",&,N,V_outputAttachedMediaKey) outputAttachedMediaKey;
@property (TB,R,N,V_flipX) flipX;
@property (Ti,R,N,V_rotationDegrees) rotationDegrees;
@property (T@"NSNumber",R,N,V_NANValue) NANValue;
@property (T@"NSNumber",R,N,V_clampMin) clampMin;
@property (T@"NSNumber",R,N,V_clampMax) clampMax;
@property (TB,R,N,V_allowUpsampling) allowUpsampling;
@property (TQ,R,N,V_concurrencyWidth) concurrencyWidth;
```

## Instance methods

```
-[BWInferenceDepthScalingConfiguration setOutputDimensions:];
-[BWInferenceDepthScalingConfiguration setOutputFormat:];
-[BWInferenceDepthScalingConfiguration rotationDegrees];
-[BWInferenceDepthScalingConfiguration dealloc];
-[BWInferenceDepthScalingConfiguration concurrencyWidth];
-[BWInferenceDepthScalingConfiguration outputDimensions];
-[BWInferenceDepthScalingConfiguration inputDimensions];
-[BWInferenceDepthScalingConfiguration setInputDimensions:];
-[BWInferenceDepthScalingConfiguration outputFormat];
-[BWInferenceDepthScalingConfiguration NANValue];
-[BWInferenceDepthScalingConfiguration allowUpsampling];
-[BWInferenceDepthScalingConfiguration clampMax];
-[BWInferenceDepthScalingConfiguration clampMin];
-[BWInferenceDepthScalingConfiguration flipX];
-[BWInferenceDepthScalingConfiguration initWithFlipX:rotationDegrees:clampMin:clampMax:NANValue:allowUpsampling:concurrencyWidth:];
-[BWInferenceDepthScalingConfiguration inputAttachedMediaKey];
-[BWInferenceDepthScalingConfiguration outputAttachedMediaKey];
-[BWInferenceDepthScalingConfiguration setInputAttachedMediaKey:];
-[BWInferenceDepthScalingConfiguration setOutputAttachedMediaKey:];
```
