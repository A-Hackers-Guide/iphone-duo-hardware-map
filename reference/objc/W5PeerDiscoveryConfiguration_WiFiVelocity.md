# `W5PeerDiscoveryConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _discoveryFlags;
q _controlFlags;
```

## Properties

```
@property (Tq,N,V_discoveryFlags) discoveryFlags;
@property (Tq,N,V_controlFlags) controlFlags;
```

## Class methods

```
+[W5PeerDiscoveryConfiguration supportsSecureCoding];
```

## Instance methods

```
-[W5PeerDiscoveryConfiguration setDiscoveryFlags:];
-[W5PeerDiscoveryConfiguration discoveryFlags];
-[W5PeerDiscoveryConfiguration setControlFlags:];
-[W5PeerDiscoveryConfiguration controlFlags];
-[W5PeerDiscoveryConfiguration encodeWithCoder:];
-[W5PeerDiscoveryConfiguration description];
-[W5PeerDiscoveryConfiguration initWithCoder:];
-[W5PeerDiscoveryConfiguration copyWithZone:];
```
