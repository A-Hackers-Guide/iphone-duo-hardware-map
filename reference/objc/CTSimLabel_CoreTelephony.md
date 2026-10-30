# `CTSimLabel`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _didSetup;
@"NSString" _unique_id;
@"NSString" _text;
```

## Properties

```
@property (T@"NSString",&,N,V_unique_id) unique_id;
@property (T@"NSString",&,N,V_text) text;
@property (TB,N,V_didSetup) didSetup;
```

## Class methods

```
+[CTSimLabel supportsSecureCoding];
```

## Instance methods

```
-[CTSimLabel didSetup];
-[CTSimLabel text];
-[CTSimLabel initWithId:andText:andDidSetup:];
-[CTSimLabel unique_id];
-[CTSimLabel setDidSetup:];
-[CTSimLabel setUnique_id:];
-[CTSimLabel encodeWithCoder:];
-[CTSimLabel description];
-[CTSimLabel initWithCoder:];
-[CTSimLabel setText:];
-[CTSimLabel copyWithZone:];
-[CTSimLabel isEqual:];
```
