# `CTBundleMatchingInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _mcc;
@"NSString" _mnc;
@"NSString" _imsi;
```

## Properties

```
@property (T@"NSString",&,N,V_mcc) mcc;
@property (T@"NSString",&,N,V_mnc) mnc;
@property (T@"NSString",&,N,V_imsi) imsi;
```

## Class methods

```
+[CTBundleMatchingInfo supportsSecureCoding];
```

## Instance methods

```
-[CTBundleMatchingInfo imsi];
-[CTBundleMatchingInfo mnc];
-[CTBundleMatchingInfo encodeWithCoder:];
-[CTBundleMatchingInfo description];
-[CTBundleMatchingInfo initWithCoder:];
-[CTBundleMatchingInfo setMnc:];
-[CTBundleMatchingInfo mcc];
-[CTBundleMatchingInfo setImsi:];
-[CTBundleMatchingInfo copyWithZone:];
-[CTBundleMatchingInfo setMcc:];
```
