# `BWInferenceEngineControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 14 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"BWVideoFormat" _inputFormat;
f _mainImageDownscalingFactor;
@"NSArray" _enabledInferenceMasks;
B _mattingOutputValidContentDetectionEnabled;
B _fastMattingEnabled;
B _smartCameraClassificationsEnabled;
B _faceAndInstanceSegmentationEnabled;
Q _enabledVisionInferences;
i _personSemanticsVersion;
@"NSArray" _swfrInferenceMasks;
B _producesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom;
B _suppressVisionTimeOutFailure;
i _stillImageFusionScheme;
B _submitWithElevatedGPUPriority;
```

## Properties

```
@property (T@"BWVideoFormat",&,N,V_inputFormat) inputFormat;
@property (Tf,N,V_mainImageDownscalingFactor) mainImageDownscalingFactor;
@property (T@"NSArray",C,N,V_enabledInferenceMasks) enabledInferenceMasks;
@property (TB,N,V_mattingOutputValidContentDetectionEnabled) mattingOutputValidContentDetectionEnabled;
@property (TB,N,V_fastMattingEnabled) fastMattingEnabled;
@property (TB,N,V_smartCameraClassificationsEnabled) smartCameraClassificationsEnabled;
@property (TB,N,V_faceAndInstanceSegmentationEnabled) faceAndInstanceSegmentationEnabled;
@property (TQ,N,V_enabledVisionInferences) enabledVisionInferences;
@property (Ti,N,V_personSemanticsVersion) personSemanticsVersion;
@property (T@"NSArray",C,N,V_swfrInferenceMasks) swfrInferenceMasks;
@property (TB,N,V_producesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom) producesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom;
@property (TB,N,V_suppressVisionTimeOutFailure) suppressVisionTimeOutFailure;
@property (Ti,N,V_stillImageFusionScheme) stillImageFusionScheme;
@property (TB,N,V_submitWithElevatedGPUPriority) submitWithElevatedGPUPriority;
```

## Instance methods

```
-[BWInferenceEngineControllerConfiguration setStillImageFusionScheme:];
-[BWInferenceEngineControllerConfiguration personSemanticsVersion];
-[BWInferenceEngineControllerConfiguration stillImageFusionScheme];
-[BWInferenceEngineControllerConfiguration swfrInferenceMasks];
-[BWInferenceEngineControllerConfiguration setSuppressVisionTimeOutFailure:];
-[BWInferenceEngineControllerConfiguration setMainImageDownscalingFactor:];
-[BWInferenceEngineControllerConfiguration enabledVisionInferences];
-[BWInferenceEngineControllerConfiguration init];
-[BWInferenceEngineControllerConfiguration setSmartCameraClassificationsEnabled:];
-[BWInferenceEngineControllerConfiguration mainImageDownscalingFactor];
-[BWInferenceEngineControllerConfiguration inputFormat];
-[BWInferenceEngineControllerConfiguration dealloc];
-[BWInferenceEngineControllerConfiguration fastMattingEnabled];
-[BWInferenceEngineControllerConfiguration setPersonSemanticsVersion:];
-[BWInferenceEngineControllerConfiguration smartCameraClassificationsEnabled];
-[BWInferenceEngineControllerConfiguration enabledInferenceMasks];
-[BWInferenceEngineControllerConfiguration setInputFormat:];
-[BWInferenceEngineControllerConfiguration faceAndInstanceSegmentationEnabled];
-[BWInferenceEngineControllerConfiguration setSubmitWithElevatedGPUPriority:];
-[BWInferenceEngineControllerConfiguration setFastMattingEnabled:];
-[BWInferenceEngineControllerConfiguration setProducesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom:];
-[BWInferenceEngineControllerConfiguration setSwfrInferenceMasks:];
-[BWInferenceEngineControllerConfiguration description];
-[BWInferenceEngineControllerConfiguration setEnabledInferenceMasks:];
-[BWInferenceEngineControllerConfiguration setEnabledVisionInferences:];
-[BWInferenceEngineControllerConfiguration producesHighQualityInferencesFromZoomRegionWithLargeDigitalZoom];
-[BWInferenceEngineControllerConfiguration submitWithElevatedGPUPriority];
-[BWInferenceEngineControllerConfiguration suppressVisionTimeOutFailure];
-[BWInferenceEngineControllerConfiguration setFaceAndInstanceSegmentationEnabled:];
-[BWInferenceEngineControllerConfiguration mattingOutputValidContentDetectionEnabled];
-[BWInferenceEngineControllerConfiguration setMattingOutputValidContentDetectionEnabled:];
```
