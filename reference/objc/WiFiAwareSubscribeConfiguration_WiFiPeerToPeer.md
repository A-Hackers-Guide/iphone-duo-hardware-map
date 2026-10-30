# `WiFiAwareSubscribeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 12 instance variables, 12 properties, 37 instance methods, 1 class methods

## Instance variables

```
I _userID;
@"NSString" _serviceName;
@"NSData" _serviceSpecificInfo;
@"WiFiMACAddress" _multicastAddress;
Q _timeoutAfterSeconds;
q _authenticationType;
@"WiFiAwareFastDiscoveryConfiguration" _fastDiscoveryConfiguration;
@"NSSet" _allowedDeviceIDs;
q _discoveryMode;
@"WiFiChannel" _channelInfo;
@"NSString" _countryCode;
@"WiFiAwareMulticastConfiguration" _multicastConfiguration;
```

## Properties

```
@property (T@"NSString",R,N,V_serviceName) serviceName;
@property (T@"NSData",C,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (T@"WiFiMACAddress",C,N,V_multicastAddress) multicastAddress;
@property (TQ,N,V_timeoutAfterSeconds) timeoutAfterSeconds;
@property (Tq,N,V_authenticationType) authenticationType;
@property (T@"WiFiAwareFastDiscoveryConfiguration",C,N,V_fastDiscoveryConfiguration) fastDiscoveryConfiguration;
@property (T@"NSSet",C,N,V_allowedDeviceIDs) allowedDeviceIDs;
@property (Tq,N,V_discoveryMode) discoveryMode;
@property (T@"WiFiChannel",C,N,V_channelInfo) channelInfo;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (T@"WiFiAwareMulticastConfiguration",C,N,V_multicastConfiguration) multicastConfiguration;
@property (TI,N,V_userID) userID;
```

## Class methods

```
+[WiFiAwareSubscribeConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareSubscribeConfiguration discoveryMode];
-[WiFiAwareSubscribeConfiguration userID];
-[WiFiAwareSubscribeConfiguration multicastAddressConfigurationEqual:];
-[WiFiAwareSubscribeConfiguration setDiscoveryMode:];
-[WiFiAwareSubscribeConfiguration setUserID:];
-[WiFiAwareSubscribeConfiguration channelInfo];
-[WiFiAwareSubscribeConfiguration multicastConfigurationEqual:];
-[WiFiAwareSubscribeConfiguration setFastDiscoveryConfiguration:];
-[WiFiAwareSubscribeConfiguration setAuthenticationType:];
-[WiFiAwareSubscribeConfiguration setTimeoutAfterSeconds:];
-[WiFiAwareSubscribeConfiguration setAllowedDeviceIDs:];
-[WiFiAwareSubscribeConfiguration allowedDeviceIDs];
-[WiFiAwareSubscribeConfiguration serviceSpecificInfo];
-[WiFiAwareSubscribeConfiguration multicastAddress];
-[WiFiAwareSubscribeConfiguration setServiceSpecificInfo:];
-[WiFiAwareSubscribeConfiguration initWithServiceName:];
-[WiFiAwareSubscribeConfiguration serviceSpecificInfoEqual:];
-[WiFiAwareSubscribeConfiguration authenticationType];
-[WiFiAwareSubscribeConfiguration fastDiscoveryConfigEqual:];
-[WiFiAwareSubscribeConfiguration initWithServiceName:discoveryMode:];
-[WiFiAwareSubscribeConfiguration setMulticastConfiguration:];
-[WiFiAwareSubscribeConfiguration serviceName];
-[WiFiAwareSubscribeConfiguration countryCode];
-[WiFiAwareSubscribeConfiguration setChannelInfo:];
-[WiFiAwareSubscribeConfiguration timeoutAfterSeconds];
-[WiFiAwareSubscribeConfiguration encodeWithCoder:];
-[WiFiAwareSubscribeConfiguration initWithServiceName:serviceSpecificInfo:];
-[WiFiAwareSubscribeConfiguration description];
-[WiFiAwareSubscribeConfiguration initWithCoder:];
-[WiFiAwareSubscribeConfiguration copyWithZone:];
-[WiFiAwareSubscribeConfiguration setMulticastAddress:];
-[WiFiAwareSubscribeConfiguration isEqual:];
-[WiFiAwareSubscribeConfiguration countryCodeEqual:];
-[WiFiAwareSubscribeConfiguration multicastConfiguration];
-[WiFiAwareSubscribeConfiguration setCountryCode:];
-[WiFiAwareSubscribeConfiguration fastDiscoveryConfiguration];
-[WiFiAwareSubscribeConfiguration channelConfigurationEqual:];
```
