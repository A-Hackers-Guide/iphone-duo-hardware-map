# `MLTreeEnsembleXGBoostClassifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLClassifier`
- 5 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _labelsForDataPoints;
@"NSURL" _modelURL;
@"NSString" _objective;
Q _numClasses;
^v _booster;
```

## Properties

```
@property (T@"NSArray",&,N,V_labelsForDataPoints) labelsForDataPoints;
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (T@"NSString",&,N,V_objective) objective;
@property (TQ,N,V_numClasses) numClasses;
@property (T^v,N,V_booster) booster;
```

## Instance methods

```
-[MLTreeEnsembleXGBoostClassifier predictionsFromBatch:options:error:];
-[MLTreeEnsembleXGBoostClassifier predictionFromFeatures:error:];
-[MLTreeEnsembleXGBoostClassifier dealloc];
-[MLTreeEnsembleXGBoostClassifier predictionsFromBatch:error:];
-[MLTreeEnsembleXGBoostClassifier modelURL];
-[MLTreeEnsembleXGBoostClassifier predictionFromFeatures:options:error:];
-[MLTreeEnsembleXGBoostClassifier setModelURL:];
-[MLTreeEnsembleXGBoostClassifier booster];
-[MLTreeEnsembleXGBoostClassifier batchProviderFromXGboostResults:length:error:];
-[MLTreeEnsembleXGBoostClassifier featureProviderArrayFromXGBoostResult:length:error:];
-[MLTreeEnsembleXGBoostClassifier featureProviderFromXGboostResults:length:error:];
-[MLTreeEnsembleXGBoostClassifier initWithDescription:configuration:indexToStringLabelArray:indexToIntLabelArray:modelURL:error:];
-[MLTreeEnsembleXGBoostClassifier initializeAndvalidateObjectiveAndNumClassesWithConfiguration:error:];
-[MLTreeEnsembleXGBoostClassifier initializeBoosterIfOneExists];
-[MLTreeEnsembleXGBoostClassifier labelsForDataPoints];
-[MLTreeEnsembleXGBoostClassifier loadLabelsWithStringLabels:intLabels:];
-[MLTreeEnsembleXGBoostClassifier numClasses];
-[MLTreeEnsembleXGBoostClassifier objective];
-[MLTreeEnsembleXGBoostClassifier packageOutputWithPredictedLabel:classProbabilities:];
-[MLTreeEnsembleXGBoostClassifier populateXGBoostDataFormat:trainingData:dataIndex:inputName:needLabels:error:];
-[MLTreeEnsembleXGBoostClassifier setBooster:];
-[MLTreeEnsembleXGBoostClassifier setLabelsForDataPoints:];
-[MLTreeEnsembleXGBoostClassifier setNumClasses:];
-[MLTreeEnsembleXGBoostClassifier setObjective:];
-[MLTreeEnsembleXGBoostClassifier xgBoostDataFormatFromBatchProvider:needLabels:error:];
-[MLTreeEnsembleXGBoostClassifier xgBoostDataFormatFromFeatureProvider:error:];
```
