# `MLNeuralNetworkUpdateEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLNeuralNetworkV1Engine`
- Protocols: `MLUpdatable`
- 11 instance variables, 22 properties, 49 instance methods, 3 class methods

## Instance variables

```
B _continueWithUpdate;
@"ETTaskState" _snapshot;
@"ETTaskDefinition" _task;
@"NSString" _lossTargetName;
@"NSDictionary" _classLabelToIndexMap;
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _progressHandlersDispatchQueue;
@"NSDictionary" _coreMLToEspressoParamsMap;
@"NSString" _lossOutputName;
@"MLShufflingBatchProvider" _shuffableTrainingData;
@"MLParameterContainer" _parameterContainer;
```

## Properties

```
@property (T@"MLUpdateProgressHandlers",&,N,V_progressHandlers) progressHandlers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_progressHandlersDispatchQueue) progressHandlersDispatchQueue;
@property (T@"NSDictionary",&,N,V_coreMLToEspressoParamsMap) coreMLToEspressoParamsMap;
@property (T@"NSString",&,N,V_lossOutputName) lossOutputName;
@property (T@"NSString",&,N,V_lossTargetName) lossTargetName;
@property (TB,N,V_continueWithUpdate) continueWithUpdate;
@property (T@"MLShufflingBatchProvider",&,N,V_shuffableTrainingData) shuffableTrainingData;
@property (T@"MLParameterContainer",&,N,V_parameterContainer) parameterContainer;
@property (T@"ETTaskState",&,N,V_snapshot) snapshot;
@property (T@"ETTaskDefinition",&,N,V_task) task;
@property (T@"NSDictionary",R,N,V_classLabelToIndexMap) classLabelToIndexMap;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLNeuralNetworkUpdateEngine supportsSecureCoding];
+[MLNeuralNetworkUpdateEngine createCoreMLToEspressoParamsMap];
+[MLNeuralNetworkUpdateEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLNeuralNetworkUpdateEngine updateModelWithData:];
-[MLNeuralNetworkUpdateEngine predictionTypeForKTrace];
-[MLNeuralNetworkUpdateEngine predictionsFromBatch:options:error:];
-[MLNeuralNetworkUpdateEngine cancelUpdate];
-[MLNeuralNetworkUpdateEngine resumeUpdateWithParameters:];
-[MLNeuralNetworkUpdateEngine setUpdateProgressHandlers:dispatchQueue:];
-[MLNeuralNetworkUpdateEngine resumeUpdate];
-[MLNeuralNetworkUpdateEngine writeToURL:error:];
-[MLNeuralNetworkUpdateEngine parameterValueForKey:error:];
-[MLNeuralNetworkUpdateEngine setSnapshot:];
-[MLNeuralNetworkUpdateEngine updateParameters];
-[MLNeuralNetworkUpdateEngine predictionFromFeatures:error:];
-[MLNeuralNetworkUpdateEngine parameterContainer];
-[MLNeuralNetworkUpdateEngine initWithCompiledArchive:nnContainer:configuration:error:];
-[MLNeuralNetworkUpdateEngine setProgressHandlers:];
-[MLNeuralNetworkUpdateEngine snapshot];
-[MLNeuralNetworkUpdateEngine progressHandlersDispatchQueue];
-[MLNeuralNetworkUpdateEngine setShuffableTrainingData:];
-[MLNeuralNetworkUpdateEngine continueWithUpdate];
-[MLNeuralNetworkUpdateEngine updateLearningRateWithTaskContext:isInCallBack:error:];
-[MLNeuralNetworkUpdateEngine shuffableTrainingData];
-[MLNeuralNetworkUpdateEngine createEspressoTaskFrom:updateParameters:lossInputName:lossTargetName:lossOutputName:updatableLayerNames:configuration:error:];
-[MLNeuralNetworkUpdateEngine setProgressHandlersDispatchQueue:];
-[MLNeuralNetworkUpdateEngine collectMetricsFromTaskContext:isInCallBack:];
-[MLNeuralNetworkUpdateEngine setLossTargetName:];
-[MLNeuralNetworkUpdateEngine setTask:];
-[MLNeuralNetworkUpdateEngine predictionsFromBatch:error:];
-[MLNeuralNetworkUpdateEngine setParameterContainer:];
-[MLNeuralNetworkUpdateEngine setLossOutputName:];
-[MLNeuralNetworkUpdateEngine loadLossTargetName:lossOutputName:fromUpdateParameters:];
-[MLNeuralNetworkUpdateEngine classLabelToIndexMap];
-[MLNeuralNetworkUpdateEngine lossTargetName];
-[MLNeuralNetworkUpdateEngine weightsForLayer:error:];
-[MLNeuralNetworkUpdateEngine parameterValueForKey:];
-[MLNeuralNetworkUpdateEngine encodeWithCoder:];
-[MLNeuralNetworkUpdateEngine setWeightsOrBiasesForLayer:layerType:value:error:];
-[MLNeuralNetworkUpdateEngine setContinueWithUpdate:];
-[MLNeuralNetworkUpdateEngine paramsForLayer:parameterType:error:];
-[MLNeuralNetworkUpdateEngine initWithCoder:];
-[MLNeuralNetworkUpdateEngine task];
-[MLNeuralNetworkUpdateEngine progressHandlers];
-[MLNeuralNetworkUpdateEngine coreMLToEspressoParamsMap];
-[MLNeuralNetworkUpdateEngine predictionFromFeatures:options:error:];
-[MLNeuralNetworkUpdateEngine updateWeightsAndBiasesFromConfigParams:error:];
-[MLNeuralNetworkUpdateEngine stringForDataType:];
-[MLNeuralNetworkUpdateEngine biasForLayer:error:];
-[MLNeuralNetworkUpdateEngine lossOutputName];
-[MLNeuralNetworkUpdateEngine loadLossInputName:updatableLayerNames:fromCompiledArchive:];
-[MLNeuralNetworkUpdateEngine setCoreMLToEspressoParamsMap:];
```
