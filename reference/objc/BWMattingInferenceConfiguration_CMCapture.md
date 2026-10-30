# `BWMattingInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
f _mainImageDownscalingFactor;
B _refinedDepthDeliveryEnabled;
@"<MTLCommandQueue>" _metalCommandQueue;
@"NSDictionary" _sdofRenderingTuningParameters;
```

## Properties

```
@property (Tf,N,V_mainImageDownscalingFactor) mainImageDownscalingFactor;
@property (TB,N,V_refinedDepthDeliveryEnabled) refinedDepthDeliveryEnabled;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (T@"NSDictionary",&,N,V_sdofRenderingTuningParameters) sdofRenderingTuningParameters;
```

## Instance methods

```
-[BWMattingInferenceConfiguration setMetalCommandQueue:];
-[BWMattingInferenceConfiguration metalCommandQueue];
-[BWMattingInferenceConfiguration setMainImageDownscalingFactor:];
-[BWMattingInferenceConfiguration mainImageDownscalingFactor];
-[BWMattingInferenceConfiguration dealloc];
-[BWMattingInferenceConfiguration setSdofRenderingTuningParameters:];
-[BWMattingInferenceConfiguration sdofRenderingTuningParameters];
-[BWMattingInferenceConfiguration setRefinedDepthDeliveryEnabled:];
-[BWMattingInferenceConfiguration refinedDepthDeliveryEnabled];
```
