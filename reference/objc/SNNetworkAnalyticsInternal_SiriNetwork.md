# `SNNetworkAnalyticsInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 0 properties, 27 instance methods, 7 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 queue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 netId;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkConnectionId;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 connectionProvider;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 orchestratorRequestId;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 netIdForRequestLink;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isConnectionActive;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 netIdAvailable;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 sequenceNumber;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 httpHeaderEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 preparationSnapshotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 debugPreparationSnapshotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 readySnapshotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 debugReadySnapshotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 sessionConnectionSnapthotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 debugSessionConnectionSnapthotEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 sessionConnectionFailedEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 peerConnectionFailedEvent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 siriAnalyticsMessageStream;
```

## Class methods

```
+[SNNetworkAnalyticsInternal netConnectionModeFrom:];
+[SNNetworkAnalyticsInternal netEndpointFromDictionary:];
+[SNNetworkAnalyticsInternal netEndpointTypeFrom:];
+[SNNetworkAnalyticsInternal netSessionConnectionFailedWithError:connectionMode:sessionType:sessionState:isDormant:snConnectionAnalysisInfo:];
+[SNNetworkAnalyticsInternal netSessionStateFrom:];
+[SNNetworkAnalyticsInternal netSessionTypeFrom:];
+[SNNetworkAnalyticsInternal sharedNetworkAnalytics];
```

## Instance methods

```
-[SNNetworkAnalyticsInternal init];
-[SNNetworkAnalyticsInternal reset];
-[SNNetworkAnalyticsInternal setConnectionProvider:];
-[SNNetworkAnalyticsInternal setNetId:];
-[SNNetworkAnalyticsInternal setNetworkConnectionId:];
-[SNNetworkAnalyticsInternal emitLogDebug];
-[SNNetworkAnalyticsInternal getSequenceNumber];
-[SNNetworkAnalyticsInternal increaseSequenceNumber];
-[SNNetworkAnalyticsInternal isNetIdAvailable];
-[SNNetworkAnalyticsInternal logDebugNetworkConnectionStatePreparationSnapshotCaptured:];
-[SNNetworkAnalyticsInternal logDebugNetworkConnectionStateReadySnapshotCaptured:];
-[SNNetworkAnalyticsInternal logDebugSessionConnectionSnapshotCaptured:];
-[SNNetworkAnalyticsInternal logNetworkConnectionStatePreparationSnapshotCaptured:];
-[SNNetworkAnalyticsInternal logNetworkConnectionStateReadySnapshotCaptured:];
-[SNNetworkAnalyticsInternal logPeerConnectionFailed:];
-[SNNetworkAnalyticsInternal logRequestLinkBetweenOrchestratorAndNetworkComponent];
-[SNNetworkAnalyticsInternal logSessionConnectionFailed:];
-[SNNetworkAnalyticsInternal logSessionConnectionHttpHeaderCreated:];
-[SNNetworkAnalyticsInternal logSessionConnectionSnapshotCaptured:];
-[SNNetworkAnalyticsInternal resetNetId];
-[SNNetworkAnalyticsInternal resetSequenceNumber];
-[SNNetworkAnalyticsInternal setIsConnectionActive:];
-[SNNetworkAnalyticsInternal setNetIdAvailable:];
-[SNNetworkAnalyticsInternal getIsConnectionActive];
-[SNNetworkAnalyticsInternal getNetId];
-[SNNetworkAnalyticsInternal getOrchestratorRequestId];
-[SNNetworkAnalyticsInternal setOrchestatorRequestId:];
```
