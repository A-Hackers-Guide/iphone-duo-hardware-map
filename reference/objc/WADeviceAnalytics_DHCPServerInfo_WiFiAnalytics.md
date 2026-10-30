# `WADeviceAnalytics_DHCPServerInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _ipv4networkSignature;
@"NSString" _ipv6networkSignature;
```

## Properties

```
@property (T@"NSString",&,N,V_ipv4networkSignature) ipv4networkSignature;
@property (T@"NSString",&,N,V_ipv6networkSignature) ipv6networkSignature;
```

## Class methods

```
+[WADeviceAnalytics_DHCPServerInfo dhcpServerInfoWithv4Signature:v6Signature:];
```

## Instance methods

```
-[WADeviceAnalytics_DHCPServerInfo hash];
-[WADeviceAnalytics_DHCPServerInfo description];
-[WADeviceAnalytics_DHCPServerInfo copyWithZone:];
-[WADeviceAnalytics_DHCPServerInfo isEqual:];
-[WADeviceAnalytics_DHCPServerInfo ipv4networkSignature];
-[WADeviceAnalytics_DHCPServerInfo ipv6networkSignature];
-[WADeviceAnalytics_DHCPServerInfo setIpv4networkSignature:];
-[WADeviceAnalytics_DHCPServerInfo setIpv6networkSignature:];
```
