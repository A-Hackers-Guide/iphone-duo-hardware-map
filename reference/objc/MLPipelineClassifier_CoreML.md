# `MLPipelineClassifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLClassifier`
- Protocols: `MLAsyncClassifier`
- 1 instance variables, 13 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"MLPipeline" _engine;
```

## Properties

```
@property (T@"MLPipeline",&,V_engine) engine;
@property (T@"MLPipeline",R) pipeline;
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
-[MLPipelineClassifier setEngine:];
-[MLPipelineClassifier executionSchedule];
-[MLPipelineClassifier enableInstrumentsTracing];
-[MLPipelineClassifier engine];
-[MLPipelineClassifier initWithEngine:description:configuration:error:];
-[MLPipelineClassifier pipeline];
-[MLPipelineClassifier classify:options:error:];
-[MLPipelineClassifier signpostID];
-[MLPipelineClassifier classify:options:completionHandler:];
```
