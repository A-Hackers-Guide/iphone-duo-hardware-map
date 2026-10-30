# `EGStillImageSoftISPNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWSoftISPProcessorControllerDelegate`
- 9 instance variables, 9 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGInput" _gatingInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _processingCompleteOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSString" _portType;
i _processingMode;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGInput",R,N,V_gatingInput) gatingInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_processingCompleteOutput) processingCompleteOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageSoftISPNode initialize];
```

## Instance methods

```
-[EGStillImageSoftISPNode processorController:didFinishProcessingInput:err:];
-[EGStillImageSoftISPNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageSoftISPNode dealloc];
-[EGStillImageSoftISPNode processorController:willAddSampleBuffer:processorInput:];
-[EGStillImageSoftISPNode gatingInput];
-[EGStillImageSoftISPNode initWithName:stillImageSettings:nodeConfiguration:portType:processingMode:addGatingInput:delegate:];
-[EGStillImageSoftISPNode processingCompleteOutput];
-[EGStillImageSoftISPNode processorInput];
-[EGStillImageSoftISPNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageSoftISPNode sbufInput];
-[EGStillImageSoftISPNode sbufOutput];
```
