# `CTQoS`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _qci;
@"NSNumber" _bitRateMax;
@"NSNumber" _bitRateMin;
@"NSArray" _filters;
```

## Properties

```
@property (T@"NSNumber",&,N,V_qci) qci;
@property (T@"NSNumber",&,N,V_bitRateMax) bitRateMax;
@property (T@"NSNumber",&,N,V_bitRateMin) bitRateMin;
@property (T@"NSArray",&,N,V_filters) filters;
@property (T@"NSNumber",R,N) gbr;
```

## Class methods

```
+[CTQoS supportsSecureCoding];
```

## Instance methods

```
-[CTQoS setFilters:];
-[CTQoS filters];
-[CTQoS encodeWithCoder:];
-[CTQoS description];
-[CTQoS initWithCoder:];
-[CTQoS copyWithZone:];
-[CTQoS gbr];
-[CTQoS setQci:];
-[CTQoS qci];
-[CTQoS bitRateMax];
-[CTQoS bitRateMin];
-[CTQoS setBitRateMax:];
-[CTQoS setBitRateMin:];
```
