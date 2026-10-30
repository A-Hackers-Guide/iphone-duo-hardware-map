# `PLIdentityServicesAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `NRDeviceMonitorDelegate`
- 15 instance variables, 19 properties, 47 instance methods, 14 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _localMessageHandler;
@"PLXPCListenerOperatorComposition" _networkStatsHandler;
@"PLXPCListenerOperatorComposition" _infraWiFiRequestHandler;
@"PLXPCListenerOperatorComposition" _localLinkTypeHandler;
@"PLXPCListenerOperatorComposition" _ipsecLinkTypeHandler;
@"PLXPCListenerOperatorComposition" _cloudMessagingHandler;
@"PLXPCListenerOperatorComposition" _idsLinkPreferenceRequestHandler;
@"PLXPCListenerOperatorComposition" _idsOutgoingPushSentListener;
@"PLXPCListenerOperatorComposition" _idsIncomingPushReceivedListener;
@"PLXPCListenerOperatorComposition" _idsSessionListener;
@"NSMutableDictionary" _previousStatsByPriority;
@"NSDate" _initialEntryDate;
@"NSDate" _lastLocalDeliveryLogDate;
@"NSMutableDictionary" _lastEntryDatePerCategory;
@"NRDeviceMonitor" _nrdm;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_localMessageHandler) localMessageHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_networkStatsHandler) networkStatsHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_infraWiFiRequestHandler) infraWiFiRequestHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_localLinkTypeHandler) localLinkTypeHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_ipsecLinkTypeHandler) ipsecLinkTypeHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_cloudMessagingHandler) cloudMessagingHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_idsLinkPreferenceRequestHandler) idsLinkPreferenceRequestHandler;
@property (T@"PLXPCListenerOperatorComposition",&,V_idsOutgoingPushSentListener) idsOutgoingPushSentListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_idsIncomingPushReceivedListener) idsIncomingPushReceivedListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_idsSessionListener) idsSessionListener;
@property (T@"NSMutableDictionary",&,V_previousStatsByPriority) previousStatsByPriority;
@property (T@"NSDate",&,V_initialEntryDate) initialEntryDate;
@property (T@"NSDate",&,V_lastLocalDeliveryLogDate) lastLocalDeliveryLogDate;
@property (T@"NSMutableDictionary",&,V_lastEntryDatePerCategory) lastEntryDatePerCategory;
@property (T@"NRDeviceMonitor",&,V_nrdm) nrdm;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLIdentityServicesAgent entryEventIntervalDefinitions];
+[PLIdentityServicesAgent entryEventPointDefinitions];
+[PLIdentityServicesAgent entryEventForwardDefinitions];
+[PLIdentityServicesAgent load];
+[PLIdentityServicesAgent entryDefinitionIDSMessageStats];
+[PLIdentityServicesAgent entryDefinitionLocalInfraWiFiRequests];
+[PLIdentityServicesAgent entryEventPointDefinitionIDSIncomingPushReceived];
+[PLIdentityServicesAgent entryDefinitionCloudMessaging];
+[PLIdentityServicesAgent entryEventPointDefinitionIDSLocalMessage];
+[PLIdentityServicesAgent entryDefinitionLocalLink];
+[PLIdentityServicesAgent entryEventPointDefinitionIDSLinkPreferenceRequest];
+[PLIdentityServicesAgent entryDefinitionSession];
+[PLIdentityServicesAgent entryDefinitionIDSSocketStats];
+[PLIdentityServicesAgent entryEventPointDefinitionIDSOutgoingPushSent];
```

## Instance methods

```
-[PLIdentityServicesAgent init];
-[PLIdentityServicesAgent initOperatorDependancies];
-[PLIdentityServicesAgent initTaskOperatorDependancies];
-[PLIdentityServicesAgent deviceLinkTypeDidChange:linkType:];
-[PLIdentityServicesAgent idsLinkPreferenceRequestHandler];
-[PLIdentityServicesAgent setIdsOutgoingPushSentListener:];
-[PLIdentityServicesAgent idsIncomingPushReceivedListener];
-[PLIdentityServicesAgent notifyLinkType:];
-[PLIdentityServicesAgent cloudMessagingHandler];
-[PLIdentityServicesAgent createBTAccountingEvents:];
-[PLIdentityServicesAgent createIDSAccountingEventsWithEntries:];
-[PLIdentityServicesAgent idsOutgoingPushSentListener];
-[PLIdentityServicesAgent idsSessionListener];
-[PLIdentityServicesAgent infraWiFiRequestHandler];
-[PLIdentityServicesAgent initialEntryDate];
-[PLIdentityServicesAgent ipsecLinkTypeHandler];
-[PLIdentityServicesAgent lastEntryDatePerCategory];
-[PLIdentityServicesAgent lastLocalDeliveryLogDate];
-[PLIdentityServicesAgent localLinkTypeHandler];
-[PLIdentityServicesAgent localMessageHandler];
-[PLIdentityServicesAgent logCloudMessaging:];
-[PLIdentityServicesAgent logIDSIncomingPushReceived:];
-[PLIdentityServicesAgent logIDSLinkPreference:];
-[PLIdentityServicesAgent logIDSNetworkEntries:];
-[PLIdentityServicesAgent logIDSOutgoingPushSent:];
-[PLIdentityServicesAgent logIDSSession:];
-[PLIdentityServicesAgent logLocalInfraWiFiFrequests:];
-[PLIdentityServicesAgent logLocalLinkType:];
-[PLIdentityServicesAgent logLocalMessageTopic:];
-[PLIdentityServicesAgent networkStatsHandler];
-[PLIdentityServicesAgent nrdm];
-[PLIdentityServicesAgent previousStatsByPriority];
-[PLIdentityServicesAgent setCloudMessagingHandler:];
-[PLIdentityServicesAgent setCurrentLinkType];
-[PLIdentityServicesAgent setIdsIncomingPushReceivedListener:];
-[PLIdentityServicesAgent setIdsLinkPreferenceRequestHandler:];
-[PLIdentityServicesAgent setIdsSessionListener:];
-[PLIdentityServicesAgent setInfraWiFiRequestHandler:];
-[PLIdentityServicesAgent setInitialEntryDate:];
-[PLIdentityServicesAgent setIpsecLinkTypeHandler:];
-[PLIdentityServicesAgent setLastEntryDatePerCategory:];
-[PLIdentityServicesAgent setLastLocalDeliveryLogDate:];
-[PLIdentityServicesAgent setLocalLinkTypeHandler:];
-[PLIdentityServicesAgent setLocalMessageHandler:];
-[PLIdentityServicesAgent setNetworkStatsHandler:];
-[PLIdentityServicesAgent setNrdm:];
-[PLIdentityServicesAgent setPreviousStatsByPriority:];
```
