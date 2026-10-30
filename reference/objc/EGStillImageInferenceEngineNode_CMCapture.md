# `EGStillImageInferenceEngineNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWInferenceEngineControllerDelegate`
- 10 instance variables, 8 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _inferencesDeliveredOutput;
@"BWStillImageSettings" _stillImageSettings;
@"NSString" _portType;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
Q _inferenceInputBufferType;
i _mode;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_inferencesDeliveredOutput) inferencesDeliveredOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageInferenceEngineNode initialize];
```

## Instance methods

```
-[EGStillImageInferenceEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageInferenceEngineNode dealloc];
-[EGStillImageInferenceEngineNode inferencesDeliveredOutput];
-[EGStillImageInferenceEngineNode initWithName:stillImageSettings:portType:nodeConfiguration:resourceCoordinator:inferenceInputBufferType:mode:delegate:];
-[EGStillImageInferenceEngineNode processorInput];
-[EGStillImageInferenceEngineNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageInferenceEngineNode sbufInput];
-[EGStillImageInferenceEngineNode sbufOutput];
```
