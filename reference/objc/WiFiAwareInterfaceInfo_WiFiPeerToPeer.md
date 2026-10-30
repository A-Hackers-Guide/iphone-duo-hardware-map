# `WiFiAwareInterfaceInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isEnabled;
@"NSString" _interfaceName;
@"WiFiMACAddress" _interfaceAddr;
```

## Properties

```
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (T@"WiFiMACAddress",R,C,N,V_interfaceAddr) interfaceAddr;
@property (TB,R,N,V_isEnabled) isEnabled;
```

## Class methods

```
+[WiFiAwareInterfaceInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareInterfaceInfo interfaceName];
-[WiFiAwareInterfaceInfo isEnabled];
-[WiFiAwareInterfaceInfo encodeWithCoder:];
-[WiFiAwareInterfaceInfo hash];
-[WiFiAwareInterfaceInfo description];
-[WiFiAwareInterfaceInfo initWithCoder:];
-[WiFiAwareInterfaceInfo copyWithZone:];
-[WiFiAwareInterfaceInfo isEqual:];
-[WiFiAwareInterfaceInfo initWithInterfaceName:interfaceAddr:isEnabled:];
-[WiFiAwareInterfaceInfo interfaceAddr];
```
