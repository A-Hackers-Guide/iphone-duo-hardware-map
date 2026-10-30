# `SNNetworkAnalytics`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"SNNetworkAnalyticsInternal" _underlyingNetworkAnalytics;
```

## Properties

```
@property (T@"SNNetworkAnalyticsInternal",&,N,V_underlyingNetworkAnalytics) underlyingNetworkAnalytics;
```

## Class methods

```
+[SNNetworkAnalytics sessionConnectionFailedError:connectionMode:sessionType:sessionState:dormant:connectionAnalysisInfo:];
+[SNNetworkAnalytics sharedSNNetworkAnalytics];
```

## Instance methods

```
-[SNNetworkAnalytics init];
-[SNNetworkAnalytics reset];
-[SNNetworkAnalytics _init];
-[SNNetworkAnalytics setNetId:];
-[SNNetworkAnalytics isConnectionActive];
-[SNNetworkAnalytics getSequenceNumber];
-[SNNetworkAnalytics increaseSequenceNumber];
-[SNNetworkAnalytics isNetIdAvailable];
-[SNNetworkAnalytics logDebugNetworkConnectionStatePreparationSnapshotCaptured:];
-[SNNetworkAnalytics logDebugNetworkConnectionStateReadySnapshotCaptured:];
-[SNNetworkAnalytics logDebugSessionConnectionSnapshotCaptured:];
-[SNNetworkAnalytics logNetworkConnectionStatePreparationSnapshotCaptured:];
-[SNNetworkAnalytics logNetworkConnectionStateReadySnapshotCaptured:];
-[SNNetworkAnalytics logPeerConnectionFailed:];
-[SNNetworkAnalytics logRequestLinkBetweenOrchestratorAndNetworkComponent];
-[SNNetworkAnalytics logSessionConnectionFailed:];
-[SNNetworkAnalytics logSessionConnectionHttpHeaderCreated:];
-[SNNetworkAnalytics logSessionConnectionSnapshotCaptured:];
-[SNNetworkAnalytics resetNetId];
-[SNNetworkAnalytics resetSequenceNumber];
-[SNNetworkAnalytics setIsConnectionActive:];
-[SNNetworkAnalytics setNetIdAvailable:];
-[SNNetworkAnalytics setOrchestratorRequestId:];
-[SNNetworkAnalytics getNetId];
-[SNNetworkAnalytics getOrchestratorRequestId];
-[SNNetworkAnalytics setUnderlyingNetworkAnalytics:];
-[SNNetworkAnalytics underlyingNetworkAnalytics];
```
