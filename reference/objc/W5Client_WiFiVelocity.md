# `W5Client`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 67 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _conn;
@"NSObject<OS_dispatch_queue>" _queue;
d _lastRecoveryTimestamp;
@"NSMutableArray" _mutableEventIDs;
@"NSMutableArray" _mutableUUIDs;
@"NSMutableDictionary" _mutableEventCallbackMap;
@"NSMutableDictionary" _mutablePeerEventCallbackMap;
@"NSMutableSet" _mutableFaultEventMonitoringPeers;
@? _eventCallback;
```

## Properties

```
@property (T@?,C,N,V_eventCallback) eventCallback;
```

## Class methods

```
+[W5Client sharedClient];
```

## Instance methods

```
-[W5Client peers];
-[W5Client init];
-[W5Client cancelAllRequests];
-[W5Client dealloc];
-[W5Client setEventCallback:];
-[W5Client receivedEvent:];
-[W5Client eventCallback];
-[W5Client localPeer];
-[W5Client startBrowsing];
-[W5Client stopBrowsing];
-[W5Client collectLogs:configuration:update:receipts:error:];
-[W5Client queryStatusForPeer:error:];
-[W5Client startMonitoringEvents:];
-[W5Client stopMonitoringEvents:];
-[W5Client submitFaultEvent:error:];
-[W5Client collectLogs:configuration:update:reply:];
-[W5Client runDiagnostics:configuration:update:reply:];
-[W5Client __cancelAllRequestsAndReply:];
-[W5Client __cancelRequestWithUUID:reply:];
-[W5Client __collectBusyFallbackLogsWithReason:compress:];
-[W5Client __collectJetsamFallbackLogsWithReason:compress:];
-[W5Client __eventCallbackSignatureForEventID:peer:];
-[W5Client __log:timestamp:reply:];
-[W5Client __logsCollectedWithTemporaryURL:outputURL:keepParent:compress:reply:];
-[W5Client __mostRecentInDirectories:include:exclude:maxAge:];
-[W5Client __purgeFilesInDirectory:matching:maxAge:maxCount:];
-[W5Client __queryLocalPeerAndReply:];
-[W5Client __startMonitoringEvents:reply:];
-[W5Client __stopMonitoringEvents:reply:];
-[W5Client __tarballWithSource:destination:error:];
-[W5Client associateToNetworkOnPeer:scanResult:configuration:reply:];
-[W5Client cancelRequestWithUUID:];
-[W5Client cancelRequestWithUUID:peer:type:reply:];
-[W5Client collectLogsDiagnosticMode:update:receipts:error:];
-[W5Client collectLogsDiagnosticMode:update:reply:];
-[W5Client faultEventCacheForPeer:error:];
-[W5Client listFilesFromPeer:remoteDirPath:reply:];
-[W5Client log:timestamp:];
-[W5Client queryDatabaseForPeer:fetch:reply:];
-[W5Client queryDebugConfigurationForPeer:error:];
-[W5Client queryDebugConfigurationForPeer:reply:];
-[W5Client queryDiagnosticsModeForPeer:info:reply:];
-[W5Client queryRegisteredDiagnosticsPeersWithReply:];
-[W5Client queryStatusForPeer:reply:];
-[W5Client receivedPeerDiscoveryEvent:];
-[W5Client registerRemoteDiagnosticEventsForPeer:configuration:error:];
-[W5Client requestFileFromPeer:remoteFilePath:reply:];
-[W5Client runDiagnostics:configuration:update:error:];
-[W5Client runDiagnosticsForPeer:diagnostics:configuration:reply:];
-[W5Client runWiFiPerformanceLoggingWithConfiguration:error:];
-[W5Client runWiFiPerformanceLoggingWithConfiguration:reply:];
-[W5Client runWiFiSnifferOnChannel:duration:peer:error:];
-[W5Client runWiFiSnifferOnChannel:duration:peer:reply:];
-[W5Client runWiFiSnifferOnChannels:duration:peer:reply:];
-[W5Client runWiFiSnifferOnChannels:duration:peer:snifferErrors:error:];
-[W5Client runWiFiSnifferWithTCPDumpOnChannels:duration:peer:error:];
-[W5Client runWiFiSnifferWithTCPDumpOnChannels:duration:peer:reply:];
-[W5Client setDebugConfiguration:peer:error:];
-[W5Client setDebugConfiguration:peer:reply:];
-[W5Client startDiagnosticsModeWithConfiguration:reply:];
-[W5Client startMonitoringFaultEventsForPeer:eventHandler:error:];
-[W5Client startNetworkDiscoveryOnPeer:configuration:reply:];
-[W5Client startPeerDiscoveryWithConfiguration:reply:];
-[W5Client stopDiagnosticsModeWithUUID:info:reply:];
-[W5Client stopMonitoringFaultEventsForPeer:error:];
-[W5Client stopPeerDiscoveryWithUUID:];
-[W5Client unregisterRemoteDiagnosticEventsForPeer:configuration:error:];
```
