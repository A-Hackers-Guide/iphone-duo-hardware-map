# `CTIPFilterEndpoint`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _addr;
@"NSNumber" _maskLen;
@"NSNumber" _port;
@"NSNumber" _portRange;
```

## Properties

```
@property (T@"NSString",&,N,V_addr) addr;
@property (T@"NSNumber",&,N,V_maskLen) maskLen;
@property (T@"NSNumber",&,N,V_port) port;
@property (T@"NSNumber",&,N,V_portRange) portRange;
```

## Class methods

```
+[CTIPFilterEndpoint supportsSecureCoding];
```

## Instance methods

```
-[CTIPFilterEndpoint setPort:];
-[CTIPFilterEndpoint port];
-[CTIPFilterEndpoint encodeWithCoder:];
-[CTIPFilterEndpoint description];
-[CTIPFilterEndpoint initWithCoder:];
-[CTIPFilterEndpoint copyWithZone:];
-[CTIPFilterEndpoint maskLen];
-[CTIPFilterEndpoint addr];
-[CTIPFilterEndpoint portRange];
-[CTIPFilterEndpoint setAddr:];
-[CTIPFilterEndpoint setMaskLen:];
-[CTIPFilterEndpoint setPortRange:];
```
