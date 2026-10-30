# `EGStillImageScalerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- 9 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"NSString" _portType;
B _deepZoomEnabled;
Q _inputImageBufferType;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
```

## Class methods

```
+[EGStillImageScalerNode initialize];
```

## Instance methods

```
-[EGStillImageScalerNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageScalerNode dealloc];
-[EGStillImageScalerNode processorController:outputPixelBufferDimensionsForProcessorInput:type:attachedMediaKey:pixelFormat:dimensions:];
-[EGStillImageScalerNode initWithName:stillImageSettings:nodeConfiguration:resourceCoordinator:deepZoomEnabled:inputImageBufferType:portType:delegate:];
-[EGStillImageScalerNode processorInput];
-[EGStillImageScalerNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageScalerNode sbufInput];
-[EGStillImageScalerNode sbufOutput];
```
