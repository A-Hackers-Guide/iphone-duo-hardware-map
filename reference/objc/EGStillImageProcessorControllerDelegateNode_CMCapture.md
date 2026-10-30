# `EGStillImageProcessorControllerDelegateNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGQueueManagementNode`
- Protocols: `BWStillImageProcessorControllerDelegate`, `BWInferencePixelBufferPoolProvider`
- 1 instance variables, 4 properties, 15 instance methods, 6 class methods

## Instance variables

```
@"<BWStillImageProcessingCoordinatorDelegate>" _processingCoordinatorDelegate;
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
+[EGStillImageProcessorControllerDelegateNode initialize];
+[EGStillImageProcessorControllerDelegateNode newProcessorControllerInput];
+[EGStillImageProcessorControllerDelegateNode newSbufInput];
+[EGStillImageProcessorControllerDelegateNode newSbufInputWithIndex:];
+[EGStillImageProcessorControllerDelegateNode newSbufOutput];
+[EGStillImageProcessorControllerDelegateNode newSbufOutputWithIndex:];
```

## Instance methods

```
-[EGStillImageProcessorControllerDelegateNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[EGStillImageProcessorControllerDelegateNode processorController:didFinishProcessingInput:err:];
-[EGStillImageProcessorControllerDelegateNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageProcessorControllerDelegateNode processorController:newOutputPixelBufferForProcessorInput:type:];
-[EGStillImageProcessorControllerDelegateNode processorController:newOutputPixelBufferForProcessorInput:type:dimensions:];
-[EGStillImageProcessorControllerDelegateNode processorControllerWillProcessInferences:];
-[EGStillImageProcessorControllerDelegateNode processorController:newInferencesForProcessorInput:];
-[EGStillImageProcessorControllerDelegateNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:];
-[EGStillImageProcessorControllerDelegateNode processorController:outputPixelBufferDimensionsForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:];
-[EGStillImageProcessorControllerDelegateNode processorController:willAddSampleBuffer:processorInput:];
-[EGStillImageProcessorControllerDelegateNode processorController:newInferencesForProcessorInput:inferenceInputBufferType:];
-[EGStillImageProcessorControllerDelegateNode processorController:didSelectFusionMode:processorInput:];
-[EGStillImageProcessorControllerDelegateNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:dimensionAlignment:];
-[EGStillImageProcessorControllerDelegateNode processorController:newOutputPixelBufferForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:];
-[EGStillImageProcessorControllerDelegateNode initWithName:delegate:];
```
