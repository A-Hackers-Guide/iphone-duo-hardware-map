# `BWPhotoEncoderNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWPhotoEncoderControllerDelegate`
- 7 instance variables, 4 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"NSDictionary" _sensorConfigurationsByPortType;
@"NSDictionary" _attachedMediaConfigurationByAttachedMediaKey;
@"BWPhotoEncoderControllerConfiguration" _photoEncoderControllerConfiguration;
@"BWPhotoEncoderController" _photoEncoderController;
@"NSString" _lastProcessedCaptureIdentifier;
B _preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPhotoEncoderNode initialize];
```

## Instance methods

```
-[BWPhotoEncoderNode prepareForCurrentConfigurationToBecomeLive];
-[BWPhotoEncoderNode smartStyleReversibilityEnabled];
-[BWPhotoEncoderNode processorController:didFinishProcessingInput:err:];
-[BWPhotoEncoderNode setPreferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer:];
-[BWPhotoEncoderNode usesHighEncodingPriority];
-[BWPhotoEncoderNode setRawColorCalibrationsByPortType:];
-[BWPhotoEncoderNode rawLensShadingCorrectionCoefficientsByPortType];
-[BWPhotoEncoderNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[BWPhotoEncoderNode setCameraSupportsFlash:];
-[BWPhotoEncoderNode renderSampleBuffer:forInput:];
-[BWPhotoEncoderNode rawColorCalibrationsByPortType];
-[BWPhotoEncoderNode setSmartStyleReversibilityEnabled:];
-[BWPhotoEncoderNode processorController:newOutputPixelBufferForProcessorInput:type:];
-[BWPhotoEncoderNode photoEncoderController];
-[BWPhotoEncoderNode preferMainImageDownscalingFactorByAttachedMediaKeyFromSampleBuffer];
-[BWPhotoEncoderNode cameraSupportsFlash];
-[BWPhotoEncoderNode smartStyleRenderingVersion];
-[BWPhotoEncoderNode processorController:newOutputPixelBufferForProcessorInput:type:dimensions:];
-[BWPhotoEncoderNode setSmartStyleRenderingVersion:];
-[BWPhotoEncoderNode setTextureStyleCreativeEffectsEnabled:];
-[BWPhotoEncoderNode zeroShutterLagEnabled];
-[BWPhotoEncoderNode inputColorInfo];
-[BWPhotoEncoderNode setRawLensShadingCorrectionCoefficientsByPortType:];
-[BWPhotoEncoderNode dealloc];
-[BWPhotoEncoderNode setZeroShutterLagEnabled:];
-[BWPhotoEncoderNode initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:clientIsCameraOrDerivative:];
-[BWPhotoEncoderNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWPhotoEncoderNode setUsesHighEncodingPriority:];
-[BWPhotoEncoderNode setInputColorInfo:];
-[BWPhotoEncoderNode setAttachedMediaConfigurationByAttachedMediaKey:];
-[BWPhotoEncoderNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWPhotoEncoderNode didReachEndOfDataForConfigurationID:input:];
-[BWPhotoEncoderNode nodeSubType];
-[BWPhotoEncoderNode attachedMediaConfigurationByAttachedMediaKey];
-[BWPhotoEncoderNode handleNodeError:forInput:];
-[BWPhotoEncoderNode nodeType];
```
