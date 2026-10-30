# `CBTDSScanFilterRule`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBTDSServiceElement`
- Protocols: `NSSecureCoding`, `CUXPCCodable`, `NSCopying`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
I _flags;
@"NSSet" _sourceTIKs;
@"NSSet" _destinationGroupTIKs;
@"NSNumber" _rssi;
```

## Properties

```
@property (TI,N,V_flags) flags;
@property (T@"NSSet",C,N,V_sourceTIKs) sourceTIKs;
@property (T@"NSSet",C,N,V_destinationGroupTIKs) destinationGroupTIKs;
@property (T@"NSNumber",C,N,V_rssi) rssi;
```

## Class methods

```
+[CBTDSScanFilterRule supportsSecureCoding];
```

## Instance methods

```
-[CBTDSScanFilterRule rssi];
-[CBTDSScanFilterRule encodeWithXPCObject:];
-[CBTDSScanFilterRule initWithXPCObject:error:];
-[CBTDSScanFilterRule descriptionWithLevel:];
-[CBTDSScanFilterRule setFlags:];
-[CBTDSScanFilterRule flags];
-[CBTDSScanFilterRule setRssi:];
-[CBTDSScanFilterRule encodeWithCoder:];
-[CBTDSScanFilterRule hash];
-[CBTDSScanFilterRule description];
-[CBTDSScanFilterRule initWithCoder:];
-[CBTDSScanFilterRule copyWithZone:];
-[CBTDSScanFilterRule isEqual:];
-[CBTDSScanFilterRule destinationGroupTIKs];
-[CBTDSScanFilterRule setDestinationGroupTIKs:];
-[CBTDSScanFilterRule setSourceTIKs:];
-[CBTDSScanFilterRule sourceTIKs];
```
