# `EGStillImageDCNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- 11 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGInput" _configurationInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"NSString" _portType;
B _processIDC;
B _processGDC;
B _deepZoomEnabled;
Q _inputImageBufferType;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGInput",R,N,V_configurationInput) configurationInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
```

## Class methods

```
+[EGStillImageDCNode initialize];
```

## Instance methods

```
-[EGStillImageDCNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageDCNode dealloc];
-[EGStillImageDCNode configurationInput];
-[EGStillImageDCNode initWithName:stillImageSettings:nodeConfiguration:addConfigurationInput:processIDC:processGDC:deepZoomEnabled:inputImageBufferType:portType:delegate:];
-[EGStillImageDCNode processorInput];
-[EGStillImageDCNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageDCNode sbufInput];
-[EGStillImageDCNode sbufOutput];
```
