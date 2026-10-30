# `WiFiAwareNDIInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
C _security;
I _sessionCount;
I _qosType;
@"NSString" _ndiName;
@"WiFiMACAddress" _ndiAddr;
```

## Properties

```
@property (T@"NSString",R,N,V_ndiName) ndiName;
@property (T@"WiFiMACAddress",R,N,V_ndiAddr) ndiAddr;
@property (TI,R,N,V_sessionCount) sessionCount;
@property (TI,R,N,V_qosType) qosType;
@property (TC,R,N,V_security) security;
```

## Class methods

```
+[WiFiAwareNDIInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareNDIInfo init];
-[WiFiAwareNDIInfo encodeWithCoder:];
-[WiFiAwareNDIInfo security];
-[WiFiAwareNDIInfo initWithCoder:];
-[WiFiAwareNDIInfo copyWithZone:];
-[WiFiAwareNDIInfo sessionCount];
-[WiFiAwareNDIInfo ndiName];
-[WiFiAwareNDIInfo ndiAddr];
-[WiFiAwareNDIInfo qosType];
-[WiFiAwareNDIInfo initWithNdiName:ndiAddr:sessionCount:qosType:security:];
```
