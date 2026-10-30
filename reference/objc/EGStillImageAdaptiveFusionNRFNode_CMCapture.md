# `EGStillImageAdaptiveFusionNRFNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWNRFProcessorControllerDelegate`
- 23 instance variables, 15 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _referenceFrameInput;
@"NSArray" _primarySbufInputs;
@"EGInput" _hdrErrorRecoveryEVZeroInput;
@"EGInput" _singleImageErrorRecoveryInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _fusionModeOutput;
@"EGStillImageOutput" _inferenceInputImageOutput;
@"EGStillImageOutput" _attemptErrorRecoveryOutput;
@"EGStillImageOutput" _attemptSingleImageErrorRecoveryOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSString" _portType;
B _provideInferenceInputImageForProcessing;
B _processSmartStyleRenderingInput;
@"BWNRFProcessorInput" _nrfProcessorControllerInput;
@"BWNRFProcessorInput" _nrfProcessorControllerErrorRecoveryInput;
@"BWNRFProcessorInput" _nrfProcessorControllerSingleImageRecoveryInput;
i _errorCodeTriggeringErrorRecovery;
@"BWNRFProcessorController" _stashedNRFProcessorController;
B _handleSyncErrorRecovery;
B _deliveredImage;
B _attemptedSingleImageRecovery;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"NSArray",R,N,V_primarySbufInputs) primarySbufInputs;
@property (T@"EGInput",R,N,V_referenceFrameInput) referenceFrameInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_fusionModeOutput) fusionModeOutput;
@property (T@"EGOutput",R,N,V_inferenceInputImageOutput) inferenceInputImageOutput;
@property (T@"EGInput",R,N,V_hdrErrorRecoveryEVZeroInput) hdrErrorRecoveryEVZeroInput;
@property (T@"EGOutput",R,N,V_attemptErrorRecoveryOutput) attemptErrorRecoveryOutput;
@property (T@"EGInput",R,N,V_singleImageErrorRecoveryInput) singleImageErrorRecoveryInput;
@property (T@"EGOutput",R,N,V_attemptSingleImageErrorRecoveryOutput) attemptSingleImageErrorRecoveryOutput;
@property (TB,N,V_processSmartStyleRenderingInput) processSmartStyleRenderingInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageAdaptiveFusionNRFNode initialize];
```

## Instance methods

```
-[EGStillImageAdaptiveFusionNRFNode processorController:didFinishProcessingInput:err:];
-[EGStillImageAdaptiveFusionNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageAdaptiveFusionNRFNode processorController:didSelectVitalityMode:forProcessorInput:];
-[EGStillImageAdaptiveFusionNRFNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:];
-[EGStillImageAdaptiveFusionNRFNode dealloc];
-[EGStillImageAdaptiveFusionNRFNode processorController:willAddSampleBuffer:processorInput:];
-[EGStillImageAdaptiveFusionNRFNode processorController:didSelectFusionMode:processorInput:];
-[EGStillImageAdaptiveFusionNRFNode processSmartStyleRenderingInput];
-[EGStillImageAdaptiveFusionNRFNode attemptErrorRecoveryOutput];
-[EGStillImageAdaptiveFusionNRFNode attemptSingleImageErrorRecoveryOutput];
-[EGStillImageAdaptiveFusionNRFNode fusionModeOutput];
-[EGStillImageAdaptiveFusionNRFNode hdrErrorRecoveryEVZeroInput];
-[EGStillImageAdaptiveFusionNRFNode inferenceInputImageOutput];
-[EGStillImageAdaptiveFusionNRFNode initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:addSyncErrorRecoveryPorts:portType:delegate:];
-[EGStillImageAdaptiveFusionNRFNode primarySbufInputs];
-[EGStillImageAdaptiveFusionNRFNode processorInput];
-[EGStillImageAdaptiveFusionNRFNode queueManagedReceiveData:fromInput:];
-[EGStillImageAdaptiveFusionNRFNode referenceFrameInput];
-[EGStillImageAdaptiveFusionNRFNode sbufOutput];
-[EGStillImageAdaptiveFusionNRFNode setProcessSmartStyleRenderingInput:];
-[EGStillImageAdaptiveFusionNRFNode singleImageErrorRecoveryInput];
```
