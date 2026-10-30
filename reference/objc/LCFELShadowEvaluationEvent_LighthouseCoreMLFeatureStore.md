# `LCFELShadowEvaluationEvent`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _contextId;
@"NSUUID" _eventId;
@"NSString" _modelName;
@"LCFELBatchProviderInfo" _inputBachProviderInfo;
@"NSArray" _evaluatedPredictions;
@"NSNumber" _accuracy;
@"NSNumber" _succeeded;
@"NSError" _evaluationError;
```

## Properties

```
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_modelName) modelName;
@property (T@"LCFELBatchProviderInfo",R,N,V_inputBachProviderInfo) inputBachProviderInfo;
@property (T@"NSArray",R,N,V_evaluatedPredictions) evaluatedPredictions;
@property (T@"NSNumber",R,N,V_accuracy) accuracy;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_evaluationError) evaluationError;
```

## Instance methods

```
-[LCFELShadowEvaluationEvent contextId];
-[LCFELShadowEvaluationEvent succeeded];
-[LCFELShadowEvaluationEvent accuracy];
-[LCFELShadowEvaluationEvent modelName];
-[LCFELShadowEvaluationEvent eventId];
-[LCFELShadowEvaluationEvent evaluationError];
-[LCFELShadowEvaluationEvent evaluatedPredictions];
-[LCFELShadowEvaluationEvent init:inputBachProviderInfo:evaluatedPredictions:accuracy:succeeded:evaluationError:];
-[LCFELShadowEvaluationEvent inputBachProviderInfo];
```
