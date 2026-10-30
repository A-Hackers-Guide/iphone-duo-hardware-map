# `SBSystemStatusWifiDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBWiFiManager" _wifiManager;
B _queue_wifiActive;
B _queue_fallingBackToCellular;
@"NSObject<OS_dispatch_queue>" _updateQueue;
@"STWifiStatusDomainPublisher" _wifiDataPublisher;
```

## Properties

```
@property (T@"STWifiStatusDomainPublisher",R,N,V_wifiDataPublisher) wifiDataPublisher;
@property (TB,N,GisWifiActive,V_queue_wifiActive) wifiActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemStatusWifiDataProvider isWifiActive];
-[SBSystemStatusWifiDataProvider _registerForNotifications];
-[SBSystemStatusWifiDataProvider dealloc];
-[SBSystemStatusWifiDataProvider setWifiActive:];
-[SBSystemStatusWifiDataProvider invalidate];
-[SBSystemStatusWifiDataProvider _updateData];
-[SBSystemStatusWifiDataProvider _queue_updateData];
-[SBSystemStatusWifiDataProvider _queue_updateWifiActive];
-[SBSystemStatusWifiDataProvider _updateWifiActive];
-[SBSystemStatusWifiDataProvider initWithServerHandle:wifiManager:];
-[SBSystemStatusWifiDataProvider wifiDataPublisher];
```
