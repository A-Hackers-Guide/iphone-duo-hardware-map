# `EGStillImageStereoDisparityNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWStereoDisparityProcessorControllerDelegate`
- 6 instance variables, 8 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _primarySbufInput;
@"EGInput" _secondarySbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"NSString" _portType;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_primarySbufInput) primarySbufInput;
@property (T@"EGInput",R,N,V_secondarySbufInput) secondarySbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageStereoDisparityNode initialize];
```

## Instance methods

```
-[EGStillImageStereoDisparityNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageStereoDisparityNode processorControllerWillProcessInferences:];
-[EGStillImageStereoDisparityNode dealloc];
-[EGStillImageStereoDisparityNode initWithName:stillImageSettings:portType:delegate:];
-[EGStillImageStereoDisparityNode primarySbufInput];
-[EGStillImageStereoDisparityNode processorInput];
-[EGStillImageStereoDisparityNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageStereoDisparityNode sbufOutput];
-[EGStillImageStereoDisparityNode secondarySbufInput];
```
