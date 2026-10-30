# `MLModeling` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
```

## Instance methods

```
-[MLModeling predictionTypeForKTrace];
-[MLModeling predictionsFromBatch:options:error:];
-[MLModeling submitPredictionRequest:completionHandler:];
-[MLModeling executionSchedule];
-[MLModeling enableInstrumentsTracing];
-[MLModeling parameterValueForKey:error:];
-[MLModeling predictionFromFeatures:error:];
-[MLModeling newRequestForModel:inputFeatures:options:error:];
-[MLModeling modelPath];
-[MLModeling metadata];
-[MLModeling predictionsFromBatch:error:];
-[MLModeling configuration];
-[MLModeling modelDescription];
-[MLModeling supportsConcurrentSubmissions];
-[MLModeling predictionFromFeatures:options:error:];
-[MLModeling signpostID];
-[MLModeling recordsPredictionEvent];
-[MLModeling setModelPath:modelName:];
```
