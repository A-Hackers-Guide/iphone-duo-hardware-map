# `W5PeerDiscoveryEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _peersFound;
@"NSArray" _peersLost;
@"NSDictionary" _info;
```

## Properties

```
@property (T@"NSArray",&,N,V_peersFound) peersFound;
@property (T@"NSArray",&,N,V_peersLost) peersLost;
@property (T@"NSDictionary",&,N,V_info) info;
```

## Class methods

```
+[W5PeerDiscoveryEvent supportsSecureCoding];
```

## Instance methods

```
-[W5PeerDiscoveryEvent info];
-[W5PeerDiscoveryEvent setInfo:];
-[W5PeerDiscoveryEvent encodeWithCoder:];
-[W5PeerDiscoveryEvent initWithCoder:];
-[W5PeerDiscoveryEvent copyWithZone:];
-[W5PeerDiscoveryEvent initWithPeersFound:peersLost:info:];
-[W5PeerDiscoveryEvent peersFound];
-[W5PeerDiscoveryEvent peersLost];
-[W5PeerDiscoveryEvent setPeersFound:];
-[W5PeerDiscoveryEvent setPeersLost:];
```
