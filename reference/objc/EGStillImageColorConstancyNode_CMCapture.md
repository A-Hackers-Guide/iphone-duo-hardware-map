# `EGStillImageColorConstancyNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWColorConstancyProcessorControllerDelegate`
- 6 instance variables, 8 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _flashSbufInput;
@"EGInput" _ambientSbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"NSString" _portType;
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
+[EGStillImageColorConstancyNode initialize];
```

## Instance methods

```
-[EGStillImageColorConstancyNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageColorConstancyNode dealloc];
-[EGStillImageColorConstancyNode ambientSbufInput];
-[EGStillImageColorConstancyNode flashSbufInput];
-[EGStillImageColorConstancyNode initWithName:stillImageSettings:portType:delegate:];
-[EGStillImageColorConstancyNode processorInput];
-[EGStillImageColorConstancyNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageColorConstancyNode sbufOutput];
```
