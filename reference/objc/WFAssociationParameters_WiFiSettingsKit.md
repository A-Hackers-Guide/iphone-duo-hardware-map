# `WFAssociationParameters`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _carPlayOnly;
B _instantHotspot;
B _joinedUsingWiFiPasswordSharing;
@"NSString" _hotspotDeviceIdentifier;
@"WFEnterpriseAssociationParameters" _enterpriseParameters;
@"NSString" _wapiPassword;
```

## Properties

```
@property (TB,N,GisCarPlayOnly,V_carPlayOnly) carPlayOnly;
@property (TB,N,GisInstantHotspot,V_instantHotspot) instantHotspot;
@property (TB,N,V_joinedUsingWiFiPasswordSharing) joinedUsingWiFiPasswordSharing;
@property (T@"NSString",&,N,V_hotspotDeviceIdentifier) hotspotDeviceIdentifier;
@property (T@"WFEnterpriseAssociationParameters",&,N,V_enterpriseParameters) enterpriseParameters;
@property (T@"NSString",&,N,V_wapiPassword) wapiPassword;
```

## Instance methods

```
-[WFAssociationParameters isInstantHotspot];
-[WFAssociationParameters isCarPlayOnly];
-[WFAssociationParameters hotspotDeviceIdentifier];
-[WFAssociationParameters setHotspotDeviceIdentifier:];
-[WFAssociationParameters setInstantHotspot:];
-[WFAssociationParameters setCarPlayOnly:];
-[WFAssociationParameters enterpriseParameters];
-[WFAssociationParameters joinedUsingWiFiPasswordSharing];
-[WFAssociationParameters setEnterpriseParameters:];
-[WFAssociationParameters setJoinedUsingWiFiPasswordSharing:];
-[WFAssociationParameters setWapiPassword:];
-[WFAssociationParameters wapiPassword];
```
