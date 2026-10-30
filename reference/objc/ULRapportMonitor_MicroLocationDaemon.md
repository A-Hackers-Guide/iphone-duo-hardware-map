# `ULRapportMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 6 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
I _identityTypeFlags;
@"ULDarwinNotificationHelper" _notificationHelper;
@"RPClient" _client;
@"NSArray" _identities;
Q _controlFlags;
@"RPCompanionLinkClient" _companionLinkClient;
```

## Properties

```
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
@property (TI,N,V_identityTypeFlags) identityTypeFlags;
@property (T@"RPClient",&,N,V_client) client;
@property (T@"NSArray",&,N,V_identities) identities;
@property (TQ,N,V_controlFlags) controlFlags;
@property (T@"RPCompanionLinkClient",&,N,V_companionLinkClient) companionLinkClient;
```

## Instance methods

```
-[ULRapportMonitor notificationHelper];
-[ULRapportMonitor identities];
-[ULRapportMonitor stopMonitoring:];
-[ULRapportMonitor setNotificationHelper:];
-[ULRapportMonitor setControlFlags:];
-[ULRapportMonitor init];
-[ULRapportMonitor setIdentities:];
-[ULRapportMonitor setClient:];
-[ULRapportMonitor _getIdentities];
-[ULRapportMonitor companionLinkClient];
-[ULRapportMonitor controlFlags];
-[ULRapportMonitor setIdentityTypeFlags:];
-[ULRapportMonitor _startMonitoringForDevices];
-[ULRapportMonitor setCompanionLinkClient:];
-[ULRapportMonitor initWithNotificationHelper:identityTypeFlags:controlFlags:];
-[ULRapportMonitor _activateCompanionLinkClientAndSetHandlers];
-[ULRapportMonitor identityTypeFlags];
-[ULRapportMonitor startMonitoring:];
-[ULRapportMonitor _stopMonitoringForDevices];
-[ULRapportMonitor client];
-[ULRapportMonitor _startMonitoringForIdentities];
-[ULRapportMonitor _stopMonitoringForIdentities];
```
