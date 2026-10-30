# `CWFWiFiNetworkSharingClientID`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bundleID;
@"NSString" _accessoryID;
```

## Properties

```
@property (T@"NSString",C,V_bundleID) bundleID;
@property (T@"NSString",C,V_accessoryID) accessoryID;
```

## Class methods

```
+[CWFWiFiNetworkSharingClientID supportsSecureCoding];
+[CWFWiFiNetworkSharingClientID clientIDWithAccessoryID:bundleID:];
```

## Instance methods

```
-[CWFWiFiNetworkSharingClientID setBundleID:];
-[CWFWiFiNetworkSharingClientID accessoryID];
-[CWFWiFiNetworkSharingClientID setAccessoryID:];
-[CWFWiFiNetworkSharingClientID encodeWithCoder:];
-[CWFWiFiNetworkSharingClientID hash];
-[CWFWiFiNetworkSharingClientID description];
-[CWFWiFiNetworkSharingClientID initWithCoder:];
-[CWFWiFiNetworkSharingClientID bundleID];
-[CWFWiFiNetworkSharingClientID copyWithZone:];
-[CWFWiFiNetworkSharingClientID isEqual:];
-[CWFWiFiNetworkSharingClientID initWithAccessoryID:bundleID:];
-[CWFWiFiNetworkSharingClientID isEqualToWiFiNetworkSharingClientID:];
```
