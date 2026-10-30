# `_ANERequest`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 20 instance methods, 6 class methods

## Instance variables

```
@"NSArray" _inputArray;
@"NSArray" _inputIndexArray;
@"NSArray" _outputArray;
@"NSArray" _outputIndexArray;
@"_ANEIOSurfaceObject" _weightsBuffer;
@"_ANESharedEvents" _sharedEvents;
@"NSNumber" _transactionHandle;
@"NSNumber" _procedureIndex;
@"_ANEPerformanceStats" _perfStats;
@"NSArray" _perfStatsArray;
@? _completionHandler;
```

## Properties

```
@property (T@"_ANEPerformanceStats",&,N,V_perfStats) perfStats;
@property (T@"NSNumber",C,N,V_transactionHandle) transactionHandle;
@property (T@"NSArray",R,N,V_inputArray) inputArray;
@property (T@"NSArray",R,N,V_inputIndexArray) inputIndexArray;
@property (T@"NSArray",R,N,V_outputArray) outputArray;
@property (T@"NSArray",R,N,V_outputIndexArray) outputIndexArray;
@property (T@"_ANEIOSurfaceObject",R,N,V_weightsBuffer) weightsBuffer;
@property (T@"_ANESharedEvents",&,N,V_sharedEvents) sharedEvents;
@property (T@"NSNumber",R,C,N,V_procedureIndex) procedureIndex;
@property (T@"NSArray",R,N,V_perfStatsArray) perfStatsArray;
@property (T@?,C,V_completionHandler) completionHandler;
```

## Class methods

```
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:perfStats:procedureIndex:];
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:procedureIndex:];
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:];
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:];
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:transactionHandle:];
+[_ANERequest requestWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:procedureIndex:];
```

## Instance methods

```
-[_ANERequest validate];
-[_ANERequest inputArray];
-[_ANERequest perfStatsArray];
-[_ANERequest setCompletionHandler:];
-[_ANERequest completionHandler];
-[_ANERequest setSharedEvents:];
-[_ANERequest outputIndexArray];
-[_ANERequest ioSurfacesCount];
-[_ANERequest transactionHandle];
-[_ANERequest perfStats];
-[_ANERequest setPerfStats:];
-[_ANERequest initWithVirtualModel:];
-[_ANERequest description];
-[_ANERequest sharedEvents];
-[_ANERequest setTransactionHandle:];
-[_ANERequest outputArray];
-[_ANERequest initWithInputs:inputIndices:outputs:outputIndices:weightsBuffer:perfStats:procedureIndex:sharedEvents:transactionHandle:];
-[_ANERequest procedureIndex];
-[_ANERequest weightsBuffer];
-[_ANERequest inputIndexArray];
```
