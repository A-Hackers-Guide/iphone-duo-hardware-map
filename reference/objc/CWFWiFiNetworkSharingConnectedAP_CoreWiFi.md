# `CWFWiFiNetworkSharingConnectedAP`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSData" _SSID;
@"NSArray" _links;
```

## Properties

```
@property (T@"NSString",R) networkName;
@property (T@"NSData",C,V_SSID) SSID;
@property (T@"NSArray",C,V_links) links;
```

## Class methods

```
+[CWFWiFiNetworkSharingConnectedAP supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingConnectedAP networkName];
-[CWFWiFiNetworkSharingConnectedAP setSSID:];
-[CWFWiFiNetworkSharingConnectedAP SSID];
-[CWFWiFiNetworkSharingConnectedAP encodeWithCoder:];
-[CWFWiFiNetworkSharingConnectedAP hash];
-[CWFWiFiNetworkSharingConnectedAP description];
-[CWFWiFiNetworkSharingConnectedAP initWithCoder:];
-[CWFWiFiNetworkSharingConnectedAP copyWithZone:];
-[CWFWiFiNetworkSharingConnectedAP links];
-[CWFWiFiNetworkSharingConnectedAP isEqual:];
-[CWFWiFiNetworkSharingConnectedAP setLinks:];
-[CWFWiFiNetworkSharingConnectedAP isEqualToWiFiNetworkSharingConnectedAP:];
```
