# `W5DiagnosticsMode`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _uuid;
q _state;
@"NSArray" _peers;
@"NSDictionary" _info;
@"NSMutableDictionary" _timestamps;
```

## Properties

```
@property (T@"NSArray",&,N,V_peers) peers;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (T@"NSDictionary",&,N,V_info) info;
@property (T@"NSMutableDictionary",&,N,V_timestamps) timestamps;
@property (Tq,R,N,V_state) state;
```

## Class methods

```
+[W5DiagnosticsMode supportsSecureCoding];
```

## Instance methods

```
-[W5DiagnosticsMode peers];
-[W5DiagnosticsMode setPeers:];
-[W5DiagnosticsMode timestamps];
-[W5DiagnosticsMode setState:];
-[W5DiagnosticsMode info];
-[W5DiagnosticsMode uuid];
-[W5DiagnosticsMode setInfo:];
-[W5DiagnosticsMode setUuid:];
-[W5DiagnosticsMode setTimestamps:];
-[W5DiagnosticsMode initWithConfiguration:];
-[W5DiagnosticsMode initWithConfiguration:uuid:];
-[W5DiagnosticsMode encodeWithCoder:];
-[W5DiagnosticsMode hash];
-[W5DiagnosticsMode description];
-[W5DiagnosticsMode initWithCoder:];
-[W5DiagnosticsMode copyWithZone:];
-[W5DiagnosticsMode isEqual:];
-[W5DiagnosticsMode state];
-[W5DiagnosticsMode compareCollectionTimeLatestFirst:];
-[W5DiagnosticsMode isEqualToDiagnosticsMode:];
-[W5DiagnosticsMode timestampFor:];
-[W5DiagnosticsMode updatePeer:];
```
