# `EGStillImageLearnedFusionNRFNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWNRFProcessorControllerDelegate`
- 18 instance variables, 13 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _referenceFrameInput;
@"NSArray" _primarySbufInputs;
@"EGInput" _hdrErrorRecoveryEVZeroInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _fusionModeOutput;
@"EGStillImageOutput" _inferenceInputImageOutput;
@"EGStillImageOutput" _attemptErrorRecoveryOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSString" _portType;
B _provideInferenceInputImageForProcessing;
B _processSmartStyleRenderingInput;
@"BWNRFProcessorInput" _nrfProcessorControllerInput;
@"BWNRFProcessorInput" _nrfProcessorControllerErrorRecoveryInput;
i _errorCodeTriggeringErrorRecovery;
@"BWNRFProcessorController" _stashedNRFProcessorController;
B _handleSyncErrorRecovery;
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
@property (TB,N,V_processSmartStyleRenderingInput) processSmartStyleRenderingInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageLearnedFusionNRFNode initialize];
```

## Instance methods

```
-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingInput:err:];
-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:];
-[EGStillImageLearnedFusionNRFNode dealloc];
-[EGStillImageLearnedFusionNRFNode processorController:willAddSampleBuffer:processorInput:];
-[EGStillImageLearnedFusionNRFNode processorController:didSelectFusionMode:processorInput:];
-[EGStillImageLearnedFusionNRFNode processSmartStyleRenderingInput];
-[EGStillImageLearnedFusionNRFNode attemptErrorRecoveryOutput];
-[EGStillImageLearnedFusionNRFNode fusionModeOutput];
-[EGStillImageLearnedFusionNRFNode hdrErrorRecoveryEVZeroInput];
-[EGStillImageLearnedFusionNRFNode inferenceInputImageOutput];
-[EGStillImageLearnedFusionNRFNode initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:addSyncErrorRecoveryPorts:portType:delegate:];
-[EGStillImageLearnedFusionNRFNode primarySbufInputs];
-[EGStillImageLearnedFusionNRFNode processorInput];
-[EGStillImageLearnedFusionNRFNode queueManagedReceiveData:fromInput:];
-[EGStillImageLearnedFusionNRFNode referenceFrameInput];
-[EGStillImageLearnedFusionNRFNode sbufOutput];
-[EGStillImageLearnedFusionNRFNode setProcessSmartStyleRenderingInput:];
```
