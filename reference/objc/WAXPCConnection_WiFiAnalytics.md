# `WAXPCConnection`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"<WAXPCConnectionDelegate>" _delegate;
@"NSXPCConnection" _connection;
@"NSString" _token;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSString",&,N,V_token) token;
@property (T@"<WAXPCConnectionDelegate>",W,N,V_delegate) delegate;
@property (T@"NSXPCConnection",R,N,V_connection) connection;
```

## Instance methods

```
-[WAXPCConnection initWithXPCConnection:];
-[WAXPCConnection lqmCrashTracerNotifyForInterfaceWithName:andReply:];
-[WAXPCConnection setDeviceAnalyticsConfiguration:andReply:];
-[WAXPCConnection triggerQueryForNWActivity:andReply:];
-[WAXPCConnection signalPotentialNewIORChannelsAndReply:];
-[WAXPCConnection triggerQueryForNWActivityWithPeers:andReply:];
-[WAXPCConnection processManagedFault:at:andReply:];
-[WAXPCConnection registerMessageGroup:andReply:];
-[WAXPCConnection queue];
-[WAXPCConnection getDeviceAnalyticsConfigurationAndReply:];
-[WAXPCConnection triggerDeviceAnalyticsStoreMigrationAndReply:];
-[WAXPCConnection setDelegate:];
-[WAXPCConnection getUsageStatsandReply:];
-[WAXPCConnection clearMessageStoreAndReply:];
-[WAXPCConnection killDaemonAndReply:];
-[WAXPCConnection issueIOReportManagementCommand:andReply:];
-[WAXPCConnection connection];
-[WAXPCConnection submitMessage:groupType:andReply:];
-[WAXPCConnection updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:];
-[WAXPCConnection delegate];
-[WAXPCConnection getNewMessageForKey:groupType:withCopy:andReply:];
-[WAXPCConnection triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:];
-[WAXPCConnection token];
-[WAXPCConnection trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:];
-[WAXPCConnection setToken:];
-[WAXPCConnection lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:];
-[WAXPCConnection getNewMessageForKey:groupType:andReply:];
-[WAXPCConnection updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:];
-[WAXPCConnection getMessagesModelForGroupType:andReply:];
-[WAXPCConnection setQueue:];
-[WAXPCConnection convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:];
-[WAXPCConnection sendMemoryPressureRequestAndReply:];
-[WAXPCConnection getDpsStatsandReply:];
-[WAXPCConnection establishConnectionWithToken:andReply:];
```
