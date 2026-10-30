# `MLPredictionEventMetric`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUTCoreAnalyticsMetric`
- 6 instance variables, 12 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"NSString" _modelName;
@"NSNumber" _firstPartyExecutable;
@"NSNumber" _modelType;
d _featuresPredictionDuration;
q _featuresPredictionCountSoFar;
```

## Properties

```
@property (T@"NSDictionary",R) dictionaryRepresentation;
@property (T@"NSString",R,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,N,V_modelName) modelName;
@property (T@"NSNumber",R,N,V_firstPartyExecutable) firstPartyExecutable;
@property (T@"NSNumber",R,N,V_modelType) modelType;
@property (Td,R,N,V_featuresPredictionDuration) featuresPredictionDuration;
@property (Tq,R,N,V_featuresPredictionCountSoFar) featuresPredictionCountSoFar;
@property (T@"NSString",R) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLPredictionEventMetric firstPartyExecutable];
-[MLPredictionEventMetric bundleIdentifier];
-[MLPredictionEventMetric featuresPredictionCountSoFar];
-[MLPredictionEventMetric featuresPredictionDuration];
-[MLPredictionEventMetric initWithBundleIdentifier:modelName:firstPartyExecutable:modelType:featuresPredictionDuration:featuresPredictionCountSoFar:];
-[MLPredictionEventMetric modelType];
-[MLPredictionEventMetric name];
-[MLPredictionEventMetric modelName];
-[MLPredictionEventMetric dictionaryRepresentation];
```
