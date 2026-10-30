# `WFDetailsProviderContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFProviderContext`
- 0 instance variables, 32 properties, 60 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) recommendations;
@property (TB) diagnosable;
@property (TB,N) autoJoinEnabled;
@property (TB,N) autoLoginEnabled;
@property (TB,N) isInSaveDataMode;
@property (TB,N) isPrivacyProxyEnabled;
@property (TB,R,N,GisCurrent) current;
@property (TB,R,N,GisRandomMACAddressDisabled) randomMACAddressDisabled;
@property (TB,R,N,GisKnownNetwork) knownNetwork;
@property (TB,R,N,GisRandomMACAddressConfigurable) randomMACAddressConfigurable;
@property (TB,R,N,GisRandomMACFeatureEnabled) randomMACFeatureEnabled;
@property (TB,R,N,GisRandomMACSwitchOn) randomMACSwitchOn;
@property (TB,R,N,GisConnectedWithHardwareAddress) connectedWithHardwareAddress;
@property (Tq,N) wifiMode;
@property (TB,R,N,GisWiFiOutranked) WiFiOutranked;
@property (T@"NSString",R,C,N) randomMACAddress;
@property (T@"NSString",R,C,N) hardwareMACAddress;
@property (T@"NSString",C,N) staticPrivateMACFooterText;
@property (T@"WFContentCachesContext",?,&,N) contentCachesContext;
@property (T@"DADevice",?,&,N) daDevice;
@property (TQ,?,R,N) scrollToCellType;
@property (T@"NSString",?,C,N) turnONPrivateMACFooterText;
@property (T@"NSString",?,C,N) turnOFFPrivateMACFooterText;
@property (TB,?,N,GisJoinable) joinable;
@property (TB,?,R,N,GisCredentialsVisible) credentialsVisible;
@property (T@"NSString",?,R,C,N) username;
@property (T@"NSString",?,R,C,N) password;
@property (TB,?,R,N,GisWifiModeConfigurable) wifiModeConfigurable;
@property (T@?,?,C,N) credentialsTappedHandler;
@property (TQ,?,R,N) autoJoinConfigurable;
@property (T@"NSString",?,R,C,N) portalURL;
@property (TQ,?,N) privateAddressMode;
```

## Instance methods

```
-[WFDetailsProviderContext hardwareMACAddress];
-[WFDetailsProviderContext setAutoJoinEnabled:];
-[WFDetailsProviderContext isCurrent];
-[WFDetailsProviderContext recommendations];
-[WFDetailsProviderContext join];
-[WFDetailsProviderContext setWifiMode:];
-[WFDetailsProviderContext wifiMode];
-[WFDetailsProviderContext manage];
-[WFDetailsProviderContext isPrivacyProxyEnabled];
-[WFDetailsProviderContext forget];
-[WFDetailsProviderContext autoJoinEnabled];
-[WFDetailsProviderContext isWiFiOutranked];
-[WFDetailsProviderContext setDiagnosable:];
-[WFDetailsProviderContext autoLoginEnabled];
-[WFDetailsProviderContext cancelNetworkQualityRun];
-[WFDetailsProviderContext diagnosable];
-[WFDetailsProviderContext diagnosticsContext];
-[WFDetailsProviderContext disableRandomMAC];
-[WFDetailsProviderContext enableRandomMAC:];
-[WFDetailsProviderContext isConnectedWithHardwareAddress];
-[WFDetailsProviderContext isInSaveDataMode];
-[WFDetailsProviderContext isKnownNetwork];
-[WFDetailsProviderContext isRandomMACAddressConfigurable];
-[WFDetailsProviderContext isRandomMACAddressDisabled];
-[WFDetailsProviderContext isRandomMACFeatureEnabled];
-[WFDetailsProviderContext isRandomMACSwitchOn];
-[WFDetailsProviderContext openRecommendationLink];
-[WFDetailsProviderContext overrideWiFiOutrank];
-[WFDetailsProviderContext randomMACAddress];
-[WFDetailsProviderContext renewLease];
-[WFDetailsProviderContext runNetworkQualityWithCompletionHandler:];
-[WFDetailsProviderContext setAutoLoginEnabled:];
-[WFDetailsProviderContext setIsInSaveDataMode:];
-[WFDetailsProviderContext setIsPrivacyProxyEnabled:];
-[WFDetailsProviderContext setStaticPrivateMACFooterText:];
-[WFDetailsProviderContext staticPrivateMACFooterText];
-[WFDetailsProviderContext username];
-[WFDetailsProviderContext password];
-[WFDetailsProviderContext networkOrigin];
-[WFDetailsProviderContext portalURL];
-[WFDetailsProviderContext daDevice];
-[WFDetailsProviderContext setTurnOFFPrivateMACFooterText:];
-[WFDetailsProviderContext autoJoinConfigurable];
-[WFDetailsProviderContext contentCachesContext];
-[WFDetailsProviderContext credentialsTappedHandler];
-[WFDetailsProviderContext isCredentialsVisible];
-[WFDetailsProviderContext isJoinable];
-[WFDetailsProviderContext isWifiModeConfigurable];
-[WFDetailsProviderContext openPortalURL];
-[WFDetailsProviderContext privateAddressMode];
-[WFDetailsProviderContext scrollToCellType];
-[WFDetailsProviderContext setContentCachesContext:];
-[WFDetailsProviderContext setCredentialsTappedHandler:];
-[WFDetailsProviderContext setDaDevice:];
-[WFDetailsProviderContext setJoinable:];
-[WFDetailsProviderContext setPrivateAddressMode:];
-[WFDetailsProviderContext setTurnONPrivateMACFooterText:];
-[WFDetailsProviderContext turnOFFPrivateMACFooterText];
-[WFDetailsProviderContext turnONPrivateMACFooterText];
-[WFDetailsProviderContext updatePrivateAddressMode:];
```
