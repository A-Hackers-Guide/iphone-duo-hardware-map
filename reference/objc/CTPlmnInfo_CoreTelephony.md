# `CTPlmnInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _mcc;
@"NSString" _mnc;
```

## Properties

```
@property (T@"NSString",R,N,V_mcc) mcc;
@property (T@"NSString",R,N,V_mnc) mnc;
```

## Class methods

```
+[CTPlmnInfo supportsSecureCoding];
```

## Instance methods

```
-[CTPlmnInfo mnc];
-[CTPlmnInfo encodeWithCoder:];
-[CTPlmnInfo description];
-[CTPlmnInfo initWithCoder:];
-[CTPlmnInfo mcc];
-[CTPlmnInfo copyWithZone:];
-[CTPlmnInfo isEqual:];
-[CTPlmnInfo initWithMcc:mnc:];
-[CTPlmnInfo initWithMccStr:mncStr:];
```
