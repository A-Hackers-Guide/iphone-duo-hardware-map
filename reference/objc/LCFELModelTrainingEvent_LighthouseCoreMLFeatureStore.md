# `LCFELModelTrainingEvent`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _contextId;
@"NSUUID" _eventId;
@"NSString" _modelName;
@"LCFELBatchProviderInfo" _bachProviderInfo;
@"NSNumber" _succeeded;
@"NSError" _trainingError;
```

## Properties

```
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_modelName) modelName;
@property (T@"LCFELBatchProviderInfo",R,N,V_bachProviderInfo) bachProviderInfo;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_trainingError) trainingError;
```

## Instance methods

```
-[LCFELModelTrainingEvent contextId];
-[LCFELModelTrainingEvent succeeded];
-[LCFELModelTrainingEvent modelName];
-[LCFELModelTrainingEvent eventId];
-[LCFELModelTrainingEvent trainingError];
-[LCFELModelTrainingEvent bachProviderInfo];
-[LCFELModelTrainingEvent init:batchProviderInfo:succeeded:trainingError:];
```
