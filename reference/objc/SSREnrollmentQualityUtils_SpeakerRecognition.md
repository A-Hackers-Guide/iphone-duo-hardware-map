# `SSREnrollmentQualityUtils`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"CSAsset" _currentAsset;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"CSAsset",&,N,V_currentAsset) currentAsset;
```

## Class methods

```
+[SSREnrollmentQualityUtils isPremiumAssetAvailableForEnrollment:configVersion:];
```

## Instance methods

```
-[SSREnrollmentQualityUtils currentAsset];
-[SSREnrollmentQualityUtils setCurrentAsset:];
-[SSREnrollmentQualityUtils init];
-[SSREnrollmentQualityUtils queue];
-[SSREnrollmentQualityUtils setQueue:];
-[SSREnrollmentQualityUtils retrieveProfileForLocale:error:];
-[SSREnrollmentQualityUtils aggregateQualityProblems:qualityProblems:];
-[SSREnrollmentQualityUtils createMetricsFromCachedValues:wer:similarityScores:profile:spIdType:];
-[SSREnrollmentQualityUtils evaluateProfileHealth:completionHandler:];
-[SSREnrollmentQualityUtils evaluateProfileHealthPerUtterance:completionHandler:];
-[SSREnrollmentQualityUtils problemNameForQualityProblem:];
-[SSREnrollmentQualityUtils problemNamesPerUtterance:];
-[SSREnrollmentQualityUtils processMetricsReport:completionHandler:];
-[SSREnrollmentQualityUtils retrieveAssetForLocale:error:];
```
