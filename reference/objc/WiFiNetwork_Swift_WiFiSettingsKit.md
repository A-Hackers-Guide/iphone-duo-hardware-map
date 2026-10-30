# `WiFiNetwork_Swift`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP15WiFiSettingsKit25WiFiNetworkRepresentation_`
- 7 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
? name;
? displayName;
? bssid;
? macAddress;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 securityType;
d rssi;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _isPreferred;
```

## Properties

```
@property (T@"NSString",N,R) name;
@property (T@"NSString",N,C) displayName;
@property (T@"NSString",N,C) bssid;
@property (T@"NSString",N,C) macAddress;
@property (Td,N,Vrssi) rssi;
@property (TB,N) isPreferred;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Instance methods

```
-[WiFiNetwork_Swift rssi];
-[WiFiNetwork_Swift macAddress];
-[WiFiNetwork_Swift isPreferred];
-[WiFiNetwork_Swift init];
-[WiFiNetwork_Swift displayName];
-[WiFiNetwork_Swift setRssi:];
-[WiFiNetwork_Swift setDisplayName:];
-[WiFiNetwork_Swift setBssid:];
-[WiFiNetwork_Swift setMacAddress:];
-[WiFiNetwork_Swift hash];
-[WiFiNetwork_Swift description];
-[WiFiNetwork_Swift bssid];
-[WiFiNetwork_Swift isEqual:];
-[WiFiNetwork_Swift name];
-[WiFiNetwork_Swift isOpen];
-[WiFiNetwork_Swift setIsPreferred:];
-[WiFiNetwork_Swift initWithSSID:securityType:rssi:macAddress:];
-[WiFiNetwork_Swift initWithNetworkInfo:cwfNetworkProfiles:];
-[WiFiNetwork_Swift initWithNetworkProfile:];
```
