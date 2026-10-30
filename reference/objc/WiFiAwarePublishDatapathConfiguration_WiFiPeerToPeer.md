# `WiFiAwarePublishDatapathConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _serviceType;
@"WiFiAwarePublishDatapathSecurityConfiguration" _securityConfiguration;
@"WiFiAwarePublishDatapathServiceSpecificInfo" _serviceSpecificInfo;
q _connectionMode;
```

## Properties

```
@property (Tq,R,N,V_serviceType) serviceType;
@property (T@"WiFiAwarePublishDatapathSecurityConfiguration",&,N,V_securityConfiguration) securityConfiguration;
@property (T@"WiFiAwarePublishDatapathServiceSpecificInfo",C,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (Tq,N,V_connectionMode) connectionMode;
```

## Class methods

```
+[WiFiAwarePublishDatapathConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublishDatapathConfiguration serviceSpecificInfo];
-[WiFiAwarePublishDatapathConfiguration setServiceSpecificInfo:];
-[WiFiAwarePublishDatapathConfiguration serviceSpecificInfoEqual:];
-[WiFiAwarePublishDatapathConfiguration encodeWithCoder:];
-[WiFiAwarePublishDatapathConfiguration description];
-[WiFiAwarePublishDatapathConfiguration setConnectionMode:];
-[WiFiAwarePublishDatapathConfiguration initWithCoder:];
-[WiFiAwarePublishDatapathConfiguration copyWithZone:];
-[WiFiAwarePublishDatapathConfiguration isEqual:];
-[WiFiAwarePublishDatapathConfiguration connectionMode];
-[WiFiAwarePublishDatapathConfiguration serviceType];
-[WiFiAwarePublishDatapathConfiguration initWithServiceType:securityConfiguration:];
-[WiFiAwarePublishDatapathConfiguration initWithServiceType:securityConfiguration:connectionMode:];
-[WiFiAwarePublishDatapathConfiguration securityConfiguration];
-[WiFiAwarePublishDatapathConfiguration securityConfigurationEqual:];
-[WiFiAwarePublishDatapathConfiguration setSecurityConfiguration:];
```
