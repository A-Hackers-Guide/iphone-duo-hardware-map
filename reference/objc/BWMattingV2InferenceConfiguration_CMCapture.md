# `BWMattingV2InferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 14 instance variables, 14 properties, 31 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _sensorConfigurationsByPortType;
I _enabledMattes;
i _tuningConfiguration;
f _mainImageDownscalingFactor;
f _targetAspectRatio;
B _appliesFinalCropRect;
B _depthDataDeliveryEnabled;
B _submitWithoutSynchronization;
@"<MTLCommandQueue>" _metalCommandQueue;
B _submitWithElevatedGPUPriority;
@"NSDictionary" _sdofRenderingTuningParameters;
i _stillImageFusionScheme;
B _inputSegmentationPortraitOrientationSupportEnabled;
@"NSString" _inferenceInputAttachedMediaKey;
```

## Properties

```
@property (TB,N,V_inputSegmentationPortraitOrientationSupportEnabled) inputSegmentationPortraitOrientationSupportEnabled;
@property (T@"NSDictionary",&,N,V_sensorConfigurationsByPortType) sensorConfigurationsByPortType;
@property (TI,N,V_enabledMattes) enabledMattes;
@property (Ti,N,V_tuningConfiguration) tuningConfiguration;
@property (Tf,N,V_mainImageDownscalingFactor) mainImageDownscalingFactor;
@property (Tf,N,V_targetAspectRatio) targetAspectRatio;
@property (TB,N,V_appliesFinalCropRect) appliesFinalCropRect;
@property (TB,N,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N,V_submitWithoutSynchronization) submitWithoutSynchronization;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,N,V_submitWithElevatedGPUPriority) submitWithElevatedGPUPriority;
@property (T@"NSDictionary",&,N,V_sdofRenderingTuningParameters) sdofRenderingTuningParameters;
@property (Ti,N,V_stillImageFusionScheme) stillImageFusionScheme;
@property (T@"NSString",&,N,V_inferenceInputAttachedMediaKey) inferenceInputAttachedMediaKey;
```

## Class methods

```
+[BWMattingV2InferenceConfiguration inputAttachedMediaKeyForMattingOutputType:];
+[BWMattingV2InferenceConfiguration isMattingOutputAttachedMediaKey:];
+[BWMattingV2InferenceConfiguration mattingOutputTypeForAttachedMediaKey:];
```

## Instance methods

```
-[BWMattingV2InferenceConfiguration setStillImageFusionScheme:];
-[BWMattingV2InferenceConfiguration setMetalCommandQueue:];
-[BWMattingV2InferenceConfiguration stillImageFusionScheme];
-[BWMattingV2InferenceConfiguration setInferenceInputAttachedMediaKey:];
-[BWMattingV2InferenceConfiguration metalCommandQueue];
-[BWMattingV2InferenceConfiguration initWithInferenceType:];
-[BWMattingV2InferenceConfiguration inferenceInputAttachedMediaKey];
-[BWMattingV2InferenceConfiguration sensorConfigurationsByPortType];
-[BWMattingV2InferenceConfiguration targetAspectRatio];
-[BWMattingV2InferenceConfiguration setTuningConfiguration:];
-[BWMattingV2InferenceConfiguration appliesFinalCropRect];
-[BWMattingV2InferenceConfiguration setMainImageDownscalingFactor:];
-[BWMattingV2InferenceConfiguration mainImageDownscalingFactor];
-[BWMattingV2InferenceConfiguration dealloc];
-[BWMattingV2InferenceConfiguration setTargetAspectRatio:];
-[BWMattingV2InferenceConfiguration setInputSegmentationPortraitOrientationSupportEnabled:];
-[BWMattingV2InferenceConfiguration tuningConfiguration];
-[BWMattingV2InferenceConfiguration setSubmitWithElevatedGPUPriority:];
-[BWMattingV2InferenceConfiguration setSdofRenderingTuningParameters:];
-[BWMattingV2InferenceConfiguration sdofRenderingTuningParameters];
-[BWMattingV2InferenceConfiguration setAppliesFinalCropRect:];
-[BWMattingV2InferenceConfiguration description];
-[BWMattingV2InferenceConfiguration setDepthDataDeliveryEnabled:];
-[BWMattingV2InferenceConfiguration submitWithElevatedGPUPriority];
-[BWMattingV2InferenceConfiguration enabledMattes];
-[BWMattingV2InferenceConfiguration setSensorConfigurationsByPortType:];
-[BWMattingV2InferenceConfiguration setSubmitWithoutSynchronization:];
-[BWMattingV2InferenceConfiguration inputSegmentationPortraitOrientationSupportEnabled];
-[BWMattingV2InferenceConfiguration submitWithoutSynchronization];
-[BWMattingV2InferenceConfiguration depthDataDeliveryEnabled];
-[BWMattingV2InferenceConfiguration setEnabledMattes:];
```
