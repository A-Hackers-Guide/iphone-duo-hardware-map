# `CWFBrokenBackhaulMonitor`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _bbhNotifyToken;
@"NSObject<OS_dispatch_queue>" _internalQueue;
Q _initialIndicationTimestamp;
@"NSMutableDictionary" _pendingMetricSubmissionPayload;
@"NSObject<OS_dispatch_source>" _metricAutoSubmissionTimer;
q _brokenBackhaulState;
@"NSDate" _brokenBackhaulStateUpdatedAt;
@"NSObject<OS_dispatch_queue>" _targetQueue;
@? _updatedBrokenBackhaulState;
```

## Properties

```
@property (Tq,V_brokenBackhaulState) brokenBackhaulState;
@property (T@"NSDate",R,C,V_brokenBackhaulStateUpdatedAt) brokenBackhaulStateUpdatedAt;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
@property (T@?,C,V_updatedBrokenBackhaulState) updatedBrokenBackhaulState;
```

## Instance methods

```
-[CWFBrokenBackhaulMonitor brokenBackhaulState];
-[CWFBrokenBackhaulMonitor brokenBackhaulStateUpdatedAt];
-[CWFBrokenBackhaulMonitor setTargetQueue:];
-[CWFBrokenBackhaulMonitor targetQueue];
-[CWFBrokenBackhaulMonitor activateWithCompletion:];
-[CWFBrokenBackhaulMonitor init];
-[CWFBrokenBackhaulMonitor reset];
-[CWFBrokenBackhaulMonitor invalidate];
-[CWFBrokenBackhaulMonitor setBrokenBackhaulState:];
-[CWFBrokenBackhaulMonitor __confirmBrokenBackhaulUsingTimeout:count:completion:];
-[CWFBrokenBackhaulMonitor __fetchSymptomsBrokenBackhaulStateWithEventID:completion:];
-[CWFBrokenBackhaulMonitor __mapSymptomsBrokenBackhaulState:];
-[CWFBrokenBackhaulMonitor __performProbeToRemoteEndpointUsingTimeout:completion:];
-[CWFBrokenBackhaulMonitor __submitCoreAnalyticsEvent];
-[CWFBrokenBackhaulMonitor __updateBrokenBackhaulState:timestamp:usingQuickProbeTimeout:];
-[CWFBrokenBackhaulMonitor __updatePendingCoreAnalyticsPayloadWithNewBrokenBackhaulState:usingQuickProbeTimeout:];
-[CWFBrokenBackhaulMonitor confirmBrokenBackhaulUsingTimeout:count:preflightPingAddress:completion:];
-[CWFBrokenBackhaulMonitor setUpdatedBrokenBackhaulState:];
-[CWFBrokenBackhaulMonitor updatedBrokenBackhaulState];
```
