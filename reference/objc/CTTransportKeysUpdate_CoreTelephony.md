# `CTTransportKeysUpdate`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _keys;
@"NSString" _sps_environment;
```

## Properties

```
@property (T@"NSArray",&,N,V_keys) keys;
@property (T@"NSString",&,N,V_sps_environment) sps_environment;
```

## Class methods

```
+[CTTransportKeysUpdate supportsSecureCoding];
```

## Instance methods

```
-[CTTransportKeysUpdate initWith:];
-[CTTransportKeysUpdate setKeys:];
-[CTTransportKeysUpdate keys];
-[CTTransportKeysUpdate encodeWithCoder:];
-[CTTransportKeysUpdate description];
-[CTTransportKeysUpdate initWithCoder:];
-[CTTransportKeysUpdate sps_environment];
-[CTTransportKeysUpdate copyWithZone:];
-[CTTransportKeysUpdate setSps_environment:];
-[CTTransportKeysUpdate initWith:sps:];
```
