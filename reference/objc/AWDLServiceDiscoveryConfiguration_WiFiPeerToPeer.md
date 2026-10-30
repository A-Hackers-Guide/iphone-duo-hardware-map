# `AWDLServiceDiscoveryConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isResolve;
@"NSData" _serviceKey;
@"NSData" _serviceValue;
```

## Properties

```
@property (T@"NSData",R,N,V_serviceKey) serviceKey;
@property (T@"NSData",R,N,V_serviceValue) serviceValue;
@property (TB,R,N,V_isResolve) isResolve;
```

## Class methods

```
+[AWDLServiceDiscoveryConfiguration supportsSecureCoding];
```

## Instance methods

```
-[AWDLServiceDiscoveryConfiguration serviceKey];
-[AWDLServiceDiscoveryConfiguration initWithKey:value:resolve:];
-[AWDLServiceDiscoveryConfiguration isResolve];
-[AWDLServiceDiscoveryConfiguration encodeWithCoder:];
-[AWDLServiceDiscoveryConfiguration description];
-[AWDLServiceDiscoveryConfiguration initWithKey:];
-[AWDLServiceDiscoveryConfiguration initWithCoder:];
-[AWDLServiceDiscoveryConfiguration copyWithZone:];
-[AWDLServiceDiscoveryConfiguration isEqual:];
-[AWDLServiceDiscoveryConfiguration serviceValue];
```
