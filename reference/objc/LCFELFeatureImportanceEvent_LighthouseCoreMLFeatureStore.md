# `LCFELFeatureImportanceEvent`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _contextId;
@"NSUUID" _eventId;
@"LCFELBatchProviderInfo" _inputBachProviderInfo;
@"NSString" _targetLabelFeatureName;
@"NSArray" _results;
@"NSNumber" _succeeded;
@"NSError" _analysisError;
```

## Properties

```
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"LCFELBatchProviderInfo",R,N,V_inputBachProviderInfo) inputBachProviderInfo;
@property (T@"NSString",R,N,V_targetLabelFeatureName) targetLabelFeatureName;
@property (T@"NSArray",R,N,V_results) results;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_analysisError) analysisError;
```

## Instance methods

```
-[LCFELFeatureImportanceEvent contextId];
-[LCFELFeatureImportanceEvent succeeded];
-[LCFELFeatureImportanceEvent results];
-[LCFELFeatureImportanceEvent eventId];
-[LCFELFeatureImportanceEvent analysisError];
-[LCFELFeatureImportanceEvent init:targetLabelFeatureName:results:succeeded:analysisError:];
-[LCFELFeatureImportanceEvent inputBachProviderInfo];
-[LCFELFeatureImportanceEvent targetLabelFeatureName];
```
