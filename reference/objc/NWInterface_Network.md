# `NWInterface`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`, `NSSecureCoding`, `NSCopying`
- 1 instance variables, 18 properties, 39 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_nw_interface>" _internalInterface;
```

## Properties

```
@property (TB,R,N) supportsMulticast;
@property (TB,R,N) hasDNS;
@property (TB,R,N) hasNAT64;
@property (TB,R,N,GisIPv4Routable) ipv4Routable;
@property (TB,R,N,GisIPv6Routable) ipv6Routable;
@property (T@"NSObject<OS_nw_interface>",R,N) cInterface;
@property (T@"NSObject<OS_nw_interface>",&,V_internalInterface) internalInterface;
@property (TQ,R,N) generation;
@property (Tq,R,N) mtu;
@property (T@"NWInterface",R,N) delegateInterface;
@property (T@"NSString",R,N) typeString;
@property (T@"NSString",R,C,N) privateDescription;
@property (T@"NSString",R,N) interfaceName;
@property (TQ,R,N) interfaceIndex;
@property (Tq,R,N) type;
@property (Tq,R,N) subtype;
@property (TB,R,N,GisExpensive) expensive;
@property (TB,R,N,GisConstrained) constrained;
```

## Class methods

```
+[NWInterface supportsSecureCoding];
+[NWInterface descriptionForSubtype:];
+[NWInterface descriptionForType:];
+[NWInterface interfaceWithProtocolBufferData:];
```

## Instance methods

```
-[NWInterface mtu];
-[NWInterface subtype];
-[NWInterface isIPv4Routable];
-[NWInterface isConstrained];
-[NWInterface isExpensive];
-[NWInterface createProtocolBufferObject];
-[NWInterface initWithInterface:];
-[NWInterface initWithInterfaceIndex:interfaceName:];
-[NWInterface internalInterface];
-[NWInterface interfaceName];
-[NWInterface interfaceIndex];
-[NWInterface setInternalInterface:];
-[NWInterface privateDescription];
-[NWInterface hasNAT64];
-[NWInterface isShallowEqual:];
-[NWInterface descriptionWithIndent:showFullContent:];
-[NWInterface copyLocalAddressForRemoteAddress:];
-[NWInterface copyLocalAddressForDefaultIPv4];
-[NWInterface generation];
-[NWInterface type];
-[NWInterface isUltraConstrained];
-[NWInterface encodeWithCoder:];
-[NWInterface cInterface];
-[NWInterface isIPv6Routable];
-[NWInterface initWithInterfaceName:];
-[NWInterface hash];
-[NWInterface description];
-[NWInterface delegateInterface];
-[NWInterface ipv4Broadcast];
-[NWInterface initWithCoder:];
-[NWInterface typeString];
-[NWInterface copyLocalAddressForDefaultIPv6];
-[NWInterface hasDNS];
-[NWInterface copyWithZone:];
-[NWInterface isEqual:];
-[NWInterface supportsMulticast];
-[NWInterface initWithInterfaceIndex:];
-[NWInterface isDeepEqual:];
-[NWInterface ipv4Netmask];
```
