# `WiFiAwareSrvInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _isEnabled;
I _publishServiceCount;
I _subscribeServiceCount;
I _srvSessionCount;
@"NSString" _interfaceName;
@"WiFiMACAddress" _interfaceAddr;
@"NSArray" _srvSessionInfos;
```

## Properties

```
@property (T@"NSString",R,N,V_interfaceName) interfaceName;
@property (T@"WiFiMACAddress",R,N,V_interfaceAddr) interfaceAddr;
@property (TB,R,N,V_isEnabled) isEnabled;
@property (TI,R,N,V_publishServiceCount) publishServiceCount;
@property (TI,R,N,V_subscribeServiceCount) subscribeServiceCount;
@property (TI,R,N,V_srvSessionCount) srvSessionCount;
@property (T@"NSArray",R,N,V_srvSessionInfos) srvSessionInfos;
```

## Class methods

```
+[WiFiAwareSrvInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareSrvInfo init];
-[WiFiAwareSrvInfo interfaceName];
-[WiFiAwareSrvInfo isEnabled];
-[WiFiAwareSrvInfo encodeWithCoder:];
-[WiFiAwareSrvInfo description];
-[WiFiAwareSrvInfo initWithCoder:];
-[WiFiAwareSrvInfo copyWithZone:];
-[WiFiAwareSrvInfo srvSessionCount];
-[WiFiAwareSrvInfo srvSessionInfos];
-[WiFiAwareSrvInfo detailedDescriptionWithChangedOptions:previousSrvInfo:];
-[WiFiAwareSrvInfo initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:];
-[WiFiAwareSrvInfo interfaceAddr];
-[WiFiAwareSrvInfo publishServiceCount];
-[WiFiAwareSrvInfo subscribeServiceCount];
```
