# `WiFiAwarePublishConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 16 instance variables, 16 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _furtherServiceDiscoveryRequired;
B _jumboServiceDiscoveryMessages;
I _userID;
@"NSString" _serviceName;
@"WiFiAwarePublishServiceSpecificInfo" _serviceSpecificInfo;
@"WiFiMACAddress" _multicastAddress;
q _authenticationType;
@"WiFiAwarePublishDatapathConfiguration" _datapathConfiguration;
@"WiFiAwareFastDiscoveryConfiguration" _fastDiscoveryConfiguration;
@"WiFiAwareInternetSharingConfiguration" _internetSharingConfiguration;
@"NSSet" _allowedDeviceIDs;
Q _timeoutAfterSeconds;
@"WiFiChannel" _channelInfo;
@"NSString" _countryCode;
@"WiFiAwareMulticastConfiguration" _multicastConfiguration;
@"WiFiAwarePairingMetadata" _pairingMetadata;
```

## Properties

```
@property (T@"NSString",R,N,V_serviceName) serviceName;
@property (T@"WiFiAwarePublishServiceSpecificInfo",C,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (TB,N,V_furtherServiceDiscoveryRequired) furtherServiceDiscoveryRequired;
@property (TB,N,V_jumboServiceDiscoveryMessages) jumboServiceDiscoveryMessages;
@property (T@"WiFiMACAddress",C,N,V_multicastAddress) multicastAddress;
@property (Tq,N,V_authenticationType) authenticationType;
@property (T@"WiFiAwarePublishDatapathConfiguration",C,N,V_datapathConfiguration) datapathConfiguration;
@property (T@"WiFiAwareFastDiscoveryConfiguration",C,N,V_fastDiscoveryConfiguration) fastDiscoveryConfiguration;
@property (T@"WiFiAwareInternetSharingConfiguration",C,N,V_internetSharingConfiguration) internetSharingConfiguration;
@property (T@"NSSet",C,N,V_allowedDeviceIDs) allowedDeviceIDs;
@property (TQ,N,V_timeoutAfterSeconds) timeoutAfterSeconds;
@property (T@"WiFiChannel",C,N,V_channelInfo) channelInfo;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (T@"WiFiAwareMulticastConfiguration",C,N,V_multicastConfiguration) multicastConfiguration;
@property (T@"WiFiAwarePairingMetadata",C,N,V_pairingMetadata) pairingMetadata;
@property (TI,N,V_userID) userID;
```

## Class methods

```
+[WiFiAwarePublishConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublishConfiguration userID];
-[WiFiAwarePublishConfiguration multicastAddressConfigurationEqual:];
-[WiFiAwarePublishConfiguration setUserID:];
-[WiFiAwarePublishConfiguration channelInfo];
-[WiFiAwarePublishConfiguration multicastConfigurationEqual:];
-[WiFiAwarePublishConfiguration setFastDiscoveryConfiguration:];
-[WiFiAwarePublishConfiguration setAuthenticationType:];
-[WiFiAwarePublishConfiguration setTimeoutAfterSeconds:];
-[WiFiAwarePublishConfiguration setAllowedDeviceIDs:];
-[WiFiAwarePublishConfiguration allowedDeviceIDs];
-[WiFiAwarePublishConfiguration serviceSpecificInfo];
-[WiFiAwarePublishConfiguration multicastAddress];
-[WiFiAwarePublishConfiguration setServiceSpecificInfo:];
-[WiFiAwarePublishConfiguration initWithServiceName:];
-[WiFiAwarePublishConfiguration serviceSpecificInfoEqual:];
-[WiFiAwarePublishConfiguration authenticationType];
-[WiFiAwarePublishConfiguration setMulticastConfiguration:];
-[WiFiAwarePublishConfiguration serviceName];
-[WiFiAwarePublishConfiguration countryCode];
-[WiFiAwarePublishConfiguration setChannelInfo:];
-[WiFiAwarePublishConfiguration timeoutAfterSeconds];
-[WiFiAwarePublishConfiguration encodeWithCoder:];
-[WiFiAwarePublishConfiguration description];
-[WiFiAwarePublishConfiguration initWithCoder:];
-[WiFiAwarePublishConfiguration copyWithZone:];
-[WiFiAwarePublishConfiguration setMulticastAddress:];
-[WiFiAwarePublishConfiguration isEqual:];
-[WiFiAwarePublishConfiguration countryCodeEqual:];
-[WiFiAwarePublishConfiguration multicastConfiguration];
-[WiFiAwarePublishConfiguration setCountryCode:];
-[WiFiAwarePublishConfiguration fastDiscoveryConfiguration];
-[WiFiAwarePublishConfiguration channelConfigurationEqual:];
-[WiFiAwarePublishConfiguration pairingMetadata];
-[WiFiAwarePublishConfiguration furtherServiceDiscoveryRequired];
-[WiFiAwarePublishConfiguration setDatapathConfiguration:];
-[WiFiAwarePublishConfiguration setInternetSharingConfiguration:];
-[WiFiAwarePublishConfiguration setPairingMetadata:];
-[WiFiAwarePublishConfiguration datapathConfiguration];
-[WiFiAwarePublishConfiguration datapathConfigurationEqual:];
-[WiFiAwarePublishConfiguration fastDiscoveryConfigurationEqual:];
-[WiFiAwarePublishConfiguration internetSharingConfiguration];
-[WiFiAwarePublishConfiguration internetSharingConfigurationEqual:];
-[WiFiAwarePublishConfiguration jumboServiceDiscoveryMessages];
-[WiFiAwarePublishConfiguration setFurtherServiceDiscoveryRequired:];
-[WiFiAwarePublishConfiguration setJumboServiceDiscoveryMessages:];
```
