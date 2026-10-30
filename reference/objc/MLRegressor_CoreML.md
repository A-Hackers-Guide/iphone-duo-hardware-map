# `MLRegressor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLRegressor`
- 0 instance variables, 11 properties, 5 instance methods, 1 class methods

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

## Class methods

```
+[MLRegressor predictionFromFeatures:regressor:options:error:];
```

## Instance methods

```
-[MLRegressor regress:options:error:];
-[MLRegressor predictionFromFeatures:options:error:];
-[MLRegressor initDescriptionOnlyWithSpecification:configuration:error:];
-[MLRegressor initWithDescription:configuration:error:];
-[MLRegressor regressorResultFromOutputFeatures:error:];
```
