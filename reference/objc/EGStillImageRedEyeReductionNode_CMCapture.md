# `EGStillImageRedEyeReductionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWRedEyeReductionControllerDelegate`
- 11 instance variables, 9 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGInput" _auxSbufInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _gateAuxProcessingOutput;
@"BWRedEyeReductionControllerInput" _redEyeReductionControllerInput;
@"NSArray" _faceObservations;
B _auxProcessingRequested;
@"NSString" _portType;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_gateAuxProcessingOutput) gateAuxProcessingOutput;
@property (T@"EGInput",R,N,V_auxSbufInput) auxSbufInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageRedEyeReductionNode initialize];
```

## Instance methods

```
-[EGStillImageRedEyeReductionNode processorController:didFinishProcessingInput:err:];
-[EGStillImageRedEyeReductionNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageRedEyeReductionNode processorController:willProcessRedEyeReductionForProcessorInput:];
-[EGStillImageRedEyeReductionNode dealloc];
-[EGStillImageRedEyeReductionNode auxSbufInput];
-[EGStillImageRedEyeReductionNode gateAuxProcessingOutput];
-[EGStillImageRedEyeReductionNode initWithName:stillImageSettings:nodeConfiguration:portType:delegate:];
-[EGStillImageRedEyeReductionNode processorInput];
-[EGStillImageRedEyeReductionNode queueManagedReceiveData:fromInput:];
-[EGStillImageRedEyeReductionNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageRedEyeReductionNode sbufInput];
-[EGStillImageRedEyeReductionNode sbufOutput];
```
