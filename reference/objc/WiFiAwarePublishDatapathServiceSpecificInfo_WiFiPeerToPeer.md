# `WiFiAwarePublishDatapathServiceSpecificInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
S _servicePort;
q _protocolType;
@"NSString" _hostname;
```

## Properties

```
@property (Tq,R,N,V_protocolType) protocolType;
@property (TS,R,N,V_servicePort) servicePort;
@property (T@"NSString",C,N,V_hostname) hostname;
```

## Class methods

```
+[WiFiAwarePublishDatapathServiceSpecificInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublishDatapathServiceSpecificInfo setHostname:];
-[WiFiAwarePublishDatapathServiceSpecificInfo hostname];
-[WiFiAwarePublishDatapathServiceSpecificInfo encodeWithCoder:];
-[WiFiAwarePublishDatapathServiceSpecificInfo description];
-[WiFiAwarePublishDatapathServiceSpecificInfo initWithCoder:];
-[WiFiAwarePublishDatapathServiceSpecificInfo copyWithZone:];
-[WiFiAwarePublishDatapathServiceSpecificInfo isEqual:];
-[WiFiAwarePublishDatapathServiceSpecificInfo protocolType];
-[WiFiAwarePublishDatapathServiceSpecificInfo initWithProtocolType:servicePort:];
-[WiFiAwarePublishDatapathServiceSpecificInfo servicePort];
-[WiFiAwarePublishDatapathServiceSpecificInfo hostnameEquals:];
```
