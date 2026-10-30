# `EGStillImageDeepZoomNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWDeepZoomProcessorControllerDelegate`
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
+[EGStillImageDeepZoomNode initialize];
```

## Instance methods

```
-[EGStillImageDeepZoomNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageDeepZoomNode dealloc];
-[EGStillImageDeepZoomNode initWithName:stillImageSettings:portType:delegate:];
-[EGStillImageDeepZoomNode processorInput];
-[EGStillImageDeepZoomNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageDeepZoomNode sbufInput];
-[EGStillImageDeepZoomNode sbufOutput];
```
