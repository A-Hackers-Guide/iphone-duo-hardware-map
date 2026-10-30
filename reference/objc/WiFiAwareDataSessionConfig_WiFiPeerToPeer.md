# `WiFiAwareDataSessionConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
I _userID;
q _serviceType;
@"WiFiAwareInternetSharingConfiguration" _internetSharingConfiguration;
```

## Properties

```
@property (Tq,N,V_serviceType) serviceType;
@property (T@"WiFiAwareInternetSharingConfiguration",C,N,V_internetSharingConfiguration) internetSharingConfiguration;
@property (TI,N,V_userID) userID;
```

## Class methods

```
+[WiFiAwareDataSessionConfig supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDataSessionConfig userID];
-[WiFiAwareDataSessionConfig setUserID:];
-[WiFiAwareDataSessionConfig initWithServiceType:];
-[WiFiAwareDataSessionConfig encodeWithCoder:];
-[WiFiAwareDataSessionConfig hash];
-[WiFiAwareDataSessionConfig description];
-[WiFiAwareDataSessionConfig initWithCoder:];
-[WiFiAwareDataSessionConfig copyWithZone:];
-[WiFiAwareDataSessionConfig setServiceType:];
-[WiFiAwareDataSessionConfig isEqual:];
-[WiFiAwareDataSessionConfig serviceType];
-[WiFiAwareDataSessionConfig setInternetSharingConfiguration:];
-[WiFiAwareDataSessionConfig initWithServiceType:internetSharingConfiguration:];
-[WiFiAwareDataSessionConfig internetSharingConfiguration];
```
