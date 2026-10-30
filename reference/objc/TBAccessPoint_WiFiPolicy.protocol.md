# `TBAccessPoint` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `TBScorable`
- 0 instance variables, 5 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) BSSID;
@property (Td,R,N) latitude;
@property (Td,R,N) longitude;
@property (TB,R,N,GisEdge) edge;
@property (TB,R,N,GisTCPGood) TCPGood;
```

## Instance methods

```
-[TBAccessPoint BSSID];
-[TBAccessPoint latitude];
-[TBAccessPoint longitude];
-[TBAccessPoint dictionaryRepresentation];
-[TBAccessPoint isEdge];
-[TBAccessPoint isTCPGood];
```
