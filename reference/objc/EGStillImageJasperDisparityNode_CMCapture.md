# `EGStillImageJasperDisparityNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWJasperDisparityProcessorControllerDelegate`
- 6 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"NSString" _portType;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageJasperDisparityNode initialize];
```

## Instance methods

```
-[EGStillImageJasperDisparityNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageJasperDisparityNode dealloc];
-[EGStillImageJasperDisparityNode initWithName:stillImageSettings:resourceCoordinator:portType:delegate:];
-[EGStillImageJasperDisparityNode processorInput];
-[EGStillImageJasperDisparityNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageJasperDisparityNode sbufInput];
-[EGStillImageJasperDisparityNode sbufOutput];
```
