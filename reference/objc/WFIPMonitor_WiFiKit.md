# `WFIPMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 59 instance methods, 0 class methods

## Instance variables

```
B _isMonitoring;
@"_WFIPMonitorObserver" _dynamicStoreInfo;
@"NSString" _serviceID;
@"NSString" _interfaceName;
^{__SCDynamicStore=} _storeRef;
^{__SCPreferences=} _prefsRef;
^{__SCDynamicStore=} _networkServiceStore;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _bundleIdentifier;
```

## Properties

```
@property (T@"NSString",C,N,V_serviceID) serviceID;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T^{__SCDynamicStore=},V_storeRef) storeRef;
@property (T^{__SCPreferences=},V_prefsRef) prefsRef;
@property (T^{__SCDynamicStore=},V_networkServiceStore) networkServiceStore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
```

## Instance methods

```
-[WFIPMonitor ipv4Addresses];
-[WFIPMonitor serviceID];
-[WFIPMonitor init];
-[WFIPMonitor hasValidIPAddress];
-[WFIPMonitor setInterfaceName:];
-[WFIPMonitor dealloc];
-[WFIPMonitor bundleIdentifier];
-[WFIPMonitor interfaceName];
-[WFIPMonitor queue];
-[WFIPMonitor dnsSearchDomains];
-[WFIPMonitor ipv6Addresses];
-[WFIPMonitor initWithInterfaceName:];
-[WFIPMonitor setBundleIdentifier:];
-[WFIPMonitor __proxiesSetupConfig];
-[WFIPMonitor setQueue:];
-[WFIPMonitor setServiceID:];
-[WFIPMonitor dnsServerAddresses];
-[WFIPMonitor httpProxyServer];
-[WFIPMonitor ipv4SubnetMasks];
-[WFIPMonitor DHCPLeaseExpirationDate];
-[WFIPMonitor __wifiServiceID];
-[WFIPMonitor __dhcpInfo];
-[WFIPMonitor __dnsSetupConfig];
-[WFIPMonitor __dnsStateConfig];
-[WFIPMonitor __ipv4InterfaceStateConfig];
-[WFIPMonitor __ipv4SetupConfig];
-[WFIPMonitor __ipv4StateConfig];
-[WFIPMonitor __ipv6SetupConfig];
-[WFIPMonitor __ipv6StateConfig];
-[WFIPMonitor __isIPConfigurationPrimaryForProperty:];
-[WFIPMonitor _postChangesNotification:];
-[WFIPMonitor dnsDomainName];
-[WFIPMonitor globalProxyIsEnabled];
-[WFIPMonitor hasValidIPv4Address];
-[WFIPMonitor hasValidIPv6Address];
-[WFIPMonitor httpProxyAutoConfigURL];
-[WFIPMonitor httpProxyAutoConfigured];
-[WFIPMonitor httpProxyIsAuthenticated];
-[WFIPMonitor httpProxyPort];
-[WFIPMonitor httpProxyUsername];
-[WFIPMonitor ipv4ConfigMethod];
-[WFIPMonitor ipv4DHCPClientID];
-[WFIPMonitor ipv4Router];
-[WFIPMonitor ipv6ConfigMethod];
-[WFIPMonitor ipv6PrefixLengths];
-[WFIPMonitor ipv6Router];
-[WFIPMonitor isIPv4Primary];
-[WFIPMonitor isIPv6Primary];
-[WFIPMonitor isUsingCustomDNSSettings];
-[WFIPMonitor isUsingCustomProxySetting];
-[WFIPMonitor monitorNetworkServiceID:];
-[WFIPMonitor networkServiceStore];
-[WFIPMonitor personalHotspotHasClients];
-[WFIPMonitor prefsRef];
-[WFIPMonitor renewLease];
-[WFIPMonitor setNetworkServiceStore:];
-[WFIPMonitor setPrefsRef:];
-[WFIPMonitor setStoreRef:];
-[WFIPMonitor storeRef];
```
