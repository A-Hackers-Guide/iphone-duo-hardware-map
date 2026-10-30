# `EGStillImageSWFRNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWSWFRProcessorControllerDelegate`
- 7 instance variables, 8 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _flashSbufInput;
@"EGInput" _ambientSbufInput;
@"EGStillImageOutput" _sbufOutput;
@"NSString" _portType;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_flashSbufInput) flashSbufInput;
@property (T@"EGInput",R,N,V_ambientSbufInput) ambientSbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageSWFRNode initialize];
```

## Instance methods

```
-[EGStillImageSWFRNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageSWFRNode dealloc];
-[EGStillImageSWFRNode ambientSbufInput];
-[EGStillImageSWFRNode flashSbufInput];
-[EGStillImageSWFRNode initWithName:stillImageSettings:nodeConfiguration:portType:delegate:];
-[EGStillImageSWFRNode processorInput];
-[EGStillImageSWFRNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageSWFRNode sbufOutput];
```
