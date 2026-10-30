# `MLE5Engine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLPreparable`, `MLProgramInternal`, `MLModelAssetDescriptionLoader`, `MLStatefulModelEngine`, `MLClassifier`, `MLCompiledModelLoader`
- 10 instance variables, 22 properties, 48 instance methods, 3 class methods

## Instance variables

```
@"MLE5ExecutionStreamPool" _streamPool;
@"<MLE5ExecutionStreamOperationPool>" _operationPool;
@"NSString" _functionName;
@"NSString" _classProbabilitiesFeatureName;
@ _classLabelsSharedKey;
@"MLFeatureProviderConformer" _inputFeatureConformer;
@"MLFeatureProviderConformer" _stateFeatureConformer;
@"NSObject<OS_dispatch_semaphore>" _batchMaxInFlightSem;
@"MLVersionInfo" _compilerVersionInfo;
@"MLE5ProgramLibrary" _programLibrary;
```

## Properties

```
@property (T@"MLE5ExecutionStreamPool",R,V_streamPool) streamPool;
@property (T@"<MLE5ExecutionStreamOperationPool>",R,V_operationPool) operationPool;
@property (T@"NSString",R,C,N,V_functionName) functionName;
@property (T@"NSString",R,V_classProbabilitiesFeatureName) classProbabilitiesFeatureName;
@property (T@,R,V_classLabelsSharedKey) classLabelsSharedKey;
@property (T@"MLFeatureProviderConformer",R,V_inputFeatureConformer) inputFeatureConformer;
@property (T@"MLFeatureProviderConformer",R,V_stateFeatureConformer) stateFeatureConformer;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_batchMaxInFlightSem) batchMaxInFlightSem;
@property (T@"MLVersionInfo",R,N,V_compilerVersionInfo) compilerVersionInfo;
@property (T@"MLE5ProgramLibrary",R,N,V_programLibrary) programLibrary;
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
@property (T@"NSString",R,C,N) serializedMILText;
```

## Class methods

```
+[MLE5Engine containerClass];
+[MLE5Engine loadModelAssetDescriptionFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLE5Engine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLE5Engine predictionTypeForKTrace];
-[MLE5Engine predictionsFromBatch:options:error:];
-[MLE5Engine classLabels];
-[MLE5Engine submitPredictionRequest:completionHandler:];
-[MLE5Engine executionSchedule];
-[MLE5Engine enableInstrumentsTracing];
-[MLE5Engine _predictionFromFeatures:usingState:options:error:];
-[MLE5Engine newStateWithClientBuffers:];
-[MLE5Engine initWithProgramLibrary:modelDescription:configuration:functionName:classProbabilitiesFeatureName:optionalInputDefaultValues:compilerVersionInfo:];
-[MLE5Engine functionName];
-[MLE5Engine _classifierResultFromOutputFeatures:classifyTopK:error:];
-[MLE5Engine _validateStreamReuse:expectation:error:];
-[MLE5Engine newRequestForModel:inputFeatures:options:error:];
-[MLE5Engine streamPool];
-[MLE5Engine newRequestForModel:inputFeatures:usingState:options:error:];
-[MLE5Engine _postProcessingForOutputs:options:error:];
-[MLE5Engine programLibrary];
-[MLE5Engine _conformInputFeatures:error:];
-[MLE5Engine _predictionFromFeatures:options:error:];
-[MLE5Engine _newRequestForModel:inputFeatures:usingState:options:error:];
-[MLE5Engine classProbabilitiesFeatureName];
-[MLE5Engine classLabelsSharedKey];
-[MLE5Engine _probabilityDictionaryWithMultiArray:classifyTopK:];
-[MLE5Engine prepareWithConcurrencyHint:error:];
-[MLE5Engine _extractSupportedComputeUnitFromString:];
-[MLE5Engine _conformState:error:];
-[MLE5Engine _outputFeaturesByAddingClassifierResultTo:classifyTopK:error:];
-[MLE5Engine evaluateFunction:arguments:error:];
-[MLE5Engine _cleanUpAndReconfigureStream:forInputFeatures:error:];
-[MLE5Engine _predictionFromFeatures:stream:options:error:];
-[MLE5Engine _extractSupportFromBackendDict:];
-[MLE5Engine supportsConcurrentSubmissions];
-[MLE5Engine _trimQuotesFromBackendName:];
-[MLE5Engine operationPool];
-[MLE5Engine newContextAndReturnError:];
-[MLE5Engine stateFeatureConformer];
-[MLE5Engine _totalRuntimeInMilliSecondsFromE5AnalyticsDictionary:];
-[MLE5Engine _classProbabilitiesInOutputFeatures:error:];
-[MLE5Engine batchMaxInFlightSem];
-[MLE5Engine _cleanUpStream:];
-[MLE5Engine compilerVersionInfo];
-[MLE5Engine predictionFromFeatures:options:error:];
-[MLE5Engine _predictionFromFeatures:options:completionHandler:];
-[MLE5Engine initWithContainer:configuration:error:];
-[MLE5Engine serializedMILText];
-[MLE5Engine predictionFromFeatures:usingState:options:error:];
-[MLE5Engine classify:options:error:];
-[MLE5Engine inputFeatureConformer];
```
