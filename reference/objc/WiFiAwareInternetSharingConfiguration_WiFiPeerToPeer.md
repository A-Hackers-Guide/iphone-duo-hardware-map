# `WiFiAwareInternetSharingConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 15 instance methods, 5 class methods

## Instance variables

```
B _provider;
B _automatic;
B _useBridging;
@"NSString" _interfaceName;
```

## Properties

```
@property (T@"NSString",&,N,V_interfaceName) interfaceName;
@property (TB,N,V_provider) provider;
@property (TB,N,V_automatic) automatic;
@property (TB,N,V_useBridging) useBridging;
```

## Class methods

```
+[WiFiAwareInternetSharingConfiguration supportsSecureCoding];
+[WiFiAwareInternetSharingConfiguration automaticallyProvideInternetToResponders];
+[WiFiAwareInternetSharingConfiguration automaticallyRequestInternetFromInitiators];
+[WiFiAwareInternetSharingConfiguration provideInternetToInitiatorsFromInterface:];
+[WiFiAwareInternetSharingConfiguration requestInterentFromResponder];
```

## Instance methods

```
-[WiFiAwareInternetSharingConfiguration setInterfaceName:];
-[WiFiAwareInternetSharingConfiguration provider];
-[WiFiAwareInternetSharingConfiguration interfaceName];
-[WiFiAwareInternetSharingConfiguration encodeWithCoder:];
-[WiFiAwareInternetSharingConfiguration description];
-[WiFiAwareInternetSharingConfiguration initWithCoder:];
-[WiFiAwareInternetSharingConfiguration copyWithZone:];
-[WiFiAwareInternetSharingConfiguration isEqual:];
-[WiFiAwareInternetSharingConfiguration setProvider:];
-[WiFiAwareInternetSharingConfiguration automatic];
-[WiFiAwareInternetSharingConfiguration setAutomatic:];
-[WiFiAwareInternetSharingConfiguration setUseBridging:];
-[WiFiAwareInternetSharingConfiguration initWithInterfaceName:isProvider:isAutomatic:];
-[WiFiAwareInternetSharingConfiguration interfaceNameEqual:];
-[WiFiAwareInternetSharingConfiguration useBridging];
```
