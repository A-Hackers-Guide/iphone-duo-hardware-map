# `EGStillImageSingleImageNRFNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWNRFProcessorControllerDelegate`
- 16 instance variables, 14 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _inferenceInputImageOutput;
@"EGStillImageOutput" _earlyGainMapOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSString" _portType;
B _processLinearImage;
B _processToneMapping;
B _processInferenceInputImage;
B _provideInferenceInputImageForProcessing;
B _emitGainMapEarlyForPiecemealEncoding;
B _processSmartStyleRenderingInput;
B _inferencesAvailable;
^{opaqueCMSampleBuffer=} _sbufForGainMapEmission;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_inferenceInputImageOutput) inferenceInputImageOutput;
@property (T@"EGOutput",R,N,V_earlyGainMapOutput) earlyGainMapOutput;
@property (TB,N,V_processLinearImage) processLinearImage;
@property (TB,N,V_processToneMapping) processToneMapping;
@property (TB,N,V_processInferenceInputImage) processInferenceInputImage;
@property (TB,N,V_processSmartStyleRenderingInput) processSmartStyleRenderingInput;
@property (TB,N,V_inferencesAvailable) inferencesAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageSingleImageNRFNode initialize];
```

## Instance methods

```
-[EGStillImageSingleImageNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageSingleImageNRFNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:];
-[EGStillImageSingleImageNRFNode dealloc];
-[EGStillImageSingleImageNRFNode processorController:willAddSampleBuffer:processorInput:];
-[EGStillImageSingleImageNRFNode inferencesAvailable];
-[EGStillImageSingleImageNRFNode processSmartStyleRenderingInput];
-[EGStillImageSingleImageNRFNode earlyGainMapOutput];
-[EGStillImageSingleImageNRFNode inferenceInputImageOutput];
-[EGStillImageSingleImageNRFNode initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:emitGainMapEarlyForPiecemealEncoding:portType:delegate:];
-[EGStillImageSingleImageNRFNode processInferenceInputImage];
-[EGStillImageSingleImageNRFNode processLinearImage];
-[EGStillImageSingleImageNRFNode processToneMapping];
-[EGStillImageSingleImageNRFNode processorInput];
-[EGStillImageSingleImageNRFNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageSingleImageNRFNode sbufInput];
-[EGStillImageSingleImageNRFNode sbufOutput];
-[EGStillImageSingleImageNRFNode setInferencesAvailable:];
-[EGStillImageSingleImageNRFNode setProcessInferenceInputImage:];
-[EGStillImageSingleImageNRFNode setProcessLinearImage:];
-[EGStillImageSingleImageNRFNode setProcessSmartStyleRenderingInput:];
-[EGStillImageSingleImageNRFNode setProcessToneMapping:];
```
