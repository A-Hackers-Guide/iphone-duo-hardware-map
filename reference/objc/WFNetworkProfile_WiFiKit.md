# `WFNetworkProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`
- 47 instance variables, 49 properties, 101 instance methods, 1 class methods

## Instance variables

```
B _hidden;
B _managed;
B _captive;
B _adhoc;
B _HS20Network;
B _HS20NetworkProvisioned;
B _autoJoinEnabled;
B _autoLoginEnabled;
B _carPlay;
B _isInSaveDataMode;
B _isPrivacyProxyEnabled;
B _carrierBased;
B _personalHotspot;
B _profileBased;
B _addedFromWiFiPasswordSharing;
B _canExposeIMSI;
B _instantHotspotJoin;
B _randomMACAddressEnabled;
B _DNSHeuristicsFiltered;
B _fetchedPassword;
B _requiresPassword;
^{__SecIdentity=} _TLSIdentity;
@"NSString" _password;
@"NSDictionary" _scanAttributes;
@"NSArray" _certificateChain;
@"NSDictionary" _enterpriseProfile;
@"NSString" _username;
@"NSString" _bssid;
@"NSString" _ssid;
@"NSString" _HS20AccountName;
@"NSString" _HS20Badge;
d _networkQualityResponsiveness;
@"NSDate" _networkQualityDate;
q _carPlayType;
@"NSString" _carPlayUUID;
@"NSString" _policyUUID;
q _securityMode;
q _securityModeExt;
@"NSDate" _addedDate;
@"NSDate" _lastAutoJoinDate;
Q _originator;
@"NSString" _originatorBundleIdentifier;
@"NSString" _originatorName;
@"NSString" _previousPassword;
@"NSString" _hotspotDeviceIdentifier;
@"NSString" _randomMACAddress;
@"NSString" _HS20OperatorName;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_enterpriseProfile) enterpriseProfile;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (T@"NSString",&,N,V_bssid) bssid;
@property (T@"NSString",&,N,V_ssid) ssid;
@property (Tq,N,V_securityMode) securityMode;
@property (Tq,N,V_securityModeExt) securityModeExt;
@property (T@"NSDictionary",&,N,V_scanAttributes) scanAttributes;
@property (TB,N,GisAdhoc,V_adhoc) adhoc;
@property (TB,N,GisCaptive,V_captive) captive;
@property (TB,N,GisHS20Network,V_HS20Network) HS20Network;
@property (TB,N,GisAutoJoinEnabled,V_autoJoinEnabled) autoJoinEnabled;
@property (TB,N,GisCarPlay,V_carPlay) carPlay;
@property (Tq,N,V_carPlayType) carPlayType;
@property (T@"NSString",C,N,V_carPlayUUID) carPlayUUID;
@property (T@"NSString",C,N,V_policyUUID) policyUUID;
@property (T@"NSString",C,N,V_originatorBundleIdentifier) originatorBundleIdentifier;
@property (T@"NSString",C,N,V_originatorName) originatorName;
@property (TB,N,GisHS20NetworkProvisioned,V_HS20NetworkProvisioned) HS20NetworkProvisioned;
@property (TB,N,GisCarrierBased,V_carrierBased) carrierBased;
@property (TB,N,GisPersonalHotspot,V_personalHotspot) personalHotspot;
@property (TB,N,GisProfileBased,V_profileBased) profileBased;
@property (TB,N,GwasAddedFromWiFiPasswordSharing,V_addedFromWiFiPasswordSharing) addedFromWiFiPasswordSharing;
@property (T@"NSString",&,N,V_HS20AccountName) HS20AccountName;
@property (T@"NSString",&,N,V_HS20Badge) HS20Badge;
@property (TB,N,V_canExposeIMSI) canExposeIMSI;
@property (T^{__SecIdentity=},N,V_TLSIdentity) TLSIdentity;
@property (TB,N,V_fetchedPassword) fetchedPassword;
@property (TB,N,V_requiresPassword) requiresPassword;
@property (TB,N,GisInstantHotspotJoin,V_instantHotspotJoin) instantHotspotJoin;
@property (T@"NSString",C,N,V_randomMACAddress) randomMACAddress;
@property (TB,N,GisRandomMACAddressEnabled,V_randomMACAddressEnabled) randomMACAddressEnabled;
@property (TB,N,GisDNSHeuristicsFiltered,V_DNSHeuristicsFiltered) DNSHeuristicsFiltered;
@property (T@"NSString",C,N,V_HS20OperatorName) HS20OperatorName;
@property (T@"NSArray",R,N,V_certificateChain) certificateChain;
@property (T@"NSString",R,C,N,V_username) username;
@property (T@"NSString",R,C,N,V_password) password;
@property (TB,R,N,GisManaged,V_managed) managed;
@property (TB,R,N,GisAutoLoginEnabled,V_autoLoginEnabled) autoLoginEnabled;
@property (TB,R,N,GisInSaveDataMode,V_isInSaveDataMode) isInSaveDataMode;
@property (TB,R,N,GisPrivacyProxyEnabled,V_isPrivacyProxyEnabled) isPrivacyProxyEnabled;
@property (Td,R,N,GnetworkQualityResponsiveness,V_networkQualityResponsiveness) networkQualityResponsiveness;
@property (T@"NSDate",R,C,N,GnetworkQualityDate,V_networkQualityDate) networkQualityDate;
@property (TB,R,N) requiresUsernameAndPassword;
@property (T@"NSDate",R,N,V_addedDate) addedDate;
@property (T@"NSDate",R,N,V_lastAutoJoinDate) lastAutoJoinDate;
@property (TQ,R,N,V_originator) originator;
@property (TB,R,N) userProvidedPassword;
@property (T@"NSString",R,N,V_previousPassword) previousPassword;
@property (T@"NSString",&,N,V_hotspotDeviceIdentifier) hotspotDeviceIdentifier;
```

## Class methods

```
+[WFNetworkProfile networkProfileRepresentSameNetwork:toNetworkProfile:];
```

## Instance methods

```
-[WFNetworkProfile ssid];
-[WFNetworkProfile setSsid:];
-[WFNetworkProfile isEnterprise];
-[WFNetworkProfile isManaged];
-[WFNetworkProfile isPersonalHotspot];
-[WFNetworkProfile mutableCopyWithZone:];
-[WFNetworkProfile setAutoJoinEnabled:];
-[WFNetworkProfile setHidden:];
-[WFNetworkProfile addedDate];
-[WFNetworkProfile dealloc];
-[WFNetworkProfile username];
-[WFNetworkProfile isCarrierBased];
-[WFNetworkProfile setBssid:];
-[WFNetworkProfile isCarPlay];
-[WFNetworkProfile isAdhoc];
-[WFNetworkProfile requiresPassword];
-[WFNetworkProfile isHidden];
-[WFNetworkProfile setRequiresPassword:];
-[WFNetworkProfile initWithNetwork:];
-[WFNetworkProfile setCarPlay:];
-[WFNetworkProfile isCaptive];
-[WFNetworkProfile hash];
-[WFNetworkProfile description];
-[WFNetworkProfile bssid];
-[WFNetworkProfile isEqual:];
-[WFNetworkProfile password];
-[WFNetworkProfile originator];
-[WFNetworkProfile originatorName];
-[WFNetworkProfile securityMode];
-[WFNetworkProfile setSecurityMode:];
-[WFNetworkProfile certificateChain];
-[WFNetworkProfile setOriginatorBundleIdentifier:];
-[WFNetworkProfile originatorBundleIdentifier];
-[WFNetworkProfile isProfileBased];
-[WFNetworkProfile setCaptive:];
-[WFNetworkProfile setTLSIdentity:];
-[WFNetworkProfile TLSIdentity];
-[WFNetworkProfile isPrivacyProxyEnabled];
-[WFNetworkProfile networkQualityDate];
-[WFNetworkProfile networkQualityResponsiveness];
-[WFNetworkProfile setPersonalHotspot:];
-[WFNetworkProfile HS20Badge];
-[WFNetworkProfile securityModeExt];
-[WFNetworkProfile setCarPlayType:];
-[WFNetworkProfile setHS20Network:];
-[WFNetworkProfile wasAddedFromWiFiPasswordSharing];
-[WFNetworkProfile HS20AccountName];
-[WFNetworkProfile HS20OperatorName];
-[WFNetworkProfile fetchedPassword];
-[WFNetworkProfile setCarPlayUUID:];
-[WFNetworkProfile TLSProfileCanJoin];
-[WFNetworkProfile canAttemptJoin];
-[WFNetworkProfile canExposeIMSI];
-[WFNetworkProfile carPlayType];
-[WFNetworkProfile carPlayUUID];
-[WFNetworkProfile enterpriseProfile];
-[WFNetworkProfile hotspotDeviceIdentifier];
-[WFNetworkProfile initWithCoreWiFiProfile:];
-[WFNetworkProfile initWithNetworkRef:];
-[WFNetworkProfile isAutoJoinEnabled];
-[WFNetworkProfile isAutoLoginEnabled];
-[WFNetworkProfile isDNSHeuristicsFiltered];
-[WFNetworkProfile isEqualToNetwork:];
-[WFNetworkProfile isHS20Network];
-[WFNetworkProfile isHS20NetworkProvisioned];
-[WFNetworkProfile isInSaveDataMode];
-[WFNetworkProfile isInstantHotspotJoin];
-[WFNetworkProfile isRandomMACAddressEnabled];
-[WFNetworkProfile lastAutoJoinDate];
-[WFNetworkProfile networkAttributes];
-[WFNetworkProfile policyUUID];
-[WFNetworkProfile previousPassword];
-[WFNetworkProfile profileContainsCarrierEAPType:];
-[WFNetworkProfile profileContainsEAPAKA:];
-[WFNetworkProfile profileContainsEAPSIM:];
-[WFNetworkProfile randomMACAddress];
-[WFNetworkProfile requiresTLSIdentityOnly];
-[WFNetworkProfile requiresUsernameAndPassword];
-[WFNetworkProfile scanAttributes];
-[WFNetworkProfile setAddedFromWiFiPasswordSharing:];
-[WFNetworkProfile setAdhoc:];
-[WFNetworkProfile setCanExposeIMSI:];
-[WFNetworkProfile setCarrierBased:];
-[WFNetworkProfile setDNSHeuristicsFiltered:];
-[WFNetworkProfile setEnterpriseProfile:];
-[WFNetworkProfile setFetchedPassword:];
-[WFNetworkProfile setHS20AccountName:];
-[WFNetworkProfile setHS20Badge:];
-[WFNetworkProfile setHS20NetworkProvisioned:];
-[WFNetworkProfile setHS20OperatorName:];
-[WFNetworkProfile setHotspotDeviceIdentifier:];
-[WFNetworkProfile setInstantHotspotJoin:];
-[WFNetworkProfile setOriginatorName:];
-[WFNetworkProfile setPolicyUUID:];
-[WFNetworkProfile setProfileBased:];
-[WFNetworkProfile setRandomMACAddress:];
-[WFNetworkProfile setRandomMACAddressEnabled:];
-[WFNetworkProfile setScanAttributes:];
-[WFNetworkProfile setSecurityModeExt:];
-[WFNetworkProfile shouldBeRemovedIfApplicationIsNoLongerInstalled];
-[WFNetworkProfile userProvidedPassword];
```
