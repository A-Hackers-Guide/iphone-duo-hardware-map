# `CBApplePayloadTypeInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
C _applePayloadType;
c _rssiThreshold;
C _maxAge;
```

## Properties

```
@property (TC,N,V_applePayloadType) applePayloadType;
@property (Tc,N,V_rssiThreshold) rssiThreshold;
@property (TC,N,V_maxAge) maxAge;
```

## Instance methods

```
-[CBApplePayloadTypeInfo encodeWithXPCObject:];
-[CBApplePayloadTypeInfo setRssiThreshold:];
-[CBApplePayloadTypeInfo rssiThreshold];
-[CBApplePayloadTypeInfo initWithXPCObject:error:];
-[CBApplePayloadTypeInfo setMaxAge:];
-[CBApplePayloadTypeInfo hash];
-[CBApplePayloadTypeInfo description];
-[CBApplePayloadTypeInfo isEqual:];
-[CBApplePayloadTypeInfo maxAge];
-[CBApplePayloadTypeInfo applePayloadType];
-[CBApplePayloadTypeInfo setApplePayloadType:];
```
