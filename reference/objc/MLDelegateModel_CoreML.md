# `MLDelegateModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- 9 instance variables, 3 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _asyncPredictionQueue;
@"<MLModeling>" _internalEngine;
@"<MLStatefulModelEngine>" _statefulModelEngine;
@"MLOutputBackingsVerifier" _outputBackingsVerifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _asyncPredictionSchedulingLock;
Q _currentAsyncPredictionsInFlight;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _prepared;
Q _maxAsyncPredictionsInFlight;
@"NSMutableArray" _pendingPredictionQueue;
```

## Properties

```
@property (TQ,R,N,V_maxAsyncPredictionsInFlight) maxAsyncPredictionsInFlight;
@property (T@"NSMutableArray",R,N,V_pendingPredictionQueue) pendingPredictionQueue;
@property (Ti,R,N) engine;
```

## Instance methods

```
-[MLDelegateModel regressor];
-[MLDelegateModel predictionTypeForKTrace];
-[MLDelegateModel predictionsFromBatch:options:error:];
-[MLDelegateModel classifier];
-[MLDelegateModel submitPredictionRequest:completionHandler:];
-[MLDelegateModel executionSchedule];
-[MLDelegateModel enableInstrumentsTracing];
-[MLDelegateModel parameterValueForKey:error:];
-[MLDelegateModel _predictionFromFeatures:usingState:options:error:];
-[MLDelegateModel newStateWithClientBuffers:];
-[MLDelegateModel engine];
-[MLDelegateModel _predictionsFromBatch:options:error:];
-[MLDelegateModel _validateStateFeatureNamed:backingMultiArray:];
-[MLDelegateModel predictionFromFeatures:options:completionHandler:];
-[MLDelegateModel _finishPredictionAndDispatchPendingPredictions];
-[MLDelegateModel predictionFromFeatures:usingState:options:completionHandler:];
-[MLDelegateModel _schedulePredictionRequest:completionHandler:];
-[MLDelegateModel updatable];
-[MLDelegateModel program];
-[MLDelegateModel _predictionFromFeatures:usingState:options:completionHandler:];
-[MLDelegateModel cancelPredictionRequest:];
-[MLDelegateModel writable];
-[MLDelegateModel prepareWithCompletionHandler:];
-[MLDelegateModel pipeline];
-[MLDelegateModel _submitPredictionRequest:completionHandler:];
-[MLDelegateModel newRequestWithInputFeatures:usingState:options:error:];
-[MLDelegateModel neuralNetwork];
-[MLDelegateModel pendingPredictionQueue];
-[MLDelegateModel internalEngine];
-[MLDelegateModel predictionFromFeatures:options:error:];
-[MLDelegateModel initWithEngine:error:];
-[MLDelegateModel predictionFromFeatures:usingState:options:error:];
-[MLDelegateModel maxAsyncPredictionsInFlight];
-[MLDelegateModel newRequestWithInputFeatures:options:error:];
-[MLDelegateModel signpostID];
```
