# `CTQoSLinkCharacteristics`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _bitRateMaxUL;
@"NSNumber" _bitRateMaxDL;
@"NSNumber" _bitRateGuaranteedUL;
@"NSNumber" _bitRateGuaranteedDL;
```

## Properties

```
@property (T@"NSNumber",&,N,V_bitRateMaxUL) bitRateMaxUL;
@property (T@"NSNumber",&,N,V_bitRateMaxDL) bitRateMaxDL;
@property (T@"NSNumber",&,N,V_bitRateGuaranteedUL) bitRateGuaranteedUL;
@property (T@"NSNumber",&,N,V_bitRateGuaranteedDL) bitRateGuaranteedDL;
```

## Class methods

```
+[CTQoSLinkCharacteristics supportsSecureCoding];
```

## Instance methods

```
-[CTQoSLinkCharacteristics init];
-[CTQoSLinkCharacteristics encodeWithCoder:];
-[CTQoSLinkCharacteristics description];
-[CTQoSLinkCharacteristics initWithCoder:];
-[CTQoSLinkCharacteristics copyWithZone:];
-[CTQoSLinkCharacteristics bitRateGuaranteedDL];
-[CTQoSLinkCharacteristics bitRateGuaranteedUL];
-[CTQoSLinkCharacteristics bitRateMaxDL];
-[CTQoSLinkCharacteristics bitRateMaxUL];
-[CTQoSLinkCharacteristics setBitRateGuaranteedDL:];
-[CTQoSLinkCharacteristics setBitRateGuaranteedUL:];
-[CTQoSLinkCharacteristics setBitRateMaxDL:];
-[CTQoSLinkCharacteristics setBitRateMaxUL:];
```
