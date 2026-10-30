# `EGStillImageSmartStyleRenderingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWSmartStyleRenderingProcessorControllerDelegate`
- 5 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
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
+[EGStillImageSmartStyleRenderingNode initialize];
```

## Instance methods

```
-[EGStillImageSmartStyleRenderingNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageSmartStyleRenderingNode dealloc];
-[EGStillImageSmartStyleRenderingNode initWithName:stillImageSettings:portType:delegate:];
-[EGStillImageSmartStyleRenderingNode processorInput];
-[EGStillImageSmartStyleRenderingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageSmartStyleRenderingNode sbufInput];
-[EGStillImageSmartStyleRenderingNode sbufOutput];
```
