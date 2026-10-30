# `MLNeuralNetworkMLComputeUpdateEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLNeuralNetworkV1Engine`
- Protocols: `MLUpdatable`
- 11 instance variables, 22 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _classifierOutputIsSigmoidOutput;
B _continueWithUpdate;
f _finalLossValue;
@"NSDictionary" _classLabelToIndexMap;
@"NSString" _lossTargetName;
@"MLShufflingBatchProvider" _shuffableTrainingData;
@"MLParameterContainer" _parameterContainer;
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _progressHandlersDispatchQueue;
Q _batchSize;
@"MLNeuralNetworkMLComputeGraph" _mlcGraph;
```

## Properties

```
@property (TB,N,V_continueWithUpdate) continueWithUpdate;
@property (T@"MLShufflingBatchProvider",&,N,V_shuffableTrainingData) shuffableTrainingData;
@property (T@"MLParameterContainer",&,N,V_parameterContainer) parameterContainer;
@property (T@"MLUpdateProgressHandlers",&,N,V_progressHandlers) progressHandlers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_progressHandlersDispatchQueue) progressHandlersDispatchQueue;
@property (TQ,N,V_batchSize) batchSize;
@property (Tf,N,V_finalLossValue) finalLossValue;
@property (T@"MLNeuralNetworkMLComputeGraph",&,N,V_mlcGraph) mlcGraph;
@property (T@"NSDictionary",R,N,V_classLabelToIndexMap) classLabelToIndexMap;
@property (TB,N,V_classifierOutputIsSigmoidOutput) classifierOutputIsSigmoidOutput;
@property (T@"NSString",R,N,V_lossTargetName) lossTargetName;
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
+[MLNeuralNetworkMLComputeUpdateEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLNeuralNetworkMLComputeUpdateEngine updateModelWithData:];
-[MLNeuralNetworkMLComputeUpdateEngine batchSize];
-[MLNeuralNetworkMLComputeUpdateEngine predictionTypeForKTrace];
-[MLNeuralNetworkMLComputeUpdateEngine predictionsFromBatch:options:error:];
-[MLNeuralNetworkMLComputeUpdateEngine cancelUpdate];
-[MLNeuralNetworkMLComputeUpdateEngine resumeUpdateWithParameters:];
-[MLNeuralNetworkMLComputeUpdateEngine setBatchSize:];
-[MLNeuralNetworkMLComputeUpdateEngine setUpdateProgressHandlers:dispatchQueue:];
-[MLNeuralNetworkMLComputeUpdateEngine resumeUpdate];
-[MLNeuralNetworkMLComputeUpdateEngine writeToURL:error:];
-[MLNeuralNetworkMLComputeUpdateEngine parameterValueForKey:error:];
-[MLNeuralNetworkMLComputeUpdateEngine setFinalLossValue:];
-[MLNeuralNetworkMLComputeUpdateEngine performTrainingWith:callBacks:numberOfEpochs:error:];
-[MLNeuralNetworkMLComputeUpdateEngine updateParameters];
-[MLNeuralNetworkMLComputeUpdateEngine parameterContainer];
-[MLNeuralNetworkMLComputeUpdateEngine initWithCompiledArchive:nnContainer:configuration:error:];
-[MLNeuralNetworkMLComputeUpdateEngine setProgressHandlers:];
-[MLNeuralNetworkMLComputeUpdateEngine setMlcGraph:];
-[MLNeuralNetworkMLComputeUpdateEngine progressHandlersDispatchQueue];
-[MLNeuralNetworkMLComputeUpdateEngine finalLossValue];
-[MLNeuralNetworkMLComputeUpdateEngine performInferenceWith:outputNameToLayerMap:error:];
-[MLNeuralNetworkMLComputeUpdateEngine setShuffableTrainingData:];
-[MLNeuralNetworkMLComputeUpdateEngine continueWithUpdate];
-[MLNeuralNetworkMLComputeUpdateEngine shuffableTrainingData];
-[MLNeuralNetworkMLComputeUpdateEngine setProgressHandlersDispatchQueue:];
-[MLNeuralNetworkMLComputeUpdateEngine setParameterContainer:];
-[MLNeuralNetworkMLComputeUpdateEngine classLabelToIndexMap];
-[MLNeuralNetworkMLComputeUpdateEngine lossTargetName];
-[MLNeuralNetworkMLComputeUpdateEngine loadLossTargetName:];
-[MLNeuralNetworkMLComputeUpdateEngine parameterValueForKey:];
-[MLNeuralNetworkMLComputeUpdateEngine setContinueWithUpdate:];
-[MLNeuralNetworkMLComputeUpdateEngine setClassifierOutputIsSigmoidOutput:];
-[MLNeuralNetworkMLComputeUpdateEngine mlcGraph];
-[MLNeuralNetworkMLComputeUpdateEngine progressHandlers];
-[MLNeuralNetworkMLComputeUpdateEngine updateLearningRateWithValue:];
-[MLNeuralNetworkMLComputeUpdateEngine classifierOutputIsSigmoidOutput];
```
