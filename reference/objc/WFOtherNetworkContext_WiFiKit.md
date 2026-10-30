# `WFOtherNetworkContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFCredentialsContext`
- Protocols: `WFContextPresenting`, `WFOtherNetworkProviderContext`, `WFOtherNetworkViewControllerDelegate`
- 16 instance variables, 26 properties, 43 instance methods, 0 class methods

## Instance variables

```
B passwordSharingSupported;
B _supportsRandomMACAddress;
B _isUsingRandomMACAddress;
@"NSArray" _availableTLSIdentities;
q _requestedFields;
@"NSString" username;
@"WFNetworkScanRecord" _network;
q _availableAuthTraits;
@"NSString" _randomMACAddress;
@"NSString" _hardwareMACAddress;
@"WFUserSuppliedNetwork" _userSuppliedNetwork;
@? _privateAddressModeChangeHandler;
@"NSArray" _WAPIRootCertificates;
@"NSArray" _WAPIIdentities;
@"WFNetworkProfile" _profile;
Q _type;
```

## Properties

```
@property (T@"NSArray",&,N,V_WAPIRootCertificates) WAPIRootCertificates;
@property (T@"NSArray",&,N,V_WAPIIdentities) WAPIIdentities;
@property (T@"NSArray",&,N,V_availableTLSIdentities) availableTLSIdentities;
@property (Tq,N,V_requestedFields) requestedFields;
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (TQ,N,V_type) type;
@property (Tq,N,V_availableAuthTraits) availableAuthTraits;
@property (TB,N,V_isUsingRandomMACAddress) isUsingRandomMACAddress;
@property (TB,N,V_supportsRandomMACAddress) supportsRandomMACAddress;
@property (T@"NSString",C,N,V_randomMACAddress) randomMACAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"WFUserSuppliedNetwork",&,N,V_userSuppliedNetwork) userSuppliedNetwork;
@property (T@?,C,N,V_privateAddressModeChangeHandler) privateAddressModeChangeHandler;
@property (T@"UIViewController<WFNetworkView>",W,N) provider;
@property (TB,R,N) needsDismissal;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) WAPIEnabled;
@property (TB,R,N,GisPasswordSharingSupported,VpasswordSharingSupported) passwordSharingSupported;
@property (T@"NSString",R,N,Vusername) username;
@property (TB,R,N,GisEnterprise) enterprise;
@property (T@"WFHealthIssue",R,N) securityIssue;
@property (TB,R,N) passwordReceivedFromPasswordSharing;
```

## Instance methods

```
-[WFOtherNetworkContext hardwareMACAddress];
-[WFOtherNetworkContext isEnterprise];
-[WFOtherNetworkContext network];
-[WFOtherNetworkContext initWithType:];
-[WFOtherNetworkContext username];
-[WFOtherNetworkContext setProfile:];
-[WFOtherNetworkContext requestedFields];
-[WFOtherNetworkContext profile];
-[WFOtherNetworkContext setType:];
-[WFOtherNetworkContext type];
-[WFOtherNetworkContext setRequestedFields:];
-[WFOtherNetworkContext securityMode];
-[WFOtherNetworkContext setNetwork:];
-[WFOtherNetworkContext isPasswordSharingSupported];
-[WFOtherNetworkContext privateAddressModeChangeHandler];
-[WFOtherNetworkContext WAPIIdentities];
-[WFOtherNetworkContext WAPIRootCertificates];
-[WFOtherNetworkContext _updateActivityStringForError:networkName:];
-[WFOtherNetworkContext availableAuthTraits];
-[WFOtherNetworkContext availableTLSIdentities];
-[WFOtherNetworkContext finishWithError:forNetwork:profile:];
-[WFOtherNetworkContext gatherCredentials:];
-[WFOtherNetworkContext initWithType:authTraits:supportRandomAddress:useRandomAddress:randomMACAddress:hardwareMACAddress:];
-[WFOtherNetworkContext isUsingRandomMACAddress];
-[WFOtherNetworkContext otherNetworkViewController:isValidPassword:];
-[WFOtherNetworkContext otherNetworkViewControllerUserDidTapCancel:];
-[WFOtherNetworkContext otherNetworkViewControllerUserDidTapJoin:];
-[WFOtherNetworkContext randomMACAddress];
-[WFOtherNetworkContext savePrivateAddressMode:];
-[WFOtherNetworkContext setAvailableAuthTraits:];
-[WFOtherNetworkContext setAvailableTLSIdentities:];
-[WFOtherNetworkContext setHardwareMACAddress:];
-[WFOtherNetworkContext setIsUsingRandomMACAddress:];
-[WFOtherNetworkContext setPrivateAddressModeChangeHandler:];
-[WFOtherNetworkContext setRandomMACAddress:];
-[WFOtherNetworkContext setSupportsRandomMACAddress:];
-[WFOtherNetworkContext setUserSuppliedNetwork:];
-[WFOtherNetworkContext setWAPIIdentities:];
-[WFOtherNetworkContext setWAPIRootCertificates:];
-[WFOtherNetworkContext supportsRandomMACAddress];
-[WFOtherNetworkContext userSuppliedNetwork];
-[WFOtherNetworkContext validateCredentials];
-[WFOtherNetworkContext validatePassword];
```
