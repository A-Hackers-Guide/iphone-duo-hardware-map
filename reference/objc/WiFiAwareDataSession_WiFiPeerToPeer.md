# `WiFiAwareDataSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAwareDatapathXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 24 instance variables, 26 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
q _internetSharingPolicy;
I _userID;
@"NSObject<OS_os_log>" _logger;
B _skipInfrastructureRelayCheck;
B _pairingCachingEnabled;
I _localInterfaceIndex;
@"WiFiAwareDiscoveryResult" _discoveryResult;
q _serviceType;
@"WiFiAwarePublishDatapathServiceSpecificInfo" _serviceSpecificInfo;
@"NSString" _passphrase;
@"NSData" _pmk;
@"NSData" _pmkID;
@"WiFiAwareInternetSharingConfiguration" _internetSharingConfiguration;
@"WiFiAwareMulticastConfiguration" _multicastConfiguration;
@"<WiFiAwareDataSessionPairingDelegate>" _pairingDelegate;
q _pairingMethod;
@"WiFiAwarePublishServiceSpecificInfo" _pairSetupServiceSpecificInfo;
@"NSString" _pinCode;
q _connectionMode;
@"WiFiAwarePairingMetadata" _pairingMetadata;
@"<WiFiAwareDataSessionDelegate>" _delegate;
@"NSNumber" _datapathID;
@"WiFiMACAddress" _initiatorDataAddress;
```

## Properties

```
@property (T@"NSNumber",&,V_datapathID) datapathID;
@property (T@"WiFiMACAddress",&,V_initiatorDataAddress) initiatorDataAddress;
@property (T@"WiFiAwareDiscoveryResult",R,C,N,V_discoveryResult) discoveryResult;
@property (Tq,R,N,V_serviceType) serviceType;
@property (T@"WiFiAwarePublishDatapathServiceSpecificInfo",R,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (T@"NSString",R,N,V_passphrase) passphrase;
@property (T@"NSData",R,N,V_pmk) pmk;
@property (T@"NSData",R,N,V_pmkID) pmkID;
@property (Tq,R,N) internetSharingPolicy;
@property (T@"WiFiAwareInternetSharingConfiguration",C,N,V_internetSharingConfiguration) internetSharingConfiguration;
@property (T@"WiFiAwareMulticastConfiguration",C,N,V_multicastConfiguration) multicastConfiguration;
@property (TB,N,V_skipInfrastructureRelayCheck) skipInfrastructureRelayCheck;
@property (T@"<WiFiAwareDataSessionPairingDelegate>",W,N,V_pairingDelegate) pairingDelegate;
@property (Tq,V_pairingMethod) pairingMethod;
@property (TB,V_pairingCachingEnabled) pairingCachingEnabled;
@property (T@"WiFiAwarePublishServiceSpecificInfo",C,N,V_pairSetupServiceSpecificInfo) pairSetupServiceSpecificInfo;
@property (T@"NSString",&,N,V_pinCode) pinCode;
@property (Tq,N,V_connectionMode) connectionMode;
@property (T@"WiFiAwarePairingMetadata",C,N,V_pairingMetadata) pairingMetadata;
@property (T@"<WiFiAwareDataSessionDelegate>",W,N,V_delegate) delegate;
@property (T@"WiFiMACAddress",R,N) localDataAddress;
@property (TI,R,N,V_localInterfaceIndex) localInterfaceIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareDataSession resetState];
-[WiFiAwareDataSession handleError:];
-[WiFiAwareDataSession startConnectionUsingProxy:completionHandler:];
-[WiFiAwareDataSession stop];
-[WiFiAwareDataSession remoteObjectInterface];
-[WiFiAwareDataSession serviceSpecificInfo];
-[WiFiAwareDataSession start];
-[WiFiAwareDataSession exportedInterface];
-[WiFiAwareDataSession setMulticastConfiguration:];
-[WiFiAwareDataSession setDelegate:];
-[WiFiAwareDataSession exportedObject];
-[WiFiAwareDataSession delegate];
-[WiFiAwareDataSession description];
-[WiFiAwareDataSession setConnectionMode:];
-[WiFiAwareDataSession connectionMode];
-[WiFiAwareDataSession multicastConfiguration];
-[WiFiAwareDataSession serviceType];
-[WiFiAwareDataSession pairingMetadata];
-[WiFiAwareDataSession pinCode];
-[WiFiAwareDataSession discoveryResult];
-[WiFiAwareDataSession datapathID];
-[WiFiAwareDataSession generateStatisticsReportWithCompletionHandler:];
-[WiFiAwareDataSession initSecureConnectionWithPairedDevice:configuration:];
-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:];
-[WiFiAwareDataSession initiatorDataAddress];
-[WiFiAwareDataSession localInterfaceIndex];
-[WiFiAwareDataSession reportIssue:];
-[WiFiAwareDataSession setInternetSharingConfiguration:];
-[WiFiAwareDataSession setPairSetupServiceSpecificInfo:];
-[WiFiAwareDataSession setPairingCachingEnabled:];
-[WiFiAwareDataSession setPairingDelegate:];
-[WiFiAwareDataSession setPairingMetadata:];
-[WiFiAwareDataSession setPairingMethod:];
-[WiFiAwareDataSession updateLinkStatus:];
-[WiFiAwareDataSession pairingDelegate];
-[WiFiAwareDataSession passphrase];
-[WiFiAwareDataSession setPinCode:];
-[WiFiAwareDataSession pmk];
-[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:];
-[WiFiAwareDataSession internetSharingPolicy];
-[WiFiAwareDataSession localDataAddress];
-[WiFiAwareDataSession setWantsPeerRSSIUpdates:withCompletionHandler:];
-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:];
-[WiFiAwareDataSession datapathFailedToStartWithError:];
-[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:];
-[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:];
-[WiFiAwareDataSession datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:];
-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:];
-[WiFiAwareDataSession datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:];
-[WiFiAwareDataSession datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:];
-[WiFiAwareDataSession datapathTerminatedWithReason:];
-[WiFiAwareDataSession datapathUpdatedInternetSharingPolicy:];
-[WiFiAwareDataSession datapathUpdatedPeerRSSI:];
-[WiFiAwareDataSession datapathUpdatedServiceSpecificInfo:];
-[WiFiAwareDataSession generateCurrentNetworkRecordForInternetSharingSession:];
-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:pmk:pmkID:];
-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:pmk:];
-[WiFiAwareDataSession initWithDiscoveryResult:serviceType:serviceSpecificInfo:pmk:pmkID:];
-[WiFiAwareDataSession internetSharingConfiguration];
-[WiFiAwareDataSession pairSetupServiceSpecificInfo];
-[WiFiAwareDataSession pairingCachingEnabled];
-[WiFiAwareDataSession pairingMethod];
-[WiFiAwareDataSession pmkID];
-[WiFiAwareDataSession setDatapathID:];
-[WiFiAwareDataSession setInitiatorDataAddress:];
-[WiFiAwareDataSession setSkipInfrastructureRelayCheck:];
-[WiFiAwareDataSession skipInfrastructureRelayCheck];
```
