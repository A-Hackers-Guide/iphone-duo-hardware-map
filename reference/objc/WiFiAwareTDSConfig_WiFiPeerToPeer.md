# `WiFiAwareTDSConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
q _operation;
@"NSString" _serviceName;
q _deviceFilter;
```

## Properties

```
@property (Tq,R,N,V_operation) operation;
@property (T@"NSString",R,N,V_serviceName) serviceName;
@property (Tq,R,N,V_deviceFilter) deviceFilter;
```

## Class methods

```
+[WiFiAwareTDSConfig supportsSecureCoding];
+[WiFiAwareTDSConfig stringForDeviceFilter:];
+[WiFiAwareTDSConfig stringForOperation:];
```

## Instance methods

```
-[WiFiAwareTDSConfig deviceFilter];
-[WiFiAwareTDSConfig operation];
-[WiFiAwareTDSConfig serviceName];
-[WiFiAwareTDSConfig encodeWithCoder:];
-[WiFiAwareTDSConfig description];
-[WiFiAwareTDSConfig initWithCoder:];
-[WiFiAwareTDSConfig copyWithZone:];
-[WiFiAwareTDSConfig initWithOperation:serviceName:deviceFilter:];
```
