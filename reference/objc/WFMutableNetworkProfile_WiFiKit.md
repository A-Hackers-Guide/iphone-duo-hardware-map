# `WFMutableNetworkProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFNetworkProfile`
- 36 instance variables, 31 properties, 70 instance methods, 1 class methods

## Instance variables

```
B _hidden;
B _managed;
B _adhoc;
B _captive;
B _HS20Network;
B _HS20NetworkProvisioned;
B _autoJoinEnabled;
B _autoLoginEnabled;
B _isInSaveDataMode;
B _isPrivacyProxyEnabled;
B _carrierBased;
B _userProvidedPassword;
B _personalHotspot;
B _instantHotspotJoin;
B _randomMACAddressEnabled;
B _addedFromWiFiPasswordSharing;
@"NSString" _ssid;
@"NSString" _bssid;
@"NSString" _username;
@"NSString" _password;
q _securityMode;
q _securityModeExt;
@"NSDictionary" _enterpriseProfile;
@"NSArray" _certificateChain;
@"NSDictionary" _scanAttributes;
d _networkQualityResponsiveness;
@"NSDate" _networkQualityDate;
@"NSDate" _lastAssociationDate;
^{__SecIdentity=} _TLSIdentity;
@"NSString" _originatorBundleIdentifier;
@"NSString" _originatorName;
@"NSString" _HS20AccountName;
@"NSString" _HS20Badge;
@"NSString" _previousPassword;
@"NSString" _hotspotDeviceIdentifier;
@"NSString" _randomMACAddress;
```

## Properties

```
@property (T@"NSArray",&,N,V_certificateChain) certificateChain;
@property (T@"NSDictionary",&,N,V_enterpriseProfile) enterpriseProfile;
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSString",C,N,V_password) password;
@property (T@"NSString",&,N,V_bssid) bssid;
@property (T@"NSString",&,N,V_ssid) ssid;
@property (T@"NSDictionary",&,N,V_scanAttributes) scanAttributes;
@property (TB,N,GisManaged,V_managed) managed;
@property (TB,N,GisCaptive,V_captive) captive;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (TB,N,GisAutoJoinEnabled,V_autoJoinEnabled) autoJoinEnabled;
@property (TB,N,GisAutoLoginEnabled,V_autoLoginEnabled) autoLoginEnabled;
@property (TB,N,GisInSaveDataMode,V_isInSaveDataMode) isInSaveDataMode;
@property (TB,N,GisPrivacyProxyEnabled,V_isPrivacyProxyEnabled) isPrivacyProxyEnabled;
@property (Td,N,GnetworkQualityResponsiveness,V_networkQualityResponsiveness) networkQualityResponsiveness;
@property (T@"NSDate",C,N,GnetworkQualityDate,V_networkQualityDate) networkQualityDate;
@property (T@"NSDate",&,N,V_lastAssociationDate) lastAssociationDate;
@property (Tq,N,V_securityMode) securityMode;
@property (Tq,N,V_securityModeExt) securityModeExt;
@property (T^{__SecIdentity=},N,V_TLSIdentity) TLSIdentity;
@property (T@"NSString",C,N,V_originatorBundleIdentifier) originatorBundleIdentifier;
@property (T@"NSString",C,N,V_originatorName) originatorName;
@property (TB,N,GisHS20Network,V_HS20Network) HS20Network;
@property (TB,N,GisHS20NetworkProvisioned,V_HS20NetworkProvisioned) HS20NetworkProvisioned;
@property (TB,N,V_userProvidedPassword) userProvidedPassword;
@property (T@"NSString",&,N,V_previousPassword) previousPassword;
@property (TB,N,GisInstantHotspotJoin,V_instantHotspotJoin) instantHotspotJoin;
@property (T@"NSString",&,N,V_hotspotDeviceIdentifier) hotspotDeviceIdentifier;
@property (T@"NSString",C,N,V_randomMACAddress) randomMACAddress;
@property (TB,N,GisRandomMACAddressEnabled,V_randomMACAddressEnabled) randomMACAddressEnabled;
@property (TB,N,GwasAddedFromWiFiPasswordSharing,V_addedFromWiFiPasswordSharing) addedFromWiFiPasswordSharing;
```

## Class methods

```
+[WFMutableNetworkProfile mutableProfileForNetwork:];
```

## Instance methods

```
-[WFMutableNetworkProfile ssid];
-[WFMutableNetworkProfile setSsid:];
-[WFMutableNetworkProfile isManaged];
-[WFMutableNetworkProfile isPersonalHotspot];
-[WFMutableNetworkProfile setAutoJoinEnabled:];
-[WFMutableNetworkProfile setHidden:];
-[WFMutableNetworkProfile dealloc];
-[WFMutableNetworkProfile username];
-[WFMutableNetworkProfile isCarrierBased];
-[WFMutableNetworkProfile setBssid:];
-[WFMutableNetworkProfile isAdhoc];
-[WFMutableNetworkProfile isHidden];
-[WFMutableNetworkProfile initWithNetwork:];
-[WFMutableNetworkProfile isCaptive];
-[WFMutableNetworkProfile bssid];
-[WFMutableNetworkProfile setUsername:];
-[WFMutableNetworkProfile setPassword:];
-[WFMutableNetworkProfile password];
-[WFMutableNetworkProfile setManaged:];
-[WFMutableNetworkProfile originatorName];
-[WFMutableNetworkProfile securityMode];
-[WFMutableNetworkProfile setSecurityMode:];
-[WFMutableNetworkProfile certificateChain];
-[WFMutableNetworkProfile setCertificateChain:];
-[WFMutableNetworkProfile setOriginatorBundleIdentifier:];
-[WFMutableNetworkProfile removePassword];
-[WFMutableNetworkProfile originatorBundleIdentifier];
-[WFMutableNetworkProfile setCaptive:];
-[WFMutableNetworkProfile setTLSIdentity:];
-[WFMutableNetworkProfile TLSIdentity];
-[WFMutableNetworkProfile isPrivacyProxyEnabled];
-[WFMutableNetworkProfile networkQualityDate];
-[WFMutableNetworkProfile networkQualityResponsiveness];
-[WFMutableNetworkProfile setNetworkQualityDate:];
-[WFMutableNetworkProfile setNetworkQualityResponsiveness:];
-[WFMutableNetworkProfile HS20Badge];
-[WFMutableNetworkProfile securityModeExt];
-[WFMutableNetworkProfile setHS20Network:];
-[WFMutableNetworkProfile wasAddedFromWiFiPasswordSharing];
-[WFMutableNetworkProfile HS20AccountName];
-[WFMutableNetworkProfile enterpriseProfile];
-[WFMutableNetworkProfile hotspotDeviceIdentifier];
-[WFMutableNetworkProfile isAutoJoinEnabled];
-[WFMutableNetworkProfile isAutoLoginEnabled];
-[WFMutableNetworkProfile isHS20Network];
-[WFMutableNetworkProfile isHS20NetworkProvisioned];
-[WFMutableNetworkProfile isInSaveDataMode];
-[WFMutableNetworkProfile isInstantHotspotJoin];
-[WFMutableNetworkProfile isRandomMACAddressEnabled];
-[WFMutableNetworkProfile lastAssociationDate];
-[WFMutableNetworkProfile previousPassword];
-[WFMutableNetworkProfile randomMACAddress];
-[WFMutableNetworkProfile scanAttributes];
-[WFMutableNetworkProfile setAddedFromWiFiPasswordSharing:];
-[WFMutableNetworkProfile setAutoLoginEnabled:];
-[WFMutableNetworkProfile setEnterpriseProfile:];
-[WFMutableNetworkProfile setHS20NetworkProvisioned:];
-[WFMutableNetworkProfile setHotspotDeviceIdentifier:];
-[WFMutableNetworkProfile setInstantHotspotJoin:];
-[WFMutableNetworkProfile setIsInSaveDataMode:];
-[WFMutableNetworkProfile setIsPrivacyProxyEnabled:];
-[WFMutableNetworkProfile setLastAssociationDate:];
-[WFMutableNetworkProfile setOriginatorName:];
-[WFMutableNetworkProfile setPreviousPassword:];
-[WFMutableNetworkProfile setRandomMACAddress:];
-[WFMutableNetworkProfile setRandomMACAddressEnabled:];
-[WFMutableNetworkProfile setScanAttributes:];
-[WFMutableNetworkProfile setSecurityModeExt:];
-[WFMutableNetworkProfile setUserProvidedPassword:];
-[WFMutableNetworkProfile userProvidedPassword];
```
