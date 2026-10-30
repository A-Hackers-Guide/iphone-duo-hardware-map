# `CTRatSelection`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
C _mask;
@"NSString" _selection;
@"NSString" _preferred;
```

## Properties

```
@property (TC,N,V_mask) mask;
@property (T@"NSString",&,N,V_selection) selection;
@property (T@"NSString",&,N,V_preferred) preferred;
```

## Class methods

```
+[CTRatSelection supportsSecureCoding];
```

## Instance methods

```
-[CTRatSelection selection];
-[CTRatSelection setSelection:];
-[CTRatSelection setPreferred:];
-[CTRatSelection mask];
-[CTRatSelection setMask:];
-[CTRatSelection encodeWithCoder:];
-[CTRatSelection description];
-[CTRatSelection initWithCoder:];
-[CTRatSelection preferred];
-[CTRatSelection copyWithZone:];
-[CTRatSelection isEqual:];
```
