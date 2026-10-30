# `MLModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModeling`
- 9 instance variables, 19 properties, 60 instance methods, 14 class methods

## Instance variables

```
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _emittedDetailsToInstruments;
{atomic<unsigned long long>="__a_"{__cxx_atomic_impl<unsigned long long, std::__cxx_atomic_base_impl<unsigned long long>>="__a_value"AQ}} _nextPredictionRequestID;
Q _signpostID;
@"NSObject<OS_dispatch_queue>" _asyncPredictionQueue;
@"MLModelMetadata" _metadata;
@"MLFairPlayDecryptSession" _decryptSession;
@"MLPredictionEvent" _predictionEvent;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _configuration;
```

## Properties

```
@property (TQ,N,V_signpostID) signpostID;
@property (T@"MLPredictionEvent",&,N,V_predictionEvent) predictionEvent;
@property (T@"MLModelDescription",&,N,V_modelDescription) modelDescription;
@property (T@"MLModelConfiguration",&,N,V_configuration) configuration;
@property (T@"MLFairPlayDecryptSession",&,N,V_decryptSession) decryptSession;
@property (T@"<MLProgram>",R,N) program;
@property (T@"<MLNeuralNetwork>",R,N) neuralNetwork;
@property (T@"<MLWritable>",R,N) writable;
@property (T@"<MLClassifier>",R,N) classifier;
@property (T@"<MLRegressor>",R,N) regressor;
@property (T@"<MLPipeline>",R,N) pipeline;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (T@"MLModelMetadata",R,V_metadata) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLModel _compileModelAtURL:options:error:];
+[MLModel availableComputeDevices];
+[MLModel compileModelAtURL:completionHandler:];
+[MLModel compileModelAtURL:error:];
+[MLModel compileModelWithoutAutoreleaseAtURL:options:error:];
+[MLModel generateSignpostId];
+[MLModel loadContentsOfURL:configuration:completionHandler:];
+[MLModel loadModelAsset:configuration:completionHandler:];
+[MLModel maxPredictionsInFlight];
+[MLModel modelWithContentsOfURL:configuration:error:];
+[MLModel modelWithContentsOfURL:error:];
+[MLModel predictionsFromLoopingOverBatch:model:options:error:];
+[MLModel predictionsFromSubbatchingBatch:maxSubbatchLength:predictionBlock:options:error:];
+[MLModel serializeInterfaceAndMetadata:toArchive:error:];
```

## Instance methods

```
-[MLModel regressor];
-[MLModel predictionTypeForKTrace];
-[MLModel predictionsFromBatch:options:error:];
-[MLModel classifier];
-[MLModel submitPredictionRequest:completionHandler:];
-[MLModel executionSchedule];
-[MLModel enableInstrumentsTracing];
-[MLModel parameterValueForKey:error:];
-[MLModel newStateWithClientBuffers:];
-[MLModel predictionFromFeatures:error:];
-[MLModel newRequestForModel:inputFeatures:options:error:];
-[MLModel debugQuickLookObject];
-[MLModel predictionFromFeatures:options:completionHandler:];
-[MLModel setConfiguration:];
-[MLModel predictionFromFeatures:usingState:options:completionHandler:];
-[MLModel initWithConfiguration:];
-[MLModel modelPath];
-[MLModel metadata];
-[MLModel predictionsFromBatch:error:];
-[MLModel updatable];
-[MLModel configuration];
-[MLModel program];
-[MLModel cancelPredictionRequest:];
-[MLModel modelDescription];
-[MLModel supportsConcurrentSubmissions];
-[MLModel writable];
-[MLModel prepareWithCompletionHandler:];
-[MLModel pipeline];
-[MLModel description];
-[MLModel setSignpostID:];
-[MLModel newRequestWithInputFeatures:usingState:options:error:];
-[MLModel neuralNetwork];
-[MLModel internalEngine];
-[MLModel predictionFromFeatures:options:error:];
-[MLModel predictionFromFeatures:usingState:options:error:];
-[MLModel newRequestWithInputFeatures:options:error:];
-[MLModel signpostID];
-[MLModel predictionEvent];
-[MLModel decryptSession];
-[MLModel enableInstrumentsTracingIfNeeded];
-[MLModel initDescriptionOnlyWithSpecification:configuration:error:];
-[MLModel initInterfaceAndMetadataWithCompiledArchive:error:];
-[MLModel initWithDescription:];
-[MLModel initWithDescription:configuration:];
-[MLModel initWithName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLModel newState];
-[MLModel newStateForFeatureNamed:initializerBlock:];
-[MLModel nextPredictionRequestID];
-[MLModel objectBoundingBoxOutputDescription];
-[MLModel pipelineOfPostVisionFeaturePrintModelsFromPipeline:];
-[MLModel predictionFromFeatures:completionHandler:];
-[MLModel predictionFromFeatures:usingState:error:];
-[MLModel prepareWithConcurrencyHint:];
-[MLModel recordsPredictionEvent];
-[MLModel setDecryptSession:];
-[MLModel setModelDescription:];
-[MLModel setModelPath:modelName:];
-[MLModel setPredictionEvent:];
-[MLModel vectorizeInput:error:];
-[MLModel visionFeaturePrintInfo];
```
