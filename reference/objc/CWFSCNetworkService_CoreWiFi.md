# `CWFSCNetworkService`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{__SCDynamicStore=} _storeRef;
^{__SCPreferences=} _prefsRef;
B _isMonitoringEvents;
@"NSString" _serviceID;
@"NSString" _serviceName;
@? _eventHandler;
@"NSString" _interfaceName;
```

## Properties

```
@property (T@?,C,V_eventHandler) eventHandler;
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (T@"NSString",R,C,N) serviceID;
```

## Instance methods

```
-[CWFSCNetworkService IPv4ARPResolvedHardwareAddress];
-[CWFSCNetworkService IPv4NetworkSignature];
-[CWFSCNetworkService IPv4SubnetMasks];
-[CWFSCNetworkService IPv4Addresses];
-[CWFSCNetworkService DHCPLeaseExpirationTimestamp];
-[CWFSCNetworkService IPv6Addresses];
-[CWFSCNetworkService DNSServerAddresses];
-[CWFSCNetworkService IPv6NetworkSignature];
-[CWFSCNetworkService IPv4ARPResolvedIPAddress];
-[CWFSCNetworkService DHCPServerID];
-[CWFSCNetworkService DHCPv6ServerID];
-[CWFSCNetworkService eventHandler];
-[CWFSCNetworkService setEventHandler:];
-[CWFSCNetworkService startEventMonitoring];
-[CWFSCNetworkService serviceID];
-[CWFSCNetworkService __IPv4SetupConfig];
-[CWFSCNetworkService __IPv4StateConfig];
-[CWFSCNetworkService isMonitoringEvents];
-[CWFSCNetworkService init];
-[CWFSCNetworkService IPv6Router];
-[CWFSCNetworkService dealloc];
-[CWFSCNetworkService refreshServiceID];
-[CWFSCNetworkService stopEventMonitoring];
-[CWFSCNetworkService interfaceName];
-[CWFSCNetworkService __refreshServiceID];
-[CWFSCNetworkService __DHCPStateConfig];
-[CWFSCNetworkService DNSDomainName];
-[CWFSCNetworkService __refreshNotificationKeys];
-[CWFSCNetworkService DHCPLeaseStartTimestamp];
-[CWFSCNetworkService serviceName];
-[CWFSCNetworkService __DNSSetupConfig];
-[CWFSCNetworkService __updateServiceID];
-[CWFSCNetworkService __IPv6SetupConfig];
-[CWFSCNetworkService IPv6ConfigMethod];
-[CWFSCNetworkService initWithInterfaceName:];
-[CWFSCNetworkService __DHCPInfo];
-[CWFSCNetworkService __IPv6StateConfig];
-[CWFSCNetworkService IPv4Router];
-[CWFSCNetworkService IPv4ConfigMethod];
-[CWFSCNetworkService __DNSStateConfig];
-[CWFSCNetworkService __serviceStateConfig];
-[CWFSCNetworkService __proxiesSetupConfig];
-[CWFSCNetworkService __DHCPv6StateConfig];
```
