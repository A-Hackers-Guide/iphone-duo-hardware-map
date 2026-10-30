# `MLE5ExecutionStreamOperation`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 20 properties, 61 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<e5rt_async_event, MLE5ObjectDeleter<e5rt_async_event>>=""{?="__ptr_"^{e5rt_async_event}}} _cachedWaitEvent;
@"MLPixelBufferPool" _pixelBufferPool;
^{e5rt_execution_stream_operation=} _operationHandle;
@"NSString" _debugLabel;
@"NSError" _asyncSubmissionError;
@"NSString" _functionName;
@"NSString" _shapeHash;
@"MLE5ProgramLibrary" _programLibrary;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _modelConfiguration;
@"NSArray" _inputPorts;
@"NSArray" _statePorts;
@"NSArray" _outputPorts;
q _state;
@"IOSurfaceSharedEventListener" _waitEventListener;
Q _modelSignpostId;
@"NSArray" _waitSharedEventsBoundToESOP;
@"<MTLSharedEvent>" _completionSharedEventBoundToESOP;
```

## Properties

```
@property (T@"MLE5ProgramLibrary",R,N,V_programLibrary) programLibrary;
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (T@"MLModelConfiguration",R,N,V_modelConfiguration) modelConfiguration;
@property (T^{e5rt_execution_stream_operation=},N,V_operationHandle) operationHandle;
@property (T@"NSArray",C,N,V_inputPorts) inputPorts;
@property (T@"NSArray",C,N,V_statePorts) statePorts;
@property (T@"NSArray",C,N,V_outputPorts) outputPorts;
@property (Tq,N,V_state) state;
@property (T@"IOSurfaceSharedEventListener",R,N,V_waitEventListener) waitEventListener;
@property (TQ,R,N,V_modelSignpostId) modelSignpostId;
@property (T@"NSArray",C,N,V_waitSharedEventsBoundToESOP) waitSharedEventsBoundToESOP;
@property (T@"<MTLSharedEvent>",&,N,V_completionSharedEventBoundToESOP) completionSharedEventBoundToESOP;
@property (T@"MLPixelBufferPool",&,N,V_pixelBufferPool) pixelBufferPool;
@property (T@"<MLFeatureProvider>",R,N) outputFeatures;
@property (T@"NSString",R,C,N,V_debugLabel) debugLabel;
@property (T@"NSError",&,N,V_asyncSubmissionError) asyncSubmissionError;
@property (T@"NSString",R,C,V_functionName) functionName;
@property (T@"NSString",C,V_shapeHash) shapeHash;
@property (T@"NSArray",R,C,N) directlyBoundInputFeatureNames;
@property (T@"NSArray",R,C,N) directlyBoundOutputFeatureNames;
```

## Instance methods

```
-[MLE5ExecutionStreamOperation debugLabel];
-[MLE5ExecutionStreamOperation setPixelBufferPool:];
-[MLE5ExecutionStreamOperation waitEventListener];
-[MLE5ExecutionStreamOperation functionName];
-[MLE5ExecutionStreamOperation setState:];
-[MLE5ExecutionStreamOperation _directlyBoundFeatureNamesForPorts:];
-[MLE5ExecutionStreamOperation _copyInputFeatures:error:];
-[MLE5ExecutionStreamOperation pixelBufferPool];
-[MLE5ExecutionStreamOperation _inputPortNames];
-[MLE5ExecutionStreamOperation prepareForInputFeatures:options:error:];
-[MLE5ExecutionStreamOperation prepareAsyncSubmissionForInputFeatures:options:error:];
-[MLE5ExecutionStreamOperation _newArrayOfOutputPorts:featureDescriptionsByName:error:];
-[MLE5ExecutionStreamOperation preloadAndReturnError:];
-[MLE5ExecutionStreamOperation outputFeatures];
-[MLE5ExecutionStreamOperation modelSignpostId];
-[MLE5ExecutionStreamOperation setInputPorts:];
-[MLE5ExecutionStreamOperation dealloc];
-[MLE5ExecutionStreamOperation _newArrayOfInoutPorts:featureDescriptionsByName:error:];
-[MLE5ExecutionStreamOperation _updateCompletionEventFutureValuesWithCompletionSyncPoint:];
-[MLE5ExecutionStreamOperation programLibrary];
-[MLE5ExecutionStreamOperation setOperationHandle:];
-[MLE5ExecutionStreamOperation _createOperationWithRetryCount:error:];
-[MLE5ExecutionStreamOperation reset];
-[MLE5ExecutionStreamOperation setOutputPorts:];
-[MLE5ExecutionStreamOperation _bindNewWaitEventsDirectlyWithWaitSyncPoints:];
-[MLE5ExecutionStreamOperation _bindOutputPortsWithOptions:error:];
-[MLE5ExecutionStreamOperation _inoutPortNames];
-[MLE5ExecutionStreamOperation _bindWaitEventsDirectly:];
-[MLE5ExecutionStreamOperation setStatePorts:];
-[MLE5ExecutionStreamOperation operationHandle];
-[MLE5ExecutionStreamOperation asyncSubmissionError];
-[MLE5ExecutionStreamOperation setShapeHash:];
-[MLE5ExecutionStreamOperation modelConfiguration];
-[MLE5ExecutionStreamOperation setCompletionSharedEventBoundToESOP:];
-[MLE5ExecutionStreamOperation _reusableForWaitSyncPoints:allInputsUseDirectBinding:];
-[MLE5ExecutionStreamOperation setAsyncSubmissionError:];
-[MLE5ExecutionStreamOperation outputPorts];
-[MLE5ExecutionStreamOperation statePorts];
-[MLE5ExecutionStreamOperation _prepareInputPortsForFeatures:error:];
-[MLE5ExecutionStreamOperation modelDescription];
-[MLE5ExecutionStreamOperation _reusableForCompletionSyncPoint:allOutputBackingsUseDirectBinding:];
-[MLE5ExecutionStreamOperation reusableForInputFeatures:options:];
-[MLE5ExecutionStreamOperation completionSharedEventBoundToESOP];
-[MLE5ExecutionStreamOperation shapeHash];
-[MLE5ExecutionStreamOperation directlyBoundOutputFeatureNames];
-[MLE5ExecutionStreamOperation waitSharedEventsBoundToESOP];
-[MLE5ExecutionStreamOperation directlyBoundInputFeatureNames];
-[MLE5ExecutionStreamOperation initWithProgramLibrary:functionName:modelDescription:configuration:debugLabel:modelSignpostId:];
-[MLE5ExecutionStreamOperation _bindCompletionSyncPointDirectlyIfPossible:];
-[MLE5ExecutionStreamOperation _updateWaitEventFutureValuesWithWaitSyncPoints:];
-[MLE5ExecutionStreamOperation _createOperationAndReturnError:];
-[MLE5ExecutionStreamOperation _bindNewCompletionEventsDirectlyWithCompletionSyncPoint:];
-[MLE5ExecutionStreamOperation setWaitSharedEventsBoundToESOP:];
-[MLE5ExecutionStreamOperation _multiArrayFeatureFromStateFeature:];
-[MLE5ExecutionStreamOperation serializeInferenceFrameDataForOptions:error:];
-[MLE5ExecutionStreamOperation _bindEventToWaitForCopyingInputFeatures:afterSyncPoints:];
-[MLE5ExecutionStreamOperation inputPorts];
-[MLE5ExecutionStreamOperation state];
-[MLE5ExecutionStreamOperation _bindInputFeaturesAndWaitEvents:options:error:];
-[MLE5ExecutionStreamOperation _outputPortNames];
-[MLE5ExecutionStreamOperation _newArrayOfInputPorts:featureDescriptionsByName:error:];
```
