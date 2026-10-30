# `BWInferenceEngineControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 10 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _inferenceImage;
^{opaqueCMSampleBuffer=} _propagationImage;
@"NSArray" _enabledInferenceMasks;
B _smartCameraClassificationsEnabled;
B _faceAndInstanceSegmentationEnabled;
Q _enabledVisionInferences;
B _expectsMoreData;
Q _inferenceInputBufferType;
Q _bufferTypeOverride;
B _textOrientationInferenceEnabled;
```

## Properties

```
@property (TB,R,N,V_expectsMoreData) expectsMoreData;
@property (TQ,R,N,V_inferenceInputBufferType) inferenceInputBufferType;
@property (T^{opaqueCMSampleBuffer=},R,N,V_inferenceImage) inferenceImage;
@property (T^{opaqueCMSampleBuffer=},R,N,V_propagationImage) propagationImage;
@property (T@"NSArray",C,N,V_enabledInferenceMasks) enabledInferenceMasks;
@property (TB,N,V_smartCameraClassificationsEnabled) smartCameraClassificationsEnabled;
@property (TB,N,V_faceAndInstanceSegmentationEnabled) faceAndInstanceSegmentationEnabled;
@property (TB,N,V_textOrientationInferenceEnabled) textOrientationInferenceEnabled;
@property (TQ,N,V_enabledVisionInferences) enabledVisionInferences;
@property (TQ,N,V_bufferTypeOverride) bufferTypeOverride;
```

## Instance methods

```
-[BWInferenceEngineControllerInput inferenceImage];
-[BWInferenceEngineControllerInput textOrientationInferenceEnabled];
-[BWInferenceEngineControllerInput enabledVisionInferences];
-[BWInferenceEngineControllerInput setSmartCameraClassificationsEnabled:];
-[BWInferenceEngineControllerInput inferenceInputBufferType];
-[BWInferenceEngineControllerInput dealloc];
-[BWInferenceEngineControllerInput expectsMoreData];
-[BWInferenceEngineControllerInput initWithSettings:portType:inferenceInputBufferType:];
-[BWInferenceEngineControllerInput addInferenceImage:];
-[BWInferenceEngineControllerInput smartCameraClassificationsEnabled];
-[BWInferenceEngineControllerInput enabledInferenceMasks];
-[BWInferenceEngineControllerInput bufferTypeOverride];
-[BWInferenceEngineControllerInput faceAndInstanceSegmentationEnabled];
-[BWInferenceEngineControllerInput setTextOrientationInferenceEnabled:];
-[BWInferenceEngineControllerInput propagationImage];
-[BWInferenceEngineControllerInput description];
-[BWInferenceEngineControllerInput setEnabledInferenceMasks:];
-[BWInferenceEngineControllerInput setEnabledVisionInferences:];
-[BWInferenceEngineControllerInput setBufferTypeOverride:];
-[BWInferenceEngineControllerInput setFaceAndInstanceSegmentationEnabled:];
-[BWInferenceEngineControllerInput waitForAsyncProcessingAndReleaseImages];
-[BWInferenceEngineControllerInput addInferenceImage:propagationImage:];
-[BWInferenceEngineControllerInput initWithSettings:portType:];
```
