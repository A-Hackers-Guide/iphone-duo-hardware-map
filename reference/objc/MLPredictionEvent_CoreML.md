# `MLPredictionEvent`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _predictionEventQueue;
q _featuresPredictionCountSoFar;
Q _epochIndex;
@"MLPredictionEventMetric" _lastReportedMetric;
{mach_timebase_info="numer"I"denom"I} _timebaseInfo;
@"NSString" _bundleIdentifier;
@"NSString" _modelName;
@"NSNumber" _firstPartyExecutable;
@"NSNumber" _modelType;
```

## Properties

```
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",C,N,V_modelName) modelName;
@property (T@"NSNumber",C,N,V_firstPartyExecutable) firstPartyExecutable;
@property (T@"NSNumber",C,N,V_modelType) modelType;
```

## Instance methods

```
-[MLPredictionEvent firstPartyExecutable];
-[MLPredictionEvent init];
-[MLPredictionEvent setFirstPartyExecutable:];
-[MLPredictionEvent bundleIdentifier];
-[MLPredictionEvent setModelName:];
-[MLPredictionEvent maybeLogPredictionEvent:];
-[MLPredictionEvent modelType];
-[MLPredictionEvent setBundleIdentifier:];
-[MLPredictionEvent lastReportedMetric];
-[MLPredictionEvent modelName];
-[MLPredictionEvent setModelType:];
```
