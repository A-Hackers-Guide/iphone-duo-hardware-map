# `BWStillImageProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
i _stillImageProcessingMode;
@"NSString" _pipelineProcessingContext;
@"NSDictionary" _sensorConfigurationsByPortType;
B _deferredCaptureSupportEnabled;
@"<MTLCommandQueue>" _metalCommandQueue;
@"BWInferenceScheduler" _inferenceScheduler;
I _figThreadPriority;
B _postponeProcessorSetup;
B _deferredPhotoProcessorEnabled;
```

## Properties

```
@property (Ti,N,V_stillImageProcessingMode) stillImageProcessingMode;
@property (T@"NSString",&,N,V_pipelineProcessingContext) pipelineProcessingContext;
@property (T@"NSDictionary",&,N,V_sensorConfigurationsByPortType) sensorConfigurationsByPortType;
@property (TB,N,V_deferredCaptureSupportEnabled) deferredCaptureSupportEnabled;
@property (TB,N,V_deferredPhotoProcessorEnabled) deferredPhotoProcessorEnabled;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (T@"BWInferenceScheduler",&,N,V_inferenceScheduler) inferenceScheduler;
@property (TI,N,V_figThreadPriority) figThreadPriority;
@property (TB,R,N) postponedProcessorSetupSupported;
@property (TB,N) postponeProcessorSetup;
```

## Instance methods

```
-[BWStillImageProcessorControllerConfiguration setMetalCommandQueue:];
-[BWStillImageProcessorControllerConfiguration pipelineProcessingContext];
-[BWStillImageProcessorControllerConfiguration setDeferredCaptureSupportEnabled:];
-[BWStillImageProcessorControllerConfiguration inferenceScheduler];
-[BWStillImageProcessorControllerConfiguration metalCommandQueue];
-[BWStillImageProcessorControllerConfiguration setPipelineProcessingContext:];
-[BWStillImageProcessorControllerConfiguration setFigThreadPriority:];
-[BWStillImageProcessorControllerConfiguration stillImageProcessingMode];
-[BWStillImageProcessorControllerConfiguration deferredCaptureSupportEnabled];
-[BWStillImageProcessorControllerConfiguration deferredPhotoProcessorEnabled];
-[BWStillImageProcessorControllerConfiguration sensorConfigurationsByPortType];
-[BWStillImageProcessorControllerConfiguration setDeferredPhotoProcessorEnabled:];
-[BWStillImageProcessorControllerConfiguration dealloc];
-[BWStillImageProcessorControllerConfiguration setStillImageProcessingMode:];
-[BWStillImageProcessorControllerConfiguration setSensorConfigurationsByPortType:];
-[BWStillImageProcessorControllerConfiguration setInferenceScheduler:];
-[BWStillImageProcessorControllerConfiguration figThreadPriority];
-[BWStillImageProcessorControllerConfiguration postponeProcessorSetup];
-[BWStillImageProcessorControllerConfiguration postponedProcessorSetupSupported];
-[BWStillImageProcessorControllerConfiguration setPostponeProcessorSetup:];
```
