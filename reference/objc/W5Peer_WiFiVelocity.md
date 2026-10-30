# `W5Peer`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 13 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _nearby;
@"NSString" _peerID;
@"NSString" _name;
@"NSString" _model;
@"NSString" _build;
@"NSString" _os;
@"NSString" _version;
@"NSData" _iconImage;
q _proximity;
q _discoveryFlags;
q _controlFlags;
@"RPCompanionLinkDevice" _device;
```

## Properties

```
@property (T@"RPCompanionLinkDevice",&,N,V_device) device;
@property (T@"NSString",C,N,V_peerID) peerID;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_build) build;
@property (T@"NSString",C,N,V_os) os;
@property (T@"NSString",C,N,V_version) version;
@property (T@"NSData",C,N,V_iconImage) iconImage;
@property (Tq,R,D,N) type;
@property (TB,N,V_nearby) nearby;
@property (Tq,N,V_proximity) proximity;
@property (Tq,N,V_discoveryFlags) discoveryFlags;
@property (Tq,N,V_controlFlags) controlFlags;
```

## Class methods

```
+[W5Peer supportsSecureCoding];
```

## Instance methods

```
-[W5Peer setDiscoveryFlags:];
-[W5Peer discoveryFlags];
-[W5Peer model];
-[W5Peer peerID];
-[W5Peer proximity];
-[W5Peer setProximity:];
-[W5Peer build];
-[W5Peer setModel:];
-[W5Peer setControlFlags:];
-[W5Peer setIconImage:];
-[W5Peer setDevice:];
-[W5Peer device];
-[W5Peer dealloc];
-[W5Peer version];
-[W5Peer setBuild:];
-[W5Peer setOs:];
-[W5Peer os];
-[W5Peer controlFlags];
-[W5Peer setPeerID:];
-[W5Peer type];
-[W5Peer nearby];
-[W5Peer iconImage];
-[W5Peer encodeWithCoder:];
-[W5Peer conformsToProtocol:];
-[W5Peer hash];
-[W5Peer setNearby:];
-[W5Peer description];
-[W5Peer setName:];
-[W5Peer initWithCoder:];
-[W5Peer setVersion:];
-[W5Peer copyWithZone:];
-[W5Peer isEqual:];
-[W5Peer name];
-[W5Peer isEqualToPeer:];
-[W5Peer companionLinkDevice];
-[W5Peer _isOSVersionSupported:];
-[W5Peer initWithCompanionLinkDevice:];
```
