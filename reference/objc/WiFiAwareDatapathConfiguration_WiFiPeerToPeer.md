# `WiFiAwareDatapathConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 15 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _skipInfrastructureRelayCheck;
B _pairingCachingEnabled;
I _userID;
@"WiFiAwareDiscoveryResult" _discoveryResult;
q _serviceType;
@"NSString" _passphrase;
@"NSData" _pmk;
@"NSData" _pmkID;
@"WiFiAwarePublishDatapathServiceSpecificInfo" _serviceSpecificInfo;
@"WiFiAwareInternetSharingConfiguration" _internetSharingConfiguration;
q _pairingMethod;
@"WiFiAwarePublishServiceSpecificInfo" _pairSetupServiceSpecificInfo;
q _connectionMode;
@"WiFiAwarePairingMetadata" _pairingMetadata;
@"WiFiAwareMulticastConfiguration" _multicastConfiguration;
```

## Properties

```
@property (T@"WiFiAwareDiscoveryResult",R,N,V_discoveryResult) discoveryResult;
@property (Tq,R,N,V_serviceType) serviceType;
@property (T@"NSString",R,N,V_passphrase) passphrase;
@property (T@"NSData",R,N,V_pmk) pmk;
@property (T@"NSData",R,N,V_pmkID) pmkID;
@property (T@"WiFiAwarePublishDatapathServiceSpecificInfo",C,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (T@"WiFiAwareInternetSharingConfiguration",C,N,V_internetSharingConfiguration) internetSharingConfiguration;
@property (Tq,N,V_pairingMethod) pairingMethod;
@property (TB,N,V_pairingCachingEnabled) pairingCachingEnabled;
@property (T@"WiFiAwarePublishServiceSpecificInfo",R,V_pairSetupServiceSpecificInfo) pairSetupServiceSpecificInfo;
@property (Tq,N,V_connectionMode) connectionMode;
@property (T@"WiFiAwarePairingMetadata",C,N,V_pairingMetadata) pairingMetadata;
@property (T@"WiFiAwareMulticastConfiguration",C,N,V_multicastConfiguration) multicastConfiguration;
@property (TB,N,V_skipInfrastructureRelayCheck) skipInfrastructureRelayCheck;
@property (TI,N,V_userID) userID;
```

## Class methods

```
+[WiFiAwareDatapathConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDatapathConfiguration userID];
-[WiFiAwareDatapathConfiguration setUserID:];
-[WiFiAwareDatapathConfiguration multicastConfigurationEqual:];
-[WiFiAwareDatapathConfiguration serviceSpecificInfo];
-[WiFiAwareDatapathConfiguration setServiceSpecificInfo:];
-[WiFiAwareDatapathConfiguration serviceSpecificInfoEqual:];
-[WiFiAwareDatapathConfiguration setMulticastConfiguration:];
-[WiFiAwareDatapathConfiguration encodeWithCoder:];
-[WiFiAwareDatapathConfiguration description];
-[WiFiAwareDatapathConfiguration setConnectionMode:];
-[WiFiAwareDatapathConfiguration initWithCoder:];
-[WiFiAwareDatapathConfiguration isEqual:];
-[WiFiAwareDatapathConfiguration connectionMode];
-[WiFiAwareDatapathConfiguration multicastConfiguration];
-[WiFiAwareDatapathConfiguration serviceType];
-[WiFiAwareDatapathConfiguration pairingMetadata];
-[WiFiAwareDatapathConfiguration discoveryResult];
-[WiFiAwareDatapathConfiguration setInternetSharingConfiguration:];
-[WiFiAwareDatapathConfiguration setPairingCachingEnabled:];
-[WiFiAwareDatapathConfiguration setPairingMetadata:];
-[WiFiAwareDatapathConfiguration setPairingMethod:];
-[WiFiAwareDatapathConfiguration passphrase];
-[WiFiAwareDatapathConfiguration pmk];
-[WiFiAwareDatapathConfiguration initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:multicastConfiguration:];
-[WiFiAwareDatapathConfiguration internetSharingConfiguration];
-[WiFiAwareDatapathConfiguration internetSharingEqual:];
-[WiFiAwareDatapathConfiguration pairSetupServiceSpecificInfo];
-[WiFiAwareDatapathConfiguration pairSetupServiceSpecificInfoEqual:];
-[WiFiAwareDatapathConfiguration pairingCachingEnabled];
-[WiFiAwareDatapathConfiguration pairingMethod];
-[WiFiAwareDatapathConfiguration passphraseEqual:];
-[WiFiAwareDatapathConfiguration pmkEqual:];
-[WiFiAwareDatapathConfiguration pmkID];
-[WiFiAwareDatapathConfiguration pmkIDEqual:];
-[WiFiAwareDatapathConfiguration setSkipInfrastructureRelayCheck:];
-[WiFiAwareDatapathConfiguration skipInfrastructureRelayCheck];
```
