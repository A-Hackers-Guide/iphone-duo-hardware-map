# `SNNetworkWiFiManagerInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 wifiManager;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 wifiDevice;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 wifiClientType;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 interface;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 queue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 queueGroup;
```

## Class methods

```
+[SNNetworkWiFiManagerInternal shared];
```

## Instance methods

```
-[SNNetworkWiFiManagerInternal releaseWiFiAssertion];
-[SNNetworkWiFiManagerInternal init];
-[SNNetworkWiFiManagerInternal dealloc];
-[SNNetworkWiFiManagerInternal acquireWiFiAssertionWithWifiAssertionTypeRawValue:];
-[SNNetworkWiFiManagerInternal isWiFiEnabled];
-[SNNetworkWiFiManagerInternal getWiFiRecordRepresentation];
-[SNNetworkWiFiManagerInternal isCurrentlyOnPersonalHotspot];
-[SNNetworkWiFiManagerInternal powerStateDidChangeForWiFiInterfaceWithName:];
-[SNNetworkWiFiManagerInternal registerOneShotPowerStateDidChangeForWiFiInterface:];
```
