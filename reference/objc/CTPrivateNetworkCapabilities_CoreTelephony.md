# `CTPrivateNetworkCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isPrivateNetworkSIM;
B _isPrivateNetworkPreferredOverWifi;
B _isPrivateNetworkModeEnabled;
B _hideDataRoaming;
```

## Properties

```
@property (TB,N,V_isPrivateNetworkSIM) isPrivateNetworkSIM;
@property (TB,N,V_isPrivateNetworkPreferredOverWifi) isPrivateNetworkPreferredOverWifi;
@property (TB,N,V_isPrivateNetworkModeEnabled) isPrivateNetworkModeEnabled;
@property (TB,N,V_hideDataRoaming) hideDataRoaming;
```

## Class methods

```
+[CTPrivateNetworkCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTPrivateNetworkCapabilities init];
-[CTPrivateNetworkCapabilities encodeWithCoder:];
-[CTPrivateNetworkCapabilities description];
-[CTPrivateNetworkCapabilities initWithCoder:];
-[CTPrivateNetworkCapabilities copyWithZone:];
-[CTPrivateNetworkCapabilities hideDataRoaming];
-[CTPrivateNetworkCapabilities setIsPrivateNetworkModeEnabled:];
-[CTPrivateNetworkCapabilities isPrivateNetworkModeEnabled];
-[CTPrivateNetworkCapabilities isPrivateNetworkPreferredOverWifi];
-[CTPrivateNetworkCapabilities isPrivateNetworkSIM];
-[CTPrivateNetworkCapabilities setHideDataRoaming:];
-[CTPrivateNetworkCapabilities setIsPrivateNetworkPreferredOverWifi:];
-[CTPrivateNetworkCapabilities setIsPrivateNetworkSIM:];
```
