# `MLModelEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModeling`
- 3 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _signpostID;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _configuration;
```

## Properties

```
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

## Instance methods

```
-[MLModelEngine predictionTypeForKTrace];
-[MLModelEngine predictionsFromBatch:options:error:];
-[MLModelEngine submitPredictionRequest:completionHandler:];
-[MLModelEngine executionSchedule];
-[MLModelEngine enableInstrumentsTracing];
-[MLModelEngine parameterValueForKey:error:];
-[MLModelEngine predictionFromFeatures:error:];
-[MLModelEngine newRequestForModel:inputFeatures:options:error:];
-[MLModelEngine modelPath];
-[MLModelEngine metadata];
-[MLModelEngine predictionsFromBatch:error:];
-[MLModelEngine configuration];
-[MLModelEngine modelDescription];
-[MLModelEngine supportsConcurrentSubmissions];
-[MLModelEngine predictionFromFeatures:options:error:];
-[MLModelEngine signpostID];
-[MLModelEngine initWithDescription:configuration:];
-[MLModelEngine initWithName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLModelEngine recordsPredictionEvent];
-[MLModelEngine setModelPath:modelName:];
-[MLModelEngine vectorizeInput:error:];
```
