# `CTNetwork`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _plmn;
@"NSString" _rat;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_plmn) plmn;
@property (T@"NSString",&,N,V_rat) rat;
```

## Class methods

```
+[CTNetwork supportsSecureCoding];
```

## Instance methods

```
-[CTNetwork setPlmn:];
-[CTNetwork rat];
-[CTNetwork encodeWithCoder:];
-[CTNetwork description];
-[CTNetwork setName:];
-[CTNetwork initWithCoder:];
-[CTNetwork copyWithZone:];
-[CTNetwork isEqual:];
-[CTNetwork name];
-[CTNetwork plmn];
-[CTNetwork setRat:];
```
