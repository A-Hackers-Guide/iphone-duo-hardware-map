# `WFKnownNetworksManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFKnownNetworksProvider`
- 3 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _allKnownProfiles;
@"CWFInterface" _interface;
@"WFPrivateAddressConfigManager" _privateAddressConfigManager;
```

## Properties

```
@property (T@"NSArray",&,N,V_allKnownProfiles) allKnownProfiles;
@property (T@"CWFInterface",&,N,V_interface) interface;
@property (T@"WFPrivateAddressConfigManager",&,N,V_privateAddressConfigManager) privateAddressConfigManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFKnownNetworksManager initWithInterface:];
-[WFKnownNetworksManager setInterface:];
-[WFKnownNetworksManager interface];
-[WFKnownNetworksManager removeNetworks:];
-[WFKnownNetworksManager setPrivateAddressConfigManager:];
-[WFKnownNetworksManager _getAllKnownProfiles];
-[WFKnownNetworksManager allEditableNetworkProfiles];
-[WFKnownNetworksManager allKnownProfiles];
-[WFKnownNetworksManager allNonEditableNetworkProfiles];
-[WFKnownNetworksManager passwordForNetworksWithSSID:];
-[WFKnownNetworksManager privateAddressConfigForNetworkName:];
-[WFKnownNetworksManager privateAddressConfigManager];
-[WFKnownNetworksManager setAllKnownProfiles:];
```
