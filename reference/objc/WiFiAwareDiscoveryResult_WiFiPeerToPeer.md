# `WiFiAwareDiscoveryResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 16 instance variables, 15 properties, 26 instance methods, 1 class methods

## Instance variables

```
q _datapathCipherSuite;
q _fsdFunction;
C _subscribeID;
C _publishID;
B _datapathSupported;
B _pairSetupRequired;
B _autoPairable;
@"NSString" _serviceName;
@"WiFiAwarePublishServiceSpecificInfo" _serviceSpecificInfo;
@"WiFiMACAddress" _publisherAddress;
q _rssi;
@"WiFiAwarePairingConfiguration" _pairingConfiguration;
@"NSUUID" _pairedUUID;
@"NSString" _pairedDeviceName;
q _signature;
@"NSDictionary" _performanceForecast;
```

## Properties

```
@property (T@"NSString",R,N,V_serviceName) serviceName;
@property (T@"WiFiAwarePublishServiceSpecificInfo",R,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (TC,R,N,V_publishID) publishID;
@property (T@"WiFiMACAddress",R,N,V_publisherAddress) publisherAddress;
@property (TB,R,N,V_datapathSupported) datapathSupported;
@property (TB,R,N) datapathSecurityRequired;
@property (TB,R,N) furtherServiceDiscoveryRequired;
@property (Tq,R,N,V_rssi) rssi;
@property (TB,R,N,V_pairSetupRequired) pairSetupRequired;
@property (T@"WiFiAwarePairingConfiguration",R,N,V_pairingConfiguration) pairingConfiguration;
@property (T@"NSUUID",R,N,V_pairedUUID) pairedUUID;
@property (T@"NSString",R,N,V_pairedDeviceName) pairedDeviceName;
@property (Tq,R,N,V_signature) signature;
@property (TB,R,N,V_autoPairable) autoPairable;
@property (T@"NSDictionary",R,N,V_performanceForecast) performanceForecast;
```

## Class methods

```
+[WiFiAwareDiscoveryResult supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDiscoveryResult rssi];
-[WiFiAwareDiscoveryResult serviceSpecificInfo];
-[WiFiAwareDiscoveryResult pairedDeviceName];
-[WiFiAwareDiscoveryResult signature];
-[WiFiAwareDiscoveryResult serviceSpecificInfoEqual:];
-[WiFiAwareDiscoveryResult serviceName];
-[WiFiAwareDiscoveryResult encodeWithCoder:];
-[WiFiAwareDiscoveryResult description];
-[WiFiAwareDiscoveryResult initWithCoder:];
-[WiFiAwareDiscoveryResult copyWithZone:];
-[WiFiAwareDiscoveryResult isEqual:];
-[WiFiAwareDiscoveryResult furtherServiceDiscoveryRequired];
-[WiFiAwareDiscoveryResult autoPairable];
-[WiFiAwareDiscoveryResult datapathSecurityRequired];
-[WiFiAwareDiscoveryResult datapathSupported];
-[WiFiAwareDiscoveryResult pairedUUID];
-[WiFiAwareDiscoveryResult publishID];
-[WiFiAwareDiscoveryResult publisherAddress];
-[WiFiAwareDiscoveryResult pairingConfiguration];
-[WiFiAwareDiscoveryResult performanceForecast];
-[WiFiAwareDiscoveryResult pairSetupRequired];
-[WiFiAwareDiscoveryResult datapathCipherSuite];
-[WiFiAwareDiscoveryResult fsdFunction];
-[WiFiAwareDiscoveryResult fsdFunctionString];
-[WiFiAwareDiscoveryResult initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:autoPairable:performanceForecast:];
-[WiFiAwareDiscoveryResult subscribeID];
```
