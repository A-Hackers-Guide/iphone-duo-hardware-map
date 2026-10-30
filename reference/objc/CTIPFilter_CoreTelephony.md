# `CTIPFilter`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 15 properties, 28 instance methods, 1 class methods

## Instance variables

```
Q _filterId;
Q _precedence;
Q _ipProtocol;
Q _ipFamilyProtocol;
@"CTIPFilterEndpoint" _src;
@"CTIPFilterEndpoint" _dst;
@"NSNumber" _tos;
@"NSNumber" _tosMask;
@"NSNumber" _flowLabel;
```

## Properties

```
@property (TQ,N,V_filterId) filterId;
@property (TQ,N,V_precedence) precedence;
@property (TB,R,N) isTcp;
@property (TB,R,N) isUdp;
@property (TB,R,N) isAnyIpProtocol;
@property (TB,R,N) isIpv4;
@property (TB,R,N) isIpv6;
@property (TB,R,N) isAnyIpFamilyProtocol;
@property (TQ,N,V_ipProtocol) ipProtocol;
@property (TQ,N,V_ipFamilyProtocol) ipFamilyProtocol;
@property (T@"CTIPFilterEndpoint",&,N,V_src) src;
@property (T@"CTIPFilterEndpoint",&,N,V_dst) dst;
@property (T@"NSNumber",&,N,V_tos) tos;
@property (T@"NSNumber",&,N,V_tosMask) tosMask;
@property (T@"NSNumber",&,N,V_flowLabel) flowLabel;
```

## Class methods

```
+[CTIPFilter supportsSecureCoding];
```

## Instance methods

```
-[CTIPFilter ipProtocol];
-[CTIPFilter precedence];
-[CTIPFilter encodeWithCoder:];
-[CTIPFilter setPrecedence:];
-[CTIPFilter description];
-[CTIPFilter initWithCoder:];
-[CTIPFilter copyWithZone:];
-[CTIPFilter src];
-[CTIPFilter setDst:];
-[CTIPFilter setSrc:];
-[CTIPFilter setTos:];
-[CTIPFilter tosMask];
-[CTIPFilter dst];
-[CTIPFilter isAnyIpProtocol];
-[CTIPFilter tos];
-[CTIPFilter filterId];
-[CTIPFilter flowLabel];
-[CTIPFilter ipFamilyProtocol];
-[CTIPFilter isAnyIpFamilyProtocol];
-[CTIPFilter isIpv4];
-[CTIPFilter isIpv6];
-[CTIPFilter isTcp];
-[CTIPFilter isUdp];
-[CTIPFilter setFilterId:];
-[CTIPFilter setFlowLabel:];
-[CTIPFilter setIpFamilyProtocol:];
-[CTIPFilter setIpProtocol:];
-[CTIPFilter setTosMask:];
```
