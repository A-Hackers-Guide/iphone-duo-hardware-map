# `BWOpportunisticInferenceAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
I _facesProcessedCount;
q _totalInferenceExecutionTime;
q _inferenceDeadlineOverdue;
```

## Properties

```
@property (Tq,N,V_totalInferenceExecutionTime) totalInferenceExecutionTime;
@property (Tq,N,V_inferenceDeadlineOverdue) inferenceDeadlineOverdue;
@property (TI,N,V_facesProcessedCount) facesProcessedCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWOpportunisticInferenceAnalyticsPayload eventDictionary];
-[BWOpportunisticInferenceAnalyticsPayload init];
-[BWOpportunisticInferenceAnalyticsPayload reset];
-[BWOpportunisticInferenceAnalyticsPayload eventName];
-[BWOpportunisticInferenceAnalyticsPayload setTotalInferenceExecutionTime:];
-[BWOpportunisticInferenceAnalyticsPayload facesProcessedCount];
-[BWOpportunisticInferenceAnalyticsPayload inferenceDeadlineOverdue];
-[BWOpportunisticInferenceAnalyticsPayload setFacesProcessedCount:];
-[BWOpportunisticInferenceAnalyticsPayload setInferenceDeadlineOverdue:];
-[BWOpportunisticInferenceAnalyticsPayload totalInferenceExecutionTime];
```
