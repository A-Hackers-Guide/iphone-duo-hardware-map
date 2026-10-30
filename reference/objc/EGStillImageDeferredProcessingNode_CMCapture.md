# `EGStillImageDeferredProcessingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWDeferredProcessorControllerDelegate`
- 12 instance variables, 12 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _referenceFrameOutput;
@"EGStillImageOutput" _inferencesDeliveredOutput;
@"NSArray" _sbufOutputs;
@"EGStillImageOutput" _stereoPhotoPrimarySbufOutput;
@"EGStillImageOutput" _stereoPhotoSecondarySbufOutput;
@"EGStillImageOutput" _provenanceFrameOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"NSString" _portType;
i _sbufOutputCount;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_referenceFrameOutput) referenceFrameOutput;
@property (T@"EGOutput",R,N,V_inferencesDeliveredOutput) inferencesDeliveredOutput;
@property (T@"NSArray",R,N,V_sbufOutputs) sbufOutputs;
@property (T@"EGOutput",R,N,V_stereoPhotoPrimarySbufOutput) stereoPhotoPrimarySbufOutput;
@property (T@"EGOutput",R,N,V_stereoPhotoSecondarySbufOutput) stereoPhotoSecondarySbufOutput;
@property (T@"EGOutput",R,N,V_provenanceFrameOutput) provenanceFrameOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageDeferredProcessingNode initialize];
```

## Instance methods

```
-[EGStillImageDeferredProcessingNode processorController:didFinishProcessingInput:err:];
-[EGStillImageDeferredProcessingNode processorController:didFinishProcessingInferenceBuffer:metadata:inferenceAttachedMediaKey:processorInput:err:];
-[EGStillImageDeferredProcessingNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageDeferredProcessingNode processorController:didFinishProcessingInferenceAttachedMediaMetadata:processorInput:];
-[EGStillImageDeferredProcessingNode dealloc];
-[EGStillImageDeferredProcessingNode processorController:didDetermineProvenanceFrame:processorInput:err:];
-[EGStillImageDeferredProcessingNode processorController:didFinishProcessingInference:inferenceAttachmentKey:processorInput:err:];
-[EGStillImageDeferredProcessingNode processorController:didDetermineReferenceFrame:processorInput:err:];
-[EGStillImageDeferredProcessingNode inferencesDeliveredOutput];
-[EGStillImageDeferredProcessingNode initWithName:stillImageSettings:resourceCoordinator:numSbufOutputs:portType:delegate:];
-[EGStillImageDeferredProcessingNode processorInput];
-[EGStillImageDeferredProcessingNode provenanceFrameOutput];
-[EGStillImageDeferredProcessingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageDeferredProcessingNode referenceFrameOutput];
-[EGStillImageDeferredProcessingNode sbufInput];
-[EGStillImageDeferredProcessingNode sbufOutputs];
-[EGStillImageDeferredProcessingNode stereoPhotoPrimarySbufOutput];
-[EGStillImageDeferredProcessingNode stereoPhotoSecondarySbufOutput];
```
