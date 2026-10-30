# `SNConnectionMetrics`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 46 instance variables, 46 properties, 93 instance methods, 0 class methods

## Instance variables

```
@"SNConnectionMetrics" _remoteMetrics;
@"NSString" _snapshotTriggerReason;
@"NSString" _providerStyle;
@"NSNumber" _metricsCount;
@"NSString" _policyId;
@"NSNumber" _timeUntilOpen;
@"NSNumber" _timeUntilFirstByteRead;
@"NSNumber" _attemptCount;
@"NSNumber" _dnsResolutionTime;
@"NSNumber" _connectionStartTimeToDNSResolutionTimeMsec;
@"NSNumber" _connectionEstablishmentTimeMsec;
@"NSNumber" _connectionStartTimeToConnectionEstablishmentTimeMsec;
@"NSNumber" _connectionStartTimeToTLSHandshakeTimeMsec;
@"NSString" _tlsVersion;
@"NSNumber" _tlsHandshakeTimeMsec;
@"NSNumber" _pingCount;
@"NSNumber" _meanPing;
@"NSNumber" _unacknowledgedPingCount;
@"NSDictionary" _flowNetworkInterfaceType;
@"NSDictionary" _tcpInfoMetricsByInterfaceName;
@"NSNumber" _subflowCount;
@"NSNumber" _connectedSubflowCount;
@"NSDictionary" _subflowSwitchCounts;
@"NSString" _primarySubflowInterfaceName;
@"NSString" _connectionMethod;
@"NSString" _connectionEdgeID;
@"NSString" _connectionEdgeType;
@"NSArray" _connectionMethodHistory;
@"NSNumber" _connectionFallbackReason;
@"NSNumber" _connectionDelay;
@"NSNumber" _firstTxByteDelay;
@"NSString" _carrierName;
@"NSNumber" _signalStrengthBars;
@"NSNumber" _simSubscriptions;
@"NSString" _wifiPhyMode;
@"NSString" _wifiChannelInfo;
@"NSNumber" _rssi;
@"NSNumber" _snr;
@"NSNumber" _cca;
@"NSNumber" _isCaptive;
@"NSDictionary" _symptomsBasedNetworkQuality;
@"NSNumber" _idsLastMessageDelay;
@"NSNumber" _idsLastSocketDelay;
@"NSNumber" _idsLastSocketOpenError;
@"NETSchemaNETSessionConnectionSnapshotCaptured" _connectionSnapshot;
@"NETSchemaNETDebugSessionConnectionSnapshotCaptured" _debugConnectionSnapshot;
```

## Properties

```
@property (T@"SNConnectionMetrics",&,N,V_remoteMetrics) remoteMetrics;
@property (T@"NSString",C,N,V_snapshotTriggerReason) snapshotTriggerReason;
@property (T@"NSString",C,N,V_providerStyle) providerStyle;
@property (T@"NSNumber",C,N,V_metricsCount) metricsCount;
@property (T@"NSString",C,N,V_policyId) policyId;
@property (T@"NSNumber",C,N,V_timeUntilOpen) timeUntilOpen;
@property (T@"NSNumber",C,N,V_timeUntilFirstByteRead) timeUntilFirstByteRead;
@property (T@"NSNumber",C,N,V_attemptCount) attemptCount;
@property (T@"NSNumber",C,N,V_dnsResolutionTime) dnsResolutionTime;
@property (T@"NSNumber",C,N,V_connectionStartTimeToDNSResolutionTimeMsec) connectionStartTimeToDNSResolutionTimeMsec;
@property (T@"NSNumber",C,N,V_connectionEstablishmentTimeMsec) connectionEstablishmentTimeMsec;
@property (T@"NSNumber",C,N,V_connectionStartTimeToConnectionEstablishmentTimeMsec) connectionStartTimeToConnectionEstablishmentTimeMsec;
@property (T@"NSNumber",C,N,V_connectionStartTimeToTLSHandshakeTimeMsec) connectionStartTimeToTLSHandshakeTimeMsec;
@property (T@"NSString",C,N,V_tlsVersion) tlsVersion;
@property (T@"NSNumber",C,N,V_tlsHandshakeTimeMsec) tlsHandshakeTimeMsec;
@property (T@"NSNumber",C,N,V_pingCount) pingCount;
@property (T@"NSNumber",C,N,V_meanPing) meanPing;
@property (T@"NSNumber",C,N,V_unacknowledgedPingCount) unacknowledgedPingCount;
@property (T@"NSDictionary",C,N,V_flowNetworkInterfaceType) flowNetworkInterfaceType;
@property (T@"NSDictionary",C,N,SsetTCPInfoMetricsByInterfaceName:,V_tcpInfoMetricsByInterfaceName) tcpInfoMetricsByInterfaceName;
@property (T@"NSNumber",C,N,V_subflowCount) subflowCount;
@property (T@"NSNumber",C,N,V_connectedSubflowCount) connectedSubflowCount;
@property (T@"NSDictionary",C,N,V_subflowSwitchCounts) subflowSwitchCounts;
@property (T@"NSString",C,N,V_primarySubflowInterfaceName) primarySubflowInterfaceName;
@property (T@"NSString",C,N,V_connectionMethod) connectionMethod;
@property (T@"NSString",C,N,V_connectionEdgeID) connectionEdgeID;
@property (T@"NSString",C,N,V_connectionEdgeType) connectionEdgeType;
@property (T@"NSArray",C,N,V_connectionMethodHistory) connectionMethodHistory;
@property (T@"NSNumber",C,N,V_connectionFallbackReason) connectionFallbackReason;
@property (T@"NSNumber",C,N,V_connectionDelay) connectionDelay;
@property (T@"NSNumber",C,N,V_firstTxByteDelay) firstTxByteDelay;
@property (T@"NSString",C,N,V_carrierName) carrierName;
@property (T@"NSNumber",C,N,V_signalStrengthBars) signalStrengthBars;
@property (T@"NSNumber",C,N,V_simSubscriptions) simSubscriptions;
@property (T@"NSString",C,N,V_wifiPhyMode) wifiPhyMode;
@property (T@"NSString",C,N,V_wifiChannelInfo) wifiChannelInfo;
@property (T@"NSNumber",C,N,V_rssi) rssi;
@property (T@"NSNumber",C,N,V_snr) snr;
@property (T@"NSNumber",C,N,V_cca) cca;
@property (T@"NSNumber",C,N,V_isCaptive) isCaptive;
@property (T@"NSDictionary",C,N,V_symptomsBasedNetworkQuality) symptomsBasedNetworkQuality;
@property (T@"NSNumber",C,N,V_idsLastMessageDelay) idsLastMessageDelay;
@property (T@"NSNumber",C,N,V_idsLastSocketDelay) idsLastSocketDelay;
@property (T@"NSNumber",C,N,V_idsLastSocketOpenError) idsLastSocketOpenError;
@property (T@"NETSchemaNETSessionConnectionSnapshotCaptured",&,N,V_connectionSnapshot) connectionSnapshot;
@property (T@"NETSchemaNETDebugSessionConnectionSnapshotCaptured",&,N,V_debugConnectionSnapshot) debugConnectionSnapshot;
```

## Instance methods

```
-[SNConnectionMetrics rssi];
-[SNConnectionMetrics cca];
-[SNConnectionMetrics setSnr:];
-[SNConnectionMetrics timeUntilOpen];
-[SNConnectionMetrics snr];
-[SNConnectionMetrics setPolicyId:];
-[SNConnectionMetrics connectionFallbackReason];
-[SNConnectionMetrics carrierName];
-[SNConnectionMetrics timeUntilFirstByteRead];
-[SNConnectionMetrics setCarrierName:];
-[SNConnectionMetrics setConnectionMethod:];
-[SNConnectionMetrics setPrimarySubflowInterfaceName:];
-[SNConnectionMetrics setConnectionMethodHistory:];
-[SNConnectionMetrics setDnsResolutionTime:];
-[SNConnectionMetrics subflowSwitchCounts];
-[SNConnectionMetrics setTimeUntilFirstByteRead:];
-[SNConnectionMetrics setMeanPing:];
-[SNConnectionMetrics connectionDelay];
-[SNConnectionMetrics setSubflowCount:];
-[SNConnectionMetrics tlsHandshakeTimeMsec];
-[SNConnectionMetrics providerStyle];
-[SNConnectionMetrics setConnectionEstablishmentTimeMsec:];
-[SNConnectionMetrics setCca:];
-[SNConnectionMetrics setRssi:];
-[SNConnectionMetrics dnsResolutionTime];
-[SNConnectionMetrics firstTxByteDelay];
-[SNConnectionMetrics setIsCaptive:];
-[SNConnectionMetrics connectionEdgeID];
-[SNConnectionMetrics unacknowledgedPingCount];
-[SNConnectionMetrics setFirstTxByteDelay:];
-[SNConnectionMetrics tlsVersion];
-[SNConnectionMetrics setProviderStyle:];
-[SNConnectionMetrics setConnectionStartTimeToTLSHandshakeTimeMsec:];
-[SNConnectionMetrics flowNetworkInterfaceType];
-[SNConnectionMetrics pingCount];
-[SNConnectionMetrics setConnectionFallbackReason:];
-[SNConnectionMetrics connectedSubflowCount];
-[SNConnectionMetrics debugConnectionSnapshot];
-[SNConnectionMetrics connectionSnapshot];
-[SNConnectionMetrics setIdsLastSocketOpenError:];
-[SNConnectionMetrics idsLastMessageDelay];
-[SNConnectionMetrics setConnectionEdgeType:];
-[SNConnectionMetrics setUnacknowledgedPingCount:];
-[SNConnectionMetrics setIdsLastSocketDelay:];
-[SNConnectionMetrics remoteMetrics];
-[SNConnectionMetrics setMetricsCount:];
-[SNConnectionMetrics setRemoteMetrics:];
-[SNConnectionMetrics setWifiPhyMode:];
-[SNConnectionMetrics tcpInfoMetricsByInterfaceName];
-[SNConnectionMetrics setConnectedSubflowCount:];
-[SNConnectionMetrics setFlowNetworkInterfaceType:];
-[SNConnectionMetrics connectionEstablishmentTimeMsec];
-[SNConnectionMetrics connectionStartTimeToTLSHandshakeTimeMsec];
-[SNConnectionMetrics setConnectionStartTimeToConnectionEstablishmentTimeMsec:];
-[SNConnectionMetrics setSimSubscriptions:];
-[SNConnectionMetrics primarySubflowInterfaceName];
-[SNConnectionMetrics isCaptive];
-[SNConnectionMetrics snapshotTriggerReason];
-[SNConnectionMetrics wifiPhyMode];
-[SNConnectionMetrics setPingCount:];
-[SNConnectionMetrics connectionStartTimeToConnectionEstablishmentTimeMsec];
-[SNConnectionMetrics idsLastSocketOpenError];
-[SNConnectionMetrics connectionEdgeType];
-[SNConnectionMetrics setSymptomsBasedNetworkQuality:];
-[SNConnectionMetrics simSubscriptions];
-[SNConnectionMetrics setConnectionEdgeID:];
-[SNConnectionMetrics symptomsBasedNetworkQuality];
-[SNConnectionMetrics setConnectionDelay:];
-[SNConnectionMetrics signalStrengthBars];
-[SNConnectionMetrics connectionMethodHistory];
-[SNConnectionMetrics policyId];
-[SNConnectionMetrics setAttemptCount:];
-[SNConnectionMetrics setConnectionSnapshot:];
-[SNConnectionMetrics setIdsLastMessageDelay:];
-[SNConnectionMetrics setWifiChannelInfo:];
-[SNConnectionMetrics setSubflowSwitchCounts:];
-[SNConnectionMetrics subflowCount];
-[SNConnectionMetrics setDebugConnectionSnapshot:];
-[SNConnectionMetrics connectionStartTimeToDNSResolutionTimeMsec];
-[SNConnectionMetrics idsLastSocketDelay];
-[SNConnectionMetrics getConnectionMetricsDescription];
-[SNConnectionMetrics setConnectionStartTimeToDNSResolutionTimeMsec:];
-[SNConnectionMetrics setSignalStrengthBars:];
-[SNConnectionMetrics setTimeUntilOpen:];
-[SNConnectionMetrics wifiChannelInfo];
-[SNConnectionMetrics setTlsHandshakeTimeMsec:];
-[SNConnectionMetrics setSnapshotTriggerReason:];
-[SNConnectionMetrics setTlsVersion:];
-[SNConnectionMetrics attemptCount];
-[SNConnectionMetrics setTCPInfoMetricsByInterfaceName:];
-[SNConnectionMetrics meanPing];
-[SNConnectionMetrics connectionMethod];
-[SNConnectionMetrics metricsCount];
```
