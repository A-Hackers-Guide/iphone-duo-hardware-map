# `CWFWiFiNetworkSharingNetwork`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 11 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _isHidden;
B _isCaptive;
@"NSData" _SSID;
Q _supportedSecurityTypes;
@"NSString" _password;
@"CWFWiFiNetworkSharingEAPCredentials" _EAPCredentials;
@"NSDate" _firstSharedDate;
@"NSDate" _lastModifiedDate;
@"NSDictionary" _captivePortalCredentials;
```

## Properties

```
@property (T@"CWFWiFiNetworkSharingNetworkID",R) wifiNetworkSharingNetworkID;
@property (T@"NSString",R) networkName;
@property (T@"NSData",C,V_SSID) SSID;
@property (TQ,V_supportedSecurityTypes) supportedSecurityTypes;
@property (TB,V_isHidden) isHidden;
@property (T@"NSString",C,V_password) password;
@property (T@"CWFWiFiNetworkSharingEAPCredentials",C,N,V_EAPCredentials) EAPCredentials;
@property (T@"NSDate",C,V_firstSharedDate) firstSharedDate;
@property (T@"NSDate",C,V_lastModifiedDate) lastModifiedDate;
@property (TB,V_isCaptive) isCaptive;
@property (T@"NSDictionary",C,V_captivePortalCredentials) captivePortalCredentials;
```

## Class methods

```
+[CWFWiFiNetworkSharingNetwork supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingNetwork setIsHidden:];
-[CWFWiFiNetworkSharingNetwork networkName];
-[CWFWiFiNetworkSharingNetwork setSSID:];
-[CWFWiFiNetworkSharingNetwork SSID];
-[CWFWiFiNetworkSharingNetwork lastModifiedDate];
-[CWFWiFiNetworkSharingNetwork setLastModifiedDate:];
-[CWFWiFiNetworkSharingNetwork setIsCaptive:];
-[CWFWiFiNetworkSharingNetwork isHidden];
-[CWFWiFiNetworkSharingNetwork captivePortalCredentials];
-[CWFWiFiNetworkSharingNetwork encodeWithCoder:];
-[CWFWiFiNetworkSharingNetwork isCaptive];
-[CWFWiFiNetworkSharingNetwork hash];
-[CWFWiFiNetworkSharingNetwork description];
-[CWFWiFiNetworkSharingNetwork initWithCoder:];
-[CWFWiFiNetworkSharingNetwork setPassword:];
-[CWFWiFiNetworkSharingNetwork copyWithZone:];
-[CWFWiFiNetworkSharingNetwork isEqual:];
-[CWFWiFiNetworkSharingNetwork password];
-[CWFWiFiNetworkSharingNetwork setCaptivePortalCredentials:];
-[CWFWiFiNetworkSharingNetwork firstSharedDate];
-[CWFWiFiNetworkSharingNetwork EAPCredentials];
-[CWFWiFiNetworkSharingNetwork isEqualToWiFiNetworkSharingNetwork:];
-[CWFWiFiNetworkSharingNetwork setEAPCredentials:];
-[CWFWiFiNetworkSharingNetwork setFirstSharedDate:];
-[CWFWiFiNetworkSharingNetwork setSupportedSecurityTypes:];
-[CWFWiFiNetworkSharingNetwork supportedSecurityTypes];
-[CWFWiFiNetworkSharingNetwork wifiNetworkSharingNetworkID];
```
