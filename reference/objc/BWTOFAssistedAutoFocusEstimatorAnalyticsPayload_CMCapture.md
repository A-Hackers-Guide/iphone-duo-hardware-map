# `BWTOFAssistedAutoFocusEstimatorAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
@"NSString" _clientApplicationID;
@"NSDictionary" _estimatorResults;
I _streamingTime;
```

## Properties

```
@property (T@"NSString",&,N,V_portType) portType;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (T@"NSDictionary",&,N,V_estimatorResults) estimatorResults;
@property (TI,N,V_streamingTime) streamingTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload portType];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload eventDictionary];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload init];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload dealloc];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload reset];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload setClientApplicationID:];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload setPortType:];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload eventName];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload setStreamingTime:];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload streamingTime];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload clientApplicationID];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload estimatorResults];
-[BWTOFAssistedAutoFocusEstimatorAnalyticsPayload setEstimatorResults:];
```
