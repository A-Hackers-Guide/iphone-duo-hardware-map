# `BWNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 20 instance variables, 21 properties, 63 instance methods, 1 class methods

## Instance variables

```
@"BWNodeInput" _input;
@"BWNodeOutput" _output;
@"NSMutableArray" _inputs;
@"NSMutableArray" _outputs;
@"NSString" _name;
@"NSString" _subgraphName;
B _supportsConcurrentLiveInputCallbacks;
B _supportsLiveReconfiguration;
B _singleInput;
B _singleOutput;
@"BWGraph" _graph;
i _deferredPreparePriority;
@"<BWNodeRenderDelegate>" _renderDelegate;
q _requestedConfigurationID;
q _preparedConfigurationID;
q _liveConfigurationID;
@"NSObject<OS_dispatch_group>" _currentConfigurationGroup;
B _preparingCancellableNode;
B _supportsPrepareWhileRunning;
B _requiresEndOfDataForConfigurationChanges;
```

## Properties

```
@property (TB,N,V_supportsConcurrentLiveInputCallbacks) supportsConcurrentLiveInputCallbacks;
@property (TB,N,V_supportsLiveReconfiguration) supportsLiveReconfiguration;
@property (TB,N,V_supportsPrepareWhileRunning) supportsPrepareWhileRunning;
@property (TB,N,V_requiresEndOfDataForConfigurationChanges) requiresEndOfDataForConfigurationChanges;
@property (T@"NSString",C,N) name;
@property (T@"NSString",C,N,V_subgraphName) subgraphName;
@property (T@"NSString",R,N) briefName;
@property (T@"NSString",R) nodeType;
@property (T@"NSString",R) nodeSubType;
@property (T@"NSArray",R) inputs;
@property (T@"NSArray",R) outputs;
@property (T@"BWNodeInput",R) input;
@property (T@"BWNodeOutput",R) output;
@property (T@"<BWNodeRenderDelegate>",N,V_renderDelegate) renderDelegate;
@property (TB,R,N) hasNonLiveConfigurationChanges;
@property (T@"BWGraph",N,V_graph) graph;
@property (Ti,N,V_deferredPreparePriority) deferredPreparePriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWNode initialize];
```

## Instance methods

```
-[BWNode outputs];
-[BWNode graph];
-[BWNode prepareForCurrentConfigurationToBecomeLive];
-[BWNode removeOutput:];
-[BWNode osStatePropertyList];
-[BWNode liveConfigurationID];
-[BWNode setRequestedConfigurationID:];
-[BWNode suspendResources];
-[BWNode renderSampleBuffer:forInput:];
-[BWNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWNode input];
-[BWNode makeCurrentConfigurationLive];
-[BWNode allInputsHaveReachedState:];
-[BWNode setRenderDelegate:];
-[BWNode init];
-[BWNode inputs];
-[BWNode supportsLiveReconfiguration];
-[BWNode dealloc];
-[BWNode setGraph:];
-[BWNode hasNonLiveConfigurationChanges];
-[BWNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWNode renderDelegate];
-[BWNode briefName];
-[BWNode didSelectFormat:forOutput:];
-[BWNode handleDroppedSample:forInput:];
-[BWNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWNode didReachEndOfDataForConfigurationID:input:];
-[BWNode description];
-[BWNode setName:];
-[BWNode preparedConfigurationID];
-[BWNode addOutput:];
-[BWNode output];
-[BWNode nodeSubType];
-[BWNode _handleMessage:fromInput:];
-[BWNode messageDispatchQueueForOutput:];
-[BWNode didSelectFormat:forInput:];
-[BWNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWNode requestedConfigurationID];
-[BWNode name];
-[BWNode handleNodeError:forInput:];
-[BWNode nodeType];
-[BWNode addInput:];
-[BWNode removeInput:];
-[BWNode setSupportsPrepareWhileRunning:];
-[BWNode osStatePropertyListWithVerbose:];
-[BWNode setSupportsLiveReconfiguration:];
-[BWNode currentConfigurationGroup];
-[BWNode deferredPreparePriority];
-[BWNode didReachEndOfDataForInput:];
-[BWNode didSelectFormat:forOutput:forAttachedMediaKey:];
-[BWNode input:hasReachedState:];
-[BWNode notifyWhenEndOfConfigurationIsHandledUsingQueue:block:];
-[BWNode prepareCancelled];
-[BWNode prepareForCurrentConfigurationToBecomeLiveCancellable];
-[BWNode requiresEndOfDataForConfigurationChanges];
-[BWNode setDeferredPreparePriority:];
-[BWNode setRequiresEndOfDataForConfigurationChanges:];
-[BWNode setSubgraphName:];
-[BWNode setSupportsConcurrentLiveInputCallbacks:];
-[BWNode subgraphName];
-[BWNode supportsConcurrentLiveInputCallbacks];
-[BWNode supportsPrepareWhileRunning];
-[BWNode waitUntilEndOfConfigurationHandled];
```
