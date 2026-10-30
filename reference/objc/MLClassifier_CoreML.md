# `MLClassifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLClassifier`
- 3 instance variables, 11 properties, 8 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _asyncClassifierQueueLock;
B _supportsAsyncClassification;
@"NSObject<OS_dispatch_queue>" _asyncClassifierQueue;
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

## Class methods

```
+[MLClassifier predictionFromFeatures:classifier:options:error:];
```

## Instance methods

```
-[MLClassifier classLabels];
-[MLClassifier predictionFromFeatures:options:completionHandler:];
-[MLClassifier predictionFromFeatures:options:error:];
-[MLClassifier classify:options:error:];
-[MLClassifier _needsToEmulateAsyncClassificationUsingQueue:];
-[MLClassifier classifierResultFromOutputFeatures:error:];
-[MLClassifier initDescriptionOnlyWithSpecification:configuration:error:];
-[MLClassifier initWithDescription:configuration:error:];
```
