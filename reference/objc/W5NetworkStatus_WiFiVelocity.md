# `W5NetworkStatus`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 12 properties, 33 instance methods, 1 class methods

## Instance variables

```
I _isAppleReachable;
@"NSString" _primaryIPv4InterfaceName;
@"NSString" _primaryIPv4ServiceName;
@"NSString" _primaryIPv6InterfaceName;
@"NSString" _primaryIPv6ServiceName;
@"NSString" _primaryIPv4ServiceID;
@"NSString" _primaryIPv6ServiceID;
@"NSArray" _primaryIPv4Addresses;
@"NSArray" _primaryIPv6Addresses;
@"NSString" _primaryIPv4Router;
@"NSString" _primaryIPv6Router;
@"NSArray" _primaryDNSAddresses;
```

## Properties

```
@property (T@"NSString",C,N,V_primaryIPv4InterfaceName) primaryIPv4InterfaceName;
@property (T@"NSString",C,N,V_primaryIPv4ServiceName) primaryIPv4ServiceName;
@property (T@"NSString",C,N,V_primaryIPv6InterfaceName) primaryIPv6InterfaceName;
@property (T@"NSString",C,N,V_primaryIPv6ServiceName) primaryIPv6ServiceName;
@property (T@"NSString",C,N,V_primaryIPv4ServiceID) primaryIPv4ServiceID;
@property (T@"NSString",C,N,V_primaryIPv6ServiceID) primaryIPv6ServiceID;
@property (T@"NSArray",C,N,V_primaryIPv4Addresses) primaryIPv4Addresses;
@property (T@"NSArray",C,N,V_primaryIPv6Addresses) primaryIPv6Addresses;
@property (T@"NSString",C,N,V_primaryIPv4Router) primaryIPv4Router;
@property (T@"NSString",C,N,V_primaryIPv6Router) primaryIPv6Router;
@property (T@"NSArray",C,N,V_primaryDNSAddresses) primaryDNSAddresses;
@property (TI,N,V_isAppleReachable) isAppleReachable;
```

## Class methods

```
+[W5NetworkStatus supportsSecureCoding];
```

## Instance methods

```
-[W5NetworkStatus dealloc];
-[W5NetworkStatus encodeWithCoder:];
-[W5NetworkStatus conformsToProtocol:];
-[W5NetworkStatus hash];
-[W5NetworkStatus description];
-[W5NetworkStatus initWithCoder:];
-[W5NetworkStatus copyWithZone:];
-[W5NetworkStatus isEqual:];
-[W5NetworkStatus primaryIPv4Addresses];
-[W5NetworkStatus primaryIPv6Addresses];
-[W5NetworkStatus isAppleReachable];
-[W5NetworkStatus primaryIPv4InterfaceName];
-[W5NetworkStatus primaryIPv4ServiceName];
-[W5NetworkStatus primaryIPv6InterfaceName];
-[W5NetworkStatus primaryIPv6ServiceName];
-[W5NetworkStatus isEqualToNetworkStatus:];
-[W5NetworkStatus primaryDNSAddresses];
-[W5NetworkStatus primaryIPv4Router];
-[W5NetworkStatus primaryIPv4ServiceID];
-[W5NetworkStatus primaryIPv6Router];
-[W5NetworkStatus primaryIPv6ServiceID];
-[W5NetworkStatus setIsAppleReachable:];
-[W5NetworkStatus setPrimaryDNSAddresses:];
-[W5NetworkStatus setPrimaryIPv4Addresses:];
-[W5NetworkStatus setPrimaryIPv4InterfaceName:];
-[W5NetworkStatus setPrimaryIPv4Router:];
-[W5NetworkStatus setPrimaryIPv4ServiceID:];
-[W5NetworkStatus setPrimaryIPv4ServiceName:];
-[W5NetworkStatus setPrimaryIPv6Addresses:];
-[W5NetworkStatus setPrimaryIPv6InterfaceName:];
-[W5NetworkStatus setPrimaryIPv6Router:];
-[W5NetworkStatus setPrimaryIPv6ServiceID:];
-[W5NetworkStatus setPrimaryIPv6ServiceName:];
```
