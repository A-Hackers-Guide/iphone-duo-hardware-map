# `WFEnterpriseJoinOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 7 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"WFNetworkProfile" _profile;
@"WFNetworkScanRecord" _network;
@"CWFAssocParameters" _associationParameters;
@"CWFInterface" _interface;
^{__WiFiManagerClient=} _manager;
^{__WiFiDeviceClient=} _device;
```

## Properties

```
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (T@"CWFAssocParameters",&,N,V_associationParameters) associationParameters;
@property (T@"CWFInterface",&,N,V_interface) interface;
@property (T^{__WiFiManagerClient=},N,V_manager) manager;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
```

## Instance methods

```
-[WFEnterpriseJoinOperation setDevice:];
-[WFEnterpriseJoinOperation network];
-[WFEnterpriseJoinOperation device];
-[WFEnterpriseJoinOperation setManager:];
-[WFEnterpriseJoinOperation dealloc];
-[WFEnterpriseJoinOperation start];
-[WFEnterpriseJoinOperation setProfile:];
-[WFEnterpriseJoinOperation setInterface:];
-[WFEnterpriseJoinOperation manager];
-[WFEnterpriseJoinOperation profile];
-[WFEnterpriseJoinOperation interface];
-[WFEnterpriseJoinOperation setName:];
-[WFEnterpriseJoinOperation name];
-[WFEnterpriseJoinOperation setNetwork:];
-[WFEnterpriseJoinOperation _joinComplete:userInfo:network:];
-[WFEnterpriseJoinOperation joinNetworkRef:];
-[WFEnterpriseJoinOperation __hasPrivateMACUserJoinFailureUIState:];
-[WFEnterpriseJoinOperation _handleEnterpriseJoinResult:userInfo:network:];
-[WFEnterpriseJoinOperation _joinWithCoreWiFi];
-[WFEnterpriseJoinOperation _joinWithMobileWiFi];
-[WFEnterpriseJoinOperation associationParameters];
-[WFEnterpriseJoinOperation initWithAssocParameters:interface:];
-[WFEnterpriseJoinOperation initWithNetwork:profile:];
-[WFEnterpriseJoinOperation setAssociationParameters:];
```
