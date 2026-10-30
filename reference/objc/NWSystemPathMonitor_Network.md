# `NWSystemPathMonitor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _wifiPrimary;
B _ethernetPrimary;
B _vpnActive;
B _interfaceInUse;
i _vpnNotifyToken;
@"NWMonitor" _vpnMonitor;
@"NWPathEvaluator" _primaryEvaluator;
@"RBSProcessMonitor" _processMonitor;
@"NSMutableDictionary" _perAppVPNEvaluators;
@"NSObject<OS_dispatch_source>" _smoothingTimer;
```

## Properties

```
@property (T@"NWMonitor",&,V_vpnMonitor) vpnMonitor;
@property (T@"NWPathEvaluator",&,V_primaryEvaluator) primaryEvaluator;
@property (Ti,V_vpnNotifyToken) vpnNotifyToken;
@property (T@"RBSProcessMonitor",&,V_processMonitor) processMonitor;
@property (T@"NSMutableDictionary",&,V_perAppVPNEvaluators) perAppVPNEvaluators;
@property (T@"NSObject<OS_dispatch_source>",&,V_smoothingTimer) smoothingTimer;
@property (TB,N,GisVPNActive,V_vpnActive) vpnActive;
@property (TB,N,GisWiFiPrimary,V_wifiPrimary) wifiPrimary;
@property (TB,N,GisEthernetPrimary,V_ethernetPrimary) ethernetPrimary;
@property (TB,N,V_interfaceInUse) interfaceInUse;
```

## Class methods

```
+[NWSystemPathMonitor sharedSystemPathMonitor];
```

## Instance methods

```
-[NWSystemPathMonitor vpnNotifyToken];
-[NWSystemPathMonitor setPrimaryEvaluator:];
-[NWSystemPathMonitor stateUpdated:forProcess:];
-[NWSystemPathMonitor observeValueForKeyPath:ofObject:change:context:];
-[NWSystemPathMonitor init];
-[NWSystemPathMonitor processMonitor];
-[NWSystemPathMonitor isEthernetPrimary];
-[NWSystemPathMonitor dealloc];
-[NWSystemPathMonitor startWatchingApplicationStates];
-[NWSystemPathMonitor vpnMonitor];
-[NWSystemPathMonitor stopWatchingApplicationStates];
-[NWSystemPathMonitor setSmoothingTimer:];
-[NWSystemPathMonitor updateFlags];
-[NWSystemPathMonitor isWiFiPrimary];
-[NWSystemPathMonitor setInterfaceInUse:];
-[NWSystemPathMonitor smoothingTimer];
-[NWSystemPathMonitor eventFired];
-[NWSystemPathMonitor registerForVPNNotifications];
-[NWSystemPathMonitor setVpnMonitor:];
-[NWSystemPathMonitor perAppVPNEvaluators];
-[NWSystemPathMonitor isVPNActive];
-[NWSystemPathMonitor setProcessMonitor:];
-[NWSystemPathMonitor setVpnNotifyToken:];
-[NWSystemPathMonitor primaryEvaluator];
-[NWSystemPathMonitor setEthernetPrimary:];
-[NWSystemPathMonitor interfaceInUse];
-[NWSystemPathMonitor setVpnActive:];
-[NWSystemPathMonitor updateVPNMonitor];
-[NWSystemPathMonitor setPerAppVPNEvaluators:];
-[NWSystemPathMonitor setWifiPrimary:];
```
