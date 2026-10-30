# `BWDeepFusionProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 9 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
{?="width"i"height"i} _maxInputDimensions;
{?="width"i"height"i} _maxOutputDimensions;
B _cmiResourceEnabled;
B _quadraSupportEnabled;
i _stillImageFusionScheme;
i _semanticRenderingVersion;
@"NSDictionary" _rawColorCalibrationsByPortType;
B _delayPrepareAndCacheBuffers;
f _gainMapMainImageDownscalingFactor;
```

## Properties

```
@property (T{?=ii},N,V_maxInputDimensions) maxInputDimensions;
@property (T{?=ii},N,V_maxOutputDimensions) maxOutputDimensions;
@property (TB,N,V_cmiResourceEnabled) cmiResourceEnabled;
@property (TB,N,V_quadraSupportEnabled) quadraSupportEnabled;
@property (Ti,N,V_stillImageFusionScheme) stillImageFusionScheme;
@property (Ti,N,V_semanticRenderingVersion) semanticRenderingVersion;
@property (T@"NSDictionary",&,N,V_rawColorCalibrationsByPortType) rawColorCalibrationsByPortType;
@property (TB,N,V_delayPrepareAndCacheBuffers) delayPrepareAndCacheBuffers;
@property (Tf,N,V_gainMapMainImageDownscalingFactor) gainMapMainImageDownscalingFactor;
```

## Instance methods

```
-[BWDeepFusionProcessorControllerConfiguration setStillImageFusionScheme:];
-[BWDeepFusionProcessorControllerConfiguration gainMapMainImageDownscalingFactor];
-[BWDeepFusionProcessorControllerConfiguration setGainMapMainImageDownscalingFactor:];
-[BWDeepFusionProcessorControllerConfiguration stillImageFusionScheme];
-[BWDeepFusionProcessorControllerConfiguration setCmiResourceEnabled:];
-[BWDeepFusionProcessorControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWDeepFusionProcessorControllerConfiguration semanticRenderingVersion];
-[BWDeepFusionProcessorControllerConfiguration setSemanticRenderingVersion:];
-[BWDeepFusionProcessorControllerConfiguration rawColorCalibrationsByPortType];
-[BWDeepFusionProcessorControllerConfiguration dealloc];
-[BWDeepFusionProcessorControllerConfiguration setMaxInputDimensions:];
-[BWDeepFusionProcessorControllerConfiguration setQuadraSupportEnabled:];
-[BWDeepFusionProcessorControllerConfiguration maxInputDimensions];
-[BWDeepFusionProcessorControllerConfiguration quadraSupportEnabled];
-[BWDeepFusionProcessorControllerConfiguration cmiResourceEnabled];
-[BWDeepFusionProcessorControllerConfiguration setDelayPrepareAndCacheBuffers:];
-[BWDeepFusionProcessorControllerConfiguration delayPrepareAndCacheBuffers];
-[BWDeepFusionProcessorControllerConfiguration maxOutputDimensions];
-[BWDeepFusionProcessorControllerConfiguration setMaxOutputDimensions:];
```
