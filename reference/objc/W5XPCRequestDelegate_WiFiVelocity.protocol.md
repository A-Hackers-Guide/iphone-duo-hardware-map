# `W5XPCRequestDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 39 instance methods, 0 class methods

## Instance methods

```
-[W5XPCRequestDelegate associateToNetworkOnPeer:scanResult:configuration:reply:];
-[W5XPCRequestDelegate cancelAllRequestsAndReply:];
-[W5XPCRequestDelegate cancelRequestWithUUID:OnPeer:OfType:reply:];
-[W5XPCRequestDelegate cancelRequestWithUUID:reply:];
-[W5XPCRequestDelegate collectLogs:configuration:uuid:reply:];
-[W5XPCRequestDelegate collectLogsDiagnosticMode:uuid:reply:];
-[W5XPCRequestDelegate listFilesFromPeer:remoteDirPath:reply:];
-[W5XPCRequestDelegate log:timestamp:reply:];
-[W5XPCRequestDelegate queryDatabaseForPeer:fetch:reply:];
-[W5XPCRequestDelegate queryDebugConfigurationForPeer:reply:];
-[W5XPCRequestDelegate queryDiagnosticsModeForPeer:info:reply:];
-[W5XPCRequestDelegate queryFaultEventCacheForPeer:reply:];
-[W5XPCRequestDelegate queryLocalPeerAndReply:];
-[W5XPCRequestDelegate queryPeerCacheAndReply:];
-[W5XPCRequestDelegate queryRegisteredDiagnosticsPeersWithReply:];
-[W5XPCRequestDelegate queryStatusForPeer:reply:];
-[W5XPCRequestDelegate registerRemoteDiagnosticEventsForPeer:configuration:reply:];
-[W5XPCRequestDelegate requestFileFromPeer:remoteFilePath:reply:];
-[W5XPCRequestDelegate runDiagnostics:configuration:uuid:reply:];
-[W5XPCRequestDelegate runDiagnosticsForPeer:diagnostics:configuration:uuid:reply:];
-[W5XPCRequestDelegate runWiFiPerformanceLoggingWithConfiguration:uuid:reply:];
-[W5XPCRequestDelegate runWiFiSnifferOnChannels:duration:peer:uuid:reply:];
-[W5XPCRequestDelegate runWiFiSnifferWithTCPDumpOnChannels:duration:peer:uuid:reply:];
-[W5XPCRequestDelegate setDebugConfiguration:peer:reply:];
-[W5XPCRequestDelegate startAdvertisingAndReply:];
-[W5XPCRequestDelegate startBrowsingAndReply:];
-[W5XPCRequestDelegate startDiagnosticsModeWithConfiguration:reply:];
-[W5XPCRequestDelegate startMonitoringEvents:reply:];
-[W5XPCRequestDelegate startMonitoringFaultEventsForPeer:reply:];
-[W5XPCRequestDelegate startNetworkDiscoveryOnPeer:configuration:reply:];
-[W5XPCRequestDelegate startPeerDiscoveryWithConfiguration:uuid:reply:];
-[W5XPCRequestDelegate stopAdvertisingAndReply:];
-[W5XPCRequestDelegate stopBrowsingAndReply:];
-[W5XPCRequestDelegate stopDiagnosticsModeWithUUID:info:reply:];
-[W5XPCRequestDelegate stopMonitoringEvents:reply:];
-[W5XPCRequestDelegate stopMonitoringFaultEventsForPeer:reply:];
-[W5XPCRequestDelegate stopPeerDiscoveryWithUUID:reply:];
-[W5XPCRequestDelegate submitFaultEvent:reply:];
-[W5XPCRequestDelegate unregisterRemoteDiagnosticEventsForPeer:configuration:reply:];
```
