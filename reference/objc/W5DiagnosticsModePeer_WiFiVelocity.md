# `W5DiagnosticsModePeer`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _role;
@"W5Peer" _peer;
@"NSMutableDictionary" _info;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_info) info;
@property (T@"W5Peer",&,N,V_peer) peer;
@property (Tq,N,V_role) role;
```

## Class methods

```
+[W5DiagnosticsModePeer supportsSecureCoding];
```

## Instance methods

```
-[W5DiagnosticsModePeer info];
-[W5DiagnosticsModePeer setInfo:];
-[W5DiagnosticsModePeer encodeWithCoder:];
-[W5DiagnosticsModePeer role];
-[W5DiagnosticsModePeer peer];
-[W5DiagnosticsModePeer setRole:];
-[W5DiagnosticsModePeer description];
-[W5DiagnosticsModePeer initWithCoder:];
-[W5DiagnosticsModePeer copyWithZone:];
-[W5DiagnosticsModePeer setPeer:];
-[W5DiagnosticsModePeer initWithRole:peer:];
-[W5DiagnosticsModePeer initWithRole:peer:info:];
```
