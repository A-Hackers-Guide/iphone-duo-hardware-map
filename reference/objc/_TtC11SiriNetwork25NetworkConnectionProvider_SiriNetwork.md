# `_TtC11SiriNetwork25NetworkConnectionProvider`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 25 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
SiriNetwork.NetworkConnectionProtocol ? connection;
SiriNetwork.ConnectionMetrics connectionMetrics;
SiriNetwork.NetworkManager ? networkManager;
SiriNetwork.ConnectionProviderDelegate ? delegate;
SiriNetwork.ConnectionProviderState connectionProviderState;
SiriNetwork.ConnectionConfiguration connectionConfiguration;
DispatchQueue connectionQueue;
Swift.Result _$syyt -> SiriNetwork.NetworkConnectionError _$sGcSg openCompletion;
_$sSu readWriteCounter;
_$sSu betterPathAvailableNotificationMachTime;
Swift.Bool betterPathAvailable;
Swift.Bool scopeToWiFiOnly;
Swift.Bool isViable;
Swift.Bool isCancelled;
Swift.Bool isMPTCP;
Swift.Bool wasConnected;
Swift.Error ? mostRecentErrorFromConnection;
(objc_protocol 0x2adeddcf0) ? openTimeoutTimer;
(objc_protocol 0x2adeddcf0) ? openSlowTimer;
(objc_protocol 0x2adeddcf0) ? staleConnectionTimer;
(objc_protocol 0x2adeddcf0) ? connectionUnviableTimer;
SiriNetwork.NetworkAnalytics networkAnalytics;
SiriNetwork.NetworkConnectionProvider.StateUpdateHandler ? stateUpdateHandler;
SiriNetwork.NetworkConnectionProvider.ViabilityUpdateHandler ? viabilityUpdateHandler;
SiriNetwork.NetworkConnectionProvider.BetterPathUpdateHandler ? betterPathUpdateHandler;
```
