# `CWFSCNetworkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{__SCDynamicStore=} _storeRef;
B _isMonitoringEvents;
@? _eventHandler;
```

## Properties

```
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFSCNetworkConfiguration IPv4SubnetMasks];
-[CWFSCNetworkConfiguration IPv4Addresses];
-[CWFSCNetworkConfiguration __startEventMonitoring];
-[CWFSCNetworkConfiguration IPv6Addresses];
-[CWFSCNetworkConfiguration DNSServerAddresses];
-[CWFSCNetworkConfiguration eventHandler];
-[CWFSCNetworkConfiguration __IPv6GlobalStateConfig];
-[CWFSCNetworkConfiguration __IPv4GlobalStateConfig];
-[CWFSCNetworkConfiguration setEventHandler:];
-[CWFSCNetworkConfiguration startEventMonitoring];
-[CWFSCNetworkConfiguration IPv6ServiceID];
-[CWFSCNetworkConfiguration isMonitoringEvents];
-[CWFSCNetworkConfiguration init];
-[CWFSCNetworkConfiguration __networkInterfaceStateConfig];
-[CWFSCNetworkConfiguration IPv6Router];
-[CWFSCNetworkConfiguration __nameForServiceWithID:];
-[CWFSCNetworkConfiguration dealloc];
-[CWFSCNetworkConfiguration stopEventMonitoring];
-[CWFSCNetworkConfiguration DNSDomainName];
-[CWFSCNetworkConfiguration IPv6PrefixLengths];
-[CWFSCNetworkConfiguration __IPv6StateConfigForServiceID:];
-[CWFSCNetworkConfiguration IEEE80211NetworkInterfacesNames];
-[CWFSCNetworkConfiguration IPv4ServiceName];
-[CWFSCNetworkConfiguration IPv4ServiceID];
-[CWFSCNetworkConfiguration DNSSearchDomains];
-[CWFSCNetworkConfiguration __IPv4StateConfigForServiceID:];
-[CWFSCNetworkConfiguration __IPv4SetupConfigForServiceID:];
-[CWFSCNetworkConfiguration __isIEEE80211NetworkInterfaceName:];
-[CWFSCNetworkConfiguration __IPv6SetupConfigForServiceID:];
-[CWFSCNetworkConfiguration networkInterfaceNames];
-[CWFSCNetworkConfiguration __DNSGlobalStateConfig];
-[CWFSCNetworkConfiguration IPv4Router];
-[CWFSCNetworkConfiguration IPv6ServiceName];
-[CWFSCNetworkConfiguration IPv6InterfaceName];
-[CWFSCNetworkConfiguration IPv4InterfaceName];
```
