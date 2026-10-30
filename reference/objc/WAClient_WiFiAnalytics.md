# `WAClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 117 instance methods, 5 class methods

## Instance variables

```
@"NSMutableDictionary" _interestedMessageIdentifiers;
@"NSMutableDictionary" _configuredMessageIdentifiers;
C _daemonConnectionValid;
C _blockDaemonConnection;
@"NSDictionary" _deviceAnalyticsConfig;
@"NSXPCConnection" _conn;
@"NSXPCInterface" _exportedRemoteInterface;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"NSObject<OS_dispatch_queue>" _propertyQueue;
@"NSObject<OS_dispatch_queue>" _fileHandlingQueue;
@"NSObject<OS_dispatch_queue>" _queryableQueue;
@"NSMutableArray" _queuedInvocations;
d _connectionRecoveryStartTime;
@? _recoveryTickBlock;
@"NSString" _tokenForThisClient;
@"NSString" _identifierForThisClient;
@"NSMutableSet" _registeredGroupTypes;
@"NSURL" _wifianalyticsTmpDir;
d _allowPurgeJSONFilesAfterSec;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_conn) conn;
@property (T@"NSXPCInterface",&,N,V_exportedRemoteInterface) exportedRemoteInterface;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_replyQueue) replyQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_propertyQueue) propertyQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_fileHandlingQueue) fileHandlingQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queryableQueue) queryableQueue;
@property (T@"NSMutableArray",&,N,V_queuedInvocations) queuedInvocations;
@property (Td,N,V_connectionRecoveryStartTime) connectionRecoveryStartTime;
@property (TC,N,V_daemonConnectionValid) daemonConnectionValid;
@property (TC,N,V_blockDaemonConnection) blockDaemonConnection;
@property (T@?,C,N,V_recoveryTickBlock) recoveryTickBlock;
@property (T@"NSString",&,N,V_tokenForThisClient) tokenForThisClient;
@property (T@"NSString",&,N,V_identifierForThisClient) identifierForThisClient;
@property (T@"NSMutableSet",&,N,V_registeredGroupTypes) registeredGroupTypes;
@property (T@"NSURL",&,N,V_wifianalyticsTmpDir) wifianalyticsTmpDir;
@property (T@"NSDictionary",&,N,V_deviceAnalyticsConfig) deviceAnalyticsConfig;
@property (Td,N,V_allowPurgeJSONFilesAfterSec) allowPurgeJSONFilesAfterSec;
@property (T@"NSMutableDictionary",&,N) configuredMessageIdentifiers;
@property (T@"NSMutableDictionary",&,N) interestedMessageIdentifiers;
```

## Class methods

```
+[WAClient sharedClient];
+[WAClient WANetworkHighestAuthFlagsLabel:];
+[WAClient WANetworkAuthFlagsLabel:];
+[WAClient ouiFromThreeBytes:];
+[WAClient sharedClientWithIdentifier:];
```

## Instance methods

```
-[WAClient _dequeueInvocation:];
-[WAClient submitEvent:withError:];
-[WAClient queryableQueue];
-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:];
-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:];
-[WAClient lqmCrashTracerNotifyForInterfaceWithName:andReply:];
-[WAClient _connectionTimedOut];
-[WAClient asyncSubmitEvent:uponCompletionDo:];
-[WAClient setRecoveryTickBlock:];
-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:];
-[WAClient setDeviceAnalyticsConfiguration:andReply:];
-[WAClient setBlockDaemonConnection:];
-[WAClient asyncSubmitEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:];
-[WAClient fileHandlingQueue];
-[WAClient triggerQueryForNWActivity:andReply:];
-[WAClient resetDeviceAnalyticsConfigurationAndReply:];
-[WAClient signalPotentialNewIORChannelsAndReply:];
-[WAClient _replyAllWithTimeoutErrorAndRemove];
-[WAClient submitEvent:withClient:async:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:];
-[WAClient init];
-[WAClient setReplyQueue:];
-[WAClient triggerQueryForNWActivityWithPeers:andReply:];
-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:];
-[WAClient setDeviceAnalyticsConfig:];
-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:];
-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:];
-[WAClient setConnectionRecoveryStartTime:];
-[WAClient processManagedFault:at:andReply:];
-[WAClient dealloc];
-[WAClient registerMessageGroup:andReply:];
-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:];
-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:];
-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:];
-[WAClient setFileHandlingQueue:];
-[WAClient _registerMessageGroup:andReply:queuedInvocation:];
-[WAClient setConn:];
-[WAClient setAllowPurgeJSONFilesAfterSec:];
-[WAClient queue];
-[WAClient setExportedRemoteInterface:];
-[WAClient _getConnectionIssueHandlerBlock];
-[WAClient setDaemonConnectionValid:];
-[WAClient _killDaemonAndReply:queuedInvocation:];
-[WAClient submitEvent:andDeferReclaimMem:andRunPostProcessing:withError:];
-[WAClient fakeDaemonConnectionDead:];
-[WAClient getDeviceAnalyticsConfigurationAndReply:];
-[WAClient _initPrivate];
-[WAClient registeredGroupTypes];
-[WAClient setPropertyQueue:];
-[WAClient submitEvent:async:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:];
-[WAClient conn];
-[WAClient _processWAMessageForCoreAnalytics:];
-[WAClient submitWiFiAnalytics:data:];
-[WAClient _getUsageStatsandReply:queuedInvocation:];
-[WAClient triggerDeviceAnalyticsStoreMigrationAndReply:];
-[WAClient setWifianalyticsTmpDir:];
-[WAClient setQueryableQueue:];
-[WAClient setIdentifierForThisClient:];
-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:];
-[WAClient getUsageStatsandReply:];
-[WAClient clearMessageStoreAndReply:];
-[WAClient asyncSubmitEvent:];
-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:];
-[WAClient killDaemonAndReply:];
-[WAClient setInterestedMessageIdentifiers:];
-[WAClient issueIOReportManagementCommand:andReply:];
-[WAClient _clearMessageStoreAndReply:queuedInvocation:];
-[WAClient submitMessage:groupType:andReply:];
-[WAClient updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:];
-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:];
-[WAClient tokenForThisClient];
-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:];
-[WAClient _submitMessage:groupType:andReply:queuedInvocation:];
-[WAClient _failInvocation:withError:];
-[WAClient getNewMessageForKey:groupType:withCopy:andReply:];
-[WAClient setQueuedInvocations:];
-[WAClient _reregister];
-[WAClient daemonConnectionValid];
-[WAClient triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:];
-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:];
-[WAClient _processManagedFault:at:andReply:queuedInvocation:];
-[WAClient blockDaemonConnection];
-[WAClient allowPurgeJSONFilesAfterSec];
-[WAClient _removeAllQueuedInvocations];
-[WAClient _startConnectionRecovery];
-[WAClient _wakeUpNotificationForThisClientReceived:];
-[WAClient replyQueue];
-[WAClient trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:];
-[WAClient interestedMessageIdentifiers];
-[WAClient propertyQueue];
-[WAClient lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:];
-[WAClient _writeWiFiAnalyticsMessageToJSONFile:metricInfo:];
-[WAClient recoveryTickBlock];
-[WAClient getNewMessageForKey:groupType:andReply:];
-[WAClient exportedRemoteInterface];
-[WAClient _getDpsStatsandReply:queuedInvocation:];
-[WAClient submitWiFiAnalyticsMessageAdvanced:];
-[WAClient deviceAnalyticsConfig];
-[WAClient connectionRecoveryStartTime];
-[WAClient _establishDaemonConnection];
-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:];
-[WAClient configuredMessageIdentifiers];
-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:];
-[WAClient wifianalyticsTmpDir];
-[WAClient identifierForThisClient];
-[WAClient getMessagesModelForGroupType:andReply:];
-[WAClient setConfiguredMessageIdentifiers:];
-[WAClient setTokenForThisClient:];
-[WAClient _connectionRecovered];
-[WAClient setRegisteredGroupTypes:];
-[WAClient _getNewMessageForKey:groupType:withCopy:andReply:queuedInvocation:];
-[WAClient setQueue:];
-[WAClient queuedInvocations];
-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:];
-[WAClient sendMemoryPressureRequestAndReply:];
-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:];
-[WAClient getDpsStatsandReply:];
-[WAClient _connectionRecoveryTick];
```
