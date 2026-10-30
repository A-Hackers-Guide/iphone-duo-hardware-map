# `RC_EspressoWrapper`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RCModelWrapper`
- 18 instance variables, 24 properties, 70 instance methods, 7 class methods

## Instance variables

```
B isBuilt;
B _autoResetEnabled;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _path;
@"NSString" _identifier;
@"RC_EspressoProgramWrapper" _program;
^{e5rt_execution_stream=} _executionStream;
^{e5rt_execution_stream_operation=} _operation;
^{e5rt_async_event=} _dependencyE5RTEvent;
^{e5rt_async_event=} _completionE5RTEvent;
@"<MTLSharedEventSPI>" _sharedEvent;
Q _currentSharedEventValue;
@? _surfaceProvider;
@ _processorOutput;
@"NSMutableDictionary" _allocatedPorts;
@"NSArray" _allocatedInputs;
@"NSArray" _allocatedOutputs;
q _inFlightOperationCount;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,&,V_queue) queue;
@property (TB,VisBuilt) isBuilt;
@property (T@"RC_EspressoProgramWrapper",&,N,V_program) program;
@property (T^{e5rt_execution_stream=},V_executionStream) executionStream;
@property (T^{e5rt_execution_stream_operation=},V_operation) operation;
@property (T^{e5rt_async_event=},V_dependencyE5RTEvent) dependencyE5RTEvent;
@property (T^{e5rt_async_event=},V_completionE5RTEvent) completionE5RTEvent;
@property (T@"<MTLSharedEventSPI>",&,N,V_sharedEvent) sharedEvent;
@property (TQ,V_currentSharedEventValue) currentSharedEventValue;
@property (T@?,C,N,V_surfaceProvider) surfaceProvider;
@property (T@,W,N,V_processorOutput) processorOutput;
@property (T@"NSMutableDictionary",&,N,V_allocatedPorts) allocatedPorts;
@property (T@"NSArray",&,N,V_allocatedInputs) allocatedInputs;
@property (T@"NSArray",&,N,V_allocatedOutputs) allocatedOutputs;
@property (Tq,N,V_inFlightOperationCount) inFlightOperationCount;
@property (T@"NSString",R,V_path) path;
@property (T@"NSString",R,V_identifier) identifier;
@property (T@"NSArray",R) inputNames;
@property (T@"NSArray",R) outputNames;
@property (TB,R,V_autoResetEnabled) autoResetEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[RC_EspressoWrapper clearCache];
+[RC_EspressoWrapper cache];
+[RC_EspressoWrapper cachedWrapperForPath:processorOutput:autoReset:preferredDevice:discriminator:];
+[RC_EspressoWrapper cachedWrapperWithPath:];
+[RC_EspressoWrapper maxCachedOperationsPerModel];
+[RC_EspressoWrapper operationCache];
+[RC_EspressoWrapper prewarmForPath:capacity:preferredDevice:];
```

## Instance methods

```
-[RC_EspressoWrapper setOperation:];
-[RC_EspressoWrapper operation];
-[RC_EspressoWrapper initWithPath:];
-[RC_EspressoWrapper executeAsync:];
-[RC_EspressoWrapper sharedEvent];
-[RC_EspressoWrapper identifier];
-[RC_EspressoWrapper dealloc];
-[RC_EspressoWrapper reset];
-[RC_EspressoWrapper queue];
-[RC_EspressoWrapper setSharedEvent:];
-[RC_EspressoWrapper execute];
-[RC_EspressoWrapper program];
-[RC_EspressoWrapper isSetup];
-[RC_EspressoWrapper CIImageProcessorDigestObject];
-[RC_EspressoWrapper outputNames];
-[RC_EspressoWrapper setProgram:];
-[RC_EspressoWrapper path];
-[RC_EspressoWrapper inputNames];
-[RC_EspressoWrapper isBuilt];
-[RC_EspressoWrapper surfaceProvider];
-[RC_EspressoWrapper _bindInternalV1:isInput:buffer:];
-[RC_EspressoWrapper allocatedInputs];
-[RC_EspressoWrapper executionStream];
-[RC_EspressoWrapper processorOutput];
-[RC_EspressoWrapper unbind:isInput:];
-[RC_EspressoWrapper _bindInternalSurface:isInput:surface:];
-[RC_EspressoWrapper _hasBinding:];
-[RC_EspressoWrapper _setupSharedEventsWithEvent:];
-[RC_EspressoWrapper _surfaceForPort:dimensions:isInput:provider:];
-[RC_EspressoWrapper allocatedOutputs];
-[RC_EspressoWrapper allocatedPorts];
-[RC_EspressoWrapper autoResetEnabled];
-[RC_EspressoWrapper bindInput:buffer:];
-[RC_EspressoWrapper bindOutput:buffer:];
-[RC_EspressoWrapper buildAndWait];
-[RC_EspressoWrapper buildAsync];
-[RC_EspressoWrapper completionE5RTEvent];
-[RC_EspressoWrapper currentSharedEventValue];
-[RC_EspressoWrapper decrementInFlightCountAndAutoReset];
-[RC_EspressoWrapper dependencyE5RTEvent];
-[RC_EspressoWrapper executeAsyncWithCommandBuffer:preInferenceEncoder:postInferenceEncoder:callback:];
-[RC_EspressoWrapper hasInputBinding:];
-[RC_EspressoWrapper hasOutputBinding:];
-[RC_EspressoWrapper inFlightOperationCount];
-[RC_EspressoWrapper incrementInFlightCount];
-[RC_EspressoWrapper initWithPath:preferredDevice:forE5Prewarming:];
-[RC_EspressoWrapper initWithPath:sharedEvent:autoReset:preferredDevice:];
-[RC_EspressoWrapper initWithPath:surfaceProvider:sharedEvent:autoReset:preferredDevice:];
-[RC_EspressoWrapper inputPortDimensionsFor:];
-[RC_EspressoWrapper inputSurfaces];
-[RC_EspressoWrapper lastSignaledValue];
-[RC_EspressoWrapper outputPortDimensionsFor:];
-[RC_EspressoWrapper outputSurfaces];
-[RC_EspressoWrapper setAllocatedInputs:];
-[RC_EspressoWrapper setAllocatedOutputs:];
-[RC_EspressoWrapper setAllocatedPorts:];
-[RC_EspressoWrapper setCompletionE5RTEvent:];
-[RC_EspressoWrapper setCurrentSharedEventValue:];
-[RC_EspressoWrapper setDependencyE5RTEvent:];
-[RC_EspressoWrapper setExecutionStream:];
-[RC_EspressoWrapper setInFlightOperationCount:];
-[RC_EspressoWrapper setIsBuilt:];
-[RC_EspressoWrapper setProcessorOutput:];
-[RC_EspressoWrapper setSurfaceProvider:];
-[RC_EspressoWrapper setupWithInputSurfaces:outputSurfaces:sharedEvent:];
-[RC_EspressoWrapper setupWithSurfaceProvider:sharedEvent:autoReset:];
-[RC_EspressoWrapper unbindAllPorts];
-[RC_EspressoWrapper unbindPort:];
-[RC_EspressoWrapper initWithPath:surfaceProvider:sharedEvent:autoReset:];
-[RC_EspressoWrapper recommendedPixelFormatForPort:];
```
