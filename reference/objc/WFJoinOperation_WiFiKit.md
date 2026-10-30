# `WFJoinOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 7 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"WFNetworkProfile" _profile;
@"WFNetworkScanRecord" _network;
^{__WiFiManagerClient=} _manager;
^{__WiFiDeviceClient=} _device;
@"CWFAssocParameters" _associationParameters;
@"CWFInterface" _interface;
```

## Properties

```
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (T^{__WiFiManagerClient=},N,V_manager) manager;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"CWFAssocParameters",&,N,V_associationParameters) associationParameters;
@property (T@"CWFInterface",&,N,V_interface) interface;
```

## Instance methods

```
-[WFJoinOperation setDevice:];
-[WFJoinOperation network];
-[WFJoinOperation device];
-[WFJoinOperation setManager:];
-[WFJoinOperation dealloc];
-[WFJoinOperation start];
-[WFJoinOperation setProfile:];
-[WFJoinOperation setInterface:];
-[WFJoinOperation manager];
-[WFJoinOperation profile];
-[WFJoinOperation interface];
-[WFJoinOperation setName:];
-[WFJoinOperation name];
-[WFJoinOperation setNetwork:];
-[WFJoinOperation _joinComplete:userInfo:network:];
-[WFJoinOperation joinNetworkRef:];
-[WFJoinOperation __hasPrivateMACUserJoinFailureUIState:];
-[WFJoinOperation _joinWithCoreWiFi];
-[WFJoinOperation associationParameters];
-[WFJoinOperation initWithAssocParameters:interface:];
-[WFJoinOperation initWithNetwork:profile:];
-[WFJoinOperation setAssociationParameters:];
```
